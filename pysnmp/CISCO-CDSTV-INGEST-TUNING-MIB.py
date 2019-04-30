#
# PySNMP MIB module CISCO-CDSTV-INGEST-TUNING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CDSTV-INGEST-TUNING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:35:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, IpAddress, Gauge32, MibIdentifier, Integer32, ModuleIdentity, Counter64, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "IpAddress", "Gauge32", "MibIdentifier", "Integer32", "ModuleIdentity", "Counter64", "Bits", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoCdstvIngestTuningMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 750))
ciscoCdstvIngestTuningMIB.setRevisions(('2010-06-24 00:00',))
if mibBuilder.loadTexts: ciscoCdstvIngestTuningMIB.setLastUpdated('201006240000Z')
if mibBuilder.loadTexts: ciscoCdstvIngestTuningMIB.setOrganization('Cisco Systems, Inc.')
ciscoCdstvIngestTuningMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 0))
ciscoCdstvIngestTuningMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 1))
ciscoCdstvIngestTuningMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 2))
ciscoCdstvIngestTuningMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 1))
cdstvTrickModeSpeedTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1), )
if mibBuilder.loadTexts: cdstvTrickModeSpeedTable.setStatus('current')
cdstvTrickModeSpeedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1, 1), ).setIndexNames((0, "CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvTrickModeSpeedIndex"))
if mibBuilder.loadTexts: cdstvTrickModeSpeedEntry.setStatus('current')
cdstvTrickModeSpeedIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cdstvTrickModeSpeedIndex.setStatus('current')
cdstvTrickModeSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-127, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvTrickModeSpeed.setStatus('current')
cdstvServerIngestMPEGSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2))
cdstvServerPIDStandardization = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerPIDStandardization.setStatus('current')
cdstvServerSequenceEndRemove = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerSequenceEndRemove.setStatus('current')
cdstvServerRateStandardize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 750, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvServerRateStandardize.setStatus('current')
ciscoCdstvIngestTuningMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 2))
ciscoCdstvIngestTuningMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 1, 1)).setObjects(("CISCO-CDSTV-INGEST-TUNING-MIB", "ciscoCdstvIngestTuningMIBMainObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvIngestTuningMIBCompliance = ciscoCdstvIngestTuningMIBCompliance.setStatus('current')
ciscoCdstvIngestTuningMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 750, 2, 2, 1)).setObjects(("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvTrickModeSpeed"), ("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvServerPIDStandardization"), ("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvServerSequenceEndRemove"), ("CISCO-CDSTV-INGEST-TUNING-MIB", "cdstvServerRateStandardize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvIngestTuningMIBMainObjectGroup = ciscoCdstvIngestTuningMIBMainObjectGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CDSTV-INGEST-TUNING-MIB", ciscoCdstvIngestTuningMIBNotifs=ciscoCdstvIngestTuningMIBNotifs, ciscoCdstvIngestTuningMIBMainObjectGroup=ciscoCdstvIngestTuningMIBMainObjectGroup, cdstvServerIngestMPEGSettings=cdstvServerIngestMPEGSettings, ciscoCdstvIngestTuningMIBCompliances=ciscoCdstvIngestTuningMIBCompliances, cdstvTrickModeSpeedIndex=cdstvTrickModeSpeedIndex, PYSNMP_MODULE_ID=ciscoCdstvIngestTuningMIB, ciscoCdstvIngestTuningMIBConform=ciscoCdstvIngestTuningMIBConform, cdstvTrickModeSpeed=cdstvTrickModeSpeed, ciscoCdstvIngestTuningMIBCompliance=ciscoCdstvIngestTuningMIBCompliance, cdstvServerPIDStandardization=cdstvServerPIDStandardization, cdstvTrickModeSpeedEntry=cdstvTrickModeSpeedEntry, cdstvServerSequenceEndRemove=cdstvServerSequenceEndRemove, cdstvServerRateStandardize=cdstvServerRateStandardize, ciscoCdstvIngestTuningMIB=ciscoCdstvIngestTuningMIB, ciscoCdstvIngestTuningMIBObjects=ciscoCdstvIngestTuningMIBObjects, ciscoCdstvIngestTuningMIBGroups=ciscoCdstvIngestTuningMIBGroups, cdstvTrickModeSpeedTable=cdstvTrickModeSpeedTable)