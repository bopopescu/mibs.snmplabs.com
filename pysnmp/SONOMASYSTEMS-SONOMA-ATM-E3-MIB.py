#
# PySNMP MIB module SONOMASYSTEMS-SONOMA-ATM-E3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONOMASYSTEMS-SONOMA-ATM-E3-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:01:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, iso, NotificationType, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Counter32, ModuleIdentity, MibIdentifier, ObjectIdentity, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "NotificationType", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Counter32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sonomaATM, = mibBuilder.importSymbols("SONOMASYSTEMS-SONOMA-MIB", "sonomaATM")
sonomaE3ATMAdapterGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3))
atmE3ConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1))
atmE3StatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2))
atmE3ConfPhyTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1), )
if mibBuilder.loadTexts: atmE3ConfPhyTable.setStatus('mandatory')
atmE3ConfPhyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1), ).setIndexNames((0, "SONOMASYSTEMS-SONOMA-ATM-E3-MIB", "atmE3ConfPhysIndex"))
if mibBuilder.loadTexts: atmE3ConfPhyEntry.setStatus('mandatory')
atmE3ConfPhysIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3ConfPhysIndex.setStatus('mandatory')
atmE3ConfFraming = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2))).clone(namedValues=NamedValues(("framingE3", 2))).clone('framingE3')).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3ConfFraming.setStatus('mandatory')
atmE3ConfInsGFCBits = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmE3ConfInsGFCBits.setStatus('mandatory')
atmE3ConfSerBipolarIO = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmE3ConfSerBipolarIO.setStatus('mandatory')
atmE3ConfPayloadScrambling = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmE3ConfPayloadScrambling.setStatus('mandatory')
atmE3ConfOverheadProcessing = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmE3ConfOverheadProcessing.setStatus('mandatory')
atmE3ConfHDB3Encoding = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmE3ConfHDB3Encoding.setStatus('mandatory')
atmE3ConfLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("internal", 2), ("external", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmE3ConfLoopback.setStatus('mandatory')
atmE3ConfCableLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notGreaterThan225Feet", 1), ("greaterThan225Feet", 2))).clone('notGreaterThan225Feet')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmE3ConfCableLength.setStatus('mandatory')
atmE3ConfInternalEqualizer = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("use", 1), ("bypass", 2))).clone('use')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmE3ConfInternalEqualizer.setStatus('mandatory')
atmE3ConfFillerCells = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unassigned", 1), ("idle", 2))).clone('unassigned')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmE3ConfFillerCells.setStatus('mandatory')
atmE3ConfGenerateClock = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmE3ConfGenerateClock.setStatus('mandatory')
atmE3StatsTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1), )
if mibBuilder.loadTexts: atmE3StatsTable.setStatus('mandatory')
atmE3StatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1), ).setIndexNames((0, "SONOMASYSTEMS-SONOMA-ATM-E3-MIB", "atmE3StatsPhysIndex"))
if mibBuilder.loadTexts: atmE3StatsEntry.setStatus('mandatory')
atmE3StatsPhysIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsPhysIndex.setStatus('mandatory')
atmE3StatsNoSignals = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsNoSignals.setStatus('mandatory')
atmE3StatsNoE3Frames = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsNoE3Frames.setStatus('mandatory')
atmE3StatsFrameErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsFrameErrors.setStatus('mandatory')
atmE3StatsHECErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsHECErrors.setStatus('mandatory')
atmE3StatsEMErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsEMErrors.setStatus('mandatory')
atmE3StatsFeBlockErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsFeBlockErrors.setStatus('mandatory')
atmE3StatsBpvErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsBpvErrors.setStatus('mandatory')
atmE3StatsPayloadTypeMismatches = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsPayloadTypeMismatches.setStatus('mandatory')
atmE3StatsTimingMarkers = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsTimingMarkers.setStatus('mandatory')
atmE3StatsAISDetects = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsAISDetects.setStatus('mandatory')
atmE3StatsRDIDetects = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsRDIDetects.setStatus('mandatory')
atmE3StatsSignalLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsSignalLoss.setStatus('mandatory')
atmE3StatsFrameLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsFrameLoss.setStatus('mandatory')
atmE3StatsSyncLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsSyncLoss.setStatus('mandatory')
atmE3StatsOutOfCell = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsOutOfCell.setStatus('mandatory')
atmE3StatsFIFOOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsFIFOOverflow.setStatus('mandatory')
atmE3StatsPayloadTypeMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsPayloadTypeMismatch.setStatus('mandatory')
atmE3StatsTimingMarker = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsTimingMarker.setStatus('mandatory')
atmE3StatsAISDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsAISDetect.setStatus('mandatory')
atmE3StatsRDIDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmE3StatsRDIDetect.setStatus('mandatory')
atmE3StatsClearCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 7, 3, 2, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2))).clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmE3StatsClearCounters.setStatus('mandatory')
mibBuilder.exportSymbols("SONOMASYSTEMS-SONOMA-ATM-E3-MIB", atmE3StatsEntry=atmE3StatsEntry, atmE3StatsHECErrors=atmE3StatsHECErrors, atmE3StatsBpvErrors=atmE3StatsBpvErrors, atmE3StatsFIFOOverflow=atmE3StatsFIFOOverflow, atmE3ConfOverheadProcessing=atmE3ConfOverheadProcessing, atmE3StatsEMErrors=atmE3StatsEMErrors, atmE3StatsGroup=atmE3StatsGroup, atmE3StatsSignalLoss=atmE3StatsSignalLoss, atmE3ConfSerBipolarIO=atmE3ConfSerBipolarIO, atmE3StatsClearCounters=atmE3StatsClearCounters, atmE3ConfInternalEqualizer=atmE3ConfInternalEqualizer, atmE3ConfGroup=atmE3ConfGroup, atmE3StatsFrameLoss=atmE3StatsFrameLoss, atmE3StatsSyncLoss=atmE3StatsSyncLoss, atmE3StatsFrameErrors=atmE3StatsFrameErrors, atmE3ConfPhyTable=atmE3ConfPhyTable, atmE3StatsAISDetect=atmE3StatsAISDetect, atmE3StatsTimingMarkers=atmE3StatsTimingMarkers, atmE3ConfPayloadScrambling=atmE3ConfPayloadScrambling, atmE3StatsNoSignals=atmE3StatsNoSignals, atmE3ConfPhysIndex=atmE3ConfPhysIndex, atmE3StatsPhysIndex=atmE3StatsPhysIndex, atmE3StatsOutOfCell=atmE3StatsOutOfCell, atmE3ConfFraming=atmE3ConfFraming, atmE3ConfLoopback=atmE3ConfLoopback, atmE3StatsRDIDetect=atmE3StatsRDIDetect, atmE3StatsFeBlockErrors=atmE3StatsFeBlockErrors, atmE3StatsRDIDetects=atmE3StatsRDIDetects, atmE3ConfInsGFCBits=atmE3ConfInsGFCBits, atmE3ConfFillerCells=atmE3ConfFillerCells, atmE3StatsTimingMarker=atmE3StatsTimingMarker, atmE3StatsPayloadTypeMismatches=atmE3StatsPayloadTypeMismatches, atmE3ConfPhyEntry=atmE3ConfPhyEntry, atmE3StatsTable=atmE3StatsTable, atmE3StatsAISDetects=atmE3StatsAISDetects, atmE3StatsPayloadTypeMismatch=atmE3StatsPayloadTypeMismatch, sonomaE3ATMAdapterGroup=sonomaE3ATMAdapterGroup, atmE3ConfHDB3Encoding=atmE3ConfHDB3Encoding, atmE3ConfCableLength=atmE3ConfCableLength, atmE3StatsNoE3Frames=atmE3StatsNoE3Frames, atmE3ConfGenerateClock=atmE3ConfGenerateClock)