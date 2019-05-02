#
# PySNMP MIB module HPN-ICF-FDMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-FDMI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:39:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
FcNameIdOrZero, fcmInstanceIndex = mibBuilder.importSymbols("FC-MGMT-MIB", "FcNameIdOrZero", "fcmInstanceIndex")
hpnicfSan, = mibBuilder.importSymbols("HPN-ICF-VSAN-MIB", "hpnicfSan")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, ModuleIdentity, Unsigned32, Integer32, Gauge32, TimeTicks, Bits, ObjectIdentity, MibIdentifier, Counter64, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "ModuleIdentity", "Unsigned32", "Integer32", "Gauge32", "TimeTicks", "Bits", "ObjectIdentity", "MibIdentifier", "Counter64", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
T11FabricIndex, = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")
hpnicfFdmi = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7))
hpnicfFdmi.setRevisions(('2012-06-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfFdmi.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: hpnicfFdmi.setLastUpdated('201206180000Z')
if mibBuilder.loadTexts: hpnicfFdmi.setOrganization('')
if mibBuilder.loadTexts: hpnicfFdmi.setContactInfo('')
if mibBuilder.loadTexts: hpnicfFdmi.setDescription('This MIB module is for monitoring Fabric Device Management Interface (FDMI) related entities. This MIB module defines objects for managing the devices such as Host Bus Adapter (HBA). It provides device information which has been registered with an Fibre Channel (FC) fabric using FDMI. For more information on FDMI, refer to Fibre Channel Generic Services-6 Section 6.7 : Fabric Device Management Interface.')
hpnicfFdmiObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1))
hpnicfFdmiInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1))
hpnicfFdmiHbaInfoTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1), )
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoTable.setDescription('This table lists all the HBAs registered with the Fabric Device Management Interface.')
hpnicfFdmiHbaInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "HPN-ICF-FDMI-MIB", "hpnicfFdmiHbaInfoFabricIndex"), (0, "HPN-ICF-FDMI-MIB", "hpnicfFdmiHbaInfoId"))
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoEntry.setDescription('An entry (conceptual row) in this table. It provides information that has been registered with FDMI by a HBA, on the Virtual Storage Area Network (VSAN) where the registration was received. If the HBA has registered some but not all of the information represented by the columnar objects in this table, then the value of the unregistered objects will be either the zero-length string (for string-based objects) or the zero value (for integer-based objects).')
hpnicfFdmiHbaInfoFabricIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 1), T11FabricIndex())
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoFabricIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoFabricIndex.setDescription('The ID of the VSAN.')
hpnicfFdmiHbaInfoId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 2), FcNameIdOrZero())
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoId.setReference('Fibre Channel Generic Services-6 Rev 9.4 Section 6.7.4.5.1 .')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoId.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoId.setDescription('The World Wide Name (WWN) of this HBA.')
hpnicfFdmiHbaInfoNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 3), FcNameIdOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoNodeName.setReference('Fibre Channel Generic Services-6 Rev 9.4 Section 6.7.4.4.2.6 .')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoNodeName.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoNodeName.setDescription('The WWN of the node containing this HBA. ')
hpnicfFdmiHbaInfoMfg = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoMfg.setReference('Fibre Channel Generic Services-6 Rev 9.4 Section 6.7.4.4.2.2 .')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoMfg.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoMfg.setDescription('The name of the manufacturer of this HBA.')
hpnicfFdmiHbaInfoSn = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoSn.setReference('Fibre Channel Generic Services-6 Rev 9.4 Section 6.7.4.4.2.3 .')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoSn.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoSn.setDescription('The serial number of this HBA.')
hpnicfFdmiHbaInfoModel = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoModel.setReference('Fibre Channel Generic Services-6 Rev 9.4 Section 6.7.4.4.2.4 .')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoModel.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoModel.setDescription('The model of this HBA.')
hpnicfFdmiHbaInfoModelDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoModelDescr.setReference('Fibre Channel Generic Services-6 Rev 9.4 Section 6.7.4.4.2.5 .')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoModelDescr.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoModelDescr.setDescription('The string that describes the model of this HBA.')
hpnicfFdmiHbaInfoHwVer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoHwVer.setReference('Fibre Channel Generic Services-6 Rev 9.4 Section 6.7.4.4.2.8 .')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoHwVer.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoHwVer.setDescription('The hardware version of this HBA.')
hpnicfFdmiHbaInfoDriverVer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoDriverVer.setReference('Fibre Channel Generic Services-6 Rev 9.4 Section 6.7.4.4.2.9 .')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoDriverVer.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoDriverVer.setDescription('The version of the driver software controlling this HBA.')
hpnicfFdmiHbaInfoOptROMVer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 10), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoOptROMVer.setReference('Fibre Channel Generic Services-6 Rev 9.4 Section 6.7.4.4.2.10 .')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoOptROMVer.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoOptROMVer.setDescription('The version of the Option ROM or the BIOS of this HBA.')
hpnicfFdmiHbaInfoFwVer = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 11), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoFwVer.setReference('Fibre Channel Generic Services-6 Rev 9.4 Section 6.7.4.4.2.11 .')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoFwVer.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoFwVer.setDescription('The version of the firmware executed by this HBA.')
hpnicfFdmiHbaInfoOSInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoOSInfo.setReference('Fibre Channel Generic Services-6 Rev 9.4 Section 6.7.4.4.2.12 .')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoOSInfo.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoOSInfo.setDescription('The type and version of the operating system controlling this HBA.')
hpnicfFdmiHbaInfoMaxCTPayload = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoMaxCTPayload.setReference('Fibre Channel Generic Services-6 Rev 9.4 Section 6.7.4.4.2.13 .')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoMaxCTPayload.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaInfoMaxCTPayload.setDescription('The maximum size of the Common Transport (CT) payload including all CT headers but no FC frame headers, that may be sent or received by application software resident in the host containing this HBA. The unit is 32-bit words.')
hpnicfFdmiHbaPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 2), )
if mibBuilder.loadTexts: hpnicfFdmiHbaPortTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaPortTable.setDescription('List of ports registered with Fabric Device Management Interface.')
hpnicfFdmiHbaPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 2, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "HPN-ICF-FDMI-MIB", "hpnicfFdmiHbaInfoFabricIndex"), (0, "HPN-ICF-FDMI-MIB", "hpnicfFdmiHbaInfoId"), (0, "HPN-ICF-FDMI-MIB", "hpnicfFdmiHbaPortId"))
if mibBuilder.loadTexts: hpnicfFdmiHbaPortEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaPortEntry.setDescription('An entry (conceptual row) in this table. It contains information about the Nx_port on the HBA, on the VSAN where the registration of the HBA with FDMI was received. If the HBA has registered some but not all of the information represented by the columnar objects in this table, then the value of the unregistered objects will be either the zero-length string (for string-based objects) or the zero value (for integer-based objects).')
hpnicfFdmiHbaPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 2, 1, 1), FcNameIdOrZero())
if mibBuilder.loadTexts: hpnicfFdmiHbaPortId.setReference('Fibre Channel Generic Services-6 Rev 9.4 Section 6.7.4.4.3.3 .')
if mibBuilder.loadTexts: hpnicfFdmiHbaPortId.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaPortId.setDescription('The WWN of the port.')
hpnicfFdmiHbaPortSupportedFC4Type = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(32, 32), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFdmiHbaPortSupportedFC4Type.setReference('Fibre Channel Generic Services-6 Rev 9.4 Section 6.7.4.4.3.6 and Section 5.2.3.8 . ')
if mibBuilder.loadTexts: hpnicfFdmiHbaPortSupportedFC4Type.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaPortSupportedFC4Type.setDescription('The supported FC-4 types attribute registered for this port on this VSAN. This is an array of 256 bits (32 bytes). The order of the bits in the 256-bit (32-byte) value is represented in network-byte order. If no FC-4 types has been registered, then the value of this object is the zero-length string.')
hpnicfFdmiHbaPortSupportedSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFdmiHbaPortSupportedSpeed.setReference('Fibre Channel Generic Services-6 Rev 9.4 Section 6.7.4.4.3.8 .')
if mibBuilder.loadTexts: hpnicfFdmiHbaPortSupportedSpeed.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaPortSupportedSpeed.setDescription('The supported speed registered for this port on this VSAN. It is a bitmask that indicates the Fibre Channel Transmission Speeds that are supported on this port.')
hpnicfFdmiHbaPortCurrentSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFdmiHbaPortCurrentSpeed.setReference('Fibre Channel Generic Services-6 Rev 9.4 Section 6.7.4.4.3.9 .')
if mibBuilder.loadTexts: hpnicfFdmiHbaPortCurrentSpeed.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaPortCurrentSpeed.setDescription('The current speed registered for this port on this VSAN. It is a bitmask that indicates the Fibre Channel Transmission Speed at which this port is currently operating.')
hpnicfFdmiHbaPortMaxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFdmiHbaPortMaxFrameSize.setReference('Fibre Channel Generic Services-6 Rev 9.4 Section 6.7.4.4.3.10 .')
if mibBuilder.loadTexts: hpnicfFdmiHbaPortMaxFrameSize.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaPortMaxFrameSize.setDescription('The maximum frame size attribute registered for this port on this VSAN. The unit is bytes.')
hpnicfFdmiHbaPortOsDevName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 2, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFdmiHbaPortOsDevName.setReference('Fibre Channel Generic Services-6 Rev 9.4 Section 6.7.4.4.3.11 .')
if mibBuilder.loadTexts: hpnicfFdmiHbaPortOsDevName.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaPortOsDevName.setDescription('The OS device name attribute registered for this port on this VSAN.')
hpnicfFdmiHbaPortHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 127, 7, 1, 1, 2, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFdmiHbaPortHostName.setReference('Fibre Channel Generic Services-6, Late Comment Section 6.7.4.4.3.12 .')
if mibBuilder.loadTexts: hpnicfFdmiHbaPortHostName.setStatus('current')
if mibBuilder.loadTexts: hpnicfFdmiHbaPortHostName.setDescription('The name of the host associated with this port.')
mibBuilder.exportSymbols("HPN-ICF-FDMI-MIB", hpnicfFdmiObjects=hpnicfFdmiObjects, hpnicfFdmiHbaInfoEntry=hpnicfFdmiHbaInfoEntry, hpnicfFdmiHbaPortSupportedFC4Type=hpnicfFdmiHbaPortSupportedFC4Type, hpnicfFdmi=hpnicfFdmi, hpnicfFdmiHbaInfoMaxCTPayload=hpnicfFdmiHbaInfoMaxCTPayload, PYSNMP_MODULE_ID=hpnicfFdmi, hpnicfFdmiHbaInfoDriverVer=hpnicfFdmiHbaInfoDriverVer, hpnicfFdmiHbaPortCurrentSpeed=hpnicfFdmiHbaPortCurrentSpeed, hpnicfFdmiHbaInfoNodeName=hpnicfFdmiHbaInfoNodeName, hpnicfFdmiHbaInfoTable=hpnicfFdmiHbaInfoTable, hpnicfFdmiHbaInfoFwVer=hpnicfFdmiHbaInfoFwVer, hpnicfFdmiHbaInfoHwVer=hpnicfFdmiHbaInfoHwVer, hpnicfFdmiHbaPortHostName=hpnicfFdmiHbaPortHostName, hpnicfFdmiHbaInfoMfg=hpnicfFdmiHbaInfoMfg, hpnicfFdmiHbaInfoSn=hpnicfFdmiHbaInfoSn, hpnicfFdmiHbaPortTable=hpnicfFdmiHbaPortTable, hpnicfFdmiHbaPortOsDevName=hpnicfFdmiHbaPortOsDevName, hpnicfFdmiHbaPortId=hpnicfFdmiHbaPortId, hpnicfFdmiHbaInfoOptROMVer=hpnicfFdmiHbaInfoOptROMVer, hpnicfFdmiInfo=hpnicfFdmiInfo, hpnicfFdmiHbaInfoFabricIndex=hpnicfFdmiHbaInfoFabricIndex, hpnicfFdmiHbaInfoModel=hpnicfFdmiHbaInfoModel, hpnicfFdmiHbaPortEntry=hpnicfFdmiHbaPortEntry, hpnicfFdmiHbaInfoId=hpnicfFdmiHbaInfoId, hpnicfFdmiHbaInfoModelDescr=hpnicfFdmiHbaInfoModelDescr, hpnicfFdmiHbaInfoOSInfo=hpnicfFdmiHbaInfoOSInfo, hpnicfFdmiHbaPortSupportedSpeed=hpnicfFdmiHbaPortSupportedSpeed, hpnicfFdmiHbaPortMaxFrameSize=hpnicfFdmiHbaPortMaxFrameSize)