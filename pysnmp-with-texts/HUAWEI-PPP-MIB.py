#
# PySNMP MIB module HUAWEI-PPP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-PPP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:47:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, TimeTicks, ObjectIdentity, Unsigned32, Integer32, Counter64, Gauge32, Bits, ModuleIdentity, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "ObjectIdentity", "Unsigned32", "Integer32", "Counter64", "Gauge32", "Bits", "ModuleIdentity", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier")
TextualConvention, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "TruthValue")
hwPppMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169))
if mibBuilder.loadTexts: hwPppMIB.setLastUpdated('200710172230Z')
if mibBuilder.loadTexts: hwPppMIB.setOrganization('Huawei Technologies co.,Ltd.')
if mibBuilder.loadTexts: hwPppMIB.setContactInfo('VRP Team Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.huawei.com Zip:100085 ')
if mibBuilder.loadTexts: hwPppMIB.setDescription('This MIB is mainly used to configure PPP , PPP MRU negotiation, MP binding with Mp-Group, and PAP/Chap authentication .')
hwPppObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1))
hwPppConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 1), )
if mibBuilder.loadTexts: hwPppConfigTable.setStatus('current')
if mibBuilder.loadTexts: hwPppConfigTable.setDescription('This table is used to configure PPP , PPP MRU negotiation, and MP binding with MP-Group.')
hwPppConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 1, 1), ).setIndexNames((0, "HUAWEI-PPP-MIB", "hwPppIfIndex"))
if mibBuilder.loadTexts: hwPppConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hwPppConfigEntry.setDescription('This table is used to configure PPP , PPP MRU negotiation, and MP binding with MP-Group.')
hwPppIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwPppIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwPppIfIndex.setDescription('This object indicates the interface index.')
hwPppMruNegType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPppMruNegType.setStatus('current')
if mibBuilder.loadTexts: hwPppMruNegType.setDescription('This object indicates the mode of MRU negotiation.')
hwPppMpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 1, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPppMpIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwPppMpIfIndex.setDescription('This object indicates the MP-Group index.')
hwPppAuthenticateTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 2), )
if mibBuilder.loadTexts: hwPppAuthenticateTable.setStatus('current')
if mibBuilder.loadTexts: hwPppAuthenticateTable.setDescription('This table is used to configure PAP/CHAP authentication .')
hwPppAuthenticateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 2, 1), ).setIndexNames((0, "HUAWEI-PPP-MIB", "hwPppIfIndex"))
if mibBuilder.loadTexts: hwPppAuthenticateEntry.setStatus('current')
if mibBuilder.loadTexts: hwPppAuthenticateEntry.setDescription('This table is used to configure PAP/CHAP authentication .')
hwPppAuthenticateMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("chap", 1), ("pap", 2), ("chappap", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPppAuthenticateMode.setStatus('current')
if mibBuilder.loadTexts: hwPppAuthenticateMode.setDescription('This object indicates the mode of the authentication.')
hwPppAuthenticateChapUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 2, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPppAuthenticateChapUserName.setStatus('current')
if mibBuilder.loadTexts: hwPppAuthenticateChapUserName.setDescription('This object indicates the username of CHAP authentication.')
hwPppAuthenticateChapPwType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cipher", 1), ("simple", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPppAuthenticateChapPwType.setStatus('current')
if mibBuilder.loadTexts: hwPppAuthenticateChapPwType.setDescription('This object indicates the encryption type of CHAP.')
hwPppAuthenticateChapPw = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 2, 1, 14), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(1, 16), ValueSizeConstraint(24, 24), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPppAuthenticateChapPw.setStatus('current')
if mibBuilder.loadTexts: hwPppAuthenticateChapPw.setDescription('This object indicates the password of CHAP authentication.')
hwPppAuthenticatePapUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 2, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPppAuthenticatePapUserName.setStatus('current')
if mibBuilder.loadTexts: hwPppAuthenticatePapUserName.setDescription('This object indicates the username of PAP authentication..')
hwPppAuthenticatePapPwType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cipher", 1), ("simple", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPppAuthenticatePapPwType.setStatus('current')
if mibBuilder.loadTexts: hwPppAuthenticatePapPwType.setDescription('This object indicates the encryption type of PAP.')
hwPppAuthenticatePapPw = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 1, 2, 1, 17), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(1, 16), ValueSizeConstraint(24, 24), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwPppAuthenticatePapPw.setStatus('current')
if mibBuilder.loadTexts: hwPppAuthenticatePapPw.setDescription('This object indicates the password of PAP authentication.')
hwPppConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 11))
hwPppCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 11, 1))
hwPppCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 11, 1, 1)).setObjects(("HUAWEI-PPP-MIB", "hwPppConfigObjectGroup"), ("HUAWEI-PPP-MIB", "hwPppAuthenticateObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPppCompliance = hwPppCompliance.setStatus('current')
if mibBuilder.loadTexts: hwPppCompliance.setDescription('The compliance statement for systems supporting the HUAWEI-PPP-MIB.')
hwPppGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 11, 2))
hwPppConfigObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 11, 2, 1)).setObjects(("HUAWEI-PPP-MIB", "hwPppMruNegType"), ("HUAWEI-PPP-MIB", "hwPppMpIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPppConfigObjectGroup = hwPppConfigObjectGroup.setStatus('current')
if mibBuilder.loadTexts: hwPppConfigObjectGroup.setDescription('This object indicates the PPP attribute group.')
hwPppAuthenticateObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 169, 11, 2, 2)).setObjects(("HUAWEI-PPP-MIB", "hwPppAuthenticateMode"), ("HUAWEI-PPP-MIB", "hwPppAuthenticateChapUserName"), ("HUAWEI-PPP-MIB", "hwPppAuthenticateChapPwType"), ("HUAWEI-PPP-MIB", "hwPppAuthenticateChapPw"), ("HUAWEI-PPP-MIB", "hwPppAuthenticatePapUserName"), ("HUAWEI-PPP-MIB", "hwPppAuthenticatePapPwType"), ("HUAWEI-PPP-MIB", "hwPppAuthenticatePapPw"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwPppAuthenticateObjectGroup = hwPppAuthenticateObjectGroup.setStatus('current')
if mibBuilder.loadTexts: hwPppAuthenticateObjectGroup.setDescription('This object indicates the PPP authentcation group.')
mibBuilder.exportSymbols("HUAWEI-PPP-MIB", hwPppConfigObjectGroup=hwPppConfigObjectGroup, hwPppAuthenticateTable=hwPppAuthenticateTable, hwPppConformance=hwPppConformance, hwPppAuthenticateEntry=hwPppAuthenticateEntry, hwPppAuthenticateChapUserName=hwPppAuthenticateChapUserName, hwPppCompliance=hwPppCompliance, PYSNMP_MODULE_ID=hwPppMIB, hwPppConfigTable=hwPppConfigTable, hwPppMIB=hwPppMIB, hwPppGroups=hwPppGroups, hwPppAuthenticatePapUserName=hwPppAuthenticatePapUserName, hwPppIfIndex=hwPppIfIndex, hwPppAuthenticatePapPwType=hwPppAuthenticatePapPwType, hwPppObjects=hwPppObjects, hwPppAuthenticateObjectGroup=hwPppAuthenticateObjectGroup, hwPppAuthenticateChapPwType=hwPppAuthenticateChapPwType, hwPppCompliances=hwPppCompliances, hwPppMruNegType=hwPppMruNegType, hwPppMpIfIndex=hwPppMpIfIndex, hwPppConfigEntry=hwPppConfigEntry, hwPppAuthenticateMode=hwPppAuthenticateMode, hwPppAuthenticateChapPw=hwPppAuthenticateChapPw, hwPppAuthenticatePapPw=hwPppAuthenticatePapPw)