from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.UserActivities
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Security.Credentials
import Windows.System
import Windows.UI
import Windows.UI.Shell
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IUserActivity(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fc103e9e-2cab-4d36-ae-a2-b4-bb-55-6c-ef-0f')
    @winrt_commethod(6)
    def get_State(self) -> Windows.ApplicationModel.UserActivities.UserActivityState: ...
    @winrt_commethod(7)
    def get_ActivityId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_VisualElements(self) -> Windows.ApplicationModel.UserActivities.UserActivityVisualElements: ...
    @winrt_commethod(9)
    def get_ContentUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(10)
    def put_ContentUri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(11)
    def get_ContentType(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_ContentType(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_FallbackUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(14)
    def put_FallbackUri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(15)
    def get_ActivationUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(16)
    def put_ActivationUri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(17)
    def get_ContentInfo(self) -> Windows.ApplicationModel.UserActivities.IUserActivityContentInfo: ...
    @winrt_commethod(18)
    def put_ContentInfo(self, value: Windows.ApplicationModel.UserActivities.IUserActivityContentInfo) -> Void: ...
    @winrt_commethod(19)
    def SaveAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(20)
    def CreateSession(self) -> Windows.ApplicationModel.UserActivities.UserActivitySession: ...
    State = property(get_State, None)
    ActivityId = property(get_ActivityId, None)
    VisualElements = property(get_VisualElements, None)
    ContentUri = property(get_ContentUri, put_ContentUri)
    ContentType = property(get_ContentType, put_ContentType)
    FallbackUri = property(get_FallbackUri, put_FallbackUri)
    ActivationUri = property(get_ActivationUri, put_ActivationUri)
    ContentInfo = property(get_ContentInfo, put_ContentInfo)
class IUserActivity2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9dc40c62-08c4-47ac-aa-9c-2b-b2-22-1c-55-fd')
    @winrt_commethod(6)
    def ToJson(self) -> WinRT_String: ...
class IUserActivity3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e7697744-e1a2-5147-8e-06-55-f1-ee-ef-27-1c')
    @winrt_commethod(6)
    def get_IsRoamable(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsRoamable(self, value: Boolean) -> Void: ...
    IsRoamable = property(get_IsRoamable, put_IsRoamable)
class IUserActivityAttribution(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('34a5c8b5-86dd-4aec-a4-91-6a-4f-ae-a5-d2-2e')
    @winrt_commethod(6)
    def get_IconUri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_IconUri(self, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_AlternateText(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_AlternateText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_AddImageQuery(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_AddImageQuery(self, value: Boolean) -> Void: ...
    IconUri = property(get_IconUri, put_IconUri)
    AlternateText = property(get_AlternateText, put_AlternateText)
    AddImageQuery = property(get_AddImageQuery, put_AddImageQuery)
class IUserActivityAttributionFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e62bd252-c566-4f42-99-74-91-6c-4d-76-37-7e')
    @winrt_commethod(6)
    def CreateWithUri(self, iconUri: Windows.Foundation.Uri) -> Windows.ApplicationModel.UserActivities.UserActivityAttribution: ...
class IUserActivityChannel(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bac0f8b8-a0e4-483b-b9-48-9c-ba-bd-06-07-0c')
    @winrt_commethod(6)
    def GetOrCreateUserActivityAsync(self, activityId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserActivities.UserActivity]: ...
    @winrt_commethod(7)
    def DeleteActivityAsync(self, activityId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def DeleteAllActivitiesAsync(self) -> Windows.Foundation.IAsyncAction: ...
class IUserActivityChannel2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1698e35b-eb7e-4ea0-bf-17-a4-59-e8-be-70-6c')
    @winrt_commethod(6)
    def GetRecentUserActivitiesAsync(self, maxUniqueActivities: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.ApplicationModel.UserActivities.UserActivitySessionHistoryItem]]: ...
    @winrt_commethod(7)
    def GetSessionHistoryItemsForUserActivityAsync(self, activityId: WinRT_String, startTime: Windows.Foundation.DateTime) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.ApplicationModel.UserActivities.UserActivitySessionHistoryItem]]: ...
class IUserActivityChannelStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c8c005ab-198d-4d80-ab-b2-c9-77-5e-c4-a7-29')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.ApplicationModel.UserActivities.UserActivityChannel: ...
class IUserActivityChannelStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8e87de30-aa4f-4624-9a-d0-d4-0f-3b-a0-31-7c')
    @winrt_commethod(6)
    def DisableAutoSessionCreation(self) -> Void: ...
    @winrt_commethod(7)
    def TryGetForWebAccount(self, account: Windows.Security.Credentials.WebAccount) -> Windows.ApplicationModel.UserActivities.UserActivityChannel: ...
class IUserActivityChannelStatics3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('53bc4ddb-bbdf-5984-80-2a-53-05-87-4e-20-5c')
    @winrt_commethod(6)
    def GetForUser(self, user: Windows.System.User) -> Windows.ApplicationModel.UserActivities.UserActivityChannel: ...
class IUserActivityContentInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b399e5ad-137f-409d-82-2d-e1-af-27-ce-08-dc')
    @winrt_commethod(6)
    def ToJson(self) -> WinRT_String: ...
class IUserActivityContentInfoStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9988c34b-0386-4bc9-96-8a-82-00-b0-04-14-4f')
    @winrt_commethod(6)
    def FromJson(self, value: WinRT_String) -> Windows.ApplicationModel.UserActivities.UserActivityContentInfo: ...
class IUserActivityFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7c385758-361d-4a67-8a-3b-34-ca-29-78-f9-a3')
    @winrt_commethod(6)
    def CreateWithActivityId(self, activityId: WinRT_String) -> Windows.ApplicationModel.UserActivities.UserActivity: ...
class IUserActivityRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a0ef6355-cf35-4ff0-88-33-50-cb-4b-72-e0-6d')
    @winrt_commethod(6)
    def SetUserActivity(self, activity: Windows.ApplicationModel.UserActivities.UserActivity) -> Void: ...
class IUserActivityRequestManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0c30be4e-903d-48d6-82-d4-40-43-ed-57-79-1b')
    @winrt_commethod(6)
    def add_UserActivityRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserActivities.UserActivityRequestManager, Windows.ApplicationModel.UserActivities.UserActivityRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_UserActivityRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IUserActivityRequestManagerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c0392df1-224a-432c-81-e5-0c-76-b4-c4-ce-fa')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.ApplicationModel.UserActivities.UserActivityRequestManager: ...
class IUserActivityRequestedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a4cc7a4c-8229-4cfd-a3-bc-c6-1d-31-85-75-a4')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.ApplicationModel.UserActivities.UserActivityRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IUserActivitySession(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ae434d78-24fa-44a3-ad-48-6e-da-61-aa-19-24')
    @winrt_commethod(6)
    def get_ActivityId(self) -> WinRT_String: ...
    ActivityId = property(get_ActivityId, None)
class IUserActivitySessionHistoryItem(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e8d59bd3-3e5d-49fd-98-d7-6d-a9-75-21-e2-55')
    @winrt_commethod(6)
    def get_UserActivity(self) -> Windows.ApplicationModel.UserActivities.UserActivity: ...
    @winrt_commethod(7)
    def get_StartTime(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_EndTime(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    UserActivity = property(get_UserActivity, None)
    StartTime = property(get_StartTime, None)
    EndTime = property(get_EndTime, None)
class IUserActivityStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8c8fd333-0e09-47f6-9a-c7-95-cf-5c-39-36-7b')
    @winrt_commethod(6)
    def TryParseFromJson(self, json: WinRT_String) -> Windows.ApplicationModel.UserActivities.UserActivity: ...
    @winrt_commethod(7)
    def TryParseFromJsonArray(self, json: WinRT_String) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.UserActivities.UserActivity]: ...
    @winrt_commethod(8)
    def ToJsonArray(self, activities: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.UserActivities.UserActivity]) -> WinRT_String: ...
class IUserActivityVisualElements(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('94757513-262f-49ef-bb-bf-9b-75-d2-e8-52-50')
    @winrt_commethod(6)
    def get_DisplayText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DisplayText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_BackgroundColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(11)
    def put_BackgroundColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(12)
    def get_Attribution(self) -> Windows.ApplicationModel.UserActivities.UserActivityAttribution: ...
    @winrt_commethod(13)
    def put_Attribution(self, value: Windows.ApplicationModel.UserActivities.UserActivityAttribution) -> Void: ...
    @winrt_commethod(14)
    def put_Content(self, value: Windows.UI.Shell.IAdaptiveCard) -> Void: ...
    @winrt_commethod(15)
    def get_Content(self) -> Windows.UI.Shell.IAdaptiveCard: ...
    DisplayText = property(get_DisplayText, put_DisplayText)
    Description = property(get_Description, put_Description)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    Attribution = property(get_Attribution, put_Attribution)
    Content = property(get_Content, put_Content)
class IUserActivityVisualElements2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('caae7fc7-3eef-4359-82-5c-9d-51-b9-22-0d-e3')
    @winrt_commethod(6)
    def get_AttributionDisplayText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_AttributionDisplayText(self, value: WinRT_String) -> Void: ...
    AttributionDisplayText = property(get_AttributionDisplayText, put_AttributionDisplayText)
class UserActivity(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserActivities.UserActivity'
    @winrt_factorymethod
    def CreateWithActivityId(cls: Windows.ApplicationModel.UserActivities.IUserActivityFactory, activityId: WinRT_String) -> Windows.ApplicationModel.UserActivities.UserActivity: ...
    @winrt_mixinmethod
    def get_State(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> Windows.ApplicationModel.UserActivities.UserActivityState: ...
    @winrt_mixinmethod
    def get_ActivityId(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_VisualElements(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> Windows.ApplicationModel.UserActivities.UserActivityVisualElements: ...
    @winrt_mixinmethod
    def get_ContentUri(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_ContentUri(self: Windows.ApplicationModel.UserActivities.IUserActivity, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ContentType(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentType(self: Windows.ApplicationModel.UserActivities.IUserActivity, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FallbackUri(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_FallbackUri(self: Windows.ApplicationModel.UserActivities.IUserActivity, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ActivationUri(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_ActivationUri(self: Windows.ApplicationModel.UserActivities.IUserActivity, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ContentInfo(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> Windows.ApplicationModel.UserActivities.IUserActivityContentInfo: ...
    @winrt_mixinmethod
    def put_ContentInfo(self: Windows.ApplicationModel.UserActivities.IUserActivity, value: Windows.ApplicationModel.UserActivities.IUserActivityContentInfo) -> Void: ...
    @winrt_mixinmethod
    def SaveAsync(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CreateSession(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> Windows.ApplicationModel.UserActivities.UserActivitySession: ...
    @winrt_mixinmethod
    def ToJson(self: Windows.ApplicationModel.UserActivities.IUserActivity2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsRoamable(self: Windows.ApplicationModel.UserActivities.IUserActivity3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsRoamable(self: Windows.ApplicationModel.UserActivities.IUserActivity3, value: Boolean) -> Void: ...
    @winrt_classmethod
    def TryParseFromJson(cls: Windows.ApplicationModel.UserActivities.IUserActivityStatics, json: WinRT_String) -> Windows.ApplicationModel.UserActivities.UserActivity: ...
    @winrt_classmethod
    def TryParseFromJsonArray(cls: Windows.ApplicationModel.UserActivities.IUserActivityStatics, json: WinRT_String) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.UserActivities.UserActivity]: ...
    @winrt_classmethod
    def ToJsonArray(cls: Windows.ApplicationModel.UserActivities.IUserActivityStatics, activities: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.UserActivities.UserActivity]) -> WinRT_String: ...
    State = property(get_State, None)
    ActivityId = property(get_ActivityId, None)
    VisualElements = property(get_VisualElements, None)
    ContentUri = property(get_ContentUri, put_ContentUri)
    ContentType = property(get_ContentType, put_ContentType)
    FallbackUri = property(get_FallbackUri, put_FallbackUri)
    ActivationUri = property(get_ActivationUri, put_ActivationUri)
    ContentInfo = property(get_ContentInfo, put_ContentInfo)
    IsRoamable = property(get_IsRoamable, put_IsRoamable)
class UserActivityAttribution(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserActivities.UserActivityAttribution'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.UserActivities.UserActivityAttribution: ...
    @winrt_factorymethod
    def CreateWithUri(cls: Windows.ApplicationModel.UserActivities.IUserActivityAttributionFactory, iconUri: Windows.Foundation.Uri) -> Windows.ApplicationModel.UserActivities.UserActivityAttribution: ...
    @winrt_mixinmethod
    def get_IconUri(self: Windows.ApplicationModel.UserActivities.IUserActivityAttribution) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_IconUri(self: Windows.ApplicationModel.UserActivities.IUserActivityAttribution, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_AlternateText(self: Windows.ApplicationModel.UserActivities.IUserActivityAttribution) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AlternateText(self: Windows.ApplicationModel.UserActivities.IUserActivityAttribution, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AddImageQuery(self: Windows.ApplicationModel.UserActivities.IUserActivityAttribution) -> Boolean: ...
    @winrt_mixinmethod
    def put_AddImageQuery(self: Windows.ApplicationModel.UserActivities.IUserActivityAttribution, value: Boolean) -> Void: ...
    IconUri = property(get_IconUri, put_IconUri)
    AlternateText = property(get_AlternateText, put_AlternateText)
    AddImageQuery = property(get_AddImageQuery, put_AddImageQuery)
class UserActivityChannel(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserActivities.UserActivityChannel'
    @winrt_mixinmethod
    def GetOrCreateUserActivityAsync(self: Windows.ApplicationModel.UserActivities.IUserActivityChannel, activityId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserActivities.UserActivity]: ...
    @winrt_mixinmethod
    def DeleteActivityAsync(self: Windows.ApplicationModel.UserActivities.IUserActivityChannel, activityId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAllActivitiesAsync(self: Windows.ApplicationModel.UserActivities.IUserActivityChannel) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetRecentUserActivitiesAsync(self: Windows.ApplicationModel.UserActivities.IUserActivityChannel2, maxUniqueActivities: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.ApplicationModel.UserActivities.UserActivitySessionHistoryItem]]: ...
    @winrt_mixinmethod
    def GetSessionHistoryItemsForUserActivityAsync(self: Windows.ApplicationModel.UserActivities.IUserActivityChannel2, activityId: WinRT_String, startTime: Windows.Foundation.DateTime) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.ApplicationModel.UserActivities.UserActivitySessionHistoryItem]]: ...
    @winrt_classmethod
    def GetForUser(cls: Windows.ApplicationModel.UserActivities.IUserActivityChannelStatics3, user: Windows.System.User) -> Windows.ApplicationModel.UserActivities.UserActivityChannel: ...
    @winrt_classmethod
    def DisableAutoSessionCreation(cls: Windows.ApplicationModel.UserActivities.IUserActivityChannelStatics2) -> Void: ...
    @winrt_classmethod
    def TryGetForWebAccount(cls: Windows.ApplicationModel.UserActivities.IUserActivityChannelStatics2, account: Windows.Security.Credentials.WebAccount) -> Windows.ApplicationModel.UserActivities.UserActivityChannel: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.ApplicationModel.UserActivities.IUserActivityChannelStatics) -> Windows.ApplicationModel.UserActivities.UserActivityChannel: ...
class UserActivityContentInfo(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserActivities.UserActivityContentInfo'
    @winrt_mixinmethod
    def ToJson(self: Windows.ApplicationModel.UserActivities.IUserActivityContentInfo) -> WinRT_String: ...
    @winrt_classmethod
    def FromJson(cls: Windows.ApplicationModel.UserActivities.IUserActivityContentInfoStatics, value: WinRT_String) -> Windows.ApplicationModel.UserActivities.UserActivityContentInfo: ...
class UserActivityRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserActivities.UserActivityRequest'
    @winrt_mixinmethod
    def SetUserActivity(self: Windows.ApplicationModel.UserActivities.IUserActivityRequest, activity: Windows.ApplicationModel.UserActivities.UserActivity) -> Void: ...
class UserActivityRequestManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserActivities.UserActivityRequestManager'
    @winrt_mixinmethod
    def add_UserActivityRequested(self: Windows.ApplicationModel.UserActivities.IUserActivityRequestManager, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserActivities.UserActivityRequestManager, Windows.ApplicationModel.UserActivities.UserActivityRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserActivityRequested(self: Windows.ApplicationModel.UserActivities.IUserActivityRequestManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.ApplicationModel.UserActivities.IUserActivityRequestManagerStatics) -> Windows.ApplicationModel.UserActivities.UserActivityRequestManager: ...
class UserActivityRequestedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserActivities.UserActivityRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.UserActivities.IUserActivityRequestedEventArgs) -> Windows.ApplicationModel.UserActivities.UserActivityRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.UserActivities.IUserActivityRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class UserActivitySession(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserActivities.UserActivitySession'
    @winrt_mixinmethod
    def get_ActivityId(self: Windows.ApplicationModel.UserActivities.IUserActivitySession) -> WinRT_String: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    ActivityId = property(get_ActivityId, None)
class UserActivitySessionHistoryItem(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserActivities.UserActivitySessionHistoryItem'
    @winrt_mixinmethod
    def get_UserActivity(self: Windows.ApplicationModel.UserActivities.IUserActivitySessionHistoryItem) -> Windows.ApplicationModel.UserActivities.UserActivity: ...
    @winrt_mixinmethod
    def get_StartTime(self: Windows.ApplicationModel.UserActivities.IUserActivitySessionHistoryItem) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_EndTime(self: Windows.ApplicationModel.UserActivities.IUserActivitySessionHistoryItem) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    UserActivity = property(get_UserActivity, None)
    StartTime = property(get_StartTime, None)
    EndTime = property(get_EndTime, None)
UserActivityState = Int32
UserActivityState_New: UserActivityState = 0
UserActivityState_Published: UserActivityState = 1
class UserActivityVisualElements(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.UserActivities.UserActivityVisualElements'
    @winrt_mixinmethod
    def get_DisplayText(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayText(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Attribution(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements) -> Windows.ApplicationModel.UserActivities.UserActivityAttribution: ...
    @winrt_mixinmethod
    def put_Attribution(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements, value: Windows.ApplicationModel.UserActivities.UserActivityAttribution) -> Void: ...
    @winrt_mixinmethod
    def put_Content(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements, value: Windows.UI.Shell.IAdaptiveCard) -> Void: ...
    @winrt_mixinmethod
    def get_Content(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements) -> Windows.UI.Shell.IAdaptiveCard: ...
    @winrt_mixinmethod
    def get_AttributionDisplayText(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AttributionDisplayText(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements2, value: WinRT_String) -> Void: ...
    DisplayText = property(get_DisplayText, put_DisplayText)
    Description = property(get_Description, put_Description)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    Attribution = property(get_Attribution, put_Attribution)
    Content = property(get_Content, put_Content)
    AttributionDisplayText = property(get_AttributionDisplayText, put_AttributionDisplayText)
make_head(_module, 'IUserActivity')
make_head(_module, 'IUserActivity2')
make_head(_module, 'IUserActivity3')
make_head(_module, 'IUserActivityAttribution')
make_head(_module, 'IUserActivityAttributionFactory')
make_head(_module, 'IUserActivityChannel')
make_head(_module, 'IUserActivityChannel2')
make_head(_module, 'IUserActivityChannelStatics')
make_head(_module, 'IUserActivityChannelStatics2')
make_head(_module, 'IUserActivityChannelStatics3')
make_head(_module, 'IUserActivityContentInfo')
make_head(_module, 'IUserActivityContentInfoStatics')
make_head(_module, 'IUserActivityFactory')
make_head(_module, 'IUserActivityRequest')
make_head(_module, 'IUserActivityRequestManager')
make_head(_module, 'IUserActivityRequestManagerStatics')
make_head(_module, 'IUserActivityRequestedEventArgs')
make_head(_module, 'IUserActivitySession')
make_head(_module, 'IUserActivitySessionHistoryItem')
make_head(_module, 'IUserActivityStatics')
make_head(_module, 'IUserActivityVisualElements')
make_head(_module, 'IUserActivityVisualElements2')
make_head(_module, 'UserActivity')
make_head(_module, 'UserActivityAttribution')
make_head(_module, 'UserActivityChannel')
make_head(_module, 'UserActivityContentInfo')
make_head(_module, 'UserActivityRequest')
make_head(_module, 'UserActivityRequestManager')
make_head(_module, 'UserActivityRequestedEventArgs')
make_head(_module, 'UserActivitySession')
make_head(_module, 'UserActivitySessionHistoryItem')
make_head(_module, 'UserActivityVisualElements')
