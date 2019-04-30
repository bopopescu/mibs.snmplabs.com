#
# PySNMP MIB module CTRON-LFAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-LFAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:14:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ctSystem, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctSystem")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, ObjectIdentity, iso, NotificationType, Unsigned32, MibIdentifier, ModuleIdentity, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "ObjectIdentity", "iso", "NotificationType", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Integer32", "Bits")
TextualConvention, DisplayString, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "PhysAddress")
ctLFAP = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11))
ctLFAP.setRevisions(('1999-12-29 00:00', '1997-09-25 00:00',))
if mibBuilder.loadTexts: ctLFAP.setLastUpdated('9912290000Z')
if mibBuilder.loadTexts: ctLFAP.setOrganization('Cabletron Systems, Inc')
flowPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1))
flowPolicyConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 6))
monLfap = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2))
monLfapCounts = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1))
monCxnCounts = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 2))
flowPolicyPolling = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 3))
flowPolicyControl = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowPolicyControl.setStatus('current')
flowPolicyStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("active", 3), ("error", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowPolicyStatus.setStatus('current')
flowPolicyActiveServer = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 3), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowPolicyActiveServer.setStatus('current')
flowPolicyServerAddrTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 4), )
if mibBuilder.loadTexts: flowPolicyServerAddrTable.setStatus('current')
flowPolicyServerAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 4, 1), ).setIndexNames((0, "CTRON-LFAP-MIB", "flowPolicyServerAddrIndex"))
if mibBuilder.loadTexts: flowPolicyServerAddrEntry.setStatus('current')
flowPolicyServerAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowPolicyServerAddrIndex.setStatus('current')
flowPolicyServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 4, 1, 2), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowPolicyServerAddr.setStatus('current')
flowPolicyConfigPolicy = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("available", 1), ("unavailable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowPolicyConfigPolicy.setStatus('current')
flowPolicyConfigStatistics = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 1, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("available", 1), ("unavailable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowPolicyConfigStatistics.setStatus('current')
monLfapFARsSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFARsSent.setStatus('current')
monLfapFARsReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFARsReceived.setStatus('current')
monLfapFAAsSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFAAsSent.setStatus('current')
monLfapFAAsReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFAAsReceived.setStatus('current')
monLfapFAUsSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFAUsSent.setStatus('current')
monLfapFAUsReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFAUsReceived.setStatus('current')
monLfapFUNsSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFUNsSent.setStatus('current')
monLfapFUNsReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFUNsReceived.setStatus('current')
monLfapFUAsSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFUAsSent.setStatus('current')
monLfapFUAsReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFUAsReceived.setStatus('current')
monLfapFCRsSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFCRsSent.setStatus('current')
monLfapFCRsReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFCRsReceived.setStatus('current')
monLfapFCAsSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFCAsSent.setStatus('current')
monLfapFCAsReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFCAsReceived.setStatus('current')
monLfapARsSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapARsSent.setStatus('current')
monLfapARsReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapARsReceived.setStatus('current')
monLfapARAsSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapARAsSent.setStatus('current')
monLfapARAsReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapARAsReceived.setStatus('current')
monLfapFSNsSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFSNsSent.setStatus('current')
monLfapFSNsReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFSNsReceived.setStatus('current')
monLfapFSAsSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFSAsSent.setStatus('current')
monLfapFSAsReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFSAsReceived.setStatus('current')
monLfapDroppedMessages = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapDroppedMessages.setStatus('current')
monLfapVRsSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapVRsSent.setStatus('current')
monLfapVRAsReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapVRAsReceived.setStatus('current')
monLfapConnSuccess = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapConnSuccess.setStatus('current')
monLfapConnFailure = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapConnFailure.setStatus('current')
monLfapBytesSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapBytesSent.setStatus('current')
monLfapBytesReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapBytesReceived.setStatus('current')
monLfapMsgsSent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapMsgsSent.setStatus('current')
monLfapMsgsReceived = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapMsgsReceived.setStatus('current')
monLfapMsgsReceivedError = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapMsgsReceivedError.setStatus('current')
monLfapMsgsSendQueue = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 33), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapMsgsSendQueue.setStatus('current')
monLfapMsgsSendQueuePeak = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 34), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapMsgsSendQueuePeak.setStatus('current')
monLfapMsgsReceiveQueue = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 35), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapMsgsReceiveQueue.setStatus('current')
monLfapDroppedMessagesConnected = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapDroppedMessagesConnected.setStatus('current')
monLfapDroppedFARs = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapDroppedFARs.setStatus('current')
monLfapDroppedFUNIs = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapDroppedFUNIs.setStatus('current')
monLfapDroppedFUNs = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapDroppedFUNs.setStatus('current')
monLfapDroppedARs = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 40), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapDroppedARs.setStatus('current')
monLfapDroppedARAs = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 41), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapDroppedARAs.setStatus('current')
monLfapDroppedVRs = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 1, 42), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapDroppedVRs.setStatus('current')
monLfapYesRespCnt = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapYesRespCnt.setStatus('current')
monLfapNoRespCnt = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapNoRespCnt.setStatus('current')
monLfapFlowSetups = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFlowSetups.setStatus('current')
monLfapFlowTeardowns = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFlowTeardowns.setStatus('current')
monLfapFlowActivePeak = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 2, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monLfapFlowActivePeak.setStatus('current')
monActiveCxnCnt = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 2, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: monActiveCxnCnt.setStatus('current')
flowPolicyPollingTimerInterval = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1440)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowPolicyPollingTimerInterval.setStatus('current')
flowPolicyPollingBatchSize = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2000)).clone(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowPolicyPollingBatchSize.setStatus('current')
flowPolicyPollingBatchInterval = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowPolicyPollingBatchInterval.setStatus('current')
flowPolicyPollingBatchUpdateInterval = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2000)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowPolicyPollingBatchUpdateInterval.setStatus('current')
flowPolicyPollingLostContactInterval = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 2000)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowPolicyPollingLostContactInterval.setStatus('current')
flowPolicyPollingServerRetryInterval = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2000)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowPolicyPollingServerRetryInterval.setStatus('current')
flowPolicyPollingSendQueueMaxSize = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 2000000)).clone(50000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowPolicyPollingSendQueueMaxSize.setStatus('current')
flowPolicyPollingTaskPriority = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 3, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 250)).clone(230)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flowPolicyPollingTaskPriority.setStatus('current')
lfapConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 4))
lfapCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 4, 1))
lfapGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 4, 2))
lfapComplianceV10 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 4, 2, 3, 1)).setObjects(("CTRON-LFAP-MIB", "lfapConfGroupV10"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lfapComplianceV10 = lfapComplianceV10.setStatus('deprecated')
lfapComplianceV40 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 4, 2, 4, 1)).setObjects(("CTRON-LFAP-MIB", "lfapConfGroupV40"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lfapComplianceV40 = lfapComplianceV40.setStatus('current')
lfapConfGroupV10 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 4, 2, 3)).setObjects(("CTRON-LFAP-MIB", "flowPolicyControl"), ("CTRON-LFAP-MIB", "flowPolicyStatus"), ("CTRON-LFAP-MIB", "flowPolicyActiveServer"), ("CTRON-LFAP-MIB", "flowPolicyServerAddrIndex"), ("CTRON-LFAP-MIB", "flowPolicyServerAddr"), ("CTRON-LFAP-MIB", "flowPolicyConfigPolicy"), ("CTRON-LFAP-MIB", "flowPolicyConfigStatistics"), ("CTRON-LFAP-MIB", "monLfapFARsSent"), ("CTRON-LFAP-MIB", "monLfapFARsReceived"), ("CTRON-LFAP-MIB", "monLfapFAAsSent"), ("CTRON-LFAP-MIB", "monLfapFAAsReceived"), ("CTRON-LFAP-MIB", "monLfapFAUsSent"), ("CTRON-LFAP-MIB", "monLfapFAUsReceived"), ("CTRON-LFAP-MIB", "monLfapFUNsSent"), ("CTRON-LFAP-MIB", "monLfapFUNsReceived"), ("CTRON-LFAP-MIB", "monLfapFUAsSent"), ("CTRON-LFAP-MIB", "monLfapFUAsReceived"), ("CTRON-LFAP-MIB", "monLfapFCRsSent"), ("CTRON-LFAP-MIB", "monLfapFCRsReceived"), ("CTRON-LFAP-MIB", "monLfapFCAsSent"), ("CTRON-LFAP-MIB", "monLfapFCAsReceived"), ("CTRON-LFAP-MIB", "monLfapARsSent"), ("CTRON-LFAP-MIB", "monLfapARsReceived"), ("CTRON-LFAP-MIB", "monLfapARAsSent"), ("CTRON-LFAP-MIB", "monLfapARAsReceived"), ("CTRON-LFAP-MIB", "monLfapFSNsSent"), ("CTRON-LFAP-MIB", "monLfapFSNsReceived"), ("CTRON-LFAP-MIB", "monLfapFSAsSent"), ("CTRON-LFAP-MIB", "monLfapFSAsReceived"), ("CTRON-LFAP-MIB", "monLfapDroppedMessages"), ("CTRON-LFAP-MIB", "monLfapYesRespCnt"), ("CTRON-LFAP-MIB", "monLfapNoRespCnt"), ("CTRON-LFAP-MIB", "monActiveCxnCnt"), ("CTRON-LFAP-MIB", "flowPolicyPollingTimerInterval"), ("CTRON-LFAP-MIB", "flowPolicyPollingBatchSize"), ("CTRON-LFAP-MIB", "flowPolicyPollingBatchInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lfapConfGroupV10 = lfapConfGroupV10.setStatus('deprecated')
lfapConfGroupV40 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11, 4, 2, 4)).setObjects(("CTRON-LFAP-MIB", "flowPolicyControl"), ("CTRON-LFAP-MIB", "flowPolicyStatus"), ("CTRON-LFAP-MIB", "flowPolicyActiveServer"), ("CTRON-LFAP-MIB", "flowPolicyServerAddrIndex"), ("CTRON-LFAP-MIB", "flowPolicyServerAddr"), ("CTRON-LFAP-MIB", "flowPolicyConfigPolicy"), ("CTRON-LFAP-MIB", "flowPolicyConfigStatistics"), ("CTRON-LFAP-MIB", "monLfapFARsSent"), ("CTRON-LFAP-MIB", "monLfapFARsReceived"), ("CTRON-LFAP-MIB", "monLfapFAAsSent"), ("CTRON-LFAP-MIB", "monLfapFAAsReceived"), ("CTRON-LFAP-MIB", "monLfapFAUsSent"), ("CTRON-LFAP-MIB", "monLfapFAUsReceived"), ("CTRON-LFAP-MIB", "monLfapFUNsSent"), ("CTRON-LFAP-MIB", "monLfapFUNsReceived"), ("CTRON-LFAP-MIB", "monLfapFUAsSent"), ("CTRON-LFAP-MIB", "monLfapFUAsReceived"), ("CTRON-LFAP-MIB", "monLfapFCRsSent"), ("CTRON-LFAP-MIB", "monLfapFCRsReceived"), ("CTRON-LFAP-MIB", "monLfapFCAsSent"), ("CTRON-LFAP-MIB", "monLfapFCAsReceived"), ("CTRON-LFAP-MIB", "monLfapARsSent"), ("CTRON-LFAP-MIB", "monLfapARsReceived"), ("CTRON-LFAP-MIB", "monLfapARAsSent"), ("CTRON-LFAP-MIB", "monLfapARAsReceived"), ("CTRON-LFAP-MIB", "monLfapFSNsSent"), ("CTRON-LFAP-MIB", "monLfapFSNsReceived"), ("CTRON-LFAP-MIB", "monLfapFSAsSent"), ("CTRON-LFAP-MIB", "monLfapFSAsReceived"), ("CTRON-LFAP-MIB", "monLfapDroppedMessages"), ("CTRON-LFAP-MIB", "monLfapVRsSent"), ("CTRON-LFAP-MIB", "monLfapVRAsReceived"), ("CTRON-LFAP-MIB", "monLfapConnSuccess"), ("CTRON-LFAP-MIB", "monLfapConnFailure"), ("CTRON-LFAP-MIB", "monLfapBytesSent"), ("CTRON-LFAP-MIB", "monLfapBytesReceived"), ("CTRON-LFAP-MIB", "monLfapMsgsSent"), ("CTRON-LFAP-MIB", "monLfapMsgsReceived"), ("CTRON-LFAP-MIB", "monLfapMsgsReceivedError"), ("CTRON-LFAP-MIB", "monLfapMsgsSendQueue"), ("CTRON-LFAP-MIB", "monLfapMsgsSendQueuePeak"), ("CTRON-LFAP-MIB", "monLfapMsgsReceiveQueue"), ("CTRON-LFAP-MIB", "monLfapDroppedMessagesConnected"), ("CTRON-LFAP-MIB", "monLfapDroppedFARs"), ("CTRON-LFAP-MIB", "monLfapDroppedFUNIs"), ("CTRON-LFAP-MIB", "monLfapDroppedFUNs"), ("CTRON-LFAP-MIB", "monLfapDroppedARs"), ("CTRON-LFAP-MIB", "monLfapDroppedARAs"), ("CTRON-LFAP-MIB", "monLfapDroppedVRs"), ("CTRON-LFAP-MIB", "monLfapYesRespCnt"), ("CTRON-LFAP-MIB", "monLfapNoRespCnt"), ("CTRON-LFAP-MIB", "monLfapFlowSetups"), ("CTRON-LFAP-MIB", "monLfapFlowTeardowns"), ("CTRON-LFAP-MIB", "monLfapFlowActivePeak"), ("CTRON-LFAP-MIB", "monActiveCxnCnt"), ("CTRON-LFAP-MIB", "flowPolicyPollingTimerInterval"), ("CTRON-LFAP-MIB", "flowPolicyPollingBatchSize"), ("CTRON-LFAP-MIB", "flowPolicyPollingBatchInterval"), ("CTRON-LFAP-MIB", "flowPolicyPollingBatchUpdateInterval"), ("CTRON-LFAP-MIB", "flowPolicyPollingLostContactInterval"), ("CTRON-LFAP-MIB", "flowPolicyPollingServerRetryInterval"), ("CTRON-LFAP-MIB", "flowPolicyPollingSendQueueMaxSize"), ("CTRON-LFAP-MIB", "flowPolicyPollingTaskPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lfapConfGroupV40 = lfapConfGroupV40.setStatus('current')
mibBuilder.exportSymbols("CTRON-LFAP-MIB", monLfapMsgsReceiveQueue=monLfapMsgsReceiveQueue, monLfapFlowActivePeak=monLfapFlowActivePeak, flowPolicyPollingTimerInterval=flowPolicyPollingTimerInterval, monLfapFUAsReceived=monLfapFUAsReceived, monLfapDroppedARs=monLfapDroppedARs, flowPolicyServerAddrIndex=flowPolicyServerAddrIndex, lfapConformance=lfapConformance, flowPolicyPollingBatchInterval=flowPolicyPollingBatchInterval, flowPolicyPollingBatchSize=flowPolicyPollingBatchSize, PYSNMP_MODULE_ID=ctLFAP, monLfapMsgsSendQueue=monLfapMsgsSendQueue, monLfapFSAsSent=monLfapFSAsSent, flowPolicyPollingLostContactInterval=flowPolicyPollingLostContactInterval, flowPolicyConfigPolicy=flowPolicyConfigPolicy, monLfapYesRespCnt=monLfapYesRespCnt, monLfapDroppedFUNIs=monLfapDroppedFUNIs, lfapConfGroupV10=lfapConfGroupV10, monLfapFlowSetups=monLfapFlowSetups, monLfapARsReceived=monLfapARsReceived, monLfapFSAsReceived=monLfapFSAsReceived, monLfapVRsSent=monLfapVRsSent, monLfapDroppedARAs=monLfapDroppedARAs, monLfapMsgsReceivedError=monLfapMsgsReceivedError, flowPolicyActiveServer=flowPolicyActiveServer, flowPolicyServerAddr=flowPolicyServerAddr, monLfapFAAsReceived=monLfapFAAsReceived, monLfapMsgsReceived=monLfapMsgsReceived, monLfapFUNsReceived=monLfapFUNsReceived, lfapComplianceV10=lfapComplianceV10, monLfapARsSent=monLfapARsSent, monLfapFCRsReceived=monLfapFCRsReceived, monActiveCxnCnt=monActiveCxnCnt, monLfapDroppedVRs=monLfapDroppedVRs, flowPolicyPollingSendQueueMaxSize=flowPolicyPollingSendQueueMaxSize, monLfapMsgsSent=monLfapMsgsSent, monLfapNoRespCnt=monLfapNoRespCnt, flowPolicyConfigStatistics=flowPolicyConfigStatistics, monLfap=monLfap, monLfapConnSuccess=monLfapConnSuccess, lfapComplianceV40=lfapComplianceV40, monLfapFCAsSent=monLfapFCAsSent, flowPolicyPollingTaskPriority=flowPolicyPollingTaskPriority, flowPolicyServerAddrEntry=flowPolicyServerAddrEntry, flowPolicyControl=flowPolicyControl, lfapCompliances=lfapCompliances, monLfapFUNsSent=monLfapFUNsSent, monLfapVRAsReceived=monLfapVRAsReceived, flowPolicyServerAddrTable=flowPolicyServerAddrTable, flowPolicy=flowPolicy, monCxnCounts=monCxnCounts, monLfapARAsReceived=monLfapARAsReceived, monLfapFSNsReceived=monLfapFSNsReceived, monLfapDroppedFUNs=monLfapDroppedFUNs, monLfapBytesSent=monLfapBytesSent, monLfapARAsSent=monLfapARAsSent, monLfapFARsReceived=monLfapFARsReceived, monLfapFARsSent=monLfapFARsSent, lfapGroups=lfapGroups, monLfapMsgsSendQueuePeak=monLfapMsgsSendQueuePeak, flowPolicyPollingServerRetryInterval=flowPolicyPollingServerRetryInterval, ctLFAP=ctLFAP, monLfapFCRsSent=monLfapFCRsSent, monLfapBytesReceived=monLfapBytesReceived, monLfapFAAsSent=monLfapFAAsSent, monLfapFUAsSent=monLfapFUAsSent, monLfapFAUsReceived=monLfapFAUsReceived, monLfapFCAsReceived=monLfapFCAsReceived, monLfapConnFailure=monLfapConnFailure, monLfapFlowTeardowns=monLfapFlowTeardowns, flowPolicyConfig=flowPolicyConfig, monLfapDroppedMessages=monLfapDroppedMessages, monLfapFSNsSent=monLfapFSNsSent, monLfapCounts=monLfapCounts, monLfapDroppedFARs=monLfapDroppedFARs, flowPolicyPolling=flowPolicyPolling, monLfapDroppedMessagesConnected=monLfapDroppedMessagesConnected, lfapConfGroupV40=lfapConfGroupV40, monLfapFAUsSent=monLfapFAUsSent, flowPolicyStatus=flowPolicyStatus, flowPolicyPollingBatchUpdateInterval=flowPolicyPollingBatchUpdateInterval)