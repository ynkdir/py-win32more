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
import win32more.Windows.Foundation.Numerics
class Matrix3x2(EasyCastStructure):
    M11: Single
    M12: Single
    M21: Single
    M22: Single
    M31: Single
    M32: Single
class Matrix4x4(EasyCastStructure):
    M11: Single
    M12: Single
    M13: Single
    M14: Single
    M21: Single
    M22: Single
    M23: Single
    M24: Single
    M31: Single
    M32: Single
    M33: Single
    M34: Single
    M41: Single
    M42: Single
    M43: Single
    M44: Single
class Plane(EasyCastStructure):
    Normal: win32more.Windows.Foundation.Numerics.Vector3
    D: Single
class Quaternion(EasyCastStructure):
    X: Single
    Y: Single
    Z: Single
    W: Single
class Rational(EasyCastStructure):
    Numerator: UInt32
    Denominator: UInt32
class Vector2(EasyCastStructure):
    X: Single
    Y: Single
class Vector3(EasyCastStructure):
    X: Single
    Y: Single
    Z: Single
class Vector4(EasyCastStructure):
    X: Single
    Y: Single
    Z: Single
    W: Single


make_ready(__name__)
