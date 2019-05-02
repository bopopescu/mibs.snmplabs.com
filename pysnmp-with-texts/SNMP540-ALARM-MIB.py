#
# PySNMP MIB module SNMP540-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP540-ALARM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:08:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
snmp540, = mibBuilder.importSymbols("SNMP540-MGMT-MIB", "snmp540")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Gauge32, Counter32, Unsigned32, NotificationType, Counter64, ObjectIdentity, NotificationType, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "Counter32", "Unsigned32", "NotificationType", "Counter64", "ObjectIdentity", "NotificationType", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "ModuleIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
snmp540Alarm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 4, 10))
snmp540AlarmMIBversion = MibScalar((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmp540AlarmMIBversion.setStatus('mandatory')
if mibBuilder.loadTexts: snmp540AlarmMIBversion.setDescription("Identifies the version of the MIB. The format of the version is x.yzT, where 'x' identifies the major revision number, 'y'identifies the minor revision number, 'z' identifies the typographical revision, and T identifies the test revision. Acceptable values for the individual revision components are as follows x: 1 - 9 y: 0 - 9 z: 0 - 9 T: A - Z Upon formal release, no designation for the test revision will be present.")
snmp540AlarmStructure = MibScalar((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("gdcProprietarySCMStandard", 1), ("generalAlarmStructure", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmp540AlarmStructure.setStatus('mandatory')
if mibBuilder.loadTexts: snmp540AlarmStructure.setDescription('The Alarm Structure configuration object. The default value GDCProprietarySCMStandard(1) uses the alarm reporting structure as compliant to the SCM and the GDC proprietary manager applications. The value GeneralAlarmStructure(2) uses a very general alarm structure suited for any Network manager applications .')
snmp540AlarmNumber = MibScalar((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmp540AlarmNumber.setStatus('mandatory')
if mibBuilder.loadTexts: snmp540AlarmNumber.setDescription('The number of Alarms Currently being reported by SNMP540 Unit.')
snmp540GeneralIntegrationTime = MibScalar((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmp540GeneralIntegrationTime.setStatus('mandatory')
if mibBuilder.loadTexts: snmp540GeneralIntegrationTime.setDescription('This is the DDS Alarm Threshold Interval. It specifies the amount of time, 1 to 15 minutes, in which the threshold setting is to be exceeded for the alarm to occur.')
snmp540AlarmTable = MibTable((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5), )
if mibBuilder.loadTexts: snmp540AlarmTable.setStatus('mandatory')
if mibBuilder.loadTexts: snmp540AlarmTable.setDescription('The GDC snmp540 Alarm Configuration Table.')
snmp540AlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1), ).setIndexNames((0, "SNMP540-ALARM-MIB", "alarmNumber"))
if mibBuilder.loadTexts: snmp540AlarmEntry.setStatus('mandatory')
if mibBuilder.loadTexts: snmp540AlarmEntry.setDescription('An entry in the snmp540 alarm table.')
alarmNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmNumber.setStatus('mandatory')
if mibBuilder.loadTexts: alarmNumber.setDescription('The index number associated with the entry in the Alarm table. The range cannot be specified on the SYNTAX line since it will vary from agent to agent. The range will be 1 to the number specified by snmp540AlarmNumber.')
description = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: description.setStatus('mandatory')
if mibBuilder.loadTexts: description.setDescription('The Description of the alarm generated.')
severityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("warning", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: severityLevel.setStatus('mandatory')
if mibBuilder.loadTexts: severityLevel.setDescription('The severity level associated with the alarm in the Alarm table. The value critical(1) is critical for the enterprise functioning. The value major(1), minor(2), warniing(3) indicates otherwise as specified by enterprise.')
pysmi_class = MibScalar((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("general", 1), ("threshold", 2), ("countWindow", 3), ("thresholdInterval", 4)))).setLabel("class").setMaxAccess("readonly")
if mibBuilder.loadTexts: pysmi_class.setStatus('mandatory')
if mibBuilder.loadTexts: pysmi_class.setDescription('The class of the associated alarm in the Alarm table. The value general(1) indicates without the threshold or interval. The value threshold (2) indicates the alarm has threshold value only. The value countWindow (3) indicates the alarm has Count Window value only. The value thresholdInterval (4) indicates the alarm has both the interval and the Count Window also.')
mask = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mask", 1), ("unmask", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mask.setStatus('mandatory')
if mibBuilder.loadTexts: mask.setDescription('The alarm masking control. When the value is mask(1), then the alarm is masked and will not be reported. When the value is unmask(2), then the alarm will be reported depending on the threshold configuration.')
threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-50, 99))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: threshold.setStatus('mandatory')
if mibBuilder.loadTexts: threshold.setDescription("This function sets/reads the alarm threshold settings criteria. This threshold is used along with the alarm window to determine the number of instances in a given time frame for an alarm to occur before the alarm is considered active. Alarm Table Entry Range Default ------- ---------------- --------- -------- Jitter snmp540JitterAlm 0 to 99% 10% BPV's snmp540BpvAlm 0 to 99Count 10 Frm Loss snmp540FrameLossAlm 0 to 99Count 10 SNRatio snmp540SignalToNoiseAlm 0 to 50 0 Rx Low snmp540RxSignalLowAlm -50 to 6db -30dB")
status = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 4, 10, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: status.setStatus('mandatory')
if mibBuilder.loadTexts: status.setDescription('The current status of the alarm. The value inactive(1) indicates that this alarm is currently inactive. The value active(2) indicates that this alarm is currently active.')
snmp540AlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 498, 8, 4) + (0,1)).setObjects(("SNMP540-ALARM-MIB", "description"), ("SNMP540-ALARM-MIB", "severityLevel"), ("SNMP540-ALARM-MIB", "status"))
if mibBuilder.loadTexts: snmp540AlarmTrap.setDescription('The Enterprise specific Trap is sent whenever the alarm conditions are set in the network element. Each trap reported has a description of the alarm, the associated severity level with an active/clear status.')
mibBuilder.exportSymbols("SNMP540-ALARM-MIB", snmp540AlarmMIBversion=snmp540AlarmMIBversion, mask=mask, status=status, snmp540AlarmStructure=snmp540AlarmStructure, snmp540AlarmNumber=snmp540AlarmNumber, alarmNumber=alarmNumber, snmp540AlarmTable=snmp540AlarmTable, pysmi_class=pysmi_class, threshold=threshold, snmp540AlarmEntry=snmp540AlarmEntry, snmp540AlarmTrap=snmp540AlarmTrap, snmp540GeneralIntegrationTime=snmp540GeneralIntegrationTime, snmp540Alarm=snmp540Alarm, description=description, severityLevel=severityLevel)