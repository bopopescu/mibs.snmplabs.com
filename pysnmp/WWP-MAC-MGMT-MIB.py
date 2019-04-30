#
# PySNMP MIB module WWP-MAC-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-MAC-MGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:31:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, MibIdentifier, Gauge32, Unsigned32, TimeTicks, Counter64, iso, Integer32, IpAddress, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "Gauge32", "Unsigned32", "TimeTicks", "Counter64", "iso", "Integer32", "IpAddress", "Bits", "Counter32")
RowStatus, DisplayString, MacAddress, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "MacAddress", "TextualConvention", "TruthValue")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpMacMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 28))
wwpMacMgmtMIB.setRevisions(('2005-11-22 19:00', '2003-04-16 00:00', '2001-04-03 17:00',))
if mibBuilder.loadTexts: wwpMacMgmtMIB.setLastUpdated('200104031700Z')
if mibBuilder.loadTexts: wwpMacMgmtMIB.setOrganization('World Wide Packets, Inc')
class VlanId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

wwpMacMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1))
wwpMacMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1))
wwpMacMgmtMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 28, 2))
wwpMacMgmtMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 28, 2, 0))
wwpMacMgmtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 28, 3))
wwpMacMgmtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 28, 3, 1))
wwpMacMgmtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 28, 3, 2))
wwpMacMgmtMacTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 1), )
if mibBuilder.loadTexts: wwpMacMgmtMacTable.setStatus('current')
wwpMacMgmtMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 1, 1), ).setIndexNames((0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtVlanID"), (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtPortId"), (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtMacAddr"))
if mibBuilder.loadTexts: wwpMacMgmtMacEntry.setStatus('current')
wwpMacMgmtVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 1, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMacMgmtVlanID.setStatus('current')
wwpMacMgmtPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMacMgmtPortId.setStatus('current')
wwpMacMgmtMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMacMgmtMacAddr.setStatus('current')
wwpMacMgmtMacAddrMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dynamic", 1), ("static", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpMacMgmtMacAddrMode.setStatus('current')
wwpMacMgmtMacStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMacMgmtMacStatus.setStatus('current')
wwpMacMgmtMacRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpMacMgmtMacRowStatus.setStatus('current')
wwpMacMgmtMacReset = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpMacMgmtMacReset.setStatus('current')
wwpMacMgmtPMTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 3), )
if mibBuilder.loadTexts: wwpMacMgmtPMTable.setStatus('current')
wwpMacMgmtPMEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 3, 1), ).setIndexNames((0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtPMVlanID"), (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtPMPortId"))
if mibBuilder.loadTexts: wwpMacMgmtPMEntry.setStatus('current')
wwpMacMgmtPMVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 3, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMacMgmtPMVlanID.setStatus('current')
wwpMacMgmtPMPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMacMgmtPMPortId.setStatus('current')
wwpMacMgmtPMLearnLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 24))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpMacMgmtPMLearnLimit.setStatus('current')
wwpMacMgmtPMLearnCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMacMgmtPMLearnCount.setStatus('current')
wwpMacMgmtPMStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpMacMgmtPMStatus.setStatus('current')
wwpMacMgmtPMMacFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("flush", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpMacMgmtPMMacFlush.setStatus('current')
wwpMacMgmtCacheMac = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpMacMgmtCacheMac.setStatus('current')
wwpMacMgmtCacheMacTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 5), )
if mibBuilder.loadTexts: wwpMacMgmtCacheMacTable.setStatus('current')
wwpMacMgmtCacheMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 5, 1), ).setIndexNames((0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtCVlanID"), (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtCPortId"), (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtCMacIndex"))
if mibBuilder.loadTexts: wwpMacMgmtCacheMacEntry.setStatus('current')
wwpMacMgmtCVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 5, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMacMgmtCVlanID.setStatus('current')
wwpMacMgmtCPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMacMgmtCPortId.setStatus('current')
wwpMacMgmtCMacIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMacMgmtCMacIndex.setStatus('current')
wwpMacMgmtCMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 5, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMacMgmtCMacAddr.setStatus('current')
wwpMacMgmtCMacAddrMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dynamic", 1), ("static", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMacMgmtCMacAddrMode.setStatus('current')
wwpMacMgmtCMacStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMacMgmtCMacStatus.setStatus('current')
wwpMacMgmtCacheMacCountTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 6), )
if mibBuilder.loadTexts: wwpMacMgmtCacheMacCountTable.setStatus('current')
wwpMacMgmtCacheMacCountEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 6, 1), ).setIndexNames((0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtCVlanID"), (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtCPortId"))
if mibBuilder.loadTexts: wwpMacMgmtCacheMacCountEntry.setStatus('current')
wwpMacMgmtCacheMacCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMacMgmtCacheMacCount.setStatus('current')
wwpMacMgmtSacTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 7), )
if mibBuilder.loadTexts: wwpMacMgmtSacTable.setStatus('current')
wwpMacMgmtSacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 7, 1), ).setIndexNames((0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtSacVlanID"), (0, "WWP-MAC-MGMT-MIB", "wwpMacMgmtSacPortId"))
if mibBuilder.loadTexts: wwpMacMgmtSacEntry.setStatus('current')
wwpMacMgmtSacVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 7, 1, 1), VlanId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMacMgmtSacVlanID.setStatus('current')
wwpMacMgmtSacPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMacMgmtSacPortId.setStatus('current')
wwpMacMgmtSacLearnCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpMacMgmtSacLearnCount.setStatus('current')
wwpMacMgmtSacMaxLearn = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3000))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpMacMgmtSacMaxLearn.setStatus('current')
wwpMacMgmtSacLearnDisabled = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 7, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpMacMgmtSacLearnDisabled.setStatus('current')
wwpMacMgmtSacMacFlush = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 7, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("flush", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpMacMgmtSacMacFlush.setStatus('current')
wwpMacMgmtSacStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 28, 1, 1, 7, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpMacMgmtSacStatus.setStatus('current')
mibBuilder.exportSymbols("WWP-MAC-MGMT-MIB", wwpMacMgmtCacheMacTable=wwpMacMgmtCacheMacTable, VlanId=VlanId, wwpMacMgmtPMTable=wwpMacMgmtPMTable, wwpMacMgmtPMVlanID=wwpMacMgmtPMVlanID, wwpMacMgmtSacTable=wwpMacMgmtSacTable, wwpMacMgmtMIBGroups=wwpMacMgmtMIBGroups, wwpMacMgmtMIBCompliances=wwpMacMgmtMIBCompliances, wwpMacMgmtMacRowStatus=wwpMacMgmtMacRowStatus, wwpMacMgmtSacEntry=wwpMacMgmtSacEntry, wwpMacMgmtPMEntry=wwpMacMgmtPMEntry, wwpMacMgmtCVlanID=wwpMacMgmtCVlanID, wwpMacMgmtCacheMac=wwpMacMgmtCacheMac, wwpMacMgmtMacReset=wwpMacMgmtMacReset, wwpMacMgmtCacheMacCountEntry=wwpMacMgmtCacheMacCountEntry, wwpMacMgmtCacheMacCountTable=wwpMacMgmtCacheMacCountTable, wwpMacMgmtVlanID=wwpMacMgmtVlanID, wwpMacMgmtMacAddr=wwpMacMgmtMacAddr, wwpMacMgmtPMLearnCount=wwpMacMgmtPMLearnCount, wwpMacMgmtSacPortId=wwpMacMgmtSacPortId, wwpMacMgmtPortId=wwpMacMgmtPortId, wwpMacMgmtCPortId=wwpMacMgmtCPortId, wwpMacMgmtSacStatus=wwpMacMgmtSacStatus, wwpMacMgmtCMacStatus=wwpMacMgmtCMacStatus, wwpMacMgmtMacEntry=wwpMacMgmtMacEntry, wwpMacMgmtSacMaxLearn=wwpMacMgmtSacMaxLearn, wwpMacMgmtMIBNotificationPrefix=wwpMacMgmtMIBNotificationPrefix, wwpMacMgmtMacTable=wwpMacMgmtMacTable, wwpMacMgmt=wwpMacMgmt, wwpMacMgmtPMLearnLimit=wwpMacMgmtPMLearnLimit, wwpMacMgmtCMacAddr=wwpMacMgmtCMacAddr, wwpMacMgmtCMacIndex=wwpMacMgmtCMacIndex, wwpMacMgmtMIB=wwpMacMgmtMIB, wwpMacMgmtPMMacFlush=wwpMacMgmtPMMacFlush, wwpMacMgmtPMPortId=wwpMacMgmtPMPortId, wwpMacMgmtMIBObjects=wwpMacMgmtMIBObjects, wwpMacMgmtSacMacFlush=wwpMacMgmtSacMacFlush, wwpMacMgmtCMacAddrMode=wwpMacMgmtCMacAddrMode, wwpMacMgmtCacheMacCount=wwpMacMgmtCacheMacCount, PYSNMP_MODULE_ID=wwpMacMgmtMIB, wwpMacMgmtCacheMacEntry=wwpMacMgmtCacheMacEntry, wwpMacMgmtMacStatus=wwpMacMgmtMacStatus, wwpMacMgmtMIBConformance=wwpMacMgmtMIBConformance, wwpMacMgmtSacLearnCount=wwpMacMgmtSacLearnCount, wwpMacMgmtPMStatus=wwpMacMgmtPMStatus, wwpMacMgmtMacAddrMode=wwpMacMgmtMacAddrMode, wwpMacMgmtSacLearnDisabled=wwpMacMgmtSacLearnDisabled, wwpMacMgmtMIBNotifications=wwpMacMgmtMIBNotifications, wwpMacMgmtSacVlanID=wwpMacMgmtSacVlanID)