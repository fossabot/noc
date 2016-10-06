# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## AlarmDiagnosticConfig model
##----------------------------------------------------------------------
## Copyright (C) 2007-2016 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
import operator
from threading import Lock
from collections import defaultdict
import logging
## Third-party modules
from mongoengine.document import Document
from mongoengine.fields import StringField, BooleanField, ReferenceField, IntField
import cachetools
## NOC modules
from noc.fm.models.alarmclass import AlarmClass
from noc.fm.models.alarmdiagnostic import AlarmDiagnostic
from noc.sa.models.action import Action
from noc.sa.models.managedobjectselector import ManagedObjectSelector
from noc.lib.nosql import ForeignKeyField
from noc.sa.models.selectorcache import SelectorCache
from noc.core.defer import call_later
from noc.core.handler import get_handler
from noc.lib.debug import error_report


ac_lock = Lock()
logger = logging.getLogger(__name__)


class AlarmDiagnosticConfig(Document):
    meta = {
        "collection": "noc.alarmdiagnosticconfig",
        "indexes": [
            "alarm_class"
        ]
    }

    name = StringField(unique=True)
    is_active = BooleanField(default=True)
    description = StringField()
    alarm_class = ReferenceField(AlarmClass)
    selector = ForeignKeyField(ManagedObjectSelector)
    # Process only on root cause
    only_root = BooleanField(default=True)
    # On alarm raise actions
    enable_on_raise = BooleanField(default=True)
    on_raise_delay = IntField(default=0)
    on_raise_script = StringField()
    on_raise_action = ReferenceField(Action)
    on_raise_handler = StringField()
    # Periodic actions
    enable_periodic = BooleanField(default=True)
    periodic_interval = IntField(default=0)
    periodic_script = StringField()
    periodic_action = ReferenceField(Action)
    periodic_handler = StringField()
    # Clear actions
    enable_on_clear = BooleanField(default=True)
    on_clear_delay = IntField(default=0)
    on_clear_script = StringField()
    on_clear_action = ReferenceField(Action)
    on_clear_handler = StringField()

    _ac_cache = cachetools.TTLCache(1000, ttl=60)

    def __unicode__(self):
        return self.name

    @classmethod
    @cachetools.cachedmethod(operator.attrgetter("_ac_cache"),
                             lock=lambda _: ac_lock)
    def get_class_diagnostics(cls, alarm_class):
        return list(AlarmDiagnosticConfig.objects.filter(
            alarm_class=alarm_class.id,
            is_active=True
        ))

    @classmethod
    def on_raise(cls, alarm):
        """
        Submit raise and periodic jobs
        :param alarm:
        :return:
        """
        r_cfg = defaultdict(list)
        p_cfg = defaultdict(list)
        for c in cls.get_class_diagnostics(alarm.alarm_class):
            if c.selector and not SelectorCache.is_in_selector(
                    alarm.managed_object, c.selector
            ):
                continue
            if c.only_root and alarm.root:
                continue
            if c.enable_on_raise:
                if c.on_raise_script:
                    r_cfg[c.on_raise_delay] += [{"script": c.on_raise_script}]
                if c.on_raise_action:
                    r_cfg[c.on_raise_delay] += [{"action": c.on_raise_action.id}]
                if c.on_raise_handler:
                    r_cfg[c.on_raise_delay] += [{"handler": c.on_raise_handler}]
            if c.enable_on_periodic:
                if c.periodic_interval:
                    p_cfg[c.periodic_interval] += [{"script": c.periodic_interval}]
                if c.periodic_interval:
                    p_cfg[c.periodic_interval] += [{"action": c.periodic_interval.id}]
                if c.periodic_interval:
                    p_cfg[c.periodic_interval] += [{"handler": c.periodic_interval}]
        # Submit on_raise job
        for delay in r_cfg:
            call_later(
                "noc.fm.models.alarmdiagnosticconfig.on_raise",
                scheduler="correlator",
                delay=delay,
                alarm=alarm.id,
                cfg=r_cfg[delay]
            )
        # @todo: Submit periodic job

    @classmethod
    def on_clear(cls, alarm):
        """
        Submit clear jobs
        :param alarm:
        :return:
        """
        cfg = defaultdict(list)
        for c in cls.get_class_diagnostics(alarm.alarm_class):
            if c.selector and not SelectorCache.is_in_selector(
                    alarm.managed_object, c.selector
            ):
                continue
            if c.only_root and alarm.root:
                continue
            if c.enable_on_clear:
                if c.on_clear_script:
                    cfg[c.on_clear_delay] += [{"script": c.on_clear_script}]
                if c.on_clear_action:
                    cfg[c.on_clear_delay] += [{"action": c.on_clear_action.id}]
                if c.on_clear_handler:
                    cfg[c.on_clear_delay] += [{"handler": c.on_clear_handler}]
        # Submit on_raise job
        for delay in cfg:
            call_later(
                "noc.fm.models.alarmdiagnosticconfig.on_clear",
                scheduler="correlator",
                delay=delay,
                alarm=alarm.id,
                cfg=cfg[delay]
            )
        AlarmDiagnostic.clear_diagnostics(alarm)

    @staticmethod
    def get_diag(alarm, cfg, state):
        mo = alarm.managed_object
        result = []
        for c in cfg:
            if "script" in c:
                try:
                    g = getattr(mo.scripts, c["script"])
                    result += [g()]
                except Exception as e:
                    error_report()
                    result += [str(e)]
            if "action" in c:
                try:
                    g = getattr(mo.actions, c["action"])
                    result += [g()]
                except Exception as e:
                    error_report()
                    result += [str(e)]
            if "handler" in c:
                try:
                    h = get_handler(c["handler"])
                    try:
                        result += [h()]
                    except Exception as e:
                        error_report()
                        result += [str(e)]
                except ImportError:
                    result += ["Invalid handler: %s" % c["handler"]]
        if result:
            AlarmDiagnostic.save_diagnostics(alarm, result, state)


def on_raise(alarm, cfg, *args, **kwargs):
    a = get_alarm(alarm)
    if not a:
        logger.info("[%s] Alarm is not found, skipping", alarm)
    if a.status == "C":
        logger.info("[%s] Alarm is closed, skipping", alarm)
        return
    AlarmDiagnosticConfig.get_diag(a, cfg, "R")


def on_clear(alarm, cfg, *args, **kwargs):
    a = get_alarm(alarm)
    if not a:
        logger.info("[%s] Alarm is not found, skipping", alarm)
    AlarmDiagnosticConfig.get_diag(a, cfg, "C")

##
from noc.fm.models.utils import get_alarm