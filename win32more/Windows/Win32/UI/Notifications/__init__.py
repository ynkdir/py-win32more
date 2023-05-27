from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.UI.Notifications
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
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{53e31837-6600-4a81-9395-75cffe746f94}')
    @commethod(3)
    def Activate(self, appUserModelId: win32more.Windows.Win32.Foundation.PWSTR, invokedArgs: win32more.Windows.Win32.Foundation.PWSTR, data: POINTER(win32more.Windows.Win32.UI.Notifications.NOTIFICATION_USER_INPUT_DATA_head), count: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class NOTIFICATION_USER_INPUT_DATA(EasyCastStructure):
    Key: win32more.Windows.Win32.Foundation.PWSTR
    Value: win32more.Windows.Win32.Foundation.PWSTR
make_head(_module, 'INotificationActivationCallback')
make_head(_module, 'NOTIFICATION_USER_INPUT_DATA')
