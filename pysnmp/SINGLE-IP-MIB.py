#
# PySNMP MIB module SINGLE-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SINGLE-IP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:56:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, NotificationType, Unsigned32, MibIdentifier, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, ObjectIdentity, Bits, Counter32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "NotificationType", "Unsigned32", "MibIdentifier", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "ObjectIdentity", "Bits", "Counter32", "TimeTicks")
TextualConvention, MacAddress, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "RowStatus", "DisplayString")
swSingleIPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 8))
if mibBuilder.loadTexts: swSingleIPMIB.setLastUpdated('9911220000Z')
if mibBuilder.loadTexts: swSingleIPMIB.setOrganization(' ')
swSingleIPMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 8, 1))
swSingleIPInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 1))
swSingleIPCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 2))
swSingleIPVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPVersion.setStatus('current')
swSingleIPCapability = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPCapability.setStatus('current')
swSingleIPPlatform = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPPlatform.setStatus('current')
swSingleIPAdmin = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSingleIPAdmin.setStatus('current')
swSingleIPRoleState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("cs", 1), ("cas", 2), ("ms", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSingleIPRoleState.setStatus('current')
swSingleIPHoldtime = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 255)).clone(100)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSingleIPHoldtime.setStatus('current')
swSingleIPTimeInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 90)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSingleIPTimeInterval.setStatus('current')
swSingleIPMSTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3), )
if mibBuilder.loadTexts: swSingleIPMSTable.setStatus('current')
swSingleIPMSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1), ).setIndexNames((0, "SINGLE-IP-MIB", "swSingleIPMSID"))
if mibBuilder.loadTexts: swSingleIPMSEntry.setStatus('current')
swSingleIPMSID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPMSID.setStatus('current')
swSingleIPMSDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPMSDeviceName.setStatus('current')
swSingleIPMSMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPMSMacAddr.setStatus('current')
swSingleIPMSFirmwareVer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPMSFirmwareVer.setStatus('current')
swSingleIPMSCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPMSCapability.setStatus('current')
swSingleIPMSPlatform = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPMSPlatform.setStatus('current')
swSingleIPMSHoldtime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPMSHoldtime.setStatus('current')
swSingleIPMSCasSource = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 8), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swSingleIPMSCasSource.setStatus('current')
swSingleIPMSPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swSingleIPMSPassword.setStatus('current')
swSingleIPMSRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 3, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swSingleIPMSRowStatus.setStatus('current')
swSingleIPCaSTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 4), )
if mibBuilder.loadTexts: swSingleIPCaSTable.setStatus('current')
swSingleIPCaSEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 4, 1), ).setIndexNames((0, "SINGLE-IP-MIB", "swSingleIPCaSID"))
if mibBuilder.loadTexts: swSingleIPCaSEntry.setStatus('current')
swSingleIPCaSID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPCaSID.setStatus('current')
swSingleIPCaSDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPCaSDeviceName.setStatus('current')
swSingleIPCaSMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 4, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPCaSMacAddr.setStatus('current')
swSingleIPCaSFirmwareVer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPCaSFirmwareVer.setStatus('current')
swSingleIPCaSCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 4, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPCaSCapability.setStatus('current')
swSingleIPCaSPlatform = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPCaSPlatform.setStatus('current')
swSingleIPCaSHoldtime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPCaSHoldtime.setStatus('current')
swSingleIPGroupTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5), )
if mibBuilder.loadTexts: swSingleIPGroupTable.setStatus('current')
swSingleIPGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5, 1), ).setIndexNames((0, "SINGLE-IP-MIB", "swSingleIPGroupMacAddr"))
if mibBuilder.loadTexts: swSingleIPGroupEntry.setStatus('current')
swSingleIPGroupMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPGroupMacAddr.setStatus('current')
swSingleIPGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPGroupName.setStatus('current')
swSingleIPGroupDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPGroupDeviceName.setStatus('current')
swSingleIPGroupMSNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPGroupMSNumber.setStatus('current')
swSingleIPGroupFirmwareVer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPGroupFirmwareVer.setStatus('current')
swSingleIPGroupCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPGroupCapability.setStatus('current')
swSingleIPGroupPlatform = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPGroupPlatform.setStatus('current')
swSingleIPGroupHoldtime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 5, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPGroupHoldtime.setStatus('current')
swSingleIPNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 6), )
if mibBuilder.loadTexts: swSingleIPNeighborTable.setStatus('current')
swSingleIPNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 6, 1), ).setIndexNames((0, "SINGLE-IP-MIB", "swSingleIPNBReceivedPort"), (0, "SINGLE-IP-MIB", "swSingleIPNBMacAddr"))
if mibBuilder.loadTexts: swSingleIPNeighborEntry.setStatus('current')
swSingleIPNBReceivedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPNBReceivedPort.setStatus('current')
swSingleIPNBMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 6, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPNBMacAddr.setStatus('current')
swSingleIPNBRoleState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 8, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("commander", 1), ("candidate", 2), ("member", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPNBRoleState.setStatus('current')
singleIPMSNotify = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 8, 6))
singleIPMSNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0))
swSingleIPMSColdStart = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 11)).setObjects(("SINGLE-IP-MIB", "swSingleIPMSID"), ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"))
if mibBuilder.loadTexts: swSingleIPMSColdStart.setStatus('current')
swSingleIPMSWarmStart = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 12)).setObjects(("SINGLE-IP-MIB", "swSingleIPMSID"), ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"))
if mibBuilder.loadTexts: swSingleIPMSWarmStart.setStatus('current')
swSingleIPMSLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 13)).setObjects(("SINGLE-IP-MIB", "swSingleIPMSID"), ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: swSingleIPMSLinkDown.setStatus('current')
swSingleIPMSLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 14)).setObjects(("SINGLE-IP-MIB", "swSingleIPMSID"), ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: swSingleIPMSLinkUp.setStatus('current')
swSingleIPMSAuthFail = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 15)).setObjects(("SINGLE-IP-MIB", "swSingleIPMSID"), ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"))
if mibBuilder.loadTexts: swSingleIPMSAuthFail.setStatus('current')
swSingleIPMSnewRoot = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 16)).setObjects(("SINGLE-IP-MIB", "swSingleIPMSID"), ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"))
if mibBuilder.loadTexts: swSingleIPMSnewRoot.setStatus('current')
swSingleIPMSTopologyChange = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 17)).setObjects(("SINGLE-IP-MIB", "swSingleIPMSID"), ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"))
if mibBuilder.loadTexts: swSingleIPMSTopologyChange.setStatus('current')
swSingleIPMSrisingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 18)).setObjects(("SINGLE-IP-MIB", "swSingleIPMSID"), ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"))
if mibBuilder.loadTexts: swSingleIPMSrisingAlarm.setStatus('current')
swSingleIPMSfallingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 19)).setObjects(("SINGLE-IP-MIB", "swSingleIPMSID"), ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"))
if mibBuilder.loadTexts: swSingleIPMSfallingAlarm.setStatus('current')
swSingleIPMSmacNotification = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 20)).setObjects(("SINGLE-IP-MIB", "swSingleIPMSID"), ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"), ("SINGLE-IP-MIB", "swSingleIPMSTrapMessage"))
if mibBuilder.loadTexts: swSingleIPMSmacNotification.setStatus('current')
swSingleIPMSPortTypeChange = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 21)).setObjects(("SINGLE-IP-MIB", "swSingleIPMSID"), ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"), ("IF-MIB", "ifIndex"), ("SINGLE-IP-MIB", "swSingleIPMSTrapMessage"))
if mibBuilder.loadTexts: swSingleIPMSPortTypeChange.setStatus('current')
swSingleIPMSPowerStatusChg = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 22)).setObjects(("SINGLE-IP-MIB", "swSingleIPMSID"), ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"), ("SINGLE-IP-MIB", "swSingleIPMSTrapMessage"))
if mibBuilder.loadTexts: swSingleIPMSPowerStatusChg.setStatus('current')
swSingleIPMSPowerFailure = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 23)).setObjects(("SINGLE-IP-MIB", "swSingleIPMSID"), ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"), ("SINGLE-IP-MIB", "swSingleIPMSTrapMessage"))
if mibBuilder.loadTexts: swSingleIPMSPowerFailure.setStatus('current')
swSingleIPMSPowerRecover = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 0, 24)).setObjects(("SINGLE-IP-MIB", "swSingleIPMSID"), ("SINGLE-IP-MIB", "swSingleIPMSMacAddr"), ("SINGLE-IP-MIB", "swSingleIPMSTrapMessage"))
if mibBuilder.loadTexts: swSingleIPMSPowerRecover.setStatus('current')
singleIPNotifyBidings = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 1))
swSingleIPMSTrapMessage = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 8, 6, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSingleIPMSTrapMessage.setStatus('current')
mibBuilder.exportSymbols("SINGLE-IP-MIB", swSingleIPNBMacAddr=swSingleIPNBMacAddr, swSingleIPMSWarmStart=swSingleIPMSWarmStart, swSingleIPMSLinkUp=swSingleIPMSLinkUp, swSingleIPMSCasSource=swSingleIPMSCasSource, swSingleIPMSPassword=swSingleIPMSPassword, swSingleIPMSnewRoot=swSingleIPMSnewRoot, swSingleIPTimeInterval=swSingleIPTimeInterval, swSingleIPMSAuthFail=swSingleIPMSAuthFail, swSingleIPAdmin=swSingleIPAdmin, swSingleIPRoleState=swSingleIPRoleState, swSingleIPNBRoleState=swSingleIPNBRoleState, swSingleIPNeighborTable=swSingleIPNeighborTable, swSingleIPGroupHoldtime=swSingleIPGroupHoldtime, swSingleIPMSPowerStatusChg=swSingleIPMSPowerStatusChg, swSingleIPCaSHoldtime=swSingleIPCaSHoldtime, swSingleIPGroupCapability=swSingleIPGroupCapability, swSingleIPGroupPlatform=swSingleIPGroupPlatform, swSingleIPNeighborEntry=swSingleIPNeighborEntry, swSingleIPNBReceivedPort=swSingleIPNBReceivedPort, swSingleIPMSrisingAlarm=swSingleIPMSrisingAlarm, swSingleIPCaSEntry=swSingleIPCaSEntry, PYSNMP_MODULE_ID=swSingleIPMIB, swSingleIPMSPortTypeChange=swSingleIPMSPortTypeChange, swSingleIPMSID=swSingleIPMSID, swSingleIPInfo=swSingleIPInfo, swSingleIPHoldtime=swSingleIPHoldtime, swSingleIPCaSFirmwareVer=swSingleIPCaSFirmwareVer, swSingleIPGroupEntry=swSingleIPGroupEntry, swSingleIPMgmt=swSingleIPMgmt, swSingleIPMSEntry=swSingleIPMSEntry, swSingleIPCaSDeviceName=swSingleIPCaSDeviceName, swSingleIPMSMacAddr=swSingleIPMSMacAddr, swSingleIPMSTopologyChange=swSingleIPMSTopologyChange, swSingleIPMSPowerFailure=swSingleIPMSPowerFailure, swSingleIPMSTrapMessage=swSingleIPMSTrapMessage, swSingleIPMSPlatform=swSingleIPMSPlatform, swSingleIPMSLinkDown=swSingleIPMSLinkDown, singleIPMSNotify=singleIPMSNotify, swSingleIPCaSID=swSingleIPCaSID, swSingleIPCaSPlatform=swSingleIPCaSPlatform, swSingleIPMSDeviceName=swSingleIPMSDeviceName, swSingleIPGroupTable=swSingleIPGroupTable, swSingleIPGroupMacAddr=swSingleIPGroupMacAddr, swSingleIPCapability=swSingleIPCapability, swSingleIPCaSMacAddr=swSingleIPCaSMacAddr, swSingleIPMSColdStart=swSingleIPMSColdStart, swSingleIPGroupName=swSingleIPGroupName, swSingleIPMSHoldtime=swSingleIPMSHoldtime, swSingleIPGroupDeviceName=swSingleIPGroupDeviceName, swSingleIPMSfallingAlarm=swSingleIPMSfallingAlarm, swSingleIPMSmacNotification=swSingleIPMSmacNotification, swSingleIPGroupFirmwareVer=swSingleIPGroupFirmwareVer, swSingleIPVersion=swSingleIPVersion, swSingleIPMSCapability=swSingleIPMSCapability, swSingleIPPlatform=swSingleIPPlatform, swSingleIPMSTable=swSingleIPMSTable, swSingleIPMSFirmwareVer=swSingleIPMSFirmwareVer, swSingleIPMSRowStatus=swSingleIPMSRowStatus, singleIPNotifyBidings=singleIPNotifyBidings, swSingleIPCtrl=swSingleIPCtrl, swSingleIPGroupMSNumber=swSingleIPGroupMSNumber, swSingleIPMSPowerRecover=swSingleIPMSPowerRecover, swSingleIPCaSTable=swSingleIPCaSTable, singleIPMSNotifyPrefix=singleIPMSNotifyPrefix, swSingleIPMIB=swSingleIPMIB, swSingleIPCaSCapability=swSingleIPCaSCapability)