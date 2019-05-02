#
# PySNMP MIB module ASCEND-MIBCLTM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBCLTM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:26:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, NotificationType, ModuleIdentity, Counter64, Gauge32, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, Bits, Counter32, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "ModuleIdentity", "Counter64", "Gauge32", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "Bits", "Counter32", "IpAddress", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibcltmCmd = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 66))
mibcltmCmdTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 66, 1), )
if mibBuilder.loadTexts: mibcltmCmdTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibcltmCmdTable.setDescription('A list of mibcltmCmd profile entries.')
mibcltmCmdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1), ).setIndexNames((0, "ASCEND-MIBCLTM-MIB", "cltmCmd-Index-o"))
if mibBuilder.loadTexts: mibcltmCmdEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibcltmCmdEntry.setDescription('A mibcltmCmd entry containing objects that maps to the parameters of mibcltmCmd profile.')
cltmCmd_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 1), Integer32()).setLabel("cltmCmd-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: cltmCmd_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_Index_o.setDescription('')
cltmCmd_CltmSlot = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17))).clone(namedValues=NamedValues(("anySlot", 1), ("slot1", 2), ("slot2", 3), ("slot3", 4), ("slot4", 5), ("slot5", 6), ("slot6", 7), ("slot7", 8), ("slot10", 11), ("slot11", 12), ("slot12", 13), ("slot13", 14), ("slot14", 15), ("slot15", 16), ("slot16", 17)))).setLabel("cltmCmd-CltmSlot").setMaxAccess("readonly")
if mibBuilder.loadTexts: cltmCmd_CltmSlot.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_CltmSlot.setDescription('Identify the CLTM slot within the system.')
cltmCmd_TestTimeStamp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 3), Integer32()).setLabel("cltmCmd-TestTimeStamp").setMaxAccess("readonly")
if mibBuilder.loadTexts: cltmCmd_TestTimeStamp.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_TestTimeStamp.setDescription('Value of the sysUpTime when the last test command was issued. This parameter is cleared when any of the test parameters are changed.')
cltmCmd_TestSequence = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 4), Integer32()).setLabel("cltmCmd-TestSequence").setMaxAccess("readonly")
if mibBuilder.loadTexts: cltmCmd_TestSequence.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_TestSequence.setDescription('Sequence of the last issued test command.')
cltmCmd_TestOperation = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40))).clone(namedValues=NamedValues(("none", 1), ("dmmTest", 2), ("lineInlsTest", 3), ("lineBgnsTest", 4), ("lineSignsTest", 5), ("lineLpresTest", 6), ("lineCldetTest", 7), ("lineImpstartTest", 8), ("lineImpstopTest", 9), ("lineImpreadTest", 10), ("calibTest", 11), ("toneSend", 12), ("toneRecv", 13), ("tdrSet", 14), ("tdrGet", 15), ("cltmReset", 16), ("cltmVersion", 17), ("cltmDownload", 18), ("dmmDcdelTest", 19), ("dmmCapeTest", 20), ("dmmAllTest", 21), ("txCtrlToneTest", 22), ("txTraceToneTest", 23), ("stopToneTest", 24), ("detRingerTest", 25), ("detAturTest", 26), ("btapTest", 27), ("voiceDetTest", 28), ("lineFcllocTest", 29), ("lineShortlocTest", 30), ("setResponderTest", 31), ("setBypassTest", 32), ("splitterDetectTest", 33), ("dmmAcdelTest", 34), ("dmmLbalTest", 35), ("dmmSoakTest", 36), ("sendVoiceTest", 37), ("measVoiceTest", 38), ("measDtaTest", 39), ("detaptorTest", 40)))).setLabel("cltmCmd-TestOperation").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_TestOperation.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_TestOperation.setDescription("The current operation that is active on the CLT Module. Defaultls to 'none'. Set to 'none' to stop the test procedure.")
cltmCmd_DmmType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("resistance", 1), ("dcVoltage", 2), ("acVoltage", 3), ("capacitance", 4)))).setLabel("cltmCmd-DmmType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_DmmType.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_DmmType.setDescription('DMM Measurement Type.')
cltmCmd_DmmLead = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tipRing", 1), ("tipSleeve", 2), ("ringSleeve", 3)))).setLabel("cltmCmd-DmmLead").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_DmmLead.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_DmmLead.setDescription('DMM Measurement Leads.')
cltmCmd_BackgroundNoiseFilter = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("psd", 1), ("e", 2), ("f", 3), ("g", 4)))).setLabel("cltmCmd-BackgroundNoiseFilter").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_BackgroundNoiseFilter.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_BackgroundNoiseFilter.setDescription('Line Filter Type for Background Noise Test.')
cltmCmd_BackgroundNoiseTermination = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("term100", 1), ("term135", 2), ("bridge100", 3), ("bridge135", 4)))).setLabel("cltmCmd-BackgroundNoiseTermination").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_BackgroundNoiseTermination.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_BackgroundNoiseTermination.setDescription('Line Termination Type for Background Noise Test.')
cltmCmd_LoopResistanceUnit = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("metric", 1), ("english", 2)))).setLabel("cltmCmd-LoopResistanceUnit").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_LoopResistanceUnit.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_LoopResistanceUnit.setDescription('Measurement System for Loop Resistance Test.')
cltmCmd_LoopResistanceTemp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 11), Integer32()).setLabel("cltmCmd-LoopResistanceTemp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_LoopResistanceTemp.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_LoopResistanceTemp.setDescription('Line Temperature for Loop Resistance Test. Assigned in degree celsius/fahrenheit.')
cltmCmd_ImpulseNoiseStartThresh = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 12), Integer32()).setLabel("cltmCmd-ImpulseNoiseStartThresh").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_ImpulseNoiseStartThresh.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_ImpulseNoiseStartThresh.setDescription('Threshold for Impulse Noise Test. The Range is 50-100 dBrm.')
cltmCmd_ImpulseNoiseStartDelta = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 13), Integer32()).setLabel("cltmCmd-ImpulseNoiseStartDelta").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_ImpulseNoiseStartDelta.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_ImpulseNoiseStartDelta.setDescription('Delta Value for Impulse Noise Test. The delta range is 2-6 dB')
cltmCmd_ImpulseNoiseStartMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 14), Integer32()).setLabel("cltmCmd-ImpulseNoiseStartMaxCount").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_ImpulseNoiseStartMaxCount.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_ImpulseNoiseStartMaxCount.setDescription('Max Count for Impulse Noise Test. The range of the value is 1-1999.')
cltmCmd_ImpulseNoiseStartDeadTime = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 15), Integer32()).setLabel("cltmCmd-ImpulseNoiseStartDeadTime").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_ImpulseNoiseStartDeadTime.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_ImpulseNoiseStartDeadTime.setDescription('Dead Time Value for Impulse Noise Start Test. The value is assigned in 0.1 ms increments.')
cltmCmd_ImpulseNoiseStartTimer = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 16), Integer32()).setLabel("cltmCmd-ImpulseNoiseStartTimer").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_ImpulseNoiseStartTimer.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_ImpulseNoiseStartTimer.setDescription('Timer values for Impulse Noise Start Test. The value is assigned in 1 minute increment.')
cltmCmd_CalibrationType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("insertionLoss", 1), ("backgroundNoise", 2)))).setLabel("cltmCmd-CalibrationType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_CalibrationType.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_CalibrationType.setDescription('Calibration Type')
cltmCmd_ToneSendFreq = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 18), Integer32()).setLabel("cltmCmd-ToneSendFreq").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_ToneSendFreq.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_ToneSendFreq.setDescription('Tone Send Frequency in KHz.')
cltmCmd_ToneSendLevel = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 19), Integer32()).setLabel("cltmCmd-ToneSendLevel").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_ToneSendLevel.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_ToneSendLevel.setDescription('Tone Send Level in dBm.')
cltmCmd_ToneSendPeriod = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 20), Integer32()).setLabel("cltmCmd-ToneSendPeriod").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_ToneSendPeriod.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_ToneSendPeriod.setDescription('Amount of time a tone is sent (1-20 Minutes).')
cltmCmd_TdrUnit = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("metric", 1), ("english", 2)))).setLabel("cltmCmd-TdrUnit").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_TdrUnit.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_TdrUnit.setDescription('Measurement System for TDR Test.')
cltmCmd_TdrGauge = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 22), Integer32()).setLabel("cltmCmd-TdrGauge").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_TdrGauge.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_TdrGauge.setDescription('TDR gauge. This is either 22/24/26 AWG for English system or 6/5/4 (0.1mm) for the metric system.')
cltmCmd_TdrVp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 23), Integer32()).setLabel("cltmCmd-TdrVp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_TdrVp.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_TdrVp.setDescription('TDR VP as percentage of the speed of light.')
cltmCmd_TdrAvg = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 24), Integer32()).setLabel("cltmCmd-TdrAvg").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_TdrAvg.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_TdrAvg.setDescription('Number of trials to get the avarage.')
cltmCmd_TdrGetType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("automatic", 1), ("manual", 2)))).setLabel("cltmCmd-TdrGetType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_TdrGetType.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_TdrGetType.setDescription('TDR Test Range Measurement Type. If set to automatic cltmCmdTdrStartLen and cltmCmdTdrMeasureLen do not need to be set.')
cltmCmd_TdrStartDistance = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 26), Integer32()).setLabel("cltmCmd-TdrStartDistance").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_TdrStartDistance.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_TdrStartDistance.setDescription('TDR Start Length for MANUAL mode, the value is given in feet (15..20000) for the English system and cm (460..609750) for the metric system.')
cltmCmd_TdrMeasurementLength = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 27), Integer32()).setLabel("cltmCmd-TdrMeasurementLength").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_TdrMeasurementLength.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_TdrMeasurementLength.setDescription('TDR Measurement Length for MANUAL mode, the value is given in feet (300..20000) for the English system and cm (9150..609750) for the metric system.')
cltmCmd_DmmdcdPeriod = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 28), Integer32()).setLabel("cltmCmd-DmmdcdPeriod").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_DmmdcdPeriod.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_DmmdcdPeriod.setDescription('Amount of time measurement is made (0,1-5 100ms;0=MAX).')
cltmCmd_DmmdcdVoltage = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 29), Integer32()).setLabel("cltmCmd-DmmdcdVoltage").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_DmmdcdVoltage.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_DmmdcdVoltage.setDescription('Test voltage to be used (-230 to 230 Volts).')
cltmCmd_DmmdcdImpedance = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 30), Integer32()).setLabel("cltmCmd-DmmdcdImpedance").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_DmmdcdImpedance.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_DmmdcdImpedance.setDescription('Output Impedance to be used (10 to 1000 Kohms).')
cltmCmd_DmmcapPeriod = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 31), Integer32()).setLabel("cltmCmd-DmmcapPeriod").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_DmmcapPeriod.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_DmmcapPeriod.setDescription('Amount of time measurement is made (0,1-5 100ms;0=MAX).')
cltmCmd_DmmallType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("resistance", 1), ("dcVoltage", 2), ("acVoltage", 3), ("capacitance", 4)))).setLabel("cltmCmd-DmmallType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_DmmallType.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_DmmallType.setDescription('DMM Measurement Type.')
cltmCmd_DmmallPeriod = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 33), Integer32()).setLabel("cltmCmd-DmmallPeriod").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_DmmallPeriod.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_DmmallPeriod.setDescription('Amount of time measurement is made (0,1-5 100ms;0=MAX).')
cltmCmd_DmmallInputImp = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 34), Integer32()).setLabel("cltmCmd-DmmallInputImp").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_DmmallInputImp.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_DmmallInputImp.setDescription('Input Impedance (100, 1000 Kohm).')
cltmCmd_CtoneType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 35), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("adsl", 1), ("glite", 2)))).setLabel("cltmCmd-CtoneType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_CtoneType.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_CtoneType.setDescription('Control tone, type of DSL service (ADSL, GLITE).')
cltmCmd_CtoneTone = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 36), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("quiet", 1), ("restore", 2)))).setLabel("cltmCmd-CtoneTone").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_CtoneTone.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_CtoneTone.setDescription('Control tone, type of Tone (QUIET, RESTORE).')
cltmCmd_TtoneLead = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 37), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tipRing", 1), ("tipSleeve", 2), ("ringSleeve", 3)))).setLabel("cltmCmd-TtoneLead").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_TtoneLead.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_TtoneLead.setDescription('trace tone, Measurement Leads.')
cltmCmd_TtoneLevel = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 38), Integer32()).setLabel("cltmCmd-TtoneLevel").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_TtoneLevel.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_TtoneLevel.setDescription('trace tone, Tone Send Level in dBm.')
cltmCmd_TtonePeriod = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 39), Integer32()).setLabel("cltmCmd-TtonePeriod").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_TtonePeriod.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_TtonePeriod.setDescription('trace tone, Amount of time a tone is sent (1-20 Minutes).')
cltmCmd_BtapStartLength = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 40), Integer32()).setLabel("cltmCmd-BtapStartLength").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_BtapStartLength.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_BtapStartLength.setDescription('Measurement start length (15 - 20000 ft. or 5 - 6097 meter).')
cltmCmd_BtapMeasureLength = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 41), Integer32()).setLabel("cltmCmd-BtapMeasureLength").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_BtapMeasureLength.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_BtapMeasureLength.setDescription('Measurement length (100 - 20000 ft. or 32 - 6097 meter).')
cltmCmd_FcllocUnit = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 43), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("metric", 1), ("english", 2)))).setLabel("cltmCmd-FcllocUnit").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_FcllocUnit.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_FcllocUnit.setDescription('Measurement System for FCLLOC Test.')
cltmCmd_FcllocGauge = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 44), Integer32()).setLabel("cltmCmd-FcllocGauge").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_FcllocGauge.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_FcllocGauge.setDescription('FCLLOC gauge. This is either 22/24/26 AWG for English system or 6/5/4 (0.1mm) for the metric system.')
cltmCmd_ShortlocUnit = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 45), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("metric", 1), ("english", 2)))).setLabel("cltmCmd-ShortlocUnit").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_ShortlocUnit.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_ShortlocUnit.setDescription('Measurement System for SHORTLOC Test.')
cltmCmd_ShortlocGauge = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 46), Integer32()).setLabel("cltmCmd-ShortlocGauge").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_ShortlocGauge.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_ShortlocGauge.setDescription('SHORTLOC gauge. This is either 22/24/26 AWG for English system or 6/5/4 (0.1mm) for the metric system.')
cltmCmd_ShortlocType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 47), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("detect", 1), ("noDetect", 2)))).setLabel("cltmCmd-ShortlocType").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_ShortlocType.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_ShortlocType.setDescription('SHORTLOC test type.')
cltmCmd_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 66, 1, 1, 42), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("cltmCmd-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: cltmCmd_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: cltmCmd_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBCLTM-MIB", cltmCmd_TdrGetType=cltmCmd_TdrGetType, cltmCmd_DmmallType=cltmCmd_DmmallType, mibcltmCmdTable=mibcltmCmdTable, cltmCmd_DmmdcdPeriod=cltmCmd_DmmdcdPeriod, cltmCmd_CalibrationType=cltmCmd_CalibrationType, cltmCmd_TtonePeriod=cltmCmd_TtonePeriod, cltmCmd_TdrStartDistance=cltmCmd_TdrStartDistance, cltmCmd_DmmallInputImp=cltmCmd_DmmallInputImp, cltmCmd_ShortlocGauge=cltmCmd_ShortlocGauge, cltmCmd_ToneSendFreq=cltmCmd_ToneSendFreq, cltmCmd_DmmLead=cltmCmd_DmmLead, cltmCmd_LoopResistanceUnit=cltmCmd_LoopResistanceUnit, cltmCmd_ShortlocType=cltmCmd_ShortlocType, cltmCmd_DmmallPeriod=cltmCmd_DmmallPeriod, cltmCmd_Index_o=cltmCmd_Index_o, cltmCmd_TdrVp=cltmCmd_TdrVp, cltmCmd_DmmType=cltmCmd_DmmType, cltmCmd_ImpulseNoiseStartMaxCount=cltmCmd_ImpulseNoiseStartMaxCount, mibcltmCmdEntry=mibcltmCmdEntry, cltmCmd_LoopResistanceTemp=cltmCmd_LoopResistanceTemp, cltmCmd_FcllocUnit=cltmCmd_FcllocUnit, mibcltmCmd=mibcltmCmd, cltmCmd_CtoneTone=cltmCmd_CtoneTone, cltmCmd_TestOperation=cltmCmd_TestOperation, cltmCmd_DmmdcdVoltage=cltmCmd_DmmdcdVoltage, cltmCmd_BackgroundNoiseFilter=cltmCmd_BackgroundNoiseFilter, cltmCmd_TdrUnit=cltmCmd_TdrUnit, DisplayString=DisplayString, cltmCmd_ImpulseNoiseStartDelta=cltmCmd_ImpulseNoiseStartDelta, cltmCmd_TestTimeStamp=cltmCmd_TestTimeStamp, cltmCmd_TestSequence=cltmCmd_TestSequence, cltmCmd_ShortlocUnit=cltmCmd_ShortlocUnit, cltmCmd_DmmdcdImpedance=cltmCmd_DmmdcdImpedance, cltmCmd_BackgroundNoiseTermination=cltmCmd_BackgroundNoiseTermination, cltmCmd_FcllocGauge=cltmCmd_FcllocGauge, cltmCmd_BtapMeasureLength=cltmCmd_BtapMeasureLength, cltmCmd_DmmcapPeriod=cltmCmd_DmmcapPeriod, cltmCmd_TdrGauge=cltmCmd_TdrGauge, cltmCmd_TdrMeasurementLength=cltmCmd_TdrMeasurementLength, cltmCmd_ToneSendLevel=cltmCmd_ToneSendLevel, cltmCmd_ImpulseNoiseStartThresh=cltmCmd_ImpulseNoiseStartThresh, cltmCmd_ImpulseNoiseStartTimer=cltmCmd_ImpulseNoiseStartTimer, cltmCmd_TdrAvg=cltmCmd_TdrAvg, cltmCmd_Action_o=cltmCmd_Action_o, cltmCmd_BtapStartLength=cltmCmd_BtapStartLength, cltmCmd_TtoneLead=cltmCmd_TtoneLead, cltmCmd_CtoneType=cltmCmd_CtoneType, cltmCmd_ToneSendPeriod=cltmCmd_ToneSendPeriod, cltmCmd_ImpulseNoiseStartDeadTime=cltmCmd_ImpulseNoiseStartDeadTime, cltmCmd_CltmSlot=cltmCmd_CltmSlot, cltmCmd_TtoneLevel=cltmCmd_TtoneLevel)