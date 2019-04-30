#
# PySNMP MIB module WWP-LEOS-RADIUS-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-LEOS-RADIUS-CLIENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:31:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, Bits, Counter64, Counter32, Integer32, NotificationType, IpAddress, MibIdentifier, iso, ObjectIdentity, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "Bits", "Counter64", "Counter32", "Integer32", "NotificationType", "IpAddress", "MibIdentifier", "iso", "ObjectIdentity", "TimeTicks", "Unsigned32")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
wwpModulesLeos, = mibBuilder.importSymbols("WWP-SMI", "wwpModulesLeos")
wwpLeosRadiusClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20))
wwpLeosRadiusClientMIB.setRevisions(('2012-04-26 00:00', '2012-04-05 00:00', '2001-04-03 17:00',))
if mibBuilder.loadTexts: wwpLeosRadiusClientMIB.setLastUpdated('201204260000Z')
if mibBuilder.loadTexts: wwpLeosRadiusClientMIB.setOrganization('Ciena, Inc')
class RadiusString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 64)

wwpLeosRadiusClientMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1))
wwpLeosRadiusClient = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1))
wwpLeosRadiusClientMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 2))
wwpLeosRadiusClientMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 2, 0))
wwpLeosRadiusClientMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 3))
wwpLeosRadiusClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 3, 1))
wwpLeosRadiusClientMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 3, 2))
wwpLeosRadiusAdminState = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosRadiusAdminState.setStatus('current')
wwpLeosRadiusOperState = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRadiusOperState.setStatus('current')
wwpLeosRadiusClientTimeout = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30)).clone(1)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosRadiusClientTimeout.setStatus('current')
wwpLeosRadiusClientRetries = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosRadiusClientRetries.setStatus('current')
wwpLeosRadiusClientAuthKey = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 5), RadiusString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosRadiusClientAuthKey.setStatus('current')
wwpLeosRadiusClientServerTable = MibTable((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6), )
if mibBuilder.loadTexts: wwpLeosRadiusClientServerTable.setStatus('current')
wwpLeosRadiusClientAuthKeyUnset = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosRadiusClientAuthKeyUnset.setStatus('current')
wwpLeosRadiusClientAuthSecretUnset = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosRadiusClientAuthSecretUnset.setStatus('current')
wwpLeosRadiusClientServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1), ).setIndexNames((0, "WWP-LEOS-RADIUS-CLIENT-MIB", "wwpLeosRadiusClientServerIndex"))
if mibBuilder.loadTexts: wwpLeosRadiusClientServerEntry.setStatus('current')
wwpLeosRadiusClientServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: wwpLeosRadiusClientServerIndex.setStatus('current')
wwpLeosRadiusClientServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerAddr.setStatus('current')
wwpLeosRadiusClientServerResolvedAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerResolvedAddr.setStatus('current')
wwpLeosRadiusClientServerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerPriority.setStatus('current')
wwpLeosRadiusClientServerAuthPort = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1812)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerAuthPort.setStatus('current')
wwpLeosRadiusClientServerRoundTripTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerRoundTripTime.setStatus('current')
wwpLeosRadiusClientServerAccessRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerAccessRequests.setStatus('current')
wwpLeosRadiusClientServerAccessRetransmissions = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerAccessRetransmissions.setStatus('current')
wwpLeosRadiusClientServerAccessAccepts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerAccessAccepts.setStatus('current')
wwpLeosRadiusClientServerAccessRejects = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerAccessRejects.setStatus('current')
wwpLeosRadiusClientServerAccessChallenges = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerAccessChallenges.setStatus('current')
wwpLeosRadiusClientServerMalformedAccessResponses = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerMalformedAccessResponses.setStatus('current')
wwpLeosRadiusClientServerBadAuthenticators = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerBadAuthenticators.setStatus('current')
wwpLeosRadiusClientServerPendingRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 14), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerPendingRequests.setStatus('current')
wwpLeosRadiusClientServerTimeouts = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerTimeouts.setStatus('current')
wwpLeosRadiusClientServerUnknownTypes = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerUnknownTypes.setStatus('current')
wwpLeosRadiusClientServerPacketsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerPacketsDropped.setStatus('current')
wwpLeosRadiusClientServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 18), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerStatus.setStatus('current')
wwpLeosRadiusClientServerApplication = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("userLogin", 1), ("dot1x", 2), ("all", 3))).clone('userLogin')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerApplication.setStatus('current')
wwpLeosRadiusClientServerResolvedInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 20), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerResolvedInetAddrType.setStatus('current')
wwpLeosRadiusClientServerResolvedInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 6, 1, 21), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosRadiusClientServerResolvedInetAddress.setStatus('current')
wwpLeosRadiusClientSearchType = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 20, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cached", 1), ("priority", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosRadiusClientSearchType.setStatus('current')
mibBuilder.exportSymbols("WWP-LEOS-RADIUS-CLIENT-MIB", wwpLeosRadiusClientServerResolvedAddr=wwpLeosRadiusClientServerResolvedAddr, wwpLeosRadiusClientServerPacketsDropped=wwpLeosRadiusClientServerPacketsDropped, wwpLeosRadiusClientMIB=wwpLeosRadiusClientMIB, wwpLeosRadiusClientServerPendingRequests=wwpLeosRadiusClientServerPendingRequests, wwpLeosRadiusClientMIBNotificationPrefix=wwpLeosRadiusClientMIBNotificationPrefix, wwpLeosRadiusClientSearchType=wwpLeosRadiusClientSearchType, wwpLeosRadiusClientServerEntry=wwpLeosRadiusClientServerEntry, wwpLeosRadiusClientServerAddr=wwpLeosRadiusClientServerAddr, wwpLeosRadiusClientServerAccessRequests=wwpLeosRadiusClientServerAccessRequests, RadiusString=RadiusString, wwpLeosRadiusClientServerTable=wwpLeosRadiusClientServerTable, wwpLeosRadiusAdminState=wwpLeosRadiusAdminState, wwpLeosRadiusClientServerAuthPort=wwpLeosRadiusClientServerAuthPort, wwpLeosRadiusClientRetries=wwpLeosRadiusClientRetries, wwpLeosRadiusClientServerRoundTripTime=wwpLeosRadiusClientServerRoundTripTime, wwpLeosRadiusClientServerMalformedAccessResponses=wwpLeosRadiusClientServerMalformedAccessResponses, wwpLeosRadiusClientServerStatus=wwpLeosRadiusClientServerStatus, wwpLeosRadiusClientServerAccessChallenges=wwpLeosRadiusClientServerAccessChallenges, wwpLeosRadiusOperState=wwpLeosRadiusOperState, wwpLeosRadiusClientServerAccessAccepts=wwpLeosRadiusClientServerAccessAccepts, wwpLeosRadiusClientMIBGroups=wwpLeosRadiusClientMIBGroups, wwpLeosRadiusClientMIBObjects=wwpLeosRadiusClientMIBObjects, wwpLeosRadiusClientServerIndex=wwpLeosRadiusClientServerIndex, wwpLeosRadiusClientServerAccessRetransmissions=wwpLeosRadiusClientServerAccessRetransmissions, wwpLeosRadiusClientServerTimeouts=wwpLeosRadiusClientServerTimeouts, PYSNMP_MODULE_ID=wwpLeosRadiusClientMIB, wwpLeosRadiusClientAuthKeyUnset=wwpLeosRadiusClientAuthKeyUnset, wwpLeosRadiusClient=wwpLeosRadiusClient, wwpLeosRadiusClientAuthSecretUnset=wwpLeosRadiusClientAuthSecretUnset, wwpLeosRadiusClientTimeout=wwpLeosRadiusClientTimeout, wwpLeosRadiusClientServerResolvedInetAddress=wwpLeosRadiusClientServerResolvedInetAddress, wwpLeosRadiusClientMIBCompliances=wwpLeosRadiusClientMIBCompliances, wwpLeosRadiusClientServerApplication=wwpLeosRadiusClientServerApplication, wwpLeosRadiusClientServerResolvedInetAddrType=wwpLeosRadiusClientServerResolvedInetAddrType, wwpLeosRadiusClientServerUnknownTypes=wwpLeosRadiusClientServerUnknownTypes, wwpLeosRadiusClientServerAccessRejects=wwpLeosRadiusClientServerAccessRejects, wwpLeosRadiusClientAuthKey=wwpLeosRadiusClientAuthKey, wwpLeosRadiusClientMIBNotifications=wwpLeosRadiusClientMIBNotifications, wwpLeosRadiusClientServerPriority=wwpLeosRadiusClientServerPriority, wwpLeosRadiusClientServerBadAuthenticators=wwpLeosRadiusClientServerBadAuthenticators, wwpLeosRadiusClientMIBConformance=wwpLeosRadiusClientMIBConformance)