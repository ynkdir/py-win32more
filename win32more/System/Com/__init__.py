from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
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
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
ADVANCED_FEATURE_FLAGS = UInt16
FADF_AUTO = 1
FADF_STATIC = 2
FADF_EMBEDDED = 4
FADF_FIXEDSIZE = 16
FADF_RECORD = 32
FADF_HAVEIID = 64
FADF_HAVEVARTYPE = 128
FADF_BSTR = 256
FADF_UNKNOWN = 512
FADF_DISPATCH = 1024
FADF_VARIANT = 2048
FADF_RESERVED = 61448
ADVF = Int32
ADVF_NODATA = 1
ADVF_PRIMEFIRST = 2
ADVF_ONLYONCE = 4
ADVF_DATAONSTOP = 64
ADVFCACHE_NOHANDLER = 8
ADVFCACHE_FORCEBUILTIN = 16
ADVFCACHE_ONSAVE = 32
MARSHALINTERFACE_MIN = 500
ASYNC_MODE_COMPATIBILITY = 1
ASYNC_MODE_DEFAULT = 0
STGTY_REPEAT = 256
STG_TOEND = -1
STG_LAYOUT_SEQUENTIAL = 0
STG_LAYOUT_INTERLEAVED = 1
COM_RIGHTS_EXECUTE = 1
COM_RIGHTS_EXECUTE_LOCAL = 2
COM_RIGHTS_EXECUTE_REMOTE = 4
COM_RIGHTS_ACTIVATE_LOCAL = 8
COM_RIGHTS_ACTIVATE_REMOTE = 16
COM_RIGHTS_RESERVED1 = 32
COM_RIGHTS_RESERVED2 = 64
CWMO_MAX_HANDLES = 56
ROTREGFLAGS_ALLOWANYCLIENT = 1
APPIDREGFLAGS_ACTIVATE_IUSERVER_INDESKTOP = 1
APPIDREGFLAGS_SECURE_SERVER_PROCESS_SD_AND_BIND = 2
APPIDREGFLAGS_ISSUE_ACTIVATION_RPC_AT_IDENTIFY = 4
APPIDREGFLAGS_IUSERVER_UNMODIFIED_LOGON_TOKEN = 8
APPIDREGFLAGS_IUSERVER_SELF_SID_IN_LAUNCH_PERMISSION = 16
APPIDREGFLAGS_IUSERVER_ACTIVATE_IN_CLIENT_SESSION_ONLY = 32
APPIDREGFLAGS_RESERVED1 = 64
APPIDREGFLAGS_RESERVED2 = 128
APPIDREGFLAGS_RESERVED3 = 256
APPIDREGFLAGS_RESERVED4 = 512
APPIDREGFLAGS_RESERVED5 = 1024
APPIDREGFLAGS_AAA_NO_IMPLICIT_ACTIVATE_AS_IU = 2048
APPIDREGFLAGS_RESERVED7 = 4096
APPIDREGFLAGS_RESERVED8 = 8192
APPIDREGFLAGS_RESERVED9 = 16384
DCOMSCM_ACTIVATION_USE_ALL_AUTHNSERVICES = 1
DCOMSCM_ACTIVATION_DISALLOW_UNSECURE_CALL = 2
DCOMSCM_RESOLVE_USE_ALL_AUTHNSERVICES = 4
DCOMSCM_RESOLVE_DISALLOW_UNSECURE_CALL = 8
DCOMSCM_PING_USE_MID_AUTHNSERVICE = 16
DCOMSCM_PING_DISALLOW_UNSECURE_CALL = 32
MAXLSN = 9223372036854775807
DMUS_ERRBASE = 4096
def _define_CoBuildVersion():
    try:
        return WINFUNCTYPE(UInt32,)(('CoBuildVersion', windll['ole32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInitialize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p)(('CoInitialize', windll['OLE32.dll']), ((1, 'pvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoRegisterMallocSpy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMallocSpy_head)(('CoRegisterMallocSpy', windll['OLE32.dll']), ((1, 'pMallocSpy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoRevokeMallocSpy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,)(('CoRevokeMallocSpy', windll['OLE32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoRegisterInitializeSpy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IInitializeSpy_head,POINTER(win32more.Foundation.ULARGE_INTEGER_head))(('CoRegisterInitializeSpy', windll['OLE32.dll']), ((1, 'pSpy'),(1, 'puliCookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoRevokeInitializeSpy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.ULARGE_INTEGER)(('CoRevokeInitializeSpy', windll['OLE32.dll']), ((1, 'uliCookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetSystemSecurityPermissions():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.COMSD,POINTER(win32more.Security.PSECURITY_DESCRIPTOR))(('CoGetSystemSecurityPermissions', windll['OLE32.dll']), ((1, 'comSDType'),(1, 'ppSD'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoLoadLibrary():
    try:
        return WINFUNCTYPE(win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)(('CoLoadLibrary', windll['OLE32.dll']), ((1, 'lpszLibName'),(1, 'bAutoFree'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoFreeLibrary():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HINSTANCE)(('CoFreeLibrary', windll['OLE32.dll']), ((1, 'hInst'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoFreeAllLibraries():
    try:
        return WINFUNCTYPE(Void,)(('CoFreeAllLibraries', windll['OLE32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoAllowSetForegroundWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,c_void_p)(('CoAllowSetForegroundWindow', windll['OLE32.dll']), ((1, 'pUnk'),(1, 'lpvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DcomChannelSetHResult():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(UInt32),win32more.Foundation.HRESULT)(('DcomChannelSetHResult', windll['ole32.dll']), ((1, 'pvReserved'),(1, 'pulReserved'),(1, 'appsHR'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoIsOle1Class():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Guid))(('CoIsOle1Class', windll['ole32.dll']), ((1, 'rclsid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLSIDFromProgIDEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid))(('CLSIDFromProgIDEx', windll['OLE32.dll']), ((1, 'lpszProgID'),(1, 'lpclsid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoFileTimeToDosDateTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.FILETIME_head),POINTER(UInt16),POINTER(UInt16))(('CoFileTimeToDosDateTime', windll['OLE32.dll']), ((1, 'lpFileTime'),(1, 'lpDosDate'),(1, 'lpDosTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoDosDateTimeToFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt16,UInt16,POINTER(win32more.Foundation.FILETIME_head))(('CoDosDateTimeToFileTime', windll['OLE32.dll']), ((1, 'nDosDate'),(1, 'nDosTime'),(1, 'lpFileTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoFileTimeNow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head))(('CoFileTimeNow', windll['OLE32.dll']), ((1, 'lpFileTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoRegisterChannelHook():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IChannelHook_head)(('CoRegisterChannelHook', windll['ole32.dll']), ((1, 'ExtensionUuid'),(1, 'pChannelHook'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoTreatAsClass():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid))(('CoTreatAsClass', windll['OLE32.dll']), ((1, 'clsidOld'),(1, 'clsidNew'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDataAdviseHolder():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDataAdviseHolder_head))(('CreateDataAdviseHolder', windll['OLE32.dll']), ((1, 'ppDAHolder'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDataCache():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(Guid),POINTER(c_void_p))(('CreateDataCache', windll['OLE32.dll']), ((1, 'pUnkOuter'),(1, 'rclsid'),(1, 'iid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInstall():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,UInt32,POINTER(win32more.System.Com.uCLSSPEC_head),POINTER(win32more.System.Com.QUERYCONTEXT_head),win32more.Foundation.PWSTR)(('CoInstall', windll['ole32.dll']), ((1, 'pbc'),(1, 'dwFlags'),(1, 'pClassSpec'),(1, 'pQuery'),(1, 'pszCodeBase'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BindMoniker():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,UInt32,POINTER(Guid),POINTER(c_void_p))(('BindMoniker', windll['OLE32.dll']), ((1, 'pmk'),(1, 'grfOpt'),(1, 'iidResult'),(1, 'ppvResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.BIND_OPTS_head),POINTER(Guid),POINTER(c_void_p))(('CoGetObject', windll['OLE32.dll']), ((1, 'pszName'),(1, 'pBindOptions'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MkParseDisplayName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.System.Com.IMoniker_head))(('MkParseDisplayName', windll['OLE32.dll']), ((1, 'pbc'),(1, 'szUserName'),(1, 'pchEaten'),(1, 'ppmk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MonikerRelativePathTo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,win32more.System.Com.IMoniker_head,POINTER(win32more.System.Com.IMoniker_head),win32more.Foundation.BOOL)(('MonikerRelativePathTo', windll['ole32.dll']), ((1, 'pmkSrc'),(1, 'pmkDest'),(1, 'ppmkRelPath'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MonikerCommonPrefixWith():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,win32more.System.Com.IMoniker_head,POINTER(win32more.System.Com.IMoniker_head))(('MonikerCommonPrefixWith', windll['ole32.dll']), ((1, 'pmkThis'),(1, 'pmkOther'),(1, 'ppmkCommon'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateBindCtx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IBindCtx_head))(('CreateBindCtx', windll['OLE32.dll']), ((1, 'reserved'),(1, 'ppbc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateGenericComposite():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,win32more.System.Com.IMoniker_head,POINTER(win32more.System.Com.IMoniker_head))(('CreateGenericComposite', windll['OLE32.dll']), ((1, 'pmkFirst'),(1, 'pmkRest'),(1, 'ppmkComposite'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetClassFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid))(('GetClassFile', windll['OLE32.dll']), ((1, 'szFilename'),(1, 'pclsid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateClassMoniker():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.IMoniker_head))(('CreateClassMoniker', windll['OLE32.dll']), ((1, 'rclsid'),(1, 'ppmk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFileMoniker():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.IMoniker_head))(('CreateFileMoniker', windll['OLE32.dll']), ((1, 'lpszPathName'),(1, 'ppmk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateItemMoniker():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.IMoniker_head))(('CreateItemMoniker', windll['OLE32.dll']), ((1, 'lpszDelim'),(1, 'lpszItem'),(1, 'ppmk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateAntiMoniker():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IMoniker_head))(('CreateAntiMoniker', windll['OLE32.dll']), ((1, 'ppmk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreatePointerMoniker():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.IMoniker_head))(('CreatePointerMoniker', windll['OLE32.dll']), ((1, 'punk'),(1, 'ppmk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateObjrefMoniker():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.IMoniker_head))(('CreateObjrefMoniker', windll['OLE32.dll']), ((1, 'punk'),(1, 'ppmk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRunningObjectTable():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IRunningObjectTable_head))(('GetRunningObjectTable', windll['OLE32.dll']), ((1, 'reserved'),(1, 'pprot'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateStdProgressIndicator():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.System.Com.IBindStatusCallback_head,POINTER(win32more.System.Com.IBindStatusCallback_head))(('CreateStdProgressIndicator', windll['ole32.dll']), ((1, 'hwndParent'),(1, 'pszTitle'),(1, 'pIbscCaller'),(1, 'ppIbsc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetMalloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IMalloc_head))(('CoGetMalloc', windll['OLE32.dll']), ((1, 'dwMemContext'),(1, 'ppMalloc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoUninitialize():
    try:
        return WINFUNCTYPE(Void,)(('CoUninitialize', windll['OLE32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetCurrentProcess():
    try:
        return WINFUNCTYPE(UInt32,)(('CoGetCurrentProcess', windll['OLE32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInitializeEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.Com.COINIT)(('CoInitializeEx', windll['OLE32.dll']), ((1, 'pvReserved'),(1, 'dwCoInit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetCallerTID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(('CoGetCallerTID', windll['OLE32.dll']), ((1, 'lpdwTID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetCurrentLogicalThreadId():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(('CoGetCurrentLogicalThreadId', windll['OLE32.dll']), ((1, 'pguid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetContextToken():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UIntPtr))(('CoGetContextToken', windll['OLE32.dll']), ((1, 'pToken'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetApartmentType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.APTTYPE),POINTER(win32more.System.Com.APTTYPEQUALIFIER))(('CoGetApartmentType', windll['OLE32.dll']), ((1, 'pAptType'),(1, 'pAptQualifier'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoIncrementMTAUsage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.CO_MTA_USAGE_COOKIE))(('CoIncrementMTAUsage', windll['OLE32.dll']), ((1, 'pCookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoDecrementMTAUsage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CO_MTA_USAGE_COOKIE)(('CoDecrementMTAUsage', windll['OLE32.dll']), ((1, 'Cookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoAllowUnmarshalerCLSID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(('CoAllowUnmarshalerCLSID', windll['OLE32.dll']), ((1, 'clsid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetObjectContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(('CoGetObjectContext', windll['OLE32.dll']), ((1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetClassObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.CLSCTX,c_void_p,POINTER(Guid),POINTER(c_void_p))(('CoGetClassObject', windll['OLE32.dll']), ((1, 'rclsid'),(1, 'dwClsContext'),(1, 'pvReserved'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoRegisterClassObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,win32more.System.Com.CLSCTX,win32more.System.Com.REGCLS,POINTER(UInt32))(('CoRegisterClassObject', windll['OLE32.dll']), ((1, 'rclsid'),(1, 'pUnk'),(1, 'dwClsContext'),(1, 'flags'),(1, 'lpdwRegister'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoRevokeClassObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(('CoRevokeClassObject', windll['OLE32.dll']), ((1, 'dwRegister'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoResumeClassObjects():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,)(('CoResumeClassObjects', windll['OLE32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoSuspendClassObjects():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,)(('CoSuspendClassObjects', windll['OLE32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoAddRefServerProcess():
    try:
        return WINFUNCTYPE(UInt32,)(('CoAddRefServerProcess', windll['OLE32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoReleaseServerProcess():
    try:
        return WINFUNCTYPE(UInt32,)(('CoReleaseServerProcess', windll['OLE32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetPSClsid():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid))(('CoGetPSClsid', windll['OLE32.dll']), ((1, 'riid'),(1, 'pClsid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoRegisterPSClsid():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid))(('CoRegisterPSClsid', windll['OLE32.dll']), ((1, 'riid'),(1, 'rclsid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoRegisterSurrogate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.ISurrogate_head)(('CoRegisterSurrogate', windll['OLE32.dll']), ((1, 'pSurrogate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoDisconnectObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32)(('CoDisconnectObject', windll['OLE32.dll']), ((1, 'pUnk'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoLockObjectExternal():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.BOOL,win32more.Foundation.BOOL)(('CoLockObjectExternal', windll['OLE32.dll']), ((1, 'pUnk'),(1, 'fLock'),(1, 'fLastUnlockReleases'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoIsHandlerConnected():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Com.IUnknown_head)(('CoIsHandlerConnected', windll['OLE32.dll']), ((1, 'pUnk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoCreateFreeThreadedMarshaler():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.IUnknown_head))(('CoCreateFreeThreadedMarshaler', windll['OLE32.dll']), ((1, 'punkOuter'),(1, 'ppunkMarshal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoFreeUnusedLibraries():
    try:
        return WINFUNCTYPE(Void,)(('CoFreeUnusedLibraries', windll['OLE32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoFreeUnusedLibrariesEx():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32)(('CoFreeUnusedLibrariesEx', windll['OLE32.dll']), ((1, 'dwUnloadDelay'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoDisconnectContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(('CoDisconnectContext', windll['OLE32.dll']), ((1, 'dwTimeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInitializeSecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Security.PSECURITY_DESCRIPTOR,Int32,POINTER(win32more.System.Com.SOLE_AUTHENTICATION_SERVICE_head),c_void_p,win32more.System.Com.RPC_C_AUTHN_LEVEL,win32more.System.Com.RPC_C_IMP_LEVEL,c_void_p,win32more.System.Com.EOLE_AUTHENTICATION_CAPABILITIES,c_void_p)(('CoInitializeSecurity', windll['OLE32.dll']), ((1, 'pSecDesc'),(1, 'cAuthSvc'),(1, 'asAuthSvc'),(1, 'pReserved1'),(1, 'dwAuthnLevel'),(1, 'dwImpLevel'),(1, 'pAuthList'),(1, 'dwCapabilities'),(1, 'pReserved3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetCallContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(('CoGetCallContext', windll['OLE32.dll']), ((1, 'riid'),(1, 'ppInterface'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoQueryProxyBlanket():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Foundation.PWSTR),POINTER(UInt32),POINTER(UInt32),POINTER(c_void_p),POINTER(UInt32))(('CoQueryProxyBlanket', windll['OLE32.dll']), ((1, 'pProxy'),(1, 'pwAuthnSvc'),(1, 'pAuthzSvc'),(1, 'pServerPrincName'),(1, 'pAuthnLevel'),(1, 'pImpLevel'),(1, 'pAuthInfo'),(1, 'pCapabilites'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoSetProxyBlanket():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.System.Com.RPC_C_AUTHN_LEVEL,win32more.System.Com.RPC_C_IMP_LEVEL,c_void_p,win32more.System.Com.EOLE_AUTHENTICATION_CAPABILITIES)(('CoSetProxyBlanket', windll['OLE32.dll']), ((1, 'pProxy'),(1, 'dwAuthnSvc'),(1, 'dwAuthzSvc'),(1, 'pServerPrincName'),(1, 'dwAuthnLevel'),(1, 'dwImpLevel'),(1, 'pAuthInfo'),(1, 'dwCapabilities'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoCopyProxy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.IUnknown_head))(('CoCopyProxy', windll['OLE32.dll']), ((1, 'pProxy'),(1, 'ppCopy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoQueryClientBlanket():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Foundation.PWSTR),POINTER(UInt32),POINTER(UInt32),POINTER(c_void_p),POINTER(UInt32))(('CoQueryClientBlanket', windll['OLE32.dll']), ((1, 'pAuthnSvc'),(1, 'pAuthzSvc'),(1, 'pServerPrincName'),(1, 'pAuthnLevel'),(1, 'pImpLevel'),(1, 'pPrivs'),(1, 'pCapabilities'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoImpersonateClient():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,)(('CoImpersonateClient', windll['OLE32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoRevertToSelf():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,)(('CoRevertToSelf', windll['OLE32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoQueryAuthenticationServices():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(win32more.System.Com.SOLE_AUTHENTICATION_SERVICE_head)))(('CoQueryAuthenticationServices', windll['OLE32.dll']), ((1, 'pcAuthSvc'),(1, 'asAuthSvc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoSwitchCallContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.IUnknown_head))(('CoSwitchCallContext', windll['OLE32.dll']), ((1, 'pNewObject'),(1, 'ppOldObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoCreateInstance():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,win32more.System.Com.CLSCTX,POINTER(Guid),POINTER(c_void_p))(('CoCreateInstance', windll['OLE32.dll']), ((1, 'rclsid'),(1, 'pUnkOuter'),(1, 'dwClsContext'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoCreateInstanceEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,win32more.System.Com.CLSCTX,POINTER(win32more.System.Com.COSERVERINFO_head),UInt32,POINTER(win32more.System.Com.MULTI_QI_head))(('CoCreateInstanceEx', windll['OLE32.dll']), ((1, 'Clsid'),(1, 'punkOuter'),(1, 'dwClsCtx'),(1, 'pServerInfo'),(1, 'dwCount'),(1, 'pResults'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoCreateInstanceFromApp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,win32more.System.Com.CLSCTX,c_void_p,UInt32,POINTER(win32more.System.Com.MULTI_QI_head))(('CoCreateInstanceFromApp', windll['OLE32.dll']), ((1, 'Clsid'),(1, 'punkOuter'),(1, 'dwClsCtx'),(1, 'reserved'),(1, 'dwCount'),(1, 'pResults'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoRegisterActivationFilter():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IActivationFilter_head)(('CoRegisterActivationFilter', windll['OLE32.dll']), ((1, 'pActivationFilter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetCancelObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p))(('CoGetCancelObject', windll['OLE32.dll']), ((1, 'dwThreadId'),(1, 'iid'),(1, 'ppUnk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoSetCancelObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(('CoSetCancelObject', windll['OLE32.dll']), ((1, 'pUnk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoCancelCall():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32)(('CoCancelCall', windll['OLE32.dll']), ((1, 'dwThreadId'),(1, 'ulTimeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoTestCancel():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,)(('CoTestCancel', windll['OLE32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoEnableCallCancellation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p)(('CoEnableCallCancellation', windll['OLE32.dll']), ((1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoDisableCallCancellation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p)(('CoDisableCallCancellation', windll['OLE32.dll']), ((1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StringFromCLSID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.PWSTR))(('StringFromCLSID', windll['OLE32.dll']), ((1, 'rclsid'),(1, 'lplpsz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLSIDFromString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid))(('CLSIDFromString', windll['OLE32.dll']), ((1, 'lpsz'),(1, 'pclsid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StringFromIID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.PWSTR))(('StringFromIID', windll['OLE32.dll']), ((1, 'rclsid'),(1, 'lplpsz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IIDFromString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid))(('IIDFromString', windll['OLE32.dll']), ((1, 'lpsz'),(1, 'lpiid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ProgIDFromCLSID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.PWSTR))(('ProgIDFromCLSID', windll['OLE32.dll']), ((1, 'clsid'),(1, 'lplpszProgID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLSIDFromProgID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid))(('CLSIDFromProgID', windll['OLE32.dll']), ((1, 'lpszProgID'),(1, 'lpclsid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StringFromGUID2():
    try:
        return WINFUNCTYPE(Int32,POINTER(Guid),win32more.Foundation.PWSTR,Int32)(('StringFromGUID2', windll['OLE32.dll']), ((1, 'rguid'),(1, 'lpsz'),(1, 'cchMax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoCreateGuid():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(('CoCreateGuid', windll['OLE32.dll']), ((1, 'pguid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoWaitForMultipleHandles():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.HANDLE),POINTER(UInt32))(('CoWaitForMultipleHandles', windll['OLE32.dll']), ((1, 'dwFlags'),(1, 'dwTimeout'),(1, 'cHandles'),(1, 'pHandles'),(1, 'lpdwindex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoWaitForMultipleObjects():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.HANDLE),POINTER(UInt32))(('CoWaitForMultipleObjects', windll['OLE32.dll']), ((1, 'dwFlags'),(1, 'dwTimeout'),(1, 'cHandles'),(1, 'pHandles'),(1, 'lpdwindex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetTreatAsClass():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid))(('CoGetTreatAsClass', windll['OLE32.dll']), ((1, 'clsidOld'),(1, 'pClsidNew'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInvalidateRemoteMachineBindings():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(('CoInvalidateRemoteMachineBindings', windll['OLE32.dll']), ((1, 'pszMachineName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoTaskMemAlloc():
    try:
        return WINFUNCTYPE(c_void_p,UIntPtr)(('CoTaskMemAlloc', windll['OLE32.dll']), ((1, 'cb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoTaskMemRealloc():
    try:
        return WINFUNCTYPE(c_void_p,c_void_p,UIntPtr)(('CoTaskMemRealloc', windll['OLE32.dll']), ((1, 'pv'),(1, 'cb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoTaskMemFree():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('CoTaskMemFree', windll['OLE32.dll']), ((1, 'pv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoRegisterDeviceCatalog():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.CO_DEVICE_CATALOG_COOKIE))(('CoRegisterDeviceCatalog', windll['OLE32.dll']), ((1, 'deviceInstanceId'),(1, 'cookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoRevokeDeviceCatalog():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CO_DEVICE_CATALOG_COOKIE)(('CoRevokeDeviceCatalog', windll['OLE32.dll']), ((1, 'cookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateUri():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.URI_CREATE_FLAGS,UIntPtr,POINTER(win32more.System.Com.IUri_head))(('CreateUri', windll['URLMON.dll']), ((1, 'pwzURI'),(1, 'dwFlags'),(1, 'dwReserved'),(1, 'ppURI'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateUriWithFragment():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UIntPtr,POINTER(win32more.System.Com.IUri_head))(('CreateUriWithFragment', windll['URLMON.dll']), ((1, 'pwzURI'),(1, 'pwzFragment'),(1, 'dwFlags'),(1, 'dwReserved'),(1, 'ppURI'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateUriFromMultiByteString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,UInt32,UInt32,UInt32,UIntPtr,POINTER(win32more.System.Com.IUri_head))(('CreateUriFromMultiByteString', windll['urlmon.dll']), ((1, 'pszANSIInputUri'),(1, 'dwEncodingFlags'),(1, 'dwCodePage'),(1, 'dwCreateFlags'),(1, 'dwReserved'),(1, 'ppUri'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateIUriBuilder():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUri_head,UInt32,UIntPtr,POINTER(win32more.System.Com.IUriBuilder_head))(('CreateIUriBuilder', windll['URLMON.dll']), ((1, 'pIUri'),(1, 'dwFlags'),(1, 'dwReserved'),(1, 'ppIUriBuilder'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetErrorInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.IErrorInfo_head)(('SetErrorInfo', windll['OLEAUT32.dll']), ((1, 'dwReserved'),(1, 'perrinfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetErrorInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IErrorInfo_head))(('GetErrorInfo', windll['OLEAUT32.dll']), ((1, 'dwReserved'),(1, 'pperrinfo'),))
    except (FileNotFoundError, AttributeError):
        return None
ApplicationType = Int32
ApplicationType_ServerApplication = 0
ApplicationType_LibraryApplication = 1
APTTYPE = Int32
APTTYPE_CURRENT = -1
APTTYPE_STA = 0
APTTYPE_MTA = 1
APTTYPE_NA = 2
APTTYPE_MAINSTA = 3
APTTYPEQUALIFIER = Int32
APTTYPEQUALIFIER_NONE = 0
APTTYPEQUALIFIER_IMPLICIT_MTA = 1
APTTYPEQUALIFIER_NA_ON_MTA = 2
APTTYPEQUALIFIER_NA_ON_STA = 3
APTTYPEQUALIFIER_NA_ON_IMPLICIT_MTA = 4
APTTYPEQUALIFIER_NA_ON_MAINSTA = 5
APTTYPEQUALIFIER_APPLICATION_STA = 6
APTTYPEQUALIFIER_RESERVED_1 = 7
def _define_AsyncIAdviseSink_head():
    class AsyncIAdviseSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000150-0000-0000-c0-00-00-00-00-00-00-46')
    return AsyncIAdviseSink
def _define_AsyncIAdviseSink():
    AsyncIAdviseSink = win32more.System.Com.AsyncIAdviseSink_head
    AsyncIAdviseSink.Begin_OnDataChange = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.System.Com.FORMATETC_head),POINTER(win32more.System.Com.STGMEDIUM_head))(3, 'Begin_OnDataChange', ((1, 'pFormatetc'),(1, 'pStgmed'),)))
    AsyncIAdviseSink.Finish_OnDataChange = COMMETHOD(WINFUNCTYPE(Void,)(4, 'Finish_OnDataChange', ()))
    AsyncIAdviseSink.Begin_OnViewChange = COMMETHOD(WINFUNCTYPE(Void,UInt32,Int32)(5, 'Begin_OnViewChange', ((1, 'dwAspect'),(1, 'lindex'),)))
    AsyncIAdviseSink.Finish_OnViewChange = COMMETHOD(WINFUNCTYPE(Void,)(6, 'Finish_OnViewChange', ()))
    AsyncIAdviseSink.Begin_OnRename = COMMETHOD(WINFUNCTYPE(Void,win32more.System.Com.IMoniker_head)(7, 'Begin_OnRename', ((1, 'pmk'),)))
    AsyncIAdviseSink.Finish_OnRename = COMMETHOD(WINFUNCTYPE(Void,)(8, 'Finish_OnRename', ()))
    AsyncIAdviseSink.Begin_OnSave = COMMETHOD(WINFUNCTYPE(Void,)(9, 'Begin_OnSave', ()))
    AsyncIAdviseSink.Finish_OnSave = COMMETHOD(WINFUNCTYPE(Void,)(10, 'Finish_OnSave', ()))
    AsyncIAdviseSink.Begin_OnClose = COMMETHOD(WINFUNCTYPE(Void,)(11, 'Begin_OnClose', ()))
    AsyncIAdviseSink.Finish_OnClose = COMMETHOD(WINFUNCTYPE(Void,)(12, 'Finish_OnClose', ()))
    win32more.System.Com.IUnknown
    return AsyncIAdviseSink
def _define_AsyncIAdviseSink2_head():
    class AsyncIAdviseSink2(win32more.System.Com.AsyncIAdviseSink_head):
        Guid = Guid('00000151-0000-0000-c0-00-00-00-00-00-00-46')
    return AsyncIAdviseSink2
def _define_AsyncIAdviseSink2():
    AsyncIAdviseSink2 = win32more.System.Com.AsyncIAdviseSink2_head
    AsyncIAdviseSink2.Begin_OnLinkSrcChange = COMMETHOD(WINFUNCTYPE(Void,win32more.System.Com.IMoniker_head)(13, 'Begin_OnLinkSrcChange', ((1, 'pmk'),)))
    AsyncIAdviseSink2.Finish_OnLinkSrcChange = COMMETHOD(WINFUNCTYPE(Void,)(14, 'Finish_OnLinkSrcChange', ()))
    win32more.System.Com.AsyncIAdviseSink
    return AsyncIAdviseSink2
def _define_AsyncIMultiQI_head():
    class AsyncIMultiQI(win32more.System.Com.IUnknown_head):
        Guid = Guid('000e0020-0000-0000-c0-00-00-00-00-00-00-46')
    return AsyncIMultiQI
def _define_AsyncIMultiQI():
    AsyncIMultiQI = win32more.System.Com.AsyncIMultiQI_head
    AsyncIMultiQI.Begin_QueryMultipleInterfaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.MULTI_QI_head))(3, 'Begin_QueryMultipleInterfaces', ((1, 'cMQIs'),(1, 'pMQIs'),)))
    AsyncIMultiQI.Finish_QueryMultipleInterfaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.MULTI_QI_head))(4, 'Finish_QueryMultipleInterfaces', ((1, 'pMQIs'),)))
    win32more.System.Com.IUnknown
    return AsyncIMultiQI
def _define_AsyncIPipeByte_head():
    class AsyncIPipeByte(win32more.System.Com.IUnknown_head):
        Guid = Guid('db2f3acb-2f86-11d1-8e-04-00-c0-4f-b9-98-9a')
    return AsyncIPipeByte
def _define_AsyncIPipeByte():
    AsyncIPipeByte = win32more.System.Com.AsyncIPipeByte_head
    AsyncIPipeByte.Begin_Pull = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(3, 'Begin_Pull', ((1, 'cRequest'),)))
    AsyncIPipeByte.Finish_Pull = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,POINTER(UInt32))(4, 'Finish_Pull', ((1, 'buf'),(1, 'pcReturned'),)))
    AsyncIPipeByte.Begin_Push = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32)(5, 'Begin_Push', ((1, 'buf'),(1, 'cSent'),)))
    AsyncIPipeByte.Finish_Push = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'Finish_Push', ()))
    win32more.System.Com.IUnknown
    return AsyncIPipeByte
def _define_AsyncIPipeDouble_head():
    class AsyncIPipeDouble(win32more.System.Com.IUnknown_head):
        Guid = Guid('db2f3acf-2f86-11d1-8e-04-00-c0-4f-b9-98-9a')
    return AsyncIPipeDouble
def _define_AsyncIPipeDouble():
    AsyncIPipeDouble = win32more.System.Com.AsyncIPipeDouble_head
    AsyncIPipeDouble.Begin_Pull = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(3, 'Begin_Pull', ((1, 'cRequest'),)))
    AsyncIPipeDouble.Finish_Pull = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),POINTER(UInt32))(4, 'Finish_Pull', ((1, 'buf'),(1, 'pcReturned'),)))
    AsyncIPipeDouble.Begin_Push = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),UInt32)(5, 'Begin_Push', ((1, 'buf'),(1, 'cSent'),)))
    AsyncIPipeDouble.Finish_Push = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'Finish_Push', ()))
    win32more.System.Com.IUnknown
    return AsyncIPipeDouble
def _define_AsyncIPipeLong_head():
    class AsyncIPipeLong(win32more.System.Com.IUnknown_head):
        Guid = Guid('db2f3acd-2f86-11d1-8e-04-00-c0-4f-b9-98-9a')
    return AsyncIPipeLong
def _define_AsyncIPipeLong():
    AsyncIPipeLong = win32more.System.Com.AsyncIPipeLong_head
    AsyncIPipeLong.Begin_Pull = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(3, 'Begin_Pull', ((1, 'cRequest'),)))
    AsyncIPipeLong.Finish_Pull = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(UInt32))(4, 'Finish_Pull', ((1, 'buf'),(1, 'pcReturned'),)))
    AsyncIPipeLong.Begin_Push = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),UInt32)(5, 'Begin_Push', ((1, 'buf'),(1, 'cSent'),)))
    AsyncIPipeLong.Finish_Push = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'Finish_Push', ()))
    win32more.System.Com.IUnknown
    return AsyncIPipeLong
def _define_AsyncIUnknown_head():
    class AsyncIUnknown(win32more.System.Com.IUnknown_head):
        Guid = Guid('000e0000-0000-0000-c0-00-00-00-00-00-00-46')
    return AsyncIUnknown
def _define_AsyncIUnknown():
    AsyncIUnknown = win32more.System.Com.AsyncIUnknown_head
    AsyncIUnknown.Begin_QueryInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'Begin_QueryInterface', ((1, 'riid'),)))
    AsyncIUnknown.Finish_QueryInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_void_p))(4, 'Finish_QueryInterface', ((1, 'ppvObject'),)))
    AsyncIUnknown.Begin_AddRef = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Begin_AddRef', ()))
    AsyncIUnknown.Finish_AddRef = COMMETHOD(WINFUNCTYPE(UInt32,)(6, 'Finish_AddRef', ()))
    AsyncIUnknown.Begin_Release = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'Begin_Release', ()))
    AsyncIUnknown.Finish_Release = COMMETHOD(WINFUNCTYPE(UInt32,)(8, 'Finish_Release', ()))
    win32more.System.Com.IUnknown
    return AsyncIUnknown
def _define_AUTHENTICATEINFO_head():
    class AUTHENTICATEINFO(Structure):
        pass
    return AUTHENTICATEINFO
def _define_AUTHENTICATEINFO():
    AUTHENTICATEINFO = win32more.System.Com.AUTHENTICATEINFO_head
    AUTHENTICATEINFO._fields_ = [
        ('dwFlags', UInt32),
        ('dwReserved', UInt32),
    ]
    return AUTHENTICATEINFO
BIND_FLAGS = Int32
BIND_MAYBOTHERUSER = 1
BIND_JUSTTESTEXISTENCE = 2
def _define_BIND_OPTS_head():
    class BIND_OPTS(Structure):
        pass
    return BIND_OPTS
def _define_BIND_OPTS():
    BIND_OPTS = win32more.System.Com.BIND_OPTS_head
    BIND_OPTS._fields_ = [
        ('cbStruct', UInt32),
        ('grfFlags', UInt32),
        ('grfMode', UInt32),
        ('dwTickCountDeadline', UInt32),
    ]
    return BIND_OPTS
def _define_BIND_OPTS2_head():
    class BIND_OPTS2(Structure):
        pass
    return BIND_OPTS2
def _define_BIND_OPTS2():
    BIND_OPTS2 = win32more.System.Com.BIND_OPTS2_head
    BIND_OPTS2._fields_ = [
        ('Base', win32more.System.Com.BIND_OPTS),
        ('dwTrackFlags', UInt32),
        ('dwClassContext', UInt32),
        ('locale', UInt32),
        ('pServerInfo', POINTER(win32more.System.Com.COSERVERINFO_head)),
    ]
    return BIND_OPTS2
def _define_BIND_OPTS3_head():
    class BIND_OPTS3(Structure):
        pass
    return BIND_OPTS3
def _define_BIND_OPTS3():
    BIND_OPTS3 = win32more.System.Com.BIND_OPTS3_head
    BIND_OPTS3._fields_ = [
        ('Base', win32more.System.Com.BIND_OPTS2),
        ('hwnd', win32more.Foundation.HWND),
    ]
    return BIND_OPTS3
def _define_BINDINFO_head():
    class BINDINFO(Structure):
        pass
    return BINDINFO
def _define_BINDINFO():
    BINDINFO = win32more.System.Com.BINDINFO_head
    BINDINFO._fields_ = [
        ('cbSize', UInt32),
        ('szExtraInfo', win32more.Foundation.PWSTR),
        ('stgmedData', win32more.System.Com.STGMEDIUM),
        ('grfBindInfoF', UInt32),
        ('dwBindVerb', UInt32),
        ('szCustomVerb', win32more.Foundation.PWSTR),
        ('cbstgmedData', UInt32),
        ('dwOptions', UInt32),
        ('dwOptionsFlags', UInt32),
        ('dwCodePage', UInt32),
        ('securityAttributes', win32more.Security.SECURITY_ATTRIBUTES),
        ('iid', Guid),
        ('pUnk', win32more.System.Com.IUnknown_head),
        ('dwReserved', UInt32),
    ]
    return BINDINFO
BINDINFOF = Int32
BINDINFOF_URLENCODESTGMEDDATA = 1
BINDINFOF_URLENCODEDEXTRAINFO = 2
def _define_BINDPTR_head():
    class BINDPTR(Union):
        pass
    return BINDPTR
def _define_BINDPTR():
    BINDPTR = win32more.System.Com.BINDPTR_head
    BINDPTR._fields_ = [
        ('lpfuncdesc', POINTER(win32more.System.Com.FUNCDESC_head)),
        ('lpvardesc', POINTER(win32more.System.Com.VARDESC_head)),
        ('lptcomp', win32more.System.Com.ITypeComp_head),
    ]
    return BINDPTR
def _define_BLOB_head():
    class BLOB(Structure):
        pass
    return BLOB
def _define_BLOB():
    BLOB = win32more.System.Com.BLOB_head
    BLOB._fields_ = [
        ('cbSize', UInt32),
        ('pBlobData', c_char_p_no),
    ]
    return BLOB
def _define_BYTE_BLOB_head():
    class BYTE_BLOB(Structure):
        pass
    return BYTE_BLOB
def _define_BYTE_BLOB():
    BYTE_BLOB = win32more.System.Com.BYTE_BLOB_head
    BYTE_BLOB._fields_ = [
        ('clSize', UInt32),
        ('abData', Byte * 1),
    ]
    return BYTE_BLOB
def _define_BYTE_SIZEDARR_head():
    class BYTE_SIZEDARR(Structure):
        pass
    return BYTE_SIZEDARR
def _define_BYTE_SIZEDARR():
    BYTE_SIZEDARR = win32more.System.Com.BYTE_SIZEDARR_head
    BYTE_SIZEDARR._fields_ = [
        ('clSize', UInt32),
        ('pData', c_char_p_no),
    ]
    return BYTE_SIZEDARR
CALLCONV = Int32
CC_FASTCALL = 0
CC_CDECL = 1
CC_MSCPASCAL = 2
CC_PASCAL = 2
CC_MACPASCAL = 3
CC_STDCALL = 4
CC_FPFASTCALL = 5
CC_SYSCALL = 6
CC_MPWCDECL = 7
CC_MPWPASCAL = 8
CC_MAX = 9
CALLTYPE = Int32
CALLTYPE_TOPLEVEL = 1
CALLTYPE_NESTED = 2
CALLTYPE_ASYNC = 3
CALLTYPE_TOPLEVEL_CALLPENDING = 4
CALLTYPE_ASYNC_CALLPENDING = 5
def _define_CATEGORYINFO_head():
    class CATEGORYINFO(Structure):
        pass
    return CATEGORYINFO
def _define_CATEGORYINFO():
    CATEGORYINFO = win32more.System.Com.CATEGORYINFO_head
    CATEGORYINFO._fields_ = [
        ('catid', Guid),
        ('lcid', UInt32),
        ('szDescription', Char * 128),
    ]
    return CATEGORYINFO
CLSCTX = UInt32
CLSCTX_INPROC_SERVER = 1
CLSCTX_INPROC_HANDLER = 2
CLSCTX_LOCAL_SERVER = 4
CLSCTX_INPROC_SERVER16 = 8
CLSCTX_REMOTE_SERVER = 16
CLSCTX_INPROC_HANDLER16 = 32
CLSCTX_RESERVED1 = 64
CLSCTX_RESERVED2 = 128
CLSCTX_RESERVED3 = 256
CLSCTX_RESERVED4 = 512
CLSCTX_NO_CODE_DOWNLOAD = 1024
CLSCTX_RESERVED5 = 2048
CLSCTX_NO_CUSTOM_MARSHAL = 4096
CLSCTX_ENABLE_CODE_DOWNLOAD = 8192
CLSCTX_NO_FAILURE_LOG = 16384
CLSCTX_DISABLE_AAA = 32768
CLSCTX_ENABLE_AAA = 65536
CLSCTX_FROM_DEFAULT_CONTEXT = 131072
CLSCTX_ACTIVATE_X86_SERVER = 262144
CLSCTX_ACTIVATE_32_BIT_SERVER = 262144
CLSCTX_ACTIVATE_64_BIT_SERVER = 524288
CLSCTX_ENABLE_CLOAKING = 1048576
CLSCTX_APPCONTAINER = 4194304
CLSCTX_ACTIVATE_AAA_AS_IU = 8388608
CLSCTX_RESERVED6 = 16777216
CLSCTX_ACTIVATE_ARM32_SERVER = 33554432
CLSCTX_PS_DLL = 2147483648
CLSCTX_ALL = 23
CLSCTX_SERVER = 21
CO_DEVICE_CATALOG_COOKIE = IntPtr
CO_MARSHALING_CONTEXT_ATTRIBUTES = Int32
CO_MARSHALING_SOURCE_IS_APP_CONTAINER = 0
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_1 = -2147483648
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_2 = -2147483647
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_3 = -2147483646
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_4 = -2147483645
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_5 = -2147483644
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_6 = -2147483643
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_7 = -2147483642
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_8 = -2147483641
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_9 = -2147483640
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_10 = -2147483639
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_11 = -2147483638
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_12 = -2147483637
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_13 = -2147483636
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_14 = -2147483635
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_15 = -2147483634
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_16 = -2147483633
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_17 = -2147483632
CO_MARSHALING_CONTEXT_ATTRIBUTE_RESERVED_18 = -2147483631
CO_MTA_USAGE_COOKIE = IntPtr
def _define_COAUTHIDENTITY_head():
    class COAUTHIDENTITY(Structure):
        pass
    return COAUTHIDENTITY
def _define_COAUTHIDENTITY():
    COAUTHIDENTITY = win32more.System.Com.COAUTHIDENTITY_head
    COAUTHIDENTITY._fields_ = [
        ('User', POINTER(UInt16)),
        ('UserLength', UInt32),
        ('Domain', POINTER(UInt16)),
        ('DomainLength', UInt32),
        ('Password', POINTER(UInt16)),
        ('PasswordLength', UInt32),
        ('Flags', UInt32),
    ]
    return COAUTHIDENTITY
def _define_COAUTHINFO_head():
    class COAUTHINFO(Structure):
        pass
    return COAUTHINFO
def _define_COAUTHINFO():
    COAUTHINFO = win32more.System.Com.COAUTHINFO_head
    COAUTHINFO._fields_ = [
        ('dwAuthnSvc', UInt32),
        ('dwAuthzSvc', UInt32),
        ('pwszServerPrincName', win32more.Foundation.PWSTR),
        ('dwAuthnLevel', UInt32),
        ('dwImpersonationLevel', UInt32),
        ('pAuthIdentityData', POINTER(win32more.System.Com.COAUTHIDENTITY_head)),
        ('dwCapabilities', UInt32),
    ]
    return COAUTHINFO
COINIT = UInt32
COINIT_APARTMENTTHREADED = 2
COINIT_MULTITHREADED = 0
COINIT_DISABLE_OLE1DDE = 4
COINIT_SPEED_OVER_MEMORY = 8
COINITBASE = Int32
COINITBASE_MULTITHREADED = 0
def _define_ComCallData_head():
    class ComCallData(Structure):
        pass
    return ComCallData
def _define_ComCallData():
    ComCallData = win32more.System.Com.ComCallData_head
    ComCallData._fields_ = [
        ('dwDispid', UInt32),
        ('dwReserved', UInt32),
        ('pUserDefined', c_void_p),
    ]
    return ComCallData
COMSD = Int32
SD_LAUNCHPERMISSIONS = 0
SD_ACCESSPERMISSIONS = 1
SD_LAUNCHRESTRICTIONS = 2
SD_ACCESSRESTRICTIONS = 3
def _define_CONNECTDATA_head():
    class CONNECTDATA(Structure):
        pass
    return CONNECTDATA
def _define_CONNECTDATA():
    CONNECTDATA = win32more.System.Com.CONNECTDATA_head
    CONNECTDATA._fields_ = [
        ('pUnk', win32more.System.Com.IUnknown_head),
        ('dwCookie', UInt32),
    ]
    return CONNECTDATA
def _define_COSERVERINFO_head():
    class COSERVERINFO(Structure):
        pass
    return COSERVERINFO
def _define_COSERVERINFO():
    COSERVERINFO = win32more.System.Com.COSERVERINFO_head
    COSERVERINFO._fields_ = [
        ('dwReserved1', UInt32),
        ('pwszName', win32more.Foundation.PWSTR),
        ('pAuthInfo', POINTER(win32more.System.Com.COAUTHINFO_head)),
        ('dwReserved2', UInt32),
    ]
    return COSERVERINFO
COWAIT_FLAGS = Int32
COWAIT_DEFAULT = 0
COWAIT_WAITALL = 1
COWAIT_ALERTABLE = 2
COWAIT_INPUTAVAILABLE = 4
COWAIT_DISPATCH_CALLS = 8
COWAIT_DISPATCH_WINDOW_MESSAGES = 16
def _define_CSPLATFORM_head():
    class CSPLATFORM(Structure):
        pass
    return CSPLATFORM
def _define_CSPLATFORM():
    CSPLATFORM = win32more.System.Com.CSPLATFORM_head
    CSPLATFORM._fields_ = [
        ('dwPlatformId', UInt32),
        ('dwVersionHi', UInt32),
        ('dwVersionLo', UInt32),
        ('dwProcessorArch', UInt32),
    ]
    return CSPLATFORM
def _define_CUSTDATA_head():
    class CUSTDATA(Structure):
        pass
    return CUSTDATA
def _define_CUSTDATA():
    CUSTDATA = win32more.System.Com.CUSTDATA_head
    CUSTDATA._fields_ = [
        ('cCustData', UInt32),
        ('prgCustData', POINTER(win32more.System.Com.CUSTDATAITEM_head)),
    ]
    return CUSTDATA
def _define_CUSTDATAITEM_head():
    class CUSTDATAITEM(Structure):
        pass
    return CUSTDATAITEM
def _define_CUSTDATAITEM():
    CUSTDATAITEM = win32more.System.Com.CUSTDATAITEM_head
    CUSTDATAITEM._fields_ = [
        ('guid', Guid),
        ('varValue', win32more.System.Com.VARIANT),
    ]
    return CUSTDATAITEM
CWMO_FLAGS = Int32
CWMO_DEFAULT = 0
CWMO_DISPATCH_CALLS = 1
CWMO_DISPATCH_WINDOW_MESSAGES = 2
def _define_CY_head():
    class CY(Union):
        pass
    return CY
def _define_CY():
    CY = win32more.System.Com.CY_head
    class CY__Anonymous_e__Struct(Structure):
        pass
    CY__Anonymous_e__Struct._fields_ = [
        ('Lo', UInt32),
        ('Hi', Int32),
    ]
    CY._anonymous_ = [
        'Anonymous',
    ]
    CY._fields_ = [
        ('Anonymous', CY__Anonymous_e__Struct),
        ('int64', Int64),
    ]
    return CY
DATADIR = Int32
DATADIR_GET = 1
DATADIR_SET = 2
DCOM_CALL_STATE = Int32
DCOM_NONE = 0
DCOM_CALL_COMPLETE = 1
DCOM_CALL_CANCELED = 2
DESCKIND = Int32
DESCKIND_NONE = 0
DESCKIND_FUNCDESC = 1
DESCKIND_VARDESC = 2
DESCKIND_TYPECOMP = 3
DESCKIND_IMPLICITAPPOBJ = 4
DESCKIND_MAX = 5
DISPATCH_FLAGS = UInt16
DISPATCH_METHOD = 1
DISPATCH_PROPERTYGET = 2
DISPATCH_PROPERTYPUT = 4
DISPATCH_PROPERTYPUTREF = 8
def _define_DISPPARAMS_head():
    class DISPPARAMS(Structure):
        pass
    return DISPPARAMS
def _define_DISPPARAMS():
    DISPPARAMS = win32more.System.Com.DISPPARAMS_head
    DISPPARAMS._fields_ = [
        ('rgvarg', POINTER(win32more.System.Com.VARIANT_head)),
        ('rgdispidNamedArgs', POINTER(Int32)),
        ('cArgs', UInt32),
        ('cNamedArgs', UInt32),
    ]
    return DISPPARAMS
DVASPECT = UInt32
DVASPECT_CONTENT = 1
DVASPECT_THUMBNAIL = 2
DVASPECT_ICON = 4
DVASPECT_DOCPRINT = 8
DVASPECT_OPAQUE = 16
DVASPECT_TRANSPARENT = 32
def _define_DVTARGETDEVICE_head():
    class DVTARGETDEVICE(Structure):
        pass
    return DVTARGETDEVICE
def _define_DVTARGETDEVICE():
    DVTARGETDEVICE = win32more.System.Com.DVTARGETDEVICE_head
    DVTARGETDEVICE._fields_ = [
        ('tdSize', UInt32),
        ('tdDriverNameOffset', UInt16),
        ('tdDeviceNameOffset', UInt16),
        ('tdPortNameOffset', UInt16),
        ('tdExtDevmodeOffset', UInt16),
        ('tdData', Byte * 1),
    ]
    return DVTARGETDEVICE
def _define_DWORD_BLOB_head():
    class DWORD_BLOB(Structure):
        pass
    return DWORD_BLOB
def _define_DWORD_BLOB():
    DWORD_BLOB = win32more.System.Com.DWORD_BLOB_head
    DWORD_BLOB._fields_ = [
        ('clSize', UInt32),
        ('alData', UInt32 * 1),
    ]
    return DWORD_BLOB
def _define_DWORD_SIZEDARR_head():
    class DWORD_SIZEDARR(Structure):
        pass
    return DWORD_SIZEDARR
def _define_DWORD_SIZEDARR():
    DWORD_SIZEDARR = win32more.System.Com.DWORD_SIZEDARR_head
    DWORD_SIZEDARR._fields_ = [
        ('clSize', UInt32),
        ('pData', POINTER(UInt32)),
    ]
    return DWORD_SIZEDARR
def _define_ELEMDESC_head():
    class ELEMDESC(Structure):
        pass
    return ELEMDESC
def _define_ELEMDESC():
    ELEMDESC = win32more.System.Com.ELEMDESC_head
    class ELEMDESC__Anonymous_e__Union(Union):
        pass
    ELEMDESC__Anonymous_e__Union._fields_ = [
        ('idldesc', win32more.System.Com.IDLDESC),
        ('paramdesc', win32more.System.Ole.PARAMDESC),
    ]
    ELEMDESC._anonymous_ = [
        'Anonymous',
    ]
    ELEMDESC._fields_ = [
        ('tdesc', win32more.System.Com.TYPEDESC),
        ('Anonymous', ELEMDESC__Anonymous_e__Union),
    ]
    return ELEMDESC
EOLE_AUTHENTICATION_CAPABILITIES = Int32
EOAC_NONE = 0
EOAC_MUTUAL_AUTH = 1
EOAC_STATIC_CLOAKING = 32
EOAC_DYNAMIC_CLOAKING = 64
EOAC_ANY_AUTHORITY = 128
EOAC_MAKE_FULLSIC = 256
EOAC_DEFAULT = 2048
EOAC_SECURE_REFS = 2
EOAC_ACCESS_CONTROL = 4
EOAC_APPID = 8
EOAC_DYNAMIC = 16
EOAC_REQUIRE_FULLSIC = 512
EOAC_AUTO_IMPERSONATE = 1024
EOAC_DISABLE_AAA = 4096
EOAC_NO_CUSTOM_MARSHAL = 8192
EOAC_RESERVED1 = 16384
def _define_EXCEPINFO_head():
    class EXCEPINFO(Structure):
        pass
    return EXCEPINFO
def _define_EXCEPINFO():
    EXCEPINFO = win32more.System.Com.EXCEPINFO_head
    EXCEPINFO._fields_ = [
        ('wCode', UInt16),
        ('wReserved', UInt16),
        ('bstrSource', win32more.Foundation.BSTR),
        ('bstrDescription', win32more.Foundation.BSTR),
        ('bstrHelpFile', win32more.Foundation.BSTR),
        ('dwHelpContext', UInt32),
        ('pvReserved', c_void_p),
        ('pfnDeferredFillIn', win32more.System.Com.LPEXCEPFINO_DEFERRED_FILLIN),
        ('scode', Int32),
    ]
    return EXCEPINFO
EXTCONN = Int32
EXTCONN_STRONG = 1
EXTCONN_WEAK = 2
EXTCONN_CALLABLE = 4
def _define_FLAG_STGMEDIUM_head():
    class FLAG_STGMEDIUM(Structure):
        pass
    return FLAG_STGMEDIUM
def _define_FLAG_STGMEDIUM():
    FLAG_STGMEDIUM = win32more.System.Com.FLAG_STGMEDIUM_head
    FLAG_STGMEDIUM._fields_ = [
        ('ContextFlags', Int32),
        ('fPassOwnership', Int32),
        ('Stgmed', win32more.System.Com.STGMEDIUM),
    ]
    return FLAG_STGMEDIUM
def _define_FLAGGED_BYTE_BLOB_head():
    class FLAGGED_BYTE_BLOB(Structure):
        pass
    return FLAGGED_BYTE_BLOB
def _define_FLAGGED_BYTE_BLOB():
    FLAGGED_BYTE_BLOB = win32more.System.Com.FLAGGED_BYTE_BLOB_head
    FLAGGED_BYTE_BLOB._fields_ = [
        ('fFlags', UInt32),
        ('clSize', UInt32),
        ('abData', Byte * 1),
    ]
    return FLAGGED_BYTE_BLOB
def _define_FLAGGED_WORD_BLOB_head():
    class FLAGGED_WORD_BLOB(Structure):
        pass
    return FLAGGED_WORD_BLOB
def _define_FLAGGED_WORD_BLOB():
    FLAGGED_WORD_BLOB = win32more.System.Com.FLAGGED_WORD_BLOB_head
    FLAGGED_WORD_BLOB._fields_ = [
        ('fFlags', UInt32),
        ('clSize', UInt32),
        ('asData', UInt16 * 1),
    ]
    return FLAGGED_WORD_BLOB
def _define_FORMATETC_head():
    class FORMATETC(Structure):
        pass
    return FORMATETC
def _define_FORMATETC():
    FORMATETC = win32more.System.Com.FORMATETC_head
    FORMATETC._fields_ = [
        ('cfFormat', UInt16),
        ('ptd', POINTER(win32more.System.Com.DVTARGETDEVICE_head)),
        ('dwAspect', UInt32),
        ('lindex', Int32),
        ('tymed', UInt32),
    ]
    return FORMATETC
def _define_FUNCDESC_head():
    class FUNCDESC(Structure):
        pass
    return FUNCDESC
def _define_FUNCDESC():
    FUNCDESC = win32more.System.Com.FUNCDESC_head
    FUNCDESC._fields_ = [
        ('memid', Int32),
        ('lprgscode', POINTER(Int32)),
        ('lprgelemdescParam', POINTER(win32more.System.Com.ELEMDESC_head)),
        ('funckind', win32more.System.Com.FUNCKIND),
        ('invkind', win32more.System.Com.INVOKEKIND),
        ('callconv', win32more.System.Com.CALLCONV),
        ('cParams', Int16),
        ('cParamsOpt', Int16),
        ('oVft', Int16),
        ('cScodes', Int16),
        ('elemdescFunc', win32more.System.Com.ELEMDESC),
        ('wFuncFlags', win32more.System.Com.FUNCFLAGS),
    ]
    return FUNCDESC
FUNCFLAGS = UInt16
FUNCFLAG_FRESTRICTED = 1
FUNCFLAG_FSOURCE = 2
FUNCFLAG_FBINDABLE = 4
FUNCFLAG_FREQUESTEDIT = 8
FUNCFLAG_FDISPLAYBIND = 16
FUNCFLAG_FDEFAULTBIND = 32
FUNCFLAG_FHIDDEN = 64
FUNCFLAG_FUSESGETLASTERROR = 128
FUNCFLAG_FDEFAULTCOLLELEM = 256
FUNCFLAG_FUIDEFAULT = 512
FUNCFLAG_FNONBROWSABLE = 1024
FUNCFLAG_FREPLACEABLE = 2048
FUNCFLAG_FIMMEDIATEBIND = 4096
FUNCKIND = Int32
FUNC_VIRTUAL = 0
FUNC_PUREVIRTUAL = 1
FUNC_NONVIRTUAL = 2
FUNC_STATIC = 3
FUNC_DISPATCH = 4
def _define_GDI_OBJECT_head():
    class GDI_OBJECT(Structure):
        pass
    return GDI_OBJECT
def _define_GDI_OBJECT():
    GDI_OBJECT = win32more.System.Com.GDI_OBJECT_head
    class GDI_OBJECT__u_e__Struct(Union):
        pass
    GDI_OBJECT__u_e__Struct._fields_ = [
        ('hBitmap', POINTER(win32more.System.SystemServices.userHBITMAP_head)),
        ('hPalette', POINTER(win32more.System.SystemServices.userHPALETTE_head)),
        ('hGeneric', POINTER(win32more.System.SystemServices.userHGLOBAL_head)),
    ]
    GDI_OBJECT._fields_ = [
        ('ObjectType', UInt32),
        ('u', GDI_OBJECT__u_e__Struct),
    ]
    return GDI_OBJECT
GLOBALOPT_EH_VALUES = Int32
COMGLB_EXCEPTION_HANDLE = 0
COMGLB_EXCEPTION_DONOT_HANDLE_FATAL = 1
COMGLB_EXCEPTION_DONOT_HANDLE = 1
COMGLB_EXCEPTION_DONOT_HANDLE_ANY = 2
GLOBALOPT_PROPERTIES = Int32
COMGLB_EXCEPTION_HANDLING = 1
COMGLB_APPID = 2
COMGLB_RPC_THREADPOOL_SETTING = 3
COMGLB_RO_SETTINGS = 4
COMGLB_UNMARSHALING_POLICY = 5
COMGLB_PROPERTIES_RESERVED1 = 6
COMGLB_PROPERTIES_RESERVED2 = 7
COMGLB_PROPERTIES_RESERVED3 = 8
GLOBALOPT_RO_FLAGS = Int32
COMGLB_STA_MODALLOOP_REMOVE_TOUCH_MESSAGES = 1
COMGLB_STA_MODALLOOP_SHARED_QUEUE_REMOVE_INPUT_MESSAGES = 2
COMGLB_STA_MODALLOOP_SHARED_QUEUE_DONOT_REMOVE_INPUT_MESSAGES = 4
COMGLB_FAST_RUNDOWN = 8
COMGLB_RESERVED1 = 16
COMGLB_RESERVED2 = 32
COMGLB_RESERVED3 = 64
COMGLB_STA_MODALLOOP_SHARED_QUEUE_REORDER_POINTER_MESSAGES = 128
COMGLB_RESERVED4 = 256
COMGLB_RESERVED5 = 512
COMGLB_RESERVED6 = 1024
GLOBALOPT_RPCTP_VALUES = Int32
COMGLB_RPC_THREADPOOL_SETTING_DEFAULT_POOL = 0
COMGLB_RPC_THREADPOOL_SETTING_PRIVATE_POOL = 1
GLOBALOPT_UNMARSHALING_POLICY_VALUES = Int32
COMGLB_UNMARSHALING_POLICY_NORMAL = 0
COMGLB_UNMARSHALING_POLICY_STRONG = 1
COMGLB_UNMARSHALING_POLICY_HYBRID = 2
def _define_HYPER_SIZEDARR_head():
    class HYPER_SIZEDARR(Structure):
        pass
    return HYPER_SIZEDARR
def _define_HYPER_SIZEDARR():
    HYPER_SIZEDARR = win32more.System.Com.HYPER_SIZEDARR_head
    HYPER_SIZEDARR._fields_ = [
        ('clSize', UInt32),
        ('pData', POINTER(Int64)),
    ]
    return HYPER_SIZEDARR
def _define_IActivationFilter_head():
    class IActivationFilter(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000017-0000-0000-c0-00-00-00-00-00-00-46')
    return IActivationFilter
def _define_IActivationFilter():
    IActivationFilter = win32more.System.Com.IActivationFilter_head
    IActivationFilter.HandleActivation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(Guid))(3, 'HandleActivation', ((1, 'dwActivationType'),(1, 'rclsid'),(1, 'pReplacementClsId'),)))
    win32more.System.Com.IUnknown
    return IActivationFilter
def _define_IAddrExclusionControl_head():
    class IAddrExclusionControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000148-0000-0000-c0-00-00-00-00-00-00-46')
    return IAddrExclusionControl
def _define_IAddrExclusionControl():
    IAddrExclusionControl = win32more.System.Com.IAddrExclusionControl_head
    IAddrExclusionControl.GetCurrentAddrExclusionList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(3, 'GetCurrentAddrExclusionList', ((1, 'riid'),(1, 'ppEnumerator'),)))
    IAddrExclusionControl.UpdateAddrExclusionList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(4, 'UpdateAddrExclusionList', ((1, 'pEnumerator'),)))
    win32more.System.Com.IUnknown
    return IAddrExclusionControl
def _define_IAddrTrackingControl_head():
    class IAddrTrackingControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000147-0000-0000-c0-00-00-00-00-00-00-46')
    return IAddrTrackingControl
def _define_IAddrTrackingControl():
    IAddrTrackingControl = win32more.System.Com.IAddrTrackingControl_head
    IAddrTrackingControl.EnableCOMDynamicAddrTracking = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'EnableCOMDynamicAddrTracking', ()))
    IAddrTrackingControl.DisableCOMDynamicAddrTracking = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'DisableCOMDynamicAddrTracking', ()))
    win32more.System.Com.IUnknown
    return IAddrTrackingControl
def _define_IAdviseSink_head():
    class IAdviseSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000010f-0000-0000-c0-00-00-00-00-00-00-46')
    return IAdviseSink
def _define_IAdviseSink():
    IAdviseSink = win32more.System.Com.IAdviseSink_head
    IAdviseSink.OnDataChange = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.System.Com.FORMATETC_head),POINTER(win32more.System.Com.STGMEDIUM_head))(3, 'OnDataChange', ((1, 'pFormatetc'),(1, 'pStgmed'),)))
    IAdviseSink.OnViewChange = COMMETHOD(WINFUNCTYPE(Void,UInt32,Int32)(4, 'OnViewChange', ((1, 'dwAspect'),(1, 'lindex'),)))
    IAdviseSink.OnRename = COMMETHOD(WINFUNCTYPE(Void,win32more.System.Com.IMoniker_head)(5, 'OnRename', ((1, 'pmk'),)))
    IAdviseSink.OnSave = COMMETHOD(WINFUNCTYPE(Void,)(6, 'OnSave', ()))
    IAdviseSink.OnClose = COMMETHOD(WINFUNCTYPE(Void,)(7, 'OnClose', ()))
    win32more.System.Com.IUnknown
    return IAdviseSink
def _define_IAdviseSink2_head():
    class IAdviseSink2(win32more.System.Com.IAdviseSink_head):
        Guid = Guid('00000125-0000-0000-c0-00-00-00-00-00-00-46')
    return IAdviseSink2
def _define_IAdviseSink2():
    IAdviseSink2 = win32more.System.Com.IAdviseSink2_head
    IAdviseSink2.OnLinkSrcChange = COMMETHOD(WINFUNCTYPE(Void,win32more.System.Com.IMoniker_head)(8, 'OnLinkSrcChange', ((1, 'pmk'),)))
    win32more.System.Com.IAdviseSink
    return IAdviseSink2
def _define_IAgileObject_head():
    class IAgileObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('94ea2b94-e9cc-49e0-c0-ff-ee-64-ca-8f-5b-90')
    return IAgileObject
def _define_IAgileObject():
    IAgileObject = win32more.System.Com.IAgileObject_head
    win32more.System.Com.IUnknown
    return IAgileObject
def _define_IAsyncManager_head():
    class IAsyncManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000002a-0000-0000-c0-00-00-00-00-00-00-46')
    return IAsyncManager
def _define_IAsyncManager():
    IAsyncManager = win32more.System.Com.IAsyncManager_head
    IAsyncManager.CompleteCall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT)(3, 'CompleteCall', ((1, 'Result'),)))
    IAsyncManager.GetCallContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(4, 'GetCallContext', ((1, 'riid'),(1, 'pInterface'),)))
    IAsyncManager.GetState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(5, 'GetState', ((1, 'pulStateFlags'),)))
    win32more.System.Com.IUnknown
    return IAsyncManager
def _define_IAsyncRpcChannelBuffer_head():
    class IAsyncRpcChannelBuffer(win32more.System.Com.IRpcChannelBuffer2_head):
        Guid = Guid('a5029fb6-3c34-11d1-9c-99-00-c0-4f-b9-98-aa')
    return IAsyncRpcChannelBuffer
def _define_IAsyncRpcChannelBuffer():
    IAsyncRpcChannelBuffer = win32more.System.Com.IAsyncRpcChannelBuffer_head
    IAsyncRpcChannelBuffer.Send = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.RPCOLEMESSAGE_head),win32more.System.Com.ISynchronize_head,POINTER(UInt32))(9, 'Send', ((1, 'pMsg'),(1, 'pSync'),(1, 'pulStatus'),)))
    IAsyncRpcChannelBuffer.Receive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.RPCOLEMESSAGE_head),POINTER(UInt32))(10, 'Receive', ((1, 'pMsg'),(1, 'pulStatus'),)))
    IAsyncRpcChannelBuffer.GetDestCtxEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.RPCOLEMESSAGE_head),POINTER(UInt32),POINTER(c_void_p))(11, 'GetDestCtxEx', ((1, 'pMsg'),(1, 'pdwDestContext'),(1, 'ppvDestContext'),)))
    win32more.System.Com.IRpcChannelBuffer2
    return IAsyncRpcChannelBuffer
def _define_IAuthenticate_head():
    class IAuthenticate(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9d0-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    return IAuthenticate
def _define_IAuthenticate():
    IAuthenticate = win32more.System.Com.IAuthenticate_head
    IAuthenticate.Authenticate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR))(3, 'Authenticate', ((1, 'phwnd'),(1, 'pszUsername'),(1, 'pszPassword'),)))
    win32more.System.Com.IUnknown
    return IAuthenticate
def _define_IAuthenticateEx_head():
    class IAuthenticateEx(win32more.System.Com.IAuthenticate_head):
        Guid = Guid('2ad1edaf-d83d-48b5-9a-df-03-db-e1-9f-53-bd')
    return IAuthenticateEx
def _define_IAuthenticateEx():
    IAuthenticateEx = win32more.System.Com.IAuthenticateEx_head
    IAuthenticateEx.AuthenticateEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.System.Com.AUTHENTICATEINFO_head))(4, 'AuthenticateEx', ((1, 'phwnd'),(1, 'pszUsername'),(1, 'pszPassword'),(1, 'pauthinfo'),)))
    win32more.System.Com.IAuthenticate
    return IAuthenticateEx
def _define_IBindCtx_head():
    class IBindCtx(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000000e-0000-0000-c0-00-00-00-00-00-00-46')
    return IBindCtx
def _define_IBindCtx():
    IBindCtx = win32more.System.Com.IBindCtx_head
    IBindCtx.RegisterObjectBound = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(3, 'RegisterObjectBound', ((1, 'punk'),)))
    IBindCtx.RevokeObjectBound = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(4, 'RevokeObjectBound', ((1, 'punk'),)))
    IBindCtx.ReleaseBoundObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'ReleaseBoundObjects', ()))
    IBindCtx.SetBindOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.BIND_OPTS_head))(6, 'SetBindOptions', ((1, 'pbindopts'),)))
    IBindCtx.GetBindOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.BIND_OPTS_head))(7, 'GetBindOptions', ((1, 'pbindopts'),)))
    IBindCtx.GetRunningObjectTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IRunningObjectTable_head))(8, 'GetRunningObjectTable', ((1, 'pprot'),)))
    IBindCtx.RegisterObjectParam = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IUnknown_head)(9, 'RegisterObjectParam', ((1, 'pszKey'),(1, 'punk'),)))
    IBindCtx.GetObjectParam = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.IUnknown_head))(10, 'GetObjectParam', ((1, 'pszKey'),(1, 'ppunk'),)))
    IBindCtx.EnumObjectParam = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumString_head))(11, 'EnumObjectParam', ((1, 'ppenum'),)))
    IBindCtx.RevokeObjectParam = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(12, 'RevokeObjectParam', ((1, 'pszKey'),)))
    win32more.System.Com.IUnknown
    return IBindCtx
def _define_IBindHost_head():
    class IBindHost(win32more.System.Com.IUnknown_head):
        Guid = Guid('fc4801a1-2ba9-11cf-a2-29-00-aa-00-3d-73-52')
    return IBindHost
def _define_IBindHost():
    IBindHost = win32more.System.Com.IBindHost_head
    IBindHost.CreateMoniker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IBindCtx_head,POINTER(win32more.System.Com.IMoniker_head),UInt32)(3, 'CreateMoniker', ((1, 'szName'),(1, 'pBC'),(1, 'ppmk'),(1, 'dwReserved'),)))
    IBindHost.MonikerBindToStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,win32more.System.Com.IBindCtx_head,win32more.System.Com.IBindStatusCallback_head,POINTER(Guid),POINTER(c_void_p))(4, 'MonikerBindToStorage', ((1, 'pMk'),(1, 'pBC'),(1, 'pBSC'),(1, 'riid'),(1, 'ppvObj'),)))
    IBindHost.MonikerBindToObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,win32more.System.Com.IBindCtx_head,win32more.System.Com.IBindStatusCallback_head,POINTER(Guid),POINTER(c_void_p))(5, 'MonikerBindToObject', ((1, 'pMk'),(1, 'pBC'),(1, 'pBSC'),(1, 'riid'),(1, 'ppvObj'),)))
    win32more.System.Com.IUnknown
    return IBindHost
def _define_IBinding_head():
    class IBinding(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9c0-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    return IBinding
def _define_IBinding():
    IBinding = win32more.System.Com.IBinding_head
    IBinding.Abort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Abort', ()))
    IBinding.Suspend = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Suspend', ()))
    IBinding.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Resume', ()))
    IBinding.SetPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(6, 'SetPriority', ((1, 'nPriority'),)))
    IBinding.GetPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(7, 'GetPriority', ((1, 'pnPriority'),)))
    IBinding.GetBindResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32),POINTER(win32more.Foundation.PWSTR),POINTER(UInt32))(8, 'GetBindResult', ((1, 'pclsidProtocol'),(1, 'pdwResult'),(1, 'pszResult'),(1, 'pdwReserved'),)))
    win32more.System.Com.IUnknown
    return IBinding
def _define_IBindStatusCallback_head():
    class IBindStatusCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9c1-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    return IBindStatusCallback
def _define_IBindStatusCallback():
    IBindStatusCallback = win32more.System.Com.IBindStatusCallback_head
    IBindStatusCallback.OnStartBinding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.IBinding_head)(3, 'OnStartBinding', ((1, 'dwReserved'),(1, 'pib'),)))
    IBindStatusCallback.GetPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(4, 'GetPriority', ((1, 'pnPriority'),)))
    IBindStatusCallback.OnLowResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(5, 'OnLowResource', ((1, 'reserved'),)))
    IBindStatusCallback.OnProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,win32more.Foundation.PWSTR)(6, 'OnProgress', ((1, 'ulProgress'),(1, 'ulProgressMax'),(1, 'ulStatusCode'),(1, 'szStatusText'),)))
    IBindStatusCallback.OnStopBinding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(7, 'OnStopBinding', ((1, 'hresult'),(1, 'szError'),)))
    IBindStatusCallback.GetBindInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.System.Com.BINDINFO_head))(8, 'GetBindInfo', ((1, 'grfBINDF'),(1, 'pbindinfo'),)))
    IBindStatusCallback.OnDataAvailable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.System.Com.FORMATETC_head),POINTER(win32more.System.Com.STGMEDIUM_head))(9, 'OnDataAvailable', ((1, 'grfBSCF'),(1, 'dwSize'),(1, 'pformatetc'),(1, 'pstgmed'),)))
    IBindStatusCallback.OnObjectAvailable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head)(10, 'OnObjectAvailable', ((1, 'riid'),(1, 'punk'),)))
    win32more.System.Com.IUnknown
    return IBindStatusCallback
def _define_IBindStatusCallbackEx_head():
    class IBindStatusCallbackEx(win32more.System.Com.IBindStatusCallback_head):
        Guid = Guid('aaa74ef9-8ee7-4659-88-d9-f8-c5-04-da-73-cc')
    return IBindStatusCallbackEx
def _define_IBindStatusCallbackEx():
    IBindStatusCallbackEx = win32more.System.Com.IBindStatusCallbackEx_head
    IBindStatusCallbackEx.GetBindInfoEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.System.Com.BINDINFO_head),POINTER(UInt32),POINTER(UInt32))(11, 'GetBindInfoEx', ((1, 'grfBINDF'),(1, 'pbindinfo'),(1, 'grfBINDF2'),(1, 'pdwReserved'),)))
    win32more.System.Com.IBindStatusCallback
    return IBindStatusCallbackEx
