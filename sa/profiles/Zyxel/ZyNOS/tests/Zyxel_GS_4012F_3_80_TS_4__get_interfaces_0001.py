# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Zyxel.ZyNOS.get_interfaces test
## Auto-generated by ./noc debug-script at 21.09.2012 20:58:13
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class Zyxel_ZyNOS_get_interfaces_Test(ScriptTestCase):
    script = "Zyxel.ZyNOS.get_interfaces"
    vendor = "Zyxel"
    platform = "GS-4012F"
    version = "3.80(TS.4)"
    input = {}
    result = [{'forwarding_instance': 'default',
  'interfaces': [{'admin_status': True,
                  'description': 'dom1',
                  'mac': '00:13:49:EA:6A:45',
                  'name': '1',
                  'oper_status': True,
                  'subinterfaces': [{'admin_status': True,
                                     'description': 'dom1',
                                     'enabled_afi': ['BRIDGE'],
                                     'is_bridge': True,
                                     'mac': '00:13:49:EA:6A:45',
                                     'name': '1',
                                     'oper_status': True,
                                     'tagged_vlans': [547,
                                                      2203,
                                                      2225,
                                                      2226,
                                                      2227,
                                                      2228,
                                                      2230,
                                                      2231,
                                                      3000,
                                                      3997,
                                                      4015,
                                                      4058]}],
                  'type': 'physical'},
                 {'admin_status': True,
                  'description': 'dom3',
                  'mac': '00:13:49:EA:6A:45',
                  'name': '2',
                  'oper_status': True,
                  'subinterfaces': [{'admin_status': True,
                                     'description': 'dom3',
                                     'enabled_afi': ['BRIDGE'],
                                     'is_bridge': True,
                                     'mac': '00:13:49:EA:6A:45',
                                     'name': '2',
                                     'oper_status': True,
                                     'tagged_vlans': [2204, 2231, 4015]}],
                  'type': 'physical'},
                 {'admin_status': True,
                  'mac': '00:13:49:EA:6A:45',
                  'name': '3',
                  'oper_status': False,
                  'subinterfaces': [{'admin_status': True,
                                     'enabled_afi': ['BRIDGE'],
                                     'is_bridge': True,
                                     'mac': '00:13:49:EA:6A:45',
                                     'name': '3',
                                     'oper_status': False,
                                     'tagged_vlans': [2231]}],
                  'type': 'physical'},
                 {'admin_status': True,
                  'mac': '00:13:49:EA:6A:45',
                  'name': '4',
                  'oper_status': False,
                  'subinterfaces': [{'admin_status': True,
                                     'enabled_afi': ['BRIDGE'],
                                     'is_bridge': True,
                                     'mac': '00:13:49:EA:6A:45',
                                     'name': '4',
                                     'oper_status': False,
                                     'tagged_vlans': [2231]}],
                  'type': 'physical'},
                 {'admin_status': True,
                  'mac': '00:13:49:EA:6A:45',
                  'name': '5',
                  'oper_status': False,
                  'subinterfaces': [{'admin_status': True,
                                     'enabled_afi': ['BRIDGE'],
                                     'is_bridge': True,
                                     'mac': '00:13:49:EA:6A:45',
                                     'name': '5',
                                     'oper_status': False,
                                     'tagged_vlans': [2231]}],
                  'type': 'physical'},
                 {'admin_status': True,
                  'mac': '00:13:49:EA:6A:45',
                  'name': '6',
                  'oper_status': False,
                  'subinterfaces': [{'admin_status': True,
                                     'enabled_afi': ['BRIDGE'],
                                     'is_bridge': True,
                                     'mac': '00:13:49:EA:6A:45',
                                     'name': '6',
                                     'oper_status': False,
                                     'tagged_vlans': [2231]}],
                  'type': 'physical'},
                 {'admin_status': True,
                  'mac': '00:13:49:EA:6A:45',
                  'name': '7',
                  'oper_status': False,
                  'subinterfaces': [{'admin_status': True,
                                     'enabled_afi': ['BRIDGE'],
                                     'is_bridge': True,
                                     'mac': '00:13:49:EA:6A:45',
                                     'name': '7',
                                     'oper_status': False,
                                     'tagged_vlans': [2231]}],
                  'type': 'physical'},
                 {'admin_status': True,
                  'mac': '00:13:49:EA:6A:45',
                  'name': '8',
                  'oper_status': False,
                  'subinterfaces': [{'admin_status': True,
                                     'enabled_afi': ['BRIDGE'],
                                     'is_bridge': True,
                                     'mac': '00:13:49:EA:6A:45',
                                     'name': '8',
                                     'oper_status': False,
                                     'tagged_vlans': [2231]}],
                  'type': 'physical'},
                 {'admin_status': True,
                  'mac': '00:13:49:EA:6A:45',
                  'name': '9',
                  'oper_status': False,
                  'subinterfaces': [{'admin_status': True,
                                     'enabled_afi': ['BRIDGE'],
                                     'is_bridge': True,
                                     'mac': '00:13:49:EA:6A:45',
                                     'name': '9',
                                     'oper_status': False,
                                     'tagged_vlans': [2231]}],
                  'type': 'physical'},
                 {'admin_status': True,
                  'mac': '00:13:49:EA:6A:45',
                  'name': '10',
                  'oper_status': False,
                  'subinterfaces': [{'admin_status': True,
                                     'enabled_afi': ['BRIDGE'],
                                     'is_bridge': True,
                                     'mac': '00:13:49:EA:6A:45',
                                     'name': '10',
                                     'oper_status': False,
                                     'tagged_vlans': [2231]}],
                  'type': 'physical'},
                 {'admin_status': True,
                  'description': 'dom5',
                  'mac': '00:13:49:EA:6A:45',
                  'name': '11',
                  'oper_status': True,
                  'subinterfaces': [{'admin_status': True,
                                     'description': 'dom5',
                                     'enabled_afi': ['BRIDGE'],
                                     'is_bridge': True,
                                     'mac': '00:13:49:EA:6A:45',
                                     'name': '11',
                                     'oper_status': True,
                                     'tagged_vlans': [515,
                                                      516,
                                                      523,
                                                      529,
                                                      2200,
                                                      2201,
                                                      2202,
                                                      2205,
                                                      2206,
                                                      2207,
                                                      2208,
                                                      2210,
                                                      2212,
                                                      2213,
                                                      2221,
                                                      2231,
                                                      4015]}],
                  'type': 'physical'},
                 {'admin_status': True,
                  'description': 'uplink',
                  'mac': '00:13:49:EA:6A:45',
                  'name': '12',
                  'oper_status': True,
                  'subinterfaces': [{'admin_status': True,
                                     'description': 'uplink',
                                     'enabled_afi': ['BRIDGE'],
                                     'is_bridge': True,
                                     'mac': '00:13:49:EA:6A:45',
                                     'name': '12',
                                     'oper_status': True,
                                     'tagged_vlans': [515,
                                                      516,
                                                      523,
                                                      529,
                                                      547,
                                                      2200,
                                                      2201,
                                                      2202,
                                                      2203,
                                                      2204,
                                                      2205,
                                                      2206,
                                                      2207,
                                                      2208,
                                                      2210,
                                                      2212,
                                                      2213,
                                                      2221,
                                                      2225,
                                                      2226,
                                                      2227,
                                                      2228,
                                                      2230,
                                                      2231,
                                                      3000,
                                                      4015,
                                                      4058]}],
                  'type': 'physical'},
                 {'admin_status': True,
                  'description': 'Outband management',
                  'mac': '00:13:49:EA:6A:45',
                  'name': 'Management',
                  'oper_status': True,
                  'subinterfaces': [{'admin_status': True,
                                     'description': 'Outband management',
                                     'enabled_afi': ['IPv4'],
                                     'enabled_protocols': [],
                                     'ipv4_addresses': ['192.168.0.1/24'],
                                     'is_ipv4': True,
                                     'mac': '00:13:49:EA:6A:45',
                                     'name': 'Management',
                                     'oper_status': True}],
                  'type': 'physical'},
                 {'admin_status': True,
                  'description': 'vlan3000',
                  'mac': '00:13:49:EA:6A:45',
                  'name': 'vlan3000',
                  'oper_status': True,
                  'subinterfaces': [{'admin_status': True,
                                     'description': 'vlan3000',
                                     'enabled_afi': ['IPv4'],
                                     'enabled_protocols': [],
                                     'ipv4_addresses': ['10.254.119.3/29'],
                                     'is_ipv4': True,
                                     'mac': '00:13:49:EA:6A:45',
                                     'name': 'vlan3000',
                                     'oper_status': True,
                                     'vlan_ids': [3000]}],
                  'type': 'SVI'},
                 {'admin_status': True,
                  'description': 'vlan3997',
                  'mac': '00:13:49:EA:6A:45',
                  'name': 'vlan3997',
                  'oper_status': True,
                  'subinterfaces': [{'admin_status': True,
                                     'description': 'vlan3997',
                                     'enabled_afi': ['IPv4'],
                                     'enabled_protocols': ['RIP', 'OSPF'],
                                     'ipv4_addresses': ['10.254.172.16/24'],
                                     'is_ipv4': True,
                                     'is_ospf': True,
                                     'is_rip': True,
                                     'mac': '00:13:49:EA:6A:45',
                                     'name': 'vlan3997',
                                     'oper_status': True,
                                     'vlan_ids': [3997]}],
                  'type': 'SVI'}],
  'type': 'ip'}]
    motd = ' **********\nCopyright (c) 1994 - 2008 ZyXEL Communications Corp.\n'
    cli = {
## 'show vlan-stacking'
'show vlan-stacking': """ show vlan-stacking
Switch Vlan Stacking Configuration
Operation: inactive
STPID: 0x8100

Port\t\t Role\t\t SPVID\t\t Priority
01\t\t access\t\t 1\t\t 0
02\t\t access\t\t 1\t\t 0
03\t\t access\t\t 1\t\t 0
04\t\t access\t\t 1\t\t 0
05\t\t access\t\t 1\t\t 0
06\t\t access\t\t 1\t\t 0
07\t\t access\t\t 1\t\t 0
08\t\t access\t\t 1\t\t 0
09\t\t access\t\t 1\t\t 0
10\t\t access\t\t 1\t\t 0
11\t\t access\t\t 1\t\t 0
12\t\t access\t\t 1\t\t 0""", 
## 'show interface config 11'
'show interface config 11': """ show interface config 11
  Port Configurations:
  
  
  Port No \t:11
    Active \t:Yes
    Name  \t:dom5
    PVID \t:1\t\tFlow Control \t:No
    Type \t:10/100/1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  """, 
## 'show trunk'
'show trunk': """ show trunk
Group ID 1:\tinactive 
  Status: -
  Member number: 0\t
Group ID 2:\tinactive 
  Status: -
  Member number: 0\t
Group ID 3:\tinactive 
  Status: -
  Member number: 0\t
Group ID 4:\tinactive 
  Status: -
  Member number: 0\t
Group ID 5:\tinactive 
  Status: -
  Member number: 0\t
Group ID 6:\tinactive 
  Status: -
  Member number: 0\t""", 
## 'show interface config 9'
'show interface config 9': """ show interface config 9
  Port Configurations:
  
  
  Port No \t:9
    Active \t:Yes
    Name  \t:
    PVID \t:1\t\tFlow Control \t:No
    Type \t:10/100/1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  """, 
## 'show vlan'
'show vlan': """ show vlan
  The Number of VLAN :    29
  Idx.  VID   Status     Elap-Time    TagCtl                                 
  ----  ----  ---------  -----------  ---------------------------------------
  
     1     1     Static   1298:26:58  Untagged :
                                      Tagged   :
  
     2   515     Static   1298:26:58  Untagged :
                                      Tagged   :11-12
  
     3   516     Static   1298:26:58  Untagged :
                                      Tagged   :11-12
  
     4   523     Static   1298:26:58  Untagged :
                                      Tagged   :11-12
  
     5   529     Static   1298:26:58  Untagged :
                                      Tagged   :11-12
  
     6   547     Static   1298:26:58  Untagged :
                                      Tagged   :1,12
  
     7  2200     Static   1298:26:58  Untagged :
                                     Tagged   :11-12
  
     8  2201     Static   1298:26:58  Untagged :
                                      Tagged   :11-12
  
     9  2202     Static   1298:26:58  Untagged :
                                      Tagged   :11-12
  
    10  2203     Static   1298:26:58  Untagged :
                                      Tagged   :1,12
  
    11  2204     Static   1298:26:58  Untagged :
                                      Tagged   :2,12
  
    12  2205     Static   1298:26:58  Untagged :
                                      Tagged   :11-12
  
    13  2206     Static   1298:26:58  Untagged :
                                      Tagged   :11-12
  
    14  2207     Static   1298:26:58  Untagged :
                                      Tagged   :11-12
  
   15  2208     Static   1298:26:58  Untagged :
                                      Tagged   :11-12
  
    16  2210     Static   1298:26:58  Untagged :
                                      Tagged   :11-12
  
    17  2212     Static   1298:26:58  Untagged :
                                      Tagged   :11-12
  
    18  2213     Static   1298:26:58  Untagged :
                                      Tagged   :11-12
  
    19  2221     Static   1298:26:58  Untagged :
                                      Tagged   :11-12
  
    20  2225     Static   1298:26:58  Untagged :
                                      Tagged   :1,12
  
    21  2226     Static   1298:26:58  Untagged :
                                      Tagged   :1,12
  
    22  2227     Static   1298:26:58  Untagged :
                                      Tagged   :1,12
 
    23  2228     Static   1298:26:58  Untagged :
                                      Tagged   :1,12
  
    24  2230     Static   1298:26:58  Untagged :
                                      Tagged   :1,12
  
    25  2231     Static   1298:26:58  Untagged :
                                      Tagged   :1-12
  
    26  3000     Static   1298:26:58  Untagged :
                                      Tagged   :1,12
  
    27  3997     Static      0:12:02  Untagged :
                                      Tagged   :1
  
    28  4015     Static   1298:26:58  Untagged :
                                      Tagged   :1-2,11-12
  
    29  4058     Static   1298:26:58  Untagged :
                                      Tagged   :1,12""", 
## 'show system-information'
'show system-information': """ show system-information

System Name\t\t: sw-dom-5
System Contact\t\t: admin@someprovider.net
System Location\t\t: Dom, 5
Ethernet Address\t: 00:13:49:ea:6a:45
ZyNOS F/W Version\t: V3.80(TS.4) | 10/07/2008
RomRasSize\t\t: 3191378 
System up Time\t\t:  1298:27:19 (1bdca11f ticks)
Bootbase Version\t: V3.0 | 04/08/2005
ZyNOS CODE\t\t: RAS Oct  6 2008 17:28:42
Product Model\t\t: GS-4012F""", 
## 'show interface config 6'
'show interface config 6': """ show interface config 6
  Port Configurations:
  
  
  Port No \t:6
    Active \t:Yes
    Name  \t:
    PVID \t:1\t\tFlow Control \t:No
    Type \t:1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  """, 
## 'show interfaces *'
'show interfaces *': """ show interfaces *
  Port Info\tPort NO.\t\t:1
  \t\tLink\t\t\t:1000M/F  
  \t\tStatus\t\t\t:FORWARDING
  \t\tLACP\t\t\t:Disabled
  \t\tTxPkts\t\t\t:3774318755
  \t\tRxPkts\t\t\t:4352735834
  \t\tErrors\t\t\t:0
  \t\tTx KBs/s\t\t:275.980
  \t\tRx KBs/s\t\t:688.466
  \t\tUp Time\t\t\t:500:01:30
  TX Packet\tTx Packets\t\t:3774318755
  \t\tMulticast\t\t:38876606
  \t\tBroadcast\t\t:3339767
  \t\tPause\t\t\t:0
  \t\tTagged\t\t\t:3774319192
  RX Packet\tRx Packets\t\t:4352735834
  \t\tMulticast\t\t:1456276
  \t\tBroadcast\t\t:706115
  \t\tPause\t\t\t:0
  \t\tControl\t\t\t:0
  TX Collison\tSingle\t\t\t:0
  \t\tMultiple\t\t:0
  \t\tExcessive\t\t:0
 \t\tLate\t\t\t:0
  Error Packet\tRX CRC\t\t\t:0
  \t\tLength\t\t\t:0
  \t\tRunt\t\t\t:0
  Distribution\t64\t\t\t:7475582
  \t\t65 to 127\t\t:3304130048
  \t\t128 to 255\t\t:380019109
  \t\t256 to 511\t\t:178523021
  \t\t512 to 1023\t\t:181857534
  \t\t1024 to 1518\t\t:3374833233
  \t\tGiant\t\t\t:3477
  
  Port Info\tPort NO.\t\t:2
  \t\tLink\t\t\t:1000M/F  
  \t\tStatus\t\t\t:FORWARDING
  \t\tLACP\t\t\t:Disabled
  \t\tTxPkts\t\t\t:144818720
  \t\tRxPkts\t\t\t:87850637
  \t\tErrors\t\t\t:0
  \t\tTx KBs/s\t\t:3976.305
  \t\tRx KBs/s\t\t:103.495
  \t\tUp Time\t\t\t:500:01:14
  TX Packet\tTx Packets\t\t:144818720
 \t\tMulticast\t\t:8688395
  \t\tBroadcast\t\t:2688128
  \t\tPause\t\t\t:0
  \t\tTagged\t\t\t:144822849
  RX Packet\tRx Packets\t\t:87850637
  \t\tMulticast\t\t:3985
  \t\tBroadcast\t\t:19900
  \t\tPause\t\t\t:0
  \t\tControl\t\t\t:0
  TX Collison\tSingle\t\t\t:0
  \t\tMultiple\t\t:0
  \t\tExcessive\t\t:0
  \t\tLate\t\t\t:0
  Error Packet\tRX CRC\t\t\t:0
  \t\tLength\t\t\t:0
  \t\tRunt\t\t\t:0
  Distribution\t64\t\t\t:119802
  \t\t65 to 127\t\t:117564345
  \t\t128 to 255\t\t:18100976
  \t\t256 to 511\t\t:4861111
  \t\t512 to 1023\t\t:3873377
  \t\t1024 to 1518\t\t:61541617
  \t\tGiant\t\t\t:0
 
  Port Info\tPort NO.\t\t:3
  \t\tLink\t\t\t:Down  
  \t\tStatus\t\t\t:STOP
  \t\tLACP\t\t\t:Disabled
  \t\tTxPkts\t\t\t:0
  \t\tRxPkts\t\t\t:0
  \t\tErrors\t\t\t:0
  \t\tTx KBs/s\t\t:0.0
  \t\tRx KBs/s\t\t:0.0
  \t\tUp Time\t\t\t::00:00
  TX Packet\tTx Packets\t\t:0
  \t\tMulticast\t\t:0
  \t\tBroadcast\t\t:0
  \t\tPause\t\t\t:0
  \t\tTagged\t\t\t:0
  RX Packet\tRx Packets\t\t:0
  \t\tMulticast\t\t:0
  \t\tBroadcast\t\t:0
  \t\tPause\t\t\t:0
  \t\tControl\t\t\t:0
  TX Collison\tSingle\t\t\t:0
  \t\tMultiple\t\t:0
 \t\tExcessive\t\t:0
  \t\tLate\t\t\t:0
  Error Packet\tRX CRC\t\t\t:0
  \t\tLength\t\t\t:0
  \t\tRunt\t\t\t:0
  Distribution\t64\t\t\t:0
  \t\t65 to 127\t\t:0
  \t\t128 to 255\t\t:0
  \t\t256 to 511\t\t:0
  \t\t512 to 1023\t\t:0
  \t\t1024 to 1518\t\t:0
  \t\tGiant\t\t\t:0
  
  Port Info\tPort NO.\t\t:4
  \t\tLink\t\t\t:Down  
  \t\tStatus\t\t\t:STOP
  \t\tLACP\t\t\t:Disabled
  \t\tTxPkts\t\t\t:0
  \t\tRxPkts\t\t\t:0
  \t\tErrors\t\t\t:0
  \t\tTx KBs/s\t\t:0.0
  \t\tRx KBs/s\t\t:0.0
  \t\tUp Time\t\t\t::00:00
 TX Packet\tTx Packets\t\t:0
  \t\tMulticast\t\t:0
  \t\tBroadcast\t\t:0
  \t\tPause\t\t\t:0
  \t\tTagged\t\t\t:0
  RX Packet\tRx Packets\t\t:0
  \t\tMulticast\t\t:0
  \t\tBroadcast\t\t:0
  \t\tPause\t\t\t:0
  \t\tControl\t\t\t:0
  TX Collison\tSingle\t\t\t:0
  \t\tMultiple\t\t:0
  \t\tExcessive\t\t:0
  \t\tLate\t\t\t:0
  Error Packet\tRX CRC\t\t\t:0
  \t\tLength\t\t\t:0
  \t\tRunt\t\t\t:0
  Distribution\t64\t\t\t:0
  \t\t65 to 127\t\t:0
  \t\t128 to 255\t\t:0
  \t\t256 to 511\t\t:0
  \t\t512 to 1023\t\t:0
  \t\t1024 to 1518\t\t:0
 \t\tGiant\t\t\t:0
  
  Port Info\tPort NO.\t\t:5
  \t\tLink\t\t\t:Down  
  \t\tStatus\t\t\t:STOP
  \t\tLACP\t\t\t:Disabled
  \t\tTxPkts\t\t\t:0
  \t\tRxPkts\t\t\t:0
  \t\tErrors\t\t\t:0
  \t\tTx KBs/s\t\t:0.0
  \t\tRx KBs/s\t\t:0.0
  \t\tUp Time\t\t\t::00:00
  TX Packet\tTx Packets\t\t:0
  \t\tMulticast\t\t:0
  \t\tBroadcast\t\t:0
  \t\tPause\t\t\t:0
  \t\tTagged\t\t\t:0
  RX Packet\tRx Packets\t\t:0
  \t\tMulticast\t\t:0
  \t\tBroadcast\t\t:0
  \t\tPause\t\t\t:0
  \t\tControl\t\t\t:0
  TX Collison\tSingle\t\t\t:0
 \t\tMultiple\t\t:0
  \t\tExcessive\t\t:0
  \t\tLate\t\t\t:0
  Error Packet\tRX CRC\t\t\t:0
  \t\tLength\t\t\t:0
  \t\tRunt\t\t\t:0
  Distribution\t64\t\t\t:0
  \t\t65 to 127\t\t:0
  \t\t128 to 255\t\t:0
  \t\t256 to 511\t\t:0
  \t\t512 to 1023\t\t:0
  \t\t1024 to 1518\t\t:0
  \t\tGiant\t\t\t:0
  
  Port Info\tPort NO.\t\t:6
  \t\tLink\t\t\t:Down  
  \t\tStatus\t\t\t:STOP
  \t\tLACP\t\t\t:Disabled
  \t\tTxPkts\t\t\t:0
  \t\tRxPkts\t\t\t:0
  \t\tErrors\t\t\t:0
  \t\tTx KBs/s\t\t:0.0
  \t\tRx KBs/s\t\t:0.0
 \t\tUp Time\t\t\t::00:00
  TX Packet\tTx Packets\t\t:0
  \t\tMulticast\t\t:0
  \t\tBroadcast\t\t:0
  \t\tPause\t\t\t:0
  \t\tTagged\t\t\t:0
  RX Packet\tRx Packets\t\t:0
  \t\tMulticast\t\t:0
  \t\tBroadcast\t\t:0
  \t\tPause\t\t\t:0
  \t\tControl\t\t\t:0
  TX Collison\tSingle\t\t\t:0
  \t\tMultiple\t\t:0
  \t\tExcessive\t\t:0
  \t\tLate\t\t\t:0
  Error Packet\tRX CRC\t\t\t:0
  \t\tLength\t\t\t:0
  \t\tRunt\t\t\t:0
  Distribution\t64\t\t\t:0
  \t\t65 to 127\t\t:0
  \t\t128 to 255\t\t:0
  \t\t256 to 511\t\t:0
  \t\t512 to 1023\t\t:0
 \t\t1024 to 1518\t\t:0
  \t\tGiant\t\t\t:0
  
  Port Info\tPort NO.\t\t:7
  \t\tLink\t\t\t:Down  
  \t\tStatus\t\t\t:STOP
  \t\tLACP\t\t\t:Disabled
  \t\tTxPkts\t\t\t:0
  \t\tRxPkts\t\t\t:0
  \t\tErrors\t\t\t:0
  \t\tTx KBs/s\t\t:0.0
  \t\tRx KBs/s\t\t:0.0
  \t\tUp Time\t\t\t::00:00
  TX Packet\tTx Packets\t\t:0
  \t\tMulticast\t\t:0
  \t\tBroadcast\t\t:0
  \t\tPause\t\t\t:0
  \t\tTagged\t\t\t:0
  RX Packet\tRx Packets\t\t:0
  \t\tMulticast\t\t:0
  \t\tBroadcast\t\t:0
  \t\tPause\t\t\t:0
  \t\tControl\t\t\t:0
 TX Collison\tSingle\t\t\t:0
  \t\tMultiple\t\t:0
  \t\tExcessive\t\t:0
  \t\tLate\t\t\t:0
  Error Packet\tRX CRC\t\t\t:0
  \t\tLength\t\t\t:0
  \t\tRunt\t\t\t:0
  Distribution\t64\t\t\t:0
  \t\t65 to 127\t\t:0
  \t\t128 to 255\t\t:0
  \t\t256 to 511\t\t:0
  \t\t512 to 1023\t\t:0
  \t\t1024 to 1518\t\t:0
  \t\tGiant\t\t\t:0
  
  Port Info\tPort NO.\t\t:8
  \t\tLink\t\t\t:Down  
  \t\tStatus\t\t\t:STOP
  \t\tLACP\t\t\t:Disabled
  \t\tTxPkts\t\t\t:0
  \t\tRxPkts\t\t\t:0
  \t\tErrors\t\t\t:0
  \t\tTx KBs/s\t\t:0.0
 \t\tRx KBs/s\t\t:0.0
  \t\tUp Time\t\t\t::00:00
  TX Packet\tTx Packets\t\t:0
  \t\tMulticast\t\t:0
  \t\tBroadcast\t\t:0
  \t\tPause\t\t\t:0
  \t\tTagged\t\t\t:0
  RX Packet\tRx Packets\t\t:0
  \t\tMulticast\t\t:0
  \t\tBroadcast\t\t:0
  \t\tPause\t\t\t:0
  \t\tControl\t\t\t:0
  TX Collison\tSingle\t\t\t:0
  \t\tMultiple\t\t:0
  \t\tExcessive\t\t:0
  \t\tLate\t\t\t:0
  Error Packet\tRX CRC\t\t\t:0
  \t\tLength\t\t\t:0
  \t\tRunt\t\t\t:0
  Distribution\t64\t\t\t:0
  \t\t65 to 127\t\t:0
  \t\t128 to 255\t\t:0
  \t\t256 to 511\t\t:0
 \t\t512 to 1023\t\t:0
  \t\t1024 to 1518\t\t:0
  \t\tGiant\t\t\t:0
  
  Port Info\tPort NO.\t\t:9
  \t\tLink\t\t\t:Down  
  \t\tStatus\t\t\t:STOP
  \t\tLACP\t\t\t:Disabled
  \t\tTxPkts\t\t\t:0
  \t\tRxPkts\t\t\t:0
  \t\tErrors\t\t\t:0
  \t\tTx KBs/s\t\t:0.0
  \t\tRx KBs/s\t\t:0.0
  \t\tUp Time\t\t\t::00:00
  TX Packet\tTx Packets\t\t:0
  \t\tMulticast\t\t:0
  \t\tBroadcast\t\t:0
  \t\tPause\t\t\t:0
  \t\tTagged\t\t\t:0
  RX Packet\tRx Packets\t\t:0
  \t\tMulticast\t\t:0
  \t\tBroadcast\t\t:0
  \t\tPause\t\t\t:0
 \t\tControl\t\t\t:0
  TX Collison\tSingle\t\t\t:0
  \t\tMultiple\t\t:0
  \t\tExcessive\t\t:0
  \t\tLate\t\t\t:0
  Error Packet\tRX CRC\t\t\t:0
  \t\tLength\t\t\t:0
  \t\tRunt\t\t\t:0
  Distribution\t64\t\t\t:0
  \t\t65 to 127\t\t:0
  \t\t128 to 255\t\t:0
  \t\t256 to 511\t\t:0
  \t\t512 to 1023\t\t:0
  \t\t1024 to 1518\t\t:0
  \t\tGiant\t\t\t:0
  
  Port Info\tPort NO.\t\t:10
  \t\tLink\t\t\t:Down  
  \t\tStatus\t\t\t:STOP
  \t\tLACP\t\t\t:Disabled
  \t\tTxPkts\t\t\t:0
  \t\tRxPkts\t\t\t:0
  \t\tErrors\t\t\t:0
 \t\tTx KBs/s\t\t:0.0
  \t\tRx KBs/s\t\t:0.0
  \t\tUp Time\t\t\t::00:00
  TX Packet\tTx Packets\t\t:0
  \t\tMulticast\t\t:0
  \t\tBroadcast\t\t:0
  \t\tPause\t\t\t:0
  \t\tTagged\t\t\t:0
  RX Packet\tRx Packets\t\t:0
  \t\tMulticast\t\t:0
  \t\tBroadcast\t\t:0
  \t\tPause\t\t\t:0
  \t\tControl\t\t\t:0
  TX Collison\tSingle\t\t\t:0
  \t\tMultiple\t\t:0
  \t\tExcessive\t\t:0
  \t\tLate\t\t\t:0
  Error Packet\tRX CRC\t\t\t:0
  \t\tLength\t\t\t:0
  \t\tRunt\t\t\t:0
  Distribution\t64\t\t\t:0
  \t\t65 to 127\t\t:0
  \t\t128 to 255\t\t:0
 \t\t256 to 511\t\t:0
  \t\t512 to 1023\t\t:0
  \t\t1024 to 1518\t\t:0
  \t\tGiant\t\t\t:0
  
  Port Info\tPort NO.\t\t:11
  \t\tLink\t\t\t:1000M/F Copper
  \t\tStatus\t\t\t:FORWARDING
  \t\tLACP\t\t\t:Disabled
  \t\tTxPkts\t\t\t:8371060664
  \t\tRxPkts\t\t\t:8049798357
  \t\tErrors\t\t\t:0
  \t\tTx KBs/s\t\t:7421.54
  \t\tRx KBs/s\t\t:589.143
  \t\tUp Time\t\t\t:298:26:42
  TX Packet\tTx Packets\t\t:8371060664
  \t\tMulticast\t\t:6884990
  \t\tBroadcast\t\t:2097603
  \t\tPause\t\t\t:0
  \t\tTagged\t\t\t:4076097037
  RX Packet\tRx Packets\t\t:8049798357
  \t\tMulticast\t\t:9864768
  \t\tBroadcast\t\t:5157965
 \t\tPause\t\t\t:0
  \t\tControl\t\t\t:0
  TX Collison\tSingle\t\t\t:0
  \t\tMultiple\t\t:0
  \t\tExcessive\t\t:0
  \t\tLate\t\t\t:0
  Error Packet\tRX CRC\t\t\t:0
  \t\tLength\t\t\t:0
  \t\tRunt\t\t\t:0
  Distribution\t64\t\t\t:55075885
  \t\t65 to 127\t\t:6701022185
  \t\t128 to 255\t\t:790584562
  \t\t256 to 511\t\t:312477222
  \t\t512 to 1023\t\t:400904783
  \t\t1024 to 1518\t\t:6537119480
  \t\tGiant\t\t\t:0
  
  Port Info\tPort NO.\t\t:12
  \t\tLink\t\t\t:1000M/F SFP
  \t\tStatus\t\t\t:FORWARDING
  \t\tLACP\t\t\t:Disabled
  \t\tTxPkts\t\t\t:12486349432
  \t\tRxPkts\t\t\t:12218506138
 \t\tErrors\t\t\t:0
  \t\tTx KBs/s\t\t:1410.951
  \t\tRx KBs/s\t\t:14909.173
  \t\tUp Time\t\t\t:500:01:31
  TX Packet\tTx Packets\t\t:12486349432
  \t\tMulticast\t\t:11324700
  \t\tBroadcast\t\t:2349730
  \t\tPause\t\t\t:0
  \t\tTagged\t\t\t:3896419413
  RX Packet\tRx Packets\t\t:12218506138
  \t\tMulticast\t\t:42221928
  \t\tBroadcast\t\t:2667334
  \t\tPause\t\t\t:0
  \t\tControl\t\t\t:0
  TX Collison\tSingle\t\t\t:0
  \t\tMultiple\t\t:0
  \t\tExcessive\t\t:0
  \t\tLate\t\t\t:0
  Error Packet\tRX CRC\t\t\t:0
  \t\tLength\t\t\t:0
  \t\tRunt\t\t\t:0
  Distribution\t64\t\t\t:62545821
  \t\t65 to 127\t\t:10070524770
 \t\t128 to 255\t\t:1166522190
  \t\t256 to 511\t\t:495468333
  \t\t512 to 1023\t\t:585945310
  \t\t1024 to 1518\t\t:9973377745
  \t\tGiant\t\t\t:3477
  """, 
## 'show interface config 4'
'show interface config 4': """ show interface config 4
  Port Configurations:
  
  
  Port No \t:4
    Active \t:Yes
    Name  \t:
    PVID \t:1\t\tFlow Control \t:No
    Type \t:1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  """, 
## 'show router rip'
'show router rip': """ show router rip
  IP Address      Subnet Mask     Direction  Version
  --------------------------------------------------
  10.254.119.3    255.255.255.248 None       V1
  10.254.172.16   255.255.255.0   Both       V2B""", 
## 'show interface config 2'
'show interface config 2': """ show interface config 2
  Port Configurations:
  
  
  Port No \t:2
    Active \t:Yes
    Name  \t:dom3
    PVID \t:1\t\tFlow Control \t:No
    Type \t:1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  """, 
## 'show interface config 1'
'show interface config 1': """ show interface config 1
  Port Configurations:
  
  
  Port No \t:1
    Active \t:Yes
    Name  \t:dom1
    PVID \t:1\t\tFlow Control \t:No
    Type \t:1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  """, 
## 'show interface config 8'
'show interface config 8': """ show interface config 8
  Port Configurations:
  
  
  Port No \t:8
    Active \t:Yes
    Name  \t:
    PVID \t:1\t\tFlow Control \t:No
    Type \t:1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  """, 
## 'show interface config 7'
'show interface config 7': """ show interface config 7
  Port Configurations:
  
  
  Port No \t:7
    Active \t:Yes
    Name  \t:
    PVID \t:1\t\tFlow Control \t:No
    Type \t:1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  """, 
## 'show interface config 10'
'show interface config 10': """ show interface config 10
  Port Configurations:
  
  
  Port No \t:10
    Active \t:Yes
    Name  \t:
    PVID \t:1\t\tFlow Control \t:No
    Type \t:10/100/1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  """, 
## 'show interface config *'
'show interface config *': """ show interface config *
  Port Configurations:
  
  
  Port No \t:1
    Active \t:Yes
    Name  \t:dom1
    PVID \t:1\t\tFlow Control \t:No
    Type \t:1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  
  Port No \t:2
    Active \t:Yes
    Name  \t:dom3
    PVID \t:1\t\tFlow Control \t:No
    Type \t:1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  
  Port No \t:3
    Active \t:Yes
    Name  \t:
    PVID \t:1\t\tFlow Control \t:No
    Type \t:1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
 
  Port No \t:4
    Active \t:Yes
    Name  \t:
    PVID \t:1\t\tFlow Control \t:No
    Type \t:1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  
  Port No \t:5
    Active \t:Yes
    Name  \t:
    PVID \t:1\t\tFlow Control \t:No
    Type \t:1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  
  Port No \t:6
    Active \t:Yes
    Name  \t:
    PVID \t:1\t\tFlow Control \t:No
    Type \t:1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  
  Port No \t:7
   Active \t:Yes
    Name  \t:
    PVID \t:1\t\tFlow Control \t:No
    Type \t:1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  
  Port No \t:8
    Active \t:Yes
    Name  \t:
    PVID \t:1\t\tFlow Control \t:No
    Type \t:1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  
  Port No \t:9
    Active \t:Yes
    Name  \t:
    PVID \t:1\t\tFlow Control \t:No
    Type \t:10/100/1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  
  Port No \t:10
    Active \t:Yes
    Name  \t:
   PVID \t:1\t\tFlow Control \t:No
    Type \t:10/100/1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  
  Port No \t:11
    Active \t:Yes
    Name  \t:dom5
    PVID \t:1\t\tFlow Control \t:No
    Type \t:10/100/1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  
  Port No \t:12
    Active \t:Yes
    Name  \t:uplink
    PVID \t:1\t\tFlow Control \t:No
    Type \t:10/100/1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  """, 
## 'show ip'
'show ip': """ show ip
Management IP Address
     IP[192.168.0.1], Netmask[255.255.255.0], VID[0]
IP Interface
     IP[10.254.172.16], Netmask[255.255.255.0], VID[3997]
     IP[10.254.119.3], Netmask[255.255.255.248], VID[3000]""", 
## 'show interface config 3'
'show interface config 3': """ show interface config 3
  Port Configurations:
  
  
  Port No \t:3
    Active \t:Yes
    Name  \t:
    PVID \t:1\t\tFlow Control \t:No
    Type \t:1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  """, 
## 'show ip ospf interface'
'show ip ospf interface': """ show ip ospf interface
swif4 is up, line protocol is up
  Internet Address 10.254.172.16/24, Area 0.0.0.0
  Router ID 10.254.119.3, Network Type BROADCAST, Cost: 15
  Transmit Delay is 1 sec, State DR, Priority 1
  Designated Router (ID) 10.254.119.3, Interface Address 10.254.172.16
  No backup designated router on this network
  Timer intervals configured, Hello 10, Dead 40, Wait 40, Retransmit 5
    Hello due in 00:00:04
  Neighbor Count is 0, Adjacent neighbor count is 0""", 
## 'show interface config 12'
'show interface config 12': """ show interface config 12
  Port Configurations:
  
  
  Port No \t:12
    Active \t:Yes
    Name  \t:uplink
    PVID \t:1\t\tFlow Control \t:No
    Type \t:10/100/1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  """, 
## 'show interface config 5'
'show interface config 5': """ show interface config 5
  Port Configurations:
  
  
  Port No \t:5
    Active \t:Yes
    Name  \t:
    PVID \t:1\t\tFlow Control \t:No
    Type \t:1000M\tSpeed/Duplex \t:auto
    BPDU \t:peer\t\t802.1p Priority :0
  """, 
}
    snmp_get = {}
    snmp_getnext = {}
    http_get = {}
