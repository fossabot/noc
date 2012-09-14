# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## H3C.VRP.get_version test
## Auto-generated by ./noc debug-script at 14.09.2012 10:37:02
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class H3C_VRP_get_version_Test(ScriptTestCase):
    script = "H3C.VRP.get_version"
    vendor = "H3C"
    platform = "5500G-EI"
    version = "3.03.02s56p05"
    input = {}
    result = {'attributes': {'Boot PROM': '5.03', 'HW version': 'REV.C'},
 'platform': '5500G-EI',
 'vendor': 'H3C',
 'version': '3.03.02s56p05'}
    motd = '\n'
    cli = {
## 'display version'
'display version': """
%Mar 11 09:37:53:326 2011 5500G-EI-Mainframe SHELL/5/LOGIN:- 2 - admin(172.20.0.181) in unit2 logindisplay version
3Com Corporation
Switch 5500G-EI Software Version 3Com OS V3.03.02s56p05
Copyright (c) 2004-2009 3Com Corporation and its licensors, All rights reserved.
Switch 5500G-EI uptime is 35 weeks, 1 day, 2 hours, 51 minutes

Switch 5500G-EI 24-Port with 1 Processor
128M    bytes SDRAM
16384K  bytes Flash Memory
Config Register points to FLASH

Hardware Version is REV.C
CPLD Version is 002
Bootrom Version is 5.03
[Subslot 0] 24GE+4SFP  Hardware Version is 00.00.00 
[Subslot 2] 2 STACK Hardware Version is REV.C """, 
}
    snmp_get = {}
    snmp_getnext = {}
    http_get = {}
