#
# PySNMP MIB module HUAWEI-VO-ANALOG-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-VO-ANALOG-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:49:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
voice, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "voice")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, IpAddress, Bits, MibIdentifier, Counter32, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, Unsigned32, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "IpAddress", "Bits", "MibIdentifier", "Counter32", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "Unsigned32", "ModuleIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwVoiceAnalogInterfaceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3))
hwVoiceAnalogInterfaceMIB.setRevisions(('2004-04-08 13:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwVoiceAnalogInterfaceMIB.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: hwVoiceAnalogInterfaceMIB.setLastUpdated('200410200000Z')
if mibBuilder.loadTexts: hwVoiceAnalogInterfaceMIB.setOrganization('Huawei-3COM Technologies Co., Ltd.')
if mibBuilder.loadTexts: hwVoiceAnalogInterfaceMIB.setContactInfo('PLAT Team Huawei 3Com Technologies co.,Ltd. Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.huawei-3com.com Zip:100085')
if mibBuilder.loadTexts: hwVoiceAnalogInterfaceMIB.setDescription(' ')
hwVoAnalogIfCommonObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 1))
hwVoAnalogIfCommonConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 1, 1), )
if mibBuilder.loadTexts: hwVoAnalogIfCommonConfigTable.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfCommonConfigTable.setDescription('The voice analog interface common configuration table contains information about configuration parameters for analog voice interface.')
hwVoAnalogIfCommonConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 1, 1, 1), ).setIndexNames((0, "HUAWEI-VO-ANALOG-IF-MIB", "hwVoAnalogIfConfigPortNumber"))
if mibBuilder.loadTexts: hwVoAnalogIfCommonConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfCommonConfigEntry.setDescription('An entry in the voice analog interface common configuration table. The entry is automatically created when a analog voice interface hardware is found.')
hwVoAnalogIfConfigPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoAnalogIfConfigPortNumber.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfConfigPortNumber.setDescription('Index of voice analog interface common config table. It identify the number of the voice port.')
hwVoAnalogIfConfigPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fxs", 1), ("fxo", 2), ("em", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoAnalogIfConfigPortType.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfConfigPortType.setDescription('This object expresses the type of the voice analog interfaces. fxs : the type of the voice port is FXS. fxo : the type of the voice port is FXO. em : the type of the voice port is E&M.')
hwVoAnaloglfConfigPortImpedance = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("impedance600Real", 1), ("impedanceComplex", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoAnaloglfConfigPortImpedance.setStatus('current')
if mibBuilder.loadTexts: hwVoAnaloglfConfigPortImpedance.setDescription('This object expresses the port impedance of voice analog interfaces. impedance600Real : 600 Ohms This impedance is primarily used by FXS. impedanceComplex : 200 Ohms + 680 Ohms || 100nF This impedance is primarily used by FX0 and E&M.')
hwVoAnalogIfConfigInitialDigitTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 300)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfConfigInitialDigitTimeOut.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfConfigInitialDigitTimeOut.setDescription('This object states the longgest time to wait the first input digit from caller side. The default value is 10 seconds.')
hwVoAnalogIfConfigInterDigitTimeOut = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 300)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfConfigInterDigitTimeOut.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfConfigInterDigitTimeOut.setDescription('This object states the longest time to wait between two input digit from caller side. The default value is 10 seconds.')
hwVoAnalogIfConfigCallDisconnect = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 120)).clone(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoAnalogIfConfigCallDisconnect.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfConfigCallDisconnect.setDescription('This object states the time the system waits for the caller side to hang up after the connect is disable. The default value is 10 seconds.')
hwVoAnalogIfFXSObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2))
hwVoAnalogIfFXSConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2, 1), )
if mibBuilder.loadTexts: hwVoAnalogIfFXSConfigTable.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXSConfigTable.setDescription('The voice analog interface fxs configuration table contains information about configuration parameters for analog fxs voice interface.')
hwVoAnalogIfFXSConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2, 1, 1), ).setIndexNames((0, "HUAWEI-VO-ANALOG-IF-MIB", "hwVoAnalogIfFXSConfigPortNumber"))
if mibBuilder.loadTexts: hwVoAnalogIfFXSConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXSConfigEntry.setDescription('An entry in the voice analog interface fxs configuration table. The entry is automatically created when a analog fxs voice interface hardware is found.')
hwVoAnalogIfFXSConfigPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoAnalogIfFXSConfigPortNumber.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXSConfigPortNumber.setDescription('Index of voice analog interface fxs config table. It identify the number of the fxs voice port.')
hwVoAnalogIfFXSConfigStartMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("loopStart", 1), ("groundStart", 2))).clone('loopStart')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoAnalogIfFXSConfigStartMode.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXSConfigStartMode.setDescription('This object expresses the signaling type of analog fxs interface. The default value is loopStart.')
hwVoAnalogIfFXSTimerTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2, 3), )
if mibBuilder.loadTexts: hwVoAnalogIfFXSTimerTable.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXSTimerTable.setDescription('The voice analog interface fxs timer table contains information about timer parameters for analog fxs voice interface.')
hwVoAnalogIfFXSTimerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2, 3, 1), ).setIndexNames((0, "HUAWEI-VO-ANALOG-IF-MIB", "hwVoAnalogIfFXSTimerPortNumber"))
if mibBuilder.loadTexts: hwVoAnalogIfFXSTimerEntry.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXSTimerEntry.setDescription('An entry in the voice analog interface fxs configuration table. The entry is automatically created when a analog fxs voice interface hardware is found.')
hwVoAnalogIfFXSTimerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoAnalogIfFXSTimerPortNumber.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXSTimerPortNumber.setDescription('Index of voice analog interface fxs timer table. It identify the number of the fxs voice port.')
hwVoAnalogIfFXSTimerDtmf = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 500)).clone(120)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoAnalogIfFXSTimerDtmf.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXSTimerDtmf.setDescription('This object expresses outgoing dtmf digit duration of the analog fxs interface. The default value is 120 milliseconds')
hwVoAnalogIfFXSTimerDtmfInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 500)).clone(120)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoAnalogIfFXSTimerDtmfInterval.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXSTimerDtmfInterval.setDescription('This object expresses outgoing dtmf interval duration of the analog fxs interface. The default value is 120 milliseconds')
hwVoAnalogIfFXOObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3))
hwVoAnalogIfFXOConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 1), )
if mibBuilder.loadTexts: hwVoAnalogIfFXOConfigTable.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXOConfigTable.setDescription('The voice analog interface fxo configuration table contains information about configuration parameters for analog fxo voice interface.')
hwVoAnalogIfFXOConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 1, 1), ).setIndexNames((0, "HUAWEI-VO-ANALOG-IF-MIB", "hwVoAnalogIfFXOConfigPortNumber"))
if mibBuilder.loadTexts: hwVoAnalogIfFXOConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXOConfigEntry.setDescription('An entry in the voice analog interface fxo configuration table. The entry is automatically created when a analog fxo voice interface hardware is found.')
hwVoAnalogIfFXOConfigPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoAnalogIfFXOConfigPortNumber.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXOConfigPortNumber.setDescription('Index of voice analog interface fxo config table. It identify the number of the fxo voice port.')
hwVoAnalogIfFXOConfigStartMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("loopStart", 1), ("groundStart", 2))).clone('loopStart')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoAnalogIfFXOConfigStartMode.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXOConfigStartMode.setDescription('This object expresses the signal type of analog fxo interface. The default value is fxoLoopStart.')
hwVoAnalogIfFXOConfigAlertNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 1, 1, 3), Integer32().clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoAnalogIfFXOConfigAlertNumber.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXOConfigAlertNumber.setDescription('This object expresses the number of rings detected before loop being closed. The default value is 2.')
hwVoAnalogIfFXOConfigArea = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("europe", 1), ("custom", 2), ("north-america", 3))).clone('europe')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfFXOConfigArea.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXOConfigArea.setDescription('This object expresses the busy tone of analog fxo interface. The default value is europe.')
hwVoAnalogIfFXOPreDialDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfFXOPreDialDelay.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXOPreDialDelay.setDescription('This object expresses the pre-dial delay of analog fxo interface. The default value is 1 seconds.')
hwVoAnaloglfFXOConfigPortImpedance = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("impedance550r", 0), ("impedance600r", 1), ("impedance600c", 2), ("impedancecomplex", 3))).clone('impedance600c')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnaloglfFXOConfigPortImpedance.setStatus('current')
if mibBuilder.loadTexts: hwVoAnaloglfFXOConfigPortImpedance.setDescription('This object expresses the port impedance of FXO interfaces.')
hwVoAnalogIfFXOTimerTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 3), )
if mibBuilder.loadTexts: hwVoAnalogIfFXOTimerTable.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXOTimerTable.setDescription('The voice analog interface fxo timer table contains information about timer parameters for analog fxo voice interface.')
hwVoAnalogIfFXOTimerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 3, 1), ).setIndexNames((0, "HUAWEI-VO-ANALOG-IF-MIB", "hwVoAnalogIfFXOTimerPortNumber"))
if mibBuilder.loadTexts: hwVoAnalogIfFXOTimerEntry.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXOTimerEntry.setDescription('An entry in the voice analog interface fxo timer table. The entry is automatically created when a analog fxo voice interface hardware is found.')
hwVoAnalogIfFXOTimerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoAnalogIfFXOTimerPortNumber.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXOTimerPortNumber.setDescription('Index of voice analog interface fxo timer table. It identify the number of the fxo voice port.')
hwVoAnalogIfFXOTimerDtmf = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 500)).clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfFXOTimerDtmf.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXOTimerDtmf.setDescription('This object expresses outgoing dtmf digit duration of the analog fxo interface. The default value is 120 milliseconds')
hwVoAnalogIfFXOTimerDtmfInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 500)).clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfFXOTimerDtmfInterval.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfFXOTimerDtmfInterval.setDescription('This object expresses outgoing dtmf interval duration of the analog fxo interface. The default value is 120 milliseconds')
hwVoAnalogIfEMObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4))
hwVoAnalogIfEMConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 1), )
if mibBuilder.loadTexts: hwVoAnalogIfEMConfigTable.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMConfigTable.setDescription('The voice analog interface e&m configuration table contains information about configuration parameters for analog e&m voice interface.')
hwVoAnalogIfEMConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 1, 1), ).setIndexNames((0, "HUAWEI-VO-ANALOG-IF-MIB", "hwVoAnalogIfEMConfigPortNumber"))
if mibBuilder.loadTexts: hwVoAnalogIfEMConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMConfigEntry.setDescription('An entry in the voice analog interface e&m configuration table. The entry is automatically created when a analog e&m voice interface hardware is found.')
hwVoAnalogIfEMConfigPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoAnalogIfEMConfigPortNumber.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMConfigPortNumber.setDescription('Index of voice analog interface e&m config table. It identify the number of the e&m voice port.')
hwVoAnalogIfEMConfigSignalMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("delayDial", 1), ("immediateDial", 2), ("winkStart", 3))).clone('immediateDial')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfEMConfigSignalMode.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMConfigSignalMode.setDescription('This object expresses the signal mode of the analog e&m interfaces. The default value is immediateDial. ')
hwVoAnalogIfEMConfigPhyParm = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("twoWiresOperation", 1), ("fourWiresOperation", 2))).clone('fourWiresOperation')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfEMConfigPhyParm.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMConfigPhyParm.setDescription('This object expresses the operation of the analog e&m signal. The default value of this object is fourWiresOperation.')
hwVoAnalogIfEMConfigPhyType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 5))).clone(namedValues=NamedValues(("type1", 1), ("type2", 2), ("type3", 3), ("type5", 5))).clone('type5')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfEMConfigPhyType.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMConfigPhyType.setDescription('This object expresses the e&m lead signaling type of the analog e&m interface. The default is type5.')
hwVoAnalogIfEMConfigTimeoutRinging = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(5, 600), ValueRangeConstraint(65535, 65535), )).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfEMConfigTimeoutRinging.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMConfigTimeoutRinging.setDescription('This object expresses the ring timeout of the analog e&m interface. The value of 65535 indicates the timer is approach infinity. The default value of this object is 60 seconds.')
hwVoAnalogIfEMConfigTimeoutWaitDigit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(3, 600), ValueRangeConstraint(65535, 65535), )).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfEMConfigTimeoutWaitDigit.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMConfigTimeoutWaitDigit.setDescription('This object expresses the wait digit timeout of the analog e&m interface. The value of 65535 indicates the timer is approach infinity. The default value of this object is 5 seconds.')
hwVoAnalogIfEMTimerTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3), )
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerTable.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerTable.setDescription('The voice analog interface e&m timer table contains information about timer parameters for analog e&m voice interface.')
hwVoAnalogIfEMTimerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1), ).setIndexNames((0, "HUAWEI-VO-ANALOG-IF-MIB", "hwVoAnalogIfEMTimerPortNumber"))
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerEntry.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerEntry.setDescription('An entry in the voice analog interface e&m timer table. The entry is automatically created when a analog e&m voice interface hardware is found.')
hwVoAnalogIfEMTimerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerPortNumber.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerPortNumber.setDescription('Index of voice analog interface e&m timer table. It identify the number of the e&m voice port.')
hwVoAnalogIfEMTimerDtmf = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 500)).clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerDtmf.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerDtmf.setDescription('This object expresses outgoing dtmf digit duration of the analog e&m interface. The default value is 120 milliseconds')
hwVoAnalogIfEMTimerDtmfInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 500)).clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerDtmfInterval.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerDtmfInterval.setDescription('This object expresses outgoing dtmf interval duration of the analog e&m interface. The default value is 120 milliseconds')
hwVoAnalogIfEMTimerCallInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(200, 2000)).clone(200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerCallInterval.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerCallInterval.setDescription('This object expresses the dureation of call clearing. The default value is 200 milliseconds.')
hwVoAnalogIfEMTimerSendWink = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 5000)).clone(200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerSendWink.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerSendWink.setDescription("This object expresses the max time between receiving seizure signal and sending wink signal. This object can olny be used when hwVoAnalogIfEMConfigSignalMode is 'winkStart'. The default value is 500 milliseconds.")
hwVoAnalogIfEMTimerWinkRising = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 5000)).clone(2000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerWinkRising.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerWinkRising.setDescription("This object expresses the max time between sending seizure signal and receiving wink signal. This object can only be used when hwVoAnalogIfEMConfigSignalMode is 'winkStart'. The default value is 2000 milliseconds.")
hwVoAnalogIfEMTimerWinkHold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 3000)).clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerWinkHold.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerWinkHold.setDescription("This object expresses the max duration for sending wink signal. This object can only be used when hwVoAnalogIfEMConfigSignalMode is 'winkStart'. The default value is 500 milliseconds.")
hwVoAnalogIfEMTimerDialoutDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(50, 5000)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerDialoutDelay.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerDialoutDelay.setDescription("This object expresses max time sending called digits. This object can only be used when hwVoAnalogIfEMConfigSignalMode is 'immediate'. The default value is 300 milliseconds.")
hwVoAnalogIfEMTimerRising = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(20, 2000)).clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerRising.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerRising.setDescription("This object expresses the wait duration between receiveing seizure signal and sending delay signal. This object can only be used when hwVoAnalogIfEMConfigSignalMode is 'delayDial'. The default value is 300 milliseconds.")
hwVoAnalogIfEMTimerHold = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 3, 4, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 5000)).clone(400)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerHold.setStatus('current')
if mibBuilder.loadTexts: hwVoAnalogIfEMTimerHold.setDescription("This object expresses the max time sending delay signal. This object can only be used when hwVoAnalogIfEMConfigSignalMode is 'delayDial'. The default value is 400 milliseconds.")
mibBuilder.exportSymbols("HUAWEI-VO-ANALOG-IF-MIB", hwVoAnalogIfEMTimerWinkRising=hwVoAnalogIfEMTimerWinkRising, hwVoAnalogIfEMTimerSendWink=hwVoAnalogIfEMTimerSendWink, hwVoAnalogIfEMTimerPortNumber=hwVoAnalogIfEMTimerPortNumber, hwVoAnalogIfFXSTimerPortNumber=hwVoAnalogIfFXSTimerPortNumber, hwVoiceAnalogInterfaceMIB=hwVoiceAnalogInterfaceMIB, hwVoAnalogIfFXOConfigPortNumber=hwVoAnalogIfFXOConfigPortNumber, hwVoAnalogIfFXOConfigArea=hwVoAnalogIfFXOConfigArea, hwVoAnalogIfFXOTimerDtmf=hwVoAnalogIfFXOTimerDtmf, hwVoAnalogIfEMConfigPhyParm=hwVoAnalogIfEMConfigPhyParm, hwVoAnalogIfFXSObjects=hwVoAnalogIfFXSObjects, hwVoAnalogIfFXOConfigTable=hwVoAnalogIfFXOConfigTable, hwVoAnalogIfFXSTimerTable=hwVoAnalogIfFXSTimerTable, hwVoAnalogIfConfigCallDisconnect=hwVoAnalogIfConfigCallDisconnect, hwVoAnalogIfConfigPortNumber=hwVoAnalogIfConfigPortNumber, hwVoAnalogIfConfigInitialDigitTimeOut=hwVoAnalogIfConfigInitialDigitTimeOut, hwVoAnalogIfEMConfigTimeoutRinging=hwVoAnalogIfEMConfigTimeoutRinging, PYSNMP_MODULE_ID=hwVoiceAnalogInterfaceMIB, hwVoAnalogIfEMConfigPhyType=hwVoAnalogIfEMConfigPhyType, hwVoAnalogIfFXOObjects=hwVoAnalogIfFXOObjects, hwVoAnalogIfFXOTimerTable=hwVoAnalogIfFXOTimerTable, hwVoAnalogIfCommonObjects=hwVoAnalogIfCommonObjects, hwVoAnalogIfFXSTimerDtmfInterval=hwVoAnalogIfFXSTimerDtmfInterval, hwVoAnalogIfEMTimerDtmf=hwVoAnalogIfEMTimerDtmf, hwVoAnalogIfFXSConfigPortNumber=hwVoAnalogIfFXSConfigPortNumber, hwVoAnalogIfEMTimerHold=hwVoAnalogIfEMTimerHold, hwVoAnalogIfEMTimerTable=hwVoAnalogIfEMTimerTable, hwVoAnalogIfFXOConfigAlertNumber=hwVoAnalogIfFXOConfigAlertNumber, hwVoAnalogIfFXOTimerPortNumber=hwVoAnalogIfFXOTimerPortNumber, hwVoAnalogIfEMConfigSignalMode=hwVoAnalogIfEMConfigSignalMode, hwVoAnalogIfFXSConfigTable=hwVoAnalogIfFXSConfigTable, hwVoAnalogIfEMConfigPortNumber=hwVoAnalogIfEMConfigPortNumber, hwVoAnalogIfFXOConfigStartMode=hwVoAnalogIfFXOConfigStartMode, hwVoAnalogIfEMTimerDtmfInterval=hwVoAnalogIfEMTimerDtmfInterval, hwVoAnalogIfEMTimerWinkHold=hwVoAnalogIfEMTimerWinkHold, hwVoAnalogIfEMTimerRising=hwVoAnalogIfEMTimerRising, hwVoAnalogIfFXSTimerEntry=hwVoAnalogIfFXSTimerEntry, hwVoAnalogIfCommonConfigTable=hwVoAnalogIfCommonConfigTable, hwVoAnalogIfFXSConfigEntry=hwVoAnalogIfFXSConfigEntry, hwVoAnalogIfEMTimerEntry=hwVoAnalogIfEMTimerEntry, hwVoAnalogIfFXSConfigStartMode=hwVoAnalogIfFXSConfigStartMode, hwVoAnalogIfFXOTimerEntry=hwVoAnalogIfFXOTimerEntry, hwVoAnalogIfEMObjects=hwVoAnalogIfEMObjects, hwVoAnalogIfEMConfigEntry=hwVoAnalogIfEMConfigEntry, hwVoAnalogIfCommonConfigEntry=hwVoAnalogIfCommonConfigEntry, hwVoAnaloglfConfigPortImpedance=hwVoAnaloglfConfigPortImpedance, hwVoAnalogIfConfigPortType=hwVoAnalogIfConfigPortType, hwVoAnalogIfEMConfigTimeoutWaitDigit=hwVoAnalogIfEMConfigTimeoutWaitDigit, hwVoAnaloglfFXOConfigPortImpedance=hwVoAnaloglfFXOConfigPortImpedance, hwVoAnalogIfFXOPreDialDelay=hwVoAnalogIfFXOPreDialDelay, hwVoAnalogIfFXOTimerDtmfInterval=hwVoAnalogIfFXOTimerDtmfInterval, hwVoAnalogIfConfigInterDigitTimeOut=hwVoAnalogIfConfigInterDigitTimeOut, hwVoAnalogIfFXOConfigEntry=hwVoAnalogIfFXOConfigEntry, hwVoAnalogIfEMTimerCallInterval=hwVoAnalogIfEMTimerCallInterval, hwVoAnalogIfFXSTimerDtmf=hwVoAnalogIfFXSTimerDtmf, hwVoAnalogIfEMConfigTable=hwVoAnalogIfEMConfigTable, hwVoAnalogIfEMTimerDialoutDelay=hwVoAnalogIfEMTimerDialoutDelay)