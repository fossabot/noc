# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## f5.BIGIP.get_license test
## Auto-generated by manage.py debug-script at 2011-06-07 07:54:55
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------
from noc.lib.test import ScriptTestCase
class f5_BIGIP_get_license_Test(ScriptTestCase):
    script = "f5.BIGIP.get_license"
    vendor = "f5"
    platform = 'BIG-IP'
    version = '10.2.1 297.0'
    input = {}
    result = {'Active Active': True,
 'Address Translation': True,
 'Basic Load Balancing': True,
 'CMP SSL': True,
 'CMP SSL per core': True,
 'CMP compression per core': True,
 'Connection Limits': True,
 'Connection Rebinding': True,
 'Connection Timeout': True,
 'Cookie Persistence': True,
 'DDoS Connection Limits': True,
 'DIAMETER Monitor': True,
 'Dynamic Connection Reaping': True,
 'Dynamic Ratio Load Balancing': True,
 'EAV Monitor': True,
 'FTP': True,
 'FTP Monitor': True,
 'Failover': True,
 'Fast L4': True,
 'Fastest Load Balancing': True,
 'HTTP': True,
 'HTTP Compression': 50,
 'HTTP Content Transformation': True,
 'HTTP Header Transformation': True,
 'HTTP Monitor': True,
 'HTTP Redirection': True,
 'HTTP traffic classifier': True,
 'HTTPS Monitor': True,
 'ICMP Monitor': True,
 'IMAP Monitor': True,
 'IPv6 DNS Support': True,
 'IPv6 Gateway Module': True,
 'Inband Monitor': True,
 'Interface Mirroring': True,
 'L3 Addr Load Balancing': True,
 'L4 iRules': True,
 'L7 iRules': True,
 'LB Pools Maximum Nodes unlimited': True,
 'LDAP Monitor': True,
 'LDAP Over SSL Monitor': True,
 'Last Hop Pool': True,
 'Least Connection Load Balancing': True,
 'Least Sessions Load Balancing': True,
 'Local Traffic Manager': True,
 'Microsoft SQL Monitor': True,
 'Module Score Monitor': True,
 'Monitor Rules': True,
 'Monitors': True,
 'MySQL Monitor': True,
 'NNTP Monitor': True,
 'Network Address Translation': True,
 'Observed Load Balancing': True,
 'OneConnect - Switching and Pooling': True,
 'Oracle Monitor': True,
 'POP3 Monitor': True,
 'PVA Enable': True,
 'Packet Filter': True,
 'Persistence': True,
 'Pool Min Up Members': True,
 'Pools': True,
 'Port Translation': True,
 'PostgreSQL Monitor': True,
 'Predictive Load Balancing': True,
 'Priority FIFO (ToS) Queuing Mode': True,
 'Priority Load Balancing': True,
 'Probe Control - IDS Traffic Management': True,
 'QoS and ToS Tagging': True,
 'RADIUS Monitor': True,
 'RAM Cache': True,
 'RPC Monitor': True,
 'RTSP switching': True,
 'Rate Shaping and Rate Class Support': True,
 'Ratio Load Balancing': True,
 'RealN Monitor': True,
 'Reverse Keyword': True,
 'Round Robin Load Balancing': True,
 'Route Pool': True,
 'SASP Monitor': True,
 'SCRIPTED Monitor': True,
 'SCTP support': True,
 'SIP': True,
 'SIP Monitor': True,
 'SIP Persistence': True,
 'SMB Monitor': True,
 'SMTP Monitor': True,
 'SNAT Standard': True,
 'SNMP Monitor': True,
 'SSL Mbps': 2000,
 'SSL Session ID Persistence': True,
 'SSL Support': True,
 'SSL Total TPS': 500,
 'SSL client certificate authorization via LDAP': True,
 'SYN Check': True,
 'Simple Persistence': True,
 'Soap Monitor': True,
 'Spanning Tree Protocol': True,
 'State Mirroring': True,
 'Sticky Persistence': True,
 'Stochastic Fair Queuing Mode': True,
 'TCP': True,
 'TCP Echo Monitor': True,
 'TCP Half Open Monitor': True,
 'TCP Monitor': True,
 'Traffic Classification L4': True,
 'Traffic Classification iRules+L7': True,
 'Transparent Device Load Balancing': True,
 'Transparent Device Monitor': True,
 'UDP': True,
 'UDP Monitor': True,
 'UDP Packet Load Balancing': True,
 'Universal Persistence': True,
 'User-Defined Statistics': True,
 'VLAN Failsafe': True,
 'Virtual Edition maximum throughput': 1,
 'Virtual Location Monitor': True,
 'WAP Monitor': True,
 'WMI Monitor': True,
 'WTS Persistence': True,
 'Web Logic Load Balancing': True,
 'gateway ICMP Monitor': True,
 'iRules': True,
 'iSNAT - Rules Referencing SNAT Pools': True,
 'iSession': True}
    motd = 'Last login: Tue Jun  7 03:54:21 2011 from 10.11.106.51\n'
    cli = {
## 'b version'
'b version': """b version
Kernel:
Linux 2.6.18-164.11.1.el5.1.0.f5app
Package:
BIG-IP Version 10.2.1 297.0
Final Edition

Enabled Features:
Rate Shaping and Rate Class Support     
Traffic Classification L4               
Traffic Classification iRules+L7        
Stochastic Fair Queuing Mode            
Priority FIFO (ToS) Queuing Mode        
QoS and ToS Tagging                     
Connection Limits                       
OneConnect - Switching and Pooling      
Connection Rebinding                    
Connection Timeout                      
Route Pool                              
Last Hop Pool                           
Active Active                           
Failover                                
Pool Min Up Members                     
State Mirroring                         
VLAN Failsafe                           
HTTP traffic classifier                 
iSession                                
iSNAT - Rules Referencing SNAT Pools    
Basic Load Balancing                    
Dynamic Ratio Load Balancing            
Fastest Load Balancing                  
L3 Addr Load Balancing                  
Least Connection Load Balancing         
Least Sessions Load Balancing           
Observed Load Balancing                 
LB Pools Maximum Nodes unlimited        
Predictive Load Balancing               
Priority Load Balancing                 
Ratio Load Balancing                    
Round Robin Load Balancing              
UDP Packet Load Balancing               
Web Logic Load Balancing                
DIAMETER Monitor                        
EAV Monitor                             
FTP Monitor                             
gateway ICMP Monitor                    
HTTP Monitor                            
HTTPS Monitor                           
ICMP Monitor                            
IMAP Monitor                            
Inband Monitor                          
LDAP Monitor                            
LDAP Over SSL Monitor                   
Module Score Monitor                    
Microsoft SQL Monitor                   
MySQL Monitor                           
NNTP Monitor                            
Oracle Monitor                          
POP3 Monitor                            
PostgreSQL Monitor                      
RADIUS Monitor                          
RealN Monitor                           
Reverse Keyword                         
RPC Monitor                             
Monitor Rules                           
SASP Monitor                            
SCRIPTED Monitor                        
SIP Monitor                             
SMB Monitor                             
SMTP Monitor                            
SNMP Monitor                            
Soap Monitor                            
TCP Monitor                             
TCP Echo Monitor                        
TCP Half Open Monitor                   
Transparent Device Monitor              
UDP Monitor                             
Virtual Location Monitor                
WAP Monitor                             
WMI Monitor                             
Monitors                                
Network Address Translation             
Persistence                             
Cookie Persistence                      
Simple Persistence                      
SIP Persistence                         
SSL Session ID Persistence              
Sticky Persistence                      
Universal Persistence                   
WTS Persistence                         
Pools                                   
HTTP Content Transformation             
Fast L4                                 
FTP                                     
HTTP Header Transformation              
HTTP                                    
Probe Control - IDS Traffic Management  
HTTP Redirection                        
SIP                                     
TCP                                     
UDP                                     
RAM Cache                               
RTSP switching                          
L4 iRules                               
L7 iRules                               
User-Defined Statistics                 
iRules                                  
SCTP support                            
SNAT Standard                           
Address Translation                     
Port Translation                        
Transparent Device Load Balancing       
Local Traffic Manager                   
IPv6 DNS Support                        
IPv6 Gateway Module                     
Interface Mirroring                     
Spanning Tree Protocol                  
PVA Enable                              
SSL Mbps 2000                           
CMP SSL                                 
CMP SSL per core                        
SSL Total TPS 500                       
Virtual Edition maximum throughput 1    
CMP compression per core                
HTTP Compression 50                     
SSL client certificate authorization via LDAP
DDoS Connection Limits                  
Dynamic Connection Reaping              
Packet Filter                           
SYN Check                               
SSL Support                             """, 
}
    snmp_get = {}
    snmp_getnext = {}
