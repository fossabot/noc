# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Huawei.VRP.get_interface_status test
## Auto-generated by manage.py debug-script at 2011-03-11 13:47:19
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
from noc.lib.test import ScriptTestCase
class Huawei_VRP_get_interface_status_Test(ScriptTestCase):
    script="Huawei.VRP.get_interface_status"
    vendor="Huawei"
    platform='NE40E'
    version='5.50'
    input={}
    result=[{'interface': 'Aux0/0/1', 'status': False},
 {'interface': 'Eth-Trunk1', 'status': False},
 {'interface': 'Eth-Trunk2', 'status': True},
 {'interface': 'GigabitEthernet1/0/6', 'status': True},
 {'interface': 'Eth-Trunk2.2007', 'status': True},
 {'interface': 'Eth-Trunk3', 'status': True},
 {'interface': 'GigabitEthernet1/0/1', 'status': True},
 {'interface': 'GigabitEthernet1/0/2', 'status': True},
 {'interface': 'GigabitEthernet1/0/3', 'status': True},
 {'interface': 'GigabitEthernet1/0/4', 'status': True},
 {'interface': 'Eth-Trunk4', 'status': True},
 {'interface': 'GigabitEthernet1/0/7', 'status': True},
 {'interface': 'GigabitEthernet1/0/8', 'status': True},
 {'interface': 'GigabitEthernet1/0/9', 'status': True},
 {'interface': 'GigabitEthernet0/0/0', 'status': False},
 {'interface': 'GigabitEthernet1/0/0', 'status': True},
 {'interface': 'GigabitEthernet1/0/5', 'status': False},
 {'interface': 'GigabitEthernet2/0/0(10G)', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.5', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.64', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.107', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.109', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.112', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.121', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.150', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.240', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.497', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.504', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.628', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.706', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.822', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.826', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.827', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.850', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.851', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.866', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.867', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.901', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.2000', 'status': True},
 {'interface': 'GigabitEthernet2/0/0.2500', 'status': True},
 {'interface': 'LoopBack0', 'status': True},
 {'interface': 'NULL0', 'status': True},
 {'interface': 'Vlanif64', 'status': True}]
    motd='\nInfo: The max number of VTY users is 10, and the number\n      of current VTY users on line is 1.\n'
    cli={
## 'display interface brief'
'display interface brief': """display interface brief
PHY: Physical
*down: administratively down
^down: standby
(l): loopback
(s): spoofing
(b): BFD down
(d): Dampening Suppressed
InUti/OutUti: input utility/output utility
Interface                   PHY   Protocol InUti OutUti   inErrors  outErrors
Aux0/0/1                    down  down        0%     0%          0          0
Eth-Trunk1                  down  down        0%     0%          0          0
Eth-Trunk2                  up    down        8%    18%          0          0
  GigabitEthernet1/0/6      up    up          8%    18%          0          0
Eth-Trunk2.2007             up    up          0%     0%          0          0
Eth-Trunk3                  up    --         48%    36%          0          0
  GigabitEthernet1/0/1      up    down       48%    40%          0          0
  GigabitEthernet1/0/2      up    down       51%    32%          0          0
  GigabitEthernet1/0/3      up    down       48%    37%          0          0
  GigabitEthernet1/0/4      up    down       45%    35%          0          0
Eth-Trunk4                  up    --       0.01%  0.01%          0          0
  GigabitEthernet1/0/7      up    down     0.01%  0.01%          0          0
  GigabitEthernet1/0/8      up    down     0.01%  0.01%          0          0
  GigabitEthernet1/0/9      up    down     0.01%  0.01%          0          0
GigabitEthernet0/0/0        down  down        0%     0%          0          0
GigabitEthernet1/0/0        up    up          0%  0.01%       2085          0
GigabitEthernet1/0/5        down  down        0%     0%          0          0
GigabitEthernet2/0/0(10G)   up    down       16%    20%          2          0
GigabitEthernet2/0/0.5      up    up          0%     0%          0          0
GigabitEthernet2/0/0.64     up    down        0%     0%          0          0
GigabitEthernet2/0/0.107    up    down        0%     0%          0          0
GigabitEthernet2/0/0.109    up    up          0%     0%          0          0
GigabitEthernet2/0/0.112    up    down        0%     0%          0          0
GigabitEthernet2/0/0.121    up    up          0%     0%          0          0
GigabitEthernet2/0/0.150    up    up          0%     0%          0          0
GigabitEthernet2/0/0.240    up    up          0%     0%          0          0
GigabitEthernet2/0/0.497    up    up          0%     0%          0          0
GigabitEthernet2/0/0.504    up    up          0%     0%          0          0
GigabitEthernet2/0/0.628    up    up          0%     0%          0          0
GigabitEthernet2/0/0.706    up    down        0%     0%          0          0
GigabitEthernet2/0/0.822    up    down        0%     0%          0          0
GigabitEthernet2/0/0.826    up    up       0.01%    19%          0          0
GigabitEthernet2/0/0.827    up    up          1%  0.01%          0          0
GigabitEthernet2/0/0.850    up    up       0.01%  0.01%          0          0
GigabitEthernet2/0/0.851    up    up       0.01%  0.01%          0          0
GigabitEthernet2/0/0.866    up    up         14%  0.01%          0          0
GigabitEthernet2/0/0.867    up    up       0.01%  0.01%          0          0
GigabitEthernet2/0/0.901    up    up       0.01%  0.01%          0          0
GigabitEthernet2/0/0.2000   up    up          0%     0%          0          0
GigabitEthernet2/0/0.2500   up    up          0%     0%          0          0
LoopBack0                   up    up(s)       0%     0%          0          0
NULL0                       up    up(s)       0%     0%          0          0
Vlanif64                    up    up          --     --          0          0""",
'screen-length 0 temporary':  'screen-length 0 temporary\nInfo: The configuration takes effect on the current user terminal interface only.\n',
## 'display version'
'display version': """display version
Huawei Versatile Routing Platform Software
VRP (R) software, Version 5.50 (V300R003C02B608)
Copyright (C) 2000-2008 Huawei Technologies Co., Ltd.
Quidway NetEngine 40E uptime is 716 days, 1 hour, 51 minutes
  
BKP 0 version information:
  1. PCB      Version : CR52BKPB REV A
  2. MPU Slot Quantity: 0
  3. SRU Slot Quantity: 2
  4. SFU Slot Quantity: 2
  5. LPU Slot Quantity: 8
  
MPU  9(Master) : uptime is 716 days, 1 hour, 51 minutes
                 StartupTime   2009/03/25   17:00:50 
  SDRAM Memory Size   : 2048M bytes  
  Flash Memory Size   : 32M  bytes 
  NVRAM Memory Size   : 512K bytes
  CF Card1 Memory Size: 487M bytes 
  CF Card2 Memory Size: 489M bytes 
  MPU version information: 
  1. PCB      Version : CR52SRUA REV C
  2. EPLD1    Version : 106
  3. EPLD2    Version : 108
  4. FPGA     Version : 009
  5. BootROM  Version : 74.0
  6. BootLoad Version : 216.0
  7. Software Version : Version 5.50 RELEASE 0041
  MIF version information: 
  1. PCB      Version : CR52MIFB REV C
  2. FPGA     Version : 009
  MonitorBUS version information: 
  1. PCB      Version : CR31MBSA REV A
  2. EPLD     Version : 019
  3. Software Version : 3.8
  
MPU 10(Slave)  : uptime is 716 days, 1 hour, 49 minutes
                 StartupTime   2009/03/25   17:01:27 
  SDRAM Memory Size   : 2048M bytes  
  Flash Memory Size   : 32M  bytes 
  NVRAM Memory Size   : 512K bytes
  CF Card1 Memory Size: 487M bytes 
  CF Card2 Memory Size: 489M bytes 
  MPU version information: 
  1. PCB      Version : CR52SRUA REV C
  2. EPLD1    Version : 106
  3. EPLD2    Version : 108
  4. FPGA     Version : 009
  5. BootROM  Version : 74.0
  6. BootLoad Version : 216.0
  7. Software Version : Version 5.50 RELEASE 0041
  MIF version information: 
  1. PCB      Version : CR52MIFB REV C
  2. FPGA     Version : 009
  MonitorBUS version information: 
  1. PCB      Version : CR31MBSA REV A
  2. EPLD     Version : 019
  3. Software Version : 3.8
  
LPU 1  : uptime is 716 days, 1 hour, 48 minutes
         StartupTime   2009/03/25   17:04:12 
  Host    processor :
  1. SDRAM Memory Size:  512M  bytes
  2. Flash Memory Size:   32M  bytes
  LPU version information:
  1. PCB      Version : CR52LPUG REV E
  2. EPLD     Version : 009
  3. NP       Version : 010
  4. BootROM  Version : 71.0
  5. BootLoad Version : 223.0
  6. FSU\t     Version : Version 2.1 RELEASE 0372
  7. EFU\t     Version : Version 23.0 RELEASE 0372
  TCM version information:
  1. PCB      Version : CR52TCMH REV A
  FAD version information:
  1. PCB      Version : CR52FADD REV C
  2. EPLD     Version : 005
  3. FPGA1    Version : 5191
  4. FPGA2    Version : 5191
  5. FPGA3    Version : 181
  LPC version information:
  1. PCB      Version : CR52LPCA REV B
  2. EPLD     Version : 000
  MonitorBUS version information:
  1. PCB      Version : CR31MBSA REV A
  2. EPLD     Version : 019
  3. Software Version : 3.8
  PIC0's version information:
  1. PCB      Version : CR52EAGF REV A
  2. EPLD     Version : 004
  
LPU 2  : uptime is 623 days, 4 hours, 29 minutes
         StartupTime   2009/06/26   10:25:38 
  Host    processor :
  1. SDRAM Memory Size: 1024M  bytes
  2. Flash Memory Size:   32M  bytes
  LPU version information:
  1. PCB      Version : CR52LPUK REV B
  2. EPLD     Version : 302
  3. EPLD2    Version : 300
  4. BootROM  Version : 11.0
  5. BootLoad Version : 52.0
  6. FSU\t     Version : Version 2.1 RELEASE 0372
  7. ASE      Version : 103
  8. LOAMNET  Version : 215
  9. PE       Version : 320
  MonitorBUS version information:
  1. PCB      Version : CR31MBSA REV A
  2. EPLD     Version : 019
  3. Software Version : 3.8
  PIC0's version information:
  1. PCB      Version : CR52L1XX REV A
  2. EPLD     Version : 201
  
SPU 8  : uptime is 611 days, 2 hours, 7 minutes
         StartupTime   2009/07/08   12:47:33 
  Host    processor :
  1. SDRAM Memory Size:  512M  bytes
  2. Flash Memory Size:   16M  bytes
  NP-1 processor :
  1. SDRAM Memory Size:   64M  bytes
  2. Flash Memory Size:   16M  bytes
  NP-1 version information:
  1. PCB      Version : CR01SPU REV A
  2. EPLD     Version : 010
  3. BootROM  Version : 2.0
  4. BootLoad Version : 8.0
  5. FSU\t     Version : Version 3.0 RELEASE 0152
  FAD version information:
  1. PCB      Version : CR52FADA REV B
  2. EPLD     Version : 107
  3. BootROM  Version : 64.0
  4. BootLoad Version : 70.0
  5. FSU\t     Version : Version 3.0 RELEASE 0338
  6. EFU\t     Version : Version 2.37 RELEASE 0338
  7. RIC EPLD Version : 050
  8. CP PCB   Version : RS01HPMB REV C
  9. CP EPLD  Version : 006
  MonitorBUS version information:
  1. PCB      Version : CR31MBSA REV A
  2. EPLD     Version : 019
  3. Software Version : 3.8

SFU 11 : uptime is 234 days, 9 hours, 2 minutes
         StartupTime   2010/07/20   05:49:12 
  SDRAM Memory Size   :  32M bytes
  Flash Memory Size   :   8M bytes
  PCB         Version : CR52SFUD REV C
  EPLD        Version : 004
  BootROM     Version : 68.0
  BootLoad    Version : 80.0
  Software    Version : Version 2.0 RELEASE 0033
  MonitorBUS version information:
  1. PCB      Version : CR31MBSA REV A
  2. EPLD     Version : 019
  3. Software Version : 3.8

SFU 12 : uptime is 716 days, 1 hour, 49 minutes
         StartupTime   2009/03/25   17:02:40 
  SDRAM Memory Size   :  32M bytes
  Flash Memory Size   :   8M bytes
  PCB         Version : CR52SFUD REV C
  EPLD        Version : 004
  BootROM     Version : 68.0
  BootLoad    Version : 80.0
  Software    Version : Version 2.0 RELEASE 0033
  MonitorBUS version information:
  1. PCB      Version : CR31MBSA REV A
  2. EPLD     Version : 019
  3. Software Version : 3.8

SFU 13 : uptime is 716 days, 1 hour, 49 minutes
         StartupTime   2009/03/25   17:02:39 
  SDRAM Memory Size   :  32M bytes
  Flash Memory Size   :   8M bytes
  PCB         Version : CR52SRUA REV C
  EPLD        Version : 103
  BootROM     Version : 68.0
  BootLoad    Version : 80.0
  Software    Version : Version 2.0 RELEASE 0033
  MonitorBUS version information:
  1. PCB      Version : CR31MBSA REV A
  2. EPLD     Version : 019
  3. Software Version : 3.8

SFU 14 : uptime is 716 days, 1 hour, 49 minutes
         StartupTime   2009/03/25   17:02:39 
  SDRAM Memory Size   :  32M bytes
  Flash Memory Size   :   8M bytes
  PCB         Version : CR52SRUA REV C
  EPLD        Version : 103
  BootROM     Version : 68.0
  BootLoad    Version : 80.0
  Software    Version : Version 2.0 RELEASE 0033
  MonitorBUS version information:
  1. PCB      Version : CR31MBSA REV A
  2. EPLD     Version : 019
  3. Software Version : 3.8
  
CLK 15 : uptime is 716 days, 1 hour, 51 minutes
         StartupTime   2009/03/25   17:01:05 
  1. PCB      Version : CR52CLKA REV B
  2. EPLD     Version : 016
  3. Software version : 021
  
CLK 16 : uptime is 716 days, 1 hour, 49 minutes
         StartupTime   2009/03/25   17:02:25 
  1. PCB      Version : CR52CLKA REV B
  2. EPLD     Version : 016
  3. Software version : 021
  
Fan19's MonitorBUS version information:
  PCB         Version : CR52FCBB REV B
  Software    Version : 1.1
""",
}
    snmp_get={}
    snmp_getnext={}
