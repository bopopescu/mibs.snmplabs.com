#
# PySNMP MIB module ONEACCESS-VLAN-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-VLAN-CONFIG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:34:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
oacExpIMIp, oacMIBModules = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMIp", "oacMIBModules")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, ObjectIdentity, TimeTicks, Bits, IpAddress, ModuleIdentity, Integer32, iso, Gauge32, Unsigned32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "TimeTicks", "Bits", "IpAddress", "ModuleIdentity", "Integer32", "iso", "Gauge32", "Unsigned32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
oaVlanConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 681))
oaVlanConfigMIB.setRevisions(('2011-06-15 00:00', '2010-07-08 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: oaVlanConfigMIB.setRevisionsDescriptions(('Fixed minor corrections.', "This MIB defines configuration capabilities relating to Vlan, Vlan QinQ and Vlan Mapping on interfaces. IEEE 802.1Q VLAN specification provides for an option to tag Ethernet frames with two VLAN tags: - An inner tag that specifies the customer's VLAN ID. This tag is called the 'C-VLAN'. - An outer tag that specifies the service provider's VLAN ID. This tag is called the 'SP-VLAN'.",))
if mibBuilder.loadTexts: oaVlanConfigMIB.setLastUpdated('201106150000Z')
if mibBuilder.loadTexts: oaVlanConfigMIB.setOrganization(' OneAccess ')
if mibBuilder.loadTexts: oaVlanConfigMIB.setContactInfo('Pascal KESTELOOT Postal: ONE ACCESS 381 Avenue du Gnral de Gaulle 92140 Clamart, France FRANCE Tel: (+33) 01 41 87 70 00 Fax: (+33) 01 41 87 74 00 E-mail: pascal.kesteloot@oneaccess-net.com')
if mibBuilder.loadTexts: oaVlanConfigMIB.setDescription('Contact updated')
class SPVlanEtherType(TextualConvention, Integer32):
    description = 'This textual convention defines the different EtherType of a SPVLAN. etherType-8100 - Specifies Ethertype value 0x8100, as defined in IEEE Standard 802.1q etherType-9100 - Specifies Ethertype value 0x9100 etherType-88a8 - Specifies Ethertype value 0x88a8, as defined in IEEE Standard 802.1ad '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("etherType-8100", 1), ("etherType-9100", 2), ("etherType-88a8", 3))

oacVlanConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6))
oacVlanConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1))
oacVlanConfigConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 2))
oacVlanMappingConfigInterfaceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 1))
oacVlanConfigInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 1, 1), )
if mibBuilder.loadTexts: oacVlanConfigInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: oacVlanConfigInterfaceTable.setDescription('This table contains the Vlan or Vlan QinQ configuration on interfaces. The ifIndex in the INDEX clause identifies the interface where Vlan configuration is applied')
oacVlanConfigInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: oacVlanConfigInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: oacVlanConfigInterfaceEntry.setDescription('An entry in this table defines a Vlan interface.')
oacVlanConfigInterfaceDot1qValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacVlanConfigInterfaceDot1qValue.setStatus('current')
if mibBuilder.loadTexts: oacVlanConfigInterfaceDot1qValue.setDescription('The VLAN IDs of a frame. Default Value 0 for no VLAN ID configured.')
oacVlanConfigInterfaceSecondDot1qValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacVlanConfigInterfaceSecondDot1qValue.setStatus('current')
if mibBuilder.loadTexts: oacVlanConfigInterfaceSecondDot1qValue.setDescription('The Second VLAN IDs of a QinQ frame. Default Value 0 for no Second VLAN ID configured.')
oacVlanConfigInterfaceDefaultPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacVlanConfigInterfaceDefaultPriority.setStatus('current')
if mibBuilder.loadTexts: oacVlanConfigInterfaceDefaultPriority.setDescription('Default IEEE 802.1p class of service/user priority By default Value = 0.')
oacVlanConfigInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oacVlanConfigInterfaceRowStatus.setStatus('current')
if mibBuilder.loadTexts: oacVlanConfigInterfaceRowStatus.setDescription('This object allows the creation, modification, or deletion of the row')
oacVlanMappingConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 2))
vlanMappingTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 2, 1), )
if mibBuilder.loadTexts: vlanMappingTable.setStatus('current')
if mibBuilder.loadTexts: vlanMappingTable.setDescription('This table contains the Vlan Mapping configuration on interfaces. The ifIndex in the INDEX clause identifies the interface where Vlan Mapping is applied.')
vlanMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ONEACCESS-VLAN-CONFIG-MIB", "outerSPVlan"))
if mibBuilder.loadTexts: vlanMappingEntry.setStatus('current')
if mibBuilder.loadTexts: vlanMappingEntry.setDescription('An entry in this table defines a QinQ interface.')
innerCVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: innerCVlan.setStatus('current')
if mibBuilder.loadTexts: innerCVlan.setDescription('The CVLAN IDs of the inner tag of a QinQ frame. Authorized value: untagged - specify untagged frame vlanid - CVlan ID (example 100) range - A range of cvlan id (example 100-120) default - All other CVlan not matched ')
outerSPVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 2, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: outerSPVlan.setStatus('current')
if mibBuilder.loadTexts: outerSPVlan.setDescription('The SPVLAN ID of the outer tag of a QinQ frame.')
outerEtherType = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 2, 1, 1, 3), SPVlanEtherType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: outerEtherType.setStatus('current')
if mibBuilder.loadTexts: outerEtherType.setDescription('This textual convention defines the different EtherType of a SPVLAN. etherType-8100 - Specifies Ethertype value 0x8100, as defined in IEEE Standard 802.1q etherType-9100 - Specifies Ethertype value 0x9100 etherType-88a8 - Specifies Ethertype value 0x88a8, as defined in IEEE Standard 802.1ad ')
vlanMappingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 6, 1, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanMappingRowStatus.setStatus('current')
if mibBuilder.loadTexts: vlanMappingRowStatus.setDescription('This object allows the creation, modification, or deletion of the row')
mibBuilder.exportSymbols("ONEACCESS-VLAN-CONFIG-MIB", oacVlanConfig=oacVlanConfig, vlanMappingEntry=vlanMappingEntry, outerEtherType=outerEtherType, oacVlanConfigInterfaceSecondDot1qValue=oacVlanConfigInterfaceSecondDot1qValue, oacVlanConfigObjects=oacVlanConfigObjects, vlanMappingRowStatus=vlanMappingRowStatus, oacVlanConfigInterfaceDot1qValue=oacVlanConfigInterfaceDot1qValue, SPVlanEtherType=SPVlanEtherType, oacVlanMappingConfigInterfaceObjects=oacVlanMappingConfigInterfaceObjects, oaVlanConfigMIB=oaVlanConfigMIB, vlanMappingTable=vlanMappingTable, outerSPVlan=outerSPVlan, oacVlanConfigInterfaceTable=oacVlanConfigInterfaceTable, PYSNMP_MODULE_ID=oaVlanConfigMIB, oacVlanConfigInterfaceDefaultPriority=oacVlanConfigInterfaceDefaultPriority, innerCVlan=innerCVlan, oacVlanConfigInterfaceRowStatus=oacVlanConfigInterfaceRowStatus, oacVlanConfigConformance=oacVlanConfigConformance, oacVlanMappingConfigObjects=oacVlanMappingConfigObjects, oacVlanConfigInterfaceEntry=oacVlanConfigInterfaceEntry)