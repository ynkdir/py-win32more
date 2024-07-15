from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel
import win32more.Windows.Data.Xml.Dom
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.System
import win32more.Windows.UI.Notifications
import win32more.Windows.Win32.System.WinRT
class AdaptiveNotificationContentKind(Enum, Int32):
    Text = 0
class AdaptiveNotificationText(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IAdaptiveNotificationText
    _classid_ = 'Windows.UI.Notifications.AdaptiveNotificationText'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Notifications.AdaptiveNotificationText.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Notifications.AdaptiveNotificationText: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.UI.Notifications.IAdaptiveNotificationText) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: win32more.Windows.UI.Notifications.IAdaptiveNotificationText, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.UI.Notifications.IAdaptiveNotificationText) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: win32more.Windows.UI.Notifications.IAdaptiveNotificationText, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.UI.Notifications.IAdaptiveNotificationContent) -> win32more.Windows.UI.Notifications.AdaptiveNotificationContentKind: ...
    @winrt_mixinmethod
    def get_Hints(self: win32more.Windows.UI.Notifications.IAdaptiveNotificationContent) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    Hints = property(get_Hints, None)
    Kind = property(get_Kind, None)
    Language = property(get_Language, put_Language)
    Text = property(get_Text, put_Text)
class BadgeNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IBadgeNotification
    _classid_ = 'Windows.UI.Notifications.BadgeNotification'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Notifications.BadgeNotification.CreateBadgeNotification(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateBadgeNotification(cls: win32more.Windows.UI.Notifications.IBadgeNotificationFactory, content: win32more.Windows.Data.Xml.Dom.XmlDocument) -> win32more.Windows.UI.Notifications.BadgeNotification: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.UI.Notifications.IBadgeNotification) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_mixinmethod
    def put_ExpirationTime(self: win32more.Windows.UI.Notifications.IBadgeNotification, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: win32more.Windows.UI.Notifications.IBadgeNotification) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    Content = property(get_Content, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
class BadgeTemplateType(Enum, Int32):
    BadgeGlyph = 0
    BadgeNumber = 1
class BadgeUpdateManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.BadgeUpdateManager'
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.UI.Notifications.IBadgeUpdateManagerStatics2, user: win32more.Windows.System.User) -> win32more.Windows.UI.Notifications.BadgeUpdateManagerForUser: ...
    @winrt_classmethod
    def CreateBadgeUpdaterForApplication(cls: win32more.Windows.UI.Notifications.IBadgeUpdateManagerStatics) -> win32more.Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_classmethod
    def CreateBadgeUpdaterForApplicationWithId(cls: win32more.Windows.UI.Notifications.IBadgeUpdateManagerStatics, applicationId: WinRT_String) -> win32more.Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_classmethod
    def CreateBadgeUpdaterForSecondaryTile(cls: win32more.Windows.UI.Notifications.IBadgeUpdateManagerStatics, tileId: WinRT_String) -> win32more.Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_classmethod
    def GetTemplateContent(cls: win32more.Windows.UI.Notifications.IBadgeUpdateManagerStatics, type: win32more.Windows.UI.Notifications.BadgeTemplateType) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
class BadgeUpdateManagerForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IBadgeUpdateManagerForUser
    _classid_ = 'Windows.UI.Notifications.BadgeUpdateManagerForUser'
    @winrt_mixinmethod
    def CreateBadgeUpdaterForApplication(self: win32more.Windows.UI.Notifications.IBadgeUpdateManagerForUser) -> win32more.Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_mixinmethod
    def CreateBadgeUpdaterForApplicationWithId(self: win32more.Windows.UI.Notifications.IBadgeUpdateManagerForUser, applicationId: WinRT_String) -> win32more.Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_mixinmethod
    def CreateBadgeUpdaterForSecondaryTile(self: win32more.Windows.UI.Notifications.IBadgeUpdateManagerForUser, tileId: WinRT_String) -> win32more.Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.UI.Notifications.IBadgeUpdateManagerForUser) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class BadgeUpdater(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IBadgeUpdater
    _classid_ = 'Windows.UI.Notifications.BadgeUpdater'
    @winrt_mixinmethod
    def Update(self: win32more.Windows.UI.Notifications.IBadgeUpdater, notification: win32more.Windows.UI.Notifications.BadgeNotification) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.UI.Notifications.IBadgeUpdater) -> Void: ...
    @winrt_mixinmethod
    def StartPeriodicUpdate(self: win32more.Windows.UI.Notifications.IBadgeUpdater, badgeContent: win32more.Windows.Foundation.Uri, requestedInterval: win32more.Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_mixinmethod
    def StartPeriodicUpdateAtTime(self: win32more.Windows.UI.Notifications.IBadgeUpdater, badgeContent: win32more.Windows.Foundation.Uri, startTime: win32more.Windows.Foundation.DateTime, requestedInterval: win32more.Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_mixinmethod
    def StopPeriodicUpdate(self: win32more.Windows.UI.Notifications.IBadgeUpdater) -> Void: ...
class IAdaptiveNotificationContent(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IAdaptiveNotificationContent'
    _iid_ = Guid('{eb0dbe66-7448-448d-9db8-d78acd2abba9}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.UI.Notifications.AdaptiveNotificationContentKind: ...
    @winrt_commethod(7)
    def get_Hints(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    Hints = property(get_Hints, None)
    Kind = property(get_Kind, None)
class IAdaptiveNotificationText(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IAdaptiveNotificationText'
    _iid_ = Guid('{46d4a3be-609a-4326-a40b-bfde872034a3}')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Text(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Language(self, value: WinRT_String) -> Void: ...
    Language = property(get_Language, put_Language)
    Text = property(get_Text, put_Text)
class IBadgeNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IBadgeNotification'
    _iid_ = Guid('{075cb4ca-d08a-4e2f-9233-7e289c1f7722}')
    @winrt_commethod(6)
    def get_Content(self) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_commethod(7)
    def put_ExpirationTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(8)
    def get_ExpirationTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    Content = property(get_Content, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
class IBadgeNotificationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IBadgeNotificationFactory'
    _iid_ = Guid('{edf255ce-0618-4d59-948a-5a61040c52f9}')
    @winrt_commethod(6)
    def CreateBadgeNotification(self, content: win32more.Windows.Data.Xml.Dom.XmlDocument) -> win32more.Windows.UI.Notifications.BadgeNotification: ...
class IBadgeUpdateManagerForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IBadgeUpdateManagerForUser'
    _iid_ = Guid('{996b21bc-0386-44e5-ba8d-0c1077a62e92}')
    @winrt_commethod(6)
    def CreateBadgeUpdaterForApplication(self) -> win32more.Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_commethod(7)
    def CreateBadgeUpdaterForApplicationWithId(self, applicationId: WinRT_String) -> win32more.Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_commethod(8)
    def CreateBadgeUpdaterForSecondaryTile(self, tileId: WinRT_String) -> win32more.Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_commethod(9)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IBadgeUpdateManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IBadgeUpdateManagerStatics'
    _iid_ = Guid('{33400faa-6dd5-4105-aebc-9b50fca492da}')
    @winrt_commethod(6)
    def CreateBadgeUpdaterForApplication(self) -> win32more.Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_commethod(7)
    def CreateBadgeUpdaterForApplicationWithId(self, applicationId: WinRT_String) -> win32more.Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_commethod(8)
    def CreateBadgeUpdaterForSecondaryTile(self, tileId: WinRT_String) -> win32more.Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_commethod(9)
    def GetTemplateContent(self, type: win32more.Windows.UI.Notifications.BadgeTemplateType) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
class IBadgeUpdateManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IBadgeUpdateManagerStatics2'
    _iid_ = Guid('{979a35ce-f940-48bf-94e8-ca244d400b41}')
    @winrt_commethod(6)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.UI.Notifications.BadgeUpdateManagerForUser: ...
class IBadgeUpdater(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IBadgeUpdater'
    _iid_ = Guid('{b5fa1fd4-7562-4f6c-bfa3-1b6ed2e57f2f}')
    @winrt_commethod(6)
    def Update(self, notification: win32more.Windows.UI.Notifications.BadgeNotification) -> Void: ...
    @winrt_commethod(7)
    def Clear(self) -> Void: ...
    @winrt_commethod(8)
    def StartPeriodicUpdate(self, badgeContent: win32more.Windows.Foundation.Uri, requestedInterval: win32more.Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_commethod(9)
    def StartPeriodicUpdateAtTime(self, badgeContent: win32more.Windows.Foundation.Uri, startTime: win32more.Windows.Foundation.DateTime, requestedInterval: win32more.Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_commethod(10)
    def StopPeriodicUpdate(self) -> Void: ...
class IKnownAdaptiveNotificationHintsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IKnownAdaptiveNotificationHintsStatics'
    _iid_ = Guid('{06206598-d496-497d-8692-4f7d7c2770df}')
    @winrt_commethod(6)
    def get_Style(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Wrap(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_MaxLines(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_MinLines(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_TextStacking(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Align(self) -> WinRT_String: ...
    Align = property(get_Align, None)
    MaxLines = property(get_MaxLines, None)
    MinLines = property(get_MinLines, None)
    Style = property(get_Style, None)
    TextStacking = property(get_TextStacking, None)
    Wrap = property(get_Wrap, None)
class IKnownAdaptiveNotificationTextStylesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics'
    _iid_ = Guid('{202192d7-8996-45aa-8ba1-d461d72c2a1b}')
    @winrt_commethod(6)
    def get_Caption(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Body(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Base(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Subtitle(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Subheader(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Header(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_TitleNumeral(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_SubheaderNumeral(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_HeaderNumeral(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_CaptionSubtle(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_BodySubtle(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_BaseSubtle(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_SubtitleSubtle(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def get_TitleSubtle(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def get_SubheaderSubtle(self) -> WinRT_String: ...
    @winrt_commethod(22)
    def get_SubheaderNumeralSubtle(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def get_HeaderSubtle(self) -> WinRT_String: ...
    @winrt_commethod(24)
    def get_HeaderNumeralSubtle(self) -> WinRT_String: ...
    Base = property(get_Base, None)
    BaseSubtle = property(get_BaseSubtle, None)
    Body = property(get_Body, None)
    BodySubtle = property(get_BodySubtle, None)
    Caption = property(get_Caption, None)
    CaptionSubtle = property(get_CaptionSubtle, None)
    Header = property(get_Header, None)
    HeaderNumeral = property(get_HeaderNumeral, None)
    HeaderNumeralSubtle = property(get_HeaderNumeralSubtle, None)
    HeaderSubtle = property(get_HeaderSubtle, None)
    Subheader = property(get_Subheader, None)
    SubheaderNumeral = property(get_SubheaderNumeral, None)
    SubheaderNumeralSubtle = property(get_SubheaderNumeralSubtle, None)
    SubheaderSubtle = property(get_SubheaderSubtle, None)
    Subtitle = property(get_Subtitle, None)
    SubtitleSubtle = property(get_SubtitleSubtle, None)
    Title = property(get_Title, None)
    TitleNumeral = property(get_TitleNumeral, None)
    TitleSubtle = property(get_TitleSubtle, None)
class IKnownNotificationBindingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IKnownNotificationBindingsStatics'
    _iid_ = Guid('{79427bae-a8b7-4d58-89ea-76a7b7bccded}')
    @winrt_commethod(6)
    def get_ToastGeneric(self) -> WinRT_String: ...
    ToastGeneric = property(get_ToastGeneric, None)
class INotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.INotification'
    _iid_ = Guid('{108037fe-eb76-4f82-97bc-da07530a2e20}')
    @winrt_commethod(6)
    def get_ExpirationTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(7)
    def put_ExpirationTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(8)
    def get_Visual(self) -> win32more.Windows.UI.Notifications.NotificationVisual: ...
    @winrt_commethod(9)
    def put_Visual(self, value: win32more.Windows.UI.Notifications.NotificationVisual) -> Void: ...
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
    Visual = property(get_Visual, put_Visual)
class INotificationBinding(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.INotificationBinding'
    _iid_ = Guid('{f29e4b85-0370-4ad3-b4ea-da9e35e7eabf}')
    @winrt_commethod(6)
    def get_Template(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Template(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Language(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Hints(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(11)
    def GetTextElements(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Notifications.AdaptiveNotificationText]: ...
    Hints = property(get_Hints, None)
    Language = property(get_Language, put_Language)
    Template = property(get_Template, put_Template)
class INotificationData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.INotificationData'
    _iid_ = Guid('{9ffd2312-9d6a-4aaf-b6ac-ff17f0c1f280}')
    @winrt_commethod(6)
    def get_Values(self) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(7)
    def get_SequenceNumber(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_SequenceNumber(self, value: UInt32) -> Void: ...
    SequenceNumber = property(get_SequenceNumber, put_SequenceNumber)
    Values = property(get_Values, None)
class INotificationDataFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.INotificationDataFactory'
    _iid_ = Guid('{23c1e33a-1c10-46fb-8040-dec384621cf8}')
    @winrt_commethod(6)
    def CreateNotificationDataWithValuesAndSequenceNumber(self, initialValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]], sequenceNumber: UInt32) -> win32more.Windows.UI.Notifications.NotificationData: ...
    @winrt_commethod(7)
    def CreateNotificationDataWithValues(self, initialValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> win32more.Windows.UI.Notifications.NotificationData: ...
class INotificationVisual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.INotificationVisual'
    _iid_ = Guid('{68835b8e-aa56-4e11-86d3-5f9a6957bc5b}')
    @winrt_commethod(6)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Language(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Bindings(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Notifications.NotificationBinding]: ...
    @winrt_commethod(9)
    def GetBinding(self, templateName: WinRT_String) -> win32more.Windows.UI.Notifications.NotificationBinding: ...
    Bindings = property(get_Bindings, None)
    Language = property(get_Language, put_Language)
class IScheduledTileNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IScheduledTileNotification'
    _iid_ = Guid('{0abca6d5-99dc-4c78-a11c-c9e7f86d7ef7}')
    @winrt_commethod(6)
    def get_Content(self) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_commethod(7)
    def get_DeliveryTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def put_ExpirationTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(9)
    def get_ExpirationTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(10)
    def put_Tag(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_Tag(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_Id(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_Id(self) -> WinRT_String: ...
    Content = property(get_Content, None)
    DeliveryTime = property(get_DeliveryTime, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
    Id = property(get_Id, put_Id)
    Tag = property(get_Tag, put_Tag)
class IScheduledTileNotificationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IScheduledTileNotificationFactory'
    _iid_ = Guid('{3383138a-98c0-4c3b-bbd6-4a633c7cfc29}')
    @winrt_commethod(6)
    def CreateScheduledTileNotification(self, content: win32more.Windows.Data.Xml.Dom.XmlDocument, deliveryTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.UI.Notifications.ScheduledTileNotification: ...
class IScheduledToastNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IScheduledToastNotification'
    _iid_ = Guid('{79f577f8-0de7-48cd-9740-9b370490c838}')
    @winrt_commethod(6)
    def get_Content(self) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_commethod(7)
    def get_DeliveryTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_SnoozeInterval(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(9)
    def get_MaximumSnoozeCount(self) -> UInt32: ...
    @winrt_commethod(10)
    def put_Id(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_Id(self) -> WinRT_String: ...
    Content = property(get_Content, None)
    DeliveryTime = property(get_DeliveryTime, None)
    Id = property(get_Id, put_Id)
    MaximumSnoozeCount = property(get_MaximumSnoozeCount, None)
    SnoozeInterval = property(get_SnoozeInterval, None)
class IScheduledToastNotification2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IScheduledToastNotification2'
    _iid_ = Guid('{a66ea09c-31b4-43b0-b5dd-7a40e85363b1}')
    @winrt_commethod(6)
    def put_Tag(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_Tag(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Group(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Group(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_SuppressPopup(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_SuppressPopup(self) -> Boolean: ...
    Group = property(get_Group, put_Group)
    SuppressPopup = property(get_SuppressPopup, put_SuppressPopup)
    Tag = property(get_Tag, put_Tag)
class IScheduledToastNotification3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IScheduledToastNotification3'
    _iid_ = Guid('{98429e8b-bd32-4a3b-9d15-22aea49462a1}')
    @winrt_commethod(6)
    def get_NotificationMirroring(self) -> win32more.Windows.UI.Notifications.NotificationMirroring: ...
    @winrt_commethod(7)
    def put_NotificationMirroring(self, value: win32more.Windows.UI.Notifications.NotificationMirroring) -> Void: ...
    @winrt_commethod(8)
    def get_RemoteId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_RemoteId(self, value: WinRT_String) -> Void: ...
    NotificationMirroring = property(get_NotificationMirroring, put_NotificationMirroring)
    RemoteId = property(get_RemoteId, put_RemoteId)
class IScheduledToastNotification4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IScheduledToastNotification4'
    _iid_ = Guid('{1d4761fd-bdef-4e4a-96be-0101369b58d2}')
    @winrt_commethod(6)
    def get_ExpirationTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(7)
    def put_ExpirationTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
class IScheduledToastNotificationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IScheduledToastNotificationFactory'
    _iid_ = Guid('{e7bed191-0bb9-4189-8394-31761b476fd7}')
    @winrt_commethod(6)
    def CreateScheduledToastNotification(self, content: win32more.Windows.Data.Xml.Dom.XmlDocument, deliveryTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.UI.Notifications.ScheduledToastNotification: ...
    @winrt_commethod(7)
    def CreateScheduledToastNotificationRecurring(self, content: win32more.Windows.Data.Xml.Dom.XmlDocument, deliveryTime: win32more.Windows.Foundation.DateTime, snoozeInterval: win32more.Windows.Foundation.TimeSpan, maximumSnoozeCount: UInt32) -> win32more.Windows.UI.Notifications.ScheduledToastNotification: ...
class IScheduledToastNotificationShowingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IScheduledToastNotificationShowingEventArgs'
    _iid_ = Guid('{6173f6b4-412a-5e2c-a6ed-a0209aef9a09}')
    @winrt_commethod(6)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_ScheduledToastNotification(self) -> win32more.Windows.UI.Notifications.ScheduledToastNotification: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Cancel = property(get_Cancel, put_Cancel)
    ScheduledToastNotification = property(get_ScheduledToastNotification, None)
class IShownTileNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IShownTileNotification'
    _iid_ = Guid('{342d8988-5af2-481a-a6a3-f2fdc78de88e}')
    @winrt_commethod(6)
    def get_Arguments(self) -> WinRT_String: ...
    Arguments = property(get_Arguments, None)
class ITileFlyoutNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.ITileFlyoutNotification'
    _iid_ = Guid('{9a53b261-c70c-42be-b2f3-f42aa97d34e5}')
    @winrt_commethod(6)
    def get_Content(self) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_commethod(7)
    def put_ExpirationTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(8)
    def get_ExpirationTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    Content = property(get_Content, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
class ITileFlyoutNotificationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.ITileFlyoutNotificationFactory'
    _iid_ = Guid('{ef556ff5-5226-4f2b-b278-88a35dfe569f}')
    @winrt_commethod(6)
    def CreateTileFlyoutNotification(self, content: win32more.Windows.Data.Xml.Dom.XmlDocument) -> win32more.Windows.UI.Notifications.TileFlyoutNotification: ...
class ITileFlyoutUpdateManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.ITileFlyoutUpdateManagerStatics'
    _iid_ = Guid('{04363b0b-1ac0-4b99-88e7-ada83e953d48}')
    @winrt_commethod(6)
    def CreateTileFlyoutUpdaterForApplication(self) -> win32more.Windows.UI.Notifications.TileFlyoutUpdater: ...
    @winrt_commethod(7)
    def CreateTileFlyoutUpdaterForApplicationWithId(self, applicationId: WinRT_String) -> win32more.Windows.UI.Notifications.TileFlyoutUpdater: ...
    @winrt_commethod(8)
    def CreateTileFlyoutUpdaterForSecondaryTile(self, tileId: WinRT_String) -> win32more.Windows.UI.Notifications.TileFlyoutUpdater: ...
    @winrt_commethod(9)
    def GetTemplateContent(self, type: win32more.Windows.UI.Notifications.TileFlyoutTemplateType) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
class ITileFlyoutUpdater(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.ITileFlyoutUpdater'
    _iid_ = Guid('{8d40c76a-c465-4052-a740-5c2654c1a089}')
    @winrt_commethod(6)
    def Update(self, notification: win32more.Windows.UI.Notifications.TileFlyoutNotification) -> Void: ...
    @winrt_commethod(7)
    def Clear(self) -> Void: ...
    @winrt_commethod(8)
    def StartPeriodicUpdate(self, tileFlyoutContent: win32more.Windows.Foundation.Uri, requestedInterval: win32more.Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_commethod(9)
    def StartPeriodicUpdateAtTime(self, tileFlyoutContent: win32more.Windows.Foundation.Uri, startTime: win32more.Windows.Foundation.DateTime, requestedInterval: win32more.Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_commethod(10)
    def StopPeriodicUpdate(self) -> Void: ...
    @winrt_commethod(11)
    def get_Setting(self) -> win32more.Windows.UI.Notifications.NotificationSetting: ...
    Setting = property(get_Setting, None)
class ITileNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.ITileNotification'
    _iid_ = Guid('{ebaec8fa-50ec-4c18-b4d0-3af02e5540ab}')
    @winrt_commethod(6)
    def get_Content(self) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_commethod(7)
    def put_ExpirationTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(8)
    def get_ExpirationTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(9)
    def put_Tag(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Tag(self) -> WinRT_String: ...
    Content = property(get_Content, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
    Tag = property(get_Tag, put_Tag)
class ITileNotificationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.ITileNotificationFactory'
    _iid_ = Guid('{c6abdd6e-4928-46c8-bdbf-81a047dea0d4}')
    @winrt_commethod(6)
    def CreateTileNotification(self, content: win32more.Windows.Data.Xml.Dom.XmlDocument) -> win32more.Windows.UI.Notifications.TileNotification: ...
class ITileUpdateManagerForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.ITileUpdateManagerForUser'
    _iid_ = Guid('{55141348-2ee2-4e2d-9cc1-216a20decc9f}')
    @winrt_commethod(6)
    def CreateTileUpdaterForApplication(self) -> win32more.Windows.UI.Notifications.TileUpdater: ...
    @winrt_commethod(7)
    def CreateTileUpdaterForApplicationWithId(self, applicationId: WinRT_String) -> win32more.Windows.UI.Notifications.TileUpdater: ...
    @winrt_commethod(8)
    def CreateTileUpdaterForSecondaryTile(self, tileId: WinRT_String) -> win32more.Windows.UI.Notifications.TileUpdater: ...
    @winrt_commethod(9)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class ITileUpdateManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.ITileUpdateManagerStatics'
    _iid_ = Guid('{da159e5d-3ea9-4986-8d84-b09d5e12276d}')
    @winrt_commethod(6)
    def CreateTileUpdaterForApplication(self) -> win32more.Windows.UI.Notifications.TileUpdater: ...
    @winrt_commethod(7)
    def CreateTileUpdaterForApplicationWithId(self, applicationId: WinRT_String) -> win32more.Windows.UI.Notifications.TileUpdater: ...
    @winrt_commethod(8)
    def CreateTileUpdaterForSecondaryTile(self, tileId: WinRT_String) -> win32more.Windows.UI.Notifications.TileUpdater: ...
    @winrt_commethod(9)
    def GetTemplateContent(self, type: win32more.Windows.UI.Notifications.TileTemplateType) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
class ITileUpdateManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.ITileUpdateManagerStatics2'
    _iid_ = Guid('{731c1ddc-8e14-4b7c-a34b-9d22de76c84d}')
    @winrt_commethod(6)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.UI.Notifications.TileUpdateManagerForUser: ...
class ITileUpdater(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.ITileUpdater'
    _iid_ = Guid('{0942a48b-1d91-44ec-9243-c1e821c29a20}')
    @winrt_commethod(6)
    def Update(self, notification: win32more.Windows.UI.Notifications.TileNotification) -> Void: ...
    @winrt_commethod(7)
    def Clear(self) -> Void: ...
    @winrt_commethod(8)
    def EnableNotificationQueue(self, enable: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_Setting(self) -> win32more.Windows.UI.Notifications.NotificationSetting: ...
    @winrt_commethod(10)
    def AddToSchedule(self, scheduledTile: win32more.Windows.UI.Notifications.ScheduledTileNotification) -> Void: ...
    @winrt_commethod(11)
    def RemoveFromSchedule(self, scheduledTile: win32more.Windows.UI.Notifications.ScheduledTileNotification) -> Void: ...
    @winrt_commethod(12)
    def GetScheduledTileNotifications(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Notifications.ScheduledTileNotification]: ...
    @winrt_commethod(13)
    def StartPeriodicUpdate(self, tileContent: win32more.Windows.Foundation.Uri, requestedInterval: win32more.Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_commethod(14)
    def StartPeriodicUpdateAtTime(self, tileContent: win32more.Windows.Foundation.Uri, startTime: win32more.Windows.Foundation.DateTime, requestedInterval: win32more.Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_commethod(15)
    def StopPeriodicUpdate(self) -> Void: ...
    @winrt_commethod(16)
    def StartPeriodicUpdateBatch(self, tileContents: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Uri], requestedInterval: win32more.Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_commethod(17)
    def StartPeriodicUpdateBatchAtTime(self, tileContents: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Uri], startTime: win32more.Windows.Foundation.DateTime, requestedInterval: win32more.Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    Setting = property(get_Setting, None)
class ITileUpdater2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.ITileUpdater2'
    _iid_ = Guid('{a2266e12-15ee-43ed-83f5-65b352bb1a84}')
    @winrt_commethod(6)
    def EnableNotificationQueueForSquare150x150(self, enable: Boolean) -> Void: ...
    @winrt_commethod(7)
    def EnableNotificationQueueForWide310x150(self, enable: Boolean) -> Void: ...
    @winrt_commethod(8)
    def EnableNotificationQueueForSquare310x310(self, enable: Boolean) -> Void: ...
class IToastActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastActivatedEventArgs'
    _iid_ = Guid('{e3bf92f3-c197-436f-8265-0625824f8dac}')
    @winrt_commethod(6)
    def get_Arguments(self) -> WinRT_String: ...
    Arguments = property(get_Arguments, None)
class IToastActivatedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastActivatedEventArgs2'
    _iid_ = Guid('{ab7da512-cc61-568e-81be-304ac31038fa}')
    @winrt_commethod(6)
    def get_UserInput(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    UserInput = property(get_UserInput, None)
class IToastCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastCollection'
    _iid_ = Guid('{0a8bc3b0-e0be-4858-bc2a-89dfe0b32863}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_LaunchArgs(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_LaunchArgs(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_Icon(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(12)
    def put_Icon(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    Icon = property(get_Icon, put_Icon)
    Id = property(get_Id, None)
    LaunchArgs = property(get_LaunchArgs, put_LaunchArgs)
class IToastCollectionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastCollectionFactory'
    _iid_ = Guid('{164dd3d7-73c4-44f7-b4ff-fb6d4bf1f4c6}')
    @winrt_commethod(6)
    def CreateInstance(self, collectionId: WinRT_String, displayName: WinRT_String, launchArgs: WinRT_String, iconUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.Notifications.ToastCollection: ...
class IToastCollectionManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastCollectionManager'
    _iid_ = Guid('{2a1821fe-179d-49bc-b79d-a527920d3665}')
    @winrt_commethod(6)
    def SaveToastCollectionAsync(self, collection: win32more.Windows.UI.Notifications.ToastCollection) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def FindAllToastCollectionsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Notifications.ToastCollection]]: ...
    @winrt_commethod(8)
    def GetToastCollectionAsync(self, collectionId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Notifications.ToastCollection]: ...
    @winrt_commethod(9)
    def RemoveToastCollectionAsync(self, collectionId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def RemoveAllToastCollectionsAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def get_User(self) -> win32more.Windows.System.User: ...
    @winrt_commethod(12)
    def get_AppId(self) -> WinRT_String: ...
    AppId = property(get_AppId, None)
    User = property(get_User, None)
class IToastDismissedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastDismissedEventArgs'
    _iid_ = Guid('{3f89d935-d9cb-4538-a0f0-ffe7659938f8}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Windows.UI.Notifications.ToastDismissalReason: ...
    Reason = property(get_Reason, None)
class IToastFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastFailedEventArgs'
    _iid_ = Guid('{35176862-cfd4-44f8-ad64-f500fd896c3b}')
    @winrt_commethod(6)
    def get_ErrorCode(self) -> win32more.Windows.Foundation.HResult: ...
    ErrorCode = property(get_ErrorCode, None)
class IToastNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotification'
    _iid_ = Guid('{997e2675-059e-4e60-8b06-1760917c8b80}')
    @winrt_commethod(6)
    def get_Content(self) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_commethod(7)
    def put_ExpirationTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(8)
    def get_ExpirationTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(9)
    def add_Dismissed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Notifications.ToastNotification, win32more.Windows.UI.Notifications.ToastDismissedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Dismissed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Activated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Notifications.ToastNotification, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Activated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_Failed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Notifications.ToastNotification, win32more.Windows.UI.Notifications.ToastFailedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_Failed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Content = property(get_Content, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
    Dismissed = event()
    Activated = event()
    Failed = event()
class IToastNotification2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotification2'
    _iid_ = Guid('{9dfb9fd1-143a-490e-90bf-b9fba7132de7}')
    @winrt_commethod(6)
    def put_Tag(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_Tag(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Group(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Group(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_SuppressPopup(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_SuppressPopup(self) -> Boolean: ...
    Group = property(get_Group, put_Group)
    SuppressPopup = property(get_SuppressPopup, put_SuppressPopup)
    Tag = property(get_Tag, put_Tag)
class IToastNotification3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotification3'
    _iid_ = Guid('{31e8aed8-8141-4f99-bc0a-c4ed21297d77}')
    @winrt_commethod(6)
    def get_NotificationMirroring(self) -> win32more.Windows.UI.Notifications.NotificationMirroring: ...
    @winrt_commethod(7)
    def put_NotificationMirroring(self, value: win32more.Windows.UI.Notifications.NotificationMirroring) -> Void: ...
    @winrt_commethod(8)
    def get_RemoteId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_RemoteId(self, value: WinRT_String) -> Void: ...
    NotificationMirroring = property(get_NotificationMirroring, put_NotificationMirroring)
    RemoteId = property(get_RemoteId, put_RemoteId)
class IToastNotification4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotification4'
    _iid_ = Guid('{15154935-28ea-4727-88e9-c58680e2d118}')
    @winrt_commethod(6)
    def get_Data(self) -> win32more.Windows.UI.Notifications.NotificationData: ...
    @winrt_commethod(7)
    def put_Data(self, value: win32more.Windows.UI.Notifications.NotificationData) -> Void: ...
    @winrt_commethod(8)
    def get_Priority(self) -> win32more.Windows.UI.Notifications.ToastNotificationPriority: ...
    @winrt_commethod(9)
    def put_Priority(self, value: win32more.Windows.UI.Notifications.ToastNotificationPriority) -> Void: ...
    Data = property(get_Data, put_Data)
    Priority = property(get_Priority, put_Priority)
class IToastNotification6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotification6'
    _iid_ = Guid('{43ebfe53-89ae-5c1e-a279-3aecfe9b6f54}')
    @winrt_commethod(6)
    def get_ExpiresOnReboot(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_ExpiresOnReboot(self, value: Boolean) -> Void: ...
    ExpiresOnReboot = property(get_ExpiresOnReboot, put_ExpiresOnReboot)
class IToastNotificationActionTriggerDetail(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotificationActionTriggerDetail'
    _iid_ = Guid('{9445135a-38f3-42f6-96aa-7955b0f03da2}')
    @winrt_commethod(6)
    def get_Argument(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_UserInput(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Argument = property(get_Argument, None)
    UserInput = property(get_UserInput, None)
class IToastNotificationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotificationFactory'
    _iid_ = Guid('{04124b20-82c6-4229-b109-fd9ed4662b53}')
    @winrt_commethod(6)
    def CreateToastNotification(self, content: win32more.Windows.Data.Xml.Dom.XmlDocument) -> win32more.Windows.UI.Notifications.ToastNotification: ...
class IToastNotificationHistory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotificationHistory'
    _iid_ = Guid('{5caddc63-01d3-4c97-986f-0533483fee14}')
    @winrt_commethod(6)
    def RemoveGroup(self, group: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def RemoveGroupWithId(self, group: WinRT_String, applicationId: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def RemoveGroupedTagWithId(self, tag: WinRT_String, group: WinRT_String, applicationId: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def RemoveGroupedTag(self, tag: WinRT_String, group: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def Remove(self, tag: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def Clear(self) -> Void: ...
    @winrt_commethod(12)
    def ClearWithId(self, applicationId: WinRT_String) -> Void: ...
class IToastNotificationHistory2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotificationHistory2'
    _iid_ = Guid('{3bc3d253-2f31-4092-9129-8ad5abf067da}')
    @winrt_commethod(6)
    def GetHistory(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Notifications.ToastNotification]: ...
    @winrt_commethod(7)
    def GetHistoryWithId(self, applicationId: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Notifications.ToastNotification]: ...
class IToastNotificationHistoryChangedTriggerDetail(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotificationHistoryChangedTriggerDetail'
    _iid_ = Guid('{db037ffa-0068-412c-9c83-267c37f65670}')
    @winrt_commethod(6)
    def get_ChangeType(self) -> win32more.Windows.UI.Notifications.ToastHistoryChangedType: ...
    ChangeType = property(get_ChangeType, None)
class IToastNotificationHistoryChangedTriggerDetail2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotificationHistoryChangedTriggerDetail2'
    _iid_ = Guid('{0b36e982-c871-49fb-babb-25bdbc4cc45b}')
    @winrt_commethod(6)
    def get_CollectionId(self) -> WinRT_String: ...
    CollectionId = property(get_CollectionId, None)
class IToastNotificationManagerForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotificationManagerForUser'
    _iid_ = Guid('{79ab57f6-43fe-487b-8a7f-99567200ae94}')
    @winrt_commethod(6)
    def CreateToastNotifier(self) -> win32more.Windows.UI.Notifications.ToastNotifier: ...
    @winrt_commethod(7)
    def CreateToastNotifierWithId(self, applicationId: WinRT_String) -> win32more.Windows.UI.Notifications.ToastNotifier: ...
    @winrt_commethod(8)
    def get_History(self) -> win32more.Windows.UI.Notifications.ToastNotificationHistory: ...
    @winrt_commethod(9)
    def get_User(self) -> win32more.Windows.System.User: ...
    History = property(get_History, None)
    User = property(get_User, None)
class IToastNotificationManagerForUser2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotificationManagerForUser2'
    _iid_ = Guid('{679c64b7-81ab-42c2-8819-c958767753f4}')
    @winrt_commethod(6)
    def GetToastNotifierForToastCollectionIdAsync(self, collectionId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Notifications.ToastNotifier]: ...
    @winrt_commethod(7)
    def GetHistoryForToastCollectionIdAsync(self, collectionId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Notifications.ToastNotificationHistory]: ...
    @winrt_commethod(8)
    def GetToastCollectionManager(self) -> win32more.Windows.UI.Notifications.ToastCollectionManager: ...
    @winrt_commethod(9)
    def GetToastCollectionManagerWithAppId(self, appId: WinRT_String) -> win32more.Windows.UI.Notifications.ToastCollectionManager: ...
class IToastNotificationManagerForUser3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotificationManagerForUser3'
    _iid_ = Guid('{3efcb176-6cc1-56dc-973b-251f7aacb1c5}')
    @winrt_commethod(6)
    def get_NotificationMode(self) -> win32more.Windows.UI.Notifications.ToastNotificationMode: ...
    @winrt_commethod(7)
    def add_NotificationModeChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Notifications.ToastNotificationManagerForUser, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_NotificationModeChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    NotificationMode = property(get_NotificationMode, None)
    NotificationModeChanged = event()
class IToastNotificationManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotificationManagerStatics'
    _iid_ = Guid('{50ac103f-d235-4598-bbef-98fe4d1a3ad4}')
    @winrt_commethod(6)
    def CreateToastNotifier(self) -> win32more.Windows.UI.Notifications.ToastNotifier: ...
    @winrt_commethod(7)
    def CreateToastNotifierWithId(self, applicationId: WinRT_String) -> win32more.Windows.UI.Notifications.ToastNotifier: ...
    @winrt_commethod(8)
    def GetTemplateContent(self, type: win32more.Windows.UI.Notifications.ToastTemplateType) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
class IToastNotificationManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotificationManagerStatics2'
    _iid_ = Guid('{7ab93c52-0e48-4750-ba9d-1a4113981847}')
    @winrt_commethod(6)
    def get_History(self) -> win32more.Windows.UI.Notifications.ToastNotificationHistory: ...
    History = property(get_History, None)
class IToastNotificationManagerStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotificationManagerStatics4'
    _iid_ = Guid('{8f993fd3-e516-45fb-8130-398e93fa52c3}')
    @winrt_commethod(6)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.UI.Notifications.ToastNotificationManagerForUser: ...
    @winrt_commethod(7)
    def ConfigureNotificationMirroring(self, value: win32more.Windows.UI.Notifications.NotificationMirroring) -> Void: ...
class IToastNotificationManagerStatics5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotificationManagerStatics5'
    _iid_ = Guid('{d6f5f569-d40d-407c-8989-88cab42cfd14}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.UI.Notifications.ToastNotificationManagerForUser: ...
class IToastNotifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotifier'
    _iid_ = Guid('{75927b93-03f3-41ec-91d3-6e5bac1b38e7}')
    @winrt_commethod(6)
    def Show(self, notification: win32more.Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_commethod(7)
    def Hide(self, notification: win32more.Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_commethod(8)
    def get_Setting(self) -> win32more.Windows.UI.Notifications.NotificationSetting: ...
    @winrt_commethod(9)
    def AddToSchedule(self, scheduledToast: win32more.Windows.UI.Notifications.ScheduledToastNotification) -> Void: ...
    @winrt_commethod(10)
    def RemoveFromSchedule(self, scheduledToast: win32more.Windows.UI.Notifications.ScheduledToastNotification) -> Void: ...
    @winrt_commethod(11)
    def GetScheduledToastNotifications(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Notifications.ScheduledToastNotification]: ...
    Setting = property(get_Setting, None)
class IToastNotifier2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotifier2'
    _iid_ = Guid('{354389c6-7c01-4bd5-9c20-604340cd2b74}')
    @winrt_commethod(6)
    def UpdateWithTagAndGroup(self, data: win32more.Windows.UI.Notifications.NotificationData, tag: WinRT_String, group: WinRT_String) -> win32more.Windows.UI.Notifications.NotificationUpdateResult: ...
    @winrt_commethod(7)
    def UpdateWithTag(self, data: win32more.Windows.UI.Notifications.NotificationData, tag: WinRT_String) -> win32more.Windows.UI.Notifications.NotificationUpdateResult: ...
class IToastNotifier3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IToastNotifier3'
    _iid_ = Guid('{ae75a04a-3b0c-51ad-b7e8-b08ab6052549}')
    @winrt_commethod(6)
    def add_ScheduledToastNotificationShowing(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Notifications.ToastNotifier, win32more.Windows.UI.Notifications.ScheduledToastNotificationShowingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ScheduledToastNotificationShowing(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ScheduledToastNotificationShowing = event()
class IUserNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IUserNotification'
    _iid_ = Guid('{adf7e52f-4e53-42d5-9c33-eb5ea515b23e}')
    @winrt_commethod(6)
    def get_Notification(self) -> win32more.Windows.UI.Notifications.Notification: ...
    @winrt_commethod(7)
    def get_AppInfo(self) -> win32more.Windows.ApplicationModel.AppInfo: ...
    @winrt_commethod(8)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_CreationTime(self) -> win32more.Windows.Foundation.DateTime: ...
    AppInfo = property(get_AppInfo, None)
    CreationTime = property(get_CreationTime, None)
    Id = property(get_Id, None)
    Notification = property(get_Notification, None)
class IUserNotificationChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.IUserNotificationChangedEventArgs'
    _iid_ = Guid('{b6bd6839-79cf-4b25-82c0-0ce1eef81f8c}')
    @winrt_commethod(6)
    def get_ChangeKind(self) -> win32more.Windows.UI.Notifications.UserNotificationChangedKind: ...
    @winrt_commethod(7)
    def get_UserNotificationId(self) -> UInt32: ...
    ChangeKind = property(get_ChangeKind, None)
    UserNotificationId = property(get_UserNotificationId, None)
class _KnownAdaptiveNotificationHints_Meta_(ComPtr.__class__):
    pass
class KnownAdaptiveNotificationHints(ComPtr, metaclass=_KnownAdaptiveNotificationHints_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.KnownAdaptiveNotificationHints'
    @winrt_classmethod
    def get_Style(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationHintsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Wrap(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationHintsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_MaxLines(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationHintsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_MinLines(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationHintsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TextStacking(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationHintsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Align(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationHintsStatics) -> WinRT_String: ...
    _KnownAdaptiveNotificationHints_Meta_.Align = property(get_Align, None)
    _KnownAdaptiveNotificationHints_Meta_.MaxLines = property(get_MaxLines, None)
    _KnownAdaptiveNotificationHints_Meta_.MinLines = property(get_MinLines, None)
    _KnownAdaptiveNotificationHints_Meta_.Style = property(get_Style, None)
    _KnownAdaptiveNotificationHints_Meta_.TextStacking = property(get_TextStacking, None)
    _KnownAdaptiveNotificationHints_Meta_.Wrap = property(get_Wrap, None)
class _KnownAdaptiveNotificationTextStyles_Meta_(ComPtr.__class__):
    pass
class KnownAdaptiveNotificationTextStyles(ComPtr, metaclass=_KnownAdaptiveNotificationTextStyles_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.KnownAdaptiveNotificationTextStyles'
    @winrt_classmethod
    def get_Caption(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Body(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Base(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Subtitle(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Title(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Subheader(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Header(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TitleNumeral(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SubheaderNumeral(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HeaderNumeral(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_CaptionSubtle(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BodySubtle(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BaseSubtle(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SubtitleSubtle(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TitleSubtle(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SubheaderSubtle(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SubheaderNumeralSubtle(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HeaderSubtle(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HeaderNumeralSubtle(cls: win32more.Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    _KnownAdaptiveNotificationTextStyles_Meta_.Base = property(get_Base, None)
    _KnownAdaptiveNotificationTextStyles_Meta_.BaseSubtle = property(get_BaseSubtle, None)
    _KnownAdaptiveNotificationTextStyles_Meta_.Body = property(get_Body, None)
    _KnownAdaptiveNotificationTextStyles_Meta_.BodySubtle = property(get_BodySubtle, None)
    _KnownAdaptiveNotificationTextStyles_Meta_.Caption = property(get_Caption, None)
    _KnownAdaptiveNotificationTextStyles_Meta_.CaptionSubtle = property(get_CaptionSubtle, None)
    _KnownAdaptiveNotificationTextStyles_Meta_.Header = property(get_Header, None)
    _KnownAdaptiveNotificationTextStyles_Meta_.HeaderNumeral = property(get_HeaderNumeral, None)
    _KnownAdaptiveNotificationTextStyles_Meta_.HeaderNumeralSubtle = property(get_HeaderNumeralSubtle, None)
    _KnownAdaptiveNotificationTextStyles_Meta_.HeaderSubtle = property(get_HeaderSubtle, None)
    _KnownAdaptiveNotificationTextStyles_Meta_.Subheader = property(get_Subheader, None)
    _KnownAdaptiveNotificationTextStyles_Meta_.SubheaderNumeral = property(get_SubheaderNumeral, None)
    _KnownAdaptiveNotificationTextStyles_Meta_.SubheaderNumeralSubtle = property(get_SubheaderNumeralSubtle, None)
    _KnownAdaptiveNotificationTextStyles_Meta_.SubheaderSubtle = property(get_SubheaderSubtle, None)
    _KnownAdaptiveNotificationTextStyles_Meta_.Subtitle = property(get_Subtitle, None)
    _KnownAdaptiveNotificationTextStyles_Meta_.SubtitleSubtle = property(get_SubtitleSubtle, None)
    _KnownAdaptiveNotificationTextStyles_Meta_.Title = property(get_Title, None)
    _KnownAdaptiveNotificationTextStyles_Meta_.TitleNumeral = property(get_TitleNumeral, None)
    _KnownAdaptiveNotificationTextStyles_Meta_.TitleSubtle = property(get_TitleSubtle, None)
class _KnownNotificationBindings_Meta_(ComPtr.__class__):
    pass
class KnownNotificationBindings(ComPtr, metaclass=_KnownNotificationBindings_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.KnownNotificationBindings'
    @winrt_classmethod
    def get_ToastGeneric(cls: win32more.Windows.UI.Notifications.IKnownNotificationBindingsStatics) -> WinRT_String: ...
    _KnownNotificationBindings_Meta_.ToastGeneric = property(get_ToastGeneric, None)
class Notification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.INotification
    _classid_ = 'Windows.UI.Notifications.Notification'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Notifications.Notification.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Notifications.Notification: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: win32more.Windows.UI.Notifications.INotification) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_ExpirationTime(self: win32more.Windows.UI.Notifications.INotification, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_Visual(self: win32more.Windows.UI.Notifications.INotification) -> win32more.Windows.UI.Notifications.NotificationVisual: ...
    @winrt_mixinmethod
    def put_Visual(self: win32more.Windows.UI.Notifications.INotification, value: win32more.Windows.UI.Notifications.NotificationVisual) -> Void: ...
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
    Visual = property(get_Visual, put_Visual)
class NotificationBinding(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.INotificationBinding
    _classid_ = 'Windows.UI.Notifications.NotificationBinding'
    @winrt_mixinmethod
    def get_Template(self: win32more.Windows.UI.Notifications.INotificationBinding) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Template(self: win32more.Windows.UI.Notifications.INotificationBinding, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.UI.Notifications.INotificationBinding) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: win32more.Windows.UI.Notifications.INotificationBinding, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Hints(self: win32more.Windows.UI.Notifications.INotificationBinding) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def GetTextElements(self: win32more.Windows.UI.Notifications.INotificationBinding) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Notifications.AdaptiveNotificationText]: ...
    Hints = property(get_Hints, None)
    Language = property(get_Language, put_Language)
    Template = property(get_Template, put_Template)
class NotificationData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.INotificationData
    _classid_ = 'Windows.UI.Notifications.NotificationData'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Notifications.NotificationData.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Notifications.NotificationData.CreateNotificationDataWithValues(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Notifications.NotificationData.CreateNotificationDataWithValuesAndSequenceNumber(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Notifications.NotificationData: ...
    @winrt_factorymethod
    def CreateNotificationDataWithValues(cls: win32more.Windows.UI.Notifications.INotificationDataFactory, initialValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> win32more.Windows.UI.Notifications.NotificationData: ...
    @winrt_factorymethod
    def CreateNotificationDataWithValuesAndSequenceNumber(cls: win32more.Windows.UI.Notifications.INotificationDataFactory, initialValues: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]], sequenceNumber: UInt32) -> win32more.Windows.UI.Notifications.NotificationData: ...
    @winrt_mixinmethod
    def get_Values(self: win32more.Windows.UI.Notifications.INotificationData) -> win32more.Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_SequenceNumber(self: win32more.Windows.UI.Notifications.INotificationData) -> UInt32: ...
    @winrt_mixinmethod
    def put_SequenceNumber(self: win32more.Windows.UI.Notifications.INotificationData, value: UInt32) -> Void: ...
    SequenceNumber = property(get_SequenceNumber, put_SequenceNumber)
    Values = property(get_Values, None)
class NotificationKinds(Enum, UInt32):
    Unknown = 0
    Toast = 1
class NotificationMirroring(Enum, Int32):
    Allowed = 0
    Disabled = 1
class NotificationSetting(Enum, Int32):
    Enabled = 0
    DisabledForApplication = 1
    DisabledForUser = 2
    DisabledByGroupPolicy = 3
    DisabledByManifest = 4
class NotificationUpdateResult(Enum, Int32):
    Succeeded = 0
    Failed = 1
    NotificationNotFound = 2
class NotificationVisual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.INotificationVisual
    _classid_ = 'Windows.UI.Notifications.NotificationVisual'
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.UI.Notifications.INotificationVisual) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: win32more.Windows.UI.Notifications.INotificationVisual, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Bindings(self: win32more.Windows.UI.Notifications.INotificationVisual) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Notifications.NotificationBinding]: ...
    @winrt_mixinmethod
    def GetBinding(self: win32more.Windows.UI.Notifications.INotificationVisual, templateName: WinRT_String) -> win32more.Windows.UI.Notifications.NotificationBinding: ...
    Bindings = property(get_Bindings, None)
    Language = property(get_Language, put_Language)
class PeriodicUpdateRecurrence(Enum, Int32):
    HalfHour = 0
    Hour = 1
    SixHours = 2
    TwelveHours = 3
    Daily = 4
class ScheduledTileNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IScheduledTileNotification
    _classid_ = 'Windows.UI.Notifications.ScheduledTileNotification'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Notifications.ScheduledTileNotification.CreateScheduledTileNotification(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateScheduledTileNotification(cls: win32more.Windows.UI.Notifications.IScheduledTileNotificationFactory, content: win32more.Windows.Data.Xml.Dom.XmlDocument, deliveryTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.UI.Notifications.ScheduledTileNotification: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.UI.Notifications.IScheduledTileNotification) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_mixinmethod
    def get_DeliveryTime(self: win32more.Windows.UI.Notifications.IScheduledTileNotification) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_ExpirationTime(self: win32more.Windows.UI.Notifications.IScheduledTileNotification, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: win32more.Windows.UI.Notifications.IScheduledTileNotification) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_Tag(self: win32more.Windows.UI.Notifications.IScheduledTileNotification, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: win32more.Windows.UI.Notifications.IScheduledTileNotification) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.UI.Notifications.IScheduledTileNotification, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Notifications.IScheduledTileNotification) -> WinRT_String: ...
    Content = property(get_Content, None)
    DeliveryTime = property(get_DeliveryTime, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
    Id = property(get_Id, put_Id)
    Tag = property(get_Tag, put_Tag)
class ScheduledToastNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IScheduledToastNotification
    _classid_ = 'Windows.UI.Notifications.ScheduledToastNotification'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Notifications.ScheduledToastNotification.CreateScheduledToastNotification(*args))
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.UI.Notifications.ScheduledToastNotification.CreateScheduledToastNotificationRecurring(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateScheduledToastNotification(cls: win32more.Windows.UI.Notifications.IScheduledToastNotificationFactory, content: win32more.Windows.Data.Xml.Dom.XmlDocument, deliveryTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.UI.Notifications.ScheduledToastNotification: ...
    @winrt_factorymethod
    def CreateScheduledToastNotificationRecurring(cls: win32more.Windows.UI.Notifications.IScheduledToastNotificationFactory, content: win32more.Windows.Data.Xml.Dom.XmlDocument, deliveryTime: win32more.Windows.Foundation.DateTime, snoozeInterval: win32more.Windows.Foundation.TimeSpan, maximumSnoozeCount: UInt32) -> win32more.Windows.UI.Notifications.ScheduledToastNotification: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.UI.Notifications.IScheduledToastNotification) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_mixinmethod
    def get_DeliveryTime(self: win32more.Windows.UI.Notifications.IScheduledToastNotification) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_SnoozeInterval(self: win32more.Windows.UI.Notifications.IScheduledToastNotification) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_MaximumSnoozeCount(self: win32more.Windows.UI.Notifications.IScheduledToastNotification) -> UInt32: ...
    @winrt_mixinmethod
    def put_Id(self: win32more.Windows.UI.Notifications.IScheduledToastNotification, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Notifications.IScheduledToastNotification) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Tag(self: win32more.Windows.UI.Notifications.IScheduledToastNotification2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: win32more.Windows.UI.Notifications.IScheduledToastNotification2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Group(self: win32more.Windows.UI.Notifications.IScheduledToastNotification2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Group(self: win32more.Windows.UI.Notifications.IScheduledToastNotification2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SuppressPopup(self: win32more.Windows.UI.Notifications.IScheduledToastNotification2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SuppressPopup(self: win32more.Windows.UI.Notifications.IScheduledToastNotification2) -> Boolean: ...
    @winrt_mixinmethod
    def get_NotificationMirroring(self: win32more.Windows.UI.Notifications.IScheduledToastNotification3) -> win32more.Windows.UI.Notifications.NotificationMirroring: ...
    @winrt_mixinmethod
    def put_NotificationMirroring(self: win32more.Windows.UI.Notifications.IScheduledToastNotification3, value: win32more.Windows.UI.Notifications.NotificationMirroring) -> Void: ...
    @winrt_mixinmethod
    def get_RemoteId(self: win32more.Windows.UI.Notifications.IScheduledToastNotification3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RemoteId(self: win32more.Windows.UI.Notifications.IScheduledToastNotification3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: win32more.Windows.UI.Notifications.IScheduledToastNotification4) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_ExpirationTime(self: win32more.Windows.UI.Notifications.IScheduledToastNotification4, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    Content = property(get_Content, None)
    DeliveryTime = property(get_DeliveryTime, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
    Group = property(get_Group, put_Group)
    Id = property(get_Id, put_Id)
    MaximumSnoozeCount = property(get_MaximumSnoozeCount, None)
    NotificationMirroring = property(get_NotificationMirroring, put_NotificationMirroring)
    RemoteId = property(get_RemoteId, put_RemoteId)
    SnoozeInterval = property(get_SnoozeInterval, None)
    SuppressPopup = property(get_SuppressPopup, put_SuppressPopup)
    Tag = property(get_Tag, put_Tag)
class ScheduledToastNotificationShowingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IScheduledToastNotificationShowingEventArgs
    _classid_ = 'Windows.UI.Notifications.ScheduledToastNotificationShowingEventArgs'
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Windows.UI.Notifications.IScheduledToastNotificationShowingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Windows.UI.Notifications.IScheduledToastNotificationShowingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ScheduledToastNotification(self: win32more.Windows.UI.Notifications.IScheduledToastNotificationShowingEventArgs) -> win32more.Windows.UI.Notifications.ScheduledToastNotification: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.Notifications.IScheduledToastNotificationShowingEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Cancel = property(get_Cancel, put_Cancel)
    ScheduledToastNotification = property(get_ScheduledToastNotification, None)
class ShownTileNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IShownTileNotification
    _classid_ = 'Windows.UI.Notifications.ShownTileNotification'
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.UI.Notifications.IShownTileNotification) -> WinRT_String: ...
    Arguments = property(get_Arguments, None)
class TileFlyoutNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.ITileFlyoutNotification
    _classid_ = 'Windows.UI.Notifications.TileFlyoutNotification'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Notifications.TileFlyoutNotification.CreateTileFlyoutNotification(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateTileFlyoutNotification(cls: win32more.Windows.UI.Notifications.ITileFlyoutNotificationFactory, content: win32more.Windows.Data.Xml.Dom.XmlDocument) -> win32more.Windows.UI.Notifications.TileFlyoutNotification: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.UI.Notifications.ITileFlyoutNotification) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_mixinmethod
    def put_ExpirationTime(self: win32more.Windows.UI.Notifications.ITileFlyoutNotification, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: win32more.Windows.UI.Notifications.ITileFlyoutNotification) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    Content = property(get_Content, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
class TileFlyoutTemplateType(Enum, Int32):
    TileFlyoutTemplate01 = 0
class TileFlyoutUpdateManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.TileFlyoutUpdateManager'
    @winrt_classmethod
    def CreateTileFlyoutUpdaterForApplication(cls: win32more.Windows.UI.Notifications.ITileFlyoutUpdateManagerStatics) -> win32more.Windows.UI.Notifications.TileFlyoutUpdater: ...
    @winrt_classmethod
    def CreateTileFlyoutUpdaterForApplicationWithId(cls: win32more.Windows.UI.Notifications.ITileFlyoutUpdateManagerStatics, applicationId: WinRT_String) -> win32more.Windows.UI.Notifications.TileFlyoutUpdater: ...
    @winrt_classmethod
    def CreateTileFlyoutUpdaterForSecondaryTile(cls: win32more.Windows.UI.Notifications.ITileFlyoutUpdateManagerStatics, tileId: WinRT_String) -> win32more.Windows.UI.Notifications.TileFlyoutUpdater: ...
    @winrt_classmethod
    def GetTemplateContent(cls: win32more.Windows.UI.Notifications.ITileFlyoutUpdateManagerStatics, type: win32more.Windows.UI.Notifications.TileFlyoutTemplateType) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
class TileFlyoutUpdater(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.ITileFlyoutUpdater
    _classid_ = 'Windows.UI.Notifications.TileFlyoutUpdater'
    @winrt_mixinmethod
    def Update(self: win32more.Windows.UI.Notifications.ITileFlyoutUpdater, notification: win32more.Windows.UI.Notifications.TileFlyoutNotification) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.UI.Notifications.ITileFlyoutUpdater) -> Void: ...
    @winrt_mixinmethod
    def StartPeriodicUpdate(self: win32more.Windows.UI.Notifications.ITileFlyoutUpdater, tileFlyoutContent: win32more.Windows.Foundation.Uri, requestedInterval: win32more.Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_mixinmethod
    def StartPeriodicUpdateAtTime(self: win32more.Windows.UI.Notifications.ITileFlyoutUpdater, tileFlyoutContent: win32more.Windows.Foundation.Uri, startTime: win32more.Windows.Foundation.DateTime, requestedInterval: win32more.Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_mixinmethod
    def StopPeriodicUpdate(self: win32more.Windows.UI.Notifications.ITileFlyoutUpdater) -> Void: ...
    @winrt_mixinmethod
    def get_Setting(self: win32more.Windows.UI.Notifications.ITileFlyoutUpdater) -> win32more.Windows.UI.Notifications.NotificationSetting: ...
    Setting = property(get_Setting, None)
class TileNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.ITileNotification
    _classid_ = 'Windows.UI.Notifications.TileNotification'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Notifications.TileNotification.CreateTileNotification(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateTileNotification(cls: win32more.Windows.UI.Notifications.ITileNotificationFactory, content: win32more.Windows.Data.Xml.Dom.XmlDocument) -> win32more.Windows.UI.Notifications.TileNotification: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.UI.Notifications.ITileNotification) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_mixinmethod
    def put_ExpirationTime(self: win32more.Windows.UI.Notifications.ITileNotification, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: win32more.Windows.UI.Notifications.ITileNotification) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_Tag(self: win32more.Windows.UI.Notifications.ITileNotification, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: win32more.Windows.UI.Notifications.ITileNotification) -> WinRT_String: ...
    Content = property(get_Content, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
    Tag = property(get_Tag, put_Tag)
class TileTemplateType(Enum, Int32):
    TileSquareImage = 0
    TileSquareBlock = 1
    TileSquareText01 = 2
    TileSquareText02 = 3
    TileSquareText03 = 4
    TileSquareText04 = 5
    TileSquarePeekImageAndText01 = 6
    TileSquarePeekImageAndText02 = 7
    TileSquarePeekImageAndText03 = 8
    TileSquarePeekImageAndText04 = 9
    TileWideImage = 10
    TileWideImageCollection = 11
    TileWideImageAndText01 = 12
    TileWideImageAndText02 = 13
    TileWideBlockAndText01 = 14
    TileWideBlockAndText02 = 15
    TileWidePeekImageCollection01 = 16
    TileWidePeekImageCollection02 = 17
    TileWidePeekImageCollection03 = 18
    TileWidePeekImageCollection04 = 19
    TileWidePeekImageCollection05 = 20
    TileWidePeekImageCollection06 = 21
    TileWidePeekImageAndText01 = 22
    TileWidePeekImageAndText02 = 23
    TileWidePeekImage01 = 24
    TileWidePeekImage02 = 25
    TileWidePeekImage03 = 26
    TileWidePeekImage04 = 27
    TileWidePeekImage05 = 28
    TileWidePeekImage06 = 29
    TileWideSmallImageAndText01 = 30
    TileWideSmallImageAndText02 = 31
    TileWideSmallImageAndText03 = 32
    TileWideSmallImageAndText04 = 33
    TileWideSmallImageAndText05 = 34
    TileWideText01 = 35
    TileWideText02 = 36
    TileWideText03 = 37
    TileWideText04 = 38
    TileWideText05 = 39
    TileWideText06 = 40
    TileWideText07 = 41
    TileWideText08 = 42
    TileWideText09 = 43
    TileWideText10 = 44
    TileWideText11 = 45
    TileSquare150x150Image = 0
    TileSquare150x150Block = 1
    TileSquare150x150Text01 = 2
    TileSquare150x150Text02 = 3
    TileSquare150x150Text03 = 4
    TileSquare150x150Text04 = 5
    TileSquare150x150PeekImageAndText01 = 6
    TileSquare150x150PeekImageAndText02 = 7
    TileSquare150x150PeekImageAndText03 = 8
    TileSquare150x150PeekImageAndText04 = 9
    TileWide310x150Image = 10
    TileWide310x150ImageCollection = 11
    TileWide310x150ImageAndText01 = 12
    TileWide310x150ImageAndText02 = 13
    TileWide310x150BlockAndText01 = 14
    TileWide310x150BlockAndText02 = 15
    TileWide310x150PeekImageCollection01 = 16
    TileWide310x150PeekImageCollection02 = 17
    TileWide310x150PeekImageCollection03 = 18
    TileWide310x150PeekImageCollection04 = 19
    TileWide310x150PeekImageCollection05 = 20
    TileWide310x150PeekImageCollection06 = 21
    TileWide310x150PeekImageAndText01 = 22
    TileWide310x150PeekImageAndText02 = 23
    TileWide310x150PeekImage01 = 24
    TileWide310x150PeekImage02 = 25
    TileWide310x150PeekImage03 = 26
    TileWide310x150PeekImage04 = 27
    TileWide310x150PeekImage05 = 28
    TileWide310x150PeekImage06 = 29
    TileWide310x150SmallImageAndText01 = 30
    TileWide310x150SmallImageAndText02 = 31
    TileWide310x150SmallImageAndText03 = 32
    TileWide310x150SmallImageAndText04 = 33
    TileWide310x150SmallImageAndText05 = 34
    TileWide310x150Text01 = 35
    TileWide310x150Text02 = 36
    TileWide310x150Text03 = 37
    TileWide310x150Text04 = 38
    TileWide310x150Text05 = 39
    TileWide310x150Text06 = 40
    TileWide310x150Text07 = 41
    TileWide310x150Text08 = 42
    TileWide310x150Text09 = 43
    TileWide310x150Text10 = 44
    TileWide310x150Text11 = 45
    TileSquare310x310BlockAndText01 = 46
    TileSquare310x310BlockAndText02 = 47
    TileSquare310x310Image = 48
    TileSquare310x310ImageAndText01 = 49
    TileSquare310x310ImageAndText02 = 50
    TileSquare310x310ImageAndTextOverlay01 = 51
    TileSquare310x310ImageAndTextOverlay02 = 52
    TileSquare310x310ImageAndTextOverlay03 = 53
    TileSquare310x310ImageCollectionAndText01 = 54
    TileSquare310x310ImageCollectionAndText02 = 55
    TileSquare310x310ImageCollection = 56
    TileSquare310x310SmallImagesAndTextList01 = 57
    TileSquare310x310SmallImagesAndTextList02 = 58
    TileSquare310x310SmallImagesAndTextList03 = 59
    TileSquare310x310SmallImagesAndTextList04 = 60
    TileSquare310x310Text01 = 61
    TileSquare310x310Text02 = 62
    TileSquare310x310Text03 = 63
    TileSquare310x310Text04 = 64
    TileSquare310x310Text05 = 65
    TileSquare310x310Text06 = 66
    TileSquare310x310Text07 = 67
    TileSquare310x310Text08 = 68
    TileSquare310x310TextList01 = 69
    TileSquare310x310TextList02 = 70
    TileSquare310x310TextList03 = 71
    TileSquare310x310SmallImageAndText01 = 72
    TileSquare310x310SmallImagesAndTextList05 = 73
    TileSquare310x310Text09 = 74
    TileSquare71x71IconWithBadge = 75
    TileSquare150x150IconWithBadge = 76
    TileWide310x150IconWithBadgeAndText = 77
    TileSquare71x71Image = 78
    TileTall150x310Image = 79
class TileUpdateManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.TileUpdateManager'
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.UI.Notifications.ITileUpdateManagerStatics2, user: win32more.Windows.System.User) -> win32more.Windows.UI.Notifications.TileUpdateManagerForUser: ...
    @winrt_classmethod
    def CreateTileUpdaterForApplication(cls: win32more.Windows.UI.Notifications.ITileUpdateManagerStatics) -> win32more.Windows.UI.Notifications.TileUpdater: ...
    @winrt_classmethod
    def CreateTileUpdaterForApplicationWithId(cls: win32more.Windows.UI.Notifications.ITileUpdateManagerStatics, applicationId: WinRT_String) -> win32more.Windows.UI.Notifications.TileUpdater: ...
    @winrt_classmethod
    def CreateTileUpdaterForSecondaryTile(cls: win32more.Windows.UI.Notifications.ITileUpdateManagerStatics, tileId: WinRT_String) -> win32more.Windows.UI.Notifications.TileUpdater: ...
    @winrt_classmethod
    def GetTemplateContent(cls: win32more.Windows.UI.Notifications.ITileUpdateManagerStatics, type: win32more.Windows.UI.Notifications.TileTemplateType) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
class TileUpdateManagerForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.ITileUpdateManagerForUser
    _classid_ = 'Windows.UI.Notifications.TileUpdateManagerForUser'
    @winrt_mixinmethod
    def CreateTileUpdaterForApplication(self: win32more.Windows.UI.Notifications.ITileUpdateManagerForUser) -> win32more.Windows.UI.Notifications.TileUpdater: ...
    @winrt_mixinmethod
    def CreateTileUpdaterForApplicationWithId(self: win32more.Windows.UI.Notifications.ITileUpdateManagerForUser, applicationId: WinRT_String) -> win32more.Windows.UI.Notifications.TileUpdater: ...
    @winrt_mixinmethod
    def CreateTileUpdaterForSecondaryTile(self: win32more.Windows.UI.Notifications.ITileUpdateManagerForUser, tileId: WinRT_String) -> win32more.Windows.UI.Notifications.TileUpdater: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.UI.Notifications.ITileUpdateManagerForUser) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class TileUpdater(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.ITileUpdater
    _classid_ = 'Windows.UI.Notifications.TileUpdater'
    @winrt_mixinmethod
    def Update(self: win32more.Windows.UI.Notifications.ITileUpdater, notification: win32more.Windows.UI.Notifications.TileNotification) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.UI.Notifications.ITileUpdater) -> Void: ...
    @winrt_mixinmethod
    def EnableNotificationQueue(self: win32more.Windows.UI.Notifications.ITileUpdater, enable: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Setting(self: win32more.Windows.UI.Notifications.ITileUpdater) -> win32more.Windows.UI.Notifications.NotificationSetting: ...
    @winrt_mixinmethod
    def AddToSchedule(self: win32more.Windows.UI.Notifications.ITileUpdater, scheduledTile: win32more.Windows.UI.Notifications.ScheduledTileNotification) -> Void: ...
    @winrt_mixinmethod
    def RemoveFromSchedule(self: win32more.Windows.UI.Notifications.ITileUpdater, scheduledTile: win32more.Windows.UI.Notifications.ScheduledTileNotification) -> Void: ...
    @winrt_mixinmethod
    def GetScheduledTileNotifications(self: win32more.Windows.UI.Notifications.ITileUpdater) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Notifications.ScheduledTileNotification]: ...
    @winrt_mixinmethod
    def StartPeriodicUpdate(self: win32more.Windows.UI.Notifications.ITileUpdater, tileContent: win32more.Windows.Foundation.Uri, requestedInterval: win32more.Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_mixinmethod
    def StartPeriodicUpdateAtTime(self: win32more.Windows.UI.Notifications.ITileUpdater, tileContent: win32more.Windows.Foundation.Uri, startTime: win32more.Windows.Foundation.DateTime, requestedInterval: win32more.Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_mixinmethod
    def StopPeriodicUpdate(self: win32more.Windows.UI.Notifications.ITileUpdater) -> Void: ...
    @winrt_mixinmethod
    def StartPeriodicUpdateBatch(self: win32more.Windows.UI.Notifications.ITileUpdater, tileContents: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Uri], requestedInterval: win32more.Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_mixinmethod
    def StartPeriodicUpdateBatchAtTime(self: win32more.Windows.UI.Notifications.ITileUpdater, tileContents: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Uri], startTime: win32more.Windows.Foundation.DateTime, requestedInterval: win32more.Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_mixinmethod
    def EnableNotificationQueueForSquare150x150(self: win32more.Windows.UI.Notifications.ITileUpdater2, enable: Boolean) -> Void: ...
    @winrt_mixinmethod
    def EnableNotificationQueueForWide310x150(self: win32more.Windows.UI.Notifications.ITileUpdater2, enable: Boolean) -> Void: ...
    @winrt_mixinmethod
    def EnableNotificationQueueForSquare310x310(self: win32more.Windows.UI.Notifications.ITileUpdater2, enable: Boolean) -> Void: ...
    Setting = property(get_Setting, None)
class ToastActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IToastActivatedEventArgs
    _classid_ = 'Windows.UI.Notifications.ToastActivatedEventArgs'
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.UI.Notifications.IToastActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserInput(self: win32more.Windows.UI.Notifications.IToastActivatedEventArgs2) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Arguments = property(get_Arguments, None)
    UserInput = property(get_UserInput, None)
class ToastCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IToastCollection
    _classid_ = 'Windows.UI.Notifications.ToastCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.UI.Notifications.ToastCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Notifications.IToastCollectionFactory, collectionId: WinRT_String, displayName: WinRT_String, launchArgs: WinRT_String, iconUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.Notifications.ToastCollection: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Notifications.IToastCollection) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.UI.Notifications.IToastCollection) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.UI.Notifications.IToastCollection, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_LaunchArgs(self: win32more.Windows.UI.Notifications.IToastCollection) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LaunchArgs(self: win32more.Windows.UI.Notifications.IToastCollection, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Icon(self: win32more.Windows.UI.Notifications.IToastCollection) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Icon(self: win32more.Windows.UI.Notifications.IToastCollection, value: win32more.Windows.Foundation.Uri) -> Void: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    Icon = property(get_Icon, put_Icon)
    Id = property(get_Id, None)
    LaunchArgs = property(get_LaunchArgs, put_LaunchArgs)
class ToastCollectionManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IToastCollectionManager
    _classid_ = 'Windows.UI.Notifications.ToastCollectionManager'
    @winrt_mixinmethod
    def SaveToastCollectionAsync(self: win32more.Windows.UI.Notifications.IToastCollectionManager, collection: win32more.Windows.UI.Notifications.ToastCollection) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def FindAllToastCollectionsAsync(self: win32more.Windows.UI.Notifications.IToastCollectionManager) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Notifications.ToastCollection]]: ...
    @winrt_mixinmethod
    def GetToastCollectionAsync(self: win32more.Windows.UI.Notifications.IToastCollectionManager, collectionId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Notifications.ToastCollection]: ...
    @winrt_mixinmethod
    def RemoveToastCollectionAsync(self: win32more.Windows.UI.Notifications.IToastCollectionManager, collectionId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RemoveAllToastCollectionsAsync(self: win32more.Windows.UI.Notifications.IToastCollectionManager) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.UI.Notifications.IToastCollectionManager) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_AppId(self: win32more.Windows.UI.Notifications.IToastCollectionManager) -> WinRT_String: ...
    AppId = property(get_AppId, None)
    User = property(get_User, None)
class ToastDismissalReason(Enum, Int32):
    UserCanceled = 0
    ApplicationHidden = 1
    TimedOut = 2
class ToastDismissedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IToastDismissedEventArgs
    _classid_ = 'Windows.UI.Notifications.ToastDismissedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.UI.Notifications.IToastDismissedEventArgs) -> win32more.Windows.UI.Notifications.ToastDismissalReason: ...
    Reason = property(get_Reason, None)
class ToastFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IToastFailedEventArgs
    _classid_ = 'Windows.UI.Notifications.ToastFailedEventArgs'
    @winrt_mixinmethod
    def get_ErrorCode(self: win32more.Windows.UI.Notifications.IToastFailedEventArgs) -> win32more.Windows.Foundation.HResult: ...
    ErrorCode = property(get_ErrorCode, None)
class ToastHistoryChangedType(Enum, Int32):
    Cleared = 0
    Removed = 1
    Expired = 2
    Added = 3
class ToastNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IToastNotification
    _classid_ = 'Windows.UI.Notifications.ToastNotification'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Notifications.ToastNotification.CreateToastNotification(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateToastNotification(cls: win32more.Windows.UI.Notifications.IToastNotificationFactory, content: win32more.Windows.Data.Xml.Dom.XmlDocument) -> win32more.Windows.UI.Notifications.ToastNotification: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.UI.Notifications.IToastNotification) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_mixinmethod
    def put_ExpirationTime(self: win32more.Windows.UI.Notifications.IToastNotification, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: win32more.Windows.UI.Notifications.IToastNotification) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def add_Dismissed(self: win32more.Windows.UI.Notifications.IToastNotification, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Notifications.ToastNotification, win32more.Windows.UI.Notifications.ToastDismissedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Dismissed(self: win32more.Windows.UI.Notifications.IToastNotification, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Activated(self: win32more.Windows.UI.Notifications.IToastNotification, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Notifications.ToastNotification, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Activated(self: win32more.Windows.UI.Notifications.IToastNotification, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Failed(self: win32more.Windows.UI.Notifications.IToastNotification, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Notifications.ToastNotification, win32more.Windows.UI.Notifications.ToastFailedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Failed(self: win32more.Windows.UI.Notifications.IToastNotification, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_Tag(self: win32more.Windows.UI.Notifications.IToastNotification2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: win32more.Windows.UI.Notifications.IToastNotification2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Group(self: win32more.Windows.UI.Notifications.IToastNotification2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Group(self: win32more.Windows.UI.Notifications.IToastNotification2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SuppressPopup(self: win32more.Windows.UI.Notifications.IToastNotification2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SuppressPopup(self: win32more.Windows.UI.Notifications.IToastNotification2) -> Boolean: ...
    @winrt_mixinmethod
    def get_NotificationMirroring(self: win32more.Windows.UI.Notifications.IToastNotification3) -> win32more.Windows.UI.Notifications.NotificationMirroring: ...
    @winrt_mixinmethod
    def put_NotificationMirroring(self: win32more.Windows.UI.Notifications.IToastNotification3, value: win32more.Windows.UI.Notifications.NotificationMirroring) -> Void: ...
    @winrt_mixinmethod
    def get_RemoteId(self: win32more.Windows.UI.Notifications.IToastNotification3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RemoteId(self: win32more.Windows.UI.Notifications.IToastNotification3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.UI.Notifications.IToastNotification4) -> win32more.Windows.UI.Notifications.NotificationData: ...
    @winrt_mixinmethod
    def put_Data(self: win32more.Windows.UI.Notifications.IToastNotification4, value: win32more.Windows.UI.Notifications.NotificationData) -> Void: ...
    @winrt_mixinmethod
    def get_Priority(self: win32more.Windows.UI.Notifications.IToastNotification4) -> win32more.Windows.UI.Notifications.ToastNotificationPriority: ...
    @winrt_mixinmethod
    def put_Priority(self: win32more.Windows.UI.Notifications.IToastNotification4, value: win32more.Windows.UI.Notifications.ToastNotificationPriority) -> Void: ...
    @winrt_mixinmethod
    def get_ExpiresOnReboot(self: win32more.Windows.UI.Notifications.IToastNotification6) -> Boolean: ...
    @winrt_mixinmethod
    def put_ExpiresOnReboot(self: win32more.Windows.UI.Notifications.IToastNotification6, value: Boolean) -> Void: ...
    Content = property(get_Content, None)
    Data = property(get_Data, put_Data)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
    ExpiresOnReboot = property(get_ExpiresOnReboot, put_ExpiresOnReboot)
    Group = property(get_Group, put_Group)
    NotificationMirroring = property(get_NotificationMirroring, put_NotificationMirroring)
    Priority = property(get_Priority, put_Priority)
    RemoteId = property(get_RemoteId, put_RemoteId)
    SuppressPopup = property(get_SuppressPopup, put_SuppressPopup)
    Tag = property(get_Tag, put_Tag)
    Dismissed = event()
    Activated = event()
    Failed = event()
class ToastNotificationActionTriggerDetail(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IToastNotificationActionTriggerDetail
    _classid_ = 'Windows.UI.Notifications.ToastNotificationActionTriggerDetail'
    @winrt_mixinmethod
    def get_Argument(self: win32more.Windows.UI.Notifications.IToastNotificationActionTriggerDetail) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserInput(self: win32more.Windows.UI.Notifications.IToastNotificationActionTriggerDetail) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Argument = property(get_Argument, None)
    UserInput = property(get_UserInput, None)
class ToastNotificationHistory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IToastNotificationHistory
    _classid_ = 'Windows.UI.Notifications.ToastNotificationHistory'
    @winrt_mixinmethod
    def GetHistory(self: win32more.Windows.UI.Notifications.IToastNotificationHistory2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Notifications.ToastNotification]: ...
    @winrt_mixinmethod
    def GetHistoryWithId(self: win32more.Windows.UI.Notifications.IToastNotificationHistory2, applicationId: WinRT_String) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Notifications.ToastNotification]: ...
    @winrt_mixinmethod
    def RemoveGroup(self: win32more.Windows.UI.Notifications.IToastNotificationHistory, group: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RemoveGroupWithId(self: win32more.Windows.UI.Notifications.IToastNotificationHistory, group: WinRT_String, applicationId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RemoveGroupedTagWithId(self: win32more.Windows.UI.Notifications.IToastNotificationHistory, tag: WinRT_String, group: WinRT_String, applicationId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RemoveGroupedTag(self: win32more.Windows.UI.Notifications.IToastNotificationHistory, tag: WinRT_String, group: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Remove(self: win32more.Windows.UI.Notifications.IToastNotificationHistory, tag: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.UI.Notifications.IToastNotificationHistory) -> Void: ...
    @winrt_mixinmethod
    def ClearWithId(self: win32more.Windows.UI.Notifications.IToastNotificationHistory, applicationId: WinRT_String) -> Void: ...
class ToastNotificationHistoryChangedTriggerDetail(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IToastNotificationHistoryChangedTriggerDetail
    _classid_ = 'Windows.UI.Notifications.ToastNotificationHistoryChangedTriggerDetail'
    @winrt_mixinmethod
    def get_ChangeType(self: win32more.Windows.UI.Notifications.IToastNotificationHistoryChangedTriggerDetail) -> win32more.Windows.UI.Notifications.ToastHistoryChangedType: ...
    @winrt_mixinmethod
    def get_CollectionId(self: win32more.Windows.UI.Notifications.IToastNotificationHistoryChangedTriggerDetail2) -> WinRT_String: ...
    ChangeType = property(get_ChangeType, None)
    CollectionId = property(get_CollectionId, None)
class _ToastNotificationManager_Meta_(ComPtr.__class__):
    pass
class ToastNotificationManager(ComPtr, metaclass=_ToastNotificationManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.ToastNotificationManager'
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.UI.Notifications.IToastNotificationManagerStatics5) -> win32more.Windows.UI.Notifications.ToastNotificationManagerForUser: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.UI.Notifications.IToastNotificationManagerStatics4, user: win32more.Windows.System.User) -> win32more.Windows.UI.Notifications.ToastNotificationManagerForUser: ...
    @winrt_classmethod
    def ConfigureNotificationMirroring(cls: win32more.Windows.UI.Notifications.IToastNotificationManagerStatics4, value: win32more.Windows.UI.Notifications.NotificationMirroring) -> Void: ...
    @winrt_classmethod
    def get_History(cls: win32more.Windows.UI.Notifications.IToastNotificationManagerStatics2) -> win32more.Windows.UI.Notifications.ToastNotificationHistory: ...
    @winrt_classmethod
    def CreateToastNotifier(cls: win32more.Windows.UI.Notifications.IToastNotificationManagerStatics) -> win32more.Windows.UI.Notifications.ToastNotifier: ...
    @winrt_classmethod
    def CreateToastNotifierWithId(cls: win32more.Windows.UI.Notifications.IToastNotificationManagerStatics, applicationId: WinRT_String) -> win32more.Windows.UI.Notifications.ToastNotifier: ...
    @winrt_classmethod
    def GetTemplateContent(cls: win32more.Windows.UI.Notifications.IToastNotificationManagerStatics, type: win32more.Windows.UI.Notifications.ToastTemplateType) -> win32more.Windows.Data.Xml.Dom.XmlDocument: ...
    _ToastNotificationManager_Meta_.History = property(get_History, None)
class ToastNotificationManagerForUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IToastNotificationManagerForUser
    _classid_ = 'Windows.UI.Notifications.ToastNotificationManagerForUser'
    @winrt_mixinmethod
    def CreateToastNotifier(self: win32more.Windows.UI.Notifications.IToastNotificationManagerForUser) -> win32more.Windows.UI.Notifications.ToastNotifier: ...
    @winrt_mixinmethod
    def CreateToastNotifierWithId(self: win32more.Windows.UI.Notifications.IToastNotificationManagerForUser, applicationId: WinRT_String) -> win32more.Windows.UI.Notifications.ToastNotifier: ...
    @winrt_mixinmethod
    def get_History(self: win32more.Windows.UI.Notifications.IToastNotificationManagerForUser) -> win32more.Windows.UI.Notifications.ToastNotificationHistory: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.UI.Notifications.IToastNotificationManagerForUser) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def GetToastNotifierForToastCollectionIdAsync(self: win32more.Windows.UI.Notifications.IToastNotificationManagerForUser2, collectionId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Notifications.ToastNotifier]: ...
    @winrt_mixinmethod
    def GetHistoryForToastCollectionIdAsync(self: win32more.Windows.UI.Notifications.IToastNotificationManagerForUser2, collectionId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.Notifications.ToastNotificationHistory]: ...
    @winrt_mixinmethod
    def GetToastCollectionManager(self: win32more.Windows.UI.Notifications.IToastNotificationManagerForUser2) -> win32more.Windows.UI.Notifications.ToastCollectionManager: ...
    @winrt_mixinmethod
    def GetToastCollectionManagerWithAppId(self: win32more.Windows.UI.Notifications.IToastNotificationManagerForUser2, appId: WinRT_String) -> win32more.Windows.UI.Notifications.ToastCollectionManager: ...
    @winrt_mixinmethod
    def get_NotificationMode(self: win32more.Windows.UI.Notifications.IToastNotificationManagerForUser3) -> win32more.Windows.UI.Notifications.ToastNotificationMode: ...
    @winrt_mixinmethod
    def add_NotificationModeChanged(self: win32more.Windows.UI.Notifications.IToastNotificationManagerForUser3, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Notifications.ToastNotificationManagerForUser, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NotificationModeChanged(self: win32more.Windows.UI.Notifications.IToastNotificationManagerForUser3, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    History = property(get_History, None)
    NotificationMode = property(get_NotificationMode, None)
    User = property(get_User, None)
    NotificationModeChanged = event()
class ToastNotificationMode(Enum, Int32):
    Unrestricted = 0
    PriorityOnly = 1
    AlarmsOnly = 2
class ToastNotificationPriority(Enum, Int32):
    Default = 0
    High = 1
class ToastNotifier(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IToastNotifier
    _classid_ = 'Windows.UI.Notifications.ToastNotifier'
    @winrt_mixinmethod
    def Show(self: win32more.Windows.UI.Notifications.IToastNotifier, notification: win32more.Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_mixinmethod
    def Hide(self: win32more.Windows.UI.Notifications.IToastNotifier, notification: win32more.Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_mixinmethod
    def get_Setting(self: win32more.Windows.UI.Notifications.IToastNotifier) -> win32more.Windows.UI.Notifications.NotificationSetting: ...
    @winrt_mixinmethod
    def AddToSchedule(self: win32more.Windows.UI.Notifications.IToastNotifier, scheduledToast: win32more.Windows.UI.Notifications.ScheduledToastNotification) -> Void: ...
    @winrt_mixinmethod
    def RemoveFromSchedule(self: win32more.Windows.UI.Notifications.IToastNotifier, scheduledToast: win32more.Windows.UI.Notifications.ScheduledToastNotification) -> Void: ...
    @winrt_mixinmethod
    def GetScheduledToastNotifications(self: win32more.Windows.UI.Notifications.IToastNotifier) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Notifications.ScheduledToastNotification]: ...
    @winrt_mixinmethod
    def UpdateWithTagAndGroup(self: win32more.Windows.UI.Notifications.IToastNotifier2, data: win32more.Windows.UI.Notifications.NotificationData, tag: WinRT_String, group: WinRT_String) -> win32more.Windows.UI.Notifications.NotificationUpdateResult: ...
    @winrt_mixinmethod
    def UpdateWithTag(self: win32more.Windows.UI.Notifications.IToastNotifier2, data: win32more.Windows.UI.Notifications.NotificationData, tag: WinRT_String) -> win32more.Windows.UI.Notifications.NotificationUpdateResult: ...
    @winrt_mixinmethod
    def add_ScheduledToastNotificationShowing(self: win32more.Windows.UI.Notifications.IToastNotifier3, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Notifications.ToastNotifier, win32more.Windows.UI.Notifications.ScheduledToastNotificationShowingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScheduledToastNotificationShowing(self: win32more.Windows.UI.Notifications.IToastNotifier3, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Setting = property(get_Setting, None)
    ScheduledToastNotificationShowing = event()
class ToastTemplateType(Enum, Int32):
    ToastImageAndText01 = 0
    ToastImageAndText02 = 1
    ToastImageAndText03 = 2
    ToastImageAndText04 = 3
    ToastText01 = 4
    ToastText02 = 5
    ToastText03 = 6
    ToastText04 = 7
class UserNotification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IUserNotification
    _classid_ = 'Windows.UI.Notifications.UserNotification'
    @winrt_mixinmethod
    def get_Notification(self: win32more.Windows.UI.Notifications.IUserNotification) -> win32more.Windows.UI.Notifications.Notification: ...
    @winrt_mixinmethod
    def get_AppInfo(self: win32more.Windows.UI.Notifications.IUserNotification) -> win32more.Windows.ApplicationModel.AppInfo: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Notifications.IUserNotification) -> UInt32: ...
    @winrt_mixinmethod
    def get_CreationTime(self: win32more.Windows.UI.Notifications.IUserNotification) -> win32more.Windows.Foundation.DateTime: ...
    AppInfo = property(get_AppInfo, None)
    CreationTime = property(get_CreationTime, None)
    Id = property(get_Id, None)
    Notification = property(get_Notification, None)
class UserNotificationChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Notifications.IUserNotificationChangedEventArgs
    _classid_ = 'Windows.UI.Notifications.UserNotificationChangedEventArgs'
    @winrt_mixinmethod
    def get_ChangeKind(self: win32more.Windows.UI.Notifications.IUserNotificationChangedEventArgs) -> win32more.Windows.UI.Notifications.UserNotificationChangedKind: ...
    @winrt_mixinmethod
    def get_UserNotificationId(self: win32more.Windows.UI.Notifications.IUserNotificationChangedEventArgs) -> UInt32: ...
    ChangeKind = property(get_ChangeKind, None)
    UserNotificationId = property(get_UserNotificationId, None)
class UserNotificationChangedKind(Enum, Int32):
    Added = 0
    Removed = 1


make_ready(__name__)
