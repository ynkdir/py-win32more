from __future__ import annotations

from ctypes import (
    POINTER,
    c_wchar_p,
    cast,
    pointer,
)

from ._win32 import (
    WINFUNCTYPE,
    ComPtr,
    Guid,
    Int32,
    LazyLoader,
    SByte,
    String,
    UInt32,
    UIntPtr,
    Void,
    VoidPtr,
    commethod,
    winfunctype,
)


def MAKELANGID(p, s):
    return (s << 10) | p


def FormatError(code):
    lpMsgBuf = c_wchar_p()
    n = FormatMessageW(
        FORMAT_MESSAGE_ALLOCATE_BUFFER | FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_IGNORE_INSERTS,
        None,
        code,
        MAKELANGID(LANG_NEUTRAL, SUBLANG_NEUTRAL),
        cast(pointer(lpMsgBuf), c_wchar_p),
        0,
        None,
    )
    if n == 0:
        return "<no description>"
    msg = lpMsgBuf.value.rstrip()
    LocalFree(lpMsgBuf)
    return msg


# Windows.Win32.Foundation

BOOL = Int32
BSTR = String
HGLOBAL = VoidPtr
HLOCAL = VoidPtr
HRESULT = Int32
PWSTR = String
WIN32_ERROR = UInt32

S_OK = 0
E_FAIL = -2147467259
E_NOINTERFACE = -2147467262


@winfunctype("KERNEL32.dll")
def GetLastError() -> WIN32_ERROR: ...


@winfunctype("KERNEL32.dll")
def LocalFree(hMem: HLOCAL) -> HLOCAL: ...


@winfunctype("OLEAUT32.dll")
def SysAllocStringLen(strIn: PWSTR, ui: UInt32) -> BSTR: ...


@winfunctype("OLEAUT32.dll")
def SysFreeString(bstrString: BSTR) -> Void: ...


@winfunctype("OLEAUT32.dll")
def SysStringLen(pbstr: BSTR) -> UInt32: ...


# Windows.Win32.System.Com

CO_MTA_USAGE_COOKIE = VoidPtr


