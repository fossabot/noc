# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Linksys.VoIP.get_config test
## Auto-generated by ./noc debug-script at 2012-01-16 14:19:21
##----------------------------------------------------------------------
## Copyright (C) 2007-2012 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.lib.test import ScriptTestCase


class Linksys_VoIP_get_config_Test(ScriptTestCase):
    script = "Linksys.VoIP.get_config"
    vendor = "Linksys"
    platform = 'SPA8000'
    version = '6.1.10(001)'
    input = {}
    result = 'Network\nVoice\nStatusWan StatusTrunk Status                    Admin Login                     &nbspbasic |                     advanced\nProduct Information\nProduct Name:SPA8000Serial Number:CQH01K806280\nSoftware Version:6.1.10(001)Hardware Version:1.0.0\nMAC Address:687F7459788CClient Certificate:Installed\nCustomization:Open\nSystem Status\nWan Connection Type:Static IPCurrent IP:10.8.27.16\nHost Name:SipuraSPADomain:\nCurrent Netmask:255.255.255.0Current Gateway:10.8.27.1\nPrimary  DNS:80.237.81.250\nSecondary  DNS:62.33.189.250 \nLAN IP Address:10.8.28.1Broadcast Pkts Sent:529\nInternet Connection Settings\nConnection Type:DHCPStatic IPPPPOEPPPOE,DHCPDHCP,PPPOE\nStatic IP:NetMask:\nGateway:\nPPPOE Login Name:PPPOE Login Password:\nHostName:Domain:\nPrimary DNS:Secondary DNS: \r\nTrunk Status                    Admin Login                     &nbspbasic |                     advanced\nCopyright  1992-2009 Cisco Systems, Inc. All Rights Reserved.'
    motd = ''
    cli = {
}
    snmp_get = {}
    snmp_getnext = {}
    http_get = {'/': '<html>\n<style>\ntable.menu1 td {\n  font-family:\tVerdana, Geneva, sans-serif;\n  font-size : 13px;\n  border: 0px solid;\n  color: blue;\n  white-space: nowrap;\n}\ntable.menu1 td a {\n color: darkblue;\n text-decoration:\tnone;\n cursor: hand;\n}\ntable.stat th, table.stat td {\n  font-family:\tVerdana, Geneva, sans-serif;\n  font-size : 11px;\n  color: blue;\n  border: 0px solid;\n  white-space: nowrap;\n}\n.inputw{\n  font-family:\tVerdana, Geneva, sans-serif;\n  font-size : 11px;\n  border : 0px;\n  color : darkblue;\n}\n\n.inputc {\n  font-family:\tVerdana, Geneva, sans-serif;\n  font-size : 11px;\n  border : 0px;\n  color : darkblue;\n}\n\n.swalft {\n  font-family : Arial;\n  font-size : 9px;\n  color : blue;\n}\n\n.swdlft {\n  font-family : Arial;\n  font-size : 9px;\n  color : black;\n}\n\n.labelft {\n  font-family:\tVerdana, Geneva, sans-serif;\n  font-size : 12px;\n  color : #990000;\n}\n\n.cpft {\n  font-family : Arial;\n  font-size : 9px;\n  color : black;\n}\n\n.navbar .tab {\n\tfont-family:\tVerdana, Geneva, sans-serif;\n\tfont-size:\t\t12px;\n\tdisplay:\t\tinline;\n\tmargin:\t\t\t1px -5px 1px 5px;\n\tfloat:\t\t\tleft;\n\tpadding:\t\t3px 4px 3px 4px;\n\tbackground:\t\trgb(234,242,255);\n\tborder:\t\t\t1px solid;\n\tborder-color:\trgb(120,172,255);\n\tborder-left:\t0;\n\tborder-bottom:\t0;\n\tborder-top:\t\t0;\n\t\n\tz-index:\t\t1;\n\tposition:\t\trelative;\n\ttop:\t\t\t0;\n\tfont-weight:\tnormal;\n}\n.navbar .tab.selected {\n\tborder:\t\t\t1px solid rgb(120,172,255);\n\tborder-bottom:\t0;\n\tz-index:\t\t3;\n\tpadding:\t\t2px 3px 12px 3px;\n\tmargin:\t\t\t1px -6px -2px 0px;\n\ttop:\t\t\t-2px;\n\tbackground:\t\twhite;\n\tfont-weight:\tbold;\n}\n.navbar .tab a {\n\tfont-family:\tVerdana, Geneva, sans-serif;\n\tfont-size:\t\t\t13px;\n\tcolor:\t\t\t\trgb(153,0,0);\n\ttext-decoration:\tnone;\n\tcursor:\t\t\t    hand;\n}\n.navbar .hover a {\n\tcolor:\trgb(0,73,150);\n}\n.tab-page {\n\tclear:\t\t\tboth;\n\tborder:\t\t\t1px solid rgb(120,172,255);\n\tbackground:\t\tWhite;\n\tz-index:\t\t2;\n\tposition:\t\trelative;\n\ttop:\t\t\t-2px;\n\tcolor:\t\t\tBlue;\n\tfont-family:\tVerdana, Geneva, sans-serif;\n\tfont-size:\t\t11px;\n\tpadding:\t\t0px;\n\twidth:\t\t\t100%;\n}\n.navbar {\n\tz-index:\t\t1;\n\twhite-space:\tnowrap;\n\tbackground:\t\trgb(234,242,255);\n\theight:\t\t\t30px;\n\twidth:\t\t\t100%;\n}\n</style>\n\n<script type="text/javascript">\nvar check = false; \nvar currentPage = null;\nvar ns4 = false;\nvar ie4 = false;\nvar dom = false;\nvar hideStr = "";\nvar showStr = "";\n\nfunction init() \n{\n  styleStr=".style.display";\n  hideStr="=\'none\'";\n  showStr="=\'block\'";\n  check = true; \n  if (document.getElementById){\n    dom = true;\n  }\n  else if (document.all){\n    ie4 = true;\n  }\n  else if (document.layers) {  \n    ns4 = true;\n    styleStr=".visibility";  \n    hideStr="=\'hide\'";\n    showStr="=\'show\'";\n  }\n  else check=false;\n}\n\nfunction getAllTags(tags)\n{\n  if (check){\n    if (document.getElementsByTagName)\n      return document.getElementsByTagName(tags);\n    if (document.document.all)\n      return document.all.tags(tags);\n    if (document.layers)\n      return document.lalyers;\n    if (document.divs)\n      return document.divs;\n  }\n  return null;\n}\n\nfunction getElement(tabName)\n{\n  if (check){\n    if (dom)\n      return document.getElementById(tabName);\n    if (ie4)\n      return document.all[tabName];  \n    if (ns4)\n      return document.layers[tabName];\n  }\n  return null; \n}\n\n\nfunction onMouseOver(tabName)\n{\n  var el;\n\n  el = getElement("nav"+tabName);\n  if (el==null)\n    return;\n\n  el.className = el.className + " hover";\n}\n\nfunction onMouseOut(tabName)\n{\n  var el;\n\n  el = getElement("nav"+tabName);\n  if (el==null)\n    return;\n  \n  el.className = el.className.replace(/ hover/g, "");\n}\n\nfunction showTab(tabName)\n{\n  var el;\n\n  el = getElement(tabName);\n  if (el==null)\n    return;\n\t\n  eval("el"+styleStr+showStr);\n\n  el = getElement("nav"+tabName);\n  if (el==null)\n    return;\n\n  el.className = el.className.replace(/tab/g, "tab selected");\n}\nfunction hideTab(tabName) \n{\n  var el;\n\n  el = getElement(tabName);\n  if (el==null)\n    return;\n\t\n  eval("el"+styleStr+hideStr);\n\n  el = getElement("nav"+tabName);\n  if (el==null)\n    return;\n\n  el.className = el.className.replace(/ selected/g, "");\n}\nfunction switchPage(newpage) \n{\n  if (currentPage!=null)\n\thideTab(currentPage);\n  currentPage=newpage;\n  showTab(newpage);\n}\nfunction hideOthers()\n{\n  var all; \n  var i;\n  var first=1;\n\n  all = getAllTags("div");\n  if (all==null)\n    return;\n  for (i=0; i<all.length; i++){\n    if (all[i].className=="tab-page"){\n      if (first==1){\n\t    first=0;\n        switchPage(all[i].id);\n      }\n\t  else eval("all[i]"+styleStr+hideStr);\n    }\n  }\n}\n\nfunction onLoad()\n{\n  init();\n  hideOthers();\n}\n</script>\n\n  <head>\n    <title>Cisco SPA Configuration</title>\r\n  </head>\n  <body>\n    <center>\n<form action="bsipura.spa" method="POST">\n      <table border="0"  bgcolor="white" cellpadding="0" cellspacing="0" width="700">\n        <tr> <td align="right" valign="middle">\n<a href="http://www.myciscocommunity.com/community/smallbizsupport" target="linksys">\n<img width="100%" height=95 src="/spabanner.jpg" border="0" alt="Cisco-Linksys, LLC">\n<tr bgcolor=#eaf2ff><td>\n  \n\r<TABLE class="menu1" height="25" cellSpacing=0 cellPadding=0 width=100% bgColor=white border=0><TR align=center>\n<td width=130 bgColor=#eaf2ff><B>Network</B><TD width=1 bgColor=#808080><IMG height=1 alt="" width=1></TD><TD width=1 bgColor=#ffffff><IMG height=1 alt="" width=1></TD>\n<td width=130 bgColor=#cfcfcf><a href=voice/>Voice</a>\n<TD width=1 bgColor=#808080><IMG height=1 alt="" width=1></TD><TD width=1 bgColor=#ffffff><IMG height=1 alt="" width=1></TD>\n<td bgColor=#cfcfcf width=436>&nbsp;</table>\n<div class="navbar"><h2 class="tab" id="navStatus" onclick="switchPage(\'Status\');"><a href="#" onmouseover="onMouseOver(\'Status\');" onmouseout="onMouseOut(\'Status\');" onclick="return false;">Status</a></h2><h2 class="tab" id="navWan Status" onclick="switchPage(\'Wan Status\');"><a href="#" onmouseover="onMouseOver(\'Wan Status\');" onmouseout="onMouseOut(\'Wan Status\');" onclick="return false;">Wan Status</a></h2><p align=right><a href="/status"><font class="swalft">Trunk Status</font></a><br>                    <a href="/admin/"><font class="swalft">Admin Login</font></a>                    <font class="swdlft">&nbsp;&nbsp</font><font class="swdlft">basic&nbsp;|&nbsp;                    </font><a href="advanced"><font class="swalft">advanced</font></a></p></div>\n<tr><td>  \n<div class="tab-page" id="Status"><BR><table class="stat" cellpadding="1px" cellspacing="0" width="100%">\n<COLGROUP>\n<COL width=26% align="left"> \n<COL align="left"> \n<COL width=26% align="left"> \n<COL align="left"></COLGROUP>\n<tr bgcolor="#d3d3d3"><td colspan="4">&nbsp;\n<tr bgcolor="#d3d3d3"><td align="left" colspan="4"><font class="labelft">Product Information</font>\n<tr bgcolor="#dcdcdc"><td>Product Name:<td><font color="darkblue">SPA8000</font><td>Serial Number:<td><font color="darkblue">CQH01K806280</font>\n<tr bgcolor="#d3d3d3"><td>Software Version:<td><font color="darkblue">6.1.10(001)</font><td>Hardware Version:<td><font color="darkblue">1.0.0</font>\n<tr bgcolor="#dcdcdc"><td>MAC Address:<td><font color="darkblue">687F7459788C</font><td>Client Certificate:<td><font color="darkblue">Installed</font>\n<tr bgcolor="#d3d3d3"><td>Customization:<td><font color="darkblue">Open</font><td><td>\n<tr bgcolor="#dcdcdc"><td colspan="4">&nbsp;\n<tr bgcolor="#dcdcdc"><td align="left" colspan="4"><font class="labelft">System Status</font>\n<tr bgcolor="#d3d3d3"><td>Current Time:<td><font color="darkblue">1/15/2012 20:20:05</font><td>Elapsed Time:<td><font color="darkblue">35 days and 00:09:29</font>\n<tr bgcolor="#dcdcdc"><td>Wan Connection Type:<td><font color="darkblue">Static IP</font><td>Current IP:<td><font color="darkblue">10.8.27.16</font>\n<tr bgcolor="#d3d3d3"><td>Host Name:<td><font color="darkblue">SipuraSPA</font><td>Domain:<td><font color="darkblue"></font>\n<tr bgcolor="#dcdcdc"><td>Current Netmask:<td><font color="darkblue">255.255.255.0</font><td>Current Gateway:<td><font color="darkblue">10.8.27.1</font>\n<tr bgcolor="#d3d3d3"><td>Primary  DNS:<td><font color="darkblue">80.237.81.250</font><td><td>\n<tr bgcolor="#dcdcdc"><td>Secondary  DNS:<td colspan="3"><font color="darkblue">62.33.189.250 </font>\n<tr bgcolor="#d3d3d3"><td>LAN IP Address:<td><font color="darkblue">10.8.28.1</font><td>Broadcast Pkts Sent:<td><font color="darkblue">529</font>\n<tr bgcolor="#dcdcdc"><td>Broadcast Bytes Sent:<td><font color="darkblue">180933</font><td>Broadcast Pkts Recv:<td><font color="darkblue">1290478</font>\n<tr bgcolor="#d3d3d3"><td>Broadcast Bytes Recv:<td><font color="darkblue">196523901</font><td>Broadcast Pkts Dropped:<td><font color="darkblue">0</font>\n<tr bgcolor="#dcdcdc"><td>Broadcast Bytes Dropped:<td><font color="darkblue">0</font><td>WAN Link Status:<td><font color="darkblue">100 Full-duplex</font></table> </div>\r\n<div class="tab-page" id="Wan Status"><BR><table class="stat" cellpadding="1px" cellspacing="0" width="100%">\n<COLGROUP>\n<COL width=26% align="left"> \n<COL align="left"> \n<COL width=26% align="left"> \n<COL align="left"></COLGROUP>\n<tr bgcolor="#d3d3d3"><td colspan="4">&nbsp;\n<tr bgcolor="#d3d3d3"><td align="left" colspan="4"><font class="labelft">Internet Connection Settings</font>\n<tr bgcolor="#dcdcdc"><td>Connection Type:<td colspan="3"><select class="inputc" name="29292"><option value="DHCP" >DHCP</option><option value="Static IP" selected>Static IP</option><option value="PPPOE" >PPPOE</option><option value="PPPOE,DHCP" >PPPOE,DHCP</option><option value="DHCP,PPPOE" >DHCP,PPPOE</option></select>\n<tr bgcolor="#d3d3d3"><td colspan="4">&nbsp;\n<tr bgcolor="#d3d3d3"><td align="left" colspan="4"><font class="labelft"> Static IP Settings</font>\n<tr bgcolor="#dcdcdc"><td>Static IP:<td><input class="inputc" size="20" name="30639" value="10.8.27.16" maxlength=2047><td>NetMask:<td><input class="inputc" size="20" name="29807" value="255.255.255.0" maxlength=2047>\n<tr bgcolor="#d3d3d3"><td>Gateway:<td><input class="inputw" size="20" name="29743" value="10.8.27.1" maxlength=2047><td><td>\n<tr bgcolor="#dcdcdc"><td colspan="4">&nbsp;\n<tr bgcolor="#dcdcdc"><td align="left" colspan="4"><font class="labelft"> PPPoE Settings</font>\n<tr bgcolor="#d3d3d3"><td>PPPOE Login Name:<td><input class="inputw" size="20" name="29228" value="" maxlength=2047><td>PPPOE Login Password:<td><input class="inputw" size="20" name="P29420" value="" maxlength=255>\n<tr bgcolor="#dcdcdc"><td colspan="4">&nbsp;\n<tr bgcolor="#dcdcdc"><td align="left" colspan="4"><font class="labelft"> Optional Settings</font>\n<tr bgcolor="#d3d3d3"><td>HostName:<td><input class="inputw" size="20" name="30255" value="" maxlength=2047><td>Domain:<td><input class="inputw" size="20" name="30447" value="" maxlength=2047>\n<tr bgcolor="#dcdcdc"><td>Primary DNS:<td><input class="inputc" size="20" name="29935" value="80.237.81.250" maxlength=2047><td>Secondary DNS:<td><input class="inputc" size="20" name="29871" value="62.33.189.250" maxlength=2047></table> </div>\r\n\n<tr><td>\n<table width="100%">\n<tr><td align=right>\n<input type="reset" value="Undo All Changes">&nbsp;\n<td align=left>&nbsp;<input type="submit" value="Submit All Changes">\n</table>\n<tr><td align="left">\n<a href="/status"><font class="swalft">Trunk Status</font></a><br>                    <a href="/admin/"><font class="swalft">Admin Login</font></a>                    <font class="swdlft">&nbsp;&nbsp</font><font class="swdlft">basic&nbsp;|&nbsp;                    </font><a href="advanced"><font class="swalft">advanced</font></a>\n<tr><td align="center"> <p class="cpft"><br><br>\nCopyright \xa9 1992-2009 Cisco Systems, Inc. All Rights Reserved.</p>\n      </table>\n     </form>\n    </center>\n  </body>\n<script type="text/javascript">\nonLoad();\n</script>\n</html>\n'}
