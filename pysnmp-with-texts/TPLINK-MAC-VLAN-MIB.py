#
# PySNMP MIB module TPLINK-MAC-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-MAC-VLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:25:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, MibIdentifier, Bits, TimeTicks, Gauge32, ModuleIdentity, Integer32, ObjectIdentity, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "MibIdentifier", "Bits", "TimeTicks", "Gauge32", "ModuleIdentity", "Integer32", "ObjectIdentity", "Counter64", "NotificationType")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
tplinkMacVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 15))
tplinkMacVlanMIB.setRevisions(('2009-08-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkMacVlanMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkMacVlanMIB.setLastUpdated('200812160000Z')
if mibBuilder.loadTexts: tplinkMacVlanMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkMacVlanMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkMacVlanMIB.setDescription('Implementation of the macvlan is mandatory for the swtich.')
tplinkMacVlanMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1))
tplinkMacVlanNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 15, 2))
macVlanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1))
macVlanPort = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 2))
macVlanConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1, 1), )
if mibBuilder.loadTexts: macVlanConfigTable.setStatus('current')
if mibBuilder.loadTexts: macVlanConfigTable.setDescription('MAC VLAN (Virtual Local Area Network) is the way to classify the VLANs based on MAC Address. A MAC address is relative to a single VLAN ID. The untagged packets and the priority-tagged packets coming from the MAC address will be tagged with this VLAN ID.')
macVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1, 1, 1), ).setIndexNames((0, "TPLINK-MAC-VLAN-MIB", "macAddr"))
if mibBuilder.loadTexts: macVlanEntry.setStatus('current')
if mibBuilder.loadTexts: macVlanEntry.setDescription('An entry contains of the information of a mac vlan.')
macAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1, 1, 1, 1), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: macAddr.setStatus('current')
if mibBuilder.loadTexts: macAddr.setDescription('Enter the MAC address.')
macDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: macDescription.setStatus('current')
if mibBuilder.loadTexts: macDescription.setDescription('Give a description to the MAC address for identification, 1-8 characters.')
macVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: macVlanId.setStatus('current')
if mibBuilder.loadTexts: macVlanId.setDescription('Enter the ID number of the MAC VLAN. This VLAN should be one of the 802.1Q VLANs the ingress port belongs to, 1-4094')
macVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1, 1, 1, 4), TPRowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: macVlanStatus.setStatus('current')
if mibBuilder.loadTexts: macVlanStatus.setDescription('the following two values are states: these values may be read or written active(1), the following three values are actions: these values may be written, but are never read createAndGo(4), destroy(6)')
macVlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 2, 1), )
if mibBuilder.loadTexts: macVlanPortTable.setStatus('current')
if mibBuilder.loadTexts: macVlanPortTable.setDescription('Here you can enable the port for the MAC VLAN feature. Only the port is enabled, can the configured MAC VLAN take effect.')
macVlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: macVlanPortEntry.setStatus('current')
if mibBuilder.loadTexts: macVlanPortEntry.setDescription('An entry contains of the information of a port.')
macVlanPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: macVlanPortNumber.setStatus('current')
if mibBuilder.loadTexts: macVlanPortNumber.setDescription('The port id.')
macVlanPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: macVlanPortEnable.setStatus('current')
if mibBuilder.loadTexts: macVlanPortEnable.setDescription('Select your desired port for MAC VLAN feature. All the ports are disabled by default 0. Disable 1. Enable')
macVlanPortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: macVlanPortLag.setStatus('current')
if mibBuilder.loadTexts: macVlanPortLag.setDescription('Displays the LAG to which the port belongs')
mibBuilder.exportSymbols("TPLINK-MAC-VLAN-MIB", macVlanEntry=macVlanEntry, tplinkMacVlanNotifications=tplinkMacVlanNotifications, PYSNMP_MODULE_ID=tplinkMacVlanMIB, macVlanId=macVlanId, macVlanStatus=macVlanStatus, macVlanPortNumber=macVlanPortNumber, macVlanPortTable=macVlanPortTable, macVlanPort=macVlanPort, tplinkMacVlanMIB=tplinkMacVlanMIB, macDescription=macDescription, macVlanPortEnable=macVlanPortEnable, macVlanConfigTable=macVlanConfigTable, macVlanPortLag=macVlanPortLag, macVlanConfig=macVlanConfig, macVlanPortEntry=macVlanPortEntry, tplinkMacVlanMIBObjects=tplinkMacVlanMIBObjects, macAddr=macAddr)