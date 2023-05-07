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
class IUserActivity(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivity'
    _iid_ = Guid('{fc103e9e-2cab-4d36-aea2-b4bb556cef0f}')
    @winrt_commethod(6)
    def get_State(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> Windows.ApplicationModel.UserActivities.UserActivityState: ...
    @winrt_commethod(7)
    def get_ActivityId(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_VisualElements(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> Windows.ApplicationModel.UserActivities.UserActivityVisualElements: ...
    @winrt_commethod(9)
    def get_ContentUri(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> Windows.Foundation.Uri: ...
    @winrt_commethod(10)
    def put_ContentUri(self: Windows.ApplicationModel.UserActivities.IUserActivity, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(11)
    def get_ContentType(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_ContentType(self: Windows.ApplicationModel.UserActivities.IUserActivity, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_FallbackUri(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> Windows.Foundation.Uri: ...
    @winrt_commethod(14)
    def put_FallbackUri(self: Windows.ApplicationModel.UserActivities.IUserActivity, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(15)
    def get_ActivationUri(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> Windows.Foundation.Uri: ...
    @winrt_commethod(16)
    def put_ActivationUri(self: Windows.ApplicationModel.UserActivities.IUserActivity, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(17)
    def get_ContentInfo(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> Windows.ApplicationModel.UserActivities.IUserActivityContentInfo: ...
    @winrt_commethod(18)
    def put_ContentInfo(self: Windows.ApplicationModel.UserActivities.IUserActivity, value: Windows.ApplicationModel.UserActivities.IUserActivityContentInfo) -> Void: ...
    @winrt_commethod(19)
    def SaveAsync(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(20)
    def CreateSession(self: Windows.ApplicationModel.UserActivities.IUserActivity) -> Windows.ApplicationModel.UserActivities.UserActivitySession: ...
    State = property(get_State, None)
    ActivityId = property(get_ActivityId, None)
    VisualElements = property(get_VisualElements, None)
    ContentUri = property(get_ContentUri, put_ContentUri)
    ContentType = property(get_ContentType, put_ContentType)
    FallbackUri = property(get_FallbackUri, put_FallbackUri)
    ActivationUri = property(get_ActivationUri, put_ActivationUri)
    ContentInfo = property(get_ContentInfo, put_ContentInfo)
class IUserActivity2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivity2'
    _iid_ = Guid('{9dc40c62-08c4-47ac-aa9c-2bb2221c55fd}')
    @winrt_commethod(6)
    def ToJson(self: Windows.ApplicationModel.UserActivities.IUserActivity2) -> WinRT_String: ...
class IUserActivity3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivity3'
    _iid_ = Guid('{e7697744-e1a2-5147-8e06-55f1eeef271c}')
    @winrt_commethod(6)
    def get_IsRoamable(self: Windows.ApplicationModel.UserActivities.IUserActivity3) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsRoamable(self: Windows.ApplicationModel.UserActivities.IUserActivity3, value: Boolean) -> Void: ...
    IsRoamable = property(get_IsRoamable, put_IsRoamable)
class IUserActivityAttribution(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityAttribution'
    _iid_ = Guid('{34a5c8b5-86dd-4aec-a491-6a4faea5d22e}')
    @winrt_commethod(6)
    def get_IconUri(self: Windows.ApplicationModel.UserActivities.IUserActivityAttribution) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_IconUri(self: Windows.ApplicationModel.UserActivities.IUserActivityAttribution, value: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_AlternateText(self: Windows.ApplicationModel.UserActivities.IUserActivityAttribution) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_AlternateText(self: Windows.ApplicationModel.UserActivities.IUserActivityAttribution, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_AddImageQuery(self: Windows.ApplicationModel.UserActivities.IUserActivityAttribution) -> Boolean: ...
    @winrt_commethod(11)
    def put_AddImageQuery(self: Windows.ApplicationModel.UserActivities.IUserActivityAttribution, value: Boolean) -> Void: ...
    IconUri = property(get_IconUri, put_IconUri)
    AlternateText = property(get_AlternateText, put_AlternateText)
    AddImageQuery = property(get_AddImageQuery, put_AddImageQuery)
class IUserActivityAttributionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityAttributionFactory'
    _iid_ = Guid('{e62bd252-c566-4f42-9974-916c4d76377e}')
    @winrt_commethod(6)
    def CreateWithUri(self: Windows.ApplicationModel.UserActivities.IUserActivityAttributionFactory, iconUri: Windows.Foundation.Uri) -> Windows.ApplicationModel.UserActivities.UserActivityAttribution: ...
class IUserActivityChannel(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityChannel'
    _iid_ = Guid('{bac0f8b8-a0e4-483b-b948-9cbabd06070c}')
    @winrt_commethod(6)
    def GetOrCreateUserActivityAsync(self: Windows.ApplicationModel.UserActivities.IUserActivityChannel, activityId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.UserActivities.UserActivity]: ...
    @winrt_commethod(7)
    def DeleteActivityAsync(self: Windows.ApplicationModel.UserActivities.IUserActivityChannel, activityId: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def DeleteAllActivitiesAsync(self: Windows.ApplicationModel.UserActivities.IUserActivityChannel) -> Windows.Foundation.IAsyncAction: ...
class IUserActivityChannel2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityChannel2'
    _iid_ = Guid('{1698e35b-eb7e-4ea0-bf17-a459e8be706c}')
    @winrt_commethod(6)
    def GetRecentUserActivitiesAsync(self: Windows.ApplicationModel.UserActivities.IUserActivityChannel2, maxUniqueActivities: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.ApplicationModel.UserActivities.UserActivitySessionHistoryItem]]: ...
    @winrt_commethod(7)
    def GetSessionHistoryItemsForUserActivityAsync(self: Windows.ApplicationModel.UserActivities.IUserActivityChannel2, activityId: WinRT_String, startTime: Windows.Foundation.DateTime) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVector[Windows.ApplicationModel.UserActivities.UserActivitySessionHistoryItem]]: ...
class IUserActivityChannelStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityChannelStatics'
    _iid_ = Guid('{c8c005ab-198d-4d80-abb2-c9775ec4a729}')
    @winrt_commethod(6)
    def GetDefault(self: Windows.ApplicationModel.UserActivities.IUserActivityChannelStatics) -> Windows.ApplicationModel.UserActivities.UserActivityChannel: ...
class IUserActivityChannelStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityChannelStatics2'
    _iid_ = Guid('{8e87de30-aa4f-4624-9ad0-d40f3ba0317c}')
    @winrt_commethod(6)
    def DisableAutoSessionCreation(self: Windows.ApplicationModel.UserActivities.IUserActivityChannelStatics2) -> Void: ...
    @winrt_commethod(7)
    def TryGetForWebAccount(self: Windows.ApplicationModel.UserActivities.IUserActivityChannelStatics2, account: Windows.Security.Credentials.WebAccount) -> Windows.ApplicationModel.UserActivities.UserActivityChannel: ...
class IUserActivityChannelStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityChannelStatics3'
    _iid_ = Guid('{53bc4ddb-bbdf-5984-802a-5305874e205c}')
    @winrt_commethod(6)
    def GetForUser(self: Windows.ApplicationModel.UserActivities.IUserActivityChannelStatics3, user: Windows.System.User) -> Windows.ApplicationModel.UserActivities.UserActivityChannel: ...
class IUserActivityContentInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityContentInfo'
    _iid_ = Guid('{b399e5ad-137f-409d-822d-e1af27ce08dc}')
    @winrt_commethod(6)
    def ToJson(self: Windows.ApplicationModel.UserActivities.IUserActivityContentInfo) -> WinRT_String: ...
class IUserActivityContentInfoStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityContentInfoStatics'
    _iid_ = Guid('{9988c34b-0386-4bc9-968a-8200b004144f}')
    @winrt_commethod(6)
    def FromJson(self: Windows.ApplicationModel.UserActivities.IUserActivityContentInfoStatics, value: WinRT_String) -> Windows.ApplicationModel.UserActivities.UserActivityContentInfo: ...
class IUserActivityFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityFactory'
    _iid_ = Guid('{7c385758-361d-4a67-8a3b-34ca2978f9a3}')
    @winrt_commethod(6)
    def CreateWithActivityId(self: Windows.ApplicationModel.UserActivities.IUserActivityFactory, activityId: WinRT_String) -> Windows.ApplicationModel.UserActivities.UserActivity: ...
class IUserActivityRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityRequest'
    _iid_ = Guid('{a0ef6355-cf35-4ff0-8833-50cb4b72e06d}')
    @winrt_commethod(6)
    def SetUserActivity(self: Windows.ApplicationModel.UserActivities.IUserActivityRequest, activity: Windows.ApplicationModel.UserActivities.UserActivity) -> Void: ...
class IUserActivityRequestManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityRequestManager'
    _iid_ = Guid('{0c30be4e-903d-48d6-82d4-4043ed57791b}')
    @winrt_commethod(6)
    def add_UserActivityRequested(self: Windows.ApplicationModel.UserActivities.IUserActivityRequestManager, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserActivities.UserActivityRequestManager, Windows.ApplicationModel.UserActivities.UserActivityRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_UserActivityRequested(self: Windows.ApplicationModel.UserActivities.IUserActivityRequestManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IUserActivityRequestManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityRequestManagerStatics'
    _iid_ = Guid('{c0392df1-224a-432c-81e5-0c76b4c4cefa}')
    @winrt_commethod(6)
    def GetForCurrentView(self: Windows.ApplicationModel.UserActivities.IUserActivityRequestManagerStatics) -> Windows.ApplicationModel.UserActivities.UserActivityRequestManager: ...
class IUserActivityRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityRequestedEventArgs'
    _iid_ = Guid('{a4cc7a4c-8229-4cfd-a3bc-c61d318575a4}')
    @winrt_commethod(6)
    def get_Request(self: Windows.ApplicationModel.UserActivities.IUserActivityRequestedEventArgs) -> Windows.ApplicationModel.UserActivities.UserActivityRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self: Windows.ApplicationModel.UserActivities.IUserActivityRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IUserActivitySession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivitySession'
    _iid_ = Guid('{ae434d78-24fa-44a3-ad48-6eda61aa1924}')
    @winrt_commethod(6)
    def get_ActivityId(self: Windows.ApplicationModel.UserActivities.IUserActivitySession) -> WinRT_String: ...
    ActivityId = property(get_ActivityId, None)
class IUserActivitySessionHistoryItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivitySessionHistoryItem'
    _iid_ = Guid('{e8d59bd3-3e5d-49fd-98d7-6da97521e255}')
    @winrt_commethod(6)
    def get_UserActivity(self: Windows.ApplicationModel.UserActivities.IUserActivitySessionHistoryItem) -> Windows.ApplicationModel.UserActivities.UserActivity: ...
    @winrt_commethod(7)
    def get_StartTime(self: Windows.ApplicationModel.UserActivities.IUserActivitySessionHistoryItem) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_EndTime(self: Windows.ApplicationModel.UserActivities.IUserActivitySessionHistoryItem) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    UserActivity = property(get_UserActivity, None)
    StartTime = property(get_StartTime, None)
    EndTime = property(get_EndTime, None)
class IUserActivityStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityStatics'
    _iid_ = Guid('{8c8fd333-0e09-47f6-9ac7-95cf5c39367b}')
    @winrt_commethod(6)
    def TryParseFromJson(self: Windows.ApplicationModel.UserActivities.IUserActivityStatics, json: WinRT_String) -> Windows.ApplicationModel.UserActivities.UserActivity: ...
    @winrt_commethod(7)
    def TryParseFromJsonArray(self: Windows.ApplicationModel.UserActivities.IUserActivityStatics, json: WinRT_String) -> Windows.Foundation.Collections.IVector[Windows.ApplicationModel.UserActivities.UserActivity]: ...
    @winrt_commethod(8)
    def ToJsonArray(self: Windows.ApplicationModel.UserActivities.IUserActivityStatics, activities: Windows.Foundation.Collections.IIterable[Windows.ApplicationModel.UserActivities.UserActivity]) -> WinRT_String: ...
class IUserActivityVisualElements(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityVisualElements'
    _iid_ = Guid('{94757513-262f-49ef-bbbf-9b75d2e85250}')
    @winrt_commethod(6)
    def get_DisplayText(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DisplayText(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Description(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Description(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_BackgroundColor(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements) -> Windows.UI.Color: ...
    @winrt_commethod(11)
    def put_BackgroundColor(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(12)
    def get_Attribution(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements) -> Windows.ApplicationModel.UserActivities.UserActivityAttribution: ...
    @winrt_commethod(13)
    def put_Attribution(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements, value: Windows.ApplicationModel.UserActivities.UserActivityAttribution) -> Void: ...
    @winrt_commethod(14)
    def put_Content(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements, value: Windows.UI.Shell.IAdaptiveCard) -> Void: ...
    @winrt_commethod(15)
    def get_Content(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements) -> Windows.UI.Shell.IAdaptiveCard: ...
    DisplayText = property(get_DisplayText, put_DisplayText)
    Description = property(get_Description, put_Description)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    Attribution = property(get_Attribution, put_Attribution)
    Content = property(get_Content, put_Content)
class IUserActivityVisualElements2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityVisualElements2'
    _iid_ = Guid('{caae7fc7-3eef-4359-825c-9d51b9220de3}')
    @winrt_commethod(6)
    def get_AttributionDisplayText(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements2) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_AttributionDisplayText(self: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements2, value: WinRT_String) -> Void: ...
    AttributionDisplayText = property(get_AttributionDisplayText, put_AttributionDisplayText)
class UserActivity(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserActivities.IUserActivity
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivity'
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
class UserActivityAttribution(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserActivities.IUserActivityAttribution
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivityAttribution'
    @winrt_factorymethod
    def CreateWithUri(cls: Windows.ApplicationModel.UserActivities.IUserActivityAttributionFactory, iconUri: Windows.Foundation.Uri) -> Windows.ApplicationModel.UserActivities.UserActivityAttribution: ...
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.ApplicationModel.UserActivities.UserActivityAttribution: ...
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
class UserActivityChannel(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserActivities.IUserActivityChannel
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivityChannel'
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
class UserActivityContentInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserActivities.IUserActivityContentInfo
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivityContentInfo'
    @winrt_mixinmethod
    def ToJson(self: Windows.ApplicationModel.UserActivities.IUserActivityContentInfo) -> WinRT_String: ...
    @winrt_classmethod
    def FromJson(cls: Windows.ApplicationModel.UserActivities.IUserActivityContentInfoStatics, value: WinRT_String) -> Windows.ApplicationModel.UserActivities.UserActivityContentInfo: ...
class UserActivityRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserActivities.IUserActivityRequest
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivityRequest'
    @winrt_mixinmethod
    def SetUserActivity(self: Windows.ApplicationModel.UserActivities.IUserActivityRequest, activity: Windows.ApplicationModel.UserActivities.UserActivity) -> Void: ...
class UserActivityRequestManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserActivities.IUserActivityRequestManager
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivityRequestManager'
    @winrt_mixinmethod
    def add_UserActivityRequested(self: Windows.ApplicationModel.UserActivities.IUserActivityRequestManager, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.UserActivities.UserActivityRequestManager, Windows.ApplicationModel.UserActivities.UserActivityRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserActivityRequested(self: Windows.ApplicationModel.UserActivities.IUserActivityRequestManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.ApplicationModel.UserActivities.IUserActivityRequestManagerStatics) -> Windows.ApplicationModel.UserActivities.UserActivityRequestManager: ...
class UserActivityRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserActivities.IUserActivityRequestedEventArgs
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivityRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.ApplicationModel.UserActivities.IUserActivityRequestedEventArgs) -> Windows.ApplicationModel.UserActivities.UserActivityRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.UserActivities.IUserActivityRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class UserActivitySession(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserActivities.IUserActivitySession
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivitySession'
    @winrt_mixinmethod
    def get_ActivityId(self: Windows.ApplicationModel.UserActivities.IUserActivitySession) -> WinRT_String: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    ActivityId = property(get_ActivityId, None)
class UserActivitySessionHistoryItem(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserActivities.IUserActivitySessionHistoryItem
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivitySessionHistoryItem'
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
class UserActivityVisualElements(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.UserActivities.IUserActivityVisualElements
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivityVisualElements'
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
