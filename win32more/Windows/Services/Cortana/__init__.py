from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.DataTransfer
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Services.Cortana
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
class CortanaActionableInsights(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Cortana.ICortanaActionableInsights
    _classid_ = 'Windows.Services.Cortana.CortanaActionableInsights'
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Services.Cortana.ICortanaActionableInsights) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def IsAvailableAsync(self: win32more.Windows.Services.Cortana.ICortanaActionableInsights) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def ShowInsightsForImageAsync(self: win32more.Windows.Services.Cortana.ICortanaActionableInsights, imageStream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ShowInsightsForImageWithOptionsAsync(self: win32more.Windows.Services.Cortana.ICortanaActionableInsights, imageStream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference, options: win32more.Windows.Services.Cortana.CortanaActionableInsightsOptions) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ShowInsightsForTextAsync(self: win32more.Windows.Services.Cortana.ICortanaActionableInsights, text: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ShowInsightsForTextWithOptionsAsync(self: win32more.Windows.Services.Cortana.ICortanaActionableInsights, text: WinRT_String, options: win32more.Windows.Services.Cortana.CortanaActionableInsightsOptions) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ShowInsightsAsync(self: win32more.Windows.Services.Cortana.ICortanaActionableInsights, datapackage: win32more.Windows.ApplicationModel.DataTransfer.DataPackage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ShowInsightsWithOptionsAsync(self: win32more.Windows.Services.Cortana.ICortanaActionableInsights, datapackage: win32more.Windows.ApplicationModel.DataTransfer.DataPackage, options: win32more.Windows.Services.Cortana.CortanaActionableInsightsOptions) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Services.Cortana.ICortanaActionableInsightsStatics) -> win32more.Windows.Services.Cortana.CortanaActionableInsights: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.Services.Cortana.ICortanaActionableInsightsStatics, user: win32more.Windows.System.User) -> win32more.Windows.Services.Cortana.CortanaActionableInsights: ...
    User = property(get_User, None)
class CortanaActionableInsightsOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Cortana.ICortanaActionableInsightsOptions
    _classid_ = 'Windows.Services.Cortana.CortanaActionableInsightsOptions'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Services.Cortana.CortanaActionableInsightsOptions: ...
    @winrt_mixinmethod
    def get_ContentSourceWebLink(self: win32more.Windows.Services.Cortana.ICortanaActionableInsightsOptions) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_ContentSourceWebLink(self: win32more.Windows.Services.Cortana.ICortanaActionableInsightsOptions, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_SurroundingText(self: win32more.Windows.Services.Cortana.ICortanaActionableInsightsOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SurroundingText(self: win32more.Windows.Services.Cortana.ICortanaActionableInsightsOptions, value: WinRT_String) -> Void: ...
    ContentSourceWebLink = property(get_ContentSourceWebLink, put_ContentSourceWebLink)
    SurroundingText = property(get_SurroundingText, put_SurroundingText)
CortanaPermission = Int32
CortanaPermission_BrowsingHistory: CortanaPermission = 0
CortanaPermission_Calendar: CortanaPermission = 1
CortanaPermission_CallHistory: CortanaPermission = 2
CortanaPermission_Contacts: CortanaPermission = 3
CortanaPermission_Email: CortanaPermission = 4
CortanaPermission_InputPersonalization: CortanaPermission = 5
CortanaPermission_Location: CortanaPermission = 6
CortanaPermission_Messaging: CortanaPermission = 7
CortanaPermission_Microphone: CortanaPermission = 8
CortanaPermission_Personalization: CortanaPermission = 9
CortanaPermission_PhoneCall: CortanaPermission = 10
CortanaPermissionsChangeResult = Int32
CortanaPermissionsChangeResult_Success: CortanaPermissionsChangeResult = 0
CortanaPermissionsChangeResult_Unavailable: CortanaPermissionsChangeResult = 1
CortanaPermissionsChangeResult_DisabledByPolicy: CortanaPermissionsChangeResult = 2
class CortanaPermissionsManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Cortana.ICortanaPermissionsManager
    _classid_ = 'Windows.Services.Cortana.CortanaPermissionsManager'
    @winrt_mixinmethod
    def IsSupported(self: win32more.Windows.Services.Cortana.ICortanaPermissionsManager) -> Boolean: ...
    @winrt_mixinmethod
    def ArePermissionsGrantedAsync(self: win32more.Windows.Services.Cortana.ICortanaPermissionsManager, permissions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Cortana.CortanaPermission]) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def GrantPermissionsAsync(self: win32more.Windows.Services.Cortana.ICortanaPermissionsManager, permissions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Cortana.CortanaPermission]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Cortana.CortanaPermissionsChangeResult]: ...
    @winrt_mixinmethod
    def RevokePermissionsAsync(self: win32more.Windows.Services.Cortana.ICortanaPermissionsManager, permissions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Cortana.CortanaPermission]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Cortana.CortanaPermissionsChangeResult]: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Services.Cortana.ICortanaPermissionsManagerStatics) -> win32more.Windows.Services.Cortana.CortanaPermissionsManager: ...
class CortanaSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Cortana.ICortanaSettings
    _classid_ = 'Windows.Services.Cortana.CortanaSettings'
    @winrt_mixinmethod
    def get_HasUserConsentToVoiceActivation(self: win32more.Windows.Services.Cortana.ICortanaSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsVoiceActivationEnabled(self: win32more.Windows.Services.Cortana.ICortanaSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsVoiceActivationEnabled(self: win32more.Windows.Services.Cortana.ICortanaSettings, value: Boolean) -> Void: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.Services.Cortana.ICortanaSettingsStatics) -> Boolean: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Services.Cortana.ICortanaSettingsStatics) -> win32more.Windows.Services.Cortana.CortanaSettings: ...
    HasUserConsentToVoiceActivation = property(get_HasUserConsentToVoiceActivation, None)
    IsVoiceActivationEnabled = property(get_IsVoiceActivationEnabled, put_IsVoiceActivationEnabled)
class ICortanaActionableInsights(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Cortana.ICortanaActionableInsights'
    _iid_ = Guid('{951ec6b1-fc83-586d-8b84-2452c8981625}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    @winrt_commethod(7)
    def IsAvailableAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def ShowInsightsForImageAsync(self, imageStream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ShowInsightsForImageWithOptionsAsync(self, imageStream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference, options: win32more.Windows.Services.Cortana.CortanaActionableInsightsOptions) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def ShowInsightsForTextAsync(self, text: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def ShowInsightsForTextWithOptionsAsync(self, text: WinRT_String, options: win32more.Windows.Services.Cortana.CortanaActionableInsightsOptions) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def ShowInsightsAsync(self, datapackage: win32more.Windows.ApplicationModel.DataTransfer.DataPackage) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def ShowInsightsWithOptionsAsync(self, datapackage: win32more.Windows.ApplicationModel.DataTransfer.DataPackage, options: win32more.Windows.Services.Cortana.CortanaActionableInsightsOptions) -> win32more.Windows.Foundation.IAsyncAction: ...
    User = property(get_User, None)
class ICortanaActionableInsightsOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Cortana.ICortanaActionableInsightsOptions'
    _iid_ = Guid('{aac2bbcf-9782-5420-b81e-7ae56af31815}')
    @winrt_commethod(6)
    def get_ContentSourceWebLink(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_ContentSourceWebLink(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_SurroundingText(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_SurroundingText(self, value: WinRT_String) -> Void: ...
    ContentSourceWebLink = property(get_ContentSourceWebLink, put_ContentSourceWebLink)
    SurroundingText = property(get_SurroundingText, put_SurroundingText)
class ICortanaActionableInsightsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Cortana.ICortanaActionableInsightsStatics'
    _iid_ = Guid('{b5ded412-9d2f-5cb5-9b05-356a0b836c10}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Services.Cortana.CortanaActionableInsights: ...
    @winrt_commethod(7)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.Services.Cortana.CortanaActionableInsights: ...
class ICortanaPermissionsManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Cortana.ICortanaPermissionsManager'
    _iid_ = Guid('{191330e0-8695-438a-9545-3da4e822ddb4}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def ArePermissionsGrantedAsync(self, permissions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Cortana.CortanaPermission]) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def GrantPermissionsAsync(self, permissions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Cortana.CortanaPermission]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Cortana.CortanaPermissionsChangeResult]: ...
    @winrt_commethod(9)
    def RevokePermissionsAsync(self, permissions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Cortana.CortanaPermission]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Cortana.CortanaPermissionsChangeResult]: ...
class ICortanaPermissionsManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Cortana.ICortanaPermissionsManagerStatics'
    _iid_ = Guid('{76b1e67a-b045-4414-9d6d-2ad3a5fe3a7e}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Services.Cortana.CortanaPermissionsManager: ...
class ICortanaSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Cortana.ICortanaSettings'
    _iid_ = Guid('{54d571a7-8062-40f4-abe7-dedfd697b019}')
    @winrt_commethod(6)
    def get_HasUserConsentToVoiceActivation(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsVoiceActivationEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_IsVoiceActivationEnabled(self, value: Boolean) -> Void: ...
    HasUserConsentToVoiceActivation = property(get_HasUserConsentToVoiceActivation, None)
    IsVoiceActivationEnabled = property(get_IsVoiceActivationEnabled, put_IsVoiceActivationEnabled)
class ICortanaSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Cortana.ICortanaSettingsStatics'
    _iid_ = Guid('{8b2ccd7e-2ec0-446d-9285-33f07ce8ac04}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def GetDefault(self) -> win32more.Windows.Services.Cortana.CortanaSettings: ...
make_head(_module, 'CortanaActionableInsights')
make_head(_module, 'CortanaActionableInsightsOptions')
make_head(_module, 'CortanaPermissionsManager')
make_head(_module, 'CortanaSettings')
make_head(_module, 'ICortanaActionableInsights')
make_head(_module, 'ICortanaActionableInsightsOptions')
make_head(_module, 'ICortanaActionableInsightsStatics')
make_head(_module, 'ICortanaPermissionsManager')
make_head(_module, 'ICortanaPermissionsManagerStatics')
make_head(_module, 'ICortanaSettings')
make_head(_module, 'ICortanaSettingsStatics')
