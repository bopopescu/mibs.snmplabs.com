#
# PySNMP MIB module Nortel-MsCarrier-MscPassport-FrameRelayNniTraceMIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Nortel-MsCarrier-MscPassport-FrameRelayNniTraceMIB
# Produced by pysmi-0.3.4 at Wed May  1 14:30:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
mscFrNniIndex, mscFrNni = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex", "mscFrNni")
RowPointer, Unsigned32, DisplayString, StorageType, RowStatus = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB", "RowPointer", "Unsigned32", "DisplayString", "StorageType", "RowStatus")
AsciiString, NonReplicated = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-TextualConventionsMIB", "AsciiString", "NonReplicated")
mscPassportMIBs, = mibBuilder.importSymbols("Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB", "mscPassportMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ObjectIdentity, TimeTicks, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, NotificationType, Unsigned32, MibIdentifier, Bits, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "TimeTicks", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "NotificationType", "Unsigned32", "MibIdentifier", "Bits", "Counter64", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
frameRelayNniTraceMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 106))
mscFrNniTrace = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7))
mscFrNniTraceRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 1), )
if mibBuilder.loadTexts: mscFrNniTraceRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceRowStatusTable.setDescription('This entry controls the addition and deletion of mscFrNniTrace components.')
mscFrNniTraceRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"), (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniTraceMIB", "mscFrNniTraceIndex"))
if mibBuilder.loadTexts: mscFrNniTraceRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceRowStatusEntry.setDescription('A single entry in the table represents a single mscFrNniTrace component.')
mscFrNniTraceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 1, 1, 1), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscFrNniTraceRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceRowStatus.setDescription('This variable is used as the basis for SNMP naming of mscFrNniTrace components. These components can be added and deleted.')
mscFrNniTraceComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFrNniTraceComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
mscFrNniTraceStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFrNniTraceStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceStorageType.setDescription('This variable represents the storage type value for the mscFrNniTrace tables.')
mscFrNniTraceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscFrNniTraceIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceIndex.setDescription('This variable represents the index for the mscFrNniTrace tables.')
mscFrNniTraceOperationalTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 10), )
if mibBuilder.loadTexts: mscFrNniTraceOperationalTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceOperationalTable.setDescription('This group provides the operational attributes for the Trace component.')
mscFrNniTraceOperationalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"), (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniTraceMIB", "mscFrNniTraceIndex"))
if mibBuilder.loadTexts: mscFrNniTraceOperationalEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceOperationalEntry.setDescription('An entry in the mscFrNniTraceOperationalTable.')
mscFrNniTraceReceiverName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 10, 1, 2), AsciiString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscFrNniTraceReceiverName.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceReceiverName.setDescription('This attribute should be set to the name of the desired trace receiver before starting a trace session. All available trace receivers are listed under the Trace Rcvr/<string> component. This attribute cannot be set while a trace is active.')
mscFrNniTraceDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscFrNniTraceDuration.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceDuration.setDescription('This attribute specifies the duration, in minutes, of a trace session. A value of 0 indicates unlimited duration in which case a trace session remains active until a stop command is issued. The default duration is 60 minutes. This attribute cannot be set while a trace is active.')
mscFrNniTraceQueueLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 10, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(20)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscFrNniTraceQueueLimit.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceQueueLimit.setDescription('This attribute specifies the total number of bytes of traced data which may be queued for transmission to the trace receiver. When this limit is exceeded, incoming traced frames are discarded. This attribute can be set while a trace is active and takes effect immediately.')
mscFrNniTraceSession = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 10, 1, 5), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFrNniTraceSession.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceSession.setDescription('This attribute is set automatically. It identifies the Trace Session component which is forwarding the trace data. This attribute is empty unless a trace is active.')
mscFrNniTraceFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2))
mscFrNniTraceFilterRowStatusTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 1), )
if mibBuilder.loadTexts: mscFrNniTraceFilterRowStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceFilterRowStatusTable.setDescription('This entry controls the addition and deletion of mscFrNniTraceFilter components.')
mscFrNniTraceFilterRowStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 1, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"), (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniTraceMIB", "mscFrNniTraceIndex"), (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniTraceMIB", "mscFrNniTraceFilterIndex"))
if mibBuilder.loadTexts: mscFrNniTraceFilterRowStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceFilterRowStatusEntry.setDescription('A single entry in the table represents a single mscFrNniTraceFilter component.')
mscFrNniTraceFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 1, 1, 1), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFrNniTraceFilterRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceFilterRowStatus.setDescription('This variable is used as the basis for SNMP naming of mscFrNniTraceFilter components. These components cannot be added nor deleted.')
mscFrNniTraceFilterComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFrNniTraceFilterComponentName.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceFilterComponentName.setDescription("This variable provides the component's string name for use with the ASCII Console Interface")
mscFrNniTraceFilterStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 1, 1, 4), StorageType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mscFrNniTraceFilterStorageType.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceFilterStorageType.setDescription('This variable represents the storage type value for the mscFrNniTraceFilter tables.')
mscFrNniTraceFilterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 1, 1, 10), NonReplicated())
if mibBuilder.loadTexts: mscFrNniTraceFilterIndex.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceFilterIndex.setDescription('This variable represents the index for the mscFrNniTraceFilter tables.')
mscFrNniTraceFilterOperationalTable = MibTable((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 10), )
if mibBuilder.loadTexts: mscFrNniTraceFilterOperationalTable.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceFilterOperationalTable.setDescription('This group provides the operational attributes for the Frame Relay Trace Filter component.')
mscFrNniTraceFilterOperationalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 10, 1), ).setIndexNames((0, "Nortel-MsCarrier-MscPassport-FrameRelayNniMIB", "mscFrNniIndex"), (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniTraceMIB", "mscFrNniTraceIndex"), (0, "Nortel-MsCarrier-MscPassport-FrameRelayNniTraceMIB", "mscFrNniTraceFilterIndex"))
if mibBuilder.loadTexts: mscFrNniTraceFilterOperationalEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceFilterOperationalEntry.setDescription('An entry in the mscFrNniTraceFilterOperationalTable.')
mscFrNniTraceFilterTraceType = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 10, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1).clone(hexValue="e0")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscFrNniTraceFilterTraceType.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceFilterTraceType.setDescription('This attribute specifies the level of filtering required for this trace session. A value of lmi indicates that Lmi frames are traced. A value of dlci indicates that frames from the Dlci specified by the tracedDlci attribute are traced. A value of badFrames indicates that bad received frames (overruns, CRC errors, aborts) are traced. The default is to trace all frames. This attribute can be set while a trace is active and takes effect immediately. Description of bits: lmi(0) dlci(1) badFrames(2)')
mscFrNniTraceFilterTracedDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 10, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1007))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscFrNniTraceFilterTracedDlci.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceFilterTracedDlci.setDescription('This attribute specifies a particular Dlci to trace. A value of zero specifies that all Dlcis are to be traced. This attribute can be set while a trace is active and takes effect immediately.')
mscFrNniTraceFilterDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 10, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1).clone(hexValue="c0")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscFrNniTraceFilterDirection.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceFilterDirection.setDescription('This attribute specifies the direction of the data to be traced as viewed by the service. The values can be egress, and/or ingress. An egress value indicates frames outbound from the service. An ingress value indicates frames inbound to the service. This attribute can be set while a trace is active and takes effect immediately. Description of bits: egress(0) ingress(1)')
mscFrNniTraceFilterTracedLength = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 70, 7, 2, 10, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2000)).clone(2000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mscFrNniTraceFilterTracedLength.setStatus('mandatory')
if mibBuilder.loadTexts: mscFrNniTraceFilterTracedLength.setDescription('This attribute specifies the maximum number of bytes to trace per frame starting from the byte following the frame flag. If the frame length is longer than the value specified by this attribute, then the traced frame is truncated. This attribute can be set while a trace is active and takes effect immediately.')
frameRelayNniTraceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 106, 1))
frameRelayNniTraceGroupCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 106, 1, 1))
frameRelayNniTraceGroupCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 106, 1, 1, 3))
frameRelayNniTraceGroupCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 106, 1, 1, 3, 2))
frameRelayNniTraceCapabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 106, 3))
frameRelayNniTraceCapabilitiesCA = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 106, 3, 1))
frameRelayNniTraceCapabilitiesCA02 = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 106, 3, 1, 3))
frameRelayNniTraceCapabilitiesCA02A = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 106, 3, 1, 3, 2))
mibBuilder.exportSymbols("Nortel-MsCarrier-MscPassport-FrameRelayNniTraceMIB", mscFrNniTraceSession=mscFrNniTraceSession, mscFrNniTraceComponentName=mscFrNniTraceComponentName, mscFrNniTraceIndex=mscFrNniTraceIndex, frameRelayNniTraceGroupCA=frameRelayNniTraceGroupCA, mscFrNniTraceStorageType=mscFrNniTraceStorageType, frameRelayNniTraceCapabilitiesCA02=frameRelayNniTraceCapabilitiesCA02, mscFrNniTraceRowStatusTable=mscFrNniTraceRowStatusTable, mscFrNniTraceFilterIndex=mscFrNniTraceFilterIndex, mscFrNniTraceFilterTracedDlci=mscFrNniTraceFilterTracedDlci, mscFrNniTraceFilterRowStatusTable=mscFrNniTraceFilterRowStatusTable, frameRelayNniTraceCapabilitiesCA02A=frameRelayNniTraceCapabilitiesCA02A, mscFrNniTrace=mscFrNniTrace, frameRelayNniTraceMIB=frameRelayNniTraceMIB, mscFrNniTraceRowStatus=mscFrNniTraceRowStatus, mscFrNniTraceFilterStorageType=mscFrNniTraceFilterStorageType, frameRelayNniTraceGroup=frameRelayNniTraceGroup, mscFrNniTraceOperationalEntry=mscFrNniTraceOperationalEntry, mscFrNniTraceFilterTracedLength=mscFrNniTraceFilterTracedLength, mscFrNniTraceRowStatusEntry=mscFrNniTraceRowStatusEntry, mscFrNniTraceQueueLimit=mscFrNniTraceQueueLimit, mscFrNniTraceFilterDirection=mscFrNniTraceFilterDirection, frameRelayNniTraceCapabilitiesCA=frameRelayNniTraceCapabilitiesCA, mscFrNniTraceFilterOperationalTable=mscFrNniTraceFilterOperationalTable, frameRelayNniTraceGroupCA02A=frameRelayNniTraceGroupCA02A, mscFrNniTraceReceiverName=mscFrNniTraceReceiverName, mscFrNniTraceFilterRowStatus=mscFrNniTraceFilterRowStatus, mscFrNniTraceFilterOperationalEntry=mscFrNniTraceFilterOperationalEntry, mscFrNniTraceOperationalTable=mscFrNniTraceOperationalTable, mscFrNniTraceDuration=mscFrNniTraceDuration, mscFrNniTraceFilter=mscFrNniTraceFilter, mscFrNniTraceFilterTraceType=mscFrNniTraceFilterTraceType, frameRelayNniTraceCapabilities=frameRelayNniTraceCapabilities, frameRelayNniTraceGroupCA02=frameRelayNniTraceGroupCA02, mscFrNniTraceFilterRowStatusEntry=mscFrNniTraceFilterRowStatusEntry, mscFrNniTraceFilterComponentName=mscFrNniTraceFilterComponentName)