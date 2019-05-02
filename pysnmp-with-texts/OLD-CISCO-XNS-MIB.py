#
# PySNMP MIB module OLD-CISCO-XNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/OLD-CISCO-XNS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:32:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
temporary, = mibBuilder.importSymbols("CISCO-SMI", "temporary")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter64, NotificationType, Gauge32, iso, Integer32, IpAddress, ModuleIdentity, Unsigned32, ObjectIdentity, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "NotificationType", "Gauge32", "iso", "Integer32", "IpAddress", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tmpxns = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 3, 2))
xnsInput = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsInput.setStatus('mandatory')
if mibBuilder.loadTexts: xnsInput.setDescription('Total input count of number of XNS packets.')
xnsLocal = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsLocal.setStatus('mandatory')
if mibBuilder.loadTexts: xnsLocal.setDescription('Total count of XNS input packets for this host.')
xnsBcastin = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsBcastin.setStatus('mandatory')
if mibBuilder.loadTexts: xnsBcastin.setDescription('Total count of number of XNS input broadcast packets.')
xnsForward = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsForward.setStatus('mandatory')
if mibBuilder.loadTexts: xnsForward.setDescription('Total count of number of XNS packets forwarded.')
xnsBcastout = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsBcastout.setStatus('mandatory')
if mibBuilder.loadTexts: xnsBcastout.setDescription('Total count of number of XNS output broadcast packets.')
xnsErrin = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsErrin.setStatus('mandatory')
if mibBuilder.loadTexts: xnsErrin.setDescription('Total count of number of XNS Error input packets.')
xnsErrout = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsErrout.setStatus('mandatory')
if mibBuilder.loadTexts: xnsErrout.setDescription('Total count of number of XNS Error output packets.')
xnsFormerr = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsFormerr.setStatus('mandatory')
if mibBuilder.loadTexts: xnsFormerr.setDescription('Total count of number of XNS input packets with header errors.')
xnsChksum = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsChksum.setStatus('mandatory')
if mibBuilder.loadTexts: xnsChksum.setDescription('Total count of number of XNS input packets with checksum errors.')
xnsNotgate = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsNotgate.setStatus('mandatory')
if mibBuilder.loadTexts: xnsNotgate.setDescription('Total count of number of XNS input packets received while not routing.')
xnsHopcnt = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsHopcnt.setStatus('mandatory')
if mibBuilder.loadTexts: xnsHopcnt.setDescription('Total count of number of XNS input packets that have exceeded the maximum hop count.')
xnsNoroute = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsNoroute.setStatus('mandatory')
if mibBuilder.loadTexts: xnsNoroute.setDescription('Total count of number of XNS packets dropped due to no route.')
xnsNoencap = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsNoencap.setStatus('mandatory')
if mibBuilder.loadTexts: xnsNoencap.setDescription('Total count of number of XNS packets dropped due to output encapsulation failure.')
xnsOutput = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsOutput.setStatus('mandatory')
if mibBuilder.loadTexts: xnsOutput.setDescription('Total count of number of XNS output packets.')
xnsInmult = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsInmult.setStatus('mandatory')
if mibBuilder.loadTexts: xnsInmult.setDescription('Total count of number of XNS input multicast packets.')
xnsUnknown = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsUnknown.setStatus('mandatory')
if mibBuilder.loadTexts: xnsUnknown.setDescription('Total count of number of unknown XNS input packets.')
xnsFwdbrd = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsFwdbrd.setStatus('mandatory')
if mibBuilder.loadTexts: xnsFwdbrd.setDescription('Total count of number of XNS broadcast packets forwarded.')
xnsEchoreqin = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 18), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsEchoreqin.setStatus('mandatory')
if mibBuilder.loadTexts: xnsEchoreqin.setDescription('Total count of number of XNS Echo request packets received.')
xnsEchoreqout = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsEchoreqout.setStatus('mandatory')
if mibBuilder.loadTexts: xnsEchoreqout.setDescription('Total count of number of XNS Echo request packets sent.')
xnsEchorepin = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsEchorepin.setStatus('mandatory')
if mibBuilder.loadTexts: xnsEchorepin.setDescription('Total count of number of XNS Echo reply packets received.')
xnsEchorepout = MibScalar((1, 3, 6, 1, 4, 1, 9, 3, 2, 21), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xnsEchorepout.setStatus('mandatory')
if mibBuilder.loadTexts: xnsEchorepout.setDescription('Total count of number of XNS Echo reply packets sent.')
mibBuilder.exportSymbols("OLD-CISCO-XNS-MIB", xnsInput=xnsInput, xnsEchorepin=xnsEchorepin, xnsEchorepout=xnsEchorepout, xnsNoencap=xnsNoencap, xnsLocal=xnsLocal, xnsNotgate=xnsNotgate, xnsChksum=xnsChksum, xnsEchoreqin=xnsEchoreqin, xnsEchoreqout=xnsEchoreqout, xnsFormerr=xnsFormerr, xnsFwdbrd=xnsFwdbrd, xnsHopcnt=xnsHopcnt, xnsBcastout=xnsBcastout, xnsInmult=xnsInmult, tmpxns=tmpxns, xnsOutput=xnsOutput, xnsErrin=xnsErrin, xnsErrout=xnsErrout, xnsNoroute=xnsNoroute, xnsUnknown=xnsUnknown, xnsBcastin=xnsBcastin, xnsForward=xnsForward)