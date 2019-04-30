#
# PySNMP MIB module EXTREME-VM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-VM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:55:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, IpAddress, Counter64, Unsigned32, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, TimeTicks, iso, Counter32, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Counter64", "Unsigned32", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "TimeTicks", "iso", "Counter32", "MibIdentifier", "ModuleIdentity")
TruthValue, TextualConvention, RowStatus, DisplayString, MacAddress, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "DisplayString", "MacAddress", "TimeStamp")
extremeVM = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 39))
extremeVM.setRevisions(('2011-04-18 00:00', '2010-02-03 00:00',))
if mibBuilder.loadTexts: extremeVM.setLastUpdated('201202270000Z')
if mibBuilder.loadTexts: extremeVM.setOrganization('Extreme Networks, Inc.')
extremeVMGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1))
extremeVMVPP = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2))
extremeVMDetected = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3))
extremeVMNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 39, 4))
extremeVMNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 39, 5))
class VMVPPSynchType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("global", 1), ("specific", 2))

class CounterDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("ingress-only", 1), ("egress-only", 2), ("both", 3))

extremeVMFTPServerTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1), )
if mibBuilder.loadTexts: extremeVMFTPServerTable.setStatus('current')
extremeVMFTPServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1, 1), ).setIndexNames((0, "EXTREME-VM-MIB", "extremeVMFTPServerType"))
if mibBuilder.loadTexts: extremeVMFTPServerEntry.setStatus('current')
extremeVMFTPServerType = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("backup", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeVMFTPServerType.setStatus('current')
extremeVMFTPAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1, 1, 2), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeVMFTPAddrType.setStatus('current')
extremeVMFTPServer = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeVMFTPServer.setStatus('current')
extremeVMFTPSynchInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeVMFTPSynchInterval.setStatus('current')
extremeVMFTPRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeVMFTPRowStatus.setStatus('current')
extremeVMFTPPathName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeVMFTPPathName.setStatus('current')
extremeVMFTPUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeVMFTPUsername.setStatus('current')
extremeVMFTPPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeVMFTPPassword.setStatus('current')
extremeVMFTPPolicyDir = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeVMFTPPolicyDir.setStatus('deprecated')
extremeVMLastSynch = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMLastSynch.setStatus('current')
extremeVMLastSynchStatus = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("success", 1), ("accessDenied", 2), ("serverTimeout", 3), ("serverNotConfigured", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMLastSynchStatus.setStatus('current')
extremeVMSynchAdminState = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idle", 1), ("synchronizeNow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeVMSynchAdminState.setStatus('current')
extremeVMSynchOperState = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idle", 1), ("synchronizing", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMSynchOperState.setStatus('current')
extremeVMTrackingEnabled = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeVMTrackingEnabled.setStatus('current')
extremeVMPortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 8), )
if mibBuilder.loadTexts: extremeVMPortConfigTable.setStatus('current')
extremeVMPortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 8, 1), ).setIndexNames((0, "EXTREME-VM-MIB", "extremeVMPortConfigIfIndex"))
if mibBuilder.loadTexts: extremeVMPortConfigEntry.setStatus('current')
extremeVMPortConfigIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 8, 1, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeVMPortConfigIfIndex.setStatus('current')
extremeVMPortConfigVMTrackingEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 8, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeVMPortConfigVMTrackingEnabled.setStatus('current')
extremeVMPortConfigVMTrackingDynVlanEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 1, 8, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeVMPortConfigVMTrackingDynVlanEnabled.setStatus('current')
extremeVMVPPTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 1), )
if mibBuilder.loadTexts: extremeVMVPPTable.setStatus('current')
extremeVMVPPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 1, 1), ).setIndexNames((0, "EXTREME-VM-MIB", "extremeVMVPPType"), (0, "EXTREME-VM-MIB", "extremeVMVPPName"))
if mibBuilder.loadTexts: extremeVMVPPEntry.setStatus('current')
extremeVMVPPType = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("network", 1), ("local", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeVMVPPType.setStatus('current')
extremeVMVPPName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeVMVPPName.setStatus('current')
extremeVMVPPControl = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("synchronizeNow", 1), ("noOperation", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeVMVPPControl.setStatus('current')
extremeVMVPPRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeVMVPPRowStatus.setStatus('current')
extremeVMVPPCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 1, 1, 5), CounterDirection()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeVMVPPCounter.setStatus('current')
extremeVMVPPVLANTag = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeVMVPPVLANTag.setStatus('current')
extremeVMVPPVLANVRName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeVMVPPVLANVRName.setStatus('current')
extremeVMMappingTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2), )
if mibBuilder.loadTexts: extremeVMMappingTable.setStatus('current')
extremeVMMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1), ).setIndexNames((0, "EXTREME-VM-MIB", "extremeVMMappingType"), (0, "EXTREME-VM-MIB", "extremeVMMappingMAC"))
if mibBuilder.loadTexts: extremeVMMappingEntry.setStatus('current')
extremeVMMappingType = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("network", 1), ("local", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeVMMappingType.setStatus('current')
extremeVMMappingMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1, 2), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeVMMappingMAC.setStatus('current')
extremeVMMappingIngressVPPName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeVMMappingIngressVPPName.setStatus('deprecated')
extremeVMMappingEgressVPPName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeVMMappingEgressVPPName.setStatus('deprecated')
extremeVMMappingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("vppValid", 1), ("vppMissing", 2), ("vppInvalid", 3), ("vppNotMapped", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMMappingStatus.setStatus('current')
extremeVMMappingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeVMMappingRowStatus.setStatus('current')
extremeVMMappingVPPName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeVMMappingVPPName.setStatus('current')
extremeVMMappingVLANTag = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeVMMappingVLANTag.setStatus('current')
extremeVMMappingVLANVRName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeVMMappingVLANVRName.setStatus('current')
extremeVMVPP2PolicyTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 3), )
if mibBuilder.loadTexts: extremeVMVPP2PolicyTable.setStatus('deprecated')
extremeVMVPP2PolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 3, 1), ).setIndexNames((0, "EXTREME-VM-MIB", "extremeVMVPP2PolicyVPPName"), (0, "EXTREME-VM-MIB", "extremeVMVPP2PolicyPolicyName"), (0, "EXTREME-VM-MIB", "extremeVMVPP2PolicyType"))
if mibBuilder.loadTexts: extremeVMVPP2PolicyEntry.setStatus('current')
extremeVMVPP2PolicyVPPName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: extremeVMVPP2PolicyVPPName.setStatus('current')
extremeVMVPP2PolicyPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: extremeVMVPP2PolicyPolicyName.setStatus('current')
extremeVMVPP2PolicyType = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("policyFile", 1), ("dynamicACL", 2))))
if mibBuilder.loadTexts: extremeVMVPP2PolicyType.setStatus('current')
extremeVMVPP2PolicyOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 3, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeVMVPP2PolicyOrder.setStatus('current')
extremeVMVPP2PolicyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeVMVPP2PolicyRowStatus.setStatus('current')
extremeVMDetectedNumber = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMDetectedNumber.setStatus('current')
extremeVMDetectedTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2), )
if mibBuilder.loadTexts: extremeVMDetectedTable.setStatus('current')
extremeVMDetectedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1), ).setIndexNames((0, "EXTREME-VM-MIB", "extremeVMDetectedMAC"))
if mibBuilder.loadTexts: extremeVMDetectedEntry.setStatus('current')
extremeVMDetectedMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 1), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeVMDetectedMAC.setStatus('current')
extremeVMDetectedVMName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMDetectedVMName.setStatus('current')
extremeVMDetectedIngressVPPName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMDetectedIngressVPPName.setStatus('deprecated')
extremeVMDetectedEgressVPPName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMDetectedEgressVPPName.setStatus('deprecated')
extremeVMDetectedIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMDetectedIfIndex.setStatus('current')
extremeVMDetectedAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("authenticating", 1), ("idle", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeVMDetectedAdminStatus.setStatus('current')
extremeVMDetectedOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("authenticating", 1), ("authenticatedNetwork", 2), ("authenticatedLocally", 3), ("authenticationDenied", 4), ("notAuthenticated", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMDetectedOperStatus.setStatus('current')
extremeVMDetectedResultIngress = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("policyApplied", 1), ("policyNotApplied", 2), ("policyInvalid", 3), ("policyNotFound", 4), ("policyNotMapped", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMDetectedResultIngress.setStatus('current')
extremeVMDetectedResultEgress = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("policyApplied", 1), ("policyNotApplied", 2), ("policyInvalid", 3), ("policyNotFound", 4), ("policyNotMapped", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMDetectedResultEgress.setStatus('current')
extremeVMDetectedIngErrPolicies = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMDetectedIngErrPolicies.setStatus('current')
extremeVMDetectedEgrErrPolicies = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMDetectedEgrErrPolicies.setStatus('current')
extremeVMDetectedVPPName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMDetectedVPPName.setStatus('current')
extremeVMDetectedVPPResult = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("vppMapped", 1), ("vppNotMapped", 2), ("vppInvalid", 3), ("vppMissing", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMDetectedVPPResult.setStatus('current')
extremeVMDetectedCounterInstallResult = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 14), CounterDirection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMDetectedCounterInstallResult.setStatus('current')
extremeVMDetectedVMVLANTag = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMDetectedVMVLANTag.setStatus('current')
extremeVMDetectedVMVLANVRName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 3, 2, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVMDetectedVMVLANVRName.setStatus('current')
extremeVMVPPDetailTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 4), )
if mibBuilder.loadTexts: extremeVMVPPDetailTable.setStatus('current')
extremeVMVPPDetailEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 4, 1), ).setIndexNames((0, "EXTREME-VM-MIB", "extremeVMVPPDetailVPPName"), (0, "EXTREME-VM-MIB", "extremeVMVPPDetailDirection"), (0, "EXTREME-VM-MIB", "extremeVMVPPDetailType"), (0, "EXTREME-VM-MIB", "extremeVMVPPDetailOrder"), (0, "EXTREME-VM-MIB", "extremeVMVPPDetailPolicyName"))
if mibBuilder.loadTexts: extremeVMVPPDetailEntry.setStatus('current')
extremeVMVPPDetailVPPName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 4, 1, 1), DisplayString())
if mibBuilder.loadTexts: extremeVMVPPDetailVPPName.setStatus('current')
extremeVMVPPDetailDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ingress", 1), ("egress", 2))))
if mibBuilder.loadTexts: extremeVMVPPDetailDirection.setStatus('current')
extremeVMVPPDetailType = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("policyFile", 1), ("dynamicACL", 2))))
if mibBuilder.loadTexts: extremeVMVPPDetailType.setStatus('current')
extremeVMVPPDetailOrder = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 4, 1, 4), Integer32())
if mibBuilder.loadTexts: extremeVMVPPDetailOrder.setStatus('current')
extremeVMVPPDetailPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 4, 1, 5), DisplayString())
if mibBuilder.loadTexts: extremeVMVPPDetailPolicyName.setStatus('current')
extremeVMVPPDetailRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 39, 2, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeVMVPPDetailRowStatus.setStatus('current')
extremeVMNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 1916, 1, 39, 5, 0))
extremeVMVPPSynchType = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 39, 4, 1), VMVPPSynchType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: extremeVMVPPSynchType.setStatus('current')
extremeVMVPPSyncFailed = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 39, 5, 0, 1)).setObjects(("EXTREME-VM-MIB", "extremeVMFTPServer"), ("EXTREME-VM-MIB", "extremeVMFTPAddrType"), ("EXTREME-VM-MIB", "extremeVMFTPServerType"), ("EXTREME-VM-MIB", "extremeVMLastSynchStatus"), ("EXTREME-VM-MIB", "extremeVMVPPName"), ("EXTREME-VM-MIB", "extremeVMVPPSynchType"))
if mibBuilder.loadTexts: extremeVMVPPSyncFailed.setStatus('current')
extremeVMVPPInvalid = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 39, 5, 0, 2)).setObjects(("EXTREME-VM-MIB", "extremeVMVPPType"), ("EXTREME-VM-MIB", "extremeVMVPPName"))
if mibBuilder.loadTexts: extremeVMVPPInvalid.setStatus('current')
extremeVMMapped = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 39, 5, 0, 3)).setObjects(("EXTREME-VM-MIB", "extremeVMMappingMAC"), ("EXTREME-VM-MIB", "extremeVMMappingIngressVPPName"), ("EXTREME-VM-MIB", "extremeVMMappingEgressVPPName"), ("EXTREME-VM-MIB", "extremeVMMappingVPPName"))
if mibBuilder.loadTexts: extremeVMMapped.setStatus('current')
extremeVMUnMapped = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 39, 5, 0, 4)).setObjects(("EXTREME-VM-MIB", "extremeVMMappingMAC"), ("EXTREME-VM-MIB", "extremeVMMappingIngressVPPName"), ("EXTREME-VM-MIB", "extremeVMMappingEgressVPPName"), ("EXTREME-VM-MIB", "extremeVMMappingVPPName"))
if mibBuilder.loadTexts: extremeVMUnMapped.setStatus('current')
extremeVMDetectResult = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 39, 5, 0, 5)).setObjects(("EXTREME-VM-MIB", "extremeVMDetectedMAC"), ("EXTREME-VM-MIB", "extremeVMDetectedIfIndex"), ("EXTREME-VM-MIB", "extremeVMDetectedIngressVPPName"), ("EXTREME-VM-MIB", "extremeVMDetectedEgressVPPName"), ("EXTREME-VM-MIB", "extremeVMDetectedResultIngress"), ("EXTREME-VM-MIB", "extremeVMDetectedResultEgress"), ("EXTREME-VM-MIB", "extremeVMDetectedOperStatus"), ("EXTREME-VM-MIB", "extremeVMDetectedIngErrPolicies"), ("EXTREME-VM-MIB", "extremeVMDetectedEgrErrPolicies"), ("EXTREME-VM-MIB", "extremeVMDetectedVPPResult"), ("EXTREME-VM-MIB", "extremeVMDetectedVPPName"), ("EXTREME-VM-MIB", "extremeVMDetectedCounterInstallResult"))
if mibBuilder.loadTexts: extremeVMDetectResult.setStatus('current')
extremeVMUnDetectResult = NotificationType((1, 3, 6, 1, 4, 1, 1916, 1, 39, 5, 0, 6)).setObjects(("EXTREME-VM-MIB", "extremeVMDetectedMAC"), ("EXTREME-VM-MIB", "extremeVMDetectedIfIndex"))
if mibBuilder.loadTexts: extremeVMUnDetectResult.setStatus('current')
mibBuilder.exportSymbols("EXTREME-VM-MIB", extremeVMDetectedIngressVPPName=extremeVMDetectedIngressVPPName, extremeVMSynchAdminState=extremeVMSynchAdminState, CounterDirection=CounterDirection, extremeVMDetectedEntry=extremeVMDetectedEntry, extremeVMDetectedAdminStatus=extremeVMDetectedAdminStatus, extremeVMPortConfigEntry=extremeVMPortConfigEntry, extremeVMDetectedEgrErrPolicies=extremeVMDetectedEgrErrPolicies, extremeVMFTPAddrType=extremeVMFTPAddrType, extremeVMFTPPolicyDir=extremeVMFTPPolicyDir, extremeVMVPPVLANVRName=extremeVMVPPVLANVRName, extremeVMVPPDetailOrder=extremeVMVPPDetailOrder, extremeVMDetectedIngErrPolicies=extremeVMDetectedIngErrPolicies, extremeVMVPPControl=extremeVMVPPControl, extremeVMVPPName=extremeVMVPPName, extremeVMNotifications=extremeVMNotifications, extremeVMDetectedVMName=extremeVMDetectedVMName, extremeVMVPPSyncFailed=extremeVMVPPSyncFailed, PYSNMP_MODULE_ID=extremeVM, extremeVMNotificationObjects=extremeVMNotificationObjects, extremeVMVPP2PolicyVPPName=extremeVMVPP2PolicyVPPName, extremeVMVPP2PolicyType=extremeVMVPP2PolicyType, VMVPPSynchType=VMVPPSynchType, extremeVMLastSynch=extremeVMLastSynch, extremeVMVPPDetailRowStatus=extremeVMVPPDetailRowStatus, extremeVMFTPRowStatus=extremeVMFTPRowStatus, extremeVMVPPDetailEntry=extremeVMVPPDetailEntry, extremeVMDetectedVMVLANTag=extremeVMDetectedVMVLANTag, extremeVMDetectedResultIngress=extremeVMDetectedResultIngress, extremeVMVPPType=extremeVMVPPType, extremeVMVPP=extremeVMVPP, extremeVMDetectedMAC=extremeVMDetectedMAC, extremeVMMappingVLANVRName=extremeVMMappingVLANVRName, extremeVMMappingMAC=extremeVMMappingMAC, extremeVMDetectedResultEgress=extremeVMDetectedResultEgress, extremeVMFTPSynchInterval=extremeVMFTPSynchInterval, extremeVMDetectedVPPResult=extremeVMDetectedVPPResult, extremeVMPortConfigTable=extremeVMPortConfigTable, extremeVMVPPRowStatus=extremeVMVPPRowStatus, extremeVMMappingStatus=extremeVMMappingStatus, extremeVMMappingVLANTag=extremeVMMappingVLANTag, extremeVMFTPUsername=extremeVMFTPUsername, extremeVMVPPCounter=extremeVMVPPCounter, extremeVMVPPDetailDirection=extremeVMVPPDetailDirection, extremeVMDetectResult=extremeVMDetectResult, extremeVMSynchOperState=extremeVMSynchOperState, extremeVMPortConfigVMTrackingEnabled=extremeVMPortConfigVMTrackingEnabled, extremeVMMapped=extremeVMMapped, extremeVMFTPServerTable=extremeVMFTPServerTable, extremeVMVPP2PolicyPolicyName=extremeVMVPP2PolicyPolicyName, extremeVMFTPServerType=extremeVMFTPServerType, extremeVMVPP2PolicyEntry=extremeVMVPP2PolicyEntry, extremeVMUnDetectResult=extremeVMUnDetectResult, extremeVMPortConfigVMTrackingDynVlanEnabled=extremeVMPortConfigVMTrackingDynVlanEnabled, extremeVMDetectedEgressVPPName=extremeVMDetectedEgressVPPName, extremeVMFTPPassword=extremeVMFTPPassword, extremeVMDetectedCounterInstallResult=extremeVMDetectedCounterInstallResult, extremeVMVPPDetailType=extremeVMVPPDetailType, extremeVMVPPEntry=extremeVMVPPEntry, extremeVMMappingRowStatus=extremeVMMappingRowStatus, extremeVMDetected=extremeVMDetected, extremeVMVPPInvalid=extremeVMVPPInvalid, extremeVMTrackingEnabled=extremeVMTrackingEnabled, extremeVMVPP2PolicyRowStatus=extremeVMVPP2PolicyRowStatus, extremeVMDetectedNumber=extremeVMDetectedNumber, extremeVMVPP2PolicyTable=extremeVMVPP2PolicyTable, extremeVMDetectedIfIndex=extremeVMDetectedIfIndex, extremeVMVPPDetailTable=extremeVMVPPDetailTable, extremeVMNotificationPrefix=extremeVMNotificationPrefix, extremeVMGeneral=extremeVMGeneral, extremeVMMappingTable=extremeVMMappingTable, extremeVMDetectedVPPName=extremeVMDetectedVPPName, extremeVMVPP2PolicyOrder=extremeVMVPP2PolicyOrder, extremeVMVPPDetailPolicyName=extremeVMVPPDetailPolicyName, extremeVMMappingEntry=extremeVMMappingEntry, extremeVM=extremeVM, extremeVMVPPSynchType=extremeVMVPPSynchType, extremeVMFTPPathName=extremeVMFTPPathName, extremeVMVPPVLANTag=extremeVMVPPVLANTag, extremeVMFTPServer=extremeVMFTPServer, extremeVMMappingIngressVPPName=extremeVMMappingIngressVPPName, extremeVMDetectedOperStatus=extremeVMDetectedOperStatus, extremeVMVPPTable=extremeVMVPPTable, extremeVMDetectedVMVLANVRName=extremeVMDetectedVMVLANVRName, extremeVMDetectedTable=extremeVMDetectedTable, extremeVMLastSynchStatus=extremeVMLastSynchStatus, extremeVMMappingType=extremeVMMappingType, extremeVMVPPDetailVPPName=extremeVMVPPDetailVPPName, extremeVMMappingVPPName=extremeVMMappingVPPName, extremeVMMappingEgressVPPName=extremeVMMappingEgressVPPName, extremeVMPortConfigIfIndex=extremeVMPortConfigIfIndex, extremeVMFTPServerEntry=extremeVMFTPServerEntry, extremeVMUnMapped=extremeVMUnMapped)