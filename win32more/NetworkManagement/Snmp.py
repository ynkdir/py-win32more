from win32more import *
import win32more.NetworkManagement.Snmp
import win32more.Foundation

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.NetworkManagement.Snmp, name, globals()[f"_define_{name}"]())
    return getattr(win32more.NetworkManagement.Snmp, name)
def __dir__():
    return __all__
ASN_UNIVERSAL = 0
ASN_APPLICATION = 64
ASN_CONTEXT = 128
ASN_PRIVATE = 192
ASN_PRIMITIVE = 0
ASN_CONSTRUCTOR = 32
SNMP_ACCESS_NONE = 0
SNMP_ACCESS_NOTIFY = 1
SNMP_ACCESS_READ_ONLY = 2
SNMP_ACCESS_READ_WRITE = 3
SNMP_ACCESS_READ_CREATE = 4
SNMPAPI_NOERROR = 1
SNMPAPI_ERROR = 0
SNMP_OUTPUT_TO_EVENTLOG = 4
DEFAULT_SNMP_PORT_UDP = 161
DEFAULT_SNMP_PORT_IPX = 36879
DEFAULT_SNMPTRAP_PORT_UDP = 162
DEFAULT_SNMPTRAP_PORT_IPX = 36880
SNMP_MAX_OID_LEN = 128
SNMP_MEM_ALLOC_ERROR = 1
SNMP_BERAPI_INVALID_LENGTH = 10
SNMP_BERAPI_INVALID_TAG = 11
SNMP_BERAPI_OVERFLOW = 12
SNMP_BERAPI_SHORT_BUFFER = 13
SNMP_BERAPI_INVALID_OBJELEM = 14
SNMP_PDUAPI_UNRECOGNIZED_PDU = 20
SNMP_PDUAPI_INVALID_ES = 21
SNMP_PDUAPI_INVALID_GT = 22
SNMP_AUTHAPI_INVALID_VERSION = 30
SNMP_AUTHAPI_INVALID_MSG_TYPE = 31
SNMP_AUTHAPI_TRIV_AUTH_FAILED = 32
ASN_CONTEXTSPECIFIC = 128
ASN_PRIMATIVE = 0
SNMP_MGMTAPI_TIMEOUT = 40
SNMP_MGMTAPI_SELECT_FDERRORS = 41
SNMP_MGMTAPI_TRAP_ERRORS = 42
SNMP_MGMTAPI_TRAP_DUPINIT = 43
SNMP_MGMTAPI_NOTRAPS = 44
SNMP_MGMTAPI_AGAIN = 45
SNMP_MGMTAPI_INVALID_CTL = 46
SNMP_MGMTAPI_INVALID_SESSION = 47
SNMP_MGMTAPI_INVALID_BUFFER = 48
MGMCTL_SETAGENTPORT = 1
MAXOBJIDSIZE = 128
MAXOBJIDSTRSIZE = 1408
SNMPLISTEN_USEENTITY_ADDR = 0
SNMPLISTEN_ALL_ADDR = 1
SNMP_TRAP_COLDSTART = 0
SNMP_TRAP_WARMSTART = 1
SNMP_TRAP_LINKDOWN = 2
SNMP_TRAP_LINKUP = 3
SNMP_TRAP_AUTHFAIL = 4
SNMP_TRAP_EGPNEIGHBORLOSS = 5
SNMP_TRAP_ENTERPRISESPECIFIC = 6
SNMPAPI_NO_SUPPORT = 0
SNMPAPI_V1_SUPPORT = 1
SNMPAPI_V2_SUPPORT = 2
SNMPAPI_M2M_SUPPORT = 3
SNMPAPI_FAILURE = 0
SNMPAPI_SUCCESS = 1
SNMPAPI_ALLOC_ERROR = 2
SNMPAPI_CONTEXT_INVALID = 3
SNMPAPI_CONTEXT_UNKNOWN = 4
SNMPAPI_ENTITY_INVALID = 5
SNMPAPI_ENTITY_UNKNOWN = 6
SNMPAPI_INDEX_INVALID = 7
SNMPAPI_NOOP = 8
SNMPAPI_OID_INVALID = 9
SNMPAPI_OPERATION_INVALID = 10
SNMPAPI_OUTPUT_TRUNCATED = 11
SNMPAPI_PDU_INVALID = 12
SNMPAPI_SESSION_INVALID = 13
SNMPAPI_SYNTAX_INVALID = 14
SNMPAPI_VBL_INVALID = 15
SNMPAPI_MODE_INVALID = 16
SNMPAPI_SIZE_INVALID = 17
SNMPAPI_NOT_INITIALIZED = 18
SNMPAPI_MESSAGE_INVALID = 19
SNMPAPI_HWND_INVALID = 20
SNMPAPI_OTHER_ERROR = 99
SNMPAPI_TL_NOT_INITIALIZED = 100
SNMPAPI_TL_NOT_SUPPORTED = 101
SNMPAPI_TL_NOT_AVAILABLE = 102
SNMPAPI_TL_RESOURCE_ERROR = 103
SNMPAPI_TL_UNDELIVERABLE = 104
SNMPAPI_TL_SRC_INVALID = 105
SNMPAPI_TL_INVALID_PARAM = 106
SNMPAPI_TL_IN_USE = 107
SNMPAPI_TL_TIMEOUT = 108
SNMPAPI_TL_PDU_TOO_BIG = 109
SNMPAPI_TL_OTHER = 199
MAXVENDORINFO = 32
SNMP_PDU_TYPE = UInt32
SNMP_PDU_GET = 160
SNMP_PDU_GETNEXT = 161
SNMP_PDU_RESPONSE = 162
SNMP_PDU_SET = 163
SNMP_PDU_GETBULK = 165
SNMP_PDU_TRAP = 167
SNMP_EXTENSION_REQUEST_TYPE = UInt32
SNMP_EXTENSION_GET = 160
SNMP_EXTENSION_GET_NEXT = 161
SNMP_EXTENSION_SET_TEST = 224
SNMP_EXTENSION_SET_COMMIT = 163
SNMP_EXTENSION_SET_UNDO = 225
SNMP_EXTENSION_SET_CLEANUP = 226
SNMP_API_TRANSLATE_MODE = UInt32
SNMPAPI_TRANSLATED = 0
SNMPAPI_UNTRANSLATED_V1 = 1
SNMPAPI_UNTRANSLATED_V2 = 2
SNMP_GENERICTRAP = UInt32
SNMP_GENERICTRAP_COLDSTART = 0
SNMP_GENERICTRAP_WARMSTART = 1
SNMP_GENERICTRAP_LINKDOWN = 2
SNMP_GENERICTRAP_LINKUP = 3
SNMP_GENERICTRAP_AUTHFAILURE = 4
SNMP_GENERICTRAP_EGPNEIGHLOSS = 5
SNMP_GENERICTRAP_ENTERSPECIFIC = 6
SNMP_ERROR_STATUS = UInt32
SNMP_ERRORSTATUS_NOERROR = 0
SNMP_ERRORSTATUS_TOOBIG = 1
SNMP_ERRORSTATUS_NOSUCHNAME = 2
SNMP_ERRORSTATUS_BADVALUE = 3
SNMP_ERRORSTATUS_READONLY = 4
SNMP_ERRORSTATUS_GENERR = 5
SNMP_ERRORSTATUS_NOACCESS = 6
SNMP_ERRORSTATUS_WRONGTYPE = 7
SNMP_ERRORSTATUS_WRONGLENGTH = 8
SNMP_ERRORSTATUS_WRONGENCODING = 9
SNMP_ERRORSTATUS_WRONGVALUE = 10
SNMP_ERRORSTATUS_NOCREATION = 11
SNMP_ERRORSTATUS_INCONSISTENTVALUE = 12
SNMP_ERRORSTATUS_RESOURCEUNAVAILABLE = 13
SNMP_ERRORSTATUS_COMMITFAILED = 14
SNMP_ERRORSTATUS_UNDOFAILED = 15
SNMP_ERRORSTATUS_AUTHORIZATIONERROR = 16
SNMP_ERRORSTATUS_NOTWRITABLE = 17
SNMP_ERRORSTATUS_INCONSISTENTNAME = 18
SNMP_STATUS = UInt32
SNMPAPI_ON = 1
SNMPAPI_OFF = 0
SNMP_OUTPUT_LOG_TYPE = UInt32
SNMP_OUTPUT_TO_CONSOLE = 1
SNMP_OUTPUT_TO_LOGFILE = 2
SNMP_OUTPUT_TO_DEBUGGER = 8
SNMP_LOG = UInt32
SNMP_LOG_SILENT = 0
SNMP_LOG_FATAL = 1
SNMP_LOG_ERROR = 2
SNMP_LOG_WARNING = 3
SNMP_LOG_TRACE = 4
SNMP_LOG_VERBOSE = 5
SNMP_ERROR = UInt32
SNMP_ERROR_NOERROR = 0
SNMP_ERROR_TOOBIG = 1
SNMP_ERROR_NOSUCHNAME = 2
SNMP_ERROR_BADVALUE = 3
SNMP_ERROR_READONLY = 4
SNMP_ERROR_GENERR = 5
SNMP_ERROR_NOACCESS = 6
SNMP_ERROR_WRONGTYPE = 7
SNMP_ERROR_WRONGLENGTH = 8
SNMP_ERROR_WRONGENCODING = 9
SNMP_ERROR_WRONGVALUE = 10
SNMP_ERROR_NOCREATION = 11
SNMP_ERROR_INCONSISTENTVALUE = 12
SNMP_ERROR_RESOURCEUNAVAILABLE = 13
SNMP_ERROR_COMMITFAILED = 14
SNMP_ERROR_UNDOFAILED = 15
SNMP_ERROR_AUTHORIZATIONERROR = 16
SNMP_ERROR_NOTWRITABLE = 17
SNMP_ERROR_INCONSISTENTNAME = 18
def _define_AsnOctetString_head():
    class AsnOctetString(Structure):
        pass
    return AsnOctetString
