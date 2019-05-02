#
# PySNMP MIB module NOKIA-HWM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-HWM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:23:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ntcHWMibs, ntcHWReqs, ntcCommonModules = mibBuilder.importSymbols("NOKIA-COMMON-MIB-OID-REGISTRATION-MIB", "ntcHWMibs", "ntcHWReqs", "ntcCommonModules")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, IpAddress, TimeTicks, ModuleIdentity, MibIdentifier, Unsigned32, Counter32, NotificationType, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "IpAddress", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Unsigned32", "Counter32", "NotificationType", "iso", "Bits")
AutonomousType, TextualConvention, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "TextualConvention", "TimeStamp", "DisplayString")
ntcHWModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 94, 1, 16, 5, 1))
ntcHWModule.setRevisions(('1998-08-24 00:00', '1998-09-03 00:00', '1998-09-24 00:00', '1998-10-04 00:00', '1999-01-08 00:00', '1999-08-05 00:00', '1999-10-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ntcHWModule.setRevisionsDescriptions(('Rev 0.1 August 24, 1998 Initial version - ready for review', 'Rev 0.2 September 3, 1998 Initial review by Tero Soukko whose comments have been incorporated.', 'Rev 0.3 September 24, 1998 ready for initial review.', 'Rev 0.4 Updated anchors to use values registered by Mika Kiikkila.', 'Rev 1.0 Syntax of ntcHWLastChangedTime changed from DateAndTime to TimeStamp. Traps commented out because they are part of Nokia Common Alarm MIB.', 'Rev 1.01 Those IMPORTS which are not used are removed. Groups ntcHWSlots and ntcHWEventGroup which are not defined in this module are removed. The name NokiaHwmSlotEntry is changed to NtcHWSlotEntry on account of convenience. All notification definions before out-commented removed. Some esthetic modifications made.', "Comment 'The NMS is not allowed to set the value of ntcHWAdminstate to missing.' added to the ntcHWAdminstate's description.",))
if mibBuilder.loadTexts: ntcHWModule.setLastUpdated('9901080000Z')
if mibBuilder.loadTexts: ntcHWModule.setOrganization('Nokia')
if mibBuilder.loadTexts: ntcHWModule.setContactInfo('Anna-Kaisa Lindfors Nokia Telecommunications Oy Hiomotie 5, FIN-00380 Helsinki +358-9-51121 anna-kaisa.lindfors@nokia.com')
if mibBuilder.loadTexts: ntcHWModule.setDescription('The MIB module that is used to control the Hardware Management information.')
ntcHWObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1))
ntcHWEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 2, 0))
ntcHWGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 1, 1))
ntcHWCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 1, 2))
ntcHWUnitTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1), )
if mibBuilder.loadTexts: ntcHWUnitTable.setStatus('current')
if mibBuilder.loadTexts: ntcHWUnitTable.setDescription("A table which contains an entry for each pluggable circuit board (in this MIB a 'unit' is the same as a pluggable circuit board.) Entries of this table are automatically created by the hardware management software.")
ntcHWUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ntcHWUnitEntry.setStatus('current')
if mibBuilder.loadTexts: ntcHWUnitEntry.setDescription('A conceptual row in the ntcHWUnitTable. Rows are created automatically by the Hardware Management software.')
ntcHWAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("inService", 1), ("outOfService", 2), ("inTest", 3), ("missing", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcHWAdminState.setStatus('current')
if mibBuilder.loadTexts: ntcHWAdminState.setDescription('Represents the desired state of the unit. inService indicates that the unit is intended to be operating normally. outOfService indicates that the unit should be taken out of normal operating mode and no data traffic should appear in this unit. inTest indicates that the unit should be placed into a selftest mode. missing indicates that the unit is expected to be present but has been detected as not being physically present. The NMS is not allowed to set the value of ntcHWAdminstate to missing.')
ntcHWOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcHWOperState.setStatus('current')
if mibBuilder.loadTexts: ntcHWOperState.setDescription('Indicates the current state of the unit. down indicates that the unit is in a non-functional state. up indicates that the unit is functioning normally.')
ntcHWAvailabilityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("inCharge", 1), ("applicationStarting", 2), ("applicationShutdown", 3), ("platformStarting", 4), ("resetting", 5), ("separated", 6), ("unconfigured", 7), ("testing", 8), ("standby", 9), ("dormant", 10), ("unavailable", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcHWAvailabilityStatus.setStatus('current')
if mibBuilder.loadTexts: ntcHWAvailabilityStatus.setDescription("Provides more specific information on the state of the unit in this conceptual row. The status column has eleven defined values: inCharge = the unit is fully operational and ready to perform its desired tasks; applicationStarting = the application software is starting up; applicationShutdown = the application software is shutting down; platformStarting = Basic platform software is starting up; resetting = the disk files are closed and hardware reset is forced; separated = Only basic OS software is running. The unit can start application software on request; unconfigured = The administrative state of the unit is 'missing', disk files are closed and only basic OS software is running. The unit refuses to start application software; testing = Selftests can be performed, only basic OS are running; standby = The unit is redundant and is fully operational but not in charge of operations. It is ready to move to 'inCharge' state when necessary; dormant = All connections are physically inactive to enable removal of the unit without electric disturbance in the backplane. Only watchdog software is running for a short duration of time; unavailable = The unit is not physically present or cannot be contacted.")
ntcHWRestart = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("reset", 1), ("hotRestart", 2), ("detach", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcHWRestart.setStatus('current')
if mibBuilder.loadTexts: ntcHWRestart.setDescription('Provides the ability to reset or perform a hot restart the unit represented by this conceptual row. reset = the Unit is shutdown in an orderly manner and restarted again via hardware reset; hotRestart = only the software in a unit is restarted, a hardware reset is not initiated; detach = all electrical connections of the unit are forced to an inactive state to enable removal of the unit without electrical disturbance in the backplane.')
ntcHWLedState = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("red", 1), ("yellow", 2), ("black", 3), ("green", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcHWLedState.setStatus('current')
if mibBuilder.loadTexts: ntcHWLedState.setDescription('Indicates the current LED color of the unit represented by this conceptual row.')
ntcHWSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcHWSerialNumber.setStatus('current')
if mibBuilder.loadTexts: ntcHWSerialNumber.setDescription('The units serial number in displayable format.')
ntcHWProductionDate = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcHWProductionDate.setStatus('current')
if mibBuilder.loadTexts: ntcHWProductionDate.setDescription('The units production date in displayable format.')
ntcHWUnitEntryChanged = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 1, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcHWUnitEntryChanged.setStatus('current')
if mibBuilder.loadTexts: ntcHWUnitEntryChanged.setDescription('Represents the value of sysUpTime at the instant that this conceptual row entry has changed.')
ntcHWSlotTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 2), )
if mibBuilder.loadTexts: ntcHWSlotTable.setStatus('current')
if mibBuilder.loadTexts: ntcHWSlotTable.setDescription('Table whose entries represent the expected circuit board type. The entries are created automatically by the hardware management software.')
ntcHWSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ntcHWSlotEntry.setStatus('current')
if mibBuilder.loadTexts: ntcHWSlotEntry.setDescription('The logical row describing the expected circiut board type of a slot.')
ntcHWDesiredUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 2, 1, 2), AutonomousType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcHWDesiredUnitType.setStatus('current')
if mibBuilder.loadTexts: ntcHWDesiredUnitType.setDescription("The unit type which is expected to be inserted or present in the current slot. An indication of the vendor-specific hardware type of the HWM entity. Note that this is different from the definition of MIB-II's sysObjectID. An agent should set this object to a enterprise-specific registration identifier value indicating the specific equipment type in detail. If no vendor-specific registration identifier exists for this entity, or the value is unknown by this agent, then the value { 0 0 } is returned.")
ntcHWLastChangedTime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcHWLastChangedTime.setStatus('current')
if mibBuilder.loadTexts: ntcHWLastChangedTime.setDescription('The value of sysUpTime at the time any of these events occur: * any instance in the following object changes value: - hwmUnitEntryChanged This object shall be set to value 0 in startup.')
ntcHWLoadInventoryContainer = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcHWLoadInventoryContainer.setStatus('current')
if mibBuilder.loadTexts: ntcHWLoadInventoryContainer.setDescription('Writing any value to this object will cause the hardware management software to reread its configuration file from disk.')
ntcHWUnits = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 1, 1, 1)).setObjects(("NOKIA-HWM-MIB", "ntcHWAdminState"), ("NOKIA-HWM-MIB", "ntcHWOperState"), ("NOKIA-HWM-MIB", "ntcHWAvailabilityStatus"), ("NOKIA-HWM-MIB", "ntcHWRestart"), ("NOKIA-HWM-MIB", "ntcHWLedState"), ("NOKIA-HWM-MIB", "ntcHWSerialNumber"), ("NOKIA-HWM-MIB", "ntcHWProductionDate"), ("NOKIA-HWM-MIB", "ntcHWUnitEntryChanged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcHWUnits = ntcHWUnits.setStatus('current')
if mibBuilder.loadTexts: ntcHWUnits.setDescription('A collection of objects representing the status of a unit.')
ntcHWCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 1, 2, 1)).setObjects(("ENTITY-MIB", "entityPhysicalGroup"), ("NOKIA-HWM-MIB", "ntcHWUnits"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcHWCompliance = ntcHWCompliance.setStatus('current')
if mibBuilder.loadTexts: ntcHWCompliance.setDescription('The compliance statement Hardware Management.')
mibBuilder.exportSymbols("NOKIA-HWM-MIB", ntcHWCompliance=ntcHWCompliance, ntcHWLedState=ntcHWLedState, ntcHWDesiredUnitType=ntcHWDesiredUnitType, ntcHWLastChangedTime=ntcHWLastChangedTime, ntcHWSlotEntry=ntcHWSlotEntry, ntcHWUnits=ntcHWUnits, ntcHWUnitEntry=ntcHWUnitEntry, ntcHWUnitEntryChanged=ntcHWUnitEntryChanged, ntcHWUnitTable=ntcHWUnitTable, ntcHWProductionDate=ntcHWProductionDate, ntcHWLoadInventoryContainer=ntcHWLoadInventoryContainer, ntcHWGroups=ntcHWGroups, ntcHWCompliances=ntcHWCompliances, ntcHWModule=ntcHWModule, ntcHWOperState=ntcHWOperState, ntcHWRestart=ntcHWRestart, ntcHWEvents=ntcHWEvents, ntcHWAvailabilityStatus=ntcHWAvailabilityStatus, ntcHWAdminState=ntcHWAdminState, ntcHWSlotTable=ntcHWSlotTable, ntcHWSerialNumber=ntcHWSerialNumber, ntcHWObjs=ntcHWObjs, PYSNMP_MODULE_ID=ntcHWModule)