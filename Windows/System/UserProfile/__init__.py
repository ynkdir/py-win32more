from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Globalization
import Windows.Storage
import Windows.Storage.Streams
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
AccountPictureKind = Int32
AccountPictureKind_SmallImage: AccountPictureKind = 0
AccountPictureKind_LargeImage: AccountPictureKind = 1
AccountPictureKind_Video: AccountPictureKind = 2
class _AdvertisingManager_Meta_(ComPtr.__class__):
    pass
class AdvertisingManager(ComPtr, metaclass=_AdvertisingManager_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.AdvertisingManager'
    @winrt_classmethod
    def GetForUser(cls: Windows.System.UserProfile.IAdvertisingManagerStatics2, user: Windows.System.User) -> Windows.System.UserProfile.AdvertisingManagerForUser: ...
    @winrt_classmethod
    def get_AdvertisingId(cls: Windows.System.UserProfile.IAdvertisingManagerStatics) -> WinRT_String: ...
    _AdvertisingManager_Meta_.AdvertisingId = property(get_AdvertisingId.__wrapped__, None)
class AdvertisingManagerForUser(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.System.UserProfile.IAdvertisingManagerForUser
    _classid_ = 'Windows.System.UserProfile.AdvertisingManagerForUser'
    @winrt_mixinmethod
    def get_AdvertisingId(self: Windows.System.UserProfile.IAdvertisingManagerForUser) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_User(self: Windows.System.UserProfile.IAdvertisingManagerForUser) -> Windows.System.User: ...
    AdvertisingId = property(get_AdvertisingId, None)
    User = property(get_User, None)
class AssignedAccessSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.System.UserProfile.IAssignedAccessSettings
    _classid_ = 'Windows.System.UserProfile.AssignedAccessSettings'
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
class DiagnosticsSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.System.UserProfile.IDiagnosticsSettings
    _classid_ = 'Windows.System.UserProfile.DiagnosticsSettings'
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
class FirstSignInSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.System.UserProfile.IFirstSignInSettings
    _classid_ = 'Windows.System.UserProfile.FirstSignInSettings'
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
class _GlobalizationPreferences_Meta_(ComPtr.__class__):
    pass
class GlobalizationPreferences(ComPtr, metaclass=_GlobalizationPreferences_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.GlobalizationPreferences'
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
    _GlobalizationPreferences_Meta_.Calendars = property(get_Calendars.__wrapped__, None)
    _GlobalizationPreferences_Meta_.Clocks = property(get_Clocks.__wrapped__, None)
    _GlobalizationPreferences_Meta_.Currencies = property(get_Currencies.__wrapped__, None)
    _GlobalizationPreferences_Meta_.Languages = property(get_Languages.__wrapped__, None)
    _GlobalizationPreferences_Meta_.HomeGeographicRegion = property(get_HomeGeographicRegion.__wrapped__, None)
    _GlobalizationPreferences_Meta_.WeekStartsOn = property(get_WeekStartsOn.__wrapped__, None)
class GlobalizationPreferencesForUser(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.System.UserProfile.IGlobalizationPreferencesForUser
    _classid_ = 'Windows.System.UserProfile.GlobalizationPreferencesForUser'
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
class IAdvertisingManagerForUser(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IAdvertisingManagerForUser'
    _iid_ = Guid('{928bf3d0-cf7c-4ab0-a7dc-6dc5bcd44252}')
    @winrt_commethod(6)
    def get_AdvertisingId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_User(self) -> Windows.System.User: ...
    AdvertisingId = property(get_AdvertisingId, None)
    User = property(get_User, None)
class IAdvertisingManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IAdvertisingManagerStatics'
    _iid_ = Guid('{add3468c-a273-48cb-b346-3544522d5581}')
    @winrt_commethod(6)
    def get_AdvertisingId(self) -> WinRT_String: ...
    AdvertisingId = property(get_AdvertisingId, None)
class IAdvertisingManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IAdvertisingManagerStatics2'
    _iid_ = Guid('{dd0947af-1a6d-46b0-95bc-f3f9d6beb9fb}')
    @winrt_commethod(6)
    def GetForUser(self, user: Windows.System.User) -> Windows.System.UserProfile.AdvertisingManagerForUser: ...
class IAssignedAccessSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IAssignedAccessSettings'
    _iid_ = Guid('{1bc57f1c-e971-5757-b8e0-512f8b8c46d2}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsSingleAppKioskMode(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_User(self) -> Windows.System.User: ...
    IsEnabled = property(get_IsEnabled, None)
    IsSingleAppKioskMode = property(get_IsSingleAppKioskMode, None)
    User = property(get_User, None)
class IAssignedAccessSettingsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IAssignedAccessSettingsStatics'
    _iid_ = Guid('{34a81d0d-8a29-5ef3-a7be-618e6ac3bd01}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.System.UserProfile.AssignedAccessSettings: ...
    @winrt_commethod(7)
    def GetForUser(self, user: Windows.System.User) -> Windows.System.UserProfile.AssignedAccessSettings: ...
class IDiagnosticsSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IDiagnosticsSettings'
    _iid_ = Guid('{e5e9eccd-2711-44e0-973c-491d78048d24}')
    @winrt_commethod(6)
    def get_CanUseDiagnosticsToTailorExperiences(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_User(self) -> Windows.System.User: ...
    CanUseDiagnosticsToTailorExperiences = property(get_CanUseDiagnosticsToTailorExperiences, None)
    User = property(get_User, None)
class IDiagnosticsSettingsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IDiagnosticsSettingsStatics'
    _iid_ = Guid('{72d2e80f-5390-4793-990b-3ccc7d6ac9c8}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.System.UserProfile.DiagnosticsSettings: ...
    @winrt_commethod(7)
    def GetForUser(self, user: Windows.System.User) -> Windows.System.UserProfile.DiagnosticsSettings: ...
class IFirstSignInSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IFirstSignInSettings'
    _iid_ = Guid('{3e945153-3a5e-452e-a601-f5baad2a4870}')
class IFirstSignInSettingsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IFirstSignInSettingsStatics'
    _iid_ = Guid('{1ce18f0f-1c41-4ea0-b7a2-6f0c1c7e8438}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.System.UserProfile.FirstSignInSettings: ...
class IGlobalizationPreferencesForUser(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IGlobalizationPreferencesForUser'
    _iid_ = Guid('{150f0795-4f6e-40ba-a010-e27d81bda7f5}')
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
class IGlobalizationPreferencesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IGlobalizationPreferencesStatics'
    _iid_ = Guid('{01bf4326-ed37-4e96-b0e9-c1340d1ea158}')
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
class IGlobalizationPreferencesStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IGlobalizationPreferencesStatics2'
    _iid_ = Guid('{fcce85f1-4300-4cd0-9cac-1a8e7b7e18f4}')
    @winrt_commethod(6)
    def TrySetHomeGeographicRegion(self, region: WinRT_String) -> Boolean: ...
    @winrt_commethod(7)
    def TrySetLanguages(self, languageTags: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Boolean: ...
class IGlobalizationPreferencesStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IGlobalizationPreferencesStatics3'
    _iid_ = Guid('{1e059733-35f5-40d8-b9e8-aef3ef856fce}')
    @winrt_commethod(6)
    def GetForUser(self, user: Windows.System.User) -> Windows.System.UserProfile.GlobalizationPreferencesForUser: ...
class ILockScreenImageFeedStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.ILockScreenImageFeedStatics'
    _iid_ = Guid('{2c0d73f6-03a9-41a6-9b01-495251ff51d5}')
    @winrt_commethod(6)
    def RequestSetImageFeedAsync(self, syndicationFeedUri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.System.UserProfile.SetImageFeedResult]: ...
    @winrt_commethod(7)
    def TryRemoveImageFeed(self) -> Boolean: ...
class ILockScreenStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.ILockScreenStatics'
    _iid_ = Guid('{3ee9d3ad-b607-40ae-b426-7631d9821269}')
    @winrt_commethod(6)
    def get_OriginalImageFile(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def GetImageStream(self) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(8)
    def SetImageFileAsync(self, value: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def SetImageStreamAsync(self, value: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncAction: ...
    OriginalImageFile = property(get_OriginalImageFile, None)
class IUserInformationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IUserInformationStatics'
    _iid_ = Guid('{77f3a910-48fa-489c-934e-2ae85ba8f772}')
    @winrt_commethod(6)
    def get_AccountPictureChangeEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_NameAccessAllowed(self) -> Boolean: ...
    @winrt_commethod(8)
    def GetAccountPicture(self, kind: Windows.System.UserProfile.AccountPictureKind) -> Windows.Storage.IStorageFile: ...
    @winrt_commethod(9)
    def SetAccountPictureAsync(self, image: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.System.UserProfile.SetAccountPictureResult]: ...
    @winrt_commethod(10)
    def SetAccountPicturesAsync(self, smallImage: Windows.Storage.IStorageFile, largeImage: Windows.Storage.IStorageFile, video: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.System.UserProfile.SetAccountPictureResult]: ...
    @winrt_commethod(11)
    def SetAccountPictureFromStreamAsync(self, image: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncOperation[Windows.System.UserProfile.SetAccountPictureResult]: ...
    @winrt_commethod(12)
    def SetAccountPicturesFromStreamsAsync(self, smallImage: Windows.Storage.Streams.IRandomAccessStream, largeImage: Windows.Storage.Streams.IRandomAccessStream, video: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncOperation[Windows.System.UserProfile.SetAccountPictureResult]: ...
    @winrt_commethod(13)
    def add_AccountPictureChanged(self, changeHandler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_AccountPictureChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def GetDisplayNameAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(16)
    def GetFirstNameAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(17)
    def GetLastNameAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(18)
    def GetPrincipalNameAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(19)
    def GetSessionInitiationProtocolUriAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Uri]: ...
    @winrt_commethod(20)
    def GetDomainNameAsync(self) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    AccountPictureChangeEnabled = property(get_AccountPictureChangeEnabled, None)
    NameAccessAllowed = property(get_NameAccessAllowed, None)
class IUserProfilePersonalizationSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IUserProfilePersonalizationSettings'
    _iid_ = Guid('{8ceddab4-7998-46d5-8dd3-184f1c5f9ab9}')
    @winrt_commethod(6)
    def TrySetLockScreenImageAsync(self, imageFile: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def TrySetWallpaperImageAsync(self, imageFile: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IUserProfilePersonalizationSettingsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IUserProfilePersonalizationSettingsStatics'
    _iid_ = Guid('{91acb841-5037-454b-9883-bb772d08dd16}')
    @winrt_commethod(6)
    def get_Current(self) -> Windows.System.UserProfile.UserProfilePersonalizationSettings: ...
    @winrt_commethod(7)
    def IsSupported(self) -> Boolean: ...
    Current = property(get_Current, None)
class _LockScreen_Meta_(ComPtr.__class__):
    pass
class LockScreen(ComPtr, metaclass=_LockScreen_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.LockScreen'
    @winrt_classmethod
    def RequestSetImageFeedAsync(cls: Windows.System.UserProfile.ILockScreenImageFeedStatics, syndicationFeedUri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.System.UserProfile.SetImageFeedResult]: ...
    @winrt_classmethod
    def TryRemoveImageFeed(cls: Windows.System.UserProfile.ILockScreenImageFeedStatics) -> Boolean: ...
    @winrt_classmethod
    def get_OriginalImageFile(cls: Windows.System.UserProfile.ILockScreenStatics) -> Windows.Foundation.Uri: ...
    @winrt_classmethod
    def GetImageStream(cls: Windows.System.UserProfile.ILockScreenStatics) -> Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_classmethod
    def SetImageFileAsync(cls: Windows.System.UserProfile.ILockScreenStatics, value: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def SetImageStreamAsync(cls: Windows.System.UserProfile.ILockScreenStatics, value: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncAction: ...
    _LockScreen_Meta_.OriginalImageFile = property(get_OriginalImageFile.__wrapped__, None)
SetAccountPictureResult = Int32
SetAccountPictureResult_Success: SetAccountPictureResult = 0
SetAccountPictureResult_ChangeDisabled: SetAccountPictureResult = 1
SetAccountPictureResult_LargeOrDynamicError: SetAccountPictureResult = 2
SetAccountPictureResult_VideoFrameSizeError: SetAccountPictureResult = 3
SetAccountPictureResult_FileSizeError: SetAccountPictureResult = 4
SetAccountPictureResult_Failure: SetAccountPictureResult = 5
SetImageFeedResult = Int32
SetImageFeedResult_Success: SetImageFeedResult = 0
SetImageFeedResult_ChangeDisabled: SetImageFeedResult = 1
SetImageFeedResult_UserCanceled: SetImageFeedResult = 2
class _UserInformation_Meta_(ComPtr.__class__):
    pass
class UserInformation(ComPtr, metaclass=_UserInformation_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.UserInformation'
    @winrt_classmethod
    def get_AccountPictureChangeEnabled(cls: Windows.System.UserProfile.IUserInformationStatics) -> Boolean: ...
    @winrt_classmethod
    def get_NameAccessAllowed(cls: Windows.System.UserProfile.IUserInformationStatics) -> Boolean: ...
    @winrt_classmethod
    def GetAccountPicture(cls: Windows.System.UserProfile.IUserInformationStatics, kind: Windows.System.UserProfile.AccountPictureKind) -> Windows.Storage.IStorageFile: ...
    @winrt_classmethod
    def SetAccountPictureAsync(cls: Windows.System.UserProfile.IUserInformationStatics, image: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.System.UserProfile.SetAccountPictureResult]: ...
    @winrt_classmethod
    def SetAccountPicturesAsync(cls: Windows.System.UserProfile.IUserInformationStatics, smallImage: Windows.Storage.IStorageFile, largeImage: Windows.Storage.IStorageFile, video: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.System.UserProfile.SetAccountPictureResult]: ...
    @winrt_classmethod
    def SetAccountPictureFromStreamAsync(cls: Windows.System.UserProfile.IUserInformationStatics, image: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncOperation[Windows.System.UserProfile.SetAccountPictureResult]: ...
    @winrt_classmethod
    def SetAccountPicturesFromStreamsAsync(cls: Windows.System.UserProfile.IUserInformationStatics, smallImage: Windows.Storage.Streams.IRandomAccessStream, largeImage: Windows.Storage.Streams.IRandomAccessStream, video: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncOperation[Windows.System.UserProfile.SetAccountPictureResult]: ...
    @winrt_classmethod
    def add_AccountPictureChanged(cls: Windows.System.UserProfile.IUserInformationStatics, changeHandler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_AccountPictureChanged(cls: Windows.System.UserProfile.IUserInformationStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDisplayNameAsync(cls: Windows.System.UserProfile.IUserInformationStatics) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetFirstNameAsync(cls: Windows.System.UserProfile.IUserInformationStatics) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetLastNameAsync(cls: Windows.System.UserProfile.IUserInformationStatics) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetPrincipalNameAsync(cls: Windows.System.UserProfile.IUserInformationStatics) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetSessionInitiationProtocolUriAsync(cls: Windows.System.UserProfile.IUserInformationStatics) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Uri]: ...
    @winrt_classmethod
    def GetDomainNameAsync(cls: Windows.System.UserProfile.IUserInformationStatics) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    _UserInformation_Meta_.AccountPictureChangeEnabled = property(get_AccountPictureChangeEnabled.__wrapped__, None)
    _UserInformation_Meta_.NameAccessAllowed = property(get_NameAccessAllowed.__wrapped__, None)
UserProfileContract: UInt32 = 131072
UserProfileLockScreenContract: UInt32 = 65536
class _UserProfilePersonalizationSettings_Meta_(ComPtr.__class__):
    pass
class UserProfilePersonalizationSettings(ComPtr, metaclass=_UserProfilePersonalizationSettings_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.System.UserProfile.IUserProfilePersonalizationSettings
    _classid_ = 'Windows.System.UserProfile.UserProfilePersonalizationSettings'
    @winrt_mixinmethod
    def TrySetLockScreenImageAsync(self: Windows.System.UserProfile.IUserProfilePersonalizationSettings, imageFile: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySetWallpaperImageAsync(self: Windows.System.UserProfile.IUserProfilePersonalizationSettings, imageFile: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def get_Current(cls: Windows.System.UserProfile.IUserProfilePersonalizationSettingsStatics) -> Windows.System.UserProfile.UserProfilePersonalizationSettings: ...
    @winrt_classmethod
    def IsSupported(cls: Windows.System.UserProfile.IUserProfilePersonalizationSettingsStatics) -> Boolean: ...
    _UserProfilePersonalizationSettings_Meta_.Current = property(get_Current.__wrapped__, None)
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
make_head(_module, 'ILockScreenImageFeedStatics')
make_head(_module, 'ILockScreenStatics')
make_head(_module, 'IUserInformationStatics')
make_head(_module, 'IUserProfilePersonalizationSettings')
make_head(_module, 'IUserProfilePersonalizationSettingsStatics')
make_head(_module, 'LockScreen')
make_head(_module, 'UserInformation')
make_head(_module, 'UserProfilePersonalizationSettings')
