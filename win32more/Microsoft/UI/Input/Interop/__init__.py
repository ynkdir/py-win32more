from __future__ import annotations
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Microsoft.UI.Input
import win32more.Microsoft.UI.Input.Interop
import win32more.Windows.Devices.Input
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
