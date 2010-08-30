# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## HP.ProCurve.get_lldp_neighbors
##----------------------------------------------------------------------
## Copyright (C) 2007-2009 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
"""
"""
import noc.sa.script
from noc.sa.interfaces import IGetLLDPNeighbors
import re

rx_split=re.compile(r"^\s*----.+?\n",re.MULTILINE|re.DOTALL)
rx_line=re.compile(r"^\s*(?P<port>\S+)\s*|",re.MULTILINE|re.DOTALL)
rx_chassis_id=re.compile(r"^\s*ChassisId\s*:\s*(.{17})",re.MULTILINE|re.DOTALL|re.IGNORECASE)
rx_port_id=re.compile(r"^\s*PortId\s*:\s*(.+?)\s*$",re.MULTILINE|re.DOTALL|re.IGNORECASE)
rx_sys_name=re.compile(r"^\s*SysName\s*:\s*(.+?)\s*$",re.MULTILINE|re.DOTALL|re.IGNORECASE)
rx_cap=re.compile(r"^\s*System Capabilities Enabled\s*:\s*(.*?)\s*$",re.MULTILINE|re.DOTALL|re.IGNORECASE)

class Script(noc.sa.script.Script):
    name="HP.ProCurve.get_lldp_neighbors"
    implements=[IGetLLDPNeighbors]
    def execute(self):
        r=[]
        v=self.cli("show lldp info remote-device")
        for l in rx_split.split(v)[1].splitlines():
            l=l.strip()
            if not l:
                continue
            match=rx_line.search(l)
            if not match:
                continue
            local_interface=match.group("port")
            i={"local_interface":local_interface,"neighbors":[]}
            v=self.cli("show lldp info remote-device %s"%local_interface)
            # Get chassis id
            match=rx_chassis_id.search(v)
            if not match:
                continue
            remote_chassis_id=match.group(1).replace(" ","")
            remote_chassis_id="%s-%s"%(remote_chassis_id[:6],remote_chassis_id[6:]) # Convert to HP-style mac
            n={"remote_chassis_id":remote_chassis_id,"remote_port_subtype":5,"remote_chassis_id_subtype":4}
            # Get remote port
            match=rx_port_id.search(v)
            if not match:
                continue
            n["remote_port"]=match.group(1)
            # Get remote system name
            match=rx_sys_name.search(v)
            if match:
                n["remote_system_name"]=match.group(1)
            # Get capabilities
            caps=0
            match=rx_cap.search(v)
            if match:
                for c in match.group(1).split(", "):
                    caps|={
                        "other"     : 1,
                        "repeater"  : 2,
                        "bridge"    : 4,
                        "wlanaccesspoint" : 8,
                        "router"    : 16,
                        "telephone" : 32,
                        "docsis"    : 64,
                        "station"   : 128
                    }[c.lower()]
            n["remote_capabilities"]=caps
            i["neighbors"]+=[n]
            r+=[i]
        return r
