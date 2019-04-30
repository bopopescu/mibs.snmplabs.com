#
# PySNMP MIB module ASCEND-MIBSCRTY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBSCRTY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:12:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, IpAddress, MibIdentifier, ObjectIdentity, Unsigned32, Counter64, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Gauge32, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "MibIdentifier", "ObjectIdentity", "Unsigned32", "Counter64", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Gauge32", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibsecurityProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 107))
mibsecurityProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 107, 1), )
if mibBuilder.loadTexts: mibsecurityProfileTable.setStatus('mandatory')
mibsecurityProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1), ).setIndexNames((0, "ASCEND-MIBSCRTY-MIB", "securityProfile-Name"))
if mibBuilder.loadTexts: mibsecurityProfileEntry.setStatus('mandatory')
securityProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 1), DisplayString()).setLabel("securityProfile-Name").setMaxAccess("readonly")
if mibBuilder.loadTexts: securityProfile_Name.setStatus('mandatory')
securityProfile_Password = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 2), DisplayString()).setLabel("securityProfile-Password").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_Password.setStatus('mandatory')
securityProfile_Operations = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("securityProfile-Operations").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_Operations.setStatus('mandatory')
securityProfile_EditSecurity = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("securityProfile-EditSecurity").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_EditSecurity.setStatus('mandatory')
securityProfile_EditSystem = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("securityProfile-EditSystem").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_EditSystem.setStatus('mandatory')
securityProfile_EditLine = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("securityProfile-EditLine").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_EditLine.setStatus('mandatory')
securityProfile_EditOwnPort = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("securityProfile-EditOwnPort").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_EditOwnPort.setStatus('mandatory')
securityProfile_EditAllPort = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("securityProfile-EditAllPort").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_EditAllPort.setStatus('mandatory')
securityProfile_EditCurCall = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("securityProfile-EditCurCall").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_EditCurCall.setStatus('mandatory')
securityProfile_EditOwnCall = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("securityProfile-EditOwnCall").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_EditOwnCall.setStatus('mandatory')
securityProfile_EditComCall = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("securityProfile-EditComCall").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_EditComCall.setStatus('mandatory')
securityProfile_EditAllCall = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("securityProfile-EditAllCall").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_EditAllCall.setStatus('mandatory')
securityProfile_SysDiag = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("securityProfile-SysDiag").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_SysDiag.setStatus('mandatory')
securityProfile_OwnPortDiag = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("securityProfile-OwnPortDiag").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_OwnPortDiag.setStatus('mandatory')
securityProfile_AllPortDiag = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("securityProfile-AllPortDiag").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_AllPortDiag.setStatus('mandatory')
securityProfile_Download = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("securityProfile-Download").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_Download.setStatus('mandatory')
securityProfile_Upload = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("securityProfile-Upload").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_Upload.setStatus('mandatory')
securityProfile_FieldService = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("securityProfile-FieldService").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_FieldService.setStatus('mandatory')
securityProfile_UseTacacsPlus = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("securityProfile-UseTacacsPlus").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_UseTacacsPlus.setStatus('mandatory')
securityProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 107, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("securityProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: securityProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBSCRTY-MIB", securityProfile_Upload=securityProfile_Upload, securityProfile_UseTacacsPlus=securityProfile_UseTacacsPlus, securityProfile_EditAllPort=securityProfile_EditAllPort, securityProfile_EditComCall=securityProfile_EditComCall, securityProfile_EditSecurity=securityProfile_EditSecurity, DisplayString=DisplayString, securityProfile_Password=securityProfile_Password, securityProfile_EditOwnPort=securityProfile_EditOwnPort, securityProfile_FieldService=securityProfile_FieldService, securityProfile_Operations=securityProfile_Operations, securityProfile_EditSystem=securityProfile_EditSystem, securityProfile_OwnPortDiag=securityProfile_OwnPortDiag, securityProfile_EditAllCall=securityProfile_EditAllCall, securityProfile_EditOwnCall=securityProfile_EditOwnCall, mibsecurityProfileEntry=mibsecurityProfileEntry, mibsecurityProfile=mibsecurityProfile, securityProfile_Name=securityProfile_Name, securityProfile_SysDiag=securityProfile_SysDiag, securityProfile_Download=securityProfile_Download, securityProfile_AllPortDiag=securityProfile_AllPortDiag, securityProfile_Action_o=securityProfile_Action_o, mibsecurityProfileTable=mibsecurityProfileTable, securityProfile_EditCurCall=securityProfile_EditCurCall, securityProfile_EditLine=securityProfile_EditLine)