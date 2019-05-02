#
# PySNMP MIB module SONUS-ANNOUNCEMENT-RESOURCES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONUS-ANNOUNCEMENT-RESOURCES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:09:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, MibIdentifier, Bits, Counter64, ModuleIdentity, iso, IpAddress, Counter32, TimeTicks, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Bits", "Counter64", "ModuleIdentity", "iso", "IpAddress", "Counter32", "TimeTicks", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sonusShelfIndex, sonusEventDescription, sonusSlotIndex, sonusEventLevel, sonusEventClass = mibBuilder.importSymbols("SONUS-COMMON-MIB", "sonusShelfIndex", "sonusEventDescription", "sonusSlotIndex", "sonusEventLevel", "sonusEventClass")
sonusResourcesMIBs, = mibBuilder.importSymbols("SONUS-SMI", "sonusResourcesMIBs")
SonusBoolean, = mibBuilder.importSymbols("SONUS-TC", "SonusBoolean")
sonusAnnouncementResourcesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5))
if mibBuilder.loadTexts: sonusAnnouncementResourcesMIB.setLastUpdated('200102030000Z')
if mibBuilder.loadTexts: sonusAnnouncementResourcesMIB.setOrganization('Sonus Networks, Inc.')
if mibBuilder.loadTexts: sonusAnnouncementResourcesMIB.setContactInfo(' Customer Support Sonus Networks, Inc, 5 carlisle Road Westford, MA 01886 USA Tel: 978-692-8999 Fax: 978-392-9118 E-mail: cs.snmp@sonusnet.com')
if mibBuilder.loadTexts: sonusAnnouncementResourcesMIB.setDescription('The MIB Module for Announcements.')
sonusAnnouncementResourcesMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1))
sonusAnnSegStatTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 1), )
if mibBuilder.loadTexts: sonusAnnSegStatTable.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegStatTable.setDescription('This table contains Announcement Segment File statistics')
sonusAnnSegStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 1, 1), ).setIndexNames((0, "SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatSegId"))
if mibBuilder.loadTexts: sonusAnnSegStatEntry.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegStatEntry.setDescription('')
sonusAnnSegStatSegId = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegStatSegId.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegStatSegId.setDescription('Represents the segment identity')
sonusAnnSegStatLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegStatLength.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegStatLength.setDescription('Represents segment length in bytes')
sonusAnnSegStatVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegStatVersion.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegStatVersion.setDescription('Represents number of segment file modifications detected')
sonusAnnSegStatPreload = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 1, 1, 4), SonusBoolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegStatPreload.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegStatPreload.setDescription('If TRUE, servers load segment during initialization rather than at first playback')
sonusAnnSegStatNfsPath = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegStatNfsPath.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegStatNfsPath.setDescription('Represents the NFS pathname of the segment file')
sonusAnnSegMemStatTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 2), )
if mibBuilder.loadTexts: sonusAnnSegMemStatTable.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegMemStatTable.setDescription('This table contains Announcement Segment Memory statistics')
sonusAnnSegMemStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 2, 1), ).setIndexNames((0, "SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegMemStatShelfIndex"), (0, "SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegMemStatSlotIndex"))
if mibBuilder.loadTexts: sonusAnnSegMemStatEntry.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegMemStatEntry.setDescription('')
sonusAnnSegMemStatShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegMemStatShelfIndex.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegMemStatShelfIndex.setDescription('Shelf index for this table')
sonusAnnSegMemStatSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegMemStatSlotIndex.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegMemStatSlotIndex.setDescription('Slot index for this table')
sonusAnnSegMemStatNumSegs = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegMemStatNumSegs.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegMemStatNumSegs.setDescription('Represents the number of segments server has loaded')
sonusAnnSegMemStatTotalBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegMemStatTotalBytes.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegMemStatTotalBytes.setDescription("Represents the server's segment memory size in bytes")
sonusAnnSegMemStatUsedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegMemStatUsedBytes.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegMemStatUsedBytes.setDescription('Represents the number of segment memory bytes used by all loaded segments. Segment memory is composed of 2K byte blocks. Therefore the actual number of bytes used by each segment is equal to the segment length rounded up to the next 2K byte boundary.')
sonusAnnSegPlayStatTable = MibTable((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3), )
if mibBuilder.loadTexts: sonusAnnSegPlayStatTable.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegPlayStatTable.setDescription('This table contains Announcement Segment Playback statistics')
sonusAnnSegPlayStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3, 1), ).setIndexNames((0, "SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegPlayStatShelfIndex"), (0, "SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegPlayStatSlotIndex"), (0, "SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegPlayStatSegId"))
if mibBuilder.loadTexts: sonusAnnSegPlayStatEntry.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegPlayStatEntry.setDescription('')
sonusAnnSegPlayStatShelfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegPlayStatShelfIndex.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegPlayStatShelfIndex.setDescription('Shelf index for this table')
sonusAnnSegPlayStatSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegPlayStatSlotIndex.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegPlayStatSlotIndex.setDescription('Slot index for this table')
sonusAnnSegPlayStatSegId = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegPlayStatSegId.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegPlayStatSegId.setDescription('SegId index for this table')
sonusAnnSegPlayStatVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegPlayStatVersion.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegPlayStatVersion.setDescription('Represents version of segment currently loaded')
sonusAnnSegPlayStatState = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("notPresent", 0), ("loading", 1), ("loaded", 2), ("updatePending", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegPlayStatState.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegPlayStatState.setDescription('Represents current state of the segment')
sonusAnnSegPlayStatDelOnceFree = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3, 1, 6), SonusBoolean()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegPlayStatDelOnceFree.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegPlayStatDelOnceFree.setDescription('If TRUE, the current version of segment data will be deleted from memory once sonusAnnSegPlayStatUseCount drops to zero. If a new version of the segment exists, then the new segment data will be automatically loaded.')
sonusAnnSegPlayStatUseCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegPlayStatUseCount.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegPlayStatUseCount.setDescription('Represents the number of calls currently playing this segment')
sonusAnnSegPlayStatTotalPlays = MibTableColumn((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegPlayStatTotalPlays.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegPlayStatTotalPlays.setDescription('Represents the cumulative number of times this version of the segment has been played since it was loaded')
sonusAnnouncementResourcesMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2))
sonusAnnouncementResourcesMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 0))
sonusAnnouncementResourcesMIBNotificationsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 1))
sonusAresUnavailCount = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAresUnavailCount.setStatus('current')
if mibBuilder.loadTexts: sonusAresUnavailCount.setDescription('Represents number of announcement resource allocate failures since the rising threshold was met.')
sonusAnnSegMemFullCount = MibScalar((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sonusAnnSegMemFullCount.setStatus('current')
if mibBuilder.loadTexts: sonusAnnSegMemFullCount.setDescription('Represents number of times an announcement cound not be loaded because segment memory was full for a given slot.')
sonusAnnouncementFileNotFoundNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 0, 1)).setObjects(("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatSegId"), ("SONUS-COMMON-MIB", "sonusShelfIndex"), ("SONUS-COMMON-MIB", "sonusSlotIndex"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusAnnouncementFileNotFoundNotification.setStatus('current')
if mibBuilder.loadTexts: sonusAnnouncementFileNotFoundNotification.setDescription('This trap indicates that the requested segment file could not be found. The segment file must be copied into either the <node>/announcement/preload or or <node>/announcement/ondemand directory.')
sonusAnnouncementFileFoundNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 0, 2)).setObjects(("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatSegId"), ("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatNfsPath"), ("SONUS-COMMON-MIB", "sonusShelfIndex"), ("SONUS-COMMON-MIB", "sonusSlotIndex"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusAnnouncementFileFoundNotification.setStatus('current')
if mibBuilder.loadTexts: sonusAnnouncementFileFoundNotification.setDescription('This trap indicates that a segment file, which previously cound not be found, was found.')
sonusAnnouncementFileInvalidNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 0, 3)).setObjects(("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatSegId"), ("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatNfsPath"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusAnnouncementFileInvalidNotification.setStatus('current')
if mibBuilder.loadTexts: sonusAnnouncementFileInvalidNotification.setDescription('This trap indicates that the specified segment file contains one or more format errors. Check SYS log for more detail.')
sonusAnnouncementFileValidNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 0, 4)).setObjects(("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatNfsPath"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusAnnouncementFileValidNotification.setStatus('current')
if mibBuilder.loadTexts: sonusAnnouncementFileValidNotification.setDescription('This trap indicates that previously invalid segment file has been replaced by a valid segment file.')
sonusAnnouncementSegmentLoadFailureNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 0, 5)).setObjects(("SONUS-COMMON-MIB", "sonusShelfIndex"), ("SONUS-COMMON-MIB", "sonusSlotIndex"), ("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatSegId"), ("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatVersion"), ("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatLength"), ("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegMemFullCount"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusAnnouncementSegmentLoadFailureNotification.setStatus('current')
if mibBuilder.loadTexts: sonusAnnouncementSegmentLoadFailureNotification.setDescription('This trap indicates that announcement segment could not be loaded because segment memory on the specified card is full. Segment ID, Version and Length pertain to the most recent segment load failure. Verify the length of this segment is within reason.')
sonusAnnouncementResUnavailRisingThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 0, 6)).setObjects(("SONUS-COMMON-MIB", "sonusShelfIndex"), ("SONUS-COMMON-MIB", "sonusSlotIndex"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusAnnouncementResUnavailRisingThresholdNotification.setStatus('current')
if mibBuilder.loadTexts: sonusAnnouncementResUnavailRisingThresholdNotification.setDescription('This trap indicates that all announcement resources on the specified card are in use.')
sonusAnnouncementResUnavailFallingThresholdNotification = NotificationType((1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 0, 7)).setObjects(("SONUS-COMMON-MIB", "sonusShelfIndex"), ("SONUS-COMMON-MIB", "sonusSlotIndex"), ("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAresUnavailCount"), ("SONUS-COMMON-MIB", "sonusEventDescription"), ("SONUS-COMMON-MIB", "sonusEventClass"), ("SONUS-COMMON-MIB", "sonusEventLevel"))
if mibBuilder.loadTexts: sonusAnnouncementResUnavailFallingThresholdNotification.setStatus('current')
if mibBuilder.loadTexts: sonusAnnouncementResUnavailFallingThresholdNotification.setDescription('This trap indicates that announcement resource usage on the specified card has dropped below a threshold.')
mibBuilder.exportSymbols("SONUS-ANNOUNCEMENT-RESOURCES-MIB", sonusAnnSegPlayStatTotalPlays=sonusAnnSegPlayStatTotalPlays, sonusAnnSegMemStatEntry=sonusAnnSegMemStatEntry, sonusAnnSegPlayStatSegId=sonusAnnSegPlayStatSegId, sonusAnnSegPlayStatVersion=sonusAnnSegPlayStatVersion, sonusAnnouncementSegmentLoadFailureNotification=sonusAnnouncementSegmentLoadFailureNotification, sonusAnnSegPlayStatShelfIndex=sonusAnnSegPlayStatShelfIndex, sonusAnnouncementFileNotFoundNotification=sonusAnnouncementFileNotFoundNotification, sonusAnnSegStatPreload=sonusAnnSegStatPreload, sonusAnnouncementResourcesMIBObjects=sonusAnnouncementResourcesMIBObjects, sonusAnnSegMemStatSlotIndex=sonusAnnSegMemStatSlotIndex, sonusAnnSegStatNfsPath=sonusAnnSegStatNfsPath, sonusAnnSegMemFullCount=sonusAnnSegMemFullCount, sonusAnnouncementFileFoundNotification=sonusAnnouncementFileFoundNotification, sonusAnnSegPlayStatTable=sonusAnnSegPlayStatTable, sonusAnnSegPlayStatSlotIndex=sonusAnnSegPlayStatSlotIndex, sonusAnnSegMemStatTable=sonusAnnSegMemStatTable, sonusAnnouncementFileValidNotification=sonusAnnouncementFileValidNotification, sonusAnnSegPlayStatEntry=sonusAnnSegPlayStatEntry, sonusAnnouncementResourcesMIBNotificationsObjects=sonusAnnouncementResourcesMIBNotificationsObjects, sonusAnnouncementResourcesMIBNotifications=sonusAnnouncementResourcesMIBNotifications, sonusAnnSegStatVersion=sonusAnnSegStatVersion, sonusAnnSegMemStatUsedBytes=sonusAnnSegMemStatUsedBytes, sonusAnnSegPlayStatState=sonusAnnSegPlayStatState, sonusAnnSegPlayStatDelOnceFree=sonusAnnSegPlayStatDelOnceFree, sonusAnnSegMemStatShelfIndex=sonusAnnSegMemStatShelfIndex, sonusAnnSegStatLength=sonusAnnSegStatLength, sonusAnnouncementResourcesMIBNotificationsPrefix=sonusAnnouncementResourcesMIBNotificationsPrefix, sonusAnnSegStatSegId=sonusAnnSegStatSegId, sonusAnnSegMemStatTotalBytes=sonusAnnSegMemStatTotalBytes, sonusAnnouncementResUnavailFallingThresholdNotification=sonusAnnouncementResUnavailFallingThresholdNotification, sonusAresUnavailCount=sonusAresUnavailCount, sonusAnnSegStatEntry=sonusAnnSegStatEntry, sonusAnnouncementResourcesMIB=sonusAnnouncementResourcesMIB, sonusAnnSegPlayStatUseCount=sonusAnnSegPlayStatUseCount, sonusAnnSegMemStatNumSegs=sonusAnnSegMemStatNumSegs, sonusAnnouncementFileInvalidNotification=sonusAnnouncementFileInvalidNotification, sonusAnnouncementResUnavailRisingThresholdNotification=sonusAnnouncementResUnavailRisingThresholdNotification, PYSNMP_MODULE_ID=sonusAnnouncementResourcesMIB, sonusAnnSegStatTable=sonusAnnSegStatTable)