def _define_IBlockingLock_head():
    class IBlockingLock(win32more.System.Com.IUnknown_head):
        Guid = Guid('30f3d47a-6447-11d1-8e-3c-00-c0-4f-b9-38-6d')
    return IBlockingLock
def _define_IBlockingLock():
    IBlockingLock = win32more.System.Com.IBlockingLock_head
    IBlockingLock.Lock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(3, 'Lock', ((1, 'dwTimeout'),)))
    IBlockingLock.Unlock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Unlock', ()))
    win32more.System.Com.IUnknown
    return IBlockingLock
def _define_ICallFactory_head():
    class ICallFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('1c733a30-2a1c-11ce-ad-e5-00-aa-00-44-77-3d')
    return ICallFactory
def _define_ICallFactory():
    ICallFactory = win32more.System.Com.ICallFactory_head
    ICallFactory.CreateCall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head))(3, 'CreateCall', ((1, 'riid'),(1, 'pCtrlUnk'),(1, 'riid2'),(1, 'ppv'),)))
    win32more.System.Com.IUnknown
    return ICallFactory
def _define_ICancelMethodCalls_head():
    class ICancelMethodCalls(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000029-0000-0000-c0-00-00-00-00-00-00-46')
    return ICancelMethodCalls
def _define_ICancelMethodCalls():
    ICancelMethodCalls = win32more.System.Com.ICancelMethodCalls_head
    ICancelMethodCalls.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(3, 'Cancel', ((1, 'ulSeconds'),)))
    ICancelMethodCalls.TestCancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'TestCancel', ()))
    win32more.System.Com.IUnknown
    return ICancelMethodCalls