class IUnknown(ComPtr):
    _iid_ = Guid("{00000000-0000-0000-c000-000000000046}")

    @commethod(0)
    def QueryInterface(self, riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> HRESULT: ...
    @commethod(1)
    def AddRef(self) -> UInt32: ...
    @commethod(2)
    def Release(self) -> UInt32: ...


LazyLoader.add_predefined("win32more.Windows.Win32.System.Com", "IUnknown", IUnknown)


class IAgileObject(IUnknown):
    _iid_ = Guid("{94ea2b94-e9cc-49e0-c0ff-ee64ca8f5b90}")


class IErrorInfo(IUnknown):
    _iid_ = Guid("{1cf2b120-547d-101b-8e65-08002b2bd119}")

    @commethod(3)
    def GetGUID(self, pGUID: POINTER(Guid)) -> HRESULT: ...
    @commethod(4)
    def GetSource(self, pBstrSource: POINTER(BSTR)) -> HRESULT: ...
    @commethod(5)
    def GetDescription(self, pBstrDescription: POINTER(BSTR)) -> HRESULT: ...
    @commethod(6)
    def GetHelpFile(self, pBstrHelpFile: POINTER(BSTR)) -> HRESULT: ...
    @commethod(7)
    def GetHelpContext(self, pdwHelpContext: POINTER(UInt32)) -> HRESULT: ...


@winfunctype("OLE32.dll")
def CoIncrementMTAUsage(pCookie: POINTER(CO_MTA_USAGE_COOKIE)) -> HRESULT: ...


@winfunctype("OLE32.dll")
def CoTaskMemAlloc(cb: UIntPtr) -> VoidPtr: ...


@winfunctype("OLE32.dll")
def CoTaskMemFree(pv: VoidPtr) -> Void: ...


@winfunctype("OLEAUT32.dll")
def SetErrorInfo(dwReserved: UInt32, perrinfo: IErrorInfo) -> HRESULT: ...


@winfunctype("OLEAUT32.dll")
def GetErrorInfo(dwReserved: UInt32, pperrinfo: POINTER(IErrorInfo)) -> HRESULT: ...


# Windows.Win32.System.Ole


class ICreateErrorInfo(IUnknown):
    _iid_ = Guid("{22f03340-547d-101b-8e65-08002b2bd119}")

    @commethod(3)
    def SetGUID(self, rguid: POINTER(Guid)) -> HRESULT: ...
    @commethod(4)
    def SetSource(self, szSource: PWSTR) -> HRESULT: ...
    @commethod(5)
    def SetDescription(self, szDescription: PWSTR) -> HRESULT: ...
    @commethod(6)
    def SetHelpFile(self, szHelpFile: PWSTR) -> HRESULT: ...
    @commethod(7)
    def SetHelpContext(self, dwHelpContext: UInt32) -> HRESULT: ...


@winfunctype("OLEAUT32.dll")
def CreateErrorInfo(pperrinfo: POINTER(ICreateErrorInfo)) -> HRESULT: ...


# Windows.Win32.System.WinRT

BaseTrust = 0

TrustLevel = Int32
HSTRING = VoidPtr


class IInspectable(IUnknown):
    _iid_ = Guid("{af86e2e0-b12d-4c6a-9c5a-d7aa65101e90}")

    @commethod(3)
    def GetIids(self, iidCount: POINTER(UInt32), iids: POINTER(POINTER(Guid))) -> HRESULT: ...
    @commethod(4)
    def GetRuntimeClassName(self, className: POINTER(HSTRING)) -> HRESULT: ...
    @commethod(5)
    def GetTrustLevel(self, trustLevel: POINTER(TrustLevel)) -> HRESULT: ...


LazyLoader.add_predefined("win32more.Windows.Win32.System.WinRT", "IInspectable", IInspectable)


class IActivationFactory(IInspectable):
    _iid_ = Guid("{00000035-0000-0000-c000-000000000046}")

    @commethod(6)
    def ActivateInstance(self, instance: POINTER(IInspectable)) -> HRESULT: ...


class IRestrictedErrorInfo(IUnknown):
    _iid_ = Guid("{82ba7092-4c88-427d-a7bc-16dd93feb67e}")

    @commethod(3)
    def GetErrorDetails(
        self,
        description: POINTER(BSTR),
        error: POINTER(HRESULT),
        restrictedDescription: POINTER(BSTR),
        capabilitySid: POINTER(BSTR),
    ) -> HRESULT: ...
    @commethod(4)
    def GetReference(self, reference: POINTER(BSTR)) -> HRESULT: ...


PFNGETACTIVATIONFACTORY = WINFUNCTYPE(HRESULT, HSTRING, POINTER(IActivationFactory))


@winfunctype("api-ms-win-core-winrt-l1-1-0.dll")
def RoGetActivationFactory(activatableClassId: HSTRING, iid: POINTER(Guid), factory: POINTER(VoidPtr)) -> HRESULT: ...


@winfunctype("api-ms-win-core-winrt-error-l1-1-0.dll")
def RoOriginateError(error: HRESULT, message: HSTRING) -> BOOL: ...


@winfunctype("api-ms-win-core-winrt-string-l1-1-0.dll")
def WindowsCreateString(sourceString: PWSTR, length: UInt32, string: POINTER(HSTRING)) -> HRESULT: ...


@winfunctype("api-ms-win-core-winrt-string-l1-1-0.dll")
def WindowsDeleteString(string: HSTRING) -> HRESULT: ...


@winfunctype("api-ms-win-core-winrt-string-l1-1-0.dll")
def WindowsGetStringLen(string: HSTRING) -> UInt32: ...


@winfunctype("api-ms-win-core-winrt-string-l1-1-0.dll")
def WindowsGetStringRawBuffer(string: HSTRING, length: POINTER(UInt32)) -> PWSTR: ...


# Windows.Win32.System.Diagnostics.Debug

FORMAT_MESSAGE_OPTIONS = UInt32

FORMAT_MESSAGE_ALLOCATE_BUFFER = 256
FORMAT_MESSAGE_FROM_SYSTEM = 4096
FORMAT_MESSAGE_IGNORE_INSERTS = 512


@winfunctype("KERNEL32.dll")
def FormatMessageW(
    dwFlags: FORMAT_MESSAGE_OPTIONS,
    lpSource: VoidPtr,
    dwMessageId: UInt32,
    dwLanguageId: UInt32,
    lpBuffer: PWSTR,
    nSize: UInt32,
    Arguments: POINTER(POINTER(SByte)),
) -> UInt32: ...


# Windows.Win32.System.SystemServices

LANG_NEUTRAL = 0
SUBLANG_NEUTRAL = 0
