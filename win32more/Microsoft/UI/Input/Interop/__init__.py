from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
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