def _define_ICatInformation_head():
    class ICatInformation(win32more.System.Com.IUnknown_head):
        Guid = Guid('0002e013-0000-0000-c0-00-00-00-00-00-00-46')
    return ICatInformation
def _define_ICatInformation():
    ICatInformation = win32more.System.Com.ICatInformation_head
    ICatInformation.EnumCategories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IEnumCATEGORYINFO_head))(3, 'EnumCategories', ((1, 'lcid'),(1, 'ppenumCategoryInfo'),)))
    ICatInformation.GetCategoryDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.Foundation.PWSTR))(4, 'GetCategoryDesc', ((1, 'rcatid'),(1, 'lcid'),(1, 'pszDesc'),)))
    ICatInformation.EnumClassesOfCategories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),UInt32,POINTER(Guid),POINTER(win32more.System.Com.IEnumGUID_head))(5, 'EnumClassesOfCategories', ((1, 'cImplemented'),(1, 'rgcatidImpl'),(1, 'cRequired'),(1, 'rgcatidReq'),(1, 'ppenumClsid'),)))
    ICatInformation.IsClassOfCategories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Guid),UInt32,POINTER(Guid))(6, 'IsClassOfCategories', ((1, 'rclsid'),(1, 'cImplemented'),(1, 'rgcatidImpl'),(1, 'cRequired'),(1, 'rgcatidReq'),)))
    ICatInformation.EnumImplCategoriesOfClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.IEnumGUID_head))(7, 'EnumImplCategoriesOfClass', ((1, 'rclsid'),(1, 'ppenumCatid'),)))
    ICatInformation.EnumReqCategoriesOfClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.IEnumGUID_head))(8, 'EnumReqCategoriesOfClass', ((1, 'rclsid'),(1, 'ppenumCatid'),)))
    win32more.System.Com.IUnknown
    return ICatInformation
