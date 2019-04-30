#
# PySNMP MIB module DLMS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLMS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:36:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter32, Unsigned32, Gauge32, IpAddress, Integer32, ModuleIdentity, MibIdentifier, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "Unsigned32", "Gauge32", "IpAddress", "Integer32", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
swDlmsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 101))
if mibBuilder.loadTexts: swDlmsMIB.setLastUpdated('201108100000Z')
if mibBuilder.loadTexts: swDlmsMIB.setOrganization('D-Link Corporation')
swDlmsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 101, 0))
swDlmsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 101, 1))
swDlmsGeneralGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 1))
swDlmsLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 2))
swDlmsStackLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3))
swDlmsInstallAc = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDlmsInstallAc.setStatus('current')
swDlmsInstallStackUnitId = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swDlmsInstallStackUnitId.setStatus('current')
swDlmsLicenseModelTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 2, 1), )
if mibBuilder.loadTexts: swDlmsLicenseModelTable.setStatus('current')
swDlmsLicenseModelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 2, 1, 1), ).setIndexNames((0, "DLMS-MIB", "swDlmsLicenseModelName"))
if mibBuilder.loadTexts: swDlmsLicenseModelEntry.setStatus('current')
swDlmsLicenseModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 2, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDlmsLicenseModelName.setStatus('current')
swDlmsLicenseModelRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDlmsLicenseModelRemaining.setStatus('current')
swDlmsLicenseAcTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 2, 2), )
if mibBuilder.loadTexts: swDlmsLicenseAcTable.setStatus('current')
swDlmsLicenseAcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 2, 2, 1), ).setIndexNames((0, "DLMS-MIB", "swDlmsLicenseModelName"), (0, "DLMS-MIB", "swDlmsLicenseAc"))
if mibBuilder.loadTexts: swDlmsLicenseAcEntry.setStatus('current')
swDlmsLicenseAc = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 2, 2, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDlmsLicenseAc.setStatus('current')
swDlmsLicenseAcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("expired", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDlmsLicenseAcStatus.setStatus('current')
swDlmsStackLicenseModelTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3, 1), )
if mibBuilder.loadTexts: swDlmsStackLicenseModelTable.setStatus('current')
swDlmsStackLicenseModelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3, 1, 1), ).setIndexNames((0, "DLMS-MIB", "swDlmsStackLicenseModelUnitId"), (0, "DLMS-MIB", "swDlmsStackLicenseModelName"))
if mibBuilder.loadTexts: swDlmsStackLicenseModelEntry.setStatus('current')
swDlmsStackLicenseModelUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDlmsStackLicenseModelUnitId.setStatus('current')
swDlmsStackLicenseModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDlmsStackLicenseModelName.setStatus('current')
swDlmsStackLicenseModelRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDlmsStackLicenseModelRemaining.setStatus('current')
swDlmsStackLicenseAcTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3, 2), )
if mibBuilder.loadTexts: swDlmsStackLicenseAcTable.setStatus('current')
swDlmsStackLicenseAcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3, 2, 1), ).setIndexNames((0, "DLMS-MIB", "swDlmsStackLicenseModelUnitId"), (0, "DLMS-MIB", "swDlmsStackLicenseModelName"), (0, "DLMS-MIB", "swDlmsStackLicenseAc"))
if mibBuilder.loadTexts: swDlmsStackLicenseAcEntry.setStatus('current')
swDlmsStackLicenseAc = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3, 2, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDlmsStackLicenseAc.setStatus('current')
swDlmsStackLicenseAcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 101, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("expired", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swDlmsStackLicenseAcStatus.setStatus('current')
swDlmsIllegalAc = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 101, 0, 1)).setObjects(("DLMS-MIB", "swDlmsInstallAc"))
if mibBuilder.loadTexts: swDlmsIllegalAc.setStatus('current')
swDlmsLicenseExpired = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 101, 0, 2)).setObjects(("DLMS-MIB", "swDlmsLicenseModelName"), ("DLMS-MIB", "swDlmsLicenseAc"))
if mibBuilder.loadTexts: swDlmsLicenseExpired.setStatus('current')
swDlmsLicenseInstallationSuccess = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 101, 0, 3)).setObjects(("DLMS-MIB", "swDlmsLicenseModelName"), ("DLMS-MIB", "swDlmsInstallAc"))
if mibBuilder.loadTexts: swDlmsLicenseInstallationSuccess.setStatus('current')
swDlmsLicenseExpiresIn30Days = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 101, 0, 4)).setObjects(("DLMS-MIB", "swDlmsLicenseModelName"), ("DLMS-MIB", "swDlmsInstallAc"))
if mibBuilder.loadTexts: swDlmsLicenseExpiresIn30Days.setStatus('current')
swDlmsStackLicenseExpired = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 101, 0, 21)).setObjects(("DLMS-MIB", "swDlmsStackLicenseModelUnitId"), ("DLMS-MIB", "swDlmsStackLicenseModelName"), ("DLMS-MIB", "swDlmsStackLicenseAc"))
if mibBuilder.loadTexts: swDlmsStackLicenseExpired.setStatus('current')
swDlmsStackLicenseInstallationSuccess = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 101, 0, 22)).setObjects(("DLMS-MIB", "swDlmsStackLicenseModelUnitId"), ("DLMS-MIB", "swDlmsStackLicenseModelName"), ("DLMS-MIB", "swDlmsInstallAc"))
if mibBuilder.loadTexts: swDlmsStackLicenseInstallationSuccess.setStatus('current')
swDlmsStackLicenseExpiresIn30Days = NotificationType((1, 3, 6, 1, 4, 1, 171, 12, 101, 0, 23)).setObjects(("DLMS-MIB", "swDlmsStackLicenseModelUnitId"), ("DLMS-MIB", "swDlmsStackLicenseModelName"), ("DLMS-MIB", "swDlmsInstallAc"))
if mibBuilder.loadTexts: swDlmsStackLicenseExpiresIn30Days.setStatus('current')
mibBuilder.exportSymbols("DLMS-MIB", swDlmsInstallAc=swDlmsInstallAc, swDlmsLicenseAcEntry=swDlmsLicenseAcEntry, swDlmsLicenseModelName=swDlmsLicenseModelName, swDlmsStackLicenseAcEntry=swDlmsStackLicenseAcEntry, swDlmsStackLicenseModelEntry=swDlmsStackLicenseModelEntry, PYSNMP_MODULE_ID=swDlmsMIB, swDlmsStackLicenseModelTable=swDlmsStackLicenseModelTable, swDlmsStackLicenseInstallationSuccess=swDlmsStackLicenseInstallationSuccess, swDlmsGeneralGroup=swDlmsGeneralGroup, swDlmsMIB=swDlmsMIB, swDlmsStackLicense=swDlmsStackLicense, swDlmsStackLicenseExpiresIn30Days=swDlmsStackLicenseExpiresIn30Days, swDlmsLicense=swDlmsLicense, swDlmsStackLicenseAcStatus=swDlmsStackLicenseAcStatus, swDlmsStackLicenseAcTable=swDlmsStackLicenseAcTable, swDlmsLicenseAcTable=swDlmsLicenseAcTable, swDlmsNotifications=swDlmsNotifications, swDlmsLicenseAc=swDlmsLicenseAc, swDlmsStackLicenseModelUnitId=swDlmsStackLicenseModelUnitId, swDlmsStackLicenseModelRemaining=swDlmsStackLicenseModelRemaining, swDlmsObjects=swDlmsObjects, swDlmsLicenseModelTable=swDlmsLicenseModelTable, swDlmsLicenseExpiresIn30Days=swDlmsLicenseExpiresIn30Days, swDlmsLicenseInstallationSuccess=swDlmsLicenseInstallationSuccess, swDlmsStackLicenseModelName=swDlmsStackLicenseModelName, swDlmsInstallStackUnitId=swDlmsInstallStackUnitId, swDlmsStackLicenseExpired=swDlmsStackLicenseExpired, swDlmsIllegalAc=swDlmsIllegalAc, swDlmsLicenseModelRemaining=swDlmsLicenseModelRemaining, swDlmsLicenseExpired=swDlmsLicenseExpired, swDlmsStackLicenseAc=swDlmsStackLicenseAc, swDlmsLicenseModelEntry=swDlmsLicenseModelEntry, swDlmsLicenseAcStatus=swDlmsLicenseAcStatus)