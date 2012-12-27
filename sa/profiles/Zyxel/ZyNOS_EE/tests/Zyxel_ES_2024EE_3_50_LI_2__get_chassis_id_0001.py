# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Zyxel.ZyNOS_EE.get_chassis_id test
## Auto-generated by ./noc debug-script at 27.12.2012 09:41:47
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class Zyxel_ZyNOS_EE_get_chassis_id_Test(ScriptTestCase):
    script = "Zyxel.ZyNOS_EE.get_chassis_id"
    vendor = "Zyxel"
    platform = "ES-2024EE"
    version = "3.50(LI.2)"
    input = {}
    result = {'first_chassis_mac': '00:A0:C5:FB:53:CA',
 'last_chassis_mac': '00:A0:C5:FB:53:CA'}
    motd = ' ****\nCopyright (c) 1994 - 2004 ZyXEL Communications Corp.\n'
    cli = {
## 'sys mrd atsh'
'sys mrd atsh': """ sys mrd atsh
 ZyNOS version : V3.50(LI.2) | 06/17/2004
 bootbase version : V1.00 | 11/20/2003
 Vendor Name : ZyXEL
 Product Model : ES-2024

 MAC Address : 00:a0:c5:fb:53:ca 
 Default Country Code : ff
 Boot Module Debug Flag : 0
 RomFile Version : 2
 RomFile Checksum : 5f63
 ZyNOS Checksum : d234
 SNMP MIB level & OID : 61234567891011121314151617181920
 Main Feature Bits : c0
 Other Feature Bits :
\taf 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
\t00 00 00 00 00 00 00 00 00 01 33 00 00 00 """, 
}
    snmp_get = {}
    snmp_getnext = {}
    http_get = {}
