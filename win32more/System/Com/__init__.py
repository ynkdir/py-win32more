from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.Security
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.System.Ole
import win32more.System.SystemServices
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
ADVANCED_FEATURE_FLAGS = UInt16
FADF_AUTO: ADVANCED_FEATURE_FLAGS = 1
FADF_STATIC: ADVANCED_FEATURE_FLAGS = 2
FADF_EMBEDDED: ADVANCED_FEATURE_FLAGS = 4
FADF_FIXEDSIZE: ADVANCED_FEATURE_FLAGS = 16
FADF_RECORD: ADVANCED_FEATURE_FLAGS = 32
FADF_HAVEIID: ADVANCED_FEATURE_FLAGS = 64
FADF_HAVEVARTYPE: ADVANCED_FEATURE_FLAGS = 128
FADF_BSTR: ADVANCED_FEATURE_FLAGS = 256
FADF_UNKNOWN: ADVANCED_FEATURE_FLAGS = 512
FADF_DISPATCH: ADVANCED_FEATURE_FLAGS = 1024
FADF_VARIANT: ADVANCED_FEATURE_FLAGS = 2048
FADF_RESERVED: ADVANCED_FEATURE_FLAGS = 61448
ADVF = Int32
ADVF_NODATA: ADVF = 1
ADVF_PRIMEFIRST: ADVF = 2
ADVF_ONLYONCE: ADVF = 4
ADVF_DATAONSTOP: ADVF = 64
ADVFCACHE_NOHANDLER: ADVF = 8
ADVFCACHE_FORCEBUILTIN: ADVF = 16
ADVFCACHE_ONSAVE: ADVF = 32
APTTYPE = Int32
APTTYPE_CURRENT: APTTYPE = -1
APTTYPE_STA: APTTYPE = 0
APTTYPE_MTA: APTTYPE = 1
APTTYPE_NA: APTTYPE = 2
APTTYPE_MAINSTA: APTTYPE = 3
APTTYPEQUALIFIER = Int32
APTTYPEQUALIFIER_NONE: APTTYPEQUALIFIER = 0
APTTYPEQUALIFIER_IMPLICIT_MTA: APTTYPEQUALIFIER = 1
APTTYPEQUALIFIER_NA_ON_MTA: APTTYPEQUALIFIER = 2
APTTYPEQUALIFIER_NA_ON_STA: APTTYPEQUALIFIER = 3
APTTYPEQUALIFIER_NA_ON_IMPLICIT_MTA: APTTYPEQUALIFIER = 4
APTTYPEQUALIFIER_NA_ON_MAINSTA: APTTYPEQUALIFIER = 5
APTTYPEQUALIFIER_APPLICATION_STA: APTTYPEQUALIFIER = 6
APTTYPEQUALIFIER_RESERVED_1: APTTYPEQUALIFIER = 7
class AUTHENTICATEINFO(Structure):
    dwFlags: UInt32
    dwReserved: UInt32
