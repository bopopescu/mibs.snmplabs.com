#
# PySNMP MIB module HH3C-DHCPSNOOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-DHCPSNOOP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:26:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hh3cdot1qVlanIndex, = mibBuilder.importSymbols("HH3C-LswVLAN-MIB", "hh3cdot1qVlanIndex")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, Counter32, ObjectIdentity, Bits, TimeTicks, ModuleIdentity, Gauge32, iso, NotificationType, Unsigned32, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "Counter32", "ObjectIdentity", "Bits", "TimeTicks", "ModuleIdentity", "Gauge32", "iso", "NotificationType", "Unsigned32", "MibIdentifier", "Integer32")
MacAddress, TruthValue, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TruthValue", "DisplayString", "TextualConvention", "RowStatus")
hh3cDhcpSnoop = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 36))
if mibBuilder.loadTexts: hh3cDhcpSnoop.setLastUpdated('200501140000Z')
if mibBuilder.loadTexts: hh3cDhcpSnoop.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cDhcpSnoop.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cDhcpSnoop.setDescription('The private MIB file includes the DHCP Snooping profile.')
hh3cDhcpSnoopMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1))
hh3cDhcpSnoopEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoopEnable.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSnoopEnable.setDescription('DHCP Snooping status (enable or disable).')
hh3cDhcpSnoopTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2), )
if mibBuilder.loadTexts: hh3cDhcpSnoopTable.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSnoopTable.setDescription("The table containing information of DHCP clients listened by DHCP snooping and it's enabled or disabled by setting hh3cDhcpSnoopEnable node.")
hh3cDhcpSnoopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2, 1), ).setIndexNames((0, "HH3C-DHCPSNOOP-MIB", "hh3cDhcpSnoopClientIpAddressType"), (0, "HH3C-DHCPSNOOP-MIB", "hh3cDhcpSnoopClientIpAddress"))
if mibBuilder.loadTexts: hh3cDhcpSnoopEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSnoopEntry.setDescription('An entry containing information of DHCP clients.')
hh3cDhcpSnoopClientIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2, 1, 1), InetAddressType().clone('ipv4'))
if mibBuilder.loadTexts: hh3cDhcpSnoopClientIpAddressType.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSnoopClientIpAddressType.setDescription("DHCP clients' IP addresses type (IPv4 or IPv6).")
hh3cDhcpSnoopClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2, 1, 2), InetAddress())
if mibBuilder.loadTexts: hh3cDhcpSnoopClientIpAddress.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSnoopClientIpAddress.setDescription("DHCP clients' IP addresses collected by DHCP snooping.")
hh3cDhcpSnoopClientMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDhcpSnoopClientMacAddress.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSnoopClientMacAddress.setDescription("DHCP clients' MAC addresses collected by DHCP snooping.")
hh3cDhcpSnoopClientProperty = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDhcpSnoopClientProperty.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSnoopClientProperty.setDescription('Method of getting IP addresses collected by DHCP snooping.')
hh3cDhcpSnoopClientUnitNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDhcpSnoopClientUnitNum.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSnoopClientUnitNum.setDescription('IRF (Intelligent Resilient Fabric) unit number via whom the clients get their IP addresses. The value 0 means this device does not support IRF.')
hh3cDhcpSnoopTrustTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 3), )
if mibBuilder.loadTexts: hh3cDhcpSnoopTrustTable.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSnoopTrustTable.setDescription('A table is used to configure and monitor port trusted status.')
hh3cDhcpSnoopTrustEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cDhcpSnoopTrustEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSnoopTrustEntry.setDescription('An entry containing information about trusted status of ports.')
hh3cDhcpSnoopTrustStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("untrusted", 0), ("trusted", 1))).clone('untrusted')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoopTrustStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSnoopTrustStatus.setDescription('Trusted status of current port which supports both get and set operation.')
hh3cDhcpSnoopVlanTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 4), )
if mibBuilder.loadTexts: hh3cDhcpSnoopVlanTable.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSnoopVlanTable.setDescription('A table is used to configure and monitor DHCP Snooping status of VLANs.')
hh3cDhcpSnoopVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 4, 1), ).setIndexNames((0, "HH3C-DHCPSNOOP-MIB", "hh3cDhcpSnoopVlanIndex"))
if mibBuilder.loadTexts: hh3cDhcpSnoopVlanEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSnoopVlanEntry.setDescription('The entry information about hh3cDhcpSnoopVlanTable.')
hh3cDhcpSnoopVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hh3cDhcpSnoopVlanIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSnoopVlanIndex.setDescription('Current VLAN index.')
hh3cDhcpSnoopVlanEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 4, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoopVlanEnable.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSnoopVlanEnable.setDescription('DHCP Snooping status of current VLAN.')
hh3cDhcpSnoopTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 36, 2))
hh3cDhcpSnoopTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 36, 2, 0))
hh3cDhcpSnoopTrapsObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 36, 2, 1))
hh3cDhcpSnoopSpoofServerMac = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 36, 2, 1, 1), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDhcpSnoopSpoofServerMac.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSnoopSpoofServerMac.setDescription('MAC address of the spoofing server and it is derived from link-layer header of offer packet. If the offer packet is relayed by dhcp relay entity, it may be the MAC address of relay entity. ')
hh3cDhcpSnoopSpoofServerIP = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 36, 2, 1, 2), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDhcpSnoopSpoofServerIP.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSnoopSpoofServerIP.setDescription("IP address of the spoofing server and it is derived from IP header of offer packet. A tricksy host may send offer packet use other host's address, so this address can not always be trust. ")
hh3cDhcpSnoopSpoofServerDetected = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 36, 2, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("HH3C-LswVLAN-MIB", "hh3cdot1qVlanIndex"), ("HH3C-DHCPSNOOP-MIB", "hh3cDhcpSnoopSpoofServerMac"), ("HH3C-DHCPSNOOP-MIB", "hh3cDhcpSnoopSpoofServerIP"))
if mibBuilder.loadTexts: hh3cDhcpSnoopSpoofServerDetected.setStatus('current')
if mibBuilder.loadTexts: hh3cDhcpSnoopSpoofServerDetected.setDescription('To detect unauthorized DHCP servers on a network, the DHCP snooping device sends DHCP-DISCOVER messages through its downstream port (which is connected to the DHCP clients). If any response (DHCP-OFFER message) is received from the downstream port, an unauthorized DHCP server is considered present, and then the device sends a trap. With unauthorized DHCP server detection enabled, the interface sends a DHCP-DISCOVER message to detect unauthorized DHCP servers on the network. If this interface receives a DHCP-OFFER message, the DHCP server which sent it is considered unauthorized. ')
mibBuilder.exportSymbols("HH3C-DHCPSNOOP-MIB", hh3cDhcpSnoopTrapsObject=hh3cDhcpSnoopTrapsObject, hh3cDhcpSnoopClientMacAddress=hh3cDhcpSnoopClientMacAddress, hh3cDhcpSnoopTraps=hh3cDhcpSnoopTraps, hh3cDhcpSnoopTrustEntry=hh3cDhcpSnoopTrustEntry, PYSNMP_MODULE_ID=hh3cDhcpSnoop, hh3cDhcpSnoopClientIpAddressType=hh3cDhcpSnoopClientIpAddressType, hh3cDhcpSnoopTrustStatus=hh3cDhcpSnoopTrustStatus, hh3cDhcpSnoopVlanTable=hh3cDhcpSnoopVlanTable, hh3cDhcpSnoopVlanEnable=hh3cDhcpSnoopVlanEnable, hh3cDhcpSnoopTrustTable=hh3cDhcpSnoopTrustTable, hh3cDhcpSnoopMibObject=hh3cDhcpSnoopMibObject, hh3cDhcpSnoopTable=hh3cDhcpSnoopTable, hh3cDhcpSnoopVlanEntry=hh3cDhcpSnoopVlanEntry, hh3cDhcpSnoopSpoofServerIP=hh3cDhcpSnoopSpoofServerIP, hh3cDhcpSnoopVlanIndex=hh3cDhcpSnoopVlanIndex, hh3cDhcpSnoopClientUnitNum=hh3cDhcpSnoopClientUnitNum, hh3cDhcpSnoopClientProperty=hh3cDhcpSnoopClientProperty, hh3cDhcpSnoop=hh3cDhcpSnoop, hh3cDhcpSnoopTrapsPrefix=hh3cDhcpSnoopTrapsPrefix, hh3cDhcpSnoopEntry=hh3cDhcpSnoopEntry, hh3cDhcpSnoopSpoofServerMac=hh3cDhcpSnoopSpoofServerMac, hh3cDhcpSnoopClientIpAddress=hh3cDhcpSnoopClientIpAddress, hh3cDhcpSnoopSpoofServerDetected=hh3cDhcpSnoopSpoofServerDetected, hh3cDhcpSnoopEnable=hh3cDhcpSnoopEnable)