from __future__ import annotations

import uuid
from ctypes import (
    POINTER,
    Structure,
    c_wchar_p,
    cast,
    pointer,
)

from ._win32 import (
    WINFUNCTYPE,
    Byte,
    ComPtr,
    Int32,
    LazyLoader,
    SByte,
    String,
    UInt16,
    UInt32,
    UIntPtr,
    Void,
    VoidPtr,
    commethod,
    winfunctype,
)


class Guid(Structure):
    _fields_ = [
        ("Data1", UInt32),
        ("Data2", UInt16),
        ("Data3", UInt16),
        ("Data4", Byte * 8),
    ]

    def __init__(self, val=None):
        if val is None:
            pass
        elif isinstance(val, self.__class__):
            self.Data1 = val.Data1
            self.Data2 = val.Data2
            self.Data3 = val.Data3
            self.Data4 = val.Data4
        elif isinstance(val, str):
            u = uuid.UUID(val)
            self.Data1 = u.time_low
            self.Data2 = u.time_mid
            self.Data3 = u.time_hi_version
            for i in range(8):
                self.Data4[i] = u.bytes[8 + i]
        elif isinstance(val, uuid.UUID):
            u = val
            self.Data1 = u.time_low
            self.Data2 = u.time_mid
            self.Data3 = u.time_hi_version
            for i in range(8):
                self.Data4[i] = u.bytes[8 + i]
        else:
            raise ValueError()

    def __str__(self):
        return f"{{{self.Data1:08x}-{self.Data2:04x}-{self.Data3:04x}-{self.Data4[0]:02x}{self.Data4[1]:02x}-{self.Data4[2]:02x}{self.Data4[3]:02x}{self.Data4[4]:02x}{self.Data4[5]:02x}{self.Data4[6]:02x}{self.Data4[7]:02x}}}"

    def __eq__(self, other):
        if not isinstance(other, Guid):
            raise ValueError(f"cannot compare with {type(other)}")
        return (
            self.Data1 == other.Data1
            and self.Data2 == other.Data2
            and self.Data3 == other.Data3
            and self.Data4[0] == other.Data4[0]
            and self.Data4[1] == other.Data4[1]
            and self.Data4[2] == other.Data4[2]
            and self.Data4[3] == other.Data4[3]
            and self.Data4[4] == other.Data4[4]
            and self.Data4[5] == other.Data4[5]
            and self.Data4[6] == other.Data4[6]
            and self.Data4[7] == other.Data4[7]
        )


def SUCCEEDED(hr):
    return hr >= 0


def FAILED(hr):
    return hr < 0


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
def GlobalFree(hMem: HGLOBAL) -> HGLOBAL: ...


@winfunctype("KERNEL32.dll")
def LocalFree(hMem: HLOCAL) -> HLOCAL: ...


@winfunctype("OLEAUT32.dll")
def SysAllocString(psz: PWSTR) -> BSTR: ...


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
