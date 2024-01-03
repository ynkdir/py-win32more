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
import win32more.Windows.Graphics
class DisplayAdapterId(EasyCastStructure):
    LowPart: UInt32
    HighPart: Int32
class DisplayId(EasyCastStructure):
    Value: UInt64
class IGeometrySource2D(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.IGeometrySource2D'
    _iid_ = Guid('{caff7902-670c-4181-a624-da977203b845}')
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


make_ready(__name__)
