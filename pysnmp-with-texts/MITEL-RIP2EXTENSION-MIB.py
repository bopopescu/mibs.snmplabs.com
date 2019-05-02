#
# PySNMP MIB module MITEL-RIP2EXTENSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-RIP2EXTENSION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:13:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
rip2IfConfAddress, = mibBuilder.importSymbols("RIPv2-MIB", "rip2IfConfAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Counter64, Unsigned32, MibIdentifier, Bits, ObjectIdentity, Integer32, ModuleIdentity, IpAddress, iso, Gauge32, NotificationType, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Counter64", "Unsigned32", "MibIdentifier", "Bits", "ObjectIdentity", "Integer32", "ModuleIdentity", "IpAddress", "iso", "Gauge32", "NotificationType", "enterprises")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
mitelRouterRipExtensionGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6))
mitelRouterRipExtensionGroup.setRevisions(('2003-03-24 10:36', '1999-03-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mitelRouterRipExtensionGroup.setRevisionsDescriptions(('Convert to SMIv2', 'RIP2 IfConf Extension MIB Version 1.0',))
if mibBuilder.loadTexts: mitelRouterRipExtensionGroup.setLastUpdated('200303241036Z')
if mibBuilder.loadTexts: mitelRouterRipExtensionGroup.setOrganization('MITEL Corporation')
if mibBuilder.loadTexts: mitelRouterRipExtensionGroup.setContactInfo('Standards Group, Postal: MITEL Corporation 350 Legget Drive, PO Box 13089 Kanata, Ontario Canada K2K 1X3 Tel: +1 613 592 2122 Fax: +1 613 592 4784 E-mail: std@mitel.com')
if mibBuilder.loadTexts: mitelRouterRipExtensionGroup.setDescription('The MITEL RIP2 IfConf Extension MIB module.')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelPropIpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8))
mitelIpNetRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1))
mitelRipExtGrpIfConfTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6, 1), )
if mibBuilder.loadTexts: mitelRipExtGrpIfConfTable.setStatus('current')
if mibBuilder.loadTexts: mitelRipExtGrpIfConfTable.setDescription('A table containing information about logical LAN destinations.')
mitelRipExtGrpIfConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6, 1, 1), ).setIndexNames((0, "RIPv2-MIB", "rip2IfConfAddress"))
if mibBuilder.loadTexts: mitelRipExtGrpIfConfEntry.setStatus('current')
if mibBuilder.loadTexts: mitelRipExtGrpIfConfEntry.setDescription('The entries in this table provide additional information to the Rip2IfConf table from RFC 1724.')
mitelIfConfTblSendDefaultRoutes = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mitelIfConfTblSendDefaultRoutes.setStatus('current')
if mibBuilder.loadTexts: mitelIfConfTblSendDefaultRoutes.setDescription('This entry determines whether default routes are sent with RIP information for this IP address.')
mitelIfConfTblRipType = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rip", 1), ("triggerRip", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelIfConfTblRipType.setStatus('current')
if mibBuilder.loadTexts: mitelIfConfTblRipType.setDescription('This entry determines which type of RIP to use on this IP address.')
mitelIfConfTblRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 6, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mitelIfConfTblRowStatus.setReference('Textual Conventions for Version 2 of the Simple Network Management Protocol (RFC 1443).')
if mibBuilder.loadTexts: mitelIfConfTblRowStatus.setStatus('current')
if mibBuilder.loadTexts: mitelIfConfTblRowStatus.setDescription('The current status of this entry.')
mibBuilder.exportSymbols("MITEL-RIP2EXTENSION-MIB", mitelRouterRipExtensionGroup=mitelRouterRipExtensionGroup, mitelRipExtGrpIfConfTable=mitelRipExtGrpIfConfTable, mitelIfConfTblSendDefaultRoutes=mitelIfConfTblSendDefaultRoutes, mitelRipExtGrpIfConfEntry=mitelRipExtGrpIfConfEntry, PYSNMP_MODULE_ID=mitelRouterRipExtensionGroup, mitelIfConfTblRowStatus=mitelIfConfTblRowStatus, mitelIpNetRouter=mitelIpNetRouter, mitelPropIpNetworking=mitelPropIpNetworking, mitelProprietary=mitelProprietary, mitel=mitel, mitelIfConfTblRipType=mitelIfConfTblRipType)