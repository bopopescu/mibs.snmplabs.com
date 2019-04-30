#
# PySNMP MIB module CISCO-IPSLA-AUTOMEASURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IPSLA-AUTOMEASURE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:45:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
IpSlaOperType, IpSlaReactVar = mibBuilder.importSymbols("CISCO-IPSLA-TC-MIB", "IpSlaOperType", "IpSlaReactVar")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InetPortNumber, InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter64, Unsigned32, Counter32, Bits, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, iso, Integer32, IpAddress, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "Counter32", "Bits", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "iso", "Integer32", "IpAddress", "ObjectIdentity", "NotificationType")
TextualConvention, StorageType, TruthValue, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "StorageType", "TruthValue", "DisplayString", "RowStatus")
ciscoIpSlaAutoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 633))
ciscoIpSlaAutoMIB.setRevisions(('2007-06-13 00:00',))
if mibBuilder.loadTexts: ciscoIpSlaAutoMIB.setLastUpdated('200706130000Z')
if mibBuilder.loadTexts: ciscoIpSlaAutoMIB.setOrganization('Cisco Systems, Inc.')
ciscoIpSlaAutoMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 633, 0))
ciscoIpSlaAutoMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 633, 1))
cipslaAutoGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1), )
if mibBuilder.loadTexts: cipslaAutoGroupTable.setStatus('current')
cipslaAutoGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1), ).setIndexNames((0, "CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupName"))
if mibBuilder.loadTexts: cipslaAutoGroupEntry.setStatus('current')
cipslaAutoGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: cipslaAutoGroupName.setStatus('current')
cipslaAutoGroupDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupDescription.setStatus('current')
cipslaAutoGroupDestinationName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupDestinationName.setStatus('current')
cipslaAutoGroupADDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 4), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupADDestPort.setStatus('current')
cipslaAutoGroupOperTemplateName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupOperTemplateName.setStatus('current')
cipslaAutoGroupSchedulerId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupSchedulerId.setStatus('current')
cipslaAutoGroupQoSEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupQoSEnable.setStatus('current')
cipslaAutoGroupOperType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 8), IpSlaOperType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupOperType.setStatus('current')
cipslaAutoGroupDestIPADEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 9), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupDestIPADEnable.setStatus('current')
cipslaAutoGroupADMeasureRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65536)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupADMeasureRetry.setStatus('current')
cipslaAutoGroupADDestIPAgeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536)).clone(3600)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupADDestIPAgeout.setStatus('current')
cipslaAutoGroupStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 12), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupStorageType.setStatus('current')
cipslaAutoGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 1, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupRowStatus.setStatus('current')
cipslaAutoGroupDestTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 2), )
if mibBuilder.loadTexts: cipslaAutoGroupDestTable.setStatus('current')
cipslaAutoGroupDestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 2, 1), ).setIndexNames((0, "CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupDestName"), (0, "CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupDestIpAddrType"), (0, "CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupDestIpAddr"), (0, "CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupDestPort"))
if mibBuilder.loadTexts: cipslaAutoGroupDestEntry.setStatus('current')
cipslaAutoGroupDestName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: cipslaAutoGroupDestName.setStatus('current')
cipslaAutoGroupDestIpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 2, 1, 2), InetAddressType())
if mibBuilder.loadTexts: cipslaAutoGroupDestIpAddrType.setStatus('current')
cipslaAutoGroupDestIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 2, 1, 3), InetAddress())
if mibBuilder.loadTexts: cipslaAutoGroupDestIpAddr.setStatus('current')
cipslaAutoGroupDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 2, 1, 4), InetPortNumber())
if mibBuilder.loadTexts: cipslaAutoGroupDestPort.setStatus('current')
cipslaAutoGroupDestStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 2, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupDestStorageType.setStatus('current')
cipslaAutoGroupDestRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupDestRowStatus.setStatus('current')
cipslaReactTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3), )
if mibBuilder.loadTexts: cipslaReactTable.setStatus('current')
cipslaReactEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1), ).setIndexNames((0, "CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupOperType"), (0, "CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactConfigIndex"), (0, "CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupOperTemplateName"))
if mibBuilder.loadTexts: cipslaReactEntry.setStatus('current')
cipslaReactConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: cipslaReactConfigIndex.setStatus('current')
cipslaReactVar = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 2), IpSlaReactVar()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaReactVar.setStatus('current')
cipslaReactThresholdType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("never", 1), ("immediate", 2), ("consecutive", 3), ("xOfy", 4), ("average", 5))).clone('never')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaReactThresholdType.setStatus('current')
cipslaReactActionType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("notificationOnly", 2))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaReactActionType.setStatus('current')
cipslaReactThresholdRising = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaReactThresholdRising.setStatus('current')
cipslaReactThresholdFalling = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 6), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaReactThresholdFalling.setStatus('current')
cipslaReactThresholdCountX = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaReactThresholdCountX.setStatus('current')
cipslaReactThresholdCountY = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaReactThresholdCountY.setStatus('current')
cipslaReactStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 9), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaReactStorageType.setStatus('current')
cipslaReactRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 3, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaReactRowStatus.setStatus('current')
cipslaAutoGroupSchedTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4), )
if mibBuilder.loadTexts: cipslaAutoGroupSchedTable.setStatus('current')
cipslaAutoGroupSchedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1), ).setIndexNames((0, "CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedId"))
if mibBuilder.loadTexts: cipslaAutoGroupSchedEntry.setStatus('current')
cipslaAutoGroupSchedId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: cipslaAutoGroupSchedId.setStatus('current')
cipslaAutoGroupSchedPeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(100, 99000)).clone(1000)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupSchedPeriod.setStatus('current')
cipslaAutoGroupSchedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 604800)).clone(60)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupSchedInterval.setStatus('current')
cipslaAutoGroupSchedLife = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(3600)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupSchedLife.setStatus('current')
cipslaAutoGroupSchedAgeout = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2073600)).clone(3600)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupSchedAgeout.setStatus('current')
cipslaAutoGroupSchedMaxInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 604800))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupSchedMaxInterval.setStatus('current')
cipslaAutoGroupSchedMinInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 604800))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupSchedMinInterval.setStatus('current')
cipslaAutoGroupSchedStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 604800)).clone(1)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupSchedStartTime.setStatus('current')
cipslaAutoGroupSchedStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 9), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupSchedStorageType.setStatus('current')
cipslaAutoGroupSchedRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 633, 1, 4, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cipslaAutoGroupSchedRowStatus.setStatus('current')
ciscoIpSlaAutoMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 633, 2))
ciscoIpSlaAutoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 633, 2, 1))
ciscoIpSlaAutoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 633, 2, 2))
ciscoIpSlaAutoMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 633, 2, 1, 1)).setObjects(("CISCO-IPSLA-AUTOMEASURE-MIB", "ciscoIpSlaAutoGroupConfGroup"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "ciscoIpSlaAutoGroupDestGroup"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "ciscoIpSlaAutoGroupReactGroup"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "ciscoIpSlaAutoGroupSchedGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpSlaAutoMIBCompliance = ciscoIpSlaAutoMIBCompliance.setStatus('current')
ciscoIpSlaAutoGroupConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 633, 2, 2, 1)).setObjects(("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupDescription"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupDestinationName"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupADDestPort"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupOperTemplateName"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedulerId"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupQoSEnable"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupOperType"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupDestIPADEnable"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupADMeasureRetry"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupADDestIPAgeout"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupStorageType"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpSlaAutoGroupConfGroup = ciscoIpSlaAutoGroupConfGroup.setStatus('current')
ciscoIpSlaAutoGroupDestGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 633, 2, 2, 2)).setObjects(("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupDestStorageType"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupDestRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpSlaAutoGroupDestGroup = ciscoIpSlaAutoGroupDestGroup.setStatus('current')
ciscoIpSlaAutoGroupReactGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 633, 2, 2, 3)).setObjects(("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactVar"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactThresholdType"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactActionType"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactThresholdRising"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactThresholdFalling"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactThresholdCountX"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactThresholdCountY"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactStorageType"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaReactRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpSlaAutoGroupReactGroup = ciscoIpSlaAutoGroupReactGroup.setStatus('current')
ciscoIpSlaAutoGroupSchedGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 633, 2, 2, 4)).setObjects(("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedPeriod"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedInterval"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedLife"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedAgeout"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedMaxInterval"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedMinInterval"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedStartTime"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedStorageType"), ("CISCO-IPSLA-AUTOMEASURE-MIB", "cipslaAutoGroupSchedRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpSlaAutoGroupSchedGroup = ciscoIpSlaAutoGroupSchedGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IPSLA-AUTOMEASURE-MIB", cipslaAutoGroupSchedRowStatus=cipslaAutoGroupSchedRowStatus, cipslaAutoGroupDescription=cipslaAutoGroupDescription, cipslaAutoGroupEntry=cipslaAutoGroupEntry, ciscoIpSlaAutoMIBCompliances=ciscoIpSlaAutoMIBCompliances, cipslaAutoGroupOperType=cipslaAutoGroupOperType, cipslaAutoGroupTable=cipslaAutoGroupTable, cipslaAutoGroupSchedId=cipslaAutoGroupSchedId, cipslaAutoGroupDestRowStatus=cipslaAutoGroupDestRowStatus, cipslaAutoGroupSchedulerId=cipslaAutoGroupSchedulerId, cipslaAutoGroupSchedPeriod=cipslaAutoGroupSchedPeriod, cipslaAutoGroupSchedAgeout=cipslaAutoGroupSchedAgeout, cipslaReactVar=cipslaReactVar, cipslaAutoGroupDestStorageType=cipslaAutoGroupDestStorageType, cipslaReactThresholdCountY=cipslaReactThresholdCountY, cipslaAutoGroupSchedTable=cipslaAutoGroupSchedTable, cipslaAutoGroupDestIpAddr=cipslaAutoGroupDestIpAddr, cipslaAutoGroupADDestIPAgeout=cipslaAutoGroupADDestIPAgeout, PYSNMP_MODULE_ID=ciscoIpSlaAutoMIB, cipslaAutoGroupDestEntry=cipslaAutoGroupDestEntry, ciscoIpSlaAutoGroupConfGroup=ciscoIpSlaAutoGroupConfGroup, cipslaAutoGroupSchedStorageType=cipslaAutoGroupSchedStorageType, cipslaReactActionType=cipslaReactActionType, cipslaReactThresholdRising=cipslaReactThresholdRising, cipslaAutoGroupSchedInterval=cipslaAutoGroupSchedInterval, cipslaAutoGroupDestTable=cipslaAutoGroupDestTable, ciscoIpSlaAutoMIBConform=ciscoIpSlaAutoMIBConform, cipslaAutoGroupDestPort=cipslaAutoGroupDestPort, cipslaAutoGroupDestIPADEnable=cipslaAutoGroupDestIPADEnable, cipslaReactRowStatus=cipslaReactRowStatus, ciscoIpSlaAutoGroupReactGroup=ciscoIpSlaAutoGroupReactGroup, cipslaAutoGroupSchedMinInterval=cipslaAutoGroupSchedMinInterval, ciscoIpSlaAutoGroupSchedGroup=ciscoIpSlaAutoGroupSchedGroup, cipslaReactEntry=cipslaReactEntry, cipslaAutoGroupQoSEnable=cipslaAutoGroupQoSEnable, cipslaReactThresholdCountX=cipslaReactThresholdCountX, cipslaAutoGroupSchedEntry=cipslaAutoGroupSchedEntry, cipslaReactTable=cipslaReactTable, cipslaAutoGroupSchedMaxInterval=cipslaAutoGroupSchedMaxInterval, ciscoIpSlaAutoMIB=ciscoIpSlaAutoMIB, cipslaAutoGroupSchedStartTime=cipslaAutoGroupSchedStartTime, ciscoIpSlaAutoMIBGroups=ciscoIpSlaAutoMIBGroups, cipslaAutoGroupStorageType=cipslaAutoGroupStorageType, cipslaAutoGroupADDestPort=cipslaAutoGroupADDestPort, cipslaAutoGroupRowStatus=cipslaAutoGroupRowStatus, cipslaAutoGroupDestName=cipslaAutoGroupDestName, cipslaReactThresholdFalling=cipslaReactThresholdFalling, cipslaAutoGroupName=cipslaAutoGroupName, ciscoIpSlaAutoMIBObjects=ciscoIpSlaAutoMIBObjects, cipslaAutoGroupDestIpAddrType=cipslaAutoGroupDestIpAddrType, cipslaReactStorageType=cipslaReactStorageType, ciscoIpSlaAutoMIBNotifs=ciscoIpSlaAutoMIBNotifs, cipslaAutoGroupADMeasureRetry=cipslaAutoGroupADMeasureRetry, cipslaAutoGroupDestinationName=cipslaAutoGroupDestinationName, cipslaAutoGroupSchedLife=cipslaAutoGroupSchedLife, ciscoIpSlaAutoGroupDestGroup=ciscoIpSlaAutoGroupDestGroup, cipslaAutoGroupOperTemplateName=cipslaAutoGroupOperTemplateName, cipslaReactThresholdType=cipslaReactThresholdType, cipslaReactConfigIndex=cipslaReactConfigIndex, ciscoIpSlaAutoMIBCompliance=ciscoIpSlaAutoMIBCompliance)