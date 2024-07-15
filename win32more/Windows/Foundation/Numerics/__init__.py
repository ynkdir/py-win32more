from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation.Numerics
class Matrix3x2(Structure):
    M11: Single
    M12: Single
    M21: Single
    M22: Single
    M31: Single
    M32: Single
class Matrix4x4(Structure):
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
class Plane(Structure):
    Normal: win32more.Windows.Foundation.Numerics.Vector3
    D: Single
class Quaternion(Structure):
    X: Single
    Y: Single
    Z: Single
    W: Single
class Rational(Structure):
    Numerator: UInt32
    Denominator: UInt32
class Vector2(Structure):
    X: Single
    Y: Single
class Vector3(Structure):
    X: Single
    Y: Single
    Z: Single
class Vector4(Structure):
    X: Single
    Y: Single
    Z: Single
    W: Single


make_ready(__name__)
