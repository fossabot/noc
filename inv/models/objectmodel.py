# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# ObjectModel model
# ---------------------------------------------------------------------
# Copyright (C) 2007-2018 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
from __future__ import absolute_import
import os
from threading import Lock
import operator
import six
# Third-party modules
from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import (StringField, UUIDField, DictField,
                                ListField, EmbeddedDocumentField,
                                ObjectIdField)
import cachetools
from pymongo import InsertOne, DeleteOne
# NOC modules
from .connectiontype import ConnectionType
from .connectionrule import ConnectionRule
from .unknownmodel import UnknownModel
from .vendor import Vendor
from noc.main.models.doccategory import category
from noc.lib.nosql import PlainReferenceField
from noc.lib.prettyjson import to_json
from noc.lib.text import quote_safe_path
from noc.core.model.decorator import on_delete_check, on_save

id_lock = Lock()


class ObjectModelConnection(EmbeddedDocument):
    meta = {
        "strict": False,
        "auto_create_index": False
    }
    name = StringField()
    description = StringField()
    type = PlainReferenceField(ConnectionType)
    direction = StringField(
        choices=[
            "i",  # Inner slot
            "o",  # Outer slot
            "s"   # Connection
        ]
    )
    gender = StringField(choices=["s", "m", "f"])
    group = StringField(required=False)
    cross = StringField(required=False)
    protocols = ListField(StringField(), required=False)
    internal_name = StringField(required=False)

    def __unicode__(self):
        return self.name

    def __eq__(self, other):
        return (
            self.name == other.name and
            self.description == other.description and
            self.type.id == other.type.id and
            self.direction == other.direction and
            self.gender == other.gender and
            self.group == other.group and
            self.cross == other.cross and
            self.protocols == other.protocols and
            self.internal_name == other.internal_name
        )

    @property
    def json_data(self):
        r = {
            "name": self.name,
            "description": self.description,
            "type__name": self.type.name,
            "direction": self.direction,
            "gender": self.gender,
        }
        if self.group:
            r["group"] = self.group
        if self.cross:
            r["cross"] = self.cross
        if self.protocols:
            r["protocols"] = self.protocols
        if self.internal_name:
            r["internal_name"] = self.internal_name
        return r


