from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.EventNotificationService
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
def IsDestinationReachableA(lpszDestination: Windows.Win32.Foundation.PSTR, lpQOCInfo: POINTER(Windows.Win32.System.EventNotificationService.QOCINFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SensApi.dll')
def IsDestinationReachableW(lpszDestination: Windows.Win32.Foundation.PWSTR, lpQOCInfo: POINTER(Windows.Win32.System.EventNotificationService.QOCINFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SensApi.dll')
def IsNetworkAlive(lpdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
class ISensLogon(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('d597bab3-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
    @commethod(7)
    def Logon(bstrUserName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Logoff(bstrUserName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def StartShell(bstrUserName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DisplayLock(bstrUserName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DisplayUnlock(bstrUserName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def StartScreenSaver(bstrUserName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def StopScreenSaver(bstrUserName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ISensLogon2(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('d597bab4-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
    @commethod(7)
    def Logon(bstrUserName: Windows.Win32.Foundation.BSTR, dwSessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Logoff(bstrUserName: Windows.Win32.Foundation.BSTR, dwSessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SessionDisconnect(bstrUserName: Windows.Win32.Foundation.BSTR, dwSessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SessionReconnect(bstrUserName: Windows.Win32.Foundation.BSTR, dwSessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def PostShell(bstrUserName: Windows.Win32.Foundation.BSTR, dwSessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISensNetwork(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('d597bab1-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
    @commethod(7)
    def ConnectionMade(bstrConnection: Windows.Win32.Foundation.BSTR, ulType: UInt32, lpQOCInfo: POINTER(Windows.Win32.System.EventNotificationService.SENS_QOCINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ConnectionMadeNoQOCInfo(bstrConnection: Windows.Win32.Foundation.BSTR, ulType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ConnectionLost(bstrConnection: Windows.Win32.Foundation.BSTR, ulType: Windows.Win32.System.EventNotificationService.SENS_CONNECTION_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DestinationReachable(bstrDestination: Windows.Win32.Foundation.BSTR, bstrConnection: Windows.Win32.Foundation.BSTR, ulType: UInt32, lpQOCInfo: POINTER(Windows.Win32.System.EventNotificationService.SENS_QOCINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DestinationReachableNoQOCInfo(bstrDestination: Windows.Win32.Foundation.BSTR, bstrConnection: Windows.Win32.Foundation.BSTR, ulType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISensOnNow(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('d597bab2-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
    @commethod(7)
    def OnACPower() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnBatteryPower(dwBatteryLifePercent: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def BatteryLow(dwBatteryLifePercent: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
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
