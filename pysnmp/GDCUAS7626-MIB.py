#
# PySNMP MIB module GDCUAS7626-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GDCUAS7626-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:05:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
SCinstance, = mibBuilder.importSymbols("GDCMACRO-MIB", "SCinstance")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, enterprises, Integer32, NotificationType, iso, Counter32, Unsigned32, IpAddress, TimeTicks, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "enterprises", "Integer32", "NotificationType", "iso", "Counter32", "Unsigned32", "IpAddress", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gdc = MibIdentifier((1, 3, 6, 1, 4, 1, 498))
bql2 = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12))
uas7626 = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 12))
uas7626Version = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 12, 1))
uas7626Maintenance = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 12, 2))
uas7626Configuration = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 12, 3))
uas7626Diagnostics = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 12, 4))
uas7626Performance = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 12, 5))
uas7626AlarmConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 12, 6))
uas7626Alarms = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 12, 7))
uas7626MIBversion = MibScalar((1, 3, 6, 1, 4, 1, 498, 12, 12, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626MIBversion.setStatus('mandatory')
uas7626VersionTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 12, 1, 2), )
if mibBuilder.loadTexts: uas7626VersionTable.setStatus('mandatory')
uas7626VersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 12, 1, 2, 1), ).setIndexNames((0, "GDCUAS7626-MIB", "uas7626VersionIndex"))
if mibBuilder.loadTexts: uas7626VersionEntry.setStatus('mandatory')
uas7626VersionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 1, 2, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626VersionIndex.setStatus('mandatory')
uas7626ActiveFirmwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626ActiveFirmwareRev.setStatus('mandatory')
uas7626StoredFirmwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626StoredFirmwareRev.setStatus('mandatory')
uas7626StoredFirmwareStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("statBlank", 1), ("statDownLoading", 2), ("statOK", 3), ("statCheckSumBad", 4), ("statUnZipping", 5), ("statBadUnZip", 6), ("statDownloadAborted", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626StoredFirmwareStatus.setStatus('mandatory')
uas7626SwitchActiveFirmware = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("switchNorm", 1), ("switchActive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626SwitchActiveFirmware.setStatus('mandatory')
uas7626DownloadingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disableAll", 1), ("enableAndWait", 2), ("enableAndSwitch", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626DownloadingMode.setStatus('mandatory')
uas7626MaintenanceTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1), )
if mibBuilder.loadTexts: uas7626MaintenanceTable.setStatus('mandatory')
uas7626MaintenanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1), ).setIndexNames((0, "GDCUAS7626-MIB", "uas7626MaintenanceLineIndex"))
if mibBuilder.loadTexts: uas7626MaintenanceEntry.setStatus('mandatory')
uas7626MaintenanceLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626MaintenanceLineIndex.setStatus('mandatory')
uas7626SoftReset = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("norm", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626SoftReset.setStatus('mandatory')
uas7626DefaultInit = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("factoryDefault", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626DefaultInit.setStatus('mandatory')
uas7626ResetMajorAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("norm", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626ResetMajorAlarm.setStatus('mandatory')
uas7626ResetMinorAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("norm", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626ResetMinorAlarm.setStatus('mandatory')
uas7626ResetStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("norm", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626ResetStatistics.setStatus('mandatory')
uas7626ValidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626ValidIntervals.setStatus('mandatory')
uas7626SysUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626SysUpTime.setStatus('mandatory')
uas7626LedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626LedStatus.setStatus('mandatory')
uas7626AlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(7, 7)).setFixedLength(7)).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626AlarmStatus.setStatus('mandatory')
uas7626StatLastInitialized = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626StatLastInitialized.setStatus('mandatory')
uas7626CircuitID = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 2, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626CircuitID.setStatus('mandatory')
uas7626ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 12, 3, 1), )
if mibBuilder.loadTexts: uas7626ConfigTable.setStatus('mandatory')
uas7626ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 12, 3, 1, 1), ).setIndexNames((0, "GDCUAS7626-MIB", "uas7626ConfigIndex"))
if mibBuilder.loadTexts: uas7626ConfigEntry.setStatus('mandatory')
uas7626ConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 3, 1, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626ConfigIndex.setStatus('mandatory')
uas7626DataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("kbps64", 1), ("kbps128", 2), ("inhibit", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626DataRate.setStatus('mandatory')
uas7626Highway = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("notAssigned", 1), ("highway1", 2), ("highway2", 3), ("highway3", 4), ("highway4", 5), ("highway5", 6), ("highway6", 7), ("highway7", 8), ("highway8", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626Highway.setStatus('mandatory')
uas7626TimeSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626TimeSlot.setStatus('mandatory')
uas7626DiagTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 12, 4, 1), )
if mibBuilder.loadTexts: uas7626DiagTable.setStatus('mandatory')
uas7626DiagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 12, 4, 1, 1), ).setIndexNames((0, "GDCUAS7626-MIB", "uas7626DiagIndex"))
if mibBuilder.loadTexts: uas7626DiagEntry.setStatus('mandatory')
uas7626DiagIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 4, 1, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626DiagIndex.setStatus('mandatory')
uas7626TestSelection = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("stopTest", 1), ("digitalLoopback", 2), ("selfTest", 3), ("remoteDigitalLoopback", 4), ("rdlSelfTest", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626TestSelection.setStatus('mandatory')
uas7626TestResults = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1048576))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626TestResults.setStatus('mandatory')
uas7626ResetTestResults = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("norm", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626ResetTestResults.setStatus('mandatory')
uas7626NoResponseAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 1))
uas7626DiagRxErrAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 2))
uas7626PowerUpAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 3))
uas7626LossofTransmitClockAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 4))
uas7626OutofSyncAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 5))
uas7626SealingCurrentNoContAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 6))
uas7626UASAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 7))
uas7626ESAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 8))
uas7626MajorBERAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 9))
uas7626MinorBERAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 12, 12, 7, 10))
uas7626AlarmConfigTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 1), )
if mibBuilder.loadTexts: uas7626AlarmConfigTable.setStatus('mandatory')
uas7626AlarmConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 1, 1), ).setIndexNames((0, "GDCUAS7626-MIB", "uas7626AlarmConfigIndex"), (0, "GDCUAS7626-MIB", "uas7626AlarmConfigIdentifier"))
if mibBuilder.loadTexts: uas7626AlarmConfigEntry.setStatus('mandatory')
uas7626AlarmConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 1, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626AlarmConfigIndex.setStatus('mandatory')
uas7626AlarmConfigIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626AlarmConfigIdentifier.setStatus('mandatory')
uas7626AlarmCountThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("thres10E03", 1), ("thres10E04", 2), ("thres10E05", 3), ("thres10E06", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626AlarmCountThreshold.setStatus('mandatory')
uas7626LocalAlarmConfigTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 2), )
if mibBuilder.loadTexts: uas7626LocalAlarmConfigTable.setStatus('mandatory')
uas7626LocalAlarmConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 2, 1), ).setIndexNames((0, "GDCUAS7626-MIB", "uas7626LocalAlarmConfigIndex"))
if mibBuilder.loadTexts: uas7626LocalAlarmConfigEntry.setStatus('mandatory')
uas7626LocalAlarmConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 2, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626LocalAlarmConfigIndex.setStatus('mandatory')
uas7626LossOfClockLocal = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabledMinor", 2), ("enabledMajor", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626LossOfClockLocal.setStatus('mandatory')
uas7626ESLocal = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabledMinor", 2), ("enabledMajor", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626ESLocal.setStatus('mandatory')
uas7626UASLocal = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabledMinor", 2), ("enabledMajor", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626UASLocal.setStatus('mandatory')
uas7626OutofSyncLocal = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabledMinor", 2), ("enabledMajor", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626OutofSyncLocal.setStatus('mandatory')
uas7626NoSealingCurrentLocal = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 6, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabledMinor", 2), ("enabledMajor", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uas7626NoSealingCurrentLocal.setStatus('mandatory')
uas7626CurrentTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 3), )
if mibBuilder.loadTexts: uas7626CurrentTable.setStatus('mandatory')
uas7626CurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 3, 1), ).setIndexNames((0, "GDCUAS7626-MIB", "uas7626CurrentIndex"))
if mibBuilder.loadTexts: uas7626CurrentEntry.setStatus('mandatory')
uas7626CurrentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 3, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626CurrentIndex.setStatus('mandatory')
uas7626CurrentStat = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626CurrentStat.setStatus('mandatory')
uas7626IntervalTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 4), )
if mibBuilder.loadTexts: uas7626IntervalTable.setStatus('mandatory')
uas7626IntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 4, 1), ).setIndexNames((0, "GDCUAS7626-MIB", "uas7626IntervalIndex"), (0, "GDCUAS7626-MIB", "uas7626IntervalNumber"))
if mibBuilder.loadTexts: uas7626IntervalEntry.setStatus('mandatory')
uas7626IntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 4, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626IntervalIndex.setStatus('mandatory')
uas7626IntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626IntervalNumber.setStatus('mandatory')
uas7626IntervalStat = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626IntervalStat.setStatus('mandatory')
uas7626TotalTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 5), )
if mibBuilder.loadTexts: uas7626TotalTable.setStatus('mandatory')
uas7626TotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 5, 1), ).setIndexNames((0, "GDCUAS7626-MIB", "uas7626TotalIndex"))
if mibBuilder.loadTexts: uas7626TotalEntry.setStatus('mandatory')
uas7626TotalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 5, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626TotalIndex.setStatus('mandatory')
uas7626TotalStat = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(14, 14)).setFixedLength(14)).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626TotalStat.setStatus('mandatory')
uas7626Recent24HrTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 6), )
if mibBuilder.loadTexts: uas7626Recent24HrTable.setStatus('mandatory')
uas7626Recent24HrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 6, 1), ).setIndexNames((0, "GDCUAS7626-MIB", "uas7626Recent24HrIndex"))
if mibBuilder.loadTexts: uas7626Recent24HrEntry.setStatus('mandatory')
uas7626Recent24HrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 6, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626Recent24HrIndex.setStatus('mandatory')
uas7626Recent24HrStat = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 6, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(14, 14)).setFixedLength(14)).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626Recent24HrStat.setStatus('mandatory')
uas7626UnavailableTimeRegTable = MibTable((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 7), )
if mibBuilder.loadTexts: uas7626UnavailableTimeRegTable.setStatus('mandatory')
uas7626UnavailableTimeRegEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 7, 1), ).setIndexNames((0, "GDCUAS7626-MIB", "uas7626UnavailableTimeRegIndex"), (0, "GDCUAS7626-MIB", "uas7626UnavailableTimeRegNumber"))
if mibBuilder.loadTexts: uas7626UnavailableTimeRegEntry.setStatus('mandatory')
uas7626UnavailableTimeRegIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 7, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626UnavailableTimeRegIndex.setStatus('mandatory')
uas7626UnavailableTimeRegNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626UnavailableTimeRegNumber.setStatus('mandatory')
uas7626UnavailableTimeRegStart = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626UnavailableTimeRegStart.setStatus('mandatory')
uas7626UnavailableTimeRegStop = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 12, 12, 5, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: uas7626UnavailableTimeRegStop.setStatus('mandatory')
mibBuilder.exportSymbols("GDCUAS7626-MIB", uas7626StatLastInitialized=uas7626StatLastInitialized, uas7626MinorBERAlm=uas7626MinorBERAlm, uas7626NoSealingCurrentLocal=uas7626NoSealingCurrentLocal, uas7626DiagIndex=uas7626DiagIndex, uas7626=uas7626, uas7626DiagTable=uas7626DiagTable, uas7626UnavailableTimeRegEntry=uas7626UnavailableTimeRegEntry, uas7626LossofTransmitClockAlm=uas7626LossofTransmitClockAlm, uas7626OutofSyncLocal=uas7626OutofSyncLocal, uas7626PowerUpAlm=uas7626PowerUpAlm, uas7626CurrentTable=uas7626CurrentTable, uas7626VersionTable=uas7626VersionTable, uas7626CircuitID=uas7626CircuitID, uas7626TestSelection=uas7626TestSelection, uas7626ResetTestResults=uas7626ResetTestResults, uas7626DiagEntry=uas7626DiagEntry, uas7626UnavailableTimeRegNumber=uas7626UnavailableTimeRegNumber, bql2=bql2, uas7626SoftReset=uas7626SoftReset, uas7626AlarmConfigIdentifier=uas7626AlarmConfigIdentifier, uas7626IntervalTable=uas7626IntervalTable, uas7626LocalAlarmConfigTable=uas7626LocalAlarmConfigTable, uas7626IntervalStat=uas7626IntervalStat, uas7626TotalEntry=uas7626TotalEntry, uas7626ConfigTable=uas7626ConfigTable, uas7626ConfigIndex=uas7626ConfigIndex, uas7626Recent24HrEntry=uas7626Recent24HrEntry, uas7626LocalAlarmConfigEntry=uas7626LocalAlarmConfigEntry, uas7626ResetMajorAlarm=uas7626ResetMajorAlarm, uas7626AlarmConfig=uas7626AlarmConfig, uas7626Version=uas7626Version, uas7626UnavailableTimeRegStart=uas7626UnavailableTimeRegStart, uas7626TestResults=uas7626TestResults, uas7626IntervalIndex=uas7626IntervalIndex, uas7626MaintenanceEntry=uas7626MaintenanceEntry, uas7626Diagnostics=uas7626Diagnostics, uas7626DownloadingMode=uas7626DownloadingMode, uas7626UnavailableTimeRegStop=uas7626UnavailableTimeRegStop, uas7626ESLocal=uas7626ESLocal, uas7626TotalIndex=uas7626TotalIndex, uas7626SwitchActiveFirmware=uas7626SwitchActiveFirmware, uas7626ResetMinorAlarm=uas7626ResetMinorAlarm, uas7626CurrentEntry=uas7626CurrentEntry, uas7626CurrentIndex=uas7626CurrentIndex, uas7626MaintenanceTable=uas7626MaintenanceTable, uas7626SysUpTime=uas7626SysUpTime, uas7626DataRate=uas7626DataRate, uas7626TimeSlot=uas7626TimeSlot, uas7626ConfigEntry=uas7626ConfigEntry, uas7626LossOfClockLocal=uas7626LossOfClockLocal, gdc=gdc, uas7626IntervalEntry=uas7626IntervalEntry, uas7626UASLocal=uas7626UASLocal, uas7626UASAlm=uas7626UASAlm, uas7626CurrentStat=uas7626CurrentStat, uas7626StoredFirmwareRev=uas7626StoredFirmwareRev, uas7626SealingCurrentNoContAlm=uas7626SealingCurrentNoContAlm, uas7626AlarmConfigEntry=uas7626AlarmConfigEntry, uas7626AlarmConfigTable=uas7626AlarmConfigTable, uas7626ValidIntervals=uas7626ValidIntervals, uas7626LocalAlarmConfigIndex=uas7626LocalAlarmConfigIndex, uas7626StoredFirmwareStatus=uas7626StoredFirmwareStatus, uas7626AlarmConfigIndex=uas7626AlarmConfigIndex, uas7626ESAlm=uas7626ESAlm, uas7626DiagRxErrAlm=uas7626DiagRxErrAlm, uas7626MaintenanceLineIndex=uas7626MaintenanceLineIndex, uas7626MIBversion=uas7626MIBversion, uas7626VersionEntry=uas7626VersionEntry, uas7626LedStatus=uas7626LedStatus, uas7626UnavailableTimeRegTable=uas7626UnavailableTimeRegTable, uas7626Recent24HrTable=uas7626Recent24HrTable, uas7626Alarms=uas7626Alarms, uas7626VersionIndex=uas7626VersionIndex, uas7626Highway=uas7626Highway, uas7626Configuration=uas7626Configuration, uas7626ActiveFirmwareRev=uas7626ActiveFirmwareRev, uas7626Maintenance=uas7626Maintenance, uas7626ResetStatistics=uas7626ResetStatistics, uas7626TotalTable=uas7626TotalTable, uas7626AlarmStatus=uas7626AlarmStatus, uas7626Performance=uas7626Performance, uas7626DefaultInit=uas7626DefaultInit, uas7626MajorBERAlm=uas7626MajorBERAlm, uas7626UnavailableTimeRegIndex=uas7626UnavailableTimeRegIndex, uas7626Recent24HrStat=uas7626Recent24HrStat, uas7626NoResponseAlm=uas7626NoResponseAlm, uas7626OutofSyncAlm=uas7626OutofSyncAlm, uas7626AlarmCountThreshold=uas7626AlarmCountThreshold, uas7626Recent24HrIndex=uas7626Recent24HrIndex, uas7626TotalStat=uas7626TotalStat, uas7626IntervalNumber=uas7626IntervalNumber)