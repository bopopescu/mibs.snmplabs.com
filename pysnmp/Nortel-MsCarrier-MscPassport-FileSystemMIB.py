#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-FileSystemMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-FileSystemMIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:20:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
DisplayString, Gauge32, RowPointer, Unsigned32, StorageType, Integer32, RowStatus = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "DisplayString", "Gauge32", "RowPointer", "Unsigned32", "StorageType", "Integer32", "RowStatus")
NonReplicated, AsciiString = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "NonReplicated", "AsciiString")
mscPassportMIBs, mscComponents = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs", "mscComponents")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, ModuleIdentity, Unsigned32, iso, Counter64, Integer32, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "ModuleIdentity", "Unsigned32", "iso", "Counter64", "Integer32", "TimeTicks", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fileSystemMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 16))
mscFs = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15))
mscFsRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 1), )
if mibBuilder.loadTexts: mscFsRowStatusTable.setStatus('mandatory')
mscFsRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"))
if mibBuilder.loadTexts: mscFsRowStatusEntry.setStatus('mandatory')
mscFsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsRowStatus.setStatus('mandatory')
mscFsComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsComponentName.setStatus('mandatory')
mscFsStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsStorageType.setStatus('mandatory')
mscFsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscFsIndex.setStatus('mandatory')
mscFsStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 10), )
if mibBuilder.loadTexts: mscFsStateTable.setStatus('mandatory')
mscFsStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"))
if mibBuilder.loadTexts: mscFsStateEntry.setStatus('mandatory')
mscFsAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsAdminState.setStatus('mandatory')
mscFsOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsOperationalState.setStatus('mandatory')
mscFsUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsUsageState.setStatus('mandatory')
mscFsOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 11), )
if mibBuilder.loadTexts: mscFsOperTable.setStatus('mandatory')
mscFsOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"))
if mibBuilder.loadTexts: mscFsOperEntry.setStatus('mandatory')
mscFsVolumeName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 11, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 11))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsVolumeName.setStatus('mandatory')
mscFsActiveDisk = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 11, 1, 2), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsActiveDisk.setStatus('mandatory')
mscFsSyncStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("synchronized", 0), ("unSynchronized", 1), ("synchronizing", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsSyncStatus.setStatus('mandatory')
mscFsSyncProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 11, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsSyncProgress.setStatus('mandatory')
mscFsCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 11, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsCapacity.setStatus('mandatory')
mscFsFreeSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 11, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsFreeSpace.setStatus('mandatory')
mscFsUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 11, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsUsage.setStatus('mandatory')
mscFsDisk = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2))
mscFsDiskRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 1), )
if mibBuilder.loadTexts: mscFsDiskRowStatusTable.setStatus('mandatory')
mscFsDiskRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"), (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskIndex"))
if mibBuilder.loadTexts: mscFsDiskRowStatusEntry.setStatus('mandatory')
mscFsDiskRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskRowStatus.setStatus('mandatory')
mscFsDiskComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskComponentName.setStatus('mandatory')
mscFsDiskStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskStorageType.setStatus('mandatory')
mscFsDiskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: mscFsDiskIndex.setStatus('mandatory')
mscFsDiskStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 10), )
if mibBuilder.loadTexts: mscFsDiskStateTable.setStatus('mandatory')
mscFsDiskStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"), (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskIndex"))
if mibBuilder.loadTexts: mscFsDiskStateEntry.setStatus('mandatory')
mscFsDiskAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskAdminState.setStatus('mandatory')
mscFsDiskOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskOperationalState.setStatus('mandatory')
mscFsDiskUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskUsageState.setStatus('mandatory')
mscFsDiskOperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 11), )
if mibBuilder.loadTexts: mscFsDiskOperTable.setStatus('mandatory')
mscFsDiskOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"), (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskIndex"))
if mibBuilder.loadTexts: mscFsDiskOperEntry.setStatus('mandatory')
mscFsDiskVolumeName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 11, 1, 1), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(1, 11))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscFsDiskVolumeName.setStatus('mandatory')
mscFsDiskCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 11, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskCapacity.setStatus('mandatory')
mscFsDiskFreeSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskFreeSpace.setStatus('mandatory')
mscFsDiskBadBlocksPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 11, 1, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskBadBlocksPercentage.setStatus('mandatory')
mscFsDiskUnformattedCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 11, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskUnformattedCapacity.setStatus('mandatory')
mscFsDiskTest = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2))
mscFsDiskTestRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 1), )
if mibBuilder.loadTexts: mscFsDiskTestRowStatusTable.setStatus('mandatory')
mscFsDiskTestRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"), (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskIndex"), (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskTestIndex"))
if mibBuilder.loadTexts: mscFsDiskTestRowStatusEntry.setStatus('mandatory')
mscFsDiskTestRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskTestRowStatus.setStatus('mandatory')
mscFsDiskTestComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskTestComponentName.setStatus('mandatory')
mscFsDiskTestStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskTestStorageType.setStatus('mandatory')
mscFsDiskTestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscFsDiskTestIndex.setStatus('mandatory')
mscFsDiskTestStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 10), )
if mibBuilder.loadTexts: mscFsDiskTestStateTable.setStatus('mandatory')
mscFsDiskTestStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"), (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskIndex"), (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskTestIndex"))
if mibBuilder.loadTexts: mscFsDiskTestStateEntry.setStatus('mandatory')
mscFsDiskTestAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskTestAdminState.setStatus('mandatory')
mscFsDiskTestOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskTestOperationalState.setStatus('mandatory')
mscFsDiskTestUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskTestUsageState.setStatus('mandatory')
mscFsDiskTestSetupTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 11), )
if mibBuilder.loadTexts: mscFsDiskTestSetupTable.setStatus('mandatory')
mscFsDiskTestSetupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"), (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskIndex"), (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskTestIndex"))
if mibBuilder.loadTexts: mscFsDiskTestSetupEntry.setStatus('mandatory')
mscFsDiskTestTestCount = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscFsDiskTestTestCount.setStatus('mandatory')
mscFsDiskTestDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 11, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 35791394)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscFsDiskTestDuration.setStatus('mandatory')
mscFsDiskTestType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("filesystemCheck", 0), ("diskRead", 1), ("flakyBitDetection", 2), ("surfaceAnalysis", 3))).clone('filesystemCheck')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscFsDiskTestType.setStatus('mandatory')
mscFsDiskTestResultsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 12), )
if mibBuilder.loadTexts: mscFsDiskTestResultsTable.setStatus('mandatory')
mscFsDiskTestResultsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"), (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskIndex"), (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskTestIndex"))
if mibBuilder.loadTexts: mscFsDiskTestResultsEntry.setStatus('mandatory')
mscFsDiskTestCauseOfTermination = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("testCountReached", 0), ("testTimeExpired", 1), ("stoppedByOperator", 2), ("neverStarted", 3), ("testRunning", 4), ("error", 5), ("internalError", 6), ("unknown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskTestCauseOfTermination.setStatus('mandatory')
mscFsDiskTestNatureOfError = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("logical", 0), ("media", 1), ("noErrorDetected", 2), ("failedToComplete", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskTestNatureOfError.setStatus('mandatory')
mscFsDiskTestSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("noDataLost", 0), ("dataLost", 1), ("hardwareProblem", 2), ("noError", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskTestSeverity.setStatus('mandatory')
mscFsDiskTestElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 12, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskTestElapsedTime.setStatus('mandatory')
mscFsDiskTestTestExecutionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 12, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFsDiskTestTestExecutionCount.setStatus('mandatory')
fileSystemGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 16, 1))
fileSystemGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 16, 1, 1))
fileSystemGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 16, 1, 1, 3))
fileSystemGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 16, 1, 1, 3, 2))
fileSystemCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 16, 3))
fileSystemCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 16, 3, 1))
fileSystemCapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 16, 3, 1, 3))
fileSystemCapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 16, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-FileSystemMIB", mscFsDiskTestUsageState=mscFsDiskTestUsageState, mscFsDiskTestNatureOfError=mscFsDiskTestNatureOfError, mscFsIndex=mscFsIndex, mscFsDiskRowStatus=mscFsDiskRowStatus, mscFsDiskTestRowStatusTable=mscFsDiskTestRowStatusTable, mscFsDiskTestComponentName=mscFsDiskTestComponentName, mscFsDiskTestRowStatusEntry=mscFsDiskTestRowStatusEntry, mscFsDiskOperationalState=mscFsDiskOperationalState, mscFsDiskStateTable=mscFsDiskStateTable, mscFsRowStatusTable=mscFsRowStatusTable, mscFsDiskUsageState=mscFsDiskUsageState, mscFsDiskVolumeName=mscFsDiskVolumeName, mscFsDiskBadBlocksPercentage=mscFsDiskBadBlocksPercentage, mscFsDiskTestStateTable=mscFsDiskTestStateTable, mscFsStorageType=mscFsStorageType, mscFsStateEntry=mscFsStateEntry, mscFsDiskTestAdminState=mscFsDiskTestAdminState, fileSystemGroupCA=fileSystemGroupCA, mscFsDiskTestRowStatus=mscFsDiskTestRowStatus, fileSystemGroup=fileSystemGroup, fileSystemCapabilitiesCA02=fileSystemCapabilitiesCA02, mscFsSyncProgress=mscFsSyncProgress, mscFsFreeSpace=mscFsFreeSpace, mscFsComponentName=mscFsComponentName, mscFsDiskOperTable=mscFsDiskOperTable, mscFsCapacity=mscFsCapacity, mscFsDiskTest=mscFsDiskTest, mscFsUsage=mscFsUsage, mscFsAdminState=mscFsAdminState, mscFsDisk=mscFsDisk, mscFsDiskRowStatusTable=mscFsDiskRowStatusTable, mscFsDiskTestStorageType=mscFsDiskTestStorageType, mscFsActiveDisk=mscFsActiveDisk, mscFsDiskTestType=mscFsDiskTestType, mscFsDiskTestTestCount=mscFsDiskTestTestCount, mscFsOperationalState=mscFsOperationalState, mscFsDiskOperEntry=mscFsDiskOperEntry, mscFsUsageState=mscFsUsageState, mscFsDiskCapacity=mscFsDiskCapacity, mscFsDiskAdminState=mscFsDiskAdminState, mscFsStateTable=mscFsStateTable, mscFsDiskFreeSpace=mscFsDiskFreeSpace, fileSystemGroupCA02=fileSystemGroupCA02, mscFsRowStatus=mscFsRowStatus, mscFsDiskTestIndex=mscFsDiskTestIndex, mscFsDiskStorageType=mscFsDiskStorageType, mscFsDiskTestDuration=mscFsDiskTestDuration, fileSystemCapabilities=fileSystemCapabilities, fileSystemCapabilitiesCA=fileSystemCapabilitiesCA, mscFsDiskTestOperationalState=mscFsDiskTestOperationalState, mscFsDiskTestSetupTable=mscFsDiskTestSetupTable, mscFsOperEntry=mscFsOperEntry, mscFsRowStatusEntry=mscFsRowStatusEntry, mscFsDiskTestSetupEntry=mscFsDiskTestSetupEntry, mscFsDiskTestSeverity=mscFsDiskTestSeverity, mscFsDiskTestResultsEntry=mscFsDiskTestResultsEntry, mscFsDiskTestCauseOfTermination=mscFsDiskTestCauseOfTermination, mscFsDiskTestElapsedTime=mscFsDiskTestElapsedTime, mscFsSyncStatus=mscFsSyncStatus, mscFsDiskTestTestExecutionCount=mscFsDiskTestTestExecutionCount, mscFsDiskTestStateEntry=mscFsDiskTestStateEntry, mscFsOperTable=mscFsOperTable, fileSystemGroupCA02A=fileSystemGroupCA02A, mscFsDiskComponentName=mscFsDiskComponentName, mscFs=mscFs, mscFsVolumeName=mscFsVolumeName, mscFsDiskIndex=mscFsDiskIndex, fileSystemMIB=fileSystemMIB, mscFsDiskTestResultsTable=mscFsDiskTestResultsTable, mscFsDiskUnformattedCapacity=mscFsDiskUnformattedCapacity, fileSystemCapabilitiesCA02A=fileSystemCapabilitiesCA02A, mscFsDiskStateEntry=mscFsDiskStateEntry, mscFsDiskRowStatusEntry=mscFsDiskRowStatusEntry)