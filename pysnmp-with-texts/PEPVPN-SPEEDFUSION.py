#
# PySNMP MIB module PEPVPN-SPEEDFUSION (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PEPVPN-SPEEDFUSION
# Produced by pysmi-0.3.4 at Wed May  1 14:40:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, Unsigned32, TimeTicks, NotificationType, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Counter32, ObjectIdentity, iso, Bits, ModuleIdentity, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "TimeTicks", "NotificationType", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Counter32", "ObjectIdentity", "iso", "Bits", "ModuleIdentity", "Integer32", "Gauge32")
RowStatus, TextualConvention, TruthValue, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TruthValue", "MacAddress", "DisplayString")
pepwave = MibIdentifier((1, 3, 6, 1, 4, 1, 27662))
productMib = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200))
generalMib = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1))
pepvpnMib = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10))
pepvpn = ModuleIdentity((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1))
if mibBuilder.loadTexts: pepvpn.setLastUpdated('201305140000Z')
if mibBuilder.loadTexts: pepvpn.setOrganization('PEPWAVE')
if mibBuilder.loadTexts: pepvpn.setContactInfo('')
if mibBuilder.loadTexts: pepvpn.setDescription('MIB module for PepVPN.')
pepVpnInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1))
pepVpnStatusTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2), )
if mibBuilder.loadTexts: pepVpnStatusTable.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusTable.setDescription('PepVpn status table')
pepVpnStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1), ).setIndexNames((0, "PEPVPN-SPEEDFUSION", "pepVpnStatusId"), (0, "PEPVPN-SPEEDFUSION", "pepVpnRemotePeerId"))
if mibBuilder.loadTexts: pepVpnStatusEntry.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusEntry.setDescription('An entry in the pepVpnStatusTable')
pepVpnStatusId = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusId.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusId.setDescription('PepVpn ID.')
pepVpnStatusProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusProfileName.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusProfileName.setDescription('PepVpn profile name.')
pepVpnStatusConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("start", 0), ("authen", 1), ("tunnel", 2), ("route", 3), ("connected", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusConnectionState.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusConnectionState.setDescription('PepVpn connection state.')
pepVpnStatusEncryption = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("na", 0), ("off", 1), ("aes256", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusEncryption.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusEncryption.setDescription('PepVpn encryption.')
pepVpnStatusL2Bridging = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusL2Bridging.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusL2Bridging.setDescription('PepVpn L2 bridging status.')
pepVpnStatusL2Vlan = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusL2Vlan.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusL2Vlan.setDescription('PepVpn L2 VLAN ID. Remark: If the value equals 0, means VLAN ID not applicable in this PepVpn.')
pepVpnRemotePeerId = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnRemotePeerId.setStatus('current')
if mibBuilder.loadTexts: pepVpnRemotePeerId.setDescription('PepVpn remote peer ID.')
pepVpnRemotePeer = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 2, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnRemotePeer.setStatus('current')
if mibBuilder.loadTexts: pepVpnRemotePeer.setDescription('PepVpn remote peer.')
pepVpnStatusWanTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3), )
if mibBuilder.loadTexts: pepVpnStatusWanTable.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusWanTable.setDescription('PepVpn status network WAN table')
pepVpnStatusWanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1), ).setIndexNames((0, "PEPVPN-SPEEDFUSION", "pepVpnStatusId"), (0, "PEPVPN-SPEEDFUSION", "pepVpnRemotePeerId"), (0, "PEPVPN-SPEEDFUSION", "pepVpnStatusWanId"))
if mibBuilder.loadTexts: pepVpnStatusWanEntry.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusWanEntry.setDescription('An entry in the pepVpnStatusWanTable')
pepVpnStatusWanId = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusWanId.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusWanId.setDescription('WAN id.')
pepVpnStatusWanName = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusWanName.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusWanName.setDescription('WAN name.')
pepVpnStatusWanTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusWanTxBytes.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusWanTxBytes.setDescription('WAN transmitted bytes.')
pepVpnStatusWanRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusWanRxBytes.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusWanRxBytes.setDescription('WAN received bytes.')
pepVpnStatusWanDropPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusWanDropPackets.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusWanDropPackets.setDescription('WAN drop packets.')
pepVpnStatusWanLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusWanLatency.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusWanLatency.setDescription('WAN latency(units: ms).')
pepVpnStatusRemoteNetworkTable = MibTable((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 4), )
if mibBuilder.loadTexts: pepVpnStatusRemoteNetworkTable.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusRemoteNetworkTable.setDescription('PepVpn status remote network table')
pepVpnStatusRemoteNetworkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 4, 1), ).setIndexNames((0, "PEPVPN-SPEEDFUSION", "pepVpnStatusId"), (0, "PEPVPN-SPEEDFUSION", "pepVpnRemotePeerId"), (0, "PEPVPN-SPEEDFUSION", "pepVpnStatusRemoteNetowrkId"))
if mibBuilder.loadTexts: pepVpnStatusRemoteNetworkEntry.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusRemoteNetworkEntry.setDescription('An entry in the pepVpnStatusRemoteNetworkTable')
pepVpnStatusRemoteNetowrkId = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusRemoteNetowrkId.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusRemoteNetowrkId.setDescription('PepVpn remote network id.')
pepVpnStatusRemoteNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusRemoteNetwork.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusRemoteNetwork.setDescription('PepVpn remote network IP.')
pepVpnStatusRemoteSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 27662, 200, 1, 10, 1, 1, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pepVpnStatusRemoteSubnet.setStatus('current')
if mibBuilder.loadTexts: pepVpnStatusRemoteSubnet.setDescription('PepVpn remote network subnet.')
mibBuilder.exportSymbols("PEPVPN-SPEEDFUSION", pepVpnInfo=pepVpnInfo, pepVpnRemotePeerId=pepVpnRemotePeerId, pepvpn=pepvpn, productMib=productMib, PYSNMP_MODULE_ID=pepvpn, pepVpnStatusWanId=pepVpnStatusWanId, pepVpnStatusRemoteNetworkEntry=pepVpnStatusRemoteNetworkEntry, generalMib=generalMib, pepVpnStatusRemoteSubnet=pepVpnStatusRemoteSubnet, pepVpnStatusRemoteNetowrkId=pepVpnStatusRemoteNetowrkId, pepVpnStatusWanRxBytes=pepVpnStatusWanRxBytes, pepVpnStatusWanDropPackets=pepVpnStatusWanDropPackets, pepvpnMib=pepvpnMib, pepVpnStatusRemoteNetwork=pepVpnStatusRemoteNetwork, pepVpnStatusConnectionState=pepVpnStatusConnectionState, pepVpnStatusEntry=pepVpnStatusEntry, pepVpnStatusRemoteNetworkTable=pepVpnStatusRemoteNetworkTable, pepwave=pepwave, pepVpnStatusWanLatency=pepVpnStatusWanLatency, pepVpnStatusWanName=pepVpnStatusWanName, pepVpnStatusProfileName=pepVpnStatusProfileName, pepVpnStatusL2Bridging=pepVpnStatusL2Bridging, pepVpnStatusEncryption=pepVpnStatusEncryption, pepVpnStatusL2Vlan=pepVpnStatusL2Vlan, pepVpnStatusWanEntry=pepVpnStatusWanEntry, pepVpnRemotePeer=pepVpnRemotePeer, pepVpnStatusId=pepVpnStatusId, pepVpnStatusTable=pepVpnStatusTable, pepVpnStatusWanTable=pepVpnStatusWanTable, pepVpnStatusWanTxBytes=pepVpnStatusWanTxBytes)