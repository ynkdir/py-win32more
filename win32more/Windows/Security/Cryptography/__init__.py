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
import win32more.Windows.Security.Cryptography
import win32more.Windows.Storage.Streams
BinaryStringEncoding = Int32
BinaryStringEncoding_Utf8: BinaryStringEncoding = 0
BinaryStringEncoding_Utf16LE: BinaryStringEncoding = 1
BinaryStringEncoding_Utf16BE: BinaryStringEncoding = 2
class CryptographicBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.CryptographicBuffer'
    @winrt_classmethod
    def Compare(cls: win32more.Windows.Security.Cryptography.ICryptographicBufferStatics, object1: win32more.Windows.Storage.Streams.IBuffer, object2: win32more.Windows.Storage.Streams.IBuffer) -> Boolean: ...
    @winrt_classmethod
    def GenerateRandom(cls: win32more.Windows.Security.Cryptography.ICryptographicBufferStatics, length: UInt32) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def GenerateRandomNumber(cls: win32more.Windows.Security.Cryptography.ICryptographicBufferStatics) -> UInt32: ...
    @winrt_classmethod
    def CreateFromByteArray(cls: win32more.Windows.Security.Cryptography.ICryptographicBufferStatics, value: Annotated[SZArray[Byte], 'In']) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def CopyToByteArray(cls: win32more.Windows.Security.Cryptography.ICryptographicBufferStatics, buffer: win32more.Windows.Storage.Streams.IBuffer, value: POINTER(SZArray[Byte])) -> Void: ...
    @winrt_classmethod
    def DecodeFromHexString(cls: win32more.Windows.Security.Cryptography.ICryptographicBufferStatics, value: WinRT_String) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def EncodeToHexString(cls: win32more.Windows.Security.Cryptography.ICryptographicBufferStatics, buffer: win32more.Windows.Storage.Streams.IBuffer) -> WinRT_String: ...
    @winrt_classmethod
    def DecodeFromBase64String(cls: win32more.Windows.Security.Cryptography.ICryptographicBufferStatics, value: WinRT_String) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def EncodeToBase64String(cls: win32more.Windows.Security.Cryptography.ICryptographicBufferStatics, buffer: win32more.Windows.Storage.Streams.IBuffer) -> WinRT_String: ...
    @winrt_classmethod
    def ConvertStringToBinary(cls: win32more.Windows.Security.Cryptography.ICryptographicBufferStatics, value: WinRT_String, encoding: win32more.Windows.Security.Cryptography.BinaryStringEncoding) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def ConvertBinaryToString(cls: win32more.Windows.Security.Cryptography.ICryptographicBufferStatics, encoding: win32more.Windows.Security.Cryptography.BinaryStringEncoding, buffer: win32more.Windows.Storage.Streams.IBuffer) -> WinRT_String: ...
class ICryptographicBufferStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.ICryptographicBufferStatics'
    _iid_ = Guid('{320b7e22-3cb0-4cdf-8663-1d28910065eb}')
    @winrt_commethod(6)
    def Compare(self, object1: win32more.Windows.Storage.Streams.IBuffer, object2: win32more.Windows.Storage.Streams.IBuffer) -> Boolean: ...
    @winrt_commethod(7)
    def GenerateRandom(self, length: UInt32) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def GenerateRandomNumber(self) -> UInt32: ...
    @winrt_commethod(9)
    def CreateFromByteArray(self, value: Annotated[SZArray[Byte], 'In']) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(10)
    def CopyToByteArray(self, buffer: win32more.Windows.Storage.Streams.IBuffer, value: POINTER(SZArray[Byte])) -> Void: ...
    @winrt_commethod(11)
    def DecodeFromHexString(self, value: WinRT_String) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(12)
    def EncodeToHexString(self, buffer: win32more.Windows.Storage.Streams.IBuffer) -> WinRT_String: ...
    @winrt_commethod(13)
    def DecodeFromBase64String(self, value: WinRT_String) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(14)
    def EncodeToBase64String(self, buffer: win32more.Windows.Storage.Streams.IBuffer) -> WinRT_String: ...
    @winrt_commethod(15)
    def ConvertStringToBinary(self, value: WinRT_String, encoding: win32more.Windows.Security.Cryptography.BinaryStringEncoding) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(16)
    def ConvertBinaryToString(self, encoding: win32more.Windows.Security.Cryptography.BinaryStringEncoding, buffer: win32more.Windows.Storage.Streams.IBuffer) -> WinRT_String: ...


make_ready(__name__)
