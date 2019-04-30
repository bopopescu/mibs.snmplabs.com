#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-DisdnNI2MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-DisdnNI2MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:20:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
mscDataSigChanIndex, mscDataSigChan = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex", "mscDataSigChan")
Unsigned32, RowStatus, StorageType, DisplayString = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "Unsigned32", "RowStatus", "StorageType", "DisplayString")
Link, NonReplicated = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "Link", "NonReplicated")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, NotificationType, Integer32, MibIdentifier, Unsigned32, ModuleIdentity, IpAddress, Counter64, TimeTicks, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "NotificationType", "Integer32", "MibIdentifier", "Unsigned32", "ModuleIdentity", "IpAddress", "Counter64", "TimeTicks", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
disdnNI2MIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126))
mscDataSigChanNi2 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12))
mscDataSigChanNi2RowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 1), )
if mibBuilder.loadTexts: mscDataSigChanNi2RowStatusTable.setStatus('mandatory')
mscDataSigChanNi2RowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"))
if mibBuilder.loadTexts: mscDataSigChanNi2RowStatusEntry.setStatus('mandatory')
mscDataSigChanNi2RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2RowStatus.setStatus('mandatory')
mscDataSigChanNi2ComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2ComponentName.setStatus('mandatory')
mscDataSigChanNi2StorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2StorageType.setStatus('mandatory')
mscDataSigChanNi2Index = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscDataSigChanNi2Index.setStatus('mandatory')
mscDataSigChanNi2L2Table = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11), )
if mibBuilder.loadTexts: mscDataSigChanNi2L2Table.setStatus('mandatory')
mscDataSigChanNi2L2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"))
if mibBuilder.loadTexts: mscDataSigChanNi2L2Entry.setStatus('mandatory')
mscDataSigChanNi2T23 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2T23.setStatus('mandatory')
mscDataSigChanNi2T200 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2T200.setStatus('mandatory')
mscDataSigChanNi2N200 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2N200.setStatus('mandatory')
mscDataSigChanNi2T203 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 40)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2T203.setStatus('mandatory')
mscDataSigChanNi2N201 = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(4, 260)).clone(260)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2N201.setStatus('mandatory')
mscDataSigChanNi2CircuitSwitchedK = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 11, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 632)).clone(7)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2CircuitSwitchedK.setStatus('mandatory')
mscDataSigChanNi2ProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 13), )
if mibBuilder.loadTexts: mscDataSigChanNi2ProvTable.setStatus('mandatory')
mscDataSigChanNi2ProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 13, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"))
if mibBuilder.loadTexts: mscDataSigChanNi2ProvEntry.setStatus('mandatory')
mscDataSigChanNi2Side = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("network", 1), ("user", 2))).clone('user')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2Side.setStatus('mandatory')
mscDataSigChanNi2OperTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 15), )
if mibBuilder.loadTexts: mscDataSigChanNi2OperTable.setStatus('mandatory')
mscDataSigChanNi2OperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 15, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"))
if mibBuilder.loadTexts: mscDataSigChanNi2OperEntry.setStatus('mandatory')
mscDataSigChanNi2ActiveChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 15, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2ActiveChannels.setStatus('mandatory')
mscDataSigChanNi2PeakActiveChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 15, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2PeakActiveChannels.setStatus('mandatory')
mscDataSigChanNi2DChanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 15, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("outOfService", 0), ("establishing", 1), ("established", 2), ("enabling", 3), ("inService", 4), ("restarting", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2DChanStatus.setStatus('mandatory')
mscDataSigChanNi2ToolsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 16), )
if mibBuilder.loadTexts: mscDataSigChanNi2ToolsTable.setStatus('mandatory')
mscDataSigChanNi2ToolsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 16, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"))
if mibBuilder.loadTexts: mscDataSigChanNi2ToolsEntry.setStatus('mandatory')
mscDataSigChanNi2Tracing = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 16, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2Tracing.setStatus('mandatory')
mscDataSigChanNi2Framer = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2))
mscDataSigChanNi2FramerRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 1), )
if mibBuilder.loadTexts: mscDataSigChanNi2FramerRowStatusTable.setStatus('mandatory')
mscDataSigChanNi2FramerRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2FramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanNi2FramerRowStatusEntry.setStatus('mandatory')
mscDataSigChanNi2FramerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerRowStatus.setStatus('mandatory')
mscDataSigChanNi2FramerComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerComponentName.setStatus('mandatory')
mscDataSigChanNi2FramerStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerStorageType.setStatus('mandatory')
mscDataSigChanNi2FramerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscDataSigChanNi2FramerIndex.setStatus('mandatory')
mscDataSigChanNi2FramerProvTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 10), )
if mibBuilder.loadTexts: mscDataSigChanNi2FramerProvTable.setStatus('mandatory')
mscDataSigChanNi2FramerProvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2FramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanNi2FramerProvEntry.setStatus('mandatory')
mscDataSigChanNi2FramerInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 10, 1, 1), Link()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerInterfaceName.setStatus('mandatory')
mscDataSigChanNi2FramerStateTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 12), )
if mibBuilder.loadTexts: mscDataSigChanNi2FramerStateTable.setStatus('mandatory')
mscDataSigChanNi2FramerStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 12, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2FramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanNi2FramerStateEntry.setStatus('mandatory')
mscDataSigChanNi2FramerAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 12, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("locked", 0), ("unlocked", 1), ("shuttingDown", 2))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerAdminState.setStatus('mandatory')
mscDataSigChanNi2FramerOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 12, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerOperationalState.setStatus('mandatory')
mscDataSigChanNi2FramerUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("idle", 0), ("active", 1), ("busy", 2))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerUsageState.setStatus('mandatory')
mscDataSigChanNi2FramerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13), )
if mibBuilder.loadTexts: mscDataSigChanNi2FramerStatsTable.setStatus('mandatory')
mscDataSigChanNi2FramerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-DataIsdnMIB", "mscDataSigChanIndex"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2Index"), (0, "Nortel-MsCarrier-MscPassport-DisdnNI2MIB", "mscDataSigChanNi2FramerIndex"))
if mibBuilder.loadTexts: mscDataSigChanNi2FramerStatsEntry.setStatus('mandatory')
mscDataSigChanNi2FramerFrmToIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerFrmToIf.setStatus('mandatory')
mscDataSigChanNi2FramerFrmFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerFrmFromIf.setStatus('mandatory')
mscDataSigChanNi2FramerOctetFromIf = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerOctetFromIf.setStatus('mandatory')
mscDataSigChanNi2FramerAborts = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerAborts.setStatus('mandatory')
mscDataSigChanNi2FramerCrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerCrcErrors.setStatus('mandatory')
mscDataSigChanNi2FramerLrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerLrcErrors.setStatus('mandatory')
mscDataSigChanNi2FramerNonOctetErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerNonOctetErrors.setStatus('mandatory')
mscDataSigChanNi2FramerOverruns = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerOverruns.setStatus('mandatory')
mscDataSigChanNi2FramerUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerUnderruns.setStatus('mandatory')
mscDataSigChanNi2FramerLargeFrmErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 120, 12, 2, 13, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscDataSigChanNi2FramerLargeFrmErrors.setStatus('mandatory')
disdnNI2Group = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 1))
disdnNI2GroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 1, 1))
disdnNI2GroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 1, 1, 3))
disdnNI2GroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 1, 1, 3, 2))
disdnNI2Capabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 3))
disdnNI2CapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 3, 1))
disdnNI2CapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 3, 1, 3))
disdnNI2CapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 126, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-DisdnNI2MIB", disdnNI2GroupCA02=disdnNI2GroupCA02, mscDataSigChanNi2ProvTable=mscDataSigChanNi2ProvTable, disdnNI2CapabilitiesCA02=disdnNI2CapabilitiesCA02, mscDataSigChanNi2OperTable=mscDataSigChanNi2OperTable, disdnNI2MIB=disdnNI2MIB, mscDataSigChanNi2FramerLrcErrors=mscDataSigChanNi2FramerLrcErrors, disdnNI2Group=disdnNI2Group, mscDataSigChanNi2StorageType=mscDataSigChanNi2StorageType, mscDataSigChanNi2FramerAdminState=mscDataSigChanNi2FramerAdminState, mscDataSigChanNi2PeakActiveChannels=mscDataSigChanNi2PeakActiveChannels, mscDataSigChanNi2DChanStatus=mscDataSigChanNi2DChanStatus, mscDataSigChanNi2ToolsTable=mscDataSigChanNi2ToolsTable, mscDataSigChanNi2FramerProvTable=mscDataSigChanNi2FramerProvTable, disdnNI2GroupCA02A=disdnNI2GroupCA02A, disdnNI2CapabilitiesCA=disdnNI2CapabilitiesCA, mscDataSigChanNi2Index=mscDataSigChanNi2Index, mscDataSigChanNi2FramerFrmToIf=mscDataSigChanNi2FramerFrmToIf, mscDataSigChanNi2RowStatusTable=mscDataSigChanNi2RowStatusTable, mscDataSigChanNi2FramerOperationalState=mscDataSigChanNi2FramerOperationalState, mscDataSigChanNi2FramerStatsEntry=mscDataSigChanNi2FramerStatsEntry, mscDataSigChanNi2FramerUnderruns=mscDataSigChanNi2FramerUnderruns, disdnNI2CapabilitiesCA02A=disdnNI2CapabilitiesCA02A, mscDataSigChanNi2FramerOverruns=mscDataSigChanNi2FramerOverruns, mscDataSigChanNi2FramerLargeFrmErrors=mscDataSigChanNi2FramerLargeFrmErrors, mscDataSigChanNi2ToolsEntry=mscDataSigChanNi2ToolsEntry, mscDataSigChanNi2Side=mscDataSigChanNi2Side, mscDataSigChanNi2T200=mscDataSigChanNi2T200, mscDataSigChanNi2N201=mscDataSigChanNi2N201, mscDataSigChanNi2T23=mscDataSigChanNi2T23, mscDataSigChanNi2FramerNonOctetErrors=mscDataSigChanNi2FramerNonOctetErrors, mscDataSigChanNi2N200=mscDataSigChanNi2N200, mscDataSigChanNi2OperEntry=mscDataSigChanNi2OperEntry, mscDataSigChanNi2FramerFrmFromIf=mscDataSigChanNi2FramerFrmFromIf, mscDataSigChanNi2FramerStatsTable=mscDataSigChanNi2FramerStatsTable, mscDataSigChanNi2FramerCrcErrors=mscDataSigChanNi2FramerCrcErrors, mscDataSigChanNi2FramerComponentName=mscDataSigChanNi2FramerComponentName, mscDataSigChanNi2=mscDataSigChanNi2, mscDataSigChanNi2L2Entry=mscDataSigChanNi2L2Entry, mscDataSigChanNi2T203=mscDataSigChanNi2T203, mscDataSigChanNi2FramerRowStatusEntry=mscDataSigChanNi2FramerRowStatusEntry, mscDataSigChanNi2FramerInterfaceName=mscDataSigChanNi2FramerInterfaceName, mscDataSigChanNi2L2Table=mscDataSigChanNi2L2Table, mscDataSigChanNi2Tracing=mscDataSigChanNi2Tracing, mscDataSigChanNi2FramerStorageType=mscDataSigChanNi2FramerStorageType, mscDataSigChanNi2FramerStateEntry=mscDataSigChanNi2FramerStateEntry, mscDataSigChanNi2ProvEntry=mscDataSigChanNi2ProvEntry, mscDataSigChanNi2FramerUsageState=mscDataSigChanNi2FramerUsageState, mscDataSigChanNi2RowStatusEntry=mscDataSigChanNi2RowStatusEntry, mscDataSigChanNi2CircuitSwitchedK=mscDataSigChanNi2CircuitSwitchedK, mscDataSigChanNi2Framer=mscDataSigChanNi2Framer, mscDataSigChanNi2FramerRowStatus=mscDataSigChanNi2FramerRowStatus, disdnNI2Capabilities=disdnNI2Capabilities, mscDataSigChanNi2FramerAborts=mscDataSigChanNi2FramerAborts, mscDataSigChanNi2ActiveChannels=mscDataSigChanNi2ActiveChannels, mscDataSigChanNi2FramerProvEntry=mscDataSigChanNi2FramerProvEntry, mscDataSigChanNi2FramerRowStatusTable=mscDataSigChanNi2FramerRowStatusTable, mscDataSigChanNi2FramerStateTable=mscDataSigChanNi2FramerStateTable, disdnNI2GroupCA=disdnNI2GroupCA, mscDataSigChanNi2FramerOctetFromIf=mscDataSigChanNi2FramerOctetFromIf, mscDataSigChanNi2RowStatus=mscDataSigChanNi2RowStatus, mscDataSigChanNi2FramerIndex=mscDataSigChanNi2FramerIndex, mscDataSigChanNi2ComponentName=mscDataSigChanNi2ComponentName)