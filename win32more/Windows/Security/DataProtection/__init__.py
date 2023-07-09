from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Security.DataProtection
import win32more.Windows.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
UserDataAvailability = Int32
UserDataAvailability_Always: UserDataAvailability = 0
UserDataAvailability_AfterFirstUnlock: UserDataAvailability = 1
UserDataAvailability_WhileUnlocked: UserDataAvailability = 2
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
UserDataBufferUnprotectStatus = Int32
UserDataBufferUnprotectStatus_Succeeded: UserDataBufferUnprotectStatus = 0
UserDataBufferUnprotectStatus_Unavailable: UserDataBufferUnprotectStatus = 1
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
class UserDataStorageItemProtectionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Security.DataProtection.IUserDataStorageItemProtectionInfo
    _classid_ = 'Windows.Security.DataProtection.UserDataStorageItemProtectionInfo'
    @winrt_mixinmethod
    def get_Availability(self: win32more.Windows.Security.DataProtection.IUserDataStorageItemProtectionInfo) -> win32more.Windows.Security.DataProtection.UserDataAvailability: ...
    Availability = property(get_Availability, None)
UserDataStorageItemProtectionStatus = Int32
UserDataStorageItemProtectionStatus_Succeeded: UserDataStorageItemProtectionStatus = 0
UserDataStorageItemProtectionStatus_NotProtectable: UserDataStorageItemProtectionStatus = 1
UserDataStorageItemProtectionStatus_DataUnavailable: UserDataStorageItemProtectionStatus = 2
make_head(_module, 'IUserDataAvailabilityStateChangedEventArgs')
make_head(_module, 'IUserDataBufferUnprotectResult')
make_head(_module, 'IUserDataProtectionManager')
make_head(_module, 'IUserDataProtectionManagerStatics')
make_head(_module, 'IUserDataStorageItemProtectionInfo')
make_head(_module, 'UserDataAvailabilityStateChangedEventArgs')
make_head(_module, 'UserDataBufferUnprotectResult')
make_head(_module, 'UserDataProtectionManager')
make_head(_module, 'UserDataStorageItemProtectionInfo')
