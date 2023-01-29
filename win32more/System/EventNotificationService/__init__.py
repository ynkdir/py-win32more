from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.EventNotificationService
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
NETWORK_ALIVE_LAN: UInt32 = 1
NETWORK_ALIVE_WAN: UInt32 = 2
NETWORK_ALIVE_AOL: UInt32 = 4
NETWORK_ALIVE_INTERNET: UInt32 = 8
CONNECTION_AOL: UInt32 = 4
SENSGUID_PUBLISHER: Guid = Guid('5fee1bd6-5b9b-11d1-8d-d2-00-aa-00-4a-bd-5e')
SENSGUID_SUBSCRIBER_LCE: Guid = Guid('d3938ab0-5b9d-11d1-8d-d2-00-aa-00-4a-bd-5e')
SENSGUID_SUBSCRIBER_WININET: Guid = Guid('d3938ab5-5b9d-11d1-8d-d2-00-aa-00-4a-bd-5e')
SENSGUID_EVENTCLASS_NETWORK: Guid = Guid('d5978620-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
SENSGUID_EVENTCLASS_LOGON: Guid = Guid('d5978630-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
SENSGUID_EVENTCLASS_ONNOW: Guid = Guid('d5978640-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
SENSGUID_EVENTCLASS_LOGON2: Guid = Guid('d5978650-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
@winfunctype('SensApi.dll')
def IsDestinationReachableA(lpszDestination: win32more.Foundation.PSTR, lpQOCInfo: POINTER(win32more.System.EventNotificationService.QOCINFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('SensApi.dll')
def IsDestinationReachableW(lpszDestination: win32more.Foundation.PWSTR, lpQOCInfo: POINTER(win32more.System.EventNotificationService.QOCINFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('SensApi.dll')
def IsNetworkAlive(lpdwFlags: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
class ISensLogon(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d597bab3-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
    @commethod(7)
    def Logon(bstrUserName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Logoff(bstrUserName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def StartShell(bstrUserName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def DisplayLock(bstrUserName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def DisplayUnlock(bstrUserName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def StartScreenSaver(bstrUserName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def StopScreenSaver(bstrUserName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class ISensLogon2(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d597bab4-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
    @commethod(7)
    def Logon(bstrUserName: win32more.Foundation.BSTR, dwSessionId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Logoff(bstrUserName: win32more.Foundation.BSTR, dwSessionId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SessionDisconnect(bstrUserName: win32more.Foundation.BSTR, dwSessionId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SessionReconnect(bstrUserName: win32more.Foundation.BSTR, dwSessionId: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def PostShell(bstrUserName: win32more.Foundation.BSTR, dwSessionId: UInt32) -> win32more.Foundation.HRESULT: ...
class ISensNetwork(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d597bab1-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
    @commethod(7)
    def ConnectionMade(bstrConnection: win32more.Foundation.BSTR, ulType: UInt32, lpQOCInfo: POINTER(win32more.System.EventNotificationService.SENS_QOCINFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ConnectionMadeNoQOCInfo(bstrConnection: win32more.Foundation.BSTR, ulType: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def ConnectionLost(bstrConnection: win32more.Foundation.BSTR, ulType: win32more.System.EventNotificationService.SENS_CONNECTION_TYPE) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def DestinationReachable(bstrDestination: win32more.Foundation.BSTR, bstrConnection: win32more.Foundation.BSTR, ulType: UInt32, lpQOCInfo: POINTER(win32more.System.EventNotificationService.SENS_QOCINFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def DestinationReachableNoQOCInfo(bstrDestination: win32more.Foundation.BSTR, bstrConnection: win32more.Foundation.BSTR, ulType: UInt32) -> win32more.Foundation.HRESULT: ...
class ISensOnNow(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('d597bab2-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
    @commethod(7)
    def OnACPower() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def OnBatteryPower(dwBatteryLifePercent: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def BatteryLow(dwBatteryLifePercent: UInt32) -> win32more.Foundation.HRESULT: ...
class QOCINFO(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwInSpeed: UInt32
    dwOutSpeed: UInt32
SENS = Guid('d597cafe-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
SENS_CONNECTION_TYPE = UInt32
CONNECTION_LAN: SENS_CONNECTION_TYPE = 0
CONNECTION_WAN: SENS_CONNECTION_TYPE = 1
class SENS_QOCINFO(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwOutSpeed: UInt32
    dwInSpeed: UInt32
make_head(_module, 'ISensLogon')
make_head(_module, 'ISensLogon2')
make_head(_module, 'ISensNetwork')
make_head(_module, 'ISensOnNow')
make_head(_module, 'QOCINFO')
make_head(_module, 'SENS_QOCINFO')
__all__ = [
    "CONNECTION_AOL",
    "CONNECTION_LAN",
    "CONNECTION_WAN",
    "ISensLogon",
    "ISensLogon2",
    "ISensNetwork",
    "ISensOnNow",
    "IsDestinationReachableA",
    "IsDestinationReachableW",
    "IsNetworkAlive",
    "NETWORK_ALIVE_AOL",
    "NETWORK_ALIVE_INTERNET",
    "NETWORK_ALIVE_LAN",
    "NETWORK_ALIVE_WAN",
    "QOCINFO",
    "SENS",
    "SENSGUID_EVENTCLASS_LOGON",
    "SENSGUID_EVENTCLASS_LOGON2",
    "SENSGUID_EVENTCLASS_NETWORK",
    "SENSGUID_EVENTCLASS_ONNOW",
    "SENSGUID_PUBLISHER",
    "SENSGUID_SUBSCRIBER_LCE",
    "SENSGUID_SUBSCRIBER_WININET",
    "SENS_CONNECTION_TYPE",
    "SENS_QOCINFO",
]
_arch_optional = [
]