def _define_AsnOctetString():
    AsnOctetString = win32more.NetworkManagement.Snmp.AsnOctetString_head
    AsnOctetString._pack_ = 4
    AsnOctetString._fields_ = [
        ("stream", c_char_p_no),
        ("length", UInt32),
        ("dynamic", win32more.Foundation.BOOL),
    ]
    return AsnOctetString
def _define_AsnObjectIdentifier_head():
    class AsnObjectIdentifier(Structure):
        pass
    return AsnObjectIdentifier
def _define_AsnObjectIdentifier():
    AsnObjectIdentifier = win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head
    AsnObjectIdentifier._pack_ = 4
    AsnObjectIdentifier._fields_ = [
        ("idLength", UInt32),
        ("ids", POINTER(UInt32)),
    ]
    return AsnObjectIdentifier
def _define_AsnAny_head():
    class AsnAny(Structure):
        pass
    return AsnAny
def _define_AsnAny():
    AsnAny = win32more.NetworkManagement.Snmp.AsnAny_head
    class AsnAny__asnValue_e__Union(Union):
        pass
    AsnAny__asnValue_e__Union._pack_ = 4
    AsnAny__asnValue_e__Union._fields_ = [
        ("number", Int32),
        ("unsigned32", UInt32),
        ("counter64", win32more.Foundation.ULARGE_INTEGER),
        ("string", win32more.NetworkManagement.Snmp.AsnOctetString),
        ("bits", win32more.NetworkManagement.Snmp.AsnOctetString),
        ("object", win32more.NetworkManagement.Snmp.AsnObjectIdentifier),
        ("sequence", win32more.NetworkManagement.Snmp.AsnOctetString),
        ("address", win32more.NetworkManagement.Snmp.AsnOctetString),
        ("counter", UInt32),
        ("gauge", UInt32),
        ("ticks", UInt32),
        ("arbitrary", win32more.NetworkManagement.Snmp.AsnOctetString),
    ]
    AsnAny._fields_ = [
        ("asnType", Byte),
        ("asnValue", AsnAny__asnValue_e__Union),
    ]
    return AsnAny
def _define_SnmpVarBind_head():
    class SnmpVarBind(Structure):
        pass
    return SnmpVarBind
def _define_SnmpVarBind():
    SnmpVarBind = win32more.NetworkManagement.Snmp.SnmpVarBind_head
    SnmpVarBind._fields_ = [
        ("name", win32more.NetworkManagement.Snmp.AsnObjectIdentifier),
        ("value", win32more.NetworkManagement.Snmp.AsnAny),
    ]
    return SnmpVarBind
def _define_SnmpVarBindList_head():
    class SnmpVarBindList(Structure):
        pass
    return SnmpVarBindList
def _define_SnmpVarBindList():
    SnmpVarBindList = win32more.NetworkManagement.Snmp.SnmpVarBindList_head
    SnmpVarBindList._pack_ = 4
    SnmpVarBindList._fields_ = [
        ("list", POINTER(win32more.NetworkManagement.Snmp.SnmpVarBind_head)),
        ("len", UInt32),
    ]
    return SnmpVarBindList
