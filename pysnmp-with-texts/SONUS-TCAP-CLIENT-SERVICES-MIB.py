#
# PySNMP MIB module SONUS-TCAP-CLIENT-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONUS-TCAP-CLIENT-SERVICES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:10:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Unsigned32, MibIdentifier, Bits, Counter64, ModuleIdentity, ObjectIdentity, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "MibIdentifier", "Bits", "Counter64", "ModuleIdentity", "ObjectIdentity", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "IpAddress", "TimeTicks")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
sonusServicesMIBs, = mibBuilder.importSymbols("SONUS-SMI", "sonusServicesMIBs")
SonusName, PointCode = mibBuilder.importSymbols("SONUS-TC", "SonusName", "PointCode")
sonusTcapClientServicesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4))
sonusTcapClientServicesMIB.setRevisions(('2000-10-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: sonusTcapClientServicesMIB.setRevisionsDescriptions(('This MIB was obsoleted because TCAP services have been removed from the GSX.',))
if mibBuilder.loadTexts: sonusTcapClientServicesMIB.setLastUpdated('200102030000Z')
if mibBuilder.loadTexts: sonusTcapClientServicesMIB.setOrganization('Sonus Networks, Inc.')
if mibBuilder.loadTexts: sonusTcapClientServicesMIB.setContactInfo(' Customer Support Sonus Networks, Inc, 5 carlisle Road Westford, MA 01886 USA Tel: 978-692-8999 Fax: 978-392-9118 E-mail: cs.snmp@sonusnet.com')
if mibBuilder.loadTexts: sonusTcapClientServicesMIB.setDescription('The MIB Module for TCAP Client Services Management.')
sonusTcapClientServicesMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1))
sonusScpAdmn = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1))
sonusScpAdmnNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusScpAdmnNextIndex.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpAdmnNextIndex.setDescription('The next valid index to use when creating an entry in the sonusScpAdmnTable.')
sonusScpAdmnTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2), )
if mibBuilder.loadTexts: sonusScpAdmnTable.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpAdmnTable.setDescription('This table contains information about each SCP configured to provide a particular TCAP application service. A management entity may create rows for SCP that are anticipated to provide services in the future.')
sonusScpAdmnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1), ).setIndexNames((0, "SONUS-TCAP-CLIENT-SERVICES-MIB", "sonusScpAdmnIndex"))
if mibBuilder.loadTexts: sonusScpAdmnEntry.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpAdmnEntry.setDescription("This table describes the SCPs' configurations that GSX9000 node has access to their services.")
sonusScpAdmnIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusScpAdmnIndex.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpAdmnIndex.setDescription('A unique value for each SCP that is between 1 and maximum allowed')
sonusScpAdmnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 2), SonusName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusScpAdmnName.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpAdmnName.setDescription('The name of the SCP.')
sonusScpAdmnCarrier = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 23))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusScpAdmnCarrier.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpAdmnCarrier.setDescription('The name of the carrier using this SCP. ')
sonusScpAdmnNode = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 23))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusScpAdmnNode.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpAdmnNode.setDescription('The name of the SS7 Node connecting to this SCP. ')
sonusScpAdmnPc = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 5), PointCode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusScpAdmnPc.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpAdmnPc.setDescription('The point code of this SCP')
sonusScpAdmnSsn = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusScpAdmnSsn.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpAdmnSsn.setDescription('The subsystem number of this SCP service')
sonusScpAdmnTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusScpAdmnTimeout.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpAdmnTimeout.setDescription('The timeout value of this SCP service')
sonusScpAdmnType = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("tollfree", 1), ("lnp", 2), ("credit", 3), ("authen", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusScpAdmnType.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpAdmnType.setDescription('The type of service of this SCP')
sonusScpAdmnProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("ain", 2), ("inap", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusScpAdmnProtocol.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpAdmnProtocol.setDescription('The encoding/decoding protocol on top of TCAP')
sonusScpAdmnState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusScpAdmnState.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpAdmnState.setDescription('The configured state of the SCP.')
sonusScpAdmnRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 1, 2, 1, 11), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sonusScpAdmnRowStatus.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpAdmnRowStatus.setDescription('')
sonusScpStatTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 2), )
if mibBuilder.loadTexts: sonusScpStatTable.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpStatTable.setDescription('This table contains status information about each SCP')
sonusScpStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 2, 1), ).setIndexNames((0, "SONUS-TCAP-CLIENT-SERVICES-MIB", "sonusScpStatIndex"))
if mibBuilder.loadTexts: sonusScpStatEntry.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpStatEntry.setDescription('This table describes the SCP stat')
sonusScpStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusScpStatIndex.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpStatIndex.setDescription('Identifies the SCP')
sonusScpStatQueryNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusScpStatQueryNum.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpStatQueryNum.setDescription('The total number of queries performed at the moment')
sonusScpStatQueryFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 5, 4, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusScpStatQueryFailed.setStatus('obsolete')
if mibBuilder.loadTexts: sonusScpStatQueryFailed.setDescription('The total number of queries failed at the moment')
mibBuilder.exportSymbols("SONUS-TCAP-CLIENT-SERVICES-MIB", sonusScpStatQueryFailed=sonusScpStatQueryFailed, sonusScpAdmnIndex=sonusScpAdmnIndex, sonusScpStatQueryNum=sonusScpStatQueryNum, sonusTcapClientServicesMIB=sonusTcapClientServicesMIB, sonusScpAdmn=sonusScpAdmn, sonusScpAdmnProtocol=sonusScpAdmnProtocol, sonusScpAdmnRowStatus=sonusScpAdmnRowStatus, sonusScpAdmnCarrier=sonusScpAdmnCarrier, sonusScpAdmnNode=sonusScpAdmnNode, sonusScpAdmnSsn=sonusScpAdmnSsn, sonusScpAdmnNextIndex=sonusScpAdmnNextIndex, sonusTcapClientServicesMIBObjects=sonusTcapClientServicesMIBObjects, sonusScpAdmnState=sonusScpAdmnState, sonusScpAdmnEntry=sonusScpAdmnEntry, sonusScpAdmnType=sonusScpAdmnType, sonusScpStatEntry=sonusScpStatEntry, sonusScpAdmnTable=sonusScpAdmnTable, PYSNMP_MODULE_ID=sonusTcapClientServicesMIB, sonusScpAdmnTimeout=sonusScpAdmnTimeout, sonusScpStatTable=sonusScpStatTable, sonusScpStatIndex=sonusScpStatIndex, sonusScpAdmnPc=sonusScpAdmnPc, sonusScpAdmnName=sonusScpAdmnName)