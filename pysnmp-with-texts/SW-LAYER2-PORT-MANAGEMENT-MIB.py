#
# PySNMP MIB module SW-LAYER2-PORT-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW-LAYER2-PORT-MANAGEMENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:12:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, NotificationType, Integer32, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, ModuleIdentity, Counter32, Gauge32, Bits, ObjectIdentity, enterprises, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "NotificationType", "Integer32", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "ModuleIdentity", "Counter32", "Gauge32", "Bits", "ObjectIdentity", "enterprises", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
marconi = MibIdentifier((1, 3, 6, 1, 4, 1, 326))
systems = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2))
external = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20))
dlink = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1))
dlinkcommon = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 1))
golf = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2))
golfproducts = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1))
es2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3))
golfcommon = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2))
marconi_products = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1)).setLabel("marconi-products")
marconi_es2000Prod = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 28)).setLabel("marconi-es2000Prod")
swProperty = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 1, 28, 1))
marconi_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2)).setLabel("marconi-mgmt")
es2000Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28))
swL2Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2))
swL2PortMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4))
swL2PortInfoTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 1), )
if mibBuilder.loadTexts: swL2PortInfoTable.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortInfoTable.setDescription('A table that contains information about every port.')
swL2PortInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 1, 1), ).setIndexNames((0, "SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoUnitIndex"), (0, "SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoModuleIndex"), (0, "SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoIndex"))
if mibBuilder.loadTexts: swL2PortInfoEntry.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortInfoEntry.setDescription('A list of information for each port of the device.')
swL2PortInfoUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortInfoUnitIndex.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortInfoUnitIndex.setDescription('Indicates ID of the unit in the device.')
swL2PortInfoModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortInfoModuleIndex.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortInfoModuleIndex.setDescription('Indicates ID of the module on the unit.')
swL2PortInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortInfoIndex.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortInfoIndex.setDescription('Indicates ID of the port on the module.')
swL2PortInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("portType-100TX", 1), ("portType-100FX", 2), ("portType-GIGA-MTRJSX", 3), ("portType-GIGA-MTRJLX", 4), ("portType-GIGA-SCSX", 5), ("portType-GIGA-SCLX", 6), ("other", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortInfoType.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortInfoType.setDescription('Indicates the connector type of this port.')
swL2PortInfoDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortInfoDescr.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortInfoDescr.setDescription('Provides port type information in displayed string format.')
swL2PortInfoLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("link-pass", 2), ("link-fail", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortInfoLinkStatus.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortInfoLinkStatus.setDescription('Indicates port link status.')
swL2PortInfoNwayStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("half-10Mbps", 2), ("full-10Mbps", 3), ("half-100Mbps", 4), ("full-100Mbps", 5), ("half-1Gigabps", 6), ("full-1Gigabps", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortInfoNwayStatus.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortInfoNwayStatus.setDescription('This object indicates the port speed and duplex mode.')
swL2PortCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2), )
if mibBuilder.loadTexts: swL2PortCtrlTable.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortCtrlTable.setDescription('A table that contains control information about every port.')
swL2PortCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1), ).setIndexNames((0, "SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortCtrlUnitIndex"), (0, "SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortCtrlModuleIndex"), (0, "SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortCtrlIndex"))
if mibBuilder.loadTexts: swL2PortCtrlEntry.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortCtrlEntry.setDescription('A list of control information for each port of the device.')
swL2PortCtrlUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortCtrlUnitIndex.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortCtrlUnitIndex.setDescription('Indicates ID of the unit in the device.')
swL2PortCtrlModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortCtrlModuleIndex.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortCtrlModuleIndex.setDescription('Indicates ID of the module on the unit.')
swL2PortCtrlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortCtrlIndex.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortCtrlIndex.setDescription('This object indicates the device port number.(1..Max port number).')
swL2PortCtrlAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("notAvailable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2PortCtrlAdminState.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortCtrlAdminState.setDescription('This object decides the port to be enabled or disabled.')
swL2PortCtrlLinkStatusAlarmState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("notAvailable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2PortCtrlLinkStatusAlarmState.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortCtrlLinkStatusAlarmState.setDescription('Depends on this object to determine to send a trap or not when link status changes.')
swL2PortCtrlNwayState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 10))).clone(namedValues=NamedValues(("other", 1), ("nway-enabled", 2), ("nway-disabled-10Mbps-Half", 3), ("nway-disabled-10Mbps-Full", 4), ("nway-disabled-100Mbps-Half", 5), ("nway-disabled-100Mbps-Full", 6), ("nway-disabled-1Gigabps-Half", 7), ("nway-disabled-1Gigabps-Full", 8), ("notAvailable", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2PortCtrlNwayState.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortCtrlNwayState.setDescription('Chooses the port speed, duplex mode, and N-Way function mode.')
swL2PortCtrlFlowCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2PortCtrlFlowCtrlState.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortCtrlFlowCtrlState.setDescription('Sets IEEE 802.3x compliant flow control function as enabled or disabled. And IEEE 802.3x compliant flow control function work only when the port is in full duplex mode.The setting is effective the next time you reset or power on the hub.')
swL2PortCtrlBackPressState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2PortCtrlBackPressState.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortCtrlBackPressState.setDescription('Depends on this object to determine to enable or disable the backpressure function when the port is working in half duplex mode.')
swL2PortCtrlLockState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("notAvailable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2PortCtrlLockState.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortCtrlLockState.setDescription('The state of this entry. The meanings of the values are: other(1) - this entry is currently in use but the conditions under which it will remain so are different from each of the following values. disable(2) - Port lock funtion disable. enable(3) - Locking a port provides the CPU with the ability to decide which address are permitted to reside on such port, who knows about these address, and unknown packet forwarding to/from such ports. This is a way to prevent undesired traffic from being received or transmmited on the port.')
swL2PortCtrlPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("default", 2), ("force-low-priority", 3), ("force-high-priority", 4), ("notAvailable", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2PortCtrlPriority.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortCtrlPriority.setDescription('The priority queueing for packets received on this port, except for BPDU/IGMP packets and packets with unknown unicast destination address. IGMP and BPDU packets are always routed with high priority; packets with unknown unicast destination addresses are always routed with low priority. Other packets follow the rules below: other(1) - this entry is currently in use but the conditions under which it will remain so are different from each of the following values. default(2) - A packet is normally classified as low priority, unless at least one of the following is true: (a)The packet contained a TAG (per 802.1Q definition) with the priority greater or equal to 4. (b)The address-table entry for the destination address had Pd=HIGH. force-low_priority(3) - A packet is normally classified as low priority. force-high_priority(4) - A packet is normally classified as high priority.')
swL2PortCtrlStpState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("notAvailable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2PortCtrlStpState.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortCtrlStpState.setDescription("The state of STP(spanning tree algorithm) operation on this port. That's meaning the port whether add in the STP. The value enabled(3) indicates that STP is enabled on this port, as long as swDevCtrlStpState is also enabled for this device. When disabled(2) but swDevCtrlStpState is still enabled for the device, STP is disabled on this port : any BPDU packets received will be discarded and no BPDU packets will be propagated from the port.")
swL2PortCtrlHOLState = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3), ("notAvailable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2PortCtrlHOLState.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortCtrlHOLState.setDescription("The object provides a way to prevent HOL (Head Of Line) blocking between ports. HOL protection may prevent forwarding a packet to a blocking port. The idea relies on the assumption that it is better to discard packets destined to blocking ports, then to let them consume more and more buffers in the input-port's Rx-counters because eventually these input ports may become totally blocked. The meanings of the values are: other(1) - this entry is currently in use but the conditions under which it will remain so are different from each of the following values. disabled(2) - HOL function disable. enabled(3) - HOL function enable.")
swL2PortCtrlBcastRisingAct = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("do-nothing", 2), ("blocking", 3), ("blocking-trap", 4), ("notAvailable", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2PortCtrlBcastRisingAct.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortCtrlBcastRisingAct.setDescription('This object indicates the system action when broadcast storm rising threshold is met. other(1) - this entry is currently in use but the conditions under which it will remain so are different from each of the following values. do-nothing(2) - no action. blocking(3) - the port can discard any coming broadcast frame. blocking-trap(4) - the port can discard any coming broadcast frame. And the device can send a broadcast rising trap.')
swL2PortCtrlBcastFallingAct = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("do-nothing", 2), ("forwarding", 3), ("forwarding-trap", 4), ("notAvailable", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL2PortCtrlBcastFallingAct.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortCtrlBcastFallingAct.setDescription('This object indicates the device action when broadcast storm falling threshold is met. other(1) - this entry is currently in use but the conditions under which it will remain so are different from each of the following values. do-nothing(2) - no action. forwarding(3) - the port has returned to normal operation mode. forwarding-trap(4) - the port has returned to normal operation mode. And the device can send a broadcast falling trap.')
swL2PortCtrlClearCounter = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 2, 1, 15), Integer32()).setMaxAccess("writeonly")
if mibBuilder.loadTexts: swL2PortCtrlClearCounter.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortCtrlClearCounter.setDescription('Sets choosed port to clear counter. First of all, any unsigned integer can be used to set.')
swL2PortStTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3), )
if mibBuilder.loadTexts: swL2PortStTable.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStTable.setDescription('A list of port statistic Counter entries.')
swL2PortStEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1), ).setIndexNames((0, "SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortStUnitIndex"), (0, "SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortStModuleIndex"), (0, "SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortStIndex"))
if mibBuilder.loadTexts: swL2PortStEntry.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStEntry.setDescription('This entry include all the port statistic Counter which support by the device, like Bytes received, Bytes Sent ...')
swL2PortStUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStUnitIndex.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStUnitIndex.setDescription('Indicates ID of the unit in the device.')
swL2PortStModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStModuleIndex.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStModuleIndex.setDescription('Indicates ID of the module on the unit.')
swL2PortStIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStIndex.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStIndex.setDescription('This object indicates the device port number.(1..Max port number)')
swL2PortStByteRx = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStByteRx.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStByteRx.setDescription('swDevCtrlCounterMode = 2(switched-frames) : This counter is incremented once for every data octet of good packets(unicast + multicast + broadcast) received. swDevCtrlCounterMode = 3(all-frames) : This counter is incremented once for every data octet of good packets(unicast + multicast + broadcast packets) and for local and dropped packets.')
swL2PortStByteTx = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStByteTx.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStByteTx.setDescription('This counter is incremented once for every data octet of a transmitted good packet.')
swL2PortStFrameRx = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStFrameRx.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStFrameRx.setDescription('swDevCtrlCounterMode = 2(switched-frames) : This counter is incremented once for every good packet(unicast + multicast + broadcast) received. swDevCtrlCounterMode = 3(all-frames) : This counter is incremented once for every good packet(unicast + multicast + broadcast packets) and for local and dropped packets received.')
swL2PortStFrameTx = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStFrameTx.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStFrameTx.setDescription('This counter is incremented once for every transmitted good packet.')
swL2PortStTotalBytesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStTotalBytesRx.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStTotalBytesRx.setDescription('This counter is incremented once for every data octet of all received packets. This include data octets of rejected and local packets which are not forwarded to the switching core for transmission. This counter should reflect all the data octets received on the line. Note: A nibble is not counted as a whole byte.')
swL2PortStTotalFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStTotalFramesRx.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStTotalFramesRx.setDescription('This counter is incremented once for every received packets. This include rejected and local packets which are not forwarded to the switching core for transmission. This counter should reflect all packets received on the line.')
swL2PortStBroadcastFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStBroadcastFramesRx.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStBroadcastFramesRx.setDescription('swDevCtrlCounterMode = 2(switched-frames) : This counter is incremented once for every good broadcast packet received. swDevCtrlCounterMode = 3(all-frames) : This counter is incremented once for every good broadcast packet received and for local and dropped broadcast packets.')
swL2PortStMulticastFramesRx = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStMulticastFramesRx.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStMulticastFramesRx.setDescription('swDevCtrlCounterMode = 2(switched-frames) : This counter is incremented once for every good multicast packet received. swDevCtrlCounterMode = 3(all-frames) : This counter is incremented once for every good multicast packet received and for local and dropped multicast packets. This counter does not include broadcast packets.')
swL2PortStCRCError = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStCRCError.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStCRCError.setDescription('This counter is incremented once for every received packet which meets all the following conditions: 1. Packet data length is between 64 and 1536 bytes inclusive. 2. Packet has invalid CRC. 3. Collision event, late collision event and receive error event have not been detected.')
swL2PortStOversizeFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStOversizeFrames.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStOversizeFrames.setDescription('The number of good frames with length more than 1536 bytes.')
swL2PortStFragments = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStFragments.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStFragments.setDescription('This counter is incremented once for every received packet which meets all the following conditions: 1. Packet data length is less than 64 bytes or packet withourt SFD and is less than 64 bytes in length. 2. Packet has invalid CRC. 3. Collision event, late collision event and receive error event have not been detected.')
swL2PortStJabber = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStJabber.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStJabber.setDescription('The number of frames with length more than 1536 bytes and with CRC error or misaligned.')
swL2PortStCollision = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStCollision.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStCollision.setDescription('The number of Collisions.')
swL2PortStLateCollision = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStLateCollision.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStLateCollision.setDescription('The number of Late Collision(collision occurring later than 576th transmitted bit).')
swL2PortStFrames_64_bytes = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 18), Counter32()).setLabel("swL2PortStFrames-64-bytes").setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStFrames_64_bytes.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStFrames_64_bytes.setDescription('This counter is incremented once for every received and transmitted packet with size of 64 bytes. This counter includes rejected received and transmitted packets.')
swL2PortStFrames_65_127_bytes = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 19), Counter32()).setLabel("swL2PortStFrames-65-127-bytes").setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStFrames_65_127_bytes.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStFrames_65_127_bytes.setDescription('This counter is incremented once for every received and transmitted packet with size of 65 to 127 bytes. This counter includes rejected received and transmitted packets.')
swL2PortStFrames_128_255_bytes = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 20), Counter32()).setLabel("swL2PortStFrames-128-255-bytes").setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStFrames_128_255_bytes.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStFrames_128_255_bytes.setDescription('This counter is incremented once for every received and transmitted packet with size of 128 to 255 bytes. This counter includes rejected received and transmitted packets.')
swL2PortStFrames_256_511_bytes = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 21), Counter32()).setLabel("swL2PortStFrames-256-511-bytes").setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStFrames_256_511_bytes.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStFrames_256_511_bytes.setDescription('This counter is incremented once for every received and transmitted packet with size of 256 to 511 bytes. This counter includes rejected received and transmitted packets.')
swL2PortStFrames_512_1023_bytes = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 22), Counter32()).setLabel("swL2PortStFrames-512-1023-bytes").setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStFrames_512_1023_bytes.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStFrames_512_1023_bytes.setDescription('This counter is incremented once for every received and transmitted packet with size of 512 to 1023 bytes. This counter includes rejected received and transmitted packets.')
swL2PortStFrames_1024_1536_bytes = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 23), Counter32()).setLabel("swL2PortStFrames-1024-1536-bytes").setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStFrames_1024_1536_bytes.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStFrames_1024_1536_bytes.setDescription('This counter is incremented once for every received and transmitted packet with size of 1024 to 1536 bytes. This counter includes rejected received and transmitted packets.')
swL2PortStFramesDroppedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStFramesDroppedFrames.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStFramesDroppedFrames.setDescription('This counter is incremented once for every received dropped packet.')
swL2PortStMulticastFramesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStMulticastFramesTx.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStMulticastFramesTx.setDescription('The number of multicast frames sent. This counter does not include broadcast packets.')
swL2PortStBroadcastFramesTx = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStBroadcastFramesTx.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStBroadcastFramesTx.setDescription('The number of broadcast frames sent.')
swL2PortStUndersizeFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 4, 3, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL2PortStUndersizeFrames.setStatus('mandatory')
if mibBuilder.loadTexts: swL2PortStUndersizeFrames.setDescription('This counter is incremented once for every received packet which meets all the following conditions: 1. Packet data length is less than 64 bytes. 2. Packet has valid CRC. 3. Collision event, late collision event and receive error event have not been detected.')
swEventPortPartition = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3) + (0,1)).setObjects(("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoUnitIndex"), ("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoModuleIndex"), ("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoIndex"))
if mibBuilder.loadTexts: swEventPortPartition.setDescription('The trap is sent whenever the port state enter the Partion mode when more than 61 collisions occur while trasmitting.')
swEventlinkChangeEvent = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3) + (0,2)).setObjects(("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoUnitIndex"), ("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoModuleIndex"), ("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoIndex"))
if mibBuilder.loadTexts: swEventlinkChangeEvent.setDescription('The trap is sent whenever the link state of a port changes from link up to link down or from link down to link up')
swEventBcastRisingStorm = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3) + (0,3)).setObjects(("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoUnitIndex"), ("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoModuleIndex"), ("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoIndex"))
if mibBuilder.loadTexts: swEventBcastRisingStorm.setDescription('The trap indicates that broadcast higher rising threshold. This trap including the port ID')
swEventBcastFallingStorm = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3) + (0,4)).setObjects(("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoUnitIndex"), ("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoModuleIndex"), ("SW-LAYER2-PORT-MANAGEMENT-MIB", "swL2PortInfoIndex"))
if mibBuilder.loadTexts: swEventBcastFallingStorm.setDescription('The trap indicates that broadcast higher falling threshold. This trap including the port ID')
mibBuilder.exportSymbols("SW-LAYER2-PORT-MANAGEMENT-MIB", swL2PortStCRCError=swL2PortStCRCError, swL2PortStFrames_1024_1536_bytes=swL2PortStFrames_1024_1536_bytes, swL2PortCtrlModuleIndex=swL2PortCtrlModuleIndex, swL2PortStLateCollision=swL2PortStLateCollision, swL2PortStOversizeFrames=swL2PortStOversizeFrames, systems=systems, swL2PortInfoTable=swL2PortInfoTable, golfcommon=golfcommon, swL2PortCtrlAdminState=swL2PortCtrlAdminState, swL2PortStByteRx=swL2PortStByteRx, swL2PortCtrlEntry=swL2PortCtrlEntry, es2000=es2000, swL2PortStFragments=swL2PortStFragments, swL2Mgmt=swL2Mgmt, swL2PortCtrlClearCounter=swL2PortCtrlClearCounter, swL2PortStJabber=swL2PortStJabber, dlinkcommon=dlinkcommon, es2000Mgmt=es2000Mgmt, swL2PortInfoNwayStatus=swL2PortInfoNwayStatus, swL2PortStUnitIndex=swL2PortStUnitIndex, swL2PortInfoUnitIndex=swL2PortInfoUnitIndex, swL2PortStFrames_128_255_bytes=swL2PortStFrames_128_255_bytes, swL2PortStModuleIndex=swL2PortStModuleIndex, swL2PortCtrlStpState=swL2PortCtrlStpState, marconi=marconi, swL2PortCtrlLockState=swL2PortCtrlLockState, swL2PortInfoType=swL2PortInfoType, swL2PortStTotalBytesRx=swL2PortStTotalBytesRx, swL2PortStTable=swL2PortStTable, swL2PortMgmt=swL2PortMgmt, swL2PortInfoIndex=swL2PortInfoIndex, swEventBcastFallingStorm=swEventBcastFallingStorm, swL2PortStMulticastFramesRx=swL2PortStMulticastFramesRx, swL2PortStFramesDroppedFrames=swL2PortStFramesDroppedFrames, swL2PortStFrames_64_bytes=swL2PortStFrames_64_bytes, swL2PortStMulticastFramesTx=swL2PortStMulticastFramesTx, swL2PortCtrlFlowCtrlState=swL2PortCtrlFlowCtrlState, marconi_products=marconi_products, swL2PortStFrames_65_127_bytes=swL2PortStFrames_65_127_bytes, swL2PortStUndersizeFrames=swL2PortStUndersizeFrames, swL2PortStBroadcastFramesTx=swL2PortStBroadcastFramesTx, dlink=dlink, swL2PortStEntry=swL2PortStEntry, external=external, golfproducts=golfproducts, swL2PortStIndex=swL2PortStIndex, swL2PortStFrameRx=swL2PortStFrameRx, marconi_mgmt=marconi_mgmt, golf=golf, swL2PortInfoLinkStatus=swL2PortInfoLinkStatus, swL2PortCtrlTable=swL2PortCtrlTable, swL2PortCtrlLinkStatusAlarmState=swL2PortCtrlLinkStatusAlarmState, swL2PortCtrlHOLState=swL2PortCtrlHOLState, swL2PortCtrlBackPressState=swL2PortCtrlBackPressState, swL2PortStByteTx=swL2PortStByteTx, swL2PortStTotalFramesRx=swL2PortStTotalFramesRx, swL2PortStFrames_256_511_bytes=swL2PortStFrames_256_511_bytes, swEventBcastRisingStorm=swEventBcastRisingStorm, swL2PortCtrlUnitIndex=swL2PortCtrlUnitIndex, swL2PortStFrames_512_1023_bytes=swL2PortStFrames_512_1023_bytes, swL2PortInfoModuleIndex=swL2PortInfoModuleIndex, swL2PortCtrlBcastFallingAct=swL2PortCtrlBcastFallingAct, swL2PortStFrameTx=swL2PortStFrameTx, swL2PortInfoEntry=swL2PortInfoEntry, swProperty=swProperty, swL2PortStBroadcastFramesRx=swL2PortStBroadcastFramesRx, swEventPortPartition=swEventPortPartition, marconi_es2000Prod=marconi_es2000Prod, swEventlinkChangeEvent=swEventlinkChangeEvent, swL2PortStCollision=swL2PortStCollision, swL2PortCtrlBcastRisingAct=swL2PortCtrlBcastRisingAct, swL2PortInfoDescr=swL2PortInfoDescr, swL2PortCtrlPriority=swL2PortCtrlPriority, swL2PortCtrlNwayState=swL2PortCtrlNwayState, swL2PortCtrlIndex=swL2PortCtrlIndex)