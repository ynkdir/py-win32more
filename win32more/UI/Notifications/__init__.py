from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.UI.Notifications
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
def _define_INotificationActivationCallback_head():
    class INotificationActivationCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('53e31837-6600-4a81-93-95-75-cf-fe-74-6f-94')
    return INotificationActivationCallback
def _define_INotificationActivationCallback():
    INotificationActivationCallback = win32more.UI.Notifications.INotificationActivationCallback_head
    INotificationActivationCallback.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.UI.Notifications.NOTIFICATION_USER_INPUT_DATA_head),UInt32)(3, 'Activate', ((1, 'appUserModelId'),(1, 'invokedArgs'),(1, 'data'),(1, 'count'),)))
    win32more.System.Com.IUnknown
    return INotificationActivationCallback
def _define_NOTIFICATION_USER_INPUT_DATA_head():
    class NOTIFICATION_USER_INPUT_DATA(Structure):
        pass
    return NOTIFICATION_USER_INPUT_DATA
def _define_NOTIFICATION_USER_INPUT_DATA():
    NOTIFICATION_USER_INPUT_DATA = win32more.UI.Notifications.NOTIFICATION_USER_INPUT_DATA_head
    NOTIFICATION_USER_INPUT_DATA._fields_ = [
        ('Key', win32more.Foundation.PWSTR),
        ('Value', win32more.Foundation.PWSTR),
    ]
    return NOTIFICATION_USER_INPUT_DATA
__all__ = [
    "INotificationActivationCallback",
    "NOTIFICATION_USER_INPUT_DATA",
]
