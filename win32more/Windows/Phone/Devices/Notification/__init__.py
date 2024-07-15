from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Phone.Devices.Notification
import win32more.Windows.Win32.System.WinRT
class IVibrationDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Devices.Notification.IVibrationDevice'
    _iid_ = Guid('{1b4a6595-cfcd-4e08-92fb-c1906d04498c}')
    @winrt_commethod(6)
    def Vibrate(self, duration: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(7)
    def Cancel(self) -> Void: ...
class IVibrationDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.Devices.Notification.IVibrationDeviceStatics'
    _iid_ = Guid('{332fd2f1-1c69-4c91-949e-4bb67a85bdc7}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Phone.Devices.Notification.VibrationDevice: ...
class VibrationDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.Devices.Notification.IVibrationDevice
    _classid_ = 'Windows.Phone.Devices.Notification.VibrationDevice'
    @winrt_mixinmethod
    def Vibrate(self: win32more.Windows.Phone.Devices.Notification.IVibrationDevice, duration: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def Cancel(self: win32more.Windows.Phone.Devices.Notification.IVibrationDevice) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Phone.Devices.Notification.IVibrationDeviceStatics) -> win32more.Windows.Phone.Devices.Notification.VibrationDevice: ...


make_ready(__name__)
