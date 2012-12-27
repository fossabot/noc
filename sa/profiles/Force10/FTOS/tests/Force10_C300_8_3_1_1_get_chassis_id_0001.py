# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Force10.FTOS.get_chassis_id test
## Auto-generated by ./noc debug-script at 27.12.2012 09:41:43
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class Force10_FTOS_get_chassis_id_Test(ScriptTestCase):
    script = "Force10.FTOS.get_chassis_id"
    vendor = "Force10"
    platform = "C300"
    version = "8.3.1.1"
    input = {}
    result = {'first_chassis_mac': '00:01:E8:79:2F:4A',
 'last_chassis_mac': '00:01:E8:79:2F:4A'}
    motd = ' \n'
    cli = {
## 'show version'
'show version': """show version
Force10 Networks Real Time Operating System Software
Force10 Operating System Version: 1.0
Force10 Application Software Version: 8.3.1.1
Copyright (c) 1999-2009 by Force10 Networks, Inc.
Build Time: Mon Jan 18 14:59:03 2010
Build Path: /sites/sjc/work/build/buildSpaces/build02/E8-3-1/SW/SRC
sw-2 uptime is 29 week(s), 5 day(s), 14 hour(s), 40 minute(s)

System image file is "flash://FTOS-CB-8.3.1.1.bin"

Chassis Type: C300 
Control Processor: IBM PowerPC 750FX (Rev D2.2) with 1090519040 bytes of memory.

128K bytes of non-volatile configuration memory.

  2 Route Processor/Switch Fabric Module
  6 48-port GE 10/100/1000Base-T line card with RJ45 interfaces (CB)
  2 8-port 10GE LAN PHY line card with XFP optics (CB)
  2 FastEthernet/IEEE 802.3 interface(s)
288 GigabitEthernet/IEEE 802.3 interface(s)
 16 Ten GigabitEthernet/IEEE 802.3 interface(s)""", 
'terminal length 0':  'terminal length 0\n', 
## 'show chassis brief'
'show chassis brief': """show chassis brief
Chassis Type  : C300      
Chassis Mode  : 1.0       
Chassis MAC   : 00:01:e8:79:2f:4a 

--  Line cards  --
Slot  Status        NxtBoot    ReqTyp   CurTyp   Version     Ports
---------------------------------------------------------------------------
  0   online        online     E48TB    E48TB    8.3.1.1     48     
  1   online        online     E48TB    E48TB    8.3.1.1     48     
  2   online        online     E48TB    E48TB    8.3.1.1     48     
  3   online        online     E48TB    E48TB    8.3.1.1     48     
  4   online        online     E48TB    E48TB    8.3.1.1     48     
  5   online        online     E48TB    E48TB    8.3.1.1     48     
  6   online        online     EX8PB    EX8PB    8.3.1.1     8     
  7   online        online     EX8PB    EX8PB    8.3.1.1     8     

--  Route Processor Modules --
Slot  Status        NxtBoot    Version          
---------------------------------------------------------------------------
  0   active        online     8.3.1.1
  1   standby       online     8.3.1.1

Switch Fabric State: up

--  Switch Fabric Modules  --
Slot  Status                     
---------------------------------------------------------------------------
  0   active               
  1   active               

--  Power Supplies  --
Bay   Status
---------------------------------------------------------------------------
  0   absent          
  1   active          
  2   absent          
  3   active          
  4   absent          
  5   active          
  6   absent          
  7   active          

--  Fan Status  --
--------------------------------------------------------------------------------
Tray   0 
--------------------------------------------------------------------------------
FanNumber    Speed    Status 
      0      3240      up       
      1      3240      up       
      2      3210      up       
      3      3210      up       
      4      3210      up       
      5      3210      up       
 """, 
}
    snmp_get = {}
    snmp_getnext = {}
    http_get = {}
