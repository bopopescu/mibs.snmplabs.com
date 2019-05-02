#
# PySNMP MIB module REDLINE-E1T1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDLINE-E1T1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:55:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Bits, Counter32, Gauge32, NotificationType, TimeTicks, Counter64, ObjectIdentity, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, enterprises, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "Counter32", "Gauge32", "NotificationType", "TimeTicks", "Counter64", "ObjectIdentity", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "enterprises", "Integer32", "NotificationType")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
redline = MibIdentifier((1, 3, 6, 1, 4, 1, 10728))
redlineProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 1))
redlineMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2))
redlineE1T1 = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 52))
e1t1General = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 52, 1))
e1t1Stats = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 52, 5))
e1t1Commands = MibIdentifier((1, 3, 6, 1, 4, 1, 10728, 2, 52, 6))
e1t1VlanIdData = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1VlanIdData.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1VlanIdData.setDescription('VLAN ID for data on E1/T1 module')
e1t1VlanIdVoice = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1VlanIdVoice.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1VlanIdVoice.setDescription('VLAN ID for voice on E1/T1 module')
e1t1Clock = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1Clock.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1Clock.setDescription('Clocking information on the E1/T1 module')
e1t1SyncOn = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1SyncOn.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1SyncOn.setDescription('The number of serial interface to be used as clocking reference. For AN-50 the number of serial interfaces is 4')
e1t1IdleCode = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1IdleCode.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1IdleCode.setDescription(' Idle Code for unused timeslots on the E1/T1 module')
e1t1Hostname = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1Hostname.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1Hostname.setDescription('E1/T1 host name')
e1t1IpAddress = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1IpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1IpAddress.setDescription('E1/T1 IP address')
e1t1IpMask = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1IpMask.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1IpMask.setDescription('E1/T1 IP mask')
e1t1IpGateway = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1IpGateway.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1IpGateway.setDescription('E1/T1 gateway.')
e1t1OptionKey = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1OptionKey.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1OptionKey.setDescription('E1/T1 Option Key.')
e1t1Line = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1Line.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1Line.setDescription('The type of the line (T1/E1).')
e1t1SoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1SoftwareVersion.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1SoftwareVersion.setDescription('E1/T1 module Software Version.')
e1t1SaveConfig = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("donothing", 1), ("saveConfig", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1SaveConfig.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1SaveConfig.setDescription('Save the running configuration in flash.')
e1t1ActivateConfig = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 6, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("donothing", 1), ("activeConfig", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1ActivateConfig.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1ActivateConfig.setDescription('Activate temporary configuration in running configuration.')
e1t1ResetBoard = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 6, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("donothing", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1ResetBoard.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1ResetBoard.setDescription('Reset the E1/T1 module.')
e1t1ResetStats = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 6, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 35))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1ResetStats.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1ResetStats.setDescription('Reset Statistics for the E1/T1 module.')
e1t1ReStartConfig = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 6, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("donothing", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1ReStartConfig.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1ReStartConfig.setDescription('ReStart the configuration operation for the E1/T1 module.')
e1t1EthRate = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1EthRate.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1EthRate.setDescription('Ethernet rate for the E1/T1 module. 0 = 10 Mbps 1 = 100 Mbps')
e1t1EthMode = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1EthMode.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1EthMode.setDescription('E1/T1 module mode. 0 - half duplex 1 - full duplex')
e1t1EthState = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 5, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1EthState.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1EthState.setDescription('E1/T1 module state. 0 - not connected 1 - connected')
e1t1EthMAC = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 5, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1EthMAC.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1EthMAC.setDescription('E1/T1 module MAC Address.')
e1t1EthFROK = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 5, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1EthFROK.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1EthFROK.setDescription('E1/T1 module frames received OK (FROK).')
e1t1EthBROK = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 5, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1EthBROK.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1EthBROK.setDescription('E1/T1 module bytes received OK (BROK).')
e1t1EthAERR = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 5, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1EthAERR.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1EthAERR.setDescription('E1/T1 module alignment errors (AERR).')
e1t1EthCERR = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 5, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1EthCERR.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1EthCERR.setDescription('E1/T1 module CRC errors (CERR).')
e1t1EthFTOK = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 5, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1EthFTOK.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1EthFTOK.setDescription('E1/T1 module frames transmitted OK (FTOK).')
e1t1EthBTOK = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 5, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1EthBTOK.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1EthBTOK.setDescription('E1/T1 module bytes transmitted OK (BTOK).')
e1t1EthSCOL = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 5, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1EthSCOL.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1EthSCOL.setDescription('E1/T1 module single collisions (SCOL).')
e1t1EthMCOL = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 5, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1EthMCOL.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1EthMCOL.setDescription('E1/T1 module multiple collisions (MCOL).')
e1t1EthTDEF = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 5, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1EthTDEF.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1EthTDEF.setDescription('E1/T1 module transmissions deferred (TDEF).')
e1t1EthLCOL = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 5, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1EthLCOL.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1EthLCOL.setDescription('E1/T1 module late collisions (LCOL).')
e1t1FanStatus = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 5, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1FanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1FanStatus.setDescription('T1E1 Fan Status (off/on).')
e1t1LastSaveErr = MibScalar((1, 3, 6, 1, 4, 1, 10728, 2, 52, 5, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1LastSaveErr.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1LastSaveErr.setDescription('The Error code from the last TDM SAVE Command.')
e1t1SerialTable = MibTable((1, 3, 6, 1, 4, 1, 10728, 2, 52, 2), )
if mibBuilder.loadTexts: e1t1SerialTable.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1SerialTable.setDescription('Table T1 / E1 Channels.')
e1t1SerialEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10728, 2, 52, 2, 1), ).setIndexNames((0, "REDLINE-E1T1-MIB", "e1t1SerialID"))
if mibBuilder.loadTexts: e1t1SerialEntry.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1SerialEntry.setDescription('A unique set of link parameters.')
e1t1SerialID = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1SerialID.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1SerialID.setDescription('Serial ID.')
e1t1SerialCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1SerialCoding.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1SerialCoding.setDescription('Serial Coding.')
e1t1SerialFraming = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1SerialFraming.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1SerialFraming.setDescription('Serial Framing.')
e1t1SerialLBO = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1SerialLBO.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1SerialLBO.setDescription('Serial LBO.')
e1t1GroupTable = MibTable((1, 3, 6, 1, 4, 1, 10728, 2, 52, 3), )
if mibBuilder.loadTexts: e1t1GroupTable.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1GroupTable.setDescription('Table E1 Groups.')
e1t1GroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10728, 2, 52, 3, 1), ).setIndexNames((0, "REDLINE-E1T1-MIB", "e1t1GroupID"))
if mibBuilder.loadTexts: e1t1GroupEntry.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1GroupEntry.setDescription('A unique set of link parameters.')
e1t1GroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1GroupID.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1GroupID.setDescription('Group ID.')
e1t1GroupTsBegin = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1GroupTsBegin.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1GroupTsBegin.setDescription('Group Ts Begin.')
e1t1GroupTsNum = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1GroupTsNum.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1GroupTsNum.setDescription('Group Ts Num.')
e1t1GroupDestGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1GroupDestGroup.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1GroupDestGroup.setDescription('Group Destination.')
e1t1GroupDestIp = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 3, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1GroupDestIp.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1GroupDestIp.setDescription('Group Destination Ip Address.')
e1t1GroupJitterBuffer = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1GroupJitterBuffer.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1GroupJitterBuffer.setDescription('Group Jitter Buffer in ms.')
e1t1GroupPacketLength = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1GroupPacketLength.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1GroupPacketLength.setDescription('Group Jitter Buffer in bytes.')
e1t1GroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 3, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: e1t1GroupRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1GroupRowStatus.setDescription('Status of the row.')
e1t1StatsTable = MibTable((1, 3, 6, 1, 4, 1, 10728, 2, 52, 4), )
if mibBuilder.loadTexts: e1t1StatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1StatsTable.setDescription('Table of statistics for E1/T1 interfaces.')
e1t1StatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10728, 2, 52, 4, 1), ).setIndexNames((0, "REDLINE-E1T1-MIB", "e1t1SerialStatsID"))
if mibBuilder.loadTexts: e1t1StatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1StatsEntry.setDescription('A unique set of statistics of link parameters.')
e1t1SerialStatsID = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1SerialStatsID.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1SerialStatsID.setDescription('Serial Interface Statistics ID.')
e1t1TdmsLOS = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1TdmsLOS.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1TdmsLOS.setDescription('E1/T1 module loss of signal.')
e1t1TdmsLFA = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1TdmsLFA.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1TdmsLFA.setDescription('E1/T1 module loss of framing alignment.')
e1t1TdmsLOMF = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1TdmsLOMF.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1TdmsLOMF.setDescription('E1/T1 module loss of multiframming.')
e1t1TdmsRAI = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1TdmsRAI.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1TdmsRAI.setDescription('E1/T1 module remote alarm indication.')
e1t1TdmsAIS = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1TdmsAIS.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1TdmsAIS.setDescription('E1/T1 module alarm indication signal.')
e1t1TdmsES = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1TdmsES.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1TdmsES.setDescription('E1/T1 module errored seconds.')
e1t1TdmsFEC = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1TdmsFEC.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1TdmsFEC.setDescription('E1/T1 module framing error counter.')
e1t1TdmsCVC = MibTableColumn((1, 3, 6, 1, 4, 1, 10728, 2, 52, 4, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: e1t1TdmsCVC.setStatus('mandatory')
if mibBuilder.loadTexts: e1t1TdmsCVC.setDescription('E1/T1 module code violation counter.')
mibBuilder.exportSymbols("REDLINE-E1T1-MIB", e1t1IdleCode=e1t1IdleCode, e1t1GroupTable=e1t1GroupTable, e1t1SoftwareVersion=e1t1SoftwareVersion, e1t1TdmsAIS=e1t1TdmsAIS, e1t1TdmsLFA=e1t1TdmsLFA, e1t1EthRate=e1t1EthRate, e1t1GroupID=e1t1GroupID, e1t1GroupDestIp=e1t1GroupDestIp, e1t1IpMask=e1t1IpMask, e1t1SerialID=e1t1SerialID, e1t1SerialLBO=e1t1SerialLBO, e1t1EthMAC=e1t1EthMAC, e1t1Hostname=e1t1Hostname, e1t1IpGateway=e1t1IpGateway, e1t1EthCERR=e1t1EthCERR, e1t1GroupJitterBuffer=e1t1GroupJitterBuffer, e1t1GroupPacketLength=e1t1GroupPacketLength, e1t1Line=e1t1Line, e1t1GroupTsNum=e1t1GroupTsNum, e1t1VlanIdVoice=e1t1VlanIdVoice, e1t1Stats=e1t1Stats, e1t1GroupTsBegin=e1t1GroupTsBegin, e1t1Clock=e1t1Clock, e1t1General=e1t1General, redline=redline, e1t1TdmsLOMF=e1t1TdmsLOMF, e1t1TdmsFEC=e1t1TdmsFEC, e1t1TdmsCVC=e1t1TdmsCVC, e1t1SerialCoding=e1t1SerialCoding, e1t1ActivateConfig=e1t1ActivateConfig, e1t1ResetStats=e1t1ResetStats, e1t1EthSCOL=e1t1EthSCOL, e1t1GroupRowStatus=e1t1GroupRowStatus, e1t1EthTDEF=e1t1EthTDEF, e1t1SerialStatsID=e1t1SerialStatsID, e1t1EthBROK=e1t1EthBROK, e1t1EthLCOL=e1t1EthLCOL, e1t1Commands=e1t1Commands, e1t1OptionKey=e1t1OptionKey, e1t1EthAERR=e1t1EthAERR, redlineMgmt=redlineMgmt, e1t1IpAddress=e1t1IpAddress, e1t1EthFROK=e1t1EthFROK, e1t1EthMode=e1t1EthMode, e1t1FanStatus=e1t1FanStatus, e1t1SaveConfig=e1t1SaveConfig, e1t1LastSaveErr=e1t1LastSaveErr, e1t1EthFTOK=e1t1EthFTOK, e1t1TdmsRAI=e1t1TdmsRAI, e1t1EthMCOL=e1t1EthMCOL, e1t1ReStartConfig=e1t1ReStartConfig, e1t1EthBTOK=e1t1EthBTOK, e1t1VlanIdData=e1t1VlanIdData, e1t1SerialEntry=e1t1SerialEntry, e1t1EthState=e1t1EthState, redlineE1T1=redlineE1T1, e1t1SyncOn=e1t1SyncOn, e1t1SerialTable=e1t1SerialTable, e1t1ResetBoard=e1t1ResetBoard, e1t1TdmsES=e1t1TdmsES, e1t1SerialFraming=e1t1SerialFraming, e1t1GroupDestGroup=e1t1GroupDestGroup, e1t1GroupEntry=e1t1GroupEntry, e1t1TdmsLOS=e1t1TdmsLOS, e1t1StatsEntry=e1t1StatsEntry, redlineProducts=redlineProducts, e1t1StatsTable=e1t1StatsTable)