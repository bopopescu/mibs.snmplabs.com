#
# PySNMP MIB module MPOA-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MPOA-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:14:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
Boolean, extensions = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "Boolean", "extensions")
mpcIndex, = mibBuilder.importSymbols("MPOA-MIB", "mpcIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Integer32, NotificationType, Gauge32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, iso, TimeTicks, Counter64, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "NotificationType", "Gauge32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "iso", "TimeTicks", "Counter64", "ObjectIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC-v1", "RowStatus", "TruthValue")
cnMpoaExt = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 3, 7))
cnMpcConfigTable = MibTable((1, 3, 6, 1, 4, 1, 930, 3, 7, 2), )
if mibBuilder.loadTexts: cnMpcConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnMpcConfigTable.setDescription('The MPOA Bay Networks proprietary Client Configuration Table. This table contains configuration information for all MPOA Clients which this agent manages.')
cnMpcConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 3, 7, 2, 1), ).setIndexNames((0, "MPOA-MIB", "mpcIndex"))
if mibBuilder.loadTexts: cnMpcConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnMpcConfigEntry.setDescription('MPOA Client Bay Networks Configuration Entry. Each entry contains configuration information for one MPOA Client.')
cnMpcShareControlVccs = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 7, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnMpcShareControlVccs.setStatus('mandatory')
if mibBuilder.loadTexts: cnMpcShareControlVccs.setDescription('This Parameter enables VCC sharing for MPOA Control VCCs if set to true. LLC encapsulation is always signaled, regardless of sharing.')
cnMpcShareDataVccs = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 7, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnMpcShareDataVccs.setStatus('mandatory')
if mibBuilder.loadTexts: cnMpcShareDataVccs.setDescription('This parameter enables VCC sharing for MPOA Data VCCs if set to true. LLC encapsulation is always signaled, regardless of sharing.')
cnMpcValidEntryCheckInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 7, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnMpcValidEntryCheckInterval.setStatus('mandatory')
if mibBuilder.loadTexts: cnMpcValidEntryCheckInterval.setDescription('This parameter specifies the interval in seconds, to check LOCAL IP FDB entries in the Valid state for minimum activity.')
cnMpcMinFlowPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 7, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnMpcMinFlowPacketCount.setStatus('mandatory')
if mibBuilder.loadTexts: cnMpcMinFlowPacketCount.setDescription('This parameter specifies the minimum number of packets to be forwarded by a Local FDB Entry in the Valid state in cnMpcValidEntryCheckInterval to maintain minimum activity level. If minimum activity is not maintained, the entry is deleted.')
cnMpoaIpVerification = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 3, 7, 3))
cnMpoaIpVerificationTableType = MibScalar((1, 3, 6, 1, 4, 1, 930, 3, 7, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("exclusion", 2), ("inclusion", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnMpoaIpVerificationTableType.setStatus('mandatory')
if mibBuilder.loadTexts: cnMpoaIpVerificationTableType.setDescription('This object controls the type of verification table that is being used. This object is used in combination with the status and download object and the IP verification table. Any change made to this object must be downloaded to the switch cards using the cnMpoaIpVerificationTableDownload object before the settings actually take effect. To enable a verification table, the table type must be set to exclusion or inclusion, enabled using the table status object and then downloaded to the cards using the download object. To delete the IP verification information, you must set the table status object to clear and then downloaded to the cards using the download object. When the information is deleted, the table type is read as unknown. To change the table type between exclusion and inclusion, you must first delete the IP verification information and then recreate it.')
cnMpoaIpVerificationTableStatus = MibScalar((1, 3, 6, 1, 4, 1, 930, 3, 7, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2), ("clear", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnMpoaIpVerificationTableStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cnMpoaIpVerificationTableStatus.setDescription('This object is used to enable, disable or clear the IP Verification information. Any change to this object information must be downloaded to the switch cards using the cnMpoaIpVerificationTableDownload object. An empty IP verification table will yield disable on a get.')
cnMpoaIpVerificationTableDownload = MibScalar((1, 3, 6, 1, 4, 1, 930, 3, 7, 3, 3), Boolean()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnMpoaIpVerificationTableDownload.setStatus('mandatory')
if mibBuilder.loadTexts: cnMpoaIpVerificationTableDownload.setDescription('Setting this object to true(1) causes the MPOA IP Verification Table information to be downloaded to all of the cards in the switch that support MPOA Clients (MPCs). You must download the IP Verification Table information to the cards before it will become effective when you are dynamically configuring this feature. The IP Verification Table is automatically downloaded to the MPC configured cards at card initialization. When read, this object always returns false(2).')
cnMpoaIpVerificationTable = MibTable((1, 3, 6, 1, 4, 1, 930, 3, 7, 3, 4), )
if mibBuilder.loadTexts: cnMpoaIpVerificationTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnMpoaIpVerificationTable.setDescription('The MPC IP Verification Table is either an inclusion or exclusion list as indicated by the cnMpoaIpVerificationTableType object. Any change to this table must be downloaded to the switch cards using the cnMpoaIpVerificationTableDownload object.')
cnMpoaIpVerificationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 3, 7, 3, 4, 1), ).setIndexNames((0, "MPOA-EXT-MIB", "cnMpoaIpVerificationAddress"), (0, "MPOA-EXT-MIB", "cnMpoaIpVerificationMask"))
if mibBuilder.loadTexts: cnMpoaIpVerificationEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnMpoaIpVerificationEntry.setDescription('Each row of the cnMpoaIpVerificationTable consists of an IP address and IP mask that is used to identify a range of addresses that are included or excluded when creating MPOA IP shortcuts. This cnMpoaIpVerificationStatus object is used to control adding or deleting each row.')
cnMpoaIpVerificationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 7, 3, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnMpoaIpVerificationAddress.setStatus('mandatory')
if mibBuilder.loadTexts: cnMpoaIpVerificationAddress.setDescription('This object is one of the two keys used to access the cnMpoaIpVerificationTable entries. This object contains an IP address used in conjunction with the cnMpoaIpVerificationMask to identify a range of one or more IP addresses.')
cnMpoaIpVerificationMask = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 7, 3, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnMpoaIpVerificationMask.setStatus('mandatory')
if mibBuilder.loadTexts: cnMpoaIpVerificationMask.setDescription('This object is one of the two keys used to access the cnMpoaIpVerificationTable entries. This object contains an IP mask used in conjunction with the cnMpoaIpVerificationAddress to identify a range of one or more IP addresses.')
cnMpoaIpVerificationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 3, 7, 3, 4, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cnMpoaIpVerificationStatus.setStatus('mandatory')
if mibBuilder.loadTexts: cnMpoaIpVerificationStatus.setDescription('Use this object to add or delete rows in the cnMpoaIpVerificationTable. To create new rows, use createAndGo(4) or createAndWait(5). To delete entries use destroy(6). A valid row will have the status of active(1) on a get.')
mibBuilder.exportSymbols("MPOA-EXT-MIB", cnMpoaIpVerificationMask=cnMpoaIpVerificationMask, cnMpoaIpVerificationTable=cnMpoaIpVerificationTable, cnMpoaIpVerificationAddress=cnMpoaIpVerificationAddress, cnMpcShareDataVccs=cnMpcShareDataVccs, cnMpcConfigTable=cnMpcConfigTable, cnMpcValidEntryCheckInterval=cnMpcValidEntryCheckInterval, cnMpoaIpVerification=cnMpoaIpVerification, cnMpoaIpVerificationTableType=cnMpoaIpVerificationTableType, cnMpoaIpVerificationTableStatus=cnMpoaIpVerificationTableStatus, cnMpcMinFlowPacketCount=cnMpcMinFlowPacketCount, cnMpcConfigEntry=cnMpcConfigEntry, cnMpcShareControlVccs=cnMpcShareControlVccs, cnMpoaExt=cnMpoaExt, cnMpoaIpVerificationEntry=cnMpoaIpVerificationEntry, cnMpoaIpVerificationStatus=cnMpoaIpVerificationStatus, cnMpoaIpVerificationTableDownload=cnMpoaIpVerificationTableDownload)