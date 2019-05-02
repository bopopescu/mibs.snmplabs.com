#
# PySNMP MIB module CISCO-DMN-DSG-AUDIO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DMN-DSG-AUDIO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:54:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, iso, Counter32, NotificationType, Unsigned32, Bits, Gauge32, ObjectIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "Counter32", "NotificationType", "Unsigned32", "Bits", "Gauge32", "ObjectIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "ModuleIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDSGAudio = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15))
ciscoDSGAudio.setRevisions(('2013-07-10 12:20', '2012-03-07 05:00', '2010-08-30 05:00', '2010-05-24 06:30', '2010-05-21 16:45', '2010-04-12 05:00', '2010-03-22 05:00', '2010-02-12 15:00', '2009-12-07 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGAudio.setRevisionsDescriptions(('V01.00.08 2013-07-10 Updated audioLangList DESCRIPTION clause.', 'V01.00.07 2012-03-07 Updated for D9854 R4 Release.', 'V01.00.06 2010-08-30 Updated for adherence to SNMPv2 format.', 'V01.00.05 2010-05-24 The names of audioAC3Comp and audioDDPMode are changed to audioDolbyDigitalComp audioDolbyDigitalPlusMode respectively.', 'V01.00.04 2010-05-21 The enumerations of Audio PMT source item updated.', 'V01.00.03 2010-04-12 The objects audioDigitalComp and audioDDPMode are updated.', 'V01.00.02 2010-03-22 The Syntax of Unsigned32 MIB objects whose range is within the range of Integer32, is updated to Integer32.', 'V01.00.01 2010-02-12 The Syntax of read-only objects is updated to DisplayString.', 'V01.00.00 2009-12-07 Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGAudio.setLastUpdated('201307101220Z')
if mibBuilder.loadTexts: ciscoDSGAudio.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGAudio.setContactInfo('Cisco Systems, Inc. Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553 NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGAudio.setDescription('Cisco Audio Control MIB.')
audioCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1), )
if mibBuilder.loadTexts: audioCtrlTable.setStatus('current')
if mibBuilder.loadTexts: audioCtrlTable.setDescription('Audio decoder information')
audioCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1), ).setIndexNames((0, "CISCO-DMN-DSG-AUDIO-MIB", "audioSelKey"))
if mibBuilder.loadTexts: audioCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: audioCtrlEntry.setDescription('Entry for audio channel is being viewed/edited.')
audioSelKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: audioSelKey.setStatus('current')
if mibBuilder.loadTexts: audioSelKey.setDescription('Selects which audio channel is being viewed/edited.')
audioMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("stereo", 1), ("mixed", 2), ("lMono", 3), ("rMono", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: audioMode.setStatus('current')
if mibBuilder.loadTexts: audioMode.setDescription('Audio Mode: Stereo/Mixed/R-Mono/L-Mono.')
audioDolbyDigitalComp = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 3))).clone(namedValues=NamedValues(("rfMode", 1), ("lineMode", 2), ("custom0", 4), ("custom1", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: audioDolbyDigitalComp.setStatus('current')
if mibBuilder.loadTexts: audioDolbyDigitalComp.setDescription('Dolby Digital (AC3) compression: RF Mode/Line/custom0/custom1 .')
audioConsumerVolLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: audioConsumerVolLeft.setStatus('current')
if mibBuilder.loadTexts: audioConsumerVolLeft.setDescription('Set Consumer Left Audio Volume: 0 to 60dB.')
audioConsumerVolRight = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: audioConsumerVolRight.setStatus('current')
if mibBuilder.loadTexts: audioConsumerVolRight.setDescription('Set Consumer Right Audio Volume: 0 to 60dB.')
audioProfAttenuationLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: audioProfAttenuationLeft.setStatus('current')
if mibBuilder.loadTexts: audioProfAttenuationLeft.setDescription('Set Professional Attenuation Left: ')
audioProfAttenuationRight = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: audioProfAttenuationRight.setStatus('current')
if mibBuilder.loadTexts: audioProfAttenuationRight.setDescription('Set Professional Attenuation Right: ')
audioPmtSource = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65))).clone(namedValues=NamedValues(("none", 1), ("aud1", 2), ("aud2", 3), ("aud3", 4), ("aud4", 5), ("aud5", 6), ("aud6", 7), ("aud7", 8), ("aud8", 9), ("aud9", 10), ("aud10", 11), ("aud11", 12), ("aud12", 13), ("aud13", 14), ("aud14", 15), ("aud15", 16), ("aud16", 17), ("aud17", 18), ("aud18", 19), ("aud19", 20), ("aud20", 21), ("aud21", 22), ("aud22", 23), ("aud23", 24), ("aud24", 25), ("aud25", 26), ("aud26", 27), ("aud27", 28), ("aud28", 29), ("aud29", 30), ("aud30", 31), ("aud31", 32), ("aud32", 33), ("aud33", 34), ("aud34", 35), ("aud35", 36), ("aud36", 37), ("aud37", 38), ("aud38", 39), ("aud39", 40), ("aud40", 41), ("aud41", 42), ("aud42", 43), ("aud43", 44), ("aud44", 45), ("aud45", 46), ("aud46", 47), ("aud47", 48), ("aud48", 49), ("aud49", 50), ("aud50", 51), ("aud51", 52), ("aud52", 53), ("aud53", 54), ("aud54", 55), ("aud55", 56), ("aud56", 57), ("aud57", 58), ("aud58", 59), ("aud59", 60), ("aud60", 61), ("aud61", 62), ("aud62", 63), ("aud63", 64), ("aud64", 65)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: audioPmtSource.setStatus('current')
if mibBuilder.loadTexts: audioPmtSource.setDescription('PMT audio PID: AUD1/AUD2/AUD3/AUD4/.../AUD64/None.')
audioMuted = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: audioMuted.setStatus('current')
if mibBuilder.loadTexts: audioMuted.setDescription('Mute or Unmute Audio.')
audioDigitalComp = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pcm", 1), ("compressed", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: audioDigitalComp.setStatus('current')
if mibBuilder.loadTexts: audioDigitalComp.setDescription('Audio Format: Dolby Digital/PCM/Compressed.')
audioDolbyDigitalPlusMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("transcoding", 1), ("passthrough", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: audioDolbyDigitalPlusMode.setStatus('current')
if mibBuilder.loadTexts: audioDolbyDigitalPlusMode.setDescription('Audio DDP(Dolby Digital Plus) Mode.')
audioLangMenu = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("languageList", 1), ("languageEntry", 2), ("pmtOrder", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: audioLangMenu.setStatus('current')
if mibBuilder.loadTexts: audioLangMenu.setDescription('Select whether to chose the language based on the selection from the language list, from the PMT order, or from manual entry.')
audioLangList = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43))).clone(namedValues=NamedValues(("ara", 1), ("btk", 2), ("ben", 3), ("bul", 4), ("chi", 5), ("cze", 6), ("dan", 7), ("dut", 8), ("eng", 9), ("fin", 10), ("fre", 11), ("ger", 12), ("gre", 13), ("heb", 14), ("hin", 15), ("hun", 16), ("ice", 17), ("ind", 18), ("ita", 19), ("jpn", 20), ("kor", 21), ("may", 22), ("mul", 23), ("nor", 24), ("per", 25), ("pol", 26), ("por", 27), ("rum", 28), ("rus", 29), ("san", 30), ("scc", 31), ("sin", 32), ("slo", 33), ("slv", 34), ("som", 35), ("spa", 36), ("swe", 37), ("tai", 38), ("tam", 39), ("tha", 40), ("tur", 41), ("ukr", 42), ("vie", 43)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: audioLangList.setStatus('current')
if mibBuilder.loadTexts: audioLangList.setDescription('Audio Language List. Language option slv(34) is only supported on D9865.')
audioManualEntry = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: audioManualEntry.setStatus('current')
if mibBuilder.loadTexts: audioManualEntry.setDescription('Audio Manual Entry.')
audioStatusTable = MibTable((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2), )
if mibBuilder.loadTexts: audioStatusTable.setStatus('current')
if mibBuilder.loadTexts: audioStatusTable.setDescription('Audio Status Table.')
audioStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1), ).setIndexNames((0, "CISCO-DMN-DSG-AUDIO-MIB", "audioStatusSelKey"))
if mibBuilder.loadTexts: audioStatusEntry.setStatus('current')
if mibBuilder.loadTexts: audioStatusEntry.setDescription('Entry for audio channel is being viewed.')
audioStatusSelKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1)))
if mibBuilder.loadTexts: audioStatusSelKey.setStatus('current')
if mibBuilder.loadTexts: audioStatusSelKey.setDescription('Selects which audio channel is being viewed.')
audioStatusFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("none", 1), ("sine", 2), ("pink", 3), ("beep", 4), ("mpeg1L1", 5), ("mpeg1L2", 6), ("mpeg2L1", 7), ("mpeg2L2", 8), ("dolbyDigital", 9), ("loasAAC", 10), ("adtsAAC", 11), ("dolbyDigitalPlus", 12), ("adtsHEAAC", 13), ("loasHEAAC", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: audioStatusFormat.setStatus('current')
if mibBuilder.loadTexts: audioStatusFormat.setDescription('Audio Format.')
audioStatusBitRate = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: audioStatusBitRate.setStatus('current')
if mibBuilder.loadTexts: audioStatusBitRate.setDescription('Audio Bitrate in Kilo bits(Kbits).The range is from 0 to 4294967295 Kbits in steps of 1 Kbits.')
audioStatusBufferLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: audioStatusBufferLevel.setStatus('current')
if mibBuilder.loadTexts: audioStatusBufferLevel.setDescription('Level of audio input buffer in bytes.The range is from 0 to 4294967295 bytes in steps of 1 byte.')
audioStatusSFR = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: audioStatusSFR.setStatus('current')
if mibBuilder.loadTexts: audioStatusSFR.setDescription('Audio sampling frequency in Hz.The range is from 0 to 4294967295 bytes in steps of 1 Hz.')
audioStatusMuted = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: audioStatusMuted.setStatus('current')
if mibBuilder.loadTexts: audioStatusMuted.setDescription('Current Mute State.')
audioStatusLanguage = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: audioStatusLanguage.setStatus('current')
if mibBuilder.loadTexts: audioStatusLanguage.setDescription('Audio Language.')
audioStatusDDPMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("ddp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: audioStatusDDPMode.setStatus('current')
if mibBuilder.loadTexts: audioStatusDDPMode.setDescription('Audio DDP Mode.')
audioStatusDualMonoMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("dualMono", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: audioStatusDualMonoMode.setStatus('current')
if mibBuilder.loadTexts: audioStatusDualMonoMode.setDescription('Dualmono Mode.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-AUDIO-MIB", audioProfAttenuationLeft=audioProfAttenuationLeft, audioCtrlTable=audioCtrlTable, audioProfAttenuationRight=audioProfAttenuationRight, audioCtrlEntry=audioCtrlEntry, ciscoDSGAudio=ciscoDSGAudio, PYSNMP_MODULE_ID=ciscoDSGAudio, audioStatusMuted=audioStatusMuted, audioSelKey=audioSelKey, audioStatusSFR=audioStatusSFR, audioStatusDualMonoMode=audioStatusDualMonoMode, audioDolbyDigitalPlusMode=audioDolbyDigitalPlusMode, audioConsumerVolLeft=audioConsumerVolLeft, audioDigitalComp=audioDigitalComp, audioMode=audioMode, audioStatusDDPMode=audioStatusDDPMode, audioManualEntry=audioManualEntry, audioConsumerVolRight=audioConsumerVolRight, audioDolbyDigitalComp=audioDolbyDigitalComp, audioLangList=audioLangList, audioMuted=audioMuted, audioStatusFormat=audioStatusFormat, audioStatusEntry=audioStatusEntry, audioStatusSelKey=audioStatusSelKey, audioPmtSource=audioPmtSource, audioStatusLanguage=audioStatusLanguage, audioStatusTable=audioStatusTable, audioLangMenu=audioLangMenu, audioStatusBitRate=audioStatusBitRate, audioStatusBufferLevel=audioStatusBufferLevel)