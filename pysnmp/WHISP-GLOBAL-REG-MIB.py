#
# PySNMP MIB module WHISP-GLOBAL-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WHISP-GLOBAL-REG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:09:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, TimeTicks, Gauge32, MibIdentifier, ObjectIdentity, enterprises, iso, IpAddress, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "TimeTicks", "Gauge32", "MibIdentifier", "ObjectIdentity", "enterprises", "iso", "IpAddress", "NotificationType", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
whispGlobalRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 161, 19, 1, 1, 1))
if mibBuilder.loadTexts: whispGlobalRegModule.setLastUpdated('200304100000Z')
if mibBuilder.loadTexts: whispGlobalRegModule.setOrganization('Motorola')
mot = MibIdentifier((1, 3, 6, 1, 4, 1, 161))
whispRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19))
whispReg = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 1))
whispGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 2))
whispProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3))
whispAps = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 1))
whispSm = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 2))
whispBox = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 3))
whispCMM = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 4))
whispPlv = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 5))
whispCMM4 = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 6))
whispPlvModem = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 7))
whispPlvGateway = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 8))
whispPlvRepeater = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 9))
whispPlvBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 3, 10))
whispModules = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 1, 1))
canopySnmpAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 250))
ucos = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 250, 256))
prizmSnmpAgent = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 1250))
prizm = MibIdentifier((1, 3, 6, 1, 4, 1, 161, 19, 1000))
mibBuilder.exportSymbols("WHISP-GLOBAL-REG-MIB", whispCMM4=whispCMM4, PYSNMP_MODULE_ID=whispGlobalRegModule, prizmSnmpAgent=prizmSnmpAgent, whispGeneric=whispGeneric, whispSm=whispSm, whispRoot=whispRoot, whispCMM=whispCMM, canopySnmpAgent=canopySnmpAgent, whispAps=whispAps, prizm=prizm, whispReg=whispReg, whispModules=whispModules, whispPlv=whispPlv, mot=mot, whispPlvRepeater=whispPlvRepeater, whispGlobalRegModule=whispGlobalRegModule, whispProducts=whispProducts, whispPlvGateway=whispPlvGateway, whispBox=whispBox, whispPlvModem=whispPlvModem, ucos=ucos, whispPlvBridge=whispPlvBridge)