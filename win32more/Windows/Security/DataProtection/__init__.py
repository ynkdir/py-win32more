from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Security.DataProtection
import win32more.Windows.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.Win32.System.WinRT
class IUserDataAvailabilityStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.DataProtection.IUserDataAvailabilityStateChangedEventArgs'
    _iid_ = Guid('{a76582c9-06a2-4273-a803-834c9f87fbeb}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
class IUserDataBufferUnprotectResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.DataProtection.IUserDataBufferUnprotectResult'
    _iid_ = Guid('{8efd0e90-fa9a-46a4-a377-01cebf1e74d8}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Security.DataProtection.UserDataBufferUnprotectStatus: ...
    @winrt_commethod(7)
    def get_UnprotectedBuffer(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Status = property(get_Status, None)
    UnprotectedBuffer = property(get_UnprotectedBuffer, None)
class IUserDataProtectionManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.DataProtection.IUserDataProtectionManager'
    _iid_ = Guid('{1f13237d-b42e-4a88-9480-0f240924c876}')
    @winrt_commethod(6)
    def ProtectStorageItemAsync(self, storageItem: win32more.Windows.Storage.IStorageItem, availability: win32more.Windows.Security.DataProtection.UserDataAvailability) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.DataProtection.UserDataStorageItemProtectionStatus]: ...
    @winrt_commethod(7)
    def GetStorageItemProtectionInfoAsync(self, storageItem: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.DataProtection.UserDataStorageItemProtectionInfo]: ...
    @winrt_commethod(8)
    def ProtectBufferAsync(self, unprotectedBuffer: win32more.Windows.Storage.Streams.IBuffer, availability: win32more.Windows.Security.DataProtection.UserDataAvailability) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(9)
    def UnprotectBufferAsync(self, protectedBuffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.DataProtection.UserDataBufferUnprotectResult]: ...
    @winrt_commethod(10)
    def IsContinuedDataAvailabilityExpected(self, availability: win32more.Windows.Security.DataProtection.UserDataAvailability) -> Boolean: ...
    @winrt_commethod(11)
    def add_DataAvailabilityStateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Security.DataProtection.UserDataProtectionManager, win32more.Windows.Security.DataProtection.UserDataAvailabilityStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_DataAvailabilityStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DataAvailabilityStateChanged = event()
class IUserDataProtectionManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.DataProtection.IUserDataProtectionManagerStatics'
    _iid_ = Guid('{977780e8-6dce-4fae-af85-782ac2cf4572}')
    @winrt_commethod(6)
    def TryGetDefault(self) -> win32more.Windows.Security.DataProtection.UserDataProtectionManager: ...
    @winrt_commethod(7)
    def TryGetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.Security.DataProtection.UserDataProtectionManager: ...
class IUserDataStorageItemProtectionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.DataProtection.IUserDataStorageItemProtectionInfo'
    _iid_ = Guid('{5b6680f6-e87f-40a1-b19d-a6187a0c662f}')
    @winrt_commethod(6)
    def get_Availability(self) -> win32more.Windows.Security.DataProtection.UserDataAvailability: ...
    Availability = property(get_Availability, None)
class UserDataAvailability(Enum, Int32):
    Always = 0
    AfterFirstUnlock = 1
    WhileUnlocked = 2
class UserDataAvailabilityStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.DataProtection.IUserDataAvailabilityStateChangedEventArgs
    _classid_ = 'Windows.Security.DataProtection.UserDataAvailabilityStateChangedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Security.DataProtection.IUserDataAvailabilityStateChangedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
class UserDataBufferUnprotectResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.DataProtection.IUserDataBufferUnprotectResult
    _classid_ = 'Windows.Security.DataProtection.UserDataBufferUnprotectResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Security.DataProtection.IUserDataBufferUnprotectResult) -> win32more.Windows.Security.DataProtection.UserDataBufferUnprotectStatus: ...
    @winrt_mixinmethod
    def get_UnprotectedBuffer(self: win32more.Windows.Security.DataProtection.IUserDataBufferUnprotectResult) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Status = property(get_Status, None)
    UnprotectedBuffer = property(get_UnprotectedBuffer, None)
class UserDataBufferUnprotectStatus(Enum, Int32):
    Succeeded = 0
    Unavailable = 1
class UserDataProtectionManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.DataProtection.IUserDataProtectionManager
    _classid_ = 'Windows.Security.DataProtection.UserDataProtectionManager'
    @winrt_mixinmethod
    def ProtectStorageItemAsync(self: win32more.Windows.Security.DataProtection.IUserDataProtectionManager, storageItem: win32more.Windows.Storage.IStorageItem, availability: win32more.Windows.Security.DataProtection.UserDataAvailability) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.DataProtection.UserDataStorageItemProtectionStatus]: ...
    @winrt_mixinmethod
    def GetStorageItemProtectionInfoAsync(self: win32more.Windows.Security.DataProtection.IUserDataProtectionManager, storageItem: win32more.Windows.Storage.IStorageItem) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.DataProtection.UserDataStorageItemProtectionInfo]: ...
    @winrt_mixinmethod
    def ProtectBufferAsync(self: win32more.Windows.Security.DataProtection.IUserDataProtectionManager, unprotectedBuffer: win32more.Windows.Storage.Streams.IBuffer, availability: win32more.Windows.Security.DataProtection.UserDataAvailability) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def UnprotectBufferAsync(self: win32more.Windows.Security.DataProtection.IUserDataProtectionManager, protectedBuffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Security.DataProtection.UserDataBufferUnprotectResult]: ...
    @winrt_mixinmethod
    def IsContinuedDataAvailabilityExpected(self: win32more.Windows.Security.DataProtection.IUserDataProtectionManager, availability: win32more.Windows.Security.DataProtection.UserDataAvailability) -> Boolean: ...
    @winrt_mixinmethod
    def add_DataAvailabilityStateChanged(self: win32more.Windows.Security.DataProtection.IUserDataProtectionManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Security.DataProtection.UserDataProtectionManager, win32more.Windows.Security.DataProtection.UserDataAvailabilityStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DataAvailabilityStateChanged(self: win32more.Windows.Security.DataProtection.IUserDataProtectionManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def TryGetDefault(cls: win32more.Windows.Security.DataProtection.IUserDataProtectionManagerStatics) -> win32more.Windows.Security.DataProtection.UserDataProtectionManager: ...
    @winrt_classmethod
    def TryGetForUser(cls: win32more.Windows.Security.DataProtection.IUserDataProtectionManagerStatics, user: win32more.Windows.System.User) -> win32more.Windows.Security.DataProtection.UserDataProtectionManager: ...
    DataAvailabilityStateChanged = event()
class UserDataStorageItemProtectionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.DataProtection.IUserDataStorageItemProtectionInfo
    _classid_ = 'Windows.Security.DataProtection.UserDataStorageItemProtectionInfo'
    @winrt_mixinmethod
    def get_Availability(self: win32more.Windows.Security.DataProtection.IUserDataStorageItemProtectionInfo) -> win32more.Windows.Security.DataProtection.UserDataAvailability: ...
    Availability = property(get_Availability, None)
class UserDataStorageItemProtectionStatus(Enum, Int32):
    Succeeded = 0
    NotProtectable = 1
    DataUnavailable = 2


make_ready(__name__)
