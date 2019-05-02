#
# PySNMP MIB module RADLAN-TBI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-TBI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:49:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, Bits, ModuleIdentity, Integer32, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, MibIdentifier, Unsigned32, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "Bits", "ModuleIdentity", "Integer32", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "MibIdentifier", "Unsigned32", "Counter64", "TimeTicks")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
rlTBIMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 145))
rlTBIMib.setRevisions(('2006-02-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlTBIMib.setRevisionsDescriptions(('Time Range Infrastructure MIBs initial version. ',))
if mibBuilder.loadTexts: rlTBIMib.setLastUpdated('200604040000Z')
if mibBuilder.loadTexts: rlTBIMib.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: rlTBIMib.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rlTBIMib.setDescription('Time Range Infrastructure MIBs initial version. ')
rlTBITimeRangeTable = MibTable((1, 3, 6, 1, 4, 1, 89, 145, 1), )
if mibBuilder.loadTexts: rlTBITimeRangeTable.setStatus('current')
if mibBuilder.loadTexts: rlTBITimeRangeTable.setDescription('This table specifies Time Based Infra table')
rlTBITimeRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 145, 1, 1), ).setIndexNames((1, "RADLAN-TBI-MIB", "rlTBITimeRangeName"))
if mibBuilder.loadTexts: rlTBITimeRangeEntry.setStatus('current')
if mibBuilder.loadTexts: rlTBITimeRangeEntry.setDescription('Each entry in this table describes the new time range for ACE. The index is time range name')
rlTBITimeRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rlTBITimeRangeName.setStatus('current')
if mibBuilder.loadTexts: rlTBITimeRangeName.setDescription('Name of time range.')
rlTBITimeRangeAbsoluteStart = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 14))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTBITimeRangeAbsoluteStart.setStatus('current')
if mibBuilder.loadTexts: rlTBITimeRangeAbsoluteStart.setDescription('Time of start of absolute time range in following format: month day year hh:mm month: 01-12 (January-December) day: 01-31 year: 0-99 (2000-2099) hh: 0-23 (hours) mm: 0-59 (minutes)')
rlTBITimeRangeAbsoluteEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 14))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTBITimeRangeAbsoluteEnd.setStatus('current')
if mibBuilder.loadTexts: rlTBITimeRangeAbsoluteEnd.setDescription('Time of end of absolute time range in following format: month day year hh:mm month: 01-12 (January-December) day: 01-31 year: 0-99 (2000-2099) hh: 0-23 (hours) mm: 0-59 (minutes)')
rlTBITimeRangeActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTBITimeRangeActiveStatus.setStatus('current')
if mibBuilder.loadTexts: rlTBITimeRangeActiveStatus.setDescription('Shows whether the current time range is active according to the current clock.')
rlTBITimeRangeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlTBITimeRangeRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlTBITimeRangeRowStatus.setDescription('Row Status. It is used for adding/deleting entries of this table.')
class RlTBIWeekDayList(TextualConvention, Bits):
    description = 'Bitmap that includes days of week. Each bit in the bitmap associated with corresponding day of the week.'
    status = 'current'
    namedValues = NamedValues(("monday", 0), ("tuesday", 1), ("wednesday", 2), ("thursday", 3), ("friday", 4), ("saturday", 5), ("sunday", 6))

rlTBIPeriodicTable = MibTable((1, 3, 6, 1, 4, 1, 89, 145, 2), )
if mibBuilder.loadTexts: rlTBIPeriodicTable.setStatus('current')
if mibBuilder.loadTexts: rlTBIPeriodicTable.setDescription('This table specifies Time Based Infra Periodic table')
rlTBIPeriodicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 145, 2, 1), ).setIndexNames((0, "RADLAN-TBI-MIB", "rlTBIPeriodicTimeRangeName"), (0, "RADLAN-TBI-MIB", "rlTBIPeriodicWeekDayList"), (0, "RADLAN-TBI-MIB", "rlTBIPeriodicStart"), (0, "RADLAN-TBI-MIB", "rlTBIPeriodicEnd"))
if mibBuilder.loadTexts: rlTBIPeriodicEntry.setStatus('current')
if mibBuilder.loadTexts: rlTBIPeriodicEntry.setDescription('Each entry in this table describes periodic time range.')
rlTBIPeriodicTimeRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rlTBIPeriodicTimeRangeName.setStatus('current')
if mibBuilder.loadTexts: rlTBIPeriodicTimeRangeName.setDescription('Time Range Name the periodic is defined on. ')
rlTBIPeriodicWeekDayList = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 2, 1, 2), RlTBIWeekDayList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTBIPeriodicWeekDayList.setStatus('current')
if mibBuilder.loadTexts: rlTBIPeriodicWeekDayList.setDescription('The bitmap allows to user to select periodic time range for several days at once. The periodic range will be associated with specific days when corresponding bits will be set. If at least one bit has been set in the rlTBIPeriodicWeekDayList, the weekday in rlTBIPeriodicStart and rlTBIPeriodicEnd is not relevant and should be set to zero.')
rlTBIPeriodicStart = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTBIPeriodicStart.setStatus('current')
if mibBuilder.loadTexts: rlTBIPeriodicStart.setDescription('Time of start of periodic time range in following format: weekday hh:mm weekday: 0-7 (0 means the weekday is not specified, 1-7 are weekdays from Monday to Sunday) hh: 0-23 (hours) mm: 0-59 (minutes) Weekday may be 0 only if periodic time range weekdays were specified in rlTBIPeriodicWeekDayList.')
rlTBIPeriodicEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTBIPeriodicEnd.setStatus('current')
if mibBuilder.loadTexts: rlTBIPeriodicEnd.setDescription('Time of end of periodic time range in following format: weekday hh:mm weekday: 0-7 (0 means the weekday is not specified, 1-7 are weekdays from Monday to Sunday) hh: 0-23 (hours) mm: 0-59 (minutes) Weekday may be 0 only if periodic time range weekdays were specified in rlTBIPeriodicWeekDayList.')
rlTBIPeriodicRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 145, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlTBIPeriodicRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlTBIPeriodicRowStatus.setDescription('Row Status. It is used for adding/deleting entries of this table.')
mibBuilder.exportSymbols("RADLAN-TBI-MIB", rlTBIPeriodicStart=rlTBIPeriodicStart, rlTBIPeriodicEnd=rlTBIPeriodicEnd, PYSNMP_MODULE_ID=rlTBIMib, rlTBITimeRangeName=rlTBITimeRangeName, rlTBITimeRangeAbsoluteStart=rlTBITimeRangeAbsoluteStart, RlTBIWeekDayList=RlTBIWeekDayList, rlTBIPeriodicWeekDayList=rlTBIPeriodicWeekDayList, rlTBIPeriodicTable=rlTBIPeriodicTable, rlTBITimeRangeEntry=rlTBITimeRangeEntry, rlTBIPeriodicEntry=rlTBIPeriodicEntry, rlTBIPeriodicTimeRangeName=rlTBIPeriodicTimeRangeName, rlTBITimeRangeTable=rlTBITimeRangeTable, rlTBIPeriodicRowStatus=rlTBIPeriodicRowStatus, rlTBITimeRangeAbsoluteEnd=rlTBITimeRangeAbsoluteEnd, rlTBITimeRangeActiveStatus=rlTBITimeRangeActiveStatus, rlTBIMib=rlTBIMib, rlTBITimeRangeRowStatus=rlTBITimeRangeRowStatus)