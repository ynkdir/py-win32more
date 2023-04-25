from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Globalization
import Windows.Storage
import Windows.System
import Windows.System.UserProfile
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AdvertisingManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.UserProfile.AdvertisingManager'
    @winrt_classmethod
    def GetForUser(cls: Windows.System.UserProfile.IAdvertisingManagerStatics2, user: Windows.System.User) -> Windows.System.UserProfile.AdvertisingManagerForUser: ...
    @winrt_classmethod
    def get_AdvertisingId(cls: Windows.System.UserProfile.IAdvertisingManagerStatics) -> WinRT_String: ...
    AdvertisingId = property(get_AdvertisingId, None)
class AdvertisingManagerForUser(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.UserProfile.AdvertisingManagerForUser'
    @winrt_mixinmethod
    def get_AdvertisingId(self: Windows.System.UserProfile.IAdvertisingManagerForUser) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_User(self: Windows.System.UserProfile.IAdvertisingManagerForUser) -> Windows.System.User: ...
    AdvertisingId = property(get_AdvertisingId, None)
    User = property(get_User, None)
class AssignedAccessSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.UserProfile.AssignedAccessSettings'
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.System.UserProfile.IAssignedAccessSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSingleAppKioskMode(self: Windows.System.UserProfile.IAssignedAccessSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_User(self: Windows.System.UserProfile.IAssignedAccessSettings) -> Windows.System.User: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.System.UserProfile.IAssignedAccessSettingsStatics) -> Windows.System.UserProfile.AssignedAccessSettings: ...
    @winrt_classmethod
    def GetForUser(cls: Windows.System.UserProfile.IAssignedAccessSettingsStatics, user: Windows.System.User) -> Windows.System.UserProfile.AssignedAccessSettings: ...
    IsEnabled = property(get_IsEnabled, None)
    IsSingleAppKioskMode = property(get_IsSingleAppKioskMode, None)
    User = property(get_User, None)
class DiagnosticsSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.UserProfile.DiagnosticsSettings'
    @winrt_mixinmethod
    def get_CanUseDiagnosticsToTailorExperiences(self: Windows.System.UserProfile.IDiagnosticsSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_User(self: Windows.System.UserProfile.IDiagnosticsSettings) -> Windows.System.User: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.System.UserProfile.IDiagnosticsSettingsStatics) -> Windows.System.UserProfile.DiagnosticsSettings: ...
    @winrt_classmethod
    def GetForUser(cls: Windows.System.UserProfile.IDiagnosticsSettingsStatics, user: Windows.System.User) -> Windows.System.UserProfile.DiagnosticsSettings: ...
    CanUseDiagnosticsToTailorExperiences = property(get_CanUseDiagnosticsToTailorExperiences, None)
    User = property(get_User, None)
class FirstSignInSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.UserProfile.FirstSignInSettings'
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Split(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], first: POINTER(Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]), second: POINTER(Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head])) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.System.UserProfile.IFirstSignInSettingsStatics) -> Windows.System.UserProfile.FirstSignInSettings: ...
    Size = property(get_Size, None)
