from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.UI.Notifications
class INotificationActivationCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{53e31837-6600-4a81-9395-75cffe746f94}')
    @commethod(3)
    def Activate(self, appUserModelId: win32more.Windows.Win32.Foundation.PWSTR, invokedArgs: win32more.Windows.Win32.Foundation.PWSTR, data: POINTER(win32more.Windows.Win32.UI.Notifications.NOTIFICATION_USER_INPUT_DATA), count: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class NOTIFICATION_USER_INPUT_DATA(Structure):
    Key: win32more.Windows.Win32.Foundation.PWSTR
    Value: win32more.Windows.Win32.Foundation.PWSTR


make_ready(__name__)
