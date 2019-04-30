#
# PySNMP MIB module HPN-ICF-VSI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-VSI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:28:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Unsigned32, Counter64, Gauge32, ObjectIdentity, Bits, ModuleIdentity, IpAddress, MibIdentifier, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Unsigned32", "Counter64", "Gauge32", "ObjectIdentity", "Bits", "ModuleIdentity", "IpAddress", "MibIdentifier", "NotificationType", "iso")
MacAddress, TruthValue, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TruthValue", "TextualConvention", "RowStatus", "DisplayString")
hpnicfVsi = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105))
hpnicfVsi.setRevisions(('2009-08-08 10:00',))
if mibBuilder.loadTexts: hpnicfVsi.setLastUpdated('200908081000Z')
if mibBuilder.loadTexts: hpnicfVsi.setOrganization('')
hpnicfVsiObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1))
hpnicfVsiScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 1))
hpnicfVsiNextAvailableVsiIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVsiNextAvailableVsiIndex.setStatus('current')
hpnicfVsiL2vpnStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfVsiL2vpnStatus.setStatus('current')
hpnicfVsiTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2), )
if mibBuilder.loadTexts: hpnicfVsiTable.setStatus('current')
hpnicfVsiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-VSI-MIB", "hpnicfVsiIndex"))
if mibBuilder.loadTexts: hpnicfVsiEntry.setStatus('current')
hpnicfVsiIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfVsiIndex.setStatus('current')
hpnicfVsiName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVsiName.setStatus('current')
hpnicfVsiMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("default", 0), ("martini", 1), ("minm", 2), ("martiniAndMinm", 3), ("kompella", 4), ("kompellaAndMinm", 5), ("minmpxp", 6), ("martiniAndMinmpxp", 7), ("kompellaAndMinmpxp", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVsiMode.setStatus('current')
hpnicfMinmIsid = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfMinmIsid.setStatus('current')
hpnicfVsiId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVsiId.setStatus('current')
hpnicfVsiTransMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vlan", 1), ("ethernet", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVsiTransMode.setStatus('current')
hpnicfVsiEnableHubSpoke = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVsiEnableHubSpoke.setStatus('current')
hpnicfVsiAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("adminUp", 1), ("adminDown", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVsiAdminState.setStatus('current')
hpnicfVsiRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVsiRowStatus.setStatus('current')
hpnicfVsiSpbIsid = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVsiSpbIsid.setStatus('current')
hpnicfVsiVxlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVsiVxlanID.setStatus('current')
hpnicfVsiArpSuppression = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 12), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVsiArpSuppression.setStatus('current')
hpnicfVsiFlooding = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 13), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVsiFlooding.setStatus('current')
hpnicfVsiLocalMacCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVsiLocalMacCount.setStatus('current')
hpnicfVsiXconnectTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 3), )
if mibBuilder.loadTexts: hpnicfVsiXconnectTable.setStatus('current')
hpnicfVsiXconnectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 3, 1), ).setIndexNames((0, "HPN-ICF-VSI-MIB", "hpnicfVsiXconnectIfIndex"), (0, "HPN-ICF-VSI-MIB", "hpnicfVsiXconnectEvcSrvInstId"))
if mibBuilder.loadTexts: hpnicfVsiXconnectEntry.setStatus('current')
hpnicfVsiXconnectIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfVsiXconnectIfIndex.setStatus('current')
hpnicfVsiXconnectEvcSrvInstId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: hpnicfVsiXconnectEvcSrvInstId.setStatus('current')
hpnicfVsiXconnectVsiName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVsiXconnectVsiName.setStatus('current')
hpnicfVsiXconnectAccessMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vlan", 1), ("ethernet", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVsiXconnectAccessMode.setStatus('current')
hpnicfVsiXconnectHubSpoke = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("hub", 2), ("spoke", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVsiXconnectHubSpoke.setStatus('current')
hpnicfVsiXconnectRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVsiXconnectRowStatus.setStatus('current')
hpnicfVsiPwBindTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 4), )
if mibBuilder.loadTexts: hpnicfVsiPwBindTable.setStatus('current')
hpnicfVsiPwBindEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 4, 1), ).setIndexNames((0, "HPN-ICF-VSI-MIB", "hpnicfVsiIndex"), (0, "HPN-ICF-VSI-MIB", "hpnicfVsiPwIndex"))
if mibBuilder.loadTexts: hpnicfVsiPwBindEntry.setStatus('current')
hpnicfVsiPwIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpnicfVsiPwIndex.setStatus('current')
hpnicfVsiPwBindAttributes = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 4, 1, 2), Bits().clone(namedValues=NamedValues(("noSplitHorizon", 0), ("hub", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVsiPwBindAttributes.setStatus('current')
hpnicfVsiPwBindRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 4, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVsiPwBindRowStatus.setStatus('current')
hpnicfVsiFloodMacTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 5), )
if mibBuilder.loadTexts: hpnicfVsiFloodMacTable.setStatus('current')
hpnicfVsiFloodMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 5, 1), ).setIndexNames((0, "HPN-ICF-VSI-MIB", "hpnicfVsiIndex"), (0, "HPN-ICF-VSI-MIB", "hpnicfVsiFloodMac"))
if mibBuilder.loadTexts: hpnicfVsiFloodMacEntry.setStatus('current')
hpnicfVsiFloodMac = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 5, 1, 1), MacAddress())
if mibBuilder.loadTexts: hpnicfVsiFloodMac.setStatus('current')
hpnicfVsiFloodMacRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 5, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVsiFloodMacRowStatus.setStatus('current')
hpnicfVsiLocalMacTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 6), )
if mibBuilder.loadTexts: hpnicfVsiLocalMacTable.setStatus('current')
hpnicfVsiLocalMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 6, 1), ).setIndexNames((0, "HPN-ICF-VSI-MIB", "hpnicfVsiIndex"), (0, "HPN-ICF-VSI-MIB", "hpnicfVsiLocalMacAddr"))
if mibBuilder.loadTexts: hpnicfVsiLocalMacEntry.setStatus('current')
hpnicfVsiLocalMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 6, 1, 1), MacAddress())
if mibBuilder.loadTexts: hpnicfVsiLocalMacAddr.setStatus('current')
hpnicfVsiLocalMacIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 6, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVsiLocalMacIfIndex.setStatus('current')
hpnicfVsiLocalMacSrvID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 6, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfVsiLocalMacSrvID.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-VSI-MIB", hpnicfVsiEnableHubSpoke=hpnicfVsiEnableHubSpoke, hpnicfVsiScalarGroup=hpnicfVsiScalarGroup, hpnicfVsiPwBindEntry=hpnicfVsiPwBindEntry, hpnicfMinmIsid=hpnicfMinmIsid, hpnicfVsiXconnectEvcSrvInstId=hpnicfVsiXconnectEvcSrvInstId, hpnicfVsiVxlanID=hpnicfVsiVxlanID, hpnicfVsi=hpnicfVsi, hpnicfVsiXconnectEntry=hpnicfVsiXconnectEntry, hpnicfVsiIndex=hpnicfVsiIndex, hpnicfVsiLocalMacTable=hpnicfVsiLocalMacTable, PYSNMP_MODULE_ID=hpnicfVsi, hpnicfVsiRowStatus=hpnicfVsiRowStatus, hpnicfVsiArpSuppression=hpnicfVsiArpSuppression, hpnicfVsiObjects=hpnicfVsiObjects, hpnicfVsiXconnectTable=hpnicfVsiXconnectTable, hpnicfVsiXconnectIfIndex=hpnicfVsiXconnectIfIndex, hpnicfVsiFloodMacEntry=hpnicfVsiFloodMacEntry, hpnicfVsiLocalMacCount=hpnicfVsiLocalMacCount, hpnicfVsiMode=hpnicfVsiMode, hpnicfVsiXconnectAccessMode=hpnicfVsiXconnectAccessMode, hpnicfVsiPwBindAttributes=hpnicfVsiPwBindAttributes, hpnicfVsiPwBindRowStatus=hpnicfVsiPwBindRowStatus, hpnicfVsiNextAvailableVsiIndex=hpnicfVsiNextAvailableVsiIndex, hpnicfVsiXconnectHubSpoke=hpnicfVsiXconnectHubSpoke, hpnicfVsiLocalMacEntry=hpnicfVsiLocalMacEntry, hpnicfVsiFlooding=hpnicfVsiFlooding, hpnicfVsiPwBindTable=hpnicfVsiPwBindTable, hpnicfVsiAdminState=hpnicfVsiAdminState, hpnicfVsiName=hpnicfVsiName, hpnicfVsiPwIndex=hpnicfVsiPwIndex, hpnicfVsiEntry=hpnicfVsiEntry, hpnicfVsiId=hpnicfVsiId, hpnicfVsiXconnectVsiName=hpnicfVsiXconnectVsiName, hpnicfVsiTable=hpnicfVsiTable, hpnicfVsiLocalMacIfIndex=hpnicfVsiLocalMacIfIndex, hpnicfVsiFloodMac=hpnicfVsiFloodMac, hpnicfVsiTransMode=hpnicfVsiTransMode, hpnicfVsiL2vpnStatus=hpnicfVsiL2vpnStatus, hpnicfVsiLocalMacAddr=hpnicfVsiLocalMacAddr, hpnicfVsiLocalMacSrvID=hpnicfVsiLocalMacSrvID, hpnicfVsiFloodMacTable=hpnicfVsiFloodMacTable, hpnicfVsiFloodMacRowStatus=hpnicfVsiFloodMacRowStatus, hpnicfVsiXconnectRowStatus=hpnicfVsiXconnectRowStatus, hpnicfVsiSpbIsid=hpnicfVsiSpbIsid)