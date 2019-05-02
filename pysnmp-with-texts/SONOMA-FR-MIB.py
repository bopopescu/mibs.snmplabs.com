#
# PySNMP MIB module SONOMA-FR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONOMA-FR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:09:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, TimeTicks, NotificationType, Gauge32, iso, Counter64, ObjectIdentity, IpAddress, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "TimeTicks", "NotificationType", "Gauge32", "iso", "Counter64", "ObjectIdentity", "IpAddress", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sonomaSeries, = mibBuilder.importSymbols("SONOMASYSTEMS-SONOMA-MIB", "sonomaSeries")
sonomaFR = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 9))
sonomaFracTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 9, 1), )
if mibBuilder.loadTexts: sonomaFracTable.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFracTable.setDescription('')
sonomaFracEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 9, 1, 1), ).setIndexNames((0, "SONOMA-FR-MIB", "sonomaFracIndex"))
if mibBuilder.loadTexts: sonomaFracEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFracEntry.setDescription('')
sonomaFracIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFracIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFracIndex.setDescription('Same index as DSX1LineIndex.')
sonomaFracCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonomaFracCount.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFracCount.setDescription('Number of Fractional T1 channels (1 - 24).')
ccT5Table = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 9, 3), )
if mibBuilder.loadTexts: ccT5Table.setStatus('mandatory')
if mibBuilder.loadTexts: ccT5Table.setDescription('FRF.5 Connection Type Table.')
ccT5Entry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 9, 3, 1), ).setIndexNames((0, "SONOMA-FR-MIB", "ccT5EndPointA"), (0, "SONOMA-FR-MIB", "ccT5EndPointB"))
if mibBuilder.loadTexts: ccT5Entry.setStatus('mandatory')
if mibBuilder.loadTexts: ccT5Entry.setDescription('An entry in the cross-connection table of type FRF.5. The indexing of this table is identical to pmCrossConnectionTable. ccT5EndPointA will always refer to a FR logical port.')
ccT5EndPointA = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccT5EndPointA.setStatus('mandatory')
if mibBuilder.loadTexts: ccT5EndPointA.setDescription('The logical port number.')
ccT5EndPointB = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccT5EndPointB.setStatus('mandatory')
if mibBuilder.loadTexts: ccT5EndPointB.setDescription('The logical port number.')
ccT5FRSSCSDLCI = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 3, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccT5FRSSCSDLCI.setStatus('mandatory')
if mibBuilder.loadTexts: ccT5FRSSCSDLCI.setDescription('DLCI which will be used over this interface. Can and often is different from the DLCI on the frame relay physical port.')
ccT5DEtoCLPMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("frandclp", 1), ("fronlyclp0", 2), ("fronlyclp1", 3))).clone('frandclp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccT5DEtoCLPMapping.setStatus('mandatory')
if mibBuilder.loadTexts: ccT5DEtoCLPMapping.setDescription('1 - Maps DE in Q.922 to DE in FR-SSCS frame and maps it to the CLP in ATM Header; 2 - Maps DE in Q.922 to DE in FR-SSCS frame but always sets CLP in ATM header to 0. 3 - Maps DE in Q.922 to DE in FR-SSCS frame but always sets CLP in ATM header to 1.')
ccT5CLPtoDEMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fronly", 1), ("either", 2))).clone('either')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccT5CLPtoDEMapping.setStatus('mandatory')
if mibBuilder.loadTexts: ccT5CLPtoDEMapping.setDescription('1 - Maps DE in FR-SSCS to DE in Q.922 frame and maps it to the CLP in ATM Header; 2 - Maps DE in FR-SSCS to DE in Q.922 frame but always sets CLP in ATM header to 0. 3 - Maps DE in FR-SSCS to DE in Q.922 frame but always sets CLP in ATM header to 1.')
ccT5SSCSManagement = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccT5SSCSManagement.setStatus('mandatory')
if mibBuilder.loadTexts: ccT5SSCSManagement.setDescription('Enable FR SSCS Management.')
ccT5RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccT5RowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ccT5RowStatus.setDescription('This object is used to create new rows in this table, modify existing rows, and to delete existing rows.')
sonomaFRDcePortTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 9, 4), )
if mibBuilder.loadTexts: sonomaFRDcePortTable.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDcePortTable.setDescription('Sonoma FR DCE Port Table.')
sonomaFRDcePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 9, 4, 1), ).setIndexNames((0, "SONOMA-FR-MIB", "sonomaFRDcePort"))
if mibBuilder.loadTexts: sonomaFRDcePortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDcePortEntry.setDescription('An entry in the Sonoma FR Port Table which represents a DCE. The main reason for this table is to support the Craft interface. For this, the number of subids in the OID of the index needs to be the same as for frLportEntry.')
sonomaFRDcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDcePort.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDcePort.setDescription('The FR port index.')
sonomaFRDcePortType = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dce", 1), ("dte", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonomaFRDcePortType.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDcePortType.setDescription('.')
sonomaFRDcePortIncomingRateControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonomaFRDcePortIncomingRateControl.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDcePortIncomingRateControl.setDescription('Enable the enforcement of incoming rate control.')
sonomaFRDcePortOutgoingRateControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonomaFRDcePortOutgoingRateControl.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDcePortOutgoingRateControl.setDescription('Enable the enforcement of outgoing rate control.')
sonomaFRDlciTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 9, 5), )
if mibBuilder.loadTexts: sonomaFRDlciTable.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciTable.setDescription('Sonoma FR Dlci Table.')
sonomaFRDlciEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 9, 5, 1), ).setIndexNames((0, "SONOMA-FR-MIB", "sonomaFRDlciPort"), (0, "SONOMA-FR-MIB", "sonomaFRDlci"))
if mibBuilder.loadTexts: sonomaFRDlciEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciEntry.setDescription('An entry in the Sonoma FR Dlci Table. The only reason for this table is to support the Craft interface. For this, the number of subids in the OID of the index needs to be the same as for frPVCEndptEntry.')
sonomaFRDlciPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDlciPort.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciPort.setDescription('The FR port index.')
sonomaFRDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDlci.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlci.setDescription('The FR port index.')
sonomaFrDlcmiTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 9, 6), )
if mibBuilder.loadTexts: sonomaFrDlcmiTable.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFrDlcmiTable.setDescription('The Parameters for the Data Link Connection Management Interface for the frame relay service on this interface.')
sonomaFrDlcmiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 9, 6, 1), ).setIndexNames((0, "SONOMA-FR-MIB", "sonomaFrDlcmiIfIndex"))
if mibBuilder.loadTexts: sonomaFrDlcmiEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFrDlcmiEntry.setDescription('The Parameters for a particular Data Link Connection Management Interface.')
sonomaFrDlcmiIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFrDlcmiIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFrDlcmiIfIndex.setDescription('The ifIndex value of the corresponding ifEntry.')
sonomaFrDlcmiState = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 5))).clone(namedValues=NamedValues(("noLmiConfigured", 1), ("lmiRev1", 2), ("ansiT1617D", 3), ("itut933A", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonomaFrDlcmiState.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFrDlcmiState.setDescription('This variable states which Data Link Connection Management scheme is active (and by implication, what DLCI it uses) on the Frame Relay interface.')
sonomaFrDlcmiPollingInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 30)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonomaFrDlcmiPollingInterval.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFrDlcmiPollingInterval.setDescription('This is the number of seconds between successive status enquiry messages.')
sonomaFrDlcmiFullEnquiryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonomaFrDlcmiFullEnquiryInterval.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFrDlcmiFullEnquiryInterval.setDescription('Number of status enquiry intervals that pass before issuance of a full status enquiry message.')
sonomaFrDlcmiErrorThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonomaFrDlcmiErrorThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFrDlcmiErrorThreshold.setDescription('This is the maximum number of unanswered Status Enquiries the equipment shall accept before declaring the interface down.')
sonomaFrDlcmiMonitoredEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 6, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonomaFrDlcmiMonitoredEvents.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFrDlcmiMonitoredEvents.setDescription("This is the number of status polling intervals over which the error threshold is counted. For example, if within 'MonitoredEvents' number of events the station receives 'ErrorThreshold' number of errors, the interface is marked as down.")
sonomaFrDlcmiStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 6, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("fault", 2), ("initializing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFrDlcmiStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFrDlcmiStatus.setDescription('This indicates the status of the Frame Relay interface as determined by the performance of the dlcmi. If no dlcmi is running, the Frame Relay interface will stay in the running state indefinitely.')
sonomaFRDtePortTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 9, 7), )
if mibBuilder.loadTexts: sonomaFRDtePortTable.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDtePortTable.setDescription('Sonoma FR DTE Port Table.')
sonomaFRDtePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 9, 7, 1), ).setIndexNames((0, "SONOMA-FR-MIB", "sonomaFRDtePort"))
if mibBuilder.loadTexts: sonomaFRDtePortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDtePortEntry.setDescription('An entry in the Sonoma FR Port Table which represents a DTE. The main reason for this table is to support the Craft interface. For this, the number of subids in the OID of the index needs to be the same as for sonomaFrDlcmiEntry.')
sonomaFRDtePort = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDtePort.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDtePort.setDescription('The FR port index.')
sonomaFRDtePortType = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dce", 1), ("dte", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonomaFRDtePortType.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDtePortType.setDescription('.')
ccT8Table = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 9, 8), )
if mibBuilder.loadTexts: ccT8Table.setStatus('mandatory')
if mibBuilder.loadTexts: ccT8Table.setDescription('FRF.8 Connection Type Table.')
ccT8Entry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 9, 8, 1), ).setIndexNames((0, "SONOMA-FR-MIB", "ccT8EndPointA"), (0, "SONOMA-FR-MIB", "ccT8EndPointB"))
if mibBuilder.loadTexts: ccT8Entry.setStatus('mandatory')
if mibBuilder.loadTexts: ccT8Entry.setDescription('An entry in the cross-connection table of type FRF.8. The indexing of this table is identical to pmCrossConnectionTable. ccT8EndPointA will always refer to a FR logical port.')
ccT8EndPointA = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccT8EndPointA.setStatus('mandatory')
if mibBuilder.loadTexts: ccT8EndPointA.setDescription('The logical port or bundle number.')
ccT8EndPointB = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ccT8EndPointB.setStatus('mandatory')
if mibBuilder.loadTexts: ccT8EndPointB.setDescription('The logical port or bundle number.')
ccT8DECLPMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("always0", 1), ("always1", 2), ("convert", 3))).clone('convert')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccT8DECLPMapping.setStatus('mandatory')
if mibBuilder.loadTexts: ccT8DECLPMapping.setDescription('')
ccT8FECNEFCIMapping = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("always0", 1), ("always1", 2), ("convert", 3))).clone('convert')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccT8FECNEFCIMapping.setStatus('mandatory')
if mibBuilder.loadTexts: ccT8FECNEFCIMapping.setDescription('FECN/EFCI Mapping.')
ccT8ULPEncapsulation = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccT8ULPEncapsulation.setStatus('mandatory')
if mibBuilder.loadTexts: ccT8ULPEncapsulation.setDescription('ULP Encapsulation.')
ccT8RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ccT8RowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ccT8RowStatus.setDescription('This object is used to create new rows in this table, modify existing rows, and to delete existing rows.')
sonomaFRPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 9, 9), )
if mibBuilder.loadTexts: sonomaFRPortStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRPortStatsTable.setDescription('Sonoma FR Port Statistics Table.')
sonomaFRPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1), ).setIndexNames((0, "SONOMA-FR-MIB", "sonomaFRPortStatsPort"))
if mibBuilder.loadTexts: sonomaFRPortStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRPortStatsEntry.setDescription('FR Port Statistics for both DCE and DTE ports.')
sonomaFRPortStatsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRPortStatsPort.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRPortStatsPort.setDescription('The FR port index.')
sonomaFRPortStatsRecvLIVReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRPortStatsRecvLIVReqs.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRPortStatsRecvLIVReqs.setDescription('')
sonomaFRPortStatsSentLIVReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRPortStatsSentLIVReqs.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRPortStatsSentLIVReqs.setDescription('')
sonomaFRPortStatsRecvLIVRsps = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRPortStatsRecvLIVRsps.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRPortStatsRecvLIVRsps.setDescription('')
sonomaFRPortStatsSentLIVRsps = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRPortStatsSentLIVRsps.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRPortStatsSentLIVRsps.setDescription('')
sonomaFRPortStatsRecvFullReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRPortStatsRecvFullReqs.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRPortStatsRecvFullReqs.setDescription('')
sonomaFRPortStatsSentFullReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRPortStatsSentFullReqs.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRPortStatsSentFullReqs.setDescription('')
sonomaFRPortStatsRecvFullRsps = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRPortStatsRecvFullRsps.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRPortStatsRecvFullRsps.setDescription('')
sonomaFRPortStatsSentFullRsps = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRPortStatsSentFullRsps.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRPortStatsSentFullRsps.setDescription('')
sonomaFRPortStatsRecvAsyncStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRPortStatsRecvAsyncStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRPortStatsRecvAsyncStatus.setDescription('')
sonomaFRPortStatsSentAsyncStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRPortStatsSentAsyncStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRPortStatsSentAsyncStatus.setDescription('')
sonomaFRPortStatsInvalidMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRPortStatsInvalidMessages.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRPortStatsInvalidMessages.setDescription('')
sonomaFRPortStatsInvalidSeqNumbers = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRPortStatsInvalidSeqNumbers.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRPortStatsInvalidSeqNumbers.setDescription('')
sonomaFRPortStatsTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRPortStatsTimeouts.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRPortStatsTimeouts.setDescription('')
sonomaFRPortStatsServAffectingConditions = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRPortStatsServAffectingConditions.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRPortStatsServAffectingConditions.setDescription('')
sonomaSerialPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 9, 10), )
if mibBuilder.loadTexts: sonomaSerialPortStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaSerialPortStatsTable.setDescription('Sonoma Serial Port Statistics Table. The error statistics are copied from the rs232SyncPortTable. ')
sonomaSerialPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1), ).setIndexNames((0, "SONOMA-FR-MIB", "sonomaSerialPortStatsPort"))
if mibBuilder.loadTexts: sonomaSerialPortStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaSerialPortStatsEntry.setDescription('Serial Port Statistics.')
sonomaSerialPortStatsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaSerialPortStatsPort.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaSerialPortStatsPort.setDescription('The FR port index.')
sonomaSerialPortStatsRecvFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaSerialPortStatsRecvFrames.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaSerialPortStatsRecvFrames.setDescription('')
sonomaSerialPortStatsSentFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaSerialPortStatsSentFrames.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaSerialPortStatsSentFrames.setDescription('')
sonomaSerialPortStatsRecvBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaSerialPortStatsRecvBytes.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaSerialPortStatsRecvBytes.setDescription('')
sonomaSerialPortStatsSentBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaSerialPortStatsSentBytes.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaSerialPortStatsSentBytes.setDescription('')
sonomaSerialPortStatsRecvUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaSerialPortStatsRecvUtilization.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaSerialPortStatsRecvUtilization.setDescription('')
sonomaSerialPortStatsSendUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaSerialPortStatsSendUtilization.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaSerialPortStatsSendUtilization.setDescription('')
sonomaSerialPortStatsFrameCheckErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaSerialPortStatsFrameCheckErrs.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaSerialPortStatsFrameCheckErrs.setDescription('')
sonomaSerialPortStatsTransmitUnderrunErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaSerialPortStatsTransmitUnderrunErrs.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaSerialPortStatsTransmitUnderrunErrs.setDescription('')
sonomaSerialPortStatsReceiveOverrunErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaSerialPortStatsReceiveOverrunErrs.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaSerialPortStatsReceiveOverrunErrs.setDescription('')
sonomaSerialPortStatsInterruptedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaSerialPortStatsInterruptedFrames.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaSerialPortStatsInterruptedFrames.setDescription('')
sonomaSerialPortStatsAbortedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaSerialPortStatsAbortedFrames.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaSerialPortStatsAbortedFrames.setDescription('')
sonomaFRDlciStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2926, 25, 9, 11), )
if mibBuilder.loadTexts: sonomaFRDlciStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciStatsTable.setDescription('Sonoma FR DLCI Statistics Table.')
sonomaFRDlciStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1), ).setIndexNames((0, "SONOMA-FR-MIB", "sonomaFRDlciStatsPort"), (0, "SONOMA-FR-MIB", "sonomaFRDlciStatsDlci"))
if mibBuilder.loadTexts: sonomaFRDlciStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciStatsEntry.setDescription('FR DLCI Statistics.')
sonomaFRDlciStatsPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDlciStatsPort.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciStatsPort.setDescription('The FR port index.')
sonomaFRDlciStatsDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDlciStatsDlci.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciStatsDlci.setDescription('The FR Dlci index.')
sonomaFRDlciStatsRecvFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDlciStatsRecvFrames.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciStatsRecvFrames.setDescription('')
sonomaFRDlciStatsSentFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDlciStatsSentFrames.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciStatsSentFrames.setDescription('')
sonomaFRDlciStatsRecvBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDlciStatsRecvBytes.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciStatsRecvBytes.setDescription('')
sonomaFRDlciStatsSentBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDlciStatsSentBytes.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciStatsSentBytes.setDescription('')
sonomaFRDlciStatsRecvDeFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDlciStatsRecvDeFrames.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciStatsRecvDeFrames.setDescription('')
sonomaFRDlciStatsSentDeFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDlciStatsSentDeFrames.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciStatsSentDeFrames.setDescription('')
sonomaFRDlciStatsRecvExcess = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDlciStatsRecvExcess.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciStatsRecvExcess.setDescription('')
sonomaFRDlciStatsSentExcess = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDlciStatsSentExcess.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciStatsSentExcess.setDescription('')
sonomaFRDlciStatsRecvDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDlciStatsRecvDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciStatsRecvDiscards.setDescription('')
sonomaFRDlciStatsSentDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDlciStatsSentDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciStatsSentDiscards.setDescription('')
sonomaFRDlciStatsRecvFecns = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDlciStatsRecvFecns.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciStatsRecvFecns.setDescription('')
sonomaFRDlciStatsSentFecns = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDlciStatsSentFecns.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciStatsSentFecns.setDescription('')
sonomaFRDlciStatsRecvBecns = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDlciStatsRecvBecns.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciStatsRecvBecns.setDescription('')
sonomaFRDlciStatsSentBecns = MibTableColumn((1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonomaFRDlciStatsSentBecns.setStatus('mandatory')
if mibBuilder.loadTexts: sonomaFRDlciStatsSentBecns.setDescription('')
mibBuilder.exportSymbols("SONOMA-FR-MIB", ccT8DECLPMapping=ccT8DECLPMapping, sonomaFRDlciTable=sonomaFRDlciTable, sonomaFRPortStatsSentAsyncStatus=sonomaFRPortStatsSentAsyncStatus, sonomaFRDlciStatsTable=sonomaFRDlciStatsTable, sonomaSerialPortStatsFrameCheckErrs=sonomaSerialPortStatsFrameCheckErrs, sonomaFRDlciStatsSentExcess=sonomaFRDlciStatsSentExcess, sonomaSerialPortStatsSendUtilization=sonomaSerialPortStatsSendUtilization, sonomaSerialPortStatsRecvBytes=sonomaSerialPortStatsRecvBytes, sonomaFRPortStatsRecvLIVRsps=sonomaFRPortStatsRecvLIVRsps, sonomaFRPortStatsRecvFullReqs=sonomaFRPortStatsRecvFullReqs, sonomaFRDcePort=sonomaFRDcePort, sonomaFRDlciStatsSentDiscards=sonomaFRDlciStatsSentDiscards, sonomaFRDlciStatsRecvExcess=sonomaFRDlciStatsRecvExcess, sonomaFRDlciStatsRecvBecns=sonomaFRDlciStatsRecvBecns, sonomaSerialPortStatsReceiveOverrunErrs=sonomaSerialPortStatsReceiveOverrunErrs, sonomaFRPortStatsRecvAsyncStatus=sonomaFRPortStatsRecvAsyncStatus, sonomaFRDlciEntry=sonomaFRDlciEntry, ccT5RowStatus=ccT5RowStatus, sonomaFRDlciStatsRecvBytes=sonomaFRDlciStatsRecvBytes, ccT8Entry=ccT8Entry, ccT5Table=ccT5Table, sonomaFRDlciStatsEntry=sonomaFRDlciStatsEntry, sonomaFRDcePortType=sonomaFRDcePortType, ccT8Table=ccT8Table, ccT8EndPointA=ccT8EndPointA, ccT5EndPointA=ccT5EndPointA, ccT5Entry=ccT5Entry, sonomaFracEntry=sonomaFracEntry, sonomaSerialPortStatsPort=sonomaSerialPortStatsPort, ccT5FRSSCSDLCI=ccT5FRSSCSDLCI, sonomaFRPortStatsSentLIVRsps=sonomaFRPortStatsSentLIVRsps, ccT8ULPEncapsulation=ccT8ULPEncapsulation, sonomaFRPortStatsSentFullReqs=sonomaFRPortStatsSentFullReqs, ccT5CLPtoDEMapping=ccT5CLPtoDEMapping, sonomaSerialPortStatsTable=sonomaSerialPortStatsTable, sonomaFrDlcmiTable=sonomaFrDlcmiTable, sonomaFracTable=sonomaFracTable, sonomaSerialPortStatsSentFrames=sonomaSerialPortStatsSentFrames, sonomaFrDlcmiMonitoredEvents=sonomaFrDlcmiMonitoredEvents, sonomaFrDlcmiFullEnquiryInterval=sonomaFrDlcmiFullEnquiryInterval, sonomaFrDlcmiPollingInterval=sonomaFrDlcmiPollingInterval, sonomaSerialPortStatsSentBytes=sonomaSerialPortStatsSentBytes, sonomaFrDlcmiStatus=sonomaFrDlcmiStatus, sonomaFRDlciStatsRecvFecns=sonomaFRDlciStatsRecvFecns, sonomaFracIndex=sonomaFracIndex, sonomaFRDtePortTable=sonomaFRDtePortTable, sonomaFRDlciStatsPort=sonomaFRDlciStatsPort, sonomaFRDtePortEntry=sonomaFRDtePortEntry, sonomaFR=sonomaFR, sonomaFRDlciStatsSentFrames=sonomaFRDlciStatsSentFrames, sonomaFRPortStatsRecvFullRsps=sonomaFRPortStatsRecvFullRsps, ccT8FECNEFCIMapping=ccT8FECNEFCIMapping, sonomaFRDcePortOutgoingRateControl=sonomaFRDcePortOutgoingRateControl, sonomaSerialPortStatsRecvUtilization=sonomaSerialPortStatsRecvUtilization, sonomaFRDlciStatsDlci=sonomaFRDlciStatsDlci, sonomaFRDlciStatsSentDeFrames=sonomaFRDlciStatsSentDeFrames, sonomaFRDlciStatsRecvDiscards=sonomaFRDlciStatsRecvDiscards, sonomaFRDtePort=sonomaFRDtePort, sonomaFRDlciStatsSentFecns=sonomaFRDlciStatsSentFecns, sonomaFRPortStatsRecvLIVReqs=sonomaFRPortStatsRecvLIVReqs, sonomaSerialPortStatsRecvFrames=sonomaSerialPortStatsRecvFrames, sonomaFRDlciStatsRecvDeFrames=sonomaFRDlciStatsRecvDeFrames, ccT5EndPointB=ccT5EndPointB, sonomaFRPortStatsInvalidMessages=sonomaFRPortStatsInvalidMessages, sonomaFRDcePortIncomingRateControl=sonomaFRDcePortIncomingRateControl, sonomaFRPortStatsTable=sonomaFRPortStatsTable, sonomaFRPortStatsInvalidSeqNumbers=sonomaFRPortStatsInvalidSeqNumbers, sonomaFrDlcmiErrorThreshold=sonomaFrDlcmiErrorThreshold, sonomaFRDlciStatsRecvFrames=sonomaFRDlciStatsRecvFrames, ccT8EndPointB=ccT8EndPointB, sonomaFRPortStatsTimeouts=sonomaFRPortStatsTimeouts, sonomaSerialPortStatsInterruptedFrames=sonomaSerialPortStatsInterruptedFrames, sonomaSerialPortStatsAbortedFrames=sonomaSerialPortStatsAbortedFrames, sonomaFRDlci=sonomaFRDlci, sonomaFRPortStatsEntry=sonomaFRPortStatsEntry, sonomaFRPortStatsSentFullRsps=sonomaFRPortStatsSentFullRsps, sonomaFRPortStatsPort=sonomaFRPortStatsPort, sonomaFRDtePortType=sonomaFRDtePortType, sonomaFRPortStatsServAffectingConditions=sonomaFRPortStatsServAffectingConditions, sonomaFracCount=sonomaFracCount, sonomaFRDlciStatsSentBecns=sonomaFRDlciStatsSentBecns, sonomaFrDlcmiState=sonomaFrDlcmiState, ccT8RowStatus=ccT8RowStatus, sonomaSerialPortStatsEntry=sonomaSerialPortStatsEntry, sonomaFRDlciPort=sonomaFRDlciPort, ccT5DEtoCLPMapping=ccT5DEtoCLPMapping, sonomaFRDcePortTable=sonomaFRDcePortTable, sonomaSerialPortStatsTransmitUnderrunErrs=sonomaSerialPortStatsTransmitUnderrunErrs, sonomaFrDlcmiEntry=sonomaFrDlcmiEntry, sonomaFRDcePortEntry=sonomaFRDcePortEntry, sonomaFRPortStatsSentLIVReqs=sonomaFRPortStatsSentLIVReqs, ccT5SSCSManagement=ccT5SSCSManagement, sonomaFrDlcmiIfIndex=sonomaFrDlcmiIfIndex, sonomaFRDlciStatsSentBytes=sonomaFRDlciStatsSentBytes)