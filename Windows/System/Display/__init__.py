from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
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
class DisplayRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Display.DisplayRequest'
    @winrt_activatemethod
    def New(cls) -> Windows.System.Display.DisplayRequest: ...
    @winrt_mixinmethod
    def RequestActive(self: Windows.System.Display.IDisplayRequest) -> Void: ...
    @winrt_mixinmethod
    def RequestRelease(self: Windows.System.Display.IDisplayRequest) -> Void: ...
class IDisplayRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e5732044-f49f-4b60-8d-d4-5e-7e-3a-63-2a-c0')
    @winrt_commethod(6)
    def RequestActive(self) -> Void: ...
    @winrt_commethod(7)
    def RequestRelease(self) -> Void: ...
make_head(_module, 'DisplayRequest')
make_head(_module, 'IDisplayRequest')