MARSHALINTERFACE_MIN: UInt32 = 500
ASYNC_MODE_COMPATIBILITY: Int32 = 1
ASYNC_MODE_DEFAULT: Int32 = 0
STGTY_REPEAT: Int32 = 256
STG_TOEND: Int32 = -1
STG_LAYOUT_SEQUENTIAL: Int32 = 0
STG_LAYOUT_INTERLEAVED: Int32 = 1
COM_RIGHTS_EXECUTE: UInt32 = 1
COM_RIGHTS_EXECUTE_LOCAL: UInt32 = 2
COM_RIGHTS_EXECUTE_REMOTE: UInt32 = 4
COM_RIGHTS_ACTIVATE_LOCAL: UInt32 = 8
COM_RIGHTS_ACTIVATE_REMOTE: UInt32 = 16
COM_RIGHTS_RESERVED1: UInt32 = 32
COM_RIGHTS_RESERVED2: UInt32 = 64
CWMO_MAX_HANDLES: UInt32 = 56
ROTREGFLAGS_ALLOWANYCLIENT: UInt32 = 1
APPIDREGFLAGS_ACTIVATE_IUSERVER_INDESKTOP: UInt32 = 1
APPIDREGFLAGS_SECURE_SERVER_PROCESS_SD_AND_BIND: UInt32 = 2
APPIDREGFLAGS_ISSUE_ACTIVATION_RPC_AT_IDENTIFY: UInt32 = 4
APPIDREGFLAGS_IUSERVER_UNMODIFIED_LOGON_TOKEN: UInt32 = 8
APPIDREGFLAGS_IUSERVER_SELF_SID_IN_LAUNCH_PERMISSION: UInt32 = 16
APPIDREGFLAGS_IUSERVER_ACTIVATE_IN_CLIENT_SESSION_ONLY: UInt32 = 32
APPIDREGFLAGS_RESERVED1: UInt32 = 64
APPIDREGFLAGS_RESERVED2: UInt32 = 128
APPIDREGFLAGS_RESERVED3: UInt32 = 256
APPIDREGFLAGS_RESERVED4: UInt32 = 512
APPIDREGFLAGS_RESERVED5: UInt32 = 1024
APPIDREGFLAGS_AAA_NO_IMPLICIT_ACTIVATE_AS_IU: UInt32 = 2048
APPIDREGFLAGS_RESERVED7: UInt32 = 4096
APPIDREGFLAGS_RESERVED8: UInt32 = 8192
APPIDREGFLAGS_RESERVED9: UInt32 = 16384
DCOMSCM_ACTIVATION_USE_ALL_AUTHNSERVICES: UInt32 = 1
DCOMSCM_ACTIVATION_DISALLOW_UNSECURE_CALL: UInt32 = 2
DCOMSCM_RESOLVE_USE_ALL_AUTHNSERVICES: UInt32 = 4
DCOMSCM_RESOLVE_DISALLOW_UNSECURE_CALL: UInt32 = 8
DCOMSCM_PING_USE_MID_AUTHNSERVICE: UInt32 = 16
DCOMSCM_PING_DISALLOW_UNSECURE_CALL: UInt32 = 32
MAXLSN: UInt64 = 9223372036854775807
DMUS_ERRBASE: UInt32 = 4096
@winfunctype('ole32.dll')
def CoBuildVersion() -> UInt32: ...
@winfunctype('OLE32.dll')
def CoInitialize(pvReserved: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRegisterMallocSpy(pMallocSpy: win32more.System.Com.IMallocSpy_head) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRevokeMallocSpy() -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRegisterInitializeSpy(pSpy: win32more.System.Com.IInitializeSpy_head, puliCookie: POINTER(win32more.Foundation.ULARGE_INTEGER_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRevokeInitializeSpy(uliCookie: win32more.Foundation.ULARGE_INTEGER) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetSystemSecurityPermissions(comSDType: win32more.System.Com.COMSD, ppSD: POINTER(win32more.Security.PSECURITY_DESCRIPTOR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoLoadLibrary(lpszLibName: win32more.Foundation.PWSTR, bAutoFree: win32more.Foundation.BOOL) -> win32more.Foundation.HINSTANCE: ...
@winfunctype('OLE32.dll')
def CoFreeLibrary(hInst: win32more.Foundation.HINSTANCE) -> Void: ...
@winfunctype('OLE32.dll')
def CoFreeAllLibraries() -> Void: ...
@winfunctype('OLE32.dll')
def CoAllowSetForegroundWindow(pUnk: win32more.System.Com.IUnknown_head, lpvReserved: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def DcomChannelSetHResult(pvReserved: c_void_p, pulReserved: POINTER(UInt32), appsHR: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def CoIsOle1Class(rclsid: POINTER(Guid)) -> win32more.Foundation.BOOL: ...
@winfunctype('OLE32.dll')
def CLSIDFromProgIDEx(lpszProgID: win32more.Foundation.PWSTR, lpclsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoFileTimeToDosDateTime(lpFileTime: POINTER(win32more.Foundation.FILETIME_head), lpDosDate: POINTER(UInt16), lpDosTime: POINTER(UInt16)) -> win32more.Foundation.BOOL: ...
@winfunctype('OLE32.dll')
def CoDosDateTimeToFileTime(nDosDate: UInt16, nDosTime: UInt16, lpFileTime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('OLE32.dll')
def CoFileTimeNow(lpFileTime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def CoRegisterChannelHook(ExtensionUuid: POINTER(Guid), pChannelHook: win32more.System.Com.IChannelHook_head) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoTreatAsClass(clsidOld: POINTER(Guid), clsidNew: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateDataAdviseHolder(ppDAHolder: POINTER(win32more.System.Com.IDataAdviseHolder_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateDataCache(pUnkOuter: win32more.System.Com.IUnknown_head, rclsid: POINTER(Guid), iid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def CoInstall(pbc: win32more.System.Com.IBindCtx_head, dwFlags: UInt32, pClassSpec: POINTER(win32more.System.Com.uCLSSPEC_head), pQuery: POINTER(win32more.System.Com.QUERYCONTEXT_head), pszCodeBase: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def BindMoniker(pmk: win32more.System.Com.IMoniker_head, grfOpt: UInt32, iidResult: POINTER(Guid), ppvResult: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetObject(pszName: win32more.Foundation.PWSTR, pBindOptions: POINTER(win32more.System.Com.BIND_OPTS_head), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def MkParseDisplayName(pbc: win32more.System.Com.IBindCtx_head, szUserName: win32more.Foundation.PWSTR, pchEaten: POINTER(UInt32), ppmk: POINTER(win32more.System.Com.IMoniker_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def MonikerRelativePathTo(pmkSrc: win32more.System.Com.IMoniker_head, pmkDest: win32more.System.Com.IMoniker_head, ppmkRelPath: POINTER(win32more.System.Com.IMoniker_head), dwReserved: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def MonikerCommonPrefixWith(pmkThis: win32more.System.Com.IMoniker_head, pmkOther: win32more.System.Com.IMoniker_head, ppmkCommon: POINTER(win32more.System.Com.IMoniker_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateBindCtx(reserved: UInt32, ppbc: POINTER(win32more.System.Com.IBindCtx_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateGenericComposite(pmkFirst: win32more.System.Com.IMoniker_head, pmkRest: win32more.System.Com.IMoniker_head, ppmkComposite: POINTER(win32more.System.Com.IMoniker_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def GetClassFile(szFilename: win32more.Foundation.PWSTR, pclsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateClassMoniker(rclsid: POINTER(Guid), ppmk: POINTER(win32more.System.Com.IMoniker_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateFileMoniker(lpszPathName: win32more.Foundation.PWSTR, ppmk: POINTER(win32more.System.Com.IMoniker_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateItemMoniker(lpszDelim: win32more.Foundation.PWSTR, lpszItem: win32more.Foundation.PWSTR, ppmk: POINTER(win32more.System.Com.IMoniker_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateAntiMoniker(ppmk: POINTER(win32more.System.Com.IMoniker_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreatePointerMoniker(punk: win32more.System.Com.IUnknown_head, ppmk: POINTER(win32more.System.Com.IMoniker_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CreateObjrefMoniker(punk: win32more.System.Com.IUnknown_head, ppmk: POINTER(win32more.System.Com.IMoniker_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def GetRunningObjectTable(reserved: UInt32, pprot: POINTER(win32more.System.Com.IRunningObjectTable_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def CreateStdProgressIndicator(hwndParent: win32more.Foundation.HWND, pszTitle: win32more.Foundation.PWSTR, pIbscCaller: win32more.System.Com.IBindStatusCallback_head, ppIbsc: POINTER(win32more.System.Com.IBindStatusCallback_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetMalloc(dwMemContext: UInt32, ppMalloc: POINTER(win32more.System.Com.IMalloc_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoUninitialize() -> Void: ...
@winfunctype('OLE32.dll')
def CoGetCurrentProcess() -> UInt32: ...
@winfunctype('OLE32.dll')
def CoInitializeEx(pvReserved: c_void_p, dwCoInit: win32more.System.Com.COINIT) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetCallerTID(lpdwTID: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetCurrentLogicalThreadId(pguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetContextToken(pToken: POINTER(UIntPtr)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetApartmentType(pAptType: POINTER(win32more.System.Com.APTTYPE), pAptQualifier: POINTER(win32more.System.Com.APTTYPEQUALIFIER)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoIncrementMTAUsage(pCookie: POINTER(win32more.System.Com.CO_MTA_USAGE_COOKIE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoDecrementMTAUsage(Cookie: win32more.System.Com.CO_MTA_USAGE_COOKIE) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoAllowUnmarshalerCLSID(clsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetObjectContext(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetClassObject(rclsid: POINTER(Guid), dwClsContext: win32more.System.Com.CLSCTX, pvReserved: c_void_p, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRegisterClassObject(rclsid: POINTER(Guid), pUnk: win32more.System.Com.IUnknown_head, dwClsContext: win32more.System.Com.CLSCTX, flags: win32more.System.Com.REGCLS, lpdwRegister: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRevokeClassObject(dwRegister: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoResumeClassObjects() -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoSuspendClassObjects() -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoAddRefServerProcess() -> UInt32: ...
@winfunctype('OLE32.dll')
def CoReleaseServerProcess() -> UInt32: ...
@winfunctype('OLE32.dll')
def CoGetPSClsid(riid: POINTER(Guid), pClsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRegisterPSClsid(riid: POINTER(Guid), rclsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRegisterSurrogate(pSurrogate: win32more.System.Com.ISurrogate_head) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoDisconnectObject(pUnk: win32more.System.Com.IUnknown_head, dwReserved: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoLockObjectExternal(pUnk: win32more.System.Com.IUnknown_head, fLock: win32more.Foundation.BOOL, fLastUnlockReleases: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoIsHandlerConnected(pUnk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.BOOL: ...
@winfunctype('OLE32.dll')
def CoCreateFreeThreadedMarshaler(punkOuter: win32more.System.Com.IUnknown_head, ppunkMarshal: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoFreeUnusedLibraries() -> Void: ...
@winfunctype('OLE32.dll')
def CoFreeUnusedLibrariesEx(dwUnloadDelay: UInt32, dwReserved: UInt32) -> Void: ...
@winfunctype('OLE32.dll')
def CoDisconnectContext(dwTimeout: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoInitializeSecurity(pSecDesc: win32more.Security.PSECURITY_DESCRIPTOR, cAuthSvc: Int32, asAuthSvc: POINTER(win32more.System.Com.SOLE_AUTHENTICATION_SERVICE_head), pReserved1: c_void_p, dwAuthnLevel: win32more.System.Com.RPC_C_AUTHN_LEVEL, dwImpLevel: win32more.System.Com.RPC_C_IMP_LEVEL, pAuthList: c_void_p, dwCapabilities: win32more.System.Com.EOLE_AUTHENTICATION_CAPABILITIES, pReserved3: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetCallContext(riid: POINTER(Guid), ppInterface: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoQueryProxyBlanket(pProxy: win32more.System.Com.IUnknown_head, pwAuthnSvc: POINTER(UInt32), pAuthzSvc: POINTER(UInt32), pServerPrincName: POINTER(win32more.Foundation.PWSTR), pAuthnLevel: POINTER(UInt32), pImpLevel: POINTER(UInt32), pAuthInfo: POINTER(c_void_p), pCapabilites: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoSetProxyBlanket(pProxy: win32more.System.Com.IUnknown_head, dwAuthnSvc: UInt32, dwAuthzSvc: UInt32, pServerPrincName: win32more.Foundation.PWSTR, dwAuthnLevel: win32more.System.Com.RPC_C_AUTHN_LEVEL, dwImpLevel: win32more.System.Com.RPC_C_IMP_LEVEL, pAuthInfo: c_void_p, dwCapabilities: win32more.System.Com.EOLE_AUTHENTICATION_CAPABILITIES) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoCopyProxy(pProxy: win32more.System.Com.IUnknown_head, ppCopy: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoQueryClientBlanket(pAuthnSvc: POINTER(UInt32), pAuthzSvc: POINTER(UInt32), pServerPrincName: POINTER(win32more.Foundation.PWSTR), pAuthnLevel: POINTER(UInt32), pImpLevel: POINTER(UInt32), pPrivs: POINTER(c_void_p), pCapabilities: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoImpersonateClient() -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRevertToSelf() -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoQueryAuthenticationServices(pcAuthSvc: POINTER(UInt32), asAuthSvc: POINTER(POINTER(win32more.System.Com.SOLE_AUTHENTICATION_SERVICE_head))) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoSwitchCallContext(pNewObject: win32more.System.Com.IUnknown_head, ppOldObject: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoCreateInstance(rclsid: POINTER(Guid), pUnkOuter: win32more.System.Com.IUnknown_head, dwClsContext: win32more.System.Com.CLSCTX, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoCreateInstanceEx(Clsid: POINTER(Guid), punkOuter: win32more.System.Com.IUnknown_head, dwClsCtx: win32more.System.Com.CLSCTX, pServerInfo: POINTER(win32more.System.Com.COSERVERINFO_head), dwCount: UInt32, pResults: POINTER(win32more.System.Com.MULTI_QI_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoCreateInstanceFromApp(Clsid: POINTER(Guid), punkOuter: win32more.System.Com.IUnknown_head, dwClsCtx: win32more.System.Com.CLSCTX, reserved: c_void_p, dwCount: UInt32, pResults: POINTER(win32more.System.Com.MULTI_QI_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRegisterActivationFilter(pActivationFilter: win32more.System.Com.IActivationFilter_head) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetCancelObject(dwThreadId: UInt32, iid: POINTER(Guid), ppUnk: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoSetCancelObject(pUnk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoCancelCall(dwThreadId: UInt32, ulTimeout: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoTestCancel() -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoEnableCallCancellation(pReserved: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoDisableCallCancellation(pReserved: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StringFromCLSID(rclsid: POINTER(Guid), lplpsz: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CLSIDFromString(lpsz: win32more.Foundation.PWSTR, pclsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StringFromIID(rclsid: POINTER(Guid), lplpsz: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def IIDFromString(lpsz: win32more.Foundation.PWSTR, lpiid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def ProgIDFromCLSID(clsid: POINTER(Guid), lplpszProgID: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CLSIDFromProgID(lpszProgID: win32more.Foundation.PWSTR, lpclsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def StringFromGUID2(rguid: POINTER(Guid), lpsz: win32more.Foundation.PWSTR, cchMax: Int32) -> Int32: ...
@winfunctype('OLE32.dll')
def CoCreateGuid(pguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoWaitForMultipleHandles(dwFlags: UInt32, dwTimeout: UInt32, cHandles: UInt32, pHandles: POINTER(win32more.Foundation.HANDLE), lpdwindex: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoWaitForMultipleObjects(dwFlags: UInt32, dwTimeout: UInt32, cHandles: UInt32, pHandles: POINTER(win32more.Foundation.HANDLE), lpdwindex: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoGetTreatAsClass(clsidOld: POINTER(Guid), pClsidNew: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoInvalidateRemoteMachineBindings(pszMachineName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoTaskMemAlloc(cb: UIntPtr) -> c_void_p: ...
@winfunctype('OLE32.dll')
def CoTaskMemRealloc(pv: c_void_p, cb: UIntPtr) -> c_void_p: ...
@winfunctype('OLE32.dll')
def CoTaskMemFree(pv: c_void_p) -> Void: ...
@winfunctype('OLE32.dll')
def CoRegisterDeviceCatalog(deviceInstanceId: win32more.Foundation.PWSTR, cookie: POINTER(win32more.System.Com.CO_DEVICE_CATALOG_COOKIE)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def CoRevokeDeviceCatalog(cookie: win32more.System.Com.CO_DEVICE_CATALOG_COOKIE) -> win32more.Foundation.HRESULT: ...
@winfunctype('URLMON.dll')
def CreateUri(pwzURI: win32more.Foundation.PWSTR, dwFlags: win32more.System.Com.URI_CREATE_FLAGS, dwReserved: UIntPtr, ppURI: POINTER(win32more.System.Com.IUri_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('URLMON.dll')
def CreateUriWithFragment(pwzURI: win32more.Foundation.PWSTR, pwzFragment: win32more.Foundation.PWSTR, dwFlags: UInt32, dwReserved: UIntPtr, ppURI: POINTER(win32more.System.Com.IUri_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CreateUriFromMultiByteString(pszANSIInputUri: win32more.Foundation.PSTR, dwEncodingFlags: UInt32, dwCodePage: UInt32, dwCreateFlags: UInt32, dwReserved: UIntPtr, ppUri: POINTER(win32more.System.Com.IUri_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('URLMON.dll')
def CreateIUriBuilder(pIUri: win32more.System.Com.IUri_head, dwFlags: UInt32, dwReserved: UIntPtr, ppIUriBuilder: POINTER(win32more.System.Com.IUriBuilder_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SetErrorInfo(dwReserved: UInt32, perrinfo: win32more.System.Com.IErrorInfo_head) -> win32more.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def GetErrorInfo(dwReserved: UInt32, pperrinfo: POINTER(win32more.System.Com.IErrorInfo_head)) -> win32more.Foundation.HRESULT: ...
ApplicationType = Int32
ApplicationType_ServerApplication: ApplicationType = 0
ApplicationType_LibraryApplication: ApplicationType = 1
class AsyncIAdviseSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000150-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Begin_OnDataChange(pFormatetc: POINTER(win32more.System.Com.FORMATETC_head), pStgmed: POINTER(win32more.System.Com.STGMEDIUM_head)) -> Void: ...
    @commethod(4)
    def Finish_OnDataChange() -> Void: ...
    @commethod(5)
    def Begin_OnViewChange(dwAspect: UInt32, lindex: Int32) -> Void: ...
    @commethod(6)
    def Finish_OnViewChange() -> Void: ...
    @commethod(7)
    def Begin_OnRename(pmk: win32more.System.Com.IMoniker_head) -> Void: ...
    @commethod(8)
    def Finish_OnRename() -> Void: ...
    @commethod(9)
    def Begin_OnSave() -> Void: ...
    @commethod(10)
    def Finish_OnSave() -> Void: ...
    @commethod(11)
    def Begin_OnClose() -> Void: ...
    @commethod(12)
    def Finish_OnClose() -> Void: ...
class AsyncIAdviseSink2(c_void_p):
    extends: win32more.System.Com.AsyncIAdviseSink
    Guid = Guid('00000151-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(13)
    def Begin_OnLinkSrcChange(pmk: win32more.System.Com.IMoniker_head) -> Void: ...
    @commethod(14)
    def Finish_OnLinkSrcChange() -> Void: ...
class AsyncIMultiQI(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('000e0020-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Begin_QueryMultipleInterfaces(cMQIs: UInt32, pMQIs: POINTER(win32more.System.Com.MULTI_QI_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_QueryMultipleInterfaces(pMQIs: POINTER(win32more.System.Com.MULTI_QI_head)) -> win32more.Foundation.HRESULT: ...
class AsyncIPipeByte(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('db2f3acb-2f86-11d1-8e-04-00-c0-4f-b9-98-9a')
    @commethod(3)
    def Begin_Pull(cRequest: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_Pull(buf: c_char_p_no, pcReturned: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_Push(buf: c_char_p_no, cSent: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_Push() -> win32more.Foundation.HRESULT: ...
class AsyncIPipeDouble(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('db2f3acf-2f86-11d1-8e-04-00-c0-4f-b9-98-9a')
    @commethod(3)
    def Begin_Pull(cRequest: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_Pull(buf: POINTER(Double), pcReturned: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_Push(buf: POINTER(Double), cSent: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_Push() -> win32more.Foundation.HRESULT: ...
class AsyncIPipeLong(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('db2f3acd-2f86-11d1-8e-04-00-c0-4f-b9-98-9a')
    @commethod(3)
    def Begin_Pull(cRequest: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_Pull(buf: POINTER(Int32), pcReturned: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_Push(buf: POINTER(Int32), cSent: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_Push() -> win32more.Foundation.HRESULT: ...
class AsyncIUnknown(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('000e0000-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Begin_QueryInterface(riid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Finish_QueryInterface(ppvObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Begin_AddRef() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Finish_AddRef() -> UInt32: ...
    @commethod(7)
    def Begin_Release() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Finish_Release() -> UInt32: ...
class BINDINFO(Structure):
    cbSize: UInt32
    szExtraInfo: win32more.Foundation.PWSTR
    stgmedData: win32more.System.Com.STGMEDIUM
    grfBindInfoF: UInt32
    dwBindVerb: UInt32
    szCustomVerb: win32more.Foundation.PWSTR
    cbstgmedData: UInt32
    dwOptions: UInt32
    dwOptionsFlags: UInt32
    dwCodePage: UInt32
    securityAttributes: win32more.Security.SECURITY_ATTRIBUTES
    iid: Guid
    pUnk: win32more.System.Com.IUnknown_head
    dwReserved: UInt32
BINDINFOF = Int32
BINDINFOF_URLENCODESTGMEDDATA: BINDINFOF = 1
BINDINFOF_URLENCODEDEXTRAINFO: BINDINFOF = 2
class BINDPTR(Union):
    lpfuncdesc: POINTER(win32more.System.Com.FUNCDESC_head)
    lpvardesc: POINTER(win32more.System.Com.VARDESC_head)
    lptcomp: win32more.System.Com.ITypeComp_head
BIND_FLAGS = Int32
BIND_MAYBOTHERUSER: BIND_FLAGS = 1
BIND_JUSTTESTEXISTENCE: BIND_FLAGS = 2
class BIND_OPTS(Structure):
    cbStruct: UInt32
    grfFlags: UInt32
    grfMode: UInt32
    dwTickCountDeadline: UInt32
class BIND_OPTS2(Structure):
    Base: win32more.System.Com.BIND_OPTS
    dwTrackFlags: UInt32
    dwClassContext: UInt32
    locale: UInt32
    pServerInfo: POINTER(win32more.System.Com.COSERVERINFO_head)
class BIND_OPTS3(Structure):
    Base: win32more.System.Com.BIND_OPTS2
    hwnd: win32more.Foundation.HWND
class BLOB(Structure):
    cbSize: UInt32
    pBlobData: c_char_p_no
class BYTE_BLOB(Structure):
    clSize: UInt32
    abData: Byte * 1
class BYTE_SIZEDARR(Structure):
    clSize: UInt32
    pData: c_char_p_no
CALLCONV = Int32
CC_FASTCALL: CALLCONV = 0
CC_CDECL: CALLCONV = 1
CC_MSCPASCAL: CALLCONV = 2
CC_PASCAL: CALLCONV = 2
CC_MACPASCAL: CALLCONV = 3
CC_STDCALL: CALLCONV = 4
CC_FPFASTCALL: CALLCONV = 5
CC_SYSCALL: CALLCONV = 6
CC_MPWCDECL: CALLCONV = 7
CC_MPWPASCAL: CALLCONV = 8
CC_MAX: CALLCONV = 9
CALLTYPE = Int32
CALLTYPE_TOPLEVEL: CALLTYPE = 1
CALLTYPE_NESTED: CALLTYPE = 2
CALLTYPE_ASYNC: CALLTYPE = 3
CALLTYPE_TOPLEVEL_CALLPENDING: CALLTYPE = 4
CALLTYPE_ASYNC_CALLPENDING: CALLTYPE = 5
class CATEGORYINFO(Structure):
    catid: Guid
    lcid: UInt32
    szDescription: Char * 128
CLSCTX = UInt32
CLSCTX_INPROC_SERVER: CLSCTX = 1
CLSCTX_INPROC_HANDLER: CLSCTX = 2
CLSCTX_LOCAL_SERVER: CLSCTX = 4
CLSCTX_INPROC_SERVER16: CLSCTX = 8
CLSCTX_REMOTE_SERVER: CLSCTX = 16
CLSCTX_INPROC_HANDLER16: CLSCTX = 32
CLSCTX_RESERVED1: CLSCTX = 64
CLSCTX_RESERVED2: CLSCTX = 128
CLSCTX_RESERVED3: CLSCTX = 256
CLSCTX_RESERVED4: CLSCTX = 512
CLSCTX_NO_CODE_DOWNLOAD: CLSCTX = 1024
CLSCTX_RESERVED5: CLSCTX = 2048
CLSCTX_NO_CUSTOM_MARSHAL: CLSCTX = 4096
CLSCTX_ENABLE_CODE_DOWNLOAD: CLSCTX = 8192
CLSCTX_NO_FAILURE_LOG: CLSCTX = 16384
CLSCTX_DISABLE_AAA: CLSCTX = 32768
CLSCTX_ENABLE_AAA: CLSCTX = 65536
CLSCTX_FROM_DEFAULT_CONTEXT: CLSCTX = 131072
CLSCTX_ACTIVATE_X86_SERVER: CLSCTX = 262144
CLSCTX_ACTIVATE_32_BIT_SERVER: CLSCTX = 262144
CLSCTX_ACTIVATE_64_BIT_SERVER: CLSCTX = 524288
CLSCTX_ENABLE_CLOAKING: CLSCTX = 1048576
CLSCTX_APPCONTAINER: CLSCTX = 4194304
CLSCTX_ACTIVATE_AAA_AS_IU: CLSCTX = 8388608
CLSCTX_RESERVED6: CLSCTX = 16777216
CLSCTX_ACTIVATE_ARM32_SERVER: CLSCTX = 33554432
CLSCTX_PS_DLL: CLSCTX = 2147483648
CLSCTX_ALL: CLSCTX = 23
CLSCTX_SERVER: CLSCTX = 21
class COAUTHIDENTITY(Structure):
    User: POINTER(UInt16)
    UserLength: UInt32
    Domain: POINTER(UInt16)
    DomainLength: UInt32
    Password: POINTER(UInt16)
    PasswordLength: UInt32
    Flags: UInt32
class COAUTHINFO(Structure):
    dwAuthnSvc: UInt32
    dwAuthzSvc: UInt32
    pwszServerPrincName: win32more.Foundation.PWSTR
    dwAuthnLevel: UInt32
    dwImpersonationLevel: UInt32
    pAuthIdentityData: POINTER(win32more.System.Com.COAUTHIDENTITY_head)
    dwCapabilities: UInt32
COINIT = UInt32
COINIT_APARTMENTTHREADED: COINIT = 2
COINIT_MULTITHREADED: COINIT = 0
COINIT_DISABLE_OLE1DDE: COINIT = 4
COINIT_SPEED_OVER_MEMORY: COINIT = 8
COINITBASE = Int32
COINITBASE_MULTITHREADED: COINITBASE = 0
COMSD = Int32
SD_LAUNCHPERMISSIONS: COMSD = 0
SD_ACCESSPERMISSIONS: COMSD = 1
SD_LAUNCHRESTRICTIONS: COMSD = 2
SD_ACCESSRESTRICTIONS: COMSD = 3
class CONNECTDATA(Structure):
    pUnk: win32more.System.Com.IUnknown_head
    dwCookie: UInt32
class COSERVERINFO(Structure):
    dwReserved1: UInt32
    pwszName: win32more.Foundation.PWSTR
    pAuthInfo: POINTER(win32more.System.Com.COAUTHINFO_head)
    dwReserved2: UInt32
COWAIT_FLAGS = Int32
COWAIT_DEFAULT: COWAIT_FLAGS = 0
COWAIT_WAITALL: COWAIT_FLAGS = 1
COWAIT_ALERTABLE: COWAIT_FLAGS = 2
COWAIT_INPUTAVAILABLE: COWAIT_FLAGS = 4
COWAIT_DISPATCH_CALLS: COWAIT_FLAGS = 8
COWAIT_DISPATCH_WINDOW_MESSAGES: COWAIT_FLAGS = 16
CO_DEVICE_CATALOG_COOKIE = IntPtr
CO_MARSHALING_CONTEXT_ATTRIBUTES = Int32
CO_MARSHALING_SOURCE_IS_APP_CONTAINER: CO_MARSHALING_CONTEXT_ATTRIBUTES = 0
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_1: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483648
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_2: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483647
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_3: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483646
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_4: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483645
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_5: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483644
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_6: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483643
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_7: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483642
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_8: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483641
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_9: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483640
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_10: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483639
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_11: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483638
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_12: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483637
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_13: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483636
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_14: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483635
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_15: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483634
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_16: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483633
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_17: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483632
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_18: CO_MARSHALING_CONTEXT_ATTRIBUTES = -2147483631
CO_MTA_USAGE_COOKIE = IntPtr
class CSPLATFORM(Structure):
    dwPlatformId: UInt32
    dwVersionHi: UInt32
    dwVersionLo: UInt32
    dwProcessorArch: UInt32
class CUSTDATA(Structure):
    cCustData: UInt32
    prgCustData: POINTER(win32more.System.Com.CUSTDATAITEM_head)
class CUSTDATAITEM(Structure):
    guid: Guid
    varValue: win32more.System.Com.VARIANT
CWMO_FLAGS = Int32
CWMO_DEFAULT: CWMO_FLAGS = 0
CWMO_DISPATCH_CALLS: CWMO_FLAGS = 1
CWMO_DISPATCH_WINDOW_MESSAGES: CWMO_FLAGS = 2
class CY(Union):
    Anonymous: _Anonymous_e__Struct
    int64: Int64
    class _Anonymous_e__Struct(Structure):
        Lo: UInt32
        Hi: Int32
class ComCallData(Structure):
    dwDispid: UInt32
    dwReserved: UInt32
    pUserDefined: c_void_p
DATADIR = Int32
DATADIR_GET: DATADIR = 1
DATADIR_SET: DATADIR = 2
DCOM_CALL_STATE = Int32
DCOM_NONE: DCOM_CALL_STATE = 0
DCOM_CALL_COMPLETE: DCOM_CALL_STATE = 1
DCOM_CALL_CANCELED: DCOM_CALL_STATE = 2
DESCKIND = Int32
DESCKIND_NONE: DESCKIND = 0
DESCKIND_FUNCDESC: DESCKIND = 1
DESCKIND_VARDESC: DESCKIND = 2
DESCKIND_TYPECOMP: DESCKIND = 3
DESCKIND_IMPLICITAPPOBJ: DESCKIND = 4
DESCKIND_MAX: DESCKIND = 5
DISPATCH_FLAGS = UInt16
DISPATCH_METHOD: DISPATCH_FLAGS = 1
DISPATCH_PROPERTYGET: DISPATCH_FLAGS = 2
DISPATCH_PROPERTYPUT: DISPATCH_FLAGS = 4
DISPATCH_PROPERTYPUTREF: DISPATCH_FLAGS = 8
class DISPPARAMS(Structure):
    rgvarg: POINTER(win32more.System.Com.VARIANT_head)
    rgdispidNamedArgs: POINTER(Int32)
    cArgs: UInt32
    cNamedArgs: UInt32
DVASPECT = UInt32
DVASPECT_CONTENT: DVASPECT = 1
DVASPECT_THUMBNAIL: DVASPECT = 2
DVASPECT_ICON: DVASPECT = 4
DVASPECT_DOCPRINT: DVASPECT = 8
DVASPECT_OPAQUE: DVASPECT = 16
DVASPECT_TRANSPARENT: DVASPECT = 32
class DVTARGETDEVICE(Structure):
    tdSize: UInt32
    tdDriverNameOffset: UInt16
    tdDeviceNameOffset: UInt16
    tdPortNameOffset: UInt16
    tdExtDevmodeOffset: UInt16
    tdData: Byte * 1
class DWORD_BLOB(Structure):
    clSize: UInt32
    alData: UInt32 * 1
class DWORD_SIZEDARR(Structure):
    clSize: UInt32
    pData: POINTER(UInt32)
class ELEMDESC(Structure):
    tdesc: win32more.System.Com.TYPEDESC
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        idldesc: win32more.System.Com.IDLDESC
        paramdesc: win32more.System.Ole.PARAMDESC
EOLE_AUTHENTICATION_CAPABILITIES = Int32
EOAC_NONE: EOLE_AUTHENTICATION_CAPABILITIES = 0
EOAC_MUTUAL_AUTH: EOLE_AUTHENTICATION_CAPABILITIES = 1
EOAC_STATIC_CLOAKING: EOLE_AUTHENTICATION_CAPABILITIES = 32
EOAC_DYNAMIC_CLOAKING: EOLE_AUTHENTICATION_CAPABILITIES = 64
EOAC_ANY_AUTHORITY: EOLE_AUTHENTICATION_CAPABILITIES = 128
EOAC_MAKE_FULLSIC: EOLE_AUTHENTICATION_CAPABILITIES = 256
EOAC_DEFAULT: EOLE_AUTHENTICATION_CAPABILITIES = 2048
EOAC_SECURE_REFS: EOLE_AUTHENTICATION_CAPABILITIES = 2
EOAC_ACCESS_CONTROL: EOLE_AUTHENTICATION_CAPABILITIES = 4
EOAC_APPID: EOLE_AUTHENTICATION_CAPABILITIES = 8
EOAC_DYNAMIC: EOLE_AUTHENTICATION_CAPABILITIES = 16
EOAC_REQUIRE_FULLSIC: EOLE_AUTHENTICATION_CAPABILITIES = 512
EOAC_AUTO_IMPERSONATE: EOLE_AUTHENTICATION_CAPABILITIES = 1024
EOAC_DISABLE_AAA: EOLE_AUTHENTICATION_CAPABILITIES = 4096
EOAC_NO_CUSTOM_MARSHAL: EOLE_AUTHENTICATION_CAPABILITIES = 8192
EOAC_RESERVED1: EOLE_AUTHENTICATION_CAPABILITIES = 16384
class EXCEPINFO(Structure):
    wCode: UInt16
    wReserved: UInt16
    bstrSource: win32more.Foundation.BSTR
    bstrDescription: win32more.Foundation.BSTR
    bstrHelpFile: win32more.Foundation.BSTR
    dwHelpContext: UInt32
    pvReserved: c_void_p
    pfnDeferredFillIn: win32more.System.Com.LPEXCEPFINO_DEFERRED_FILLIN
    scode: Int32
EXTCONN = Int32
EXTCONN_STRONG: EXTCONN = 1
EXTCONN_WEAK: EXTCONN = 2
EXTCONN_CALLABLE: EXTCONN = 4
class FLAGGED_BYTE_BLOB(Structure):
    fFlags: UInt32
    clSize: UInt32
    abData: Byte * 1
class FLAGGED_WORD_BLOB(Structure):
    fFlags: UInt32
    clSize: UInt32
    asData: UInt16 * 1
class FLAG_STGMEDIUM(Structure):
    ContextFlags: Int32
    fPassOwnership: Int32
    Stgmed: win32more.System.Com.STGMEDIUM
class FORMATETC(Structure):
    cfFormat: UInt16
    ptd: POINTER(win32more.System.Com.DVTARGETDEVICE_head)
    dwAspect: UInt32
    lindex: Int32
    tymed: UInt32
class FUNCDESC(Structure):
    memid: Int32
    lprgscode: POINTER(Int32)
    lprgelemdescParam: POINTER(win32more.System.Com.ELEMDESC_head)
    funckind: win32more.System.Com.FUNCKIND
    invkind: win32more.System.Com.INVOKEKIND
    callconv: win32more.System.Com.CALLCONV
    cParams: Int16
    cParamsOpt: Int16
    oVft: Int16
    cScodes: Int16
    elemdescFunc: win32more.System.Com.ELEMDESC
    wFuncFlags: win32more.System.Com.FUNCFLAGS
FUNCFLAGS = UInt16
FUNCFLAG_FRESTRICTED: FUNCFLAGS = 1
FUNCFLAG_FSOURCE: FUNCFLAGS = 2
FUNCFLAG_FBINDABLE: FUNCFLAGS = 4
FUNCFLAG_FREQUESTEDIT: FUNCFLAGS = 8
FUNCFLAG_FDISPLAYBIND: FUNCFLAGS = 16
FUNCFLAG_FDEFAULTBIND: FUNCFLAGS = 32
FUNCFLAG_FHIDDEN: FUNCFLAGS = 64
FUNCFLAG_FUSESGETLASTERROR: FUNCFLAGS = 128
FUNCFLAG_FDEFAULTCOLLELEM: FUNCFLAGS = 256
FUNCFLAG_FUIDEFAULT: FUNCFLAGS = 512
FUNCFLAG_FNONBROWSABLE: FUNCFLAGS = 1024
FUNCFLAG_FREPLACEABLE: FUNCFLAGS = 2048
FUNCFLAG_FIMMEDIATEBIND: FUNCFLAGS = 4096
FUNCKIND = Int32
FUNC_VIRTUAL: FUNCKIND = 0
FUNC_PUREVIRTUAL: FUNCKIND = 1
FUNC_NONVIRTUAL: FUNCKIND = 2
FUNC_STATIC: FUNCKIND = 3
FUNC_DISPATCH: FUNCKIND = 4
class GDI_OBJECT(Structure):
    ObjectType: UInt32
    u: _u_e__Struct
    class _u_e__Struct(Union):
        hBitmap: POINTER(win32more.System.SystemServices.userHBITMAP_head)
        hPalette: POINTER(win32more.System.SystemServices.userHPALETTE_head)
        hGeneric: POINTER(win32more.System.SystemServices.userHGLOBAL_head)
GLOBALOPT_EH_VALUES = Int32
COMGLB_EXCEPTION_HANDLE: GLOBALOPT_EH_VALUES = 0
COMGLB_EXCEPTION_DONOT_HANDLE_FATAL: GLOBALOPT_EH_VALUES = 1
COMGLB_EXCEPTION_DONOT_HANDLE: GLOBALOPT_EH_VALUES = 1
COMGLB_EXCEPTION_DONOT_HANDLE_ANY: GLOBALOPT_EH_VALUES = 2
GLOBALOPT_PROPERTIES = Int32
COMGLB_EXCEPTION_HANDLING: GLOBALOPT_PROPERTIES = 1
COMGLB_APPID: GLOBALOPT_PROPERTIES = 2
COMGLB_RPC_THREADPOOL_SETTING: GLOBALOPT_PROPERTIES = 3
COMGLB_RO_SETTINGS: GLOBALOPT_PROPERTIES = 4
COMGLB_UNMARSHALING_POLICY: GLOBALOPT_PROPERTIES = 5
COMGLB_PROPERTIES_RESERVED1: GLOBALOPT_PROPERTIES = 6
COMGLB_PROPERTIES_RESERVED2: GLOBALOPT_PROPERTIES = 7
COMGLB_PROPERTIES_RESERVED3: GLOBALOPT_PROPERTIES = 8
GLOBALOPT_RO_FLAGS = Int32
COMGLB_STA_MODALLOOP_REMOVE_TOUCH_MESSAGES: GLOBALOPT_RO_FLAGS = 1
COMGLB_STA_MODALLOOP_SHARED_QUEUE_REMOVE_INPUT_MESSAGES: GLOBALOPT_RO_FLAGS = 2
COMGLB_STA_MODALLOOP_SHARED_QUEUE_DONOT_REMOVE_INPUT_MESSAGES: GLOBALOPT_RO_FLAGS = 4
COMGLB_FAST_RUNDOWN: GLOBALOPT_RO_FLAGS = 8
COMGLB_RESERVED1: GLOBALOPT_RO_FLAGS = 16
COMGLB_RESERVED2: GLOBALOPT_RO_FLAGS = 32
COMGLB_RESERVED3: GLOBALOPT_RO_FLAGS = 64
COMGLB_STA_MODALLOOP_SHARED_QUEUE_REORDER_POINTER_MESSAGES: GLOBALOPT_RO_FLAGS = 128
COMGLB_RESERVED4: GLOBALOPT_RO_FLAGS = 256
COMGLB_RESERVED5: GLOBALOPT_RO_FLAGS = 512
COMGLB_RESERVED6: GLOBALOPT_RO_FLAGS = 1024
GLOBALOPT_RPCTP_VALUES = Int32
COMGLB_RPC_THREADPOOL_SETTING_DEFAULT_POOL: GLOBALOPT_RPCTP_VALUES = 0
COMGLB_RPC_THREADPOOL_SETTING_PRIVATE_POOL: GLOBALOPT_RPCTP_VALUES = 1
GLOBALOPT_UNMARSHALING_POLICY_VALUES = Int32
COMGLB_UNMARSHALING_POLICY_NORMAL: GLOBALOPT_UNMARSHALING_POLICY_VALUES = 0
COMGLB_UNMARSHALING_POLICY_STRONG: GLOBALOPT_UNMARSHALING_POLICY_VALUES = 1
COMGLB_UNMARSHALING_POLICY_HYBRID: GLOBALOPT_UNMARSHALING_POLICY_VALUES = 2
class HYPER_SIZEDARR(Structure):
    clSize: UInt32
    pData: POINTER(Int64)
class IActivationFilter(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000017-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def HandleActivation(dwActivationType: UInt32, rclsid: POINTER(Guid), pReplacementClsId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IAddrExclusionControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000148-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetCurrentAddrExclusionList(riid: POINTER(Guid), ppEnumerator: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateAddrExclusionList(pEnumerator: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
class IAddrTrackingControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000147-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def EnableCOMDynamicAddrTracking() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def DisableCOMDynamicAddrTracking() -> win32more.Foundation.HRESULT: ...
class IAdviseSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0000010f-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def OnDataChange(pFormatetc: POINTER(win32more.System.Com.FORMATETC_head), pStgmed: POINTER(win32more.System.Com.STGMEDIUM_head)) -> Void: ...
    @commethod(4)
    def OnViewChange(dwAspect: UInt32, lindex: Int32) -> Void: ...
    @commethod(5)
    def OnRename(pmk: win32more.System.Com.IMoniker_head) -> Void: ...
    @commethod(6)
    def OnSave() -> Void: ...
    @commethod(7)
    def OnClose() -> Void: ...
class IAdviseSink2(c_void_p):
    extends: win32more.System.Com.IAdviseSink
    Guid = Guid('00000125-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(8)
    def OnLinkSrcChange(pmk: win32more.System.Com.IMoniker_head) -> Void: ...
class IAgileObject(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('94ea2b94-e9cc-49e0-c0-ff-ee-64-ca-8f-5b-90')
class IAsyncManager(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0000002a-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def CompleteCall(Result: win32more.Foundation.HRESULT) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCallContext(riid: POINTER(Guid), pInterface: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetState(pulStateFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IAsyncRpcChannelBuffer(c_void_p):
    extends: win32more.System.Com.IRpcChannelBuffer2
    Guid = Guid('a5029fb6-3c34-11d1-9c-99-00-c0-4f-b9-98-aa')
    @commethod(9)
    def Send(pMsg: POINTER(win32more.System.Com.RPCOLEMESSAGE_head), pSync: win32more.System.Com.ISynchronize_head, pulStatus: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Receive(pMsg: POINTER(win32more.System.Com.RPCOLEMESSAGE_head), pulStatus: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetDestCtxEx(pMsg: POINTER(win32more.System.Com.RPCOLEMESSAGE_head), pdwDestContext: POINTER(UInt32), ppvDestContext: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IAuthenticate(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('79eac9d0-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def Authenticate(phwnd: POINTER(win32more.Foundation.HWND), pszUsername: POINTER(win32more.Foundation.PWSTR), pszPassword: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class IAuthenticateEx(c_void_p):
    extends: win32more.System.Com.IAuthenticate
    Guid = Guid('2ad1edaf-d83d-48b5-9a-df-03-db-e1-9f-53-bd')
    @commethod(4)
    def AuthenticateEx(phwnd: POINTER(win32more.Foundation.HWND), pszUsername: POINTER(win32more.Foundation.PWSTR), pszPassword: POINTER(win32more.Foundation.PWSTR), pauthinfo: POINTER(win32more.System.Com.AUTHENTICATEINFO_head)) -> win32more.Foundation.HRESULT: ...
class IBindCtx(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0000000e-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def RegisterObjectBound(punk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RevokeObjectBound(punk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ReleaseBoundObjects() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetBindOptions(pbindopts: POINTER(win32more.System.Com.BIND_OPTS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetBindOptions(pbindopts: POINTER(win32more.System.Com.BIND_OPTS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRunningObjectTable(pprot: POINTER(win32more.System.Com.IRunningObjectTable_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def RegisterObjectParam(pszKey: win32more.Foundation.PWSTR, punk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetObjectParam(pszKey: win32more.Foundation.PWSTR, ppunk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def EnumObjectParam(ppenum: POINTER(win32more.System.Com.IEnumString_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def RevokeObjectParam(pszKey: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IBindHost(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fc4801a1-2ba9-11cf-a2-29-00-aa-00-3d-73-52')
    @commethod(3)
    def CreateMoniker(szName: win32more.Foundation.PWSTR, pBC: win32more.System.Com.IBindCtx_head, ppmk: POINTER(win32more.System.Com.IMoniker_head), dwReserved: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def MonikerBindToStorage(pMk: win32more.System.Com.IMoniker_head, pBC: win32more.System.Com.IBindCtx_head, pBSC: win32more.System.Com.IBindStatusCallback_head, riid: POINTER(Guid), ppvObj: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def MonikerBindToObject(pMk: win32more.System.Com.IMoniker_head, pBC: win32more.System.Com.IBindCtx_head, pBSC: win32more.System.Com.IBindStatusCallback_head, riid: POINTER(Guid), ppvObj: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IBindStatusCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('79eac9c1-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def OnStartBinding(dwReserved: UInt32, pib: win32more.System.Com.IBinding_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPriority(pnPriority: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def OnLowResource(reserved: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def OnProgress(ulProgress: UInt32, ulProgressMax: UInt32, ulStatusCode: UInt32, szStatusText: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OnStopBinding(hresult: win32more.Foundation.HRESULT, szError: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetBindInfo(grfBINDF: POINTER(UInt32), pbindinfo: POINTER(win32more.System.Com.BINDINFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def OnDataAvailable(grfBSCF: UInt32, dwSize: UInt32, pformatetc: POINTER(win32more.System.Com.FORMATETC_head), pstgmed: POINTER(win32more.System.Com.STGMEDIUM_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def OnObjectAvailable(riid: POINTER(Guid), punk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
class IBindStatusCallbackEx(c_void_p):
    extends: win32more.System.Com.IBindStatusCallback
    Guid = Guid('aaa74ef9-8ee7-4659-88-d9-f8-c5-04-da-73-cc')
    @commethod(11)
    def GetBindInfoEx(grfBINDF: POINTER(UInt32), pbindinfo: POINTER(win32more.System.Com.BINDINFO_head), grfBINDF2: POINTER(UInt32), pdwReserved: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IBinding(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('79eac9c0-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def Abort() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Suspend() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Resume() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetPriority(nPriority: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetPriority(pnPriority: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetBindResult(pclsidProtocol: POINTER(Guid), pdwResult: POINTER(UInt32), pszResult: POINTER(win32more.Foundation.PWSTR), pdwReserved: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IBlockingLock(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('30f3d47a-6447-11d1-8e-3c-00-c0-4f-b9-38-6d')
    @commethod(3)
    def Lock(dwTimeout: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Unlock() -> win32more.Foundation.HRESULT: ...
class ICallFactory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1c733a30-2a1c-11ce-ad-e5-00-aa-00-44-77-3d')
    @commethod(3)
    def CreateCall(riid: POINTER(Guid), pCtrlUnk: win32more.System.Com.IUnknown_head, riid2: POINTER(Guid), ppv: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class ICancelMethodCalls(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000029-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Cancel(ulSeconds: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def TestCancel() -> win32more.Foundation.HRESULT: ...
class ICatInformation(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0002e013-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def EnumCategories(lcid: UInt32, ppenumCategoryInfo: POINTER(win32more.System.Com.IEnumCATEGORYINFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCategoryDesc(rcatid: POINTER(Guid), lcid: UInt32, pszDesc: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnumClassesOfCategories(cImplemented: UInt32, rgcatidImpl: POINTER(Guid), cRequired: UInt32, rgcatidReq: POINTER(Guid), ppenumClsid: POINTER(win32more.System.Com.IEnumGUID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def IsClassOfCategories(rclsid: POINTER(Guid), cImplemented: UInt32, rgcatidImpl: POINTER(Guid), cRequired: UInt32, rgcatidReq: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def EnumImplCategoriesOfClass(rclsid: POINTER(Guid), ppenumCatid: POINTER(win32more.System.Com.IEnumGUID_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def EnumReqCategoriesOfClass(rclsid: POINTER(Guid), ppenumCatid: POINTER(win32more.System.Com.IEnumGUID_head)) -> win32more.Foundation.HRESULT: ...
class ICatRegister(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0002e012-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def RegisterCategories(cCategories: UInt32, rgCategoryInfo: POINTER(win32more.System.Com.CATEGORYINFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnRegisterCategories(cCategories: UInt32, rgcatid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterClassImplCategories(rclsid: POINTER(Guid), cCategories: UInt32, rgcatid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def UnRegisterClassImplCategories(rclsid: POINTER(Guid), cCategories: UInt32, rgcatid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def RegisterClassReqCategories(rclsid: POINTER(Guid), cCategories: UInt32, rgcatid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def UnRegisterClassReqCategories(rclsid: POINTER(Guid), cCategories: UInt32, rgcatid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IChannelHook(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1008c4a0-7613-11cf-9a-f1-00-20-af-6e-72-f4')
    @commethod(3)
    def ClientGetSize(uExtent: POINTER(Guid), riid: POINTER(Guid), pDataSize: POINTER(UInt32)) -> Void: ...
    @commethod(4)
    def ClientFillBuffer(uExtent: POINTER(Guid), riid: POINTER(Guid), pDataSize: POINTER(UInt32), pDataBuffer: c_void_p) -> Void: ...
    @commethod(5)
    def ClientNotify(uExtent: POINTER(Guid), riid: POINTER(Guid), cbDataSize: UInt32, pDataBuffer: c_void_p, lDataRep: UInt32, hrFault: win32more.Foundation.HRESULT) -> Void: ...
    @commethod(6)
    def ServerNotify(uExtent: POINTER(Guid), riid: POINTER(Guid), cbDataSize: UInt32, pDataBuffer: c_void_p, lDataRep: UInt32) -> Void: ...
    @commethod(7)
    def ServerGetSize(uExtent: POINTER(Guid), riid: POINTER(Guid), hrFault: win32more.Foundation.HRESULT, pDataSize: POINTER(UInt32)) -> Void: ...
    @commethod(8)
    def ServerFillBuffer(uExtent: POINTER(Guid), riid: POINTER(Guid), pDataSize: POINTER(UInt32), pDataBuffer: c_void_p, hrFault: win32more.Foundation.HRESULT) -> Void: ...
class IClassActivator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000140-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetClassObject(rclsid: POINTER(Guid), dwClassContext: UInt32, locale: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IClassFactory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000001-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def CreateInstance(pUnkOuter: win32more.System.Com.IUnknown_head, riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def LockServer(fLock: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IClientSecurity(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0000013d-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def QueryBlanket(pProxy: win32more.System.Com.IUnknown_head, pAuthnSvc: POINTER(UInt32), pAuthzSvc: POINTER(UInt32), pServerPrincName: POINTER(POINTER(UInt16)), pAuthnLevel: POINTER(win32more.System.Com.RPC_C_AUTHN_LEVEL), pImpLevel: POINTER(win32more.System.Com.RPC_C_IMP_LEVEL), pAuthInfo: POINTER(c_void_p), pCapabilites: POINTER(win32more.System.Com.EOLE_AUTHENTICATION_CAPABILITIES)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetBlanket(pProxy: win32more.System.Com.IUnknown_head, dwAuthnSvc: UInt32, dwAuthzSvc: UInt32, pServerPrincName: win32more.Foundation.PWSTR, dwAuthnLevel: win32more.System.Com.RPC_C_AUTHN_LEVEL, dwImpLevel: win32more.System.Com.RPC_C_IMP_LEVEL, pAuthInfo: c_void_p, dwCapabilities: win32more.System.Com.EOLE_AUTHENTICATION_CAPABILITIES) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CopyProxy(pProxy: win32more.System.Com.IUnknown_head, ppCopy: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IComThreadingInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('000001ce-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetCurrentApartmentType(pAptType: POINTER(win32more.System.Com.APTTYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentThreadType(pThreadType: POINTER(win32more.System.Com.THDTYPE)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrentLogicalThreadId(pguidLogicalThreadId: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetCurrentLogicalThreadId(rguid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IConnectionPoint(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b196b286-bab4-101a-b6-9c-00-aa-00-34-1d-07')
    @commethod(3)
    def GetConnectionInterface(pIID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetConnectionPointContainer(ppCPC: POINTER(win32more.System.Com.IConnectionPointContainer_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Advise(pUnkSink: win32more.System.Com.IUnknown_head, pdwCookie: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Unadvise(dwCookie: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def EnumConnections(ppEnum: POINTER(win32more.System.Com.IEnumConnections_head)) -> win32more.Foundation.HRESULT: ...
class IConnectionPointContainer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b196b284-bab4-101a-b6-9c-00-aa-00-34-1d-07')
    @commethod(3)
    def EnumConnectionPoints(ppEnum: POINTER(win32more.System.Com.IEnumConnectionPoints_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def FindConnectionPoint(riid: POINTER(Guid), ppCP: POINTER(win32more.System.Com.IConnectionPoint_head)) -> win32more.Foundation.HRESULT: ...
class IContext(Structure):
    pass
class IContextCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('000001da-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def ContextCallback(pfnCallback: win32more.System.Com.PFNCONTEXTCALL, pParam: POINTER(win32more.System.Com.ComCallData_head), riid: POINTER(Guid), iMethod: Int32, pUnk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
class IDLDESC(Structure):
    dwReserved: UIntPtr
    wIDLFlags: win32more.System.Com.IDLFLAGS
IDLFLAGS = UInt16
IDLFLAG_NONE: IDLFLAGS = 0
IDLFLAG_FIN: IDLFLAGS = 1
IDLFLAG_FOUT: IDLFLAGS = 2
IDLFLAG_FLCID: IDLFLAGS = 4
IDLFLAG_FRETVAL: IDLFLAGS = 8
class IDataAdviseHolder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000110-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Advise(pDataObject: win32more.System.Com.IDataObject_head, pFetc: POINTER(win32more.System.Com.FORMATETC_head), advf: UInt32, pAdvise: win32more.System.Com.IAdviseSink_head, pdwConnection: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Unadvise(dwConnection: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def EnumAdvise(ppenumAdvise: POINTER(win32more.System.Com.IEnumSTATDATA_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SendOnDataChange(pDataObject: win32more.System.Com.IDataObject_head, dwReserved: UInt32, advf: UInt32) -> win32more.Foundation.HRESULT: ...
class IDataObject(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0000010e-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetData(pformatetcIn: POINTER(win32more.System.Com.FORMATETC_head), pmedium: POINTER(win32more.System.Com.STGMEDIUM_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetDataHere(pformatetc: POINTER(win32more.System.Com.FORMATETC_head), pmedium: POINTER(win32more.System.Com.STGMEDIUM_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def QueryGetData(pformatetc: POINTER(win32more.System.Com.FORMATETC_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCanonicalFormatEtc(pformatectIn: POINTER(win32more.System.Com.FORMATETC_head), pformatetcOut: POINTER(win32more.System.Com.FORMATETC_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetData(pformatetc: POINTER(win32more.System.Com.FORMATETC_head), pmedium: POINTER(win32more.System.Com.STGMEDIUM_head), fRelease: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def EnumFormatEtc(dwDirection: UInt32, ppenumFormatEtc: POINTER(win32more.System.Com.IEnumFORMATETC_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def DAdvise(pformatetc: POINTER(win32more.System.Com.FORMATETC_head), advf: UInt32, pAdvSink: win32more.System.Com.IAdviseSink_head, pdwConnection: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def DUnadvise(dwConnection: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def EnumDAdvise(ppenumAdvise: POINTER(win32more.System.Com.IEnumSTATDATA_head)) -> win32more.Foundation.HRESULT: ...
class IDispatch(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00020400-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetTypeInfoCount(pctinfo: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetTypeInfo(iTInfo: UInt32, lcid: UInt32, ppTInfo: POINTER(win32more.System.Com.ITypeInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetIDsOfNames(riid: POINTER(Guid), rgszNames: POINTER(win32more.Foundation.PWSTR), cNames: UInt32, lcid: UInt32, rgDispId: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Invoke(dispIdMember: Int32, riid: POINTER(Guid), lcid: UInt32, wFlags: win32more.System.Com.DISPATCH_FLAGS, pDispParams: POINTER(win32more.System.Com.DISPPARAMS_head), pVarResult: POINTER(win32more.System.Com.VARIANT_head), pExcepInfo: POINTER(win32more.System.Com.EXCEPINFO_head), puArgErr: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IEnumCATEGORYINFO(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0002e011-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.System.Com.CATEGORYINFO_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.System.Com.IEnumCATEGORYINFO_head)) -> win32more.Foundation.HRESULT: ...
class IEnumConnectionPoints(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b196b285-bab4-101a-b6-9c-00-aa-00-34-1d-07')
    @commethod(3)
    def Next(cConnections: UInt32, ppCP: POINTER(win32more.System.Com.IConnectionPoint_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cConnections: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.System.Com.IEnumConnectionPoints_head)) -> win32more.Foundation.HRESULT: ...
class IEnumConnections(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b196b287-bab4-101a-b6-9c-00-aa-00-34-1d-07')
    @commethod(3)
    def Next(cConnections: UInt32, rgcd: POINTER(win32more.System.Com.CONNECTDATA_head), pcFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cConnections: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.System.Com.IEnumConnections_head)) -> win32more.Foundation.HRESULT: ...
class IEnumContextProps(Structure):
    pass
class IEnumFORMATETC(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000103-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.System.Com.FORMATETC_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.System.Com.IEnumFORMATETC_head)) -> win32more.Foundation.HRESULT: ...
class IEnumGUID(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0002e000-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Guid), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.System.Com.IEnumGUID_head)) -> win32more.Foundation.HRESULT: ...
class IEnumMoniker(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000102-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.System.Com.IMoniker_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.System.Com.IEnumMoniker_head)) -> win32more.Foundation.HRESULT: ...
class IEnumSTATDATA(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000105-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.System.Com.STATDATA_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.System.Com.IEnumSTATDATA_head)) -> win32more.Foundation.HRESULT: ...
class IEnumString(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000101-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.Foundation.PWSTR), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.System.Com.IEnumString_head)) -> win32more.Foundation.HRESULT: ...
class IEnumUnknown(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000100-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(win32more.System.Com.IUnknown_head), pceltFetched: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(win32more.System.Com.IEnumUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IErrorInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1cf2b120-547d-101b-8e-65-08-00-2b-2b-d1-19')
    @commethod(3)
    def GetGUID(pGUID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetSource(pBstrSource: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDescription(pBstrDescription: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetHelpFile(pBstrHelpFile: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetHelpContext(pdwHelpContext: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IErrorLog(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3127ca40-446e-11ce-81-35-00-aa-00-4b-b8-51')
    @commethod(3)
    def AddError(pszPropName: win32more.Foundation.PWSTR, pExcepInfo: POINTER(win32more.System.Com.EXCEPINFO_head)) -> win32more.Foundation.HRESULT: ...
class IExternalConnection(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000019-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def AddConnection(extconn: UInt32, reserved: UInt32) -> UInt32: ...
    @commethod(4)
    def ReleaseConnection(extconn: UInt32, reserved: UInt32, fLastReleaseCloses: win32more.Foundation.BOOL) -> UInt32: ...
class IFastRundown(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000040-0000-0000-c0-00-00-00-00-00-00-46')
class IForegroundTransfer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000145-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def AllowForegroundTransfer(lpvReserved: c_void_p) -> win32more.Foundation.HRESULT: ...
class IGlobalInterfaceTable(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000146-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def RegisterInterfaceInGlobal(pUnk: win32more.System.Com.IUnknown_head, riid: POINTER(Guid), pdwCookie: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RevokeInterfaceFromGlobal(dwCookie: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetInterfaceFromGlobal(dwCookie: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IGlobalOptions(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0000015b-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Set(dwProperty: win32more.System.Com.GLOBALOPT_PROPERTIES, dwValue: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Query(dwProperty: win32more.System.Com.GLOBALOPT_PROPERTIES, pdwValue: POINTER(UIntPtr)) -> win32more.Foundation.HRESULT: ...
class IInitializeSpy(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000034-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def PreInitialize(dwCoInit: UInt32, dwCurThreadAptRefs: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def PostInitialize(hrCoInit: win32more.Foundation.HRESULT, dwCoInit: UInt32, dwNewThreadAptRefs: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def PreUninitialize(dwCurThreadAptRefs: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def PostUninitialize(dwNewThreadAptRefs: UInt32) -> win32more.Foundation.HRESULT: ...
class IInternalUnknown(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000021-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def QueryInternalInterface(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
IMPLTYPEFLAGS = Int32
IMPLTYPEFLAG_FDEFAULT: IMPLTYPEFLAGS = 1
IMPLTYPEFLAG_FSOURCE: IMPLTYPEFLAGS = 2
IMPLTYPEFLAG_FRESTRICTED: IMPLTYPEFLAGS = 4
IMPLTYPEFLAG_FDEFAULTVTABLE: IMPLTYPEFLAGS = 8
class IMachineGlobalObjectTable(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('26d709ac-f70b-4421-a9-6f-d2-87-8f-af-b0-0d')
    @commethod(3)
    def RegisterObject(clsid: POINTER(Guid), identifier: win32more.Foundation.PWSTR, object: win32more.System.Com.IUnknown_head, token: POINTER(POINTER(win32more.System.Com.MachineGlobalObjectTableRegistrationToken___head))) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetObject(clsid: POINTER(Guid), identifier: win32more.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RevokeObject(token: POINTER(win32more.System.Com.MachineGlobalObjectTableRegistrationToken___head)) -> win32more.Foundation.HRESULT: ...
class IMalloc(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000002-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Alloc(cb: UIntPtr) -> c_void_p: ...
    @commethod(4)
    def Realloc(pv: c_void_p, cb: UIntPtr) -> c_void_p: ...
    @commethod(5)
    def Free(pv: c_void_p) -> Void: ...
    @commethod(6)
    def GetSize(pv: c_void_p) -> UIntPtr: ...
    @commethod(7)
    def DidAlloc(pv: c_void_p) -> Int32: ...
    @commethod(8)
    def HeapMinimize() -> Void: ...
class IMallocSpy(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0000001d-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def PreAlloc(cbRequest: UIntPtr) -> UIntPtr: ...
    @commethod(4)
    def PostAlloc(pActual: c_void_p) -> c_void_p: ...
    @commethod(5)
    def PreFree(pRequest: c_void_p, fSpyed: win32more.Foundation.BOOL) -> c_void_p: ...
    @commethod(6)
    def PostFree(fSpyed: win32more.Foundation.BOOL) -> Void: ...
    @commethod(7)
    def PreRealloc(pRequest: c_void_p, cbRequest: UIntPtr, ppNewRequest: POINTER(c_void_p), fSpyed: win32more.Foundation.BOOL) -> UIntPtr: ...
    @commethod(8)
    def PostRealloc(pActual: c_void_p, fSpyed: win32more.Foundation.BOOL) -> c_void_p: ...
    @commethod(9)
    def PreGetSize(pRequest: c_void_p, fSpyed: win32more.Foundation.BOOL) -> c_void_p: ...
    @commethod(10)
    def PostGetSize(cbActual: UIntPtr, fSpyed: win32more.Foundation.BOOL) -> UIntPtr: ...
    @commethod(11)
    def PreDidAlloc(pRequest: c_void_p, fSpyed: win32more.Foundation.BOOL) -> c_void_p: ...
    @commethod(12)
    def PostDidAlloc(pRequest: c_void_p, fSpyed: win32more.Foundation.BOOL, fActual: Int32) -> Int32: ...
    @commethod(13)
    def PreHeapMinimize() -> Void: ...
    @commethod(14)
    def PostHeapMinimize() -> Void: ...
class IMoniker(c_void_p):
    extends: win32more.System.Com.IPersistStream
    Guid = Guid('0000000f-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(8)
    def BindToObject(pbc: win32more.System.Com.IBindCtx_head, pmkToLeft: win32more.System.Com.IMoniker_head, riidResult: POINTER(Guid), ppvResult: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def BindToStorage(pbc: win32more.System.Com.IBindCtx_head, pmkToLeft: win32more.System.Com.IMoniker_head, riid: POINTER(Guid), ppvObj: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Reduce(pbc: win32more.System.Com.IBindCtx_head, dwReduceHowFar: UInt32, ppmkToLeft: POINTER(win32more.System.Com.IMoniker_head), ppmkReduced: POINTER(win32more.System.Com.IMoniker_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def ComposeWith(pmkRight: win32more.System.Com.IMoniker_head, fOnlyIfNotGeneric: win32more.Foundation.BOOL, ppmkComposite: POINTER(win32more.System.Com.IMoniker_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Enum(fForward: win32more.Foundation.BOOL, ppenumMoniker: POINTER(win32more.System.Com.IEnumMoniker_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def IsEqual(pmkOtherMoniker: win32more.System.Com.IMoniker_head) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Hash(pdwHash: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def IsRunning(pbc: win32more.System.Com.IBindCtx_head, pmkToLeft: win32more.System.Com.IMoniker_head, pmkNewlyRunning: win32more.System.Com.IMoniker_head) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetTimeOfLastChange(pbc: win32more.System.Com.IBindCtx_head, pmkToLeft: win32more.System.Com.IMoniker_head, pFileTime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def Inverse(ppmk: POINTER(win32more.System.Com.IMoniker_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def CommonPrefixWith(pmkOther: win32more.System.Com.IMoniker_head, ppmkPrefix: POINTER(win32more.System.Com.IMoniker_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def RelativePathTo(pmkOther: win32more.System.Com.IMoniker_head, ppmkRelPath: POINTER(win32more.System.Com.IMoniker_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetDisplayName(pbc: win32more.System.Com.IBindCtx_head, pmkToLeft: win32more.System.Com.IMoniker_head, ppszDisplayName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def ParseDisplayName(pbc: win32more.System.Com.IBindCtx_head, pmkToLeft: win32more.System.Com.IMoniker_head, pszDisplayName: win32more.Foundation.PWSTR, pchEaten: POINTER(UInt32), ppmkOut: POINTER(win32more.System.Com.IMoniker_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def IsSystemMoniker(pdwMksys: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IMultiQI(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000020-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def QueryMultipleInterfaces(cMQIs: UInt32, pMQIs: POINTER(win32more.System.Com.MULTI_QI_head)) -> win32more.Foundation.HRESULT: ...
class INTERFACEINFO(Structure):
    pUnk: win32more.System.Com.IUnknown_head
    iid: Guid
    wMethod: UInt16
INVOKEKIND = Int32
INVOKE_FUNC: INVOKEKIND = 1
INVOKE_PROPERTYGET: INVOKEKIND = 2
INVOKE_PROPERTYPUT: INVOKEKIND = 4
INVOKE_PROPERTYPUTREF: INVOKEKIND = 8
class INoMarshal(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ecc8691b-c1db-4dc0-85-5e-65-f6-c5-51-af-49')
class IOplockStorage(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8d19c834-8879-11d1-83-e9-00-c0-4f-c2-c6-d4')
    @commethod(3)
    def CreateStorageEx(pwcsName: win32more.Foundation.PWSTR, grfMode: UInt32, stgfmt: UInt32, grfAttrs: UInt32, riid: POINTER(Guid), ppstgOpen: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OpenStorageEx(pwcsName: win32more.Foundation.PWSTR, grfMode: UInt32, stgfmt: UInt32, grfAttrs: UInt32, riid: POINTER(Guid), ppstgOpen: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IPSFactoryBuffer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d5f569d0-593b-101a-b5-69-08-00-2b-2d-bf-7a')
    @commethod(3)
    def CreateProxy(pUnkOuter: win32more.System.Com.IUnknown_head, riid: POINTER(Guid), ppProxy: POINTER(win32more.System.Com.IRpcProxyBuffer_head), ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreateStub(riid: POINTER(Guid), pUnkServer: win32more.System.Com.IUnknown_head, ppStub: POINTER(win32more.System.Com.IRpcStubBuffer_head)) -> win32more.Foundation.HRESULT: ...
class IPersist(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0000010c-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetClassID(pClassID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IPersistFile(c_void_p):
    extends: win32more.System.Com.IPersist
    Guid = Guid('0000010b-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(4)
    def IsDirty() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Load(pszFileName: win32more.Foundation.PWSTR, dwMode: win32more.System.Com.STGM) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Save(pszFileName: win32more.Foundation.PWSTR, fRemember: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SaveCompleted(pszFileName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetCurFile(ppszFileName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
class IPersistMemory(c_void_p):
    extends: win32more.System.Com.IPersist
    Guid = Guid('bd1ae5e0-a6ae-11ce-bd-37-50-42-00-c1-00-00')
    @commethod(4)
    def IsDirty() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Load(pMem: c_void_p, cbSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Save(pMem: c_void_p, fClearDirty: win32more.Foundation.BOOL, cbSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetSizeMax(pCbSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def InitNew() -> win32more.Foundation.HRESULT: ...
class IPersistStream(c_void_p):
    extends: win32more.System.Com.IPersist
    Guid = Guid('00000109-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(4)
    def IsDirty() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Load(pStm: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Save(pStm: win32more.System.Com.IStream_head, fClearDirty: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetSizeMax(pcbSize: POINTER(win32more.Foundation.ULARGE_INTEGER_head)) -> win32more.Foundation.HRESULT: ...
class IPersistStreamInit(c_void_p):
    extends: win32more.System.Com.IPersist
    Guid = Guid('7fd52380-4e07-101b-ae-2d-08-00-2b-2e-c7-13')
    @commethod(4)
    def IsDirty() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Load(pStm: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Save(pStm: win32more.System.Com.IStream_head, fClearDirty: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetSizeMax(pCbSize: POINTER(win32more.Foundation.ULARGE_INTEGER_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def InitNew() -> win32more.Foundation.HRESULT: ...
class IPipeByte(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('db2f3aca-2f86-11d1-8e-04-00-c0-4f-b9-98-9a')
    @commethod(3)
    def Pull(buf: c_char_p_no, cRequest: UInt32, pcReturned: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Push(buf: c_char_p_no, cSent: UInt32) -> win32more.Foundation.HRESULT: ...
class IPipeDouble(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('db2f3ace-2f86-11d1-8e-04-00-c0-4f-b9-98-9a')
    @commethod(3)
    def Pull(buf: POINTER(Double), cRequest: UInt32, pcReturned: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Push(buf: POINTER(Double), cSent: UInt32) -> win32more.Foundation.HRESULT: ...
class IPipeLong(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('db2f3acc-2f86-11d1-8e-04-00-c0-4f-b9-98-9a')
    @commethod(3)
    def Pull(buf: POINTER(Int32), cRequest: UInt32, pcReturned: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Push(buf: POINTER(Int32), cSent: UInt32) -> win32more.Foundation.HRESULT: ...
class IProcessInitControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('72380d55-8d2b-43a3-85-13-2b-6e-f3-14-34-e9')
    @commethod(3)
    def ResetInitializerTimeout(dwSecondsRemaining: UInt32) -> win32more.Foundation.HRESULT: ...
class IProcessLock(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('000001d5-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def AddRefOnProcess() -> UInt32: ...
    @commethod(4)
    def ReleaseRefOnProcess() -> UInt32: ...
class IProgressNotify(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a9d758a0-4617-11cf-95-fc-00-aa-00-68-0d-b4')
    @commethod(3)
    def OnProgress(dwProgressCurrent: UInt32, dwProgressMaximum: UInt32, fAccurate: win32more.Foundation.BOOL, fOwner: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IROTData(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f29f6bc0-5021-11ce-aa-15-00-00-69-01-29-3f')
    @commethod(3)
    def GetComparisonData(pbData: c_char_p_no, cbMax: UInt32, pcbData: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IReleaseMarshalBuffers(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('eb0cb9e8-7996-11d2-87-2e-00-00-f8-08-08-59')
    @commethod(3)
    def ReleaseMarshalBuffer(pMsg: POINTER(win32more.System.Com.RPCOLEMESSAGE_head), dwFlags: UInt32, pChnl: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
class IRpcChannelBuffer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d5f56b60-593b-101a-b5-69-08-00-2b-2d-bf-7a')
    @commethod(3)
    def GetBuffer(pMessage: POINTER(win32more.System.Com.RPCOLEMESSAGE_head), riid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SendReceive(pMessage: POINTER(win32more.System.Com.RPCOLEMESSAGE_head), pStatus: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def FreeBuffer(pMessage: POINTER(win32more.System.Com.RPCOLEMESSAGE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetDestCtx(pdwDestContext: POINTER(UInt32), ppvDestContext: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def IsConnected() -> win32more.Foundation.HRESULT: ...
class IRpcChannelBuffer2(c_void_p):
    extends: win32more.System.Com.IRpcChannelBuffer
    Guid = Guid('594f31d0-7f19-11d0-b1-94-00-a0-c9-0d-c8-bf')
    @commethod(8)
    def GetProtocolVersion(pdwVersion: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IRpcChannelBuffer3(c_void_p):
    extends: win32more.System.Com.IRpcChannelBuffer2
    Guid = Guid('25b15600-0115-11d0-bf-0d-00-aa-00-b8-df-d2')
    @commethod(9)
    def Send(pMsg: POINTER(win32more.System.Com.RPCOLEMESSAGE_head), pulStatus: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Receive(pMsg: POINTER(win32more.System.Com.RPCOLEMESSAGE_head), ulSize: UInt32, pulStatus: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Cancel(pMsg: POINTER(win32more.System.Com.RPCOLEMESSAGE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetCallContext(pMsg: POINTER(win32more.System.Com.RPCOLEMESSAGE_head), riid: POINTER(Guid), pInterface: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetDestCtxEx(pMsg: POINTER(win32more.System.Com.RPCOLEMESSAGE_head), pdwDestContext: POINTER(UInt32), ppvDestContext: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetState(pMsg: POINTER(win32more.System.Com.RPCOLEMESSAGE_head), pState: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def RegisterAsync(pMsg: POINTER(win32more.System.Com.RPCOLEMESSAGE_head), pAsyncMgr: win32more.System.Com.IAsyncManager_head) -> win32more.Foundation.HRESULT: ...
class IRpcHelper(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000149-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetDCOMProtocolVersion(pComVersion: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetIIDFromOBJREF(pObjRef: c_void_p, piid: POINTER(POINTER(Guid))) -> win32more.Foundation.HRESULT: ...
class IRpcOptions(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000144-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Set(pPrx: win32more.System.Com.IUnknown_head, dwProperty: win32more.System.Com.RPCOPT_PROPERTIES, dwValue: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Query(pPrx: win32more.System.Com.IUnknown_head, dwProperty: win32more.System.Com.RPCOPT_PROPERTIES, pdwValue: POINTER(UIntPtr)) -> win32more.Foundation.HRESULT: ...
class IRpcProxyBuffer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d5f56a34-593b-101a-b5-69-08-00-2b-2d-bf-7a')
    @commethod(3)
    def Connect(pRpcChannelBuffer: win32more.System.Com.IRpcChannelBuffer_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Disconnect() -> Void: ...
class IRpcStubBuffer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d5f56afc-593b-101a-b5-69-08-00-2b-2d-bf-7a')
    @commethod(3)
    def Connect(pUnkServer: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Disconnect() -> Void: ...
    @commethod(5)
    def Invoke(_prpcmsg: POINTER(win32more.System.Com.RPCOLEMESSAGE_head), _pRpcChannelBuffer: win32more.System.Com.IRpcChannelBuffer_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def IsIIDSupported(riid: POINTER(Guid)) -> win32more.System.Com.IRpcStubBuffer_head: ...
    @commethod(7)
    def CountRefs() -> UInt32: ...
    @commethod(8)
    def DebugServerQueryInterface(ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def DebugServerRelease(pv: c_void_p) -> Void: ...
class IRpcSyntaxNegotiate(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('58a08519-24c8-4935-b4-82-3f-d8-23-33-3a-4f')
    @commethod(3)
    def NegotiateSyntax(pMsg: POINTER(win32more.System.Com.RPCOLEMESSAGE_head)) -> win32more.Foundation.HRESULT: ...
class IRunnableObject(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000126-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetRunningClass(lpClsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Run(pbc: win32more.System.Com.IBindCtx_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def IsRunning() -> win32more.Foundation.BOOL: ...
    @commethod(6)
    def LockRunning(fLock: win32more.Foundation.BOOL, fLastUnlockCloses: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetContainedObject(fContained: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IRunningObjectTable(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000010-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Register(grfFlags: win32more.System.Com.ROT_FLAGS, punkObject: win32more.System.Com.IUnknown_head, pmkObjectName: win32more.System.Com.IMoniker_head, pdwRegister: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Revoke(dwRegister: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def IsRunning(pmkObjectName: win32more.System.Com.IMoniker_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetObject(pmkObjectName: win32more.System.Com.IMoniker_head, ppunkObject: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def NoteChangeTime(dwRegister: UInt32, pfiletime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTimeOfLastChange(pmkObjectName: win32more.System.Com.IMoniker_head, pfiletime: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def EnumRunning(ppenumMoniker: POINTER(win32more.System.Com.IEnumMoniker_head)) -> win32more.Foundation.HRESULT: ...
class ISequentialStream(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0c733a30-2a1c-11ce-ad-e5-00-aa-00-44-77-3d')
    @commethod(3)
    def Read(pv: c_void_p, cb: UInt32, pcbRead: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Write(pv: c_void_p, cb: UInt32, pcbWritten: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class IServerSecurity(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0000013e-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def QueryBlanket(pAuthnSvc: POINTER(UInt32), pAuthzSvc: POINTER(UInt32), pServerPrincName: POINTER(POINTER(UInt16)), pAuthnLevel: POINTER(UInt32), pImpLevel: POINTER(UInt32), pPrivs: POINTER(c_void_p), pCapabilities: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ImpersonateClient() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def RevertToSelf() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def IsImpersonating() -> win32more.Foundation.BOOL: ...
class IServiceProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6d5140c1-7436-11ce-80-34-00-aa-00-60-09-fa')
    @commethod(3)
    def QueryService(guidService: POINTER(Guid), riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IStdMarshalInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000018-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetClassForHandler(dwDestContext: UInt32, pvDestContext: c_void_p, pClsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class IStream(c_void_p):
    extends: win32more.System.Com.ISequentialStream
    Guid = Guid('0000000c-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(5)
    def Seek(dlibMove: win32more.Foundation.LARGE_INTEGER, dwOrigin: win32more.System.Com.STREAM_SEEK, plibNewPosition: POINTER(win32more.Foundation.ULARGE_INTEGER_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetSize(libNewSize: win32more.Foundation.ULARGE_INTEGER) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def CopyTo(pstm: win32more.System.Com.IStream_head, cb: win32more.Foundation.ULARGE_INTEGER, pcbRead: POINTER(win32more.Foundation.ULARGE_INTEGER_head), pcbWritten: POINTER(win32more.Foundation.ULARGE_INTEGER_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Commit(grfCommitFlags: win32more.System.Com.STGC) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Revert() -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def LockRegion(libOffset: win32more.Foundation.ULARGE_INTEGER, cb: win32more.Foundation.ULARGE_INTEGER, dwLockType: win32more.System.Com.LOCKTYPE) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def UnlockRegion(libOffset: win32more.Foundation.ULARGE_INTEGER, cb: win32more.Foundation.ULARGE_INTEGER, dwLockType: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Stat(pstatstg: POINTER(win32more.System.Com.STATSTG_head), grfStatFlag: win32more.System.Com.STATFLAG) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Clone(ppstm: POINTER(win32more.System.Com.IStream_head)) -> win32more.Foundation.HRESULT: ...
class ISupportErrorInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('df0b3d60-548f-101b-8e-65-08-00-2b-2b-d1-19')
    @commethod(3)
    def InterfaceSupportsErrorInfo(riid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
class ISurrogate(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000022-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def LoadDllServer(Clsid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def FreeSurrogate() -> win32more.Foundation.HRESULT: ...
class ISurrogateService(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('000001d4-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Init(rguidProcessID: POINTER(Guid), pProcessLock: win32more.System.Com.IProcessLock_head, pfApplicationAware: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def ApplicationLaunch(rguidApplID: POINTER(Guid), appType: win32more.System.Com.ApplicationType) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ApplicationFree(rguidApplID: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def CatalogRefresh(ulReserved: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ProcessShutdown(shutdownType: win32more.System.Com.ShutdownType) -> win32more.Foundation.HRESULT: ...
class ISynchronize(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000030-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Wait(dwFlags: UInt32, dwMilliseconds: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Signal() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> win32more.Foundation.HRESULT: ...
class ISynchronizeContainer(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000033-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def AddSynchronize(pSync: win32more.System.Com.ISynchronize_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def WaitMultiple(dwFlags: UInt32, dwTimeOut: UInt32, ppSync: POINTER(win32more.System.Com.ISynchronize_head)) -> win32more.Foundation.HRESULT: ...
class ISynchronizeEvent(c_void_p):
    extends: win32more.System.Com.ISynchronizeHandle
    Guid = Guid('00000032-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(4)
    def SetEventHandle(ph: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
class ISynchronizeHandle(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000031-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetHandle(ph: POINTER(win32more.Foundation.HANDLE)) -> win32more.Foundation.HRESULT: ...
class ISynchronizeMutex(c_void_p):
    extends: win32more.System.Com.ISynchronize
    Guid = Guid('00000025-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(6)
    def ReleaseMutex() -> win32more.Foundation.HRESULT: ...
class ITimeAndNoticeControl(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bc0bf6ae-8878-11d1-83-e9-00-c0-4f-c2-c6-d4')
    @commethod(3)
    def SuppressChanges(res1: UInt32, res2: UInt32) -> win32more.Foundation.HRESULT: ...
class ITypeComp(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00020403-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Bind(szName: win32more.Foundation.PWSTR, lHashVal: UInt32, wFlags: UInt16, ppTInfo: POINTER(win32more.System.Com.ITypeInfo_head), pDescKind: POINTER(win32more.System.Com.DESCKIND), pBindPtr: POINTER(win32more.System.Com.BINDPTR_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def BindType(szName: win32more.Foundation.PWSTR, lHashVal: UInt32, ppTInfo: POINTER(win32more.System.Com.ITypeInfo_head), ppTComp: POINTER(win32more.System.Com.ITypeComp_head)) -> win32more.Foundation.HRESULT: ...
class ITypeInfo(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00020401-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetTypeAttr(ppTypeAttr: POINTER(POINTER(win32more.System.Com.TYPEATTR_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetTypeComp(ppTComp: POINTER(win32more.System.Com.ITypeComp_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetFuncDesc(index: UInt32, ppFuncDesc: POINTER(POINTER(win32more.System.Com.FUNCDESC_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetVarDesc(index: UInt32, ppVarDesc: POINTER(POINTER(win32more.System.Com.VARDESC_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetNames(memid: Int32, rgBstrNames: POINTER(win32more.Foundation.BSTR), cMaxNames: UInt32, pcNames: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetRefTypeOfImplType(index: UInt32, pRefType: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetImplTypeFlags(index: UInt32, pImplTypeFlags: POINTER(win32more.System.Com.IMPLTYPEFLAGS)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetIDsOfNames(rgszNames: POINTER(win32more.Foundation.PWSTR), cNames: UInt32, pMemId: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Invoke(pvInstance: c_void_p, memid: Int32, wFlags: win32more.System.Com.DISPATCH_FLAGS, pDispParams: POINTER(win32more.System.Com.DISPPARAMS_head), pVarResult: POINTER(win32more.System.Com.VARIANT_head), pExcepInfo: POINTER(win32more.System.Com.EXCEPINFO_head), puArgErr: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetDocumentation(memid: Int32, pBstrName: POINTER(win32more.Foundation.BSTR), pBstrDocString: POINTER(win32more.Foundation.BSTR), pdwHelpContext: POINTER(UInt32), pBstrHelpFile: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetDllEntry(memid: Int32, invKind: win32more.System.Com.INVOKEKIND, pBstrDllName: POINTER(win32more.Foundation.BSTR), pBstrName: POINTER(win32more.Foundation.BSTR), pwOrdinal: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetRefTypeInfo(hRefType: UInt32, ppTInfo: POINTER(win32more.System.Com.ITypeInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def AddressOfMember(memid: Int32, invKind: win32more.System.Com.INVOKEKIND, ppv: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def CreateInstance(pUnkOuter: win32more.System.Com.IUnknown_head, riid: POINTER(Guid), ppvObj: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetMops(memid: Int32, pBstrMops: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetContainingTypeLib(ppTLib: POINTER(win32more.System.Com.ITypeLib_head), pIndex: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def ReleaseTypeAttr(pTypeAttr: POINTER(win32more.System.Com.TYPEATTR_head)) -> Void: ...
    @commethod(20)
    def ReleaseFuncDesc(pFuncDesc: POINTER(win32more.System.Com.FUNCDESC_head)) -> Void: ...
    @commethod(21)
    def ReleaseVarDesc(pVarDesc: POINTER(win32more.System.Com.VARDESC_head)) -> Void: ...
class ITypeInfo2(c_void_p):
    extends: win32more.System.Com.ITypeInfo
    Guid = Guid('00020412-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(22)
    def GetTypeKind(pTypeKind: POINTER(win32more.System.Com.TYPEKIND)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetTypeFlags(pTypeFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetFuncIndexOfMemId(memid: Int32, invKind: win32more.System.Com.INVOKEKIND, pFuncIndex: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetVarIndexOfMemId(memid: Int32, pVarIndex: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetCustData(guid: POINTER(Guid), pVarVal: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def GetFuncCustData(index: UInt32, guid: POINTER(Guid), pVarVal: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def GetParamCustData(indexFunc: UInt32, indexParam: UInt32, guid: POINTER(Guid), pVarVal: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def GetVarCustData(index: UInt32, guid: POINTER(Guid), pVarVal: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def GetImplTypeCustData(index: UInt32, guid: POINTER(Guid), pVarVal: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def GetDocumentation2(memid: Int32, lcid: UInt32, pbstrHelpString: POINTER(win32more.Foundation.BSTR), pdwHelpStringContext: POINTER(UInt32), pbstrHelpStringDll: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def GetAllCustData(pCustData: POINTER(win32more.System.Com.CUSTDATA_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def GetAllFuncCustData(index: UInt32, pCustData: POINTER(win32more.System.Com.CUSTDATA_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def GetAllParamCustData(indexFunc: UInt32, indexParam: UInt32, pCustData: POINTER(win32more.System.Com.CUSTDATA_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def GetAllVarCustData(index: UInt32, pCustData: POINTER(win32more.System.Com.CUSTDATA_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def GetAllImplTypeCustData(index: UInt32, pCustData: POINTER(win32more.System.Com.CUSTDATA_head)) -> win32more.Foundation.HRESULT: ...
class ITypeLib(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00020402-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetTypeInfoCount() -> UInt32: ...
    @commethod(4)
    def GetTypeInfo(index: UInt32, ppTInfo: POINTER(win32more.System.Com.ITypeInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetTypeInfoType(index: UInt32, pTKind: POINTER(win32more.System.Com.TYPEKIND)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetTypeInfoOfGuid(guid: POINTER(Guid), ppTinfo: POINTER(win32more.System.Com.ITypeInfo_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetLibAttr(ppTLibAttr: POINTER(POINTER(win32more.System.Com.TLIBATTR_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetTypeComp(ppTComp: POINTER(win32more.System.Com.ITypeComp_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetDocumentation(index: Int32, pBstrName: POINTER(win32more.Foundation.BSTR), pBstrDocString: POINTER(win32more.Foundation.BSTR), pdwHelpContext: POINTER(UInt32), pBstrHelpFile: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def IsName(szNameBuf: win32more.Foundation.PWSTR, lHashVal: UInt32, pfName: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def FindName(szNameBuf: win32more.Foundation.PWSTR, lHashVal: UInt32, ppTInfo: POINTER(win32more.System.Com.ITypeInfo_head), rgMemId: POINTER(Int32), pcFound: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def ReleaseTLibAttr(pTLibAttr: POINTER(win32more.System.Com.TLIBATTR_head)) -> Void: ...
class ITypeLib2(c_void_p):
    extends: win32more.System.Com.ITypeLib
    Guid = Guid('00020411-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(13)
    def GetCustData(guid: POINTER(Guid), pVarVal: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetLibStatistics(pcUniqueNames: POINTER(UInt32), pcchUniqueNames: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetDocumentation2(index: Int32, lcid: UInt32, pbstrHelpString: POINTER(win32more.Foundation.BSTR), pdwHelpStringContext: POINTER(UInt32), pbstrHelpStringDll: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetAllCustData(pCustData: POINTER(win32more.System.Com.CUSTDATA_head)) -> win32more.Foundation.HRESULT: ...
class ITypeLibRegistration(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('76a3e735-02df-4a12-98-eb-04-3a-d3-60-0a-f3')
    @commethod(3)
    def GetGuid(pGuid: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetVersion(pVersion: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetLcid(pLcid: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetWin32Path(pWin32Path: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetWin64Path(pWin64Path: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetDisplayName(pDisplayName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetFlags(pFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetHelpDir(pHelpDir: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class ITypeLibRegistrationReader(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ed6a8a2a-b160-4e77-8f-73-aa-74-35-cd-5c-27')
    @commethod(3)
    def EnumTypeLibRegistrations(ppEnumUnknown: POINTER(win32more.System.Com.IEnumUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IUnknown(c_void_p):
    extends: None
    Guid = Guid('00000000-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(0)
    def QueryInterface(riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(1)
    def AddRef() -> UInt32: ...
    @commethod(2)
    def Release() -> UInt32: ...
class IUri(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a39ee748-6a27-4817-a6-f2-13-91-4b-ef-58-90')
    @commethod(3)
    def GetPropertyBSTR(uriProp: win32more.System.Com.Uri_PROPERTY, pbstrProperty: POINTER(win32more.Foundation.BSTR), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyLength(uriProp: win32more.System.Com.Uri_PROPERTY, pcchProperty: POINTER(UInt32), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyDWORD(uriProp: win32more.System.Com.Uri_PROPERTY, pdwProperty: POINTER(UInt32), dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def HasProperty(uriProp: win32more.System.Com.Uri_PROPERTY, pfHasProperty: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetAbsoluteUri(pbstrAbsoluteUri: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetAuthority(pbstrAuthority: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetDisplayUri(pbstrDisplayString: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetDomain(pbstrDomain: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetExtension(pbstrExtension: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetFragment(pbstrFragment: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetHost(pbstrHost: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetPassword(pbstrPassword: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetPath(pbstrPath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetPathAndQuery(pbstrPathAndQuery: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetQuery(pbstrQuery: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetRawUri(pbstrRawUri: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetSchemeName(pbstrSchemeName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetUserInfo(pbstrUserInfo: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetUserName(pbstrUserName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetHostType(pdwHostType: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetPort(pdwPort: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetScheme(pdwScheme: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetZone(pdwZone: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetProperties(pdwFlags: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def IsEqual(pUri: win32more.System.Com.IUri_head, pfEqual: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IUriBuilder(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('4221b2e1-8955-46c0-bd-5b-de-98-97-56-5d-e7')
    @commethod(3)
    def CreateUriSimple(dwAllowEncodingPropertyMask: UInt32, dwReserved: UIntPtr, ppIUri: POINTER(win32more.System.Com.IUri_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreateUri(dwCreateFlags: UInt32, dwAllowEncodingPropertyMask: UInt32, dwReserved: UIntPtr, ppIUri: POINTER(win32more.System.Com.IUri_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CreateUriWithFlags(dwCreateFlags: UInt32, dwUriBuilderFlags: UInt32, dwAllowEncodingPropertyMask: UInt32, dwReserved: UIntPtr, ppIUri: POINTER(win32more.System.Com.IUri_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetIUri(ppIUri: POINTER(win32more.System.Com.IUri_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetIUri(pIUri: win32more.System.Com.IUri_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetFragment(pcchFragment: POINTER(UInt32), ppwzFragment: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetHost(pcchHost: POINTER(UInt32), ppwzHost: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetPassword(pcchPassword: POINTER(UInt32), ppwzPassword: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetPath(pcchPath: POINTER(UInt32), ppwzPath: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetPort(pfHasPort: POINTER(win32more.Foundation.BOOL), pdwPort: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetQuery(pcchQuery: POINTER(UInt32), ppwzQuery: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetSchemeName(pcchSchemeName: POINTER(UInt32), ppwzSchemeName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetUserName(pcchUserName: POINTER(UInt32), ppwzUserName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetFragment(pwzNewValue: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetHost(pwzNewValue: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SetPassword(pwzNewValue: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SetPath(pwzNewValue: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetPort(fHasPort: win32more.Foundation.BOOL, dwNewValue: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def SetQuery(pwzNewValue: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def SetSchemeName(pwzNewValue: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def SetUserName(pwzNewValue: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def RemoveProperties(dwPropertyMask: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def HasBeenModified(pfModified: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
class IUrlMon(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00000026-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def AsyncGetClassBits(rclsid: POINTER(Guid), pszTYPE: win32more.Foundation.PWSTR, pszExt: win32more.Foundation.PWSTR, dwFileVersionMS: UInt32, dwFileVersionLS: UInt32, pszCodeBase: win32more.Foundation.PWSTR, pbc: win32more.System.Com.IBindCtx_head, dwClassContext: UInt32, riid: POINTER(Guid), flags: UInt32) -> win32more.Foundation.HRESULT: ...
class IWaitMultiple(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('0000002b-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def WaitMultiple(timeout: UInt32, pSync: POINTER(win32more.System.Com.ISynchronize_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def AddSynchronize(pSync: win32more.System.Com.ISynchronize_head) -> win32more.Foundation.HRESULT: ...
LOCKTYPE = Int32
LOCK_WRITE: LOCKTYPE = 1
LOCK_EXCLUSIVE: LOCKTYPE = 2
LOCK_ONLYONCE: LOCKTYPE = 4
@winfunctype_pointer
def LPEXCEPFINO_DEFERRED_FILLIN(pExcepInfo: POINTER(win32more.System.Com.EXCEPINFO_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNCANUNLOADNOW() -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNGETCLASSOBJECT(param0: POINTER(Guid), param1: POINTER(Guid), param2: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
MEMCTX = Int32
MEMCTX_TASK: MEMCTX = 1
MEMCTX_SHARED: MEMCTX = 2
MEMCTX_MACSYSTEM: MEMCTX = 3
MEMCTX_UNKNOWN: MEMCTX = -1
MEMCTX_SAME: MEMCTX = -2
MKRREDUCE = Int32
MKRREDUCE_ONE: MKRREDUCE = 196608
MKRREDUCE_TOUSER: MKRREDUCE = 131072
MKRREDUCE_THROUGHUSER: MKRREDUCE = 65536
MKRREDUCE_ALL: MKRREDUCE = 0
MKSYS = Int32
MKSYS_NONE: MKSYS = 0
MKSYS_GENERICCOMPOSITE: MKSYS = 1
MKSYS_FILEMONIKER: MKSYS = 2
MKSYS_ANTIMONIKER: MKSYS = 3
MKSYS_ITEMMONIKER: MKSYS = 4
MKSYS_POINTERMONIKER: MKSYS = 5
MKSYS_CLASSMONIKER: MKSYS = 7
MKSYS_OBJREFMONIKER: MKSYS = 8
MKSYS_SESSIONMONIKER: MKSYS = 9
MKSYS_LUAMONIKER: MKSYS = 10
MSHCTX = Int32
MSHCTX_LOCAL: MSHCTX = 0
MSHCTX_NOSHAREDMEM: MSHCTX = 1
MSHCTX_DIFFERENTMACHINE: MSHCTX = 2
MSHCTX_INPROC: MSHCTX = 3
MSHCTX_CROSSCTX: MSHCTX = 4
MSHCTX_CONTAINER: MSHCTX = 5
MSHLFLAGS = Int32
MSHLFLAGS_NORMAL: MSHLFLAGS = 0
MSHLFLAGS_TABLESTRONG: MSHLFLAGS = 1
MSHLFLAGS_TABLEWEAK: MSHLFLAGS = 2
MSHLFLAGS_NOPING: MSHLFLAGS = 4
MSHLFLAGS_RESERVED1: MSHLFLAGS = 8
MSHLFLAGS_RESERVED2: MSHLFLAGS = 16
MSHLFLAGS_RESERVED3: MSHLFLAGS = 32
MSHLFLAGS_RESERVED4: MSHLFLAGS = 64
class MULTI_QI(Structure):
    pIID: POINTER(Guid)
    pItf: win32more.System.Com.IUnknown_head
    hr: win32more.Foundation.HRESULT
class MachineGlobalObjectTableRegistrationToken__(Structure):
    unused: Int32
PENDINGMSG = Int32
PENDINGMSG_CANCELCALL: PENDINGMSG = 0
PENDINGMSG_WAITNOPROCESS: PENDINGMSG = 1
PENDINGMSG_WAITDEFPROCESS: PENDINGMSG = 2
PENDINGTYPE = Int32
PENDINGTYPE_TOPLEVEL: PENDINGTYPE = 1
PENDINGTYPE_NESTED: PENDINGTYPE = 2
@winfunctype_pointer
def PFNCONTEXTCALL(pParam: POINTER(win32more.System.Com.ComCallData_head)) -> win32more.Foundation.HRESULT: ...
class QUERYCONTEXT(Structure):
    dwContext: UInt32
    Platform: win32more.System.Com.CSPLATFORM
    Locale: UInt32
    dwVersionHi: UInt32
    dwVersionLo: UInt32
REGCLS = Int32
REGCLS_SINGLEUSE: REGCLS = 0
REGCLS_MULTIPLEUSE: REGCLS = 1
REGCLS_MULTI_SEPARATE: REGCLS = 2
REGCLS_SUSPENDED: REGCLS = 4
REGCLS_SURROGATE: REGCLS = 8
REGCLS_AGILE: REGCLS = 16
ROT_FLAGS = UInt32
ROTFLAGS_REGISTRATIONKEEPSALIVE: ROT_FLAGS = 1
ROTFLAGS_ALLOWANYCLIENT: ROT_FLAGS = 2
class RPCOLEMESSAGE(Structure):
    reserved1: c_void_p
    dataRepresentation: UInt32
    Buffer: c_void_p
    cbBuffer: UInt32
    iMethod: UInt32
    reserved2: c_void_p * 5
    rpcFlags: UInt32
RPCOPT_PROPERTIES = Int32
COMBND_RPCTIMEOUT: RPCOPT_PROPERTIES = 1
COMBND_SERVER_LOCALITY: RPCOPT_PROPERTIES = 2
COMBND_RESERVED1: RPCOPT_PROPERTIES = 4
COMBND_RESERVED2: RPCOPT_PROPERTIES = 5
COMBND_RESERVED3: RPCOPT_PROPERTIES = 8
COMBND_RESERVED4: RPCOPT_PROPERTIES = 16
RPCOPT_SERVER_LOCALITY_VALUES = Int32
SERVER_LOCALITY_PROCESS_LOCAL: RPCOPT_SERVER_LOCALITY_VALUES = 0
SERVER_LOCALITY_MACHINE_LOCAL: RPCOPT_SERVER_LOCALITY_VALUES = 1
SERVER_LOCALITY_REMOTE: RPCOPT_SERVER_LOCALITY_VALUES = 2
RPC_C_AUTHN_LEVEL = UInt32
RPC_C_AUTHN_LEVEL_DEFAULT: RPC_C_AUTHN_LEVEL = 0
RPC_C_AUTHN_LEVEL_NONE: RPC_C_AUTHN_LEVEL = 1
RPC_C_AUTHN_LEVEL_CONNECT: RPC_C_AUTHN_LEVEL = 2
RPC_C_AUTHN_LEVEL_CALL: RPC_C_AUTHN_LEVEL = 3
RPC_C_AUTHN_LEVEL_PKT: RPC_C_AUTHN_LEVEL = 4
RPC_C_AUTHN_LEVEL_PKT_INTEGRITY: RPC_C_AUTHN_LEVEL = 5
RPC_C_AUTHN_LEVEL_PKT_PRIVACY: RPC_C_AUTHN_LEVEL = 6
RPC_C_IMP_LEVEL = UInt32
RPC_C_IMP_LEVEL_DEFAULT: RPC_C_IMP_LEVEL = 0
RPC_C_IMP_LEVEL_ANONYMOUS: RPC_C_IMP_LEVEL = 1
RPC_C_IMP_LEVEL_IDENTIFY: RPC_C_IMP_LEVEL = 2
RPC_C_IMP_LEVEL_IMPERSONATE: RPC_C_IMP_LEVEL = 3
RPC_C_IMP_LEVEL_DELEGATE: RPC_C_IMP_LEVEL = 4
class RemSTGMEDIUM(Structure):
    tymed: win32more.System.Com.TYMED
    dwHandleType: UInt32
    pData: UInt32
    pUnkForRelease: UInt32
    cbData: UInt32
    data: Byte * 1
class SAFEARRAY(Structure):
    cDims: UInt16
    fFeatures: win32more.System.Com.ADVANCED_FEATURE_FLAGS
    cbElements: UInt32
    cLocks: UInt32
    pvData: c_void_p
    rgsabound: win32more.System.Com.SAFEARRAYBOUND * 1
class SAFEARRAYBOUND(Structure):
    cElements: UInt32
    lLbound: Int32
class SChannelHookCallInfo(Structure):
    iid: Guid
    cbSize: UInt32
    uCausality: Guid
    dwServerPid: UInt32
    iMethod: UInt32
    pObject: c_void_p
SERVERCALL = Int32
SERVERCALL_ISHANDLED: SERVERCALL = 0
SERVERCALL_REJECTED: SERVERCALL = 1
SERVERCALL_RETRYLATER: SERVERCALL = 2
class SOLE_AUTHENTICATION_INFO(Structure):
    dwAuthnSvc: UInt32
    dwAuthzSvc: UInt32
    pAuthInfo: c_void_p
class SOLE_AUTHENTICATION_LIST(Structure):
    cAuthInfo: UInt32
    aAuthInfo: POINTER(win32more.System.Com.SOLE_AUTHENTICATION_INFO_head)
class SOLE_AUTHENTICATION_SERVICE(Structure):
    dwAuthnSvc: UInt32
    dwAuthzSvc: UInt32
    pPrincipalName: win32more.Foundation.PWSTR
    hr: win32more.Foundation.HRESULT
class STATDATA(Structure):
    formatetc: win32more.System.Com.FORMATETC
    advf: UInt32
    pAdvSink: win32more.System.Com.IAdviseSink_head
    dwConnection: UInt32
STATFLAG = Int32
STATFLAG_DEFAULT: STATFLAG = 0
STATFLAG_NONAME: STATFLAG = 1
STATFLAG_NOOPEN: STATFLAG = 2
class STATSTG(Structure):
    pwcsName: win32more.Foundation.PWSTR
    type: UInt32
    cbSize: win32more.Foundation.ULARGE_INTEGER
    mtime: win32more.Foundation.FILETIME
    ctime: win32more.Foundation.FILETIME
    atime: win32more.Foundation.FILETIME
    grfMode: win32more.System.Com.STGM
    grfLocksSupported: win32more.System.Com.LOCKTYPE
    clsid: Guid
    grfStateBits: UInt32
    reserved: UInt32
STGC = UInt32
STGC_DEFAULT: STGC = 0
STGC_OVERWRITE: STGC = 1
STGC_ONLYIFCURRENT: STGC = 2
STGC_DANGEROUSLYCOMMITMERELYTODISKCACHE: STGC = 4
STGC_CONSOLIDATE: STGC = 8
STGM = UInt32
STGM_DIRECT: STGM = 0
STGM_TRANSACTED: STGM = 65536
STGM_SIMPLE: STGM = 134217728
STGM_READ: STGM = 0
STGM_WRITE: STGM = 1
STGM_READWRITE: STGM = 2
STGM_SHARE_DENY_NONE: STGM = 64
STGM_SHARE_DENY_READ: STGM = 48
STGM_SHARE_DENY_WRITE: STGM = 32
STGM_SHARE_EXCLUSIVE: STGM = 16
STGM_PRIORITY: STGM = 262144
STGM_DELETEONRELEASE: STGM = 67108864
STGM_NOSCRATCH: STGM = 1048576
STGM_CREATE: STGM = 4096
STGM_CONVERT: STGM = 131072
STGM_FAILIFTHERE: STGM = 0
STGM_NOSNAPSHOT: STGM = 2097152
STGM_DIRECT_SWMR: STGM = 4194304
class STGMEDIUM(Structure):
    tymed: win32more.System.Com.TYMED
    Anonymous: _Anonymous_e__Union
    pUnkForRelease: win32more.System.Com.IUnknown_head
    class _Anonymous_e__Union(Union):
        hBitmap: win32more.Graphics.Gdi.HBITMAP
        hMetaFilePict: c_void_p
        hEnhMetaFile: win32more.Graphics.Gdi.HENHMETAFILE
        hGlobal: IntPtr
        lpszFileName: win32more.Foundation.PWSTR
        pstm: win32more.System.Com.IStream_head
        pstg: win32more.System.Com.StructuredStorage.IStorage_head
STGTY = Int32
STGTY_STORAGE: STGTY = 1
STGTY_STREAM: STGTY = 2
STGTY_LOCKBYTES: STGTY = 3
STGTY_PROPERTY: STGTY = 4
STREAM_SEEK = UInt32
STREAM_SEEK_SET: STREAM_SEEK = 0
STREAM_SEEK_CUR: STREAM_SEEK = 1
STREAM_SEEK_END: STREAM_SEEK = 2
SYSKIND = Int32
SYS_WIN16: SYSKIND = 0
SYS_WIN32: SYSKIND = 1
SYS_MAC: SYSKIND = 2
SYS_WIN64: SYSKIND = 3
ShutdownType = Int32
ShutdownType_IdleShutdown: ShutdownType = 0
ShutdownType_ForcedShutdown: ShutdownType = 1
class StorageLayout(Structure):
    LayoutType: UInt32
    pwcsElementName: win32more.Foundation.PWSTR
    cOffset: win32more.Foundation.LARGE_INTEGER
    cBytes: win32more.Foundation.LARGE_INTEGER
THDTYPE = Int32
THDTYPE_BLOCKMESSAGES: THDTYPE = 0
THDTYPE_PROCESSMESSAGES: THDTYPE = 1
class TLIBATTR(Structure):
    guid: Guid
    lcid: UInt32
    syskind: win32more.System.Com.SYSKIND
    wMajorVerNum: UInt16
    wMinorVerNum: UInt16
    wLibFlags: UInt16
TYMED = Int32
TYMED_HGLOBAL: TYMED = 1
TYMED_FILE: TYMED = 2
TYMED_ISTREAM: TYMED = 4
TYMED_ISTORAGE: TYMED = 8
TYMED_GDI: TYMED = 16
TYMED_MFPICT: TYMED = 32
TYMED_ENHMF: TYMED = 64
TYMED_NULL: TYMED = 0
class TYPEATTR(Structure):
    guid: Guid
    lcid: UInt32
    dwReserved: UInt32
    memidConstructor: Int32
    memidDestructor: Int32
    lpstrSchema: win32more.Foundation.PWSTR
    cbSizeInstance: UInt32
    typekind: win32more.System.Com.TYPEKIND
    cFuncs: UInt16
    cVars: UInt16
    cImplTypes: UInt16
    cbSizeVft: UInt16
    cbAlignment: UInt16
    wTypeFlags: UInt16
    wMajorVerNum: UInt16
    wMinorVerNum: UInt16
    tdescAlias: win32more.System.Com.TYPEDESC
    idldescType: win32more.System.Com.IDLDESC
class TYPEDESC(Structure):
    Anonymous: _Anonymous_e__Union
    vt: win32more.System.Com.VARENUM
    class _Anonymous_e__Union(Union):
        lptdesc: POINTER(win32more.System.Com.TYPEDESC_head)
        lpadesc: POINTER(win32more.System.Ole.ARRAYDESC_head)
        hreftype: UInt32
TYPEKIND = Int32
TKIND_ENUM: TYPEKIND = 0
TKIND_RECORD: TYPEKIND = 1
TKIND_MODULE: TYPEKIND = 2
TKIND_INTERFACE: TYPEKIND = 3
TKIND_DISPATCH: TYPEKIND = 4
TKIND_COCLASS: TYPEKIND = 5
TKIND_ALIAS: TYPEKIND = 6
TKIND_UNION: TYPEKIND = 7
TKIND_MAX: TYPEKIND = 8
TYSPEC = Int32
TYSPEC_CLSID: TYSPEC = 0
TYSPEC_FILEEXT: TYSPEC = 1
TYSPEC_MIMETYPE: TYSPEC = 2
TYSPEC_FILENAME: TYSPEC = 3
TYSPEC_PROGID: TYSPEC = 4
TYSPEC_PACKAGENAME: TYSPEC = 5
TYSPEC_OBJECTID: TYSPEC = 6
URI_CREATE_FLAGS = UInt32
Uri_CREATE_ALLOW_RELATIVE: URI_CREATE_FLAGS = 1
Uri_CREATE_ALLOW_IMPLICIT_WILDCARD_SCHEME: URI_CREATE_FLAGS = 2
Uri_CREATE_ALLOW_IMPLICIT_FILE_SCHEME: URI_CREATE_FLAGS = 4
Uri_CREATE_NOFRAG: URI_CREATE_FLAGS = 8
Uri_CREATE_NO_CANONICALIZE: URI_CREATE_FLAGS = 16
Uri_CREATE_CANONICALIZE: URI_CREATE_FLAGS = 256
Uri_CREATE_FILE_USE_DOS_PATH: URI_CREATE_FLAGS = 32
Uri_CREATE_DECODE_EXTRA_INFO: URI_CREATE_FLAGS = 64
Uri_CREATE_NO_DECODE_EXTRA_INFO: URI_CREATE_FLAGS = 128
Uri_CREATE_CRACK_UNKNOWN_SCHEMES: URI_CREATE_FLAGS = 512
Uri_CREATE_NO_CRACK_UNKNOWN_SCHEMES: URI_CREATE_FLAGS = 1024
Uri_CREATE_PRE_PROCESS_HTML_URI: URI_CREATE_FLAGS = 2048
Uri_CREATE_NO_PRE_PROCESS_HTML_URI: URI_CREATE_FLAGS = 4096
Uri_CREATE_IE_SETTINGS: URI_CREATE_FLAGS = 8192
Uri_CREATE_NO_IE_SETTINGS: URI_CREATE_FLAGS = 16384
Uri_CREATE_NO_ENCODE_FORBIDDEN_CHARACTERS: URI_CREATE_FLAGS = 32768
Uri_CREATE_NORMALIZE_INTL_CHARACTERS: URI_CREATE_FLAGS = 65536
Uri_CREATE_CANONICALIZE_ABSOLUTE: URI_CREATE_FLAGS = 131072
Uri_PROPERTY = Int32
Uri_PROPERTY_ABSOLUTE_URI: Uri_PROPERTY = 0
Uri_PROPERTY_STRING_START: Uri_PROPERTY = 0
Uri_PROPERTY_AUTHORITY: Uri_PROPERTY = 1
Uri_PROPERTY_DISPLAY_URI: Uri_PROPERTY = 2
Uri_PROPERTY_DOMAIN: Uri_PROPERTY = 3
Uri_PROPERTY_EXTENSION: Uri_PROPERTY = 4
Uri_PROPERTY_FRAGMENT: Uri_PROPERTY = 5
Uri_PROPERTY_HOST: Uri_PROPERTY = 6
Uri_PROPERTY_PASSWORD: Uri_PROPERTY = 7
Uri_PROPERTY_PATH: Uri_PROPERTY = 8
Uri_PROPERTY_PATH_AND_QUERY: Uri_PROPERTY = 9
Uri_PROPERTY_QUERY: Uri_PROPERTY = 10
Uri_PROPERTY_RAW_URI: Uri_PROPERTY = 11
Uri_PROPERTY_SCHEME_NAME: Uri_PROPERTY = 12
Uri_PROPERTY_USER_INFO: Uri_PROPERTY = 13
Uri_PROPERTY_USER_NAME: Uri_PROPERTY = 14
Uri_PROPERTY_STRING_LAST: Uri_PROPERTY = 14
Uri_PROPERTY_HOST_TYPE: Uri_PROPERTY = 15
Uri_PROPERTY_DWORD_START: Uri_PROPERTY = 15
Uri_PROPERTY_PORT: Uri_PROPERTY = 16
Uri_PROPERTY_SCHEME: Uri_PROPERTY = 17
Uri_PROPERTY_ZONE: Uri_PROPERTY = 18
Uri_PROPERTY_DWORD_LAST: Uri_PROPERTY = 18
class VARDESC(Structure):
    memid: Int32
    lpstrSchema: win32more.Foundation.PWSTR
    Anonymous: _Anonymous_e__Union
    elemdescVar: win32more.System.Com.ELEMDESC
    wVarFlags: win32more.System.Com.VARFLAGS
    varkind: win32more.System.Com.VARKIND
    class _Anonymous_e__Union(Union):
        oInst: UInt32
        lpvarValue: POINTER(win32more.System.Com.VARIANT_head)
VARENUM = UInt16
VT_EMPTY: VARENUM = 0
VT_NULL: VARENUM = 1
VT_I2: VARENUM = 2
VT_I4: VARENUM = 3
VT_R4: VARENUM = 4
VT_R8: VARENUM = 5
VT_CY: VARENUM = 6
VT_DATE: VARENUM = 7
VT_BSTR: VARENUM = 8
VT_DISPATCH: VARENUM = 9
VT_ERROR: VARENUM = 10
VT_BOOL: VARENUM = 11
VT_VARIANT: VARENUM = 12
VT_UNKNOWN: VARENUM = 13
VT_DECIMAL: VARENUM = 14
VT_I1: VARENUM = 16
VT_UI1: VARENUM = 17
VT_UI2: VARENUM = 18
VT_UI4: VARENUM = 19
VT_I8: VARENUM = 20
VT_UI8: VARENUM = 21
VT_INT: VARENUM = 22
VT_UINT: VARENUM = 23
VT_VOID: VARENUM = 24
VT_HRESULT: VARENUM = 25
VT_PTR: VARENUM = 26
VT_SAFEARRAY: VARENUM = 27
VT_CARRAY: VARENUM = 28
VT_USERDEFINED: VARENUM = 29
VT_LPSTR: VARENUM = 30
VT_LPWSTR: VARENUM = 31
VT_RECORD: VARENUM = 36
VT_INT_PTR: VARENUM = 37
VT_UINT_PTR: VARENUM = 38
VT_FILETIME: VARENUM = 64
VT_BLOB: VARENUM = 65
VT_STREAM: VARENUM = 66
VT_STORAGE: VARENUM = 67
VT_STREAMED_OBJECT: VARENUM = 68
VT_STORED_OBJECT: VARENUM = 69
VT_BLOB_OBJECT: VARENUM = 70
VT_CF: VARENUM = 71
VT_CLSID: VARENUM = 72
VT_VERSIONED_STREAM: VARENUM = 73
VT_BSTR_BLOB: VARENUM = 4095
VT_VECTOR: VARENUM = 4096
VT_ARRAY: VARENUM = 8192
VT_BYREF: VARENUM = 16384
VT_RESERVED: VARENUM = 32768
VT_ILLEGAL: VARENUM = 65535
VT_ILLEGALMASKED: VARENUM = 4095
VT_TYPEMASK: VARENUM = 4095
VARFLAGS = UInt16
VARFLAG_FREADONLY: VARFLAGS = 1
VARFLAG_FSOURCE: VARFLAGS = 2
VARFLAG_FBINDABLE: VARFLAGS = 4
VARFLAG_FREQUESTEDIT: VARFLAGS = 8
VARFLAG_FDISPLAYBIND: VARFLAGS = 16
VARFLAG_FDEFAULTBIND: VARFLAGS = 32
VARFLAG_FHIDDEN: VARFLAGS = 64
VARFLAG_FRESTRICTED: VARFLAGS = 128
VARFLAG_FDEFAULTCOLLELEM: VARFLAGS = 256
VARFLAG_FUIDEFAULT: VARFLAGS = 512
VARFLAG_FNONBROWSABLE: VARFLAGS = 1024
VARFLAG_FREPLACEABLE: VARFLAGS = 2048
VARFLAG_FIMMEDIATEBIND: VARFLAGS = 4096
class VARIANT(Structure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        decVal: win32more.Foundation.DECIMAL
        class _Anonymous_e__Struct(Structure):
            vt: win32more.System.Com.VARENUM
            wReserved1: UInt16
            wReserved2: UInt16
            wReserved3: UInt16
            Anonymous: _Anonymous_e__Union
            class _Anonymous_e__Union(Union):
                llVal: Int64
                lVal: Int32
                bVal: Byte
                iVal: Int16
                fltVal: Single
                dblVal: Double
                boolVal: win32more.Foundation.VARIANT_BOOL
                __OBSOLETE__VARIANT_BOOL: win32more.Foundation.VARIANT_BOOL
                scode: Int32
                cyVal: win32more.System.Com.CY
                date: Double
                bstrVal: win32more.Foundation.BSTR
                punkVal: win32more.System.Com.IUnknown_head
                pdispVal: win32more.System.Com.IDispatch_head
                parray: POINTER(win32more.System.Com.SAFEARRAY_head)
                pbVal: c_char_p_no
                piVal: POINTER(Int16)
                plVal: POINTER(Int32)
                pllVal: POINTER(Int64)
                pfltVal: POINTER(Single)
                pdblVal: POINTER(Double)
                pboolVal: POINTER(win32more.Foundation.VARIANT_BOOL)
                __OBSOLETE__VARIANT_PBOOL: POINTER(win32more.Foundation.VARIANT_BOOL)
                pscode: POINTER(Int32)
                pcyVal: POINTER(win32more.System.Com.CY_head)
                pdate: POINTER(Double)
                pbstrVal: POINTER(win32more.Foundation.BSTR)
                ppunkVal: POINTER(win32more.System.Com.IUnknown_head)
                ppdispVal: POINTER(win32more.System.Com.IDispatch_head)
                pparray: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))
                pvarVal: POINTER(win32more.System.Com.VARIANT_head)
                byref: c_void_p
                cVal: win32more.Foundation.CHAR
                uiVal: UInt16
                ulVal: UInt32
                ullVal: UInt64
                intVal: Int32
                uintVal: UInt32
                pdecVal: POINTER(win32more.Foundation.DECIMAL_head)
                pcVal: win32more.Foundation.PSTR
                puiVal: POINTER(UInt16)
                pulVal: POINTER(UInt32)
                pullVal: POINTER(UInt64)
                pintVal: POINTER(Int32)
                puintVal: POINTER(UInt32)
                Anonymous: _Anonymous_e__Struct
                class _Anonymous_e__Struct(Structure):
                    pvRecord: c_void_p
                    pRecInfo: win32more.System.Ole.IRecordInfo_head
VARKIND = Int32
VAR_PERINSTANCE: VARKIND = 0
VAR_STATIC: VARKIND = 1
VAR_CONST: VARKIND = 2
VAR_DISPATCH: VARKIND = 3
class WORD_BLOB(Structure):
    clSize: UInt32
    asData: UInt16 * 1
class WORD_SIZEDARR(Structure):
    clSize: UInt32
    pData: POINTER(UInt16)
class uCLSSPEC(Structure):
    tyspec: UInt32
    tagged_union: _tagged_union_e__Struct
    class _tagged_union_e__Struct(Union):
        clsid: Guid
        pFileExt: win32more.Foundation.PWSTR
        pMimeType: win32more.Foundation.PWSTR
        pProgId: win32more.Foundation.PWSTR
        pFileName: win32more.Foundation.PWSTR
        ByName: _ByName_e__Struct
        ByObjectId: _ByObjectId_e__Struct
        class _ByName_e__Struct(Structure):
            pPackageName: win32more.Foundation.PWSTR
            PolicyId: Guid
        class _ByObjectId_e__Struct(Structure):
            ObjectId: Guid
            PolicyId: Guid
class userFLAG_STGMEDIUM(Structure):
    ContextFlags: Int32
    fPassOwnership: Int32
    Stgmed: win32more.System.Com.userSTGMEDIUM
class userSTGMEDIUM(Structure):
    pUnkForRelease: win32more.System.Com.IUnknown_head
    class _STGMEDIUM_UNION(Structure):
        tymed: UInt32
        u: _u_e__Struct
        class _u_e__Struct(Union):
            hMetaFilePict: POINTER(win32more.System.SystemServices.userHMETAFILEPICT_head)
            hHEnhMetaFile: POINTER(win32more.System.SystemServices.userHENHMETAFILE_head)
            hGdiHandle: POINTER(win32more.System.Com.GDI_OBJECT_head)
            hGlobal: POINTER(win32more.System.SystemServices.userHGLOBAL_head)
            lpszFileName: win32more.Foundation.PWSTR
            pstm: POINTER(win32more.System.Com.BYTE_BLOB_head)
            pstg: POINTER(win32more.System.Com.BYTE_BLOB_head)
make_head(_module, 'AUTHENTICATEINFO')
make_head(_module, 'AsyncIAdviseSink')
make_head(_module, 'AsyncIAdviseSink2')
make_head(_module, 'AsyncIMultiQI')
make_head(_module, 'AsyncIPipeByte')
make_head(_module, 'AsyncIPipeDouble')
make_head(_module, 'AsyncIPipeLong')
make_head(_module, 'AsyncIUnknown')
make_head(_module, 'BINDINFO')
make_head(_module, 'BINDPTR')
make_head(_module, 'BIND_OPTS')
make_head(_module, 'BIND_OPTS2')
make_head(_module, 'BIND_OPTS3')
make_head(_module, 'BLOB')
make_head(_module, 'BYTE_BLOB')
make_head(_module, 'BYTE_SIZEDARR')
make_head(_module, 'CATEGORYINFO')
make_head(_module, 'COAUTHIDENTITY')
make_head(_module, 'COAUTHINFO')
make_head(_module, 'CONNECTDATA')
make_head(_module, 'COSERVERINFO')
make_head(_module, 'CSPLATFORM')
make_head(_module, 'CUSTDATA')
make_head(_module, 'CUSTDATAITEM')
make_head(_module, 'CY')
make_head(_module, 'ComCallData')
make_head(_module, 'DISPPARAMS')
make_head(_module, 'DVTARGETDEVICE')
make_head(_module, 'DWORD_BLOB')
make_head(_module, 'DWORD_SIZEDARR')
make_head(_module, 'ELEMDESC')
make_head(_module, 'EXCEPINFO')
make_head(_module, 'FLAGGED_BYTE_BLOB')
make_head(_module, 'FLAGGED_WORD_BLOB')
make_head(_module, 'FLAG_STGMEDIUM')
make_head(_module, 'FORMATETC')
make_head(_module, 'FUNCDESC')
make_head(_module, 'GDI_OBJECT')
make_head(_module, 'HYPER_SIZEDARR')
make_head(_module, 'IActivationFilter')
make_head(_module, 'IAddrExclusionControl')
make_head(_module, 'IAddrTrackingControl')
make_head(_module, 'IAdviseSink')
make_head(_module, 'IAdviseSink2')
make_head(_module, 'IAgileObject')
make_head(_module, 'IAsyncManager')
make_head(_module, 'IAsyncRpcChannelBuffer')
make_head(_module, 'IAuthenticate')
make_head(_module, 'IAuthenticateEx')
make_head(_module, 'IBindCtx')
make_head(_module, 'IBindHost')
make_head(_module, 'IBindStatusCallback')
make_head(_module, 'IBindStatusCallbackEx')
make_head(_module, 'IBinding')
make_head(_module, 'IBlockingLock')
make_head(_module, 'ICallFactory')
make_head(_module, 'ICancelMethodCalls')
make_head(_module, 'ICatInformation')
make_head(_module, 'ICatRegister')
make_head(_module, 'IChannelHook')
make_head(_module, 'IClassActivator')
make_head(_module, 'IClassFactory')
make_head(_module, 'IClientSecurity')
make_head(_module, 'IComThreadingInfo')
make_head(_module, 'IConnectionPoint')
make_head(_module, 'IConnectionPointContainer')
make_head(_module, 'IContext')
make_head(_module, 'IContextCallback')
make_head(_module, 'IDLDESC')
make_head(_module, 'IDataAdviseHolder')
make_head(_module, 'IDataObject')
make_head(_module, 'IDispatch')
make_head(_module, 'IEnumCATEGORYINFO')
make_head(_module, 'IEnumConnectionPoints')
make_head(_module, 'IEnumConnections')
make_head(_module, 'IEnumContextProps')
make_head(_module, 'IEnumFORMATETC')
make_head(_module, 'IEnumGUID')
make_head(_module, 'IEnumMoniker')
make_head(_module, 'IEnumSTATDATA')
make_head(_module, 'IEnumString')
make_head(_module, 'IEnumUnknown')
make_head(_module, 'IErrorInfo')
make_head(_module, 'IErrorLog')
make_head(_module, 'IExternalConnection')
make_head(_module, 'IFastRundown')
make_head(_module, 'IForegroundTransfer')
make_head(_module, 'IGlobalInterfaceTable')
make_head(_module, 'IGlobalOptions')
make_head(_module, 'IInitializeSpy')
make_head(_module, 'IInternalUnknown')
make_head(_module, 'IMachineGlobalObjectTable')
make_head(_module, 'IMalloc')
make_head(_module, 'IMallocSpy')
make_head(_module, 'IMoniker')
make_head(_module, 'IMultiQI')
make_head(_module, 'INTERFACEINFO')
make_head(_module, 'INoMarshal')
make_head(_module, 'IOplockStorage')
make_head(_module, 'IPSFactoryBuffer')
make_head(_module, 'IPersist')
make_head(_module, 'IPersistFile')
make_head(_module, 'IPersistMemory')
make_head(_module, 'IPersistStream')
make_head(_module, 'IPersistStreamInit')
make_head(_module, 'IPipeByte')
make_head(_module, 'IPipeDouble')
make_head(_module, 'IPipeLong')
make_head(_module, 'IProcessInitControl')
make_head(_module, 'IProcessLock')
make_head(_module, 'IProgressNotify')
make_head(_module, 'IROTData')
make_head(_module, 'IReleaseMarshalBuffers')
make_head(_module, 'IRpcChannelBuffer')
make_head(_module, 'IRpcChannelBuffer2')
make_head(_module, 'IRpcChannelBuffer3')
make_head(_module, 'IRpcHelper')
make_head(_module, 'IRpcOptions')
make_head(_module, 'IRpcProxyBuffer')
make_head(_module, 'IRpcStubBuffer')
make_head(_module, 'IRpcSyntaxNegotiate')
make_head(_module, 'IRunnableObject')
make_head(_module, 'IRunningObjectTable')
make_head(_module, 'ISequentialStream')
make_head(_module, 'IServerSecurity')
make_head(_module, 'IServiceProvider')
make_head(_module, 'IStdMarshalInfo')
make_head(_module, 'IStream')
make_head(_module, 'ISupportErrorInfo')
make_head(_module, 'ISurrogate')
make_head(_module, 'ISurrogateService')
make_head(_module, 'ISynchronize')
make_head(_module, 'ISynchronizeContainer')
make_head(_module, 'ISynchronizeEvent')
make_head(_module, 'ISynchronizeHandle')
make_head(_module, 'ISynchronizeMutex')
make_head(_module, 'ITimeAndNoticeControl')
make_head(_module, 'ITypeComp')
make_head(_module, 'ITypeInfo')
make_head(_module, 'ITypeInfo2')
make_head(_module, 'ITypeLib')
make_head(_module, 'ITypeLib2')
make_head(_module, 'ITypeLibRegistration')
make_head(_module, 'ITypeLibRegistrationReader')
make_head(_module, 'IUnknown')
make_head(_module, 'IUri')
make_head(_module, 'IUriBuilder')
make_head(_module, 'IUrlMon')
make_head(_module, 'IWaitMultiple')
make_head(_module, 'LPEXCEPFINO_DEFERRED_FILLIN')
make_head(_module, 'LPFNCANUNLOADNOW')
make_head(_module, 'LPFNGETCLASSOBJECT')
make_head(_module, 'MULTI_QI')
make_head(_module, 'MachineGlobalObjectTableRegistrationToken__')
make_head(_module, 'PFNCONTEXTCALL')
make_head(_module, 'QUERYCONTEXT')
make_head(_module, 'RPCOLEMESSAGE')
make_head(_module, 'RemSTGMEDIUM')
make_head(_module, 'SAFEARRAY')
make_head(_module, 'SAFEARRAYBOUND')
make_head(_module, 'SChannelHookCallInfo')
make_head(_module, 'SOLE_AUTHENTICATION_INFO')
make_head(_module, 'SOLE_AUTHENTICATION_LIST')
make_head(_module, 'SOLE_AUTHENTICATION_SERVICE')
make_head(_module, 'STATDATA')
make_head(_module, 'STATSTG')
make_head(_module, 'STGMEDIUM')
make_head(_module, 'StorageLayout')
make_head(_module, 'TLIBATTR')
make_head(_module, 'TYPEATTR')
make_head(_module, 'TYPEDESC')
make_head(_module, 'VARDESC')
make_head(_module, 'VARIANT')
make_head(_module, 'WORD_BLOB')
make_head(_module, 'WORD_SIZEDARR')
make_head(_module, 'uCLSSPEC')
make_head(_module, 'userFLAG_STGMEDIUM')
make_head(_module, 'userSTGMEDIUM')
__all__ = [
    "ADVANCED_FEATURE_FLAGS",
    "ADVF",
    "ADVFCACHE_FORCEBUILTIN",
    "ADVFCACHE_NOHANDLER",
    "ADVFCACHE_ONSAVE",
    "ADVF_DATAONSTOP",
    "ADVF_NODATA",
    "ADVF_ONLYONCE",
    "ADVF_PRIMEFIRST",
    "APPIDREGFLAGS_AAA_NO_IMPLICIT_ACTIVATE_AS_IU",
    "APPIDREGFLAGS_ACTIVATE_IUSERVER_INDESKTOP",
    "APPIDREGFLAGS_ISSUE_ACTIVATION_RPC_AT_IDENTIFY",
    "APPIDREGFLAGS_IUSERVER_ACTIVATE_IN_CLIENT_SESSION_ONLY",
    "APPIDREGFLAGS_IUSERVER_SELF_SID_IN_LAUNCH_PERMISSION",
    "APPIDREGFLAGS_IUSERVER_UNMODIFIED_LOGON_TOKEN",
    "APPIDREGFLAGS_RESERVED1",
    "APPIDREGFLAGS_RESERVED2",
    "APPIDREGFLAGS_RESERVED3",
    "APPIDREGFLAGS_RESERVED4",
    "APPIDREGFLAGS_RESERVED5",
    "APPIDREGFLAGS_RESERVED7",
    "APPIDREGFLAGS_RESERVED8",
    "APPIDREGFLAGS_RESERVED9",
    "APPIDREGFLAGS_SECURE_SERVER_PROCESS_SD_AND_BIND",
    "APTTYPE",
    "APTTYPEQUALIFIER",
    "APTTYPEQUALIFIER_APPLICATION_STA",
    "APTTYPEQUALIFIER_IMPLICIT_MTA",
    "APTTYPEQUALIFIER_NA_ON_IMPLICIT_MTA",
    "APTTYPEQUALIFIER_NA_ON_MAINSTA",
    "APTTYPEQUALIFIER_NA_ON_MTA",
    "APTTYPEQUALIFIER_NA_ON_STA",
    "APTTYPEQUALIFIER_NONE",
    "APTTYPEQUALIFIER_RESERVED_1",
    "APTTYPE_CURRENT",
    "APTTYPE_MAINSTA",
    "APTTYPE_MTA",
    "APTTYPE_NA",
    "APTTYPE_STA",
    "ASYNC_MODE_COMPATIBILITY",
    "ASYNC_MODE_DEFAULT",
    "AUTHENTICATEINFO",
    "ApplicationType",
    "ApplicationType_LibraryApplication",
    "ApplicationType_ServerApplication",
    "AsyncIAdviseSink",
    "AsyncIAdviseSink2",
    "AsyncIMultiQI",
    "AsyncIPipeByte",
    "AsyncIPipeDouble",
    "AsyncIPipeLong",
    "AsyncIUnknown",
    "BINDINFO",
    "BINDINFOF",
    "BINDINFOF_URLENCODEDEXTRAINFO",
    "BINDINFOF_URLENCODESTGMEDDATA",
    "BINDPTR",
    "BIND_FLAGS",
    "BIND_JUSTTESTEXISTENCE",
    "BIND_MAYBOTHERUSER",
    "BIND_OPTS",
    "BIND_OPTS2",
    "BIND_OPTS3",
    "BLOB",
    "BYTE_BLOB",
    "BYTE_SIZEDARR",
    "BindMoniker",
    "CALLCONV",
    "CALLTYPE",
    "CALLTYPE_ASYNC",
    "CALLTYPE_ASYNC_CALLPENDING",
    "CALLTYPE_NESTED",
    "CALLTYPE_TOPLEVEL",
    "CALLTYPE_TOPLEVEL_CALLPENDING",
    "CATEGORYINFO",
    "CC_CDECL",
    "CC_FASTCALL",
    "CC_FPFASTCALL",
    "CC_MACPASCAL",
    "CC_MAX",
    "CC_MPWCDECL",
    "CC_MPWPASCAL",
    "CC_MSCPASCAL",
    "CC_PASCAL",
    "CC_STDCALL",
    "CC_SYSCALL",
    "CLSCTX",
    "CLSCTX_ACTIVATE_32_BIT_SERVER",
    "CLSCTX_ACTIVATE_64_BIT_SERVER",
    "CLSCTX_ACTIVATE_AAA_AS_IU",
    "CLSCTX_ACTIVATE_ARM32_SERVER",
    "CLSCTX_ACTIVATE_X86_SERVER",
    "CLSCTX_ALL",
    "CLSCTX_APPCONTAINER",
    "CLSCTX_DISABLE_AAA",
    "CLSCTX_ENABLE_AAA",
    "CLSCTX_ENABLE_CLOAKING",
    "CLSCTX_ENABLE_CODE_DOWNLOAD",
    "CLSCTX_FROM_DEFAULT_CONTEXT",
    "CLSCTX_INPROC_HANDLER",
    "CLSCTX_INPROC_HANDLER16",
    "CLSCTX_INPROC_SERVER",
    "CLSCTX_INPROC_SERVER16",
    "CLSCTX_LOCAL_SERVER",
    "CLSCTX_NO_CODE_DOWNLOAD",
    "CLSCTX_NO_CUSTOM_MARSHAL",
    "CLSCTX_NO_FAILURE_LOG",
    "CLSCTX_PS_DLL",
    "CLSCTX_REMOTE_SERVER",
    "CLSCTX_RESERVED1",
    "CLSCTX_RESERVED2",
    "CLSCTX_RESERVED3",
    "CLSCTX_RESERVED4",
    "CLSCTX_RESERVED5",
    "CLSCTX_RESERVED6",
    "CLSCTX_SERVER",
    "CLSIDFromProgID",
    "CLSIDFromProgIDEx",
    "CLSIDFromString",
    "COAUTHIDENTITY",
    "COAUTHINFO",
    "COINIT",
    "COINITBASE",
    "COINITBASE_MULTITHREADED",
    "COINIT_APARTMENTTHREADED",
    "COINIT_DISABLE_OLE1DDE",
    "COINIT_MULTITHREADED",
    "COINIT_SPEED_OVER_MEMORY",
    "COMBND_RESERVED1",
    "COMBND_RESERVED2",
    "COMBND_RESERVED3",
    "COMBND_RESERVED4",
    "COMBND_RPCTIMEOUT",
    "COMBND_SERVER_LOCALITY",
    "COMGLB_APPID",
    "COMGLB_EXCEPTION_DONOT_HANDLE",
    "COMGLB_EXCEPTION_DONOT_HANDLE_ANY",
    "COMGLB_EXCEPTION_DONOT_HANDLE_FATAL",
    "COMGLB_EXCEPTION_HANDLE",
    "COMGLB_EXCEPTION_HANDLING",
    "COMGLB_FAST_RUNDOWN",
    "COMGLB_PROPERTIES_RESERVED1",
    "COMGLB_PROPERTIES_RESERVED2",
    "COMGLB_PROPERTIES_RESERVED3",
    "COMGLB_RESERVED1",
    "COMGLB_RESERVED2",
    "COMGLB_RESERVED3",
    "COMGLB_RESERVED4",
    "COMGLB_RESERVED5",
    "COMGLB_RESERVED6",
    "COMGLB_RO_SETTINGS",
    "COMGLB_RPC_THREADPOOL_SETTING",
    "COMGLB_RPC_THREADPOOL_SETTING_DEFAULT_POOL",
    "COMGLB_RPC_THREADPOOL_SETTING_PRIVATE_POOL",
    "COMGLB_STA_MODALLOOP_REMOVE_TOUCH_MESSAGES",
    "COMGLB_STA_MODALLOOP_SHARED_QUEUE_DONOT_REMOVE_INPUT_MESSAGES",
    "COMGLB_STA_MODALLOOP_SHARED_QUEUE_REMOVE_INPUT_MESSAGES",
    "COMGLB_STA_MODALLOOP_SHARED_QUEUE_REORDER_POINTER_MESSAGES",
    "COMGLB_UNMARSHALING_POLICY",
    "COMGLB_UNMARSHALING_POLICY_HYBRID",
    "COMGLB_UNMARSHALING_POLICY_NORMAL",
    "COMGLB_UNMARSHALING_POLICY_STRONG",
    "COMSD",
    "COM_RIGHTS_ACTIVATE_LOCAL",
    "COM_RIGHTS_ACTIVATE_REMOTE",
    "COM_RIGHTS_EXECUTE",
    "COM_RIGHTS_EXECUTE_LOCAL",
    "COM_RIGHTS_EXECUTE_REMOTE",
    "COM_RIGHTS_RESERVED1",
    "COM_RIGHTS_RESERVED2",
    "CONNECTDATA",
    "COSERVERINFO",
    "COWAIT_ALERTABLE",
    "COWAIT_DEFAULT",
    "COWAIT_DISPATCH_CALLS",
    "COWAIT_DISPATCH_WINDOW_MESSAGES",
    "COWAIT_FLAGS",
    "COWAIT_INPUTAVAILABLE",
    "COWAIT_WAITALL",
    "CO_DEVICE_CATALOG_COOKIE",
    "CO_MARSHALING_CONTEXT_ATTRIBUTES",
    "CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_1",
    "CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_10",
    "CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_11",
    "CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_12",
    "CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_13",
    "CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_14",
    "CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_15",
    "CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_16",
    "CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_17",
    "CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_18",
    "CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_2",
    "CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_3",
    "CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_4",
    "CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_5",
    "CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_6",
    "CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_7",
    "CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_8",
    "CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_9",
    "CO_MARSHALING_SOURCE_IS_APP_CONTAINER",
    "CO_MTA_USAGE_COOKIE",
    "CSPLATFORM",
    "CUSTDATA",
    "CUSTDATAITEM",
    "CWMO_DEFAULT",
    "CWMO_DISPATCH_CALLS",
    "CWMO_DISPATCH_WINDOW_MESSAGES",
    "CWMO_FLAGS",
    "CWMO_MAX_HANDLES",
    "CY",
    "CoAddRefServerProcess",
    "CoAllowSetForegroundWindow",
    "CoAllowUnmarshalerCLSID",
    "CoBuildVersion",
    "CoCancelCall",
    "CoCopyProxy",
    "CoCreateFreeThreadedMarshaler",
    "CoCreateGuid",
    "CoCreateInstance",
    "CoCreateInstanceEx",
    "CoCreateInstanceFromApp",
    "CoDecrementMTAUsage",
    "CoDisableCallCancellation",
    "CoDisconnectContext",
    "CoDisconnectObject",
    "CoDosDateTimeToFileTime",
    "CoEnableCallCancellation",
    "CoFileTimeNow",
    "CoFileTimeToDosDateTime",
    "CoFreeAllLibraries",
    "CoFreeLibrary",
    "CoFreeUnusedLibraries",
    "CoFreeUnusedLibrariesEx",
    "CoGetApartmentType",
    "CoGetCallContext",
    "CoGetCallerTID",
    "CoGetCancelObject",
    "CoGetClassObject",
    "CoGetContextToken",
    "CoGetCurrentLogicalThreadId",
    "CoGetCurrentProcess",
    "CoGetMalloc",
    "CoGetObject",
    "CoGetObjectContext",
    "CoGetPSClsid",
    "CoGetSystemSecurityPermissions",
    "CoGetTreatAsClass",
    "CoImpersonateClient",
    "CoIncrementMTAUsage",
    "CoInitialize",
    "CoInitializeEx",
    "CoInitializeSecurity",
    "CoInstall",
    "CoInvalidateRemoteMachineBindings",
    "CoIsHandlerConnected",
    "CoIsOle1Class",
    "CoLoadLibrary",
    "CoLockObjectExternal",
    "CoQueryAuthenticationServices",
    "CoQueryClientBlanket",
    "CoQueryProxyBlanket",
    "CoRegisterActivationFilter",
    "CoRegisterChannelHook",
    "CoRegisterClassObject",
    "CoRegisterDeviceCatalog",
    "CoRegisterInitializeSpy",
    "CoRegisterMallocSpy",
    "CoRegisterPSClsid",
    "CoRegisterSurrogate",
    "CoReleaseServerProcess",
    "CoResumeClassObjects",
    "CoRevertToSelf",
    "CoRevokeClassObject",
    "CoRevokeDeviceCatalog",
    "CoRevokeInitializeSpy",
    "CoRevokeMallocSpy",
    "CoSetCancelObject",
    "CoSetProxyBlanket",
    "CoSuspendClassObjects",
    "CoSwitchCallContext",
    "CoTaskMemAlloc",
    "CoTaskMemFree",
    "CoTaskMemRealloc",
    "CoTestCancel",
    "CoTreatAsClass",
    "CoUninitialize",
    "CoWaitForMultipleHandles",
    "CoWaitForMultipleObjects",
    "ComCallData",
    "CreateAntiMoniker",
    "CreateBindCtx",
    "CreateClassMoniker",
    "CreateDataAdviseHolder",
    "CreateDataCache",
    "CreateFileMoniker",
    "CreateGenericComposite",
    "CreateIUriBuilder",
    "CreateItemMoniker",
    "CreateObjrefMoniker",
    "CreatePointerMoniker",
    "CreateStdProgressIndicator",
    "CreateUri",
    "CreateUriFromMultiByteString",
    "CreateUriWithFragment",
    "DATADIR",
    "DATADIR_GET",
    "DATADIR_SET",
    "DCOMSCM_ACTIVATION_DISALLOW_UNSECURE_CALL",
    "DCOMSCM_ACTIVATION_USE_ALL_AUTHNSERVICES",
    "DCOMSCM_PING_DISALLOW_UNSECURE_CALL",
    "DCOMSCM_PING_USE_MID_AUTHNSERVICE",
    "DCOMSCM_RESOLVE_DISALLOW_UNSECURE_CALL",
    "DCOMSCM_RESOLVE_USE_ALL_AUTHNSERVICES",
    "DCOM_CALL_CANCELED",
    "DCOM_CALL_COMPLETE",
    "DCOM_CALL_STATE",
    "DCOM_NONE",
    "DESCKIND",
    "DESCKIND_FUNCDESC",
    "DESCKIND_IMPLICITAPPOBJ",
    "DESCKIND_MAX",
    "DESCKIND_NONE",
    "DESCKIND_TYPECOMP",
    "DESCKIND_VARDESC",
    "DISPATCH_FLAGS",
    "DISPATCH_METHOD",
    "DISPATCH_PROPERTYGET",
    "DISPATCH_PROPERTYPUT",
    "DISPATCH_PROPERTYPUTREF",
    "DISPPARAMS",
    "DMUS_ERRBASE",
    "DVASPECT",
    "DVASPECT_CONTENT",
    "DVASPECT_DOCPRINT",
    "DVASPECT_ICON",
    "DVASPECT_OPAQUE",
    "DVASPECT_THUMBNAIL",
    "DVASPECT_TRANSPARENT",
    "DVTARGETDEVICE",
    "DWORD_BLOB",
    "DWORD_SIZEDARR",
    "DcomChannelSetHResult",
    "ELEMDESC",
    "EOAC_ACCESS_CONTROL",
    "EOAC_ANY_AUTHORITY",
    "EOAC_APPID",
    "EOAC_AUTO_IMPERSONATE",
    "EOAC_DEFAULT",
    "EOAC_DISABLE_AAA",
    "EOAC_DYNAMIC",
    "EOAC_DYNAMIC_CLOAKING",
    "EOAC_MAKE_FULLSIC",
    "EOAC_MUTUAL_AUTH",
    "EOAC_NONE",
    "EOAC_NO_CUSTOM_MARSHAL",
    "EOAC_REQUIRE_FULLSIC",
    "EOAC_RESERVED1",
    "EOAC_SECURE_REFS",
    "EOAC_STATIC_CLOAKING",
    "EOLE_AUTHENTICATION_CAPABILITIES",
    "EXCEPINFO",
    "EXTCONN",
    "EXTCONN_CALLABLE",
    "EXTCONN_STRONG",
    "EXTCONN_WEAK",
    "FADF_AUTO",
    "FADF_BSTR",
    "FADF_DISPATCH",
    "FADF_EMBEDDED",
    "FADF_FIXEDSIZE",
    "FADF_HAVEIID",
    "FADF_HAVEVARTYPE",
    "FADF_RECORD",
    "FADF_RESERVED",
    "FADF_STATIC",
    "FADF_UNKNOWN",
    "FADF_VARIANT",
    "FLAGGED_BYTE_BLOB",
    "FLAGGED_WORD_BLOB",
    "FLAG_STGMEDIUM",
    "FORMATETC",
    "FUNCDESC",
    "FUNCFLAGS",
    "FUNCFLAG_FBINDABLE",
    "FUNCFLAG_FDEFAULTBIND",
    "FUNCFLAG_FDEFAULTCOLLELEM",
    "FUNCFLAG_FDISPLAYBIND",
    "FUNCFLAG_FHIDDEN",
    "FUNCFLAG_FIMMEDIATEBIND",
    "FUNCFLAG_FNONBROWSABLE",
    "FUNCFLAG_FREPLACEABLE",
    "FUNCFLAG_FREQUESTEDIT",
    "FUNCFLAG_FRESTRICTED",
    "FUNCFLAG_FSOURCE",
    "FUNCFLAG_FUIDEFAULT",
    "FUNCFLAG_FUSESGETLASTERROR",
    "FUNCKIND",
    "FUNC_DISPATCH",
    "FUNC_NONVIRTUAL",
    "FUNC_PUREVIRTUAL",
    "FUNC_STATIC",
    "FUNC_VIRTUAL",
    "GDI_OBJECT",
    "GLOBALOPT_EH_VALUES",
    "GLOBALOPT_PROPERTIES",
    "GLOBALOPT_RO_FLAGS",
    "GLOBALOPT_RPCTP_VALUES",
    "GLOBALOPT_UNMARSHALING_POLICY_VALUES",
    "GetClassFile",
    "GetErrorInfo",
    "GetRunningObjectTable",
    "HYPER_SIZEDARR",
    "IActivationFilter",
    "IAddrExclusionControl",
    "IAddrTrackingControl",
    "IAdviseSink",
    "IAdviseSink2",
    "IAgileObject",
    "IAsyncManager",
    "IAsyncRpcChannelBuffer",
    "IAuthenticate",
    "IAuthenticateEx",
    "IBindCtx",
    "IBindHost",
    "IBindStatusCallback",
    "IBindStatusCallbackEx",
    "IBinding",
    "IBlockingLock",
    "ICallFactory",
    "ICancelMethodCalls",
    "ICatInformation",
    "ICatRegister",
    "IChannelHook",
    "IClassActivator",
    "IClassFactory",
    "IClientSecurity",
    "IComThreadingInfo",
    "IConnectionPoint",
    "IConnectionPointContainer",
    "IContext",
    "IContextCallback",
    "IDLDESC",
    "IDLFLAGS",
    "IDLFLAG_FIN",
    "IDLFLAG_FLCID",
    "IDLFLAG_FOUT",
    "IDLFLAG_FRETVAL",
    "IDLFLAG_NONE",
    "IDataAdviseHolder",
    "IDataObject",
    "IDispatch",
    "IEnumCATEGORYINFO",
    "IEnumConnectionPoints",
    "IEnumConnections",
    "IEnumContextProps",
    "IEnumFORMATETC",
    "IEnumGUID",
    "IEnumMoniker",
    "IEnumSTATDATA",
    "IEnumString",
    "IEnumUnknown",
    "IErrorInfo",
    "IErrorLog",
    "IExternalConnection",
    "IFastRundown",
    "IForegroundTransfer",
    "IGlobalInterfaceTable",
    "IGlobalOptions",
    "IIDFromString",
    "IInitializeSpy",
    "IInternalUnknown",
    "IMPLTYPEFLAGS",
    "IMPLTYPEFLAG_FDEFAULT",
    "IMPLTYPEFLAG_FDEFAULTVTABLE",
    "IMPLTYPEFLAG_FRESTRICTED",
    "IMPLTYPEFLAG_FSOURCE",
    "IMachineGlobalObjectTable",
    "IMalloc",
    "IMallocSpy",
    "IMoniker",
    "IMultiQI",
    "INTERFACEINFO",
    "INVOKEKIND",
    "INVOKE_FUNC",
    "INVOKE_PROPERTYGET",
    "INVOKE_PROPERTYPUT",
    "INVOKE_PROPERTYPUTREF",
    "INoMarshal",
    "IOplockStorage",
    "IPSFactoryBuffer",
    "IPersist",
    "IPersistFile",
    "IPersistMemory",
    "IPersistStream",
    "IPersistStreamInit",
    "IPipeByte",
    "IPipeDouble",
    "IPipeLong",
    "IProcessInitControl",
    "IProcessLock",
    "IProgressNotify",
    "IROTData",
    "IReleaseMarshalBuffers",
    "IRpcChannelBuffer",
    "IRpcChannelBuffer2",
    "IRpcChannelBuffer3",
    "IRpcHelper",
    "IRpcOptions",
    "IRpcProxyBuffer",
    "IRpcStubBuffer",
    "IRpcSyntaxNegotiate",
    "IRunnableObject",
    "IRunningObjectTable",
    "ISequentialStream",
    "IServerSecurity",
    "IServiceProvider",
    "IStdMarshalInfo",
    "IStream",
    "ISupportErrorInfo",
    "ISurrogate",
    "ISurrogateService",
    "ISynchronize",
    "ISynchronizeContainer",
    "ISynchronizeEvent",
    "ISynchronizeHandle",
    "ISynchronizeMutex",
    "ITimeAndNoticeControl",
    "ITypeComp",
    "ITypeInfo",
    "ITypeInfo2",
    "ITypeLib",
    "ITypeLib2",
    "ITypeLibRegistration",
    "ITypeLibRegistrationReader",
    "IUnknown",
    "IUri",
    "IUriBuilder",
    "IUrlMon",
    "IWaitMultiple",
    "LOCKTYPE",
    "LOCK_EXCLUSIVE",
    "LOCK_ONLYONCE",
    "LOCK_WRITE",
    "LPEXCEPFINO_DEFERRED_FILLIN",
    "LPFNCANUNLOADNOW",
    "LPFNGETCLASSOBJECT",
    "MARSHALINTERFACE_MIN",
    "MAXLSN",
    "MEMCTX",
    "MEMCTX_MACSYSTEM",
    "MEMCTX_SAME",
    "MEMCTX_SHARED",
    "MEMCTX_TASK",
    "MEMCTX_UNKNOWN",
    "MKRREDUCE",
    "MKRREDUCE_ALL",
    "MKRREDUCE_ONE",
    "MKRREDUCE_THROUGHUSER",
    "MKRREDUCE_TOUSER",
    "MKSYS",
    "MKSYS_ANTIMONIKER",
    "MKSYS_CLASSMONIKER",
    "MKSYS_FILEMONIKER",
    "MKSYS_GENERICCOMPOSITE",
    "MKSYS_ITEMMONIKER",
    "MKSYS_LUAMONIKER",
    "MKSYS_NONE",
    "MKSYS_OBJREFMONIKER",
    "MKSYS_POINTERMONIKER",
    "MKSYS_SESSIONMONIKER",
    "MSHCTX",
    "MSHCTX_CONTAINER",
    "MSHCTX_CROSSCTX",
    "MSHCTX_DIFFERENTMACHINE",
    "MSHCTX_INPROC",
    "MSHCTX_LOCAL",
    "MSHCTX_NOSHAREDMEM",
    "MSHLFLAGS",
    "MSHLFLAGS_NOPING",
    "MSHLFLAGS_NORMAL",
    "MSHLFLAGS_RESERVED1",
    "MSHLFLAGS_RESERVED2",
    "MSHLFLAGS_RESERVED3",
    "MSHLFLAGS_RESERVED4",
    "MSHLFLAGS_TABLESTRONG",
    "MSHLFLAGS_TABLEWEAK",
    "MULTI_QI",
    "MachineGlobalObjectTableRegistrationToken__",
    "MkParseDisplayName",
    "MonikerCommonPrefixWith",
    "MonikerRelativePathTo",
    "PENDINGMSG",
    "PENDINGMSG_CANCELCALL",
    "PENDINGMSG_WAITDEFPROCESS",
    "PENDINGMSG_WAITNOPROCESS",
    "PENDINGTYPE",
    "PENDINGTYPE_NESTED",
    "PENDINGTYPE_TOPLEVEL",
    "PFNCONTEXTCALL",
    "ProgIDFromCLSID",
    "QUERYCONTEXT",
    "REGCLS",
    "REGCLS_AGILE",
    "REGCLS_MULTIPLEUSE",
    "REGCLS_MULTI_SEPARATE",
    "REGCLS_SINGLEUSE",
    "REGCLS_SURROGATE",
    "REGCLS_SUSPENDED",
    "ROTFLAGS_ALLOWANYCLIENT",
    "ROTFLAGS_REGISTRATIONKEEPSALIVE",
    "ROTREGFLAGS_ALLOWANYCLIENT",
    "ROT_FLAGS",
    "RPCOLEMESSAGE",
    "RPCOPT_PROPERTIES",
    "RPCOPT_SERVER_LOCALITY_VALUES",
    "RPC_C_AUTHN_LEVEL",
    "RPC_C_AUTHN_LEVEL_CALL",
    "RPC_C_AUTHN_LEVEL_CONNECT",
    "RPC_C_AUTHN_LEVEL_DEFAULT",
    "RPC_C_AUTHN_LEVEL_NONE",
    "RPC_C_AUTHN_LEVEL_PKT",
    "RPC_C_AUTHN_LEVEL_PKT_INTEGRITY",
    "RPC_C_AUTHN_LEVEL_PKT_PRIVACY",
    "RPC_C_IMP_LEVEL",
    "RPC_C_IMP_LEVEL_ANONYMOUS",
    "RPC_C_IMP_LEVEL_DEFAULT",
    "RPC_C_IMP_LEVEL_DELEGATE",
    "RPC_C_IMP_LEVEL_IDENTIFY",
    "RPC_C_IMP_LEVEL_IMPERSONATE",
    "RemSTGMEDIUM",
    "SAFEARRAY",
    "SAFEARRAYBOUND",
    "SChannelHookCallInfo",
    "SD_ACCESSPERMISSIONS",
    "SD_ACCESSRESTRICTIONS",
    "SD_LAUNCHPERMISSIONS",
    "SD_LAUNCHRESTRICTIONS",
    "SERVERCALL",
    "SERVERCALL_ISHANDLED",
    "SERVERCALL_REJECTED",
    "SERVERCALL_RETRYLATER",
    "SERVER_LOCALITY_MACHINE_LOCAL",
    "SERVER_LOCALITY_PROCESS_LOCAL",
    "SERVER_LOCALITY_REMOTE",
    "SOLE_AUTHENTICATION_INFO",
    "SOLE_AUTHENTICATION_LIST",
    "SOLE_AUTHENTICATION_SERVICE",
    "STATDATA",
    "STATFLAG",
    "STATFLAG_DEFAULT",
    "STATFLAG_NONAME",
    "STATFLAG_NOOPEN",
    "STATSTG",
    "STGC",
    "STGC_CONSOLIDATE",
    "STGC_DANGEROUSLYCOMMITMERELYTODISKCACHE",
    "STGC_DEFAULT",
    "STGC_ONLYIFCURRENT",
    "STGC_OVERWRITE",
    "STGM",
    "STGMEDIUM",
    "STGM_CONVERT",
    "STGM_CREATE",
    "STGM_DELETEONRELEASE",
    "STGM_DIRECT",
    "STGM_DIRECT_SWMR",
    "STGM_FAILIFTHERE",
    "STGM_NOSCRATCH",
    "STGM_NOSNAPSHOT",
    "STGM_PRIORITY",
    "STGM_READ",
    "STGM_READWRITE",
    "STGM_SHARE_DENY_NONE",
    "STGM_SHARE_DENY_READ",
    "STGM_SHARE_DENY_WRITE",
    "STGM_SHARE_EXCLUSIVE",
    "STGM_SIMPLE",
    "STGM_TRANSACTED",
    "STGM_WRITE",
    "STGTY",
    "STGTY_LOCKBYTES",
    "STGTY_PROPERTY",
    "STGTY_REPEAT",
    "STGTY_STORAGE",
    "STGTY_STREAM",
    "STG_LAYOUT_INTERLEAVED",
    "STG_LAYOUT_SEQUENTIAL",
    "STG_TOEND",
    "STREAM_SEEK",
    "STREAM_SEEK_CUR",
    "STREAM_SEEK_END",
    "STREAM_SEEK_SET",
    "SYSKIND",
    "SYS_MAC",
    "SYS_WIN16",
    "SYS_WIN32",
    "SYS_WIN64",
    "SetErrorInfo",
    "ShutdownType",
    "ShutdownType_ForcedShutdown",
    "ShutdownType_IdleShutdown",
    "StorageLayout",
    "StringFromCLSID",
    "StringFromGUID2",
    "StringFromIID",
    "THDTYPE",
    "THDTYPE_BLOCKMESSAGES",
    "THDTYPE_PROCESSMESSAGES",
    "TKIND_ALIAS",
    "TKIND_COCLASS",
    "TKIND_DISPATCH",
    "TKIND_ENUM",
    "TKIND_INTERFACE",
    "TKIND_MAX",
    "TKIND_MODULE",
    "TKIND_RECORD",
    "TKIND_UNION",
    "TLIBATTR",
    "TYMED",
    "TYMED_ENHMF",
    "TYMED_FILE",
    "TYMED_GDI",
    "TYMED_HGLOBAL",
    "TYMED_ISTORAGE",
    "TYMED_ISTREAM",
    "TYMED_MFPICT",
    "TYMED_NULL",
    "TYPEATTR",
    "TYPEDESC",
    "TYPEKIND",
    "TYSPEC",
    "TYSPEC_CLSID",
    "TYSPEC_FILEEXT",
    "TYSPEC_FILENAME",
    "TYSPEC_MIMETYPE",
    "TYSPEC_OBJECTID",
    "TYSPEC_PACKAGENAME",
    "TYSPEC_PROGID",
    "URI_CREATE_FLAGS",
    "Uri_CREATE_ALLOW_IMPLICIT_FILE_SCHEME",
    "Uri_CREATE_ALLOW_IMPLICIT_WILDCARD_SCHEME",
    "Uri_CREATE_ALLOW_RELATIVE",
    "Uri_CREATE_CANONICALIZE",
    "Uri_CREATE_CANONICALIZE_ABSOLUTE",
    "Uri_CREATE_CRACK_UNKNOWN_SCHEMES",
    "Uri_CREATE_DECODE_EXTRA_INFO",
    "Uri_CREATE_FILE_USE_DOS_PATH",
    "Uri_CREATE_IE_SETTINGS",
    "Uri_CREATE_NOFRAG",
    "Uri_CREATE_NORMALIZE_INTL_CHARACTERS",
    "Uri_CREATE_NO_CANONICALIZE",
    "Uri_CREATE_NO_CRACK_UNKNOWN_SCHEMES",
    "Uri_CREATE_NO_DECODE_EXTRA_INFO",
    "Uri_CREATE_NO_ENCODE_FORBIDDEN_CHARACTERS",
    "Uri_CREATE_NO_IE_SETTINGS",
    "Uri_CREATE_NO_PRE_PROCESS_HTML_URI",
    "Uri_CREATE_PRE_PROCESS_HTML_URI",
    "Uri_PROPERTY",
    "Uri_PROPERTY_ABSOLUTE_URI",
    "Uri_PROPERTY_AUTHORITY",
    "Uri_PROPERTY_DISPLAY_URI",
    "Uri_PROPERTY_DOMAIN",
    "Uri_PROPERTY_DWORD_LAST",
    "Uri_PROPERTY_DWORD_START",
    "Uri_PROPERTY_EXTENSION",
    "Uri_PROPERTY_FRAGMENT",
    "Uri_PROPERTY_HOST",
    "Uri_PROPERTY_HOST_TYPE",
    "Uri_PROPERTY_PASSWORD",
    "Uri_PROPERTY_PATH",
    "Uri_PROPERTY_PATH_AND_QUERY",
    "Uri_PROPERTY_PORT",
    "Uri_PROPERTY_QUERY",
    "Uri_PROPERTY_RAW_URI",
    "Uri_PROPERTY_SCHEME",
    "Uri_PROPERTY_SCHEME_NAME",
    "Uri_PROPERTY_STRING_LAST",
    "Uri_PROPERTY_STRING_START",
    "Uri_PROPERTY_USER_INFO",
    "Uri_PROPERTY_USER_NAME",
    "Uri_PROPERTY_ZONE",
    "VARDESC",
    "VARENUM",
    "VARFLAGS",
    "VARFLAG_FBINDABLE",
    "VARFLAG_FDEFAULTBIND",
    "VARFLAG_FDEFAULTCOLLELEM",
    "VARFLAG_FDISPLAYBIND",
    "VARFLAG_FHIDDEN",
    "VARFLAG_FIMMEDIATEBIND",
    "VARFLAG_FNONBROWSABLE",
    "VARFLAG_FREADONLY",
    "VARFLAG_FREPLACEABLE",
    "VARFLAG_FREQUESTEDIT",
    "VARFLAG_FRESTRICTED",
    "VARFLAG_FSOURCE",
    "VARFLAG_FUIDEFAULT",
    "VARIANT",
    "VARKIND",
    "VAR_CONST",
    "VAR_DISPATCH",
    "VAR_PERINSTANCE",
    "VAR_STATIC",
    "VT_ARRAY",
    "VT_BLOB",
    "VT_BLOB_OBJECT",
    "VT_BOOL",
    "VT_BSTR",
    "VT_BSTR_BLOB",
    "VT_BYREF",
    "VT_CARRAY",
    "VT_CF",
    "VT_CLSID",
    "VT_CY",
    "VT_DATE",
    "VT_DECIMAL",
    "VT_DISPATCH",
    "VT_EMPTY",
    "VT_ERROR",
    "VT_FILETIME",
    "VT_HRESULT",
    "VT_I1",
    "VT_I2",
    "VT_I4",
    "VT_I8",
    "VT_ILLEGAL",
    "VT_ILLEGALMASKED",
    "VT_INT",
    "VT_INT_PTR",
    "VT_LPSTR",
    "VT_LPWSTR",
    "VT_NULL",
    "VT_PTR",
    "VT_R4",
    "VT_R8",
    "VT_RECORD",
    "VT_RESERVED",
    "VT_SAFEARRAY",
    "VT_STORAGE",
    "VT_STORED_OBJECT",
    "VT_STREAM",
    "VT_STREAMED_OBJECT",
    "VT_TYPEMASK",
    "VT_UI1",
    "VT_UI2",
    "VT_UI4",
    "VT_UI8",
    "VT_UINT",
    "VT_UINT_PTR",
    "VT_UNKNOWN",
    "VT_USERDEFINED",
    "VT_VARIANT",
    "VT_VECTOR",
    "VT_VERSIONED_STREAM",
    "VT_VOID",
    "WORD_BLOB",
    "WORD_SIZEDARR",
    "uCLSSPEC",
    "userFLAG_STGMEDIUM",
    "userSTGMEDIUM",
]
_arch_optional = [
]