def _define_ICatRegister_head():
    class ICatRegister(win32more.System.Com.IUnknown_head):
        Guid = Guid('0002e012-0000-0000-c0-00-00-00-00-00-00-46')
    return ICatRegister
def _define_ICatRegister():
    ICatRegister = win32more.System.Com.ICatRegister_head
    ICatRegister.RegisterCategories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.CATEGORYINFO_head))(3, 'RegisterCategories', ((1, 'cCategories'),(1, 'rgCategoryInfo'),)))
    ICatRegister.UnRegisterCategories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid))(4, 'UnRegisterCategories', ((1, 'cCategories'),(1, 'rgcatid'),)))
    ICatRegister.RegisterClassImplCategories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Guid))(5, 'RegisterClassImplCategories', ((1, 'rclsid'),(1, 'cCategories'),(1, 'rgcatid'),)))
    ICatRegister.UnRegisterClassImplCategories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Guid))(6, 'UnRegisterClassImplCategories', ((1, 'rclsid'),(1, 'cCategories'),(1, 'rgcatid'),)))
    ICatRegister.RegisterClassReqCategories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Guid))(7, 'RegisterClassReqCategories', ((1, 'rclsid'),(1, 'cCategories'),(1, 'rgcatid'),)))
    ICatRegister.UnRegisterClassReqCategories = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(Guid))(8, 'UnRegisterClassReqCategories', ((1, 'rclsid'),(1, 'cCategories'),(1, 'rgcatid'),)))
    win32more.System.Com.IUnknown
    return ICatRegister
def _define_IChannelHook_head():
    class IChannelHook(win32more.System.Com.IUnknown_head):
        Guid = Guid('1008c4a0-7613-11cf-9a-f1-00-20-af-6e-72-f4')
    return IChannelHook
def _define_IChannelHook():
    IChannelHook = win32more.System.Com.IChannelHook_head
    IChannelHook.ClientGetSize = COMMETHOD(WINFUNCTYPE(Void,POINTER(Guid),POINTER(Guid),POINTER(UInt32))(3, 'ClientGetSize', ((1, 'uExtent'),(1, 'riid'),(1, 'pDataSize'),)))
    IChannelHook.ClientFillBuffer = COMMETHOD(WINFUNCTYPE(Void,POINTER(Guid),POINTER(Guid),POINTER(UInt32),c_void_p)(4, 'ClientFillBuffer', ((1, 'uExtent'),(1, 'riid'),(1, 'pDataSize'),(1, 'pDataBuffer'),)))
    IChannelHook.ClientNotify = COMMETHOD(WINFUNCTYPE(Void,POINTER(Guid),POINTER(Guid),UInt32,c_void_p,UInt32,win32more.Foundation.HRESULT)(5, 'ClientNotify', ((1, 'uExtent'),(1, 'riid'),(1, 'cbDataSize'),(1, 'pDataBuffer'),(1, 'lDataRep'),(1, 'hrFault'),)))
    IChannelHook.ServerNotify = COMMETHOD(WINFUNCTYPE(Void,POINTER(Guid),POINTER(Guid),UInt32,c_void_p,UInt32)(6, 'ServerNotify', ((1, 'uExtent'),(1, 'riid'),(1, 'cbDataSize'),(1, 'pDataBuffer'),(1, 'lDataRep'),)))
    IChannelHook.ServerGetSize = COMMETHOD(WINFUNCTYPE(Void,POINTER(Guid),POINTER(Guid),win32more.Foundation.HRESULT,POINTER(UInt32))(7, 'ServerGetSize', ((1, 'uExtent'),(1, 'riid'),(1, 'hrFault'),(1, 'pDataSize'),)))
    IChannelHook.ServerFillBuffer = COMMETHOD(WINFUNCTYPE(Void,POINTER(Guid),POINTER(Guid),POINTER(UInt32),c_void_p,win32more.Foundation.HRESULT)(8, 'ServerFillBuffer', ((1, 'uExtent'),(1, 'riid'),(1, 'pDataSize'),(1, 'pDataBuffer'),(1, 'hrFault'),)))
    win32more.System.Com.IUnknown
    return IChannelHook
def _define_IClassActivator_head():
    class IClassActivator(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000140-0000-0000-c0-00-00-00-00-00-00-46')
    return IClassActivator
def _define_IClassActivator():
    IClassActivator = win32more.System.Com.IClassActivator_head
    IClassActivator.GetClassObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,UInt32,POINTER(Guid),POINTER(c_void_p))(3, 'GetClassObject', ((1, 'rclsid'),(1, 'dwClassContext'),(1, 'locale'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.Com.IUnknown
    return IClassActivator
def _define_IClassFactory_head():
    class IClassFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000001-0000-0000-c0-00-00-00-00-00-00-46')
    return IClassFactory
def _define_IClassFactory():
    IClassFactory = win32more.System.Com.IClassFactory_head
    IClassFactory.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p))(3, 'CreateInstance', ((1, 'pUnkOuter'),(1, 'riid'),(1, 'ppvObject'),)))
    IClassFactory.LockServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(4, 'LockServer', ((1, 'fLock'),)))
    win32more.System.Com.IUnknown
    return IClassFactory
def _define_IClientSecurity_head():
    class IClientSecurity(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000013d-0000-0000-c0-00-00-00-00-00-00-46')
    return IClientSecurity
def _define_IClientSecurity():
    IClientSecurity = win32more.System.Com.IClientSecurity_head
    IClientSecurity.QueryBlanket = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(UInt32),POINTER(UInt32),POINTER(POINTER(UInt16)),POINTER(win32more.System.Com.RPC_C_AUTHN_LEVEL),POINTER(win32more.System.Com.RPC_C_IMP_LEVEL),POINTER(c_void_p),POINTER(win32more.System.Com.EOLE_AUTHENTICATION_CAPABILITIES))(3, 'QueryBlanket', ((1, 'pProxy'),(1, 'pAuthnSvc'),(1, 'pAuthzSvc'),(1, 'pServerPrincName'),(1, 'pAuthnLevel'),(1, 'pImpLevel'),(1, 'pAuthInfo'),(1, 'pCapabilites'),)))
    IClientSecurity.SetBlanket = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.System.Com.RPC_C_AUTHN_LEVEL,win32more.System.Com.RPC_C_IMP_LEVEL,c_void_p,win32more.System.Com.EOLE_AUTHENTICATION_CAPABILITIES)(4, 'SetBlanket', ((1, 'pProxy'),(1, 'dwAuthnSvc'),(1, 'dwAuthzSvc'),(1, 'pServerPrincName'),(1, 'dwAuthnLevel'),(1, 'dwImpLevel'),(1, 'pAuthInfo'),(1, 'dwCapabilities'),)))
    IClientSecurity.CopyProxy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.IUnknown_head))(5, 'CopyProxy', ((1, 'pProxy'),(1, 'ppCopy'),)))
    win32more.System.Com.IUnknown
    return IClientSecurity
def _define_IComThreadingInfo_head():
    class IComThreadingInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('000001ce-0000-0000-c0-00-00-00-00-00-00-46')
    return IComThreadingInfo
def _define_IComThreadingInfo():
    IComThreadingInfo = win32more.System.Com.IComThreadingInfo_head
    IComThreadingInfo.GetCurrentApartmentType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.APTTYPE))(3, 'GetCurrentApartmentType', ((1, 'pAptType'),)))
    IComThreadingInfo.GetCurrentThreadType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.THDTYPE))(4, 'GetCurrentThreadType', ((1, 'pThreadType'),)))
    IComThreadingInfo.GetCurrentLogicalThreadId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(5, 'GetCurrentLogicalThreadId', ((1, 'pguidLogicalThreadId'),)))
    IComThreadingInfo.SetCurrentLogicalThreadId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(6, 'SetCurrentLogicalThreadId', ((1, 'rguid'),)))
    win32more.System.Com.IUnknown
    return IComThreadingInfo
def _define_IConnectionPoint_head():
    class IConnectionPoint(win32more.System.Com.IUnknown_head):
        Guid = Guid('b196b286-bab4-101a-b6-9c-00-aa-00-34-1d-07')
    return IConnectionPoint
def _define_IConnectionPoint():
    IConnectionPoint = win32more.System.Com.IConnectionPoint_head
    IConnectionPoint.GetConnectionInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'GetConnectionInterface', ((1, 'pIID'),)))
    IConnectionPoint.GetConnectionPointContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IConnectionPointContainer_head))(4, 'GetConnectionPointContainer', ((1, 'ppCPC'),)))
    IConnectionPoint.Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(UInt32))(5, 'Advise', ((1, 'pUnkSink'),(1, 'pdwCookie'),)))
    IConnectionPoint.Unadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'Unadvise', ((1, 'dwCookie'),)))
    IConnectionPoint.EnumConnections = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumConnections_head))(7, 'EnumConnections', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IConnectionPoint
def _define_IConnectionPointContainer_head():
    class IConnectionPointContainer(win32more.System.Com.IUnknown_head):
        Guid = Guid('b196b284-bab4-101a-b6-9c-00-aa-00-34-1d-07')
    return IConnectionPointContainer
def _define_IConnectionPointContainer():
    IConnectionPointContainer = win32more.System.Com.IConnectionPointContainer_head
    IConnectionPointContainer.EnumConnectionPoints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumConnectionPoints_head))(3, 'EnumConnectionPoints', ((1, 'ppEnum'),)))
    IConnectionPointContainer.FindConnectionPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.IConnectionPoint_head))(4, 'FindConnectionPoint', ((1, 'riid'),(1, 'ppCP'),)))
    win32more.System.Com.IUnknown
    return IConnectionPointContainer
def _define_IContext_head():
    class IContext(Structure):
        pass
    return IContext
def _define_IContext():
    IContext = win32more.System.Com.IContext_head
    return IContext
def _define_IContextCallback_head():
    class IContextCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('000001da-0000-0000-c0-00-00-00-00-00-00-46')
    return IContextCallback
def _define_IContextCallback():
    IContextCallback = win32more.System.Com.IContextCallback_head
    IContextCallback.ContextCallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.PFNCONTEXTCALL,POINTER(win32more.System.Com.ComCallData_head),POINTER(Guid),Int32,win32more.System.Com.IUnknown_head)(3, 'ContextCallback', ((1, 'pfnCallback'),(1, 'pParam'),(1, 'riid'),(1, 'iMethod'),(1, 'pUnk'),)))
    win32more.System.Com.IUnknown
    return IContextCallback
def _define_IDataAdviseHolder_head():
    class IDataAdviseHolder(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000110-0000-0000-c0-00-00-00-00-00-00-46')
    return IDataAdviseHolder
def _define_IDataAdviseHolder():
    IDataAdviseHolder = win32more.System.Com.IDataAdviseHolder_head
    IDataAdviseHolder.Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,POINTER(win32more.System.Com.FORMATETC_head),UInt32,win32more.System.Com.IAdviseSink_head,POINTER(UInt32))(3, 'Advise', ((1, 'pDataObject'),(1, 'pFetc'),(1, 'advf'),(1, 'pAdvise'),(1, 'pdwConnection'),)))
    IDataAdviseHolder.Unadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Unadvise', ((1, 'dwConnection'),)))
    IDataAdviseHolder.EnumAdvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumSTATDATA_head))(5, 'EnumAdvise', ((1, 'ppenumAdvise'),)))
    IDataAdviseHolder.SendOnDataChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,UInt32,UInt32)(6, 'SendOnDataChange', ((1, 'pDataObject'),(1, 'dwReserved'),(1, 'advf'),)))
    win32more.System.Com.IUnknown
    return IDataAdviseHolder
def _define_IDataObject_head():
    class IDataObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000010e-0000-0000-c0-00-00-00-00-00-00-46')
    return IDataObject
def _define_IDataObject():
    IDataObject = win32more.System.Com.IDataObject_head
    IDataObject.GetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.FORMATETC_head),POINTER(win32more.System.Com.STGMEDIUM_head))(3, 'GetData', ((1, 'pformatetcIn'),(1, 'pmedium'),)))
    IDataObject.GetDataHere = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.FORMATETC_head),POINTER(win32more.System.Com.STGMEDIUM_head))(4, 'GetDataHere', ((1, 'pformatetc'),(1, 'pmedium'),)))
    IDataObject.QueryGetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.FORMATETC_head))(5, 'QueryGetData', ((1, 'pformatetc'),)))
    IDataObject.GetCanonicalFormatEtc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.FORMATETC_head),POINTER(win32more.System.Com.FORMATETC_head))(6, 'GetCanonicalFormatEtc', ((1, 'pformatectIn'),(1, 'pformatetcOut'),)))
    IDataObject.SetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.FORMATETC_head),POINTER(win32more.System.Com.STGMEDIUM_head),win32more.Foundation.BOOL)(7, 'SetData', ((1, 'pformatetc'),(1, 'pmedium'),(1, 'fRelease'),)))
    IDataObject.EnumFormatEtc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IEnumFORMATETC_head))(8, 'EnumFormatEtc', ((1, 'dwDirection'),(1, 'ppenumFormatEtc'),)))
    IDataObject.DAdvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.FORMATETC_head),UInt32,win32more.System.Com.IAdviseSink_head,POINTER(UInt32))(9, 'DAdvise', ((1, 'pformatetc'),(1, 'advf'),(1, 'pAdvSink'),(1, 'pdwConnection'),)))
    IDataObject.DUnadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(10, 'DUnadvise', ((1, 'dwConnection'),)))
    IDataObject.EnumDAdvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumSTATDATA_head))(11, 'EnumDAdvise', ((1, 'ppenumAdvise'),)))
    win32more.System.Com.IUnknown
    return IDataObject
def _define_IDispatch_head():
    class IDispatch(win32more.System.Com.IUnknown_head):
        Guid = Guid('00020400-0000-0000-c0-00-00-00-00-00-00-46')
    return IDispatch
def _define_IDispatch():
    IDispatch = win32more.System.Com.IDispatch_head
    IDispatch.GetTypeInfoCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetTypeInfoCount', ((1, 'pctinfo'),)))
    IDispatch.GetTypeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.System.Com.ITypeInfo_head))(4, 'GetTypeInfo', ((1, 'iTInfo'),(1, 'lcid'),(1, 'ppTInfo'),)))
    IDispatch.GetIDsOfNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.PWSTR),UInt32,UInt32,POINTER(Int32))(5, 'GetIDsOfNames', ((1, 'riid'),(1, 'rgszNames'),(1, 'cNames'),(1, 'lcid'),(1, 'rgDispId'),)))
    IDispatch.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Guid),UInt32,win32more.System.Com.DISPATCH_FLAGS,POINTER(win32more.System.Com.DISPPARAMS_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.EXCEPINFO_head),POINTER(UInt32))(6, 'Invoke', ((1, 'dispIdMember'),(1, 'riid'),(1, 'lcid'),(1, 'wFlags'),(1, 'pDispParams'),(1, 'pVarResult'),(1, 'pExcepInfo'),(1, 'puArgErr'),)))
    win32more.System.Com.IUnknown
    return IDispatch
def _define_IDLDESC_head():
    class IDLDESC(Structure):
        pass
    return IDLDESC
def _define_IDLDESC():
    IDLDESC = win32more.System.Com.IDLDESC_head
    IDLDESC._fields_ = [
        ('dwReserved', UIntPtr),
        ('wIDLFlags', win32more.System.Com.IDLFLAGS),
    ]
    return IDLDESC
IDLFLAGS = UInt16
IDLFLAG_NONE = 0
IDLFLAG_FIN = 1
IDLFLAG_FOUT = 2
IDLFLAG_FLCID = 4
IDLFLAG_FRETVAL = 8
def _define_IEnumCATEGORYINFO_head():
    class IEnumCATEGORYINFO(win32more.System.Com.IUnknown_head):
        Guid = Guid('0002e011-0000-0000-c0-00-00-00-00-00-00-46')
    return IEnumCATEGORYINFO
def _define_IEnumCATEGORYINFO():
    IEnumCATEGORYINFO = win32more.System.Com.IEnumCATEGORYINFO_head
    IEnumCATEGORYINFO.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.CATEGORYINFO_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumCATEGORYINFO.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumCATEGORYINFO.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumCATEGORYINFO.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumCATEGORYINFO_head))(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumCATEGORYINFO
def _define_IEnumConnectionPoints_head():
    class IEnumConnectionPoints(win32more.System.Com.IUnknown_head):
        Guid = Guid('b196b285-bab4-101a-b6-9c-00-aa-00-34-1d-07')
    return IEnumConnectionPoints
def _define_IEnumConnectionPoints():
    IEnumConnectionPoints = win32more.System.Com.IEnumConnectionPoints_head
    IEnumConnectionPoints.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IConnectionPoint_head),POINTER(UInt32))(3, 'Next', ((1, 'cConnections'),(1, 'ppCP'),(1, 'pcFetched'),)))
    IEnumConnectionPoints.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'cConnections'),)))
    IEnumConnectionPoints.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumConnectionPoints.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumConnectionPoints_head))(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumConnectionPoints
def _define_IEnumConnections_head():
    class IEnumConnections(win32more.System.Com.IUnknown_head):
        Guid = Guid('b196b287-bab4-101a-b6-9c-00-aa-00-34-1d-07')
    return IEnumConnections
def _define_IEnumConnections():
    IEnumConnections = win32more.System.Com.IEnumConnections_head
    IEnumConnections.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.CONNECTDATA_head),POINTER(UInt32))(3, 'Next', ((1, 'cConnections'),(1, 'rgcd'),(1, 'pcFetched'),)))
    IEnumConnections.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'cConnections'),)))
    IEnumConnections.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumConnections.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumConnections_head))(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumConnections
def _define_IEnumContextProps_head():
    class IEnumContextProps(Structure):
        pass
    return IEnumContextProps
def _define_IEnumContextProps():
    IEnumContextProps = win32more.System.Com.IEnumContextProps_head
    return IEnumContextProps
def _define_IEnumFORMATETC_head():
    class IEnumFORMATETC(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000103-0000-0000-c0-00-00-00-00-00-00-46')
    return IEnumFORMATETC
def _define_IEnumFORMATETC():
    IEnumFORMATETC = win32more.System.Com.IEnumFORMATETC_head
    IEnumFORMATETC.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.FORMATETC_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumFORMATETC.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumFORMATETC.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumFORMATETC.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumFORMATETC_head))(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumFORMATETC
def _define_IEnumGUID_head():
    class IEnumGUID(win32more.System.Com.IUnknown_head):
        Guid = Guid('0002e000-0000-0000-c0-00-00-00-00-00-00-46')
    return IEnumGUID
def _define_IEnumGUID():
    IEnumGUID = win32more.System.Com.IEnumGUID_head
    IEnumGUID.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumGUID.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumGUID.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumGUID.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumGUID_head))(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumGUID
def _define_IEnumMoniker_head():
    class IEnumMoniker(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000102-0000-0000-c0-00-00-00-00-00-00-46')
    return IEnumMoniker
def _define_IEnumMoniker():
    IEnumMoniker = win32more.System.Com.IEnumMoniker_head
    IEnumMoniker.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IMoniker_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumMoniker.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumMoniker.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumMoniker.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumMoniker_head))(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumMoniker
def _define_IEnumSTATDATA_head():
    class IEnumSTATDATA(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000105-0000-0000-c0-00-00-00-00-00-00-46')
    return IEnumSTATDATA
def _define_IEnumSTATDATA():
    IEnumSTATDATA = win32more.System.Com.IEnumSTATDATA_head
    IEnumSTATDATA.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.STATDATA_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumSTATDATA.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumSTATDATA.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumSTATDATA.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumSTATDATA_head))(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumSTATDATA
def _define_IEnumString_head():
    class IEnumString(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000101-0000-0000-c0-00-00-00-00-00-00-46')
    return IEnumString
def _define_IEnumString():
    IEnumString = win32more.System.Com.IEnumString_head
    IEnumString.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumString.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumString.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumString.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumString_head))(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumString
def _define_IEnumUnknown_head():
    class IEnumUnknown(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000100-0000-0000-c0-00-00-00-00-00-00-46')
    return IEnumUnknown
def _define_IEnumUnknown():
    IEnumUnknown = win32more.System.Com.IEnumUnknown_head
    IEnumUnknown.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IUnknown_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumUnknown.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumUnknown.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumUnknown.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumUnknown_head))(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumUnknown
def _define_IErrorInfo_head():
    class IErrorInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('1cf2b120-547d-101b-8e-65-08-00-2b-2b-d1-19')
    return IErrorInfo
def _define_IErrorInfo():
    IErrorInfo = win32more.System.Com.IErrorInfo_head
    IErrorInfo.GetGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'GetGUID', ((1, 'pGUID'),)))
    IErrorInfo.GetSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'GetSource', ((1, 'pBstrSource'),)))
    IErrorInfo.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(5, 'GetDescription', ((1, 'pBstrDescription'),)))
    IErrorInfo.GetHelpFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(6, 'GetHelpFile', ((1, 'pBstrHelpFile'),)))
    IErrorInfo.GetHelpContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(7, 'GetHelpContext', ((1, 'pdwHelpContext'),)))
    win32more.System.Com.IUnknown
    return IErrorInfo
def _define_IErrorLog_head():
    class IErrorLog(win32more.System.Com.IUnknown_head):
        Guid = Guid('3127ca40-446e-11ce-81-35-00-aa-00-4b-b8-51')
    return IErrorLog
def _define_IErrorLog():
    IErrorLog = win32more.System.Com.IErrorLog_head
    IErrorLog.AddError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.EXCEPINFO_head))(3, 'AddError', ((1, 'pszPropName'),(1, 'pExcepInfo'),)))
    win32more.System.Com.IUnknown
    return IErrorLog
def _define_IExternalConnection_head():
    class IExternalConnection(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000019-0000-0000-c0-00-00-00-00-00-00-46')
    return IExternalConnection
def _define_IExternalConnection():
    IExternalConnection = win32more.System.Com.IExternalConnection_head
    IExternalConnection.AddConnection = COMMETHOD(WINFUNCTYPE(UInt32,UInt32,UInt32)(3, 'AddConnection', ((1, 'extconn'),(1, 'reserved'),)))
    IExternalConnection.ReleaseConnection = COMMETHOD(WINFUNCTYPE(UInt32,UInt32,UInt32,win32more.Foundation.BOOL)(4, 'ReleaseConnection', ((1, 'extconn'),(1, 'reserved'),(1, 'fLastReleaseCloses'),)))
    win32more.System.Com.IUnknown
    return IExternalConnection
def _define_IFastRundown_head():
    class IFastRundown(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000040-0000-0000-c0-00-00-00-00-00-00-46')
    return IFastRundown
def _define_IFastRundown():
    IFastRundown = win32more.System.Com.IFastRundown_head
    win32more.System.Com.IUnknown
    return IFastRundown
def _define_IForegroundTransfer_head():
    class IForegroundTransfer(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000145-0000-0000-c0-00-00-00-00-00-00-46')
    return IForegroundTransfer
def _define_IForegroundTransfer():
    IForegroundTransfer = win32more.System.Com.IForegroundTransfer_head
    IForegroundTransfer.AllowForegroundTransfer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p)(3, 'AllowForegroundTransfer', ((1, 'lpvReserved'),)))
    win32more.System.Com.IUnknown
    return IForegroundTransfer
def _define_IGlobalInterfaceTable_head():
    class IGlobalInterfaceTable(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000146-0000-0000-c0-00-00-00-00-00-00-46')
    return IGlobalInterfaceTable
def _define_IGlobalInterfaceTable():
    IGlobalInterfaceTable = win32more.System.Com.IGlobalInterfaceTable_head
    IGlobalInterfaceTable.RegisterInterfaceInGlobal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(UInt32))(3, 'RegisterInterfaceInGlobal', ((1, 'pUnk'),(1, 'riid'),(1, 'pdwCookie'),)))
    IGlobalInterfaceTable.RevokeInterfaceFromGlobal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'RevokeInterfaceFromGlobal', ((1, 'dwCookie'),)))
    IGlobalInterfaceTable.GetInterfaceFromGlobal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p))(5, 'GetInterfaceFromGlobal', ((1, 'dwCookie'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.Com.IUnknown
    return IGlobalInterfaceTable
def _define_IGlobalOptions_head():
    class IGlobalOptions(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000015b-0000-0000-c0-00-00-00-00-00-00-46')
    return IGlobalOptions
def _define_IGlobalOptions():
    IGlobalOptions = win32more.System.Com.IGlobalOptions_head
    IGlobalOptions.Set = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.GLOBALOPT_PROPERTIES,UIntPtr)(3, 'Set', ((1, 'dwProperty'),(1, 'dwValue'),)))
    IGlobalOptions.Query = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.GLOBALOPT_PROPERTIES,POINTER(UIntPtr))(4, 'Query', ((1, 'dwProperty'),(1, 'pdwValue'),)))
    win32more.System.Com.IUnknown
    return IGlobalOptions
