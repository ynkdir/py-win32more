from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.EventNotificationService
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
def IsDestinationReachableA(lpszDestination: win32more.Windows.Win32.Foundation.PSTR, lpQOCInfo: POINTER(win32more.Windows.Win32.System.EventNotificationService.QOCINFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SensApi.dll')
def IsDestinationReachableW(lpszDestination: win32more.Windows.Win32.Foundation.PWSTR, lpQOCInfo: POINTER(win32more.Windows.Win32.System.EventNotificationService.QOCINFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
IsDestinationReachable = UnicodeAlias('IsDestinationReachableW')
@winfunctype('SensApi.dll')
def IsNetworkAlive(lpdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
class ISensLogon(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d597bab3-5b9f-11d1-8dd2-00aa004abd5e}')
    @commethod(7)
    def Logon(self, bstrUserName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Logoff(self, bstrUserName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def StartShell(self, bstrUserName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DisplayLock(self, bstrUserName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DisplayUnlock(self, bstrUserName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def StartScreenSaver(self, bstrUserName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def StopScreenSaver(self, bstrUserName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISensLogon2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d597bab4-5b9f-11d1-8dd2-00aa004abd5e}')
    @commethod(7)
    def Logon(self, bstrUserName: win32more.Windows.Win32.Foundation.BSTR, dwSessionId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Logoff(self, bstrUserName: win32more.Windows.Win32.Foundation.BSTR, dwSessionId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SessionDisconnect(self, bstrUserName: win32more.Windows.Win32.Foundation.BSTR, dwSessionId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SessionReconnect(self, bstrUserName: win32more.Windows.Win32.Foundation.BSTR, dwSessionId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def PostShell(self, bstrUserName: win32more.Windows.Win32.Foundation.BSTR, dwSessionId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISensNetwork(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d597bab1-5b9f-11d1-8dd2-00aa004abd5e}')
    @commethod(7)
    def ConnectionMade(self, bstrConnection: win32more.Windows.Win32.Foundation.BSTR, ulType: UInt32, lpQOCInfo: POINTER(win32more.Windows.Win32.System.EventNotificationService.SENS_QOCINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ConnectionMadeNoQOCInfo(self, bstrConnection: win32more.Windows.Win32.Foundation.BSTR, ulType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ConnectionLost(self, bstrConnection: win32more.Windows.Win32.Foundation.BSTR, ulType: win32more.Windows.Win32.System.EventNotificationService.SENS_CONNECTION_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DestinationReachable(self, bstrDestination: win32more.Windows.Win32.Foundation.BSTR, bstrConnection: win32more.Windows.Win32.Foundation.BSTR, ulType: UInt32, lpQOCInfo: POINTER(win32more.Windows.Win32.System.EventNotificationService.SENS_QOCINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DestinationReachableNoQOCInfo(self, bstrDestination: win32more.Windows.Win32.Foundation.BSTR, bstrConnection: win32more.Windows.Win32.Foundation.BSTR, ulType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISensOnNow(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d597bab2-5b9f-11d1-8dd2-00aa004abd5e}')
    @commethod(7)
    def OnACPower(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnBatteryPower(self, dwBatteryLifePercent: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def BatteryLow(self, dwBatteryLifePercent: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class QOCINFO(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwInSpeed: UInt32
    dwOutSpeed: UInt32
SENS = Guid('{d597cafe-5b9f-11d1-8dd2-00aa004abd5e}')
SENS_CONNECTION_TYPE = UInt32
CONNECTION_LAN: win32more.Windows.Win32.System.EventNotificationService.SENS_CONNECTION_TYPE = 0
CONNECTION_WAN: win32more.Windows.Win32.System.EventNotificationService.SENS_CONNECTION_TYPE = 1
class SENS_QOCINFO(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwOutSpeed: UInt32
    dwInSpeed: UInt32


make_ready(__name__)
