#
# PySNMP MIB module HPN-ICF-MPLSTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-MPLSTE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:40:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, ModuleIdentity, Integer32, IpAddress, MibIdentifier, Counter64, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Integer32", "IpAddress", "MibIdentifier", "Counter64", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter32", "ObjectIdentity", "iso")
TextualConvention, TruthValue, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "RowStatus", "DisplayString")
hpnicfMplsTe = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143))
hpnicfMplsTe.setRevisions(('2013-06-13 18:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfMplsTe.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: hpnicfMplsTe.setLastUpdated('201306131800Z')
if mibBuilder.loadTexts: hpnicfMplsTe.setOrganization('')
if mibBuilder.loadTexts: hpnicfMplsTe.setContactInfo('')
if mibBuilder.loadTexts: hpnicfMplsTe.setDescription('Multiprotocol Label Switching Traffic Engineering MIB')
hpnicfMplsTeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1))
hpnicfMplsTeScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 1))
hpnicfMplsTeStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfMplsTeStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfMplsTeStatus.setDescription('The global configuration of MPLS(Multiprotocol Label Switching) TE(Traffic Engineering).')
hpnicfMplsTeRsvpStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfMplsTeRsvpStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfMplsTeRsvpStatus.setDescription('The global configuration of RSVP(Resource Reservation Protocol).')
hpnicfMplsTeTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 2), )
if mibBuilder.loadTexts: hpnicfMplsTeTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfMplsTeTable.setDescription('A table for configuring MPLS TE parameters.')
hpnicfMplsTeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-MPLSTE-MIB", "hpnicfMplsTeIndex"))
if mibBuilder.loadTexts: hpnicfMplsTeEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfMplsTeEntry.setDescription('An entry for configuring MPLS TE parameters.')
hpnicfMplsTeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: hpnicfMplsTeIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfMplsTeIndex.setDescription('Index of TE interface.')
hpnicfMplsTeCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 2, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfMplsTeCapability.setStatus('current')
if mibBuilder.loadTexts: hpnicfMplsTeCapability.setDescription('The TE capability of an interface.')
hpnicfMplsTeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfMplsTeRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfMplsTeRowStatus.setDescription("Operation status of this table entry. A row entry cannot be modified when the value of this object is 'active'.")
hpnicfMplsTeRsvpTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 3), )
if mibBuilder.loadTexts: hpnicfMplsTeRsvpTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfMplsTeRsvpTable.setDescription('A table for configuring RSVP(Resource Reservation Protocol) TE parameters.')
hpnicfMplsTeRsvpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 3, 1), ).setIndexNames((0, "HPN-ICF-MPLSTE-MIB", "hpnicfMplsTeRsvpIndex"))
if mibBuilder.loadTexts: hpnicfMplsTeRsvpEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfMplsTeRsvpEntry.setDescription('An entry for configuring RSVP TE parameters.')
hpnicfMplsTeRsvpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: hpnicfMplsTeRsvpIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfMplsTeRsvpIndex.setDescription('Index of RSVP interface.')
hpnicfMplsTeRsvpCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 3, 1, 2), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfMplsTeRsvpCapability.setStatus('current')
if mibBuilder.loadTexts: hpnicfMplsTeRsvpCapability.setDescription('The RSVP capability of an interface.')
hpnicfMplsTeRsvpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 143, 1, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfMplsTeRsvpRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfMplsTeRsvpRowStatus.setDescription("Operation status of this table entry. A row entry cannot be modified when the value of this object is 'active'.")
mibBuilder.exportSymbols("HPN-ICF-MPLSTE-MIB", hpnicfMplsTeScalarGroup=hpnicfMplsTeScalarGroup, hpnicfMplsTeRsvpEntry=hpnicfMplsTeRsvpEntry, hpnicfMplsTeRowStatus=hpnicfMplsTeRowStatus, hpnicfMplsTeObjects=hpnicfMplsTeObjects, hpnicfMplsTeTable=hpnicfMplsTeTable, hpnicfMplsTeStatus=hpnicfMplsTeStatus, hpnicfMplsTe=hpnicfMplsTe, hpnicfMplsTeCapability=hpnicfMplsTeCapability, hpnicfMplsTeIndex=hpnicfMplsTeIndex, hpnicfMplsTeRsvpIndex=hpnicfMplsTeRsvpIndex, hpnicfMplsTeRsvpCapability=hpnicfMplsTeRsvpCapability, hpnicfMplsTeRsvpTable=hpnicfMplsTeRsvpTable, hpnicfMplsTeEntry=hpnicfMplsTeEntry, hpnicfMplsTeRsvpRowStatus=hpnicfMplsTeRsvpRowStatus, hpnicfMplsTeRsvpStatus=hpnicfMplsTeRsvpStatus, PYSNMP_MODULE_ID=hpnicfMplsTe)