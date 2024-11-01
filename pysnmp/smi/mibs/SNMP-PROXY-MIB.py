#
# This file is part of pysnmp software.
#
# Copyright (c) 2005-2020, Ilya Etingof <etingof@gmail.com>
# License: https://www.pysnmp.com/pysnmp/license.html
#
# PySNMP MIB module SNMP-PROXY-MIB (https://www.pysnmp.com/pysnmp)
# ASN.1 source http://mibs.pysnmp.com:80/asn1/SNMP-PROXY-MIB
# Produced by pysmi-0.1.3 at Tue Apr 18 00:43:17 2017
# On host grommit.local platform Darwin version 16.4.0 by user ilya
# Using Python version 3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22)
#
ObjectIdentifier, Integer, OctetString = mibBuilder.import_symbols(
    "ASN1", "ObjectIdentifier", "Integer", "OctetString"
)
(NamedValues,) = mibBuilder.import_symbols("ASN1-ENUMERATION", "NamedValues")
(
    SingleValueConstraint,
    ValueSizeConstraint,
    ConstraintsUnion,
    ValueRangeConstraint,
    ConstraintsIntersection,
) = mibBuilder.import_symbols(
    "ASN1-REFINEMENT",
    "SingleValueConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion",
    "ValueRangeConstraint",
    "ConstraintsIntersection",
)
SnmpAdminString, SnmpEngineID = mibBuilder.import_symbols(
    "SNMP-FRAMEWORK-MIB", "SnmpAdminString", "SnmpEngineID"
)
(SnmpTagValue,) = mibBuilder.import_symbols("SNMP-TARGET-MIB", "SnmpTagValue")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.import_symbols(
    "SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup"
)
(
    ModuleIdentity,
    Counter64,
    Gauge32,
    Integer32,
    Bits,
    MibScalar,
    MibTable,
    MibTableRow,
    MibTableColumn,
    MibIdentifier,
    NotificationType,
    iso,
    Counter32,
    ObjectIdentity,
    IpAddress,
    TimeTicks,
    Unsigned32,
    snmpModules,
) = mibBuilder.import_symbols(
    "SNMPv2-SMI",
    "ModuleIdentity",
    "Counter64",
    "Gauge32",
    "Integer32",
    "Bits",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "MibIdentifier",
    "NotificationType",
    "iso",
    "Counter32",
    "ObjectIdentity",
    "IpAddress",
    "TimeTicks",
    "Unsigned32",
    "snmpModules",
)
TextualConvention, RowStatus, DisplayString, StorageType = mibBuilder.import_symbols(
    "SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "StorageType"
)
snmpProxyMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 14))
if mibBuilder.loadTexts:
    snmpProxyMIB.setRevisions(
        (
            "1998-08-04 00:00",
            "1997-07-14 00:00",
        )
    )
if mibBuilder.loadTexts:
    snmpProxyMIB.setLastUpdated("9808040000Z")
if mibBuilder.loadTexts:
    snmpProxyMIB.setOrganization("IETF SNMPv3 Working Group")
if mibBuilder.loadTexts:
    snmpProxyMIB.setContactInfo(
        "WG-email: snmpv3@lists.tislabs.com Subscribe: majordomo@lists.tislabs.com In message body: subscribe snmpv3 Chair: Russ Mundy Trusted Information Systems Postal: 3060 Washington Rd Glenwood MD 21738 USA EMail: mundy@tislabs.com Phone: +1-301-854-6889 Co-editor: David B. Levi SNMP Research, Inc. Postal: 3001 Kimberlin Heights Road Knoxville, TN 37920-9716 EMail: levi@snmp.com Phone: +1 423 573 1434 Co-editor: Paul Meyer Secure Computing Corporation Postal: 2675 Long Lake Road Roseville, MN 55113 EMail: paul_meyer@securecomputing.com Phone: +1 651 628 1592 Co-editor: Bob Stewart Cisco Systems, Inc. Postal: 170 West Tasman Drive San Jose, CA 95134-1706 EMail: bstewart@cisco.com Phone: +1 603 654 2686"
    )
if mibBuilder.loadTexts:
    snmpProxyMIB.setDescription(
        "This MIB module defines MIB objects which provide mechanisms to remotely configure the parameters used by a proxy forwarding application."
    )
snmpProxyObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 14, 1))
snmpProxyConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 14, 3))
snmpProxyTable = MibTable(
    (1, 3, 6, 1, 6, 3, 14, 1, 2),
)
if mibBuilder.loadTexts:
    snmpProxyTable.setStatus("current")
if mibBuilder.loadTexts:
    snmpProxyTable.setDescription(
        "The table of translation parameters used by proxy forwarder applications for forwarding SNMP messages."
    )
snmpProxyEntry = MibTableRow(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1),
).setIndexNames((1, "SNMP-PROXY-MIB", "snmpProxyName"))
if mibBuilder.loadTexts:
    snmpProxyEntry.setStatus("current")
if mibBuilder.loadTexts:
    snmpProxyEntry.setDescription(
        "A set of translation parameters used by a proxy forwarder application for forwarding SNMP messages. Entries in the snmpProxyTable are created and deleted using the snmpProxyRowStatus object."
    )
snmpProxyName = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 1),
    SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)),
)
if mibBuilder.loadTexts:
    snmpProxyName.setStatus("current")
if mibBuilder.loadTexts:
    snmpProxyName.setDescription(
        "The locally arbitrary, but unique identifier associated with this snmpProxyEntry."
    )
snmpProxyType = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 2),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4)))
    .clone(
        namedValues=NamedValues(("read", 1), ("write", 2), ("trap", 3), ("inform", 4))
    ),
).setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpProxyType.setStatus("current")
if mibBuilder.loadTexts:
    snmpProxyType.setDescription(
        "The type of message that may be forwarded using the translation parameters defined by this entry."
    )
