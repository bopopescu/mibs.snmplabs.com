#
# PySNMP MIB module TIMETRA-BFD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMETRA-BFD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:09:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, Counter64, Unsigned32, NotificationType, iso, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, ModuleIdentity, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "Counter64", "Unsigned32", "NotificationType", "iso", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "ModuleIdentity", "MibIdentifier", "Counter32")
TextualConvention, TimeStamp, TimeInterval, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "TimeInterval", "DisplayString", "TruthValue", "RowStatus")
tmnxSRConfs, tmnxSRNotifyPrefix, tmnxSRObjs, timetraSRMIBModules = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "tmnxSRConfs", "tmnxSRNotifyPrefix", "tmnxSRObjs", "timetraSRMIBModules")
TNamedItem, = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TNamedItem")
timetraBfdMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 85))
if mibBuilder.loadTexts: timetraBfdMIBModule.setLastUpdated('201206080000Z')
if mibBuilder.loadTexts: timetraBfdMIBModule.setOrganization('Alcatel-Lucent')
tmnxBfdObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85))
tmnxBfdConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85))
tmnxBfdCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 1))
tmnxBfdGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 2))
tmnxBfdOperObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1))
tmnxBfdAdminObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2))
tmnxBfdAdminControlObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 1))
tmnxBfdAdminValueObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2))
tmnxBfdAdminOwner = MibScalar((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmnxBfdAdminOwner.setStatus('current')
tmnxBfdAdminControlApply = MibScalar((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("initialize", 2), ("commit", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmnxBfdAdminControlApply.setStatus('current')
tmnxBfdAdminLastSetTimer = MibScalar((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 1, 3), TimeInterval()).setUnits('centiseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxBfdAdminLastSetTimer.setStatus('current')
tmnxBfdAdminLastSetTimeout = MibScalar((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 1, 4), TimeInterval().clone(180000)).setUnits('centiseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmnxBfdAdminLastSetTimeout.setStatus('current')
tmnxBfdAdminTemplateTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1), )
if mibBuilder.loadTexts: tmnxBfdAdminTemplateTable.setStatus('current')
tmnxBfdAdminTemplateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1), ).setIndexNames((0, "TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateName"))
if mibBuilder.loadTexts: tmnxBfdAdminTemplateEntry.setStatus('current')
tmnxBfdAdminTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 1), TNamedItem())
if mibBuilder.loadTexts: tmnxBfdAdminTemplateName.setStatus('current')
tmnxBfdAdminTemplateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxBfdAdminTemplateRowStatus.setStatus('current')
tmnxBfdAdminTemplateTxInt = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 100000)).clone(100)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxBfdAdminTemplateTxInt.setStatus('current')
tmnxBfdAdminTemplateRxInt = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 100000)).clone(100)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxBfdAdminTemplateRxInt.setStatus('current')
tmnxBfdAdminTemplateMultiplier = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(3, 20)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxBfdAdminTemplateMultiplier.setStatus('current')
tmnxBfdAdminTemplateEchoRxInt = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 100000)).clone(100)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxBfdAdminTemplateEchoRxInt.setStatus('current')
tmnxBfdAdminTemplateType = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cpmNp", 1), ("auto", 2), ("iomHw", 3))).clone('auto')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxBfdAdminTemplateType.setStatus('current')
tmnxBfdOperValueObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1))
tmnxBfdOperTemplateTable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1), )
if mibBuilder.loadTexts: tmnxBfdOperTemplateTable.setStatus('current')
tmnxBfdOperTemplateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1), ).setIndexNames((0, "TIMETRA-BFD-MIB", "tmnxBfdOperTemplateName"))
if mibBuilder.loadTexts: tmnxBfdOperTemplateEntry.setStatus('current')
tmnxBfdOperTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 1), TNamedItem())
if mibBuilder.loadTexts: tmnxBfdOperTemplateName.setStatus('current')
tmnxBfdOperTemplateRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxBfdOperTemplateRowStatus.setStatus('current')
tmnxBfdOperTemplateTxInt = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 100000))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxBfdOperTemplateTxInt.setStatus('current')
tmnxBfdOperTemplateRxInt = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 100000))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxBfdOperTemplateRxInt.setStatus('current')
tmnxBfdOperTemplateMultiplier = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(3, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxBfdOperTemplateMultiplier.setStatus('current')
tmnxBfdOperTemplateEchoRxInt = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 100000))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxBfdOperTemplateEchoRxInt.setStatus('current')
tmnxBfdOperTemplateType = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cpmNp", 1), ("auto", 2), ("iomHw", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxBfdOperTemplateType.setStatus('current')
tmnxBfdV11v0Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 1, 1)).setObjects(("TIMETRA-BFD-MIB", "tmnxBfdV11v0Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxBfdV11v0Compliance = tmnxBfdV11v0Compliance.setStatus('current')
tmnxBfdV11v0Group = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 2, 1)).setObjects(("TIMETRA-BFD-MIB", "tmnxBfdAdminOwner"), ("TIMETRA-BFD-MIB", "tmnxBfdAdminControlApply"), ("TIMETRA-BFD-MIB", "tmnxBfdAdminLastSetTimer"), ("TIMETRA-BFD-MIB", "tmnxBfdAdminLastSetTimeout"), ("TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateRowStatus"), ("TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateTxInt"), ("TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateRxInt"), ("TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateMultiplier"), ("TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateEchoRxInt"), ("TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateType"), ("TIMETRA-BFD-MIB", "tmnxBfdOperTemplateRowStatus"), ("TIMETRA-BFD-MIB", "tmnxBfdOperTemplateTxInt"), ("TIMETRA-BFD-MIB", "tmnxBfdOperTemplateRxInt"), ("TIMETRA-BFD-MIB", "tmnxBfdOperTemplateMultiplier"), ("TIMETRA-BFD-MIB", "tmnxBfdOperTemplateEchoRxInt"), ("TIMETRA-BFD-MIB", "tmnxBfdOperTemplateType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxBfdV11v0Group = tmnxBfdV11v0Group.setStatus('current')
mibBuilder.exportSymbols("TIMETRA-BFD-MIB", tmnxBfdOperObjects=tmnxBfdOperObjects, tmnxBfdAdminTemplateType=tmnxBfdAdminTemplateType, tmnxBfdOperValueObjects=tmnxBfdOperValueObjects, tmnxBfdAdminControlApply=tmnxBfdAdminControlApply, tmnxBfdAdminObjects=tmnxBfdAdminObjects, tmnxBfdAdminOwner=tmnxBfdAdminOwner, tmnxBfdObjects=tmnxBfdObjects, tmnxBfdCompliances=tmnxBfdCompliances, tmnxBfdAdminLastSetTimeout=tmnxBfdAdminLastSetTimeout, tmnxBfdOperTemplateTable=tmnxBfdOperTemplateTable, tmnxBfdOperTemplateEchoRxInt=tmnxBfdOperTemplateEchoRxInt, tmnxBfdConformance=tmnxBfdConformance, tmnxBfdOperTemplateName=tmnxBfdOperTemplateName, tmnxBfdAdminTemplateRowStatus=tmnxBfdAdminTemplateRowStatus, tmnxBfdAdminTemplateEchoRxInt=tmnxBfdAdminTemplateEchoRxInt, tmnxBfdAdminTemplateEntry=tmnxBfdAdminTemplateEntry, tmnxBfdGroups=tmnxBfdGroups, tmnxBfdAdminLastSetTimer=tmnxBfdAdminLastSetTimer, tmnxBfdAdminTemplateRxInt=tmnxBfdAdminTemplateRxInt, tmnxBfdOperTemplateEntry=tmnxBfdOperTemplateEntry, tmnxBfdOperTemplateTxInt=tmnxBfdOperTemplateTxInt, tmnxBfdOperTemplateType=tmnxBfdOperTemplateType, tmnxBfdAdminTemplateTxInt=tmnxBfdAdminTemplateTxInt, tmnxBfdOperTemplateRowStatus=tmnxBfdOperTemplateRowStatus, tmnxBfdAdminTemplateTable=tmnxBfdAdminTemplateTable, tmnxBfdAdminTemplateName=tmnxBfdAdminTemplateName, tmnxBfdAdminValueObjects=tmnxBfdAdminValueObjects, tmnxBfdV11v0Group=tmnxBfdV11v0Group, tmnxBfdAdminTemplateMultiplier=tmnxBfdAdminTemplateMultiplier, PYSNMP_MODULE_ID=timetraBfdMIBModule, tmnxBfdOperTemplateRxInt=tmnxBfdOperTemplateRxInt, tmnxBfdOperTemplateMultiplier=tmnxBfdOperTemplateMultiplier, tmnxBfdAdminControlObjects=tmnxBfdAdminControlObjects, tmnxBfdV11v0Compliance=tmnxBfdV11v0Compliance, timetraBfdMIBModule=timetraBfdMIBModule)