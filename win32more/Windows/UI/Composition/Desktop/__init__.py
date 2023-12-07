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
import win32more.Windows.UI.Composition.Desktop
class DesktopWindowTarget(ComPtr):
    extends: win32more.Windows.UI.Composition.CompositionTarget
    default_interface: win32more.Windows.UI.Composition.Desktop.IDesktopWindowTarget
    _classid_ = 'Windows.UI.Composition.Desktop.DesktopWindowTarget'
    @winrt_mixinmethod
    def get_IsTopmost(self: win32more.Windows.UI.Composition.Desktop.IDesktopWindowTarget) -> Boolean: ...
    IsTopmost = property(get_IsTopmost, None)
class IDesktopWindowTarget(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Desktop.IDesktopWindowTarget'
    _iid_ = Guid('{6329d6ca-3366-490e-9db3-25312929ac51}')
    @winrt_commethod(6)
    def get_IsTopmost(self) -> Boolean: ...
    IsTopmost = property(get_IsTopmost, None)
make_ready(__name__)
