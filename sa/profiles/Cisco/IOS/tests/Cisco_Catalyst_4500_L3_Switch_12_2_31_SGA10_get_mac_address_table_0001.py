# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Cisco.IOS.get_mac_address_table test
## Auto-generated by manage.py debug-script at 2010-09-27 10:41:22
##----------------------------------------------------------------------
## Copyright (C) 2007-2010 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
from noc.lib.test import ScriptTestCase
class Cisco_IOS_get_mac_address_table_Test(ScriptTestCase):
    script="Cisco.IOS.get_mac_address_table"
    vendor="Cisco"
    platform='Catalyst 4500 L3 Switch'
    version='12.2(31)SGA10'
    input={}
    result=[
        {'mac': '00:07:E9:D7:BA:1E', 'type': 'D', 'interfaces': ['Gi 1/1'], 'vlan_id': 2},
        {'mac': '00:0D:61:7C:A4:B5', 'type': 'D', 'interfaces': ['Gi 1/1'], 'vlan_id': 2},
        {'mac': '00:0E:7F:7C:CA:3E', 'type': 'D', 'interfaces': ['Gi 1/1'], 'vlan_id': 2},
        {'mac': '00:0F:F8:CF:98:0A', 'type': 'D', 'interfaces': ['Gi 1/1'], 'vlan_id': 2},
        {'mac': '00:15:F2:04:76:04', 'type': 'D', 'interfaces': ['Fa 4/4'], 'vlan_id': 2},
        {'mac': '00:16:C7:BE:14:58', 'type': 'D', 'interfaces': ['Gi 1/1'], 'vlan_id': 2},
        {'mac': '00:1A:A2:90:58:C1', 'type': 'D', 'interfaces': ['Gi 1/1'], 'vlan_id': 2},
        {'mac': '00:1A:E2:13:BE:41', 'type': 'D', 'interfaces': ['Gi 1/1'], 'vlan_id': 2},
        {'mac': '00:1B:77:2D:A5:90', 'type': 'D', 'interfaces': ['Gi 1/1'], 'vlan_id': 2},
        {'mac': '00:1E:BE:5A:6D:3F', 'type': 'D', 'interfaces': ['Gi 1/1'], 'vlan_id': 2},
        {'mac': '00:30:48:92:DC:8A', 'type': 'D', 'interfaces': ['Gi 1/1'], 'vlan_id': 2},
        {'mac': '00:30:48:93:B8:79', 'type': 'D', 'interfaces': ['Gi 1/1'], 'vlan_id': 2},
        {'mac': '00:30:48:93:B9:5C', 'type': 'D', 'interfaces': ['Gi 1/1'], 'vlan_id': 2}]
    motd=''
    cli={
## 'show mac address-table'
'show mac address-table': """show mac address-table
Unicast Entries
 vlan   mac address     type        protocols               port
-------+---------------+--------+---------------------+--------------------
   2    0007.e9d7.ba1e   dynamic ip                    GigabitEthernet1/1    
   2    000d.617c.a4b5   dynamic ip                    GigabitEthernet1/1    
   2    000e.7f7c.ca3e   dynamic ip                    GigabitEthernet1/1    
   2    000f.f8cf.980a   dynamic ip,assigned           GigabitEthernet1/1    
   2    0015.f204.7604   dynamic ip                    FastEthernet4/4       
   2    0016.c7be.1458   dynamic ip,assigned           GigabitEthernet1/1    
   2    0019.e8c0.27ff    static ip,ipx,assigned,other Switch                
   2    001a.a290.58c1   dynamic ip                    GigabitEthernet1/1    
   2    001a.e213.be41   dynamic ip,assigned           GigabitEthernet1/1    
   2    001b.772d.a590   dynamic ip,other              GigabitEthernet1/1    
   2    001e.be5a.6d3f   dynamic ip                    GigabitEthernet1/1    
   2    0030.4892.dc8a   dynamic ip                    GigabitEthernet1/1    
   2    0030.4893.b879   dynamic ip                    GigabitEthernet1/1    
   2    0030.4893.b95c   dynamic ip                    GigabitEthernet1/1    
Fa4/30  0004.9605.31ba   dynamic ip,other              FastEthernet4/30      
Fa4/30  000d.6135.2ab5   dynamic ip                    FastEthernet4/30      

Multicast Entries
 vlan    mac address     type    ports
-------+---------------+-------+--------------------------------------------
   1    ffff.ffff.ffff   system Fa4/9,Fa4/18,Fa4/23
   2    ffff.ffff.ffff   system Fa4/4,Fa4/9,Gi1/1,Switch
   3    ffff.ffff.ffff   system Fa4/9,Gi1/1
   4    0100.5e7f.fffa     igmp Fa4/10,Gi1/1
   5    0100.5e7f.fffa     igmp Fa2/3,Fa2/4,Fa2/5,Fa2/6,Fa2/12,Fa2/14,Fa2/15
                                Fa2/18,Fa2/20,Fa2/25,Fa5/1
   6    ffff.ffff.ffff   system Fa2/3,Fa2/4,Fa2/5,Fa2/6,Fa2/9,Fa2/10,Fa2/12
                                Fa2/14,Fa2/15,Fa2/18,Fa2/20,Fa2/25,Fa2/26
                                Fa2/32,Fa2/34,Fa4/7,Fa4/9,Fa5/1,Fa5/2,Gi1/1
   7    ffff.ffff.ffff   system Fa4/9,Fa4/38,Gi1/1
Fa4/30  ffff.ffff.ffff   system Fa4/30,Switch
""",
'terminal length 0':  'terminal length 0\n',
}
    snmp_get={}
    snmp_getnext={}
