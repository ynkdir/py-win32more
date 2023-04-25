from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Graphics
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class DisplayAdapterId(EasyCastStructure):
    LowPart: UInt32
    HighPart: Int32
class DisplayId(EasyCastStructure):
    Value: UInt64
class IGeometrySource2D(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('caff7902-670c-4181-a6-24-da-97-72-03-b8-45')
class PointInt32(EasyCastStructure):
    X: Int32
    Y: Int32
class RectInt32(EasyCastStructure):
    X: Int32
    Y: Int32
    Width: Int32
    Height: Int32
class SizeInt32(EasyCastStructure):
    Width: Int32
    Height: Int32
make_head(_module, 'DisplayAdapterId')
make_head(_module, 'DisplayId')
make_head(_module, 'IGeometrySource2D')
make_head(_module, 'PointInt32')
make_head(_module, 'RectInt32')
make_head(_module, 'SizeInt32')
