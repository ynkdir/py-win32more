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
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.System.Display
class DisplayRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Display.IDisplayRequest
    _classid_ = 'Windows.System.Display.DisplayRequest'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.System.Display.DisplayRequest: ...
    @winrt_mixinmethod
    def RequestActive(self: win32more.Windows.System.Display.IDisplayRequest) -> Void: ...
    @winrt_mixinmethod
    def RequestRelease(self: win32more.Windows.System.Display.IDisplayRequest) -> Void: ...
class IDisplayRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Display.IDisplayRequest'
    _iid_ = Guid('{e5732044-f49f-4b60-8dd4-5e7e3a632ac0}')
    @winrt_commethod(6)
    def RequestActive(self) -> Void: ...
    @winrt_commethod(7)
    def RequestRelease(self) -> Void: ...
make_ready(__name__)
