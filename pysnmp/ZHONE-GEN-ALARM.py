#
# PySNMP MIB module ZHONE-GEN-ALARM (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHONE-GEN-ALARM
# Produced by pysmi-0.3.4 at Mon Apr 29 21:41:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, ModuleIdentity, MibIdentifier, Unsigned32, Opaque, Counter32, Integer32, IpAddress, Bits, Gauge32, iso, Counter64, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "MibIdentifier", "Unsigned32", "Opaque", "Counter32", "Integer32", "IpAddress", "Bits", "Gauge32", "iso", "Counter64", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
zhoneSystem, zhoneModules = mibBuilder.importSymbols("Zhone", "zhoneSystem", "zhoneModules")
ZhoneAlarmTypeId, ZhoneAlarmSeverity = mibBuilder.importSymbols("Zhone-TC", "ZhoneAlarmTypeId", "ZhoneAlarmSeverity")
genAlarm = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 6, 79))
genAlarm.setRevisions(('2004-02-18 14:30', '2004-01-12 13:37',))
if mibBuilder.loadTexts: genAlarm.setLastUpdated('200402181430Z')
if mibBuilder.loadTexts: genAlarm.setOrganization('Zhone Technologies, Inc.')
class ZhoneAlarmActiveVariableValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("counter32", 1), ("unsigned32", 2), ("timeTicks", 3), ("integer32", 4), ("ipAddress", 5), ("octetString", 6), ("objectId", 7), ("counter64", 8), ("opaque", 9))

