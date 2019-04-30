#
# PySNMP MIB module RAPID-IPSEC-ENDPOINT-PAIR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RAPID-IPSEC-ENDPOINT-PAIR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:43:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
rapidstream, = mibBuilder.importSymbols("RAPID-MIB", "rapidstream")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, ObjectIdentity, Unsigned32, NotificationType, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, MibIdentifier, enterprises, ModuleIdentity, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "ObjectIdentity", "Unsigned32", "NotificationType", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "MibIdentifier", "enterprises", "ModuleIdentity", "Integer32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rsIpsecEndpointPairModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 4355, 5))
rsIpsecEndpointPairModule.setRevisions(('2000-03-21 12:00', '2002-11-01 12:00',))
if mibBuilder.loadTexts: rsIpsecEndpointPairModule.setLastUpdated('9909081200Z')
if mibBuilder.loadTexts: rsIpsecEndpointPairModule.setOrganization('WatchGuard Technologies, Inc.')
rsIpsecEndpointPairMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 5, 1))
if mibBuilder.loadTexts: rsIpsecEndpointPairMIB.setStatus('current')
rsIpsecEndpointPair = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1))
if mibBuilder.loadTexts: rsIpsecEndpointPair.setStatus('current')
rsIpsecEndpointPairStatistics = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2))
if mibBuilder.loadTexts: rsIpsecEndpointPairStatistics.setStatus('current')
rsIpsecEndpointPairNum = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairNum.setStatus('current')
rsIpsecEndpointPairTable = MibTable((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2), )
if mibBuilder.loadTexts: rsIpsecEndpointPairTable.setStatus('current')
rsIpsecEndpointPairEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1), ).setIndexNames((0, "RAPID-IPSEC-ENDPOINT-PAIR-MIB", "rsIpsecEndpointPairIndex"))
if mibBuilder.loadTexts: rsIpsecEndpointPairEntry.setStatus('current')
rsIpsecEndpointPairIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairIndex.setStatus('current')
rsIpsecEndpointPairLocalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairLocalAddr.setStatus('current')
rsIpsecEndpointPairPeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerAddr.setStatus('current')
rsIpsecEndpointPairInSAs = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairInSAs.setStatus('current')
rsIpsecEndpointPairOutSAs = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairOutSAs.setStatus('current')
rsIpsecEndpointPairInAccKbytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 6), Counter32()).setUnits('Kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairInAccKbytes.setStatus('current')
rsIpsecEndpointPairOutAccKbytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 7), Counter32()).setUnits('Kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairOutAccKbytes.setStatus('current')
rsIpsecEndpointPairInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairInPackets.setStatus('current')
rsIpsecEndpointPairOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairOutPackets.setStatus('current')
rsIpsecEndpointPairDecryptErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairDecryptErrors.setStatus('current')
rsIpsecEndpointPairAuthErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairAuthErrors.setStatus('current')
rsIpsecEndpointPairReplayErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairReplayErrors.setStatus('current')
rsIpsecEndpointPairPolicyErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairPolicyErrors.setStatus('current')
rsIpsecEndpointPairPadErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairPadErrors.setStatus('current')
rsIpsecEndpointPairOtherReceiveErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairOtherReceiveErrors.setStatus('current')
rsIpsecEndpointPairSendErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairSendErrors.setStatus('current')
rsIpsecEndpointPairTotalInSAs = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalInSAs.setStatus('current')
rsIpsecEndpointPairTotalOutSAs = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalOutSAs.setStatus('current')
rsIpsecEndpointPairTotalInAccKbytes = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 3), Counter32()).setUnits('Kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalInAccKbytes.setStatus('current')
rsIpsecEndpointPairTotalOutAccKbytes = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalOutAccKbytes.setStatus('current')
rsIpsecEndpointPairTotalInPackets = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 5), Counter32()).setUnits('Kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalInPackets.setStatus('current')
rsIpsecEndpointPairTotalOutPackets = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalOutPackets.setStatus('current')
rsIpsecEndpointPairTotalDecryptErrors = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalDecryptErrors.setStatus('current')
rsIpsecEndpointPairTotalAuthErrors = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalAuthErrors.setStatus('current')
rsIpsecEndpointPairTotalReplayErrors = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalReplayErrors.setStatus('current')
rsIpsecEndpointPairTotalPolicyErrors = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalPolicyErrors.setStatus('current')
rsIpsecEndpointPairTotalPadErrors = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalPadErrors.setStatus('current')
rsIpsecEndpointPairTotalOtherReceiveErrors = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalOtherReceiveErrors.setStatus('current')
rsIpsecEndpointPairTotalSendErrors = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 2, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairTotalSendErrors.setStatus('current')
rsIpsecEndpointPairPeerIPToTunnel = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 5, 1, 3))
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerIPToTunnel.setStatus('current')
rsIpsecEndpointPairPeerIPToTunnelNum = MibScalar((1, 3, 6, 1, 4, 1, 4355, 5, 1, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerIPToTunnelNum.setStatus('current')
rsIpsecEndpointPairPeerIPToTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 4355, 5, 1, 3, 2), )
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerIPToTunnelTable.setStatus('current')
rsIpsecEndpointPairPeerIPToTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4355, 5, 1, 3, 2, 1), ).setIndexNames((0, "RAPID-IPSEC-ENDPOINT-PAIR-MIB", "rsIpsecEndpointPairPeerIPToTunnelPeerIP"), (0, "RAPID-IPSEC-ENDPOINT-PAIR-MIB", "rsIpsecEndpointPairPeerIPToTunnelTunnelID"))
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerIPToTunnelEntry.setStatus('current')
rsIpsecEndpointPairPeerIPToTunnelPeerIP = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 3, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerIPToTunnelPeerIP.setStatus('current')
rsIpsecEndpointPairPeerIPToTunnelTunnelID = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 5, 1, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecEndpointPairPeerIPToTunnelTunnelID.setStatus('current')
mibBuilder.exportSymbols("RAPID-IPSEC-ENDPOINT-PAIR-MIB", rsIpsecEndpointPairEntry=rsIpsecEndpointPairEntry, rsIpsecEndpointPairInAccKbytes=rsIpsecEndpointPairInAccKbytes, rsIpsecEndpointPairReplayErrors=rsIpsecEndpointPairReplayErrors, rsIpsecEndpointPairPolicyErrors=rsIpsecEndpointPairPolicyErrors, rsIpsecEndpointPairTotalOutPackets=rsIpsecEndpointPairTotalOutPackets, rsIpsecEndpointPairTotalInAccKbytes=rsIpsecEndpointPairTotalInAccKbytes, rsIpsecEndpointPair=rsIpsecEndpointPair, rsIpsecEndpointPairPeerIPToTunnel=rsIpsecEndpointPairPeerIPToTunnel, rsIpsecEndpointPairMIB=rsIpsecEndpointPairMIB, rsIpsecEndpointPairIndex=rsIpsecEndpointPairIndex, rsIpsecEndpointPairInSAs=rsIpsecEndpointPairInSAs, rsIpsecEndpointPairOtherReceiveErrors=rsIpsecEndpointPairOtherReceiveErrors, rsIpsecEndpointPairPeerIPToTunnelPeerIP=rsIpsecEndpointPairPeerIPToTunnelPeerIP, rsIpsecEndpointPairTotalOutAccKbytes=rsIpsecEndpointPairTotalOutAccKbytes, rsIpsecEndpointPairTotalOtherReceiveErrors=rsIpsecEndpointPairTotalOtherReceiveErrors, rsIpsecEndpointPairPeerAddr=rsIpsecEndpointPairPeerAddr, rsIpsecEndpointPairOutPackets=rsIpsecEndpointPairOutPackets, rsIpsecEndpointPairInPackets=rsIpsecEndpointPairInPackets, rsIpsecEndpointPairTotalPadErrors=rsIpsecEndpointPairTotalPadErrors, rsIpsecEndpointPairPadErrors=rsIpsecEndpointPairPadErrors, rsIpsecEndpointPairSendErrors=rsIpsecEndpointPairSendErrors, rsIpsecEndpointPairTotalAuthErrors=rsIpsecEndpointPairTotalAuthErrors, rsIpsecEndpointPairPeerIPToTunnelTunnelID=rsIpsecEndpointPairPeerIPToTunnelTunnelID, rsIpsecEndpointPairAuthErrors=rsIpsecEndpointPairAuthErrors, rsIpsecEndpointPairTotalDecryptErrors=rsIpsecEndpointPairTotalDecryptErrors, rsIpsecEndpointPairPeerIPToTunnelNum=rsIpsecEndpointPairPeerIPToTunnelNum, rsIpsecEndpointPairModule=rsIpsecEndpointPairModule, rsIpsecEndpointPairStatistics=rsIpsecEndpointPairStatistics, rsIpsecEndpointPairOutSAs=rsIpsecEndpointPairOutSAs, rsIpsecEndpointPairTotalInSAs=rsIpsecEndpointPairTotalInSAs, rsIpsecEndpointPairDecryptErrors=rsIpsecEndpointPairDecryptErrors, rsIpsecEndpointPairTotalOutSAs=rsIpsecEndpointPairTotalOutSAs, rsIpsecEndpointPairNum=rsIpsecEndpointPairNum, rsIpsecEndpointPairOutAccKbytes=rsIpsecEndpointPairOutAccKbytes, PYSNMP_MODULE_ID=rsIpsecEndpointPairModule, rsIpsecEndpointPairLocalAddr=rsIpsecEndpointPairLocalAddr, rsIpsecEndpointPairPeerIPToTunnelTable=rsIpsecEndpointPairPeerIPToTunnelTable, rsIpsecEndpointPairTable=rsIpsecEndpointPairTable, rsIpsecEndpointPairTotalReplayErrors=rsIpsecEndpointPairTotalReplayErrors, rsIpsecEndpointPairPeerIPToTunnelEntry=rsIpsecEndpointPairPeerIPToTunnelEntry, rsIpsecEndpointPairTotalPolicyErrors=rsIpsecEndpointPairTotalPolicyErrors, rsIpsecEndpointPairTotalSendErrors=rsIpsecEndpointPairTotalSendErrors, rsIpsecEndpointPairTotalInPackets=rsIpsecEndpointPairTotalInPackets)