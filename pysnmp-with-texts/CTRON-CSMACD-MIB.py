#
# PySNMP MIB module CTRON-CSMACD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-CSMACD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:29:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ctCSMACD, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctCSMACD")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibIdentifier, ModuleIdentity, TimeTicks, Integer32, NotificationType, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, iso, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Integer32", "NotificationType", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "iso", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctFnbCSMACD = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 1))
ctFnbPortConnect = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2))
ctFnbCSMACDTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 1, 1), )
if mibBuilder.loadTexts: ctFnbCSMACDTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbCSMACDTable.setDescription('A list of entries that provide connection status of CSMA/CD subsystems, for the FNB.')
ctFnbCSMACDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 1, 1, 1), ).setIndexNames((0, "CTRON-CSMACD-MIB", "ctFnbCSMACDIndex"))
if mibBuilder.loadTexts: ctFnbCSMACDEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbCSMACDEntry.setDescription('An entry in the ctFnbCSMACDTable containing objects that provide FNB connection status for a CSMA/CD subsystem.')
ctFnbCSMACDIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 1, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFnbCSMACDIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbCSMACDIndex.setDescription("An unique value for each CSMACD subsystem. Its value ranges between 1 and chassisSlots. The value for each interface must remain constant, at least, from one re-initialization of the entity's network management system to the next re-initialization.")
ctFnbConnect = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("connectB", 1), ("connectC", 2), ("disconnect", 3), ("connectA", 4), ("subnetB", 5), ("subnetC", 6), ("multiChannel", 7), ("frontpanel", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFnbConnect.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbConnect.setDescription('Denotes the connection status of the CSMA/CD board to the inter-RIC bus. The values of 1, 2, and 4 define connection status of connect for the subsystem, values 5 and 6 define connection status of subnet connect for the subsystem, value 8 is defined as a front panel connection on the module, and a value of 3 defines disconnect status.')
ctFnbPortChanges = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFnbPortChanges.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbPortChanges.setDescription("Denotes the number of times any port on the given MIM has changed it's connection to the inter-RIC bus.")
ctFnbPortConnectTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 1), )
if mibBuilder.loadTexts: ctFnbPortConnectTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbPortConnectTable.setDescription('This table is used to control port association on ethernet devices. Only those boards that support port switching will be listed in this table.')
ctFnbPortConnectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 1, 1), ).setIndexNames((0, "CTRON-CSMACD-MIB", "ctFnbPortConnectBoardIndex"), (0, "CTRON-CSMACD-MIB", "ctFnbPortConnectPortIndex"))
if mibBuilder.loadTexts: ctFnbPortConnectEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbPortConnectEntry.setDescription('Describes a specific port connection entry.')
ctFnbPortConnectBoardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFnbPortConnectBoardIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbPortConnectBoardIndex.setDescription('An instance of a board for which this port assignment relationship exists.')
ctFnbPortConnectPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFnbPortConnectPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbPortConnectPortIndex.setDescription('An instance of a port for which this assignment relationship exists.')
ctFnbPortConnectPortAssignment = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("connectA", 1), ("connectB", 2), ("connectC", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFnbPortConnectPortAssignment.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbPortConnectPortAssignment.setDescription('The specific channel that the port is assigned.')
ctFnbPortCompID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFnbPortCompID.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbPortCompID.setDescription('This is the component ID as defined in the chassis MIB that this port is associated with. These components will be repeater components.')
ctFnbPortConnectionChanges = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctFnbPortConnectionChanges.setStatus('mandatory')
if mibBuilder.loadTexts: ctFnbPortConnectionChanges.setDescription("Maintains the number of times any port within the mangement domain of this MIM changes it's port assignment.")
mibBuilder.exportSymbols("CTRON-CSMACD-MIB", ctFnbPortConnect=ctFnbPortConnect, ctFnbPortConnectPortIndex=ctFnbPortConnectPortIndex, ctFnbPortConnectEntry=ctFnbPortConnectEntry, ctFnbCSMACDIndex=ctFnbCSMACDIndex, ctFnbPortConnectPortAssignment=ctFnbPortConnectPortAssignment, ctFnbPortConnectionChanges=ctFnbPortConnectionChanges, ctFnbConnect=ctFnbConnect, ctFnbCSMACDEntry=ctFnbCSMACDEntry, ctFnbPortConnectBoardIndex=ctFnbPortConnectBoardIndex, ctFnbPortCompID=ctFnbPortCompID, ctFnbPortConnectTable=ctFnbPortConnectTable, ctFnbCSMACDTable=ctFnbCSMACDTable, ctFnbCSMACD=ctFnbCSMACD, ctFnbPortChanges=ctFnbPortChanges)