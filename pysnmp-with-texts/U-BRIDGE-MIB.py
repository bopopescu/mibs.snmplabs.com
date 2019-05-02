#
# PySNMP MIB module U-BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/U-BRIDGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:28:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
dot1dBasePortEntry, dot1dBasePort, dot1dBridge = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePortEntry", "dot1dBasePort", "dot1dBridge")
dot1dGmrp, = mibBuilder.importSymbols("P-BRIDGE-MIB", "dot1dGmrp")
dot1qPvid, dot1qVlan = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qPvid", "dot1qVlan")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Unsigned32, IpAddress, iso, Gauge32, Counter64, Integer32, MibIdentifier, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Unsigned32", "IpAddress", "iso", "Gauge32", "Counter64", "Integer32", "MibIdentifier", "ObjectIdentity", "Bits")
MacAddress, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TruthValue", "TextualConvention", "DisplayString")
uBridgeMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 17, 12))
uBridgeMIB.setRevisions(('2001-11-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: uBridgeMIB.setRevisionsDescriptions(('Draft 1',))
if mibBuilder.loadTexts: uBridgeMIB.setLastUpdated('200111160000Z')
if mibBuilder.loadTexts: uBridgeMIB.setOrganization('IETF Bridge MIB Working Group')
if mibBuilder.loadTexts: uBridgeMIB.setContactInfo('Email: Bridge-mib@ietf.org')
if mibBuilder.loadTexts: uBridgeMIB.setDescription('The Bridge MIB Extension module for managing devices that allow control over dynamic VLAN registration through Restricted VLAN Registration as defined by IEEE 802.1u.')
dot1dExtPortGmrpTable = MibTable((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 2), )
if mibBuilder.loadTexts: dot1dExtPortGmrpTable.setStatus('current')
if mibBuilder.loadTexts: dot1dExtPortGmrpTable.setDescription('A table containing per port Restricted Group Registration control information.')
dot1dExtPortGmrpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 2, 1), )
dot1dBasePortEntry.registerAugmentions(("U-BRIDGE-MIB", "dot1dExtPortGmrpEntry"))
dot1dExtPortGmrpEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: dot1dExtPortGmrpEntry.setStatus('current')
if mibBuilder.loadTexts: dot1dExtPortGmrpEntry.setDescription('Information controlling Group Registration for a port on the device. This is indexed by dot1dBasePort.')
dot1dPortRestrictedGroupRegistration = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dPortRestrictedGroupRegistration.setReference('IEEE 802.1t clause 10.3.2.3, 14.10.1.3.')
if mibBuilder.loadTexts: dot1dPortRestrictedGroupRegistration.setStatus('current')
if mibBuilder.loadTexts: dot1dPortRestrictedGroupRegistration.setDescription('The state of Restricted Group Registration on this port. If the value of this control is true(1), then creation of a new dynamic entry is permitted only if there is a Static Filtering Entry for the VLAN concerned, in which the Registrar Administrative Control value is Normal Registration.')
dot1dPortLastGroupFailed = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 2, 1, 2), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dot1dPortLastGroupFailed.setReference('IEEE 802.1t clause 14.10.1.2.3a.')
if mibBuilder.loadTexts: dot1dPortLastGroupFailed.setStatus('current')
if mibBuilder.loadTexts: dot1dPortLastGroupFailed.setDescription('The MAC address of the Group GMRP failed to register on this port. This object is accessible only through gmrpFailure notification.')
dot1dPortGmrpFailingReason = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 6, 1, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lackOfResources", 1), ("registrationRestricted", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dot1dPortGmrpFailingReason.setReference('IEEE 802.1t clause 14.10.1.2.3c.')
if mibBuilder.loadTexts: dot1dPortGmrpFailingReason.setStatus('current')
if mibBuilder.loadTexts: dot1dPortGmrpFailingReason.setDescription("The reason for the last registration failure on this port. The value 'lackofResources(1)' indicates that GMRP failed due to lack of resources in the Filtering Database for the creation of a Group Registration Entry. The value 'registrationRestricted(2)' indicates that GMRP failed because dynamic group is restricted. This object is accessible only through gmrpFailure notification.")
dot1qExtPortVlanTable = MibTable((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 11), )
if mibBuilder.loadTexts: dot1qExtPortVlanTable.setStatus('current')
if mibBuilder.loadTexts: dot1qExtPortVlanTable.setDescription('A table containing per port Restricted VLAN Registration control information.')
dot1qExtPortVlanEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 11, 1), )
dot1dBasePortEntry.registerAugmentions(("U-BRIDGE-MIB", "dot1qExtPortVlanEntry"))
dot1qExtPortVlanEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: dot1qExtPortVlanEntry.setStatus('current')
if mibBuilder.loadTexts: dot1qExtPortVlanEntry.setDescription('Information controlling VLAN Registration for a port on the device. This is indexed by dot1dBasePort.')
dot1qPortRestrictedVlanRegistration = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 11, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1qPortRestrictedVlanRegistration.setReference('IEEE 802.1u clause 11.2.3.2.3, 12.10.1.7.')
if mibBuilder.loadTexts: dot1qPortRestrictedVlanRegistration.setStatus('current')
if mibBuilder.loadTexts: dot1qPortRestrictedVlanRegistration.setDescription('The state of Restricted VLAN Registration on this port. If the value of this control is true(1), then creation of a new dynamic VLAN entry is permitted only if there is a Static VLAN Registration Entry for the VLAN concerned, in which the Registrar Administrative Control value for this port is Normal Registration.')
dot1qPortGvrpFailingReason = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("lackOfResources", 1), ("registrationRestricted", 2), ("unsupportedVID", 3)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dot1qPortGvrpFailingReason.setReference('IEEE 802.1u clause 12.10.1.6.3c.')
if mibBuilder.loadTexts: dot1qPortGvrpFailingReason.setStatus('current')
if mibBuilder.loadTexts: dot1qPortGvrpFailingReason.setDescription("The reason for the last registration failure on this port. The value 'lackofResources(1)' indicates that GVRP failed due to lack of resources in the Filtering Database for the creation of a VLAN Registration Entry. The value 'registrationRestricted(2)' indicates that GVRP failed because dynamic VLAN registration is restricted. And the value 'unsupportedVID(3)' indicates that a registration request for an unsupported VID is received.")
gmrpFailure = NotificationType((1, 3, 6, 1, 2, 1, 17, 0, 3)).setObjects(("U-BRIDGE-MIB", "dot1dPortLastGroupFailed"), ("BRIDGE-MIB", "dot1dBasePort"), ("U-BRIDGE-MIB", "dot1dPortGmrpFailingReason"))
if mibBuilder.loadTexts: gmrpFailure.setStatus('current')
if mibBuilder.loadTexts: gmrpFailure.setDescription('The trap that is generated when there is a GMRP failure. dot1dPortLastGroupFailed indicates the MAC address of the Group that has failed to be registered, dot1dBasePort indicates the port on which the registration is received, and dot1dPortGmrpFailingReason indicates the reason for the failure.')
if mibBuilder.loadTexts: gmrpFailure.setReference('IEEE 802.1t 14.10.1.2.')
gvrpFailure = NotificationType((1, 3, 6, 1, 2, 1, 17, 0, 4)).setObjects(("Q-BRIDGE-MIB", "dot1qPvid"), ("BRIDGE-MIB", "dot1dBasePort"), ("U-BRIDGE-MIB", "dot1qPortGvrpFailingReason"))
if mibBuilder.loadTexts: gvrpFailure.setStatus('current')
if mibBuilder.loadTexts: gvrpFailure.setDescription('The trap that is generated when there is a GVRP failure. dot1qPvid indicates the VID of he VLAN that GVRP has failed to register, dot1dBasePort indicates the port on which the registration is received, and dot1qPortGvrpFailingReason indicates the reason for the failure.')
if mibBuilder.loadTexts: gvrpFailure.setReference('IEEE 802.1t 12.10.1.6.')
uBridgeConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 12, 1))
uBridgeGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 12, 1, 1))
uBridgeCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 12, 1, 2))
uBridgePortVlanGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 12, 1, 1, 1)).setObjects(("U-BRIDGE-MIB", "dot1qPortRestrictedVlanRegistration"), ("U-BRIDGE-MIB", "dot1qPortGvrpFailingReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    uBridgePortVlanGroup = uBridgePortVlanGroup.setStatus('current')
if mibBuilder.loadTexts: uBridgePortVlanGroup.setDescription('Per-port Restricted VLAN Registration Control parameter')
uBridgePortGmrpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 12, 1, 1, 2)).setObjects(("U-BRIDGE-MIB", "dot1dPortRestrictedGroupRegistration"), ("U-BRIDGE-MIB", "dot1dPortLastGroupFailed"), ("U-BRIDGE-MIB", "dot1dPortGmrpFailingReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    uBridgePortGmrpGroup = uBridgePortGmrpGroup.setStatus('current')
if mibBuilder.loadTexts: uBridgePortGmrpGroup.setDescription('Per-port Restricted Group Registration Control parameter')
uBridgeTrapGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 17, 12, 1, 1, 3)).setObjects(("U-BRIDGE-MIB", "gmrpFailure"), ("U-BRIDGE-MIB", "gvrpFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    uBridgeTrapGroup = uBridgeTrapGroup.setStatus('current')
if mibBuilder.loadTexts: uBridgeTrapGroup.setDescription('GMRP and GVRP notifications')
uBridgeCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 17, 12, 1, 2, 1)).setObjects(("U-BRIDGE-MIB", "uBridgePortVlanGroup"), ("U-BRIDGE-MIB", "uBridgePortGmrpGroup"), ("U-BRIDGE-MIB", "uBridgeTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    uBridgeCompliance = uBridgeCompliance.setStatus('current')
if mibBuilder.loadTexts: uBridgeCompliance.setDescription('The compliance statement for device support of bridging services.')
mibBuilder.exportSymbols("U-BRIDGE-MIB", uBridgePortGmrpGroup=uBridgePortGmrpGroup, PYSNMP_MODULE_ID=uBridgeMIB, uBridgeConformance=uBridgeConformance, dot1qPortGvrpFailingReason=dot1qPortGvrpFailingReason, dot1qExtPortVlanEntry=dot1qExtPortVlanEntry, dot1dExtPortGmrpEntry=dot1dExtPortGmrpEntry, dot1dPortRestrictedGroupRegistration=dot1dPortRestrictedGroupRegistration, uBridgeMIB=uBridgeMIB, gvrpFailure=gvrpFailure, gmrpFailure=gmrpFailure, uBridgeCompliance=uBridgeCompliance, uBridgeTrapGroup=uBridgeTrapGroup, dot1qExtPortVlanTable=dot1qExtPortVlanTable, uBridgePortVlanGroup=uBridgePortVlanGroup, dot1qPortRestrictedVlanRegistration=dot1qPortRestrictedVlanRegistration, dot1dPortGmrpFailingReason=dot1dPortGmrpFailingReason, uBridgeCompliances=uBridgeCompliances, dot1dExtPortGmrpTable=dot1dExtPortGmrpTable, dot1dPortLastGroupFailed=dot1dPortLastGroupFailed, uBridgeGroups=uBridgeGroups)