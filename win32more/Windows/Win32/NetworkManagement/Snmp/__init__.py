from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.NetworkManagement.Snmp
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
def SnmpUtilOidCpy(pOidDst: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier), pOidSrc: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier)) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilOidAppend(pOidDst: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier), pOidSrc: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier)) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilOidNCmp(pOid1: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier), pOid2: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier), nSubIds: UInt32) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilOidCmp(pOid1: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier), pOid2: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier)) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilOidFree(pOid: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier)) -> Void: ...
@winfunctype('snmpapi.dll')
def SnmpUtilOctetsCmp(pOctets1: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnOctetString), pOctets2: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnOctetString)) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilOctetsNCmp(pOctets1: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnOctetString), pOctets2: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnOctetString), nChars: UInt32) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilOctetsCpy(pOctetsDst: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnOctetString), pOctetsSrc: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnOctetString)) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilOctetsFree(pOctets: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnOctetString)) -> Void: ...
@winfunctype('snmpapi.dll')
def SnmpUtilAsnAnyCpy(pAnyDst: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnAny), pAnySrc: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnAny)) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilAsnAnyFree(pAny: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnAny)) -> Void: ...
@winfunctype('snmpapi.dll')
def SnmpUtilVarBindCpy(pVbDst: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SnmpVarBind), pVbSrc: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SnmpVarBind)) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilVarBindFree(pVb: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SnmpVarBind)) -> Void: ...
@winfunctype('snmpapi.dll')
def SnmpUtilVarBindListCpy(pVblDst: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SnmpVarBindList), pVblSrc: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SnmpVarBindList)) -> Int32: ...
@winfunctype('snmpapi.dll')
def SnmpUtilVarBindListFree(pVbl: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SnmpVarBindList)) -> Void: ...
@winfunctype('snmpapi.dll')
def SnmpUtilMemFree(pMem: VoidPtr) -> Void: ...
@winfunctype('snmpapi.dll')
def SnmpUtilMemAlloc(nBytes: UInt32) -> VoidPtr: ...
@winfunctype('snmpapi.dll')
def SnmpUtilMemReAlloc(pMem: VoidPtr, nBytes: UInt32) -> VoidPtr: ...
@winfunctype('snmpapi.dll')
def SnmpUtilOidToA(Oid: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier)) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('snmpapi.dll')
def SnmpUtilIdsToA(Ids: POINTER(UInt32), IdLength: UInt32) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('snmpapi.dll')
def SnmpUtilPrintOid(Oid: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier)) -> Void: ...
@winfunctype('snmpapi.dll')
def SnmpUtilPrintAsnAny(pAny: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnAny)) -> Void: ...
@winfunctype('snmpapi.dll')
def SnmpSvcGetUptime() -> UInt32: ...
@winfunctype('snmpapi.dll')
def SnmpSvcSetLogLevel(nLogLevel: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_LOG) -> Void: ...
@winfunctype('snmpapi.dll')
def SnmpSvcSetLogType(nLogType: Int32) -> Void: ...
@cfunctype('snmpapi.dll', variadic=True)
def SnmpUtilDbgPrint(nLogLevel: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_LOG, szFormat: win32more.Windows.Win32.Foundation.PSTR, *__arglist) -> Void: ...
@winfunctype('mgmtapi.dll')
def SnmpMgrOpen(lpAgentAddress: win32more.Windows.Win32.Foundation.PSTR, lpAgentCommunity: win32more.Windows.Win32.Foundation.PSTR, nTimeOut: Int32, nRetries: Int32) -> VoidPtr: ...
@winfunctype('mgmtapi.dll')
def SnmpMgrCtl(session: VoidPtr, dwCtlCode: UInt32, lpvInBuffer: VoidPtr, cbInBuffer: UInt32, lpvOUTBuffer: VoidPtr, cbOUTBuffer: UInt32, lpcbBytesReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mgmtapi.dll')
def SnmpMgrClose(session: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mgmtapi.dll')
def SnmpMgrRequest(session: VoidPtr, requestType: Byte, variableBindings: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SnmpVarBindList), errorStatus: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS), errorIndex: POINTER(Int32)) -> Int32: ...
@winfunctype('mgmtapi.dll')
def SnmpMgrStrToOid(string: win32more.Windows.Win32.Foundation.PSTR, oid: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mgmtapi.dll')
def SnmpMgrOidToStr(oid: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier), string: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mgmtapi.dll')
def SnmpMgrTrapListen(phTrapAvailable: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mgmtapi.dll')
def SnmpMgrGetTrap(enterprise: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier), IPAddress: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnOctetString), genericTrap: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_GENERICTRAP), specificTrap: POINTER(Int32), timeStamp: POINTER(UInt32), variableBindings: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SnmpVarBindList)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mgmtapi.dll')
def SnmpMgrGetTrapEx(enterprise: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier), agentAddress: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnOctetString), sourceAddress: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnOctetString), genericTrap: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_GENERICTRAP), specificTrap: POINTER(Int32), community: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnOctetString), timeStamp: POINTER(UInt32), variableBindings: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SnmpVarBindList)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('wsnmp32.dll')
def SnmpGetTranslateMode(nTranslateMode: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_API_TRANSLATE_MODE)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpSetTranslateMode(nTranslateMode: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_API_TRANSLATE_MODE) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpGetRetransmitMode(nRetransmitMode: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_STATUS)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpSetRetransmitMode(nRetransmitMode: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_STATUS) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpGetTimeout(hEntity: IntPtr, nPolicyTimeout: POINTER(UInt32), nActualTimeout: POINTER(UInt32)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpSetTimeout(hEntity: IntPtr, nPolicyTimeout: UInt32) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpGetRetry(hEntity: IntPtr, nPolicyRetry: POINTER(UInt32), nActualRetry: POINTER(UInt32)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpSetRetry(hEntity: IntPtr, nPolicyRetry: UInt32) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpGetVendorInfo(vendorInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiVENDORINFO)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpStartup(nMajorVersion: POINTER(UInt32), nMinorVersion: POINTER(UInt32), nLevel: POINTER(UInt32), nTranslateMode: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_API_TRANSLATE_MODE), nRetransmitMode: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_STATUS)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpCleanup() -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpOpen(hWnd: win32more.Windows.Win32.Foundation.HWND, wMsg: UInt32) -> IntPtr: ...
@winfunctype('wsnmp32.dll')
def SnmpClose(session: IntPtr) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpSendMsg(session: IntPtr, srcEntity: IntPtr, dstEntity: IntPtr, context: IntPtr, PDU: IntPtr) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpRecvMsg(session: IntPtr, srcEntity: POINTER(IntPtr), dstEntity: POINTER(IntPtr), context: POINTER(IntPtr), PDU: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpRegister(session: IntPtr, srcEntity: IntPtr, dstEntity: IntPtr, context: IntPtr, notification: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiOID), state: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_STATUS) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpCreateSession(hWnd: win32more.Windows.Win32.Foundation.HWND, wMsg: UInt32, fCallBack: win32more.Windows.Win32.NetworkManagement.Snmp.SNMPAPI_CALLBACK, lpClientData: VoidPtr) -> IntPtr: ...
@winfunctype('wsnmp32.dll')
def SnmpListen(hEntity: IntPtr, lStatus: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_STATUS) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpListenEx(hEntity: IntPtr, lStatus: UInt32, nUseEntityAddr: UInt32) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpCancelMsg(session: IntPtr, reqId: Int32) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpStartupEx(nMajorVersion: POINTER(UInt32), nMinorVersion: POINTER(UInt32), nLevel: POINTER(UInt32), nTranslateMode: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_API_TRANSLATE_MODE), nRetransmitMode: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_STATUS)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpCleanupEx() -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpStrToEntity(session: IntPtr, string: win32more.Windows.Win32.Foundation.PSTR) -> IntPtr: ...
@winfunctype('wsnmp32.dll')
def SnmpEntityToStr(entity: IntPtr, size: UInt32, string: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpFreeEntity(entity: IntPtr) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpStrToContext(session: IntPtr, string: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiOCTETS)) -> IntPtr: ...
@winfunctype('wsnmp32.dll')
def SnmpContextToStr(context: IntPtr, string: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiOCTETS)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpFreeContext(context: IntPtr) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpSetPort(hEntity: IntPtr, nPort: UInt32) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpCreatePdu(session: IntPtr, PDU_type: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_PDU_TYPE, request_id: Int32, error_status: Int32, error_index: Int32, varbindlist: IntPtr) -> IntPtr: ...
@winfunctype('wsnmp32.dll')
def SnmpGetPduData(PDU: IntPtr, PDU_type: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_PDU_TYPE), request_id: POINTER(Int32), error_status: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR), error_index: POINTER(Int32), varbindlist: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpSetPduData(PDU: IntPtr, PDU_type: POINTER(Int32), request_id: POINTER(Int32), non_repeaters: POINTER(Int32), max_repetitions: POINTER(Int32), varbindlist: POINTER(IntPtr)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpDuplicatePdu(session: IntPtr, PDU: IntPtr) -> IntPtr: ...
@winfunctype('wsnmp32.dll')
def SnmpFreePdu(PDU: IntPtr) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpCreateVbl(session: IntPtr, name: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiOID), value: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiVALUE)) -> IntPtr: ...
@winfunctype('wsnmp32.dll')
def SnmpDuplicateVbl(session: IntPtr, vbl: IntPtr) -> IntPtr: ...
@winfunctype('wsnmp32.dll')
def SnmpFreeVbl(vbl: IntPtr) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpCountVbl(vbl: IntPtr) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpGetVb(vbl: IntPtr, index: UInt32, name: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiOID), value: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiVALUE)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpSetVb(vbl: IntPtr, index: UInt32, name: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiOID), value: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiVALUE)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpDeleteVb(vbl: IntPtr, index: UInt32) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpGetLastError(session: IntPtr) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpStrToOid(string: win32more.Windows.Win32.Foundation.PSTR, dstOID: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiOID)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpOidToStr(srcOID: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiOID), size: UInt32, string: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpOidCopy(srcOID: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiOID), dstOID: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiOID)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpOidCompare(xOID: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiOID), yOID: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiOID), maxlen: UInt32, result: POINTER(Int32)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpEncodeMsg(session: IntPtr, srcEntity: IntPtr, dstEntity: IntPtr, context: IntPtr, pdu: IntPtr, msgBufDesc: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiOCTETS)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpDecodeMsg(session: IntPtr, srcEntity: POINTER(IntPtr), dstEntity: POINTER(IntPtr), context: POINTER(IntPtr), pdu: POINTER(IntPtr), msgBufDesc: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiOCTETS)) -> UInt32: ...
@winfunctype('wsnmp32.dll')
def SnmpFreeDescriptor(syntax: UInt32, descriptor: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.smiOCTETS)) -> UInt32: ...
class AsnAny(Structure):
    asnType: Byte
    asnValue: _asnValue_e__Union
    _pack_ = 4
    class _asnValue_e__Union(Union):
        number: Int32
        unsigned32: UInt32
        counter64: UInt64
        string: win32more.Windows.Win32.NetworkManagement.Snmp.AsnOctetString
        bits: win32more.Windows.Win32.NetworkManagement.Snmp.AsnOctetString
        object: win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier
        sequence: win32more.Windows.Win32.NetworkManagement.Snmp.AsnOctetString
        address: win32more.Windows.Win32.NetworkManagement.Snmp.AsnOctetString
        counter: UInt32
        gauge: UInt32
        ticks: UInt32
        arbitrary: win32more.Windows.Win32.NetworkManagement.Snmp.AsnOctetString
        _pack_ = 4
