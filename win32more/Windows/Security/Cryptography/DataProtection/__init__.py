from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Security.Cryptography.DataProtection
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class DataProtectionProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.Cryptography.DataProtection.IDataProtectionProvider
    _classid_ = 'Windows.Security.Cryptography.DataProtection.DataProtectionProvider'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Security.Cryptography.DataProtection.DataProtectionProvider.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Security.Cryptography.DataProtection.DataProtectionProvider.CreateOverloadExplicit(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Security.Cryptography.DataProtection.DataProtectionProvider: ...
    @winrt_factorymethod
    def CreateOverloadExplicit(cls: win32more.Windows.Security.Cryptography.DataProtection.IDataProtectionProviderFactory, protectionDescriptor: WinRT_String) -> win32more.Windows.Security.Cryptography.DataProtection.DataProtectionProvider: ...
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
