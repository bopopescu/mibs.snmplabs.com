#
# PySNMP MIB module CIENA-CES-RSVPTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CIENA-CES-RSVPTE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:49:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
cienaCesNotifications, cienaCesConfig = mibBuilder.importSymbols("CIENA-SMI", "cienaCesNotifications", "cienaCesConfig")
CienaGlobalState, = mibBuilder.importSymbols("CIENA-TC", "CienaGlobalState")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Bits, ModuleIdentity, TimeTicks, Counter32, ObjectIdentity, Gauge32, Integer32, iso, MibIdentifier, IpAddress, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "ModuleIdentity", "TimeTicks", "Counter32", "ObjectIdentity", "Gauge32", "Integer32", "iso", "MibIdentifier", "IpAddress", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString, TruthValue, MacAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "MacAddress", "RowStatus")
cienaCesRsvpteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16))
cienaCesRsvpteMIB.setRevisions(('2016-07-15 00:00', '2016-07-14 00:00', '2016-07-04 00:00', '2013-05-08 00:00', '2011-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cienaCesRsvpteMIB.setRevisionsDescriptions(('Modified the description of cienaCesRsvpteRecoveryTime and cienaCesRsvpteRestartTime under cienaCesRsvpteObjects.', 'Modified the attribute cienaCesRsvpteGRStatus to cienaCesRsvpteGRAdminStatus. Added the attribute cienaCesRsvpteGROperStatus under cienaCesRsvpteObjects.', 'Added the attribute cienaCesRsvpteGRStatus under cienaCesRsvpteObjects. Modified the default values of cienaCesRsvpteRecoveryTime and cienaCesRsvpteRestartTime under cienaCesRsvpteObjects.', 'Modified the status of cienaCesRsvpteRfrshSlewDenom and cienaCesRsvpteRfrshSlewNumerator to deprecated under cienaCesRsvpteObjects. Modified the status of cienaCesRsvpteIfMtu to deprecated under cienaCesRsvpteIfTable. Added objects cienaCesRsvpteRefreshSlewDenominator and cienaCesRsvpteRefreshSlewNumerator under cienaCesRsvpteObjects. ', 'Initial version.',))
if mibBuilder.loadTexts: cienaCesRsvpteMIB.setLastUpdated('201607150000Z')
if mibBuilder.loadTexts: cienaCesRsvpteMIB.setOrganization('Ciena, Inc')
if mibBuilder.loadTexts: cienaCesRsvpteMIB.setContactInfo(' Mib Meister 115 North Sullivan Road Spokane Valley, WA 99037 USA Phone: +1 509 242 9000 Email: support@ciena.com')
if mibBuilder.loadTexts: cienaCesRsvpteMIB.setDescription('This MIB module is for the RSVP-TE configuration for MPLS tunnels')
class AdvertisedLabel(TextualConvention, Integer32):
    description = 'Advertised Label'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 99))
    namedValues = NamedValues(("implicitnull", 1), ("nonreserved", 99))

class RsvpOperStatus(TextualConvention, Integer32):
    description = 'The current operational state of RSVP-TE.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("operStatusUp", 1), ("operStatusDown", 2), ("operStatusGoingUp", 3), ("operStatusGoingDown", 4), ("operStatusActFailed", 5))

class RsvpGRMode(TextualConvention, Integer32):
    description = 'The current GR operational state of RSVP-TE.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("helpNeighbor", 1), ("restartCapable", 2), ("notApplicable", 3))

cienaCesRsvpteMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1))
cienaCesRsvpteObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1))
cienaCesRsvpte = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2))
cienaCesRsvpteAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 1), CienaGlobalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteAdminStatus.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteAdminStatus.setDescription('The desired administrative status of RSVP-TE.')
cienaCesRsvpteOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 2), RsvpOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteOperStatus.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteOperStatus.setDescription('The current operational status of RSVP-TE.')
cienaCesRsvpteRetryInterval = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(3, 65)).clone(3)).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteRetryInterval.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteRetryInterval.setDescription('The persistent tunnel retry interval. This is the interval between the first failure of a persistent tunnel and the first attempt to re-establish the tunnel. This cannot be changed while the administrative status is enabled or the operational status is up.')
cienaCesRsvpteRetryInfiniteState = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('on')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteRetryInfiniteState.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteRetryInfiniteState.setDescription('The persistent tunnel retry infinity. This is the state which when on, triggers RSVP-TE to try to restore the tunnels infinite times. This object can only be set if RSVP-TE is globally disabled.')
cienaCesRsvpteRetryMax = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteRetryMax.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteRetryMax.setDescription("The maximum number of retry attempts that will be made before a persistent tunnel is deemed inoperable. Once in this state, a management agent should set mplsTunnelAdminStatus to 'up' to attempt to re-establish the tunnel. This field is not used when cienaCesRsvpteRetryInfiniteState is on.")
cienaCesRsvpteRefreshInterval = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 6), Integer32().clone(30000)).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteRefreshInterval.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteRefreshInterval.setDescription('The RSVP-TE value, R, which is used to set the average interval between refresh path and RESV messages.')
cienaCesRsvpteRefreshMultiple = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 214783647)).clone(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteRefreshMultiple.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteRefreshMultiple.setDescription('The RSVP-TE value, K, which is the number of unresponded path or RESV refresh attempts that must be made, spaced by the refresh interval, before the state is deemed to have timed out.')
cienaCesRsvpteRfrshSlewDenom = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 214783647)).clone(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteRfrshSlewDenom.setStatus('deprecated')
if mibBuilder.loadTexts: cienaCesRsvpteRfrshSlewDenom.setDescription('This object is deprecated and the new object to provide this information is cienaCesRsvpteRefreshSlewDenominator in this table.')
cienaCesRsvpteRfrshSlewNumerator = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 214783647)).clone(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteRfrshSlewNumerator.setStatus('deprecated')
if mibBuilder.loadTexts: cienaCesRsvpteRfrshSlewNumerator.setDescription('This object is deprecated and the new object to provide this information is cienaCesRsvpteRefreshSlewNumerator in this table.')
cienaCesRsvpteBlockadeMultiple = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 214783647)).clone(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteBlockadeMultiple.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteBlockadeMultiple.setDescription('The RSVP-TE value, Kb, which is the number of refresh timeout periods after which the blockade state is deleted.')
cienaCesRsvpteLSPSetupPriority = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteLSPSetupPriority.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteLSPSetupPriority.setDescription('The setup priority to apply to LSPs that are not signaling this parameter. 0 represents the highest priority and 7 the lowest. The value of this object must be numerically greater than or equal to (lower or equal priority) than the value of the holding priority object.')
cienaCesRsvpteLSPHoldingPriority = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteLSPHoldingPriority.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteLSPHoldingPriority.setDescription('The holding priority to apply to LSPs that are not signaling this parameter. 0 represents the highest priority and 7 the lowest. The value of this object must be numerically less than or equal to (higher or equal priority) than the value of the holding priority object.')
cienaCesRsvpteUseHopByHop = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 13), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteUseHopByHop.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteUseHopByHop.setDescription('A flag to indicate that RSVP-TE should use the hop by hop addressing scheme for the PATH and PATH-TEAR messages it sends. If set, then the IP addresses used in the IP header of the PATH messages forwarded by RSVP-TE set the source as the local outgoing interface IP address, and set the destination as the next hop router IP address.')
cienaCesRsvpteRestartCapable = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 14), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteRestartCapable.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteRestartCapable.setDescription('A flag to indicate whether the local node should advertise itself as restart capable.')
cienaCesRsvpteRestartTime = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 15), Unsigned32().clone(60000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteRestartTime.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteRestartTime.setDescription('The time in milliseconds that the local node takes to restart RSVP-TE and the communication channel used for RSVP-TE communication. This is advertised to neighbors in the Restart_Cap object in Hello messages. Only used if cienaCesRsvpteRestartCapable is set to true. For devices which only act as the Helper node, this timer is unused and will return value 0.')
cienaCesRsvpteRecoveryTime = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 16), Unsigned32().clone(120000)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteRecoveryTime.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteRecoveryTime.setDescription('The period of time in milliseconds that the local node would like neighbors to take to resyncronize RSVP-TE and MPLS forwarding information after the re-establishment of Hello connectivity. This is advertised to neighbors in the Restart_Cap object in Hello messages. A value of zero indicates that the node does not support resynchronization following failure of the local node. A value of 0xFFFFFFFF indicates an infinite recovery time. Only used if cienaCesRsvpteRestartCapable is set to true. For devices which only act as the Helper node, this timer is unused and will return value 0.')
cienaCesRsvpteMinPeerRestart = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteMinPeerRestart.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteMinPeerRestart.setDescription('The mininum period of time in milliseconds that RSVP-TE should wait for a restart capable neighbor to regain Hello connectivity before invoking procedures related to communication loss. RSVP-TE waits for the maximum of this time and the restart_time advertised in the RESTART_CAP object in Hello messages from the neighbor.')
cienaCesRsvpteRefreshSlewDenominator = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 214783647)).clone(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteRefreshSlewDenominator.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteRefreshSlewDenominator.setDescription('The denominator of the fraction, SlewMax, which is the maximum allowable increase in the refresh interval, R, to prevent state timeout while changing R. R is increased by this fraction until it reaches the new desired value.')
cienaCesRsvpteRefreshSlewNumerator = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 214783647)).clone(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteRefreshSlewNumerator.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteRefreshSlewNumerator.setDescription('The numerator of the fraction, SlewMax, which is the maximum allowable increase in the refresh interval, R, to prevent state timeout while changing R. R is increased by this fraction until it reaches the new desired value.')
cienaCesRsvpteGRAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 20), CienaGlobalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteGRAdminStatus.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteGRAdminStatus.setDescription('RSVP-TE Graceful restart status (Enabled/Disabled).')
cienaCesRsvpteGRMode = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 1, 21), RsvpGRMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteGRMode.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteGRMode.setDescription('RSVP-TE Graceful restart Operational status.')
cienaCesRsvpteIfTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1), )
if mibBuilder.loadTexts: cienaCesRsvpteIfTable.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteIfTable.setDescription('A table of interfaces on which RSVP-TE can be enabled.')
cienaCesRsvpteIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1), ).setIndexNames((0, "CIENA-CES-RSVPTE-MIB", "cienaCesRsvpteIfIndex"))
if mibBuilder.loadTexts: cienaCesRsvpteIfEntry.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteIfEntry.setDescription('An entry in the RSVP-TE interface table.')
cienaCesRsvpteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096)))
if mibBuilder.loadTexts: cienaCesRsvpteIfIndex.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteIfIndex.setDescription('Interface index.')
cienaCesRsvpteIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteIfName.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteIfName.setDescription('Interface name.')
cienaCesRsvpteIfIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteIfIpAddr.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteIfIpAddr.setDescription('Interface IP address.')
cienaCesRsvpteIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1500, 9216))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteIfMtu.setStatus('deprecated')
if mibBuilder.loadTexts: cienaCesRsvpteIfMtu.setDescription('This object is deprecated and no longer in use.')
cienaCesRsvpteIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1, 5), CienaGlobalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteIfAdminStatus.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteIfAdminStatus.setDescription('RSVP-TE administrative status on this interface.')
cienaCesRsvpteIfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteIfOperStatus.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteIfOperStatus.setDescription('RSVP-TE operational status on this interface.')
cienaCesRsvpteIfHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteIfHelloInterval.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteIfHelloInterval.setDescription('RSVP-TE Hello message interval.')
cienaCesRsvpteIfHelloTolerance = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10)).clone(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteIfHelloTolerance.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteIfHelloTolerance.setDescription('RSVP-TE Hello tolerance defines the number of Hello intervals that can pass without receiving a successful Hello message from a partner before the Hello session times out.')
cienaCesRsvpteIfAdvertisedLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 2, 1, 16, 1, 2, 1, 1, 9), AdvertisedLabel().clone(99)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesRsvpteIfAdvertisedLabel.setStatus('current')
if mibBuilder.loadTexts: cienaCesRsvpteIfAdvertisedLabel.setDescription('This object indicates what kind of label will be advertised by RSVP-TE for a Label Request received on this L3 interface.')
mibBuilder.exportSymbols("CIENA-CES-RSVPTE-MIB", cienaCesRsvpteLSPHoldingPriority=cienaCesRsvpteLSPHoldingPriority, cienaCesRsvpteIfEntry=cienaCesRsvpteIfEntry, cienaCesRsvpteRefreshMultiple=cienaCesRsvpteRefreshMultiple, cienaCesRsvpteIfIndex=cienaCesRsvpteIfIndex, cienaCesRsvpteGRAdminStatus=cienaCesRsvpteGRAdminStatus, PYSNMP_MODULE_ID=cienaCesRsvpteMIB, cienaCesRsvpteRfrshSlewNumerator=cienaCesRsvpteRfrshSlewNumerator, cienaCesRsvpteMinPeerRestart=cienaCesRsvpteMinPeerRestart, cienaCesRsvpteMIBObjects=cienaCesRsvpteMIBObjects, cienaCesRsvpteIfName=cienaCesRsvpteIfName, RsvpOperStatus=RsvpOperStatus, cienaCesRsvpteIfAdminStatus=cienaCesRsvpteIfAdminStatus, cienaCesRsvpteOperStatus=cienaCesRsvpteOperStatus, cienaCesRsvpteIfHelloInterval=cienaCesRsvpteIfHelloInterval, cienaCesRsvpteRfrshSlewDenom=cienaCesRsvpteRfrshSlewDenom, cienaCesRsvpteObjects=cienaCesRsvpteObjects, cienaCesRsvpteLSPSetupPriority=cienaCesRsvpteLSPSetupPriority, cienaCesRsvpteUseHopByHop=cienaCesRsvpteUseHopByHop, AdvertisedLabel=AdvertisedLabel, cienaCesRsvpteRefreshSlewNumerator=cienaCesRsvpteRefreshSlewNumerator, cienaCesRsvpteRefreshInterval=cienaCesRsvpteRefreshInterval, RsvpGRMode=RsvpGRMode, cienaCesRsvpteMIB=cienaCesRsvpteMIB, cienaCesRsvpteAdminStatus=cienaCesRsvpteAdminStatus, cienaCesRsvpteIfOperStatus=cienaCesRsvpteIfOperStatus, cienaCesRsvpteRetryMax=cienaCesRsvpteRetryMax, cienaCesRsvpteRetryInterval=cienaCesRsvpteRetryInterval, cienaCesRsvpteRestartCapable=cienaCesRsvpteRestartCapable, cienaCesRsvpteIfTable=cienaCesRsvpteIfTable, cienaCesRsvpte=cienaCesRsvpte, cienaCesRsvpteIfAdvertisedLabel=cienaCesRsvpteIfAdvertisedLabel, cienaCesRsvpteIfIpAddr=cienaCesRsvpteIfIpAddr, cienaCesRsvpteIfHelloTolerance=cienaCesRsvpteIfHelloTolerance, cienaCesRsvpteIfMtu=cienaCesRsvpteIfMtu, cienaCesRsvpteRefreshSlewDenominator=cienaCesRsvpteRefreshSlewDenominator, cienaCesRsvpteRestartTime=cienaCesRsvpteRestartTime, cienaCesRsvpteRecoveryTime=cienaCesRsvpteRecoveryTime, cienaCesRsvpteRetryInfiniteState=cienaCesRsvpteRetryInfiniteState, cienaCesRsvpteBlockadeMultiple=cienaCesRsvpteBlockadeMultiple, cienaCesRsvpteGRMode=cienaCesRsvpteGRMode)