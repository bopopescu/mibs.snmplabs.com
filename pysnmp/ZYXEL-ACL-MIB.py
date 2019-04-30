#
# PySNMP MIB module ZYXEL-ACL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-ACL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:42:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, Unsigned32, MibIdentifier, Integer32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Counter32, Bits, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Unsigned32", "MibIdentifier", "Integer32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Counter32", "Bits", "TimeTicks", "Counter64")
MacAddress, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TextualConvention", "DisplayString")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelAcl = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10))
if mibBuilder.loadTexts: zyxelAcl.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelAcl.setOrganization('Enterprise Solution ZyXEL')
zyxelClassifierStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1))
zyxelPolicyStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2))
zyxelClassifierTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1), )
if mibBuilder.loadTexts: zyxelClassifierTable.setStatus('current')
zyxelClassifierEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1), ).setIndexNames((0, "ZYXEL-ACL-MIB", "zyClassifierName"))
if mibBuilder.loadTexts: zyxelClassifierEntry.setStatus('current')
zyClassifierName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 1), DisplayString())
if mibBuilder.loadTexts: zyClassifierName.setStatus('current')
zyClassifierState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 2), EnabledStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierState.setStatus('current')
zyClassifierPacketFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("all", 1), ("ethernetIIUntagged", 2), ("ethernetIITagged", 3), ("ethernet802dot3Untagged", 4), ("ethernet802dot3Tagged", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierPacketFormat.setStatus('current')
zyClassifierVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierVid.setStatus('current')
zyClassifier8021pPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifier8021pPriority.setStatus('current')
zyClassifierEthernetType = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierEthernetType.setStatus('current')
zyClassifierSourceMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierSourceMacAddress.setStatus('current')
zyClassifierIncomingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierIncomingPort.setStatus('current')
zyClassifierDestinationMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierDestinationMacAddress.setStatus('current')
zyClassifierDSCP = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierDSCP.setStatus('current')
zyClassifierIpProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierIpProtocol.setStatus('current')
zyClassifierEstablishOnly = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 12), EnabledStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierEstablishOnly.setStatus('current')
zyClassifierSourceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierSourceIpAddress.setStatus('current')
zyClassifierSourceIpMaskBits = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierSourceIpMaskBits.setStatus('current')
zyClassifierSourceSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierSourceSocket.setStatus('current')
zyClassifierDestinationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 16), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierDestinationIpAddress.setStatus('current')
zyClassifierDestinationIpMaskBits = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierDestinationIpMaskBits.setStatus('current')
zyClassifierDestinationSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierDestinationSocket.setStatus('current')
zyClassifierIPv6DSCP = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierIPv6DSCP.setStatus('current')
zyClassifierIPv6NextHeader = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierIPv6NextHeader.setStatus('current')
zyClassifierIPv6EstablishOnly = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 21), EnabledStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierIPv6EstablishOnly.setStatus('current')
zyClassifierIPv6SourceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 22), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierIPv6SourceIpAddress.setStatus('current')
zyClassifierIPv6SourceIpPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierIPv6SourceIpPrefixLength.setStatus('current')
zyClassifierIPv6DestinationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 24), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierIPv6DestinationIpAddress.setStatus('current')
zyClassifierIPv6DestinationIpPrefixLength = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierIPv6DestinationIpPrefixLength.setStatus('current')
zyClassifierRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 1, 1, 1, 26), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyClassifierRowstatus.setStatus('current')
zyxelPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1), )
if mibBuilder.loadTexts: zyxelPolicyTable.setStatus('current')
zyxelPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1), ).setIndexNames((0, "ZYXEL-ACL-MIB", "zyPolicyName"))
if mibBuilder.loadTexts: zyxelPolicyEntry.setStatus('current')
zyPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 1), DisplayString())
if mibBuilder.loadTexts: zyPolicyName.setStatus('current')
zyPolicyState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 2), EnabledStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPolicyState.setStatus('current')
zyPolicyClassifier = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPolicyClassifier.setStatus('current')
zyPolicyVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPolicyVid.setStatus('current')
zyPolicyEgressPort = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPolicyEgressPort.setStatus('current')
zyPolicy8021pPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPolicy8021pPriority.setStatus('current')
zyPolicyDSCP = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPolicyDSCP.setStatus('current')
zyPolicyTOS = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPolicyTOS.setStatus('current')
zyPolicyBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPolicyBandwidth.setStatus('current')
zyPolicyOutOfProfileDSCP = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPolicyOutOfProfileDSCP.setStatus('current')
zyPolicyForwardingAction = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noChange", 1), ("discardThePacket", 2), ("doNotDropTheMatchingFramePreviouslyMarkedForDropping", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPolicyForwardingAction.setStatus('current')
zyPolicyPriorityAction = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noChange", 1), ("setThePackets802dot1Priority", 2), ("sendThePacketToPriorityQueue", 3), ("replaceThe802dot1PriorityFieldWithTheIpTosValue", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPolicyPriorityAction.setStatus('current')
zyPolicyDiffServAction = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noChange", 1), ("setThePacketsTosField", 2), ("replaceTheIpTosFieldWithThe802dot1PriorityValue", 3), ("setTheDiffservCodepointFieldInTheFrame", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPolicyDiffServAction.setStatus('current')
zyPolicyOutgoingAction = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 14), Bits().clone(namedValues=NamedValues(("sendThePacketToTheMirrorPort", 0), ("sendThePacketToTheEgressPort", 1), ("sendTheMatchingFramesToTheEgressPort", 2), ("setThePacketVlanId", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPolicyOutgoingAction.setStatus('current')
zyPolicyMeteringState = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPolicyMeteringState.setStatus('current')
zyPolicyOutOfProfileAction = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 16), Bits().clone(namedValues=NamedValues(("dropThePacket", 0), ("changeTheDscpValue", 1), ("setOutDropPrecedence", 2), ("doNotDropTheMatchingFramePreviouslyMarkedForDropping", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPolicyOutOfProfileAction.setStatus('current')
zyPolicyRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 10, 2, 1, 1, 17), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyPolicyRowstatus.setStatus('current')
mibBuilder.exportSymbols("ZYXEL-ACL-MIB", zyClassifierDestinationIpAddress=zyClassifierDestinationIpAddress, zyClassifierSourceIpAddress=zyClassifierSourceIpAddress, zyPolicyForwardingAction=zyPolicyForwardingAction, zyClassifierRowstatus=zyClassifierRowstatus, zyPolicyDSCP=zyPolicyDSCP, zyClassifierIPv6DestinationIpAddress=zyClassifierIPv6DestinationIpAddress, zyxelClassifierEntry=zyxelClassifierEntry, zyClassifier8021pPriority=zyClassifier8021pPriority, zyPolicyName=zyPolicyName, zyPolicyDiffServAction=zyPolicyDiffServAction, zyPolicyVid=zyPolicyVid, zyPolicyBandwidth=zyPolicyBandwidth, zyClassifierDSCP=zyClassifierDSCP, zyPolicyState=zyPolicyState, zyxelPolicyStatus=zyxelPolicyStatus, zyClassifierSourceSocket=zyClassifierSourceSocket, zyxelPolicyEntry=zyxelPolicyEntry, zyClassifierIPv6SourceIpPrefixLength=zyClassifierIPv6SourceIpPrefixLength, PYSNMP_MODULE_ID=zyxelAcl, zyClassifierIpProtocol=zyClassifierIpProtocol, zyPolicyMeteringState=zyPolicyMeteringState, zyClassifierIPv6DestinationIpPrefixLength=zyClassifierIPv6DestinationIpPrefixLength, zyPolicyClassifier=zyPolicyClassifier, zyClassifierIPv6DSCP=zyClassifierIPv6DSCP, zyClassifierIncomingPort=zyClassifierIncomingPort, zyClassifierDestinationIpMaskBits=zyClassifierDestinationIpMaskBits, zyClassifierEstablishOnly=zyClassifierEstablishOnly, zyxelClassifierStatus=zyxelClassifierStatus, zyClassifierIPv6NextHeader=zyClassifierIPv6NextHeader, zyPolicyPriorityAction=zyPolicyPriorityAction, zyPolicyOutOfProfileDSCP=zyPolicyOutOfProfileDSCP, zyClassifierPacketFormat=zyClassifierPacketFormat, zyPolicyOutgoingAction=zyPolicyOutgoingAction, zyxelAcl=zyxelAcl, zyClassifierName=zyClassifierName, zyClassifierState=zyClassifierState, zyPolicyOutOfProfileAction=zyPolicyOutOfProfileAction, zyClassifierDestinationSocket=zyClassifierDestinationSocket, zyPolicyRowstatus=zyPolicyRowstatus, zyxelPolicyTable=zyxelPolicyTable, zyPolicyEgressPort=zyPolicyEgressPort, zyClassifierDestinationMacAddress=zyClassifierDestinationMacAddress, zyPolicyTOS=zyPolicyTOS, zyClassifierEthernetType=zyClassifierEthernetType, zyPolicy8021pPriority=zyPolicy8021pPriority, zyClassifierIPv6SourceIpAddress=zyClassifierIPv6SourceIpAddress, zyClassifierSourceIpMaskBits=zyClassifierSourceIpMaskBits, zyxelClassifierTable=zyxelClassifierTable, zyClassifierIPv6EstablishOnly=zyClassifierIPv6EstablishOnly, zyClassifierVid=zyClassifierVid, zyClassifierSourceMacAddress=zyClassifierSourceMacAddress)