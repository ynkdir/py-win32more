from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.UI.Notifications
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
class INotificationActivationCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('53e31837-6600-4a81-93-95-75-cf-fe-74-6f-94')
    @commethod(3)
    def Activate(appUserModelId: win32more.Foundation.PWSTR, invokedArgs: win32more.Foundation.PWSTR, data: POINTER(win32more.UI.Notifications.NOTIFICATION_USER_INPUT_DATA_head), count: UInt32) -> win32more.Foundation.HRESULT: ...
class NOTIFICATION_USER_INPUT_DATA(Structure):
    Key: win32more.Foundation.PWSTR
    Value: win32more.Foundation.PWSTR
make_head(_module, 'INotificationActivationCallback')
make_head(_module, 'NOTIFICATION_USER_INPUT_DATA')
__all__ = [
    "INotificationActivationCallback",
    "NOTIFICATION_USER_INPUT_DATA",
]
_arch_optional = [
]
