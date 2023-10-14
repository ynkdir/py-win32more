from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Security.Cryptography.DataProtection
import win32more.Windows.Storage.Streams
class DataProtectionProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.DataProtection.IDataProtectionProvider
    _classid_ = 'Windows.Security.Cryptography.DataProtection.DataProtectionProvider'
    @winrt_factorymethod
    def CreateOverloadExplicit(cls: win32more.Windows.Security.Cryptography.DataProtection.IDataProtectionProviderFactory, protectionDescriptor: WinRT_String) -> win32more.Windows.Security.Cryptography.DataProtection.DataProtectionProvider: ...
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.Cryptography.DataProtection.DataProtectionProvider: ...
    @winrt_mixinmethod
    def ProtectAsync(self: win32more.Windows.Security.Cryptography.DataProtection.IDataProtectionProvider, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def UnprotectAsync(self: win32more.Windows.Security.Cryptography.DataProtection.IDataProtectionProvider, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def ProtectStreamAsync(self: win32more.Windows.Security.Cryptography.DataProtection.IDataProtectionProvider, src: win32more.Windows.Storage.Streams.IInputStream, dest: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def UnprotectStreamAsync(self: win32more.Windows.Security.Cryptography.DataProtection.IDataProtectionProvider, src: win32more.Windows.Storage.Streams.IInputStream, dest: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncAction: ...
class IDataProtectionProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.DataProtection.IDataProtectionProvider'
    _iid_ = Guid('{09639948-ed22-4270-bd1c-6d72c00f8787}')
    @winrt_commethod(6)
    def ProtectAsync(self, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(7)
    def UnprotectAsync(self, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(8)
    def ProtectStreamAsync(self, src: win32more.Windows.Storage.Streams.IInputStream, dest: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def UnprotectStreamAsync(self, src: win32more.Windows.Storage.Streams.IInputStream, dest: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncAction: ...
class IDataProtectionProviderFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.Cryptography.DataProtection.IDataProtectionProviderFactory'
    _iid_ = Guid('{adf33dac-4932-4cdf-ac41-7214333514ca}')
    @winrt_commethod(6)
    def CreateOverloadExplicit(self, protectionDescriptor: WinRT_String) -> win32more.Windows.Security.Cryptography.DataProtection.DataProtectionProvider: ...
make_ready(__name__)
