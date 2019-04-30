#
# PySNMP MIB module HPN-ICF-RMON-EXT2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-RMON-EXT2-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:29:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
OwnerString, EntryStatus = mibBuilder.importSymbols("RMON-MIB", "OwnerString", "EntryStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, Counter64, NotificationType, MibIdentifier, IpAddress, TimeTicks, Integer32, Unsigned32, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Counter64", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Integer32", "Unsigned32", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfRmonExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125))
hpnicfRmonExt.setRevisions(('2012-06-19 00:00',))
if mibBuilder.loadTexts: hpnicfRmonExt.setLastUpdated('201206190000Z')
if mibBuilder.loadTexts: hpnicfRmonExt.setOrganization('')
hpnicfRmonExtAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1), )
if mibBuilder.loadTexts: hpnicfRmonExtAlarmTable.setStatus('current')
hpnicfRmonExtAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1), ).setIndexNames((0, "HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmIndex"))
if mibBuilder.loadTexts: hpnicfRmonExtAlarmEntry.setStatus('current')
hpnicfRmonExtAlarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRmonExtAlarmIndex.setStatus('current')
hpnicfRmonExtAlarmInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 65535)).clone(1800)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRmonExtAlarmInterval.setStatus('current')
hpnicfRmonExtAlarmVariable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRmonExtAlarmVariable.setStatus('current')
hpnicfRmonExtAlarmSympol = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRmonExtAlarmSympol.setStatus('current')
hpnicfRmonExtAlarmSampleType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("absoluteValue", 1), ("deltaValue", 2), ("speedValue", 3))).clone('absoluteValue')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRmonExtAlarmSampleType.setStatus('current')
hpnicfRmonExtAlarmValue = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfRmonExtAlarmValue.setStatus('current')
hpnicfRmonExtAlarmStartupAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("risingAlarm", 1), ("fallingAlarm", 2), ("risingOrFallingAlarm", 3))).clone('risingOrFallingAlarm')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRmonExtAlarmStartupAlarm.setStatus('current')
hpnicfRmonExtAlarmRisingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 8), Integer32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRmonExtAlarmRisingThreshold.setStatus('current')
hpnicfRmonExtAlarmFallingThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRmonExtAlarmFallingThreshold.setStatus('current')
hpnicfRmonExtAlarmRisingEvtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRmonExtAlarmRisingEvtIndex.setStatus('current')
hpnicfRmonExtAlarmFallingEvtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRmonExtAlarmFallingEvtIndex.setStatus('current')
hpnicfRmonExtAlarmStatCycle = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRmonExtAlarmStatCycle.setStatus('current')
hpnicfRmonExtAlarmStatType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forever", 1), ("during", 2))).clone('forever')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRmonExtAlarmStatType.setStatus('current')
hpnicfRmonExtAlarmOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 14), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRmonExtAlarmOwner.setStatus('current')
hpnicfRmonExtAlarmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 15), EntryStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfRmonExtAlarmStatus.setStatus('current')
hpnicfRmonExtEvent = ObjectIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 0))
if mibBuilder.loadTexts: hpnicfRmonExtEvent.setStatus('current')
hpnicfRmonExtRisingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 0, 1)).setObjects(("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmIndex"), ("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmSympol"), ("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmSampleType"), ("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmValue"), ("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmRisingThreshold"))
if mibBuilder.loadTexts: hpnicfRmonExtRisingAlarm.setStatus('current')
hpnicfRmonExtFallingAlarm = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 0, 2)).setObjects(("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmIndex"), ("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmSympol"), ("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmSampleType"), ("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmValue"), ("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmFallingThreshold"))
if mibBuilder.loadTexts: hpnicfRmonExtFallingAlarm.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-RMON-EXT2-MIB", hpnicfRmonExtAlarmFallingThreshold=hpnicfRmonExtAlarmFallingThreshold, hpnicfRmonExtFallingAlarm=hpnicfRmonExtFallingAlarm, hpnicfRmonExtAlarmRisingEvtIndex=hpnicfRmonExtAlarmRisingEvtIndex, hpnicfRmonExtAlarmEntry=hpnicfRmonExtAlarmEntry, hpnicfRmonExtAlarmIndex=hpnicfRmonExtAlarmIndex, PYSNMP_MODULE_ID=hpnicfRmonExt, hpnicfRmonExtEvent=hpnicfRmonExtEvent, hpnicfRmonExtAlarmStatus=hpnicfRmonExtAlarmStatus, hpnicfRmonExtRisingAlarm=hpnicfRmonExtRisingAlarm, hpnicfRmonExtAlarmRisingThreshold=hpnicfRmonExtAlarmRisingThreshold, hpnicfRmonExtAlarmStatType=hpnicfRmonExtAlarmStatType, hpnicfRmonExtAlarmStartupAlarm=hpnicfRmonExtAlarmStartupAlarm, hpnicfRmonExtAlarmTable=hpnicfRmonExtAlarmTable, hpnicfRmonExtAlarmInterval=hpnicfRmonExtAlarmInterval, hpnicfRmonExtAlarmSampleType=hpnicfRmonExtAlarmSampleType, hpnicfRmonExtAlarmValue=hpnicfRmonExtAlarmValue, hpnicfRmonExtAlarmVariable=hpnicfRmonExtAlarmVariable, hpnicfRmonExt=hpnicfRmonExt, hpnicfRmonExtAlarmStatCycle=hpnicfRmonExtAlarmStatCycle, hpnicfRmonExtAlarmOwner=hpnicfRmonExtAlarmOwner, hpnicfRmonExtAlarmFallingEvtIndex=hpnicfRmonExtAlarmFallingEvtIndex, hpnicfRmonExtAlarmSympol=hpnicfRmonExtAlarmSympol)