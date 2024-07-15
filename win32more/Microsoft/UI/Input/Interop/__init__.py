from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI.Input
import win32more.Microsoft.UI.Input.Interop
import win32more.Windows.Devices.Input
import win32more.Windows.Win32.System.WinRT
class IPenDeviceInteropStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.Interop.IPenDeviceInteropStatics'
    _iid_ = Guid('{c2a59f2a-e077-5d30-a1bd-cf84dd09ee39}')
    @winrt_commethod(6)
    def FromPointerPoint(self, pointerPoint: win32more.Microsoft.UI.Input.PointerPoint) -> win32more.Windows.Devices.Input.PenDevice: ...
class PenDeviceInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.Interop.PenDeviceInterop'
    @winrt_classmethod
    def FromPointerPoint(cls: win32more.Microsoft.UI.Input.Interop.IPenDeviceInteropStatics, pointerPoint: win32more.Microsoft.UI.Input.PointerPoint) -> win32more.Windows.Devices.Input.PenDevice: ...


make_ready(__name__)
