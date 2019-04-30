#
# PySNMP MIB module HUAWEI-MPLSOAM-PS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-MPLSOAM-PS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:35:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
hwMpls, = mibBuilder.importSymbols("HUAWEI-MIB", "hwMpls")
hwMplsTunnelSignalProto, = mibBuilder.importSymbols("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, Gauge32, iso, IpAddress, Unsigned32, Bits, MibIdentifier, NotificationType, Integer32, Counter32, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "iso", "IpAddress", "Unsigned32", "Bits", "MibIdentifier", "NotificationType", "Integer32", "Counter32", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "TruthValue")
hwMplsOam = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7))
if mibBuilder.loadTexts: hwMplsOam.setLastUpdated('200504271724Z')
if mibBuilder.loadTexts: hwMplsOam.setOrganization('Huawei Technologies Co., Ltd.')
hwMplsOamPs = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1))
hwMplsPsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3))
hwMplsPsTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1), )
if mibBuilder.loadTexts: hwMplsPsTable.setStatus('current')
hwMplsPsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1), ).setIndexNames((0, "HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsIndex"))
if mibBuilder.loadTexts: hwMplsPsEntry.setStatus('current')
hwMplsPsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsIndex.setStatus('current')
hwMplsPsType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsType.setStatus('current')
hwMplsPsWorkTunnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsWorkTunnName.setStatus('current')
hwMplsPsWorkTunnId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsWorkTunnId.setStatus('current')
hwMplsPsProtectTunnName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsProtectTunnName.setStatus('current')
hwMplsPsProtectTunnId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsProtectTunnId.setStatus('current')
hwMplsPsRevertiveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsRevertiveMode.setStatus('current')
hwMplsPsWTR = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsWTR.setStatus('current')
hwMplsPsHoldOff = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsHoldOff.setStatus('current')
hwMplsPsSwitchCondition = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsSwitchCondition.setStatus('current')
hwMplsPsWorkTunnelState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsWorkTunnelState.setStatus('current')
hwMplsPsProtTunnelState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsProtTunnelState.setStatus('current')
hwMplsPsSwitchResult = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsSwitchResult.setStatus('current')
hwMplsPsCfgType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsCfgType.setStatus('current')
hwMplsPsCfgProtectTunnId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsCfgProtectTunnId.setStatus('current')
hwMplsPsCfgRevertiveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsCfgRevertiveMode.setStatus('current')
hwMplsPsCfgWTR = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsCfgWTR.setStatus('current')
hwMplsPsCfgHoldOff = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsCfgHoldOff.setStatus('current')
hwMplsPsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 19), RowStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsPsRowStatus.setStatus('current')
hwTunnPsTrapOpen = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTunnPsTrapOpen.setStatus('current')
hwMplsVCPsTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3), )
if mibBuilder.loadTexts: hwMplsVCPsTable.setStatus('current')
hwMplsApsMismatchReason = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("bridge", 1), ("channel", 2), ("switching", 3), ("operation", 4), ("traffic", 5)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hwMplsApsMismatchReason.setStatus('current')
hwMplsVCPsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1), ).setIndexNames((0, "HUAWEI-MPLSOAM-PS-MIB", "hwMplsVCPsIfIndex"))
if mibBuilder.loadTexts: hwMplsVCPsEntry.setStatus('current')
hwMplsVCPsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwMplsVCPsIfIndex.setStatus('current')
hwMplsVCPsTNLBinding = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1, 2), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMplsVCPsTNLBinding.setStatus('current')
hwMplsTeReverseLspName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1, 3), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMplsTeReverseLspName.setStatus('current')
hwMplsVcPsRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMplsVcPsRowStatus.setStatus('current')
hwMplsTeReverseLspLsrId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMplsTeReverseLspLsrId.setStatus('current')
hwMplsTeReverseLspTunnId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwMplsTeReverseLspTunnId.setStatus('current')
hwMplsPsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4))
hwMplsPsSwitchPtoW = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4, 1)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnId"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtectTunnName"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtectTunnId"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsSwitchResult"))
if mibBuilder.loadTexts: hwMplsPsSwitchPtoW.setStatus('current')
hwMplsPsSwitchWtoP = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4, 2)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnId"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtectTunnName"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtectTunnId"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsSwitchResult"))
if mibBuilder.loadTexts: hwMplsPsSwitchWtoP.setStatus('current')
hwMplsApsMismatch = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4, 3)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsApsMismatchReason"))
if mibBuilder.loadTexts: hwMplsApsMismatch.setStatus('current')
hwMplsApsMismatchRecovery = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4, 4)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsApsMismatchReason"))
if mibBuilder.loadTexts: hwMplsApsMismatchRecovery.setStatus('current')
hwMplsApsLost = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4, 5)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"), ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
if mibBuilder.loadTexts: hwMplsApsLost.setStatus('current')
hwMplsApsLostRecovery = NotificationType((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4, 6)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"), ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
if mibBuilder.loadTexts: hwMplsApsLostRecovery.setStatus('current')
hwMplsOamPsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100))
hwMplsOamPsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100, 1))
hwMplsOamPsGroupCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100, 1, 1)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsGroup"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsVcPsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMplsOamPsGroupCompliance = hwMplsOamPsGroupCompliance.setStatus('current')
hwMplsOamPsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100, 2))
hwMplsPsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100, 2, 1)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsType"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnId"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtectTunnName"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtectTunnId"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsRevertiveMode"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWTR"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsHoldOff"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsSwitchCondition"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnelState"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtTunnelState"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsSwitchResult"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsCfgType"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsCfgProtectTunnId"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsCfgRevertiveMode"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsCfgWTR"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsCfgHoldOff"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsRowStatus"), ("HUAWEI-MPLSOAM-PS-MIB", "hwTunnPsTrapOpen"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsVCPsIfIndex"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMplsPsGroup = hwMplsPsGroup.setStatus('current')
hwMplsVcPsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100, 2, 2)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsVCPsTNLBinding"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsTeReverseLspName"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsVcPsRowStatus"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsTeReverseLspLsrId"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsTeReverseLspTunnId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMplsVcPsGroup = hwMplsVcPsGroup.setStatus('current')
hwMplsPsNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100, 2, 3)).setObjects(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsSwitchPtoW"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsSwitchWtoP"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsApsMismatch"), ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsApsMismatchRecovery"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwMplsPsNotificationGroup = hwMplsPsNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-MPLSOAM-PS-MIB", hwMplsTeReverseLspName=hwMplsTeReverseLspName, hwMplsVcPsGroup=hwMplsVcPsGroup, hwMplsPsSwitchPtoW=hwMplsPsSwitchPtoW, hwMplsPsObjects=hwMplsPsObjects, hwMplsPsTable=hwMplsPsTable, hwTunnPsTrapOpen=hwTunnPsTrapOpen, hwMplsPsEntry=hwMplsPsEntry, hwMplsOamPsGroupCompliance=hwMplsOamPsGroupCompliance, hwMplsVcPsRowStatus=hwMplsVcPsRowStatus, hwMplsOam=hwMplsOam, hwMplsOamPsConformance=hwMplsOamPsConformance, hwMplsPsWorkTunnelState=hwMplsPsWorkTunnelState, hwMplsPsCfgProtectTunnId=hwMplsPsCfgProtectTunnId, hwMplsOamPsCompliances=hwMplsOamPsCompliances, hwMplsVCPsIfIndex=hwMplsVCPsIfIndex, hwMplsPsProtectTunnId=hwMplsPsProtectTunnId, hwMplsPsHoldOff=hwMplsPsHoldOff, PYSNMP_MODULE_ID=hwMplsOam, hwMplsPsSwitchResult=hwMplsPsSwitchResult, hwMplsPsSwitchCondition=hwMplsPsSwitchCondition, hwMplsPsIndex=hwMplsPsIndex, hwMplsPsCfgHoldOff=hwMplsPsCfgHoldOff, hwMplsPsCfgRevertiveMode=hwMplsPsCfgRevertiveMode, hwMplsPsProtTunnelState=hwMplsPsProtTunnelState, hwMplsVCPsEntry=hwMplsVCPsEntry, hwMplsVCPsTable=hwMplsVCPsTable, hwMplsApsLost=hwMplsApsLost, hwMplsPsCfgType=hwMplsPsCfgType, hwMplsVCPsTNLBinding=hwMplsVCPsTNLBinding, hwMplsPsWTR=hwMplsPsWTR, hwMplsApsMismatchRecovery=hwMplsApsMismatchRecovery, hwMplsPsSwitchWtoP=hwMplsPsSwitchWtoP, hwMplsPsGroup=hwMplsPsGroup, hwMplsTeReverseLspTunnId=hwMplsTeReverseLspTunnId, hwMplsPsWorkTunnName=hwMplsPsWorkTunnName, hwMplsOamPs=hwMplsOamPs, hwMplsPsRevertiveMode=hwMplsPsRevertiveMode, hwMplsOamPsGroups=hwMplsOamPsGroups, hwMplsApsMismatchReason=hwMplsApsMismatchReason, hwMplsPsProtectTunnName=hwMplsPsProtectTunnName, hwMplsPsType=hwMplsPsType, hwMplsPsRowStatus=hwMplsPsRowStatus, hwMplsPsCfgWTR=hwMplsPsCfgWTR, hwMplsTeReverseLspLsrId=hwMplsTeReverseLspLsrId, hwMplsPsWorkTunnId=hwMplsPsWorkTunnId, hwMplsPsNotificationGroup=hwMplsPsNotificationGroup, hwMplsPsNotifications=hwMplsPsNotifications, hwMplsApsLostRecovery=hwMplsApsLostRecovery, hwMplsApsMismatch=hwMplsApsMismatch)