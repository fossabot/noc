# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## vc.vc application
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
from collections import defaultdict
## NOC modules
from noc.lib.app import ExtModelApplication, view
from noc.vc.models import VC, VCDomain, VCFilter
from noc.inv.models import SubInterface, Q
from noc.lib.ip import IP
from noc.sa.interfaces import DictParameter, ModelParameter, ListOfParameter,\
    IntParameter, StringParameter


class VCApplication(ExtModelApplication):
    """
    VC application
    """
    title = "VC"
    menu = "Virtual Circuits"
    model = VC
    icon = "icon_link"

    query_fields = ["name", "description"]
    query_condition = "icontains"
    int_query_fields = ["l1", "l2"]

    mrt_config = {
        "get_vlans": {
            "map_script": "get_vlans",
            "timeout": 120
        }
    }

    def lookup_vcfilter(self, q, name, value):
        """
        Resolve __vcflter lookups
        :param q:
        :param name:
        :param value:
        :return:
        """
        value = ModelParameter(VCFilter).clean(value)
        x = value.to_sql(name)
        try:
            q[None] += [x]
        except KeyError:
            q[None] = [x]

    def field_interfaces_count(self, obj):
        if not obj.vc_domain.selector:
            return "-"
        objects = set(obj.vc_domain.selector.managed_objects.values_list("id",
                                                                    flat=True))
        l1 = obj.l1
        n = SubInterface.objects.filter(
            Q(managed_object__in=objects) &
            (
                Q(untagged_vlan=l1, is_bridge=True) |
                Q(tagged_vlans=l1, is_bridge=True) |
                Q(vlan_ids=l1)
            )
        ).count()
        return str(n)

    def field_prefixes(self, obj):
        if not obj.vc_domain.selector:
            return "-"
        objects = set(obj.vc_domain.selector.managed_objects.values_list("id",
                                                                    flat=True))
        ipv4 = set()
        ipv6 = set()
        # @todo: Exact match on vlan_ids
        for si in SubInterface.objects.filter(
            Q(managed_object__in=objects) &
            Q(vlan_ids=obj.l1) &
            (Q(is_ipv4=True) | Q(is_ipv6=True))
        ):
            if si.is_ipv4:
                ipv4.update([IP.prefix(ip).first
                          for ip in si.ipv4_addresses])
            if si.is_ipv6:
                ipv6.update([IP.prefix(ip).first
                          for ip in si.ipv6_addresses])
        p = [str(x.first) for x in sorted(ipv4)]
        p += [str(x.first) for x in sorted(ipv6)]
        return p

    @view(url="^find_free/$", method=["GET"], access="read", api=True,
          validate={
              "vc_domain": ModelParameter(VCDomain),
              "vc_filter": ModelParameter(VCFilter)
          })
    def api_find_free(self, request, vc_domain, vc_filter, **kwargs):
        return vc_domain.get_free_label(vc_filter)

    @view(url="^bulk/import/", method=["POST"], access="import", api=True,
          validate={
              "vc_domain": ModelParameter(VCDomain),
              "items": ListOfParameter(element=DictParameter(attrs={
                  "l1": IntParameter(),
                  "l2": IntParameter(),
                  "name": StringParameter(),
                  "description": StringParameter(default="")
              }))
          })
    def api_bulk_import(self, request, vc_domain, items):
        n = 0
        for i in items:
            if not VC.objects.filter(vc_domain=vc_domain,
                                     l1=i["l1"], l2=i["l2"]).exists():
                # Add only not-existing
                VC(vc_domain=vc_domain, l1=i["l1"], l2=i["l2"],
                   name=i["name"], description=i["description"]).save()
                n += 1
        return {
            "status": True,
            "imported": n
        }

    @view(url=r"^(?P<vc_id>\d+)/interfaces/$", method=["GET"],
          access="read", api=True)
    def api_interfaces(self, request, vc_id):
        """
        Returns a dict of {untagged: ..., tagged: ...., l3: ...}
        :param request:
        :param vc_id:
        :return:
        """
        vc = self.get_object_or_404(VC, id=int(vc_id))
        l1 = vc.l1
                # Check VC domain has selector
        if not vc.vc_domain.selector:
            return self.render(request, "interfaces.html",
                               no_selector=True, vc=vc)
        # Managed objects in selector
        objects = set(vc.vc_domain.selector.managed_objects.values_list("id",
                                                                    flat=True))
        # Find untagged interfaces
        si_objects = defaultdict(list)
        for si in SubInterface.objects.filter(
            managed_object__in=objects,
            untagged_vlan=l1,
            is_bridge=True):
            si_objects[si.managed_object] += [{"name": si.name}]
        untagged = [{
            "managed_object_id": o.id,
            "managed_object_name": o.name,
            "interfaces": sorted(si_objects[o], key=lambda x: x["name"])
        } for o in si_objects]
        # Find tagged interfaces
        si_objects = defaultdict(list)
        for si in SubInterface.objects.filter(
            managed_object__in=objects,
            tagged_vlans=l1,
            is_bridge=True):
            si_objects[si.managed_object] += [{"name": si.name}]
        tagged = [{
            "managed_object_id": o.id,
            "managed_object_name": o.name,
            "interfaces": sorted(si_objects[o], key=lambda x: x["name"])
        } for o in si_objects]
        # Find l3 interfaces
        si_objects = defaultdict(list)
        for si in SubInterface.objects.filter(
            managed_object__in=objects,
            vlan_ids=l1):
            si_objects[si.managed_object] += [{
                "name": si.name,
                "ipv4_addresses": si.ipv4_addresses,
                "ipv6_addresses": si.ipv6_addresses
            }]
        l3 = [{"managed_object_id": o.id,
               "managed_object_name": o.name,
               "interfaces": sorted(si_objects[o], key=lambda x: x["name"])
        } for o in si_objects]
        return {
            "untagged": sorted(untagged,
                               key=lambda x: x["managed_object_name"]),
            "tagged": sorted(tagged, key=lambda x: x["managed_object_name"]),
            "l3": sorted(l3, key=lambda x: x["managed_object_name"])
        }
