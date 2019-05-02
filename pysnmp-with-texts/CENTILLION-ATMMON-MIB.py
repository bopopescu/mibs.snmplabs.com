#
# PySNMP MIB module CENTILLION-ATMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-ATMMON-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:47:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
MacAddress, CardId, PortId, atmMonitor = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "MacAddress", "CardId", "PortId", "atmMonitor")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, iso, Counter32, Counter64, ModuleIdentity, Unsigned32, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "iso", "Counter32", "Counter64", "ModuleIdentity", "Unsigned32", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atmPortMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1))
atmElanMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2))
atmPvcStatusMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3))
atmSigMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4))
atmCardMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 5))
atmStatusEnqMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6))
atmPortStatTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1), )
if mibBuilder.loadTexts: atmPortStatTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmPortStatTable.setDescription('ATM Port Statistics')
atmPortStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1), ).setIndexNames((0, "CENTILLION-ATMMON-MIB", "atmStatCardId"), (0, "CENTILLION-ATMMON-MIB", "atmStatPortId"))
if mibBuilder.loadTexts: atmPortStatEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmPortStatEntry.setDescription('ATM Port Statistics. Each entry is indexed by two fields: The card number and the port number.')
atmStatCardId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 1), CardId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmStatCardId.setStatus('mandatory')
if mibBuilder.loadTexts: atmStatCardId.setDescription('This field is the card index ')
atmStatPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 2), PortId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmStatPortId.setStatus('mandatory')
if mibBuilder.loadTexts: atmStatPortId.setDescription('This field is the port index ')
atmSigDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("signalpresent", 1), ("nosignal", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSigDetected.setStatus('mandatory')
if mibBuilder.loadTexts: atmSigDetected.setDescription('This bit field indicates if the port receives signal from the remote ATM port. 1= signal present, 2= no signal.')
atmRxBadHecCell = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmRxBadHecCell.setStatus('mandatory')
if mibBuilder.loadTexts: atmRxBadHecCell.setDescription('The number of cells received that has a bad ATM cell header (HEC). The error is usually due to a physical layer problem. For example, when the fiber is first connected to the system or a clock mismatch.')
atmRxDmaDropCell = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmRxDmaDropCell.setStatus('mandatory')
if mibBuilder.loadTexts: atmRxDmaDropCell.setDescription('The number of cells received but is discarded by the ATM header validation checking. The error is usually due to a incorrectly configured VPI/VCI or other configuration error.')
atmRxGoodCell = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmRxGoodCell.setStatus('mandatory')
if mibBuilder.loadTexts: atmRxGoodCell.setDescription('The number of cells received that is valid.')
atmTxDmaDropCell = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmTxDmaDropCell.setStatus('mandatory')
if mibBuilder.loadTexts: atmTxDmaDropCell.setDescription('The number of outgoing cells dropped due to congestions.')
atmTxGoodCell = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmTxGoodCell.setStatus('mandatory')
if mibBuilder.loadTexts: atmTxGoodCell.setDescription('The number of cells transmitted.')
atmSuniFifoOverrun = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmSuniFifoOverrun.setStatus('mandatory')
if mibBuilder.loadTexts: atmSuniFifoOverrun.setDescription('The number of times that the SUNI FIFO overrun status bit has been read in the true state.')
atmElanPvcStatisticTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1), )
if mibBuilder.loadTexts: atmElanPvcStatisticTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmElanPvcStatisticTable.setDescription('Tmp ATM Elan PVC statistics')
atmElanPvcStatisticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1, 1), ).setIndexNames((0, "CENTILLION-ATMMON-MIB", "atmElanId"))
if mibBuilder.loadTexts: atmElanPvcStatisticEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmElanPvcStatisticEntry.setDescription('ATM Elan PVC statistics. The Elan ID is used as the index of the object.')
atmElanId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmElanId.setStatus('mandatory')
if mibBuilder.loadTexts: atmElanId.setDescription('The Elan index.')
atmElanPvcInUcastPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmElanPvcInUcastPkt.setStatus('mandatory')
if mibBuilder.loadTexts: atmElanPvcInUcastPkt.setDescription('The number of unicast packet that is received from this Elan PVC.')
atmElanPvcInMcastPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmElanPvcInMcastPkt.setStatus('mandatory')
if mibBuilder.loadTexts: atmElanPvcInMcastPkt.setDescription('The number of multicast packet that is received from this Elan PVC.')
atmElanPvcOutUcastPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmElanPvcOutUcastPkt.setStatus('mandatory')
if mibBuilder.loadTexts: atmElanPvcOutUcastPkt.setDescription('The number of unicast packet that is transmitted from this Elan PVC.')
atmElanPvcOutMcastPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmElanPvcOutMcastPkt.setStatus('mandatory')
if mibBuilder.loadTexts: atmElanPvcOutMcastPkt.setDescription('The number of unicast packet that is transmitted from this Elan PVC.')
atmPvcStatusTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1), )
if mibBuilder.loadTexts: atmPvcStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmPvcStatusTable.setDescription('Tmp ATM InterSwitch PVC status')
atmPvcStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1), ).setIndexNames((0, "CENTILLION-ATMMON-MIB", "atmPvcCktId"))
if mibBuilder.loadTexts: atmPvcStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmPvcStatusEntry.setDescription('ATM PVC status. The PVC circuit ID is used as the index of the object.')
atmPvcCktId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPvcCktId.setStatus('mandatory')
if mibBuilder.loadTexts: atmPvcCktId.setDescription('This field is the index of the circuit.')
atmPvcElanId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPvcElanId.setStatus('mandatory')
if mibBuilder.loadTexts: atmPvcElanId.setDescription('This field is the index of the elan this circuit belongs to.')
atmPvcRemoteSwitchInfoValid = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPvcRemoteSwitchInfoValid.setStatus('mandatory')
if mibBuilder.loadTexts: atmPvcRemoteSwitchInfoValid.setDescription('This field is based on the aging timer of a remote switch. If the local switch has not received any packets from the remote switch for a period of time, then it is declared as non-valid. 1 = non-valid 2 = valid (normal state of operation).')
atmPvcRemoteSwitchMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPvcRemoteSwitchMacAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atmPvcRemoteSwitchMacAddress.setDescription("This field lists the remote switch's MAC address. If the atmInterSwitchPvcRemoteSwitchInfoValid object is 1, then this field contains the valid info. Otherwise, this field contains the last learned info.")
atmPvcRemoteSwitchPvcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPvcRemoteSwitchPvcStatus.setStatus('mandatory')
if mibBuilder.loadTexts: atmPvcRemoteSwitchPvcStatus.setDescription('This field is set if the remote switch receives packets from this switch. If atmInterSwitchPvcRemoteSwitchInfoValid objeect is 1, then this field contains the valid info. Otherwise, this field contains the last learned info.')
atmPvcSTPState = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disabled", 1), ("blocking", 2), ("listening", 3), ("learning", 4), ("forwarding", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPvcSTPState.setStatus('mandatory')
if mibBuilder.loadTexts: atmPvcSTPState.setDescription('This field indicates the STP port state of the circuit.')
atmPvcRemoteElanId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPvcRemoteElanId.setStatus('mandatory')
if mibBuilder.loadTexts: atmPvcRemoteElanId.setDescription('This field indicates the elan ID of the circuit.')
atmPvcRemoteMcpIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 3, 1, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPvcRemoteMcpIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atmPvcRemoteMcpIpAddress.setDescription('This is the remote mcp ip address.')
cnCurPtptConns = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnCurPtptConns.setStatus('mandatory')
if mibBuilder.loadTexts: cnCurPtptConns.setDescription('This counter counts the number of current point-to-point calls of the switch.')
cnCurPtmptConns = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnCurPtmptConns.setStatus('mandatory')
if mibBuilder.loadTexts: cnCurPtmptConns.setDescription('This counter counts the number of current point-to-multipoint calls of the switch.')
cnCurActiveConns = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnCurActiveConns.setStatus('mandatory')
if mibBuilder.loadTexts: cnCurActiveConns.setDescription('This counter counts the number of current active calls of the switch.')
cnCurPortConnsTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 4), )
if mibBuilder.loadTexts: cnCurPortConnsTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnCurPortConnsTable.setDescription('This table contains the point-to-point, point-to-multipoint and active calls per port for all the atm ports in the switch.')
cnCurPortConnsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cnCurPortConnsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnCurPortConnsEntry.setDescription('This entry contains the point-to-point, point-to-multipoint and active calls per port.')
cnCurPortConnsPtptConns = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnCurPortConnsPtptConns.setStatus('mandatory')
if mibBuilder.loadTexts: cnCurPortConnsPtptConns.setDescription('This entry counts the number of current point-to-point calls per port.')
cnCurPortConnsPtmptConns = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnCurPortConnsPtmptConns.setStatus('mandatory')
if mibBuilder.loadTexts: cnCurPortConnsPtmptConns.setDescription('This entry counts the number of current point-to-multipoint calls per port.')
cnCurPortConnsActiveConns = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 4, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnCurPortConnsActiveConns.setStatus('mandatory')
if mibBuilder.loadTexts: cnCurPortConnsActiveConns.setDescription('This entry counts the number of current active calls per port.')
atmCardOperTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 5, 1), )
if mibBuilder.loadTexts: atmCardOperTable.setStatus('mandatory')
if mibBuilder.loadTexts: atmCardOperTable.setDescription('ATM Card Operational values')
atmCardOperEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 5, 1, 1), ).setIndexNames((0, "CENTILLION-ATMMON-MIB", "atmCardOperCardId"))
if mibBuilder.loadTexts: atmCardOperEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atmCardOperEntry.setDescription('ATM Card Operational values. Each entry is indexed by card number')
atmCardOperCardId = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 5, 1, 1, 1), CardId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmCardOperCardId.setStatus('mandatory')
if mibBuilder.loadTexts: atmCardOperCardId.setDescription('This field is the card index ')
atmCardOperExtClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmCardOperExtClockSource.setStatus('mandatory')
if mibBuilder.loadTexts: atmCardOperExtClockSource.setDescription('This field indicates the operational external clock source. The following value is read-only: 0 = Local Oscillator, 1..N = ATM port id for external clock source. This object only applies to ATM MDA modules with SM, MM, or UTP media types.')
cnStsEnqPTPCalls = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnStsEnqPTPCalls.setStatus('mandatory')
if mibBuilder.loadTexts: cnStsEnqPTPCalls.setDescription('The number of current point-to-point calls in the status enquiry queue of the switch.')
cnStsEnqActiveParties = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnStsEnqActiveParties.setStatus('mandatory')
if mibBuilder.loadTexts: cnStsEnqActiveParties.setDescription('The number of current active parties in the status enquiry queue of the switch. (This includes point- to-multi-point calls).')
cnStsEnqSent = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnStsEnqSent.setStatus('mandatory')
if mibBuilder.loadTexts: cnStsEnqSent.setDescription('The total number of status enquiry requests sent.')
cnStsEnqCfmsRecvd = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnStsEnqCfmsRecvd.setStatus('mandatory')
if mibBuilder.loadTexts: cnStsEnqCfmsRecvd.setDescription('The number of current status messages (in response to status enquiry) received.')
cnStsEnqRetried = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnStsEnqRetried.setStatus('mandatory')
if mibBuilder.loadTexts: cnStsEnqRetried.setDescription('The total number of status enquiry commands retried.')
cnStsEnqTimeOuts = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnStsEnqTimeOuts.setStatus('mandatory')
if mibBuilder.loadTexts: cnStsEnqTimeOuts.setDescription('The total number of status enquiry commands timed out i.e The number of calls for which status (in response to status enquiry) was not received.')
cnStsEnqQueueSize = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnStsEnqQueueSize.setStatus('mandatory')
if mibBuilder.loadTexts: cnStsEnqQueueSize.setDescription('The size of the status enquiry queue.')
cnStsEnqCallsCleared = MibScalar((1, 3, 6, 1, 4, 1, 930, 2, 2, 2, 6, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnStsEnqCallsCleared.setStatus('mandatory')
if mibBuilder.loadTexts: cnStsEnqCallsCleared.setDescription('The number of calls cleared by status enquiry. ')
mibBuilder.exportSymbols("CENTILLION-ATMMON-MIB", cnStsEnqRetried=cnStsEnqRetried, atmElanMonitor=atmElanMonitor, atmElanId=atmElanId, cnStsEnqCallsCleared=cnStsEnqCallsCleared, atmTxDmaDropCell=atmTxDmaDropCell, atmPvcCktId=atmPvcCktId, atmSuniFifoOverrun=atmSuniFifoOverrun, atmRxDmaDropCell=atmRxDmaDropCell, atmElanPvcStatisticTable=atmElanPvcStatisticTable, cnStsEnqCfmsRecvd=cnStsEnqCfmsRecvd, atmPortStatEntry=atmPortStatEntry, cnCurPortConnsPtmptConns=cnCurPortConnsPtmptConns, cnCurPortConnsEntry=cnCurPortConnsEntry, cnStsEnqTimeOuts=cnStsEnqTimeOuts, atmSigMonitor=atmSigMonitor, atmPvcStatusMonitor=atmPvcStatusMonitor, cnStsEnqSent=cnStsEnqSent, atmCardOperTable=atmCardOperTable, cnStsEnqActiveParties=cnStsEnqActiveParties, atmElanPvcStatisticEntry=atmElanPvcStatisticEntry, atmCardMonitor=atmCardMonitor, atmPvcStatusTable=atmPvcStatusTable, atmPortStatTable=atmPortStatTable, cnCurPortConnsPtptConns=cnCurPortConnsPtptConns, cnCurActiveConns=cnCurActiveConns, atmStatusEnqMonitor=atmStatusEnqMonitor, atmElanPvcInMcastPkt=atmElanPvcInMcastPkt, atmRxGoodCell=atmRxGoodCell, atmSigDetected=atmSigDetected, atmStatPortId=atmStatPortId, atmRxBadHecCell=atmRxBadHecCell, atmPvcSTPState=atmPvcSTPState, cnCurPtmptConns=cnCurPtmptConns, atmElanPvcInUcastPkt=atmElanPvcInUcastPkt, cnCurPortConnsActiveConns=cnCurPortConnsActiveConns, cnStsEnqPTPCalls=cnStsEnqPTPCalls, atmElanPvcOutMcastPkt=atmElanPvcOutMcastPkt, atmPvcRemoteSwitchPvcStatus=atmPvcRemoteSwitchPvcStatus, cnStsEnqQueueSize=cnStsEnqQueueSize, atmPortMonitor=atmPortMonitor, atmTxGoodCell=atmTxGoodCell, atmPvcElanId=atmPvcElanId, atmCardOperCardId=atmCardOperCardId, atmPvcStatusEntry=atmPvcStatusEntry, atmPvcRemoteMcpIpAddress=atmPvcRemoteMcpIpAddress, atmStatCardId=atmStatCardId, atmCardOperEntry=atmCardOperEntry, cnCurPortConnsTable=cnCurPortConnsTable, atmPvcRemoteElanId=atmPvcRemoteElanId, cnCurPtptConns=cnCurPtptConns, atmCardOperExtClockSource=atmCardOperExtClockSource, atmPvcRemoteSwitchMacAddress=atmPvcRemoteSwitchMacAddress, atmPvcRemoteSwitchInfoValid=atmPvcRemoteSwitchInfoValid, atmElanPvcOutUcastPkt=atmElanPvcOutUcastPkt)