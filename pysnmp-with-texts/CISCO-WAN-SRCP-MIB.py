#
# PySNMP MIB module CISCO-WAN-SRCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-SRCP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:18:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
mgcRedundancyGrpNum, = mibBuilder.importSymbols("CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpNum")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, Counter32, IpAddress, Unsigned32, MibIdentifier, NotificationType, Integer32, TimeTicks, Bits, iso, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "Counter32", "IpAddress", "Unsigned32", "MibIdentifier", "NotificationType", "Integer32", "TimeTicks", "Bits", "iso", "ModuleIdentity", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanSrcpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 11))
ciscoWanSrcpMIB.setRevisions(('2004-01-30 00:00', '2000-12-26 00:00', '2000-08-31 00:00', '2000-07-21 00:00', '2000-05-28 00:00', '2000-05-24 00:00', '1999-11-23 00:00', '1999-11-01 00:00', '1999-10-21 00:00', '1999-06-23 00:00', '1999-06-07 00:00', '1999-04-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanSrcpMIB.setRevisionsDescriptions(('Update descriptions in the MIB. ', 'Changed description of srcpRequestMaxTimeout which had a reference to an object srcpRequestMinTimeout which should actually be srcpRequestTimeout. ', 'moved srcpRequestMinTimeout, srcpRequestRetries and srcpRequestMaxTimeout objects to new subgroup srcpAdminRetyObject ', 'Added following new objects for exponential retry srcpRequestTimeOut , srcpRequestRetries, srcpRequestMaxTimeout ', 'Moved some objects from the srcpPeerTable to the srcpPeerGrpTable for the implementation of the MGC Redundancy Feature. ', 'added srcpRequestMinTimeout, srcpRequestRetries and srcpRequestMaxTimeout objects ', 'Added DEFVAL clause for srcpPeerHeartbeatInterval, srcpPeerMaxPduSize. ', 'Changed the description of srcpPeerHeartbeatInterval to say that value less than 100 (except 0) is not allowed. ', 'Changed the description of TimeSinceHeartbeat as it was saying return -1 if in locked state or unassociated state. But -1 is not a valid value as per the specified range. Changed it to return 0. ', 'Added definition for srcpStatsPeerName & changed srcpPeerName to read-only. ', 'Added DEFVAL clause for srcpPortNumber and srcpPeerPortNumber ', 'Initial version of the MIB. ',))
if mibBuilder.loadTexts: ciscoWanSrcpMIB.setLastUpdated('200401300000Z')
if mibBuilder.loadTexts: ciscoWanSrcpMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanSrcpMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoWanSrcpMIB.setDescription('The MIB module for managing SRCP(Simple Resource Coordination Protocol) implementations. SRCP is a resource coordination protocol used between a MGC(Media Gateway Controller) and a MG(Media Gateway). SRCP MIB is applicable to both controllers (SRCP clients) and gateways (SRCP servers). MGMIB: This is the short name used for CISCO-WAN-MG-MIB in this MIB.')
srcpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 11, 1))
srcpAdminObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1))
srcpStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2))
srcpAdminRetyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 3))
srcpVersion = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: srcpVersion.setStatus('current')
if mibBuilder.loadTexts: srcpVersion.setDescription('The name of the SRCP protocol version for exmaple SRCP 1.0.2. If MGMIB is supported, this name corresponds to mgProtocolName (defined in CISCO-WAN-MG-MIB MIB) in an entry to mgSupportedProtocolTable. ')
srcpPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1025, 65535)).clone(2428)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srcpPortNumber.setStatus('current')
if mibBuilder.loadTexts: srcpPortNumber.setDescription("This object is used to configure the UDP port used for SRCP on the system (local UDP port). It is configurable only if the system is in a locked or disabled state (i.e If MGMIB Is supported, mgAdministrativeState(defined in CISCO-WAN-MG-MIB MIB) should be 'locked' before the UDP port can be configured). ")
srcpPeerTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 3), )
if mibBuilder.loadTexts: srcpPeerTable.setStatus('current')
if mibBuilder.loadTexts: srcpPeerTable.setDescription('This is a table which is used to provision peer-specific SRCP configuration and administration information. Each table entry corresponds to an SRCP peer as identified by its domain name(srcpPeerName). ')
srcpPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-WAN-SRCP-MIB", "srcpPeerId"))
if mibBuilder.loadTexts: srcpPeerEntry.setStatus('current')
if mibBuilder.loadTexts: srcpPeerEntry.setDescription('Represents an individual table entry in srcpPeerTable. Each row corresponds to an SRCP peer and is identified by its domain name (srcpPeerName). Entries in this table are implicitly created by the agent. If the agent supports MGMIB, this occurs as follows: An entry shall be created when an entry is created in the mgcRedundancyGrpProtocolTable(defined in CISCO-WAN-MGC-REDUN-MIB MIB) and when mgProtocolNumber (defined in CISCO-WAN-MG-MIB MIB) refers to SRCP as supported protocol. An entry will be made for all MGC(Media Gateway Controller) in that MGC Redundancy Group. Accordingly, an entry shall be deleted if the corresponding entry in the mgcRedundancyGrpProtocolTable is deleted. If the agent does not support MGMIB, entry creation might occur when the first SRCP communication with an IP address/domain name occurs. if MGC Redundacy feature is supported the following objects: srcpPeerHeartbeatInterval, srcpPeerTimeSinceHeartbeat rcpPeerMaxPduSize are not meaningful here. These objects are defined per MGC Redundancy Group rather than per MGC. ')
srcpPeerId = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: srcpPeerId.setStatus('current')
if mibBuilder.loadTexts: srcpPeerId.setDescription('This object identifies the SRCP peer and serves as index to this table. If MGMIB is supported, this is the same as the mgcNumber(defined in CISCO-WAN-MG-MIB MIB) from the mgcTable. ')
srcpPeerName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: srcpPeerName.setStatus('current')
if mibBuilder.loadTexts: srcpPeerName.setDescription('This object identifies the name of the SRCP peer. If MGMIB is supported, this is the same as the mgcName from the mgcTable. ')
srcpPeerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1025, 65535)).clone(2428)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srcpPeerPortNumber.setStatus('current')
if mibBuilder.loadTexts: srcpPeerPortNumber.setDescription('This object is used to configure the UDP port of the SRCP peer. ')
srcpPeerHeartbeatInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: srcpPeerHeartbeatInterval.setStatus('deprecated')
if mibBuilder.loadTexts: srcpPeerHeartbeatInterval.setDescription('This object is used to configure the length of the heartbeat interval, in milliseconds. The heartbeat interval indicate when the GW(Gateway) is expected to receive a heartbeat from a specific peer or MGC group. If value is 0, heartbeat for this peer is not monitored. The heartbeat interval less than 100 is not allowed (except 0). If MGC Redundancy is supported, this object is not effective. Instead, the user should use srcpPeerGrpHeartbeatInterval. ')
srcpPeerTimeSinceHeartbeat = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: srcpPeerTimeSinceHeartbeat.setStatus('deprecated')
if mibBuilder.loadTexts: srcpPeerTimeSinceHeartbeat.setDescription('The time since the last heartbeat was received, in milliseconds. This represents the difference between the current time and the last time an SRCP command was received. A value of 0 shall be returned if the heartbeat is not monitored. Even if the heartbeat is monitored, a value of 0 shall be returned if any of the following is true: i) The system is locked or disabled (as indicated by mgAdministrativeState). ii) The srcpPeer is unassociated as indicated by mgcAssociationState(defined in CISCO-WAN-MG-MIB MIB). If MGC Redundancy is supported, this object is not effective. Instead, the user should use srcpPeerGrpTimeSinceHeartbeat. ')
srcpPeerMaxPduSize = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4095, 65535)).clone(16384)).setUnits('octets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: srcpPeerMaxPduSize.setStatus('deprecated')
if mibBuilder.loadTexts: srcpPeerMaxPduSize.setDescription('This object is used to configure the maximum UDP PDU(Protocol Data Unit) size, in octets, that may be used for SRCP communications with the peer. This value may not be configurable for all agents. If MGC Redundancy is supported, this object is not effective. Instead, the user should use srcpPeerGrpMaxPduSize. ')
srcpPeerGrpParamTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 4), )
if mibBuilder.loadTexts: srcpPeerGrpParamTable.setStatus('current')
if mibBuilder.loadTexts: srcpPeerGrpParamTable.setDescription('This table is used to provision SRCP parameters for an MGC Redundancy group. MGCs can be configured as part of MGC Redundancy groups. This feature allows for redundant call agents. Each table entry corresponds to an SRCP peer entry that is identified by the MGC Redundancy group number. ')
srcpPeerGrpParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-WAN-MGC-REDUN-MIB", "mgcRedundancyGrpNum"))
if mibBuilder.loadTexts: srcpPeerGrpParamEntry.setStatus('current')
if mibBuilder.loadTexts: srcpPeerGrpParamEntry.setDescription('Represents an individual table entry in the srcpPeerGrpParamTable. Each row corresponds to an MGC Redundancy Group and is identified by the MGC Redundancy Group Number. Entries are implicitly created when the SRCP protocol is added for an MGC Redundancy Group. The entry will be removed if the SRCP protocol is removed for an MGC Redundancy Group. ')
srcpPeerGrpHeartbeatInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: srcpPeerGrpHeartbeatInterval.setStatus('current')
if mibBuilder.loadTexts: srcpPeerGrpHeartbeatInterval.setDescription('This object is used to configure the length of the heartbeat interval, in milliseconds. If 0, heartbeat for this peer Group is not monitored. The heartbeat interval less than 100 is not allowed (except 0). ')
srcpPeerGrpTimeSinceHeartbeat = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: srcpPeerGrpTimeSinceHeartbeat.setStatus('current')
if mibBuilder.loadTexts: srcpPeerGrpTimeSinceHeartbeat.setDescription('The time since the last heartbeat was received, in milliseconds. This represents the difference between the current time and the last time an SRCP command was received. A value of 0 shall be returned if the heartbeat is not monitored. Even if the heartbeat is monitored, a value of 0 shall be returned if any of the following is true: i) The system is locked or disabled (as indicated by mgAdministrativeState). ii) The stateChangeNtfy flag is disabled for the srcpPeer Group (as indicated by mgcRedundancyGrpStateChangeNtfy of CISCO-WAN-MGC-REDUN-MIB). ')
srcpPeerGrpMaxPduSize = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4095, 65535)).clone(16384)).setUnits('octets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: srcpPeerGrpMaxPduSize.setStatus('current')
if mibBuilder.loadTexts: srcpPeerGrpMaxPduSize.setDescription('This object is used to configure the maximum UDP PDU size, in octets, that may be used for SRCP communications with the peer. This value may not be configurable for all agents. ')
srcpRequestTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: srcpRequestTimeOut.setStatus('current')
if mibBuilder.loadTexts: srcpRequestTimeOut.setDescription('This object specifies the minimum timeout value. This value along with srcpRequestMaxTimeout and srcpRequestRetries is used to determine the exponential retry interval for retransmitting unacknowledged SRCP messages. It is the responsibility of the requesting entity to provide suitable timeouts for all outstanding commands, and to retry commands when timeouts exceeded. The default value of this object is 500 milliseconds. When the value of this object changes srcpAdminObjects group changed trap will be sent as specify by vismConfigChangeTypeBitMap in CISCO-VISM-MODULE-MIB. ')
srcpRequestRetries = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: srcpRequestRetries.setStatus('current')
if mibBuilder.loadTexts: srcpRequestRetries.setDescription('This object specifies the number of retries for a SRCP request that exceeds timeout. It is the responsibility of the requesting entity to provide suitable timeouts for all outstanding commands, and to retry when times out. The default value of this object is 3. When the value of this object changes srcpAdminObjects group changed trap will be sent as specify by vismConfigChangeTypeBitMap in CISCO-VISM-MODULE-MIB. ')
srcpRequestMaxTimeout = MibScalar((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: srcpRequestMaxTimeout.setStatus('current')
if mibBuilder.loadTexts: srcpRequestMaxTimeout.setDescription('This object specifies the maximum timeout value. This timer value is used along with srcpRequestTimeOut and srcpRequestRetries to determine the exponential retry interval for retransmitting unacknowledged SRCP messages. The value of this timer has to be greater than or equal to srcpRequestTimeOut. The default value of this object is 500 milliseconds. When the value of this object changes srcpAdminObjects group changed trap will be sent as specify by vismConfigChangeTypeBitMap in CISCO-VISM-MODULE-MIB. ')
srcpPeerStatsTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1), )
if mibBuilder.loadTexts: srcpPeerStatsTable.setStatus('current')
if mibBuilder.loadTexts: srcpPeerStatsTable.setDescription('This table contains SRCP statistics information since reset. SRCP statistics are kept in this table, with each table entry containing the statistics of SRCP messages that communicated with a peer at a specific IP address of the peer. It differs from the SRCP peer table which maintains information on a per call agent basis as identified by their domain names. ')
srcpPeerStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1), ).setIndexNames((0, "CISCO-WAN-SRCP-MIB", "srcpStatsPeerIpAddress"))
if mibBuilder.loadTexts: srcpPeerStatsEntry.setStatus('current')
if mibBuilder.loadTexts: srcpPeerStatsEntry.setDescription('The row of the srcpPeerStatsTable contains information about SRCP message statistics per IP address of the MGC. An entry is implicitly created and deleted by the agent. There can be two cases: 1. Case of Internal address resolution : In this case IP addresses of all SRCP peers are resolved internally. If the agent supports the MGMIB, the following referential integrity rules apply: When an entry is added to mgcResolutionTable defined in CISCO-WAN-MG-MIB with a specific IP address, an entry is created in this srcpPeerStatsTable for that IP address. When an entry is deleted from mgcResolutionTable, the row with the corresponding IP address in this table will be deleted. 2. Case of External address resolution : If there is at least one Call agent whose IP address is resolved externally, an entry is created whenever SRCP communication occurs with a new IP address. Table entries are never deleted, but must be nonpersistent in agent implementations, i.e. must be purged in case of a system shutdown/restart. ')
srcpStatsPeerIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: srcpStatsPeerIpAddress.setStatus('current')
if mibBuilder.loadTexts: srcpStatsPeerIpAddress.setDescription('This object specifies the IP address of the SRCP peer and serves as index to the table. ')
srcpStatsPeerName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: srcpStatsPeerName.setStatus('current')
if mibBuilder.loadTexts: srcpStatsPeerName.setDescription('Denotes the name of the SRCP peer. This is the same as the mgcName from the mgcTable. It is provided here as a read-only parameter as a convinience feature. ')
packetsDiscardedCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: packetsDiscardedCnts.setStatus('current')
if mibBuilder.loadTexts: packetsDiscardedCnts.setDescription('The number of packets that were received and discarded. The packets may get discarded because of indecipherable PDUs like bad protocol version, bad command verb etc, or because of unknown transaction IDs (in case of SRCP clients). ')
augwCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: augwCnts.setStatus('current')
if mibBuilder.loadTexts: augwCnts.setDescription('The total number of AUGW(Audit Gateway) commands received from the peer on this IP address.')
aulnCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aulnCnts.setStatus('current')
if mibBuilder.loadTexts: aulnCnts.setDescription('The total number of AULN(Audit Line) commands received from or sent to the peer on this IP address. ')
rqntCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rqntCnts.setStatus('current')
if mibBuilder.loadTexts: rqntCnts.setDescription('The total number of RQNT(Notification Request) commands received from or sent to the peer on this IP address. ')
ntfyCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntfyCnts.setStatus('current')
if mibBuilder.loadTexts: ntfyCnts.setDescription('The total number of NTFY(Notify) commands received from or sent to the peer on this IP address. ')
augwFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: augwFailCnts.setStatus('current')
if mibBuilder.loadTexts: augwFailCnts.setDescription('For MG : The total number of AUGW commands received that were responded to with a failure return code. For MGC : The total number of AUGW commands sent which were timed out without a response or for which a response with failure return code was received. ')
aulnFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aulnFailCnts.setStatus('current')
if mibBuilder.loadTexts: aulnFailCnts.setDescription('Media gateway : The total number of AULN commands received that were responded to with a failure return code. Media gateway controller : The total number of AULN commands sent which were timed out without a response or For which a response with failure return code was received. ')
rqntFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rqntFailCnts.setStatus('current')
if mibBuilder.loadTexts: rqntFailCnts.setDescription('Media gateway : The total number of RQNT commands received that were responded to with a failure return code. Media gateway controller : The total number of RQNT commands sent which were timed out without a response or for which a response with failure return code was received. ')
ntfyFailCnts = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 11, 1, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntfyFailCnts.setStatus('current')
if mibBuilder.loadTexts: ntfyFailCnts.setDescription('Media gateway : The total number of NTFY commands sent which were timed out without a response or for which a response with failure return code was received. Media gateway controller: The total number of NTFY commands received that were responded to with a failure return code. ')
srcpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 11, 3))
srcpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 1))
srcpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 2))
srcpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 1, 1)).setObjects(("CISCO-WAN-SRCP-MIB", "srcpConfigurationGroup"), ("CISCO-WAN-SRCP-MIB", "srcpStatisticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    srcpMIBCompliance = srcpMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: srcpMIBCompliance.setDescription('The compliance statement for the SNMPv2 entities which implement SRCP MIB.')
srcpMIBComplaince2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 1, 2)).setObjects(("CISCO-WAN-SRCP-MIB", "srcpConfigurationGroup2"), ("CISCO-WAN-SRCP-MIB", "srcpStatisticsGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    srcpMIBComplaince2 = srcpMIBComplaince2.setStatus('deprecated')
if mibBuilder.loadTexts: srcpMIBComplaince2.setDescription(' The compliance statement for the SNMPv2 entities which implement SRCP MIB.')
srcpMIBComplaince3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 1, 3)).setObjects(("CISCO-WAN-SRCP-MIB", "srcpConfigurationGroup3"), ("CISCO-WAN-SRCP-MIB", "srcpStatisticsGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    srcpMIBComplaince3 = srcpMIBComplaince3.setStatus('current')
if mibBuilder.loadTexts: srcpMIBComplaince3.setDescription('The compliance statement for the SNMPv2 entities which implement SRCP MIB.')
srcpConfigurationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 2, 1)).setObjects(("CISCO-WAN-SRCP-MIB", "srcpVersion"), ("CISCO-WAN-SRCP-MIB", "srcpPortNumber"), ("CISCO-WAN-SRCP-MIB", "srcpPeerName"), ("CISCO-WAN-SRCP-MIB", "srcpPeerPortNumber"), ("CISCO-WAN-SRCP-MIB", "srcpPeerHeartbeatInterval"), ("CISCO-WAN-SRCP-MIB", "srcpPeerTimeSinceHeartbeat"), ("CISCO-WAN-SRCP-MIB", "srcpPeerMaxPduSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    srcpConfigurationGroup = srcpConfigurationGroup.setStatus('deprecated')
if mibBuilder.loadTexts: srcpConfigurationGroup.setDescription('This group contains objects related to configuration of SRCP. Min Access of read only is permissible for system providing only a fixed SRCP port.')
srcpStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 2, 2)).setObjects(("CISCO-WAN-SRCP-MIB", "srcpStatsPeerName"), ("CISCO-WAN-SRCP-MIB", "packetsDiscardedCnts"), ("CISCO-WAN-SRCP-MIB", "augwCnts"), ("CISCO-WAN-SRCP-MIB", "aulnCnts"), ("CISCO-WAN-SRCP-MIB", "rqntCnts"), ("CISCO-WAN-SRCP-MIB", "ntfyCnts"), ("CISCO-WAN-SRCP-MIB", "augwFailCnts"), ("CISCO-WAN-SRCP-MIB", "aulnFailCnts"), ("CISCO-WAN-SRCP-MIB", "rqntFailCnts"), ("CISCO-WAN-SRCP-MIB", "ntfyFailCnts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    srcpStatisticsGroup = srcpStatisticsGroup.setStatus('deprecated')
if mibBuilder.loadTexts: srcpStatisticsGroup.setDescription('This group contains the statistics per SRCP peer.')
srcpConfigurationGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 2, 3)).setObjects(("CISCO-WAN-SRCP-MIB", "srcpVersion"), ("CISCO-WAN-SRCP-MIB", "srcpPortNumber"), ("CISCO-WAN-SRCP-MIB", "srcpPeerName"), ("CISCO-WAN-SRCP-MIB", "srcpPeerPortNumber"), ("CISCO-WAN-SRCP-MIB", "srcpPeerHeartbeatInterval"), ("CISCO-WAN-SRCP-MIB", "srcpPeerTimeSinceHeartbeat"), ("CISCO-WAN-SRCP-MIB", "srcpPeerMaxPduSize"), ("CISCO-WAN-SRCP-MIB", "srcpRequestTimeOut"), ("CISCO-WAN-SRCP-MIB", "srcpRequestRetries"), ("CISCO-WAN-SRCP-MIB", "srcpRequestMaxTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    srcpConfigurationGroup2 = srcpConfigurationGroup2.setStatus('deprecated')
if mibBuilder.loadTexts: srcpConfigurationGroup2.setDescription('This group contains objects related to configuration of SRCP. Min Access of read only is permissible for system providing only a fixed SRCP port.')
srcpConfigurationGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 2, 5)).setObjects(("CISCO-WAN-SRCP-MIB", "srcpVersion"), ("CISCO-WAN-SRCP-MIB", "srcpPortNumber"), ("CISCO-WAN-SRCP-MIB", "srcpPeerName"), ("CISCO-WAN-SRCP-MIB", "srcpPeerPortNumber"), ("CISCO-WAN-SRCP-MIB", "srcpPeerGrpHeartbeatInterval"), ("CISCO-WAN-SRCP-MIB", "srcpPeerGrpTimeSinceHeartbeat"), ("CISCO-WAN-SRCP-MIB", "srcpPeerGrpMaxPduSize"), ("CISCO-WAN-SRCP-MIB", "srcpRequestTimeOut"), ("CISCO-WAN-SRCP-MIB", "srcpRequestRetries"), ("CISCO-WAN-SRCP-MIB", "srcpRequestMaxTimeout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    srcpConfigurationGroup3 = srcpConfigurationGroup3.setStatus('current')
if mibBuilder.loadTexts: srcpConfigurationGroup3.setDescription('This group contains objects related to configuration of SRCP. Min Access of read only is permissible for system providing only a fixed SRCP port.')
srcpStatisticsGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 11, 3, 2, 4)).setObjects(("CISCO-WAN-SRCP-MIB", "srcpStatsPeerName"), ("CISCO-WAN-SRCP-MIB", "packetsDiscardedCnts"), ("CISCO-WAN-SRCP-MIB", "augwCnts"), ("CISCO-WAN-SRCP-MIB", "aulnCnts"), ("CISCO-WAN-SRCP-MIB", "rqntCnts"), ("CISCO-WAN-SRCP-MIB", "ntfyCnts"), ("CISCO-WAN-SRCP-MIB", "augwFailCnts"), ("CISCO-WAN-SRCP-MIB", "aulnFailCnts"), ("CISCO-WAN-SRCP-MIB", "rqntFailCnts"), ("CISCO-WAN-SRCP-MIB", "ntfyFailCnts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    srcpStatisticsGroup2 = srcpStatisticsGroup2.setStatus('current')
if mibBuilder.loadTexts: srcpStatisticsGroup2.setDescription('This group contains the statistics per SRCP peer.')
mibBuilder.exportSymbols("CISCO-WAN-SRCP-MIB", srcpRequestTimeOut=srcpRequestTimeOut, augwCnts=augwCnts, rqntCnts=rqntCnts, srcpPeerHeartbeatInterval=srcpPeerHeartbeatInterval, aulnCnts=aulnCnts, srcpMIBGroups=srcpMIBGroups, srcpObjects=srcpObjects, srcpAdminRetyObjects=srcpAdminRetyObjects, srcpAdminObjects=srcpAdminObjects, srcpPeerPortNumber=srcpPeerPortNumber, srcpPeerGrpHeartbeatInterval=srcpPeerGrpHeartbeatInterval, srcpMIBCompliances=srcpMIBCompliances, srcpConfigurationGroup2=srcpConfigurationGroup2, srcpPeerEntry=srcpPeerEntry, srcpConfigurationGroup=srcpConfigurationGroup, srcpPeerStatsEntry=srcpPeerStatsEntry, srcpVersion=srcpVersion, srcpMIBCompliance=srcpMIBCompliance, srcpMIBComplaince3=srcpMIBComplaince3, ntfyFailCnts=ntfyFailCnts, srcpPeerName=srcpPeerName, srcpPeerGrpParamTable=srcpPeerGrpParamTable, srcpMIBComplaince2=srcpMIBComplaince2, srcpStatsObjects=srcpStatsObjects, srcpPeerGrpMaxPduSize=srcpPeerGrpMaxPduSize, srcpRequestMaxTimeout=srcpRequestMaxTimeout, srcpStatsPeerIpAddress=srcpStatsPeerIpAddress, aulnFailCnts=aulnFailCnts, srcpPeerTable=srcpPeerTable, srcpMIBConformance=srcpMIBConformance, srcpPeerGrpParamEntry=srcpPeerGrpParamEntry, srcpStatsPeerName=srcpStatsPeerName, packetsDiscardedCnts=packetsDiscardedCnts, srcpPeerStatsTable=srcpPeerStatsTable, ciscoWanSrcpMIB=ciscoWanSrcpMIB, srcpPeerId=srcpPeerId, srcpRequestRetries=srcpRequestRetries, srcpStatisticsGroup=srcpStatisticsGroup, augwFailCnts=augwFailCnts, srcpPeerTimeSinceHeartbeat=srcpPeerTimeSinceHeartbeat, srcpPeerGrpTimeSinceHeartbeat=srcpPeerGrpTimeSinceHeartbeat, srcpConfigurationGroup3=srcpConfigurationGroup3, PYSNMP_MODULE_ID=ciscoWanSrcpMIB, srcpStatisticsGroup2=srcpStatisticsGroup2, ntfyCnts=ntfyCnts, srcpPeerMaxPduSize=srcpPeerMaxPduSize, rqntFailCnts=rqntFailCnts, srcpPortNumber=srcpPortNumber)