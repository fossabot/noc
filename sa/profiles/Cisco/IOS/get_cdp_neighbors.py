# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Cisco.IOS.get_cdp_neighbors
##----------------------------------------------------------------------
## Copyright (C) 2007-2010 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
"""
"""
import noc.sa.script
from noc.sa.interfaces import IGetCDPNeighbors
import re

class Script(noc.sa.script.Script):
    name="Cisco.IOS.get_cdp_neighbors"
    implements=[IGetCDPNeighbors]
    
    rx_hostname=re.compile(r"^hostname\s+(?P<hostname>\S+)",re.MULTILINE)
    rx_domain_name=re.compile(r"^ip domain-name\s+(?P<domain>\S+)",re.MULTILINE)
    
    rx_entry=re.compile(r"Device ID: (?P<device_id>\S+).+?"
        r"Interface: (?P<local_interface>\S+),\s+Port ID \(outgoing port\): (?P<remote_interface>\S+)",re.MULTILINE|re.DOTALL|re.IGNORECASE)
    def execute(self):
        # Get device id
        # @todo: Find more clean way
        v=self.cli("show running-config | include ^(hostname|ip domain-name)")
        device_id=[]
        match=self.rx_hostname.search(v)
        if match:
            device_id+=[match.group("hostname")]
        match=self.rx_domain_name.search(v)
        if match:
            device_id+=[match.group("domain")]
        device_id=".".join(device_id)
        # Get neighbors
        neighbors=[]
        for match in self.rx_entry.finditer(self.cli("show cdp neighbors detail")):
            neighbors+=[{
                "device_id"        : match.group("device_id"),
                "local_interface"  : match.group("local_interface"),
                "remote_interface" : match.group("remote_interface")
            }]
        return {
            "device_id" : device_id,
            "neighbors" : neighbors
        }
    