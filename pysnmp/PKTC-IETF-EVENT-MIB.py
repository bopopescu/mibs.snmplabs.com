#
# PySNMP MIB module PKTC-IETF-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PKTC-IETF-EVENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:31:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ifPhysAddress, = mibBuilder.importSymbols("IF-MIB", "ifPhysAddress")
InetAddressType, InetPortNumber, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetPortNumber", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
snmpNotifyGroup, snmpNotifyFilterGroup = mibBuilder.importSymbols("SNMP-NOTIFICATION-MIB", "snmpNotifyGroup", "snmpNotifyFilterGroup")
snmpTargetBasicGroup, snmpTargetResponseGroup = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetBasicGroup", "snmpTargetResponseGroup")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, Gauge32, MibIdentifier, iso, ModuleIdentity, NotificationType, Counter32, Counter64, IpAddress, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "Gauge32", "MibIdentifier", "iso", "ModuleIdentity", "NotificationType", "Counter32", "Counter64", "IpAddress", "mib-2")
DateAndTime, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TruthValue", "DisplayString", "TextualConvention")
SyslogFacility, SyslogSeverity = mibBuilder.importSymbols("SYSLOG-TC-MIB", "SyslogFacility", "SyslogSeverity")
pktcIetfEventMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 182))
pktcIetfEventMib.setRevisions(('2009-03-30 00:00',))
if mibBuilder.loadTexts: pktcIetfEventMib.setLastUpdated('200903300000Z')
if mibBuilder.loadTexts: pktcIetfEventMib.setOrganization('IETF IP over Cable Data Network Working Group')
class SyslogSeverityMask(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("emerg", 0), ("alert", 1), ("crit", 2), ("err", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7))

pktcEventNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 182, 0))
pktcEventMibObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 182, 1))
pktcEventConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 182, 2))
pktcEventControl = MibIdentifier((1, 3, 6, 1, 2, 1, 182, 1, 1))
pktcEventThrottle = MibIdentifier((1, 3, 6, 1, 2, 1, 182, 1, 2))
pktcEventStatus = MibIdentifier((1, 3, 6, 1, 2, 1, 182, 1, 3))
pktcEvents = MibIdentifier((1, 3, 6, 1, 2, 1, 182, 1, 4))
pktcEventLog = MibIdentifier((1, 3, 6, 1, 2, 1, 182, 1, 5))
pktcEventReset = MibScalar((1, 3, 6, 1, 2, 1, 182, 1, 1, 1), Bits().clone(namedValues=NamedValues(("resetEventLogTable", 0), ("resetEventTable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcEventReset.setStatus('current')
pktcEventSyslog = MibIdentifier((1, 3, 6, 1, 2, 1, 182, 1, 1, 2))
pktcEventSyslogCapabilities = MibScalar((1, 3, 6, 1, 2, 1, 182, 1, 1, 2, 1), Bits().clone(namedValues=NamedValues(("formatBSDSyslog", 0), ("formatSyslogProtocol", 1), ("transportUDP", 2), ("transportTLS", 3), ("transportBEEP", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEventSyslogCapabilities.setStatus('current')
pktcEventSyslogAddressType = MibScalar((1, 3, 6, 1, 2, 1, 182, 1, 1, 2, 2), InetAddressType().clone('ipv4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcEventSyslogAddressType.setStatus('current')
pktcEventSyslogAddress = MibScalar((1, 3, 6, 1, 2, 1, 182, 1, 1, 2, 3), InetAddress().clone('0.0.0.0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcEventSyslogAddress.setStatus('current')
pktcEventSyslogMessageFormat = MibScalar((1, 3, 6, 1, 2, 1, 182, 1, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("formatBSDSyslog", 1), ("formatSyslogProtocol", 2))).clone('formatSyslogProtocol')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcEventSyslogMessageFormat.setStatus('current')
pktcEventSyslogTransport = MibScalar((1, 3, 6, 1, 2, 1, 182, 1, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("udp", 1), ("tls", 2), ("beep", 3))).clone('tls')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcEventSyslogTransport.setStatus('current')
pktcEventSyslogPort = MibScalar((1, 3, 6, 1, 2, 1, 182, 1, 1, 2, 6), InetPortNumber().clone(6514)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcEventSyslogPort.setStatus('current')
pktcEventClassTable = MibTable((1, 3, 6, 1, 2, 1, 182, 1, 1, 3), )
if mibBuilder.loadTexts: pktcEventClassTable.setStatus('current')
pktcEventClassEntry = MibTableRow((1, 3, 6, 1, 2, 1, 182, 1, 1, 3, 1), ).setIndexNames((0, "PKTC-IETF-EVENT-MIB", "pktcEventClassIndex"))
if mibBuilder.loadTexts: pktcEventClassEntry.setStatus('current')
pktcEventClassIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)))
if mibBuilder.loadTexts: pktcEventClassIndex.setStatus('current')
pktcEventClassName = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 1, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEventClassName.setStatus('current')
pktcEventClassStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 1, 3, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcEventClassStatus.setStatus('current')
pktcEventClassSeverity = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 1, 3, 1, 4), SyslogSeverityMask()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcEventClassSeverity.setStatus('current')
pktcEventThrottleAdminStatus = MibScalar((1, 3, 6, 1, 2, 1, 182, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unconstrained", 1), ("maintainBelowThreshold", 2), ("stopAtThreshold", 3), ("inhibited", 4))).clone('unconstrained')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcEventThrottleAdminStatus.setStatus('current')
pktcEventThrottleThreshold = MibScalar((1, 3, 6, 1, 2, 1, 182, 1, 2, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 1024)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcEventThrottleThreshold.setStatus('current')
pktcEventThrottleInterval = MibScalar((1, 3, 6, 1, 2, 1, 182, 1, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 604800)).clone(1)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcEventThrottleInterval.setStatus('current')
pktcEventTransmissionStatus = MibScalar((1, 3, 6, 1, 2, 1, 182, 1, 3, 1), Bits().clone(namedValues=NamedValues(("syslogThrottled", 0), ("snmpThrottled", 1), ("validsyslogServerAbsent", 2), ("validSnmpManagerAbsent", 3), ("syslogTransmitError", 4), ("snmpTransmitError", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEventTransmissionStatus.setStatus('current')
pktcEventTable = MibTable((1, 3, 6, 1, 2, 1, 182, 1, 4, 1), )
if mibBuilder.loadTexts: pktcEventTable.setStatus('current')
pktcEventEntry = MibTableRow((1, 3, 6, 1, 2, 1, 182, 1, 4, 1, 1), ).setIndexNames((0, "PKTC-IETF-EVENT-MIB", "pktcEventOrganization"), (0, "PKTC-IETF-EVENT-MIB", "pktcEventIdentifier"))
if mibBuilder.loadTexts: pktcEventEntry.setStatus('current')
pktcEventOrganization = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 4, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: pktcEventOrganization.setStatus('current')
pktcEventIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 4, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: pktcEventIdentifier.setStatus('current')
pktcEventFacility = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 4, 1, 1, 3), SyslogFacility()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEventFacility.setStatus('current')
pktcEventSeverityLevel = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 4, 1, 1, 4), SyslogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcEventSeverityLevel.setStatus('current')
pktcEventReporting = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 4, 1, 1, 5), Bits().clone(namedValues=NamedValues(("local", 0), ("syslog", 1), ("snmpTrap", 2), ("snmpInform", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcEventReporting.setStatus('current')
pktcEventText = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 4, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pktcEventText.setStatus('current')
pktcEventClass = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 4, 1, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEventClass.setStatus('current')
pktcEventLogTable = MibTable((1, 3, 6, 1, 2, 1, 182, 1, 5, 1), )
if mibBuilder.loadTexts: pktcEventLogTable.setStatus('current')
pktcEventLogEntry = MibTableRow((1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1), ).setIndexNames((0, "PKTC-IETF-EVENT-MIB", "pktcEventLogIndex"))
if mibBuilder.loadTexts: pktcEventLogEntry.setStatus('current')
pktcEventLogIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: pktcEventLogIndex.setStatus('current')
pktcEventLogTime = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEventLogTime.setStatus('current')
pktcEventLogOrganization = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEventLogOrganization.setStatus('current')
pktcEventLogIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEventLogIdentifier.setStatus('current')
pktcEventLogText = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEventLogText.setStatus('current')
pktcEventLogEndpointName = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEventLogEndpointName.setStatus('current')
pktcEventLogType = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 7), Bits().clone(namedValues=NamedValues(("local", 0), ("syslog", 1), ("snmpTrap", 2), ("snmpInform", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEventLogType.setStatus('current')
pktcEventLogTargetInfo = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 8), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEventLogTargetInfo.setStatus('current')
pktcEventLogCorrelationId = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEventLogCorrelationId.setStatus('current')
pktcEventLogAdditionalInfo = MibTableColumn((1, 3, 6, 1, 2, 1, 182, 1, 5, 1, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pktcEventLogAdditionalInfo.setStatus('current')
pktcEventNotification = NotificationType((1, 3, 6, 1, 2, 1, 182, 0, 1)).setObjects(("PKTC-IETF-EVENT-MIB", "pktcEventLogTime"), ("PKTC-IETF-EVENT-MIB", "pktcEventLogOrganization"), ("PKTC-IETF-EVENT-MIB", "pktcEventLogIdentifier"), ("PKTC-IETF-EVENT-MIB", "pktcEventLogEndpointName"), ("PKTC-IETF-EVENT-MIB", "pktcEventLogCorrelationId"), ("IF-MIB", "ifPhysAddress"))
if mibBuilder.loadTexts: pktcEventNotification.setStatus('current')
pktcEventCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 182, 2, 1))
pktcEventGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 182, 2, 2))
pktcEventBasicCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 182, 2, 1, 3)).setObjects(("PKTC-IETF-EVENT-MIB", "pktcEventGroup"), ("PKTC-IETF-EVENT-MIB", "pktcEventNotificationGroup"), ("SNMP-TARGET-MIB", "snmpTargetBasicGroup"), ("SNMP-TARGET-MIB", "snmpTargetResponseGroup"), ("SNMP-NOTIFICATION-MIB", "snmpNotifyGroup"), ("SNMP-NOTIFICATION-MIB", "snmpNotifyFilterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEventBasicCompliance = pktcEventBasicCompliance.setStatus('current')
pktcEventGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 182, 2, 2, 1)).setObjects(("PKTC-IETF-EVENT-MIB", "pktcEventReset"), ("PKTC-IETF-EVENT-MIB", "pktcEventSyslogCapabilities"), ("PKTC-IETF-EVENT-MIB", "pktcEventSyslogAddressType"), ("PKTC-IETF-EVENT-MIB", "pktcEventSyslogAddress"), ("PKTC-IETF-EVENT-MIB", "pktcEventSyslogTransport"), ("PKTC-IETF-EVENT-MIB", "pktcEventSyslogPort"), ("PKTC-IETF-EVENT-MIB", "pktcEventSyslogMessageFormat"), ("PKTC-IETF-EVENT-MIB", "pktcEventThrottleAdminStatus"), ("PKTC-IETF-EVENT-MIB", "pktcEventThrottleThreshold"), ("PKTC-IETF-EVENT-MIB", "pktcEventThrottleInterval"), ("PKTC-IETF-EVENT-MIB", "pktcEventTransmissionStatus"), ("PKTC-IETF-EVENT-MIB", "pktcEventFacility"), ("PKTC-IETF-EVENT-MIB", "pktcEventSeverityLevel"), ("PKTC-IETF-EVENT-MIB", "pktcEventReporting"), ("PKTC-IETF-EVENT-MIB", "pktcEventText"), ("PKTC-IETF-EVENT-MIB", "pktcEventLogTime"), ("PKTC-IETF-EVENT-MIB", "pktcEventLogOrganization"), ("PKTC-IETF-EVENT-MIB", "pktcEventLogIdentifier"), ("PKTC-IETF-EVENT-MIB", "pktcEventLogText"), ("PKTC-IETF-EVENT-MIB", "pktcEventLogEndpointName"), ("PKTC-IETF-EVENT-MIB", "pktcEventLogType"), ("PKTC-IETF-EVENT-MIB", "pktcEventLogTargetInfo"), ("PKTC-IETF-EVENT-MIB", "pktcEventLogCorrelationId"), ("PKTC-IETF-EVENT-MIB", "pktcEventLogAdditionalInfo"), ("PKTC-IETF-EVENT-MIB", "pktcEventClass"), ("PKTC-IETF-EVENT-MIB", "pktcEventClassName"), ("PKTC-IETF-EVENT-MIB", "pktcEventClassStatus"), ("PKTC-IETF-EVENT-MIB", "pktcEventClassSeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEventGroup = pktcEventGroup.setStatus('current')
pktcEventNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 182, 2, 2, 2)).setObjects(("PKTC-IETF-EVENT-MIB", "pktcEventNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pktcEventNotificationGroup = pktcEventNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("PKTC-IETF-EVENT-MIB", pktcIetfEventMib=pktcIetfEventMib, pktcEventMibObjects=pktcEventMibObjects, pktcEventLog=pktcEventLog, pktcEventSyslogCapabilities=pktcEventSyslogCapabilities, pktcEventControl=pktcEventControl, pktcEventTable=pktcEventTable, pktcEventReporting=pktcEventReporting, pktcEventThrottleInterval=pktcEventThrottleInterval, pktcEventClassStatus=pktcEventClassStatus, pktcEventText=pktcEventText, SyslogSeverityMask=SyslogSeverityMask, pktcEventThrottleThreshold=pktcEventThrottleThreshold, pktcEventClassName=pktcEventClassName, pktcEventSyslogTransport=pktcEventSyslogTransport, pktcEventClassTable=pktcEventClassTable, pktcEventThrottleAdminStatus=pktcEventThrottleAdminStatus, pktcEventNotificationGroup=pktcEventNotificationGroup, pktcEventSyslogPort=pktcEventSyslogPort, pktcEventFacility=pktcEventFacility, pktcEventBasicCompliance=pktcEventBasicCompliance, pktcEventSeverityLevel=pktcEventSeverityLevel, pktcEventLogType=pktcEventLogType, pktcEventClass=pktcEventClass, pktcEventGroups=pktcEventGroups, pktcEventLogIdentifier=pktcEventLogIdentifier, pktcEventClassIndex=pktcEventClassIndex, pktcEventClassSeverity=pktcEventClassSeverity, pktcEventLogTable=pktcEventLogTable, pktcEventGroup=pktcEventGroup, pktcEventLogOrganization=pktcEventLogOrganization, pktcEventLogAdditionalInfo=pktcEventLogAdditionalInfo, pktcEventConformance=pktcEventConformance, pktcEventSyslog=pktcEventSyslog, pktcEventReset=pktcEventReset, pktcEventThrottle=pktcEventThrottle, pktcEventClassEntry=pktcEventClassEntry, pktcEventSyslogAddressType=pktcEventSyslogAddressType, pktcEventLogIndex=pktcEventLogIndex, pktcEventLogTargetInfo=pktcEventLogTargetInfo, pktcEventNotifications=pktcEventNotifications, pktcEventSyslogAddress=pktcEventSyslogAddress, pktcEventTransmissionStatus=pktcEventTransmissionStatus, pktcEventLogCorrelationId=pktcEventLogCorrelationId, pktcEventIdentifier=pktcEventIdentifier, pktcEventEntry=pktcEventEntry, pktcEventLogEntry=pktcEventLogEntry, pktcEventCompliances=pktcEventCompliances, PYSNMP_MODULE_ID=pktcIetfEventMib, pktcEventStatus=pktcEventStatus, pktcEventSyslogMessageFormat=pktcEventSyslogMessageFormat, pktcEventLogTime=pktcEventLogTime, pktcEventLogText=pktcEventLogText, pktcEvents=pktcEvents, pktcEventOrganization=pktcEventOrganization, pktcEventNotification=pktcEventNotification, pktcEventLogEndpointName=pktcEventLogEndpointName)