#
# PySNMP MIB module FOUNDRY-SN-IPX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FOUNDRY-SN-IPX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:01:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
snIpx, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "snIpx")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, iso, Counter32, Bits, Unsigned32, Counter64, ObjectIdentity, Gauge32, MibIdentifier, NotificationType, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "iso", "Counter32", "Bits", "Unsigned32", "Counter64", "ObjectIdentity", "Gauge32", "MibIdentifier", "NotificationType", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class RtrStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class ClearStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("normal", 0), ("clear", 1))

class PortIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 3900)

class Action(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("deny", 0), ("permit", 1))

class PhysAddress(OctetString):
    pass

class NetNumber(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

snIpxGen = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1))
snIpxCache = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 2))
snIpxRoute = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 3))
snIpxServer = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4))
snIpxFwdFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5))
snIpxRipFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 6))
snIpxSapFilter = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 7))
snIpxIfFwdAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 8))
snIpxIfRipAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 9))
snIpxIfSapAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 10))
snIpxPortAddr = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 11))
snIpxPortCounters = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12))
snIpxRoutingMode = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 1), RtrStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxRoutingMode.setStatus('mandatory')
snIpxNetBiosFilterMode = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 2), RtrStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxNetBiosFilterMode.setStatus('mandatory')
snIpxClearCache = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 3), ClearStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxClearCache.setStatus('mandatory')
snIpxClearRoute = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 4), ClearStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxClearRoute.setStatus('mandatory')
snIpxClearTrafficCnts = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 5), ClearStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxClearTrafficCnts.setStatus('mandatory')
snIpxRcvPktsCnt = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxRcvPktsCnt.setStatus('mandatory')
snIpxTxPktsCnt = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxTxPktsCnt.setStatus('mandatory')
snIpxFwdPktsCnt = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxFwdPktsCnt.setStatus('mandatory')
snIpxRcvDropPktsCnt = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxRcvDropPktsCnt.setStatus('mandatory')
snIpxRcvFiltPktsCnt = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxRcvFiltPktsCnt.setStatus('mandatory')
snIpxRipGblFiltList = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxRipGblFiltList.setStatus('mandatory')
snIpxRipFiltOnAllPort = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("valid", 1), ("deleteAllInBound", 2), ("deleteAllOutBound", 3), ("addAllInBound", 4), ("addAllOutBound", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxRipFiltOnAllPort.setStatus('mandatory')
snIpxSapGblFiltList = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxSapGblFiltList.setStatus('mandatory')
snIpxSapFiltOnAllPort = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("valid", 1), ("deleteAllInBound", 2), ("deleteAllOutBound", 3), ("addAllInBound", 4), ("addAllOutBound", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxSapFiltOnAllPort.setStatus('mandatory')
snIpxTxDropPktsCnt = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxTxDropPktsCnt.setStatus('mandatory')
snIpxTxFiltPktsCnt = MibScalar((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxTxFiltPktsCnt.setStatus('mandatory')
snIpxCacheTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 2, 1), )
if mibBuilder.loadTexts: snIpxCacheTable.setStatus('mandatory')
snIpxCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 2, 1, 1), ).setIndexNames((0, "FOUNDRY-SN-IPX-MIB", "snIpxCacheIndex"))
if mibBuilder.loadTexts: snIpxCacheEntry.setStatus('mandatory')
snIpxCacheIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxCacheIndex.setStatus('mandatory')
snIpxCacheNetNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 2, 1, 1, 2), NetNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxCacheNetNum.setStatus('mandatory')
snIpxCacheNode = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 2, 1, 1, 3), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxCacheNode.setStatus('mandatory')
snIpxCacheOutFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 2, 1, 1, 4), RtrStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxCacheOutFilter.setStatus('mandatory')
snIpxCacheEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ethernetII", 1), ("ethernet8022", 2), ("ethernet8023", 3), ("ethernetSnap", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxCacheEncap.setStatus('mandatory')
snIpxCachePort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 2, 1, 1, 6), PortIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxCachePort.setStatus('mandatory')
snIpxRouteTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 3, 1), )
if mibBuilder.loadTexts: snIpxRouteTable.setStatus('mandatory')
snIpxRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 3, 1, 1), ).setIndexNames((0, "FOUNDRY-SN-IPX-MIB", "snIpxRouteIndex"))
if mibBuilder.loadTexts: snIpxRouteEntry.setStatus('mandatory')
snIpxRouteIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxRouteIndex.setStatus('mandatory')
snIpxDestNetNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 3, 1, 1, 2), NetNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxDestNetNum.setStatus('mandatory')
snIpxFwdRouterNode = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 3, 1, 1, 3), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxFwdRouterNode.setStatus('mandatory')
snIpxDestHopCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxDestHopCnts.setStatus('mandatory')
snIpxRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxRouteMetric.setStatus('mandatory')
snIpxDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 3, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxDestPort.setStatus('mandatory')
snIpxServerTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4, 1), )
if mibBuilder.loadTexts: snIpxServerTable.setStatus('mandatory')
snIpxServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4, 1, 1), ).setIndexNames((0, "FOUNDRY-SN-IPX-MIB", "snIpxServerIndex"))
if mibBuilder.loadTexts: snIpxServerEntry.setStatus('mandatory')
snIpxServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxServerIndex.setStatus('mandatory')
snIpxServerType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxServerType.setStatus('mandatory')
snIpxServerNetNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4, 1, 1, 3), NetNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxServerNetNum.setStatus('mandatory')
snIpxServerNode = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4, 1, 1, 4), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxServerNode.setStatus('mandatory')
snIpxServerSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxServerSocket.setStatus('mandatory')
snIpxServerHopCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxServerHopCnts.setStatus('mandatory')
snIpxServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 4, 1, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 47))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxServerName.setStatus('mandatory')
snIpxFwdFilterTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1), )
if mibBuilder.loadTexts: snIpxFwdFilterTable.setStatus('mandatory')
snIpxFwdFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1, 1), ).setIndexNames((0, "FOUNDRY-SN-IPX-MIB", "snIpxFwdFilterId"))
if mibBuilder.loadTexts: snIpxFwdFilterEntry.setStatus('mandatory')
snIpxFwdFilterId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxFwdFilterId.setStatus('mandatory')
snIpxFwdFilterAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1, 1, 2), Action()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxFwdFilterAction.setStatus('mandatory')
snIpxFwdFilterSocket = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxFwdFilterSocket.setStatus('mandatory')
snIpxFwdFilterSrcNet = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1, 1, 4), NetNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxFwdFilterSrcNet.setStatus('mandatory')
snIpxFwdFilterSrcNode = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1, 1, 5), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxFwdFilterSrcNode.setStatus('mandatory')
snIpxFwdFilterDestNet = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1, 1, 6), NetNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxFwdFilterDestNet.setStatus('mandatory')
snIpxFwdFilterDestNode = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1, 1, 7), PhysAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxFwdFilterDestNode.setStatus('mandatory')
snIpxFwdFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2), ("delete", 3), ("create", 4), ("modify", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxFwdFilterRowStatus.setStatus('mandatory')
snIpxRipFilterTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 6, 1), )
if mibBuilder.loadTexts: snIpxRipFilterTable.setStatus('mandatory')
snIpxRipFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 6, 1, 1), ).setIndexNames((0, "FOUNDRY-SN-IPX-MIB", "snIpxRipFilterId"))
if mibBuilder.loadTexts: snIpxRipFilterEntry.setStatus('mandatory')
snIpxRipFilterId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxRipFilterId.setStatus('mandatory')
snIpxRipFilterAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 6, 1, 1, 2), Action()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxRipFilterAction.setStatus('mandatory')
snIpxRipFilterNet = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 6, 1, 1, 3), NetNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxRipFilterNet.setStatus('mandatory')
snIpxRipFilterMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 6, 1, 1, 4), NetNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxRipFilterMask.setStatus('mandatory')
snIpxRipFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2), ("delete", 3), ("create", 4), ("modify", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxRipFilterRowStatus.setStatus('mandatory')
snIpxSapFilterTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 7, 1), )
if mibBuilder.loadTexts: snIpxSapFilterTable.setStatus('mandatory')
snIpxSapFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 7, 1, 1), ).setIndexNames((0, "FOUNDRY-SN-IPX-MIB", "snIpxSapFilterId"))
if mibBuilder.loadTexts: snIpxSapFilterEntry.setStatus('mandatory')
snIpxSapFilterId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 7, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxSapFilterId.setStatus('mandatory')
snIpxSapFilterAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 7, 1, 1, 2), Action()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxSapFilterAction.setStatus('mandatory')
snIpxSapFilterType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 7, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxSapFilterType.setStatus('mandatory')
snIpxSapFilterName = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 7, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 47))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxSapFilterName.setStatus('mandatory')
snIpxSapFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 7, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2), ("delete", 3), ("create", 4), ("modify", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxSapFilterRowStatus.setStatus('mandatory')
snIpxIfFwdAccessTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 8, 1), )
if mibBuilder.loadTexts: snIpxIfFwdAccessTable.setStatus('mandatory')
snIpxIfFwdAccessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 8, 1, 1), ).setIndexNames((0, "FOUNDRY-SN-IPX-MIB", "snIpxIfFwdAccessPort"), (0, "FOUNDRY-SN-IPX-MIB", "snIpxIfFwdAccessDir"))
if mibBuilder.loadTexts: snIpxIfFwdAccessEntry.setStatus('mandatory')
snIpxIfFwdAccessPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 8, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxIfFwdAccessPort.setStatus('mandatory')
snIpxIfFwdAccessDir = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 8, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("in", 1), ("out", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxIfFwdAccessDir.setStatus('mandatory')
snIpxIfFwdAccessFilterList = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 8, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxIfFwdAccessFilterList.setStatus('mandatory')
snIpxIfFwdAccessRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 8, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2), ("delete", 3), ("create", 4), ("modify", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxIfFwdAccessRowStatus.setStatus('mandatory')
snIpxIfRipAccessTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 9, 1), )
if mibBuilder.loadTexts: snIpxIfRipAccessTable.setStatus('mandatory')
snIpxIfRipAccessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 9, 1, 1), ).setIndexNames((0, "FOUNDRY-SN-IPX-MIB", "snIpxIfRipAccessPort"), (0, "FOUNDRY-SN-IPX-MIB", "snIpxIfRipAccessDir"))
if mibBuilder.loadTexts: snIpxIfRipAccessEntry.setStatus('mandatory')
snIpxIfRipAccessPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 9, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxIfRipAccessPort.setStatus('mandatory')
snIpxIfRipAccessDir = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("in", 1), ("out", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxIfRipAccessDir.setStatus('mandatory')
snIpxIfRipAccessFilterList = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 9, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxIfRipAccessFilterList.setStatus('mandatory')
snIpxIfRipAccessRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2), ("delete", 3), ("create", 4), ("modify", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxIfRipAccessRowStatus.setStatus('mandatory')
snIpxIfSapAccessTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 10, 1), )
if mibBuilder.loadTexts: snIpxIfSapAccessTable.setStatus('mandatory')
snIpxIfSapAccessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 10, 1, 1), ).setIndexNames((0, "FOUNDRY-SN-IPX-MIB", "snIpxIfSapAccessPort"), (0, "FOUNDRY-SN-IPX-MIB", "snIpxIfSapAccessDir"))
if mibBuilder.loadTexts: snIpxIfSapAccessEntry.setStatus('mandatory')
snIpxIfSapAccessPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 10, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxIfSapAccessPort.setStatus('mandatory')
snIpxIfSapAccessDir = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("in", 1), ("out", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxIfSapAccessDir.setStatus('mandatory')
snIpxIfSapAccessFilterList = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 10, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxIfSapAccessFilterList.setStatus('mandatory')
snIpxIfSapAccessRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2), ("delete", 3), ("create", 4), ("modify", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxIfSapAccessRowStatus.setStatus('mandatory')
snIpxPortAddrTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 11, 1), )
if mibBuilder.loadTexts: snIpxPortAddrTable.setStatus('mandatory')
snIpxPortAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 11, 1, 1), ).setIndexNames((0, "FOUNDRY-SN-IPX-MIB", "snIpxPortAddrPort"), (0, "FOUNDRY-SN-IPX-MIB", "snIpxPortAddrEncap"))
if mibBuilder.loadTexts: snIpxPortAddrEntry.setStatus('mandatory')
snIpxPortAddrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 11, 1, 1, 1), PortIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxPortAddrPort.setStatus('mandatory')
snIpxPortAddrEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 11, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ethernet8022", 1), ("ethernet8023", 2), ("ethernetII", 3), ("ethernetSnap", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxPortAddrEncap.setStatus('mandatory')
snIpxPortAddrNetNum = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 11, 1, 1, 3), NetNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxPortAddrNetNum.setStatus('mandatory')
snIpxPortAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 11, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2), ("delete", 3), ("create", 4), ("modify", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxPortAddrRowStatus.setStatus('mandatory')
snIpxPortAddrNetBiosFilterMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 11, 1, 1, 5), RtrStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snIpxPortAddrNetBiosFilterMode.setStatus('mandatory')
snIpxPortCountersTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1), )
if mibBuilder.loadTexts: snIpxPortCountersTable.setStatus('mandatory')
snIpxPortCountersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1), ).setIndexNames((0, "FOUNDRY-SN-IPX-MIB", "snIpxPortCountersPort"))
if mibBuilder.loadTexts: snIpxPortCountersEntry.setStatus('mandatory')
snIpxPortCountersPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1, 1), PortIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxPortCountersPort.setStatus('mandatory')
snIpxPortCountersRcvPktsCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxPortCountersRcvPktsCnt.setStatus('mandatory')
snIpxPortCountersTxPktsCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxPortCountersTxPktsCnt.setStatus('mandatory')
snIpxPortCountersFwdPktsCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxPortCountersFwdPktsCnt.setStatus('mandatory')
snIpxPortCountersRcvDropPktsCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxPortCountersRcvDropPktsCnt.setStatus('mandatory')
snIpxPortCountersTxDropPktsCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxPortCountersTxDropPktsCnt.setStatus('mandatory')
snIpxPortCountersRcvFiltPktsCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxPortCountersRcvFiltPktsCnt.setStatus('mandatory')
snIpxPortCountersTxFiltPktsCnt = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 1, 12, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snIpxPortCountersTxFiltPktsCnt.setStatus('mandatory')
mibBuilder.exportSymbols("FOUNDRY-SN-IPX-MIB", snIpxFwdFilterAction=snIpxFwdFilterAction, snIpxDestNetNum=snIpxDestNetNum, snIpxIfFwdAccessRowStatus=snIpxIfFwdAccessRowStatus, snIpxIfSapAccessRowStatus=snIpxIfSapAccessRowStatus, snIpxPortCounters=snIpxPortCounters, snIpxRoutingMode=snIpxRoutingMode, snIpxRcvDropPktsCnt=snIpxRcvDropPktsCnt, snIpxRcvFiltPktsCnt=snIpxRcvFiltPktsCnt, RtrStatus=RtrStatus, snIpxFwdRouterNode=snIpxFwdRouterNode, snIpxSapFiltOnAllPort=snIpxSapFiltOnAllPort, snIpxPortCountersEntry=snIpxPortCountersEntry, snIpxPortCountersPort=snIpxPortCountersPort, PhysAddress=PhysAddress, snIpxSapFilterId=snIpxSapFilterId, snIpxPortAddr=snIpxPortAddr, snIpxIfRipAccessPort=snIpxIfRipAccessPort, snIpxSapFilter=snIpxSapFilter, snIpxIfFwdAccess=snIpxIfFwdAccess, snIpxServerType=snIpxServerType, snIpxServerTable=snIpxServerTable, snIpxPortCountersRcvDropPktsCnt=snIpxPortCountersRcvDropPktsCnt, snIpxCacheEncap=snIpxCacheEncap, snIpxPortAddrTable=snIpxPortAddrTable, snIpxRipGblFiltList=snIpxRipGblFiltList, snIpxClearCache=snIpxClearCache, snIpxServer=snIpxServer, snIpxIfFwdAccessFilterList=snIpxIfFwdAccessFilterList, snIpxCachePort=snIpxCachePort, snIpxRipFilterId=snIpxRipFilterId, snIpxServerNetNum=snIpxServerNetNum, snIpxSapFilterAction=snIpxSapFilterAction, snIpxIfFwdAccessTable=snIpxIfFwdAccessTable, snIpxDestHopCnts=snIpxDestHopCnts, snIpxIfSapAccessFilterList=snIpxIfSapAccessFilterList, snIpxIfSapAccessTable=snIpxIfSapAccessTable, snIpxCacheEntry=snIpxCacheEntry, snIpxIfRipAccessRowStatus=snIpxIfRipAccessRowStatus, snIpxServerEntry=snIpxServerEntry, snIpxRipFilterMask=snIpxRipFilterMask, snIpxIfRipAccessFilterList=snIpxIfRipAccessFilterList, snIpxRipFilterAction=snIpxRipFilterAction, snIpxPortAddrEncap=snIpxPortAddrEncap, snIpxIfFwdAccessDir=snIpxIfFwdAccessDir, snIpxPortAddrNetBiosFilterMode=snIpxPortAddrNetBiosFilterMode, snIpxIfFwdAccessEntry=snIpxIfFwdAccessEntry, snIpxFwdFilterSrcNet=snIpxFwdFilterSrcNet, snIpxCache=snIpxCache, snIpxIfSapAccessDir=snIpxIfSapAccessDir, snIpxServerSocket=snIpxServerSocket, snIpxIfSapAccessPort=snIpxIfSapAccessPort, snIpxSapGblFiltList=snIpxSapGblFiltList, snIpxFwdFilterRowStatus=snIpxFwdFilterRowStatus, snIpxCacheNode=snIpxCacheNode, snIpxCacheIndex=snIpxCacheIndex, snIpxFwdFilterId=snIpxFwdFilterId, snIpxRipFiltOnAllPort=snIpxRipFiltOnAllPort, snIpxFwdFilterEntry=snIpxFwdFilterEntry, snIpxSapFilterName=snIpxSapFilterName, snIpxPortAddrNetNum=snIpxPortAddrNetNum, snIpxPortCountersTable=snIpxPortCountersTable, snIpxNetBiosFilterMode=snIpxNetBiosFilterMode, snIpxPortCountersTxPktsCnt=snIpxPortCountersTxPktsCnt, snIpxFwdFilterSrcNode=snIpxFwdFilterSrcNode, snIpxServerName=snIpxServerName, snIpxTxFiltPktsCnt=snIpxTxFiltPktsCnt, snIpxRipFilterNet=snIpxRipFilterNet, snIpxSapFilterTable=snIpxSapFilterTable, snIpxPortCountersRcvFiltPktsCnt=snIpxPortCountersRcvFiltPktsCnt, snIpxPortCountersFwdPktsCnt=snIpxPortCountersFwdPktsCnt, snIpxSapFilterType=snIpxSapFilterType, snIpxPortCountersTxFiltPktsCnt=snIpxPortCountersTxFiltPktsCnt, snIpxPortCountersTxDropPktsCnt=snIpxPortCountersTxDropPktsCnt, PortIndex=PortIndex, snIpxRouteTable=snIpxRouteTable, snIpxIfRipAccessEntry=snIpxIfRipAccessEntry, snIpxRipFilterEntry=snIpxRipFilterEntry, snIpxServerNode=snIpxServerNode, snIpxRipFilter=snIpxRipFilter, snIpxPortCountersRcvPktsCnt=snIpxPortCountersRcvPktsCnt, snIpxFwdFilterDestNode=snIpxFwdFilterDestNode, snIpxTxPktsCnt=snIpxTxPktsCnt, snIpxCacheOutFilter=snIpxCacheOutFilter, snIpxGen=snIpxGen, snIpxRouteEntry=snIpxRouteEntry, snIpxFwdFilter=snIpxFwdFilter, snIpxRcvPktsCnt=snIpxRcvPktsCnt, snIpxCacheNetNum=snIpxCacheNetNum, snIpxIfRipAccessDir=snIpxIfRipAccessDir, snIpxPortAddrRowStatus=snIpxPortAddrRowStatus, snIpxRouteMetric=snIpxRouteMetric, snIpxFwdFilterDestNet=snIpxFwdFilterDestNet, snIpxFwdFilterSocket=snIpxFwdFilterSocket, snIpxServerHopCnts=snIpxServerHopCnts, snIpxClearRoute=snIpxClearRoute, snIpxRouteIndex=snIpxRouteIndex, Action=Action, snIpxDestPort=snIpxDestPort, snIpxIfSapAccess=snIpxIfSapAccess, snIpxFwdFilterTable=snIpxFwdFilterTable, snIpxIfFwdAccessPort=snIpxIfFwdAccessPort, snIpxSapFilterRowStatus=snIpxSapFilterRowStatus, snIpxIfSapAccessEntry=snIpxIfSapAccessEntry, snIpxFwdPktsCnt=snIpxFwdPktsCnt, NetNumber=NetNumber, snIpxTxDropPktsCnt=snIpxTxDropPktsCnt, ClearStatus=ClearStatus, snIpxRoute=snIpxRoute, snIpxIfRipAccess=snIpxIfRipAccess, snIpxPortAddrEntry=snIpxPortAddrEntry, snIpxRipFilterTable=snIpxRipFilterTable, snIpxRipFilterRowStatus=snIpxRipFilterRowStatus, snIpxServerIndex=snIpxServerIndex, snIpxClearTrafficCnts=snIpxClearTrafficCnts, snIpxSapFilterEntry=snIpxSapFilterEntry, snIpxIfRipAccessTable=snIpxIfRipAccessTable, snIpxCacheTable=snIpxCacheTable, snIpxPortAddrPort=snIpxPortAddrPort)