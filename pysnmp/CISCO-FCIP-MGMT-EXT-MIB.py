#
# PySNMP MIB module CISCO-FCIP-MGMT-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FCIP-MGMT-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:41:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
cfmFcipLinkEntry, cfmFcipEntityInstanceEntry = mibBuilder.importSymbols("CISCO-FCIP-MGMT-MIB", "cfmFcipLinkEntry", "cfmFcipEntityInstanceEntry")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoPort, = mibBuilder.importSymbols("CISCO-TC", "CiscoPort")
FcList, = mibBuilder.importSymbols("CISCO-ZS-MIB", "FcList")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetPortNumber, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, NotificationType, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, TimeTicks, IpAddress, MibIdentifier, Counter32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "NotificationType", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "TimeTicks", "IpAddress", "MibIdentifier", "Counter32", "ObjectIdentity", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoFcipMgmtExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 329))
ciscoFcipMgmtExtMIB.setRevisions(('2005-10-12 00:00', '2005-06-07 00:00', '2005-05-14 00:00', '2004-09-23 00:00', '2004-03-10 00:00', '2003-11-05 00:00', '2003-09-19 00:00', '2003-05-06 00:00', '2003-03-25 00:00', '2003-01-07 00:00', '2002-12-06 00:00',))
if mibBuilder.loadTexts: ciscoFcipMgmtExtMIB.setLastUpdated('200510120000Z')
if mibBuilder.loadTexts: ciscoFcipMgmtExtMIB.setOrganization('Cisco Systems Inc.')
ciscoFcipMgmtExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 329, 0))
ciscoFcipMgmtExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 329, 1))
ciscoFcipMgmtExtMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 329, 2))
cfmFcipMgmtExtConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1))
cfmFcipMgmtExtStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 2))
cfmFcipEntityExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1), )
if mibBuilder.loadTexts: cfmFcipEntityExtTable.setStatus('current')
cfmFcipEntityExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1), )
cfmFcipEntityInstanceEntry.registerAugmentions(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtEntry"))
cfmFcipEntityExtEntry.setIndexNames(*cfmFcipEntityInstanceEntry.getIndexNames())
if mibBuilder.loadTexts: cfmFcipEntityExtEntry.setStatus('current')
cfmFcipEntityExtTcpKeepAliveTO = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 7200)).clone(60)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipEntityExtTcpKeepAliveTO.setStatus('current')
cfmFcipEntityExtTcpMaxReTx = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)).clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipEntityExtTcpMaxReTx.setStatus('current')
cfmFcipEntityExtPMTUEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 3), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipEntityExtPMTUEnable.setStatus('current')
cfmFcipEntityExtPMTUResetTO = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(60, 3600)).clone(3600)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipEntityExtPMTUResetTO.setStatus('current')
cfmFcipEntityExtTcpMinRTO = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 5000)).clone(100)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipEntityExtTcpMinRTO.setStatus('current')
cfmFcipEntityExtTcpSendBufSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 8192))).setUnits('kilobytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipEntityExtTcpSendBufSize.setStatus('current')
cfmFcipEntityExtTcpMaxBW = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1000, 1000000)).clone(1000000)).setUnits('kilobits').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipEntityExtTcpMaxBW.setStatus('current')
cfmFcipEntityExtTcpMinAvailBW = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1000, 1000000)).clone(15000)).setUnits('kilobits').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipEntityExtTcpMinAvailBW.setStatus('current')
cfmFcipEntityExtTcpRndTrpTimeEst = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 300000)).clone(1000)).setUnits('microseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipEntityExtTcpRndTrpTimeEst.setStatus('current')
cfmFcipEntityExtCWMEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 10), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipEntityExtCWMEnable.setStatus('current')
cfmFcipEntityExtCWMBurstSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 100)).clone(50)).setUnits('kilobytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipEntityExtCWMBurstSize.setStatus('current')
cfmFcipEntityExtTcpSACKEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 12), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipEntityExtTcpSACKEnable.setStatus('current')
cfmFcipEntityExtTcpLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 13), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipEntityExtTcpLocalPort.setStatus('current')
cfmFcipEntityExtTcpMaxJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 1, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipEntityExtTcpMaxJitter.setStatus('current')
cfmFcipLinkExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2), )
if mibBuilder.loadTexts: cfmFcipLinkExtTable.setStatus('current')
cfmFcipLinkExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1), )
cfmFcipLinkEntry.registerAugmentions(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtEntry"))
cfmFcipLinkExtEntry.setIndexNames(*cfmFcipLinkEntry.getIndexNames())
if mibBuilder.loadTexts: cfmFcipLinkExtEntry.setStatus('current')
cfmFcipLinkExtPassiveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipLinkExtPassiveMode.setStatus('current')
cfmFcipLinkExtNumTcpConn = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(2)).setUnits('tcp connections').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipLinkExtNumTcpConn.setStatus('current')
cfmFcipLinkExtCheckTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 3), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipLinkExtCheckTimestamp.setStatus('current')
cfmFcipLinkExtTimestampTolerance = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 10000))).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipLinkExtTimestampTolerance.setStatus('current')
cfmFcipLinkExtTcpRemPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 5), CiscoPort().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipLinkExtTcpRemPort.setStatus('current')
cfmFcipLinkExtLocalBPortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipLinkExtLocalBPortEnable.setStatus('current')
cfmFcipLinkExtSpecialFrameEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipLinkExtSpecialFrameEnable.setStatus('current')
cfmFcipLinkExtBPortKAEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 8), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipLinkExtBPortKAEnable.setStatus('current')
cfmFcipLinkExtCntrlQOSField = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipLinkExtCntrlQOSField.setStatus('current')
cfmFcipLinkExtDataQOSField = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipLinkExtDataQOSField.setStatus('current')
cfmFcipLinkExtEthIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 11), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmFcipLinkExtEthIfIndex.setStatus('current')
cfmFcipLinkExtWriteAccelerator = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 12), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipLinkExtWriteAccelerator.setStatus('current')
cfmFcipLinkExtIPComp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("none", 1), ("highCompressionRatio", 2), ("highThroughput", 3), ("auto", 4), ("mode1", 5), ("mode2", 6), ("mode3", 7))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipLinkExtIPComp.setStatus('current')
cfmFcipLinkExtTapeAccelerator = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 14), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipLinkExtTapeAccelerator.setStatus('current')
cfmFcipLinkExtFlowCtrlBufSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 12288)).clone(256)).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipLinkExtFlowCtrlBufSize.setStatus('current')
cfmFcipLinkExtIPSec = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 16), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmFcipLinkExtIPSec.setStatus('current')
cfmFcipLinkExtPhyIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 17), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmFcipLinkExtPhyIfIndex.setStatus('current')
cfmFcipLinkExtWriteAccOper = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 18), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmFcipLinkExtWriteAccOper.setStatus('current')
cfmFcipLinkExtTapeAccOper = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 19), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmFcipLinkExtTapeAccOper.setStatus('current')
cfmFcipLinkExtTapeReadAccOper = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 20), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmFcipLinkExtTapeReadAccOper.setStatus('current')
cfmFcipLinkExtFiconTAVsanL2k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 21), FcList().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipLinkExtFiconTAVsanL2k.setStatus('current')
cfmFcipLinkExtFiconTAVsanL4k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 22), FcList().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cfmFcipLinkExtFiconTAVsanL4k.setStatus('current')
cfmFcipLinkExtFiconTAVsanLOper2k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 23), FcList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmFcipLinkExtFiconTAVsanLOper2k.setStatus('current')
cfmFcipLinkExtFiconTAVsanLOper4k = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 2, 1, 24), FcList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmFcipLinkExtFiconTAVsanLOper4k.setStatus('current')
cfmFcipLinkMapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 3), )
if mibBuilder.loadTexts: cfmFcipLinkMapTable.setStatus('current')
cfmFcipLinkMapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkMapIndex"))
if mibBuilder.loadTexts: cfmFcipLinkMapEntry.setStatus('current')
cfmFcipLinkMapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cfmFcipLinkMapIndex.setStatus('current')
cfmFcipMapEntityId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmFcipMapEntityId.setStatus('current')
cfmFcipLinkExtStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 2, 1), )
if mibBuilder.loadTexts: cfmFcipLinkExtStatsTable.setStatus('current')
cfmFcipLinkExtStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 2, 1, 1), )
cfmFcipLinkEntry.registerAugmentions(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtStatsEntry"))
cfmFcipLinkExtStatsEntry.setIndexNames(*cfmFcipLinkEntry.getIndexNames())
if mibBuilder.loadTexts: cfmFcipLinkExtStatsEntry.setStatus('current')
cfmFcipLinkStatsRxIPCompRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 2, 1, 1, 1), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmFcipLinkStatsRxIPCompRatio.setStatus('current')
cfmFcipLinkStatsTxIPCompRatio = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 329, 1, 2, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfmFcipLinkStatsTxIPCompRatio.setStatus('current')
cfmFcipExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 1))
cfmFcipExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2))
cfmFcipExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 1, 1)).setObjects(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtGroup"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmFcipExtCompliance = cfmFcipExtCompliance.setStatus('deprecated')
cfmFcipExtCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 1, 2)).setObjects(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtGroup"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroup"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmFcipExtCompliance1 = cfmFcipExtCompliance1.setStatus('deprecated')
cfmFcipExtCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 1, 3)).setObjects(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtGroup"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroup"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroupRev1"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtCWMGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmFcipExtCompliance2 = cfmFcipExtCompliance2.setStatus('deprecated')
cfmFcipExtCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 1, 4)).setObjects(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtGroup"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroup"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroupRev1"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtCWMGroup"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroupRev2"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtMapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmFcipExtCompliance3 = cfmFcipExtCompliance3.setStatus('deprecated')
cfmFcipExtCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 1, 5)).setObjects(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtGroup"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtGroupSup1"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroup"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroupRev1"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtCWMGroup"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroupRev2"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroupRev2Sup1"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtMapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmFcipExtCompliance4 = cfmFcipExtCompliance4.setStatus('deprecated')
cfmFcipExtCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 1, 6)).setObjects(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtGroup"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroup"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroupRev1"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtCWMGroup"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroupRev2"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroupRev2Sup1"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroupRev2Sup2"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmFcipExtCompliance5 = cfmFcipExtCompliance5.setStatus('deprecated')
cfmFcipExtCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 1, 7)).setObjects(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtGroup"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroup"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroupRev1"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtCWMGroup"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroupRev2"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroupRev2Sup1"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroupRev2Sup2"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtStatsGroup"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtGroupRev2Sup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmFcipExtCompliance6 = cfmFcipExtCompliance6.setStatus('current')
cfmFcipEntityExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 1)).setObjects(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpKeepAliveTO"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpMaxReTx"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtPMTUEnable"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtPMTUResetTO"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpMinRTO"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpSendBufSize"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpMaxBW"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpMinAvailBW"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpRndTrpTimeEst"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmFcipEntityExtGroup = cfmFcipEntityExtGroup.setStatus('current')
cfmFcipLinkExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 2)).setObjects(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtPassiveMode"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtNumTcpConn"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtCheckTimestamp"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtTimestampTolerance"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtTcpRemPort"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtLocalBPortEnable"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtSpecialFrameEnable"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtBPortKAEnable"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtCntrlQOSField"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtDataQOSField"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmFcipLinkExtGroup = cfmFcipLinkExtGroup.setStatus('current')
cfmFcipLinkExtGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 3)).setObjects(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtEthIfIndex"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtWriteAccelerator"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtIPComp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmFcipLinkExtGroupRev1 = cfmFcipLinkExtGroupRev1.setStatus('current')
cfmFcipEntityExtCWMGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 4)).setObjects(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtCWMEnable"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtCWMBurstSize"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpSACKEnable"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpLocalPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmFcipEntityExtCWMGroup = cfmFcipEntityExtCWMGroup.setStatus('current')
cfmFcipLinkExtGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 5)).setObjects(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtTapeAccelerator"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtFlowCtrlBufSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmFcipLinkExtGroupRev2 = cfmFcipLinkExtGroupRev2.setStatus('current')
cfmFcipLinkExtMapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 6)).setObjects(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipMapEntityId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmFcipLinkExtMapGroup = cfmFcipLinkExtMapGroup.setStatus('current')
cfmFcipEntityExtGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 7)).setObjects(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipEntityExtTcpMaxJitter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmFcipEntityExtGroupSup1 = cfmFcipEntityExtGroupSup1.setStatus('current')
cfmFcipLinkExtGroupRev2Sup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 8)).setObjects(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtIPSec"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmFcipLinkExtGroupRev2Sup1 = cfmFcipLinkExtGroupRev2Sup1.setStatus('current')
cfmFcipLinkExtGroupRev2Sup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 9)).setObjects(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtPhyIfIndex"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtWriteAccOper"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtTapeAccOper"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmFcipLinkExtGroupRev2Sup2 = cfmFcipLinkExtGroupRev2Sup2.setStatus('current')
cfmFcipLinkExtStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 10)).setObjects(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkStatsRxIPCompRatio"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkStatsTxIPCompRatio"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmFcipLinkExtStatsGroup = cfmFcipLinkExtStatsGroup.setStatus('current')
cfmFcipLinkExtGroupRev2Sup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 329, 2, 2, 11)).setObjects(("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtTapeReadAccOper"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtFiconTAVsanL2k"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtFiconTAVsanL4k"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtFiconTAVsanLOper2k"), ("CISCO-FCIP-MGMT-EXT-MIB", "cfmFcipLinkExtFiconTAVsanLOper4k"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmFcipLinkExtGroupRev2Sup3 = cfmFcipLinkExtGroupRev2Sup3.setStatus('current')
mibBuilder.exportSymbols("CISCO-FCIP-MGMT-EXT-MIB", cfmFcipEntityExtPMTUResetTO=cfmFcipEntityExtPMTUResetTO, cfmFcipEntityExtTcpSendBufSize=cfmFcipEntityExtTcpSendBufSize, cfmFcipLinkExtGroupRev2Sup3=cfmFcipLinkExtGroupRev2Sup3, cfmFcipEntityExtTcpLocalPort=cfmFcipEntityExtTcpLocalPort, ciscoFcipMgmtExtMIBObjects=ciscoFcipMgmtExtMIBObjects, cfmFcipEntityExtTcpSACKEnable=cfmFcipEntityExtTcpSACKEnable, cfmFcipLinkExtEthIfIndex=cfmFcipLinkExtEthIfIndex, cfmFcipLinkExtFiconTAVsanL2k=cfmFcipLinkExtFiconTAVsanL2k, cfmFcipLinkStatsTxIPCompRatio=cfmFcipLinkStatsTxIPCompRatio, cfmFcipLinkExtDataQOSField=cfmFcipLinkExtDataQOSField, cfmFcipLinkExtPassiveMode=cfmFcipLinkExtPassiveMode, cfmFcipEntityExtTcpMaxReTx=cfmFcipEntityExtTcpMaxReTx, cfmFcipLinkExtWriteAccelerator=cfmFcipLinkExtWriteAccelerator, ciscoFcipMgmtExtMIBConform=ciscoFcipMgmtExtMIBConform, cfmFcipLinkMapIndex=cfmFcipLinkMapIndex, cfmFcipExtCompliance5=cfmFcipExtCompliance5, cfmFcipMgmtExtStats=cfmFcipMgmtExtStats, cfmFcipLinkExtFiconTAVsanLOper4k=cfmFcipLinkExtFiconTAVsanLOper4k, cfmFcipEntityExtTcpMinRTO=cfmFcipEntityExtTcpMinRTO, cfmFcipLinkExtGroupRev2Sup2=cfmFcipLinkExtGroupRev2Sup2, cfmFcipEntityExtEntry=cfmFcipEntityExtEntry, cfmFcipLinkMapEntry=cfmFcipLinkMapEntry, cfmFcipLinkExtFiconTAVsanLOper2k=cfmFcipLinkExtFiconTAVsanLOper2k, cfmFcipLinkExtGroupRev2Sup1=cfmFcipLinkExtGroupRev2Sup1, cfmFcipMapEntityId=cfmFcipMapEntityId, cfmFcipLinkExtTapeAccOper=cfmFcipLinkExtTapeAccOper, cfmFcipEntityExtTcpRndTrpTimeEst=cfmFcipEntityExtTcpRndTrpTimeEst, cfmFcipLinkExtGroupRev2=cfmFcipLinkExtGroupRev2, cfmFcipExtGroups=cfmFcipExtGroups, cfmFcipEntityExtTcpKeepAliveTO=cfmFcipEntityExtTcpKeepAliveTO, cfmFcipLinkMapTable=cfmFcipLinkMapTable, cfmFcipLinkExtGroupRev1=cfmFcipLinkExtGroupRev1, cfmFcipLinkExtFlowCtrlBufSize=cfmFcipLinkExtFlowCtrlBufSize, cfmFcipMgmtExtConfig=cfmFcipMgmtExtConfig, cfmFcipExtCompliance6=cfmFcipExtCompliance6, cfmFcipLinkExtIPSec=cfmFcipLinkExtIPSec, ciscoFcipMgmtExtMIBNotifs=ciscoFcipMgmtExtMIBNotifs, cfmFcipExtCompliance1=cfmFcipExtCompliance1, cfmFcipExtCompliances=cfmFcipExtCompliances, cfmFcipLinkExtFiconTAVsanL4k=cfmFcipLinkExtFiconTAVsanL4k, cfmFcipLinkExtStatsGroup=cfmFcipLinkExtStatsGroup, cfmFcipLinkExtStatsEntry=cfmFcipLinkExtStatsEntry, cfmFcipLinkExtSpecialFrameEnable=cfmFcipLinkExtSpecialFrameEnable, cfmFcipLinkExtTapeReadAccOper=cfmFcipLinkExtTapeReadAccOper, cfmFcipLinkExtPhyIfIndex=cfmFcipLinkExtPhyIfIndex, cfmFcipEntityExtTable=cfmFcipEntityExtTable, cfmFcipLinkExtLocalBPortEnable=cfmFcipLinkExtLocalBPortEnable, cfmFcipLinkExtTapeAccelerator=cfmFcipLinkExtTapeAccelerator, PYSNMP_MODULE_ID=ciscoFcipMgmtExtMIB, cfmFcipExtCompliance2=cfmFcipExtCompliance2, cfmFcipLinkExtWriteAccOper=cfmFcipLinkExtWriteAccOper, cfmFcipLinkExtCntrlQOSField=cfmFcipLinkExtCntrlQOSField, cfmFcipLinkExtStatsTable=cfmFcipLinkExtStatsTable, cfmFcipLinkExtBPortKAEnable=cfmFcipLinkExtBPortKAEnable, cfmFcipEntityExtCWMEnable=cfmFcipEntityExtCWMEnable, cfmFcipEntityExtTcpMaxJitter=cfmFcipEntityExtTcpMaxJitter, cfmFcipLinkExtMapGroup=cfmFcipLinkExtMapGroup, cfmFcipExtCompliance3=cfmFcipExtCompliance3, cfmFcipLinkExtTimestampTolerance=cfmFcipLinkExtTimestampTolerance, cfmFcipLinkExtIPComp=cfmFcipLinkExtIPComp, cfmFcipLinkStatsRxIPCompRatio=cfmFcipLinkStatsRxIPCompRatio, cfmFcipLinkExtNumTcpConn=cfmFcipLinkExtNumTcpConn, cfmFcipExtCompliance=cfmFcipExtCompliance, cfmFcipLinkExtGroup=cfmFcipLinkExtGroup, cfmFcipEntityExtGroupSup1=cfmFcipEntityExtGroupSup1, cfmFcipEntityExtPMTUEnable=cfmFcipEntityExtPMTUEnable, cfmFcipLinkExtEntry=cfmFcipLinkExtEntry, cfmFcipLinkExtTable=cfmFcipLinkExtTable, cfmFcipEntityExtGroup=cfmFcipEntityExtGroup, cfmFcipEntityExtTcpMinAvailBW=cfmFcipEntityExtTcpMinAvailBW, cfmFcipEntityExtCWMGroup=cfmFcipEntityExtCWMGroup, cfmFcipExtCompliance4=cfmFcipExtCompliance4, cfmFcipEntityExtTcpMaxBW=cfmFcipEntityExtTcpMaxBW, cfmFcipEntityExtCWMBurstSize=cfmFcipEntityExtCWMBurstSize, ciscoFcipMgmtExtMIB=ciscoFcipMgmtExtMIB, cfmFcipLinkExtCheckTimestamp=cfmFcipLinkExtCheckTimestamp, cfmFcipLinkExtTcpRemPort=cfmFcipLinkExtTcpRemPort)