snmpProxyContextEngineID = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 3), SnmpEngineID()
).setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpProxyContextEngineID.setStatus("current")
if mibBuilder.loadTexts:
    snmpProxyContextEngineID.setDescription(
        "The contextEngineID contained in messages that may be forwarded using the translation parameters defined by this entry."
    )
snmpProxyContextName = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 4), SnmpAdminString()
).setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpProxyContextName.setStatus("current")
if mibBuilder.loadTexts:
    snmpProxyContextName.setDescription(
        "The contextName contained in messages that may be forwarded using the translation parameters defined by this entry. This object is optional, and if not supported, the contextName contained in a message is ignored when selecting an entry in the snmpProxyTable."
    )
snmpProxyTargetParamsIn = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 5), SnmpAdminString()
).setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpProxyTargetParamsIn.setStatus("current")
if mibBuilder.loadTexts:
    snmpProxyTargetParamsIn.setDescription(
        "This object selects an entry in the snmpTargetParamsTable. The selected entry is used to determine which row of the snmpProxyTable to use for forwarding received messages."
    )
snmpProxySingleTargetOut = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 6), SnmpAdminString()
).setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpProxySingleTargetOut.setStatus("current")
if mibBuilder.loadTexts:
    snmpProxySingleTargetOut.setDescription(
        "This object selects a management target defined in the snmpTargetAddrTable (in the SNMP-TARGET-MIB). The selected target is defined by an entry in the snmpTargetAddrTable whose index value (snmpTargetAddrName) is equal to this object. This object is only used when selection of a single target is required (i.e. when forwarding an incoming read or write request)."
    )
snmpProxyMultipleTargetOut = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 7), SnmpTagValue()
).setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpProxyMultipleTargetOut.setStatus("current")
if mibBuilder.loadTexts:
    snmpProxyMultipleTargetOut.setDescription(
        "This object selects a set of management targets defined in the snmpTargetAddrTable (in the SNMP-TARGET-MIB). This object is only used when selection of multiple targets is required (i.e. when forwarding an incoming notification)."
    )
snmpProxyStorageType = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 8), StorageType().clone("nonVolatile")
).setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpProxyStorageType.setStatus("current")
if mibBuilder.loadTexts:
    snmpProxyStorageType.setDescription("The storage type of this conceptual row.")
snmpProxyRowStatus = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 14, 1, 2, 1, 9), RowStatus()
).setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpProxyRowStatus.setStatus("current")
if mibBuilder.loadTexts:
    snmpProxyRowStatus.setDescription(
        "The status of this conceptual row. To create a row in this table, a manager must set this object to either createAndGo(4) or createAndWait(5). The following objects may not be modified while the value of this object is active(1): - snmpProxyType - snmpProxyContextEngineID - snmpProxyContextName - snmpProxyTargetParamsIn - snmpProxySingleTargetOut - snmpProxyMultipleTargetOut"
    )
snmpProxyCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 14, 3, 1))
snmpProxyGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 14, 3, 2))
snmpProxyCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 14, 3, 1, 1)).setObjects(
    ("SNMP-TARGET-MIB", "snmpTargetBasicGroup"),
    ("SNMP-TARGET-MIB", "snmpTargetResponseGroup"),
    ("SNMP-PROXY-MIB", "snmpProxyGroup"),
)
if mibBuilder.loadTexts:
    snmpProxyCompliance.setDescription(
        "The compliance statement for SNMP entities which include a proxy forwarding application."
    )
snmpProxyGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 14, 3, 2, 3)).setObjects(
    ("SNMP-PROXY-MIB", "snmpProxyType"),
    ("SNMP-PROXY-MIB", "snmpProxyContextEngineID"),
    ("SNMP-PROXY-MIB", "snmpProxyContextName"),
    ("SNMP-PROXY-MIB", "snmpProxyTargetParamsIn"),
    ("SNMP-PROXY-MIB", "snmpProxySingleTargetOut"),
    ("SNMP-PROXY-MIB", "snmpProxyMultipleTargetOut"),
    ("SNMP-PROXY-MIB", "snmpProxyStorageType"),
    ("SNMP-PROXY-MIB", "snmpProxyRowStatus"),
)
if mibBuilder.loadTexts:
    snmpProxyGroup.setDescription(
        "A collection of objects providing remote configuration of management target translation parameters for use by proxy forwarder applications."
    )
mibBuilder.export_symbols(
    "SNMP-PROXY-MIB",
    snmpProxyObjects=snmpProxyObjects,
    snmpProxyType=snmpProxyType,
    snmpProxyRowStatus=snmpProxyRowStatus,
    snmpProxyName=snmpProxyName,
    snmpProxyGroups=snmpProxyGroups,
    snmpProxySingleTargetOut=snmpProxySingleTargetOut,
    snmpProxyGroup=snmpProxyGroup,
    snmpProxyConformance=snmpProxyConformance,
    snmpProxyCompliance=snmpProxyCompliance,
    PYSNMP_MODULE_ID=snmpProxyMIB,
    snmpProxyContextEngineID=snmpProxyContextEngineID,
    snmpProxyCompliances=snmpProxyCompliances,
    snmpProxyStorageType=snmpProxyStorageType,
    snmpProxyEntry=snmpProxyEntry,
    snmpProxyTargetParamsIn=snmpProxyTargetParamsIn,
    snmpProxyContextName=snmpProxyContextName,
    snmpProxyMultipleTargetOut=snmpProxyMultipleTargetOut,
    snmpProxyTable=snmpProxyTable,
    snmpProxyMIB=snmpProxyMIB,
)
