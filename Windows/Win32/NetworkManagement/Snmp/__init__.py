from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.NetworkManagement.Snmp
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ASN_UNIVERSAL: UInt32 = 0
ASN_APPLICATION: UInt32 = 64
ASN_CONTEXT: UInt32 = 128
ASN_PRIVATE: UInt32 = 192
ASN_PRIMITIVE: UInt32 = 0
ASN_CONSTRUCTOR: UInt32 = 32
SNMP_ACCESS_NONE: UInt32 = 0
SNMP_ACCESS_NOTIFY: UInt32 = 1
SNMP_ACCESS_READ_ONLY: UInt32 = 2
SNMP_ACCESS_READ_WRITE: UInt32 = 3
SNMP_ACCESS_READ_CREATE: UInt32 = 4
SNMPAPI_NOERROR: UInt32 = 1
SNMPAPI_ERROR: UInt32 = 0
SNMP_OUTPUT_TO_EVENTLOG: UInt32 = 4
DEFAULT_SNMP_PORT_UDP: UInt32 = 161
DEFAULT_SNMP_PORT_IPX: UInt32 = 36879
DEFAULT_SNMPTRAP_PORT_UDP: UInt32 = 162
DEFAULT_SNMPTRAP_PORT_IPX: UInt32 = 36880
SNMP_MAX_OID_LEN: UInt32 = 128
SNMP_MEM_ALLOC_ERROR: UInt32 = 1
SNMP_BERAPI_INVALID_LENGTH: UInt32 = 10
SNMP_BERAPI_INVALID_TAG: UInt32 = 11
SNMP_BERAPI_OVERFLOW: UInt32 = 12
SNMP_BERAPI_SHORT_BUFFER: UInt32 = 13
SNMP_BERAPI_INVALID_OBJELEM: UInt32 = 14
SNMP_PDUAPI_UNRECOGNIZED_PDU: UInt32 = 20
SNMP_PDUAPI_INVALID_ES: UInt32 = 21
SNMP_PDUAPI_INVALID_GT: UInt32 = 22
SNMP_AUTHAPI_INVALID_VERSION: UInt32 = 30
SNMP_AUTHAPI_INVALID_MSG_TYPE: UInt32 = 31
SNMP_AUTHAPI_TRIV_AUTH_FAILED: UInt32 = 32
ASN_CONTEXTSPECIFIC: UInt32 = 128
ASN_PRIMATIVE: UInt32 = 0
SNMP_MGMTAPI_TIMEOUT: UInt32 = 40
SNMP_MGMTAPI_SELECT_FDERRORS: UInt32 = 41
SNMP_MGMTAPI_TRAP_ERRORS: UInt32 = 42
SNMP_MGMTAPI_TRAP_DUPINIT: UInt32 = 43
SNMP_MGMTAPI_NOTRAPS: UInt32 = 44
SNMP_MGMTAPI_AGAIN: UInt32 = 45
SNMP_MGMTAPI_INVALID_CTL: UInt32 = 46
SNMP_MGMTAPI_INVALID_SESSION: UInt32 = 47
SNMP_MGMTAPI_INVALID_BUFFER: UInt32 = 48
MGMCTL_SETAGENTPORT: UInt32 = 1
MAXOBJIDSIZE: UInt32 = 128
MAXOBJIDSTRSIZE: UInt32 = 1408
SNMPLISTEN_USEENTITY_ADDR: UInt32 = 0
SNMPLISTEN_ALL_ADDR: UInt32 = 1
SNMP_TRAP_COLDSTART: UInt32 = 0
SNMP_TRAP_WARMSTART: UInt32 = 1
SNMP_TRAP_LINKDOWN: UInt32 = 2
SNMP_TRAP_LINKUP: UInt32 = 3
SNMP_TRAP_AUTHFAIL: UInt32 = 4
SNMP_TRAP_EGPNEIGHBORLOSS: UInt32 = 5
SNMP_TRAP_ENTERPRISESPECIFIC: UInt32 = 6
SNMPAPI_NO_SUPPORT: UInt32 = 0
SNMPAPI_V1_SUPPORT: UInt32 = 1
SNMPAPI_V2_SUPPORT: UInt32 = 2
SNMPAPI_M2M_SUPPORT: UInt32 = 3
SNMPAPI_FAILURE: UInt32 = 0
SNMPAPI_SUCCESS: UInt32 = 1
SNMPAPI_ALLOC_ERROR: UInt32 = 2
SNMPAPI_CONTEXT_INVALID: UInt32 = 3
SNMPAPI_CONTEXT_UNKNOWN: UInt32 = 4
SNMPAPI_ENTITY_INVALID: UInt32 = 5
SNMPAPI_ENTITY_UNKNOWN: UInt32 = 6
SNMPAPI_INDEX_INVALID: UInt32 = 7
SNMPAPI_NOOP: UInt32 = 8
SNMPAPI_OID_INVALID: UInt32 = 9
SNMPAPI_OPERATION_INVALID: UInt32 = 10
SNMPAPI_OUTPUT_TRUNCATED: UInt32 = 11
SNMPAPI_PDU_INVALID: UInt32 = 12
SNMPAPI_SESSION_INVALID: UInt32 = 13
SNMPAPI_SYNTAX_INVALID: UInt32 = 14
SNMPAPI_VBL_INVALID: UInt32 = 15
SNMPAPI_MODE_INVALID: UInt32 = 16
SNMPAPI_SIZE_INVALID: UInt32 = 17
SNMPAPI_NOT_INITIALIZED: UInt32 = 18
SNMPAPI_MESSAGE_INVALID: UInt32 = 19
SNMPAPI_HWND_INVALID: UInt32 = 20
SNMPAPI_OTHER_ERROR: UInt32 = 99
SNMPAPI_TL_NOT_INITIALIZED: UInt32 = 100
SNMPAPI_TL_NOT_SUPPORTED: UInt32 = 101
SNMPAPI_TL_NOT_AVAILABLE: UInt32 = 102
SNMPAPI_TL_RESOURCE_ERROR: UInt32 = 103
SNMPAPI_TL_UNDELIVERABLE: UInt32 = 104
SNMPAPI_TL_SRC_INVALID: UInt32 = 105
SNMPAPI_TL_INVALID_PARAM: UInt32 = 106
SNMPAPI_TL_IN_USE: UInt32 = 107
SNMPAPI_TL_TIMEOUT: UInt32 = 108
SNMPAPI_TL_PDU_TOO_BIG: UInt32 = 109
SNMPAPI_TL_OTHER: UInt32 = 199
MAXVENDORINFO: UInt32 = 32
@winfunctype('snmpapi.dll')
def SnmpUtilOidCpy(pOidDst: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier_head), pOidSrc: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier_head)) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilOidAppend(pOidDst: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier_head), pOidSrc: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier_head)) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilOidNCmp(pOid1: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier_head), pOid2: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier_head), nSubIds: UInt32) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilOidCmp(pOid1: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier_head), pOid2: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier_head)) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilOidFree(pOid: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier_head)) -> Void: ...
@winfunctype('snmpapi.dll')
def SnmpUtilOctetsCmp(pOctets1: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnOctetString_head), pOctets2: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnOctetString_head)) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilOctetsNCmp(pOctets1: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnOctetString_head), pOctets2: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnOctetString_head), nChars: UInt32) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilOctetsCpy(pOctetsDst: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnOctetString_head), pOctetsSrc: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnOctetString_head)) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilOctetsFree(pOctets: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnOctetString_head)) -> Void: ...
@winfunctype('snmpapi.dll')
def SnmpUtilAsnAnyCpy(pAnyDst: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnAny_head), pAnySrc: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnAny_head)) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilAsnAnyFree(pAny: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnAny_head)) -> Void: ...
@winfunctype('snmpapi.dll')
def SnmpUtilVarBindCpy(pVbDst: POINTER(Windows.Win32.NetworkManagement.Snmp.SnmpVarBind_head), pVbSrc: POINTER(Windows.Win32.NetworkManagement.Snmp.SnmpVarBind_head)) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilVarBindFree(pVb: POINTER(Windows.Win32.NetworkManagement.Snmp.SnmpVarBind_head)) -> Void: ...
@winfunctype('snmpapi.dll')
def SnmpUtilVarBindListCpy(pVblDst: POINTER(Windows.Win32.NetworkManagement.Snmp.SnmpVarBindList_head), pVblSrc: POINTER(Windows.Win32.NetworkManagement.Snmp.SnmpVarBindList_head)) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilVarBindListFree(pVbl: POINTER(Windows.Win32.NetworkManagement.Snmp.SnmpVarBindList_head)) -> Void: ...
@winfunctype('snmpapi.dll')
def SnmpUtilMemFree(pMem: c_void_p) -> Void: ...
@winfunctype('snmpapi.dll')
def SnmpUtilMemAlloc(nBytes: UInt32) -> c_void_p: ...
@winfunctype('snmpapi.dll')
def SnmpUtilMemReAlloc(pMem: c_void_p, nBytes: UInt32) -> c_void_p: ...
@winfunctype('snmpapi.dll')
def SnmpUtilOidToA(Oid: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier_head)) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('snmpapi.dll')
def SnmpUtilIdsToA(Ids: POINTER(UInt32), IdLength: UInt32) -> Windows.Win32.Foundation.PSTR: ...
@winfunctype('snmpapi.dll')
def SnmpUtilPrintOid(Oid: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier_head)) -> Void: ...
@winfunctype('snmpapi.dll')
def SnmpUtilPrintAsnAny(pAny: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnAny_head)) -> Void: ...
@winfunctype('snmpapi.dll')
def SnmpSvcGetUptime() -> UInt32: ...
@winfunctype('snmpapi.dll')
def SnmpSvcSetLogLevel(nLogLevel: Windows.Win32.NetworkManagement.Snmp.SNMP_LOG) -> Void: ...
@winfunctype('snmpapi.dll')
def SnmpSvcSetLogType(nLogType: Windows.Win32.NetworkManagement.Snmp.SNMP_OUTPUT_LOG_TYPE) -> Void: ...
@cfunctype('snmpapi.dll', variadic=True)
def SnmpUtilDbgPrint(nLogLevel: Windows.Win32.NetworkManagement.Snmp.SNMP_LOG, szFormat: Windows.Win32.Foundation.PSTR, *__arglist) -> Void: ...
@winfunctype('mgmtapi.dll')
def SnmpMgrOpen(lpAgentAddress: Windows.Win32.Foundation.PSTR, lpAgentCommunity: Windows.Win32.Foundation.PSTR, nTimeOut: Int32, nRetries: Int32) -> c_void_p: ...
@winfunctype('mgmtapi.dll')
def SnmpMgrCtl(session: c_void_p, dwCtlCode: UInt32, lpvInBuffer: c_void_p, cbInBuffer: UInt32, lpvOUTBuffer: c_void_p, cbOUTBuffer: UInt32, lpcbBytesReturned: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mgmtapi.dll')
def SnmpMgrClose(session: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mgmtapi.dll')
def SnmpMgrRequest(session: c_void_p, requestType: Byte, variableBindings: POINTER(Windows.Win32.NetworkManagement.Snmp.SnmpVarBindList_head), errorStatus: POINTER(Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS), errorIndex: POINTER(Int32)) -> Int32: ...
@winfunctype('mgmtapi.dll')
def SnmpMgrStrToOid(string: Windows.Win32.Foundation.PSTR, oid: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mgmtapi.dll')
def SnmpMgrOidToStr(oid: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier_head), string: POINTER(Windows.Win32.Foundation.PSTR)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mgmtapi.dll')
def SnmpMgrTrapListen(phTrapAvailable: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mgmtapi.dll')
def SnmpMgrGetTrap(enterprise: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier_head), IPAddress: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnOctetString_head), genericTrap: POINTER(Windows.Win32.NetworkManagement.Snmp.SNMP_GENERICTRAP), specificTrap: POINTER(Int32), timeStamp: POINTER(UInt32), variableBindings: POINTER(Windows.Win32.NetworkManagement.Snmp.SnmpVarBindList_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mgmtapi.dll')
def SnmpMgrGetTrapEx(enterprise: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier_head), agentAddress: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnOctetString_head), sourceAddress: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnOctetString_head), genericTrap: POINTER(Windows.Win32.NetworkManagement.Snmp.SNMP_GENERICTRAP), specificTrap: POINTER(Int32), community: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnOctetString_head), timeStamp: POINTER(UInt32), variableBindings: POINTER(Windows.Win32.NetworkManagement.Snmp.SnmpVarBindList_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('wsnmp32.dll')
def SnmpGetTranslateMode(nTranslateMode: POINTER(Windows.Win32.NetworkManagement.Snmp.SNMP_API_TRANSLATE_MODE)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpSetTranslateMode(nTranslateMode: Windows.Win32.NetworkManagement.Snmp.SNMP_API_TRANSLATE_MODE) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpGetRetransmitMode(nRetransmitMode: POINTER(Windows.Win32.NetworkManagement.Snmp.SNMP_STATUS)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpSetRetransmitMode(nRetransmitMode: Windows.Win32.NetworkManagement.Snmp.SNMP_STATUS) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpGetTimeout(hEntity: IntPtr, nPolicyTimeout: POINTER(UInt32), nActualTimeout: POINTER(UInt32)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpSetTimeout(hEntity: IntPtr, nPolicyTimeout: UInt32) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpGetRetry(hEntity: IntPtr, nPolicyRetry: POINTER(UInt32), nActualRetry: POINTER(UInt32)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpSetRetry(hEntity: IntPtr, nPolicyRetry: UInt32) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpGetVendorInfo(vendorInfo: POINTER(Windows.Win32.NetworkManagement.Snmp.smiVENDORINFO_head)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpStartup(nMajorVersion: POINTER(UInt32), nMinorVersion: POINTER(UInt32), nLevel: POINTER(UInt32), nTranslateMode: POINTER(Windows.Win32.NetworkManagement.Snmp.SNMP_API_TRANSLATE_MODE), nRetransmitMode: POINTER(Windows.Win32.NetworkManagement.Snmp.SNMP_STATUS)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpCleanup() -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpOpen(hWnd: Windows.Win32.Foundation.HWND, wMsg: UInt32) -> IntPtr: ...
@winfunctype('wsnmp32.dll')
def SnmpClose(session: IntPtr) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpSendMsg(session: IntPtr, srcEntity: IntPtr, dstEntity: IntPtr, context: IntPtr, PDU: IntPtr) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpRecvMsg(session: IntPtr, srcEntity: POINTER(IntPtr), dstEntity: POINTER(IntPtr), context: POINTER(IntPtr), PDU: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpRegister(session: IntPtr, srcEntity: IntPtr, dstEntity: IntPtr, context: IntPtr, notification: POINTER(Windows.Win32.NetworkManagement.Snmp.smiOID_head), state: Windows.Win32.NetworkManagement.Snmp.SNMP_STATUS) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpCreateSession(hWnd: Windows.Win32.Foundation.HWND, wMsg: UInt32, fCallBack: Windows.Win32.NetworkManagement.Snmp.SNMPAPI_CALLBACK, lpClientData: c_void_p) -> IntPtr: ...
@winfunctype('wsnmp32.dll')
def SnmpListen(hEntity: IntPtr, lStatus: Windows.Win32.NetworkManagement.Snmp.SNMP_STATUS) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpListenEx(hEntity: IntPtr, lStatus: UInt32, nUseEntityAddr: UInt32) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpCancelMsg(session: IntPtr, reqId: Int32) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpStartupEx(nMajorVersion: POINTER(UInt32), nMinorVersion: POINTER(UInt32), nLevel: POINTER(UInt32), nTranslateMode: POINTER(Windows.Win32.NetworkManagement.Snmp.SNMP_API_TRANSLATE_MODE), nRetransmitMode: POINTER(Windows.Win32.NetworkManagement.Snmp.SNMP_STATUS)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpCleanupEx() -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpStrToEntity(session: IntPtr, string: Windows.Win32.Foundation.PSTR) -> IntPtr: ...
@winfunctype('wsnmp32.dll')
def SnmpEntityToStr(entity: IntPtr, size: UInt32, string: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpFreeEntity(entity: IntPtr) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpStrToContext(session: IntPtr, string: POINTER(Windows.Win32.NetworkManagement.Snmp.smiOCTETS_head)) -> IntPtr: ...
@winfunctype('wsnmp32.dll')
def SnmpContextToStr(context: IntPtr, string: POINTER(Windows.Win32.NetworkManagement.Snmp.smiOCTETS_head)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpFreeContext(context: IntPtr) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpSetPort(hEntity: IntPtr, nPort: UInt32) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpCreatePdu(session: IntPtr, PDU_type: Windows.Win32.NetworkManagement.Snmp.SNMP_PDU_TYPE, request_id: Int32, error_status: Int32, error_index: Int32, varbindlist: IntPtr) -> IntPtr: ...
@winfunctype('wsnmp32.dll')
def SnmpGetPduData(PDU: IntPtr, PDU_type: POINTER(Windows.Win32.NetworkManagement.Snmp.SNMP_PDU_TYPE), request_id: POINTER(Int32), error_status: POINTER(Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR), error_index: POINTER(Int32), varbindlist: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpSetPduData(PDU: IntPtr, PDU_type: POINTER(Int32), request_id: POINTER(Int32), non_repeaters: POINTER(Int32), max_repetitions: POINTER(Int32), varbindlist: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpDuplicatePdu(session: IntPtr, PDU: IntPtr) -> IntPtr: ...
@winfunctype('wsnmp32.dll')
def SnmpFreePdu(PDU: IntPtr) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpCreateVbl(session: IntPtr, name: POINTER(Windows.Win32.NetworkManagement.Snmp.smiOID_head), value: POINTER(Windows.Win32.NetworkManagement.Snmp.smiVALUE_head)) -> IntPtr: ...
@winfunctype('wsnmp32.dll')
def SnmpDuplicateVbl(session: IntPtr, vbl: IntPtr) -> IntPtr: ...
@winfunctype('wsnmp32.dll')
def SnmpFreeVbl(vbl: IntPtr) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpCountVbl(vbl: IntPtr) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpGetVb(vbl: IntPtr, index: UInt32, name: POINTER(Windows.Win32.NetworkManagement.Snmp.smiOID_head), value: POINTER(Windows.Win32.NetworkManagement.Snmp.smiVALUE_head)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpSetVb(vbl: IntPtr, index: UInt32, name: POINTER(Windows.Win32.NetworkManagement.Snmp.smiOID_head), value: POINTER(Windows.Win32.NetworkManagement.Snmp.smiVALUE_head)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpDeleteVb(vbl: IntPtr, index: UInt32) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpGetLastError(session: IntPtr) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpStrToOid(string: Windows.Win32.Foundation.PSTR, dstOID: POINTER(Windows.Win32.NetworkManagement.Snmp.smiOID_head)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpOidToStr(srcOID: POINTER(Windows.Win32.NetworkManagement.Snmp.smiOID_head), size: UInt32, string: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpOidCopy(srcOID: POINTER(Windows.Win32.NetworkManagement.Snmp.smiOID_head), dstOID: POINTER(Windows.Win32.NetworkManagement.Snmp.smiOID_head)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpOidCompare(xOID: POINTER(Windows.Win32.NetworkManagement.Snmp.smiOID_head), yOID: POINTER(Windows.Win32.NetworkManagement.Snmp.smiOID_head), maxlen: UInt32, result: POINTER(Int32)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpEncodeMsg(session: IntPtr, srcEntity: IntPtr, dstEntity: IntPtr, context: IntPtr, pdu: IntPtr, msgBufDesc: POINTER(Windows.Win32.NetworkManagement.Snmp.smiOCTETS_head)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpDecodeMsg(session: IntPtr, srcEntity: POINTER(IntPtr), dstEntity: POINTER(IntPtr), context: POINTER(IntPtr), pdu: POINTER(IntPtr), msgBufDesc: POINTER(Windows.Win32.NetworkManagement.Snmp.smiOCTETS_head)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpFreeDescriptor(syntax: UInt32, descriptor: POINTER(Windows.Win32.NetworkManagement.Snmp.smiOCTETS_head)) -> UInt32: ...
class AsnAny(EasyCastStructure):
    asnType: Byte
    asnValue: _asnValue_e__Union
    _pack_ = 4
    class _asnValue_e__Union(EasyCastUnion):
        number: Int32
        unsigned32: UInt32
        counter64: UInt64
        string: Windows.Win32.NetworkManagement.Snmp.AsnOctetString
        bits: Windows.Win32.NetworkManagement.Snmp.AsnOctetString
        object: Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier
        sequence: Windows.Win32.NetworkManagement.Snmp.AsnOctetString
        address: Windows.Win32.NetworkManagement.Snmp.AsnOctetString
        counter: UInt32
        gauge: UInt32
        ticks: UInt32
        arbitrary: Windows.Win32.NetworkManagement.Snmp.AsnOctetString
        _pack_ = 4
class AsnObjectIdentifier(EasyCastStructure):
    idLength: UInt32
    ids: POINTER(UInt32)
    _pack_ = 4
class AsnOctetString(EasyCastStructure):
    stream: POINTER(Byte)
    length: UInt32
    dynamic: Windows.Win32.Foundation.BOOL
    _pack_ = 4
@winfunctype_pointer
def PFNSNMPCLEANUPEX() -> UInt32: ...
@winfunctype_pointer
def PFNSNMPEXTENSIONCLOSE() -> Void: ...
@winfunctype_pointer
def PFNSNMPEXTENSIONINIT(dwUpTimeReference: UInt32, phSubagentTrapEvent: POINTER(Windows.Win32.Foundation.HANDLE), pFirstSupportedRegion: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFNSNMPEXTENSIONINITEX(pNextSupportedRegion: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFNSNMPEXTENSIONMONITOR(pAgentMgmtData: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFNSNMPEXTENSIONQUERY(bPduType: Byte, pVarBindList: POINTER(Windows.Win32.NetworkManagement.Snmp.SnmpVarBindList_head), pErrorStatus: POINTER(Int32), pErrorIndex: POINTER(Int32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFNSNMPEXTENSIONQUERYEX(nRequestType: UInt32, nTransactionId: UInt32, pVarBindList: POINTER(Windows.Win32.NetworkManagement.Snmp.SnmpVarBindList_head), pContextInfo: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnOctetString_head), pErrorStatus: POINTER(Int32), pErrorIndex: POINTER(Int32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFNSNMPEXTENSIONTRAP(pEnterpriseOid: POINTER(Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier_head), pGenericTrapId: POINTER(Int32), pSpecificTrapId: POINTER(Int32), pTimeStamp: POINTER(UInt32), pVarBindList: POINTER(Windows.Win32.NetworkManagement.Snmp.SnmpVarBindList_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFNSNMPSTARTUPEX(param0: POINTER(UInt32), param1: POINTER(UInt32), param2: POINTER(UInt32), param3: POINTER(UInt32), param4: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def SNMPAPI_CALLBACK(hSession: IntPtr, hWnd: Windows.Win32.Foundation.HWND, wMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, lpClientData: c_void_p) -> UInt32: ...
SNMP_API_TRANSLATE_MODE = UInt32
SNMPAPI_TRANSLATED: SNMP_API_TRANSLATE_MODE = 0
SNMPAPI_UNTRANSLATED_V1: SNMP_API_TRANSLATE_MODE = 1
SNMPAPI_UNTRANSLATED_V2: SNMP_API_TRANSLATE_MODE = 2
SNMP_ERROR = UInt32
SNMP_ERROR_NOERROR: SNMP_ERROR = 0
SNMP_ERROR_TOOBIG: SNMP_ERROR = 1
SNMP_ERROR_NOSUCHNAME: SNMP_ERROR = 2
SNMP_ERROR_BADVALUE: SNMP_ERROR = 3
SNMP_ERROR_READONLY: SNMP_ERROR = 4
SNMP_ERROR_GENERR: SNMP_ERROR = 5
SNMP_ERROR_NOACCESS: SNMP_ERROR = 6
SNMP_ERROR_WRONGTYPE: SNMP_ERROR = 7
SNMP_ERROR_WRONGLENGTH: SNMP_ERROR = 8
SNMP_ERROR_WRONGENCODING: SNMP_ERROR = 9
SNMP_ERROR_WRONGVALUE: SNMP_ERROR = 10
SNMP_ERROR_NOCREATION: SNMP_ERROR = 11
SNMP_ERROR_INCONSISTENTVALUE: SNMP_ERROR = 12
SNMP_ERROR_RESOURCEUNAVAILABLE: SNMP_ERROR = 13
SNMP_ERROR_COMMITFAILED: SNMP_ERROR = 14
SNMP_ERROR_UNDOFAILED: SNMP_ERROR = 15
SNMP_ERROR_AUTHORIZATIONERROR: SNMP_ERROR = 16
SNMP_ERROR_NOTWRITABLE: SNMP_ERROR = 17
SNMP_ERROR_INCONSISTENTNAME: SNMP_ERROR = 18
SNMP_ERROR_STATUS = UInt32
SNMP_ERRORSTATUS_NOERROR: SNMP_ERROR_STATUS = 0
SNMP_ERRORSTATUS_TOOBIG: SNMP_ERROR_STATUS = 1
SNMP_ERRORSTATUS_NOSUCHNAME: SNMP_ERROR_STATUS = 2
SNMP_ERRORSTATUS_BADVALUE: SNMP_ERROR_STATUS = 3
SNMP_ERRORSTATUS_READONLY: SNMP_ERROR_STATUS = 4
SNMP_ERRORSTATUS_GENERR: SNMP_ERROR_STATUS = 5
SNMP_ERRORSTATUS_NOACCESS: SNMP_ERROR_STATUS = 6
SNMP_ERRORSTATUS_WRONGTYPE: SNMP_ERROR_STATUS = 7
SNMP_ERRORSTATUS_WRONGLENGTH: SNMP_ERROR_STATUS = 8
SNMP_ERRORSTATUS_WRONGENCODING: SNMP_ERROR_STATUS = 9
SNMP_ERRORSTATUS_WRONGVALUE: SNMP_ERROR_STATUS = 10
SNMP_ERRORSTATUS_NOCREATION: SNMP_ERROR_STATUS = 11
SNMP_ERRORSTATUS_INCONSISTENTVALUE: SNMP_ERROR_STATUS = 12
SNMP_ERRORSTATUS_RESOURCEUNAVAILABLE: SNMP_ERROR_STATUS = 13
SNMP_ERRORSTATUS_COMMITFAILED: SNMP_ERROR_STATUS = 14
SNMP_ERRORSTATUS_UNDOFAILED: SNMP_ERROR_STATUS = 15
SNMP_ERRORSTATUS_AUTHORIZATIONERROR: SNMP_ERROR_STATUS = 16
SNMP_ERRORSTATUS_NOTWRITABLE: SNMP_ERROR_STATUS = 17
SNMP_ERRORSTATUS_INCONSISTENTNAME: SNMP_ERROR_STATUS = 18
SNMP_EXTENSION_REQUEST_TYPE = UInt32
SNMP_EXTENSION_GET: SNMP_EXTENSION_REQUEST_TYPE = 160
SNMP_EXTENSION_GET_NEXT: SNMP_EXTENSION_REQUEST_TYPE = 161
SNMP_EXTENSION_SET_TEST: SNMP_EXTENSION_REQUEST_TYPE = 224
SNMP_EXTENSION_SET_COMMIT: SNMP_EXTENSION_REQUEST_TYPE = 163
SNMP_EXTENSION_SET_UNDO: SNMP_EXTENSION_REQUEST_TYPE = 225
SNMP_EXTENSION_SET_CLEANUP: SNMP_EXTENSION_REQUEST_TYPE = 226
SNMP_GENERICTRAP = UInt32
SNMP_GENERICTRAP_COLDSTART: SNMP_GENERICTRAP = 0
SNMP_GENERICTRAP_WARMSTART: SNMP_GENERICTRAP = 1
SNMP_GENERICTRAP_LINKDOWN: SNMP_GENERICTRAP = 2
SNMP_GENERICTRAP_LINKUP: SNMP_GENERICTRAP = 3
SNMP_GENERICTRAP_AUTHFAILURE: SNMP_GENERICTRAP = 4
SNMP_GENERICTRAP_EGPNEIGHLOSS: SNMP_GENERICTRAP = 5
SNMP_GENERICTRAP_ENTERSPECIFIC: SNMP_GENERICTRAP = 6
SNMP_LOG = UInt32
SNMP_LOG_SILENT: SNMP_LOG = 0
SNMP_LOG_FATAL: SNMP_LOG = 1
SNMP_LOG_ERROR: SNMP_LOG = 2
SNMP_LOG_WARNING: SNMP_LOG = 3
SNMP_LOG_TRACE: SNMP_LOG = 4
SNMP_LOG_VERBOSE: SNMP_LOG = 5
SNMP_OUTPUT_LOG_TYPE = UInt32
SNMP_OUTPUT_TO_CONSOLE: SNMP_OUTPUT_LOG_TYPE = 1
SNMP_OUTPUT_TO_LOGFILE: SNMP_OUTPUT_LOG_TYPE = 2
SNMP_OUTPUT_TO_DEBUGGER: SNMP_OUTPUT_LOG_TYPE = 8
SNMP_PDU_TYPE = UInt32
SNMP_PDU_GET: SNMP_PDU_TYPE = 160
SNMP_PDU_GETNEXT: SNMP_PDU_TYPE = 161
SNMP_PDU_RESPONSE: SNMP_PDU_TYPE = 162
SNMP_PDU_SET: SNMP_PDU_TYPE = 163
SNMP_PDU_GETBULK: SNMP_PDU_TYPE = 165
SNMP_PDU_TRAP: SNMP_PDU_TYPE = 167
SNMP_STATUS = UInt32
SNMPAPI_ON: SNMP_STATUS = 1
SNMPAPI_OFF: SNMP_STATUS = 0
class SnmpVarBind(EasyCastStructure):
    name: Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier
    value: Windows.Win32.NetworkManagement.Snmp.AsnAny
    _pack_ = 4
class SnmpVarBindList(EasyCastStructure):
    list: POINTER(Windows.Win32.NetworkManagement.Snmp.SnmpVarBind_head)
    len: UInt32
    _pack_ = 4
class smiCNTR64(EasyCastStructure):
    hipart: UInt32
    lopart: UInt32
class smiOCTETS(EasyCastStructure):
    len: UInt32
    ptr: POINTER(Byte)
class smiOID(EasyCastStructure):
    len: UInt32
    ptr: POINTER(UInt32)
class smiVALUE(EasyCastStructure):
    syntax: UInt32
    value: _value_e__Union
    class _value_e__Union(EasyCastUnion):
        sNumber: Int32
        uNumber: UInt32
        hNumber: Windows.Win32.NetworkManagement.Snmp.smiCNTR64
        string: Windows.Win32.NetworkManagement.Snmp.smiOCTETS
        oid: Windows.Win32.NetworkManagement.Snmp.smiOID
        empty: Byte
class smiVENDORINFO(EasyCastStructure):
    vendorName: Windows.Win32.Foundation.CHAR * 64
    vendorContact: Windows.Win32.Foundation.CHAR * 64
    vendorVersionId: Windows.Win32.Foundation.CHAR * 32
    vendorVersionDate: Windows.Win32.Foundation.CHAR * 32
    vendorEnterprise: UInt32
make_head(_module, 'AsnAny')
make_head(_module, 'AsnObjectIdentifier')
make_head(_module, 'AsnOctetString')
make_head(_module, 'PFNSNMPCLEANUPEX')
make_head(_module, 'PFNSNMPEXTENSIONCLOSE')
make_head(_module, 'PFNSNMPEXTENSIONINIT')
make_head(_module, 'PFNSNMPEXTENSIONINITEX')
make_head(_module, 'PFNSNMPEXTENSIONMONITOR')
make_head(_module, 'PFNSNMPEXTENSIONQUERY')
make_head(_module, 'PFNSNMPEXTENSIONQUERYEX')
make_head(_module, 'PFNSNMPEXTENSIONTRAP')
make_head(_module, 'PFNSNMPSTARTUPEX')
make_head(_module, 'SNMPAPI_CALLBACK')
make_head(_module, 'SnmpVarBind')
make_head(_module, 'SnmpVarBindList')
make_head(_module, 'smiCNTR64')
make_head(_module, 'smiOCTETS')
make_head(_module, 'smiOID')
make_head(_module, 'smiVALUE')
make_head(_module, 'smiVENDORINFO')