def _define_PFNSNMPEXTENSIONINIT():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(win32more.Foundation.HANDLE),POINTER(win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head), use_last_error=False)
def _define_PFNSNMPEXTENSIONINITEX():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head), use_last_error=False)
def _define_PFNSNMPEXTENSIONMONITOR():
    return CFUNCTYPE(win32more.Foundation.BOOL,c_void_p, use_last_error=False)
def _define_PFNSNMPEXTENSIONQUERY():
    return CFUNCTYPE(win32more.Foundation.BOOL,Byte,POINTER(win32more.NetworkManagement.Snmp.SnmpVarBindList_head),POINTER(Int32),POINTER(Int32), use_last_error=False)
def _define_PFNSNMPEXTENSIONQUERYEX():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,POINTER(win32more.NetworkManagement.Snmp.SnmpVarBindList_head),POINTER(win32more.NetworkManagement.Snmp.AsnOctetString_head),POINTER(Int32),POINTER(Int32), use_last_error=False)
def _define_PFNSNMPEXTENSIONTRAP():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head),POINTER(Int32),POINTER(Int32),POINTER(UInt32),POINTER(win32more.NetworkManagement.Snmp.SnmpVarBindList_head), use_last_error=False)
def _define_PFNSNMPEXTENSIONCLOSE():
    return CFUNCTYPE(Void, use_last_error=False)
def _define_smiOCTETS_head():
    class smiOCTETS(Structure):
        pass
    return smiOCTETS
def _define_smiOCTETS():
    smiOCTETS = win32more.NetworkManagement.Snmp.smiOCTETS_head
    smiOCTETS._fields_ = [
        ("len", UInt32),
        ("ptr", c_char_p_no),
    ]
    return smiOCTETS
def _define_smiOID_head():
    class smiOID(Structure):
        pass
    return smiOID
def _define_smiOID():
    smiOID = win32more.NetworkManagement.Snmp.smiOID_head
    smiOID._fields_ = [
        ("len", UInt32),
        ("ptr", POINTER(UInt32)),
    ]
    return smiOID
def _define_smiCNTR64_head():
    class smiCNTR64(Structure):
        pass
    return smiCNTR64
def _define_smiCNTR64():
    smiCNTR64 = win32more.NetworkManagement.Snmp.smiCNTR64_head
    smiCNTR64._fields_ = [
        ("hipart", UInt32),
        ("lopart", UInt32),
    ]
    return smiCNTR64
def _define_smiVALUE_head():
    class smiVALUE(Structure):
        pass
    return smiVALUE
def _define_smiVALUE():
    smiVALUE = win32more.NetworkManagement.Snmp.smiVALUE_head
    class smiVALUE__value_e__Union(Union):
        pass
    smiVALUE__value_e__Union._fields_ = [
        ("sNumber", Int32),
        ("uNumber", UInt32),
        ("hNumber", win32more.NetworkManagement.Snmp.smiCNTR64),
        ("string", win32more.NetworkManagement.Snmp.smiOCTETS),
        ("oid", win32more.NetworkManagement.Snmp.smiOID),
        ("empty", Byte),
    ]
    smiVALUE._fields_ = [
        ("syntax", UInt32),
        ("value", smiVALUE__value_e__Union),
    ]
    return smiVALUE
def _define_smiVENDORINFO_head():
    class smiVENDORINFO(Structure):
        pass
    return smiVENDORINFO
def _define_smiVENDORINFO():
    smiVENDORINFO = win32more.NetworkManagement.Snmp.smiVENDORINFO_head
    smiVENDORINFO._fields_ = [
        ("vendorName", win32more.Foundation.CHAR * 64),
        ("vendorContact", win32more.Foundation.CHAR * 64),
        ("vendorVersionId", win32more.Foundation.CHAR * 32),
        ("vendorVersionDate", win32more.Foundation.CHAR * 32),
        ("vendorEnterprise", UInt32),
    ]
    return smiVENDORINFO
def _define_SNMPAPI_CALLBACK():
    return CFUNCTYPE(UInt32,IntPtr,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,c_void_p, use_last_error=False)
def _define_PFNSNMPSTARTUPEX():
    return CFUNCTYPE(UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)
def _define_PFNSNMPCLEANUPEX():
    return CFUNCTYPE(UInt32, use_last_error=False)
