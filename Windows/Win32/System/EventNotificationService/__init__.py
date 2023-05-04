from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.EventNotificationService
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
NETWORK_ALIVE_LAN: UInt32 = 1
NETWORK_ALIVE_WAN: UInt32 = 2
NETWORK_ALIVE_AOL: UInt32 = 4
NETWORK_ALIVE_INTERNET: UInt32 = 8
CONNECTION_AOL: UInt32 = 4
SENSGUID_PUBLISHER: Guid = Guid('{5fee1bd6-5b9b-11d1-8dd2-00aa004abd5e}')
SENSGUID_SUBSCRIBER_LCE: Guid = Guid('{d3938ab0-5b9d-11d1-8dd2-00aa004abd5e}')
SENSGUID_SUBSCRIBER_WININET: Guid = Guid('{d3938ab5-5b9d-11d1-8dd2-00aa004abd5e}')
SENSGUID_EVENTCLASS_NETWORK: Guid = Guid('{d5978620-5b9f-11d1-8dd2-00aa004abd5e}')
SENSGUID_EVENTCLASS_LOGON: Guid = Guid('{d5978630-5b9f-11d1-8dd2-00aa004abd5e}')
SENSGUID_EVENTCLASS_ONNOW: Guid = Guid('{d5978640-5b9f-11d1-8dd2-00aa004abd5e}')
SENSGUID_EVENTCLASS_LOGON2: Guid = Guid('{d5978650-5b9f-11d1-8dd2-00aa004abd5e}')
@winfunctype('SensApi.dll')
def IsDestinationReachableA(lpszDestination: Windows.Win32.Foundation.PSTR, lpQOCInfo: POINTER(Windows.Win32.System.EventNotificationService.QOCINFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SensApi.dll')
def IsDestinationReachableW(lpszDestination: Windows.Win32.Foundation.PWSTR, lpQOCInfo: POINTER(Windows.Win32.System.EventNotificationService.QOCINFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('SensApi.dll')
def IsNetworkAlive(lpdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
class ISensLogon(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d597bab3-5b9f-11d1-8dd2-00aa004abd5e}')
    @commethod(7)
    def Logon(self, bstrUserName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Logoff(self, bstrUserName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def StartShell(self, bstrUserName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DisplayLock(self, bstrUserName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DisplayUnlock(self, bstrUserName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def StartScreenSaver(self, bstrUserName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def StopScreenSaver(self, bstrUserName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ISensLogon2(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d597bab4-5b9f-11d1-8dd2-00aa004abd5e}')
    @commethod(7)
    def Logon(self, bstrUserName: Windows.Win32.Foundation.BSTR, dwSessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Logoff(self, bstrUserName: Windows.Win32.Foundation.BSTR, dwSessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SessionDisconnect(self, bstrUserName: Windows.Win32.Foundation.BSTR, dwSessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SessionReconnect(self, bstrUserName: Windows.Win32.Foundation.BSTR, dwSessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def PostShell(self, bstrUserName: Windows.Win32.Foundation.BSTR, dwSessionId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISensNetwork(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d597bab1-5b9f-11d1-8dd2-00aa004abd5e}')
    @commethod(7)
    def ConnectionMade(self, bstrConnection: Windows.Win32.Foundation.BSTR, ulType: UInt32, lpQOCInfo: POINTER(Windows.Win32.System.EventNotificationService.SENS_QOCINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ConnectionMadeNoQOCInfo(self, bstrConnection: Windows.Win32.Foundation.BSTR, ulType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ConnectionLost(self, bstrConnection: Windows.Win32.Foundation.BSTR, ulType: Windows.Win32.System.EventNotificationService.SENS_CONNECTION_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DestinationReachable(self, bstrDestination: Windows.Win32.Foundation.BSTR, bstrConnection: Windows.Win32.Foundation.BSTR, ulType: UInt32, lpQOCInfo: POINTER(Windows.Win32.System.EventNotificationService.SENS_QOCINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DestinationReachableNoQOCInfo(self, bstrDestination: Windows.Win32.Foundation.BSTR, bstrConnection: Windows.Win32.Foundation.BSTR, ulType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISensOnNow(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d597bab2-5b9f-11d1-8dd2-00aa004abd5e}')
    @commethod(7)
    def OnACPower(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnBatteryPower(self, dwBatteryLifePercent: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def BatteryLow(self, dwBatteryLifePercent: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class QOCINFO(EasyCastStructure):
    dwSize: UInt32
    dwFlags: UInt32
    dwInSpeed: UInt32
    dwOutSpeed: UInt32
SENS = Guid('{d597cafe-5b9f-11d1-8dd2-00aa004abd5e}')
SENS_CONNECTION_TYPE = UInt32
CONNECTION_LAN: SENS_CONNECTION_TYPE = 0
CONNECTION_WAN: SENS_CONNECTION_TYPE = 1
class SENS_QOCINFO(EasyCastStructure):
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
