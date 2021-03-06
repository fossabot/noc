# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Generic.get_topology_data
# ---------------------------------------------------------------------
# Copyright (C) 2007-2012 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# NOC modules
from noc.core.script.base import BaseScript
from noc.sa.interfaces.igetipdiscovery import IGetIPDiscovery


class Script(BaseScript):
    """
    Retrieve data for IP discovery
    """
    name = "Generic.get_ip_discovery"
    interface = IGetIPDiscovery
    requires = ["get_arp"]

    def execute(self):
        # Prepare VRFs
        vrfs = {
            "default": {
                "name": "default",
                "addresses": []
            }
        }
        if "get_mpls_vpn" in self.scripts:
            try:
                r = self.scripts.get_mpls_vpn()
            except self.CLISyntaxError:
                r = []
            for v in r:
                if v["status"] and v["type"] == "VRF":
                    vrf = {
                        "name": v["name"],
                        "addresses": []
                    }
                    if "rd" in v:
                        vrf["rd"] = v["rd"]
                    if "vpn_id" in v:
                        vrf["vpn_id"] = v["vpn_id"]
                    vrfs[v["name"]] = vrf
        # Get IPv6 neighbors (global?)
        if "get_ipv6_neighbor" in self.scripts:
            try:
                r = self.scripts.get_ipv6_neighbor()
            except self.CLISyntaxError:
                r = []
            if r:
                vrfs["default"]["addresses"] += [
                    {
                        "ip": x["ip"],
                        "afi": "6",
                        "mac": x["mac"],
                        "interface": x["interface"]
                    }
                    for x in r if x["state"] == "reachable"
                ]
        # Iterate through VRF
        data = []
        for v in vrfs:
            a = []
            vrf = None if v == "default" else v
            # Process ARP cache
            arp_cache = self.scripts.get_arp(vrf=vrf)
            a += [{
                "ip": x["ip"],
                "afi": "4",
                "mac": x["mac"],
                "interface": x["interface"]
            } for x in arp_cache if "mac" in x and x["mac"]]
            # Process NBD
            vd = vrfs[v].copy()
            vd["addresses"] += a
            data += [vd]
        # Return collected data
        return data
