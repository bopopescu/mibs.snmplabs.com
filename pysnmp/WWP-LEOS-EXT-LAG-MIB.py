#
# PySNMP MIB module WWP-LEOS-EXT-LAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-LEOS-EXT-LAG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:31:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, TimeTicks, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, ObjectIdentity, MibIdentifier, Integer32, Counter32, IpAddress, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "TimeTicks", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "ObjectIdentity", "MibIdentifier", "Integer32", "Counter32", "IpAddress", "Bits", "Gauge32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
wwpModulesLeos, = mibBuilder.importSymbols("WWP-SMI", "wwpModulesLeos")
wwpLeosExtLagMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14))
wwpLeosExtLagMIB.setRevisions(('2003-01-15 17:00',))
if mibBuilder.loadTexts: wwpLeosExtLagMIB.setLastUpdated('200301151700Z')
if mibBuilder.loadTexts: wwpLeosExtLagMIB.setOrganization('Ciena, Inc')
wwpLeosExtLagMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1))
wwpLeosExtLag = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1))
wwpLeosExtLagMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 2))
wwpLeosExtLagMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 2, 0))
wwpLeosExtLagMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 3))
wwpLeosExtLagMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 3, 1))
wwpLeosExtLagMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 3, 2))
wwpLeosMaxLags = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosMaxLags.setStatus('current')
wwpLeosNumLags = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosNumLags.setStatus('current')
wwpLeosExtLagTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3), )
if mibBuilder.loadTexts: wwpLeosExtLagTable.setStatus('current')
wwpLeosExtLagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1), ).setIndexNames((0, "WWP-LEOS-EXT-LAG-MIB", "wwpLeosExtAggId"))
if mibBuilder.loadTexts: wwpLeosExtLagEntry.setStatus('current')
wwpLeosExtAggId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosExtAggId.setStatus('current')
wwpLeosExtAggName = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosExtAggName.setStatus('current')
wwpLeosExtAggIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosExtAggIndex.setStatus('current')
wwpLeosExtAggStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosExtAggStatus.setStatus('current')
wwpLeosExtAggMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lacp", 1), ("manual", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosExtAggMode.setStatus('current')
wwpLeosExtLagProtectionRevertState = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosExtLagProtectionRevertState.setStatus('current')
wwpLeosExtLagProtectionRevertTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60000)).clone(5000)).setUnits('msec').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosExtLagProtectionRevertTimer.setStatus('current')
wwpLeosExtAggHashMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mac-based", 1), ("ip-based", 2), ("enhanced", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosExtAggHashMode.setStatus('current')
wwpLeosExtLagProtectionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("proprietary", 1), ("standard", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosExtLagProtectionMode.setStatus('current')
wwpLeosLagModeTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 4), )
if mibBuilder.loadTexts: wwpLeosLagModeTable.setStatus('current')
wwpLeosLagModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 4, 1), ).setIndexNames((0, "WWP-LEOS-EXT-LAG-MIB", "wwpLeosLagPhyPortId"))
if mibBuilder.loadTexts: wwpLeosLagModeEntry.setStatus('current')
wwpLeosLagPhyPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLagPhyPortId.setStatus('current')
wwpLeosLagAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lacp", 1), ("manual", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosLagAdminMode.setStatus('current')
wwpLeosLagOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lacp", 1), ("manual", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLagOperMode.setStatus('current')
wwpLeosLagProtectionTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 5), )
if mibBuilder.loadTexts: wwpLeosLagProtectionTable.setStatus('current')
wwpLeosLagProtectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 5, 1), ).setIndexNames((0, "WWP-LEOS-EXT-LAG-MIB", "wwpLeosExtAggId"), (0, "WWP-LEOS-EXT-LAG-MIB", "wwpLeosLagProtectionPort"))
if mibBuilder.loadTexts: wwpLeosLagProtectionEntry.setStatus('current')
wwpLeosLagProtectionPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosLagProtectionPort.setStatus('current')
wwpLeosLagProtectionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 5, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosLagProtectionRowStatus.setStatus('current')
wwpLeosExtAggFloodHashMode = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 14, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("simplified", 1), ("enhanced", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosExtAggFloodHashMode.setStatus('current')
mibBuilder.exportSymbols("WWP-LEOS-EXT-LAG-MIB", wwpLeosExtLagEntry=wwpLeosExtLagEntry, wwpLeosExtLagMIBNotifications=wwpLeosExtLagMIBNotifications, wwpLeosLagProtectionPort=wwpLeosLagProtectionPort, wwpLeosExtLagProtectionRevertState=wwpLeosExtLagProtectionRevertState, wwpLeosExtAggName=wwpLeosExtAggName, wwpLeosExtAggFloodHashMode=wwpLeosExtAggFloodHashMode, wwpLeosExtLagTable=wwpLeosExtLagTable, wwpLeosLagProtectionTable=wwpLeosLagProtectionTable, wwpLeosLagPhyPortId=wwpLeosLagPhyPortId, wwpLeosExtAggIndex=wwpLeosExtAggIndex, wwpLeosExtAggId=wwpLeosExtAggId, wwpLeosLagProtectionRowStatus=wwpLeosLagProtectionRowStatus, wwpLeosExtLagMIB=wwpLeosExtLagMIB, wwpLeosExtAggStatus=wwpLeosExtAggStatus, wwpLeosNumLags=wwpLeosNumLags, wwpLeosExtLagProtectionRevertTimer=wwpLeosExtLagProtectionRevertTimer, wwpLeosLagAdminMode=wwpLeosLagAdminMode, PYSNMP_MODULE_ID=wwpLeosExtLagMIB, wwpLeosLagOperMode=wwpLeosLagOperMode, wwpLeosExtLag=wwpLeosExtLag, wwpLeosExtLagMIBGroups=wwpLeosExtLagMIBGroups, wwpLeosExtAggMode=wwpLeosExtAggMode, wwpLeosExtLagProtectionMode=wwpLeosExtLagProtectionMode, wwpLeosLagModeTable=wwpLeosLagModeTable, wwpLeosExtLagMIBConformance=wwpLeosExtLagMIBConformance, wwpLeosExtAggHashMode=wwpLeosExtAggHashMode, wwpLeosLagModeEntry=wwpLeosLagModeEntry, wwpLeosLagProtectionEntry=wwpLeosLagProtectionEntry, wwpLeosExtLagMIBNotificationPrefix=wwpLeosExtLagMIBNotificationPrefix, wwpLeosExtLagMIBCompliances=wwpLeosExtLagMIBCompliances, wwpLeosMaxLags=wwpLeosMaxLags, wwpLeosExtLagMIBObjects=wwpLeosExtLagMIBObjects)