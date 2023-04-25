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
import Windows.ApplicationModel
import Windows.Data.Xml.Dom
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.System
import Windows.UI.Notifications
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
AdaptiveNotificationContentKind = Int32
AdaptiveNotificationContentKind_Text: AdaptiveNotificationContentKind = 0
class AdaptiveNotificationText(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.AdaptiveNotificationText'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Notifications.AdaptiveNotificationText: ...
    @winrt_mixinmethod
    def get_Text(self: Windows.UI.Notifications.IAdaptiveNotificationText) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: Windows.UI.Notifications.IAdaptiveNotificationText, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.UI.Notifications.IAdaptiveNotificationText) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: Windows.UI.Notifications.IAdaptiveNotificationText, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.UI.Notifications.IAdaptiveNotificationContent) -> Windows.UI.Notifications.AdaptiveNotificationContentKind: ...
    @winrt_mixinmethod
    def get_Hints(self: Windows.UI.Notifications.IAdaptiveNotificationContent) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    Text = property(get_Text, put_Text)
    Language = property(get_Language, put_Language)
    Kind = property(get_Kind, None)
    Hints = property(get_Hints, None)
class BadgeNotification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.BadgeNotification'
    @winrt_factorymethod
    def CreateBadgeNotification(cls: Windows.UI.Notifications.IBadgeNotificationFactory, content: Windows.Data.Xml.Dom.XmlDocument) -> Windows.UI.Notifications.BadgeNotification: ...
    @winrt_mixinmethod
    def get_Content(self: Windows.UI.Notifications.IBadgeNotification) -> Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_mixinmethod
    def put_ExpirationTime(self: Windows.UI.Notifications.IBadgeNotification, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: Windows.UI.Notifications.IBadgeNotification) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    Content = property(get_Content, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
BadgeTemplateType = Int32
BadgeTemplateType_BadgeGlyph: BadgeTemplateType = 0
BadgeTemplateType_BadgeNumber: BadgeTemplateType = 1
class BadgeUpdateManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.BadgeUpdateManager'
    @winrt_classmethod
    def GetForUser(cls: Windows.UI.Notifications.IBadgeUpdateManagerStatics2, user: Windows.System.User) -> Windows.UI.Notifications.BadgeUpdateManagerForUser: ...
    @winrt_classmethod
    def CreateBadgeUpdaterForApplication(cls: Windows.UI.Notifications.IBadgeUpdateManagerStatics) -> Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_classmethod
    def CreateBadgeUpdaterForApplicationWithId(cls: Windows.UI.Notifications.IBadgeUpdateManagerStatics, applicationId: WinRT_String) -> Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_classmethod
    def CreateBadgeUpdaterForSecondaryTile(cls: Windows.UI.Notifications.IBadgeUpdateManagerStatics, tileId: WinRT_String) -> Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_classmethod
    def GetTemplateContent(cls: Windows.UI.Notifications.IBadgeUpdateManagerStatics, type: Windows.UI.Notifications.BadgeTemplateType) -> Windows.Data.Xml.Dom.XmlDocument: ...
class BadgeUpdateManagerForUser(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.BadgeUpdateManagerForUser'
    @winrt_mixinmethod
    def CreateBadgeUpdaterForApplication(self: Windows.UI.Notifications.IBadgeUpdateManagerForUser) -> Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_mixinmethod
    def CreateBadgeUpdaterForApplicationWithId(self: Windows.UI.Notifications.IBadgeUpdateManagerForUser, applicationId: WinRT_String) -> Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_mixinmethod
    def CreateBadgeUpdaterForSecondaryTile(self: Windows.UI.Notifications.IBadgeUpdateManagerForUser, tileId: WinRT_String) -> Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_mixinmethod
    def get_User(self: Windows.UI.Notifications.IBadgeUpdateManagerForUser) -> Windows.System.User: ...
    User = property(get_User, None)
class BadgeUpdater(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.BadgeUpdater'
    @winrt_mixinmethod
    def Update(self: Windows.UI.Notifications.IBadgeUpdater, notification: Windows.UI.Notifications.BadgeNotification) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.UI.Notifications.IBadgeUpdater) -> Void: ...
    @winrt_mixinmethod
    def StartPeriodicUpdate(self: Windows.UI.Notifications.IBadgeUpdater, badgeContent: Windows.Foundation.Uri, requestedInterval: Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_mixinmethod
    def StartPeriodicUpdateAtTime(self: Windows.UI.Notifications.IBadgeUpdater, badgeContent: Windows.Foundation.Uri, startTime: Windows.Foundation.DateTime, requestedInterval: Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_mixinmethod
    def StopPeriodicUpdate(self: Windows.UI.Notifications.IBadgeUpdater) -> Void: ...
class IAdaptiveNotificationContent(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('eb0dbe66-7448-448d-9d-b8-d7-8a-cd-2a-bb-a9')
    @winrt_commethod(6)
    def get_Kind(self) -> Windows.UI.Notifications.AdaptiveNotificationContentKind: ...
    @winrt_commethod(7)
    def get_Hints(self) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    Kind = property(get_Kind, None)
    Hints = property(get_Hints, None)
class IAdaptiveNotificationText(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('46d4a3be-609a-4326-a4-0b-bf-de-87-20-34-a3')
    @winrt_commethod(6)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Text(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Language(self, value: WinRT_String) -> Void: ...
    Text = property(get_Text, put_Text)
    Language = property(get_Language, put_Language)
class IBadgeNotification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('075cb4ca-d08a-4e2f-92-33-7e-28-9c-1f-77-22')
    @winrt_commethod(6)
    def get_Content(self) -> Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_commethod(7)
    def put_ExpirationTime(self, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(8)
    def get_ExpirationTime(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    Content = property(get_Content, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
class IBadgeNotificationFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('edf255ce-0618-4d59-94-8a-5a-61-04-0c-52-f9')
    @winrt_commethod(6)
    def CreateBadgeNotification(self, content: Windows.Data.Xml.Dom.XmlDocument) -> Windows.UI.Notifications.BadgeNotification: ...
class IBadgeUpdateManagerForUser(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('996b21bc-0386-44e5-ba-8d-0c-10-77-a6-2e-92')
    @winrt_commethod(6)
    def CreateBadgeUpdaterForApplication(self) -> Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_commethod(7)
    def CreateBadgeUpdaterForApplicationWithId(self, applicationId: WinRT_String) -> Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_commethod(8)
    def CreateBadgeUpdaterForSecondaryTile(self, tileId: WinRT_String) -> Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_commethod(9)
    def get_User(self) -> Windows.System.User: ...
    User = property(get_User, None)
class IBadgeUpdateManagerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('33400faa-6dd5-4105-ae-bc-9b-50-fc-a4-92-da')
    @winrt_commethod(6)
    def CreateBadgeUpdaterForApplication(self) -> Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_commethod(7)
    def CreateBadgeUpdaterForApplicationWithId(self, applicationId: WinRT_String) -> Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_commethod(8)
    def CreateBadgeUpdaterForSecondaryTile(self, tileId: WinRT_String) -> Windows.UI.Notifications.BadgeUpdater: ...
    @winrt_commethod(9)
    def GetTemplateContent(self, type: Windows.UI.Notifications.BadgeTemplateType) -> Windows.Data.Xml.Dom.XmlDocument: ...
class IBadgeUpdateManagerStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('979a35ce-f940-48bf-94-e8-ca-24-4d-40-0b-41')
    @winrt_commethod(6)
    def GetForUser(self, user: Windows.System.User) -> Windows.UI.Notifications.BadgeUpdateManagerForUser: ...
class IBadgeUpdater(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b5fa1fd4-7562-4f6c-bf-a3-1b-6e-d2-e5-7f-2f')
    @winrt_commethod(6)
    def Update(self, notification: Windows.UI.Notifications.BadgeNotification) -> Void: ...
    @winrt_commethod(7)
    def Clear(self) -> Void: ...
    @winrt_commethod(8)
    def StartPeriodicUpdate(self, badgeContent: Windows.Foundation.Uri, requestedInterval: Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_commethod(9)
    def StartPeriodicUpdateAtTime(self, badgeContent: Windows.Foundation.Uri, startTime: Windows.Foundation.DateTime, requestedInterval: Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_commethod(10)
    def StopPeriodicUpdate(self) -> Void: ...
class IKnownAdaptiveNotificationHintsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('06206598-d496-497d-86-92-4f-7d-7c-27-70-df')
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
    Style = property(get_Style, None)
    Wrap = property(get_Wrap, None)
    MaxLines = property(get_MaxLines, None)
    MinLines = property(get_MinLines, None)
    TextStacking = property(get_TextStacking, None)
    Align = property(get_Align, None)
class IKnownAdaptiveNotificationTextStylesStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('202192d7-8996-45aa-8b-a1-d4-61-d7-2c-2a-1b')
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
    Caption = property(get_Caption, None)
    Body = property(get_Body, None)
    Base = property(get_Base, None)
    Subtitle = property(get_Subtitle, None)
    Title = property(get_Title, None)
    Subheader = property(get_Subheader, None)
    Header = property(get_Header, None)
    TitleNumeral = property(get_TitleNumeral, None)
    SubheaderNumeral = property(get_SubheaderNumeral, None)
    HeaderNumeral = property(get_HeaderNumeral, None)
    CaptionSubtle = property(get_CaptionSubtle, None)
    BodySubtle = property(get_BodySubtle, None)
    BaseSubtle = property(get_BaseSubtle, None)
    SubtitleSubtle = property(get_SubtitleSubtle, None)
    TitleSubtle = property(get_TitleSubtle, None)
    SubheaderSubtle = property(get_SubheaderSubtle, None)
    SubheaderNumeralSubtle = property(get_SubheaderNumeralSubtle, None)
    HeaderSubtle = property(get_HeaderSubtle, None)
    HeaderNumeralSubtle = property(get_HeaderNumeralSubtle, None)
class IKnownNotificationBindingsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('79427bae-a8b7-4d58-89-ea-76-a7-b7-bc-cd-ed')
    @winrt_commethod(6)
    def get_ToastGeneric(self) -> WinRT_String: ...
    ToastGeneric = property(get_ToastGeneric, None)
class INotification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('108037fe-eb76-4f82-97-bc-da-07-53-0a-2e-20')
    @winrt_commethod(6)
    def get_ExpirationTime(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(7)
    def put_ExpirationTime(self, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(8)
    def get_Visual(self) -> Windows.UI.Notifications.NotificationVisual: ...
    @winrt_commethod(9)
    def put_Visual(self, value: Windows.UI.Notifications.NotificationVisual) -> Void: ...
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
    Visual = property(get_Visual, put_Visual)
class INotificationBinding(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f29e4b85-0370-4ad3-b4-ea-da-9e-35-e7-ea-bf')
    @winrt_commethod(6)
    def get_Template(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Template(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Language(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Hints(self) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(11)
    def GetTextElements(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Notifications.AdaptiveNotificationText]: ...
    Template = property(get_Template, put_Template)
    Language = property(get_Language, put_Language)
    Hints = property(get_Hints, None)
class INotificationData(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9ffd2312-9d6a-4aaf-b6-ac-ff-17-f0-c1-f2-80')
    @winrt_commethod(6)
    def get_Values(self) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_commethod(7)
    def get_SequenceNumber(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_SequenceNumber(self, value: UInt32) -> Void: ...
    Values = property(get_Values, None)
    SequenceNumber = property(get_SequenceNumber, put_SequenceNumber)
class INotificationDataFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('23c1e33a-1c10-46fb-80-40-de-c3-84-62-1c-f8')
    @winrt_commethod(6)
    def CreateNotificationDataWithValuesAndSequenceNumber(self, initialValues: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]], sequenceNumber: UInt32) -> Windows.UI.Notifications.NotificationData: ...
    @winrt_commethod(7)
    def CreateNotificationDataWithValues(self, initialValues: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.UI.Notifications.NotificationData: ...
class INotificationVisual(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('68835b8e-aa56-4e11-86-d3-5f-9a-69-57-bc-5b')
    @winrt_commethod(6)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Language(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Bindings(self) -> Windows.Foundation.Collections.IVector[Windows.UI.Notifications.NotificationBinding]: ...
    @winrt_commethod(9)
    def GetBinding(self, templateName: WinRT_String) -> Windows.UI.Notifications.NotificationBinding: ...
    Language = property(get_Language, put_Language)
    Bindings = property(get_Bindings, None)
class IScheduledTileNotification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0abca6d5-99dc-4c78-a1-1c-c9-e7-f8-6d-7e-f7')
    @winrt_commethod(6)
    def get_Content(self) -> Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_commethod(7)
    def get_DeliveryTime(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def put_ExpirationTime(self, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(9)
    def get_ExpirationTime(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
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
    Tag = property(get_Tag, put_Tag)
    Id = property(get_Id, put_Id)
class IScheduledTileNotificationFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3383138a-98c0-4c3b-bb-d6-4a-63-3c-7c-fc-29')
    @winrt_commethod(6)
    def CreateScheduledTileNotification(self, content: Windows.Data.Xml.Dom.XmlDocument, deliveryTime: Windows.Foundation.DateTime) -> Windows.UI.Notifications.ScheduledTileNotification: ...
class IScheduledToastNotification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('79f577f8-0de7-48cd-97-40-9b-37-04-90-c8-38')
    @winrt_commethod(6)
    def get_Content(self) -> Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_commethod(7)
    def get_DeliveryTime(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_SnoozeInterval(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(9)
    def get_MaximumSnoozeCount(self) -> UInt32: ...
    @winrt_commethod(10)
    def put_Id(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_Id(self) -> WinRT_String: ...
    Content = property(get_Content, None)
    DeliveryTime = property(get_DeliveryTime, None)
    SnoozeInterval = property(get_SnoozeInterval, None)
    MaximumSnoozeCount = property(get_MaximumSnoozeCount, None)
    Id = property(get_Id, put_Id)
class IScheduledToastNotification2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a66ea09c-31b4-43b0-b5-dd-7a-40-e8-53-63-b1')
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
    Tag = property(get_Tag, put_Tag)
    Group = property(get_Group, put_Group)
    SuppressPopup = property(get_SuppressPopup, put_SuppressPopup)
class IScheduledToastNotification3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('98429e8b-bd32-4a3b-9d-15-22-ae-a4-94-62-a1')
    @winrt_commethod(6)
    def get_NotificationMirroring(self) -> Windows.UI.Notifications.NotificationMirroring: ...
    @winrt_commethod(7)
    def put_NotificationMirroring(self, value: Windows.UI.Notifications.NotificationMirroring) -> Void: ...
    @winrt_commethod(8)
    def get_RemoteId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_RemoteId(self, value: WinRT_String) -> Void: ...
    NotificationMirroring = property(get_NotificationMirroring, put_NotificationMirroring)
    RemoteId = property(get_RemoteId, put_RemoteId)
class IScheduledToastNotification4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1d4761fd-bdef-4e4a-96-be-01-01-36-9b-58-d2')
    @winrt_commethod(6)
    def get_ExpirationTime(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(7)
    def put_ExpirationTime(self, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
class IScheduledToastNotificationFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e7bed191-0bb9-4189-83-94-31-76-1b-47-6f-d7')
    @winrt_commethod(6)
    def CreateScheduledToastNotification(self, content: Windows.Data.Xml.Dom.XmlDocument, deliveryTime: Windows.Foundation.DateTime) -> Windows.UI.Notifications.ScheduledToastNotification: ...
    @winrt_commethod(7)
    def CreateScheduledToastNotificationRecurring(self, content: Windows.Data.Xml.Dom.XmlDocument, deliveryTime: Windows.Foundation.DateTime, snoozeInterval: Windows.Foundation.TimeSpan, maximumSnoozeCount: UInt32) -> Windows.UI.Notifications.ScheduledToastNotification: ...
class IScheduledToastNotificationShowingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6173f6b4-412a-5e2c-a6-ed-a0-20-9a-ef-9a-09')
    @winrt_commethod(6)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_ScheduledToastNotification(self) -> Windows.UI.Notifications.ScheduledToastNotification: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Cancel = property(get_Cancel, put_Cancel)
    ScheduledToastNotification = property(get_ScheduledToastNotification, None)
class IShownTileNotification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('342d8988-5af2-481a-a6-a3-f2-fd-c7-8d-e8-8e')
    @winrt_commethod(6)
    def get_Arguments(self) -> WinRT_String: ...
    Arguments = property(get_Arguments, None)
class ITileFlyoutNotification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9a53b261-c70c-42be-b2-f3-f4-2a-a9-7d-34-e5')
    @winrt_commethod(6)
    def get_Content(self) -> Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_commethod(7)
    def put_ExpirationTime(self, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(8)
    def get_ExpirationTime(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    Content = property(get_Content, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
class ITileFlyoutNotificationFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ef556ff5-5226-4f2b-b2-78-88-a3-5d-fe-56-9f')
    @winrt_commethod(6)
    def CreateTileFlyoutNotification(self, content: Windows.Data.Xml.Dom.XmlDocument) -> Windows.UI.Notifications.TileFlyoutNotification: ...
class ITileFlyoutUpdateManagerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('04363b0b-1ac0-4b99-88-e7-ad-a8-3e-95-3d-48')
    @winrt_commethod(6)
    def CreateTileFlyoutUpdaterForApplication(self) -> Windows.UI.Notifications.TileFlyoutUpdater: ...
    @winrt_commethod(7)
    def CreateTileFlyoutUpdaterForApplicationWithId(self, applicationId: WinRT_String) -> Windows.UI.Notifications.TileFlyoutUpdater: ...
    @winrt_commethod(8)
    def CreateTileFlyoutUpdaterForSecondaryTile(self, tileId: WinRT_String) -> Windows.UI.Notifications.TileFlyoutUpdater: ...
    @winrt_commethod(9)
    def GetTemplateContent(self, type: Windows.UI.Notifications.TileFlyoutTemplateType) -> Windows.Data.Xml.Dom.XmlDocument: ...
class ITileFlyoutUpdater(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8d40c76a-c465-4052-a7-40-5c-26-54-c1-a0-89')
    @winrt_commethod(6)
    def Update(self, notification: Windows.UI.Notifications.TileFlyoutNotification) -> Void: ...
    @winrt_commethod(7)
    def Clear(self) -> Void: ...
    @winrt_commethod(8)
    def StartPeriodicUpdate(self, tileFlyoutContent: Windows.Foundation.Uri, requestedInterval: Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_commethod(9)
    def StartPeriodicUpdateAtTime(self, tileFlyoutContent: Windows.Foundation.Uri, startTime: Windows.Foundation.DateTime, requestedInterval: Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_commethod(10)
    def StopPeriodicUpdate(self) -> Void: ...
    @winrt_commethod(11)
    def get_Setting(self) -> Windows.UI.Notifications.NotificationSetting: ...
    Setting = property(get_Setting, None)
class ITileNotification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ebaec8fa-50ec-4c18-b4-d0-3a-f0-2e-55-40-ab')
    @winrt_commethod(6)
    def get_Content(self) -> Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_commethod(7)
    def put_ExpirationTime(self, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(8)
    def get_ExpirationTime(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(9)
    def put_Tag(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Tag(self) -> WinRT_String: ...
    Content = property(get_Content, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
    Tag = property(get_Tag, put_Tag)
class ITileNotificationFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c6abdd6e-4928-46c8-bd-bf-81-a0-47-de-a0-d4')
    @winrt_commethod(6)
    def CreateTileNotification(self, content: Windows.Data.Xml.Dom.XmlDocument) -> Windows.UI.Notifications.TileNotification: ...
class ITileUpdateManagerForUser(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('55141348-2ee2-4e2d-9c-c1-21-6a-20-de-cc-9f')
    @winrt_commethod(6)
    def CreateTileUpdaterForApplication(self) -> Windows.UI.Notifications.TileUpdater: ...
    @winrt_commethod(7)
    def CreateTileUpdaterForApplicationWithId(self, applicationId: WinRT_String) -> Windows.UI.Notifications.TileUpdater: ...
    @winrt_commethod(8)
    def CreateTileUpdaterForSecondaryTile(self, tileId: WinRT_String) -> Windows.UI.Notifications.TileUpdater: ...
    @winrt_commethod(9)
    def get_User(self) -> Windows.System.User: ...
    User = property(get_User, None)
class ITileUpdateManagerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('da159e5d-3ea9-4986-8d-84-b0-9d-5e-12-27-6d')
    @winrt_commethod(6)
    def CreateTileUpdaterForApplication(self) -> Windows.UI.Notifications.TileUpdater: ...
    @winrt_commethod(7)
    def CreateTileUpdaterForApplicationWithId(self, applicationId: WinRT_String) -> Windows.UI.Notifications.TileUpdater: ...
    @winrt_commethod(8)
    def CreateTileUpdaterForSecondaryTile(self, tileId: WinRT_String) -> Windows.UI.Notifications.TileUpdater: ...
    @winrt_commethod(9)
    def GetTemplateContent(self, type: Windows.UI.Notifications.TileTemplateType) -> Windows.Data.Xml.Dom.XmlDocument: ...
class ITileUpdateManagerStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('731c1ddc-8e14-4b7c-a3-4b-9d-22-de-76-c8-4d')
    @winrt_commethod(6)
    def GetForUser(self, user: Windows.System.User) -> Windows.UI.Notifications.TileUpdateManagerForUser: ...
class ITileUpdater(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0942a48b-1d91-44ec-92-43-c1-e8-21-c2-9a-20')
    @winrt_commethod(6)
    def Update(self, notification: Windows.UI.Notifications.TileNotification) -> Void: ...
    @winrt_commethod(7)
    def Clear(self) -> Void: ...
    @winrt_commethod(8)
    def EnableNotificationQueue(self, enable: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_Setting(self) -> Windows.UI.Notifications.NotificationSetting: ...
    @winrt_commethod(10)
    def AddToSchedule(self, scheduledTile: Windows.UI.Notifications.ScheduledTileNotification) -> Void: ...
    @winrt_commethod(11)
    def RemoveFromSchedule(self, scheduledTile: Windows.UI.Notifications.ScheduledTileNotification) -> Void: ...
    @winrt_commethod(12)
    def GetScheduledTileNotifications(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Notifications.ScheduledTileNotification]: ...
    @winrt_commethod(13)
    def StartPeriodicUpdate(self, tileContent: Windows.Foundation.Uri, requestedInterval: Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_commethod(14)
    def StartPeriodicUpdateAtTime(self, tileContent: Windows.Foundation.Uri, startTime: Windows.Foundation.DateTime, requestedInterval: Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_commethod(15)
    def StopPeriodicUpdate(self) -> Void: ...
    @winrt_commethod(16)
    def StartPeriodicUpdateBatch(self, tileContents: Windows.Foundation.Collections.IIterable[Windows.Foundation.Uri], requestedInterval: Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_commethod(17)
    def StartPeriodicUpdateBatchAtTime(self, tileContents: Windows.Foundation.Collections.IIterable[Windows.Foundation.Uri], startTime: Windows.Foundation.DateTime, requestedInterval: Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    Setting = property(get_Setting, None)
class ITileUpdater2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a2266e12-15ee-43ed-83-f5-65-b3-52-bb-1a-84')
    @winrt_commethod(6)
    def EnableNotificationQueueForSquare150x150(self, enable: Boolean) -> Void: ...
    @winrt_commethod(7)
    def EnableNotificationQueueForWide310x150(self, enable: Boolean) -> Void: ...
    @winrt_commethod(8)
    def EnableNotificationQueueForSquare310x310(self, enable: Boolean) -> Void: ...
class IToastActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e3bf92f3-c197-436f-82-65-06-25-82-4f-8d-ac')
    @winrt_commethod(6)
    def get_Arguments(self) -> WinRT_String: ...
    Arguments = property(get_Arguments, None)
class IToastActivatedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ab7da512-cc61-568e-81-be-30-4a-c3-10-38-fa')
    @winrt_commethod(6)
    def get_UserInput(self) -> Windows.Foundation.Collections.ValueSet: ...
    UserInput = property(get_UserInput, None)
class IToastCollection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0a8bc3b0-e0be-4858-bc-2a-89-df-e0-b3-28-63')
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
    def get_Icon(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(12)
    def put_Icon(self, value: Windows.Foundation.Uri) -> Void: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
    LaunchArgs = property(get_LaunchArgs, put_LaunchArgs)
    Icon = property(get_Icon, put_Icon)
class IToastCollectionFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('164dd3d7-73c4-44f7-b4-ff-fb-6d-4b-f1-f4-c6')
    @winrt_commethod(6)
    def CreateInstance(self, collectionId: WinRT_String, displayName: WinRT_String, launchArgs: WinRT_String, iconUri: Windows.Foundation.Uri) -> Windows.UI.Notifications.ToastCollection: ...
class IToastCollectionManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2a1821fe-179d-49bc-b7-9d-a5-27-92-0d-36-65')
    @winrt_commethod(6)
    def SaveToastCollectionAsync(self, collection: Windows.UI.Notifications.ToastCollection) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def FindAllToastCollectionsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.UI.Notifications.ToastCollection]]: ...
    @winrt_commethod(8)
    def GetToastCollectionAsync(self, collectionId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.UI.Notifications.ToastCollection]: ...
    @winrt_commethod(9)
    def RemoveToastCollectionAsync(self, collectionId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def RemoveAllToastCollectionsAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(11)
    def get_User(self) -> Windows.System.User: ...
    @winrt_commethod(12)
    def get_AppId(self) -> WinRT_String: ...
    User = property(get_User, None)
    AppId = property(get_AppId, None)
class IToastDismissedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3f89d935-d9cb-4538-a0-f0-ff-e7-65-99-38-f8')
    @winrt_commethod(6)
    def get_Reason(self) -> Windows.UI.Notifications.ToastDismissalReason: ...
    Reason = property(get_Reason, None)
class IToastFailedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('35176862-cfd4-44f8-ad-64-f5-00-fd-89-6c-3b')
    @winrt_commethod(6)
    def get_ErrorCode(self) -> Windows.Foundation.HResult: ...
    ErrorCode = property(get_ErrorCode, None)
class IToastNotification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('997e2675-059e-4e60-8b-06-17-60-91-7c-8b-80')
    @winrt_commethod(6)
    def get_Content(self) -> Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_commethod(7)
    def put_ExpirationTime(self, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(8)
    def get_ExpirationTime(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(9)
    def add_Dismissed(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Notifications.ToastNotification, Windows.UI.Notifications.ToastDismissedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Dismissed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Activated(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Notifications.ToastNotification, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Activated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_Failed(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Notifications.ToastNotification, Windows.UI.Notifications.ToastFailedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_Failed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Content = property(get_Content, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
class IToastNotification2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9dfb9fd1-143a-490e-90-bf-b9-fb-a7-13-2d-e7')
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
    Tag = property(get_Tag, put_Tag)
    Group = property(get_Group, put_Group)
    SuppressPopup = property(get_SuppressPopup, put_SuppressPopup)
class IToastNotification3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('31e8aed8-8141-4f99-bc-0a-c4-ed-21-29-7d-77')
    @winrt_commethod(6)
    def get_NotificationMirroring(self) -> Windows.UI.Notifications.NotificationMirroring: ...
    @winrt_commethod(7)
    def put_NotificationMirroring(self, value: Windows.UI.Notifications.NotificationMirroring) -> Void: ...
    @winrt_commethod(8)
    def get_RemoteId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_RemoteId(self, value: WinRT_String) -> Void: ...
    NotificationMirroring = property(get_NotificationMirroring, put_NotificationMirroring)
    RemoteId = property(get_RemoteId, put_RemoteId)
class IToastNotification4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('15154935-28ea-4727-88-e9-c5-86-80-e2-d1-18')
    @winrt_commethod(6)
    def get_Data(self) -> Windows.UI.Notifications.NotificationData: ...
    @winrt_commethod(7)
    def put_Data(self, value: Windows.UI.Notifications.NotificationData) -> Void: ...
    @winrt_commethod(8)
    def get_Priority(self) -> Windows.UI.Notifications.ToastNotificationPriority: ...
    @winrt_commethod(9)
    def put_Priority(self, value: Windows.UI.Notifications.ToastNotificationPriority) -> Void: ...
    Data = property(get_Data, put_Data)
    Priority = property(get_Priority, put_Priority)
class IToastNotification6(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('43ebfe53-89ae-5c1e-a2-79-3a-ec-fe-9b-6f-54')
    @winrt_commethod(6)
    def get_ExpiresOnReboot(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_ExpiresOnReboot(self, value: Boolean) -> Void: ...
    ExpiresOnReboot = property(get_ExpiresOnReboot, put_ExpiresOnReboot)
class IToastNotificationActionTriggerDetail(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9445135a-38f3-42f6-96-aa-79-55-b0-f0-3d-a2')
    @winrt_commethod(6)
    def get_Argument(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_UserInput(self) -> Windows.Foundation.Collections.ValueSet: ...
    Argument = property(get_Argument, None)
    UserInput = property(get_UserInput, None)
class IToastNotificationFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('04124b20-82c6-4229-b1-09-fd-9e-d4-66-2b-53')
    @winrt_commethod(6)
    def CreateToastNotification(self, content: Windows.Data.Xml.Dom.XmlDocument) -> Windows.UI.Notifications.ToastNotification: ...
class IToastNotificationHistory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5caddc63-01d3-4c97-98-6f-05-33-48-3f-ee-14')
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
class IToastNotificationHistory2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3bc3d253-2f31-4092-91-29-8a-d5-ab-f0-67-da')
    @winrt_commethod(6)
    def GetHistory(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Notifications.ToastNotification]: ...
    @winrt_commethod(7)
    def GetHistoryWithId(self, applicationId: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Notifications.ToastNotification]: ...
class IToastNotificationHistoryChangedTriggerDetail(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('db037ffa-0068-412c-9c-83-26-7c-37-f6-56-70')
    @winrt_commethod(6)
    def get_ChangeType(self) -> Windows.UI.Notifications.ToastHistoryChangedType: ...
    ChangeType = property(get_ChangeType, None)
class IToastNotificationHistoryChangedTriggerDetail2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0b36e982-c871-49fb-ba-bb-25-bd-bc-4c-c4-5b')
    @winrt_commethod(6)
    def get_CollectionId(self) -> WinRT_String: ...
    CollectionId = property(get_CollectionId, None)
class IToastNotificationManagerForUser(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('79ab57f6-43fe-487b-8a-7f-99-56-72-00-ae-94')
    @winrt_commethod(6)
    def CreateToastNotifier(self) -> Windows.UI.Notifications.ToastNotifier: ...
    @winrt_commethod(7)
    def CreateToastNotifierWithId(self, applicationId: WinRT_String) -> Windows.UI.Notifications.ToastNotifier: ...
    @winrt_commethod(8)
    def get_History(self) -> Windows.UI.Notifications.ToastNotificationHistory: ...
    @winrt_commethod(9)
    def get_User(self) -> Windows.System.User: ...
    History = property(get_History, None)
    User = property(get_User, None)
class IToastNotificationManagerForUser2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('679c64b7-81ab-42c2-88-19-c9-58-76-77-53-f4')
    @winrt_commethod(6)
    def GetToastNotifierForToastCollectionIdAsync(self, collectionId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.UI.Notifications.ToastNotifier]: ...
    @winrt_commethod(7)
    def GetHistoryForToastCollectionIdAsync(self, collectionId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.UI.Notifications.ToastNotificationHistory]: ...
    @winrt_commethod(8)
    def GetToastCollectionManager(self) -> Windows.UI.Notifications.ToastCollectionManager: ...
    @winrt_commethod(9)
    def GetToastCollectionManagerWithAppId(self, appId: WinRT_String) -> Windows.UI.Notifications.ToastCollectionManager: ...
class IToastNotificationManagerForUser3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3efcb176-6cc1-56dc-97-3b-25-1f-7a-ac-b1-c5')
    @winrt_commethod(6)
    def get_NotificationMode(self) -> Windows.UI.Notifications.ToastNotificationMode: ...
    @winrt_commethod(7)
    def add_NotificationModeChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Notifications.ToastNotificationManagerForUser, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_NotificationModeChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    NotificationMode = property(get_NotificationMode, None)
class IToastNotificationManagerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('50ac103f-d235-4598-bb-ef-98-fe-4d-1a-3a-d4')
    @winrt_commethod(6)
    def CreateToastNotifier(self) -> Windows.UI.Notifications.ToastNotifier: ...
    @winrt_commethod(7)
    def CreateToastNotifierWithId(self, applicationId: WinRT_String) -> Windows.UI.Notifications.ToastNotifier: ...
    @winrt_commethod(8)
    def GetTemplateContent(self, type: Windows.UI.Notifications.ToastTemplateType) -> Windows.Data.Xml.Dom.XmlDocument: ...
class IToastNotificationManagerStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7ab93c52-0e48-4750-ba-9d-1a-41-13-98-18-47')
    @winrt_commethod(6)
    def get_History(self) -> Windows.UI.Notifications.ToastNotificationHistory: ...
    History = property(get_History, None)
class IToastNotificationManagerStatics4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8f993fd3-e516-45fb-81-30-39-8e-93-fa-52-c3')
    @winrt_commethod(6)
    def GetForUser(self, user: Windows.System.User) -> Windows.UI.Notifications.ToastNotificationManagerForUser: ...
    @winrt_commethod(7)
    def ConfigureNotificationMirroring(self, value: Windows.UI.Notifications.NotificationMirroring) -> Void: ...
class IToastNotificationManagerStatics5(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d6f5f569-d40d-407c-89-89-88-ca-b4-2c-fd-14')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.UI.Notifications.ToastNotificationManagerForUser: ...
class IToastNotifier(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('75927b93-03f3-41ec-91-d3-6e-5b-ac-1b-38-e7')
    @winrt_commethod(6)
    def Show(self, notification: Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_commethod(7)
    def Hide(self, notification: Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_commethod(8)
    def get_Setting(self) -> Windows.UI.Notifications.NotificationSetting: ...
    @winrt_commethod(9)
    def AddToSchedule(self, scheduledToast: Windows.UI.Notifications.ScheduledToastNotification) -> Void: ...
    @winrt_commethod(10)
    def RemoveFromSchedule(self, scheduledToast: Windows.UI.Notifications.ScheduledToastNotification) -> Void: ...
    @winrt_commethod(11)
    def GetScheduledToastNotifications(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Notifications.ScheduledToastNotification]: ...
    Setting = property(get_Setting, None)
class IToastNotifier2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('354389c6-7c01-4bd5-9c-20-60-43-40-cd-2b-74')
    @winrt_commethod(6)
    def UpdateWithTagAndGroup(self, data: Windows.UI.Notifications.NotificationData, tag: WinRT_String, group: WinRT_String) -> Windows.UI.Notifications.NotificationUpdateResult: ...
    @winrt_commethod(7)
    def UpdateWithTag(self, data: Windows.UI.Notifications.NotificationData, tag: WinRT_String) -> Windows.UI.Notifications.NotificationUpdateResult: ...
class IToastNotifier3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ae75a04a-3b0c-51ad-b7-e8-b0-8a-b6-05-25-49')
    @winrt_commethod(6)
    def add_ScheduledToastNotificationShowing(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Notifications.ToastNotifier, Windows.UI.Notifications.ScheduledToastNotificationShowingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ScheduledToastNotificationShowing(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IUserNotification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('adf7e52f-4e53-42d5-9c-33-eb-5e-a5-15-b2-3e')
    @winrt_commethod(6)
    def get_Notification(self) -> Windows.UI.Notifications.Notification: ...
    @winrt_commethod(7)
    def get_AppInfo(self) -> Windows.ApplicationModel.AppInfo: ...
    @winrt_commethod(8)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_CreationTime(self) -> Windows.Foundation.DateTime: ...
    Notification = property(get_Notification, None)
    AppInfo = property(get_AppInfo, None)
    Id = property(get_Id, None)
    CreationTime = property(get_CreationTime, None)
class IUserNotificationChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b6bd6839-79cf-4b25-82-c0-0c-e1-ee-f8-1f-8c')
    @winrt_commethod(6)
    def get_ChangeKind(self) -> Windows.UI.Notifications.UserNotificationChangedKind: ...
    @winrt_commethod(7)
    def get_UserNotificationId(self) -> UInt32: ...
    ChangeKind = property(get_ChangeKind, None)
    UserNotificationId = property(get_UserNotificationId, None)
class KnownAdaptiveNotificationHints(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.KnownAdaptiveNotificationHints'
    @winrt_classmethod
    def get_Style(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationHintsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Wrap(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationHintsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_MaxLines(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationHintsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_MinLines(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationHintsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TextStacking(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationHintsStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Align(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationHintsStatics) -> WinRT_String: ...
    Style = property(get_Style, None)
    Wrap = property(get_Wrap, None)
    MaxLines = property(get_MaxLines, None)
    MinLines = property(get_MinLines, None)
    TextStacking = property(get_TextStacking, None)
    Align = property(get_Align, None)
class KnownAdaptiveNotificationTextStyles(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.KnownAdaptiveNotificationTextStyles'
    @winrt_classmethod
    def get_Caption(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Body(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Base(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Subtitle(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Title(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Subheader(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_Header(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TitleNumeral(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SubheaderNumeral(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HeaderNumeral(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_CaptionSubtle(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BodySubtle(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_BaseSubtle(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SubtitleSubtle(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_TitleSubtle(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SubheaderSubtle(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_SubheaderNumeralSubtle(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HeaderSubtle(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def get_HeaderNumeralSubtle(cls: Windows.UI.Notifications.IKnownAdaptiveNotificationTextStylesStatics) -> WinRT_String: ...
    Caption = property(get_Caption, None)
    Body = property(get_Body, None)
    Base = property(get_Base, None)
    Subtitle = property(get_Subtitle, None)
    Title = property(get_Title, None)
    Subheader = property(get_Subheader, None)
    Header = property(get_Header, None)
    TitleNumeral = property(get_TitleNumeral, None)
    SubheaderNumeral = property(get_SubheaderNumeral, None)
    HeaderNumeral = property(get_HeaderNumeral, None)
    CaptionSubtle = property(get_CaptionSubtle, None)
    BodySubtle = property(get_BodySubtle, None)
    BaseSubtle = property(get_BaseSubtle, None)
    SubtitleSubtle = property(get_SubtitleSubtle, None)
    TitleSubtle = property(get_TitleSubtle, None)
    SubheaderSubtle = property(get_SubheaderSubtle, None)
    SubheaderNumeralSubtle = property(get_SubheaderNumeralSubtle, None)
    HeaderSubtle = property(get_HeaderSubtle, None)
    HeaderNumeralSubtle = property(get_HeaderNumeralSubtle, None)
class KnownNotificationBindings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.KnownNotificationBindings'
    @winrt_classmethod
    def get_ToastGeneric(cls: Windows.UI.Notifications.IKnownNotificationBindingsStatics) -> WinRT_String: ...
    ToastGeneric = property(get_ToastGeneric, None)
class Notification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.Notification'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Notifications.Notification: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: Windows.UI.Notifications.INotification) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_ExpirationTime(self: Windows.UI.Notifications.INotification, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_Visual(self: Windows.UI.Notifications.INotification) -> Windows.UI.Notifications.NotificationVisual: ...
    @winrt_mixinmethod
    def put_Visual(self: Windows.UI.Notifications.INotification, value: Windows.UI.Notifications.NotificationVisual) -> Void: ...
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
    Visual = property(get_Visual, put_Visual)
class NotificationBinding(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.NotificationBinding'
    @winrt_mixinmethod
    def get_Template(self: Windows.UI.Notifications.INotificationBinding) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Template(self: Windows.UI.Notifications.INotificationBinding, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.UI.Notifications.INotificationBinding) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: Windows.UI.Notifications.INotificationBinding, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Hints(self: Windows.UI.Notifications.INotificationBinding) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def GetTextElements(self: Windows.UI.Notifications.INotificationBinding) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Notifications.AdaptiveNotificationText]: ...
    Template = property(get_Template, put_Template)
    Language = property(get_Language, put_Language)
    Hints = property(get_Hints, None)
class NotificationData(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.NotificationData'
    @winrt_factorymethod
    def CreateNotificationData(cls: Windows.UI.Notifications.INotificationDataFactory, initialValues: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]], sequenceNumber: UInt32) -> Windows.UI.Notifications.NotificationData: ...
    @winrt_factorymethod
    def CreateNotificationData(cls: Windows.UI.Notifications.INotificationDataFactory, initialValues: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.UI.Notifications.NotificationData: ...
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Notifications.NotificationData: ...
    @winrt_mixinmethod
    def get_Values(self: Windows.UI.Notifications.INotificationData) -> Windows.Foundation.Collections.IMap[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_SequenceNumber(self: Windows.UI.Notifications.INotificationData) -> UInt32: ...
    @winrt_mixinmethod
    def put_SequenceNumber(self: Windows.UI.Notifications.INotificationData, value: UInt32) -> Void: ...
    Values = property(get_Values, None)
    SequenceNumber = property(get_SequenceNumber, put_SequenceNumber)
NotificationKinds = UInt32
NotificationKinds_Unknown: NotificationKinds = 0
NotificationKinds_Toast: NotificationKinds = 1
NotificationMirroring = Int32
NotificationMirroring_Allowed: NotificationMirroring = 0
NotificationMirroring_Disabled: NotificationMirroring = 1
NotificationSetting = Int32
NotificationSetting_Enabled: NotificationSetting = 0
NotificationSetting_DisabledForApplication: NotificationSetting = 1
NotificationSetting_DisabledForUser: NotificationSetting = 2
NotificationSetting_DisabledByGroupPolicy: NotificationSetting = 3
NotificationSetting_DisabledByManifest: NotificationSetting = 4
NotificationUpdateResult = Int32
NotificationUpdateResult_Succeeded: NotificationUpdateResult = 0
NotificationUpdateResult_Failed: NotificationUpdateResult = 1
NotificationUpdateResult_NotificationNotFound: NotificationUpdateResult = 2
class NotificationVisual(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.NotificationVisual'
    @winrt_mixinmethod
    def get_Language(self: Windows.UI.Notifications.INotificationVisual) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: Windows.UI.Notifications.INotificationVisual, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Bindings(self: Windows.UI.Notifications.INotificationVisual) -> Windows.Foundation.Collections.IVector[Windows.UI.Notifications.NotificationBinding]: ...
    @winrt_mixinmethod
    def GetBinding(self: Windows.UI.Notifications.INotificationVisual, templateName: WinRT_String) -> Windows.UI.Notifications.NotificationBinding: ...
    Language = property(get_Language, put_Language)
    Bindings = property(get_Bindings, None)
PeriodicUpdateRecurrence = Int32
PeriodicUpdateRecurrence_HalfHour: PeriodicUpdateRecurrence = 0
PeriodicUpdateRecurrence_Hour: PeriodicUpdateRecurrence = 1
PeriodicUpdateRecurrence_SixHours: PeriodicUpdateRecurrence = 2
PeriodicUpdateRecurrence_TwelveHours: PeriodicUpdateRecurrence = 3
PeriodicUpdateRecurrence_Daily: PeriodicUpdateRecurrence = 4
class ScheduledTileNotification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.ScheduledTileNotification'
    @winrt_factorymethod
    def CreateScheduledTileNotification(cls: Windows.UI.Notifications.IScheduledTileNotificationFactory, content: Windows.Data.Xml.Dom.XmlDocument, deliveryTime: Windows.Foundation.DateTime) -> Windows.UI.Notifications.ScheduledTileNotification: ...
    @winrt_mixinmethod
    def get_Content(self: Windows.UI.Notifications.IScheduledTileNotification) -> Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_mixinmethod
    def get_DeliveryTime(self: Windows.UI.Notifications.IScheduledTileNotification) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_ExpirationTime(self: Windows.UI.Notifications.IScheduledTileNotification, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: Windows.UI.Notifications.IScheduledTileNotification) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_Tag(self: Windows.UI.Notifications.IScheduledTileNotification, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: Windows.UI.Notifications.IScheduledTileNotification) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Id(self: Windows.UI.Notifications.IScheduledTileNotification, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Notifications.IScheduledTileNotification) -> WinRT_String: ...
    Content = property(get_Content, None)
    DeliveryTime = property(get_DeliveryTime, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
    Tag = property(get_Tag, put_Tag)
    Id = property(get_Id, put_Id)
class ScheduledToastNotification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.ScheduledToastNotification'
    @winrt_factorymethod
    def CreateScheduledToastNotification(cls: Windows.UI.Notifications.IScheduledToastNotificationFactory, content: Windows.Data.Xml.Dom.XmlDocument, deliveryTime: Windows.Foundation.DateTime) -> Windows.UI.Notifications.ScheduledToastNotification: ...
    @winrt_factorymethod
    def CreateScheduledToastNotificationRecurring(cls: Windows.UI.Notifications.IScheduledToastNotificationFactory, content: Windows.Data.Xml.Dom.XmlDocument, deliveryTime: Windows.Foundation.DateTime, snoozeInterval: Windows.Foundation.TimeSpan, maximumSnoozeCount: UInt32) -> Windows.UI.Notifications.ScheduledToastNotification: ...
    @winrt_mixinmethod
    def get_Content(self: Windows.UI.Notifications.IScheduledToastNotification) -> Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_mixinmethod
    def get_DeliveryTime(self: Windows.UI.Notifications.IScheduledToastNotification) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_SnoozeInterval(self: Windows.UI.Notifications.IScheduledToastNotification) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_MaximumSnoozeCount(self: Windows.UI.Notifications.IScheduledToastNotification) -> UInt32: ...
    @winrt_mixinmethod
    def put_Id(self: Windows.UI.Notifications.IScheduledToastNotification, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Notifications.IScheduledToastNotification) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Tag(self: Windows.UI.Notifications.IScheduledToastNotification2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: Windows.UI.Notifications.IScheduledToastNotification2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Group(self: Windows.UI.Notifications.IScheduledToastNotification2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Group(self: Windows.UI.Notifications.IScheduledToastNotification2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SuppressPopup(self: Windows.UI.Notifications.IScheduledToastNotification2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SuppressPopup(self: Windows.UI.Notifications.IScheduledToastNotification2) -> Boolean: ...
    @winrt_mixinmethod
    def get_NotificationMirroring(self: Windows.UI.Notifications.IScheduledToastNotification3) -> Windows.UI.Notifications.NotificationMirroring: ...
    @winrt_mixinmethod
    def put_NotificationMirroring(self: Windows.UI.Notifications.IScheduledToastNotification3, value: Windows.UI.Notifications.NotificationMirroring) -> Void: ...
    @winrt_mixinmethod
    def get_RemoteId(self: Windows.UI.Notifications.IScheduledToastNotification3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RemoteId(self: Windows.UI.Notifications.IScheduledToastNotification3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: Windows.UI.Notifications.IScheduledToastNotification4) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_ExpirationTime(self: Windows.UI.Notifications.IScheduledToastNotification4, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    Content = property(get_Content, None)
    DeliveryTime = property(get_DeliveryTime, None)
    SnoozeInterval = property(get_SnoozeInterval, None)
    MaximumSnoozeCount = property(get_MaximumSnoozeCount, None)
    Id = property(get_Id, put_Id)
    Tag = property(get_Tag, put_Tag)
    Group = property(get_Group, put_Group)
    SuppressPopup = property(get_SuppressPopup, put_SuppressPopup)
    NotificationMirroring = property(get_NotificationMirroring, put_NotificationMirroring)
    RemoteId = property(get_RemoteId, put_RemoteId)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
class ScheduledToastNotificationShowingEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.ScheduledToastNotificationShowingEventArgs'
    @winrt_mixinmethod
    def get_Cancel(self: Windows.UI.Notifications.IScheduledToastNotificationShowingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: Windows.UI.Notifications.IScheduledToastNotificationShowingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ScheduledToastNotification(self: Windows.UI.Notifications.IScheduledToastNotificationShowingEventArgs) -> Windows.UI.Notifications.ScheduledToastNotification: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.UI.Notifications.IScheduledToastNotificationShowingEventArgs) -> Windows.Foundation.Deferral: ...
    Cancel = property(get_Cancel, put_Cancel)
    ScheduledToastNotification = property(get_ScheduledToastNotification, None)
class ShownTileNotification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.ShownTileNotification'
    @winrt_mixinmethod
    def get_Arguments(self: Windows.UI.Notifications.IShownTileNotification) -> WinRT_String: ...
    Arguments = property(get_Arguments, None)
class TileFlyoutNotification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.TileFlyoutNotification'
    @winrt_factorymethod
    def CreateTileFlyoutNotification(cls: Windows.UI.Notifications.ITileFlyoutNotificationFactory, content: Windows.Data.Xml.Dom.XmlDocument) -> Windows.UI.Notifications.TileFlyoutNotification: ...
    @winrt_mixinmethod
    def get_Content(self: Windows.UI.Notifications.ITileFlyoutNotification) -> Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_mixinmethod
    def put_ExpirationTime(self: Windows.UI.Notifications.ITileFlyoutNotification, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: Windows.UI.Notifications.ITileFlyoutNotification) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    Content = property(get_Content, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
TileFlyoutTemplateType = Int32
TileFlyoutTemplateType_TileFlyoutTemplate01: TileFlyoutTemplateType = 0
class TileFlyoutUpdateManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.TileFlyoutUpdateManager'
    @winrt_classmethod
    def CreateTileFlyoutUpdaterForApplication(cls: Windows.UI.Notifications.ITileFlyoutUpdateManagerStatics) -> Windows.UI.Notifications.TileFlyoutUpdater: ...
    @winrt_classmethod
    def CreateTileFlyoutUpdaterForApplicationWithId(cls: Windows.UI.Notifications.ITileFlyoutUpdateManagerStatics, applicationId: WinRT_String) -> Windows.UI.Notifications.TileFlyoutUpdater: ...
    @winrt_classmethod
    def CreateTileFlyoutUpdaterForSecondaryTile(cls: Windows.UI.Notifications.ITileFlyoutUpdateManagerStatics, tileId: WinRT_String) -> Windows.UI.Notifications.TileFlyoutUpdater: ...
    @winrt_classmethod
    def GetTemplateContent(cls: Windows.UI.Notifications.ITileFlyoutUpdateManagerStatics, type: Windows.UI.Notifications.TileFlyoutTemplateType) -> Windows.Data.Xml.Dom.XmlDocument: ...
class TileFlyoutUpdater(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.TileFlyoutUpdater'
    @winrt_mixinmethod
    def Update(self: Windows.UI.Notifications.ITileFlyoutUpdater, notification: Windows.UI.Notifications.TileFlyoutNotification) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.UI.Notifications.ITileFlyoutUpdater) -> Void: ...
    @winrt_mixinmethod
    def StartPeriodicUpdate(self: Windows.UI.Notifications.ITileFlyoutUpdater, tileFlyoutContent: Windows.Foundation.Uri, requestedInterval: Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_mixinmethod
    def StartPeriodicUpdateAtTime(self: Windows.UI.Notifications.ITileFlyoutUpdater, tileFlyoutContent: Windows.Foundation.Uri, startTime: Windows.Foundation.DateTime, requestedInterval: Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_mixinmethod
    def StopPeriodicUpdate(self: Windows.UI.Notifications.ITileFlyoutUpdater) -> Void: ...
    @winrt_mixinmethod
    def get_Setting(self: Windows.UI.Notifications.ITileFlyoutUpdater) -> Windows.UI.Notifications.NotificationSetting: ...
    Setting = property(get_Setting, None)
class TileNotification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.TileNotification'
    @winrt_factorymethod
    def CreateTileNotification(cls: Windows.UI.Notifications.ITileNotificationFactory, content: Windows.Data.Xml.Dom.XmlDocument) -> Windows.UI.Notifications.TileNotification: ...
    @winrt_mixinmethod
    def get_Content(self: Windows.UI.Notifications.ITileNotification) -> Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_mixinmethod
    def put_ExpirationTime(self: Windows.UI.Notifications.ITileNotification, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: Windows.UI.Notifications.ITileNotification) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_Tag(self: Windows.UI.Notifications.ITileNotification, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: Windows.UI.Notifications.ITileNotification) -> WinRT_String: ...
    Content = property(get_Content, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
    Tag = property(get_Tag, put_Tag)
TileTemplateType = Int32
TileTemplateType_TileSquareImage: TileTemplateType = 0
TileTemplateType_TileSquareBlock: TileTemplateType = 1
TileTemplateType_TileSquareText01: TileTemplateType = 2
TileTemplateType_TileSquareText02: TileTemplateType = 3
TileTemplateType_TileSquareText03: TileTemplateType = 4
TileTemplateType_TileSquareText04: TileTemplateType = 5
TileTemplateType_TileSquarePeekImageAndText01: TileTemplateType = 6
TileTemplateType_TileSquarePeekImageAndText02: TileTemplateType = 7
TileTemplateType_TileSquarePeekImageAndText03: TileTemplateType = 8
TileTemplateType_TileSquarePeekImageAndText04: TileTemplateType = 9
TileTemplateType_TileWideImage: TileTemplateType = 10
TileTemplateType_TileWideImageCollection: TileTemplateType = 11
TileTemplateType_TileWideImageAndText01: TileTemplateType = 12
TileTemplateType_TileWideImageAndText02: TileTemplateType = 13
TileTemplateType_TileWideBlockAndText01: TileTemplateType = 14
TileTemplateType_TileWideBlockAndText02: TileTemplateType = 15
TileTemplateType_TileWidePeekImageCollection01: TileTemplateType = 16
TileTemplateType_TileWidePeekImageCollection02: TileTemplateType = 17
TileTemplateType_TileWidePeekImageCollection03: TileTemplateType = 18
TileTemplateType_TileWidePeekImageCollection04: TileTemplateType = 19
TileTemplateType_TileWidePeekImageCollection05: TileTemplateType = 20
TileTemplateType_TileWidePeekImageCollection06: TileTemplateType = 21
TileTemplateType_TileWidePeekImageAndText01: TileTemplateType = 22
TileTemplateType_TileWidePeekImageAndText02: TileTemplateType = 23
TileTemplateType_TileWidePeekImage01: TileTemplateType = 24
TileTemplateType_TileWidePeekImage02: TileTemplateType = 25
TileTemplateType_TileWidePeekImage03: TileTemplateType = 26
TileTemplateType_TileWidePeekImage04: TileTemplateType = 27
TileTemplateType_TileWidePeekImage05: TileTemplateType = 28
TileTemplateType_TileWidePeekImage06: TileTemplateType = 29
TileTemplateType_TileWideSmallImageAndText01: TileTemplateType = 30
TileTemplateType_TileWideSmallImageAndText02: TileTemplateType = 31
TileTemplateType_TileWideSmallImageAndText03: TileTemplateType = 32
TileTemplateType_TileWideSmallImageAndText04: TileTemplateType = 33
TileTemplateType_TileWideSmallImageAndText05: TileTemplateType = 34
TileTemplateType_TileWideText01: TileTemplateType = 35
TileTemplateType_TileWideText02: TileTemplateType = 36
TileTemplateType_TileWideText03: TileTemplateType = 37
TileTemplateType_TileWideText04: TileTemplateType = 38
TileTemplateType_TileWideText05: TileTemplateType = 39
TileTemplateType_TileWideText06: TileTemplateType = 40
TileTemplateType_TileWideText07: TileTemplateType = 41
TileTemplateType_TileWideText08: TileTemplateType = 42
TileTemplateType_TileWideText09: TileTemplateType = 43
TileTemplateType_TileWideText10: TileTemplateType = 44
TileTemplateType_TileWideText11: TileTemplateType = 45
TileTemplateType_TileSquare150x150Image: TileTemplateType = 0
TileTemplateType_TileSquare150x150Block: TileTemplateType = 1
TileTemplateType_TileSquare150x150Text01: TileTemplateType = 2
TileTemplateType_TileSquare150x150Text02: TileTemplateType = 3
TileTemplateType_TileSquare150x150Text03: TileTemplateType = 4
TileTemplateType_TileSquare150x150Text04: TileTemplateType = 5
TileTemplateType_TileSquare150x150PeekImageAndText01: TileTemplateType = 6
TileTemplateType_TileSquare150x150PeekImageAndText02: TileTemplateType = 7
TileTemplateType_TileSquare150x150PeekImageAndText03: TileTemplateType = 8
TileTemplateType_TileSquare150x150PeekImageAndText04: TileTemplateType = 9
TileTemplateType_TileWide310x150Image: TileTemplateType = 10
TileTemplateType_TileWide310x150ImageCollection: TileTemplateType = 11
TileTemplateType_TileWide310x150ImageAndText01: TileTemplateType = 12
TileTemplateType_TileWide310x150ImageAndText02: TileTemplateType = 13
TileTemplateType_TileWide310x150BlockAndText01: TileTemplateType = 14
TileTemplateType_TileWide310x150BlockAndText02: TileTemplateType = 15
TileTemplateType_TileWide310x150PeekImageCollection01: TileTemplateType = 16
TileTemplateType_TileWide310x150PeekImageCollection02: TileTemplateType = 17
TileTemplateType_TileWide310x150PeekImageCollection03: TileTemplateType = 18
TileTemplateType_TileWide310x150PeekImageCollection04: TileTemplateType = 19
TileTemplateType_TileWide310x150PeekImageCollection05: TileTemplateType = 20
TileTemplateType_TileWide310x150PeekImageCollection06: TileTemplateType = 21
TileTemplateType_TileWide310x150PeekImageAndText01: TileTemplateType = 22
TileTemplateType_TileWide310x150PeekImageAndText02: TileTemplateType = 23
TileTemplateType_TileWide310x150PeekImage01: TileTemplateType = 24
TileTemplateType_TileWide310x150PeekImage02: TileTemplateType = 25
TileTemplateType_TileWide310x150PeekImage03: TileTemplateType = 26
TileTemplateType_TileWide310x150PeekImage04: TileTemplateType = 27
TileTemplateType_TileWide310x150PeekImage05: TileTemplateType = 28
TileTemplateType_TileWide310x150PeekImage06: TileTemplateType = 29
TileTemplateType_TileWide310x150SmallImageAndText01: TileTemplateType = 30
TileTemplateType_TileWide310x150SmallImageAndText02: TileTemplateType = 31
TileTemplateType_TileWide310x150SmallImageAndText03: TileTemplateType = 32
TileTemplateType_TileWide310x150SmallImageAndText04: TileTemplateType = 33
TileTemplateType_TileWide310x150SmallImageAndText05: TileTemplateType = 34
TileTemplateType_TileWide310x150Text01: TileTemplateType = 35
TileTemplateType_TileWide310x150Text02: TileTemplateType = 36
TileTemplateType_TileWide310x150Text03: TileTemplateType = 37
TileTemplateType_TileWide310x150Text04: TileTemplateType = 38
TileTemplateType_TileWide310x150Text05: TileTemplateType = 39
TileTemplateType_TileWide310x150Text06: TileTemplateType = 40
TileTemplateType_TileWide310x150Text07: TileTemplateType = 41
TileTemplateType_TileWide310x150Text08: TileTemplateType = 42
TileTemplateType_TileWide310x150Text09: TileTemplateType = 43
TileTemplateType_TileWide310x150Text10: TileTemplateType = 44
TileTemplateType_TileWide310x150Text11: TileTemplateType = 45
TileTemplateType_TileSquare310x310BlockAndText01: TileTemplateType = 46
TileTemplateType_TileSquare310x310BlockAndText02: TileTemplateType = 47
TileTemplateType_TileSquare310x310Image: TileTemplateType = 48
TileTemplateType_TileSquare310x310ImageAndText01: TileTemplateType = 49
TileTemplateType_TileSquare310x310ImageAndText02: TileTemplateType = 50
TileTemplateType_TileSquare310x310ImageAndTextOverlay01: TileTemplateType = 51
TileTemplateType_TileSquare310x310ImageAndTextOverlay02: TileTemplateType = 52
TileTemplateType_TileSquare310x310ImageAndTextOverlay03: TileTemplateType = 53
TileTemplateType_TileSquare310x310ImageCollectionAndText01: TileTemplateType = 54
TileTemplateType_TileSquare310x310ImageCollectionAndText02: TileTemplateType = 55
TileTemplateType_TileSquare310x310ImageCollection: TileTemplateType = 56
TileTemplateType_TileSquare310x310SmallImagesAndTextList01: TileTemplateType = 57
TileTemplateType_TileSquare310x310SmallImagesAndTextList02: TileTemplateType = 58
TileTemplateType_TileSquare310x310SmallImagesAndTextList03: TileTemplateType = 59
TileTemplateType_TileSquare310x310SmallImagesAndTextList04: TileTemplateType = 60
TileTemplateType_TileSquare310x310Text01: TileTemplateType = 61
TileTemplateType_TileSquare310x310Text02: TileTemplateType = 62
TileTemplateType_TileSquare310x310Text03: TileTemplateType = 63
TileTemplateType_TileSquare310x310Text04: TileTemplateType = 64
TileTemplateType_TileSquare310x310Text05: TileTemplateType = 65
TileTemplateType_TileSquare310x310Text06: TileTemplateType = 66
TileTemplateType_TileSquare310x310Text07: TileTemplateType = 67
TileTemplateType_TileSquare310x310Text08: TileTemplateType = 68
TileTemplateType_TileSquare310x310TextList01: TileTemplateType = 69
TileTemplateType_TileSquare310x310TextList02: TileTemplateType = 70
TileTemplateType_TileSquare310x310TextList03: TileTemplateType = 71
TileTemplateType_TileSquare310x310SmallImageAndText01: TileTemplateType = 72
TileTemplateType_TileSquare310x310SmallImagesAndTextList05: TileTemplateType = 73
TileTemplateType_TileSquare310x310Text09: TileTemplateType = 74
TileTemplateType_TileSquare71x71IconWithBadge: TileTemplateType = 75
TileTemplateType_TileSquare150x150IconWithBadge: TileTemplateType = 76
TileTemplateType_TileWide310x150IconWithBadgeAndText: TileTemplateType = 77
TileTemplateType_TileSquare71x71Image: TileTemplateType = 78
TileTemplateType_TileTall150x310Image: TileTemplateType = 79
class TileUpdateManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.TileUpdateManager'
    @winrt_classmethod
    def GetForUser(cls: Windows.UI.Notifications.ITileUpdateManagerStatics2, user: Windows.System.User) -> Windows.UI.Notifications.TileUpdateManagerForUser: ...
    @winrt_classmethod
    def CreateTileUpdaterForApplication(cls: Windows.UI.Notifications.ITileUpdateManagerStatics) -> Windows.UI.Notifications.TileUpdater: ...
    @winrt_classmethod
    def CreateTileUpdaterForApplicationWithId(cls: Windows.UI.Notifications.ITileUpdateManagerStatics, applicationId: WinRT_String) -> Windows.UI.Notifications.TileUpdater: ...
    @winrt_classmethod
    def CreateTileUpdaterForSecondaryTile(cls: Windows.UI.Notifications.ITileUpdateManagerStatics, tileId: WinRT_String) -> Windows.UI.Notifications.TileUpdater: ...
    @winrt_classmethod
    def GetTemplateContent(cls: Windows.UI.Notifications.ITileUpdateManagerStatics, type: Windows.UI.Notifications.TileTemplateType) -> Windows.Data.Xml.Dom.XmlDocument: ...
class TileUpdateManagerForUser(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.TileUpdateManagerForUser'
    @winrt_mixinmethod
    def CreateTileUpdaterForApplication(self: Windows.UI.Notifications.ITileUpdateManagerForUser) -> Windows.UI.Notifications.TileUpdater: ...
    @winrt_mixinmethod
    def CreateTileUpdaterForApplicationWithId(self: Windows.UI.Notifications.ITileUpdateManagerForUser, applicationId: WinRT_String) -> Windows.UI.Notifications.TileUpdater: ...
    @winrt_mixinmethod
    def CreateTileUpdaterForSecondaryTile(self: Windows.UI.Notifications.ITileUpdateManagerForUser, tileId: WinRT_String) -> Windows.UI.Notifications.TileUpdater: ...
    @winrt_mixinmethod
    def get_User(self: Windows.UI.Notifications.ITileUpdateManagerForUser) -> Windows.System.User: ...
    User = property(get_User, None)
class TileUpdater(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.TileUpdater'
    @winrt_mixinmethod
    def Update(self: Windows.UI.Notifications.ITileUpdater, notification: Windows.UI.Notifications.TileNotification) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.UI.Notifications.ITileUpdater) -> Void: ...
    @winrt_mixinmethod
    def EnableNotificationQueue(self: Windows.UI.Notifications.ITileUpdater, enable: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Setting(self: Windows.UI.Notifications.ITileUpdater) -> Windows.UI.Notifications.NotificationSetting: ...
    @winrt_mixinmethod
    def AddToSchedule(self: Windows.UI.Notifications.ITileUpdater, scheduledTile: Windows.UI.Notifications.ScheduledTileNotification) -> Void: ...
    @winrt_mixinmethod
    def RemoveFromSchedule(self: Windows.UI.Notifications.ITileUpdater, scheduledTile: Windows.UI.Notifications.ScheduledTileNotification) -> Void: ...
    @winrt_mixinmethod
    def GetScheduledTileNotifications(self: Windows.UI.Notifications.ITileUpdater) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Notifications.ScheduledTileNotification]: ...
    @winrt_mixinmethod
    def StartPeriodicUpdate(self: Windows.UI.Notifications.ITileUpdater, tileContent: Windows.Foundation.Uri, requestedInterval: Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_mixinmethod
    def StartPeriodicUpdateAtTime(self: Windows.UI.Notifications.ITileUpdater, tileContent: Windows.Foundation.Uri, startTime: Windows.Foundation.DateTime, requestedInterval: Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_mixinmethod
    def StopPeriodicUpdate(self: Windows.UI.Notifications.ITileUpdater) -> Void: ...
    @winrt_mixinmethod
    def StartPeriodicUpdateBatch(self: Windows.UI.Notifications.ITileUpdater, tileContents: Windows.Foundation.Collections.IIterable[Windows.Foundation.Uri], requestedInterval: Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_mixinmethod
    def StartPeriodicUpdateBatchAtTime(self: Windows.UI.Notifications.ITileUpdater, tileContents: Windows.Foundation.Collections.IIterable[Windows.Foundation.Uri], startTime: Windows.Foundation.DateTime, requestedInterval: Windows.UI.Notifications.PeriodicUpdateRecurrence) -> Void: ...
    @winrt_mixinmethod
    def EnableNotificationQueueForSquare150x150(self: Windows.UI.Notifications.ITileUpdater2, enable: Boolean) -> Void: ...
    @winrt_mixinmethod
    def EnableNotificationQueueForWide310x150(self: Windows.UI.Notifications.ITileUpdater2, enable: Boolean) -> Void: ...
    @winrt_mixinmethod
    def EnableNotificationQueueForSquare310x310(self: Windows.UI.Notifications.ITileUpdater2, enable: Boolean) -> Void: ...
    Setting = property(get_Setting, None)
class ToastActivatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.ToastActivatedEventArgs'
    @winrt_mixinmethod
    def get_Arguments(self: Windows.UI.Notifications.IToastActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserInput(self: Windows.UI.Notifications.IToastActivatedEventArgs2) -> Windows.Foundation.Collections.ValueSet: ...
    Arguments = property(get_Arguments, None)
    UserInput = property(get_UserInput, None)
class ToastCollection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.ToastCollection'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Notifications.IToastCollectionFactory, collectionId: WinRT_String, displayName: WinRT_String, launchArgs: WinRT_String, iconUri: Windows.Foundation.Uri) -> Windows.UI.Notifications.ToastCollection: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Notifications.IToastCollection) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.UI.Notifications.IToastCollection) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayName(self: Windows.UI.Notifications.IToastCollection, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_LaunchArgs(self: Windows.UI.Notifications.IToastCollection) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LaunchArgs(self: Windows.UI.Notifications.IToastCollection, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Icon(self: Windows.UI.Notifications.IToastCollection) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Icon(self: Windows.UI.Notifications.IToastCollection, value: Windows.Foundation.Uri) -> Void: ...
    Id = property(get_Id, None)
    DisplayName = property(get_DisplayName, put_DisplayName)
    LaunchArgs = property(get_LaunchArgs, put_LaunchArgs)
    Icon = property(get_Icon, put_Icon)
class ToastCollectionManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.ToastCollectionManager'
    @winrt_mixinmethod
    def SaveToastCollectionAsync(self: Windows.UI.Notifications.IToastCollectionManager, collection: Windows.UI.Notifications.ToastCollection) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def FindAllToastCollectionsAsync(self: Windows.UI.Notifications.IToastCollectionManager) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.UI.Notifications.ToastCollection]]: ...
    @winrt_mixinmethod
    def GetToastCollectionAsync(self: Windows.UI.Notifications.IToastCollectionManager, collectionId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.UI.Notifications.ToastCollection]: ...
    @winrt_mixinmethod
    def RemoveToastCollectionAsync(self: Windows.UI.Notifications.IToastCollectionManager, collectionId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RemoveAllToastCollectionsAsync(self: Windows.UI.Notifications.IToastCollectionManager) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_User(self: Windows.UI.Notifications.IToastCollectionManager) -> Windows.System.User: ...
    @winrt_mixinmethod
    def get_AppId(self: Windows.UI.Notifications.IToastCollectionManager) -> WinRT_String: ...
    User = property(get_User, None)
    AppId = property(get_AppId, None)
ToastDismissalReason = Int32
ToastDismissalReason_UserCanceled: ToastDismissalReason = 0
ToastDismissalReason_ApplicationHidden: ToastDismissalReason = 1
ToastDismissalReason_TimedOut: ToastDismissalReason = 2
class ToastDismissedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.ToastDismissedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: Windows.UI.Notifications.IToastDismissedEventArgs) -> Windows.UI.Notifications.ToastDismissalReason: ...
    Reason = property(get_Reason, None)
class ToastFailedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.ToastFailedEventArgs'
    @winrt_mixinmethod
    def get_ErrorCode(self: Windows.UI.Notifications.IToastFailedEventArgs) -> Windows.Foundation.HResult: ...
    ErrorCode = property(get_ErrorCode, None)
ToastHistoryChangedType = Int32
ToastHistoryChangedType_Cleared: ToastHistoryChangedType = 0
ToastHistoryChangedType_Removed: ToastHistoryChangedType = 1
ToastHistoryChangedType_Expired: ToastHistoryChangedType = 2
ToastHistoryChangedType_Added: ToastHistoryChangedType = 3
class ToastNotification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.ToastNotification'
    @winrt_factorymethod
    def CreateToastNotification(cls: Windows.UI.Notifications.IToastNotificationFactory, content: Windows.Data.Xml.Dom.XmlDocument) -> Windows.UI.Notifications.ToastNotification: ...
    @winrt_mixinmethod
    def get_Content(self: Windows.UI.Notifications.IToastNotification) -> Windows.Data.Xml.Dom.XmlDocument: ...
    @winrt_mixinmethod
    def put_ExpirationTime(self: Windows.UI.Notifications.IToastNotification, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_ExpirationTime(self: Windows.UI.Notifications.IToastNotification) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def add_Dismissed(self: Windows.UI.Notifications.IToastNotification, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Notifications.ToastNotification, Windows.UI.Notifications.ToastDismissedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Dismissed(self: Windows.UI.Notifications.IToastNotification, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Activated(self: Windows.UI.Notifications.IToastNotification, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Notifications.ToastNotification, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Activated(self: Windows.UI.Notifications.IToastNotification, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Failed(self: Windows.UI.Notifications.IToastNotification, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Notifications.ToastNotification, Windows.UI.Notifications.ToastFailedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Failed(self: Windows.UI.Notifications.IToastNotification, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_Tag(self: Windows.UI.Notifications.IToastNotification2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Tag(self: Windows.UI.Notifications.IToastNotification2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Group(self: Windows.UI.Notifications.IToastNotification2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Group(self: Windows.UI.Notifications.IToastNotification2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SuppressPopup(self: Windows.UI.Notifications.IToastNotification2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SuppressPopup(self: Windows.UI.Notifications.IToastNotification2) -> Boolean: ...
    @winrt_mixinmethod
    def get_NotificationMirroring(self: Windows.UI.Notifications.IToastNotification3) -> Windows.UI.Notifications.NotificationMirroring: ...
    @winrt_mixinmethod
    def put_NotificationMirroring(self: Windows.UI.Notifications.IToastNotification3, value: Windows.UI.Notifications.NotificationMirroring) -> Void: ...
    @winrt_mixinmethod
    def get_RemoteId(self: Windows.UI.Notifications.IToastNotification3) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_RemoteId(self: Windows.UI.Notifications.IToastNotification3, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.UI.Notifications.IToastNotification4) -> Windows.UI.Notifications.NotificationData: ...
    @winrt_mixinmethod
    def put_Data(self: Windows.UI.Notifications.IToastNotification4, value: Windows.UI.Notifications.NotificationData) -> Void: ...
    @winrt_mixinmethod
    def get_Priority(self: Windows.UI.Notifications.IToastNotification4) -> Windows.UI.Notifications.ToastNotificationPriority: ...
    @winrt_mixinmethod
    def put_Priority(self: Windows.UI.Notifications.IToastNotification4, value: Windows.UI.Notifications.ToastNotificationPriority) -> Void: ...
    @winrt_mixinmethod
    def get_ExpiresOnReboot(self: Windows.UI.Notifications.IToastNotification6) -> Boolean: ...
    @winrt_mixinmethod
    def put_ExpiresOnReboot(self: Windows.UI.Notifications.IToastNotification6, value: Boolean) -> Void: ...
    Content = property(get_Content, None)
    ExpirationTime = property(get_ExpirationTime, put_ExpirationTime)
    Tag = property(get_Tag, put_Tag)
    Group = property(get_Group, put_Group)
    SuppressPopup = property(get_SuppressPopup, put_SuppressPopup)
    NotificationMirroring = property(get_NotificationMirroring, put_NotificationMirroring)
    RemoteId = property(get_RemoteId, put_RemoteId)
    Data = property(get_Data, put_Data)
    Priority = property(get_Priority, put_Priority)
    ExpiresOnReboot = property(get_ExpiresOnReboot, put_ExpiresOnReboot)
class ToastNotificationActionTriggerDetail(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.ToastNotificationActionTriggerDetail'
    @winrt_mixinmethod
    def get_Argument(self: Windows.UI.Notifications.IToastNotificationActionTriggerDetail) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserInput(self: Windows.UI.Notifications.IToastNotificationActionTriggerDetail) -> Windows.Foundation.Collections.ValueSet: ...
    Argument = property(get_Argument, None)
    UserInput = property(get_UserInput, None)
class ToastNotificationHistory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.ToastNotificationHistory'
    @winrt_mixinmethod
    def GetHistory(self: Windows.UI.Notifications.IToastNotificationHistory2) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Notifications.ToastNotification]: ...
    @winrt_mixinmethod
    def GetHistoryWithId(self: Windows.UI.Notifications.IToastNotificationHistory2, applicationId: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Notifications.ToastNotification]: ...
    @winrt_mixinmethod
    def RemoveGroup(self: Windows.UI.Notifications.IToastNotificationHistory, group: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RemoveGroupWithId(self: Windows.UI.Notifications.IToastNotificationHistory, group: WinRT_String, applicationId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RemoveGroupedTagWithId(self: Windows.UI.Notifications.IToastNotificationHistory, tag: WinRT_String, group: WinRT_String, applicationId: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RemoveGroupedTag(self: Windows.UI.Notifications.IToastNotificationHistory, tag: WinRT_String, group: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Remove(self: Windows.UI.Notifications.IToastNotificationHistory, tag: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.UI.Notifications.IToastNotificationHistory) -> Void: ...
    @winrt_mixinmethod
    def ClearWithId(self: Windows.UI.Notifications.IToastNotificationHistory, applicationId: WinRT_String) -> Void: ...
class ToastNotificationHistoryChangedTriggerDetail(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.ToastNotificationHistoryChangedTriggerDetail'
    @winrt_mixinmethod
    def get_ChangeType(self: Windows.UI.Notifications.IToastNotificationHistoryChangedTriggerDetail) -> Windows.UI.Notifications.ToastHistoryChangedType: ...
    @winrt_mixinmethod
    def get_CollectionId(self: Windows.UI.Notifications.IToastNotificationHistoryChangedTriggerDetail2) -> WinRT_String: ...
    ChangeType = property(get_ChangeType, None)
    CollectionId = property(get_CollectionId, None)
class ToastNotificationManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.ToastNotificationManager'
    @winrt_classmethod
    def GetDefault(cls: Windows.UI.Notifications.IToastNotificationManagerStatics5) -> Windows.UI.Notifications.ToastNotificationManagerForUser: ...
    @winrt_classmethod
    def GetForUser(cls: Windows.UI.Notifications.IToastNotificationManagerStatics4, user: Windows.System.User) -> Windows.UI.Notifications.ToastNotificationManagerForUser: ...
    @winrt_classmethod
    def ConfigureNotificationMirroring(cls: Windows.UI.Notifications.IToastNotificationManagerStatics4, value: Windows.UI.Notifications.NotificationMirroring) -> Void: ...
    @winrt_classmethod
    def get_History(cls: Windows.UI.Notifications.IToastNotificationManagerStatics2) -> Windows.UI.Notifications.ToastNotificationHistory: ...
    @winrt_classmethod
    def CreateToastNotifier(cls: Windows.UI.Notifications.IToastNotificationManagerStatics) -> Windows.UI.Notifications.ToastNotifier: ...
    @winrt_classmethod
    def CreateToastNotifierWithId(cls: Windows.UI.Notifications.IToastNotificationManagerStatics, applicationId: WinRT_String) -> Windows.UI.Notifications.ToastNotifier: ...
    @winrt_classmethod
    def GetTemplateContent(cls: Windows.UI.Notifications.IToastNotificationManagerStatics, type: Windows.UI.Notifications.ToastTemplateType) -> Windows.Data.Xml.Dom.XmlDocument: ...
    History = property(get_History, None)
class ToastNotificationManagerForUser(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.ToastNotificationManagerForUser'
    @winrt_mixinmethod
    def CreateToastNotifier(self: Windows.UI.Notifications.IToastNotificationManagerForUser) -> Windows.UI.Notifications.ToastNotifier: ...
    @winrt_mixinmethod
    def CreateToastNotifierWithId(self: Windows.UI.Notifications.IToastNotificationManagerForUser, applicationId: WinRT_String) -> Windows.UI.Notifications.ToastNotifier: ...
    @winrt_mixinmethod
    def get_History(self: Windows.UI.Notifications.IToastNotificationManagerForUser) -> Windows.UI.Notifications.ToastNotificationHistory: ...
    @winrt_mixinmethod
    def get_User(self: Windows.UI.Notifications.IToastNotificationManagerForUser) -> Windows.System.User: ...
    @winrt_mixinmethod
    def GetToastNotifierForToastCollectionIdAsync(self: Windows.UI.Notifications.IToastNotificationManagerForUser2, collectionId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.UI.Notifications.ToastNotifier]: ...
    @winrt_mixinmethod
    def GetHistoryForToastCollectionIdAsync(self: Windows.UI.Notifications.IToastNotificationManagerForUser2, collectionId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.UI.Notifications.ToastNotificationHistory]: ...
    @winrt_mixinmethod
    def GetToastCollectionManager(self: Windows.UI.Notifications.IToastNotificationManagerForUser2) -> Windows.UI.Notifications.ToastCollectionManager: ...
    @winrt_mixinmethod
    def GetToastCollectionManagerWithAppId(self: Windows.UI.Notifications.IToastNotificationManagerForUser2, appId: WinRT_String) -> Windows.UI.Notifications.ToastCollectionManager: ...
    @winrt_mixinmethod
    def get_NotificationMode(self: Windows.UI.Notifications.IToastNotificationManagerForUser3) -> Windows.UI.Notifications.ToastNotificationMode: ...
    @winrt_mixinmethod
    def add_NotificationModeChanged(self: Windows.UI.Notifications.IToastNotificationManagerForUser3, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Notifications.ToastNotificationManagerForUser, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NotificationModeChanged(self: Windows.UI.Notifications.IToastNotificationManagerForUser3, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    History = property(get_History, None)
    User = property(get_User, None)
    NotificationMode = property(get_NotificationMode, None)
ToastNotificationMode = Int32
ToastNotificationMode_Unrestricted: ToastNotificationMode = 0
ToastNotificationMode_PriorityOnly: ToastNotificationMode = 1
ToastNotificationMode_AlarmsOnly: ToastNotificationMode = 2
ToastNotificationPriority = Int32
ToastNotificationPriority_Default: ToastNotificationPriority = 0
ToastNotificationPriority_High: ToastNotificationPriority = 1
class ToastNotifier(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.ToastNotifier'
    @winrt_mixinmethod
    def Show(self: Windows.UI.Notifications.IToastNotifier, notification: Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_mixinmethod
    def Hide(self: Windows.UI.Notifications.IToastNotifier, notification: Windows.UI.Notifications.ToastNotification) -> Void: ...
    @winrt_mixinmethod
    def get_Setting(self: Windows.UI.Notifications.IToastNotifier) -> Windows.UI.Notifications.NotificationSetting: ...
    @winrt_mixinmethod
    def AddToSchedule(self: Windows.UI.Notifications.IToastNotifier, scheduledToast: Windows.UI.Notifications.ScheduledToastNotification) -> Void: ...
    @winrt_mixinmethod
    def RemoveFromSchedule(self: Windows.UI.Notifications.IToastNotifier, scheduledToast: Windows.UI.Notifications.ScheduledToastNotification) -> Void: ...
    @winrt_mixinmethod
    def GetScheduledToastNotifications(self: Windows.UI.Notifications.IToastNotifier) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Notifications.ScheduledToastNotification]: ...
    @winrt_mixinmethod
    def UpdateWithTagAndGroup(self: Windows.UI.Notifications.IToastNotifier2, data: Windows.UI.Notifications.NotificationData, tag: WinRT_String, group: WinRT_String) -> Windows.UI.Notifications.NotificationUpdateResult: ...
    @winrt_mixinmethod
    def UpdateWithTag(self: Windows.UI.Notifications.IToastNotifier2, data: Windows.UI.Notifications.NotificationData, tag: WinRT_String) -> Windows.UI.Notifications.NotificationUpdateResult: ...
    @winrt_mixinmethod
    def add_ScheduledToastNotificationShowing(self: Windows.UI.Notifications.IToastNotifier3, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Notifications.ToastNotifier, Windows.UI.Notifications.ScheduledToastNotificationShowingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScheduledToastNotificationShowing(self: Windows.UI.Notifications.IToastNotifier3, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Setting = property(get_Setting, None)
ToastTemplateType = Int32
ToastTemplateType_ToastImageAndText01: ToastTemplateType = 0
ToastTemplateType_ToastImageAndText02: ToastTemplateType = 1
ToastTemplateType_ToastImageAndText03: ToastTemplateType = 2
ToastTemplateType_ToastImageAndText04: ToastTemplateType = 3
ToastTemplateType_ToastText01: ToastTemplateType = 4
ToastTemplateType_ToastText02: ToastTemplateType = 5
ToastTemplateType_ToastText03: ToastTemplateType = 6
ToastTemplateType_ToastText04: ToastTemplateType = 7
class UserNotification(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.UserNotification'
    @winrt_mixinmethod
    def get_Notification(self: Windows.UI.Notifications.IUserNotification) -> Windows.UI.Notifications.Notification: ...
    @winrt_mixinmethod
    def get_AppInfo(self: Windows.UI.Notifications.IUserNotification) -> Windows.ApplicationModel.AppInfo: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Notifications.IUserNotification) -> UInt32: ...
    @winrt_mixinmethod
    def get_CreationTime(self: Windows.UI.Notifications.IUserNotification) -> Windows.Foundation.DateTime: ...
    Notification = property(get_Notification, None)
    AppInfo = property(get_AppInfo, None)
    Id = property(get_Id, None)
    CreationTime = property(get_CreationTime, None)
class UserNotificationChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Notifications.UserNotificationChangedEventArgs'
    @winrt_mixinmethod
    def get_ChangeKind(self: Windows.UI.Notifications.IUserNotificationChangedEventArgs) -> Windows.UI.Notifications.UserNotificationChangedKind: ...
    @winrt_mixinmethod
    def get_UserNotificationId(self: Windows.UI.Notifications.IUserNotificationChangedEventArgs) -> UInt32: ...
    ChangeKind = property(get_ChangeKind, None)
    UserNotificationId = property(get_UserNotificationId, None)
UserNotificationChangedKind = Int32
UserNotificationChangedKind_Added: UserNotificationChangedKind = 0
UserNotificationChangedKind_Removed: UserNotificationChangedKind = 1
make_head(_module, 'AdaptiveNotificationText')
make_head(_module, 'BadgeNotification')
make_head(_module, 'BadgeUpdateManager')
make_head(_module, 'BadgeUpdateManagerForUser')
make_head(_module, 'BadgeUpdater')
make_head(_module, 'IAdaptiveNotificationContent')
make_head(_module, 'IAdaptiveNotificationText')
make_head(_module, 'IBadgeNotification')
make_head(_module, 'IBadgeNotificationFactory')
make_head(_module, 'IBadgeUpdateManagerForUser')
make_head(_module, 'IBadgeUpdateManagerStatics')
make_head(_module, 'IBadgeUpdateManagerStatics2')
make_head(_module, 'IBadgeUpdater')
make_head(_module, 'IKnownAdaptiveNotificationHintsStatics')
make_head(_module, 'IKnownAdaptiveNotificationTextStylesStatics')
make_head(_module, 'IKnownNotificationBindingsStatics')
make_head(_module, 'INotification')
make_head(_module, 'INotificationBinding')
make_head(_module, 'INotificationData')
make_head(_module, 'INotificationDataFactory')
make_head(_module, 'INotificationVisual')
make_head(_module, 'IScheduledTileNotification')
make_head(_module, 'IScheduledTileNotificationFactory')
make_head(_module, 'IScheduledToastNotification')
make_head(_module, 'IScheduledToastNotification2')
make_head(_module, 'IScheduledToastNotification3')
make_head(_module, 'IScheduledToastNotification4')
make_head(_module, 'IScheduledToastNotificationFactory')
make_head(_module, 'IScheduledToastNotificationShowingEventArgs')
make_head(_module, 'IShownTileNotification')
make_head(_module, 'ITileFlyoutNotification')
make_head(_module, 'ITileFlyoutNotificationFactory')
make_head(_module, 'ITileFlyoutUpdateManagerStatics')
make_head(_module, 'ITileFlyoutUpdater')
make_head(_module, 'ITileNotification')
make_head(_module, 'ITileNotificationFactory')
make_head(_module, 'ITileUpdateManagerForUser')
make_head(_module, 'ITileUpdateManagerStatics')
make_head(_module, 'ITileUpdateManagerStatics2')
make_head(_module, 'ITileUpdater')
make_head(_module, 'ITileUpdater2')
make_head(_module, 'IToastActivatedEventArgs')
make_head(_module, 'IToastActivatedEventArgs2')
make_head(_module, 'IToastCollection')
make_head(_module, 'IToastCollectionFactory')
make_head(_module, 'IToastCollectionManager')
make_head(_module, 'IToastDismissedEventArgs')
make_head(_module, 'IToastFailedEventArgs')
make_head(_module, 'IToastNotification')
make_head(_module, 'IToastNotification2')
make_head(_module, 'IToastNotification3')
make_head(_module, 'IToastNotification4')
make_head(_module, 'IToastNotification6')
make_head(_module, 'IToastNotificationActionTriggerDetail')
make_head(_module, 'IToastNotificationFactory')
make_head(_module, 'IToastNotificationHistory')
make_head(_module, 'IToastNotificationHistory2')
make_head(_module, 'IToastNotificationHistoryChangedTriggerDetail')
make_head(_module, 'IToastNotificationHistoryChangedTriggerDetail2')
make_head(_module, 'IToastNotificationManagerForUser')
make_head(_module, 'IToastNotificationManagerForUser2')
make_head(_module, 'IToastNotificationManagerForUser3')
make_head(_module, 'IToastNotificationManagerStatics')
make_head(_module, 'IToastNotificationManagerStatics2')
make_head(_module, 'IToastNotificationManagerStatics4')
make_head(_module, 'IToastNotificationManagerStatics5')
make_head(_module, 'IToastNotifier')
make_head(_module, 'IToastNotifier2')
make_head(_module, 'IToastNotifier3')
make_head(_module, 'IUserNotification')
make_head(_module, 'IUserNotificationChangedEventArgs')
make_head(_module, 'KnownAdaptiveNotificationHints')
make_head(_module, 'KnownAdaptiveNotificationTextStyles')
make_head(_module, 'KnownNotificationBindings')
make_head(_module, 'Notification')
make_head(_module, 'NotificationBinding')
make_head(_module, 'NotificationData')
make_head(_module, 'NotificationVisual')
make_head(_module, 'ScheduledTileNotification')
make_head(_module, 'ScheduledToastNotification')
make_head(_module, 'ScheduledToastNotificationShowingEventArgs')
make_head(_module, 'ShownTileNotification')
make_head(_module, 'TileFlyoutNotification')
make_head(_module, 'TileFlyoutUpdateManager')
make_head(_module, 'TileFlyoutUpdater')
make_head(_module, 'TileNotification')
make_head(_module, 'TileUpdateManager')
make_head(_module, 'TileUpdateManagerForUser')
make_head(_module, 'TileUpdater')
make_head(_module, 'ToastActivatedEventArgs')
make_head(_module, 'ToastCollection')
make_head(_module, 'ToastCollectionManager')
make_head(_module, 'ToastDismissedEventArgs')
make_head(_module, 'ToastFailedEventArgs')
make_head(_module, 'ToastNotification')
make_head(_module, 'ToastNotificationActionTriggerDetail')
make_head(_module, 'ToastNotificationHistory')
make_head(_module, 'ToastNotificationHistoryChangedTriggerDetail')
make_head(_module, 'ToastNotificationManager')
make_head(_module, 'ToastNotificationManagerForUser')
make_head(_module, 'ToastNotifier')
make_head(_module, 'UserNotification')
make_head(_module, 'UserNotificationChangedEventArgs')
