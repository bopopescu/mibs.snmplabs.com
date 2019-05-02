#
# PySNMP MIB module NETSCREEN-RESOURCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-RESOURCE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:20:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
netscreenResource, = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenResource")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, iso, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, TimeTicks, Counter32, ObjectIdentity, Integer32, NotificationType, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "TimeTicks", "Counter32", "ObjectIdentity", "Integer32", "NotificationType", "MibIdentifier", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netscreenResourceMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 16, 0))
netscreenResourceMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-10 00:00', '2002-05-05 00:00', '2001-04-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netscreenResourceMibModule.setRevisionsDescriptions(('Modified copyright and contact information', 'Converted to SMIv2 by Longview Software', 'Correct spelling mistake', 'Remove active session', 'Creation Date',))
if mibBuilder.loadTexts: netscreenResourceMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenResourceMibModule.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: netscreenResourceMibModule.setContactInfo('Customer Support 1194 North Mathilda Avenue Sunnyvale, California 94089-1206 USA Tel: 1-800-638-8296 E-mail: customerservice@juniper.net HTTP://www.juniper.net')
if mibBuilder.loadTexts: netscreenResourceMibModule.setDescription('This module defines the object that are used to monitor resource in netscreen box')
nsResCPU = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 16, 1))
nsResCpuAvg = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResCpuAvg.setStatus('current')
if mibBuilder.loadTexts: nsResCpuAvg.setDescription('Average System CPU utilization in percentage.')
nsResCpuLast1Min = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResCpuLast1Min.setStatus('current')
if mibBuilder.loadTexts: nsResCpuLast1Min.setDescription('Last one minute CPU utilization in percentage.')
nsResCpuLast5Min = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResCpuLast5Min.setStatus('current')
if mibBuilder.loadTexts: nsResCpuLast5Min.setDescription('Last five minutes CPU utilization in percentage.')
nsResCpuLast15Min = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResCpuLast15Min.setStatus('current')
if mibBuilder.loadTexts: nsResCpuLast15Min.setDescription('Last fifteen minutes CPU utilization in percentage.')
nsResMem = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 16, 2))
nsResMemAllocate = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResMemAllocate.setStatus('current')
if mibBuilder.loadTexts: nsResMemAllocate.setDescription('Memory allocated.')
nsResMemLeft = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResMemLeft.setStatus('current')
if mibBuilder.loadTexts: nsResMemLeft.setDescription('Memory left.')
nsResMemFrag = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResMemFrag.setStatus('current')
if mibBuilder.loadTexts: nsResMemFrag.setDescription('Memory fragment.')
nsResSession = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 16, 3))
nsResSessAllocate = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 3, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResSessAllocate.setStatus('current')
if mibBuilder.loadTexts: nsResSessAllocate.setDescription('Allocate session number.')
nsResSessMaxium = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 3, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResSessMaxium.setStatus('current')
if mibBuilder.loadTexts: nsResSessMaxium.setDescription('Maxium session number system can afford.')
nsResSessFailed = MibScalar((1, 3, 6, 1, 4, 1, 3224, 16, 3, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsResSessFailed.setStatus('current')
if mibBuilder.loadTexts: nsResSessFailed.setDescription('Failed session allocation counters.')
mibBuilder.exportSymbols("NETSCREEN-RESOURCE-MIB", nsResSession=nsResSession, nsResCpuAvg=nsResCpuAvg, nsResCpuLast5Min=nsResCpuLast5Min, nsResMemFrag=nsResMemFrag, nsResSessFailed=nsResSessFailed, netscreenResourceMibModule=netscreenResourceMibModule, nsResCPU=nsResCPU, nsResMemAllocate=nsResMemAllocate, nsResCpuLast1Min=nsResCpuLast1Min, nsResSessAllocate=nsResSessAllocate, nsResCpuLast15Min=nsResCpuLast15Min, nsResMem=nsResMem, PYSNMP_MODULE_ID=netscreenResourceMibModule, nsResMemLeft=nsResMemLeft, nsResSessMaxium=nsResSessMaxium)