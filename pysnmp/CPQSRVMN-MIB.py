#
# PySNMP MIB module CPQSRVMN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CPQSRVMN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:12:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
compaq, = mibBuilder.importSymbols("CPQHOST-MIB", "compaq")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, iso, TimeTicks, IpAddress, Counter64, ModuleIdentity, ObjectIdentity, MibIdentifier, Unsigned32, NotificationType, Bits, Gauge32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "TimeTicks", "IpAddress", "Counter64", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Unsigned32", "NotificationType", "Bits", "Gauge32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cpqServerManager = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 4))
cpqSmMibRev = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 4, 1))
cpqSmComponent = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 4, 2))
cpqSmTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 4, 3))
cpqSmInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 4, 2, 1))
cpqSmCntlr = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 4, 2, 2))
cpqSmObjData = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 4, 2, 3))
cpqSmAsyncComm = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 4, 2, 4))
cpqSmAlert = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 4, 2, 5))
cpqSmOsNetWare3x = MibIdentifier((1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1))
cpqSmNw3xDriverName = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmNw3xDriverName.setStatus('mandatory')
cpqSmNw3xDriverDate = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmNw3xDriverDate.setStatus('mandatory')
cpqSmNw3xDriverVersion = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmNw3xDriverVersion.setStatus('mandatory')
cpqSmNw3xDriverIssuedCommands = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmNw3xDriverIssuedCommands.setStatus('mandatory')
cpqSmNw3xDriverReceivedCommands = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmNw3xDriverReceivedCommands.setStatus('mandatory')
cpqSmNw3xDriverWatchdogFrequency = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmNw3xDriverWatchdogFrequency.setStatus('mandatory')
cpqSmNw3xDriverClockSyncFrequency = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmNw3xDriverClockSyncFrequency.setStatus('mandatory')
cpqSmNw3xDriverIssuedWatchdogs = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmNw3xDriverIssuedWatchdogs.setStatus('mandatory')
cpqSmNw3xDriverIssuedClockSyncs = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmNw3xDriverIssuedClockSyncs.setStatus('mandatory')
cpqSmNw3xDriverMemoryAllocationFailedErrs = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmNw3xDriverMemoryAllocationFailedErrs.setStatus('mandatory')
cpqSmNw3xDriverBoardResets = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmNw3xDriverBoardResets.setStatus('mandatory')
cpqSmNw3xBoardState = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmNw3xBoardState.setStatus('mandatory')
cpqSmCntlrBoardName = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmCntlrBoardName.setStatus('mandatory')
cpqSmCntlrBoardId = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmCntlrBoardId.setStatus('mandatory')
cpqSmCntlrRomDate = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmCntlrRomDate.setStatus('mandatory')
cpqSmCntlrCountryCode = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmCntlrCountryCode.setStatus('mandatory')
cpqSmCntlrVoiceRomStatus = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("notInstalled", 2), ("installed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmCntlrVoiceRomStatus.setStatus('mandatory')
cpqSmCntlrBatteryStatus = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("connected", 2), ("disconnected", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmCntlrBatteryStatus.setStatus('mandatory')
cpqSmCntlrDormantModeStatus = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("normal", 2), ("dormantOnPowerDown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmCntlrDormantModeStatus.setStatus('mandatory')
cpqSmCntlrSelfTestErrorCode = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmCntlrSelfTestErrorCode.setStatus('mandatory')
cpqSmCntlrOsId = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 177, 178, 179, 180, 181, 182))).clone(namedValues=NamedValues(("other", 1), ("netware286", 177), ("netware386", 178), ("os2LanManager", 179), ("unix", 180), ("banyan", 181), ("dos", 182)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmCntlrOsId.setStatus('mandatory')
cpqSmCntlrOsMajorRev = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmCntlrOsMajorRev.setStatus('mandatory')
cpqSmCntlrOsMinorRev = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmCntlrOsMinorRev.setStatus('mandatory')
cpqSmCntlrPostTimeout = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmCntlrPostTimeout.setStatus('mandatory')
cpqSmCntlrCondition = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("degraded", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmCntlrCondition.setStatus('mandatory')
cpqSmObjDataTotalObjects = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmObjDataTotalObjects.setStatus('mandatory')
cpqSmObjDataObjectTotalSpace = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmObjDataObjectTotalSpace.setStatus('mandatory')
cpqSmObjDataObjectSpaceAvailable = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmObjDataObjectSpaceAvailable.setStatus('mandatory')
cpqSmObjDataInnateMonitoringStatus = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmObjDataInnateMonitoringStatus.setStatus('mandatory')
cpqSmObjectTable = MibTable((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 5), )
if mibBuilder.loadTexts: cpqSmObjectTable.setStatus('mandatory')
cpqSmObjectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 5, 1), ).setIndexNames((0, "CPQSRVMN-MIB", "cpqSmObjectIndex"), (0, "CPQSRVMN-MIB", "cpqSmObjectInstIndex"))
if mibBuilder.loadTexts: cpqSmObjectEntry.setStatus('mandatory')
cpqSmObjectIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmObjectIndex.setStatus('mandatory')
cpqSmObjectInstIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmObjectInstIndex.setStatus('mandatory')
cpqSmObjectClass = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmObjectClass.setStatus('mandatory')
cpqSmObjectLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 5, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmObjectLabel.setStatus('mandatory')
cpqSmMonItemTable = MibTable((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6), )
if mibBuilder.loadTexts: cpqSmMonItemTable.setStatus('mandatory')
cpqSmMonItemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1), ).setIndexNames((0, "CPQSRVMN-MIB", "cpqSmMonItemObjIndex"), (0, "CPQSRVMN-MIB", "cpqSmMonItemInstIndex"), (0, "CPQSRVMN-MIB", "cpqSmMonItemIndex"))
if mibBuilder.loadTexts: cpqSmMonItemEntry.setStatus('mandatory')
cpqSmMonItemObjIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemObjIndex.setStatus('mandatory')
cpqSmMonItemInstIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemInstIndex.setStatus('mandatory')
cpqSmMonItemIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemIndex.setStatus('mandatory')
cpqSmMonItemOnNetAlertStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemOnNetAlertStatus.setStatus('mandatory')
cpqSmMonItemRemoteAlertStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemRemoteAlertStatus.setStatus('mandatory')
cpqSmMonItemInnateStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("externallyManaged", 2), ("innate", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemInnateStatus.setStatus('mandatory')
cpqSmMonItemHostNotify = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemHostNotify.setStatus('mandatory')
cpqSmMonItemLogicalOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("other", 1), ("equal", 2), ("notEqual", 3), ("lessThan", 4), ("greaterThan", 5), ("lessThanOrEqual", 6), ("greaterThanOrEqual", 7), ("inside", 8), ("outside", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemLogicalOperator.setStatus('mandatory')
cpqSmMonItemSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("status", 2), ("warning", 3), ("critical", 4), ("catastrophic", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemSeverity.setStatus('mandatory')
cpqSmMonItemDataType = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("counter", 2), ("state", 3), ("range", 4), ("string", 5), ("data", 6), ("queue", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemDataType.setStatus('mandatory')
cpqSmMonItemVoiceMsgNum = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 511))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemVoiceMsgNum.setStatus('mandatory')
cpqSmMonItemLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemLabel.setStatus('mandatory')
cpqSmMonItemLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemLimit.setStatus('mandatory')
cpqSmMonItemOptional = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemOptional.setStatus('mandatory')
cpqSmMonItemDefVal = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemDefVal.setStatus('mandatory')
cpqSmMonItemCurVal = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemCurVal.setStatus('mandatory')
cpqSmMonItemCurString = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemCurString.setStatus('mandatory')
cpqSmMonItemCurContents = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemCurContents.setStatus('mandatory')
cpqSmMonItemTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 3, 6, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmMonItemTimeStamp.setStatus('mandatory')
cpqSmCommAsyncCommunicationStatus = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmCommAsyncCommunicationStatus.setStatus('mandatory')
cpqSmCommInternalModemMaxBaudRate = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmCommInternalModemMaxBaudRate.setStatus('mandatory')
cpqSmCommAudibleIndicatorStatus = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmCommAudibleIndicatorStatus.setStatus('mandatory')
cpqSmCommRemoteSessionStatus = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("notSupported", 2), ("noSessionActive", 3), ("remoteSessionActive", 4), ("pgrVoiceSessionActive", 5), ("remoteConsoleActive", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmCommRemoteSessionStatus.setStatus('mandatory')
cpqSmCommCallbackStatus = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmCommCallbackStatus.setStatus('mandatory')
cpqSmModemSettingsTable = MibTable((1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6), )
if mibBuilder.loadTexts: cpqSmModemSettingsTable.setStatus('mandatory')
cpqSmModemSettingsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1), ).setIndexNames((0, "CPQSRVMN-MIB", "cpqSmModemSettingsIndex"))
if mibBuilder.loadTexts: cpqSmModemSettingsEntry.setStatus('mandatory')
cpqSmModemSettingsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(48, 49, 50))).clone(namedValues=NamedValues(("internalModem", 48), ("externalModem", 49), ("pager", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmModemSettingsIndex.setStatus('mandatory')
cpqSmModemSettingsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("other", 1), ("noInternalModem", 2), ("internalUSModem", 3), ("internalIntnlModem", 4), ("serialPortNotSetup", 5), ("serialDirectConnect", 6), ("serialExternalModem", 7), ("pagerInformationData", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmModemSettingsStatus.setStatus('mandatory')
cpqSmModemSettingsBaudRate = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmModemSettingsBaudRate.setStatus('mandatory')
cpqSmModemSettingsParity = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("none", 2), ("odd", 3), ("even", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmModemSettingsParity.setStatus('mandatory')
cpqSmModemSettingsDataLength = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmModemSettingsDataLength.setStatus('mandatory')
cpqSmModemSettingsStopBits = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmModemSettingsStopBits.setStatus('mandatory')
cpqSmModemSettingsDialString = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmModemSettingsDialString.setStatus('mandatory')
cpqSmModemSettingsHangUpString = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmModemSettingsHangUpString.setStatus('mandatory')
cpqSmModemSettingsAnswerString = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmModemSettingsAnswerString.setStatus('mandatory')
cpqSmModemSettingsOriginateString = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 4, 6, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmModemSettingsOriginateString.setStatus('mandatory')
cpqSmAlertStatus = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmAlertStatus.setStatus('mandatory')
cpqSmAlertDestTable = MibTable((1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2), )
if mibBuilder.loadTexts: cpqSmAlertDestTable.setStatus('mandatory')
cpqSmAlertDestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1), ).setIndexNames((0, "CPQSRVMN-MIB", "cpqSmAlertDestPriorityIndex"))
if mibBuilder.loadTexts: cpqSmAlertDestEntry.setStatus('mandatory')
cpqSmAlertDestPriorityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmAlertDestPriorityIndex.setStatus('mandatory')
cpqSmAlertDestType = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 161, 162, 163, 164, 165, 166))).clone(namedValues=NamedValues(("other", 1), ("internalModemToSmf", 161), ("internalModemToPager", 162), ("internalModemToVoice", 163), ("externalModemToSmf", 164), ("externalModemToPager", 165), ("externalDirectToSmf", 166)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmAlertDestType.setStatus('mandatory')
cpqSmAlertDestRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmAlertDestRetries.setStatus('mandatory')
cpqSmAlertDestConnectFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("alertOnly", 2), ("callbackOnly", 3), ("alertAndCallback", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmAlertDestConnectFlags.setStatus('mandatory')
cpqSmAlertDestPhoneNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmAlertDestPhoneNumber.setStatus('mandatory')
cpqSmAlertDestTimeMask = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(21, 21)).setFixedLength(21)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmAlertDestTimeMask.setStatus('mandatory')
cpqSmAlertDestPagerType = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("numericOnly", 2), ("alphanumeric", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmAlertDestPagerType.setStatus('mandatory')
cpqSmAlertDestPagerId = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmAlertDestPagerId.setStatus('mandatory')
cpqSmAlertDestPagerDisplayLength = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 2, 5, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmAlertDestPagerDisplayLength.setStatus('mandatory')
cpqSmTrapPkts = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmTrapPkts.setStatus('mandatory')
cpqSmTrapLogMaxSize = MibScalar((1, 3, 6, 1, 4, 1, 232, 4, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmTrapLogMaxSize.setStatus('mandatory')
cpqSmTrapLogTable = MibTable((1, 3, 6, 1, 4, 1, 232, 4, 3, 3), )
if mibBuilder.loadTexts: cpqSmTrapLogTable.setStatus('mandatory')
cpqSmTrapLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 232, 4, 3, 3, 1), ).setIndexNames((0, "CPQSRVMN-MIB", "cpqSmTrapLogIndex"))
if mibBuilder.loadTexts: cpqSmTrapLogEntry.setStatus('mandatory')
cpqSmTrapLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmTrapLogIndex.setStatus('mandatory')
cpqSmTrapType = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("cpqSmBoardFailed", 1), ("cpqSmBoardReset", 2), ("cpqSmServerManagerAlert", 3), ("cpqSmCommFailed", 4), ("cpqSmBatteryFailed", 5), ("cpqSmBoardTimeout", 6), ("cpqSmAlertDestinationBlacklisted", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmTrapType.setStatus('mandatory')
cpqSmTrapTime = MibTableColumn((1, 3, 6, 1, 4, 1, 232, 4, 3, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpqSmTrapTime.setStatus('mandatory')
cpqSmBoardFailed = NotificationType((1, 3, 6, 1, 4, 1, 232, 4) + (0,1))
cpqSmBoardReset = NotificationType((1, 3, 6, 1, 4, 1, 232, 4) + (0,2))
cpqSmServerManagerAlert = NotificationType((1, 3, 6, 1, 4, 1, 232, 4) + (0,3)).setObjects(("CPQSRVMN-MIB", "cpqSmMonItemCurVal"), ("CPQSRVMN-MIB", "cpqSmObjectLabel"), ("CPQSRVMN-MIB", "cpqSmMonItemLabel"), ("CPQSRVMN-MIB", "cpqSmMonItemDataType"), ("CPQSRVMN-MIB", "cpqSmMonItemSeverity"), ("CPQSRVMN-MIB", "cpqSmMonItemLimit"), ("CPQSRVMN-MIB", "cpqSmMonItemOptional"), ("CPQSRVMN-MIB", "cpqSmMonItemLogicalOperator"), ("CPQSRVMN-MIB", "cpqSmMonItemTimeStamp"))
cpqSmCommFailed = NotificationType((1, 3, 6, 1, 4, 1, 232, 4) + (0,4))
cpqSmBatteryFailed = NotificationType((1, 3, 6, 1, 4, 1, 232, 4) + (0,5))
cpqSmBoardTimeout = NotificationType((1, 3, 6, 1, 4, 1, 232, 4) + (0,6))
cpqSmAlertDestinationBlacklisted = NotificationType((1, 3, 6, 1, 4, 1, 232, 4) + (0,7)).setObjects(("CPQSRVMN-MIB", "cpqSmAlertDestType"), ("CPQSRVMN-MIB", "cpqSmAlertDestPhoneNumber"), ("CPQSRVMN-MIB", "cpqSmAlertDestPagerId"))
mibBuilder.exportSymbols("CPQSRVMN-MIB", cpqSmCntlrBatteryStatus=cpqSmCntlrBatteryStatus, cpqSmModemSettingsTable=cpqSmModemSettingsTable, cpqSmNw3xBoardState=cpqSmNw3xBoardState, cpqSmNw3xDriverName=cpqSmNw3xDriverName, cpqSmCommRemoteSessionStatus=cpqSmCommRemoteSessionStatus, cpqSmMonItemLogicalOperator=cpqSmMonItemLogicalOperator, cpqSmCntlrPostTimeout=cpqSmCntlrPostTimeout, cpqSmTrap=cpqSmTrap, cpqSmMonItemTimeStamp=cpqSmMonItemTimeStamp, cpqSmModemSettingsDialString=cpqSmModemSettingsDialString, cpqSmModemSettingsAnswerString=cpqSmModemSettingsAnswerString, cpqSmCommFailed=cpqSmCommFailed, cpqSmObjDataObjectTotalSpace=cpqSmObjDataObjectTotalSpace, cpqSmCntlrVoiceRomStatus=cpqSmCntlrVoiceRomStatus, cpqSmCntlrCountryCode=cpqSmCntlrCountryCode, cpqSmMonItemOptional=cpqSmMonItemOptional, cpqSmAsyncComm=cpqSmAsyncComm, cpqSmModemSettingsDataLength=cpqSmModemSettingsDataLength, cpqSmComponent=cpqSmComponent, cpqSmTrapType=cpqSmTrapType, cpqSmCntlr=cpqSmCntlr, cpqSmMonItemLabel=cpqSmMonItemLabel, cpqSmCommCallbackStatus=cpqSmCommCallbackStatus, cpqSmNw3xDriverWatchdogFrequency=cpqSmNw3xDriverWatchdogFrequency, cpqSmMonItemInstIndex=cpqSmMonItemInstIndex, cpqSmMonItemIndex=cpqSmMonItemIndex, cpqSmServerManagerAlert=cpqSmServerManagerAlert, cpqSmModemSettingsBaudRate=cpqSmModemSettingsBaudRate, cpqSmMonItemDataType=cpqSmMonItemDataType, cpqSmObjDataTotalObjects=cpqSmObjDataTotalObjects, cpqSmTrapLogTable=cpqSmTrapLogTable, cpqSmTrapLogMaxSize=cpqSmTrapLogMaxSize, cpqSmNw3xDriverIssuedClockSyncs=cpqSmNw3xDriverIssuedClockSyncs, cpqSmCntlrRomDate=cpqSmCntlrRomDate, cpqSmNw3xDriverDate=cpqSmNw3xDriverDate, cpqSmMonItemTable=cpqSmMonItemTable, cpqSmAlertDestinationBlacklisted=cpqSmAlertDestinationBlacklisted, cpqSmCntlrCondition=cpqSmCntlrCondition, cpqSmObjDataInnateMonitoringStatus=cpqSmObjDataInnateMonitoringStatus, cpqSmMonItemCurContents=cpqSmMonItemCurContents, cpqSmOsNetWare3x=cpqSmOsNetWare3x, cpqSmObjData=cpqSmObjData, cpqSmAlertDestPagerDisplayLength=cpqSmAlertDestPagerDisplayLength, cpqSmObjectIndex=cpqSmObjectIndex, cpqSmNw3xDriverVersion=cpqSmNw3xDriverVersion, cpqSmCntlrBoardName=cpqSmCntlrBoardName, cpqSmObjDataObjectSpaceAvailable=cpqSmObjDataObjectSpaceAvailable, cpqSmCntlrOsMajorRev=cpqSmCntlrOsMajorRev, cpqSmObjectTable=cpqSmObjectTable, cpqSmAlertDestPagerType=cpqSmAlertDestPagerType, cpqSmCntlrOsId=cpqSmCntlrOsId, cpqSmModemSettingsStopBits=cpqSmModemSettingsStopBits, cpqSmCntlrOsMinorRev=cpqSmCntlrOsMinorRev, cpqSmModemSettingsStatus=cpqSmModemSettingsStatus, cpqSmMonItemInnateStatus=cpqSmMonItemInnateStatus, cpqSmMonItemCurVal=cpqSmMonItemCurVal, cpqSmNw3xDriverBoardResets=cpqSmNw3xDriverBoardResets, cpqSmInterface=cpqSmInterface, cpqSmNw3xDriverIssuedWatchdogs=cpqSmNw3xDriverIssuedWatchdogs, cpqSmMonItemEntry=cpqSmMonItemEntry, cpqSmBoardFailed=cpqSmBoardFailed, cpqSmModemSettingsIndex=cpqSmModemSettingsIndex, cpqSmAlertDestRetries=cpqSmAlertDestRetries, cpqSmModemSettingsOriginateString=cpqSmModemSettingsOriginateString, cpqSmAlertDestPhoneNumber=cpqSmAlertDestPhoneNumber, cpqSmAlertDestTable=cpqSmAlertDestTable, cpqSmNw3xDriverClockSyncFrequency=cpqSmNw3xDriverClockSyncFrequency, cpqSmAlertDestEntry=cpqSmAlertDestEntry, cpqSmTrapLogIndex=cpqSmTrapLogIndex, cpqSmTrapLogEntry=cpqSmTrapLogEntry, cpqSmAlertStatus=cpqSmAlertStatus, cpqSmCntlrBoardId=cpqSmCntlrBoardId, cpqSmObjectClass=cpqSmObjectClass, cpqSmNw3xDriverReceivedCommands=cpqSmNw3xDriverReceivedCommands, cpqSmModemSettingsParity=cpqSmModemSettingsParity, cpqSmMonItemVoiceMsgNum=cpqSmMonItemVoiceMsgNum, cpqSmCommInternalModemMaxBaudRate=cpqSmCommInternalModemMaxBaudRate, cpqSmCntlrSelfTestErrorCode=cpqSmCntlrSelfTestErrorCode, cpqSmMonItemOnNetAlertStatus=cpqSmMonItemOnNetAlertStatus, cpqSmNw3xDriverMemoryAllocationFailedErrs=cpqSmNw3xDriverMemoryAllocationFailedErrs, cpqSmMonItemRemoteAlertStatus=cpqSmMonItemRemoteAlertStatus, cpqSmMonItemCurString=cpqSmMonItemCurString, cpqSmObjectInstIndex=cpqSmObjectInstIndex, cpqSmAlertDestTimeMask=cpqSmAlertDestTimeMask, cpqSmObjectEntry=cpqSmObjectEntry, cpqSmAlertDestPriorityIndex=cpqSmAlertDestPriorityIndex, cpqSmMonItemDefVal=cpqSmMonItemDefVal, cpqSmNw3xDriverIssuedCommands=cpqSmNw3xDriverIssuedCommands, cpqSmBoardTimeout=cpqSmBoardTimeout, cpqSmModemSettingsEntry=cpqSmModemSettingsEntry, cpqSmAlert=cpqSmAlert, cpqSmCommAsyncCommunicationStatus=cpqSmCommAsyncCommunicationStatus, cpqSmTrapTime=cpqSmTrapTime, cpqSmTrapPkts=cpqSmTrapPkts, cpqSmMibRev=cpqSmMibRev, cpqSmCommAudibleIndicatorStatus=cpqSmCommAudibleIndicatorStatus, cpqSmCntlrDormantModeStatus=cpqSmCntlrDormantModeStatus, cpqSmBatteryFailed=cpqSmBatteryFailed, cpqSmAlertDestType=cpqSmAlertDestType, cpqServerManager=cpqServerManager, cpqSmObjectLabel=cpqSmObjectLabel, cpqSmAlertDestConnectFlags=cpqSmAlertDestConnectFlags, cpqSmMonItemSeverity=cpqSmMonItemSeverity, cpqSmMonItemHostNotify=cpqSmMonItemHostNotify, cpqSmBoardReset=cpqSmBoardReset, cpqSmModemSettingsHangUpString=cpqSmModemSettingsHangUpString, cpqSmAlertDestPagerId=cpqSmAlertDestPagerId, cpqSmMonItemLimit=cpqSmMonItemLimit, cpqSmMonItemObjIndex=cpqSmMonItemObjIndex)