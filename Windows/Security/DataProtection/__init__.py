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
import Windows.Foundation
import Windows.Security.DataProtection
import Windows.Storage
import Windows.Storage.Streams
import Windows.System
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a76582c9-06a2-4273-a803-834c9f87fbeb}')
    @winrt_commethod(6)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
class IUserDataBufferUnprotectResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{8efd0e90-fa9a-46a4-a377-01cebf1e74d8}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Security.DataProtection.UserDataBufferUnprotectStatus: ...
    @winrt_commethod(7)
    def get_UnprotectedBuffer(self) -> Windows.Storage.Streams.IBuffer: ...
    Status = property(get_Status, None)
    UnprotectedBuffer = property(get_UnprotectedBuffer, None)
class IUserDataProtectionManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1f13237d-b42e-4a88-9480-0f240924c876}')
    @winrt_commethod(6)
    def ProtectStorageItemAsync(self, storageItem: Windows.Storage.IStorageItem, availability: Windows.Security.DataProtection.UserDataAvailability) -> Windows.Foundation.IAsyncOperation[Windows.Security.DataProtection.UserDataStorageItemProtectionStatus]: ...
    @winrt_commethod(7)
    def GetStorageItemProtectionInfoAsync(self, storageItem: Windows.Storage.IStorageItem) -> Windows.Foundation.IAsyncOperation[Windows.Security.DataProtection.UserDataStorageItemProtectionInfo]: ...
    @winrt_commethod(8)
    def ProtectBufferAsync(self, unprotectedBuffer: Windows.Storage.Streams.IBuffer, availability: Windows.Security.DataProtection.UserDataAvailability) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(9)
    def UnprotectBufferAsync(self, protectedBuffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Security.DataProtection.UserDataBufferUnprotectResult]: ...
    @winrt_commethod(10)
    def IsContinuedDataAvailabilityExpected(self, availability: Windows.Security.DataProtection.UserDataAvailability) -> Boolean: ...
    @winrt_commethod(11)
    def add_DataAvailabilityStateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Security.DataProtection.UserDataProtectionManager, Windows.Security.DataProtection.UserDataAvailabilityStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_DataAvailabilityStateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IUserDataProtectionManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{977780e8-6dce-4fae-af85-782ac2cf4572}')
    @winrt_commethod(6)
    def TryGetDefault(self) -> Windows.Security.DataProtection.UserDataProtectionManager: ...
    @winrt_commethod(7)
    def TryGetForUser(self, user: Windows.System.User) -> Windows.Security.DataProtection.UserDataProtectionManager: ...
class IUserDataStorageItemProtectionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5b6680f6-e87f-40a1-b19d-a6187a0c662f}')
    @winrt_commethod(6)
    def get_Availability(self) -> Windows.Security.DataProtection.UserDataAvailability: ...
    Availability = property(get_Availability, None)
UserDataAvailability = Int32
UserDataAvailability_Always: UserDataAvailability = 0
UserDataAvailability_AfterFirstUnlock: UserDataAvailability = 1
UserDataAvailability_WhileUnlocked: UserDataAvailability = 2
class UserDataAvailabilityStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.DataProtection.UserDataAvailabilityStateChangedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Security.DataProtection.IUserDataAvailabilityStateChangedEventArgs) -> Windows.Foundation.Deferral: ...
class UserDataBufferUnprotectResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.DataProtection.UserDataBufferUnprotectResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.DataProtection.IUserDataBufferUnprotectResult) -> Windows.Security.DataProtection.UserDataBufferUnprotectStatus: ...
    @winrt_mixinmethod
    def get_UnprotectedBuffer(self: Windows.Security.DataProtection.IUserDataBufferUnprotectResult) -> Windows.Storage.Streams.IBuffer: ...
    Status = property(get_Status, None)
    UnprotectedBuffer = property(get_UnprotectedBuffer, None)
UserDataBufferUnprotectStatus = Int32
UserDataBufferUnprotectStatus_Succeeded: UserDataBufferUnprotectStatus = 0
UserDataBufferUnprotectStatus_Unavailable: UserDataBufferUnprotectStatus = 1
class UserDataProtectionManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.DataProtection.UserDataProtectionManager'
    @winrt_mixinmethod
    def ProtectStorageItemAsync(self: Windows.Security.DataProtection.IUserDataProtectionManager, storageItem: Windows.Storage.IStorageItem, availability: Windows.Security.DataProtection.UserDataAvailability) -> Windows.Foundation.IAsyncOperation[Windows.Security.DataProtection.UserDataStorageItemProtectionStatus]: ...
    @winrt_mixinmethod
    def GetStorageItemProtectionInfoAsync(self: Windows.Security.DataProtection.IUserDataProtectionManager, storageItem: Windows.Storage.IStorageItem) -> Windows.Foundation.IAsyncOperation[Windows.Security.DataProtection.UserDataStorageItemProtectionInfo]: ...
    @winrt_mixinmethod
    def ProtectBufferAsync(self: Windows.Security.DataProtection.IUserDataProtectionManager, unprotectedBuffer: Windows.Storage.Streams.IBuffer, availability: Windows.Security.DataProtection.UserDataAvailability) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def UnprotectBufferAsync(self: Windows.Security.DataProtection.IUserDataProtectionManager, protectedBuffer: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Security.DataProtection.UserDataBufferUnprotectResult]: ...
    @winrt_mixinmethod
    def IsContinuedDataAvailabilityExpected(self: Windows.Security.DataProtection.IUserDataProtectionManager, availability: Windows.Security.DataProtection.UserDataAvailability) -> Boolean: ...
    @winrt_mixinmethod
    def add_DataAvailabilityStateChanged(self: Windows.Security.DataProtection.IUserDataProtectionManager, handler: Windows.Foundation.TypedEventHandler[Windows.Security.DataProtection.UserDataProtectionManager, Windows.Security.DataProtection.UserDataAvailabilityStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DataAvailabilityStateChanged(self: Windows.Security.DataProtection.IUserDataProtectionManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def TryGetDefault(cls: Windows.Security.DataProtection.IUserDataProtectionManagerStatics) -> Windows.Security.DataProtection.UserDataProtectionManager: ...
    @winrt_classmethod
    def TryGetForUser(cls: Windows.Security.DataProtection.IUserDataProtectionManagerStatics, user: Windows.System.User) -> Windows.Security.DataProtection.UserDataProtectionManager: ...
class UserDataStorageItemProtectionInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Security.DataProtection.UserDataStorageItemProtectionInfo'
    @winrt_mixinmethod
    def get_Availability(self: Windows.Security.DataProtection.IUserDataStorageItemProtectionInfo) -> Windows.Security.DataProtection.UserDataAvailability: ...
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
