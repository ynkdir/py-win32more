from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.System.Display
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class DisplayRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.System.Display.IDisplayRequest
    _classid_ = 'Windows.System.Display.DisplayRequest'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.System.Display.DisplayRequest: ...
    @winrt_mixinmethod
    def RequestActive(self: Windows.System.Display.IDisplayRequest) -> Void: ...
    @winrt_mixinmethod
    def RequestRelease(self: Windows.System.Display.IDisplayRequest) -> Void: ...
class IDisplayRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Display.IDisplayRequest'
    _iid_ = Guid('{e5732044-f49f-4b60-8dd4-5e7e3a632ac0}')
    @winrt_commethod(6)
    def RequestActive(self) -> Void: ...
    @winrt_commethod(7)
    def RequestRelease(self) -> Void: ...
make_head(_module, 'DisplayRequest')
make_head(_module, 'IDisplayRequest')
