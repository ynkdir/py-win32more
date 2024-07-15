from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Graphics
import win32more.Windows.Win32.System.WinRT
class DisplayAdapterId(Structure):
    LowPart: UInt32
    HighPart: Int32
class DisplayId(Structure):
    Value: UInt64
class IGeometrySource2D(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.IGeometrySource2D'
    _iid_ = Guid('{caff7902-670c-4181-a624-da977203b845}')
class PointInt32(Structure):
    X: Int32
    Y: Int32
class RectInt32(Structure):
    X: Int32
    Y: Int32
    Width: Int32
    Height: Int32
class SizeInt32(Structure):
    Width: Int32
    Height: Int32


make_ready(__name__)
