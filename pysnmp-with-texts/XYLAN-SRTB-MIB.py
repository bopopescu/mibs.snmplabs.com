#
# PySNMP MIB module XYLAN-SRTB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XYLAN-SRTB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:45:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Bits, Counter64, ModuleIdentity, NotificationType, Unsigned32, ObjectIdentity, IpAddress, iso, MibIdentifier, Counter32, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "Counter64", "ModuleIdentity", "NotificationType", "Unsigned32", "ObjectIdentity", "IpAddress", "iso", "MibIdentifier", "Counter32", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
xylanSrtbArch, = mibBuilder.importSymbols("XYLAN-BASE-MIB", "xylanSrtbArch")
xylanSRTB = MibIdentifier((1, 3, 6, 1, 4, 1, 800, 2, 24, 1))
srtbConfigTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 1), )
if mibBuilder.loadTexts: srtbConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: srtbConfigTable.setDescription('This table contains information related to SRTB configuration for the groups in the switch.')
srtbConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 1, 1), ).setIndexNames((0, "XYLAN-SRTB-MIB", "srtbGroupID"))
if mibBuilder.loadTexts: srtbConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: srtbConfigEntry.setDescription('An entry in the SRTB configuration table. Each entry represents a group for which SRTB has been configured.')
srtbGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtbGroupID.setStatus('mandatory')
if mibBuilder.loadTexts: srtbGroupID.setDescription('This object contains the group ID for SRTB is being configured. This object uniquely identifies the group in the switch.')
srtbOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srtbOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: srtbOperStatus.setDescription('This is used to enable/disable SRTB for the group and report on status of SRTB for the group.')
srtbEthernetRingId = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srtbEthernetRingId.setStatus('mandatory')
if mibBuilder.loadTexts: srtbEthernetRingId.setDescription('Ring ID to be assigned to the Ethernet segment. Valid ring-id is from 0x001(1) to 0xFFF(4095). Users can set EthRingID from 1 to 4095. But for 0 which is read-only, is not avaliable for user to set. If 0 is returned (from GET), meaning SRTB is OFF, hence not available for users to configure. ')
srtbExplorerTypeToSend = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(3, 2, 1))).clone(namedValues=NamedValues(("notAvailable", 3), ("typeSTE", 2), ("typeARE", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srtbExplorerTypeToSend.setStatus('mandatory')
if mibBuilder.loadTexts: srtbExplorerTypeToSend.setDescription('The value of this object specifies which explorer type to send when unknown destination, multicast or broadcast frame is forwarded from Ethernet to Token Ring. If notAvailable is returned (from GET), meaning SRTB is OFF, hence not available for users to configure. ')
srtbRIFTable = MibTable((1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 2), )
if mibBuilder.loadTexts: srtbRIFTable.setStatus('mandatory')
if mibBuilder.loadTexts: srtbRIFTable.setDescription('This table is used to display the RIF values cached in the switch and to purge the value stored.')
srtbRIFEntry = MibTableRow((1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 2, 1), ).setIndexNames((0, "XYLAN-SRTB-MIB", "srtbRIFMac"), (0, "XYLAN-SRTB-MIB", "srtbRIFGroupID"))
if mibBuilder.loadTexts: srtbRIFEntry.setStatus('mandatory')
if mibBuilder.loadTexts: srtbRIFEntry.setDescription('An entry in the srtbRIF table.')
srtbRIFMac = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 2, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtbRIFMac.setStatus('mandatory')
if mibBuilder.loadTexts: srtbRIFMac.setDescription('This object contains the MAC address associated with the RIF.')
srtbRIFGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtbRIFGroupID.setStatus('mandatory')
if mibBuilder.loadTexts: srtbRIFGroupID.setDescription('This object uniquely identifies the group in the Xylan switch.')
srtbRIFString = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 2, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: srtbRIFString.setStatus('mandatory')
if mibBuilder.loadTexts: srtbRIFString.setDescription('This object contains the RIF that has been cached for MAC address associated with the entry.')
srtbRIFPurge = MibTableColumn((1, 3, 6, 1, 4, 1, 800, 2, 24, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAction", 1), ("purgeRif", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srtbRIFPurge.setStatus('mandatory')
if mibBuilder.loadTexts: srtbRIFPurge.setDescription('This object when set to 2 causes the RIF associated with the MAC address to be purged.')
mibBuilder.exportSymbols("XYLAN-SRTB-MIB", srtbConfigEntry=srtbConfigEntry, srtbEthernetRingId=srtbEthernetRingId, srtbOperStatus=srtbOperStatus, srtbRIFEntry=srtbRIFEntry, srtbRIFString=srtbRIFString, srtbGroupID=srtbGroupID, srtbRIFMac=srtbRIFMac, srtbConfigTable=srtbConfigTable, srtbRIFGroupID=srtbRIFGroupID, xylanSRTB=xylanSRTB, srtbRIFPurge=srtbRIFPurge, srtbExplorerTypeToSend=srtbExplorerTypeToSend, srtbRIFTable=srtbRIFTable)