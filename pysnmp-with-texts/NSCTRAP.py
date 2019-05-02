#
# PySNMP MIB module NSCTRAP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NSCTRAP
# Produced by pysmi-0.3.4 at Wed May  1 14:25:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, ifDescr, ifType = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifDescr", "ifType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, NotificationType, Counter32, Counter64, Integer32, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, TimeTicks, Unsigned32, IpAddress, NotificationType, Gauge32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Counter32", "Counter64", "Integer32", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Unsigned32", "IpAddress", "NotificationType", "Gauge32", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nsc = MibIdentifier((1, 3, 6, 1, 4, 1, 10))
nscMib = MibIdentifier((1, 3, 6, 1, 4, 1, 10, 2))
nscManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 10, 2, 2))
nscTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 10, 2, 2, 4))
nscTrapsProtBindIndex = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 9, 10))).clone(namedValues=NamedValues(("ip", 1), ("decnet", 2), ("appleTalk", 3), ("ipx", 4), ("xns", 5), ("bridging", 9), ("bridgingEc", 10))))
if mibBuilder.loadTexts: nscTrapsProtBindIndex.setStatus('mandatory')
if mibBuilder.loadTexts: nscTrapsProtBindIndex.setDescription('The communication protocols whose bind state changes would cause traps to be generated. ')
nscTrapsFddiSMTCFState = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("cf0", 1), ("cf1", 2), ("cf2", 3), ("cf3", 4), ("cf4", 5), ("cf5", 6))))
if mibBuilder.loadTexts: nscTrapsFddiSMTCFState.setStatus('mandatory')
if mibBuilder.loadTexts: nscTrapsFddiSMTCFState.setDescription('The attachment configuration for the station or concentrator. The values are the same as those defined in the SMT group in RFC-1285.')
nscTrapsDecNetAreaNbr = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1))
if mibBuilder.loadTexts: nscTrapsDecNetAreaNbr.setStatus('mandatory')
if mibBuilder.loadTexts: nscTrapsDecNetAreaNbr.setDescription('')
nscTrapsDecNetNodeNbr = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1))
if mibBuilder.loadTexts: nscTrapsDecNetNodeNbr.setStatus('mandatory')
if mibBuilder.loadTexts: nscTrapsDecNetNodeNbr.setDescription('')
nscTrapsDecNetCircuitName = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 6)))
if mibBuilder.loadTexts: nscTrapsDecNetCircuitName.setStatus('mandatory')
if mibBuilder.loadTexts: nscTrapsDecNetCircuitName.setDescription('The name of a DECnet circuit. ')
nscTrapsDecNetEventReason = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256)))
if mibBuilder.loadTexts: nscTrapsDecNetEventReason.setStatus('mandatory')
if mibBuilder.loadTexts: nscTrapsDecNetEventReason.setDescription('The reason that causes the routing event to happen. Possible reasons are: SYNC_LOST (0), DATA_ERRORS (1), UNEXPECTED_PKT_TYPE (2), ROUTING_UPDATE_CHECKSUM_ERROR (3), ADJ_ADDR_CHANGE (4), VERIF_RECV_TIMEOUT (5), VERSION_SKEW (6), ADJ_ADDR_OUT_OF_RANGE (7), ADJ_BLOCK_SIZE_TOO_SMALL (8), INVALID_VERIF_SEED_VALUE (9), ADJ_LIST_RECV_TIMEOUT (10), ADJ_LIST_RECV_INVALID_DATA (11), CALL_FAILED (12), VERIF_PASSWORD_REQ_FROM_PIII_NODE (13), DROPPED_BY_ADJ_NODE (14).')
nscTrapsDecNetReachStatus = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reachable", 1), ("unreachable", 2))))
if mibBuilder.loadTexts: nscTrapsDecNetReachStatus.setStatus('mandatory')
if mibBuilder.loadTexts: nscTrapsDecNetReachStatus.setDescription('The reachable status of a node or area.')
nscTrapsVcpPortName = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12)))
if mibBuilder.loadTexts: nscTrapsVcpPortName.setStatus('mandatory')
if mibBuilder.loadTexts: nscTrapsVcpPortName.setDescription('The name of the VCP port.')
nscTrapsVcpLogicalState = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30)))
if mibBuilder.loadTexts: nscTrapsVcpLogicalState.setStatus('mandatory')
if mibBuilder.loadTexts: nscTrapsVcpLogicalState.setDescription('The logical state of a VCP port. The possible states are ACTIVE, DOWN, DISABLED.')
nscTrapsVcpPhysicalState = MibScalar((1, 3, 6, 1, 4, 1, 10, 2, 2, 4, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30)))
if mibBuilder.loadTexts: nscTrapsVcpPhysicalState.setStatus('mandatory')
if mibBuilder.loadTexts: nscTrapsVcpPhysicalState.setDescription('The physical state of a VCP port. The possible states are Off, On, Broken_Cannot_IO, Broken_Purge, Broken_Reconfigure, Broken_Misconfigure.')
protocolBound = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("NSCTRAP", "nscTrapsProtBindIndex"))
if mibBuilder.loadTexts: protocolBound.setDescription('A protocolBound trap is sent when a protocol is bound to an interface.')
protocolUnbound = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("NSCTRAP", "nscTrapsProtBindIndex"))
if mibBuilder.loadTexts: protocolUnbound.setDescription('A protocolBound trap is sent when a protocol is unbound from an interface.')
physicalLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"))
if mibBuilder.loadTexts: physicalLinkUp.setDescription('A physicalLinkUp trap is sent for devices that represent both a logical and physical device. The physicalLinkUp trap is sent when the physical device becomes active. The SNMP linkUp is sent when the logical device becomes active.')
physicalLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"))
if mibBuilder.loadTexts: physicalLinkDown.setDescription('A physicalLinkDown trap is sent for devices that represent both a logical and physical device. The physicalLinkDown trap is sent when the physical device becomes not active. The SNMP linkDown is sent when the logical device becomes not active.')
fddiWrap = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,5)).setObjects(("IF-MIB", "ifIndex"), ("NSCTRAP", "nscTrapsFddiSMTCFState"))
if mibBuilder.loadTexts: fddiWrap.setDescription('A FDDI wrap trap indicates that a FDDI ring is broken and the signal path wraps through a device and out the parallel fiber. The trap also occures when the wrapped condition is relieved.')
vcpActive = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,6)).setObjects(("NSCTRAP", "nscTrapsVcpPortName"), ("NSCTRAP", "nscTrapsVcpLogicalState"), ("NSCTRAP", "nscTrapsVcpPhysicalState"))
if mibBuilder.loadTexts: vcpActive.setDescription('This trap indicates that a VCP physical link just came up.')
vcpInactive = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,7)).setObjects(("NSCTRAP", "nscTrapsVcpPortName"), ("NSCTRAP", "nscTrapsVcpLogicalState"), ("NSCTRAP", "nscTrapsVcpPhysicalState"))
if mibBuilder.loadTexts: vcpInactive.setDescription('This trap indicates that a VCP physical link just went down.')
vcpReconfig = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,8)).setObjects(("NSCTRAP", "nscTrapsVcpPortName"), ("NSCTRAP", "nscTrapsVcpLogicalState"), ("NSCTRAP", "nscTrapsVcpPhysicalState"))
if mibBuilder.loadTexts: vcpReconfig.setDescription('This trap indicates that a VCP physical link is reconfiguring.')
vcpBroken = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,9)).setObjects(("NSCTRAP", "nscTrapsVcpPortName"), ("NSCTRAP", "nscTrapsVcpLogicalState"), ("NSCTRAP", "nscTrapsVcpPhysicalState"))
if mibBuilder.loadTexts: vcpBroken.setDescription('This trap indicates that a VCP physical link lost connection with its remote end.')
vcpMisconfigured = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,10)).setObjects(("NSCTRAP", "nscTrapsVcpPortName"))
if mibBuilder.loadTexts: vcpMisconfigured.setDescription('This trap indicates that a VCP physical link has detected different configuration on the remote end.')
decNetCircDownFault = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,407)).setObjects(("NSCTRAP", "nscTrapsDecNetAreaNbr"), ("NSCTRAP", "nscTrapsDecNetNodeNbr"), ("NSCTRAP", "nscTrapsDecNetCircuitName"), ("NSCTRAP", "nscTrapsDecNetEventReason"))
if mibBuilder.loadTexts: decNetCircDownFault.setDescription('This trap shows that a fault has brought down the indicated DECnet circuit.')
decNetCircDown = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,408)).setObjects(("NSCTRAP", "nscTrapsDecNetAreaNbr"), ("NSCTRAP", "nscTrapsDecNetNodeNbr"), ("NSCTRAP", "nscTrapsDecNetCircuitName"), ("NSCTRAP", "nscTrapsDecNetEventReason"))
if mibBuilder.loadTexts: decNetCircDown.setDescription('This trap indicates that the named DECnet circuit is down. (This trap is not supported.)')
decNetCircUp = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,410)).setObjects(("NSCTRAP", "nscTrapsDecNetAreaNbr"), ("NSCTRAP", "nscTrapsDecNetNodeNbr"), ("NSCTRAP", "nscTrapsDecNetCircuitName"))
if mibBuilder.loadTexts: decNetCircUp.setDescription('This trap indicates that a DECnet circuit has become enabled.')
decNetNodeReachChg = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,414)).setObjects(("NSCTRAP", "nscTrapsDecNetNodeNbr"), ("NSCTRAP", "nscTrapsDecNetReachStatus"))
if mibBuilder.loadTexts: decNetNodeReachChg.setDescription('This trap reports a change in the nodes that can be reached. (This trap is not supported.)')
decNetAdjUp = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,415)).setObjects(("NSCTRAP", "nscTrapsDecNetAreaNbr"), ("NSCTRAP", "nscTrapsDecNetNodeNbr"), ("NSCTRAP", "nscTrapsDecNetCircuitName"))
if mibBuilder.loadTexts: decNetAdjUp.setDescription('This trap indicates that a DECnet adjacent node just has come up.')
decNetAdjRejected = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,416)).setObjects(("NSCTRAP", "nscTrapsDecNetAreaNbr"), ("NSCTRAP", "nscTrapsDecNetNodeNbr"), ("NSCTRAP", "nscTrapsDecNetCircuitName"), ("NSCTRAP", "nscTrapsDecNetEventReason"))
if mibBuilder.loadTexts: decNetAdjRejected.setDescription("This trap indicates that an adjacent node has been rejected of communication, or become inactive. The reason could be either the numbers of broadcast (non)routers or the address of a node exceeds the ones in the router's configuartion. ")
decNetAreaReachChg = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,417)).setObjects(("NSCTRAP", "nscTrapsDecNetAreaNbr"), ("NSCTRAP", "nscTrapsDecNetReachStatus"))
if mibBuilder.loadTexts: decNetAreaReachChg.setDescription('This trap reports a change in the areas that can be reached. (This trap is not supported.)')
decNetAdjDown = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,418)).setObjects(("NSCTRAP", "nscTrapsDecNetAreaNbr"), ("NSCTRAP", "nscTrapsDecNetNodeNbr"), ("NSCTRAP", "nscTrapsDecNetCircuitName"), ("NSCTRAP", "nscTrapsDecNetEventReason"))
if mibBuilder.loadTexts: decNetAdjDown.setDescription('This trap indicates that a adjacent node has come down or lost.')
decNetDesignatedRouter = NotificationType((1, 3, 6, 1, 4, 1, 10, 2, 2, 4) + (0,422)).setObjects(("NSCTRAP", "nscTrapsDecNetAreaNbr"), ("NSCTRAP", "nscTrapsDecNetNodeNbr"), ("NSCTRAP", "nscTrapsDecNetCircuitName"))
if mibBuilder.loadTexts: decNetDesignatedRouter.setDescription('This trap reports a change in the designated router.')
mibBuilder.exportSymbols("NSCTRAP", nscTrapsProtBindIndex=nscTrapsProtBindIndex, vcpInactive=vcpInactive, nscTrapsDecNetCircuitName=nscTrapsDecNetCircuitName, nscMib=nscMib, nscTrapsDecNetAreaNbr=nscTrapsDecNetAreaNbr, nscTrapsDecNetReachStatus=nscTrapsDecNetReachStatus, nscTrapsVcpLogicalState=nscTrapsVcpLogicalState, decNetCircDown=decNetCircDown, protocolUnbound=protocolUnbound, vcpActive=vcpActive, decNetCircDownFault=decNetCircDownFault, vcpReconfig=vcpReconfig, fddiWrap=fddiWrap, nscTrapsFddiSMTCFState=nscTrapsFddiSMTCFState, decNetAdjRejected=decNetAdjRejected, decNetAdjUp=decNetAdjUp, nscTrapsVcpPortName=nscTrapsVcpPortName, vcpMisconfigured=vcpMisconfigured, nscManagement=nscManagement, physicalLinkUp=physicalLinkUp, decNetDesignatedRouter=decNetDesignatedRouter, decNetAdjDown=decNetAdjDown, nscTrapsVcpPhysicalState=nscTrapsVcpPhysicalState, nscTraps=nscTraps, decNetAreaReachChg=decNetAreaReachChg, decNetCircUp=decNetCircUp, protocolBound=protocolBound, nscTrapsDecNetNodeNbr=nscTrapsDecNetNodeNbr, nsc=nsc, decNetNodeReachChg=decNetNodeReachChg, nscTrapsDecNetEventReason=nscTrapsDecNetEventReason, vcpBroken=vcpBroken, physicalLinkDown=physicalLinkDown)