def _define_IInitializeSpy_head():
    class IInitializeSpy(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000034-0000-0000-c0-00-00-00-00-00-00-46')
    return IInitializeSpy
def _define_IInitializeSpy():
    IInitializeSpy = win32more.System.Com.IInitializeSpy_head
    IInitializeSpy.PreInitialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32)(3, 'PreInitialize', ((1, 'dwCoInit'),(1, 'dwCurThreadAptRefs'),)))
    IInitializeSpy.PostInitialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt32,UInt32)(4, 'PostInitialize', ((1, 'hrCoInit'),(1, 'dwCoInit'),(1, 'dwNewThreadAptRefs'),)))
    IInitializeSpy.PreUninitialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(5, 'PreUninitialize', ((1, 'dwCurThreadAptRefs'),)))
    IInitializeSpy.PostUninitialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'PostUninitialize', ((1, 'dwNewThreadAptRefs'),)))
    win32more.System.Com.IUnknown
    return IInitializeSpy
def _define_IInternalUnknown_head():
    class IInternalUnknown(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000021-0000-0000-c0-00-00-00-00-00-00-46')
    return IInternalUnknown
def _define_IInternalUnknown():
    IInternalUnknown = win32more.System.Com.IInternalUnknown_head
    IInternalUnknown.QueryInternalInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(3, 'QueryInternalInterface', ((1, 'riid'),(1, 'ppv'),)))
    win32more.System.Com.IUnknown
    return IInternalUnknown
def _define_IMachineGlobalObjectTable_head():
    class IMachineGlobalObjectTable(win32more.System.Com.IUnknown_head):
        Guid = Guid('26d709ac-f70b-4421-a9-6f-d2-87-8f-af-b0-0d')
    return IMachineGlobalObjectTable
def _define_IMachineGlobalObjectTable():
    IMachineGlobalObjectTable = win32more.System.Com.IMachineGlobalObjectTable_head
    IMachineGlobalObjectTable.RegisterObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,win32more.System.Com.IUnknown_head,POINTER(POINTER(win32more.System.Com.MachineGlobalObjectTableRegistrationToken___head)))(3, 'RegisterObject', ((1, 'clsid'),(1, 'identifier'),(1, 'object'),(1, 'token'),)))
    IMachineGlobalObjectTable.GetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,POINTER(Guid),POINTER(c_void_p))(4, 'GetObject', ((1, 'clsid'),(1, 'identifier'),(1, 'riid'),(1, 'ppv'),)))
    IMachineGlobalObjectTable.RevokeObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.MachineGlobalObjectTableRegistrationToken___head))(5, 'RevokeObject', ((1, 'token'),)))
    win32more.System.Com.IUnknown
    return IMachineGlobalObjectTable
def _define_IMalloc_head():
    class IMalloc(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000002-0000-0000-c0-00-00-00-00-00-00-46')
    return IMalloc
def _define_IMalloc():
    IMalloc = win32more.System.Com.IMalloc_head
    IMalloc.Alloc = COMMETHOD(WINFUNCTYPE(c_void_p,UIntPtr)(3, 'Alloc', ((1, 'cb'),)))
    IMalloc.Realloc = COMMETHOD(WINFUNCTYPE(c_void_p,c_void_p,UIntPtr)(4, 'Realloc', ((1, 'pv'),(1, 'cb'),)))
    IMalloc.Free = COMMETHOD(WINFUNCTYPE(Void,c_void_p)(5, 'Free', ((1, 'pv'),)))
    IMalloc.GetSize = COMMETHOD(WINFUNCTYPE(UIntPtr,c_void_p)(6, 'GetSize', ((1, 'pv'),)))
    IMalloc.DidAlloc = COMMETHOD(WINFUNCTYPE(Int32,c_void_p)(7, 'DidAlloc', ((1, 'pv'),)))
    IMalloc.HeapMinimize = COMMETHOD(WINFUNCTYPE(Void,)(8, 'HeapMinimize', ()))
    win32more.System.Com.IUnknown
    return IMalloc
def _define_IMallocSpy_head():
    class IMallocSpy(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000001d-0000-0000-c0-00-00-00-00-00-00-46')
    return IMallocSpy
def _define_IMallocSpy():
    IMallocSpy = win32more.System.Com.IMallocSpy_head
    IMallocSpy.PreAlloc = COMMETHOD(WINFUNCTYPE(UIntPtr,UIntPtr)(3, 'PreAlloc', ((1, 'cbRequest'),)))
    IMallocSpy.PostAlloc = COMMETHOD(WINFUNCTYPE(c_void_p,c_void_p)(4, 'PostAlloc', ((1, 'pActual'),)))
    IMallocSpy.PreFree = COMMETHOD(WINFUNCTYPE(c_void_p,c_void_p,win32more.Foundation.BOOL)(5, 'PreFree', ((1, 'pRequest'),(1, 'fSpyed'),)))
    IMallocSpy.PostFree = COMMETHOD(WINFUNCTYPE(Void,win32more.Foundation.BOOL)(6, 'PostFree', ((1, 'fSpyed'),)))
    IMallocSpy.PreRealloc = COMMETHOD(WINFUNCTYPE(UIntPtr,c_void_p,UIntPtr,POINTER(c_void_p),win32more.Foundation.BOOL)(7, 'PreRealloc', ((1, 'pRequest'),(1, 'cbRequest'),(1, 'ppNewRequest'),(1, 'fSpyed'),)))
    IMallocSpy.PostRealloc = COMMETHOD(WINFUNCTYPE(c_void_p,c_void_p,win32more.Foundation.BOOL)(8, 'PostRealloc', ((1, 'pActual'),(1, 'fSpyed'),)))
    IMallocSpy.PreGetSize = COMMETHOD(WINFUNCTYPE(c_void_p,c_void_p,win32more.Foundation.BOOL)(9, 'PreGetSize', ((1, 'pRequest'),(1, 'fSpyed'),)))
    IMallocSpy.PostGetSize = COMMETHOD(WINFUNCTYPE(UIntPtr,UIntPtr,win32more.Foundation.BOOL)(10, 'PostGetSize', ((1, 'cbActual'),(1, 'fSpyed'),)))
    IMallocSpy.PreDidAlloc = COMMETHOD(WINFUNCTYPE(c_void_p,c_void_p,win32more.Foundation.BOOL)(11, 'PreDidAlloc', ((1, 'pRequest'),(1, 'fSpyed'),)))
    IMallocSpy.PostDidAlloc = COMMETHOD(WINFUNCTYPE(Int32,c_void_p,win32more.Foundation.BOOL,Int32)(12, 'PostDidAlloc', ((1, 'pRequest'),(1, 'fSpyed'),(1, 'fActual'),)))
    IMallocSpy.PreHeapMinimize = COMMETHOD(WINFUNCTYPE(Void,)(13, 'PreHeapMinimize', ()))
    IMallocSpy.PostHeapMinimize = COMMETHOD(WINFUNCTYPE(Void,)(14, 'PostHeapMinimize', ()))
    win32more.System.Com.IUnknown
    return IMallocSpy
def _define_IMoniker_head():
    class IMoniker(win32more.System.Com.IPersistStream_head):
        Guid = Guid('0000000f-0000-0000-c0-00-00-00-00-00-00-46')
    return IMoniker
def _define_IMoniker():
    IMoniker = win32more.System.Com.IMoniker_head
    IMoniker.BindToObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,win32more.System.Com.IMoniker_head,POINTER(Guid),POINTER(c_void_p))(8, 'BindToObject', ((1, 'pbc'),(1, 'pmkToLeft'),(1, 'riidResult'),(1, 'ppvResult'),)))
    IMoniker.BindToStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,win32more.System.Com.IMoniker_head,POINTER(Guid),POINTER(c_void_p))(9, 'BindToStorage', ((1, 'pbc'),(1, 'pmkToLeft'),(1, 'riid'),(1, 'ppvObj'),)))
    IMoniker.Reduce = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,UInt32,POINTER(win32more.System.Com.IMoniker_head),POINTER(win32more.System.Com.IMoniker_head))(10, 'Reduce', ((1, 'pbc'),(1, 'dwReduceHowFar'),(1, 'ppmkToLeft'),(1, 'ppmkReduced'),)))
    IMoniker.ComposeWith = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,win32more.Foundation.BOOL,POINTER(win32more.System.Com.IMoniker_head))(11, 'ComposeWith', ((1, 'pmkRight'),(1, 'fOnlyIfNotGeneric'),(1, 'ppmkComposite'),)))
    IMoniker.Enum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,POINTER(win32more.System.Com.IEnumMoniker_head))(12, 'Enum', ((1, 'fForward'),(1, 'ppenumMoniker'),)))
    IMoniker.IsEqual = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head)(13, 'IsEqual', ((1, 'pmkOtherMoniker'),)))
    IMoniker.Hash = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(14, 'Hash', ((1, 'pdwHash'),)))
    IMoniker.IsRunning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,win32more.System.Com.IMoniker_head,win32more.System.Com.IMoniker_head)(15, 'IsRunning', ((1, 'pbc'),(1, 'pmkToLeft'),(1, 'pmkNewlyRunning'),)))
    IMoniker.GetTimeOfLastChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,win32more.System.Com.IMoniker_head,POINTER(win32more.Foundation.FILETIME_head))(16, 'GetTimeOfLastChange', ((1, 'pbc'),(1, 'pmkToLeft'),(1, 'pFileTime'),)))
    IMoniker.Inverse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IMoniker_head))(17, 'Inverse', ((1, 'ppmk'),)))
    IMoniker.CommonPrefixWith = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,POINTER(win32more.System.Com.IMoniker_head))(18, 'CommonPrefixWith', ((1, 'pmkOther'),(1, 'ppmkPrefix'),)))
    IMoniker.RelativePathTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,POINTER(win32more.System.Com.IMoniker_head))(19, 'RelativePathTo', ((1, 'pmkOther'),(1, 'ppmkRelPath'),)))
    IMoniker.GetDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,win32more.System.Com.IMoniker_head,POINTER(win32more.Foundation.PWSTR))(20, 'GetDisplayName', ((1, 'pbc'),(1, 'pmkToLeft'),(1, 'ppszDisplayName'),)))
    IMoniker.ParseDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,win32more.System.Com.IMoniker_head,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.System.Com.IMoniker_head))(21, 'ParseDisplayName', ((1, 'pbc'),(1, 'pmkToLeft'),(1, 'pszDisplayName'),(1, 'pchEaten'),(1, 'ppmkOut'),)))
    IMoniker.IsSystemMoniker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(22, 'IsSystemMoniker', ((1, 'pdwMksys'),)))
    win32more.System.Com.IPersistStream
    return IMoniker
IMPLTYPEFLAGS = Int32
IMPLTYPEFLAG_FDEFAULT = 1
IMPLTYPEFLAG_FSOURCE = 2
IMPLTYPEFLAG_FRESTRICTED = 4
IMPLTYPEFLAG_FDEFAULTVTABLE = 8
def _define_IMultiQI_head():
    class IMultiQI(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000020-0000-0000-c0-00-00-00-00-00-00-46')
    return IMultiQI
def _define_IMultiQI():
    IMultiQI = win32more.System.Com.IMultiQI_head
    IMultiQI.QueryMultipleInterfaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.MULTI_QI_head))(3, 'QueryMultipleInterfaces', ((1, 'cMQIs'),(1, 'pMQIs'),)))
    win32more.System.Com.IUnknown
    return IMultiQI
def _define_INoMarshal_head():
    class INoMarshal(win32more.System.Com.IUnknown_head):
        Guid = Guid('ecc8691b-c1db-4dc0-85-5e-65-f6-c5-51-af-49')
    return INoMarshal
def _define_INoMarshal():
    INoMarshal = win32more.System.Com.INoMarshal_head
    win32more.System.Com.IUnknown
    return INoMarshal
def _define_INTERFACEINFO_head():
    class INTERFACEINFO(Structure):
        pass
    return INTERFACEINFO
def _define_INTERFACEINFO():
    INTERFACEINFO = win32more.System.Com.INTERFACEINFO_head
    INTERFACEINFO._fields_ = [
        ('pUnk', win32more.System.Com.IUnknown_head),
        ('iid', Guid),
        ('wMethod', UInt16),
    ]
    return INTERFACEINFO
INVOKEKIND = Int32
INVOKE_FUNC = 1
INVOKE_PROPERTYGET = 2
INVOKE_PROPERTYPUT = 4
INVOKE_PROPERTYPUTREF = 8
def _define_IOplockStorage_head():
    class IOplockStorage(win32more.System.Com.IUnknown_head):
        Guid = Guid('8d19c834-8879-11d1-83-e9-00-c0-4f-c2-c6-d4')
    return IOplockStorage
def _define_IOplockStorage():
    IOplockStorage = win32more.System.Com.IOplockStorage_head
    IOplockStorage.CreateStorageEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,UInt32,POINTER(Guid),POINTER(c_void_p))(3, 'CreateStorageEx', ((1, 'pwcsName'),(1, 'grfMode'),(1, 'stgfmt'),(1, 'grfAttrs'),(1, 'riid'),(1, 'ppstgOpen'),)))
    IOplockStorage.OpenStorageEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,UInt32,POINTER(Guid),POINTER(c_void_p))(4, 'OpenStorageEx', ((1, 'pwcsName'),(1, 'grfMode'),(1, 'stgfmt'),(1, 'grfAttrs'),(1, 'riid'),(1, 'ppstgOpen'),)))
    win32more.System.Com.IUnknown
    return IOplockStorage
def _define_IPersist_head():
    class IPersist(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000010c-0000-0000-c0-00-00-00-00-00-00-46')
    return IPersist
def _define_IPersist():
    IPersist = win32more.System.Com.IPersist_head
    IPersist.GetClassID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'GetClassID', ((1, 'pClassID'),)))
    win32more.System.Com.IUnknown
    return IPersist
def _define_IPersistFile_head():
    class IPersistFile(win32more.System.Com.IPersist_head):
        Guid = Guid('0000010b-0000-0000-c0-00-00-00-00-00-00-46')
    return IPersistFile
def _define_IPersistFile():
    IPersistFile = win32more.System.Com.IPersistFile_head
    IPersistFile.IsDirty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'IsDirty', ()))
    IPersistFile.Load = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.STGM)(5, 'Load', ((1, 'pszFileName'),(1, 'dwMode'),)))
    IPersistFile.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)(6, 'Save', ((1, 'pszFileName'),(1, 'fRemember'),)))
    IPersistFile.SaveCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(7, 'SaveCompleted', ((1, 'pszFileName'),)))
    IPersistFile.GetCurFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(8, 'GetCurFile', ((1, 'ppszFileName'),)))
    win32more.System.Com.IPersist
    return IPersistFile
def _define_IPersistMemory_head():
    class IPersistMemory(win32more.System.Com.IPersist_head):
        Guid = Guid('bd1ae5e0-a6ae-11ce-bd-37-50-42-00-c1-00-00')
    return IPersistMemory
def _define_IPersistMemory():
    IPersistMemory = win32more.System.Com.IPersistMemory_head
    IPersistMemory.IsDirty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'IsDirty', ()))
    IPersistMemory.Load = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32)(5, 'Load', ((1, 'pMem'),(1, 'cbSize'),)))
    IPersistMemory.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.BOOL,UInt32)(6, 'Save', ((1, 'pMem'),(1, 'fClearDirty'),(1, 'cbSize'),)))
    IPersistMemory.GetSizeMax = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(7, 'GetSizeMax', ((1, 'pCbSize'),)))
    IPersistMemory.InitNew = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'InitNew', ()))
    win32more.System.Com.IPersist
    return IPersistMemory
def _define_IPersistStream_head():
    class IPersistStream(win32more.System.Com.IPersist_head):
        Guid = Guid('00000109-0000-0000-c0-00-00-00-00-00-00-46')
    return IPersistStream
def _define_IPersistStream():
    IPersistStream = win32more.System.Com.IPersistStream_head
    IPersistStream.IsDirty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'IsDirty', ()))
    IPersistStream.Load = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(5, 'Load', ((1, 'pStm'),)))
    IPersistStream.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Foundation.BOOL)(6, 'Save', ((1, 'pStm'),(1, 'fClearDirty'),)))
    IPersistStream.GetSizeMax = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.ULARGE_INTEGER_head))(7, 'GetSizeMax', ((1, 'pcbSize'),)))
    win32more.System.Com.IPersist
    return IPersistStream
def _define_IPersistStreamInit_head():
    class IPersistStreamInit(win32more.System.Com.IPersist_head):
        Guid = Guid('7fd52380-4e07-101b-ae-2d-08-00-2b-2e-c7-13')
    return IPersistStreamInit
def _define_IPersistStreamInit():
    IPersistStreamInit = win32more.System.Com.IPersistStreamInit_head
    IPersistStreamInit.IsDirty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'IsDirty', ()))
    IPersistStreamInit.Load = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(5, 'Load', ((1, 'pStm'),)))
    IPersistStreamInit.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Foundation.BOOL)(6, 'Save', ((1, 'pStm'),(1, 'fClearDirty'),)))
    IPersistStreamInit.GetSizeMax = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.ULARGE_INTEGER_head))(7, 'GetSizeMax', ((1, 'pCbSize'),)))
    IPersistStreamInit.InitNew = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'InitNew', ()))
    win32more.System.Com.IPersist
    return IPersistStreamInit
def _define_IPipeByte_head():
    class IPipeByte(win32more.System.Com.IUnknown_head):
        Guid = Guid('db2f3aca-2f86-11d1-8e-04-00-c0-4f-b9-98-9a')
    return IPipeByte
def _define_IPipeByte():
    IPipeByte = win32more.System.Com.IPipeByte_head
    IPipeByte.Pull = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,POINTER(UInt32))(3, 'Pull', ((1, 'buf'),(1, 'cRequest'),(1, 'pcReturned'),)))
    IPipeByte.Push = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32)(4, 'Push', ((1, 'buf'),(1, 'cSent'),)))
    win32more.System.Com.IUnknown
    return IPipeByte
def _define_IPipeDouble_head():
    class IPipeDouble(win32more.System.Com.IUnknown_head):
        Guid = Guid('db2f3ace-2f86-11d1-8e-04-00-c0-4f-b9-98-9a')
    return IPipeDouble
def _define_IPipeDouble():
    IPipeDouble = win32more.System.Com.IPipeDouble_head
    IPipeDouble.Pull = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),UInt32,POINTER(UInt32))(3, 'Pull', ((1, 'buf'),(1, 'cRequest'),(1, 'pcReturned'),)))
    IPipeDouble.Push = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double),UInt32)(4, 'Push', ((1, 'buf'),(1, 'cSent'),)))
    win32more.System.Com.IUnknown
    return IPipeDouble
def _define_IPipeLong_head():
    class IPipeLong(win32more.System.Com.IUnknown_head):
        Guid = Guid('db2f3acc-2f86-11d1-8e-04-00-c0-4f-b9-98-9a')
    return IPipeLong
def _define_IPipeLong():
    IPipeLong = win32more.System.Com.IPipeLong_head
    IPipeLong.Pull = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),UInt32,POINTER(UInt32))(3, 'Pull', ((1, 'buf'),(1, 'cRequest'),(1, 'pcReturned'),)))
    IPipeLong.Push = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),UInt32)(4, 'Push', ((1, 'buf'),(1, 'cSent'),)))
    win32more.System.Com.IUnknown
    return IPipeLong
def _define_IProcessInitControl_head():
    class IProcessInitControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('72380d55-8d2b-43a3-85-13-2b-6e-f3-14-34-e9')
    return IProcessInitControl
def _define_IProcessInitControl():
    IProcessInitControl = win32more.System.Com.IProcessInitControl_head
    IProcessInitControl.ResetInitializerTimeout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(3, 'ResetInitializerTimeout', ((1, 'dwSecondsRemaining'),)))
    win32more.System.Com.IUnknown
    return IProcessInitControl
def _define_IProcessLock_head():
    class IProcessLock(win32more.System.Com.IUnknown_head):
        Guid = Guid('000001d5-0000-0000-c0-00-00-00-00-00-00-46')
    return IProcessLock
def _define_IProcessLock():
    IProcessLock = win32more.System.Com.IProcessLock_head
    IProcessLock.AddRefOnProcess = COMMETHOD(WINFUNCTYPE(UInt32,)(3, 'AddRefOnProcess', ()))
    IProcessLock.ReleaseRefOnProcess = COMMETHOD(WINFUNCTYPE(UInt32,)(4, 'ReleaseRefOnProcess', ()))
    win32more.System.Com.IUnknown
    return IProcessLock
def _define_IProgressNotify_head():
    class IProgressNotify(win32more.System.Com.IUnknown_head):
        Guid = Guid('a9d758a0-4617-11cf-95-fc-00-aa-00-68-0d-b4')
    return IProgressNotify
def _define_IProgressNotify():
    IProgressNotify = win32more.System.Com.IProgressNotify_head
    IProgressNotify.OnProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Foundation.BOOL,win32more.Foundation.BOOL)(3, 'OnProgress', ((1, 'dwProgressCurrent'),(1, 'dwProgressMaximum'),(1, 'fAccurate'),(1, 'fOwner'),)))
    win32more.System.Com.IUnknown
    return IProgressNotify
def _define_IPSFactoryBuffer_head():
    class IPSFactoryBuffer(win32more.System.Com.IUnknown_head):
        Guid = Guid('d5f569d0-593b-101a-b5-69-08-00-2b-2d-bf-7a')
    return IPSFactoryBuffer
def _define_IPSFactoryBuffer():
    IPSFactoryBuffer = win32more.System.Com.IPSFactoryBuffer_head
    IPSFactoryBuffer.CreateProxy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(win32more.System.Com.IRpcProxyBuffer_head),POINTER(c_void_p))(3, 'CreateProxy', ((1, 'pUnkOuter'),(1, 'riid'),(1, 'ppProxy'),(1, 'ppv'),)))
    IPSFactoryBuffer.CreateStub = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.IRpcStubBuffer_head))(4, 'CreateStub', ((1, 'riid'),(1, 'pUnkServer'),(1, 'ppStub'),)))
    win32more.System.Com.IUnknown
    return IPSFactoryBuffer
def _define_IReleaseMarshalBuffers_head():
    class IReleaseMarshalBuffers(win32more.System.Com.IUnknown_head):
        Guid = Guid('eb0cb9e8-7996-11d2-87-2e-00-00-f8-08-08-59')
    return IReleaseMarshalBuffers
def _define_IReleaseMarshalBuffers():
    IReleaseMarshalBuffers = win32more.System.Com.IReleaseMarshalBuffers_head
    IReleaseMarshalBuffers.ReleaseMarshalBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.RPCOLEMESSAGE_head),UInt32,win32more.System.Com.IUnknown_head)(3, 'ReleaseMarshalBuffer', ((1, 'pMsg'),(1, 'dwFlags'),(1, 'pChnl'),)))
    win32more.System.Com.IUnknown
    return IReleaseMarshalBuffers
def _define_IROTData_head():
    class IROTData(win32more.System.Com.IUnknown_head):
        Guid = Guid('f29f6bc0-5021-11ce-aa-15-00-00-69-01-29-3f')
    return IROTData
def _define_IROTData():
    IROTData = win32more.System.Com.IROTData_head
    IROTData.GetComparisonData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,POINTER(UInt32))(3, 'GetComparisonData', ((1, 'pbData'),(1, 'cbMax'),(1, 'pcbData'),)))
    win32more.System.Com.IUnknown
    return IROTData
def _define_IRpcChannelBuffer_head():
    class IRpcChannelBuffer(win32more.System.Com.IUnknown_head):
        Guid = Guid('d5f56b60-593b-101a-b5-69-08-00-2b-2d-bf-7a')
    return IRpcChannelBuffer
def _define_IRpcChannelBuffer():
    IRpcChannelBuffer = win32more.System.Com.IRpcChannelBuffer_head
    IRpcChannelBuffer.GetBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.RPCOLEMESSAGE_head),POINTER(Guid))(3, 'GetBuffer', ((1, 'pMessage'),(1, 'riid'),)))
    IRpcChannelBuffer.SendReceive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.RPCOLEMESSAGE_head),POINTER(UInt32))(4, 'SendReceive', ((1, 'pMessage'),(1, 'pStatus'),)))
    IRpcChannelBuffer.FreeBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.RPCOLEMESSAGE_head))(5, 'FreeBuffer', ((1, 'pMessage'),)))
    IRpcChannelBuffer.GetDestCtx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(c_void_p))(6, 'GetDestCtx', ((1, 'pdwDestContext'),(1, 'ppvDestContext'),)))
    IRpcChannelBuffer.IsConnected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'IsConnected', ()))
    win32more.System.Com.IUnknown
    return IRpcChannelBuffer
def _define_IRpcChannelBuffer2_head():
    class IRpcChannelBuffer2(win32more.System.Com.IRpcChannelBuffer_head):
        Guid = Guid('594f31d0-7f19-11d0-b1-94-00-a0-c9-0d-c8-bf')
    return IRpcChannelBuffer2
