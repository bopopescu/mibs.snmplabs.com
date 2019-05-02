#
# PySNMP MIB module CMU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CMU-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:25:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, NotificationType, iso, Bits, ObjectIdentity, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, IpAddress, MibIdentifier, Counter64, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "NotificationType", "iso", "Bits", "ObjectIdentity", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "IpAddress", "MibIdentifier", "Counter64", "TimeTicks", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
proteon = MibIdentifier((1, 3, 6, 1, 4, 1, 1))
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
cmu = MibIdentifier((1, 3, 6, 1, 4, 1, 3))
unix = MibIdentifier((1, 3, 6, 1, 4, 1, 4))
acc = MibIdentifier((1, 3, 6, 1, 4, 1, 5))
twg = MibIdentifier((1, 3, 6, 1, 4, 1, 6))
cayman = MibIdentifier((1, 3, 6, 1, 4, 1, 7))
psi = MibIdentifier((1, 3, 6, 1, 4, 1, 8))
cisco = MibIdentifier((1, 3, 6, 1, 4, 1, 9))
nsc = MibIdentifier((1, 3, 6, 1, 4, 1, 10))
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
epilogue = MibIdentifier((1, 3, 6, 1, 4, 1, 12))
utk = MibIdentifier((1, 3, 6, 1, 4, 1, 13))
bbn = MibIdentifier((1, 3, 6, 1, 4, 1, 14))
xylogics = MibIdentifier((1, 3, 6, 1, 4, 1, 15))
timeplex = MibIdentifier((1, 3, 6, 1, 4, 1, 16))
canstar = MibIdentifier((1, 3, 6, 1, 4, 1, 17))
wellfleet = MibIdentifier((1, 3, 6, 1, 4, 1, 18))
trw = MibIdentifier((1, 3, 6, 1, 4, 1, 19))
mit = MibIdentifier((1, 3, 6, 1, 4, 1, 20))
eon = MibIdentifier((1, 3, 6, 1, 4, 1, 21))
spartacus = MibIdentifier((1, 3, 6, 1, 4, 1, 22))
excelan = MibIdentifier((1, 3, 6, 1, 4, 1, 23))
spider = MibIdentifier((1, 3, 6, 1, 4, 1, 24))
nsfnet = MibIdentifier((1, 3, 6, 1, 4, 1, 25))
hls = MibIdentifier((1, 3, 6, 1, 4, 1, 26))
xyplex = MibIdentifier((1, 3, 6, 1, 4, 1, 33))
cray = MibIdentifier((1, 3, 6, 1, 4, 1, 34))
sun = MibIdentifier((1, 3, 6, 1, 4, 1, 42))
synoptics = MibIdentifier((1, 3, 6, 1, 4, 1, 45))
dec = MibIdentifier((1, 3, 6, 1, 4, 1, 36))
tgv = MibIdentifier((1, 3, 6, 1, 4, 1, 58))
apple = MibIdentifier((1, 3, 6, 1, 4, 1, 63))
nat = MibIdentifier((1, 3, 6, 1, 4, 1, 86))
snmp_research = MibIdentifier((1, 3, 6, 1, 4, 1, 99)).setLabel("snmp-research")
ftp = MibIdentifier((1, 3, 6, 1, 4, 1, 121))
shiva = MibIdentifier((1, 3, 6, 1, 4, 1, 166))
transarc = MibIdentifier((1, 3, 6, 1, 4, 1, 257))
lexcel = MibIdentifier((1, 3, 6, 1, 4, 1, 379))
mibBuilder.exportSymbols("CMU-MIB", twg=twg, acc=acc, cmu=cmu, proteon=proteon, cray=cray, snmp_research=snmp_research, dec=dec, tgv=tgv, transarc=transarc, psi=psi, wellfleet=wellfleet, spartacus=spartacus, synoptics=synoptics, lexcel=lexcel, ftp=ftp, spider=spider, utk=utk, trw=trw, ibm=ibm, nsfnet=nsfnet, xyplex=xyplex, xylogics=xylogics, cayman=cayman, shiva=shiva, cisco=cisco, hls=hls, unix=unix, mit=mit, eon=eon, nsc=nsc, nat=nat, bbn=bbn, sun=sun, apple=apple, excelan=excelan, hp=hp, epilogue=epilogue, timeplex=timeplex, canstar=canstar)