from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Globalization
import win32more.Windows.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.System.UserProfile
import win32more.Windows.Win32.System.WinRT
class AccountPictureKind(Enum, Int32):
    SmallImage = 0
    LargeImage = 1
    Video = 2
class _AdvertisingManager_Meta_(ComPtr.__class__):
    pass
class AdvertisingManager(ComPtr, metaclass=_AdvertisingManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.AdvertisingManager'
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.System.UserProfile.IAdvertisingManagerStatics2, user: win32more.Windows.System.User) -> win32more.Windows.System.UserProfile.AdvertisingManagerForUser: ...
    @winrt_classmethod
    def get_AdvertisingId(cls: win32more.Windows.System.UserProfile.IAdvertisingManagerStatics) -> WinRT_String: ...
    _AdvertisingManager_Meta_.AdvertisingId = property(get_AdvertisingId, None)
class AdvertisingManagerForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.UserProfile.IAdvertisingManagerForUser
    _classid_ = 'Windows.System.UserProfile.AdvertisingManagerForUser'
    @winrt_mixinmethod
    def get_AdvertisingId(self: win32more.Windows.System.UserProfile.IAdvertisingManagerForUser) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.System.UserProfile.IAdvertisingManagerForUser) -> win32more.Windows.System.User: ...
    AdvertisingId = property(get_AdvertisingId, None)
    User = property(get_User, None)
class AssignedAccessSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.UserProfile.IAssignedAccessSettings
    _classid_ = 'Windows.System.UserProfile.AssignedAccessSettings'
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.System.UserProfile.IAssignedAccessSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSingleAppKioskMode(self: win32more.Windows.System.UserProfile.IAssignedAccessSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.System.UserProfile.IAssignedAccessSettings) -> win32more.Windows.System.User: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.System.UserProfile.IAssignedAccessSettingsStatics) -> win32more.Windows.System.UserProfile.AssignedAccessSettings: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.System.UserProfile.IAssignedAccessSettingsStatics, user: win32more.Windows.System.User) -> win32more.Windows.System.UserProfile.AssignedAccessSettings: ...
    IsEnabled = property(get_IsEnabled, None)
    IsSingleAppKioskMode = property(get_IsSingleAppKioskMode, None)
    User = property(get_User, None)
class DiagnosticsSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.UserProfile.IDiagnosticsSettings
    _classid_ = 'Windows.System.UserProfile.DiagnosticsSettings'
    @winrt_mixinmethod
    def get_CanUseDiagnosticsToTailorExperiences(self: win32more.Windows.System.UserProfile.IDiagnosticsSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.System.UserProfile.IDiagnosticsSettings) -> win32more.Windows.System.User: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.System.UserProfile.IDiagnosticsSettingsStatics) -> win32more.Windows.System.UserProfile.DiagnosticsSettings: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.System.UserProfile.IDiagnosticsSettingsStatics, user: win32more.Windows.System.User) -> win32more.Windows.System.UserProfile.DiagnosticsSettings: ...
    CanUseDiagnosticsToTailorExperiences = property(get_CanUseDiagnosticsToTailorExperiences, None)
    User = property(get_User, None)
class FirstSignInSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[MappingProtocol[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]
    default_interface: win32more.Windows.System.UserProfile.IFirstSignInSettings
    _classid_ = 'Windows.System.UserProfile.FirstSignInSettings'
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Split(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], first: POINTER(win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]), second: POINTER(win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable])) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.System.UserProfile.IFirstSignInSettingsStatics) -> win32more.Windows.System.UserProfile.FirstSignInSettings: ...
    Size = property(get_Size, None)
class _GlobalizationPreferences_Meta_(ComPtr.__class__):
    pass