def _define_IRpcChannelBuffer2():
    IRpcChannelBuffer2 = win32more.System.Com.IRpcChannelBuffer2_head
    IRpcChannelBuffer2.GetProtocolVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(8, 'GetProtocolVersion', ((1, 'pdwVersion'),)))
    win32more.System.Com.IRpcChannelBuffer
    return IRpcChannelBuffer2
def _define_IRpcChannelBuffer3_head():
    class IRpcChannelBuffer3(win32more.System.Com.IRpcChannelBuffer2_head):
        Guid = Guid('25b15600-0115-11d0-bf-0d-00-aa-00-b8-df-d2')
    return IRpcChannelBuffer3
def _define_IRpcChannelBuffer3():
    IRpcChannelBuffer3 = win32more.System.Com.IRpcChannelBuffer3_head
    IRpcChannelBuffer3.Send = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.RPCOLEMESSAGE_head),POINTER(UInt32))(9, 'Send', ((1, 'pMsg'),(1, 'pulStatus'),)))
    IRpcChannelBuffer3.Receive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.RPCOLEMESSAGE_head),UInt32,POINTER(UInt32))(10, 'Receive', ((1, 'pMsg'),(1, 'ulSize'),(1, 'pulStatus'),)))
    IRpcChannelBuffer3.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.RPCOLEMESSAGE_head))(11, 'Cancel', ((1, 'pMsg'),)))
    IRpcChannelBuffer3.GetCallContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.RPCOLEMESSAGE_head),POINTER(Guid),POINTER(c_void_p))(12, 'GetCallContext', ((1, 'pMsg'),(1, 'riid'),(1, 'pInterface'),)))
    IRpcChannelBuffer3.GetDestCtxEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.RPCOLEMESSAGE_head),POINTER(UInt32),POINTER(c_void_p))(13, 'GetDestCtxEx', ((1, 'pMsg'),(1, 'pdwDestContext'),(1, 'ppvDestContext'),)))
    IRpcChannelBuffer3.GetState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.RPCOLEMESSAGE_head),POINTER(UInt32))(14, 'GetState', ((1, 'pMsg'),(1, 'pState'),)))
    IRpcChannelBuffer3.RegisterAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.RPCOLEMESSAGE_head),win32more.System.Com.IAsyncManager_head)(15, 'RegisterAsync', ((1, 'pMsg'),(1, 'pAsyncMgr'),)))
    win32more.System.Com.IRpcChannelBuffer2
    return IRpcChannelBuffer3
def _define_IRpcHelper_head():
    class IRpcHelper(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000149-0000-0000-c0-00-00-00-00-00-00-46')
    return IRpcHelper
def _define_IRpcHelper():
    IRpcHelper = win32more.System.Com.IRpcHelper_head
    IRpcHelper.GetDCOMProtocolVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetDCOMProtocolVersion', ((1, 'pComVersion'),)))
    IRpcHelper.GetIIDFromOBJREF = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(POINTER(Guid)))(4, 'GetIIDFromOBJREF', ((1, 'pObjRef'),(1, 'piid'),)))
    win32more.System.Com.IUnknown
    return IRpcHelper
def _define_IRpcOptions_head():
    class IRpcOptions(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000144-0000-0000-c0-00-00-00-00-00-00-46')
    return IRpcOptions
def _define_IRpcOptions():
    IRpcOptions = win32more.System.Com.IRpcOptions_head
    IRpcOptions.Set = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.RPCOPT_PROPERTIES,UIntPtr)(3, 'Set', ((1, 'pPrx'),(1, 'dwProperty'),(1, 'dwValue'),)))
    IRpcOptions.Query = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.RPCOPT_PROPERTIES,POINTER(UIntPtr))(4, 'Query', ((1, 'pPrx'),(1, 'dwProperty'),(1, 'pdwValue'),)))
    win32more.System.Com.IUnknown
    return IRpcOptions
def _define_IRpcProxyBuffer_head():
    class IRpcProxyBuffer(win32more.System.Com.IUnknown_head):
        Guid = Guid('d5f56a34-593b-101a-b5-69-08-00-2b-2d-bf-7a')
    return IRpcProxyBuffer
def _define_IRpcProxyBuffer():
    IRpcProxyBuffer = win32more.System.Com.IRpcProxyBuffer_head
    IRpcProxyBuffer.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IRpcChannelBuffer_head)(3, 'Connect', ((1, 'pRpcChannelBuffer'),)))
    IRpcProxyBuffer.Disconnect = COMMETHOD(WINFUNCTYPE(Void,)(4, 'Disconnect', ()))
    win32more.System.Com.IUnknown
    return IRpcProxyBuffer
def _define_IRpcStubBuffer_head():
    class IRpcStubBuffer(win32more.System.Com.IUnknown_head):
        Guid = Guid('d5f56afc-593b-101a-b5-69-08-00-2b-2d-bf-7a')
    return IRpcStubBuffer
def _define_IRpcStubBuffer():
    IRpcStubBuffer = win32more.System.Com.IRpcStubBuffer_head
    IRpcStubBuffer.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(3, 'Connect', ((1, 'pUnkServer'),)))
    IRpcStubBuffer.Disconnect = COMMETHOD(WINFUNCTYPE(Void,)(4, 'Disconnect', ()))
    IRpcStubBuffer.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.RPCOLEMESSAGE_head),win32more.System.Com.IRpcChannelBuffer_head)(5, 'Invoke', ((1, '_prpcmsg'),(1, '_pRpcChannelBuffer'),)))
    IRpcStubBuffer.IsIIDSupported = COMMETHOD(WINFUNCTYPE(win32more.System.Com.IRpcStubBuffer_head,POINTER(Guid))(6, 'IsIIDSupported', ((1, 'riid'),)))
    IRpcStubBuffer.CountRefs = COMMETHOD(WINFUNCTYPE(UInt32,)(7, 'CountRefs', ()))
    IRpcStubBuffer.DebugServerQueryInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_void_p))(8, 'DebugServerQueryInterface', ((1, 'ppv'),)))
    IRpcStubBuffer.DebugServerRelease = COMMETHOD(WINFUNCTYPE(Void,c_void_p)(9, 'DebugServerRelease', ((1, 'pv'),)))
    win32more.System.Com.IUnknown
    return IRpcStubBuffer
def _define_IRpcSyntaxNegotiate_head():
    class IRpcSyntaxNegotiate(win32more.System.Com.IUnknown_head):
        Guid = Guid('58a08519-24c8-4935-b4-82-3f-d8-23-33-3a-4f')
    return IRpcSyntaxNegotiate
def _define_IRpcSyntaxNegotiate():
    IRpcSyntaxNegotiate = win32more.System.Com.IRpcSyntaxNegotiate_head
    IRpcSyntaxNegotiate.NegotiateSyntax = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.RPCOLEMESSAGE_head))(3, 'NegotiateSyntax', ((1, 'pMsg'),)))
    win32more.System.Com.IUnknown
    return IRpcSyntaxNegotiate
def _define_IRunnableObject_head():
    class IRunnableObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000126-0000-0000-c0-00-00-00-00-00-00-46')
    return IRunnableObject
def _define_IRunnableObject():
    IRunnableObject = win32more.System.Com.IRunnableObject_head
    IRunnableObject.GetRunningClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'GetRunningClass', ((1, 'lpClsid'),)))
    IRunnableObject.Run = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head)(4, 'Run', ((1, 'pbc'),)))
    IRunnableObject.IsRunning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(5, 'IsRunning', ()))
    IRunnableObject.LockRunning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Foundation.BOOL)(6, 'LockRunning', ((1, 'fLock'),(1, 'fLastUnlockCloses'),)))
    IRunnableObject.SetContainedObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(7, 'SetContainedObject', ((1, 'fContained'),)))
    win32more.System.Com.IUnknown
    return IRunnableObject
def _define_IRunningObjectTable_head():
    class IRunningObjectTable(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000010-0000-0000-c0-00-00-00-00-00-00-46')
    return IRunningObjectTable
def _define_IRunningObjectTable():
    IRunningObjectTable = win32more.System.Com.IRunningObjectTable_head
    IRunningObjectTable.Register = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.ROT_FLAGS,win32more.System.Com.IUnknown_head,win32more.System.Com.IMoniker_head,POINTER(UInt32))(3, 'Register', ((1, 'grfFlags'),(1, 'punkObject'),(1, 'pmkObjectName'),(1, 'pdwRegister'),)))
    IRunningObjectTable.Revoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Revoke', ((1, 'dwRegister'),)))
    IRunningObjectTable.IsRunning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head)(5, 'IsRunning', ((1, 'pmkObjectName'),)))
    IRunningObjectTable.GetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,POINTER(win32more.System.Com.IUnknown_head))(6, 'GetObject', ((1, 'pmkObjectName'),(1, 'ppunkObject'),)))
    IRunningObjectTable.NoteChangeTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.FILETIME_head))(7, 'NoteChangeTime', ((1, 'dwRegister'),(1, 'pfiletime'),)))
    IRunningObjectTable.GetTimeOfLastChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,POINTER(win32more.Foundation.FILETIME_head))(8, 'GetTimeOfLastChange', ((1, 'pmkObjectName'),(1, 'pfiletime'),)))
    IRunningObjectTable.EnumRunning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumMoniker_head))(9, 'EnumRunning', ((1, 'ppenumMoniker'),)))
    win32more.System.Com.IUnknown
    return IRunningObjectTable
def _define_ISequentialStream_head():
    class ISequentialStream(win32more.System.Com.IUnknown_head):
        Guid = Guid('0c733a30-2a1c-11ce-ad-e5-00-aa-00-44-77-3d')
    return ISequentialStream
def _define_ISequentialStream():
    ISequentialStream = win32more.System.Com.ISequentialStream_head
    ISequentialStream.Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(UInt32))(3, 'Read', ((1, 'pv'),(1, 'cb'),(1, 'pcbRead'),)))
    ISequentialStream.Write = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(UInt32))(4, 'Write', ((1, 'pv'),(1, 'cb'),(1, 'pcbWritten'),)))
    win32more.System.Com.IUnknown
    return ISequentialStream
def _define_IServerSecurity_head():
    class IServerSecurity(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000013e-0000-0000-c0-00-00-00-00-00-00-46')
    return IServerSecurity
def _define_IServerSecurity():
    IServerSecurity = win32more.System.Com.IServerSecurity_head
    IServerSecurity.QueryBlanket = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(POINTER(UInt16)),POINTER(UInt32),POINTER(UInt32),POINTER(c_void_p),POINTER(UInt32))(3, 'QueryBlanket', ((1, 'pAuthnSvc'),(1, 'pAuthzSvc'),(1, 'pServerPrincName'),(1, 'pAuthnLevel'),(1, 'pImpLevel'),(1, 'pPrivs'),(1, 'pCapabilities'),)))
    IServerSecurity.ImpersonateClient = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'ImpersonateClient', ()))
    IServerSecurity.RevertToSelf = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'RevertToSelf', ()))
    IServerSecurity.IsImpersonating = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(6, 'IsImpersonating', ()))
    win32more.System.Com.IUnknown
    return IServerSecurity
def _define_IServiceProvider_head():
    class IServiceProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('6d5140c1-7436-11ce-80-34-00-aa-00-60-09-fa')
    return IServiceProvider
def _define_IServiceProvider():
    IServiceProvider = win32more.System.Com.IServiceProvider_head
    IServiceProvider.QueryService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(c_void_p))(3, 'QueryService', ((1, 'guidService'),(1, 'riid'),(1, 'ppvObject'),)))
    win32more.System.Com.IUnknown
    return IServiceProvider
def _define_IStdMarshalInfo_head():
    class IStdMarshalInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000018-0000-0000-c0-00-00-00-00-00-00-46')
    return IStdMarshalInfo
def _define_IStdMarshalInfo():
    IStdMarshalInfo = win32more.System.Com.IStdMarshalInfo_head
    IStdMarshalInfo.GetClassForHandler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,POINTER(Guid))(3, 'GetClassForHandler', ((1, 'dwDestContext'),(1, 'pvDestContext'),(1, 'pClsid'),)))
    win32more.System.Com.IUnknown
    return IStdMarshalInfo
def _define_IStream_head():
    class IStream(win32more.System.Com.ISequentialStream_head):
        Guid = Guid('0000000c-0000-0000-c0-00-00-00-00-00-00-46')
    return IStream
def _define_IStream():
    IStream = win32more.System.Com.IStream_head
    IStream.Seek = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.LARGE_INTEGER,win32more.System.Com.STREAM_SEEK,POINTER(win32more.Foundation.ULARGE_INTEGER_head))(5, 'Seek', ((1, 'dlibMove'),(1, 'dwOrigin'),(1, 'plibNewPosition'),)))
    IStream.SetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.ULARGE_INTEGER)(6, 'SetSize', ((1, 'libNewSize'),)))
    IStream.CopyTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Foundation.ULARGE_INTEGER,POINTER(win32more.Foundation.ULARGE_INTEGER_head),POINTER(win32more.Foundation.ULARGE_INTEGER_head))(7, 'CopyTo', ((1, 'pstm'),(1, 'cb'),(1, 'pcbRead'),(1, 'pcbWritten'),)))
    IStream.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.STGC)(8, 'Commit', ((1, 'grfCommitFlags'),)))
    IStream.Revert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'Revert', ()))
    IStream.LockRegion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.ULARGE_INTEGER,win32more.Foundation.ULARGE_INTEGER,win32more.System.Com.LOCKTYPE)(10, 'LockRegion', ((1, 'libOffset'),(1, 'cb'),(1, 'dwLockType'),)))
    IStream.UnlockRegion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.ULARGE_INTEGER,win32more.Foundation.ULARGE_INTEGER,UInt32)(11, 'UnlockRegion', ((1, 'libOffset'),(1, 'cb'),(1, 'dwLockType'),)))
    IStream.Stat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.STATSTG_head),win32more.System.Com.STATFLAG)(12, 'Stat', ((1, 'pstatstg'),(1, 'grfStatFlag'),)))
    IStream.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head))(13, 'Clone', ((1, 'ppstm'),)))
    win32more.System.Com.ISequentialStream
    return IStream
def _define_ISupportErrorInfo_head():
    class ISupportErrorInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('df0b3d60-548f-101b-8e-65-08-00-2b-2b-d1-19')
    return ISupportErrorInfo
def _define_ISupportErrorInfo():
    ISupportErrorInfo = win32more.System.Com.ISupportErrorInfo_head
    ISupportErrorInfo.InterfaceSupportsErrorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'InterfaceSupportsErrorInfo', ((1, 'riid'),)))
    win32more.System.Com.IUnknown
    return ISupportErrorInfo
def _define_ISurrogate_head():
    class ISurrogate(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000022-0000-0000-c0-00-00-00-00-00-00-46')
    return ISurrogate
def _define_ISurrogate():
    ISurrogate = win32more.System.Com.ISurrogate_head
    ISurrogate.LoadDllServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'LoadDllServer', ((1, 'Clsid'),)))
    ISurrogate.FreeSurrogate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'FreeSurrogate', ()))
    win32more.System.Com.IUnknown
    return ISurrogate
def _define_ISurrogateService_head():
    class ISurrogateService(win32more.System.Com.IUnknown_head):
        Guid = Guid('000001d4-0000-0000-c0-00-00-00-00-00-00-46')
    return ISurrogateService
def _define_ISurrogateService():
    ISurrogateService = win32more.System.Com.ISurrogateService_head
    ISurrogateService.Init = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IProcessLock_head,POINTER(win32more.Foundation.BOOL))(3, 'Init', ((1, 'rguidProcessID'),(1, 'pProcessLock'),(1, 'pfApplicationAware'),)))
    ISurrogateService.ApplicationLaunch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.ApplicationType)(4, 'ApplicationLaunch', ((1, 'rguidApplID'),(1, 'appType'),)))
    ISurrogateService.ApplicationFree = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(5, 'ApplicationFree', ((1, 'rguidApplID'),)))
    ISurrogateService.CatalogRefresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'CatalogRefresh', ((1, 'ulReserved'),)))
    ISurrogateService.ProcessShutdown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.ShutdownType)(7, 'ProcessShutdown', ((1, 'shutdownType'),)))
    win32more.System.Com.IUnknown
    return ISurrogateService
def _define_ISynchronize_head():
    class ISynchronize(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000030-0000-0000-c0-00-00-00-00-00-00-46')
    return ISynchronize
def _define_ISynchronize():
    ISynchronize = win32more.System.Com.ISynchronize_head
    ISynchronize.Wait = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32)(3, 'Wait', ((1, 'dwFlags'),(1, 'dwMilliseconds'),)))
    ISynchronize.Signal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Signal', ()))
    ISynchronize.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    win32more.System.Com.IUnknown
    return ISynchronize
def _define_ISynchronizeContainer_head():
    class ISynchronizeContainer(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000033-0000-0000-c0-00-00-00-00-00-00-46')
    return ISynchronizeContainer
def _define_ISynchronizeContainer():
    ISynchronizeContainer = win32more.System.Com.ISynchronizeContainer_head
    ISynchronizeContainer.AddSynchronize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.ISynchronize_head)(3, 'AddSynchronize', ((1, 'pSync'),)))
    ISynchronizeContainer.WaitMultiple = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.System.Com.ISynchronize_head))(4, 'WaitMultiple', ((1, 'dwFlags'),(1, 'dwTimeOut'),(1, 'ppSync'),)))
    win32more.System.Com.IUnknown
    return ISynchronizeContainer
def _define_ISynchronizeEvent_head():
    class ISynchronizeEvent(win32more.System.Com.ISynchronizeHandle_head):
        Guid = Guid('00000032-0000-0000-c0-00-00-00-00-00-00-46')
    return ISynchronizeEvent
def _define_ISynchronizeEvent():
    ISynchronizeEvent = win32more.System.Com.ISynchronizeEvent_head
    ISynchronizeEvent.SetEventHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE))(4, 'SetEventHandle', ((1, 'ph'),)))
    win32more.System.Com.ISynchronizeHandle
    return ISynchronizeEvent
def _define_ISynchronizeHandle_head():
    class ISynchronizeHandle(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000031-0000-0000-c0-00-00-00-00-00-00-46')
    return ISynchronizeHandle
def _define_ISynchronizeHandle():
    ISynchronizeHandle = win32more.System.Com.ISynchronizeHandle_head
    ISynchronizeHandle.GetHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HANDLE))(3, 'GetHandle', ((1, 'ph'),)))
    win32more.System.Com.IUnknown
    return ISynchronizeHandle
def _define_ISynchronizeMutex_head():
    class ISynchronizeMutex(win32more.System.Com.ISynchronize_head):
        Guid = Guid('00000025-0000-0000-c0-00-00-00-00-00-00-46')
    return ISynchronizeMutex
def _define_ISynchronizeMutex():
    ISynchronizeMutex = win32more.System.Com.ISynchronizeMutex_head
    ISynchronizeMutex.ReleaseMutex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'ReleaseMutex', ()))
    win32more.System.Com.ISynchronize
    return ISynchronizeMutex
def _define_ITimeAndNoticeControl_head():
    class ITimeAndNoticeControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('bc0bf6ae-8878-11d1-83-e9-00-c0-4f-c2-c6-d4')
    return ITimeAndNoticeControl
def _define_ITimeAndNoticeControl():
    ITimeAndNoticeControl = win32more.System.Com.ITimeAndNoticeControl_head
    ITimeAndNoticeControl.SuppressChanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32)(3, 'SuppressChanges', ((1, 'res1'),(1, 'res2'),)))
    win32more.System.Com.IUnknown
    return ITimeAndNoticeControl
def _define_ITypeComp_head():
    class ITypeComp(win32more.System.Com.IUnknown_head):
        Guid = Guid('00020403-0000-0000-c0-00-00-00-00-00-00-46')
    return ITypeComp
def _define_ITypeComp():
    ITypeComp = win32more.System.Com.ITypeComp_head
    ITypeComp.Bind = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt16,POINTER(win32more.System.Com.ITypeInfo_head),POINTER(win32more.System.Com.DESCKIND),POINTER(win32more.System.Com.BINDPTR_head))(3, 'Bind', ((1, 'szName'),(1, 'lHashVal'),(1, 'wFlags'),(1, 'ppTInfo'),(1, 'pDescKind'),(1, 'pBindPtr'),)))
    ITypeComp.BindType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.System.Com.ITypeInfo_head),POINTER(win32more.System.Com.ITypeComp_head))(4, 'BindType', ((1, 'szName'),(1, 'lHashVal'),(1, 'ppTInfo'),(1, 'ppTComp'),)))
    win32more.System.Com.IUnknown
    return ITypeComp
def _define_ITypeInfo_head():
    class ITypeInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('00020401-0000-0000-c0-00-00-00-00-00-00-46')
    return ITypeInfo
def _define_ITypeInfo():
    ITypeInfo = win32more.System.Com.ITypeInfo_head
    ITypeInfo.GetTypeAttr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.TYPEATTR_head)))(3, 'GetTypeAttr', ((1, 'ppTypeAttr'),)))
    ITypeInfo.GetTypeComp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.ITypeComp_head))(4, 'GetTypeComp', ((1, 'ppTComp'),)))
    ITypeInfo.GetFuncDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.System.Com.FUNCDESC_head)))(5, 'GetFuncDesc', ((1, 'index'),(1, 'ppFuncDesc'),)))
    ITypeInfo.GetVarDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.System.Com.VARDESC_head)))(6, 'GetVarDesc', ((1, 'index'),(1, 'ppVarDesc'),)))
    ITypeInfo.GetNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR),UInt32,POINTER(UInt32))(7, 'GetNames', ((1, 'memid'),(1, 'rgBstrNames'),(1, 'cMaxNames'),(1, 'pcNames'),)))
    ITypeInfo.GetRefTypeOfImplType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32))(8, 'GetRefTypeOfImplType', ((1, 'index'),(1, 'pRefType'),)))
    ITypeInfo.GetImplTypeFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Int32))(9, 'GetImplTypeFlags', ((1, 'index'),(1, 'pImplTypeFlags'),)))
    ITypeInfo.GetIDsOfNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(Int32))(10, 'GetIDsOfNames', ((1, 'rgszNames'),(1, 'cNames'),(1, 'pMemId'),)))
    ITypeInfo.Invoke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,Int32,win32more.System.Com.DISPATCH_FLAGS,POINTER(win32more.System.Com.DISPPARAMS_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.EXCEPINFO_head),POINTER(UInt32))(11, 'Invoke', ((1, 'pvInstance'),(1, 'memid'),(1, 'wFlags'),(1, 'pDispParams'),(1, 'pVarResult'),(1, 'pExcepInfo'),(1, 'puArgErr'),)))
    ITypeInfo.GetDocumentation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(UInt32),POINTER(win32more.Foundation.BSTR))(12, 'GetDocumentation', ((1, 'memid'),(1, 'pBstrName'),(1, 'pBstrDocString'),(1, 'pdwHelpContext'),(1, 'pBstrHelpFile'),)))
    ITypeInfo.GetDllEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.INVOKEKIND,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(UInt16))(13, 'GetDllEntry', ((1, 'memid'),(1, 'invKind'),(1, 'pBstrDllName'),(1, 'pBstrName'),(1, 'pwOrdinal'),)))
    ITypeInfo.GetRefTypeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.ITypeInfo_head))(14, 'GetRefTypeInfo', ((1, 'hRefType'),(1, 'ppTInfo'),)))
    ITypeInfo.AddressOfMember = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.INVOKEKIND,POINTER(c_void_p))(15, 'AddressOfMember', ((1, 'memid'),(1, 'invKind'),(1, 'ppv'),)))
    ITypeInfo.CreateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p))(16, 'CreateInstance', ((1, 'pUnkOuter'),(1, 'riid'),(1, 'ppvObj'),)))
    ITypeInfo.GetMops = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR))(17, 'GetMops', ((1, 'memid'),(1, 'pBstrMops'),)))
    ITypeInfo.GetContainingTypeLib = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.ITypeLib_head),POINTER(UInt32))(18, 'GetContainingTypeLib', ((1, 'ppTLib'),(1, 'pIndex'),)))
    ITypeInfo.ReleaseTypeAttr = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.System.Com.TYPEATTR_head))(19, 'ReleaseTypeAttr', ((1, 'pTypeAttr'),)))
    ITypeInfo.ReleaseFuncDesc = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.System.Com.FUNCDESC_head))(20, 'ReleaseFuncDesc', ((1, 'pFuncDesc'),)))
    ITypeInfo.ReleaseVarDesc = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.System.Com.VARDESC_head))(21, 'ReleaseVarDesc', ((1, 'pVarDesc'),)))
    win32more.System.Com.IUnknown
    return ITypeInfo
def _define_ITypeInfo2_head():
    class ITypeInfo2(win32more.System.Com.ITypeInfo_head):
        Guid = Guid('00020412-0000-0000-c0-00-00-00-00-00-00-46')
    return ITypeInfo2
