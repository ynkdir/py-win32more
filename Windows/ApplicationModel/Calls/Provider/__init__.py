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
import Windows.ApplicationModel.Calls.Provider
import Windows.Foundation
import Windows.Storage
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPhoneCallOrigin(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin2'
    _iid_ = Guid('{04c7e980-9ac2-4768-b536-b68da4957d02}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
class IPhoneCallOrigin3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin3'
    _iid_ = Guid('{49330fb4-d1a7-43a2-aeee-c07b6dbaf068}')
    @winrt_commethod(6)
    def get_DisplayPicture(self) -> Windows.Storage.StorageFile: ...
    @winrt_commethod(7)
    def put_DisplayPicture(self, value: Windows.Storage.StorageFile) -> Void: ...
    DisplayPicture = property(get_DisplayPicture, put_DisplayPicture)
class IPhoneCallOriginManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Provider.IPhoneCallOriginManagerStatics'
    _iid_ = Guid('{ccfc5a0a-9af7-6149-39d0-e076fcce1395}')
    @winrt_commethod(6)
    def get_IsCurrentAppActiveCallOriginApp(self) -> Boolean: ...
    @winrt_commethod(7)
    def ShowPhoneCallOriginSettingsUI(self) -> Void: ...
    @winrt_commethod(8)
    def SetCallOrigin(self, requestId: Guid, callOrigin: Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin) -> Void: ...
    IsCurrentAppActiveCallOriginApp = property(get_IsCurrentAppActiveCallOriginApp, None)
class IPhoneCallOriginManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Provider.IPhoneCallOriginManagerStatics2'
    _iid_ = Guid('{8bf3ee3f-40f4-4380-8c7c-aea2c9b8dd7a}')
    @winrt_commethod(6)
    def RequestSetAsActiveCallOriginAppAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IPhoneCallOriginManagerStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Provider.IPhoneCallOriginManagerStatics3'
    _iid_ = Guid('{2ed69764-a6e3-50f0-b76a-d67cb39bdfde}')
    @winrt_commethod(6)
    def get_IsSupported(self) -> Boolean: ...
    IsSupported = property(get_IsSupported, None)
class PhoneCallOrigin(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin
    _classid_ = 'Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin: ...
    @winrt_mixinmethod
    def get_Category(self: Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Category(self: Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CategoryDescription(self: Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CategoryDescription(self: Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Location(self: Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Location(self: Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayPicture(self: Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin3) -> Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def put_DisplayPicture(self: Windows.ApplicationModel.Calls.Provider.IPhoneCallOrigin3, value: Windows.Storage.StorageFile) -> Void: ...
    Category = property(get_Category, put_Category)
    CategoryDescription = property(get_CategoryDescription, put_CategoryDescription)
    Location = property(get_Location, put_Location)
    DisplayName = property(get_DisplayName, put_DisplayName)
    DisplayPicture = property(get_DisplayPicture, put_DisplayPicture)
class PhoneCallOriginManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Calls.Provider.PhoneCallOriginManager'
    @winrt_classmethod
    def get_IsSupported(cls: Windows.ApplicationModel.Calls.Provider.IPhoneCallOriginManagerStatics3) -> Boolean: ...
    @winrt_classmethod
    def RequestSetAsActiveCallOriginAppAsync(cls: Windows.ApplicationModel.Calls.Provider.IPhoneCallOriginManagerStatics2) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def get_IsCurrentAppActiveCallOriginApp(cls: Windows.ApplicationModel.Calls.Provider.IPhoneCallOriginManagerStatics) -> Boolean: ...
    @winrt_classmethod
    def ShowPhoneCallOriginSettingsUI(cls: Windows.ApplicationModel.Calls.Provider.IPhoneCallOriginManagerStatics) -> Void: ...
    @winrt_classmethod
    def SetCallOrigin(cls: Windows.ApplicationModel.Calls.Provider.IPhoneCallOriginManagerStatics, requestId: Guid, callOrigin: Windows.ApplicationModel.Calls.Provider.PhoneCallOrigin) -> Void: ...
    IsSupported = property(get_IsSupported, None)
    IsCurrentAppActiveCallOriginApp = property(get_IsCurrentAppActiveCallOriginApp, None)
make_head(_module, 'IPhoneCallOrigin')
make_head(_module, 'IPhoneCallOrigin2')
make_head(_module, 'IPhoneCallOrigin3')
make_head(_module, 'IPhoneCallOriginManagerStatics')
make_head(_module, 'IPhoneCallOriginManagerStatics2')
make_head(_module, 'IPhoneCallOriginManagerStatics3')
make_head(_module, 'PhoneCallOrigin')
make_head(_module, 'PhoneCallOriginManager')
