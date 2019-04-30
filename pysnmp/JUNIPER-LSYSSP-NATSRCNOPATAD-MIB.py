#
# PySNMP MIB module JUNIPER-LSYSSP-NATSRCNOPATAD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-LSYSSP-NATSRCNOPATAD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:49:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
jnxLsysSpNATsrcnopatad, = mibBuilder.importSymbols("JUNIPER-LSYS-SECURITYPROFILE-MIB", "jnxLsysSpNATsrcnopatad")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Bits, iso, ObjectIdentity, MibIdentifier, Integer32, TimeTicks, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Bits", "iso", "ObjectIdentity", "MibIdentifier", "Integer32", "TimeTicks", "Counter64", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxLsysSpNATsrcnopatadMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1))
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadMIB.setLastUpdated('201005191644Z')
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadMIB.setOrganization('Juniper Networks, Inc.')
jnxLsysSpNATsrcnopatadObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1))
jnxLsysSpNATsrcnopatadSummary = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2))
jnxLsysSpNATsrcnopatadTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1), )
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadTable.setStatus('current')
jnxLsysSpNATsrcnopatadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1), ).setIndexNames((1, "JUNIPER-LSYSSP-NATSRCNOPATAD-MIB", "jnxLsysSpNATsrcnopatadLsysName"))
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadEntry.setStatus('current')
jnxLsysSpNATsrcnopatadLsysName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadLsysName.setStatus('current')
jnxLsysSpNATsrcnopatadProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadProfileName.setStatus('current')
jnxLsysSpNATsrcnopatadUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadUsage.setStatus('current')
jnxLsysSpNATsrcnopatadReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadReserved.setStatus('current')
jnxLsysSpNATsrcnopatadMaximum = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadMaximum.setStatus('current')
jnxLsysSpNATsrcnopatadUsedAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadUsedAmount.setStatus('current')
jnxLsysSpNATsrcnopatadMaxQuota = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadMaxQuota.setStatus('current')
jnxLsysSpNATsrcnopatadAvailableAmount = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadAvailableAmount.setStatus('current')
jnxLsysSpNATsrcnopatadHeaviestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadHeaviestUsage.setStatus('current')
jnxLsysSpNATsrcnopatadHeaviestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadHeaviestUser.setStatus('current')
jnxLsysSpNATsrcnopatadLightestUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadLightestUsage.setStatus('current')
jnxLsysSpNATsrcnopatadLightestUser = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 17, 11, 1, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxLsysSpNATsrcnopatadLightestUser.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-LSYSSP-NATSRCNOPATAD-MIB", PYSNMP_MODULE_ID=jnxLsysSpNATsrcnopatadMIB, jnxLsysSpNATsrcnopatadTable=jnxLsysSpNATsrcnopatadTable, jnxLsysSpNATsrcnopatadReserved=jnxLsysSpNATsrcnopatadReserved, jnxLsysSpNATsrcnopatadEntry=jnxLsysSpNATsrcnopatadEntry, jnxLsysSpNATsrcnopatadObjects=jnxLsysSpNATsrcnopatadObjects, jnxLsysSpNATsrcnopatadSummary=jnxLsysSpNATsrcnopatadSummary, jnxLsysSpNATsrcnopatadProfileName=jnxLsysSpNATsrcnopatadProfileName, jnxLsysSpNATsrcnopatadHeaviestUsage=jnxLsysSpNATsrcnopatadHeaviestUsage, jnxLsysSpNATsrcnopatadAvailableAmount=jnxLsysSpNATsrcnopatadAvailableAmount, jnxLsysSpNATsrcnopatadHeaviestUser=jnxLsysSpNATsrcnopatadHeaviestUser, jnxLsysSpNATsrcnopatadMaxQuota=jnxLsysSpNATsrcnopatadMaxQuota, jnxLsysSpNATsrcnopatadLightestUsage=jnxLsysSpNATsrcnopatadLightestUsage, jnxLsysSpNATsrcnopatadUsage=jnxLsysSpNATsrcnopatadUsage, jnxLsysSpNATsrcnopatadMaximum=jnxLsysSpNATsrcnopatadMaximum, jnxLsysSpNATsrcnopatadUsedAmount=jnxLsysSpNATsrcnopatadUsedAmount, jnxLsysSpNATsrcnopatadLightestUser=jnxLsysSpNATsrcnopatadLightestUser, jnxLsysSpNATsrcnopatadLsysName=jnxLsysSpNATsrcnopatadLsysName, jnxLsysSpNATsrcnopatadMIB=jnxLsysSpNATsrcnopatadMIB)