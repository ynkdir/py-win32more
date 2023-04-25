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
import Windows.Foundation
import Windows.Security.Cryptography.DataProtection
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
class DataProtectionProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Security.Cryptography.DataProtection.DataProtectionProvider'
    @winrt_factorymethod
    def CreateOverloadExplicit(cls: Windows.Security.Cryptography.DataProtection.IDataProtectionProviderFactory, protectionDescriptor: WinRT_String) -> Windows.Security.Cryptography.DataProtection.DataProtectionProvider: ...
    @winrt_activatemethod
    def New(cls) -> Windows.Security.Cryptography.DataProtection.DataProtectionProvider: ...
    @winrt_mixinmethod
    def ProtectAsync(self: Windows.Security.Cryptography.DataProtection.IDataProtectionProvider, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def UnprotectAsync(self: Windows.Security.Cryptography.DataProtection.IDataProtectionProvider, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def ProtectStreamAsync(self: Windows.Security.Cryptography.DataProtection.IDataProtectionProvider, src: Windows.Storage.Streams.IInputStream, dest: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def UnprotectStreamAsync(self: Windows.Security.Cryptography.DataProtection.IDataProtectionProvider, src: Windows.Storage.Streams.IInputStream, dest: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncAction: ...
class IDataProtectionProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('09639948-ed22-4270-bd-1c-6d-72-c0-0f-87-87')
    @winrt_commethod(6)
    def ProtectAsync(self, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(7)
    def UnprotectAsync(self, data: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(8)
    def ProtectStreamAsync(self, src: Windows.Storage.Streams.IInputStream, dest: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def UnprotectStreamAsync(self, src: Windows.Storage.Streams.IInputStream, dest: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncAction: ...
class IDataProtectionProviderFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('adf33dac-4932-4cdf-ac-41-72-14-33-35-14-ca')
    @winrt_commethod(6)
    def CreateOverloadExplicit(self, protectionDescriptor: WinRT_String) -> Windows.Security.Cryptography.DataProtection.DataProtectionProvider: ...
make_head(_module, 'DataProtectionProvider')
make_head(_module, 'IDataProtectionProvider')
make_head(_module, 'IDataProtectionProviderFactory')
