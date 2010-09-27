# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Force10.FTOS.get_lldp_neighbors test
## Auto-generated by manage.py debug-script at 2010-09-25 12:15:10
##----------------------------------------------------------------------
## Copyright (C) 2007-2010 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
from noc.lib.test import ScriptTestCase
class Force10_FTOS_get_lldp_neighbors_Test(ScriptTestCase):
    script="Force10.FTOS.get_lldp_neighbors"
    vendor="Force10"
    platform='C300'
    version='8.3.1.1'
    input={}
    result=[{'local_interface': 'Gi 2/36',
  'neighbors': [{'remote_capabilities': 4,
                 'remote_chassis_id': '00:24:81:D9:BC:21',
                 'remote_chassis_id_subtype': 4,
                 'remote_port': '19',
                 'remote_port_subtype': 7,
                 'remote_system_name': 'switch30-1'}]},
 {'local_interface': 'Gi 2/37',
  'neighbors': [{'remote_capabilities': 4,
                 'remote_chassis_id': '00:24:81:D9:BC:21',
                 'remote_chassis_id_subtype': 4,
                 'remote_port': '20',
                 'remote_port_subtype': 7,
                 'remote_system_name': 'switch30-1'}]},
 {'local_interface': 'Gi 2/38',
  'neighbors': [{'remote_capabilities': 4,
                 'remote_chassis_id': '00:24:81:D9:2D:E1',
                 'remote_chassis_id_subtype': 4,
                 'remote_port': '19',
                 'remote_port_subtype': 7,
                 'remote_system_name': 'switch30-2'}]},
 {'local_interface': 'Gi 2/39',
  'neighbors': [{'remote_capabilities': 4,
                 'remote_chassis_id': '00:24:81:D9:2D:E1',
                 'remote_chassis_id_subtype': 4,
                 'remote_port': '20',
                 'remote_port_subtype': 7,
                 'remote_system_name': 'switch30-2'}]},
 {'local_interface': 'Gi 2/40',
  'neighbors': [{'remote_capabilities': 4,
                 'remote_chassis_id': '00:24:81:D9:BC:21',
                 'remote_chassis_id_subtype': 4,
                 'remote_port': '17',
                 'remote_port_subtype': 7,
                 'remote_system_name': 'switch30-1'}]},
 {'local_interface': 'Gi 2/41',
  'neighbors': [{'remote_capabilities': 4,
                 'remote_chassis_id': '00:24:81:D9:BC:21',
                 'remote_chassis_id_subtype': 4,
                 'remote_port': '18',
                 'remote_port_subtype': 7,
                 'remote_system_name': 'switch30-1'}]},
 {'local_interface': 'Gi 2/42',
  'neighbors': [{'remote_capabilities': 4,
                 'remote_chassis_id': '00:24:81:D9:2D:E1',
                 'remote_chassis_id_subtype': 4,
                 'remote_port': '17',
                 'remote_port_subtype': 7,
                 'remote_system_name': 'switch30-2'}]},
 {'local_interface': 'Gi 2/43',
  'neighbors': [{'remote_capabilities': 4,
                 'remote_chassis_id': '00:24:81:D9:2D:E1',
                 'remote_chassis_id_subtype': 4,
                 'remote_port': '18',
                 'remote_port_subtype': 7,
                 'remote_system_name': 'switch30-2'}]},
 {'local_interface': 'Te 6/0',
  'neighbors': [{'remote_capabilities': 22,
                 'remote_chassis_id': '00:01:E8:6D:1C:5C',
                 'remote_chassis_id_subtype': 4,
                 'remote_port': 'TenGigabitEthernet 1/8',
                 'remote_port_subtype': 5,
                 'remote_system_name': 'switch1'}]},
 {'local_interface': 'Te 7/0',
  'neighbors': [{'remote_capabilities': 22,
                 'remote_chassis_id': '00:01:E8:6D:1C:5C',
                 'remote_chassis_id_subtype': 4,
                 'remote_port': 'TenGigabitEthernet 2/8',
                 'remote_port_subtype': 5,
                 'remote_system_name': 'switch1'}]}]
    motd=' \n'
    cli={
## 'show lldp neighbors detail'
'show lldp neighbors detail': """show lldp neighbors detail
========================================================================
 Local Interface Gi 2/36 has 1 neighbor 
  Total Frames Out: 379241 
  Total Frames In: 391048 
  Total Neighbor information Age outs: 0 
  Total Frames Discarded: 0 
  Total In Error Frames: 0 
  Total Unrecognized TLVs: 782096 
  Total TLVs Discarded: 0 
  Next packet will be sent after 26 seconds
  The neighbors are given below:
  -----------------------------------------------------------------------
 
    Remote Chassis ID Subtype: Mac address (4)
    Remote Chassis ID:  00:24:81:d9:bc:21
    Remote Port Subtype:  Locally assigned (7)
    Remote Port ID:  19
    Local Port ID: GigabitEthernet 2/36
    Locally assigned remote Neighbor Index: 1
    Remote TTL:  120
    Information valid for next 107 seconds 
    Time since last information change of this neighbor:  19w2d18h
    Remote System Name:  switch30-1
    Remote System Desc:  ProCurve 498358-B21 6120G/XG Blade Switch, revision 
     Z.14.08, ROM Z.14.06 (/sw/code/build/vern(t4br))
    Existing System Capabilities:  Bridge
    Enabled System Capabilities:  Bridge
    MAC PHY Configuration:
      Auto-neg supported: 1
      Auto-neg enabled: 1
      Auto-neg advertised capabilities:
        1000BASE-T full duplex mode,
        100BASE-TX full duplex mode,
        100BASE-TX half duplex mode,
        10BASE-T  full duplex mode,
        10BASE-T  half duplex mode
      Operational MAU type:
        1000BaseTFD: Four-pair Category 5 UTP, full duplex mode
   ---------------------------------------------------------------------------
 
========================================================================
 Local Interface Gi 2/37 has 1 neighbor 
  Total Frames Out: 379238 
  Total Frames In: 391048 
  Total Neighbor information Age outs: 0 
  Total Frames Discarded: 0 
  Total In Error Frames: 0 
  Total Unrecognized TLVs: 782096 
  Total TLVs Discarded: 0 
  Next packet will be sent after 6 seconds
  The neighbors are given below:
  -----------------------------------------------------------------------
 
    Remote Chassis ID Subtype: Mac address (4)
    Remote Chassis ID:  00:24:81:d9:bc:21
    Remote Port Subtype:  Locally assigned (7)
    Remote Port ID:  20
    Local Port ID: GigabitEthernet 2/37
    Locally assigned remote Neighbor Index: 1
    Remote TTL:  120
    Information valid for next 117 seconds 
    Time since last information change of this neighbor:  19w2d18h
    Remote System Name:  switch30-1
    Remote System Desc:  ProCurve 498358-B21 6120G/XG Blade Switch, revision 
     Z.14.08, ROM Z.14.06 (/sw/code/build/vern(t4br))
    Existing System Capabilities:  Bridge
    Enabled System Capabilities:  Bridge
    MAC PHY Configuration:
      Auto-neg supported: 1
      Auto-neg enabled: 1
      Auto-neg advertised capabilities:
        1000BASE-T full duplex mode,
        100BASE-TX full duplex mode,
        100BASE-TX half duplex mode,
        10BASE-T  full duplex mode,
        10BASE-T  half duplex mode
      Operational MAU type:
        1000BaseTFD: Four-pair Category 5 UTP, full duplex mode
   ---------------------------------------------------------------------------
 
========================================================================
 Local Interface Gi 2/38 has 1 neighbor 
  Total Frames Out: 379228 
  Total Frames In: 391026 
  Total Neighbor information Age outs: 0 
  Total Frames Discarded: 0 
  Total In Error Frames: 0 
  Total Unrecognized TLVs: 782052 
  Total TLVs Discarded: 0 
  Next packet will be sent after 23 seconds
  The neighbors are given below:
  -----------------------------------------------------------------------
 
    Remote Chassis ID Subtype: Mac address (4)
    Remote Chassis ID:  00:24:81:d9:2d:e1
    Remote Port Subtype:  Locally assigned (7)
    Remote Port ID:  19
    Local Port ID: GigabitEthernet 2/38
    Locally assigned remote Neighbor Index: 1
    Remote TTL:  120
    Information valid for next 104 seconds 
    Time since last information change of this neighbor:  19w2d18h
    Remote System Name:  switch30-2
    Remote System Desc:  ProCurve 498358-B21 6120G/XG Blade Switch, revision 
     Z.14.08, ROM Z.14.06 (/sw/code/build/vern(t4br))
    Existing System Capabilities:  Bridge
    Enabled System Capabilities:  Bridge
    MAC PHY Configuration:
      Auto-neg supported: 1
      Auto-neg enabled: 1
      Auto-neg advertised capabilities:
        1000BASE-T full duplex mode,
        100BASE-TX full duplex mode,
        100BASE-TX half duplex mode,
        10BASE-T  full duplex mode,
        10BASE-T  half duplex mode
      Operational MAU type:
        1000BaseTFD: Four-pair Category 5 UTP, full duplex mode
   ---------------------------------------------------------------------------
 
========================================================================
 Local Interface Gi 2/39 has 1 neighbor 
  Total Frames Out: 379226 
  Total Frames In: 391026 
  Total Neighbor information Age outs: 0 
  Total Frames Discarded: 0 
  Total In Error Frames: 0 
  Total Unrecognized TLVs: 782052 
  Total TLVs Discarded: 0 
  Next packet will be sent after 24 seconds
  The neighbors are given below:
  -----------------------------------------------------------------------
 
    Remote Chassis ID Subtype: Mac address (4)
    Remote Chassis ID:  00:24:81:d9:2d:e1
    Remote Port Subtype:  Locally assigned (7)
    Remote Port ID:  20
    Local Port ID: GigabitEthernet 2/39
    Locally assigned remote Neighbor Index: 1
    Remote TTL:  120
    Information valid for next 104 seconds 
    Time since last information change of this neighbor:  19w2d18h
    Remote System Name:  switch30-2
    Remote System Desc:  ProCurve 498358-B21 6120G/XG Blade Switch, revision 
     Z.14.08, ROM Z.14.06 (/sw/code/build/vern(t4br))
    Existing System Capabilities:  Bridge
    Enabled System Capabilities:  Bridge
    MAC PHY Configuration:
      Auto-neg supported: 1
      Auto-neg enabled: 1
      Auto-neg advertised capabilities:
        1000BASE-T full duplex mode,
        100BASE-TX full duplex mode,
        100BASE-TX half duplex mode,
        10BASE-T  full duplex mode,
        10BASE-T  half duplex mode
      Operational MAU type:
        1000BaseTFD: Four-pair Category 5 UTP, full duplex mode
   ---------------------------------------------------------------------------
 
========================================================================
 Local Interface Gi 2/40 has 1 neighbor 
  Total Frames Out: 396270 
  Total Frames In: 408829 
  Total Neighbor information Age outs: 0 
  Total Frames Discarded: 0 
  Total In Error Frames: 0 
  Total Unrecognized TLVs: 817658 
  Total TLVs Discarded: 0 
  Next packet will be sent after 24 seconds
  The neighbors are given below:
  -----------------------------------------------------------------------
 
    Remote Chassis ID Subtype: Mac address (4)
    Remote Chassis ID:  00:24:81:d9:bc:21
    Remote Port Subtype:  Locally assigned (7)
    Remote Port ID:  17
    Local Port ID: GigabitEthernet 2/40
    Locally assigned remote Neighbor Index: 1
    Remote TTL:  120
    Information valid for next 100 seconds 
    Time since last information change of this neighbor:  20w1d22h
    Remote System Name:  switch30-1
    Remote System Desc:  ProCurve 498358-B21 6120G/XG Blade Switch, revision 
     Z.14.08, ROM Z.14.06 (/sw/code/build/vern(t4br))
    Existing System Capabilities:  Bridge
    Enabled System Capabilities:  Bridge
    MAC PHY Configuration:
      Auto-neg supported: 1
      Auto-neg enabled: 1
      Auto-neg advertised capabilities:
        1000BASE-T full duplex mode,
        100BASE-TX full duplex mode,
        100BASE-TX half duplex mode,
        10BASE-T  full duplex mode,
        10BASE-T  half duplex mode
      Operational MAU type:
        1000BaseTFD: Four-pair Category 5 UTP, full duplex mode
   ---------------------------------------------------------------------------
 
========================================================================
 Local Interface Gi 2/41 has 1 neighbor 
  Total Frames Out: 396269 
  Total Frames In: 408829 
  Total Neighbor information Age outs: 0 
  Total Frames Discarded: 0 
  Total In Error Frames: 0 
  Total Unrecognized TLVs: 817658 
  Total TLVs Discarded: 0 
  Next packet will be sent after 1 seconds
  The neighbors are given below:
  -----------------------------------------------------------------------
 
    Remote Chassis ID Subtype: Mac address (4)
    Remote Chassis ID:  00:24:81:d9:bc:21
    Remote Port Subtype:  Locally assigned (7)
    Remote Port ID:  18
    Local Port ID: GigabitEthernet 2/41
    Locally assigned remote Neighbor Index: 1
    Remote TTL:  120
    Information valid for next 108 seconds 
    Time since last information change of this neighbor:  20w1d22h
    Remote System Name:  switch30-1
    Remote System Desc:  ProCurve 498358-B21 6120G/XG Blade Switch, revision 
     Z.14.08, ROM Z.14.06 (/sw/code/build/vern(t4br))
    Existing System Capabilities:  Bridge
    Enabled System Capabilities:  Bridge
    MAC PHY Configuration:
      Auto-neg supported: 1
      Auto-neg enabled: 1
      Auto-neg advertised capabilities:
        1000BASE-T full duplex mode,
        100BASE-TX full duplex mode,
        100BASE-TX half duplex mode,
        10BASE-T  full duplex mode,
        10BASE-T  half duplex mode
      Operational MAU type:
        1000BaseTFD: Four-pair Category 5 UTP, full duplex mode
   ---------------------------------------------------------------------------
 
========================================================================
 Local Interface Gi 2/42 has 1 neighbor 
  Total Frames Out: 396269 
  Total Frames In: 408814 
  Total Neighbor information Age outs: 0 
  Total Frames Discarded: 0 
  Total In Error Frames: 0 
  Total Unrecognized TLVs: 817628 
  Total TLVs Discarded: 0 
  Next packet will be sent after 12 seconds
  The neighbors are given below:
  -----------------------------------------------------------------------
 
    Remote Chassis ID Subtype: Mac address (4)
    Remote Chassis ID:  00:24:81:d9:2d:e1
    Remote Port Subtype:  Locally assigned (7)
    Remote Port ID:  17
    Local Port ID: GigabitEthernet 2/42
    Locally assigned remote Neighbor Index: 1
    Remote TTL:  120
    Information valid for next 120 seconds 
    Time since last information change of this neighbor:  19w2d18h
    Remote System Name:  switch30-2
    Remote System Desc:  ProCurve 498358-B21 6120G/XG Blade Switch, revision 
     Z.14.08, ROM Z.14.06 (/sw/code/build/vern(t4br))
    Existing System Capabilities:  Bridge
    Enabled System Capabilities:  Bridge
    MAC PHY Configuration:
      Auto-neg supported: 1
      Auto-neg enabled: 1
      Auto-neg advertised capabilities:
        1000BASE-T full duplex mode,
        100BASE-TX full duplex mode,
        100BASE-TX half duplex mode,
        10BASE-T  full duplex mode,
        10BASE-T  half duplex mode
      Operational MAU type:
        1000BaseTFD: Four-pair Category 5 UTP, full duplex mode
   ---------------------------------------------------------------------------
 
========================================================================
 Local Interface Gi 2/43 has 1 neighbor 
  Total Frames Out: 396269 
  Total Frames In: 408813 
  Total Neighbor information Age outs: 0 
  Total Frames Discarded: 0 
  Total In Error Frames: 0 
  Total Unrecognized TLVs: 817626 
  Total TLVs Discarded: 0 
  Next packet will be sent after 25 seconds
  The neighbors are given below:
  -----------------------------------------------------------------------
 
    Remote Chassis ID Subtype: Mac address (4)
    Remote Chassis ID:  00:24:81:d9:2d:e1
    Remote Port Subtype:  Locally assigned (7)
    Remote Port ID:  18
    Local Port ID: GigabitEthernet 2/43
    Locally assigned remote Neighbor Index: 1
    Remote TTL:  120
    Information valid for next 120 seconds 
    Time since last information change of this neighbor:  19w2d18h
    Remote System Name:  switch30-2
    Remote System Desc:  ProCurve 498358-B21 6120G/XG Blade Switch, revision 
     Z.14.08, ROM Z.14.06 (/sw/code/build/vern(t4br))
    Existing System Capabilities:  Bridge
    Enabled System Capabilities:  Bridge
    MAC PHY Configuration:
      Auto-neg supported: 1
      Auto-neg enabled: 1
      Auto-neg advertised capabilities:
        1000BASE-T full duplex mode,
        100BASE-TX full duplex mode,
        100BASE-TX half duplex mode,
        10BASE-T  full duplex mode,
        10BASE-T  half duplex mode
      Operational MAU type:
        1000BaseTFD: Four-pair Category 5 UTP, full duplex mode
   ---------------------------------------------------------------------------
 
========================================================================
 Local Interface Te 6/0 has 1 neighbor 
  Total Frames Out: 390416 
  Total Frames In: 387127 
  Total Neighbor information Age outs: 29 
  Total Frames Discarded: 0 
  Total In Error Frames: 0 
  Total Unrecognized TLVs: 0 
  Total TLVs Discarded: 0 
  Next packet will be sent after 1 seconds
  The neighbors are given below:
  -----------------------------------------------------------------------
 
    Remote Chassis ID Subtype: Mac address (4)
    Remote Chassis ID:  00:01:e8:6d:1c:5c
    Remote Port Subtype:  Interface name (5)
    Remote Port ID:  TenGigabitEthernet 1/8
    Local Port ID: TenGigabitEthernet 6/0
    Locally assigned remote Neighbor Index: 30
    Remote TTL:  120
    Information valid for next 113 seconds 
    Time since last information change of this neighbor:  1d10h58m
    Remote System Name:  switch1
    Remote System Desc:  Force10 Networks Real Time Operating System Software
     . Force10 Operating System Version: 1.0. Force10 App
     lication Software Version: 8.3.1.3d. Copyright (c) 1
     999-2010 by Force10 Networks, Inc. Build Time: Mon A
     ug 9 12:57:45 PDT 2010
    Existing System Capabilities:  Repeater Bridge Router
    Enabled System Capabilities:  Repeater Bridge Router
   ---------------------------------------------------------------------------
 
========================================================================
 Local Interface Te 7/0 has 1 neighbor 
  Total Frames Out: 401862 
  Total Frames In: 398411 
  Total Neighbor information Age outs: 11 
  Total Frames Discarded: 0 
  Total In Error Frames: 0 
  Total Unrecognized TLVs: 0 
  Total TLVs Discarded: 0 
  Next packet will be sent after 7 seconds
  The neighbors are given below:
  -----------------------------------------------------------------------
 
    Remote Chassis ID Subtype: Mac address (4)
    Remote Chassis ID:  00:01:e8:6d:1c:5c
    Remote Port Subtype:  Interface name (5)
    Remote Port ID:  TenGigabitEthernet 2/8
    Local Port ID: TenGigabitEthernet 7/0
    Locally assigned remote Neighbor Index: 12
    Remote TTL:  120
    Information valid for next 107 seconds 
    Time since last information change of this neighbor:  5d20h10m
    Remote System Name:  switch1
    Remote System Desc:  Force10 Networks Real Time Operating System Software
     . Force10 Operating System Version: 1.0. Force10 App
     lication Software Version: 8.3.1.3d. Copyright (c) 1
     999-2010 by Force10 Networks, Inc. Build Time: Mon A
     ug 9 12:57:45 PDT 2010
    Existing System Capabilities:  Repeater Bridge Router
    Enabled System Capabilities:  Repeater Bridge Router
   ---------------------------------------------------------------------------
 """,
'terminal length 0':  'terminal length 0\n',
}
    snmp_get={}
    snmp_getnext={}
