# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Alentis.NetPing.get_chassis_id test
## Auto-generated by ./noc debug-script at 27.12.2012 09:41:24
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class Alentis_NetPing_get_chassis_id_Test(ScriptTestCase):
    script = "Alentis.NetPing.get_chassis_id"
    vendor = "Alentis"
    platform = "UniPing-RS232"
    version = "50.8.7.A-2"
    input = {}
    result = {'first_chassis_mac': '00:A2:E0:CF:00:00',
 'last_chassis_mac': '00:A2:E0:CF:00:00'}
    motd = ''
    cli = {
}
    snmp_get = {'1.3.6.1.2.1.2.2.1.6.1': '\x00\xa2\xe0\xcf\x00\x00'}
    snmp_getnext = {}
    http_get = {}
