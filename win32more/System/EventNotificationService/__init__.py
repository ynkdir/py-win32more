from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.EventNotificationService
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
NETWORK_ALIVE_LAN = 1
NETWORK_ALIVE_WAN = 2
NETWORK_ALIVE_AOL = 4
NETWORK_ALIVE_INTERNET = 8
CONNECTION_AOL = 4
def _define_SENSGUID_PUBLISHER():
    return Guid('5fee1bd6-5b9b-11d1-8d-d2-00-aa-00-4a-bd-5e')
def _define_SENSGUID_SUBSCRIBER_LCE():
    return Guid('d3938ab0-5b9d-11d1-8d-d2-00-aa-00-4a-bd-5e')
def _define_SENSGUID_SUBSCRIBER_WININET():
    return Guid('d3938ab5-5b9d-11d1-8d-d2-00-aa-00-4a-bd-5e')
def _define_SENSGUID_EVENTCLASS_NETWORK():
    return Guid('d5978620-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
def _define_SENSGUID_EVENTCLASS_LOGON():
    return Guid('d5978630-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
def _define_SENSGUID_EVENTCLASS_ONNOW():
    return Guid('d5978640-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
def _define_SENSGUID_EVENTCLASS_LOGON2():
    return Guid('d5978650-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
def _define_IsDestinationReachableA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.System.EventNotificationService.QOCINFO_head))(('IsDestinationReachableA', windll['SensApi.dll']), ((1, 'lpszDestination'),(1, 'lpQOCInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsDestinationReachableW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.System.EventNotificationService.QOCINFO_head))(('IsDestinationReachableW', windll['SensApi.dll']), ((1, 'lpszDestination'),(1, 'lpQOCInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsNetworkAlive():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt32))(('IsNetworkAlive', windll['SensApi.dll']), ((1, 'lpdwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ISensLogon_head():
    class ISensLogon(win32more.System.Com.IDispatch_head):
        Guid = Guid('d597bab3-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
    return ISensLogon
def _define_ISensLogon():
    ISensLogon = win32more.System.EventNotificationService.ISensLogon_head
    ISensLogon.Logon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(7, 'Logon', ((1, 'bstrUserName'),)))
    ISensLogon.Logoff = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(8, 'Logoff', ((1, 'bstrUserName'),)))
    ISensLogon.StartShell = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(9, 'StartShell', ((1, 'bstrUserName'),)))
    ISensLogon.DisplayLock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(10, 'DisplayLock', ((1, 'bstrUserName'),)))
    ISensLogon.DisplayUnlock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(11, 'DisplayUnlock', ((1, 'bstrUserName'),)))
    ISensLogon.StartScreenSaver = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(12, 'StartScreenSaver', ((1, 'bstrUserName'),)))
    ISensLogon.StopScreenSaver = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR)(13, 'StopScreenSaver', ((1, 'bstrUserName'),)))
    win32more.System.Com.IDispatch
    return ISensLogon
def _define_ISensLogon2_head():
    class ISensLogon2(win32more.System.Com.IDispatch_head):
        Guid = Guid('d597bab4-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
    return ISensLogon2
def _define_ISensLogon2():
    ISensLogon2 = win32more.System.EventNotificationService.ISensLogon2_head
    ISensLogon2.Logon = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32)(7, 'Logon', ((1, 'bstrUserName'),(1, 'dwSessionId'),)))
    ISensLogon2.Logoff = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32)(8, 'Logoff', ((1, 'bstrUserName'),(1, 'dwSessionId'),)))
    ISensLogon2.SessionDisconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32)(9, 'SessionDisconnect', ((1, 'bstrUserName'),(1, 'dwSessionId'),)))
    ISensLogon2.SessionReconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32)(10, 'SessionReconnect', ((1, 'bstrUserName'),(1, 'dwSessionId'),)))
    ISensLogon2.PostShell = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32)(11, 'PostShell', ((1, 'bstrUserName'),(1, 'dwSessionId'),)))
    win32more.System.Com.IDispatch
    return ISensLogon2
def _define_ISensNetwork_head():
    class ISensNetwork(win32more.System.Com.IDispatch_head):
        Guid = Guid('d597bab1-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
    return ISensNetwork
def _define_ISensNetwork():
    ISensNetwork = win32more.System.EventNotificationService.ISensNetwork_head
    ISensNetwork.ConnectionMade = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32,POINTER(win32more.System.EventNotificationService.SENS_QOCINFO_head))(7, 'ConnectionMade', ((1, 'bstrConnection'),(1, 'ulType'),(1, 'lpQOCInfo'),)))
    ISensNetwork.ConnectionMadeNoQOCInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32)(8, 'ConnectionMadeNoQOCInfo', ((1, 'bstrConnection'),(1, 'ulType'),)))
    ISensNetwork.ConnectionLost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.EventNotificationService.SENS_CONNECTION_TYPE)(9, 'ConnectionLost', ((1, 'bstrConnection'),(1, 'ulType'),)))
    ISensNetwork.DestinationReachable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,UInt32,POINTER(win32more.System.EventNotificationService.SENS_QOCINFO_head))(10, 'DestinationReachable', ((1, 'bstrDestination'),(1, 'bstrConnection'),(1, 'ulType'),(1, 'lpQOCInfo'),)))
    ISensNetwork.DestinationReachableNoQOCInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,UInt32)(11, 'DestinationReachableNoQOCInfo', ((1, 'bstrDestination'),(1, 'bstrConnection'),(1, 'ulType'),)))
    win32more.System.Com.IDispatch
    return ISensNetwork
def _define_ISensOnNow_head():
    class ISensOnNow(win32more.System.Com.IDispatch_head):
        Guid = Guid('d597bab2-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
    return ISensOnNow
def _define_ISensOnNow():
    ISensOnNow = win32more.System.EventNotificationService.ISensOnNow_head
    ISensOnNow.OnACPower = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'OnACPower', ()))
    ISensOnNow.OnBatteryPower = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(8, 'OnBatteryPower', ((1, 'dwBatteryLifePercent'),)))
    ISensOnNow.BatteryLow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(9, 'BatteryLow', ((1, 'dwBatteryLifePercent'),)))
    win32more.System.Com.IDispatch
    return ISensOnNow
def _define_QOCINFO_head():
    class QOCINFO(Structure):
        pass
    return QOCINFO
def _define_QOCINFO():
    QOCINFO = win32more.System.EventNotificationService.QOCINFO_head
    QOCINFO._fields_ = [
        ('dwSize', UInt32),
        ('dwFlags', UInt32),
        ('dwInSpeed', UInt32),
        ('dwOutSpeed', UInt32),
    ]
    return QOCINFO
SENS = Guid('d597cafe-5b9f-11d1-8d-d2-00-aa-00-4a-bd-5e')
SENS_CONNECTION_TYPE = UInt32
CONNECTION_LAN = 0
CONNECTION_WAN = 1
def _define_SENS_QOCINFO_head():
    class SENS_QOCINFO(Structure):
        pass
    return SENS_QOCINFO
def _define_SENS_QOCINFO():
    SENS_QOCINFO = win32more.System.EventNotificationService.SENS_QOCINFO_head
    SENS_QOCINFO._fields_ = [
        ('dwSize', UInt32),
        ('dwFlags', UInt32),
        ('dwOutSpeed', UInt32),
        ('dwInSpeed', UInt32),
    ]
    return SENS_QOCINFO
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