class GlobalizationPreferences(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.UserProfile.GlobalizationPreferences'
    @winrt_classmethod
    def GetForUser(cls: Windows.System.UserProfile.IGlobalizationPreferencesStatics3, user: Windows.System.User) -> Windows.System.UserProfile.GlobalizationPreferencesForUser: ...
    @winrt_classmethod
    def TrySetHomeGeographicRegion(cls: Windows.System.UserProfile.IGlobalizationPreferencesStatics2, region: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def TrySetLanguages(cls: Windows.System.UserProfile.IGlobalizationPreferencesStatics2, languageTags: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Boolean: ...
    @winrt_classmethod
    def get_Calendars(cls: Windows.System.UserProfile.IGlobalizationPreferencesStatics) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def get_Clocks(cls: Windows.System.UserProfile.IGlobalizationPreferencesStatics) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def get_Currencies(cls: Windows.System.UserProfile.IGlobalizationPreferencesStatics) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def get_Languages(cls: Windows.System.UserProfile.IGlobalizationPreferencesStatics) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def get_HomeGeographicRegion(cls: Windows.System.UserProfile.IGlobalizationPreferencesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_WeekStartsOn(cls: Windows.System.UserProfile.IGlobalizationPreferencesStatics) -> Windows.Globalization.DayOfWeek: ...
    Calendars = property(get_Calendars, None)
    Clocks = property(get_Clocks, None)
    Currencies = property(get_Currencies, None)
    Languages = property(get_Languages, None)
    HomeGeographicRegion = property(get_HomeGeographicRegion, None)
    WeekStartsOn = property(get_WeekStartsOn, None)
class GlobalizationPreferencesForUser(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.UserProfile.GlobalizationPreferencesForUser'
    @winrt_mixinmethod
    def get_User(self: Windows.System.UserProfile.IGlobalizationPreferencesForUser) -> Windows.System.User: ...
    @winrt_mixinmethod
    def get_Calendars(self: Windows.System.UserProfile.IGlobalizationPreferencesForUser) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Clocks(self: Windows.System.UserProfile.IGlobalizationPreferencesForUser) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Currencies(self: Windows.System.UserProfile.IGlobalizationPreferencesForUser) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Languages(self: Windows.System.UserProfile.IGlobalizationPreferencesForUser) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_HomeGeographicRegion(self: Windows.System.UserProfile.IGlobalizationPreferencesForUser) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WeekStartsOn(self: Windows.System.UserProfile.IGlobalizationPreferencesForUser) -> Windows.Globalization.DayOfWeek: ...
    User = property(get_User, None)
    Calendars = property(get_Calendars, None)
    Clocks = property(get_Clocks, None)
    Currencies = property(get_Currencies, None)
    Languages = property(get_Languages, None)
    HomeGeographicRegion = property(get_HomeGeographicRegion, None)
    WeekStartsOn = property(get_WeekStartsOn, None)
class IAdvertisingManagerForUser(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('928bf3d0-cf7c-4ab0-a7-dc-6d-c5-bc-d4-42-52')
    @winrt_commethod(6)
    def get_AdvertisingId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_User(self) -> Windows.System.User: ...
    AdvertisingId = property(get_AdvertisingId, None)
    User = property(get_User, None)
class IAdvertisingManagerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('add3468c-a273-48cb-b3-46-35-44-52-2d-55-81')
    @winrt_commethod(6)
    def get_AdvertisingId(self) -> WinRT_String: ...
    AdvertisingId = property(get_AdvertisingId, None)
class IAdvertisingManagerStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('dd0947af-1a6d-46b0-95-bc-f3-f9-d6-be-b9-fb')
    @winrt_commethod(6)
    def GetForUser(self, user: Windows.System.User) -> Windows.System.UserProfile.AdvertisingManagerForUser: ...
class IAssignedAccessSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1bc57f1c-e971-5757-b8-e0-51-2f-8b-8c-46-d2')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsSingleAppKioskMode(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_User(self) -> Windows.System.User: ...
    IsEnabled = property(get_IsEnabled, None)
    IsSingleAppKioskMode = property(get_IsSingleAppKioskMode, None)
    User = property(get_User, None)
class IAssignedAccessSettingsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('34a81d0d-8a29-5ef3-a7-be-61-8e-6a-c3-bd-01')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.System.UserProfile.AssignedAccessSettings: ...
    @winrt_commethod(7)
    def GetForUser(self, user: Windows.System.User) -> Windows.System.UserProfile.AssignedAccessSettings: ...
class IDiagnosticsSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e5e9eccd-2711-44e0-97-3c-49-1d-78-04-8d-24')
    @winrt_commethod(6)
    def get_CanUseDiagnosticsToTailorExperiences(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_User(self) -> Windows.System.User: ...
    CanUseDiagnosticsToTailorExperiences = property(get_CanUseDiagnosticsToTailorExperiences, None)
    User = property(get_User, None)
class IDiagnosticsSettingsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('72d2e80f-5390-4793-99-0b-3c-cc-7d-6a-c9-c8')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.System.UserProfile.DiagnosticsSettings: ...
    @winrt_commethod(7)
    def GetForUser(self, user: Windows.System.User) -> Windows.System.UserProfile.DiagnosticsSettings: ...
class IFirstSignInSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3e945153-3a5e-452e-a6-01-f5-ba-ad-2a-48-70')
class IFirstSignInSettingsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1ce18f0f-1c41-4ea0-b7-a2-6f-0c-1c-7e-84-38')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.System.UserProfile.FirstSignInSettings: ...
class IGlobalizationPreferencesForUser(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('150f0795-4f6e-40ba-a0-10-e2-7d-81-bd-a7-f5')
    @winrt_commethod(6)
    def get_User(self) -> Windows.System.User: ...
    @winrt_commethod(7)
    def get_Calendars(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def get_Clocks(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(9)
    def get_Currencies(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def get_Languages(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(11)
    def get_HomeGeographicRegion(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_WeekStartsOn(self) -> Windows.Globalization.DayOfWeek: ...
    User = property(get_User, None)
    Calendars = property(get_Calendars, None)
    Clocks = property(get_Clocks, None)
    Currencies = property(get_Currencies, None)
    Languages = property(get_Languages, None)
    HomeGeographicRegion = property(get_HomeGeographicRegion, None)
    WeekStartsOn = property(get_WeekStartsOn, None)
class IGlobalizationPreferencesStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('01bf4326-ed37-4e96-b0-e9-c1-34-0d-1e-a1-58')
    @winrt_commethod(6)
    def get_Calendars(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def get_Clocks(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def get_Currencies(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(9)
    def get_Languages(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def get_HomeGeographicRegion(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_WeekStartsOn(self) -> Windows.Globalization.DayOfWeek: ...
    Calendars = property(get_Calendars, None)
    Clocks = property(get_Clocks, None)
    Currencies = property(get_Currencies, None)
    Languages = property(get_Languages, None)
    HomeGeographicRegion = property(get_HomeGeographicRegion, None)
    WeekStartsOn = property(get_WeekStartsOn, None)
class IGlobalizationPreferencesStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fcce85f1-4300-4cd0-9c-ac-1a-8e-7b-7e-18-f4')
    @winrt_commethod(6)
    def TrySetHomeGeographicRegion(self, region: WinRT_String) -> Boolean: ...
    @winrt_commethod(7)
    def TrySetLanguages(self, languageTags: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Boolean: ...
class IGlobalizationPreferencesStatics3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1e059733-35f5-40d8-b9-e8-ae-f3-ef-85-6f-ce')
    @winrt_commethod(6)
    def GetForUser(self, user: Windows.System.User) -> Windows.System.UserProfile.GlobalizationPreferencesForUser: ...
class IUserProfilePersonalizationSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8ceddab4-7998-46d5-8d-d3-18-4f-1c-5f-9a-b9')
    @winrt_commethod(6)
    def TrySetLockScreenImageAsync(self, imageFile: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def TrySetWallpaperImageAsync(self, imageFile: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IUserProfilePersonalizationSettingsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('91acb841-5037-454b-98-83-bb-77-2d-08-dd-16')
    @winrt_commethod(6)
    def get_Current(self) -> Windows.System.UserProfile.UserProfilePersonalizationSettings: ...
    @winrt_commethod(7)
    def IsSupported(self) -> Boolean: ...
    Current = property(get_Current, None)
class UserProfilePersonalizationSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.UserProfile.UserProfilePersonalizationSettings'
    @winrt_mixinmethod
    def TrySetLockScreenImageAsync(self: Windows.System.UserProfile.IUserProfilePersonalizationSettings, imageFile: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySetWallpaperImageAsync(self: Windows.System.UserProfile.IUserProfilePersonalizationSettings, imageFile: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def get_Current(cls: Windows.System.UserProfile.IUserProfilePersonalizationSettingsStatics) -> Windows.System.UserProfile.UserProfilePersonalizationSettings: ...
    @winrt_classmethod
    def IsSupported(cls: Windows.System.UserProfile.IUserProfilePersonalizationSettingsStatics) -> Boolean: ...
    Current = property(get_Current, None)
make_head(_module, 'AdvertisingManager')
make_head(_module, 'AdvertisingManagerForUser')
make_head(_module, 'AssignedAccessSettings')
make_head(_module, 'DiagnosticsSettings')
make_head(_module, 'FirstSignInSettings')
make_head(_module, 'GlobalizationPreferences')
make_head(_module, 'GlobalizationPreferencesForUser')
make_head(_module, 'IAdvertisingManagerForUser')
make_head(_module, 'IAdvertisingManagerStatics')
make_head(_module, 'IAdvertisingManagerStatics2')
make_head(_module, 'IAssignedAccessSettings')
make_head(_module, 'IAssignedAccessSettingsStatics')
make_head(_module, 'IDiagnosticsSettings')
make_head(_module, 'IDiagnosticsSettingsStatics')
make_head(_module, 'IFirstSignInSettings')
make_head(_module, 'IFirstSignInSettingsStatics')
make_head(_module, 'IGlobalizationPreferencesForUser')
make_head(_module, 'IGlobalizationPreferencesStatics')
make_head(_module, 'IGlobalizationPreferencesStatics2')
make_head(_module, 'IGlobalizationPreferencesStatics3')
make_head(_module, 'IUserProfilePersonalizationSettings')
make_head(_module, 'IUserProfilePersonalizationSettingsStatics')
make_head(_module, 'UserProfilePersonalizationSettings')
