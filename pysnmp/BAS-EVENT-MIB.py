#
# PySNMP MIB module BAS-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAS-EVENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:17:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
basExtEvent, = mibBuilder.importSymbols("BAS-MIB", "basExtEvent")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Unsigned32, IpAddress, Counter32, TimeTicks, MibIdentifier, ModuleIdentity, Gauge32, Bits, Integer32, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter32", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Gauge32", "Bits", "Integer32", "NotificationType", "iso")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
basEventMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3493, 2, 8, 1))
if mibBuilder.loadTexts: basEventMib.setLastUpdated('9811171430Z')
if mibBuilder.loadTexts: basEventMib.setOrganization('Broadband Access Systems, Inc.')
basEvent = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1))
basTrapRecipientTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 1), )
if mibBuilder.loadTexts: basTrapRecipientTable.setStatus('current')
basTrapRecipientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 1, 1), ).setIndexNames((0, "BAS-EVENT-MIB", "basTrapRecipientIndex"))
if mibBuilder.loadTexts: basTrapRecipientEntry.setStatus('current')
basTrapRecipientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basTrapRecipientIndex.setStatus('current')
basTrapRecipientIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basTrapRecipientIpAddr.setStatus('current')
basTrapRecipientUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basTrapRecipientUdpPort.setStatus('current')
basTrapRecipientCommName = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basTrapRecipientCommName.setStatus('current')
basTrapRecipientRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basTrapRecipientRowStatus.setStatus('current')
basTrapRecipientSnmpVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basTrapRecipientSnmpVersion.setStatus('current')
basTrapNotificationTable = MibTable((1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 2), )
if mibBuilder.loadTexts: basTrapNotificationTable.setStatus('current')
basTrapNotificationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 2, 1), ).setIndexNames((0, "BAS-EVENT-MIB", "basTrapNotificationId"), (0, "BAS-EVENT-MIB", "basTrapNotificationIndex"))
if mibBuilder.loadTexts: basTrapNotificationEntry.setStatus('current')
basTrapNotificationId = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 2, 1, 1), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: basTrapNotificationId.setStatus('current')
basTrapNotificationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: basTrapNotificationIndex.setStatus('current')
basTrapNotificationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3493, 2, 8, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: basTrapNotificationRowStatus.setStatus('current')
mibBuilder.exportSymbols("BAS-EVENT-MIB", basTrapRecipientSnmpVersion=basTrapRecipientSnmpVersion, basEvent=basEvent, basTrapRecipientRowStatus=basTrapRecipientRowStatus, basTrapNotificationEntry=basTrapNotificationEntry, basTrapRecipientEntry=basTrapRecipientEntry, basTrapRecipientTable=basTrapRecipientTable, basTrapNotificationIndex=basTrapNotificationIndex, basEventMib=basEventMib, basTrapNotificationRowStatus=basTrapNotificationRowStatus, basTrapRecipientIpAddr=basTrapRecipientIpAddr, basTrapRecipientIndex=basTrapRecipientIndex, basTrapRecipientUdpPort=basTrapRecipientUdpPort, PYSNMP_MODULE_ID=basEventMib, basTrapNotificationTable=basTrapNotificationTable, basTrapRecipientCommName=basTrapRecipientCommName, basTrapNotificationId=basTrapNotificationId)