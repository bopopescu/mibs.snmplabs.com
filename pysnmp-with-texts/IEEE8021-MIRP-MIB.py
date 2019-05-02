#
# PySNMP MIB module IEEE8021-MIRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IEEE8021-MIRP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:52:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ieee8021BridgeBasePortEntry, = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortEntry")
ieee8021PbbBackboneEdgeBridgeObjects, = mibBuilder.importSymbols("IEEE8021-PBB-MIB", "ieee8021PbbBackboneEdgeBridgeObjects")
IEEE8021BridgePortNumberOrZero, = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021BridgePortNumberOrZero")
VlanIdOrNone, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIdOrNone")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
systemGroup, = mibBuilder.importSymbols("SNMPv2-MIB", "systemGroup")
Counter64, Counter32, NotificationType, TimeTicks, ModuleIdentity, MibIdentifier, Gauge32, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "NotificationType", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Gauge32", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "IpAddress", "Bits")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ieee8021MirpMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 23))
ieee8021MirpMib.setRevisions(('2011-04-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ieee8021MirpMib.setRevisionsDescriptions(('Included in IEEE Std. 802.1Qbe-2011 Copyright (C) IEEE802.1.',))
if mibBuilder.loadTexts: ieee8021MirpMib.setLastUpdated('201104050000Z')
if mibBuilder.loadTexts: ieee8021MirpMib.setOrganization('IEEE 802.1 Working Group')
if mibBuilder.loadTexts: ieee8021MirpMib.setContactInfo('WG-URL: http://grouper.ieee.org/groups/802/1/index.html WG-EMail: stds-802-1@ieee.org Contact: Norman Finn c/o Tony Jeffree, IEEE 802.1 Working Group Chair Postal: IEEE Standards Board 445 Hoes Lane P.O. Box 1331 Piscataway, NJ 08855-1331 USA E-mail: tony@jeffree.co.uk ')
if mibBuilder.loadTexts: ieee8021MirpMib.setDescription('Multiple I-SID Registration Protocol module for managing IEEE 802.1Qbe ')
ieee8021MirpMIBObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 23, 1))
ieee8021MirpConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 23, 2))
ieee8021MirpPortTable = MibTable((1, 3, 111, 2, 802, 1, 1, 23, 1, 1), )
if mibBuilder.loadTexts: ieee8021MirpPortTable.setReference('12.9.2')
if mibBuilder.loadTexts: ieee8021MirpPortTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021MirpPortTable.setDescription('A table that contains controls for the Multiple I-SID Registration Protocol (MIRP) state machines for all of the Ports of a Bridge.')
ieee8021MirpPortEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 23, 1, 1, 1), )
ieee8021BridgeBasePortEntry.registerAugmentions(("IEEE8021-MIRP-MIB", "ieee8021MirpPortEntry"))
ieee8021MirpPortEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021MirpPortEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021MirpPortEntry.setDescription('Each entry contains the MIRP Participant controls for one Port.')
ieee8021MirpPortEnabledStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 23, 1, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021MirpPortEnabledStatus.setReference('12.7.7.1, 12.7.7.2, 39.2.1.11')
if mibBuilder.loadTexts: ieee8021MirpPortEnabledStatus.setStatus('current')
if mibBuilder.loadTexts: ieee8021MirpPortEnabledStatus.setDescription("The state of MIRP operation on this port. The value true(1) indicates that MIRP is enabled on this port, as long as ieee8021PbbMirpEnableStatus is also enabled for this component. When false(2) but ieee8021PbbMirpEnableStatus is still enabled for the device, MIRP is disabled on this port. If MIRP is enabled on a VIP, then the MIRP Participant is enabled on that VIP's PIP. If MIRP is enabled on none of the VIPs on a PIP, then the MIRP Participant on the PIP is diabled; any MIRP packets received will be silently discarded, and no MIRP registrations will be propagated from the PIP. A transition from all VIPs on a PIP false(2) to at least one VIP on the PIP true(1) will cause a reset of all MIRP state machines on this PIP. If MIRP is enabled on any port not a VIP, then the MIRP Participant is enabled on that port. If MIRP is disabled on a non-VIP port, then MIRP packets received will be silently discarded, and no MIRP registrations will be propagated from the port. A transition from false(2) to true(1) will cause a reset of all MIRP state machines on a non-VIP port. The value of this object MUST be retained across reinitializations of the management system.")
ieee8021PbbMirpEnableStatus = MibScalar((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbbMirpEnableStatus.setReference('12.16.1.1.3:i, 12.16.1.2.2:b')
if mibBuilder.loadTexts: ieee8021PbbMirpEnableStatus.setStatus('current')
if mibBuilder.loadTexts: ieee8021PbbMirpEnableStatus.setDescription('The administrative status requested by management for MIRP. The value true(1) indicates that MIRP should be enabled on this component, on all ports for which it has not been specifically disabled. When false(2), MIRP is disabled on all ports. This object affects all MIRP Applicant and Registrar state machines. A transition from false(2) to true(1) will cause a reset of all MIRP state machines on all ports. The value of this object MUST be retained across reinitializations of the management system.')
ieee8021PbbMirpBvid = MibScalar((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 8), VlanIdOrNone()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbbMirpBvid.setReference('12.16.1.1.3:j, 12.16.1.2.2:c')
if mibBuilder.loadTexts: ieee8021PbbMirpBvid.setStatus('current')
if mibBuilder.loadTexts: ieee8021PbbMirpBvid.setDescription('The B-VID to which received MIRPDUs are to be assigned, or 0, if they are to be sent on the CBP PVID.')
ieee8021PbbMirpDestSelector = MibScalar((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cbpMirpGroup", 1), ("cbpMirpVlan", 2), ("cbpMirpTable", 3))).clone('cbpMirpGroup')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbbMirpDestSelector.setReference('Table 8-1, 12.16.1.1.3:k, 12.16.1.2.2:d')
if mibBuilder.loadTexts: ieee8021PbbMirpDestSelector.setStatus('current')
if mibBuilder.loadTexts: ieee8021PbbMirpDestSelector.setDescription('An enumerated value specifying what destination_address and vlan_identifier are to be used when the MIRP Participant transmits an MIRPDU towards the MAC relay entity: cbpMirpGroup (1) Use the Nearest Customer Bridge group address from Table 8-1 with the MIRP B-VID. cbpMirpVlan (2) Use the Nearest Customer Bridge group address from Table 8-1 with the Backbone VLAN Identifier field from the Backbone Service Instance table. cbpMirpTable (3) Use the Default Backbone Destination and Backbone VLAN Identifier fields from the Backbone Service Instance table. The value of this object MUST be retained across reinitializations of the management system.')
ieee8021PbbMirpPnpEnable = MibScalar((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 10), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021PbbMirpPnpEnable.setReference('12.16.1.1.3:j, 12.16.1.2.2:c')
if mibBuilder.loadTexts: ieee8021PbbMirpPnpEnable.setStatus('current')
if mibBuilder.loadTexts: ieee8021PbbMirpPnpEnable.setDescription('A Boolean value specifying the administrative status requested by management for attaching a MIRP Participant to a PNP if and only if this system is a Backbone Edge Bridge (BEB): true(1) The BEB is to attach a MIRP Participant to exactly one Port, either a management Port with no LAN connection external to the BEB, or a PNP. false(2) No MIRP Participant is to be present on any PNP (or on the MAC Relay-facing side of a CBP). The value of this object MUST be retained across reinitializations of the management system. ')
ieee8021PbbMirpPnpPortNumber = MibScalar((1, 3, 111, 2, 802, 1, 1, 9, 1, 1, 1, 11), IEEE8021BridgePortNumberOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021PbbMirpPnpPortNumber.setReference('12.16.1.1.3:j, 12.16.1.2.2:c')
if mibBuilder.loadTexts: ieee8021PbbMirpPnpPortNumber.setStatus('current')
if mibBuilder.loadTexts: ieee8021PbbMirpPnpPortNumber.setDescription('The Bridge Port Number of the Provider Network Port (PNP) that has an associated MIRP Participant, or 0, if no Bridge Port has an associated MIRP Participant. This object indexes an entry in the Bridge Port Table. The system SHALL ensure that either ieee8021PbbMirpPnpPortNumber contains 0, or that the indexed ieee8021BridgeBasePortType object contains the value providerNetworkPort(3).')
ieee8021MirpCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 23, 2, 1))
ieee8021MirpGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 23, 2, 2))
ieee8021MirpReqdGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 23, 2, 2, 1)).setObjects(("IEEE8021-MIRP-MIB", "ieee8021MirpPortEnabledStatus"), ("IEEE8021-MIRP-MIB", "ieee8021PbbMirpEnableStatus"), ("IEEE8021-MIRP-MIB", "ieee8021PbbMirpBvid"), ("IEEE8021-MIRP-MIB", "ieee8021PbbMirpDestSelector"), ("IEEE8021-MIRP-MIB", "ieee8021PbbMirpPnpEnable"), ("IEEE8021-MIRP-MIB", "ieee8021PbbMirpPnpPortNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MirpReqdGroup = ieee8021MirpReqdGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021MirpReqdGroup.setDescription('Objects in the MIRP augmentation required group.')
ieee8021MirpBridgeCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 23, 2, 1, 1)).setObjects(("SNMPv2-MIB", "systemGroup"), ("IEEE8021-MIRP-MIB", "ieee8021MirpReqdGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021MirpBridgeCompliance = ieee8021MirpBridgeCompliance.setStatus('current')
if mibBuilder.loadTexts: ieee8021MirpBridgeCompliance.setDescription('The compliance statement for support by a bridge of the IEEE8021-MIRP-MIB module.')
mibBuilder.exportSymbols("IEEE8021-MIRP-MIB", ieee8021PbbMirpBvid=ieee8021PbbMirpBvid, ieee8021MirpMib=ieee8021MirpMib, ieee8021MirpPortEntry=ieee8021MirpPortEntry, ieee8021MirpGroups=ieee8021MirpGroups, ieee8021MirpMIBObjects=ieee8021MirpMIBObjects, ieee8021MirpBridgeCompliance=ieee8021MirpBridgeCompliance, ieee8021MirpReqdGroup=ieee8021MirpReqdGroup, ieee8021MirpCompliances=ieee8021MirpCompliances, ieee8021MirpPortEnabledStatus=ieee8021MirpPortEnabledStatus, PYSNMP_MODULE_ID=ieee8021MirpMib, ieee8021PbbMirpEnableStatus=ieee8021PbbMirpEnableStatus, ieee8021MirpConformance=ieee8021MirpConformance, ieee8021PbbMirpDestSelector=ieee8021PbbMirpDestSelector, ieee8021PbbMirpPnpPortNumber=ieee8021PbbMirpPnpPortNumber, ieee8021PbbMirpPnpEnable=ieee8021PbbMirpPnpEnable, ieee8021MirpPortTable=ieee8021MirpPortTable)