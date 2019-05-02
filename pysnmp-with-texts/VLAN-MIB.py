#
# PySNMP MIB module VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:34:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
preDot1qVlanMIB, = mibBuilder.importSymbols("Fore-Common-MIB", "preDot1qVlanMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, IpAddress, Unsigned32, Counter32, TimeTicks, iso, Integer32, Bits, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Unsigned32", "Counter32", "TimeTicks", "iso", "Integer32", "Bits", "Gauge32", "MibIdentifier")
TextualConvention, TestAndIncr, MacAddress, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TestAndIncr", "MacAddress", "RowStatus", "DisplayString")
vlanMIBObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 1, 8, 1))
if mibBuilder.loadTexts: vlanMIBObjects.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: vlanMIBObjects.setOrganization('FORE')
if mibBuilder.loadTexts: vlanMIBObjects.setContactInfo(' Postal: FORE Systems Inc. 1000 FORE Drive Warrendale, PA 15086-7502 Tel: +1 724 742 6900 Email: nm_mibs@fore.com Web: http://www.fore.com')
if mibBuilder.loadTexts: vlanMIBObjects.setDescription(" This module contains definitions for management information for pre-standards IEEE 802.1Q VLANs and their association with a Lan Emulation Client (lec). Devices implementing these pre-standards maintain port groupings and associated filters used to form a 'virtual bridge'.")
vlanConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1))
vlanConfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1), )
if mibBuilder.loadTexts: vlanConfTable.setStatus('current')
if mibBuilder.loadTexts: vlanConfTable.setDescription('A table of VLAN names and characteristics.')
vlanConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1), ).setIndexNames((0, "VLAN-MIB", "vlanName"))
if mibBuilder.loadTexts: vlanConfEntry.setStatus('current')
if mibBuilder.loadTexts: vlanConfEntry.setDescription('A table entry containing VLAN names and characteristics. IMPORTANT: The read-write fields of this table should be modifiable, such that as VLAN characteristics change, the individual parameters in the table can be modified.')
vlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanName.setStatus('current')
if mibBuilder.loadTexts: vlanName.setDescription('The textual name of this VLAN, this is the identifier that the user of a configuration utility will be using. Using a VLAN ID for the index and resolving to a name would be easier for an individual switch. However, the user will not (and should not) use this ID. The problem would then be how to resolve an ID to a Name, given that network manager needs to know this for all devices. Using the name as the index allows a management application to have a list of names and each network device resolves that to a locally significant ID. This means however, if the user configures, via a local interface, two switches with VLANs that have the same name, the network manager will assume that they are the same VLAN. In the future, when the 802.1Q standard comes out, there will be a standard way of maintaining globally unique VLAN IDs because these will be used as the VLAN tag. At that time the index into this table should become the VLAN tag.')
vlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanID.setStatus('current')
if mibBuilder.loadTexts: vlanID.setDescription('This is the locally significant ID that is used internally by this device to reference this VLAN.')
vlanConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanConfRowStatus.setStatus('current')
if mibBuilder.loadTexts: vlanConfRowStatus.setDescription('This object is used to create a new row or to modify or delete an existing row in this table.')
vlanCreatedBy = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanCreatedBy.setStatus('current')
if mibBuilder.loadTexts: vlanCreatedBy.setDescription('This object is used to enter a string to identify the management entity that created this entry.')
vlanType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 5), Integer32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanType.setStatus('current')
if mibBuilder.loadTexts: vlanType.setDescription('The type of vlan, specified as a bitmap. The bitmap indicates all the types of filters that are to be applied to the vlan. The bit locations and meanings are: 0x01 - port-based VLAN 0x02 - MAC-based VLAN 0x04 - protocol-based VLAN 0x08 - IP subnet VLAN for example a VLAN that will look at an incoming port and then apply a MAC filter would use the value 0x03 to indicate both the port and the MAC filters.')
vlanPortGroupInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanPortGroupInstance.setStatus('current')
if mibBuilder.loadTexts: vlanPortGroupInstance.setDescription('The index that identifies the the sub tree in the vlanPortGroupTable that should be walked to retrieve the group of ports in this VLAN. IMPORTANT: This table has slightly different semantics than the next three objects because in all 802 VLANs, in the end they all resolve down to a group of ports. Therefore, this object has the following semantic based on its value and the value of vlanType: vlanType vlanPortGroupInstance mode ------------------ ------------------------------- ---- Port-based set points to a user configured Manual set of ports Port-based not set 0 - There are no ports assigned Auto to this VLAN at this time. Port-based not set non zero - points to a system Auto (agent) maintained list of ports ')
vlanMacListInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanMacListInstance.setStatus('current')
if mibBuilder.loadTexts: vlanMacListInstance.setDescription('If this is a MAC-based VLAN then this is the index that identifies the sub tree in the vlanMacListTable that should be walked to retrieve the list of MAC address to allow into this VLAN. If this is not a MAC-based VLAN then the value is 0')
vlanProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("ethernetv2", 2), ("ieee802dot3", 3))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanProtocolType.setStatus('current')
if mibBuilder.loadTexts: vlanProtocolType.setDescription("If this is a protocol-based VLAN then this is the protocol type whose traffic is allowed into this VLAN. If this is not a protocol-based VLAN the value is 'none'.")
vlanProtocolSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 2))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanProtocolSubtype.setStatus('current')
if mibBuilder.loadTexts: vlanProtocolSubtype.setDescription('If this is a protocol-based VLAN then this is the protocol subtype whose traffic is allowed into this VLAN. This value is based on the protocol type (vlanProtocolType). If the protocol type is Ethernet V2.0 (ethernetv2) then the value is the value assigned by Xerox (two octets). For example, the value 08-00 is the value for IP. If the protocol type is IEEE 802.3 DSAP then the value is the DSAP value (one octet). For example, the value 224 (0xE0) is the value for IPX. If this is not a protocol-based VLAN the value is a zero length octet string.')
vlanIPSubnetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 10), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanIPSubnetAddress.setStatus('current')
if mibBuilder.loadTexts: vlanIPSubnetAddress.setDescription('If this is a subnetBased VLAN then this is the subnet whose traffic is allowed into this VLAN. If this is not a subnetBased VLAN then the value is 0.0.0.0')
vlanBridgeName = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanBridgeName.setStatus('current')
if mibBuilder.loadTexts: vlanBridgeName.setDescription("The textual name of the bridge that is associated with this VLAN. This is provided for those devices that allow multiple bridge (spanning tree) instances under the management of a single agent. If this value is a NULL string, then the default bridge's name will be applied. See the Fore-Bridge-Extensions-MIB for details on how bridges are managed.")
vlanIPMulticastFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanIPMulticastFilter.setStatus('current')
if mibBuilder.loadTexts: vlanIPMulticastFilter.setDescription('This object allows the enabling and disabling of IP multicast filtering on the VLAN.')
vlanPortGroupTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 2), )
if mibBuilder.loadTexts: vlanPortGroupTable.setStatus('current')
if mibBuilder.loadTexts: vlanPortGroupTable.setDescription('A table of port groupings. The first index breaks down the table into multiple port groups. Then the second index is the port that belongs in the group. This way walking the table, given the first index, will give the list of all ports in that group. This allows the user of this MIB to create many port groupings, and then each VLAN can point to the port grouping they want to associate with a particular VLAN. IMPORTANT: This table depends on RFC 1573 extensions to the interfaces.ifTable. This is because, entries in vlanPort can be virtual interfaces (representing LEC instances)')
vlanPortGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 2, 1), ).setIndexNames((0, "VLAN-MIB", "vlanPortGroupIndex"), (0, "VLAN-MIB", "vlanPort"))
if mibBuilder.loadTexts: vlanPortGroupEntry.setStatus('current')
if mibBuilder.loadTexts: vlanPortGroupEntry.setDescription('A table entry containing a port number')
vlanPortGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: vlanPortGroupIndex.setStatus('current')
if mibBuilder.loadTexts: vlanPortGroupIndex.setDescription('Index used so that there can be many different port groups')
vlanPort = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: vlanPort.setStatus('current')
if mibBuilder.loadTexts: vlanPort.setDescription('The value of the instance of the ifIndex object, defined in MIB-II, for the interface corresponding to this port. In the case of a non-atm port this is the physical ifIndex of that port, in the case of an atm port it is the virtual ifIndex that represents the LEC. IMPORTANT: By adding a port here, that port will now be part of any VLAN(s) that this port group is associated with. In addition, if the port is a virtual interface that represents a LEC, the ELAN that that LEC represents will also be part of the VLAN that this port group is associated with. Control of the LECs (creating and assignment) is handled by the ATMF Lan Emulation Client MIB, specifically the lecConfigTable in Configuration Group')
vlanPortGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanPortGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: vlanPortGroupRowStatus.setDescription('This object is used to create a new row or to modify or delete an existing row in this table.')
vlanPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("autoActive", 1), ("allowed", 2), ("allowedActive", 3), ("allowedNotAvail", 4), ("notAssociated", 5))).clone('allowed')).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortStatus.setStatus('current')
if mibBuilder.loadTexts: vlanPortStatus.setDescription("The status of this port relative to the VLAN that points at this port group. The meanings of each value are: autoActive: Means that the port is part of this VLAN because the switch automatically added it. allowed: Means that the port has been configured so that if all other criteria (if any) are met, this port is allowed to be in this VLAN. allowedActive: Means the same as allowed plus the fact that there is a device attached to this port and participating in the VLAN. allowedNotAvail: This value is only needed for devices that don't allow a port to be in more than one VLAN at a time. This value means that this port also exists in some other VLAN(s) and is active in another VLAN. Therefore this port is not available to be used in this VLAN. notAssociated: Means that the Port Group is not currently associated with any VLAN.")
vlanPortGroupNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 3), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanPortGroupNextIndex.setStatus('current')
if mibBuilder.loadTexts: vlanPortGroupNextIndex.setDescription('The index of the next free row in the table.')
vlanMacListTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 4), )
if mibBuilder.loadTexts: vlanMacListTable.setStatus('current')
if mibBuilder.loadTexts: vlanMacListTable.setDescription('A table of MAC Lists. The first index breaks down the table into multiple MAC Lists. Then the second index is the MAC Address that belongs in the group. This way walking the table, given the first index, will give the list of all MAC Addresses in that group. This allows the user of this MIB to create many MAC Lists, and then each VLAN can point to the MAC List they want to associate with a particular VLAN.')
vlanMacListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 4, 1), ).setIndexNames((0, "VLAN-MIB", "vlanMacListIndex"), (0, "VLAN-MIB", "vlanMacAddress"))
if mibBuilder.loadTexts: vlanMacListEntry.setStatus('current')
if mibBuilder.loadTexts: vlanMacListEntry.setDescription('A table entry containing MAC Addresses')
vlanMacListNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 4, 2), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanMacListNextIndex.setStatus('current')
if mibBuilder.loadTexts: vlanMacListNextIndex.setDescription('The index of the next free row in the table.')
vlanMacListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: vlanMacListIndex.setStatus('current')
if mibBuilder.loadTexts: vlanMacListIndex.setDescription('Index used so that there can be many different MAC Lists')
vlanMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 4, 1, 2), MacAddress())
if mibBuilder.loadTexts: vlanMacAddress.setStatus('current')
if mibBuilder.loadTexts: vlanMacAddress.setDescription('The MAC Address that belongs to this group. Adding a new MAC Address will mean that packets from that MAC are allow to be sent on the VLAN that this MAC List is associated with.')
vlanMacListRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 4, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanMacListRowStatus.setStatus('current')
if mibBuilder.loadTexts: vlanMacListRowStatus.setDescription('This object is used to create a new row or to modify or delete an existing row in this table.')
mibBuilder.exportSymbols("VLAN-MIB", vlanPortGroupTable=vlanPortGroupTable, vlanMIBObjects=vlanMIBObjects, vlanPortGroupNextIndex=vlanPortGroupNextIndex, vlanID=vlanID, vlanPortGroupInstance=vlanPortGroupInstance, vlanMacListIndex=vlanMacListIndex, vlanConfRowStatus=vlanConfRowStatus, vlanConfTable=vlanConfTable, vlanMacAddress=vlanMacAddress, vlanIPSubnetAddress=vlanIPSubnetAddress, vlanType=vlanType, vlanMacListEntry=vlanMacListEntry, vlanProtocolType=vlanProtocolType, vlanMacListNextIndex=vlanMacListNextIndex, vlanIPMulticastFilter=vlanIPMulticastFilter, vlanPortGroupIndex=vlanPortGroupIndex, vlanCreatedBy=vlanCreatedBy, PYSNMP_MODULE_ID=vlanMIBObjects, vlanPortStatus=vlanPortStatus, vlanName=vlanName, vlanPortGroupRowStatus=vlanPortGroupRowStatus, vlanPortGroupEntry=vlanPortGroupEntry, vlanConfGroup=vlanConfGroup, vlanProtocolSubtype=vlanProtocolSubtype, vlanPort=vlanPort, vlanMacListRowStatus=vlanMacListRowStatus, vlanMacListInstance=vlanMacListInstance, vlanBridgeName=vlanBridgeName, vlanConfEntry=vlanConfEntry, vlanMacListTable=vlanMacListTable)