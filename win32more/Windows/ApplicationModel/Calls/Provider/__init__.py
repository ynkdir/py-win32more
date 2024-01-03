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
import win32more.Windows.ApplicationModel.Calls.Provider
import win32more.Windows.Foundation
import win32more.Windows.Storage
class IPhoneCallOrigin(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin'
    _iid_ = Guid('{20613479-0ef9-4454-871c-afb66a14b6a5}')
    @winrt_commethod(6)
    def get_Category(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Category(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_CategoryDescription(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_CategoryDescription(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Location(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Location(self, value: WinRT_String) -> Void: ...
    Category = property(get_Category, put_Category)
    CategoryDescription = property(get_CategoryDescription, put_CategoryDescription)
    Location = property(get_Location, put_Location)
class IPhoneCallOrigin2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin2'
    _iid_ = Guid('{04c7e980-9ac2-4768-b536-b68da4957d02}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
class IPhoneCallOrigin3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin3'
    _iid_ = Guid('{49330fb4-d1a7-43a2-aeee-c07b6dbaf068}')
    @winrt_commethod(6)
    def get_DisplayPicture(self) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_commethod(7)
    def put_DisplayPicture(self, value: win32more.Windows.Storage.StorageFile) -> Void: ...
    DisplayPicture = property(get_DisplayPicture, put_DisplayPicture)
class IPhoneCallOriginManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Provider.IPhoneCallOriginManagerStatics'
    _iid_ = Guid('{ccfc5a0a-9af7-6149-39d0-e076fcce1395}')
    @winrt_commethod(6)
    def get_IsCurrentAppActiveCallOriginApp(self) -> Boolean: ...
    @winrt_commethod(7)
    def ShowPhoneCallOriginSettingsUI(self) -> Void: ...
    @winrt_commethod(8)
    def SetCallOrigin(self, requestId: Guid, callOrigin: win32more.Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin) -> Void: ...
    IsCurrentAppActiveCallOriginApp = property(get_IsCurrentAppActiveCallOriginApp, None)
class IPhoneCallOriginManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Provider.IPhoneCallOriginManagerStatics2'
    _iid_ = Guid('{8bf3ee3f-40f4-4380-8c7c-aea2c9b8dd7a}')
    @winrt_commethod(6)
    def RequestSetAsActiveCallOriginAppAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IPhoneCallOriginManagerStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Provider.IPhoneCallOriginManagerStatics3'
    _iid_ = Guid('{2ed69764-a6e3-50f0-b76a-d67cb39bdfde}')
    @winrt_commethod(6)
    def get_IsSupported(self) -> Boolean: ...
    IsSupported = property(get_IsSupported, None)
class PhoneCallOrigin(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin
    _classid_ = 'Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin: ...
    @winrt_mixinmethod
    def get_Category(self: win32more.Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Category(self: win32more.Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CategoryDescription(self: win32more.Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CategoryDescription(self: win32more.Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Location(self: win32more.Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayPicture(self: win32more.Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin3) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def put_DisplayPicture(self: win32more.Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin3, value: win32more.Windows.Storage.StorageFile) -> Void: ...
    Category = property(get_Category, put_Category)
    CategoryDescription = property(get_CategoryDescription, put_CategoryDescription)
    Location = property(get_Location, put_Location)
    DisplayName = property(get_DisplayName, put_DisplayName)
    DisplayPicture = property(get_DisplayPicture, put_DisplayPicture)
class _PhoneCallOriginManager_Meta_(ComPtr.__class__):
    pass
class PhoneCallOriginManager(ComPtr, metaclass=_PhoneCallOriginManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Provider.PhoneCallOriginManager'
    @winrt_classmethod
    def get_IsSupported(cls: win32more.Windows.ApplicationModel.Calls.Provider.IPhoneCallOriginManagerStatics3) -> Boolean: ...
    @winrt_classmethod
    def RequestSetAsActiveCallOriginAppAsync(cls: win32more.Windows.ApplicationModel.Calls.Provider.IPhoneCallOriginManagerStatics2) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def get_IsCurrentAppActiveCallOriginApp(cls: win32more.Windows.ApplicationModel.Calls.Provider.IPhoneCallOriginManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def ShowPhoneCallOriginSettingsUI(cls: win32more.Windows.ApplicationModel.Calls.Provider.IPhoneCallOriginManagerStatics) -> Void: ...
    @winrt_classmethod
    def SetCallOrigin(cls: win32more.Windows.ApplicationModel.Calls.Provider.IPhoneCallOriginManagerStatics, requestId: Guid, callOrigin: win32more.Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin) -> Void: ...
    _PhoneCallOriginManager_Meta_.IsSupported = property(get_IsSupported.__wrapped__, None)
    _PhoneCallOriginManager_Meta_.IsCurrentAppActiveCallOriginApp = property(get_IsCurrentAppActiveCallOriginApp.__wrapped__, None)


make_ready(__name__)
