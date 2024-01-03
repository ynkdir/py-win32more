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
