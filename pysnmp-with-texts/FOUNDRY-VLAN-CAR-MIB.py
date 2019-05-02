#
# PySNMP MIB module FOUNDRY-VLAN-CAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FOUNDRY-VLAN-CAR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:15:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
PacketSource, RateLimitType, RateLimitAction = mibBuilder.importSymbols("FOUNDRY-CAR-MIB", "PacketSource", "RateLimitType", "RateLimitAction")
snSwitch, = mibBuilder.importSymbols("FOUNDRY-SN-SWITCH-GROUP-MIB", "snSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, Counter64, TimeTicks, NotificationType, ObjectIdentity, ModuleIdentity, Bits, IpAddress, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "Counter64", "TimeTicks", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Bits", "IpAddress", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snVLanCAR = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17))
snVLanCAR.setRevisions(('2010-06-02 00:00', '2009-09-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snVLanCAR.setRevisionsDescriptions(('Changed the ORGANIZATION, CONTACT-INFO and DESCRIPTION fields.', 'convert from SMIv1 to SMIv2',))
if mibBuilder.loadTexts: snVLanCAR.setLastUpdated('201006020000Z')
if mibBuilder.loadTexts: snVLanCAR.setOrganization('Brocade Communications Systems, Inc.')
if mibBuilder.loadTexts: snVLanCAR.setContactInfo('Technical Support Center 130 Holger Way, San Jose, CA 95134 Email: ipsupport@brocade.com Phone: 1-800-752-8061 URL: www.brocade.com')
if mibBuilder.loadTexts: snVLanCAR.setDescription("Copyright 1996-2010 Brocade Communications Systems, Inc. All rights reserved. This Brocade Communications Systems SNMP Management Information Base Specification embodies Brocade Communications Systems' confidential and proprietary intellectual property. Brocade Communications Systems retains all title and ownership in the Specification, including any revisions. This Specification is supplied AS IS, and Brocade Communications Systems makes no warranty, either express or implied, as to the use, operation, condition, or performance of the specification, and any unintended consequence it may on the user environment.")
snVLanCARs = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1))
snVLanCARTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1), )
if mibBuilder.loadTexts: snVLanCARTable.setStatus('current')
if mibBuilder.loadTexts: snVLanCARTable.setDescription('A table of rate limit configuration entries for a vlan. Rate Limit is a method of traffic control. It allows a set of rate limits to be configured and applied to packets flowing into/out of an interface to regulate network traffic.')
snVLanCAREntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1), ).setIndexNames((0, "FOUNDRY-VLAN-CAR-MIB", "snVLanCARVLanId"), (0, "FOUNDRY-VLAN-CAR-MIB", "snVLanCARDirection"), (0, "FOUNDRY-VLAN-CAR-MIB", "snVLanCARRowIndex"))
if mibBuilder.loadTexts: snVLanCAREntry.setStatus('current')
if mibBuilder.loadTexts: snVLanCAREntry.setDescription('A collection of rate-limit configuration objects on this vlan.')
snVLanCARVLanId = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVLanCARVLanId.setStatus('current')
if mibBuilder.loadTexts: snVLanCARVLanId.setDescription('The VLAN ID as one of the indices of this table . Each VLAN ID can have a membership of multiple ports.')
snVLanCARDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 2), PacketSource()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVLanCARDirection.setStatus('current')
if mibBuilder.loadTexts: snVLanCARDirection.setDescription('The input or output transmission direction for the Rate Limit object.')
snVLanCARRowIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVLanCARRowIndex.setStatus('current')
if mibBuilder.loadTexts: snVLanCARRowIndex.setDescription('The table index for rate limit objects. It increases as the rate limit entries are added. Skips the number when a row is deleted.')
snVLanCARType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 4), RateLimitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVLanCARType.setStatus('current')
if mibBuilder.loadTexts: snVLanCARType.setDescription('The type of traffic rate-limited against.')
snVLanCARAccIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVLanCARAccIdx.setStatus('current')
if mibBuilder.loadTexts: snVLanCARAccIdx.setDescription('The index to the access list if RateLimitType is either quickAcc or standardAcc.')
snVLanCARRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVLanCARRate.setStatus('current')
if mibBuilder.loadTexts: snVLanCARRate.setDescription('The comitted access rate. This determines the long term average transmission rate. Traffic that falls under this rate always conforms. This is average rate in bits per second.')
snVLanCARLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVLanCARLimit.setStatus('current')
if mibBuilder.loadTexts: snVLanCARLimit.setDescription('This is the normal burst size that determines how large traffic bursts can be before some traffic exceeds the rate limit. This specifies the number of bytes that are guaranteed to be transported by the network at the average rate under normal conditions during committed time interval. This normal burst size is in bytes.')
snVLanCARExtLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVLanCARExtLimit.setStatus('current')
if mibBuilder.loadTexts: snVLanCARExtLimit.setDescription('This is the extended burst limit that determines how large traffic bursts can be before all the traffic exceeds the rate limit. This burst size is in bytes. ')
snVLanCARConformAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 9), RateLimitAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVLanCARConformAction.setStatus('current')
if mibBuilder.loadTexts: snVLanCARConformAction.setDescription('Action to be taken when the traffic is within the Rate Limit. drop drop the packet. xmit transmit the packet. continue continue to evaluate to the subsequent rate limits. precedXmit rewrite the IP precedence and transmit the packet. precedCont rewrite the IP precedence and allow it evaluated by subsequent rate limits.')
snVLanCARExceedAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 10), RateLimitAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVLanCARExceedAction.setStatus('current')
if mibBuilder.loadTexts: snVLanCARExceedAction.setDescription('Action to be taken when the traffic exceeds the Rate Limit. drop drop the packet. xmit transmit the packet. continue continue to evaluate to the subsequent rate limits. precedXmit rewrite the IP precedence and transmit the packet. precedCont rewrite the IP precedence and allow it evaluated by subsequent rate limits.')
snVLanCARStatSwitchedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVLanCARStatSwitchedPkts.setStatus('current')
if mibBuilder.loadTexts: snVLanCARStatSwitchedPkts.setDescription('The counter of packets permitted by this rate limit.')
snVLanCARStatSwitchedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVLanCARStatSwitchedBytes.setStatus('current')
if mibBuilder.loadTexts: snVLanCARStatSwitchedBytes.setDescription('The counter of bytes permitted by this interface.')
snVLanCARStatFilteredPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVLanCARStatFilteredPkts.setStatus('current')
if mibBuilder.loadTexts: snVLanCARStatFilteredPkts.setDescription('The counter of packets which exceeded this rate limit.')
snVLanCARStatFilteredBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVLanCARStatFilteredBytes.setStatus('current')
if mibBuilder.loadTexts: snVLanCARStatFilteredBytes.setDescription('The counter of bytes which exceeded this rate limit.')
snVLanCARStatCurBurst = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 17, 1, 1, 1, 15), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snVLanCARStatCurBurst.setStatus('current')
if mibBuilder.loadTexts: snVLanCARStatCurBurst.setDescription('The current received burst size.')
mibBuilder.exportSymbols("FOUNDRY-VLAN-CAR-MIB", snVLanCARStatSwitchedPkts=snVLanCARStatSwitchedPkts, snVLanCARRate=snVLanCARRate, snVLanCARType=snVLanCARType, snVLanCARAccIdx=snVLanCARAccIdx, PYSNMP_MODULE_ID=snVLanCAR, snVLanCARStatCurBurst=snVLanCARStatCurBurst, snVLanCARStatFilteredPkts=snVLanCARStatFilteredPkts, snVLanCARDirection=snVLanCARDirection, snVLanCAR=snVLanCAR, snVLanCARVLanId=snVLanCARVLanId, snVLanCARStatSwitchedBytes=snVLanCARStatSwitchedBytes, snVLanCARExceedAction=snVLanCARExceedAction, snVLanCARExtLimit=snVLanCARExtLimit, snVLanCARConformAction=snVLanCARConformAction, snVLanCARRowIndex=snVLanCARRowIndex, snVLanCARStatFilteredBytes=snVLanCARStatFilteredBytes, snVLanCARTable=snVLanCARTable, snVLanCAREntry=snVLanCAREntry, snVLanCARLimit=snVLanCARLimit, snVLanCARs=snVLanCARs)