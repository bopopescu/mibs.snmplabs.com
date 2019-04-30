#
# PySNMP MIB module ASCEND-MIBSS7NMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBSS7NMI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:12:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, Gauge32, iso, Unsigned32, ModuleIdentity, ObjectIdentity, TimeTicks, Counter32, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Gauge32", "iso", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Counter32", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibsS7Profile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 121))
mibpRITunlStatProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 158))
mibsS7ProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 121, 1), )
if mibBuilder.loadTexts: mibsS7ProfileTable.setStatus('mandatory')
mibsS7ProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1), ).setIndexNames((0, "ASCEND-MIBSS7NMI-MIB", "sS7Profile-Index-o"))
if mibBuilder.loadTexts: mibsS7ProfileEntry.setStatus('mandatory')
sS7Profile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 1), Integer32()).setLabel("sS7Profile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: sS7Profile_Index_o.setStatus('mandatory')
sS7Profile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("sS7Profile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_Enabled.setStatus('mandatory')
sS7Profile_ControlProtocol = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("asgcp", 1), ("ipdc0X", 2), ("q931Plus", 3)))).setLabel("sS7Profile-ControlProtocol").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_ControlProtocol.setStatus('mandatory')
sS7Profile_PrimaryIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 4), IpAddress()).setLabel("sS7Profile-PrimaryIpAddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_PrimaryIpAddress.setStatus('mandatory')
sS7Profile_PrimaryTcpPort = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 5), Integer32()).setLabel("sS7Profile-PrimaryTcpPort").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_PrimaryTcpPort.setStatus('mandatory')
sS7Profile_SecondaryIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 6), IpAddress()).setLabel("sS7Profile-SecondaryIpAddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_SecondaryIpAddress.setStatus('mandatory')
sS7Profile_SecondaryTcpPort = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 7), Integer32()).setLabel("sS7Profile-SecondaryTcpPort").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_SecondaryTcpPort.setStatus('mandatory')
sS7Profile_BayId = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 8), DisplayString()).setLabel("sS7Profile-BayId").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_BayId.setStatus('mandatory')
sS7Profile_SystemType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 9), DisplayString()).setLabel("sS7Profile-SystemType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_SystemType.setStatus('mandatory')
sS7Profile_TransportOptions_Type = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ascend", 1), ("tcpEncaps2", 2)))).setLabel("sS7Profile-TransportOptions-Type").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_TransportOptions_Type.setStatus('mandatory')
sS7Profile_TransportOptions_DeviceId = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 11), Integer32()).setLabel("sS7Profile-TransportOptions-DeviceId").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_TransportOptions_DeviceId.setStatus('mandatory')
sS7Profile_TransportOptions_T1Duration = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 12), Integer32()).setLabel("sS7Profile-TransportOptions-T1Duration").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_TransportOptions_T1Duration.setStatus('mandatory')
sS7Profile_TransportOptions_T2Duration = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 13), Integer32()).setLabel("sS7Profile-TransportOptions-T2Duration").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_TransportOptions_T2Duration.setStatus('mandatory')
sS7Profile_TransportOptions_T3Duration = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 14), Integer32()).setLabel("sS7Profile-TransportOptions-T3Duration").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_TransportOptions_T3Duration.setStatus('mandatory')
sS7Profile_TransportOptions_WindowSize = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 15), Integer32()).setLabel("sS7Profile-TransportOptions-WindowSize").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_TransportOptions_WindowSize.setStatus('mandatory')
sS7Profile_TransportOptions_AckThreshold = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 16), Integer32()).setLabel("sS7Profile-TransportOptions-AckThreshold").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_TransportOptions_AckThreshold.setStatus('mandatory')
sS7Profile_TransportOptions_HeartBeat = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("sS7Profile-TransportOptions-HeartBeat").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_TransportOptions_HeartBeat.setStatus('mandatory')
sS7Profile_TransportOptions_Tos_Active = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("sS7Profile-TransportOptions-Tos-Active").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_TransportOptions_Tos_Active.setStatus('mandatory')
sS7Profile_TransportOptions_Tos_Precedence = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 33, 65, 97, 129, 161, 193, 225))).clone(namedValues=NamedValues(("n-000", 1), ("n-001", 33), ("n-010", 65), ("n-011", 97), ("n-100", 129), ("n-101", 161), ("n-110", 193), ("n-111", 225)))).setLabel("sS7Profile-TransportOptions-Tos-Precedence").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_TransportOptions_Tos_Precedence.setStatus('mandatory')
sS7Profile_TransportOptions_Tos_TypeOfService = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 36), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 5, 9, 17))).clone(namedValues=NamedValues(("normal", 1), ("cost", 3), ("reliability", 5), ("throughput", 9), ("latency", 17)))).setLabel("sS7Profile-TransportOptions-Tos-TypeOfService").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_TransportOptions_Tos_TypeOfService.setStatus('mandatory')
sS7Profile_TransportOptions_Tos_ApplyTo = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 37), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1025, 2049, 3073))).clone(namedValues=NamedValues(("incoming", 1025), ("outgoing", 2049), ("both", 3073)))).setLabel("sS7Profile-TransportOptions-Tos-ApplyTo").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_TransportOptions_Tos_ApplyTo.setStatus('mandatory')
sS7Profile_TransportOptions_Tos_MarkingType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 38), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("precedenceTos", 1), ("dscp", 2)))).setLabel("sS7Profile-TransportOptions-Tos-MarkingType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_TransportOptions_Tos_MarkingType.setStatus('mandatory')
sS7Profile_TransportOptions_Tos_Dscp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 39), DisplayString()).setLabel("sS7Profile-TransportOptions-Tos-Dscp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_TransportOptions_Tos_Dscp.setStatus('mandatory')
sS7Profile_UseSystemIpAddressAsSource = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("sS7Profile-UseSystemIpAddressAsSource").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_UseSystemIpAddressAsSource.setStatus('mandatory')
sS7Profile_IpdcSourceAdddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 32), IpAddress()).setLabel("sS7Profile-IpdcSourceAdddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_IpdcSourceAdddress.setStatus('mandatory')
sS7Profile_Vrouter = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 33), DisplayString()).setLabel("sS7Profile-Vrouter").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_Vrouter.setStatus('mandatory')
sS7Profile_CongestionControl_CongestionControlType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("l3QueueDepth", 2)))).setLabel("sS7Profile-CongestionControl-CongestionControlType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_CongestionControl_CongestionControlType.setStatus('mandatory')
sS7Profile_CongestionControl_Cl1Level = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 20), Integer32()).setLabel("sS7Profile-CongestionControl-Cl1Level").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_CongestionControl_Cl1Level.setStatus('mandatory')
sS7Profile_CongestionControl_Cl1Action = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ignore", 1), ("sendInfoToMgc", 2)))).setLabel("sS7Profile-CongestionControl-Cl1Action").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_CongestionControl_Cl1Action.setStatus('mandatory')
sS7Profile_CongestionControl_Cl2Level = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 22), Integer32()).setLabel("sS7Profile-CongestionControl-Cl2Level").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_CongestionControl_Cl2Level.setStatus('mandatory')
sS7Profile_CongestionControl_Cl2Action = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ignore", 1), ("sendInfoToMgc", 2), ("rejectNewCall", 3)))).setLabel("sS7Profile-CongestionControl-Cl2Action").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_CongestionControl_Cl2Action.setStatus('mandatory')
sS7Profile_SignalingHeartbeat_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("sS7Profile-SignalingHeartbeat-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_SignalingHeartbeat_Enabled.setStatus('mandatory')
sS7Profile_SignalingHeartbeat_Interval = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 25), Integer32()).setLabel("sS7Profile-SignalingHeartbeat-Interval").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_SignalingHeartbeat_Interval.setStatus('mandatory')
sS7Profile_ResilienceOptions_Type = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("releaseAll", 1), ("maintainActive", 2), ("timedRelease", 3)))).setLabel("sS7Profile-ResilienceOptions-Type").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_ResilienceOptions_Type.setStatus('mandatory')
sS7Profile_ResilienceOptions_Duration = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 28), Integer32()).setLabel("sS7Profile-ResilienceOptions-Duration").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_ResilienceOptions_Duration.setStatus('mandatory')
sS7Profile_PriTunnelingOptions_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("sS7Profile-PriTunnelingOptions-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_PriTunnelingOptions_Enabled.setStatus('mandatory')
sS7Profile_PriTunnelingOptions_Duration = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 30), Integer32()).setLabel("sS7Profile-PriTunnelingOptions-Duration").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_PriTunnelingOptions_Duration.setStatus('mandatory')
sS7Profile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("sS7Profile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: sS7Profile_Action_o.setStatus('mandatory')
mibpRITunlStatProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 158, 1), )
if mibBuilder.loadTexts: mibpRITunlStatProfileTable.setStatus('mandatory')
mibpRITunlStatProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 158, 1, 1), ).setIndexNames((0, "ASCEND-MIBSS7NMI-MIB", "pRITunlStatProfile-Index-o"))
if mibBuilder.loadTexts: mibpRITunlStatProfileEntry.setStatus('mandatory')
pRITunlStatProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 158, 1, 1, 1), Integer32()).setLabel("pRITunlStatProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: pRITunlStatProfile_Index_o.setStatus('mandatory')
pRITunlStatProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 158, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("pRITunlStatProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: pRITunlStatProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBSS7NMI-MIB", sS7Profile_TransportOptions_T3Duration=sS7Profile_TransportOptions_T3Duration, mibsS7Profile=mibsS7Profile, sS7Profile_Index_o=sS7Profile_Index_o, sS7Profile_Enabled=sS7Profile_Enabled, sS7Profile_SecondaryIpAddress=sS7Profile_SecondaryIpAddress, sS7Profile_BayId=sS7Profile_BayId, sS7Profile_TransportOptions_Tos_Active=sS7Profile_TransportOptions_Tos_Active, mibpRITunlStatProfileEntry=mibpRITunlStatProfileEntry, pRITunlStatProfile_Index_o=pRITunlStatProfile_Index_o, sS7Profile_TransportOptions_Type=sS7Profile_TransportOptions_Type, DisplayString=DisplayString, sS7Profile_ControlProtocol=sS7Profile_ControlProtocol, sS7Profile_TransportOptions_HeartBeat=sS7Profile_TransportOptions_HeartBeat, sS7Profile_TransportOptions_Tos_Dscp=sS7Profile_TransportOptions_Tos_Dscp, sS7Profile_IpdcSourceAdddress=sS7Profile_IpdcSourceAdddress, sS7Profile_TransportOptions_DeviceId=sS7Profile_TransportOptions_DeviceId, sS7Profile_Vrouter=sS7Profile_Vrouter, mibsS7ProfileTable=mibsS7ProfileTable, sS7Profile_SystemType=sS7Profile_SystemType, sS7Profile_SecondaryTcpPort=sS7Profile_SecondaryTcpPort, sS7Profile_TransportOptions_WindowSize=sS7Profile_TransportOptions_WindowSize, sS7Profile_PrimaryIpAddress=sS7Profile_PrimaryIpAddress, sS7Profile_TransportOptions_Tos_ApplyTo=sS7Profile_TransportOptions_Tos_ApplyTo, sS7Profile_ResilienceOptions_Duration=sS7Profile_ResilienceOptions_Duration, sS7Profile_Action_o=sS7Profile_Action_o, sS7Profile_CongestionControl_CongestionControlType=sS7Profile_CongestionControl_CongestionControlType, sS7Profile_CongestionControl_Cl1Action=sS7Profile_CongestionControl_Cl1Action, sS7Profile_CongestionControl_Cl2Action=sS7Profile_CongestionControl_Cl2Action, sS7Profile_CongestionControl_Cl1Level=sS7Profile_CongestionControl_Cl1Level, sS7Profile_PriTunnelingOptions_Enabled=sS7Profile_PriTunnelingOptions_Enabled, sS7Profile_TransportOptions_AckThreshold=sS7Profile_TransportOptions_AckThreshold, sS7Profile_ResilienceOptions_Type=sS7Profile_ResilienceOptions_Type, sS7Profile_TransportOptions_T1Duration=sS7Profile_TransportOptions_T1Duration, sS7Profile_PrimaryTcpPort=sS7Profile_PrimaryTcpPort, sS7Profile_CongestionControl_Cl2Level=sS7Profile_CongestionControl_Cl2Level, pRITunlStatProfile_Action_o=pRITunlStatProfile_Action_o, sS7Profile_SignalingHeartbeat_Enabled=sS7Profile_SignalingHeartbeat_Enabled, mibpRITunlStatProfile=mibpRITunlStatProfile, sS7Profile_TransportOptions_Tos_Precedence=sS7Profile_TransportOptions_Tos_Precedence, sS7Profile_TransportOptions_Tos_TypeOfService=sS7Profile_TransportOptions_Tos_TypeOfService, mibpRITunlStatProfileTable=mibpRITunlStatProfileTable, sS7Profile_TransportOptions_Tos_MarkingType=sS7Profile_TransportOptions_Tos_MarkingType, sS7Profile_SignalingHeartbeat_Interval=sS7Profile_SignalingHeartbeat_Interval, sS7Profile_TransportOptions_T2Duration=sS7Profile_TransportOptions_T2Duration, sS7Profile_UseSystemIpAddressAsSource=sS7Profile_UseSystemIpAddressAsSource, sS7Profile_PriTunnelingOptions_Duration=sS7Profile_PriTunnelingOptions_Duration, mibsS7ProfileEntry=mibsS7ProfileEntry)