@category
@on_delete_check(check=[
    ("inv.ModelMapping", "model"),
    ("inv.Object", "model")
])
@on_save
class ObjectModel(Document):
    """
    Equipment vendor
    """
    meta = {
        "collection": "noc.objectmodels",
        "strict": False,
        "auto_create_index": False,
        "indexes": [
            ("vendor", "data.asset.part_no"),
            ("vendor", "data.asset.order_part_no")
        ],
        "json_collection": "inv.objectmodels",
        "json_unique_fields": ["name"],
        "json_depends_on": [
            "inv.vendors",
            "inv.connectionrules"
        ]
    }

    name = StringField(unique=True)
    description = StringField()
    vendor = PlainReferenceField(Vendor)
    connection_rule = PlainReferenceField(ConnectionRule, required=False)
    # Connection rule context
    cr_context = StringField(required=False)
    data = DictField()
    connections = ListField(EmbeddedDocumentField(ObjectModelConnection))
    uuid = UUIDField(binary=True)
    plugins = ListField(StringField(), required=False)
    category = ObjectIdField()

    _id_cache = cachetools.TTLCache(maxsize=1000, ttl=60)

    def __unicode__(self):
        return self.name

    @classmethod
    @cachetools.cachedmethod(operator.attrgetter("_id_cache"), lock=lambda _: id_lock)
    def get_by_id(cls, id):
        return ObjectModel.objects.filter(id=id).first()

    def get_data(self, interface, key):
        v = self.data.get(interface, {})
        return v.get(key)

    def on_save(self):
        # Update connection cache
        ModelConnectionsCache.update_for_model(self)
        # Exclude all part numbers from unknown models
        self.clear_unknown_models()

    def has_connection(self, name):
        if self.get_model_connection(name) is None:
            # Check twinax virtual connection
            return (self.get_data("twinax", "twinax") and
                    self.get_data("twinax", "alias") == name)
        else:
            return True

    def get_connection_proposals(self, name):
        """
        Return possible connections for connection name
        as (model id, connection name)
        """
        cn = self.get_model_connection(name)
        if not cn:
            return []  # Connection not found
        r = []
        c_types = cn.type.get_compatible_types(cn.gender)
        og = ConnectionType.OPPOSITE_GENDER[cn.gender]
        for cc in ModelConnectionsCache.objects.filter(
                type__in=c_types, gender=og):
            r += [(cc.model, cc.name)]
        return r

    def get_model_connection(self, name):
        for c in self.connections:
            if (c.name == name or (
                    c.internal_name and c.internal_name == name)):
                return c
        return None

    @classmethod
    def get_model(cls, vendor, part_no):
        """
        Get ObjectModel by part part_no,
        Search order:
            * NOC model name
            * asset.part_no* value (Part numbers)
            * asset.order_part_no* value (FRU numbers)
        """
        if isinstance(part_no, list):
            for p in part_no:
                m = cls._get_model(vendor, p)
                if m:
                    return m
            return None
        else:
            return cls._get_model(vendor, part_no)

    @classmethod
    @cachetools.ttl_cache(maxsize=10000, ttl=60)
    def _get_model(cls, vendor, part_no):
        """
        Get ObjectModel by part part_no,
        Search order:
            * NOC model name
            * asset.part_no* value (Part numbers)
            * asset.order_part_no* value (FRU numbers)
        """
        # Check for model name
        if " | " in part_no:
            m = ObjectModel.objects.filter(name=part_no).first()
            if m:
                return m
        # Check for asset_part_no
        m = ObjectModel.objects.filter(
            vendor=vendor.id,
            data__asset__part_no=part_no
        ).first()
        if m:
            return m
        m = ObjectModel.objects.filter(
            vendor=vendor.id,
            data__asset__order_part_no=part_no
        ).first()
        if m:
            return m
        # Not found
        # Fallback and search by unique part no
        oml = list(ObjectModel.objects.filter(data__asset__part_no=part_no))
        if len(oml) == 1:
            # Unique match found
            return oml[0]
        oml = list(ObjectModel.objects.filter(data__asset__order_part_no=part_no))
        if len(oml) == 1:
            # Unique match found
            return oml[0]
        # Nothing found
        return None

    @property
    def json_data(self):
        r = {
            "name": self.name,
            "$collection": self._meta["json_collection"],
            "uuid": self.uuid,
            "description": self.description,
            "vendor__code": self.vendor.code,
            "data": self.data,
            "connections": [c.json_data for c in self.connections]
        }
        if self.connection_rule:
            r["connection_rule__name"] = self.connection_rule.name
        if self.cr_context:
            r["cr_context"] = self.cr_context
        if self.plugins:
            r["plugins"] = self.plugins
        return r

    def to_json(self):
        return to_json(self.json_data,
                       order=["name", "$collection",
                              "uuid", "vendor__code",
                              "description",
                              "connection_rule__name",
                              "cr_context",
                              "plugins"])

    def get_json_path(self):
        p = [quote_safe_path(n.strip()) for n in self.name.split("|")]
        return os.path.join(*p) + ".json"

    def clear_unknown_models(self):
        """
        Exclude model's part numbers from unknown models
        """
        if "asset" in self.data:
            part_no = (self.data["asset"].get("part_no", []) +
                       self.data["asset"].get("order_part_no", []))
            if part_no:
                vendor = self.vendor
                if isinstance(vendor, six.string_types):
                    vendor = Vendor.get_by_id(vendor)
                UnknownModel.clear_unknown(vendor.code, part_no)


class ModelConnectionsCache(Document):
    meta = {
        "collection": "noc.inv.objectconnectionscache",
        "strict": False,
        "auto_create_index": False,
        "indexes": ["model", ("type", "gender")]
    }
    # Connection type
    type = ObjectIdField()
    gender = StringField(choices=["s", "m", "f"])
    model = ObjectIdField()
    name = StringField()

    @classmethod
    def rebuild(cls):
        """
        Rebuild cache
        """
        nc = []
        for m in ObjectModel.objects.all():
            for c in m.connections:
                nc += [{
                    "type": c.type.id,
                    "gender": c.gender,
                    "model": m.id,
                    "name": c.name
                }]
        collection = ModelConnectionsCache._get_collection()
        collection.drop()
        if nc:
            collection.insert(nc)

    @classmethod
    def update_for_model(cls, model):
        """
        Update connection cache for object model
        :param model: ObjectModel instance
        :return:
        """
        cache = {}
        collection = ModelConnectionsCache._get_collection()
        for cc in ModelConnectionsCache.objects.filter(model=model.id):
            cache[(cc.type, cc.gender, cc.model, cc.name)] = cc.id
        bulk = []
        for c in model.connections:
            k = (c.type.id, c.gender, model.id, c.name)
            if k in cache:
                del cache[k]
                continue
            bulk += [InsertOne({
                "type": c.type.id,
                "gender": c.gender,
                "model": model.id,
                "name": c.name
            })]
        if cache:
            bulk += [DeleteOne({"_id": x}) for x in cache.values()]
        if bulk:
            collection.bulk_write(bulk)
