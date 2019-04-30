#
# PySNMP MIB module PANASAS-EVENTS-MIB-V1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PANASAS-EVENTS-MIB-V1
# Produced by pysmi-0.3.4 at Mon Apr 29 20:27:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
panFs, = mibBuilder.importSymbols("PANASAS-PANFS-MIB-V1", "panFs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, Unsigned32, Counter64, iso, Counter32, Bits, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Unsigned32", "Counter64", "iso", "Counter32", "Bits", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "NotificationType", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
panEvents = ModuleIdentity((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1))
panEvents.setRevisions(('2011-04-07 00:00',))
if mibBuilder.loadTexts: panEvents.setLastUpdated('201104070000Z')
if mibBuilder.loadTexts: panEvents.setOrganization('Panasas, Inc')
panEventTableSize = MibScalar((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventTableSize.setStatus('current')
panEventTable = MibTable((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2), )
if mibBuilder.loadTexts: panEventTable.setStatus('current')
panEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1), ).setIndexNames((0, "PANASAS-EVENTS-MIB-V1", "panEventIndex"))
if mibBuilder.loadTexts: panEventEntry.setStatus('current')
panEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventIndex.setStatus('current')
panEventCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventCategory.setStatus('current')
panEventDate = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventDate.setStatus('current')
panEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventTime.setStatus('current')
panEventShelfName = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventShelfName.setStatus('current')
panEventShelfSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventShelfSlot.setStatus('current')
panEventHwDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventHwDesc.setStatus('current')
panEventBladeIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventBladeIPAddr.setStatus('current')
panEventText = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventText.setStatus('current')
panEventCode = MibTableColumn((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: panEventCode.setStatus('current')
mibBuilder.exportSymbols("PANASAS-EVENTS-MIB-V1", panEventShelfName=panEventShelfName, panEventIndex=panEventIndex, panEventText=panEventText, panEventEntry=panEventEntry, panEventCategory=panEventCategory, panEventTime=panEventTime, panEventTableSize=panEventTableSize, panEventTable=panEventTable, panEventBladeIPAddr=panEventBladeIPAddr, panEventCode=panEventCode, PYSNMP_MODULE_ID=panEvents, panEventShelfSlot=panEventShelfSlot, panEventHwDesc=panEventHwDesc, panEvents=panEvents, panEventDate=panEventDate)