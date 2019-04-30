#
# PySNMP MIB module ENTERASYS-POWER-ETHERNET-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-POWER-ETHERNET-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:50:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
pethPsePortEntry, pethMainPseEntry = mibBuilder.importSymbols("POWER-ETHERNET-MIB", "pethPsePortEntry", "pethMainPseEntry")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, NotificationType, IpAddress, ModuleIdentity, ObjectIdentity, Counter64, Integer32, Counter32, iso, Bits, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "IpAddress", "ModuleIdentity", "ObjectIdentity", "Counter64", "Integer32", "Counter32", "iso", "Bits", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etsysPowerEthernetMibExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50))
etsysPowerEthernetMibExtMIB.setRevisions(('2009-08-27 20:31', '2005-01-10 16:30', '2004-08-17 22:27',))
if mibBuilder.loadTexts: etsysPowerEthernetMibExtMIB.setLastUpdated('200908272031Z')
if mibBuilder.loadTexts: etsysPowerEthernetMibExtMIB.setOrganization('Enterasys Networks, Inc')
etsysPowerEthernetObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1))
etsysPseChassisPowerAllocation = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 1))
etsysPseSlotPowerAllocation = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 2))
etsysPseChassisPowerStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3))
etsysPseSlotPowerManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 4))
etsysPsePortPowerManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5))
etsysPsePowerNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 0))
etsysPseChassisPowerAllocationMode = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("manual", 2))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysPseChassisPowerAllocationMode.setStatus('current')
etsysPseChassisPowerSnmpNotification = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 1, 2), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysPseChassisPowerSnmpNotification.setStatus('current')
etsysPseChassisPowerAvailableMaximum = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(100)).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysPseChassisPowerAvailableMaximum.setStatus('current')
etsysPseSlotPowerAllocationTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 2, 1), )
if mibBuilder.loadTexts: etsysPseSlotPowerAllocationTable.setStatus('current')
etsysPseSlotPowerAllocationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: etsysPseSlotPowerAllocationEntry.setStatus('current')
etsysPseSlotPowerMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 2, 1, 1, 1), Unsigned32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPseSlotPowerMaximum.setStatus('current')
etsysPseSlotPowerAssigned = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 2, 1, 1, 2), Unsigned32()).setUnits('Watts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysPseSlotPowerAssigned.setStatus('current')
etsysPseChassisPowerDetected = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 1), Gauge32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPseChassisPowerDetected.setStatus('current')
etsysPseChassisPowerAvailable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 2), Gauge32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPseChassisPowerAvailable.setStatus('current')
etsysPseChassisPowerConsumable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 3), Gauge32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPseChassisPowerConsumable.setStatus('current')
etsysPseChassisPowerAssigned = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 4), Unsigned32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPseChassisPowerAssigned.setStatus('current')
etsysPseChassisPowerRedundancy = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("redundant", 1), ("notRedundant", 2), ("notSupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPseChassisPowerRedundancy.setStatus('current')
etsysPseModulePowerManagementTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 4, 1), )
if mibBuilder.loadTexts: etsysPseModulePowerManagementTable.setStatus('current')
etsysPseModulePowerManagementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 4, 1, 1), )
pethMainPseEntry.registerAugmentions(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseModulePowerManagementEntry"))
etsysPseModulePowerManagementEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
if mibBuilder.loadTexts: etsysPseModulePowerManagementEntry.setStatus('current')
etsysPseModulePowerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("realtime", 1), ("class", 2))).clone('realtime')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysPseModulePowerMode.setStatus('current')
etsysPseModulePowerClassBudget = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 4, 1, 1, 2), Gauge32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPseModulePowerClassBudget.setStatus('current')
etsysPseModulePowerUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPseModulePowerUsage.setStatus('current')
etsysPsePortPowerManagementTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1), )
if mibBuilder.loadTexts: etsysPsePortPowerManagementTable.setStatus('current')
etsysPsePortPowerManagementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1), )
pethPsePortEntry.registerAugmentions(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPowerManagementEntry"))
etsysPsePortPowerManagementEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
if mibBuilder.loadTexts: etsysPsePortPowerManagementEntry.setStatus('current')
etsysPsePortPowerLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 34000)).clone(15400)).setUnits('milliwatts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysPsePortPowerLimit.setStatus('current')
etsysPsePortPowerUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1, 2), Gauge32()).setUnits('milliwatts').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPsePortPowerUsage.setStatus('current')
etsysPsePortPDType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("legacy", 1), ("ieee8023af", 2), ("other", 3), ("ieee8023", 4), ("ieee8023at", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPsePortPDType.setStatus('current')
etsysPsePortCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1, 4), Bits().clone(namedValues=NamedValues(("other", 0), ("ieee8023afCapable", 1), ("ieee8023atCapable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPsePortCapability.setStatus('current')
etsysPsePortCapabilitySelect = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ieee8023af", 1), ("ieee8023at", 2))).clone('ieee8023af')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysPsePortCapabilitySelect.setStatus('current')
etsysPsePortDetectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("disabled", 1), ("searching", 2), ("deliveringPower", 3), ("fault", 4), ("test", 5), ("otherFault", 6), ("requestingPower", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPsePortDetectionStatus.setStatus('current')
etsysPsePowerSupplyStatusTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 6), )
if mibBuilder.loadTexts: etsysPsePowerSupplyStatusTable.setStatus('current')
etsysPsePowerSupplyStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 6, 1), ).setIndexNames((0, "ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerSupplyModuleNumber"))
if mibBuilder.loadTexts: etsysPsePowerSupplyStatusEntry.setStatus('current')
etsysPsePowerSupplyModuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 6, 1, 1), Unsigned32())
if mibBuilder.loadTexts: etsysPsePowerSupplyModuleNumber.setStatus('current')
etsysPsePowerSupplyModuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 3, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("infoNotAvailable", 1), ("notInstalled", 2), ("installedAndOperating", 3), ("installedAndNotOperating", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysPsePowerSupplyModuleStatus.setStatus('current')
etsysPseChassisPowerRedundant = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 0, 1)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerDetected"))
if mibBuilder.loadTexts: etsysPseChassisPowerRedundant.setStatus('current')
etsysPseChassisPowerNonRedundant = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 0, 2)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerDetected"))
if mibBuilder.loadTexts: etsysPseChassisPowerNonRedundant.setStatus('current')
etsysPsePowerSupplyModuleStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 1, 0, 3)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerSupplyModuleStatus"))
if mibBuilder.loadTexts: etsysPsePowerSupplyModuleStatusChange.setStatus('current')
etsysPsePowerAllocationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2))
etsysPsePowerAllocationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1))
etsysPsePowerAllocationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 2))
etsysPsePowerAllocationControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1, 1)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerAllocationMode"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerSnmpNotification"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerAvailableMaximum"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseSlotPowerMaximum"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseSlotPowerAssigned"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPsePowerAllocationControlGroup = etsysPsePowerAllocationControlGroup.setStatus('current')
etsysPseChassisPowerStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1, 2)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerDetected"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerAvailable"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerConsumable"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerAssigned"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerRedundancy"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerSupplyModuleStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPseChassisPowerStatusGroup = etsysPseChassisPowerStatusGroup.setStatus('current')
etsysPsePowerNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1, 3)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerRedundant"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerNonRedundant"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerSupplyModuleStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPsePowerNotificationGroup = etsysPsePowerNotificationGroup.setStatus('current')
etsysPseModulePowerManagementGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1, 4)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseModulePowerMode"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseModulePowerClassBudget"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseModulePowerUsage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPseModulePowerManagementGroup = etsysPseModulePowerManagementGroup.setStatus('current')
etsysPsePortPowerManagementGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1, 5)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPowerLimit"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPowerUsage"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPDType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPsePortPowerManagementGroup = etsysPsePortPowerManagementGroup.setStatus('deprecated')
etsysPsePortPowerManagementGroupRev2 = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 1, 6)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPowerLimit"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPowerUsage"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPDType"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortCapability"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortCapabilitySelect"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortDetectionStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPsePortPowerManagementGroupRev2 = etsysPsePortPowerManagementGroupRev2.setStatus('current')
etsysPsePowerAllocationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 2, 1)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerAllocationControlGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerStatusGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPsePowerAllocationCompliance = etsysPsePowerAllocationCompliance.setStatus('current')
etsysPsePowerAllocationCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 2, 2)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerAllocationControlGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerStatusGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerNotificationGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseModulePowerManagementGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPowerManagementGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPsePowerAllocationCompliance2 = etsysPsePowerAllocationCompliance2.setStatus('deprecated')
etsysPsePowerAllocationCompliance2Rev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 50, 2, 2, 3)).setObjects(("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerAllocationControlGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseChassisPowerStatusGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePowerNotificationGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPseModulePowerManagementGroup"), ("ENTERASYS-POWER-ETHERNET-EXT-MIB", "etsysPsePortPowerManagementGroupRev2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysPsePowerAllocationCompliance2Rev2 = etsysPsePowerAllocationCompliance2Rev2.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-POWER-ETHERNET-EXT-MIB", etsysPseChassisPowerNonRedundant=etsysPseChassisPowerNonRedundant, etsysPsePortPowerManagementGroupRev2=etsysPsePortPowerManagementGroupRev2, etsysPsePowerSupplyModuleNumber=etsysPsePowerSupplyModuleNumber, etsysPseChassisPowerDetected=etsysPseChassisPowerDetected, etsysPseModulePowerClassBudget=etsysPseModulePowerClassBudget, etsysPseChassisPowerAllocation=etsysPseChassisPowerAllocation, etsysPseModulePowerManagementGroup=etsysPseModulePowerManagementGroup, etsysPsePowerNotification=etsysPsePowerNotification, etsysPsePowerAllocationCompliance2Rev2=etsysPsePowerAllocationCompliance2Rev2, etsysPsePortPowerManagementEntry=etsysPsePortPowerManagementEntry, etsysPseChassisPowerSnmpNotification=etsysPseChassisPowerSnmpNotification, etsysPsePortCapabilitySelect=etsysPsePortCapabilitySelect, etsysPseSlotPowerAssigned=etsysPseSlotPowerAssigned, etsysPsePowerAllocationCompliance=etsysPsePowerAllocationCompliance, etsysPseChassisPowerConsumable=etsysPseChassisPowerConsumable, etsysPseChassisPowerStatusGroup=etsysPseChassisPowerStatusGroup, etsysPsePortPowerUsage=etsysPsePortPowerUsage, etsysPseModulePowerManagementEntry=etsysPseModulePowerManagementEntry, etsysPseChassisPowerAssigned=etsysPseChassisPowerAssigned, etsysPseChassisPowerStatus=etsysPseChassisPowerStatus, etsysPseChassisPowerAvailableMaximum=etsysPseChassisPowerAvailableMaximum, etsysPsePortPowerLimit=etsysPsePortPowerLimit, etsysPsePowerSupplyModuleStatusChange=etsysPsePowerSupplyModuleStatusChange, PYSNMP_MODULE_ID=etsysPowerEthernetMibExtMIB, etsysPseChassisPowerRedundancy=etsysPseChassisPowerRedundancy, etsysPseSlotPowerAllocation=etsysPseSlotPowerAllocation, etsysPsePowerAllocationCompliance2=etsysPsePowerAllocationCompliance2, etsysPsePortCapability=etsysPsePortCapability, etsysPseChassisPowerAvailable=etsysPseChassisPowerAvailable, etsysPseSlotPowerAllocationTable=etsysPseSlotPowerAllocationTable, etsysPseSlotPowerAllocationEntry=etsysPseSlotPowerAllocationEntry, etsysPseModulePowerUsage=etsysPseModulePowerUsage, etsysPseChassisPowerRedundant=etsysPseChassisPowerRedundant, etsysPseSlotPowerManagement=etsysPseSlotPowerManagement, etsysPsePowerSupplyStatusEntry=etsysPsePowerSupplyStatusEntry, etsysPsePortPowerManagementTable=etsysPsePortPowerManagementTable, etsysPsePowerSupplyStatusTable=etsysPsePowerSupplyStatusTable, etsysPsePortPDType=etsysPsePortPDType, etsysPsePortPowerManagement=etsysPsePortPowerManagement, etsysPsePortPowerManagementGroup=etsysPsePortPowerManagementGroup, etsysPseModulePowerMode=etsysPseModulePowerMode, etsysPseChassisPowerAllocationMode=etsysPseChassisPowerAllocationMode, etsysPsePowerAllocationControlGroup=etsysPsePowerAllocationControlGroup, etsysPseModulePowerManagementTable=etsysPseModulePowerManagementTable, etsysPsePowerSupplyModuleStatus=etsysPsePowerSupplyModuleStatus, etsysPowerEthernetMibExtMIB=etsysPowerEthernetMibExtMIB, etsysPsePowerAllocationCompliances=etsysPsePowerAllocationCompliances, etsysPsePowerNotificationGroup=etsysPsePowerNotificationGroup, etsysPseSlotPowerMaximum=etsysPseSlotPowerMaximum, etsysPsePowerAllocationConformance=etsysPsePowerAllocationConformance, etsysPsePowerAllocationGroups=etsysPsePowerAllocationGroups, etsysPsePortDetectionStatus=etsysPsePortDetectionStatus, etsysPowerEthernetObjects=etsysPowerEthernetObjects)