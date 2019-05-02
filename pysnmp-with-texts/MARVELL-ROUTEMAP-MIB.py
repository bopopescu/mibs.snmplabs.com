#
# PySNMP MIB module MARVELL-ROUTEMAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MARVELL-ROUTEMAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:10:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
InetAddress, InetAddressIPv6, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressIPv6", "InetAddressType")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, IpAddress, Integer32, Counter64, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Gauge32, ObjectIdentity, NotificationType, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Integer32", "Counter64", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Gauge32", "ObjectIdentity", "NotificationType", "ModuleIdentity", "Counter32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
rlRouteMap = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 227))
rlRouteMap.setRevisions(('1970-01-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlRouteMap.setRevisionsDescriptions(('Added this MODULE-IDENTITY clause.',))
if mibBuilder.loadTexts: rlRouteMap.setLastUpdated('201506080000A')
if mibBuilder.loadTexts: rlRouteMap.setOrganization('Marvell Computer Communications Ltd.')
if mibBuilder.loadTexts: rlRouteMap.setContactInfo('www.Marvell.com')
if mibBuilder.loadTexts: rlRouteMap.setDescription('The private MIB module definition for Route Map distribution mechanism.')
class RlRouteMapInetType(TextualConvention, Integer32):
    description = 'The inet type of a route map'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

rlRouteMapPbrTable = MibTable((1, 3, 6, 1, 4, 1, 89, 227, 1), )
if mibBuilder.loadTexts: rlRouteMapPbrTable.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrTable.setDescription('Main table serving as container for route map table definition.')
rlRouteMapPbrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 227, 1, 1), ).setIndexNames((0, "MARVELL-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapName"), (0, "MARVELL-ROUTEMAP-MIB", "rlRouteMapPbrRouteMapSectionId"), (0, "MARVELL-ROUTEMAP-MIB", "rlRouteMapPbrInetType"))
if mibBuilder.loadTexts: rlRouteMapPbrEntry.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrEntry.setDescription('The row definition for this table.')
rlRouteMapPbrRouteMapName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: rlRouteMapPbrRouteMapName.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrRouteMapName.setDescription('Name (identifier) of the route map.')
rlRouteMapPbrRouteMapSectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: rlRouteMapPbrRouteMapSectionId.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrRouteMapSectionId.setDescription('Identifier of single section the route map.')
rlRouteMapPbrInetType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 3), RlRouteMapInetType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrInetType.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrInetType.setDescription('Inet type of this route-map.')
rlRouteMapPbrMatchAccessListName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrMatchAccessListName.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrMatchAccessListName.setDescription('Identifier of access list, if used for matching.')
rlRouteMapPbrActionNexthopInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 5), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrActionNexthopInetAddressType.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrActionNexthopInetAddressType.setDescription('The inet type of rlRouteMapPbrActionNexthopInetAddress')
rlRouteMapPbrActionNexthopInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 6), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrActionNexthopInetAddress.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrActionNexthopInetAddress.setDescription('Inet address of nexthop, if used for action.')
rlRouteMapPbrActionNexthopIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrActionNexthopIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrActionNexthopIfIndex.setDescription('Inet address of nexthop, if used for action.')
rlRouteMapPbrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 227, 1, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRouteMapPbrRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlRouteMapPbrRowStatus.setDescription('The row status of this entry.')
mibBuilder.exportSymbols("MARVELL-ROUTEMAP-MIB", rlRouteMapPbrMatchAccessListName=rlRouteMapPbrMatchAccessListName, rlRouteMapPbrActionNexthopInetAddress=rlRouteMapPbrActionNexthopInetAddress, rlRouteMapPbrActionNexthopIfIndex=rlRouteMapPbrActionNexthopIfIndex, rlRouteMap=rlRouteMap, RlRouteMapInetType=RlRouteMapInetType, rlRouteMapPbrRowStatus=rlRouteMapPbrRowStatus, rlRouteMapPbrInetType=rlRouteMapPbrInetType, PYSNMP_MODULE_ID=rlRouteMap, rlRouteMapPbrRouteMapName=rlRouteMapPbrRouteMapName, rlRouteMapPbrRouteMapSectionId=rlRouteMapPbrRouteMapSectionId, rlRouteMapPbrEntry=rlRouteMapPbrEntry, rlRouteMapPbrActionNexthopInetAddressType=rlRouteMapPbrActionNexthopInetAddressType, rlRouteMapPbrTable=rlRouteMapPbrTable)