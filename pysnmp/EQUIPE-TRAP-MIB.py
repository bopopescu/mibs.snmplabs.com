#
# PySNMP MIB module EQUIPE-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EQUIPE-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:51:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
EqSeverityLevel, eqModuleSlotId, eqModuleEid, EqApsLineState, eqHardDiskUsedLowMark, eqFaultTime, eqFaultScope, eqHardDiskUsedHiMark, eqFaultSwlm, eqModuleRedOperRole, EqIfType, eqModuleShelfId, eqFanUnitEid, eqStratumCentStatus, EqAtmPvcType, eqFaultModule, eqStratumCentRedStatus, eqHardDiskEid = mibBuilder.importSymbols("EQUIPE-SYSTEM-MIB", "EqSeverityLevel", "eqModuleSlotId", "eqModuleEid", "EqApsLineState", "eqHardDiskUsedLowMark", "eqFaultTime", "eqFaultScope", "eqHardDiskUsedHiMark", "eqFaultSwlm", "eqModuleRedOperRole", "EqIfType", "eqModuleShelfId", "eqFanUnitEid", "eqStratumCentStatus", "EqAtmPvcType", "eqFaultModule", "eqStratumCentRedStatus", "eqHardDiskEid")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, Counter64, ObjectIdentity, Unsigned32, Integer32, MibIdentifier, Gauge32, enterprises, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Counter64", "ObjectIdentity", "Unsigned32", "Integer32", "MibIdentifier", "Gauge32", "enterprises", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "ModuleIdentity", "Bits")
TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime")
equipe = MibIdentifier((1, 3, 6, 1, 4, 1, 5022))
eqTraps = ModuleIdentity((1, 3, 6, 1, 4, 1, 5022, 4))
if mibBuilder.loadTexts: eqTraps.setLastUpdated('0112040000Z')
if mibBuilder.loadTexts: eqTraps.setOrganization('')
eqTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5022, 4, 1))
eqSystemTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5022, 4, 2))
eqModuleTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5022, 4, 3))
eqIfTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5022, 4, 4))
eqAppsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5022, 4, 5))
eqSrmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5022, 4, 5, 1))
eqSonetTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5022, 4, 5, 2))
eqAtmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5022, 4, 5, 3))
eqIpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5022, 4, 5, 4))
eqMplsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5022, 4, 5, 5))
eqSystemId = MibScalar((1, 3, 6, 1, 4, 1, 5022, 4, 1, 1), DisplayString())
if mibBuilder.loadTexts: eqSystemId.setStatus('current')
eqEid = MibScalar((1, 3, 6, 1, 4, 1, 5022, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: eqEid.setStatus('current')
eqIfName = MibScalar((1, 3, 6, 1, 4, 1, 5022, 4, 1, 3), DisplayString())
if mibBuilder.loadTexts: eqIfName.setStatus('current')
eqIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 5022, 4, 1, 4), IpAddress())
if mibBuilder.loadTexts: eqIpAddress.setStatus('current')
eqFileName = MibScalar((1, 3, 6, 1, 4, 1, 5022, 4, 1, 5), DisplayString())
if mibBuilder.loadTexts: eqFileName.setStatus('current')
eqTrapDescr = MibScalar((1, 3, 6, 1, 4, 1, 5022, 4, 1, 6), DisplayString())
if mibBuilder.loadTexts: eqTrapDescr.setStatus('current')
eqModuleFuseType = MibScalar((1, 3, 6, 1, 4, 1, 5022, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("fuseTypeA", 1), ("fuseTypeB", 2))))
if mibBuilder.loadTexts: eqModuleFuseType.setStatus('current')
eqApsLineState = MibScalar((1, 3, 6, 1, 4, 1, 5022, 4, 1, 8), EqApsLineState())
if mibBuilder.loadTexts: eqApsLineState.setStatus('current')
eqIfType = MibScalar((1, 3, 6, 1, 4, 1, 5022, 4, 1, 9), EqIfType())
if mibBuilder.loadTexts: eqIfType.setStatus('current')
eqAtmPvcType = MibScalar((1, 3, 6, 1, 4, 1, 5022, 4, 1, 10), EqAtmPvcType())
if mibBuilder.loadTexts: eqAtmPvcType.setStatus('current')
eqEventTime = MibScalar((1, 3, 6, 1, 4, 1, 5022, 4, 1, 11), DateAndTime())
if mibBuilder.loadTexts: eqEventTime.setStatus('current')
eqThresholdValue = MibScalar((1, 3, 6, 1, 4, 1, 5022, 4, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: eqThresholdValue.setStatus('current')
eqCurrentValue = MibScalar((1, 3, 6, 1, 4, 1, 5022, 4, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: eqCurrentValue.setStatus('current')
eqResourceId = MibScalar((1, 3, 6, 1, 4, 1, 5022, 4, 1, 14), DisplayString())
if mibBuilder.loadTexts: eqResourceId.setStatus('current')
eqSeverityLevel = MibScalar((1, 3, 6, 1, 4, 1, 5022, 4, 1, 15), EqSeverityLevel())
if mibBuilder.loadTexts: eqSeverityLevel.setStatus('current')
eqHardDiskUsedHiMarkReached = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 2, 1)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-SYSTEM-MIB", "eqHardDiskEid"), ("EQUIPE-SYSTEM-MIB", "eqHardDiskUsedHiMark"))
if mibBuilder.loadTexts: eqHardDiskUsedHiMarkReached.setStatus('current')
eqHardDiskUsedLowMarkReached = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 2, 2)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-SYSTEM-MIB", "eqHardDiskEid"), ("EQUIPE-SYSTEM-MIB", "eqHardDiskUsedLowMark"))
if mibBuilder.loadTexts: eqHardDiskUsedLowMarkReached.setStatus('current')
eqFanUnitFailed = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 2, 3)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-SYSTEM-MIB", "eqFanUnitEid"))
if mibBuilder.loadTexts: eqFanUnitFailed.setStatus('current')
eqFanUnitFaulty = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 2, 4)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-SYSTEM-MIB", "eqFanUnitEid"))
if mibBuilder.loadTexts: eqFanUnitFaulty.setStatus('current')
eqAcctDataWriteToDiskFailed = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 2, 5)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"))
if mibBuilder.loadTexts: eqAcctDataWriteToDiskFailed.setStatus('current')
eqAcctDataFileDeletedBeforeTransfer = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 2, 6)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-TRAP-MIB", "eqFileName"), ("EQUIPE-TRAP-MIB", "eqSystemId"))
if mibBuilder.loadTexts: eqAcctDataFileDeletedBeforeTransfer.setStatus('current')
eqAcctDataXferError = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 2, 7)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-TRAP-MIB", "eqIpAddress"), ("EQUIPE-TRAP-MIB", "eqFileName"), ("EQUIPE-TRAP-MIB", "eqSystemId"))
if mibBuilder.loadTexts: eqAcctDataXferError.setStatus('current')
eqLogServerWriteToDiskFailed = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 2, 8)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"))
if mibBuilder.loadTexts: eqLogServerWriteToDiskFailed.setStatus('current')
eqLogDataFileDeletedBeforeTransfer = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 2, 9)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-TRAP-MIB", "eqFileName"), ("EQUIPE-TRAP-MIB", "eqSystemId"))
if mibBuilder.loadTexts: eqLogDataFileDeletedBeforeTransfer.setStatus('current')
eqLogDataXferError = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 2, 10)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-TRAP-MIB", "eqIpAddress"), ("EQUIPE-TRAP-MIB", "eqFileName"), ("EQUIPE-TRAP-MIB", "eqSystemId"))
if mibBuilder.loadTexts: eqLogDataXferError.setStatus('current')
eqMidPlaneParityError = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 2, 11)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"))
if mibBuilder.loadTexts: eqMidPlaneParityError.setStatus('current')
eqSonetTimingCfgChanged = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 2, 12)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-TRAP-MIB", "eqEid"))
if mibBuilder.loadTexts: eqSonetTimingCfgChanged.setStatus('current')
eqRisingThresholdAlert = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 2, 13)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-TRAP-MIB", "eqEid"), ("EQUIPE-TRAP-MIB", "eqIfName"), ("EQUIPE-TRAP-MIB", "eqEventTime"), ("EQUIPE-TRAP-MIB", "eqThresholdValue"), ("EQUIPE-TRAP-MIB", "eqCurrentValue"), ("EQUIPE-TRAP-MIB", "eqResourceId"), ("EQUIPE-TRAP-MIB", "eqSeverityLevel"))
if mibBuilder.loadTexts: eqRisingThresholdAlert.setStatus('current')
eqFallingThresholdAlert = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 2, 14)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-TRAP-MIB", "eqEid"), ("EQUIPE-TRAP-MIB", "eqIfName"), ("EQUIPE-TRAP-MIB", "eqEventTime"), ("EQUIPE-TRAP-MIB", "eqThresholdValue"), ("EQUIPE-TRAP-MIB", "eqCurrentValue"), ("EQUIPE-TRAP-MIB", "eqResourceId"), ("EQUIPE-TRAP-MIB", "eqSeverityLevel"))
if mibBuilder.loadTexts: eqFallingThresholdAlert.setStatus('current')
eqModuleInserted = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 3, 1)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-SYSTEM-MIB", "eqModuleEid"))
if mibBuilder.loadTexts: eqModuleInserted.setStatus('current')
eqModuleRemoved = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 3, 2)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-SYSTEM-MIB", "eqModuleEid"))
if mibBuilder.loadTexts: eqModuleRemoved.setStatus('current')
eqModuleWentOffline = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 3, 3)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-SYSTEM-MIB", "eqModuleEid"))
if mibBuilder.loadTexts: eqModuleWentOffline.setStatus('current')
eqModuleReset = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 3, 4)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-SYSTEM-MIB", "eqModuleEid"))
if mibBuilder.loadTexts: eqModuleReset.setStatus('current')
eqModuleFuseBlownMother = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 3, 5)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-SYSTEM-MIB", "eqModuleEid"), ("EQUIPE-TRAP-MIB", "eqModuleFuseType"))
if mibBuilder.loadTexts: eqModuleFuseBlownMother.setStatus('current')
eqModuleFuseBlownDaughter = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 3, 6)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-SYSTEM-MIB", "eqModuleEid"), ("EQUIPE-TRAP-MIB", "eqModuleFuseType"))
if mibBuilder.loadTexts: eqModuleFuseBlownDaughter.setStatus('current')
eqModulePowerSupplyFailed = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 3, 7)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-SYSTEM-MIB", "eqModuleEid"))
if mibBuilder.loadTexts: eqModulePowerSupplyFailed.setStatus('current')
eqModuleRedRoleChanged = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 3, 8)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleEid"), ("EQUIPE-SYSTEM-MIB", "eqModuleRedOperRole"))
if mibBuilder.loadTexts: eqModuleRedRoleChanged.setStatus('current')
eqModuleTypeMismatch = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 3, 9)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-SYSTEM-MIB", "eqModuleEid"))
if mibBuilder.loadTexts: eqModuleTypeMismatch.setStatus('current')
eqModuleStratumCentStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 3, 10)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-SYSTEM-MIB", "eqModuleEid"), ("EQUIPE-SYSTEM-MIB", "eqStratumCentStatus"))
if mibBuilder.loadTexts: eqModuleStratumCentStatusChanged.setStatus('current')
eqModuleStratumCentRedStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 3, 11)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-SYSTEM-MIB", "eqModuleEid"), ("EQUIPE-SYSTEM-MIB", "eqStratumCentRedStatus"))
if mibBuilder.loadTexts: eqModuleStratumCentRedStatusChanged.setStatus('current')
eqIfAdded = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 4, 1)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("IF-MIB", "ifIndex"), ("EQUIPE-TRAP-MIB", "eqIfName"), ("EQUIPE-TRAP-MIB", "eqIfType"))
if mibBuilder.loadTexts: eqIfAdded.setStatus('current')
eqIfRemoved = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 4, 2)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("IF-MIB", "ifIndex"), ("EQUIPE-TRAP-MIB", "eqIfName"), ("EQUIPE-TRAP-MIB", "eqIfType"))
if mibBuilder.loadTexts: eqIfRemoved.setStatus('current')
eqIfModified = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 4, 3)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("IF-MIB", "ifIndex"), ("EQUIPE-TRAP-MIB", "eqIfName"), ("EQUIPE-TRAP-MIB", "eqIfType"))
if mibBuilder.loadTexts: eqIfModified.setStatus('current')
eqAtmPvcAdded = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 4, 4)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-TRAP-MIB", "eqEid"), ("EQUIPE-TRAP-MIB", "eqIfName"), ("EQUIPE-TRAP-MIB", "eqAtmPvcType"))
if mibBuilder.loadTexts: eqAtmPvcAdded.setStatus('current')
eqAtmPvcRemoved = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 4, 5)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-TRAP-MIB", "eqEid"), ("EQUIPE-TRAP-MIB", "eqIfName"), ("EQUIPE-TRAP-MIB", "eqAtmPvcType"))
if mibBuilder.loadTexts: eqAtmPvcRemoved.setStatus('current')
eqAtmPvcModified = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 4, 6)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("EQUIPE-TRAP-MIB", "eqEid"), ("EQUIPE-TRAP-MIB", "eqIfName"), ("EQUIPE-TRAP-MIB", "eqAtmPvcType"))
if mibBuilder.loadTexts: eqAtmPvcModified.setStatus('current')
eqSonetApsSwitchEvent = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 5, 2, 1)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("IF-MIB", "ifIndex"), ("EQUIPE-TRAP-MIB", "eqIfName"), ("EQUIPE-TRAP-MIB", "eqApsLineState"))
if mibBuilder.loadTexts: eqSonetApsSwitchEvent.setStatus('current')
eqSonetApsWorkingLineRestored = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 5, 2, 2)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("IF-MIB", "ifIndex"), ("EQUIPE-TRAP-MIB", "eqIfName"))
if mibBuilder.loadTexts: eqSonetApsWorkingLineRestored.setStatus('current')
eqSonetApsModeMismatch = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 5, 2, 3)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("IF-MIB", "ifIndex"), ("EQUIPE-TRAP-MIB", "eqIfName"))
if mibBuilder.loadTexts: eqSonetApsModeMismatch.setStatus('current')
eqSonetApsProtectLineFailure = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 5, 2, 4)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("IF-MIB", "ifIndex"), ("EQUIPE-TRAP-MIB", "eqIfName"))
if mibBuilder.loadTexts: eqSonetApsProtectLineFailure.setStatus('current')
eqSonetApsProtectLineRestored = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 5, 2, 5)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("IF-MIB", "ifIndex"), ("EQUIPE-TRAP-MIB", "eqIfName"))
if mibBuilder.loadTexts: eqSonetApsProtectLineRestored.setStatus('current')
eqSonetApsProtectByteFailure = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 5, 2, 6)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("IF-MIB", "ifIndex"), ("EQUIPE-TRAP-MIB", "eqIfName"))
if mibBuilder.loadTexts: eqSonetApsProtectByteFailure.setStatus('current')
eqSonetApsFarEndProtectLineFailure = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 5, 2, 7)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("IF-MIB", "ifIndex"), ("EQUIPE-TRAP-MIB", "eqIfName"))
if mibBuilder.loadTexts: eqSonetApsFarEndProtectLineFailure.setStatus('current')
eqSonetApsFarEndProtectLineCleared = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 5, 2, 8)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqModuleShelfId"), ("EQUIPE-SYSTEM-MIB", "eqModuleSlotId"), ("IF-MIB", "ifIndex"), ("EQUIPE-TRAP-MIB", "eqIfName"))
if mibBuilder.loadTexts: eqSonetApsFarEndProtectLineCleared.setStatus('current')
eqSrmFault = NotificationType((1, 3, 6, 1, 4, 1, 5022, 4, 5, 1, 1)).setObjects(("EQUIPE-TRAP-MIB", "eqTrapDescr"), ("EQUIPE-SYSTEM-MIB", "eqFaultTime"), ("EQUIPE-SYSTEM-MIB", "eqFaultScope"), ("EQUIPE-SYSTEM-MIB", "eqFaultModule"), ("EQUIPE-SYSTEM-MIB", "eqFaultSwlm"))
if mibBuilder.loadTexts: eqSrmFault.setStatus('current')
mibBuilder.exportSymbols("EQUIPE-TRAP-MIB", eqAcctDataXferError=eqAcctDataXferError, eqModulePowerSupplyFailed=eqModulePowerSupplyFailed, eqAtmPvcModified=eqAtmPvcModified, eqSonetApsFarEndProtectLineFailure=eqSonetApsFarEndProtectLineFailure, eqTrapObjects=eqTrapObjects, eqLogDataFileDeletedBeforeTransfer=eqLogDataFileDeletedBeforeTransfer, eqModuleTraps=eqModuleTraps, eqFanUnitFailed=eqFanUnitFailed, eqHardDiskUsedHiMarkReached=eqHardDiskUsedHiMarkReached, eqSonetTimingCfgChanged=eqSonetTimingCfgChanged, eqModuleRedRoleChanged=eqModuleRedRoleChanged, eqModuleStratumCentStatusChanged=eqModuleStratumCentStatusChanged, eqRisingThresholdAlert=eqRisingThresholdAlert, equipe=equipe, eqMplsTraps=eqMplsTraps, eqAcctDataWriteToDiskFailed=eqAcctDataWriteToDiskFailed, eqSonetApsModeMismatch=eqSonetApsModeMismatch, eqModuleStratumCentRedStatusChanged=eqModuleStratumCentRedStatusChanged, eqLogDataXferError=eqLogDataXferError, eqSonetApsWorkingLineRestored=eqSonetApsWorkingLineRestored, eqIpTraps=eqIpTraps, eqIpAddress=eqIpAddress, eqAtmPvcAdded=eqAtmPvcAdded, eqSonetApsProtectLineFailure=eqSonetApsProtectLineFailure, eqSeverityLevel=eqSeverityLevel, eqSystemTraps=eqSystemTraps, eqSonetTraps=eqSonetTraps, eqModuleTypeMismatch=eqModuleTypeMismatch, eqModuleRemoved=eqModuleRemoved, eqEventTime=eqEventTime, eqApsLineState=eqApsLineState, eqAcctDataFileDeletedBeforeTransfer=eqAcctDataFileDeletedBeforeTransfer, eqTraps=eqTraps, eqIfName=eqIfName, eqTrapDescr=eqTrapDescr, eqSystemId=eqSystemId, eqIfTraps=eqIfTraps, eqModuleFuseType=eqModuleFuseType, eqModuleInserted=eqModuleInserted, eqAtmPvcType=eqAtmPvcType, eqModuleReset=eqModuleReset, eqModuleFuseBlownMother=eqModuleFuseBlownMother, PYSNMP_MODULE_ID=eqTraps, eqModuleWentOffline=eqModuleWentOffline, eqModuleFuseBlownDaughter=eqModuleFuseBlownDaughter, eqFanUnitFaulty=eqFanUnitFaulty, eqSonetApsSwitchEvent=eqSonetApsSwitchEvent, eqSonetApsProtectLineRestored=eqSonetApsProtectLineRestored, eqSrmFault=eqSrmFault, eqCurrentValue=eqCurrentValue, eqLogServerWriteToDiskFailed=eqLogServerWriteToDiskFailed, eqIfType=eqIfType, eqSonetApsProtectByteFailure=eqSonetApsProtectByteFailure, eqMidPlaneParityError=eqMidPlaneParityError, eqAtmTraps=eqAtmTraps, eqHardDiskUsedLowMarkReached=eqHardDiskUsedLowMarkReached, eqIfRemoved=eqIfRemoved, eqIfAdded=eqIfAdded, eqFileName=eqFileName, eqSrmTraps=eqSrmTraps, eqResourceId=eqResourceId, eqAppsTraps=eqAppsTraps, eqEid=eqEid, eqAtmPvcRemoved=eqAtmPvcRemoved, eqSonetApsFarEndProtectLineCleared=eqSonetApsFarEndProtectLineCleared, eqIfModified=eqIfModified, eqThresholdValue=eqThresholdValue, eqFallingThresholdAlert=eqFallingThresholdAlert)