def _define_ITypeInfo2():
    ITypeInfo2 = win32more.System.Com.ITypeInfo2_head
    ITypeInfo2.GetTypeKind = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.TYPEKIND))(22, 'GetTypeKind', ((1, 'pTypeKind'),)))
    ITypeInfo2.GetTypeFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(23, 'GetTypeFlags', ((1, 'pTypeFlags'),)))
    ITypeInfo2.GetFuncIndexOfMemId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.INVOKEKIND,POINTER(UInt32))(24, 'GetFuncIndexOfMemId', ((1, 'memid'),(1, 'invKind'),(1, 'pFuncIndex'),)))
    ITypeInfo2.GetVarIndexOfMemId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(UInt32))(25, 'GetVarIndexOfMemId', ((1, 'memid'),(1, 'pVarIndex'),)))
    ITypeInfo2.GetCustData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.VARIANT_head))(26, 'GetCustData', ((1, 'guid'),(1, 'pVarVal'),)))
    ITypeInfo2.GetFuncCustData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.System.Com.VARIANT_head))(27, 'GetFuncCustData', ((1, 'index'),(1, 'guid'),(1, 'pVarVal'),)))
    ITypeInfo2.GetParamCustData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Guid),POINTER(win32more.System.Com.VARIANT_head))(28, 'GetParamCustData', ((1, 'indexFunc'),(1, 'indexParam'),(1, 'guid'),(1, 'pVarVal'),)))
    ITypeInfo2.GetVarCustData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.System.Com.VARIANT_head))(29, 'GetVarCustData', ((1, 'index'),(1, 'guid'),(1, 'pVarVal'),)))
    ITypeInfo2.GetImplTypeCustData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.System.Com.VARIANT_head))(30, 'GetImplTypeCustData', ((1, 'index'),(1, 'guid'),(1, 'pVarVal'),)))
    ITypeInfo2.GetDocumentation2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,POINTER(win32more.Foundation.BSTR),POINTER(UInt32),POINTER(win32more.Foundation.BSTR))(31, 'GetDocumentation2', ((1, 'memid'),(1, 'lcid'),(1, 'pbstrHelpString'),(1, 'pdwHelpStringContext'),(1, 'pbstrHelpStringDll'),)))
    ITypeInfo2.GetAllCustData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.CUSTDATA_head))(32, 'GetAllCustData', ((1, 'pCustData'),)))
    ITypeInfo2.GetAllFuncCustData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.CUSTDATA_head))(33, 'GetAllFuncCustData', ((1, 'index'),(1, 'pCustData'),)))
    ITypeInfo2.GetAllParamCustData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.System.Com.CUSTDATA_head))(34, 'GetAllParamCustData', ((1, 'indexFunc'),(1, 'indexParam'),(1, 'pCustData'),)))
    ITypeInfo2.GetAllVarCustData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.CUSTDATA_head))(35, 'GetAllVarCustData', ((1, 'index'),(1, 'pCustData'),)))
    ITypeInfo2.GetAllImplTypeCustData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.CUSTDATA_head))(36, 'GetAllImplTypeCustData', ((1, 'index'),(1, 'pCustData'),)))
    win32more.System.Com.ITypeInfo
    return ITypeInfo2
def _define_ITypeLib_head():
    class ITypeLib(win32more.System.Com.IUnknown_head):
        Guid = Guid('00020402-0000-0000-c0-00-00-00-00-00-00-46')
    return ITypeLib
def _define_ITypeLib():
    ITypeLib = win32more.System.Com.ITypeLib_head
    ITypeLib.GetTypeInfoCount = COMMETHOD(WINFUNCTYPE(UInt32,)(3, 'GetTypeInfoCount', ()))
    ITypeLib.GetTypeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.ITypeInfo_head))(4, 'GetTypeInfo', ((1, 'index'),(1, 'ppTInfo'),)))
    ITypeLib.GetTypeInfoType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.TYPEKIND))(5, 'GetTypeInfoType', ((1, 'index'),(1, 'pTKind'),)))
    ITypeLib.GetTypeInfoOfGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.ITypeInfo_head))(6, 'GetTypeInfoOfGuid', ((1, 'guid'),(1, 'ppTinfo'),)))
    ITypeLib.GetLibAttr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.TLIBATTR_head)))(7, 'GetLibAttr', ((1, 'ppTLibAttr'),)))
    ITypeLib.GetTypeComp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.ITypeComp_head))(8, 'GetTypeComp', ((1, 'ppTComp'),)))
    ITypeLib.GetDocumentation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR),POINTER(UInt32),POINTER(win32more.Foundation.BSTR))(9, 'GetDocumentation', ((1, 'index'),(1, 'pBstrName'),(1, 'pBstrDocString'),(1, 'pdwHelpContext'),(1, 'pBstrHelpFile'),)))
    ITypeLib.IsName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.BOOL))(10, 'IsName', ((1, 'szNameBuf'),(1, 'lHashVal'),(1, 'pfName'),)))
    ITypeLib.FindName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.System.Com.ITypeInfo_head),POINTER(Int32),POINTER(UInt16))(11, 'FindName', ((1, 'szNameBuf'),(1, 'lHashVal'),(1, 'ppTInfo'),(1, 'rgMemId'),(1, 'pcFound'),)))
    ITypeLib.ReleaseTLibAttr = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.System.Com.TLIBATTR_head))(12, 'ReleaseTLibAttr', ((1, 'pTLibAttr'),)))
    win32more.System.Com.IUnknown
    return ITypeLib
def _define_ITypeLib2_head():
    class ITypeLib2(win32more.System.Com.ITypeLib_head):
        Guid = Guid('00020411-0000-0000-c0-00-00-00-00-00-00-46')
    return ITypeLib2
def _define_ITypeLib2():
    ITypeLib2 = win32more.System.Com.ITypeLib2_head
    ITypeLib2.GetCustData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.VARIANT_head))(13, 'GetCustData', ((1, 'guid'),(1, 'pVarVal'),)))
    ITypeLib2.GetLibStatistics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32))(14, 'GetLibStatistics', ((1, 'pcUniqueNames'),(1, 'pcchUniqueNames'),)))
    ITypeLib2.GetDocumentation2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,POINTER(win32more.Foundation.BSTR),POINTER(UInt32),POINTER(win32more.Foundation.BSTR))(15, 'GetDocumentation2', ((1, 'index'),(1, 'lcid'),(1, 'pbstrHelpString'),(1, 'pdwHelpStringContext'),(1, 'pbstrHelpStringDll'),)))
    ITypeLib2.GetAllCustData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.CUSTDATA_head))(16, 'GetAllCustData', ((1, 'pCustData'),)))
    win32more.System.Com.ITypeLib
    return ITypeLib2
def _define_ITypeLibRegistration_head():
    class ITypeLibRegistration(win32more.System.Com.IUnknown_head):
        Guid = Guid('76a3e735-02df-4a12-98-eb-04-3a-d3-60-0a-f3')
    return ITypeLibRegistration
def _define_ITypeLibRegistration():
    ITypeLibRegistration = win32more.System.Com.ITypeLibRegistration_head
    ITypeLibRegistration.GetGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(3, 'GetGuid', ((1, 'pGuid'),)))
    ITypeLibRegistration.GetVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'GetVersion', ((1, 'pVersion'),)))
    ITypeLibRegistration.GetLcid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(5, 'GetLcid', ((1, 'pLcid'),)))
    ITypeLibRegistration.GetWin32Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(6, 'GetWin32Path', ((1, 'pWin32Path'),)))
    ITypeLibRegistration.GetWin64Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'GetWin64Path', ((1, 'pWin64Path'),)))
    ITypeLibRegistration.GetDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'GetDisplayName', ((1, 'pDisplayName'),)))
    ITypeLibRegistration.GetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(9, 'GetFlags', ((1, 'pFlags'),)))
    ITypeLibRegistration.GetHelpDir = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'GetHelpDir', ((1, 'pHelpDir'),)))
    win32more.System.Com.IUnknown
    return ITypeLibRegistration
def _define_ITypeLibRegistrationReader_head():
    class ITypeLibRegistrationReader(win32more.System.Com.IUnknown_head):
        Guid = Guid('ed6a8a2a-b160-4e77-8f-73-aa-74-35-cd-5c-27')
    return ITypeLibRegistrationReader
def _define_ITypeLibRegistrationReader():
    ITypeLibRegistrationReader = win32more.System.Com.ITypeLibRegistrationReader_head
    ITypeLibRegistrationReader.EnumTypeLibRegistrations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumUnknown_head))(3, 'EnumTypeLibRegistrations', ((1, 'ppEnumUnknown'),)))
    win32more.System.Com.IUnknown
    return ITypeLibRegistrationReader
def _define_IUnknown_head():
    class IUnknown(c_void_p):
        Guid = Guid('00000000-0000-0000-c0-00-00-00-00-00-00-46')
    return IUnknown
def _define_IUnknown():
    IUnknown = win32more.System.Com.IUnknown_head
    IUnknown.QueryInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(0, 'QueryInterface', ((1, 'riid'),(1, 'ppvObject'),)))
    IUnknown.AddRef = COMMETHOD(WINFUNCTYPE(UInt32,)(1, 'AddRef', ()))
    IUnknown.Release = COMMETHOD(WINFUNCTYPE(UInt32,)(2, 'Release', ()))
    return IUnknown
def _define_IUri_head():
    class IUri(win32more.System.Com.IUnknown_head):
        Guid = Guid('a39ee748-6a27-4817-a6-f2-13-91-4b-ef-58-90')
    return IUri
def _define_IUri():
    IUri = win32more.System.Com.IUri_head
    IUri.GetPropertyBSTR = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Uri_PROPERTY,POINTER(win32more.Foundation.BSTR),UInt32)(3, 'GetPropertyBSTR', ((1, 'uriProp'),(1, 'pbstrProperty'),(1, 'dwFlags'),)))
    IUri.GetPropertyLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Uri_PROPERTY,POINTER(UInt32),UInt32)(4, 'GetPropertyLength', ((1, 'uriProp'),(1, 'pcchProperty'),(1, 'dwFlags'),)))
    IUri.GetPropertyDWORD = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Uri_PROPERTY,POINTER(UInt32),UInt32)(5, 'GetPropertyDWORD', ((1, 'uriProp'),(1, 'pdwProperty'),(1, 'dwFlags'),)))
    IUri.HasProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Uri_PROPERTY,POINTER(win32more.Foundation.BOOL))(6, 'HasProperty', ((1, 'uriProp'),(1, 'pfHasProperty'),)))
    IUri.GetAbsoluteUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(7, 'GetAbsoluteUri', ((1, 'pbstrAbsoluteUri'),)))
    IUri.GetAuthority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(8, 'GetAuthority', ((1, 'pbstrAuthority'),)))
    IUri.GetDisplayUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(9, 'GetDisplayUri', ((1, 'pbstrDisplayString'),)))
    IUri.GetDomain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(10, 'GetDomain', ((1, 'pbstrDomain'),)))
    IUri.GetExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(11, 'GetExtension', ((1, 'pbstrExtension'),)))
    IUri.GetFragment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(12, 'GetFragment', ((1, 'pbstrFragment'),)))
    IUri.GetHost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(13, 'GetHost', ((1, 'pbstrHost'),)))
    IUri.GetPassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(14, 'GetPassword', ((1, 'pbstrPassword'),)))
    IUri.GetPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(15, 'GetPath', ((1, 'pbstrPath'),)))
    IUri.GetPathAndQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(16, 'GetPathAndQuery', ((1, 'pbstrPathAndQuery'),)))
    IUri.GetQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(17, 'GetQuery', ((1, 'pbstrQuery'),)))
    IUri.GetRawUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(18, 'GetRawUri', ((1, 'pbstrRawUri'),)))
    IUri.GetSchemeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(19, 'GetSchemeName', ((1, 'pbstrSchemeName'),)))
    IUri.GetUserInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(20, 'GetUserInfo', ((1, 'pbstrUserInfo'),)))
    IUri.GetUserName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(21, 'GetUserName', ((1, 'pbstrUserName'),)))
    IUri.GetHostType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(22, 'GetHostType', ((1, 'pdwHostType'),)))
    IUri.GetPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(23, 'GetPort', ((1, 'pdwPort'),)))
    IUri.GetScheme = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(24, 'GetScheme', ((1, 'pdwScheme'),)))
    IUri.GetZone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(25, 'GetZone', ((1, 'pdwZone'),)))
    IUri.GetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(26, 'GetProperties', ((1, 'pdwFlags'),)))
    IUri.IsEqual = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUri_head,POINTER(win32more.Foundation.BOOL))(27, 'IsEqual', ((1, 'pUri'),(1, 'pfEqual'),)))
    win32more.System.Com.IUnknown
    return IUri
def _define_IUriBuilder_head():
    class IUriBuilder(win32more.System.Com.IUnknown_head):
        Guid = Guid('4221b2e1-8955-46c0-bd-5b-de-98-97-56-5d-e7')
    return IUriBuilder
def _define_IUriBuilder():
    IUriBuilder = win32more.System.Com.IUriBuilder_head
    IUriBuilder.CreateUriSimple = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UIntPtr,POINTER(win32more.System.Com.IUri_head))(3, 'CreateUriSimple', ((1, 'dwAllowEncodingPropertyMask'),(1, 'dwReserved'),(1, 'ppIUri'),)))
    IUriBuilder.CreateUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UIntPtr,POINTER(win32more.System.Com.IUri_head))(4, 'CreateUri', ((1, 'dwCreateFlags'),(1, 'dwAllowEncodingPropertyMask'),(1, 'dwReserved'),(1, 'ppIUri'),)))
    IUriBuilder.CreateUriWithFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,UIntPtr,POINTER(win32more.System.Com.IUri_head))(5, 'CreateUriWithFlags', ((1, 'dwCreateFlags'),(1, 'dwUriBuilderFlags'),(1, 'dwAllowEncodingPropertyMask'),(1, 'dwReserved'),(1, 'ppIUri'),)))
    IUriBuilder.GetIUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUri_head))(6, 'GetIUri', ((1, 'ppIUri'),)))
    IUriBuilder.SetIUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUri_head)(7, 'SetIUri', ((1, 'pIUri'),)))
    IUriBuilder.GetFragment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Foundation.PWSTR))(8, 'GetFragment', ((1, 'pcchFragment'),(1, 'ppwzFragment'),)))
    IUriBuilder.GetHost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Foundation.PWSTR))(9, 'GetHost', ((1, 'pcchHost'),(1, 'ppwzHost'),)))
    IUriBuilder.GetPassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Foundation.PWSTR))(10, 'GetPassword', ((1, 'pcchPassword'),(1, 'ppwzPassword'),)))
    IUriBuilder.GetPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Foundation.PWSTR))(11, 'GetPath', ((1, 'pcchPath'),(1, 'ppwzPath'),)))
    IUriBuilder.GetPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(UInt32))(12, 'GetPort', ((1, 'pfHasPort'),(1, 'pdwPort'),)))
    IUriBuilder.GetQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Foundation.PWSTR))(13, 'GetQuery', ((1, 'pcchQuery'),(1, 'ppwzQuery'),)))
    IUriBuilder.GetSchemeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Foundation.PWSTR))(14, 'GetSchemeName', ((1, 'pcchSchemeName'),(1, 'ppwzSchemeName'),)))
    IUriBuilder.GetUserName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Foundation.PWSTR))(15, 'GetUserName', ((1, 'pcchUserName'),(1, 'ppwzUserName'),)))
    IUriBuilder.SetFragment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(16, 'SetFragment', ((1, 'pwzNewValue'),)))
    IUriBuilder.SetHost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(17, 'SetHost', ((1, 'pwzNewValue'),)))
    IUriBuilder.SetPassword = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(18, 'SetPassword', ((1, 'pwzNewValue'),)))
    IUriBuilder.SetPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(19, 'SetPath', ((1, 'pwzNewValue'),)))
    IUriBuilder.SetPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,UInt32)(20, 'SetPort', ((1, 'fHasPort'),(1, 'dwNewValue'),)))
    IUriBuilder.SetQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(21, 'SetQuery', ((1, 'pwzNewValue'),)))
    IUriBuilder.SetSchemeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(22, 'SetSchemeName', ((1, 'pwzNewValue'),)))
    IUriBuilder.SetUserName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(23, 'SetUserName', ((1, 'pwzNewValue'),)))
    IUriBuilder.RemoveProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(24, 'RemoveProperties', ((1, 'dwPropertyMask'),)))
    IUriBuilder.HasBeenModified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(25, 'HasBeenModified', ((1, 'pfModified'),)))
    win32more.System.Com.IUnknown
    return IUriBuilder
def _define_IUrlMon_head():
    class IUrlMon(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000026-0000-0000-c0-00-00-00-00-00-00-46')
    return IUrlMon
def _define_IUrlMon():
    IUrlMon = win32more.System.Com.IUrlMon_head
    IUrlMon.AsyncGetClassBits = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.System.Com.IBindCtx_head,UInt32,POINTER(Guid),UInt32)(3, 'AsyncGetClassBits', ((1, 'rclsid'),(1, 'pszTYPE'),(1, 'pszExt'),(1, 'dwFileVersionMS'),(1, 'dwFileVersionLS'),(1, 'pszCodeBase'),(1, 'pbc'),(1, 'dwClassContext'),(1, 'riid'),(1, 'flags'),)))
    win32more.System.Com.IUnknown
    return IUrlMon
def _define_IWaitMultiple_head():
    class IWaitMultiple(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000002b-0000-0000-c0-00-00-00-00-00-00-46')
    return IWaitMultiple
def _define_IWaitMultiple():
    IWaitMultiple = win32more.System.Com.IWaitMultiple_head
    IWaitMultiple.WaitMultiple = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.ISynchronize_head))(3, 'WaitMultiple', ((1, 'timeout'),(1, 'pSync'),)))
    IWaitMultiple.AddSynchronize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.ISynchronize_head)(4, 'AddSynchronize', ((1, 'pSync'),)))
    win32more.System.Com.IUnknown
    return IWaitMultiple
LOCKTYPE = Int32
LOCK_WRITE = 1
LOCK_EXCLUSIVE = 2
LOCK_ONLYONCE = 4
def _define_LPEXCEPFINO_DEFERRED_FILLIN():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.EXCEPINFO_head))
def _define_LPFNCANUNLOADNOW():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,)
def _define_LPFNGETCLASSOBJECT():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(c_void_p))
def _define_MachineGlobalObjectTableRegistrationToken___head():
    class MachineGlobalObjectTableRegistrationToken__(Structure):
        pass
    return MachineGlobalObjectTableRegistrationToken__
def _define_MachineGlobalObjectTableRegistrationToken__():
    MachineGlobalObjectTableRegistrationToken__ = win32more.System.Com.MachineGlobalObjectTableRegistrationToken___head
    MachineGlobalObjectTableRegistrationToken__._fields_ = [
        ('unused', Int32),
    ]
    return MachineGlobalObjectTableRegistrationToken__
MEMCTX = Int32
MEMCTX_TASK = 1
MEMCTX_SHARED = 2
MEMCTX_MACSYSTEM = 3
MEMCTX_UNKNOWN = -1
MEMCTX_SAME = -2
MKRREDUCE = Int32
MKRREDUCE_ONE = 196608
MKRREDUCE_TOUSER = 131072
MKRREDUCE_THROUGHUSER = 65536
MKRREDUCE_ALL = 0
MKSYS = Int32
MKSYS_NONE = 0
MKSYS_GENERICCOMPOSITE = 1
MKSYS_FILEMONIKER = 2
MKSYS_ANTIMONIKER = 3
MKSYS_ITEMMONIKER = 4
MKSYS_POINTERMONIKER = 5
MKSYS_CLASSMONIKER = 7
MKSYS_OBJREFMONIKER = 8
MKSYS_SESSIONMONIKER = 9
MKSYS_LUAMONIKER = 10
MSHCTX = Int32
MSHCTX_LOCAL = 0
MSHCTX_NOSHAREDMEM = 1
MSHCTX_DIFFERENTMACHINE = 2
MSHCTX_INPROC = 3
MSHCTX_CROSSCTX = 4
MSHCTX_CONTAINER = 5
MSHLFLAGS = Int32
MSHLFLAGS_NORMAL = 0
MSHLFLAGS_TABLESTRONG = 1
MSHLFLAGS_TABLEWEAK = 2
MSHLFLAGS_NOPING = 4
MSHLFLAGS_RESERVED1 = 8
MSHLFLAGS_RESERVED2 = 16
MSHLFLAGS_RESERVED3 = 32
MSHLFLAGS_RESERVED4 = 64
def _define_MULTI_QI_head():
    class MULTI_QI(Structure):
        pass
    return MULTI_QI
def _define_MULTI_QI():
    MULTI_QI = win32more.System.Com.MULTI_QI_head
    MULTI_QI._fields_ = [
        ('pIID', POINTER(Guid)),
        ('pItf', win32more.System.Com.IUnknown_head),
        ('hr', win32more.Foundation.HRESULT),
    ]
    return MULTI_QI
PENDINGMSG = Int32
PENDINGMSG_CANCELCALL = 0
PENDINGMSG_WAITNOPROCESS = 1
PENDINGMSG_WAITDEFPROCESS = 2
PENDINGTYPE = Int32
PENDINGTYPE_TOPLEVEL = 1
PENDINGTYPE_NESTED = 2
def _define_PFNCONTEXTCALL():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.ComCallData_head))
def _define_QUERYCONTEXT_head():
    class QUERYCONTEXT(Structure):
        pass
    return QUERYCONTEXT
def _define_QUERYCONTEXT():
    QUERYCONTEXT = win32more.System.Com.QUERYCONTEXT_head
    QUERYCONTEXT._fields_ = [
        ('dwContext', UInt32),
        ('Platform', win32more.System.Com.CSPLATFORM),
        ('Locale', UInt32),
        ('dwVersionHi', UInt32),
        ('dwVersionLo', UInt32),
    ]
    return QUERYCONTEXT
REGCLS = Int32
REGCLS_SINGLEUSE = 0
REGCLS_MULTIPLEUSE = 1
REGCLS_MULTI_SEPARATE = 2
REGCLS_SUSPENDED = 4
REGCLS_SURROGATE = 8
REGCLS_AGILE = 16
def _define_RemSTGMEDIUM_head():
    class RemSTGMEDIUM(Structure):
        pass
    return RemSTGMEDIUM
def _define_RemSTGMEDIUM():
    RemSTGMEDIUM = win32more.System.Com.RemSTGMEDIUM_head
    RemSTGMEDIUM._fields_ = [
        ('tymed', win32more.System.Com.TYMED),
        ('dwHandleType', UInt32),
        ('pData', UInt32),
        ('pUnkForRelease', UInt32),
        ('cbData', UInt32),
        ('data', Byte * 1),
    ]
    return RemSTGMEDIUM
ROT_FLAGS = UInt32
ROTFLAGS_REGISTRATIONKEEPSALIVE = 1
ROTFLAGS_ALLOWANYCLIENT = 2
RPC_C_AUTHN_LEVEL = UInt32
RPC_C_AUTHN_LEVEL_DEFAULT = 0
RPC_C_AUTHN_LEVEL_NONE = 1
RPC_C_AUTHN_LEVEL_CONNECT = 2
RPC_C_AUTHN_LEVEL_CALL = 3
RPC_C_AUTHN_LEVEL_PKT = 4
RPC_C_AUTHN_LEVEL_PKT_INTEGRITY = 5
RPC_C_AUTHN_LEVEL_PKT_PRIVACY = 6
RPC_C_IMP_LEVEL = UInt32
RPC_C_IMP_LEVEL_DEFAULT = 0
RPC_C_IMP_LEVEL_ANONYMOUS = 1
RPC_C_IMP_LEVEL_IDENTIFY = 2
RPC_C_IMP_LEVEL_IMPERSONATE = 3
RPC_C_IMP_LEVEL_DELEGATE = 4
def _define_RPCOLEMESSAGE_head():
    class RPCOLEMESSAGE(Structure):
        pass
    return RPCOLEMESSAGE
def _define_RPCOLEMESSAGE():
    RPCOLEMESSAGE = win32more.System.Com.RPCOLEMESSAGE_head
    RPCOLEMESSAGE._fields_ = [
        ('reserved1', c_void_p),
        ('dataRepresentation', UInt32),
        ('Buffer', c_void_p),
        ('cbBuffer', UInt32),
        ('iMethod', UInt32),
        ('reserved2', c_void_p * 5),
        ('rpcFlags', UInt32),
    ]
    return RPCOLEMESSAGE
RPCOPT_PROPERTIES = Int32
COMBND_RPCTIMEOUT = 1
COMBND_SERVER_LOCALITY = 2
COMBND_RESERVED1 = 4
COMBND_RESERVED2 = 5
COMBND_RESERVED3 = 8
COMBND_RESERVED4 = 16
RPCOPT_SERVER_LOCALITY_VALUES = Int32
SERVER_LOCALITY_PROCESS_LOCAL = 0
SERVER_LOCALITY_MACHINE_LOCAL = 1
SERVER_LOCALITY_REMOTE = 2
def _define_SAFEARRAY_head():
    class SAFEARRAY(Structure):
        pass
    return SAFEARRAY
def _define_SAFEARRAY():
    SAFEARRAY = win32more.System.Com.SAFEARRAY_head
    SAFEARRAY._fields_ = [
        ('cDims', UInt16),
        ('fFeatures', win32more.System.Com.ADVANCED_FEATURE_FLAGS),
        ('cbElements', UInt32),
        ('cLocks', UInt32),
        ('pvData', c_void_p),
        ('rgsabound', win32more.System.Com.SAFEARRAYBOUND * 1),
    ]
    return SAFEARRAY
def _define_SAFEARRAYBOUND_head():
    class SAFEARRAYBOUND(Structure):
        pass
    return SAFEARRAYBOUND
def _define_SAFEARRAYBOUND():
    SAFEARRAYBOUND = win32more.System.Com.SAFEARRAYBOUND_head
    SAFEARRAYBOUND._fields_ = [
        ('cElements', UInt32),
        ('lLbound', Int32),
    ]
    return SAFEARRAYBOUND
