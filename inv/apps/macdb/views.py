# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## inv.macdb application
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.app import ExtDocApplication, view
from noc.inv.models import MACDB, MACLog, Q


class MACApplication(ExtDocApplication):
    """
    MAC application
    """
    title = "MacDB"
    menu = "Mac DB"
    model = MACDB

    query_fields = ["mac", "interface", "managed_object"]
    query_condition = "icontains"
    int_query_fields = ["vlan"]

    implied_permissions = {
        "read": ["inv:macdb:lookup", "main:style:lookup"]
    }

    @view(url="^(?P<mac>[0-9A-F:]+)/$", method=["GET"],
        access="view", api=True)
    def api_get_maclog(self, request, mac):
        """
        GET maclog
        :param mac:
        :return:
        """
        current = []
        
        m = MACDB.objects.filter(mac=mac).order_by("-timestamp")
        for p in m:
            if p:
                vc_d = str(p.vc_domain.name) if p.vc_domain else None
                current = [{
                    "timestamp": str(p.last_changed),
                    "mac": p.mac,
                    "vc_domain": vc_d,
                    "vlan": p.vlan,
                    "managed_object_name": str(p.managed_object.name),
                    "interface_name": str(p.interface.name)
                }]
        history = [
            {
                "timestamp": str(i.timestamp),
                "mac": i.mac,
                "vc_domain": str(i.vc_domain_name),
                "vlan": i.vlan,
                "managed_object_name": str(i.managed_object_name),
                "interface_name": str(i.interface_name)
            } for i in
              MACLog.objects.filter(mac=mac).order_by("-timestamp")
        ]
        return current + history
