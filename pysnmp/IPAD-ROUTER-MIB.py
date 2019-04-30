#
# PySNMP MIB module IPAD-ROUTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPAD-ROUTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:44:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Gauge32, Bits, IpAddress, ObjectIdentity, Counter32, NotificationType, iso, MibIdentifier, TimeTicks, ModuleIdentity, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Bits", "IpAddress", "ObjectIdentity", "Counter32", "NotificationType", "iso", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
verilink = MibIdentifier((1, 3, 6, 1, 4, 1, 321))
hbu = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100))
ipad = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1))
ipadFrPort = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 1))
ipadService = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 2))
ipadChannel = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 3))
ipadDLCI = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 4))
ipadEndpoint = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 5))
ipadUser = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 6))
ipadPPP = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 7))
ipadModem = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 8))
ipadSvcAware = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 9))
ipadPktSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 10))
ipadTrapDest = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 11))
ipadMisc = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 12))
ipadRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 13))
ipadCircuitParms = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1))
ipadRIPParms = MibIdentifier((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2))
ipadCircuitTable = MibTable((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1), )
if mibBuilder.loadTexts: ipadCircuitTable.setStatus('optional')
ipadCircuitTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1), ).setIndexNames((0, "IPAD-ROUTER-MIB", "ipadCircuitIndex"))
if mibBuilder.loadTexts: ipadCircuitTableEntry.setStatus('mandatory')
ipadCircuitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadCircuitIndex.setStatus('mandatory')
ipadCircuitEndpoint = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitEndpoint.setStatus('mandatory')
ipadCircuitIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitIpAddress.setStatus('mandatory')
ipadCircuitIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitIpMask.setStatus('mandatory')
ipadCircuitMaxTransmitUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitMaxTransmitUnit.setStatus('mandatory')
ipadCircuitCost = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitCost.setStatus('mandatory')
ipadCircuitEnableRIP = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitEnableRIP.setStatus('mandatory')
ipadCircuitEnableOSPF = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitEnableOSPF.setStatus('mandatory')
ipadCircuitEnableMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitEnableMulticast.setStatus('mandatory')
ipadCircuitAdd = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("addnew", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitAdd.setStatus('mandatory')
ipadCircuitDelete = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadCircuitDelete.setStatus('mandatory')
ipadRIPEnable = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPEnable.setStatus('mandatory')
ipadRIPTrustNeighbors = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPTrustNeighbors.setStatus('mandatory')
ipadRIPInterval = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPInterval.setStatus('mandatory')
ipadRIPDomain = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPDomain.setStatus('mandatory')
ipadRIPStaticARPTable = MibTable((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5), )
if mibBuilder.loadTexts: ipadRIPStaticARPTable.setStatus('optional')
ipadRIPStaticARPTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1), ).setIndexNames((0, "IPAD-ROUTER-MIB", "ipadRIPStaticARPIndex"))
if mibBuilder.loadTexts: ipadRIPStaticARPTableEntry.setStatus('mandatory')
ipadRIPStaticARPIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadRIPStaticARPIndex.setStatus('mandatory')
ipadRIPStaticARPEndpoint = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticARPEndpoint.setStatus('mandatory')
ipadRIPStaticARPIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticARPIpAddress.setStatus('mandatory')
ipadRIPStaticARPMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticARPMacAddress.setStatus('mandatory')
ipadRIPStaticARPDLCIAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticARPDLCIAddress.setStatus('mandatory')
ipadRIPStaticARPEnableARP = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticARPEnableARP.setStatus('mandatory')
ipadRIPStaticARPAdd = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("addnew", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticARPAdd.setStatus('mandatory')
ipadRIPStaticARPDelete = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticARPDelete.setStatus('mandatory')
ipadRIPStaticRouteTable = MibTable((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8), )
if mibBuilder.loadTexts: ipadRIPStaticRouteTable.setStatus('optional')
ipadRIPStaticRouteTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1), ).setIndexNames((0, "IPAD-ROUTER-MIB", "ipadRIPStaticRouteIndex"))
if mibBuilder.loadTexts: ipadRIPStaticRouteTableEntry.setStatus('mandatory')
ipadRIPStaticRouteIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadRIPStaticRouteIndex.setStatus('mandatory')
ipadRIPStaticRouteEndpoint = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticRouteEndpoint.setStatus('mandatory')
ipadRIPStaticRouteTargetIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticRouteTargetIpAddress.setStatus('mandatory')
ipadRIPStaticRouteTargetIpMask = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticRouteTargetIpMask.setStatus('mandatory')
ipadRIPStaticRouteNextHopIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticRouteNextHopIpAddress.setStatus('mandatory')
ipadRIPStaticRouteCost = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticRouteCost.setStatus('mandatory')
ipadRIPStaticRouteEnableRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticRouteEnableRouter.setStatus('mandatory')
ipadRIPStaticRouteAdd = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("addnew", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticRouteAdd.setStatus('mandatory')
ipadRIPStaticRouteDelete = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPStaticRouteDelete.setStatus('mandatory')
ipadRIPNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 11), )
if mibBuilder.loadTexts: ipadRIPNeighborTable.setStatus('optional')
ipadRIPNeighborTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 11, 1), ).setIndexNames((0, "IPAD-ROUTER-MIB", "ipadRIPNeighborIndex"))
if mibBuilder.loadTexts: ipadRIPNeighborTableEntry.setStatus('mandatory')
ipadRIPNeighborIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 11, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadRIPNeighborIndex.setStatus('mandatory')
ipadRIPNeighborAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 11, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipadRIPNeighborAddress.setStatus('mandatory')
ipadRIPNeighborAdd = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPNeighborAdd.setStatus('mandatory')
ipadRIPNeighborDelete = MibScalar((1, 3, 6, 1, 4, 1, 321, 100, 1, 13, 2, 13), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipadRIPNeighborDelete.setStatus('mandatory')
mibBuilder.exportSymbols("IPAD-ROUTER-MIB", ipadRIPStaticRouteTable=ipadRIPStaticRouteTable, ipadRIPStaticRouteTargetIpMask=ipadRIPStaticRouteTargetIpMask, ipadRouter=ipadRouter, ipadEndpoint=ipadEndpoint, ipadChannel=ipadChannel, ipadTrapDest=ipadTrapDest, ipadRIPStaticRouteIndex=ipadRIPStaticRouteIndex, ipadCircuitEnableMulticast=ipadCircuitEnableMulticast, ipadModem=ipadModem, ipadRIPStaticARPTable=ipadRIPStaticARPTable, ipadCircuitParms=ipadCircuitParms, ipadRIPInterval=ipadRIPInterval, ipadRIPStaticRouteCost=ipadRIPStaticRouteCost, ipadPktSwitch=ipadPktSwitch, ipadRIPNeighborAddress=ipadRIPNeighborAddress, ipadPPP=ipadPPP, ipadCircuitIndex=ipadCircuitIndex, ipadCircuitAdd=ipadCircuitAdd, ipadRIPStaticARPDelete=ipadRIPStaticARPDelete, ipadCircuitEnableRIP=ipadCircuitEnableRIP, ipadRIPStaticRouteEndpoint=ipadRIPStaticRouteEndpoint, ipadRIPStaticARPTableEntry=ipadRIPStaticARPTableEntry, ipadRIPStaticARPIndex=ipadRIPStaticARPIndex, ipadRIPStaticARPAdd=ipadRIPStaticARPAdd, hbu=hbu, ipadCircuitMaxTransmitUnit=ipadCircuitMaxTransmitUnit, ipadRIPStaticRouteTargetIpAddress=ipadRIPStaticRouteTargetIpAddress, ipadRIPNeighborTable=ipadRIPNeighborTable, ipadRIPStaticRouteNextHopIpAddress=ipadRIPStaticRouteNextHopIpAddress, ipadService=ipadService, ipadFrPort=ipadFrPort, ipadRIPEnable=ipadRIPEnable, ipadRIPDomain=ipadRIPDomain, ipadCircuitIpMask=ipadCircuitIpMask, ipad=ipad, ipadRIPStaticARPIpAddress=ipadRIPStaticARPIpAddress, ipadCircuitTable=ipadCircuitTable, ipadCircuitDelete=ipadCircuitDelete, ipadRIPNeighborIndex=ipadRIPNeighborIndex, ipadRIPStaticRouteEnableRouter=ipadRIPStaticRouteEnableRouter, ipadRIPStaticARPEnableARP=ipadRIPStaticARPEnableARP, ipadCircuitCost=ipadCircuitCost, ipadRIPStaticARPDLCIAddress=ipadRIPStaticARPDLCIAddress, ipadRIPNeighborAdd=ipadRIPNeighborAdd, ipadDLCI=ipadDLCI, verilink=verilink, ipadCircuitEndpoint=ipadCircuitEndpoint, ipadCircuitIpAddress=ipadCircuitIpAddress, ipadMisc=ipadMisc, ipadRIPStaticRouteTableEntry=ipadRIPStaticRouteTableEntry, ipadCircuitTableEntry=ipadCircuitTableEntry, ipadRIPTrustNeighbors=ipadRIPTrustNeighbors, ipadRIPNeighborTableEntry=ipadRIPNeighborTableEntry, ipadCircuitEnableOSPF=ipadCircuitEnableOSPF, ipadRIPStaticRouteDelete=ipadRIPStaticRouteDelete, ipadRIPStaticARPEndpoint=ipadRIPStaticARPEndpoint, ipadRIPStaticRouteAdd=ipadRIPStaticRouteAdd, ipadSvcAware=ipadSvcAware, ipadRIPNeighborDelete=ipadRIPNeighborDelete, ipadRIPStaticARPMacAddress=ipadRIPStaticARPMacAddress, ipadUser=ipadUser, ipadRIPParms=ipadRIPParms)