def _define_SChannelHookCallInfo_head():
    class SChannelHookCallInfo(Structure):
        pass
    return SChannelHookCallInfo
def _define_SChannelHookCallInfo():
    SChannelHookCallInfo = win32more.System.Com.SChannelHookCallInfo_head
    SChannelHookCallInfo._fields_ = [
        ('iid', Guid),
        ('cbSize', UInt32),
        ('uCausality', Guid),
        ('dwServerPid', UInt32),
        ('iMethod', UInt32),
        ('pObject', c_void_p),
    ]
    return SChannelHookCallInfo
SERVERCALL = Int32
SERVERCALL_ISHANDLED = 0
SERVERCALL_REJECTED = 1
SERVERCALL_RETRYLATER = 2
ShutdownType = Int32
ShutdownType_IdleShutdown = 0
ShutdownType_ForcedShutdown = 1
def _define_SOLE_AUTHENTICATION_INFO_head():
    class SOLE_AUTHENTICATION_INFO(Structure):
        pass
    return SOLE_AUTHENTICATION_INFO
def _define_SOLE_AUTHENTICATION_INFO():
    SOLE_AUTHENTICATION_INFO = win32more.System.Com.SOLE_AUTHENTICATION_INFO_head
    SOLE_AUTHENTICATION_INFO._fields_ = [
        ('dwAuthnSvc', UInt32),
        ('dwAuthzSvc', UInt32),
        ('pAuthInfo', c_void_p),
    ]
    return SOLE_AUTHENTICATION_INFO
def _define_SOLE_AUTHENTICATION_LIST_head():
    class SOLE_AUTHENTICATION_LIST(Structure):
        pass
    return SOLE_AUTHENTICATION_LIST
def _define_SOLE_AUTHENTICATION_LIST():
    SOLE_AUTHENTICATION_LIST = win32more.System.Com.SOLE_AUTHENTICATION_LIST_head
    SOLE_AUTHENTICATION_LIST._fields_ = [
        ('cAuthInfo', UInt32),
        ('aAuthInfo', POINTER(win32more.System.Com.SOLE_AUTHENTICATION_INFO_head)),
    ]
    return SOLE_AUTHENTICATION_LIST
def _define_SOLE_AUTHENTICATION_SERVICE_head():
    class SOLE_AUTHENTICATION_SERVICE(Structure):
        pass
    return SOLE_AUTHENTICATION_SERVICE
def _define_SOLE_AUTHENTICATION_SERVICE():
    SOLE_AUTHENTICATION_SERVICE = win32more.System.Com.SOLE_AUTHENTICATION_SERVICE_head
    SOLE_AUTHENTICATION_SERVICE._fields_ = [
        ('dwAuthnSvc', UInt32),
        ('dwAuthzSvc', UInt32),
        ('pPrincipalName', win32more.Foundation.PWSTR),
        ('hr', win32more.Foundation.HRESULT),
    ]
    return SOLE_AUTHENTICATION_SERVICE
def _define_STATDATA_head():
    class STATDATA(Structure):
        pass
    return STATDATA
def _define_STATDATA():
    STATDATA = win32more.System.Com.STATDATA_head
    STATDATA._fields_ = [
        ('formatetc', win32more.System.Com.FORMATETC),
        ('advf', UInt32),
        ('pAdvSink', win32more.System.Com.IAdviseSink_head),
        ('dwConnection', UInt32),
    ]
    return STATDATA
STATFLAG = Int32
STATFLAG_DEFAULT = 0
STATFLAG_NONAME = 1
STATFLAG_NOOPEN = 2
def _define_STATSTG_head():
    class STATSTG(Structure):
        pass
    return STATSTG
def _define_STATSTG():
    STATSTG = win32more.System.Com.STATSTG_head
    STATSTG._fields_ = [
        ('pwcsName', win32more.Foundation.PWSTR),
        ('type', UInt32),
        ('cbSize', win32more.Foundation.ULARGE_INTEGER),
        ('mtime', win32more.Foundation.FILETIME),
        ('ctime', win32more.Foundation.FILETIME),
        ('atime', win32more.Foundation.FILETIME),
        ('grfMode', win32more.System.Com.STGM),
        ('grfLocksSupported', win32more.System.Com.LOCKTYPE),
        ('clsid', Guid),
        ('grfStateBits', UInt32),
        ('reserved', UInt32),
    ]
    return STATSTG
STGC = UInt32
STGC_DEFAULT = 0
STGC_OVERWRITE = 1
STGC_ONLYIFCURRENT = 2
STGC_DANGEROUSLYCOMMITMERELYTODISKCACHE = 4
STGC_CONSOLIDATE = 8
STGM = UInt32
STGM_DIRECT = 0
STGM_TRANSACTED = 65536
STGM_SIMPLE = 134217728
STGM_READ = 0
STGM_WRITE = 1
STGM_READWRITE = 2
STGM_SHARE_DENY_NONE = 64
STGM_SHARE_DENY_READ = 48
STGM_SHARE_DENY_WRITE = 32
STGM_SHARE_EXCLUSIVE = 16
STGM_PRIORITY = 262144
STGM_DELETEONRELEASE = 67108864
STGM_NOSCRATCH = 1048576
STGM_CREATE = 4096
STGM_CONVERT = 131072
STGM_FAILIFTHERE = 0
STGM_NOSNAPSHOT = 2097152
STGM_DIRECT_SWMR = 4194304
def _define_STGMEDIUM_head():
    class STGMEDIUM(Structure):
        pass
    return STGMEDIUM
def _define_STGMEDIUM():
    STGMEDIUM = win32more.System.Com.STGMEDIUM_head
    class STGMEDIUM__Anonymous_e__Union(Union):
        pass
    STGMEDIUM__Anonymous_e__Union._fields_ = [
        ('hBitmap', win32more.Graphics.Gdi.HBITMAP),
        ('hMetaFilePict', c_void_p),
        ('hEnhMetaFile', win32more.Graphics.Gdi.HENHMETAFILE),
        ('hGlobal', IntPtr),
        ('lpszFileName', win32more.Foundation.PWSTR),
        ('pstm', win32more.System.Com.IStream_head),
        ('pstg', win32more.System.Com.StructuredStorage.IStorage_head),
    ]
    STGMEDIUM._anonymous_ = [
        'Anonymous',
    ]
    STGMEDIUM._fields_ = [
        ('tymed', win32more.System.Com.TYMED),
        ('Anonymous', STGMEDIUM__Anonymous_e__Union),
        ('pUnkForRelease', win32more.System.Com.IUnknown_head),
    ]
    return STGMEDIUM
STGTY = Int32
STGTY_STORAGE = 1
STGTY_STREAM = 2
STGTY_LOCKBYTES = 3
STGTY_PROPERTY = 4
def _define_StorageLayout_head():
    class StorageLayout(Structure):
        pass
    return StorageLayout
def _define_StorageLayout():
    StorageLayout = win32more.System.Com.StorageLayout_head
    StorageLayout._fields_ = [
        ('LayoutType', UInt32),
        ('pwcsElementName', win32more.Foundation.PWSTR),
        ('cOffset', win32more.Foundation.LARGE_INTEGER),
        ('cBytes', win32more.Foundation.LARGE_INTEGER),
    ]
    return StorageLayout
STREAM_SEEK = UInt32
STREAM_SEEK_SET = 0
STREAM_SEEK_CUR = 1
STREAM_SEEK_END = 2
SYSKIND = Int32
SYS_WIN16 = 0
SYS_WIN32 = 1
SYS_MAC = 2
SYS_WIN64 = 3
THDTYPE = Int32
THDTYPE_BLOCKMESSAGES = 0
THDTYPE_PROCESSMESSAGES = 1
def _define_TLIBATTR_head():
    class TLIBATTR(Structure):
        pass
    return TLIBATTR
def _define_TLIBATTR():
    TLIBATTR = win32more.System.Com.TLIBATTR_head
    TLIBATTR._fields_ = [
        ('guid', Guid),
        ('lcid', UInt32),
        ('syskind', win32more.System.Com.SYSKIND),
        ('wMajorVerNum', UInt16),
        ('wMinorVerNum', UInt16),
        ('wLibFlags', UInt16),
    ]
    return TLIBATTR
TYMED = Int32
TYMED_HGLOBAL = 1
TYMED_FILE = 2
TYMED_ISTREAM = 4
TYMED_ISTORAGE = 8
TYMED_GDI = 16
TYMED_MFPICT = 32
TYMED_ENHMF = 64
TYMED_NULL = 0
def _define_TYPEATTR_head():
    class TYPEATTR(Structure):
        pass
    return TYPEATTR
def _define_TYPEATTR():
    TYPEATTR = win32more.System.Com.TYPEATTR_head
    TYPEATTR._fields_ = [
        ('guid', Guid),
        ('lcid', UInt32),
        ('dwReserved', UInt32),
        ('memidConstructor', Int32),
        ('memidDestructor', Int32),
        ('lpstrSchema', win32more.Foundation.PWSTR),
        ('cbSizeInstance', UInt32),
        ('typekind', win32more.System.Com.TYPEKIND),
        ('cFuncs', UInt16),
        ('cVars', UInt16),
        ('cImplTypes', UInt16),
        ('cbSizeVft', UInt16),
        ('cbAlignment', UInt16),
        ('wTypeFlags', UInt16),
        ('wMajorVerNum', UInt16),
        ('wMinorVerNum', UInt16),
        ('tdescAlias', win32more.System.Com.TYPEDESC),
        ('idldescType', win32more.System.Com.IDLDESC),
    ]
    return TYPEATTR
def _define_TYPEDESC_head():
    class TYPEDESC(Structure):
        pass
    return TYPEDESC
def _define_TYPEDESC():
    TYPEDESC = win32more.System.Com.TYPEDESC_head
    class TYPEDESC__Anonymous_e__Union(Union):
        pass
    TYPEDESC__Anonymous_e__Union._fields_ = [
        ('lptdesc', POINTER(win32more.System.Com.TYPEDESC_head)),
        ('lpadesc', POINTER(win32more.System.Ole.ARRAYDESC_head)),
        ('hreftype', UInt32),
    ]
    TYPEDESC._anonymous_ = [
        'Anonymous',
    ]
    TYPEDESC._fields_ = [
        ('Anonymous', TYPEDESC__Anonymous_e__Union),
        ('vt', win32more.System.Com.VARENUM),
    ]
    return TYPEDESC
TYPEKIND = Int32
TKIND_ENUM = 0
TKIND_RECORD = 1
TKIND_MODULE = 2
TKIND_INTERFACE = 3
TKIND_DISPATCH = 4
TKIND_COCLASS = 5
TKIND_ALIAS = 6
TKIND_UNION = 7
TKIND_MAX = 8
TYSPEC = Int32
TYSPEC_CLSID = 0
TYSPEC_FILEEXT = 1
TYSPEC_MIMETYPE = 2
TYSPEC_FILENAME = 3
TYSPEC_PROGID = 4
TYSPEC_PACKAGENAME = 5
TYSPEC_OBJECTID = 6
def _define_uCLSSPEC_head():
    class uCLSSPEC(Structure):
        pass
    return uCLSSPEC
def _define_uCLSSPEC():
    uCLSSPEC = win32more.System.Com.uCLSSPEC_head
    class uCLSSPEC__tagged_union_e__Struct(Union):
        pass
    class uCLSSPEC__tagged_union_e__Struct__ByName_e__Struct(Structure):
        pass
    uCLSSPEC__tagged_union_e__Struct__ByName_e__Struct._fields_ = [
        ('pPackageName', win32more.Foundation.PWSTR),
        ('PolicyId', Guid),
    ]
    class uCLSSPEC__tagged_union_e__Struct__ByObjectId_e__Struct(Structure):
        pass
    uCLSSPEC__tagged_union_e__Struct__ByObjectId_e__Struct._fields_ = [
        ('ObjectId', Guid),
        ('PolicyId', Guid),
    ]
    uCLSSPEC__tagged_union_e__Struct._fields_ = [
        ('clsid', Guid),
        ('pFileExt', win32more.Foundation.PWSTR),
        ('pMimeType', win32more.Foundation.PWSTR),
        ('pProgId', win32more.Foundation.PWSTR),
        ('pFileName', win32more.Foundation.PWSTR),
        ('ByName', uCLSSPEC__tagged_union_e__Struct__ByName_e__Struct),
        ('ByObjectId', uCLSSPEC__tagged_union_e__Struct__ByObjectId_e__Struct),
    ]
    uCLSSPEC._fields_ = [
        ('tyspec', UInt32),
        ('tagged_union', uCLSSPEC__tagged_union_e__Struct),
    ]
    return uCLSSPEC
URI_CREATE_FLAGS = UInt32
Uri_CREATE_ALLOW_RELATIVE = 1
Uri_CREATE_ALLOW_IMPLICIT_WILDCARD_SCHEME = 2
Uri_CREATE_ALLOW_IMPLICIT_FILE_SCHEME = 4
Uri_CREATE_NOFRAG = 8
Uri_CREATE_NO_CANONICALIZE = 16
Uri_CREATE_CANONICALIZE = 256
Uri_CREATE_FILE_USE_DOS_PATH = 32
Uri_CREATE_DECODE_EXTRA_INFO = 64
Uri_CREATE_NO_DECODE_EXTRA_INFO = 128
Uri_CREATE_CRACK_UNKNOWN_SCHEMES = 512
Uri_CREATE_NO_CRACK_UNKNOWN_SCHEMES = 1024
Uri_CREATE_PRE_PROCESS_HTML_URI = 2048
Uri_CREATE_NO_PRE_PROCESS_HTML_URI = 4096
Uri_CREATE_IE_SETTINGS = 8192
Uri_CREATE_NO_IE_SETTINGS = 16384
Uri_CREATE_NO_ENCODE_FORBIDDEN_CHARACTERS = 32768
Uri_CREATE_NORMALIZE_INTL_CHARACTERS = 65536
Uri_CREATE_CANONICALIZE_ABSOLUTE = 131072
Uri_PROPERTY = Int32
Uri_PROPERTY_ABSOLUTE_URI = 0
Uri_PROPERTY_STRING_START = 0
Uri_PROPERTY_AUTHORITY = 1
Uri_PROPERTY_DISPLAY_URI = 2
Uri_PROPERTY_DOMAIN = 3
Uri_PROPERTY_EXTENSION = 4
Uri_PROPERTY_FRAGMENT = 5
Uri_PROPERTY_HOST = 6
Uri_PROPERTY_PASSWORD = 7
Uri_PROPERTY_PATH = 8
Uri_PROPERTY_PATH_AND_QUERY = 9
Uri_PROPERTY_QUERY = 10
Uri_PROPERTY_RAW_URI = 11
Uri_PROPERTY_SCHEME_NAME = 12
Uri_PROPERTY_USER_INFO = 13
Uri_PROPERTY_USER_NAME = 14
Uri_PROPERTY_STRING_LAST = 14
Uri_PROPERTY_HOST_TYPE = 15
Uri_PROPERTY_DWORD_START = 15
Uri_PROPERTY_PORT = 16
Uri_PROPERTY_SCHEME = 17
Uri_PROPERTY_ZONE = 18
Uri_PROPERTY_DWORD_LAST = 18
def _define_userFLAG_STGMEDIUM_head():
    class userFLAG_STGMEDIUM(Structure):
        pass
    return userFLAG_STGMEDIUM
def _define_userFLAG_STGMEDIUM():
    userFLAG_STGMEDIUM = win32more.System.Com.userFLAG_STGMEDIUM_head
    userFLAG_STGMEDIUM._fields_ = [
        ('ContextFlags', Int32),
        ('fPassOwnership', Int32),
        ('Stgmed', win32more.System.Com.userSTGMEDIUM),
    ]
    return userFLAG_STGMEDIUM
def _define_userSTGMEDIUM_head():
    class userSTGMEDIUM(Structure):
        pass
    return userSTGMEDIUM
def _define_userSTGMEDIUM():
    userSTGMEDIUM = win32more.System.Com.userSTGMEDIUM_head
    class userSTGMEDIUM__STGMEDIUM_UNION(Structure):
        pass
    class userSTGMEDIUM__STGMEDIUM_UNION__u_e__Struct(Union):
        pass
    userSTGMEDIUM__STGMEDIUM_UNION__u_e__Struct._fields_ = [
        ('hMetaFilePict', POINTER(win32more.System.SystemServices.userHMETAFILEPICT_head)),
        ('hHEnhMetaFile', POINTER(win32more.System.SystemServices.userHENHMETAFILE_head)),
        ('hGdiHandle', POINTER(win32more.System.Com.GDI_OBJECT_head)),
        ('hGlobal', POINTER(win32more.System.SystemServices.userHGLOBAL_head)),
        ('lpszFileName', win32more.Foundation.PWSTR),
        ('pstm', POINTER(win32more.System.Com.BYTE_BLOB_head)),
        ('pstg', POINTER(win32more.System.Com.BYTE_BLOB_head)),
    ]
    userSTGMEDIUM__STGMEDIUM_UNION._fields_ = [
        ('tymed', UInt32),
        ('u', userSTGMEDIUM__STGMEDIUM_UNION__u_e__Struct),
    ]
    userSTGMEDIUM._fields_ = [
        ('pUnkForRelease', win32more.System.Com.IUnknown_head),
    ]
    return userSTGMEDIUM
def _define_VARDESC_head():
    class VARDESC(Structure):
        pass
    return VARDESC
def _define_VARDESC():
    VARDESC = win32more.System.Com.VARDESC_head
    class VARDESC__Anonymous_e__Union(Union):
        pass
    VARDESC__Anonymous_e__Union._fields_ = [
        ('oInst', UInt32),
        ('lpvarValue', POINTER(win32more.System.Com.VARIANT_head)),
    ]
    VARDESC._anonymous_ = [
        'Anonymous',
    ]
    VARDESC._fields_ = [
        ('memid', Int32),
        ('lpstrSchema', win32more.Foundation.PWSTR),
        ('Anonymous', VARDESC__Anonymous_e__Union),
        ('elemdescVar', win32more.System.Com.ELEMDESC),
        ('wVarFlags', win32more.System.Com.VARFLAGS),
        ('varkind', win32more.System.Com.VARKIND),
    ]
    return VARDESC
VARENUM = UInt16
VT_EMPTY = 0
VT_NULL = 1
VT_I2 = 2
VT_I4 = 3
VT_R4 = 4
VT_R8 = 5
VT_CY = 6
VT_DATE = 7
VT_BSTR = 8
VT_DISPATCH = 9
VT_ERROR = 10
VT_BOOL = 11
VT_VARIANT = 12
VT_UNKNOWN = 13
VT_DECIMAL = 14
VT_I1 = 16
VT_UI1 = 17
VT_UI2 = 18
VT_UI4 = 19
VT_I8 = 20
VT_UI8 = 21
VT_INT = 22
VT_UINT = 23
VT_VOID = 24
VT_HRESULT = 25
VT_PTR = 26
VT_SAFEARRAY = 27
VT_CARRAY = 28
VT_USERDEFINED = 29
VT_LPSTR = 30
VT_LPWSTR = 31
VT_RECORD = 36
VT_INT_PTR = 37
VT_UINT_PTR = 38
VT_FILETIME = 64
VT_BLOB = 65
VT_STREAM = 66
VT_STORAGE = 67
VT_STREAMED_OBJECT = 68
VT_STORED_OBJECT = 69
VT_BLOB_OBJECT = 70
VT_CF = 71
VT_CLSID = 72
VT_VERSIONED_STREAM = 73
VT_BSTR_BLOB = 4095
VT_VECTOR = 4096
VT_ARRAY = 8192
VT_BYREF = 16384
VT_RESERVED = 32768
VT_ILLEGAL = 65535
VT_ILLEGALMASKED = 4095
VT_TYPEMASK = 4095
VARFLAGS = UInt16
VARFLAG_FREADONLY = 1
VARFLAG_FSOURCE = 2
VARFLAG_FBINDABLE = 4
VARFLAG_FREQUESTEDIT = 8
VARFLAG_FDISPLAYBIND = 16
VARFLAG_FDEFAULTBIND = 32
VARFLAG_FHIDDEN = 64
VARFLAG_FRESTRICTED = 128
VARFLAG_FDEFAULTCOLLELEM = 256
VARFLAG_FUIDEFAULT = 512
VARFLAG_FNONBROWSABLE = 1024
VARFLAG_FREPLACEABLE = 2048
VARFLAG_FIMMEDIATEBIND = 4096
def _define_VARIANT_head():
    class VARIANT(Structure):
        pass
    return VARIANT
def _define_VARIANT():
    VARIANT = win32more.System.Com.VARIANT_head
    class VARIANT__Anonymous_e__Union(Union):
        pass
    class VARIANT__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    class VARIANT__Anonymous_e__Union__Anonymous_e__Struct__Anonymous_e__Union(Union):
        pass
    class VARIANT__Anonymous_e__Union__Anonymous_e__Struct__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    VARIANT__Anonymous_e__Union__Anonymous_e__Struct__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('pvRecord', c_void_p),
        ('pRecInfo', win32more.System.Ole.IRecordInfo_head),
    ]
    VARIANT__Anonymous_e__Union__Anonymous_e__Struct__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    VARIANT__Anonymous_e__Union__Anonymous_e__Struct__Anonymous_e__Union._fields_ = [
        ('llVal', Int64),
        ('lVal', Int32),
        ('bVal', Byte),
        ('iVal', Int16),
        ('fltVal', Single),
        ('dblVal', Double),
        ('boolVal', win32more.Foundation.VARIANT_BOOL),
        ('__OBSOLETE__VARIANT_BOOL', win32more.Foundation.VARIANT_BOOL),
        ('scode', Int32),
        ('cyVal', win32more.System.Com.CY),
        ('date', Double),
        ('bstrVal', win32more.Foundation.BSTR),
        ('punkVal', win32more.System.Com.IUnknown_head),
        ('pdispVal', win32more.System.Com.IDispatch_head),
        ('parray', POINTER(win32more.System.Com.SAFEARRAY_head)),
        ('pbVal', c_char_p_no),
        ('piVal', POINTER(Int16)),
        ('plVal', POINTER(Int32)),
        ('pllVal', POINTER(Int64)),
        ('pfltVal', POINTER(Single)),
        ('pdblVal', POINTER(Double)),
        ('pboolVal', POINTER(win32more.Foundation.VARIANT_BOOL)),
        ('__OBSOLETE__VARIANT_PBOOL', POINTER(win32more.Foundation.VARIANT_BOOL)),
        ('pscode', POINTER(Int32)),
        ('pcyVal', POINTER(win32more.System.Com.CY_head)),
        ('pdate', POINTER(Double)),
        ('pbstrVal', POINTER(win32more.Foundation.BSTR)),
        ('ppunkVal', POINTER(win32more.System.Com.IUnknown_head)),
        ('ppdispVal', POINTER(win32more.System.Com.IDispatch_head)),
        ('pparray', POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))),
        ('pvarVal', POINTER(win32more.System.Com.VARIANT_head)),
        ('byref', c_void_p),
        ('cVal', win32more.Foundation.CHAR),
        ('uiVal', UInt16),
        ('ulVal', UInt32),
        ('ullVal', UInt64),
        ('intVal', Int32),
        ('uintVal', UInt32),
        ('pdecVal', POINTER(win32more.Foundation.DECIMAL_head)),
        ('pcVal', win32more.Foundation.PSTR),
        ('puiVal', POINTER(UInt16)),
        ('pulVal', POINTER(UInt32)),
        ('pullVal', POINTER(UInt64)),
        ('pintVal', POINTER(Int32)),
        ('puintVal', POINTER(UInt32)),
        ('Anonymous', VARIANT__Anonymous_e__Union__Anonymous_e__Struct__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    VARIANT__Anonymous_e__Union__Anonymous_e__Struct._anonymous_ = [
        'Anonymous',
    ]
    VARIANT__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('vt', win32more.System.Com.VARENUM),
        ('wReserved1', UInt16),
        ('wReserved2', UInt16),
        ('wReserved3', UInt16),
        ('Anonymous', VARIANT__Anonymous_e__Union__Anonymous_e__Struct__Anonymous_e__Union),
    ]
    VARIANT__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    VARIANT__Anonymous_e__Union._fields_ = [
        ('Anonymous', VARIANT__Anonymous_e__Union__Anonymous_e__Struct),
        ('decVal', win32more.Foundation.DECIMAL),
    ]
    VARIANT._anonymous_ = [
        'Anonymous',
    ]
    VARIANT._fields_ = [
        ('Anonymous', VARIANT__Anonymous_e__Union),
    ]
    return VARIANT
VARKIND = Int32
VAR_PERINSTANCE = 0
VAR_STATIC = 1
VAR_CONST = 2
VAR_DISPATCH = 3
def _define_WORD_BLOB_head():
    class WORD_BLOB(Structure):
        pass
    return WORD_BLOB
def _define_WORD_BLOB():
    WORD_BLOB = win32more.System.Com.WORD_BLOB_head
    WORD_BLOB._fields_ = [
        ('clSize', UInt32),
        ('asData', UInt16 * 1),
    ]
    return WORD_BLOB
def _define_WORD_SIZEDARR_head():
    class WORD_SIZEDARR(Structure):
        pass
    return WORD_SIZEDARR
def _define_WORD_SIZEDARR():
    WORD_SIZEDARR = win32more.System.Com.WORD_SIZEDARR_head
    WORD_SIZEDARR._fields_ = [
        ('clSize', UInt32),
        ('pData', POINTER(UInt16)),
    ]
    return WORD_SIZEDARR
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