if ARCH in 'X64,ARM64':
    class AsnObjectIdentifier(Structure):
        idLength: UInt32
        ids: POINTER(UInt32)
        _pack_ = 4
elif ARCH in 'X86':
    class AsnObjectIdentifier(Structure):
        idLength: UInt32
        ids: POINTER(UInt32)
if ARCH in 'X64,ARM64':
    class AsnOctetString(Structure):
        stream: POINTER(Byte)
        length: UInt32
        dynamic: win32more.Windows.Win32.Foundation.BOOL
        _pack_ = 4
elif ARCH in 'X86':
    class AsnOctetString(Structure):
        stream: POINTER(Byte)
        length: UInt32
        dynamic: win32more.Windows.Win32.Foundation.BOOL
@winfunctype_pointer
def PFNSNMPCLEANUPEX() -> UInt32: ...
@winfunctype_pointer
def PFNSNMPEXTENSIONCLOSE() -> Void: ...
@winfunctype_pointer
def PFNSNMPEXTENSIONINIT(dwUpTimeReference: UInt32, phSubagentTrapEvent: POINTER(win32more.Windows.Win32.Foundation.HANDLE), pFirstSupportedRegion: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFNSNMPEXTENSIONINITEX(pNextSupportedRegion: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFNSNMPEXTENSIONMONITOR(pAgentMgmtData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFNSNMPEXTENSIONQUERY(bPduType: Byte, pVarBindList: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SnmpVarBindList), pErrorStatus: POINTER(Int32), pErrorIndex: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFNSNMPEXTENSIONQUERYEX(nRequestType: UInt32, nTransactionId: UInt32, pVarBindList: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SnmpVarBindList), pContextInfo: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnOctetString), pErrorStatus: POINTER(Int32), pErrorIndex: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFNSNMPEXTENSIONTRAP(pEnterpriseOid: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier), pGenericTrapId: POINTER(Int32), pSpecificTrapId: POINTER(Int32), pTimeStamp: POINTER(UInt32), pVarBindList: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SnmpVarBindList)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PFNSNMPSTARTUPEX(param0: POINTER(UInt32), param1: POINTER(UInt32), param2: POINTER(UInt32), param3: POINTER(UInt32), param4: POINTER(UInt32)) -> UInt32: ...
@winfunctype_pointer
def SNMPAPI_CALLBACK(hSession: IntPtr, hWnd: win32more.Windows.Win32.Foundation.HWND, wMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, lpClientData: VoidPtr) -> UInt32: ...
SNMP_API_TRANSLATE_MODE = UInt32
SNMPAPI_TRANSLATED: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_API_TRANSLATE_MODE = 0
SNMPAPI_UNTRANSLATED_V1: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_API_TRANSLATE_MODE = 1
SNMPAPI_UNTRANSLATED_V2: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_API_TRANSLATE_MODE = 2
SNMP_ERROR = UInt32
SNMP_ERROR_NOERROR: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 0
SNMP_ERROR_TOOBIG: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 1
SNMP_ERROR_NOSUCHNAME: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 2
SNMP_ERROR_BADVALUE: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 3
SNMP_ERROR_READONLY: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 4
SNMP_ERROR_GENERR: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 5
SNMP_ERROR_NOACCESS: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 6
SNMP_ERROR_WRONGTYPE: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 7
SNMP_ERROR_WRONGLENGTH: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 8
SNMP_ERROR_WRONGENCODING: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 9
SNMP_ERROR_WRONGVALUE: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 10
SNMP_ERROR_NOCREATION: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 11
SNMP_ERROR_INCONSISTENTVALUE: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 12
SNMP_ERROR_RESOURCEUNAVAILABLE: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 13
SNMP_ERROR_COMMITFAILED: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 14
SNMP_ERROR_UNDOFAILED: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 15
SNMP_ERROR_AUTHORIZATIONERROR: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 16
SNMP_ERROR_NOTWRITABLE: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 17
SNMP_ERROR_INCONSISTENTNAME: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR = 18
SNMP_ERROR_STATUS = UInt32
SNMP_ERRORSTATUS_NOERROR: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 0
SNMP_ERRORSTATUS_TOOBIG: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 1
SNMP_ERRORSTATUS_NOSUCHNAME: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 2
SNMP_ERRORSTATUS_BADVALUE: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 3
SNMP_ERRORSTATUS_READONLY: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 4
SNMP_ERRORSTATUS_GENERR: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 5
SNMP_ERRORSTATUS_NOACCESS: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 6
SNMP_ERRORSTATUS_WRONGTYPE: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 7
SNMP_ERRORSTATUS_WRONGLENGTH: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 8
SNMP_ERRORSTATUS_WRONGENCODING: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 9
SNMP_ERRORSTATUS_WRONGVALUE: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 10
SNMP_ERRORSTATUS_NOCREATION: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 11
SNMP_ERRORSTATUS_INCONSISTENTVALUE: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 12
SNMP_ERRORSTATUS_RESOURCEUNAVAILABLE: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 13
SNMP_ERRORSTATUS_COMMITFAILED: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 14
SNMP_ERRORSTATUS_UNDOFAILED: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 15
SNMP_ERRORSTATUS_AUTHORIZATIONERROR: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 16
SNMP_ERRORSTATUS_NOTWRITABLE: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 17
SNMP_ERRORSTATUS_INCONSISTENTNAME: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_ERROR_STATUS = 18
SNMP_EXTENSION_REQUEST_TYPE = UInt32
SNMP_EXTENSION_GET: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_EXTENSION_REQUEST_TYPE = 160
SNMP_EXTENSION_GET_NEXT: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_EXTENSION_REQUEST_TYPE = 161
SNMP_EXTENSION_SET_TEST: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_EXTENSION_REQUEST_TYPE = 224
SNMP_EXTENSION_SET_COMMIT: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_EXTENSION_REQUEST_TYPE = 163
SNMP_EXTENSION_SET_UNDO: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_EXTENSION_REQUEST_TYPE = 225
SNMP_EXTENSION_SET_CLEANUP: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_EXTENSION_REQUEST_TYPE = 226
SNMP_GENERICTRAP = UInt32
SNMP_GENERICTRAP_COLDSTART: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_GENERICTRAP = 0
SNMP_GENERICTRAP_WARMSTART: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_GENERICTRAP = 1
SNMP_GENERICTRAP_LINKDOWN: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_GENERICTRAP = 2
SNMP_GENERICTRAP_LINKUP: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_GENERICTRAP = 3
SNMP_GENERICTRAP_AUTHFAILURE: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_GENERICTRAP = 4
SNMP_GENERICTRAP_EGPNEIGHLOSS: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_GENERICTRAP = 5
SNMP_GENERICTRAP_ENTERSPECIFIC: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_GENERICTRAP = 6
SNMP_LOG = Int32
SNMP_LOG_SILENT: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_LOG = 0
SNMP_LOG_FATAL: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_LOG = 1
SNMP_LOG_ERROR: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_LOG = 2
SNMP_LOG_WARNING: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_LOG = 3
SNMP_LOG_TRACE: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_LOG = 4
SNMP_LOG_VERBOSE: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_LOG = 5
SNMP_OUTPUT_LOG_TYPE = UInt32
SNMP_OUTPUT_TO_CONSOLE: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_OUTPUT_LOG_TYPE = 1
SNMP_OUTPUT_TO_LOGFILE: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_OUTPUT_LOG_TYPE = 2
SNMP_OUTPUT_TO_DEBUGGER: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_OUTPUT_LOG_TYPE = 8
SNMP_PDU_TYPE = UInt32
SNMP_PDU_GET: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_PDU_TYPE = 160
SNMP_PDU_GETNEXT: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_PDU_TYPE = 161
SNMP_PDU_RESPONSE: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_PDU_TYPE = 162
SNMP_PDU_SET: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_PDU_TYPE = 163
SNMP_PDU_GETBULK: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_PDU_TYPE = 165
SNMP_PDU_TRAP: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_PDU_TYPE = 167
SNMP_STATUS = UInt32
SNMPAPI_ON: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_STATUS = 1
SNMPAPI_OFF: win32more.Windows.Win32.NetworkManagement.Snmp.SNMP_STATUS = 0
class SnmpVarBind(Structure):
    name: win32more.Windows.Win32.NetworkManagement.Snmp.AsnObjectIdentifier
    value: win32more.Windows.Win32.NetworkManagement.Snmp.AsnAny
    _pack_ = 4
if ARCH in 'X64,ARM64':
    class SnmpVarBindList(Structure):
        list: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SnmpVarBind)
        len: UInt32
        _pack_ = 4