def _define_SnmpUtilOidCpy():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head),POINTER(win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head), use_last_error=False)(("SnmpUtilOidCpy", windll["snmpapi"]), ((1, 'pOidDst'),(1, 'pOidSrc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilOidAppend():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head),POINTER(win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head), use_last_error=True)(("SnmpUtilOidAppend", windll["snmpapi"]), ((1, 'pOidDst'),(1, 'pOidSrc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilOidNCmp():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head),POINTER(win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head),UInt32, use_last_error=False)(("SnmpUtilOidNCmp", windll["snmpapi"]), ((1, 'pOid1'),(1, 'pOid2'),(1, 'nSubIds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilOidCmp():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head),POINTER(win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head), use_last_error=False)(("SnmpUtilOidCmp", windll["snmpapi"]), ((1, 'pOid1'),(1, 'pOid2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilOidFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head), use_last_error=False)(("SnmpUtilOidFree", windll["snmpapi"]), ((1, 'pOid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilOctetsCmp():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Snmp.AsnOctetString_head),POINTER(win32more.NetworkManagement.Snmp.AsnOctetString_head), use_last_error=False)(("SnmpUtilOctetsCmp", windll["snmpapi"]), ((1, 'pOctets1'),(1, 'pOctets2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilOctetsNCmp():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Snmp.AsnOctetString_head),POINTER(win32more.NetworkManagement.Snmp.AsnOctetString_head),UInt32, use_last_error=False)(("SnmpUtilOctetsNCmp", windll["snmpapi"]), ((1, 'pOctets1'),(1, 'pOctets2'),(1, 'nChars'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilOctetsCpy():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Snmp.AsnOctetString_head),POINTER(win32more.NetworkManagement.Snmp.AsnOctetString_head), use_last_error=False)(("SnmpUtilOctetsCpy", windll["snmpapi"]), ((1, 'pOctetsDst'),(1, 'pOctetsSrc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilOctetsFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Snmp.AsnOctetString_head), use_last_error=False)(("SnmpUtilOctetsFree", windll["snmpapi"]), ((1, 'pOctets'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilAsnAnyCpy():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Snmp.AsnAny_head),POINTER(win32more.NetworkManagement.Snmp.AsnAny_head), use_last_error=False)(("SnmpUtilAsnAnyCpy", windll["snmpapi"]), ((1, 'pAnyDst'),(1, 'pAnySrc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilAsnAnyFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Snmp.AsnAny_head), use_last_error=False)(("SnmpUtilAsnAnyFree", windll["snmpapi"]), ((1, 'pAny'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilVarBindCpy():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Snmp.SnmpVarBind_head),POINTER(win32more.NetworkManagement.Snmp.SnmpVarBind_head), use_last_error=False)(("SnmpUtilVarBindCpy", windll["snmpapi"]), ((1, 'pVbDst'),(1, 'pVbSrc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilVarBindFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Snmp.SnmpVarBind_head), use_last_error=False)(("SnmpUtilVarBindFree", windll["snmpapi"]), ((1, 'pVb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilVarBindListCpy():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.NetworkManagement.Snmp.SnmpVarBindList_head),POINTER(win32more.NetworkManagement.Snmp.SnmpVarBindList_head), use_last_error=False)(("SnmpUtilVarBindListCpy", windll["snmpapi"]), ((1, 'pVblDst'),(1, 'pVblSrc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilVarBindListFree():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Snmp.SnmpVarBindList_head), use_last_error=False)(("SnmpUtilVarBindListFree", windll["snmpapi"]), ((1, 'pVbl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilMemFree():
    try:
        return WINFUNCTYPE(Void,c_void_p, use_last_error=False)(("SnmpUtilMemFree", windll["snmpapi"]), ((1, 'pMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilMemAlloc():
    try:
        return WINFUNCTYPE(c_void_p,UInt32, use_last_error=False)(("SnmpUtilMemAlloc", windll["snmpapi"]), ((1, 'nBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilMemReAlloc():
    try:
        return WINFUNCTYPE(c_void_p,c_void_p,UInt32, use_last_error=False)(("SnmpUtilMemReAlloc", windll["snmpapi"]), ((1, 'pMem'),(1, 'nBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilOidToA():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head), use_last_error=False)(("SnmpUtilOidToA", windll["snmpapi"]), ((1, 'Oid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilIdsToA():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,POINTER(UInt32),UInt32, use_last_error=False)(("SnmpUtilIdsToA", windll["snmpapi"]), ((1, 'Ids'),(1, 'IdLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilPrintOid():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head), use_last_error=False)(("SnmpUtilPrintOid", windll["snmpapi"]), ((1, 'Oid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilPrintAsnAny():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.NetworkManagement.Snmp.AsnAny_head), use_last_error=False)(("SnmpUtilPrintAsnAny", windll["snmpapi"]), ((1, 'pAny'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpSvcGetUptime():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("SnmpSvcGetUptime", windll["snmpapi"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpSvcSetLogLevel():
    try:
        return WINFUNCTYPE(Void,win32more.NetworkManagement.Snmp.SNMP_LOG, use_last_error=False)(("SnmpSvcSetLogLevel", windll["snmpapi"]), ((1, 'nLogLevel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpSvcSetLogType():
    try:
        return WINFUNCTYPE(Void,win32more.NetworkManagement.Snmp.SNMP_OUTPUT_LOG_TYPE, use_last_error=False)(("SnmpSvcSetLogType", windll["snmpapi"]), ((1, 'nLogType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpUtilDbgPrint():
    try:
        return WINFUNCTYPE(Void,win32more.NetworkManagement.Snmp.SNMP_LOG,win32more.Foundation.PSTR, use_last_error=False)(("SnmpUtilDbgPrint", windll["snmpapi"]), ((1, 'nLogLevel'),(1, 'szFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpMgrOpen():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32,Int32, use_last_error=True)(("SnmpMgrOpen", windll["mgmtapi"]), ((1, 'lpAgentAddress'),(1, 'lpAgentCommunity'),(1, 'nTimeOut'),(1, 'nRetries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpMgrCtl():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UInt32,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32), use_last_error=True)(("SnmpMgrCtl", windll["mgmtapi"]), ((1, 'session'),(1, 'dwCtlCode'),(1, 'lpvInBuffer'),(1, 'cbInBuffer'),(1, 'lpvOUTBuffer'),(1, 'cbOUTBuffer'),(1, 'lpcbBytesReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpMgrClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p, use_last_error=False)(("SnmpMgrClose", windll["mgmtapi"]), ((1, 'session'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpMgrRequest():
    try:
        return WINFUNCTYPE(Int32,c_void_p,Byte,POINTER(win32more.NetworkManagement.Snmp.SnmpVarBindList_head),POINTER(win32more.NetworkManagement.Snmp.SNMP_ERROR_STATUS),POINTER(Int32), use_last_error=True)(("SnmpMgrRequest", windll["mgmtapi"]), ((1, 'session'),(1, 'requestType'),(1, 'variableBindings'),(1, 'errorStatus'),(1, 'errorIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpMgrStrToOid():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head), use_last_error=False)(("SnmpMgrStrToOid", windll["mgmtapi"]), ((1, 'string'),(1, 'oid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpMgrOidToStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head),POINTER(win32more.Foundation.PSTR), use_last_error=False)(("SnmpMgrOidToStr", windll["mgmtapi"]), ((1, 'oid'),(1, 'string'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpMgrTrapListen():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.HANDLE), use_last_error=True)(("SnmpMgrTrapListen", windll["mgmtapi"]), ((1, 'phTrapAvailable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpMgrGetTrap():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head),POINTER(win32more.NetworkManagement.Snmp.AsnOctetString_head),POINTER(win32more.NetworkManagement.Snmp.SNMP_GENERICTRAP),POINTER(Int32),POINTER(UInt32),POINTER(win32more.NetworkManagement.Snmp.SnmpVarBindList_head), use_last_error=False)(("SnmpMgrGetTrap", windll["mgmtapi"]), ((1, 'enterprise'),(1, 'IPAddress'),(1, 'genericTrap'),(1, 'specificTrap'),(1, 'timeStamp'),(1, 'variableBindings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpMgrGetTrapEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.NetworkManagement.Snmp.AsnObjectIdentifier_head),POINTER(win32more.NetworkManagement.Snmp.AsnOctetString_head),POINTER(win32more.NetworkManagement.Snmp.AsnOctetString_head),POINTER(win32more.NetworkManagement.Snmp.SNMP_GENERICTRAP),POINTER(Int32),POINTER(win32more.NetworkManagement.Snmp.AsnOctetString_head),POINTER(UInt32),POINTER(win32more.NetworkManagement.Snmp.SnmpVarBindList_head), use_last_error=False)(("SnmpMgrGetTrapEx", windll["mgmtapi"]), ((1, 'enterprise'),(1, 'agentAddress'),(1, 'sourceAddress'),(1, 'genericTrap'),(1, 'specificTrap'),(1, 'community'),(1, 'timeStamp'),(1, 'variableBindings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpGetTranslateMode():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Snmp.SNMP_API_TRANSLATE_MODE), use_last_error=False)(("SnmpGetTranslateMode", windll["wsnmp32"]), ((1, 'nTranslateMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpSetTranslateMode():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Snmp.SNMP_API_TRANSLATE_MODE, use_last_error=False)(("SnmpSetTranslateMode", windll["wsnmp32"]), ((1, 'nTranslateMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpGetRetransmitMode():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Snmp.SNMP_STATUS), use_last_error=False)(("SnmpGetRetransmitMode", windll["wsnmp32"]), ((1, 'nRetransmitMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpSetRetransmitMode():
    try:
        return WINFUNCTYPE(UInt32,win32more.NetworkManagement.Snmp.SNMP_STATUS, use_last_error=False)(("SnmpSetRetransmitMode", windll["wsnmp32"]), ((1, 'nRetransmitMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpGetTimeout():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("SnmpGetTimeout", windll["wsnmp32"]), ((1, 'hEntity'),(1, 'nPolicyTimeout'),(1, 'nActualTimeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpSetTimeout():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32, use_last_error=False)(("SnmpSetTimeout", windll["wsnmp32"]), ((1, 'hEntity'),(1, 'nPolicyTimeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpGetRetry():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("SnmpGetRetry", windll["wsnmp32"]), ((1, 'hEntity'),(1, 'nPolicyRetry'),(1, 'nActualRetry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpSetRetry():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32, use_last_error=False)(("SnmpSetRetry", windll["wsnmp32"]), ((1, 'hEntity'),(1, 'nPolicyRetry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpGetVendorInfo():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Snmp.smiVENDORINFO_head), use_last_error=False)(("SnmpGetVendorInfo", windll["wsnmp32"]), ((1, 'vendorInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpStartup():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(win32more.NetworkManagement.Snmp.SNMP_API_TRANSLATE_MODE),POINTER(win32more.NetworkManagement.Snmp.SNMP_STATUS), use_last_error=False)(("SnmpStartup", windll["wsnmp32"]), ((1, 'nMajorVersion'),(1, 'nMinorVersion'),(1, 'nLevel'),(1, 'nTranslateMode'),(1, 'nRetransmitMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpCleanup():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("SnmpCleanup", windll["wsnmp32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpOpen():
    try:
        return WINFUNCTYPE(IntPtr,win32more.Foundation.HWND,UInt32, use_last_error=False)(("SnmpOpen", windll["wsnmp32"]), ((1, 'hWnd'),(1, 'wMsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpClose():
    try:
        return WINFUNCTYPE(UInt32,IntPtr, use_last_error=False)(("SnmpClose", windll["wsnmp32"]), ((1, 'session'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpSendMsg():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,IntPtr,IntPtr,IntPtr, use_last_error=False)(("SnmpSendMsg", windll["wsnmp32"]), ((1, 'session'),(1, 'srcEntity'),(1, 'dstEntity'),(1, 'context'),(1, 'PDU'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpRecvMsg():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(IntPtr),POINTER(IntPtr),POINTER(IntPtr),POINTER(IntPtr), use_last_error=False)(("SnmpRecvMsg", windll["wsnmp32"]), ((1, 'session'),(1, 'srcEntity'),(1, 'dstEntity'),(1, 'context'),(1, 'PDU'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpRegister():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,IntPtr,IntPtr,POINTER(win32more.NetworkManagement.Snmp.smiOID_head),win32more.NetworkManagement.Snmp.SNMP_STATUS, use_last_error=False)(("SnmpRegister", windll["wsnmp32"]), ((1, 'session'),(1, 'srcEntity'),(1, 'dstEntity'),(1, 'context'),(1, 'notification'),(1, 'state'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpCreateSession():
    try:
        return WINFUNCTYPE(IntPtr,win32more.Foundation.HWND,UInt32,win32more.NetworkManagement.Snmp.SNMPAPI_CALLBACK,c_void_p, use_last_error=False)(("SnmpCreateSession", windll["wsnmp32"]), ((1, 'hWnd'),(1, 'wMsg'),(1, 'fCallBack'),(1, 'lpClientData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpListen():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,win32more.NetworkManagement.Snmp.SNMP_STATUS, use_last_error=False)(("SnmpListen", windll["wsnmp32"]), ((1, 'hEntity'),(1, 'lStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpListenEx():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,UInt32, use_last_error=False)(("SnmpListenEx", windll["wsnmp32"]), ((1, 'hEntity'),(1, 'lStatus'),(1, 'nUseEntityAddr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpCancelMsg():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,Int32, use_last_error=False)(("SnmpCancelMsg", windll["wsnmp32"]), ((1, 'session'),(1, 'reqId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpStartupEx():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(win32more.NetworkManagement.Snmp.SNMP_API_TRANSLATE_MODE),POINTER(win32more.NetworkManagement.Snmp.SNMP_STATUS), use_last_error=False)(("SnmpStartupEx", windll["wsnmp32"]), ((1, 'nMajorVersion'),(1, 'nMinorVersion'),(1, 'nLevel'),(1, 'nTranslateMode'),(1, 'nRetransmitMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpCleanupEx():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("SnmpCleanupEx", windll["wsnmp32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpStrToEntity():
    try:
        return WINFUNCTYPE(IntPtr,IntPtr,win32more.Foundation.PSTR, use_last_error=False)(("SnmpStrToEntity", windll["wsnmp32"]), ((1, 'session'),(1, 'string'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpEntityToStr():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,POINTER(Byte), use_last_error=False)(("SnmpEntityToStr", windll["wsnmp32"]), ((1, 'entity'),(1, 'size'),(1, 'string'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpFreeEntity():
    try:
        return WINFUNCTYPE(UInt32,IntPtr, use_last_error=False)(("SnmpFreeEntity", windll["wsnmp32"]), ((1, 'entity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpStrToContext():
    try:
        return WINFUNCTYPE(IntPtr,IntPtr,POINTER(win32more.NetworkManagement.Snmp.smiOCTETS_head), use_last_error=False)(("SnmpStrToContext", windll["wsnmp32"]), ((1, 'session'),(1, 'string'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpContextToStr():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(win32more.NetworkManagement.Snmp.smiOCTETS_head), use_last_error=False)(("SnmpContextToStr", windll["wsnmp32"]), ((1, 'context'),(1, 'string'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpFreeContext():
    try:
        return WINFUNCTYPE(UInt32,IntPtr, use_last_error=False)(("SnmpFreeContext", windll["wsnmp32"]), ((1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpSetPort():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32, use_last_error=False)(("SnmpSetPort", windll["wsnmp32"]), ((1, 'hEntity'),(1, 'nPort'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpCreatePdu():
    try:
        return WINFUNCTYPE(IntPtr,IntPtr,win32more.NetworkManagement.Snmp.SNMP_PDU_TYPE,Int32,Int32,Int32,IntPtr, use_last_error=False)(("SnmpCreatePdu", windll["wsnmp32"]), ((1, 'session'),(1, 'PDU_type'),(1, 'request_id'),(1, 'error_status'),(1, 'error_index'),(1, 'varbindlist'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpGetPduData():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(win32more.NetworkManagement.Snmp.SNMP_PDU_TYPE),POINTER(Int32),POINTER(win32more.NetworkManagement.Snmp.SNMP_ERROR),POINTER(Int32),POINTER(IntPtr), use_last_error=False)(("SnmpGetPduData", windll["wsnmp32"]), ((1, 'PDU'),(1, 'PDU_type'),(1, 'request_id'),(1, 'error_status'),(1, 'error_index'),(1, 'varbindlist'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpSetPduData():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(IntPtr), use_last_error=False)(("SnmpSetPduData", windll["wsnmp32"]), ((1, 'PDU'),(1, 'PDU_type'),(1, 'request_id'),(1, 'non_repeaters'),(1, 'max_repetitions'),(1, 'varbindlist'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpDuplicatePdu():
    try:
        return WINFUNCTYPE(IntPtr,IntPtr,IntPtr, use_last_error=False)(("SnmpDuplicatePdu", windll["wsnmp32"]), ((1, 'session'),(1, 'PDU'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpFreePdu():
    try:
        return WINFUNCTYPE(UInt32,IntPtr, use_last_error=False)(("SnmpFreePdu", windll["wsnmp32"]), ((1, 'PDU'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpCreateVbl():
    try:
        return WINFUNCTYPE(IntPtr,IntPtr,POINTER(win32more.NetworkManagement.Snmp.smiOID_head),POINTER(win32more.NetworkManagement.Snmp.smiVALUE_head), use_last_error=False)(("SnmpCreateVbl", windll["wsnmp32"]), ((1, 'session'),(1, 'name'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpDuplicateVbl():
    try:
        return WINFUNCTYPE(IntPtr,IntPtr,IntPtr, use_last_error=False)(("SnmpDuplicateVbl", windll["wsnmp32"]), ((1, 'session'),(1, 'vbl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpFreeVbl():
    try:
        return WINFUNCTYPE(UInt32,IntPtr, use_last_error=False)(("SnmpFreeVbl", windll["wsnmp32"]), ((1, 'vbl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpCountVbl():
    try:
        return WINFUNCTYPE(UInt32,IntPtr, use_last_error=False)(("SnmpCountVbl", windll["wsnmp32"]), ((1, 'vbl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpGetVb():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,POINTER(win32more.NetworkManagement.Snmp.smiOID_head),POINTER(win32more.NetworkManagement.Snmp.smiVALUE_head), use_last_error=False)(("SnmpGetVb", windll["wsnmp32"]), ((1, 'vbl'),(1, 'index'),(1, 'name'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpSetVb():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32,POINTER(win32more.NetworkManagement.Snmp.smiOID_head),POINTER(win32more.NetworkManagement.Snmp.smiVALUE_head), use_last_error=False)(("SnmpSetVb", windll["wsnmp32"]), ((1, 'vbl'),(1, 'index'),(1, 'name'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpDeleteVb():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32, use_last_error=False)(("SnmpDeleteVb", windll["wsnmp32"]), ((1, 'vbl'),(1, 'index'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpGetLastError():
    try:
        return WINFUNCTYPE(UInt32,IntPtr, use_last_error=False)(("SnmpGetLastError", windll["wsnmp32"]), ((1, 'session'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpStrToOid():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(win32more.NetworkManagement.Snmp.smiOID_head), use_last_error=False)(("SnmpStrToOid", windll["wsnmp32"]), ((1, 'string'),(1, 'dstOID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpOidToStr():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Snmp.smiOID_head),UInt32,POINTER(Byte), use_last_error=False)(("SnmpOidToStr", windll["wsnmp32"]), ((1, 'srcOID'),(1, 'size'),(1, 'string'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpOidCopy():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Snmp.smiOID_head),POINTER(win32more.NetworkManagement.Snmp.smiOID_head), use_last_error=False)(("SnmpOidCopy", windll["wsnmp32"]), ((1, 'srcOID'),(1, 'dstOID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpOidCompare():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.NetworkManagement.Snmp.smiOID_head),POINTER(win32more.NetworkManagement.Snmp.smiOID_head),UInt32,POINTER(Int32), use_last_error=False)(("SnmpOidCompare", windll["wsnmp32"]), ((1, 'xOID'),(1, 'yOID'),(1, 'maxlen'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpEncodeMsg():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,IntPtr,IntPtr,IntPtr,IntPtr,POINTER(win32more.NetworkManagement.Snmp.smiOCTETS_head), use_last_error=False)(("SnmpEncodeMsg", windll["wsnmp32"]), ((1, 'session'),(1, 'srcEntity'),(1, 'dstEntity'),(1, 'context'),(1, 'pdu'),(1, 'msgBufDesc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpDecodeMsg():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,POINTER(IntPtr),POINTER(IntPtr),POINTER(IntPtr),POINTER(IntPtr),POINTER(win32more.NetworkManagement.Snmp.smiOCTETS_head), use_last_error=False)(("SnmpDecodeMsg", windll["wsnmp32"]), ((1, 'session'),(1, 'srcEntity'),(1, 'dstEntity'),(1, 'context'),(1, 'pdu'),(1, 'msgBufDesc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SnmpFreeDescriptor():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.NetworkManagement.Snmp.smiOCTETS_head), use_last_error=False)(("SnmpFreeDescriptor", windll["wsnmp32"]), ((1, 'syntax'),(1, 'descriptor'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "ASN_UNIVERSAL",
    "ASN_APPLICATION",
    "ASN_CONTEXT",
    "ASN_PRIVATE",
    "ASN_PRIMITIVE",
    "ASN_CONSTRUCTOR",
    "SNMP_ACCESS_NONE",
    "SNMP_ACCESS_NOTIFY",
    "SNMP_ACCESS_READ_ONLY",
    "SNMP_ACCESS_READ_WRITE",
    "SNMP_ACCESS_READ_CREATE",
    "SNMPAPI_NOERROR",
    "SNMPAPI_ERROR",
    "SNMP_OUTPUT_TO_EVENTLOG",
    "DEFAULT_SNMP_PORT_UDP",
    "DEFAULT_SNMP_PORT_IPX",
    "DEFAULT_SNMPTRAP_PORT_UDP",
    "DEFAULT_SNMPTRAP_PORT_IPX",
    "SNMP_MAX_OID_LEN",
    "SNMP_MEM_ALLOC_ERROR",
    "SNMP_BERAPI_INVALID_LENGTH",
    "SNMP_BERAPI_INVALID_TAG",
    "SNMP_BERAPI_OVERFLOW",
    "SNMP_BERAPI_SHORT_BUFFER",
    "SNMP_BERAPI_INVALID_OBJELEM",
    "SNMP_PDUAPI_UNRECOGNIZED_PDU",
    "SNMP_PDUAPI_INVALID_ES",
    "SNMP_PDUAPI_INVALID_GT",
    "SNMP_AUTHAPI_INVALID_VERSION",
    "SNMP_AUTHAPI_INVALID_MSG_TYPE",
    "SNMP_AUTHAPI_TRIV_AUTH_FAILED",
    "ASN_CONTEXTSPECIFIC",
    "ASN_PRIMATIVE",
    "SNMP_MGMTAPI_TIMEOUT",
    "SNMP_MGMTAPI_SELECT_FDERRORS",
    "SNMP_MGMTAPI_TRAP_ERRORS",
    "SNMP_MGMTAPI_TRAP_DUPINIT",
    "SNMP_MGMTAPI_NOTRAPS",
    "SNMP_MGMTAPI_AGAIN",
    "SNMP_MGMTAPI_INVALID_CTL",
    "SNMP_MGMTAPI_INVALID_SESSION",
    "SNMP_MGMTAPI_INVALID_BUFFER",
    "MGMCTL_SETAGENTPORT",
    "MAXOBJIDSIZE",
    "MAXOBJIDSTRSIZE",
    "SNMPLISTEN_USEENTITY_ADDR",
    "SNMPLISTEN_ALL_ADDR",
    "SNMP_TRAP_COLDSTART",
    "SNMP_TRAP_WARMSTART",
    "SNMP_TRAP_LINKDOWN",
    "SNMP_TRAP_LINKUP",
    "SNMP_TRAP_AUTHFAIL",
    "SNMP_TRAP_EGPNEIGHBORLOSS",
    "SNMP_TRAP_ENTERPRISESPECIFIC",
    "SNMPAPI_NO_SUPPORT",
    "SNMPAPI_V1_SUPPORT",
    "SNMPAPI_V2_SUPPORT",
    "SNMPAPI_M2M_SUPPORT",
    "SNMPAPI_FAILURE",
    "SNMPAPI_SUCCESS",
    "SNMPAPI_ALLOC_ERROR",
    "SNMPAPI_CONTEXT_INVALID",
    "SNMPAPI_CONTEXT_UNKNOWN",
    "SNMPAPI_ENTITY_INVALID",
    "SNMPAPI_ENTITY_UNKNOWN",
    "SNMPAPI_INDEX_INVALID",
    "SNMPAPI_NOOP",
    "SNMPAPI_OID_INVALID",
    "SNMPAPI_OPERATION_INVALID",
    "SNMPAPI_OUTPUT_TRUNCATED",
    "SNMPAPI_PDU_INVALID",
    "SNMPAPI_SESSION_INVALID",
    "SNMPAPI_SYNTAX_INVALID",
    "SNMPAPI_VBL_INVALID",
    "SNMPAPI_MODE_INVALID",
    "SNMPAPI_SIZE_INVALID",
    "SNMPAPI_NOT_INITIALIZED",
    "SNMPAPI_MESSAGE_INVALID",
    "SNMPAPI_HWND_INVALID",
    "SNMPAPI_OTHER_ERROR",
    "SNMPAPI_TL_NOT_INITIALIZED",
    "SNMPAPI_TL_NOT_SUPPORTED",
    "SNMPAPI_TL_NOT_AVAILABLE",
    "SNMPAPI_TL_RESOURCE_ERROR",
    "SNMPAPI_TL_UNDELIVERABLE",
    "SNMPAPI_TL_SRC_INVALID",
    "SNMPAPI_TL_INVALID_PARAM",
    "SNMPAPI_TL_IN_USE",
    "SNMPAPI_TL_TIMEOUT",
    "SNMPAPI_TL_PDU_TOO_BIG",
    "SNMPAPI_TL_OTHER",
    "MAXVENDORINFO",
    "SNMP_PDU_TYPE",
    "SNMP_PDU_GET",
    "SNMP_PDU_GETNEXT",
    "SNMP_PDU_RESPONSE",
    "SNMP_PDU_SET",
    "SNMP_PDU_GETBULK",
    "SNMP_PDU_TRAP",
    "SNMP_EXTENSION_REQUEST_TYPE",
    "SNMP_EXTENSION_GET",
    "SNMP_EXTENSION_GET_NEXT",
    "SNMP_EXTENSION_SET_TEST",
    "SNMP_EXTENSION_SET_COMMIT",
    "SNMP_EXTENSION_SET_UNDO",
    "SNMP_EXTENSION_SET_CLEANUP",
    "SNMP_API_TRANSLATE_MODE",
    "SNMPAPI_TRANSLATED",
    "SNMPAPI_UNTRANSLATED_V1",
    "SNMPAPI_UNTRANSLATED_V2",
    "SNMP_GENERICTRAP",
    "SNMP_GENERICTRAP_COLDSTART",
    "SNMP_GENERICTRAP_WARMSTART",
    "SNMP_GENERICTRAP_LINKDOWN",
    "SNMP_GENERICTRAP_LINKUP",
    "SNMP_GENERICTRAP_AUTHFAILURE",
    "SNMP_GENERICTRAP_EGPNEIGHLOSS",
    "SNMP_GENERICTRAP_ENTERSPECIFIC",
    "SNMP_ERROR_STATUS",
    "SNMP_ERRORSTATUS_NOERROR",
    "SNMP_ERRORSTATUS_TOOBIG",
    "SNMP_ERRORSTATUS_NOSUCHNAME",
    "SNMP_ERRORSTATUS_BADVALUE",
    "SNMP_ERRORSTATUS_READONLY",
    "SNMP_ERRORSTATUS_GENERR",
    "SNMP_ERRORSTATUS_NOACCESS",
    "SNMP_ERRORSTATUS_WRONGTYPE",
    "SNMP_ERRORSTATUS_WRONGLENGTH",
    "SNMP_ERRORSTATUS_WRONGENCODING",
    "SNMP_ERRORSTATUS_WRONGVALUE",
    "SNMP_ERRORSTATUS_NOCREATION",
    "SNMP_ERRORSTATUS_INCONSISTENTVALUE",
    "SNMP_ERRORSTATUS_RESOURCEUNAVAILABLE",
    "SNMP_ERRORSTATUS_COMMITFAILED",
    "SNMP_ERRORSTATUS_UNDOFAILED",
    "SNMP_ERRORSTATUS_AUTHORIZATIONERROR",
    "SNMP_ERRORSTATUS_NOTWRITABLE",
    "SNMP_ERRORSTATUS_INCONSISTENTNAME",
    "SNMP_STATUS",
    "SNMPAPI_ON",
    "SNMPAPI_OFF",
    "SNMP_OUTPUT_LOG_TYPE",
    "SNMP_OUTPUT_TO_CONSOLE",
    "SNMP_OUTPUT_TO_LOGFILE",
    "SNMP_OUTPUT_TO_DEBUGGER",
    "SNMP_LOG",
    "SNMP_LOG_SILENT",
    "SNMP_LOG_FATAL",
    "SNMP_LOG_ERROR",
    "SNMP_LOG_WARNING",
    "SNMP_LOG_TRACE",
    "SNMP_LOG_VERBOSE",
    "SNMP_ERROR",
    "SNMP_ERROR_NOERROR",
    "SNMP_ERROR_TOOBIG",
    "SNMP_ERROR_NOSUCHNAME",
    "SNMP_ERROR_BADVALUE",
    "SNMP_ERROR_READONLY",
    "SNMP_ERROR_GENERR",
    "SNMP_ERROR_NOACCESS",
    "SNMP_ERROR_WRONGTYPE",
    "SNMP_ERROR_WRONGLENGTH",
    "SNMP_ERROR_WRONGENCODING",
    "SNMP_ERROR_WRONGVALUE",
    "SNMP_ERROR_NOCREATION",
    "SNMP_ERROR_INCONSISTENTVALUE",
    "SNMP_ERROR_RESOURCEUNAVAILABLE",
    "SNMP_ERROR_COMMITFAILED",
    "SNMP_ERROR_UNDOFAILED",
    "SNMP_ERROR_AUTHORIZATIONERROR",
    "SNMP_ERROR_NOTWRITABLE",
    "SNMP_ERROR_INCONSISTENTNAME",
    "AsnOctetString",
    "AsnObjectIdentifier",
    "AsnAny",
    "SnmpVarBind",
    "SnmpVarBindList",
    "PFNSNMPEXTENSIONINIT",
    "PFNSNMPEXTENSIONINITEX",
    "PFNSNMPEXTENSIONMONITOR",
    "PFNSNMPEXTENSIONQUERY",
    "PFNSNMPEXTENSIONQUERYEX",
    "PFNSNMPEXTENSIONTRAP",
    "PFNSNMPEXTENSIONCLOSE",
    "smiOCTETS",
    "smiOID",
    "smiCNTR64",
    "smiVALUE",
    "smiVENDORINFO",
    "SNMPAPI_CALLBACK",
    "PFNSNMPSTARTUPEX",
    "PFNSNMPCLEANUPEX",
    "SnmpUtilOidCpy",
    "SnmpUtilOidAppend",
    "SnmpUtilOidNCmp",
    "SnmpUtilOidCmp",
    "SnmpUtilOidFree",
    "SnmpUtilOctetsCmp",
    "SnmpUtilOctetsNCmp",
    "SnmpUtilOctetsCpy",
    "SnmpUtilOctetsFree",
    "SnmpUtilAsnAnyCpy",
    "SnmpUtilAsnAnyFree",
    "SnmpUtilVarBindCpy",
    "SnmpUtilVarBindFree",
    "SnmpUtilVarBindListCpy",
    "SnmpUtilVarBindListFree",
    "SnmpUtilMemFree",
    "SnmpUtilMemAlloc",
    "SnmpUtilMemReAlloc",
    "SnmpUtilOidToA",
    "SnmpUtilIdsToA",
    "SnmpUtilPrintOid",
    "SnmpUtilPrintAsnAny",
    "SnmpSvcGetUptime",
    "SnmpSvcSetLogLevel",
    "SnmpSvcSetLogType",
    "SnmpUtilDbgPrint",
    "SnmpMgrOpen",
    "SnmpMgrCtl",
    "SnmpMgrClose",
    "SnmpMgrRequest",
    "SnmpMgrStrToOid",
    "SnmpMgrOidToStr",
    "SnmpMgrTrapListen",
    "SnmpMgrGetTrap",
    "SnmpMgrGetTrapEx",
    "SnmpGetTranslateMode",
    "SnmpSetTranslateMode",
    "SnmpGetRetransmitMode",
    "SnmpSetRetransmitMode",
    "SnmpGetTimeout",
    "SnmpSetTimeout",
    "SnmpGetRetry",
    "SnmpSetRetry",
    "SnmpGetVendorInfo",
    "SnmpStartup",
    "SnmpCleanup",
    "SnmpOpen",
    "SnmpClose",
    "SnmpSendMsg",
    "SnmpRecvMsg",
    "SnmpRegister",
    "SnmpCreateSession",
    "SnmpListen",
    "SnmpListenEx",
    "SnmpCancelMsg",
    "SnmpStartupEx",
    "SnmpCleanupEx",
    "SnmpStrToEntity",
    "SnmpEntityToStr",
    "SnmpFreeEntity",
    "SnmpStrToContext",
    "SnmpContextToStr",
    "SnmpFreeContext",
    "SnmpSetPort",
    "SnmpCreatePdu",
    "SnmpGetPduData",
    "SnmpSetPduData",
    "SnmpDuplicatePdu",
    "SnmpFreePdu",
    "SnmpCreateVbl",
    "SnmpDuplicateVbl",
    "SnmpFreeVbl",
    "SnmpCountVbl",
    "SnmpGetVb",
    "SnmpSetVb",
    "SnmpDeleteVb",
    "SnmpGetLastError",
    "SnmpStrToOid",
    "SnmpOidToStr",
    "SnmpOidCopy",
    "SnmpOidCompare",
    "SnmpEncodeMsg",
    "SnmpDecodeMsg",
    "SnmpFreeDescriptor",
]