zhoneAlarm = ObjectIdentity((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18))
if mibBuilder.loadTexts: zhoneAlarm.setStatus('current')
zhoneAlarmStats = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 1))
zhoneAlarmActiveOverflowCnt = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmActiveOverflowCnt.setStatus('current')
zhoneAlarmActiveStatsCurrentCnt = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmActiveStatsCurrentCnt.setStatus('current')
zhoneAlarmActiveStatsTotalCnt = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmActiveStatsTotalCnt.setStatus('current')
zhoneAlarmClearStatsTotalCnt = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmClearStatsTotalCnt.setStatus('current')
zhoneAlarmLastRaised = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmLastRaised.setStatus('current')
zhoneAlarmLastCleared = MibScalar((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmLastCleared.setStatus('current')
zhoneAlarmModelTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 2), )
if mibBuilder.loadTexts: zhoneAlarmModelTable.setStatus('current')
zhoneAlarmModelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 2, 1), ).setIndexNames((0, "ZHONE-GEN-ALARM", "zhoneAlarmModelAlarmId"), (0, "ZHONE-GEN-ALARM", "zhoneAlarmModelNotificationId"))
if mibBuilder.loadTexts: zhoneAlarmModelEntry.setStatus('current')
zhoneAlarmModelAlarmId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 2, 1, 1), ZhoneAlarmTypeId())
if mibBuilder.loadTexts: zhoneAlarmModelAlarmId.setStatus('current')
zhoneAlarmModelNotificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 2, 1, 2), ObjectIdentifier())
if mibBuilder.loadTexts: zhoneAlarmModelNotificationId.setStatus('current')
zhoneAlarmModelVariableId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmModelVariableId.setStatus('current')
zhoneAlarmModelDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmModelDescription.setStatus('current')
zhoneAlarmActiveTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 3), )
if mibBuilder.loadTexts: zhoneAlarmActiveTable.setStatus('current')
zhoneAlarmActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 3, 1), ).setIndexNames((0, "ZHONE-GEN-ALARM", "zhoneAlarmActiveId"), (0, "ZHONE-GEN-ALARM", "zhoneAlarmActiveResourceId"))
if mibBuilder.loadTexts: zhoneAlarmActiveEntry.setStatus('current')
zhoneAlarmActiveId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 3, 1, 1), ZhoneAlarmTypeId())
if mibBuilder.loadTexts: zhoneAlarmActiveId.setStatus('current')
zhoneAlarmActiveResourceId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 3, 1, 2), ObjectIdentifier())
if mibBuilder.loadTexts: zhoneAlarmActiveResourceId.setStatus('current')
zhoneAlarmActiveVariables = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmActiveVariables.setStatus('current')
zhoneAlarmActiveNotificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 3, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmActiveNotificationId.setStatus('current')
zhoneAlarmActiveSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 3, 1, 5), ZhoneAlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmActiveSeverity.setStatus('current')
zhoneAlarmActiveVariableTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4), )
if mibBuilder.loadTexts: zhoneAlarmActiveVariableTable.setStatus('current')
zhoneAlarmActiveVariableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1), ).setIndexNames((0, "ZHONE-GEN-ALARM", "zhoneAlarmActiveId"), (0, "ZHONE-GEN-ALARM", "zhoneAlarmActiveResourceId"), (0, "ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableId"))
if mibBuilder.loadTexts: zhoneAlarmActiveVariableEntry.setStatus('current')
zhoneAlarmActiveVariableId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: zhoneAlarmActiveVariableId.setStatus('current')
zhoneAlarmActiveVariableValueType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 2), ZhoneAlarmActiveVariableValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmActiveVariableValueType.setStatus('current')
zhoneAlarmActiveVariableCounter32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmActiveVariableCounter32Val.setStatus('current')
zhoneAlarmActiveVariableUnsigned32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmActiveVariableUnsigned32Val.setStatus('current')
zhoneAlarmActiveVariableTimeTicksVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmActiveVariableTimeTicksVal.setStatus('current')
zhoneAlarmActiveVariableInteger32Val = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmActiveVariableInteger32Val.setStatus('current')
zhoneAlarmActiveVariableOctetStringVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmActiveVariableOctetStringVal.setStatus('current')
zhoneAlarmActiveVariableIpAddressVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmActiveVariableIpAddressVal.setStatus('current')
zhoneAlarmActiveVariableOidVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 9), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmActiveVariableOidVal.setStatus('current')
zhoneAlarmActiveVariableCounter64Val = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmActiveVariableCounter64Val.setStatus('current')
zhoneAlarmActiveVariableOpaqueVal = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 11), Opaque()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmActiveVariableOpaqueVal.setStatus('current')
zhoneAlarmActiveVariableResourceId = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 4, 1, 12), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zhoneAlarmActiveVariableResourceId.setStatus('current')
zhoneAlarmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 3, 1, 18, 5)).setObjects(("ZHONE-GEN-ALARM", "zhoneAlarmActiveOverflowCnt"), ("ZHONE-GEN-ALARM", "zhoneAlarmActiveStatsCurrentCnt"), ("ZHONE-GEN-ALARM", "zhoneAlarmActiveStatsTotalCnt"), ("ZHONE-GEN-ALARM", "zhoneAlarmClearStatsTotalCnt"), ("ZHONE-GEN-ALARM", "zhoneAlarmLastRaised"), ("ZHONE-GEN-ALARM", "zhoneAlarmLastCleared"), ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariables"), ("ZHONE-GEN-ALARM", "zhoneAlarmActiveNotificationId"), ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableValueType"), ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableCounter32Val"), ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableUnsigned32Val"), ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableTimeTicksVal"), ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableInteger32Val"), ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableOctetStringVal"), ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableIpAddressVal"), ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableOidVal"), ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableCounter64Val"), ("ZHONE-GEN-ALARM", "zhoneAlarmModelVariableId"), ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableResourceId"), ("ZHONE-GEN-ALARM", "zhoneAlarmActiveVariableOpaqueVal"), ("ZHONE-GEN-ALARM", "zhoneAlarmModelDescription"), ("ZHONE-GEN-ALARM", "zhoneAlarmActiveSeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhoneAlarmGroup = zhoneAlarmGroup.setStatus('current')
mibBuilder.exportSymbols("ZHONE-GEN-ALARM", PYSNMP_MODULE_ID=genAlarm, zhoneAlarmActiveVariableUnsigned32Val=zhoneAlarmActiveVariableUnsigned32Val, ZhoneAlarmActiveVariableValue=ZhoneAlarmActiveVariableValue, zhoneAlarmActiveVariableOidVal=zhoneAlarmActiveVariableOidVal, zhoneAlarmActiveVariableEntry=zhoneAlarmActiveVariableEntry, zhoneAlarmActiveVariableTimeTicksVal=zhoneAlarmActiveVariableTimeTicksVal, zhoneAlarmActiveVariableCounter32Val=zhoneAlarmActiveVariableCounter32Val, zhoneAlarmActiveVariableId=zhoneAlarmActiveVariableId, zhoneAlarmModelVariableId=zhoneAlarmModelVariableId, zhoneAlarmLastCleared=zhoneAlarmLastCleared, zhoneAlarmActiveSeverity=zhoneAlarmActiveSeverity, zhoneAlarmActiveVariableValueType=zhoneAlarmActiveVariableValueType, zhoneAlarmModelDescription=zhoneAlarmModelDescription, genAlarm=genAlarm, zhoneAlarmActiveVariableResourceId=zhoneAlarmActiveVariableResourceId, zhoneAlarmActiveVariableCounter64Val=zhoneAlarmActiveVariableCounter64Val, zhoneAlarmModelNotificationId=zhoneAlarmModelNotificationId, zhoneAlarmActiveVariableIpAddressVal=zhoneAlarmActiveVariableIpAddressVal, zhoneAlarmActiveStatsCurrentCnt=zhoneAlarmActiveStatsCurrentCnt, zhoneAlarmModelAlarmId=zhoneAlarmModelAlarmId, zhoneAlarmActiveStatsTotalCnt=zhoneAlarmActiveStatsTotalCnt, zhoneAlarmActiveVariableTable=zhoneAlarmActiveVariableTable, zhoneAlarmActiveVariableOctetStringVal=zhoneAlarmActiveVariableOctetStringVal, zhoneAlarmModelTable=zhoneAlarmModelTable, zhoneAlarmActiveVariableOpaqueVal=zhoneAlarmActiveVariableOpaqueVal, zhoneAlarmActiveEntry=zhoneAlarmActiveEntry, zhoneAlarmGroup=zhoneAlarmGroup, zhoneAlarmActiveResourceId=zhoneAlarmActiveResourceId, zhoneAlarmClearStatsTotalCnt=zhoneAlarmClearStatsTotalCnt, zhoneAlarmModelEntry=zhoneAlarmModelEntry, zhoneAlarmActiveVariables=zhoneAlarmActiveVariables, zhoneAlarmActiveOverflowCnt=zhoneAlarmActiveOverflowCnt, zhoneAlarmStats=zhoneAlarmStats, zhoneAlarmLastRaised=zhoneAlarmLastRaised, zhoneAlarmActiveId=zhoneAlarmActiveId, zhoneAlarmActiveNotificationId=zhoneAlarmActiveNotificationId, zhoneAlarmActiveVariableInteger32Val=zhoneAlarmActiveVariableInteger32Val, zhoneAlarm=zhoneAlarm, zhoneAlarmActiveTable=zhoneAlarmActiveTable)