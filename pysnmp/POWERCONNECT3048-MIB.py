#
# PySNMP MIB module POWERCONNECT3048-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/POWERCONNECT3048-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:32:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, IpAddress, Bits, Integer32, ObjectIdentity, Counter32, enterprises, TimeTicks, iso, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "IpAddress", "Bits", "Integer32", "ObjectIdentity", "Counter32", "enterprises", "TimeTicks", "iso", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Counter64", "ModuleIdentity")
DisplayString, PhysAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "TextualConvention")
dell = MibIdentifier((1, 3, 6, 1, 4, 1, 674))
dellLan = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895))
powerconnect3048 = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5))
class OwnerString(DisplayString):
    pass

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

dellCommGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5, 1))
dellHostGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5, 2))
dellMiscGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5, 3))
dellSpanGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5, 4))
dellConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11))
dellVlanGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5, 13))
dellPortTrunkGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5, 14))
commTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5, 1, 1), )
if mibBuilder.loadTexts: commTable.setStatus('mandatory')
commEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5, 1, 1, 1), ).setIndexNames((0, "POWERCONNECT3048-MIB", "commIndex"))
if mibBuilder.loadTexts: commEntry.setStatus('mandatory')
commIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: commIndex.setStatus('mandatory')
commName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commName.setStatus('mandatory')
commGet = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commGet.setStatus('mandatory')
commSet = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commSet.setStatus('mandatory')
commTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commTrap.setStatus('mandatory')
commStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commStatus.setStatus('mandatory')
hostTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5, 2, 1), )
if mibBuilder.loadTexts: hostTable.setStatus('mandatory')
hostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5, 2, 1, 1), ).setIndexNames((0, "POWERCONNECT3048-MIB", "hostIndex"))
if mibBuilder.loadTexts: hostEntry.setStatus('mandatory')
hostIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hostIndex.setStatus('mandatory')
hostName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hostName.setStatus('mandatory')
hostIP = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 2, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hostIP.setStatus('mandatory')
hostComm = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hostComm.setStatus('mandatory')
hostStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hostStatus.setStatus('mandatory')
hostAuthorization = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hostAuthorization.setStatus('mandatory')
miscBaud = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: miscBaud.setStatus('mandatory')
miscReset = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("noop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: miscReset.setStatus('mandatory')
miscStatisticsReset = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("reset", 1), ("noop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: miscStatisticsReset.setStatus('mandatory')
miscSwitchOperState = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("unknown", 2), ("ok", 3), ("noncritical", 4), ("critical", 5), ("nonrecoverable", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: miscSwitchOperState.setStatus('current')
spanOnOff = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: spanOnOff.setStatus('mandatory')
configVerSwPrimary = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configVerSwPrimary.setStatus('mandatory')
configVerHwChipSet = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configVerHwChipSet.setStatus('mandatory')
configBootMode = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("flash", 1), ("net", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configBootMode.setStatus('mandatory')
configBootFtpServerIp = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configBootFtpServerIp.setStatus('mandatory')
configBootImageFileName = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configBootImageFileName.setStatus('mandatory')
configPortTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6), )
if mibBuilder.loadTexts: configPortTable.setStatus('mandatory')
configPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1), ).setIndexNames((0, "POWERCONNECT3048-MIB", "configPort"))
if mibBuilder.loadTexts: configPortEntry.setStatus('mandatory')
configPort = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPort.setStatus('mandatory')
configPortDuplex = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("half-duplex", 1), ("full-duplex", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPortDuplex.setStatus('mandatory')
configPortRuntFilt = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPortRuntFilt.setStatus('mandatory')
configPortSrcSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPortSrcSecurity.setStatus('mandatory')
configPortDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4))).clone(namedValues=NamedValues(("rate10Meg", 1), ("rate100Meg", 2), ("rate1Gig", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPortDataRate.setStatus('mandatory')
configForwardingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("store-and-forward", 1), ("cut-through", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configForwardingMode.setStatus('mandatory')
configPortDuplexOper = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("half-duplex", 1), ("full-duplex", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configPortDuplexOper.setStatus('mandatory')
configPortDataRateOper = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4))).clone(namedValues=NamedValues(("rate10Meg", 1), ("rate100Meg", 2), ("rate1Gig", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configPortDataRateOper.setStatus('mandatory')
configPortStateOper = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disabled", 1), ("blocking", 2), ("listening", 3), ("learning", 4), ("forwarding", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configPortStateOper.setStatus('mandatory')
configPortFlowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPortFlowControl.setStatus('mandatory')
configPortDefaultVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPortDefaultVlanId.setStatus('mandatory')
configPortComments = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPortComments.setStatus('mandatory')
configPortAutoNegotiation = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPortAutoNegotiation.setStatus('mandatory')
configPortHOLBlocking = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPortHOLBlocking.setStatus('mandatory')
configPortFlowControlOper = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configPortFlowControlOper.setStatus('mandatory')
configPortGBIC = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPortGBIC.setStatus('mandatory')
configPortFastLink = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPortFastLink.setStatus('mandatory')
configPortPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 6, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("high", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configPortPriority.setStatus('mandatory')
configRmonOnOff = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configRmonOnOff.setStatus('mandatory')
configMirroringOnOff = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configMirroringOnOff.setStatus('mandatory')
configMirrorSrc = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configMirrorSrc.setStatus('mandatory')
configMirrorMon = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configMirrorMon.setStatus('mandatory')
configIpAssignmentMode = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("manual", 1), ("bootP", 2), ("dhcp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configIpAssignmentMode.setStatus('mandatory')
configPhysAddress = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 13), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configPhysAddress.setStatus('mandatory')
configPasswordUser = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: configPasswordUser.setStatus('mandatory')
configPasswordAdmin = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: configPasswordAdmin.setStatus('mandatory')
configIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 16), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configIpAddress.setStatus('mandatory')
configNetMask = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 17), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configNetMask.setStatus('mandatory')
configGateway = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 18), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configGateway.setStatus('mandatory')
configSave = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("save", 1), ("noop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configSave.setStatus('mandatory')
configVerifyPassword = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: configVerifyPassword.setStatus('mandatory')
configVerBootRomImage = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: configVerBootRomImage.setStatus('mandatory')
configRestoreDefaults = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("restore", 1), ("noop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configRestoreDefaults.setStatus('mandatory')
configIGMPOnOff = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configIGMPOnOff.setStatus('mandatory')
configWebOnOff = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configWebOnOff.setStatus('mandatory')
configHighPriorityOptimization = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configHighPriorityOptimization.setStatus('mandatory')
configDynamicAddressLearning = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configDynamicAddressLearning.setStatus('mandatory')
configUserAuthenticationMode = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("local", 1), ("localThenRemote", 2), ("remoteThenLocal", 3), ("remote", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configUserAuthenticationMode.setStatus('mandatory')
configRadiusServerIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 28), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configRadiusServerIpAddress.setStatus('mandatory')
configRadiusSharedSecret = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 29), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configRadiusSharedSecret.setStatus('mandatory')
configTelnetConsole = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configTelnetConsole.setStatus('mandatory')
configDiffServTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 31), )
if mibBuilder.loadTexts: configDiffServTable.setStatus('mandatory')
configDiffServEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 31, 1), ).setIndexNames((0, "POWERCONNECT3048-MIB", "configDiffServDSCP"))
if mibBuilder.loadTexts: configDiffServEntry.setStatus('mandatory')
configDiffServDSCP = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 31, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configDiffServDSCP.setStatus('mandatory')
configDiffServPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 31, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("high", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configDiffServPriority.setStatus('mandatory')
configTftpServerIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 32), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configTftpServerIpAddress.setStatus('mandatory')
configTftpServerFileName = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 33), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configTftpServerFileName.setStatus('mandatory')
configTftpOperation = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("download", 1), ("upload", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configTftpOperation.setStatus('mandatory')
configIpFilter = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configIpFilter.setStatus('mandatory')
configIpFilterTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 36), )
if mibBuilder.loadTexts: configIpFilterTable.setStatus('mandatory')
configIpFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 36, 1), ).setIndexNames((0, "POWERCONNECT3048-MIB", "configIpFilterIpAddress"))
if mibBuilder.loadTexts: configIpFilterEntry.setStatus('mandatory')
configIpFilterIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 36, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configIpFilterIpAddress.setStatus('mandatory')
configIpFilterStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 11, 36, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 6))).clone(namedValues=NamedValues(("active", 1), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configIpFilterStatus.setStatus('mandatory')
vlanTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5, 13, 1), )
if mibBuilder.loadTexts: vlanTable.setStatus('mandatory')
vlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5, 13, 1, 1), ).setIndexNames((0, "POWERCONNECT3048-MIB", "vlanId"))
if mibBuilder.loadTexts: vlanEntry.setStatus('mandatory')
vlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 13, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanId.setStatus('mandatory')
vlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 13, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanName.setStatus('mandatory')
vlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 13, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4, 6))).clone(namedValues=NamedValues(("active", 1), ("createAndGo", 4), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanStatus.setStatus('mandatory')
vlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5, 13, 2), )
if mibBuilder.loadTexts: vlanPortTable.setStatus('mandatory')
vlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5, 13, 2, 1), ).setIndexNames((0, "POWERCONNECT3048-MIB", "vlanPortPortId"), (0, "POWERCONNECT3048-MIB", "vlanPortVlanId"))
if mibBuilder.loadTexts: vlanPortEntry.setStatus('mandatory')
vlanPortPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 13, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortPortId.setStatus('mandatory')
vlanPortVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 13, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPortVlanId.setStatus('mandatory')
vlanPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 13, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4, 6))).clone(namedValues=NamedValues(("active", 1), ("createAndGo", 4), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanPortStatus.setStatus('mandatory')
vlanPortTaggedMode = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 13, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("untagged", 1), ("tagged", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanPortTaggedMode.setStatus('mandatory')
portTrunkTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10895, 5, 14, 1), )
if mibBuilder.loadTexts: portTrunkTable.setStatus('mandatory')
portTrunkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10895, 5, 14, 1, 1), ).setIndexNames((0, "POWERCONNECT3048-MIB", "portTrunkId"), (0, "POWERCONNECT3048-MIB", "portTrunkMember"))
if mibBuilder.loadTexts: portTrunkEntry.setStatus('mandatory')
portTrunkId = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 14, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portTrunkId.setStatus('mandatory')
portTrunkMember = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 14, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portTrunkMember.setStatus('mandatory')
portTrunkMemberValue = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10895, 5, 14, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portTrunkMemberValue.setStatus('mandatory')
addressIntrusion = NotificationType((1, 3, 6, 1, 4, 1, 674) + (0,0)).setObjects(("POWERCONNECT3048-MIB", "ifIndex"))
mibBuilder.exportSymbols("POWERCONNECT3048-MIB", configPortDuplex=configPortDuplex, vlanEntry=vlanEntry, vlanPortVlanId=vlanPortVlanId, configPortPriority=configPortPriority, configSave=configSave, hostAuthorization=hostAuthorization, configRestoreDefaults=configRestoreDefaults, configDynamicAddressLearning=configDynamicAddressLearning, dellMiscGroup=dellMiscGroup, configDiffServEntry=configDiffServEntry, configIpAssignmentMode=configIpAssignmentMode, configRmonOnOff=configRmonOnOff, hostIP=hostIP, portTrunkEntry=portTrunkEntry, configPortRuntFilt=configPortRuntFilt, commStatus=commStatus, configBootFtpServerIp=configBootFtpServerIp, configPasswordUser=configPasswordUser, configDiffServPriority=configDiffServPriority, configPortFlowControl=configPortFlowControl, dellLan=dellLan, configPortFastLink=configPortFastLink, configPortTable=configPortTable, vlanTable=vlanTable, configVerHwChipSet=configVerHwChipSet, portTrunkTable=portTrunkTable, configPortFlowControlOper=configPortFlowControlOper, configBootMode=configBootMode, vlanPortStatus=vlanPortStatus, vlanStatus=vlanStatus, vlanId=vlanId, miscStatisticsReset=miscStatisticsReset, configIpFilterEntry=configIpFilterEntry, powerconnect3048=powerconnect3048, configDiffServTable=configDiffServTable, commTable=commTable, portTrunkId=portTrunkId, dellConfigGroup=dellConfigGroup, dell=dell, configPortHOLBlocking=configPortHOLBlocking, configRadiusServerIpAddress=configRadiusServerIpAddress, configIGMPOnOff=configIGMPOnOff, configPortEntry=configPortEntry, configIpFilterIpAddress=configIpFilterIpAddress, dellPortTrunkGroup=dellPortTrunkGroup, hostComm=hostComm, vlanName=vlanName, configBootImageFileName=configBootImageFileName, commName=commName, OwnerString=OwnerString, vlanPortPortId=vlanPortPortId, configPortDataRate=configPortDataRate, dellSpanGroup=dellSpanGroup, dellVlanGroup=dellVlanGroup, configVerBootRomImage=configVerBootRomImage, configIpFilterStatus=configIpFilterStatus, vlanPortEntry=vlanPortEntry, configPhysAddress=configPhysAddress, vlanPortTaggedMode=vlanPortTaggedMode, configForwardingMode=configForwardingMode, configIpAddress=configIpAddress, configPortDataRateOper=configPortDataRateOper, configPortDefaultVlanId=configPortDefaultVlanId, configRadiusSharedSecret=configRadiusSharedSecret, configTelnetConsole=configTelnetConsole, configPortComments=configPortComments, configDiffServDSCP=configDiffServDSCP, configIpFilterTable=configIpFilterTable, miscSwitchOperState=miscSwitchOperState, configVerSwPrimary=configVerSwPrimary, miscBaud=miscBaud, configVerifyPassword=configVerifyPassword, hostStatus=hostStatus, commSet=commSet, configTftpServerIpAddress=configTftpServerIpAddress, spanOnOff=spanOnOff, hostIndex=hostIndex, configWebOnOff=configWebOnOff, commIndex=commIndex, configTftpOperation=configTftpOperation, configUserAuthenticationMode=configUserAuthenticationMode, hostTable=hostTable, configPortGBIC=configPortGBIC, commEntry=commEntry, miscReset=miscReset, configPortSrcSecurity=configPortSrcSecurity, hostEntry=hostEntry, configPortStateOper=configPortStateOper, MacAddress=MacAddress, configPort=configPort, configPortAutoNegotiation=configPortAutoNegotiation, configPortDuplexOper=configPortDuplexOper, hostName=hostName, commGet=commGet, commTrap=commTrap, addressIntrusion=addressIntrusion, vlanPortTable=vlanPortTable, configMirroringOnOff=configMirroringOnOff, dellCommGroup=dellCommGroup, configTftpServerFileName=configTftpServerFileName, configGateway=configGateway, portTrunkMember=portTrunkMember, configIpFilter=configIpFilter, portTrunkMemberValue=portTrunkMemberValue, configMirrorSrc=configMirrorSrc, dellHostGroup=dellHostGroup, configPasswordAdmin=configPasswordAdmin, configNetMask=configNetMask, configHighPriorityOptimization=configHighPriorityOptimization, configMirrorMon=configMirrorMon)