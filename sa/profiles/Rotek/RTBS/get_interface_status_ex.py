# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Raisecom.RCIOS.get_interface_status_ex
# ---------------------------------------------------------------------
# Copyright (C) 2007-2017 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# NOC modules
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igetinterfacestatusex import IGetInterfaceStatusEx
from noc.sa.interfaces.base import InterfaceTypeError
from noc.core.mib import mib


class Script(BaseScript):
    name = "Rotek.RTBS.get_interface_status_ex"
    interface = IGetInterfaceStatusEx
    requires = []

    def get_iftable(self, oid):
        if "::" in oid:
            oid = mib[oid]
        r = {}
        for oid, v in self.snmp.getnext(oid, max_repetitions=40):
            ifindex = int(oid.split(".")[-1])
            r[ifindex] = v
        return r

    def apply_table(self, r, mib, name, f=None):
        if not f:
            f = lambda x: x
        d = self.get_iftable(mib)
        for ifindex in d:
            if ifindex in r:
                r[ifindex][name] = f(d[ifindex])

    def get_data(self):
        # ifIndex -> ifName mapping
        r = {}  # ifindex -> data
        unknown_interfaces = []
        for oid, name in self.snmp.getnext(mib["IF-MIB::ifDescr"]):
            try:
                v = self.profile.convert_interface_name(name)
            except InterfaceTypeError, why:
                self.logger.debug(
                    "Ignoring unknown interface %s: %s",
                    name, why
                )
                unknown_interfaces += [name]
                continue
            ifindex =  int(oid.split(".")[-1])
            r[ifindex] = {
                "interface": v
            }
        # Apply ifAdminStatus
        self.apply_table(r, "IF-MIB::ifAdminStatus", "admin_status", lambda x: x == 1)
        # Apply ifOperStatus
        self.apply_table(r, "IF-MIB::ifOperStatus", "oper_status", lambda x: x == 1)
        # Apply ifSpeed
        s_table = self.get_iftable("IF-MIB::ifSpeed")
        highspeed = set()
        for ifindex in r:
            s = s_table.get(ifindex)
            if s is not None:
                s = int(s)
                if s == 4294967295:
                    highspeed.add(ifindex)
                elif s:
                    r[ifindex]["in_speed"] = s // 1000
                    r[ifindex]["out_speed"] = s // 1000

        # Refer to ifHighSpeed if necessary
        if highspeed:
            hs_table = self.get_iftable("IF-MIB::ifHighSpeed")
            for ifindex in highspeed:
                s = hs_table.get(ifindex)
                if s is not None:
                    s = int(s)
                    if s:
                        r[ifindex]["in_speed"] = s * 1000
                        r[ifindex]["out_speed"] = s * 1000
        if unknown_interfaces:
            self.logger.info("%d unknown interfaces has been ignored",
                             len(unknown_interfaces))
        return r.values()
    def get_data2(self):
        # ifIndex -> ifName mapping
        ss = {}
        r = {}  # ifindex -> data
        unknown_interfaces = []
        for soid, sname in self.snmp.getnext("1.3.6.1.4.1.32761.3.5.1.2.1.1.4"):
            sifindex = int(soid.split(".")[-1])
            ss[sifindex] = sname
        for soid, sname in self.snmp.getnext("1.3.6.1.4.1.41752.3.5.1.2.1.1.4"):
            sifindex = int(soid.split(".")[-1])
            ss[sifindex] = sname
        for oid, name in self.snmp.getnext(mib["IF-MIB::ifDescr"]):
            try:
                v = self.profile.convert_interface_name(name)
            except InterfaceTypeError, why:
                self.logger.debug(
                    "Ignoring unknown interface %s: %s",
                    name, why
                )
                unknown_interfaces += [name]
                continue
            ifindex =  int(oid.split(".")[-1])
            for i in ss.items():
                if int(i[0]) == ifindex:
                    v= "%s.%s" % (v, i[1])
                    r[ifindex] = {
                        "interface": v
                    }
        # Apply ifAdminStatus
        self.apply_table(r, "IF-MIB::ifAdminStatus", "admin_status", lambda x: x == 1)
        # Apply ifOperStatus
        self.apply_table(r, "IF-MIB::ifOperStatus", "oper_status", lambda x: x == 1)
        # Apply ifSpeed
        s_table = self.get_iftable("IF-MIB::ifSpeed")
        highspeed = set()
        for ifindex in r:
            s = s_table.get(ifindex)
            if s is not None:
                s = int(s)
                if s == 4294967295:
                    highspeed.add(ifindex)
                elif s:
                    r[ifindex]["in_speed"] = s // 1000
                    r[ifindex]["out_speed"] = s // 1000

        # Refer to ifHighSpeed if necessary
        if highspeed:
            hs_table = self.get_iftable("IF-MIB::ifHighSpeed")
            for ifindex in highspeed:
                s = hs_table.get(ifindex)
                if s is not None:
                    s = int(s)
                    if s:
                        r[ifindex]["in_speed"] = s * 1000
                        r[ifindex]["out_speed"] = s * 1000
        if unknown_interfaces:
            self.logger.info("%d unknown interfaces has been ignored",
                             len(unknown_interfaces))
        return r.values()

    def execute(self):
        r = []
        if self.has_snmp():
            try:
                r = self.get_data()
                r2 = self.get_data2()
                r += r2
            except self.snmp.TimeOutError:
                pass
        return r