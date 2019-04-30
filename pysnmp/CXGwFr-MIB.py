#
# PySNMP MIB module CXGwFr-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXGwFr-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:17:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
SapIndex, Alias, cxGwFr = mibBuilder.importSymbols("CXProduct-SMI", "SapIndex", "Alias", "cxGwFr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, MibIdentifier, iso, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, ModuleIdentity, Gauge32, Unsigned32, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "MibIdentifier", "iso", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "ModuleIdentity", "Gauge32", "Unsigned32", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gffSapTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1), )
if mibBuilder.loadTexts: gffSapTable.setStatus('mandatory')
gffSapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1), ).setIndexNames((0, "CXGwFr-MIB", "gffSapId"))
if mibBuilder.loadTexts: gffSapEntry.setStatus('mandatory')
gffSapId = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gffSapId.setStatus('mandatory')
gffSapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gffSapRowStatus.setStatus('mandatory')
gffSapType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lower", 1), ("upper", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gffSapType.setStatus('mandatory')
gffSapAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1, 4), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gffSapAlias.setStatus('mandatory')
gffSapCompanionAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1, 5), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gffSapCompanionAlias.setStatus('mandatory')
gffSapAssociatedSlotNo = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gffSapAssociatedSlotNo.setStatus('mandatory')
gffSapWindowWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(40, 100)).clone(40)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gffSapWindowWidth.setStatus('mandatory')
gffSapTrafficPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gffSapTrafficPriority.setStatus('mandatory')
gffSapMaxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 8192)).clone(4096)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gffSapMaxFrameSize.setStatus('mandatory')
mibBuilder.exportSymbols("CXGwFr-MIB", gffSapMaxFrameSize=gffSapMaxFrameSize, gffSapType=gffSapType, gffSapAlias=gffSapAlias, gffSapEntry=gffSapEntry, gffSapTable=gffSapTable, gffSapTrafficPriority=gffSapTrafficPriority, gffSapRowStatus=gffSapRowStatus, gffSapWindowWidth=gffSapWindowWidth, gffSapId=gffSapId, gffSapCompanionAlias=gffSapCompanionAlias, gffSapAssociatedSlotNo=gffSapAssociatedSlotNo)