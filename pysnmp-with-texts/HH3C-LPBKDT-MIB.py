#
# PySNMP MIB module HH3C-LPBKDT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-LPBKDT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:27:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifDescr, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifIndex")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, Gauge32, MibIdentifier, iso, ObjectIdentity, Integer32, IpAddress, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "Gauge32", "MibIdentifier", "iso", "ObjectIdentity", "Integer32", "IpAddress", "Bits", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cLpbkdt = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 95))
hh3cLpbkdt.setRevisions(('2009-03-30 17:41', '2008-09-27 15:04',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cLpbkdt.setRevisionsDescriptions(('To fix bugs in the MIB file.', 'The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hh3cLpbkdt.setLastUpdated('200903301741Z')
if mibBuilder.loadTexts: hh3cLpbkdt.setOrganization('H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: hh3cLpbkdt.setContactInfo('Comware Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: hh3cLpbkdt.setDescription('Loops may cause broadcast storms. The purpose of loopback detection is to detect loops on the device and to protect the network.')
hh3cLpbkdtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 95, 1))
hh3cLpbkdtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 95, 2))
hh3cLpbkdtTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 95, 1, 0))
hh3cLpbkdtTrapLoopbacked = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 95, 1, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hh3cLpbkdtTrapLoopbacked.setStatus('current')
if mibBuilder.loadTexts: hh3cLpbkdtTrapLoopbacked.setDescription('Trap message is generated when the interface is looped.')
hh3cLpbkdtTrapRecovered = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 95, 1, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hh3cLpbkdtTrapRecovered.setStatus('current')
if mibBuilder.loadTexts: hh3cLpbkdtTrapRecovered.setDescription('Trap message is generated when the loops on the interface are eliminated.')
hh3cLpbkdtTrapPerVlanLoopbacked = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 95, 1, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("HH3C-LPBKDT-MIB", "hh3cLpbkdtVlanID"))
if mibBuilder.loadTexts: hh3cLpbkdtTrapPerVlanLoopbacked.setStatus('current')
if mibBuilder.loadTexts: hh3cLpbkdtTrapPerVlanLoopbacked.setDescription('Trap message is generated when the interface is looped in the VLAN.')
hh3cLpbkdtTrapPerVlanRecovered = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 95, 1, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("HH3C-LPBKDT-MIB", "hh3cLpbkdtVlanID"))
if mibBuilder.loadTexts: hh3cLpbkdtTrapPerVlanRecovered.setStatus('current')
if mibBuilder.loadTexts: hh3cLpbkdtTrapPerVlanRecovered.setDescription('Trap message is generated when the loop on the interface is eliminated in the VLAN.')
hh3cLpbkdtVlanID = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 95, 2, 1), VlanId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cLpbkdtVlanID.setStatus('current')
if mibBuilder.loadTexts: hh3cLpbkdtVlanID.setDescription('The ID of VLAN.')
mibBuilder.exportSymbols("HH3C-LPBKDT-MIB", hh3cLpbkdtNotifications=hh3cLpbkdtNotifications, hh3cLpbkdtVlanID=hh3cLpbkdtVlanID, hh3cLpbkdtTrapPrefix=hh3cLpbkdtTrapPrefix, hh3cLpbkdtTrapRecovered=hh3cLpbkdtTrapRecovered, hh3cLpbkdtObjects=hh3cLpbkdtObjects, hh3cLpbkdtTrapPerVlanLoopbacked=hh3cLpbkdtTrapPerVlanLoopbacked, hh3cLpbkdtTrapLoopbacked=hh3cLpbkdtTrapLoopbacked, hh3cLpbkdt=hh3cLpbkdt, hh3cLpbkdtTrapPerVlanRecovered=hh3cLpbkdtTrapPerVlanRecovered, PYSNMP_MODULE_ID=hh3cLpbkdt)