elif ARCH in 'X86':
    class SnmpVarBindList(Structure):
        list: POINTER(win32more.Windows.Win32.NetworkManagement.Snmp.SnmpVarBind)
        len: UInt32
class smiCNTR64(Structure):
    hipart: UInt32
    lopart: UInt32
class smiOCTETS(Structure):
    len: UInt32
    ptr: POINTER(Byte)
class smiOID(Structure):
    len: UInt32
    ptr: POINTER(UInt32)
class smiVALUE(Structure):
    syntax: UInt32
    value: _value_e__Union
    class _value_e__Union(Union):
        sNumber: Int32
        uNumber: UInt32
        hNumber: win32more.Windows.Win32.NetworkManagement.Snmp.smiCNTR64
        string: win32more.Windows.Win32.NetworkManagement.Snmp.smiOCTETS
        oid: win32more.Windows.Win32.NetworkManagement.Snmp.smiOID
        empty: Byte
class smiVENDORINFO(Structure):
    vendorName: win32more.Windows.Win32.Foundation.CHAR * 64
    vendorContact: win32more.Windows.Win32.Foundation.CHAR * 64
    vendorVersionId: win32more.Windows.Win32.Foundation.CHAR * 32
    vendorVersionDate: win32more.Windows.Win32.Foundation.CHAR * 32
    vendorEnterprise: UInt32


make_ready(__name__)
