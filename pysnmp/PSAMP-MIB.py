#
# PySNMP MIB module PSAMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PSAMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:33:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Unsigned64TC, = mibBuilder.importSymbols("APPLICATION-MIB", "Unsigned64TC")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
Float64TC, = mibBuilder.importSymbols("FLOAT-TC-MIB", "Float64TC")
ipfixSelectorFunctions, = mibBuilder.importSymbols("IPFIX-SELECTOR-MIB", "ipfixSelectorFunctions")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, NotificationType, TimeTicks, ObjectIdentity, IpAddress, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, iso, Counter64, MibIdentifier, Integer32, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "TimeTicks", "ObjectIdentity", "IpAddress", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "iso", "Counter64", "MibIdentifier", "Integer32", "Bits", "Unsigned32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
psampMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 212))
psampMIB.setRevisions(('2012-09-05 12:00',))
if mibBuilder.loadTexts: psampMIB.setLastUpdated('201209051200Z')
if mibBuilder.loadTexts: psampMIB.setOrganization('IETF IPFIX Working Group')
psampObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 212, 1))
psampConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 212, 2))
psampSampCountBased = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 1, 1, 2))
psampSampCountBasedAvail = MibScalar((1, 3, 6, 1, 2, 1, 194, 1, 1, 2, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psampSampCountBasedAvail.setStatus('current')
psampSampCountBasedParamSetTable = MibTable((1, 3, 6, 1, 2, 1, 194, 1, 1, 2, 2), )
if mibBuilder.loadTexts: psampSampCountBasedParamSetTable.setStatus('current')
psampSampCountBasedParamSetEntry = MibTableRow((1, 3, 6, 1, 2, 1, 194, 1, 1, 2, 2, 1), ).setIndexNames((0, "PSAMP-MIB", "psampSampCountBasedIndex"))
if mibBuilder.loadTexts: psampSampCountBasedParamSetEntry.setStatus('current')
psampSampCountBasedIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: psampSampCountBasedIndex.setStatus('current')
psampSampCountBasedInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 2, 2, 1, 2), Unsigned32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: psampSampCountBasedInterval.setStatus('current')
psampSampCountBasedSpace = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 2, 2, 1, 3), Unsigned32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: psampSampCountBasedSpace.setStatus('current')
psampSampTimeBased = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 1, 1, 3))
psampSampTimeBasedAvail = MibScalar((1, 3, 6, 1, 2, 1, 194, 1, 1, 3, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psampSampTimeBasedAvail.setStatus('current')
psampSampTimeBasedParamSetTable = MibTable((1, 3, 6, 1, 2, 1, 194, 1, 1, 3, 2), )
if mibBuilder.loadTexts: psampSampTimeBasedParamSetTable.setStatus('current')
psampSampTimeBasedParamSetEntry = MibTableRow((1, 3, 6, 1, 2, 1, 194, 1, 1, 3, 2, 1), ).setIndexNames((0, "PSAMP-MIB", "psampSampTimeBasedIndex"))
if mibBuilder.loadTexts: psampSampTimeBasedParamSetEntry.setStatus('current')
psampSampTimeBasedIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: psampSampTimeBasedIndex.setStatus('current')
psampSampTimeBasedInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 3, 2, 1, 2), Unsigned32()).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: psampSampTimeBasedInterval.setStatus('current')
psampSampTimeBasedSpace = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 3, 2, 1, 3), Unsigned32()).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: psampSampTimeBasedSpace.setStatus('current')
psampSampRandOutOfN = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 1, 1, 4))
psampSampRandOutOfNAvail = MibScalar((1, 3, 6, 1, 2, 1, 194, 1, 1, 4, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psampSampRandOutOfNAvail.setStatus('current')
psampSampRandOutOfNParamSetTable = MibTable((1, 3, 6, 1, 2, 1, 194, 1, 1, 4, 2), )
if mibBuilder.loadTexts: psampSampRandOutOfNParamSetTable.setStatus('current')
psampSampRandOutOfNParamSetEntry = MibTableRow((1, 3, 6, 1, 2, 1, 194, 1, 1, 4, 2, 1), ).setIndexNames((0, "PSAMP-MIB", "psampSampRandOutOfNIndex"))
if mibBuilder.loadTexts: psampSampRandOutOfNParamSetEntry.setStatus('current')
psampSampRandOutOfNIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: psampSampRandOutOfNIndex.setStatus('current')
psampSampRandOutOfNSize = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 4, 2, 1, 2), Unsigned32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: psampSampRandOutOfNSize.setStatus('current')
psampSampRandOutOfNPopulation = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 4, 2, 1, 3), Unsigned32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: psampSampRandOutOfNPopulation.setStatus('current')
psampSampUniProb = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 1, 1, 5))
psampSampUniProbAvail = MibScalar((1, 3, 6, 1, 2, 1, 194, 1, 1, 5, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psampSampUniProbAvail.setStatus('current')
psampSampUniProbParamSetTable = MibTable((1, 3, 6, 1, 2, 1, 194, 1, 1, 5, 2), )
if mibBuilder.loadTexts: psampSampUniProbParamSetTable.setStatus('current')
psampSampUniProbParamSetEntry = MibTableRow((1, 3, 6, 1, 2, 1, 194, 1, 1, 5, 2, 1), ).setIndexNames((0, "PSAMP-MIB", "psampSampUniProbIndex"))
if mibBuilder.loadTexts: psampSampUniProbParamSetEntry.setStatus('current')
psampSampUniProbIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 5, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: psampSampUniProbIndex.setStatus('current')
psampSampUniProbProbability = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 5, 2, 1, 2), Float64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psampSampUniProbProbability.setStatus('current')
psampFiltPropMatch = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 1, 1, 6))
psampFiltPropMatchAvail = MibScalar((1, 3, 6, 1, 2, 1, 194, 1, 1, 6, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psampFiltPropMatchAvail.setStatus('current')
psampFiltHash = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 1, 1, 7))
psampFiltHashAvail = MibScalar((1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psampFiltHashAvail.setStatus('current')
psampFiltHashCapabilities = MibIdentifier((1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 2))
psampFiltHashParamSetTable = MibTable((1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3), )
if mibBuilder.loadTexts: psampFiltHashParamSetTable.setStatus('current')
psampFiltHashParamSetEntry = MibTableRow((1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1), ).setIndexNames((0, "PSAMP-MIB", "psampFiltHashIndex"))
if mibBuilder.loadTexts: psampFiltHashParamSetEntry.setStatus('current')
psampFiltHashIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: psampFiltHashIndex.setStatus('current')
psampFiltHashFunction = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("crc32", 1), ("ipsx", 2), ("bob", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psampFiltHashFunction.setStatus('current')
psampFiltHashInitializerValue = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1, 3), Unsigned64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psampFiltHashInitializerValue.setStatus('current')
psampFiltHashIpPayloadOffset = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1, 4), Unsigned64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psampFiltHashIpPayloadOffset.setStatus('current')
psampFiltHashIpPayloadSize = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1, 5), Unsigned64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psampFiltHashIpPayloadSize.setStatus('current')
psampFiltHashSelectedRangeMin = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1, 6), Unsigned64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psampFiltHashSelectedRangeMin.setStatus('current')
psampFiltHashSelectedRangeMax = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1, 7), Unsigned64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psampFiltHashSelectedRangeMax.setStatus('current')
psampFiltHashOutputRangeMin = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1, 8), Unsigned64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psampFiltHashOutputRangeMin.setStatus('current')
psampFiltHashOutputRangeMax = MibTableColumn((1, 3, 6, 1, 2, 1, 194, 1, 1, 7, 3, 1, 9), Unsigned64TC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psampFiltHashOutputRangeMax.setStatus('current')
psampCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 212, 2, 1))
psampGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 212, 2, 2))
psampCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 212, 2, 1, 1)).setObjects(("PSAMP-MIB", "psampGroupSampCountBased"), ("PSAMP-MIB", "psampGroupSampTimeBased"), ("PSAMP-MIB", "psampGroupSampRandOutOfN"), ("PSAMP-MIB", "psampGroupSampUniProb"), ("PSAMP-MIB", "psampGroupFiltPropMatch"), ("PSAMP-MIB", "psampGroupFiltHash"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    psampCompliance = psampCompliance.setStatus('current')
psampGroupSampCountBased = ObjectGroup((1, 3, 6, 1, 2, 1, 212, 2, 2, 1)).setObjects(("PSAMP-MIB", "psampSampCountBasedAvail"), ("PSAMP-MIB", "psampSampCountBasedInterval"), ("PSAMP-MIB", "psampSampCountBasedSpace"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    psampGroupSampCountBased = psampGroupSampCountBased.setStatus('current')
psampGroupSampTimeBased = ObjectGroup((1, 3, 6, 1, 2, 1, 212, 2, 2, 2)).setObjects(("PSAMP-MIB", "psampSampTimeBasedAvail"), ("PSAMP-MIB", "psampSampTimeBasedInterval"), ("PSAMP-MIB", "psampSampTimeBasedSpace"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    psampGroupSampTimeBased = psampGroupSampTimeBased.setStatus('current')
psampGroupSampRandOutOfN = ObjectGroup((1, 3, 6, 1, 2, 1, 212, 2, 2, 3)).setObjects(("PSAMP-MIB", "psampSampRandOutOfNAvail"), ("PSAMP-MIB", "psampSampRandOutOfNSize"), ("PSAMP-MIB", "psampSampRandOutOfNPopulation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    psampGroupSampRandOutOfN = psampGroupSampRandOutOfN.setStatus('current')
psampGroupSampUniProb = ObjectGroup((1, 3, 6, 1, 2, 1, 212, 2, 2, 4)).setObjects(("PSAMP-MIB", "psampSampUniProbAvail"), ("PSAMP-MIB", "psampSampUniProbProbability"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    psampGroupSampUniProb = psampGroupSampUniProb.setStatus('current')
psampGroupFiltPropMatch = ObjectGroup((1, 3, 6, 1, 2, 1, 212, 2, 2, 5)).setObjects(("PSAMP-MIB", "psampFiltPropMatchAvail"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    psampGroupFiltPropMatch = psampGroupFiltPropMatch.setStatus('current')
psampGroupFiltHash = ObjectGroup((1, 3, 6, 1, 2, 1, 212, 2, 2, 6)).setObjects(("PSAMP-MIB", "psampFiltHashAvail"), ("PSAMP-MIB", "psampFiltHashFunction"), ("PSAMP-MIB", "psampFiltHashInitializerValue"), ("PSAMP-MIB", "psampFiltHashIpPayloadOffset"), ("PSAMP-MIB", "psampFiltHashIpPayloadSize"), ("PSAMP-MIB", "psampFiltHashSelectedRangeMin"), ("PSAMP-MIB", "psampFiltHashSelectedRangeMax"), ("PSAMP-MIB", "psampFiltHashOutputRangeMin"), ("PSAMP-MIB", "psampFiltHashOutputRangeMax"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    psampGroupFiltHash = psampGroupFiltHash.setStatus('current')
mibBuilder.exportSymbols("PSAMP-MIB", psampSampRandOutOfNParamSetEntry=psampSampRandOutOfNParamSetEntry, psampFiltHashOutputRangeMax=psampFiltHashOutputRangeMax, psampSampTimeBased=psampSampTimeBased, psampFiltHashParamSetTable=psampFiltHashParamSetTable, psampFiltHashFunction=psampFiltHashFunction, psampConformance=psampConformance, psampFiltHashAvail=psampFiltHashAvail, psampSampRandOutOfNAvail=psampSampRandOutOfNAvail, psampSampUniProbAvail=psampSampUniProbAvail, psampSampCountBasedAvail=psampSampCountBasedAvail, psampSampUniProbParamSetTable=psampSampUniProbParamSetTable, psampSampTimeBasedIndex=psampSampTimeBasedIndex, psampGroups=psampGroups, psampSampTimeBasedAvail=psampSampTimeBasedAvail, psampCompliances=psampCompliances, psampGroupSampUniProb=psampGroupSampUniProb, psampGroupFiltHash=psampGroupFiltHash, psampObjects=psampObjects, psampFiltHashCapabilities=psampFiltHashCapabilities, psampSampUniProbProbability=psampSampUniProbProbability, psampFiltHashSelectedRangeMin=psampFiltHashSelectedRangeMin, psampGroupSampRandOutOfN=psampGroupSampRandOutOfN, psampGroupFiltPropMatch=psampGroupFiltPropMatch, psampSampCountBasedParamSetTable=psampSampCountBasedParamSetTable, psampSampCountBased=psampSampCountBased, psampGroupSampTimeBased=psampGroupSampTimeBased, psampSampUniProbParamSetEntry=psampSampUniProbParamSetEntry, psampFiltHashIpPayloadOffset=psampFiltHashIpPayloadOffset, psampSampCountBasedIndex=psampSampCountBasedIndex, psampCompliance=psampCompliance, psampSampRandOutOfNPopulation=psampSampRandOutOfNPopulation, psampSampTimeBasedSpace=psampSampTimeBasedSpace, psampFiltHashIndex=psampFiltHashIndex, PYSNMP_MODULE_ID=psampMIB, psampSampUniProb=psampSampUniProb, psampSampCountBasedInterval=psampSampCountBasedInterval, psampMIB=psampMIB, psampSampUniProbIndex=psampSampUniProbIndex, psampSampTimeBasedParamSetTable=psampSampTimeBasedParamSetTable, psampSampRandOutOfNSize=psampSampRandOutOfNSize, psampFiltHashSelectedRangeMax=psampFiltHashSelectedRangeMax, psampFiltHashInitializerValue=psampFiltHashInitializerValue, psampGroupSampCountBased=psampGroupSampCountBased, psampSampCountBasedParamSetEntry=psampSampCountBasedParamSetEntry, psampFiltPropMatch=psampFiltPropMatch, psampSampTimeBasedParamSetEntry=psampSampTimeBasedParamSetEntry, psampSampCountBasedSpace=psampSampCountBasedSpace, psampFiltHashOutputRangeMin=psampFiltHashOutputRangeMin, psampSampTimeBasedInterval=psampSampTimeBasedInterval, psampSampRandOutOfNIndex=psampSampRandOutOfNIndex, psampFiltHashParamSetEntry=psampFiltHashParamSetEntry, psampSampRandOutOfNParamSetTable=psampSampRandOutOfNParamSetTable, psampFiltPropMatchAvail=psampFiltPropMatchAvail, psampFiltHashIpPayloadSize=psampFiltHashIpPayloadSize, psampSampRandOutOfN=psampSampRandOutOfN, psampFiltHash=psampFiltHash)