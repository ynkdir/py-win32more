from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.UI.Notifications
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class INotificationActivationCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('53e31837-6600-4a81-93-95-75-cf-fe-74-6f-94')
    @commethod(3)
    def Activate(self, appUserModelId: Windows.Win32.Foundation.PWSTR, invokedArgs: Windows.Win32.Foundation.PWSTR, data: POINTER(Windows.Win32.UI.Notifications.NOTIFICATION_USER_INPUT_DATA_head), count: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class NOTIFICATION_USER_INPUT_DATA(EasyCastStructure):
    Key: Windows.Win32.Foundation.PWSTR
    Value: Windows.Win32.Foundation.PWSTR
make_head(_module, 'INotificationActivationCallback')
make_head(_module, 'NOTIFICATION_USER_INPUT_DATA')
