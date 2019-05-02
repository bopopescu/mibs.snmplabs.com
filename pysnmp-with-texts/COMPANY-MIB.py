#
# PySNMP MIB module COMPANY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/COMPANY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:26:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, TimeTicks, Counter64, IpAddress, MibIdentifier, Counter32, Gauge32, NotificationType, ObjectIdentity, enterprises, Unsigned32, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "TimeTicks", "Counter64", "IpAddress", "MibIdentifier", "Counter32", "Gauge32", "NotificationType", "ObjectIdentity", "enterprises", "Unsigned32", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
allotCom = ModuleIdentity((1, 3, 6, 1, 4, 1, 2603))
if mibBuilder.loadTexts: allotCom.setLastUpdated('0103120000Z')
if mibBuilder.loadTexts: allotCom.setOrganization('Allot Communications')
if mibBuilder.loadTexts: allotCom.setContactInfo('Allot Communications postal: 5 Hanagar St. Industrial Zone Neve Neeman Hod Hasharon 45800 Israel phone: +972-(0)9-761-9200 fax: +972-(0)9-744-3626 email: support@allot.com')
if mibBuilder.loadTexts: allotCom.setDescription('This file defines the private Allot SNMP MIB extensions.')
neTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2603, 2))
nePrimaryActive = NotificationType((1, 3, 6, 1, 4, 1, 2603, 2, 11))
if mibBuilder.loadTexts: nePrimaryActive.setStatus('current')
if mibBuilder.loadTexts: nePrimaryActive.setDescription('This trap is sent when the primary NE changes to Active mode')
nePrimaryBypass = NotificationType((1, 3, 6, 1, 4, 1, 2603, 2, 12))
if mibBuilder.loadTexts: nePrimaryBypass.setStatus('current')
if mibBuilder.loadTexts: nePrimaryBypass.setDescription('This trap is sent when the primary NE changes to Bypass mode')
neSecondaryActive = NotificationType((1, 3, 6, 1, 4, 1, 2603, 2, 13))
if mibBuilder.loadTexts: neSecondaryActive.setStatus('current')
if mibBuilder.loadTexts: neSecondaryActive.setDescription('This trap is sent when the secondary NE changes to Active mode')
neSecondaryStandBy = NotificationType((1, 3, 6, 1, 4, 1, 2603, 2, 14))
if mibBuilder.loadTexts: neSecondaryStandBy.setStatus('current')
if mibBuilder.loadTexts: neSecondaryStandBy.setDescription('This trap is sent when the secondary NE changes to StandBy mode')
neSecondaryBypass = NotificationType((1, 3, 6, 1, 4, 1, 2603, 2, 15))
if mibBuilder.loadTexts: neSecondaryBypass.setStatus('current')
if mibBuilder.loadTexts: neSecondaryBypass.setDescription('This trap is sent when the secondary NE changes to Bypass mode')
collTableOverFlow = NotificationType((1, 3, 6, 1, 4, 1, 2603, 2, 21))
if mibBuilder.loadTexts: collTableOverFlow.setStatus('current')
if mibBuilder.loadTexts: collTableOverFlow.setDescription('This trap is sent when acounting is not reading from the collector which causes the collector table to exceeds limits')
neAlertEvent = NotificationType((1, 3, 6, 1, 4, 1, 2603, 2, 22))
if mibBuilder.loadTexts: neAlertEvent.setStatus('current')
if mibBuilder.loadTexts: neAlertEvent.setDescription('This trap is sent when user defined event occurs')
neNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2603, 3)).setObjects(("COMPANY-MIB", "nePrimaryActive"), ("COMPANY-MIB", "nePrimaryBypass"), ("COMPANY-MIB", "neSecondaryActive"), ("COMPANY-MIB", "neSecondaryStandBy"), ("COMPANY-MIB", "neSecondaryBypass"), ("COMPANY-MIB", "collTableOverFlow"), ("COMPANY-MIB", "neAlertEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    neNotificationsGroup = neNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: neNotificationsGroup.setDescription('The notifications which indicate specific changes of the NE state.')
mibBuilder.exportSymbols("COMPANY-MIB", nePrimaryBypass=nePrimaryBypass, nePrimaryActive=nePrimaryActive, neSecondaryBypass=neSecondaryBypass, PYSNMP_MODULE_ID=allotCom, neSecondaryActive=neSecondaryActive, allotCom=allotCom, collTableOverFlow=collTableOverFlow, neNotificationsGroup=neNotificationsGroup, neTraps=neTraps, neSecondaryStandBy=neSecondaryStandBy, neAlertEvent=neAlertEvent)