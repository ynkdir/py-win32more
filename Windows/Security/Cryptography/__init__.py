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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Security.Cryptography
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
BinaryStringEncoding = Int32
BinaryStringEncoding_Utf8: BinaryStringEncoding = 0
BinaryStringEncoding_Utf16LE: BinaryStringEncoding = 1
BinaryStringEncoding_Utf16BE: BinaryStringEncoding = 2
class CryptographicBuffer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.CryptographicBuffer'
    @winrt_classmethod
    def Compare(cls: Windows.Security.Cryptography.ICryptographicBufferStatics, object1: Windows.Storage.Streams.IBuffer, object2: Windows.Storage.Streams.IBuffer) -> Boolean: ...
    @winrt_classmethod
    def GenerateRandom(cls: Windows.Security.Cryptography.ICryptographicBufferStatics, length: UInt32) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def GenerateRandomNumber(cls: Windows.Security.Cryptography.ICryptographicBufferStatics) -> UInt32: ...
    @winrt_classmethod
    def CreateFromByteArray(cls: Windows.Security.Cryptography.ICryptographicBufferStatics, value: c_char_p_no) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def CopyToByteArray(cls: Windows.Security.Cryptography.ICryptographicBufferStatics, buffer: Windows.Storage.Streams.IBuffer, value: POINTER(c_char_p_no)) -> Void: ...
    @winrt_classmethod
    def DecodeFromHexString(cls: Windows.Security.Cryptography.ICryptographicBufferStatics, value: WinRT_String) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def EncodeToHexString(cls: Windows.Security.Cryptography.ICryptographicBufferStatics, buffer: Windows.Storage.Streams.IBuffer) -> WinRT_String: ...
    @winrt_classmethod
    def DecodeFromBase64String(cls: Windows.Security.Cryptography.ICryptographicBufferStatics, value: WinRT_String) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def EncodeToBase64String(cls: Windows.Security.Cryptography.ICryptographicBufferStatics, buffer: Windows.Storage.Streams.IBuffer) -> WinRT_String: ...
    @winrt_classmethod
    def ConvertStringToBinary(cls: Windows.Security.Cryptography.ICryptographicBufferStatics, value: WinRT_String, encoding: Windows.Security.Cryptography.BinaryStringEncoding) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_classmethod
    def ConvertBinaryToString(cls: Windows.Security.Cryptography.ICryptographicBufferStatics, encoding: Windows.Security.Cryptography.BinaryStringEncoding, buffer: Windows.Storage.Streams.IBuffer) -> WinRT_String: ...
class ICryptographicBufferStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{320b7e22-3cb0-4cdf-8663-1d28910065eb}')
    @winrt_commethod(6)
    def Compare(self, object1: Windows.Storage.Streams.IBuffer, object2: Windows.Storage.Streams.IBuffer) -> Boolean: ...
    @winrt_commethod(7)
    def GenerateRandom(self, length: UInt32) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def GenerateRandomNumber(self) -> UInt32: ...
    @winrt_commethod(9)
    def CreateFromByteArray(self, value: c_char_p_no) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(10)
    def CopyToByteArray(self, buffer: Windows.Storage.Streams.IBuffer, value: POINTER(c_char_p_no)) -> Void: ...
    @winrt_commethod(11)
    def DecodeFromHexString(self, value: WinRT_String) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(12)
    def EncodeToHexString(self, buffer: Windows.Storage.Streams.IBuffer) -> WinRT_String: ...
    @winrt_commethod(13)
    def DecodeFromBase64String(self, value: WinRT_String) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(14)
    def EncodeToBase64String(self, buffer: Windows.Storage.Streams.IBuffer) -> WinRT_String: ...
    @winrt_commethod(15)
    def ConvertStringToBinary(self, value: WinRT_String, encoding: Windows.Security.Cryptography.BinaryStringEncoding) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(16)
    def ConvertBinaryToString(self, encoding: Windows.Security.Cryptography.BinaryStringEncoding, buffer: Windows.Storage.Streams.IBuffer) -> WinRT_String: ...
make_head(_module, 'CryptographicBuffer')
make_head(_module, 'ICryptographicBufferStatics')
