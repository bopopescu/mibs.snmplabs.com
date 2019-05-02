#
# PySNMP MIB module USR-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/USR-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:30:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
uchasPowerSupplyIndex, uchasEntityIndex, uchasEntityObjectID, uchasPowerSupplyOutNominalVolt, uchasPowerSupplyOutOfferedVolt, uchasSlotIndex, uchasSlotModuleType = mibBuilder.importSymbols("CHS-MIB", "uchasPowerSupplyIndex", "uchasEntityIndex", "uchasEntityObjectID", "uchasPowerSupplyOutNominalVolt", "uchasPowerSupplyOutOfferedVolt", "uchasSlotIndex", "uchasSlotModuleType")
mdmCsSecurityUserName, mdmCsCallDuration, mdmCsCallRefNum = mibBuilder.importSymbols("MDM-MIB", "mdmCsSecurityUserName", "mdmCsCallDuration", "mdmCsCallRefNum")
nmcGmtime, nmcArTrapId, nmcStatEventId, nmcTrapSequenceNumber, nmcStatTemperature, nmcCfgLogSrvrSelect = mibBuilder.importSymbols("NMC-MIB", "nmcGmtime", "nmcArTrapId", "nmcStatEventId", "nmcTrapSequenceNumber", "nmcStatTemperature", "nmcCfgLogSrvrSelect")
pbSessionIndex, pbSessionErrorStatus = mibBuilder.importSymbols("PB-MIB", "pbSessionIndex", "pbSessionErrorStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, NotificationType, TimeTicks, Gauge32, ModuleIdentity, Bits, enterprises, IpAddress, Unsigned32, MibIdentifier, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "NotificationType", "TimeTicks", "Gauge32", "ModuleIdentity", "Bits", "enterprises", "IpAddress", "Unsigned32", "MibIdentifier", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
uds1StatE1PhysicalState, = mibBuilder.importSymbols("UDS1-MIB", "uds1StatE1PhysicalState")
usr = MibIdentifier((1, 3, 6, 1, 4, 1, 429))
moduleInserted = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,1)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasSlotModuleType"))
if mibBuilder.loadTexts: moduleInserted.setDescription('A card has been inserted into the hub.')
moduleRemoved = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,2)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasSlotModuleType"))
if mibBuilder.loadTexts: moduleRemoved.setDescription('A card has been removed from the hub.')
psuWarning = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,3)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasPowerSupplyOutNominalVolt"), ("CHS-MIB", "uchasPowerSupplyOutOfferedVolt"))
if mibBuilder.loadTexts: psuWarning.setDescription('Power supply voltage out of normal operating range.')
psuFailure = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,4)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasPowerSupplyIndex"))
if mibBuilder.loadTexts: psuFailure.setDescription('Power supply failure.')
tempWarning = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,5)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("NMC-MIB", "nmcStatTemperature"))
if mibBuilder.loadTexts: tempWarning.setDescription('Internal hub temperature out of normal operating range.')
fanFailure = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,6)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"))
if mibBuilder.loadTexts: fanFailure.setDescription('Hub cooling fan failed.')
entityWatchdogTimeout = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,7)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: entityWatchdogTimeout.setDescription('Watchdog timeout detected; indication of software failure.')
entityMgtBusFailure = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,8)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: entityMgtBusFailure.setDescription('Management bus failure. Entity fails to respond to Managment Card.')
incomingConnectionEstablished = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,9)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: incomingConnectionEstablished.setDescription('Incoming connection established on modem.')
outgoingConnectionEstablished = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,10)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: outgoingConnectionEstablished.setDescription('Outgoing connection established on modem.')
incomingConnectionTerminated = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,11)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: incomingConnectionTerminated.setDescription('Incoming connection terminated on modem.')
outgoingConnectionTerminated = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,12)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: outgoingConnectionTerminated.setDescription('Outgoing connection terminated on modem.')
connectAttemptFailure = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,13)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: connectAttemptFailure.setDescription('Modem failed an attempt to connect with another modem.')
connectTimerExpired = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,14)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: connectTimerExpired.setDescription("Modem's connection time limit expired. The connection was terminated.")
dteTransmitDataIdle = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,15)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: dteTransmitDataIdle.setDescription('The DTE connected to this modem has not transmitted anything to this modem for a period longer than its idle time threshold.')
dtrTrue = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,16)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: dtrTrue.setDescription("The attached DTE is asserting the DTR signal in a 'true' condition.")
dtrFalse = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,17)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: dtrFalse.setDescription("The DTE attached to this modem is asserting DTR in a 'false' condition.")
blerCountAtThreshold = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,18)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: blerCountAtThreshold.setDescription("This modem's block error counter has exceeded the defined 'good' threshold during the current call.")
fallbackCountAtThreshold = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,19)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: fallbackCountAtThreshold.setDescription("This modem's fallback counter has exceeded the normal 'good' threshold during the current call.")
noDialtone = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,20))
if mibBuilder.loadTexts: noDialtone.setDescription('The modem has detected a lack of dial tone when it went off hook to dial.')
noLoopCurrent = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,21)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: noLoopCurrent.setDescription('The modem has detected a lack of loop current on the phone line when it went off hook to dial.')
yellowAlarm = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,22)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: yellowAlarm.setDescription("A yellow alarm condition exists when the remote end of a DS1 is experiencing an 'out-of-frame' or 'OOF' condition.")
redAlarm = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,23)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: redAlarm.setDescription("The framing pattern has been lost on the DS1's receiver. This is also known as an 'out-of-frame' or 'OOF' condition.")
lossOfSignal = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,24)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: lossOfSignal.setDescription("The DS1 receiver has received 175 consecutive 0's. The DS1 is unable to recover a receive signal.")
alarmIndicationSignal = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,25)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: alarmIndicationSignal.setDescription('The DS1 is receiving an all ones pattern. This is an indication that the remote end has lost its receive signal. This condition is also known as blue alarm.')
transmitTimingSourceSwitch = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,26)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasSlotModuleType"))
if mibBuilder.loadTexts: transmitTimingSourceSwitch.setDescription('The specified Dual T1 card has switched to an alternate timing source.')
modemResetByDte = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,27)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: modemResetByDte.setDescription('This specific trap is generated when modem is reset by dte.')
modemRingNoAnswer = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,28)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: modemRingNoAnswer.setDescription('If the DTR is present and s0 register on the NAC is not equal to zero, then the Modem Ring No Answer event is generated.')
dteRingNoAnswer = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,29)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: dteRingNoAnswer.setDescription('The DTE Ring No Answer event is generated when the DTR is not present and the s0 register on the NAC is not equal to zero.')
pktBusSessActive = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,30)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("PB-MIB", "pbSessionIndex"))
if mibBuilder.loadTexts: pktBusSessActive.setDescription('Packet bus session active trap.')
pktBusSessCongestion = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,31)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("PB-MIB", "pbSessionIndex"))
if mibBuilder.loadTexts: pktBusSessCongestion.setDescription('Packet bus session congestion trap.')
pktBusSessLost = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,32)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("PB-MIB", "pbSessionIndex"))
if mibBuilder.loadTexts: pktBusSessLost.setDescription('Packet bus session lost trap.')
pktBusSessInactive = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,33)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("PB-MIB", "pbSessionIndex"))
if mibBuilder.loadTexts: pktBusSessInactive.setDescription('Packet bus session inactive trap.')
nacUserInterfaceReset = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,34)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"))
if mibBuilder.loadTexts: nacUserInterfaceReset.setDescription('The NAC has been RESET from the User Interface.')
gwWanPortOutOfService = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,35)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"))
if mibBuilder.loadTexts: gwWanPortOutOfService.setDescription('A gateway WAN port has changed from Link Active to Out of Service.')
gwWanPortLinkActive = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,36)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"))
if mibBuilder.loadTexts: gwWanPortLinkActive.setDescription('A gateway WAN port has changed from Out of Service to Link Active.')
dialOutLoginFail = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,37)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("MDM-MIB", "mdmCsSecurityUserName"))
if mibBuilder.loadTexts: dialOutLoginFail.setDescription('A dial out login security session has failed.')
dialInLoginFail = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,38)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("MDM-MIB", "mdmCsSecurityUserName"))
if mibBuilder.loadTexts: dialInLoginFail.setDescription('A dial in login security session has failed.')
dialOutRestrictedNum = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,39)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("MDM-MIB", "mdmCsSecurityUserName"))
if mibBuilder.loadTexts: dialOutRestrictedNum.setDescription('A dial out security session has failed as a result of attempting to dial a restricted phone number.')
dialBackRestrictedNum = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,40)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("MDM-MIB", "mdmCsSecurityUserName"))
if mibBuilder.loadTexts: dialBackRestrictedNum.setDescription('A dial back security session has failed as a result of attempting to dial a restricted phone number.')
userBlacklisted = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,41)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("MDM-MIB", "mdmCsSecurityUserName"))
if mibBuilder.loadTexts: userBlacklisted.setDescription('A security user has reached their final failed login attempt number and is now being blacklisted.')
loginAttemptByBlacklistedUser = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,42)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("MDM-MIB", "mdmCsSecurityUserName"))
if mibBuilder.loadTexts: loginAttemptByBlacklistedUser.setDescription('A security login attempt by a currently blacklisted user has occurred.')
responseAttemptLimExceeded = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,43)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("MDM-MIB", "mdmCsSecurityUserName"))
if mibBuilder.loadTexts: responseAttemptLimExceeded.setDescription('A security user has failed to issue a valid response to a particular security prompt before the configured limit.')
mdmLoginAttemptLimExceeded = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,44)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("MDM-MIB", "mdmCsSecurityUserName"))
if mibBuilder.loadTexts: mdmLoginAttemptLimExceeded.setDescription('This signals a security session failure when the indicated user does not appear in the security user database.')
dialOutCallDuration = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,45)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("MDM-MIB", "mdmCsSecurityUserName"), ("MDM-MIB", "mdmCsCallDuration"))
if mibBuilder.loadTexts: dialOutCallDuration.setDescription('A dial out call has ended.')
dialInCallDuration = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,46)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("MDM-MIB", "mdmCsSecurityUserName"), ("MDM-MIB", "mdmCsCallDuration"))
if mibBuilder.loadTexts: dialInCallDuration.setDescription('A dial in call has ended.')
pktBusSessError = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,47)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("PB-MIB", "pbSessionIndex"), ("PB-MIB", "pbSessionErrorStatus"))
if mibBuilder.loadTexts: pktBusSessError.setDescription('Packet bus session error trap.')
nmcArCustomTrap = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,48)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("NMC-MIB", "nmcArTrapId"))
if mibBuilder.loadTexts: nmcArCustomTrap.setDescription('NMC AutoResponse SNMP TRAP')
acctSrvrLoss = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,49)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("NMC-MIB", "nmcCfgLogSrvrSelect"))
if mibBuilder.loadTexts: acctSrvrLoss.setDescription('Contact lost with RADIUS accounting server.')
yellowAlarmClear = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,50)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: yellowAlarmClear.setDescription('A yellow alarm condition has been cleared.')
redAlarmClear = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,51)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: redAlarmClear.setDescription('The red alarm condition has been cleared.')
lossOfSignalClear = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,52)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: lossOfSignalClear.setDescription('The loss of signal condition has been cleared.')
alarmIndicationSignalClear = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,53)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: alarmIndicationSignalClear.setDescription('The blue alarm condition has been cleared.')
ctIncomingConnectionEstablished = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,54)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"), ("MDM-MIB", "mdmCsCallRefNum"))
if mibBuilder.loadTexts: ctIncomingConnectionEstablished.setDescription('Incoming connection established on modem.')
ctOutgoingConnectionEstablished = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,55)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"), ("MDM-MIB", "mdmCsCallRefNum"))
if mibBuilder.loadTexts: ctOutgoingConnectionEstablished.setDescription('Outgoing connection established on modem.')
ctIncomingConnectionTerminated = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,56)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"), ("MDM-MIB", "mdmCsCallRefNum"))
if mibBuilder.loadTexts: ctIncomingConnectionTerminated.setDescription('Incoming connection terminated on modem.')
ctOutgoingConnectionTerminated = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,57)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"), ("MDM-MIB", "mdmCsCallRefNum"))
if mibBuilder.loadTexts: ctOutgoingConnectionTerminated.setDescription('Outgoing connection terminated on modem.')
ctConnectAttemptFailure = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,58)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"), ("MDM-MIB", "mdmCsCallRefNum"))
if mibBuilder.loadTexts: ctConnectAttemptFailure.setDescription('Modem failed an attempt to connect with another modem.')
contCrcAlarm = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,59)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: contCrcAlarm.setDescription('A continuous CRC error condition has occurred on the DS1.')
contCrcAlarmClear = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,60)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"))
if mibBuilder.loadTexts: contCrcAlarmClear.setDescription('A continuous CRC error condition has cleared on the DS1.')
phyStateChng = NotificationType((1, 3, 6, 1, 4, 1, 429) + (0,61)).setObjects(("NMC-MIB", "nmcTrapSequenceNumber"), ("NMC-MIB", "nmcStatEventId"), ("NMC-MIB", "nmcGmtime"), ("CHS-MIB", "uchasSlotIndex"), ("CHS-MIB", "uchasEntityIndex"), ("CHS-MIB", "uchasEntityObjectID"), ("UDS1-MIB", "uds1StatE1PhysicalState"))
if mibBuilder.loadTexts: phyStateChng.setDescription('A physical state change has occurred on the DS1.')
mibBuilder.exportSymbols("USR-TRAP-MIB", redAlarm=redAlarm, dialOutLoginFail=dialOutLoginFail, alarmIndicationSignal=alarmIndicationSignal, pktBusSessInactive=pktBusSessInactive, ctIncomingConnectionTerminated=ctIncomingConnectionTerminated, yellowAlarm=yellowAlarm, loginAttemptByBlacklistedUser=loginAttemptByBlacklistedUser, ctConnectAttemptFailure=ctConnectAttemptFailure, fallbackCountAtThreshold=fallbackCountAtThreshold, modemRingNoAnswer=modemRingNoAnswer, pktBusSessLost=pktBusSessLost, dialBackRestrictedNum=dialBackRestrictedNum, dteRingNoAnswer=dteRingNoAnswer, dtrTrue=dtrTrue, acctSrvrLoss=acctSrvrLoss, lossOfSignalClear=lossOfSignalClear, ctOutgoingConnectionTerminated=ctOutgoingConnectionTerminated, contCrcAlarm=contCrcAlarm, redAlarmClear=redAlarmClear, blerCountAtThreshold=blerCountAtThreshold, transmitTimingSourceSwitch=transmitTimingSourceSwitch, incomingConnectionEstablished=incomingConnectionEstablished, pktBusSessError=pktBusSessError, contCrcAlarmClear=contCrcAlarmClear, mdmLoginAttemptLimExceeded=mdmLoginAttemptLimExceeded, outgoingConnectionEstablished=outgoingConnectionEstablished, gwWanPortOutOfService=gwWanPortOutOfService, alarmIndicationSignalClear=alarmIndicationSignalClear, dialInCallDuration=dialInCallDuration, pktBusSessCongestion=pktBusSessCongestion, yellowAlarmClear=yellowAlarmClear, dialOutCallDuration=dialOutCallDuration, usr=usr, gwWanPortLinkActive=gwWanPortLinkActive, phyStateChng=phyStateChng, moduleInserted=moduleInserted, responseAttemptLimExceeded=responseAttemptLimExceeded, dteTransmitDataIdle=dteTransmitDataIdle, nacUserInterfaceReset=nacUserInterfaceReset, tempWarning=tempWarning, ctIncomingConnectionEstablished=ctIncomingConnectionEstablished, outgoingConnectionTerminated=outgoingConnectionTerminated, dialInLoginFail=dialInLoginFail, incomingConnectionTerminated=incomingConnectionTerminated, fanFailure=fanFailure, psuWarning=psuWarning, connectTimerExpired=connectTimerExpired, noDialtone=noDialtone, pktBusSessActive=pktBusSessActive, userBlacklisted=userBlacklisted, psuFailure=psuFailure, dtrFalse=dtrFalse, lossOfSignal=lossOfSignal, moduleRemoved=moduleRemoved, modemResetByDte=modemResetByDte, nmcArCustomTrap=nmcArCustomTrap, noLoopCurrent=noLoopCurrent, entityWatchdogTimeout=entityWatchdogTimeout, entityMgtBusFailure=entityMgtBusFailure, dialOutRestrictedNum=dialOutRestrictedNum, connectAttemptFailure=connectAttemptFailure, ctOutgoingConnectionEstablished=ctOutgoingConnectionEstablished)