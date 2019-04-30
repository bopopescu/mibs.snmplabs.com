#
# PySNMP MIB module HUAWEI-BRAS-VSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-BRAS-VSM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:31:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
hwBRASMib, = mibBuilder.importSymbols("HUAWEI-MIB", "hwBRASMib")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, IpAddress, Counter32, Unsigned32, ModuleIdentity, Bits, Counter64, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "IpAddress", "Counter32", "Unsigned32", "ModuleIdentity", "Bits", "Counter64", "ObjectIdentity", "TimeTicks")
DateAndTime, TruthValue, RowStatus, TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TruthValue", "RowStatus", "TextualConvention", "DisplayString", "MacAddress")
hwBRASVsm = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9))
if mibBuilder.loadTexts: hwBRASVsm.setLastUpdated('200504181334Z')
if mibBuilder.loadTexts: hwBRASVsm.setOrganization('Huawei Technologies Co., Ltd. ')
hwVsmSetFlowQryTLenTable = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 1))
hwVsmSetTimeLen = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmSetTimeLen.setStatus('current')
hwVsmServicePolicyTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2), )
if mibBuilder.loadTexts: hwVsmServicePolicyTable.setStatus('current')
hwVsmServicePolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1), ).setIndexNames((0, "HUAWEI-BRAS-VSM-MIB", "hwVsmServicePolicyName"))
if mibBuilder.loadTexts: hwVsmServicePolicyEntry.setStatus('current')
hwVsmServicePolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmServicePolicyName.setStatus('current')
hwVsmAcctSchemeName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmAcctSchemeName.setStatus('current')
hwVsmTrafficPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmTrafficPolicyName.setStatus('current')
hwVsmSetIdleCutTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 120))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmSetIdleCutTime.setStatus('current')
hwVsmSetIdleCutFlow = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 768000)).clone(60)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmSetIdleCutFlow.setStatus('current')
hwVsmSevicePolicyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmSevicePolicyRowStatus.setStatus('current')
hwVsmOutTrafficPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmOutTrafficPolicyName.setStatus('current')
hwVsmDaaPolicyFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("vas", 0), ("daa", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmDaaPolicyFlag.setStatus('current')
hwVsmSetTariffLevel1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmSetTariffLevel1.setStatus('current')
hwVsmSetTariffLevel2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmSetTariffLevel2.setStatus('current')
hwVsmSetTariffLevel3 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmSetTariffLevel3.setStatus('current')
hwVsmSetTariffLevel4 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmSetTariffLevel4.setStatus('current')
hwVsmSetTariffLevel5 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmSetTariffLevel5.setStatus('current')
hwVsmSetTariffLevel6 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmSetTariffLevel6.setStatus('current')
hwVsmSetTariffLevel7 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmSetTariffLevel7.setStatus('current')
hwVsmSetTariffLevel8 = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmSetTariffLevel8.setStatus('current')
hwVsmTariffLevel1AcctSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 17), EnabledStatus().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmTariffLevel1AcctSwitch.setStatus('current')
hwVsmTariffLevel2AcctSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 18), EnabledStatus().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmTariffLevel2AcctSwitch.setStatus('current')
hwVsmTariffLevel3AcctSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 19), EnabledStatus().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmTariffLevel3AcctSwitch.setStatus('current')
hwVsmTariffLevel4AcctSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 20), EnabledStatus().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmTariffLevel4AcctSwitch.setStatus('current')
hwVsmTariffLevel5AcctSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 21), EnabledStatus().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmTariffLevel5AcctSwitch.setStatus('current')
hwVsmTariffLevel6AcctSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 22), EnabledStatus().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmTariffLevel6AcctSwitch.setStatus('current')
hwVsmTariffLevel7AcctSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 23), EnabledStatus().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmTariffLevel7AcctSwitch.setStatus('current')
hwVsmTariffLevel8AcctSwitch = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 24), EnabledStatus().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmTariffLevel8AcctSwitch.setStatus('current')
hwVsmValServiceTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3), )
if mibBuilder.loadTexts: hwVsmValServiceTable.setStatus('current')
hwVsmValServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1), ).setIndexNames((0, "HUAWEI-BRAS-VSM-MIB", "hwVsmServiceID"), (0, "HUAWEI-BRAS-VSM-MIB", "hwVsmServiceSlot"))
if mibBuilder.loadTexts: hwVsmValServiceEntry.setStatus('current')
hwVsmServiceID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmServiceID.setStatus('current')
hwVsmUserID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(4294967295)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmUserID.setStatus('current')
hwVsmFlowNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmFlowNum.setStatus('current')
hwVsmServiceSource = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("vsmSourceDefault", 0), ("vsmSourceSig", 1), ("vsmSourceIptn", 2), ("vsmSourceRadius", 3), ("vsmSourceBod", 4), ("vsmSourceCopsNet", 5), ("vsmSourceCopsNetPm", 6), ("vsmSourceCopsUser", 7), ("vsmSourceCopsPm", 8), ("vsmSourceBmi", 9), ("vsmSourceIpBod", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmServiceSource.setStatus('current')
hwVsmServiceSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmServiceSlot.setStatus('current')
hwVsmValServicePolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmValServicePolicy.setStatus('current')
hwVsmAcctMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("local", 1), ("none", 2), ("radius", 3), ("cops", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmAcctMethod.setStatus('current')
hwVsmAcctStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmAcctStartTime.setStatus('current')
hwVsmAcctServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmAcctServerName.setStatus('current')
hwVsmTwoLevelAcctServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmTwoLevelAcctServerName.setStatus('current')
hwVsmPhyInfoAcctServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmPhyInfoAcctServerName.setStatus('current')
hwVsmServiceIdleCutTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 120))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmServiceIdleCutTime.setStatus('current')
hwVsmServiceIdleCutFlow = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 768000)).clone(60)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmServiceIdleCutFlow.setStatus('current')
hwVsmUpPacketNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmUpPacketNum.setStatus('current')
hwVsmUpByteNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmUpByteNum.setStatus('current')
hwVsmDownPacketNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmDownPacketNum.setStatus('current')
hwVsmDownByteNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmDownByteNum.setStatus('current')
hwVsmDownloadServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmDownloadServerName.setStatus('current')
hwVsmAcctServerType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVsmAcctServerType.setStatus('current')
hwVsmAcctServicePolicyEnableTable = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 5))
hwVsmAcctServicePolicyEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 5, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmAcctServicePolicyEnable.setStatus('current')
hwVsmAcctServicePolicyDisable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 5, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwVsmAcctServicePolicyDisable.setStatus('current')
hwVsmConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 4))
hwVsmCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 4, 1))
hwVsmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 4, 1, 1)).setObjects(("HUAWEI-BRAS-VSM-MIB", "hwVsmSetFlowQryTLenObjectGroup"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmServicePolicyObjectGroup"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmValServiceObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVsmCompliance = hwVsmCompliance.setStatus('current')
hwVsmObjectGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 4, 2))
hwVsmSetFlowQryTLenObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 4, 2, 1)).setObjects(("HUAWEI-BRAS-VSM-MIB", "hwVsmSetTimeLen"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVsmSetFlowQryTLenObjectGroup = hwVsmSetFlowQryTLenObjectGroup.setStatus('current')
hwVsmServicePolicyObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 4, 2, 2)).setObjects(("HUAWEI-BRAS-VSM-MIB", "hwVsmServicePolicyName"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmAcctSchemeName"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmTrafficPolicyName"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetIdleCutTime"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetIdleCutFlow"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmSevicePolicyRowStatus"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmOutTrafficPolicyName"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmDaaPolicyFlag"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetTariffLevel1"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetTariffLevel2"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetTariffLevel3"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetTariffLevel4"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetTariffLevel5"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetTariffLevel6"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetTariffLevel7"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetTariffLevel8"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmTariffLevel1AcctSwitch"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmTariffLevel2AcctSwitch"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmTariffLevel3AcctSwitch"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmTariffLevel4AcctSwitch"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmTariffLevel5AcctSwitch"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmTariffLevel6AcctSwitch"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmTariffLevel7AcctSwitch"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmTariffLevel8AcctSwitch"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVsmServicePolicyObjectGroup = hwVsmServicePolicyObjectGroup.setStatus('current')
hwVsmValServiceObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 4, 2, 3)).setObjects(("HUAWEI-BRAS-VSM-MIB", "hwVsmServiceID"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmUserID"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmFlowNum"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmServiceSource"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmServiceSlot"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmValServicePolicy"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmAcctMethod"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmAcctStartTime"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmAcctServerName"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmTwoLevelAcctServerName"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmPhyInfoAcctServerName"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmServiceIdleCutTime"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmServiceIdleCutFlow"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmUpPacketNum"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmUpByteNum"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmDownPacketNum"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmDownByteNum"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmDownloadServerName"), ("HUAWEI-BRAS-VSM-MIB", "hwVsmAcctServerType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwVsmValServiceObjectGroup = hwVsmValServiceObjectGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-BRAS-VSM-MIB", hwVsmSetIdleCutTime=hwVsmSetIdleCutTime, hwVsmAcctMethod=hwVsmAcctMethod, hwVsmUpByteNum=hwVsmUpByteNum, hwVsmSetFlowQryTLenTable=hwVsmSetFlowQryTLenTable, hwVsmSevicePolicyRowStatus=hwVsmSevicePolicyRowStatus, hwVsmAcctServerName=hwVsmAcctServerName, hwVsmPhyInfoAcctServerName=hwVsmPhyInfoAcctServerName, hwVsmSetTariffLevel6=hwVsmSetTariffLevel6, hwVsmSetTariffLevel8=hwVsmSetTariffLevel8, hwVsmConformance=hwVsmConformance, hwVsmTariffLevel1AcctSwitch=hwVsmTariffLevel1AcctSwitch, hwVsmValServicePolicy=hwVsmValServicePolicy, hwVsmTwoLevelAcctServerName=hwVsmTwoLevelAcctServerName, hwVsmSetTariffLevel7=hwVsmSetTariffLevel7, hwVsmDownPacketNum=hwVsmDownPacketNum, hwVsmTariffLevel7AcctSwitch=hwVsmTariffLevel7AcctSwitch, hwVsmDownloadServerName=hwVsmDownloadServerName, hwVsmCompliances=hwVsmCompliances, hwVsmServiceID=hwVsmServiceID, hwVsmValServiceEntry=hwVsmValServiceEntry, hwVsmAcctServerType=hwVsmAcctServerType, hwVsmTariffLevel6AcctSwitch=hwVsmTariffLevel6AcctSwitch, hwVsmFlowNum=hwVsmFlowNum, hwVsmServiceSlot=hwVsmServiceSlot, hwVsmAcctServicePolicyDisable=hwVsmAcctServicePolicyDisable, hwVsmCompliance=hwVsmCompliance, PYSNMP_MODULE_ID=hwBRASVsm, hwVsmTariffLevel3AcctSwitch=hwVsmTariffLevel3AcctSwitch, hwVsmTariffLevel5AcctSwitch=hwVsmTariffLevel5AcctSwitch, hwVsmSetTariffLevel4=hwVsmSetTariffLevel4, hwVsmUserID=hwVsmUserID, hwVsmTariffLevel2AcctSwitch=hwVsmTariffLevel2AcctSwitch, hwVsmValServiceTable=hwVsmValServiceTable, hwVsmAcctStartTime=hwVsmAcctStartTime, hwVsmAcctServicePolicyEnableTable=hwVsmAcctServicePolicyEnableTable, hwVsmAcctSchemeName=hwVsmAcctSchemeName, hwVsmServicePolicyEntry=hwVsmServicePolicyEntry, hwVsmOutTrafficPolicyName=hwVsmOutTrafficPolicyName, hwVsmServiceIdleCutFlow=hwVsmServiceIdleCutFlow, hwVsmSetTariffLevel1=hwVsmSetTariffLevel1, hwVsmServicePolicyName=hwVsmServicePolicyName, hwVsmUpPacketNum=hwVsmUpPacketNum, hwVsmValServiceObjectGroup=hwVsmValServiceObjectGroup, hwVsmSetIdleCutFlow=hwVsmSetIdleCutFlow, hwVsmSetTimeLen=hwVsmSetTimeLen, hwVsmSetTariffLevel2=hwVsmSetTariffLevel2, hwVsmTrafficPolicyName=hwVsmTrafficPolicyName, hwVsmServicePolicyTable=hwVsmServicePolicyTable, hwVsmSetTariffLevel3=hwVsmSetTariffLevel3, hwVsmSetTariffLevel5=hwVsmSetTariffLevel5, hwVsmAcctServicePolicyEnable=hwVsmAcctServicePolicyEnable, hwVsmServiceIdleCutTime=hwVsmServiceIdleCutTime, hwVsmServiceSource=hwVsmServiceSource, hwVsmTariffLevel4AcctSwitch=hwVsmTariffLevel4AcctSwitch, hwVsmTariffLevel8AcctSwitch=hwVsmTariffLevel8AcctSwitch, hwVsmDaaPolicyFlag=hwVsmDaaPolicyFlag, hwVsmServicePolicyObjectGroup=hwVsmServicePolicyObjectGroup, hwVsmDownByteNum=hwVsmDownByteNum, hwVsmObjectGroups=hwVsmObjectGroups, hwBRASVsm=hwBRASVsm, hwVsmSetFlowQryTLenObjectGroup=hwVsmSetFlowQryTLenObjectGroup)