class GlobalizationPreferences(ComPtr, metaclass=_GlobalizationPreferences_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.GlobalizationPreferences'
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.System.UserProfile.IGlobalizationPreferencesStatics3, user: win32more.Windows.System.User) -> win32more.Windows.System.UserProfile.GlobalizationPreferencesForUser: ...
    @winrt_classmethod
    def TrySetHomeGeographicRegion(cls: win32more.Windows.System.UserProfile.IGlobalizationPreferencesStatics2, region: WinRT_String) -> Boolean: ...
    @winrt_classmethod
    def TrySetLanguages(cls: win32more.Windows.System.UserProfile.IGlobalizationPreferencesStatics2, languageTags: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Boolean: ...
    @winrt_classmethod
    def get_Calendars(cls: win32more.Windows.System.UserProfile.IGlobalizationPreferencesStatics) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def get_Clocks(cls: win32more.Windows.System.UserProfile.IGlobalizationPreferencesStatics) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def get_Currencies(cls: win32more.Windows.System.UserProfile.IGlobalizationPreferencesStatics) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def get_Languages(cls: win32more.Windows.System.UserProfile.IGlobalizationPreferencesStatics) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def get_HomeGeographicRegion(cls: win32more.Windows.System.UserProfile.IGlobalizationPreferencesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_WeekStartsOn(cls: win32more.Windows.System.UserProfile.IGlobalizationPreferencesStatics) -> win32more.Windows.Globalization.DayOfWeek: ...
    _GlobalizationPreferences_Meta_.Calendars = property(get_Calendars, None)
    _GlobalizationPreferences_Meta_.Clocks = property(get_Clocks, None)
    _GlobalizationPreferences_Meta_.Currencies = property(get_Currencies, None)
    _GlobalizationPreferences_Meta_.HomeGeographicRegion = property(get_HomeGeographicRegion, None)
    _GlobalizationPreferences_Meta_.Languages = property(get_Languages, None)
    _GlobalizationPreferences_Meta_.WeekStartsOn = property(get_WeekStartsOn, None)
class GlobalizationPreferencesForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.UserProfile.IGlobalizationPreferencesForUser
    _classid_ = 'Windows.System.UserProfile.GlobalizationPreferencesForUser'
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.System.UserProfile.IGlobalizationPreferencesForUser) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_Calendars(self: win32more.Windows.System.UserProfile.IGlobalizationPreferencesForUser) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Clocks(self: win32more.Windows.System.UserProfile.IGlobalizationPreferencesForUser) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Currencies(self: win32more.Windows.System.UserProfile.IGlobalizationPreferencesForUser) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Languages(self: win32more.Windows.System.UserProfile.IGlobalizationPreferencesForUser) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_HomeGeographicRegion(self: win32more.Windows.System.UserProfile.IGlobalizationPreferencesForUser) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WeekStartsOn(self: win32more.Windows.System.UserProfile.IGlobalizationPreferencesForUser) -> win32more.Windows.Globalization.DayOfWeek: ...
    Calendars = property(get_Calendars, None)
    Clocks = property(get_Clocks, None)
    Currencies = property(get_Currencies, None)
    HomeGeographicRegion = property(get_HomeGeographicRegion, None)
    Languages = property(get_Languages, None)
    User = property(get_User, None)
    WeekStartsOn = property(get_WeekStartsOn, None)
class IAdvertisingManagerForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IAdvertisingManagerForUser'
    _iid_ = Guid('{928bf3d0-cf7c-4ab0-a7dc-6dc5bcd44252}')
    @winrt_commethod(6)
    def get_AdvertisingId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_User(self) -> win32more.Windows.System.User: ...
    AdvertisingId = property(get_AdvertisingId, None)
    User = property(get_User, None)
class IAdvertisingManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IAdvertisingManagerStatics'
    _iid_ = Guid('{add3468c-a273-48cb-b346-3544522d5581}')
    @winrt_commethod(6)
    def get_AdvertisingId(self) -> WinRT_String: ...
    AdvertisingId = property(get_AdvertisingId, None)
class IAdvertisingManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IAdvertisingManagerStatics2'
    _iid_ = Guid('{dd0947af-1a6d-46b0-95bc-f3f9d6beb9fb}')
    @winrt_commethod(6)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.System.UserProfile.AdvertisingManagerForUser: ...
class IAssignedAccessSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IAssignedAccessSettings'
    _iid_ = Guid('{1bc57f1c-e971-5757-b8e0-512f8b8c46d2}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsSingleAppKioskMode(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_User(self) -> win32more.Windows.System.User: ...
    IsEnabled = property(get_IsEnabled, None)
    IsSingleAppKioskMode = property(get_IsSingleAppKioskMode, None)
    User = property(get_User, None)
class IAssignedAccessSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IAssignedAccessSettingsStatics'
    _iid_ = Guid('{34a81d0d-8a29-5ef3-a7be-618e6ac3bd01}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.System.UserProfile.AssignedAccessSettings: ...
    @winrt_commethod(7)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.System.UserProfile.AssignedAccessSettings: ...
class IDiagnosticsSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IDiagnosticsSettings'
    _iid_ = Guid('{e5e9eccd-2711-44e0-973c-491d78048d24}')
    @winrt_commethod(6)
    def get_CanUseDiagnosticsToTailorExperiences(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_User(self) -> win32more.Windows.System.User: ...
    CanUseDiagnosticsToTailorExperiences = property(get_CanUseDiagnosticsToTailorExperiences, None)
    User = property(get_User, None)
class IDiagnosticsSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IDiagnosticsSettingsStatics'
    _iid_ = Guid('{72d2e80f-5390-4793-990b-3ccc7d6ac9c8}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.System.UserProfile.DiagnosticsSettings: ...
    @winrt_commethod(7)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.System.UserProfile.DiagnosticsSettings: ...
class IFirstSignInSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[MappingProtocol[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]
    _classid_ = 'Windows.System.UserProfile.IFirstSignInSettings'
    _iid_ = Guid('{3e945153-3a5e-452e-a601-f5baad2a4870}')
class IFirstSignInSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IFirstSignInSettingsStatics'
    _iid_ = Guid('{1ce18f0f-1c41-4ea0-b7a2-6f0c1c7e8438}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.System.UserProfile.FirstSignInSettings: ...
class IGlobalizationPreferencesForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IGlobalizationPreferencesForUser'
    _iid_ = Guid('{150f0795-4f6e-40ba-a010-e27d81bda7f5}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    @winrt_commethod(7)
    def get_Calendars(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def get_Clocks(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(9)
    def get_Currencies(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def get_Languages(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(11)
    def get_HomeGeographicRegion(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_WeekStartsOn(self) -> win32more.Windows.Globalization.DayOfWeek: ...
    Calendars = property(get_Calendars, None)
    Clocks = property(get_Clocks, None)
    Currencies = property(get_Currencies, None)
    HomeGeographicRegion = property(get_HomeGeographicRegion, None)
    Languages = property(get_Languages, None)
    User = property(get_User, None)
    WeekStartsOn = property(get_WeekStartsOn, None)
class IGlobalizationPreferencesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IGlobalizationPreferencesStatics'
    _iid_ = Guid('{01bf4326-ed37-4e96-b0e9-c1340d1ea158}')
    @winrt_commethod(6)
    def get_Calendars(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def get_Clocks(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def get_Currencies(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(9)
    def get_Languages(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def get_HomeGeographicRegion(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_WeekStartsOn(self) -> win32more.Windows.Globalization.DayOfWeek: ...
    Calendars = property(get_Calendars, None)
    Clocks = property(get_Clocks, None)
    Currencies = property(get_Currencies, None)
    HomeGeographicRegion = property(get_HomeGeographicRegion, None)
    Languages = property(get_Languages, None)
    WeekStartsOn = property(get_WeekStartsOn, None)
class IGlobalizationPreferencesStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IGlobalizationPreferencesStatics2'
    _iid_ = Guid('{fcce85f1-4300-4cd0-9cac-1a8e7b7e18f4}')
    @winrt_commethod(6)
    def TrySetHomeGeographicRegion(self, region: WinRT_String) -> Boolean: ...
    @winrt_commethod(7)
    def TrySetLanguages(self, languageTags: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> Boolean: ...
class IGlobalizationPreferencesStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IGlobalizationPreferencesStatics3'
    _iid_ = Guid('{1e059733-35f5-40d8-b9e8-aef3ef856fce}')
    @winrt_commethod(6)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.System.UserProfile.GlobalizationPreferencesForUser: ...
class ILockScreenImageFeedStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.ILockScreenImageFeedStatics'
    _iid_ = Guid('{2c0d73f6-03a9-41a6-9b01-495251ff51d5}')
    @winrt_commethod(6)
    def RequestSetImageFeedAsync(self, syndicationFeedUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.UserProfile.SetImageFeedResult]: ...
    @winrt_commethod(7)
    def TryRemoveImageFeed(self) -> Boolean: ...
class ILockScreenStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.ILockScreenStatics'
    _iid_ = Guid('{3ee9d3ad-b607-40ae-b426-7631d9821269}')
    @winrt_commethod(6)
    def get_OriginalImageFile(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def GetImageStream(self) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(8)
    def SetImageFileAsync(self, value: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def SetImageStreamAsync(self, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    OriginalImageFile = property(get_OriginalImageFile, None)
class IUserInformationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IUserInformationStatics'
    _iid_ = Guid('{77f3a910-48fa-489c-934e-2ae85ba8f772}')
    @winrt_commethod(6)
    def get_AccountPictureChangeEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_NameAccessAllowed(self) -> Boolean: ...
    @winrt_commethod(8)
    def GetAccountPicture(self, kind: win32more.Windows.System.UserProfile.AccountPictureKind) -> win32more.Windows.Storage.IStorageFile: ...
    @winrt_commethod(9)
    def SetAccountPictureAsync(self, image: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.UserProfile.SetAccountPictureResult]: ...
    @winrt_commethod(10)
    def SetAccountPicturesAsync(self, smallImage: win32more.Windows.Storage.IStorageFile, largeImage: win32more.Windows.Storage.IStorageFile, video: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.UserProfile.SetAccountPictureResult]: ...
    @winrt_commethod(11)
    def SetAccountPictureFromStreamAsync(self, image: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.UserProfile.SetAccountPictureResult]: ...
    @winrt_commethod(12)
    def SetAccountPicturesFromStreamsAsync(self, smallImage: win32more.Windows.Storage.Streams.IRandomAccessStream, largeImage: win32more.Windows.Storage.Streams.IRandomAccessStream, video: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.UserProfile.SetAccountPictureResult]: ...
    @winrt_commethod(13)
    def add_AccountPictureChanged(self, changeHandler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_AccountPictureChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def GetDisplayNameAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(16)
    def GetFirstNameAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(17)
    def GetLastNameAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(18)
    def GetPrincipalNameAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(19)
    def GetSessionInitiationProtocolUriAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Uri]: ...
    @winrt_commethod(20)
    def GetDomainNameAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    AccountPictureChangeEnabled = property(get_AccountPictureChangeEnabled, None)
    NameAccessAllowed = property(get_NameAccessAllowed, None)
    AccountPictureChanged = event()
class IUserProfilePersonalizationSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IUserProfilePersonalizationSettings'
    _iid_ = Guid('{8ceddab4-7998-46d5-8dd3-184f1c5f9ab9}')
    @winrt_commethod(6)
    def TrySetLockScreenImageAsync(self, imageFile: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def TrySetWallpaperImageAsync(self, imageFile: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IUserProfilePersonalizationSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.IUserProfilePersonalizationSettingsStatics'
    _iid_ = Guid('{91acb841-5037-454b-9883-bb772d08dd16}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.System.UserProfile.UserProfilePersonalizationSettings: ...
    @winrt_commethod(7)
    def IsSupported(self) -> Boolean: ...
    Current = property(get_Current, None)
class _LockScreen_Meta_(ComPtr.__class__):
    pass
class LockScreen(ComPtr, metaclass=_LockScreen_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.LockScreen'
    @winrt_classmethod
    def RequestSetImageFeedAsync(cls: win32more.Windows.System.UserProfile.ILockScreenImageFeedStatics, syndicationFeedUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.UserProfile.SetImageFeedResult]: ...
    @winrt_classmethod
    def TryRemoveImageFeed(cls: win32more.Windows.System.UserProfile.ILockScreenImageFeedStatics) -> Boolean: ...
    @winrt_classmethod
    def get_OriginalImageFile(cls: win32more.Windows.System.UserProfile.ILockScreenStatics) -> win32more.Windows.Foundation.Uri: ...
    @winrt_classmethod
    def GetImageStream(cls: win32more.Windows.System.UserProfile.ILockScreenStatics) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_classmethod
    def SetImageFileAsync(cls: win32more.Windows.System.UserProfile.ILockScreenStatics, value: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def SetImageStreamAsync(cls: win32more.Windows.System.UserProfile.ILockScreenStatics, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    _LockScreen_Meta_.OriginalImageFile = property(get_OriginalImageFile, None)
class SetAccountPictureResult(Enum, Int32):
    Success = 0
    ChangeDisabled = 1
    LargeOrDynamicError = 2
    VideoFrameSizeError = 3
    FileSizeError = 4
    Failure = 5
class SetImageFeedResult(Enum, Int32):
    Success = 0
    ChangeDisabled = 1
    UserCanceled = 2
class _UserInformation_Meta_(ComPtr.__class__):
    pass
class UserInformation(ComPtr, metaclass=_UserInformation_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.UserProfile.UserInformation'
    @winrt_classmethod
    def get_AccountPictureChangeEnabled(cls: win32more.Windows.System.UserProfile.IUserInformationStatics) -> Boolean: ...
    @winrt_classmethod
    def get_NameAccessAllowed(cls: win32more.Windows.System.UserProfile.IUserInformationStatics) -> Boolean: ...
    @winrt_classmethod
    def GetAccountPicture(cls: win32more.Windows.System.UserProfile.IUserInformationStatics, kind: win32more.Windows.System.UserProfile.AccountPictureKind) -> win32more.Windows.Storage.IStorageFile: ...
    @winrt_classmethod
    def SetAccountPictureAsync(cls: win32more.Windows.System.UserProfile.IUserInformationStatics, image: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.UserProfile.SetAccountPictureResult]: ...
    @winrt_classmethod
    def SetAccountPicturesAsync(cls: win32more.Windows.System.UserProfile.IUserInformationStatics, smallImage: win32more.Windows.Storage.IStorageFile, largeImage: win32more.Windows.Storage.IStorageFile, video: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.UserProfile.SetAccountPictureResult]: ...
    @winrt_classmethod
    def SetAccountPictureFromStreamAsync(cls: win32more.Windows.System.UserProfile.IUserInformationStatics, image: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.UserProfile.SetAccountPictureResult]: ...
    @winrt_classmethod
    def SetAccountPicturesFromStreamsAsync(cls: win32more.Windows.System.UserProfile.IUserInformationStatics, smallImage: win32more.Windows.Storage.Streams.IRandomAccessStream, largeImage: win32more.Windows.Storage.Streams.IRandomAccessStream, video: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.System.UserProfile.SetAccountPictureResult]: ...
    @winrt_classmethod
    def add_AccountPictureChanged(cls: win32more.Windows.System.UserProfile.IUserInformationStatics, changeHandler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_AccountPictureChanged(cls: win32more.Windows.System.UserProfile.IUserInformationStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDisplayNameAsync(cls: win32more.Windows.System.UserProfile.IUserInformationStatics) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetFirstNameAsync(cls: win32more.Windows.System.UserProfile.IUserInformationStatics) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetLastNameAsync(cls: win32more.Windows.System.UserProfile.IUserInformationStatics) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetPrincipalNameAsync(cls: win32more.Windows.System.UserProfile.IUserInformationStatics) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_classmethod
    def GetSessionInitiationProtocolUriAsync(cls: win32more.Windows.System.UserProfile.IUserInformationStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Uri]: ...
    @winrt_classmethod
    def GetDomainNameAsync(cls: win32more.Windows.System.UserProfile.IUserInformationStatics) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    _UserInformation_Meta_.AccountPictureChangeEnabled = property(get_AccountPictureChangeEnabled, None)
    _UserInformation_Meta_.NameAccessAllowed = property(get_NameAccessAllowed, None)
UserProfileContract: UInt32 = 131072
UserProfileLockScreenContract: UInt32 = 65536
class _UserProfilePersonalizationSettings_Meta_(ComPtr.__class__):
    pass
class UserProfilePersonalizationSettings(ComPtr, metaclass=_UserProfilePersonalizationSettings_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.UserProfile.IUserProfilePersonalizationSettings
    _classid_ = 'Windows.System.UserProfile.UserProfilePersonalizationSettings'
    @winrt_mixinmethod
    def TrySetLockScreenImageAsync(self: win32more.Windows.System.UserProfile.IUserProfilePersonalizationSettings, imageFile: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySetWallpaperImageAsync(self: win32more.Windows.System.UserProfile.IUserProfilePersonalizationSettings, imageFile: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.System.UserProfile.IUserProfilePersonalizationSettingsStatics) -> win32more.Windows.System.UserProfile.UserProfilePersonalizationSettings: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Windows.System.UserProfile.IUserProfilePersonalizationSettingsStatics) -> Boolean: ...
    _UserProfilePersonalizationSettings_Meta_.Current = property(get_Current, None)


make_ready(__name__)
