from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.UserActivities
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Credentials
import win32more.Windows.System
import win32more.Windows.UI
import win32more.Windows.UI.Shell
import win32more.Windows.Win32.System.WinRT
class IUserActivity(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivity'
    _iid_ = Guid('{fc103e9e-2cab-4d36-aea2-b4bb556cef0f}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityState: ...
    @winrt_commethod(7)
    def get_ActivityId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_VisualElements(self) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityVisualElements: ...
    @winrt_commethod(9)
    def get_ContentUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(10)
    def put_ContentUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(11)
    def get_ContentType(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_ContentType(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_FallbackUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(14)
    def put_FallbackUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(15)
    def get_ActivationUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(16)
    def put_ActivationUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(17)
    def get_ContentInfo(self) -> win32more.Windows.ApplicationModel.UserActivities.IUserActivityContentInfo: ...
    @winrt_commethod(18)
    def put_ContentInfo(self, value: win32more.Windows.ApplicationModel.UserActivities.IUserActivityContentInfo) -> Void: ...
    @winrt_commethod(19)
    def SaveAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(20)
    def CreateSession(self) -> win32more.Windows.ApplicationModel.UserActivities.UserActivitySession: ...
    ActivationUri = property(get_ActivationUri, put_ActivationUri)
    ActivityId = property(get_ActivityId, None)
    ContentInfo = property(get_ContentInfo, put_ContentInfo)
    ContentType = property(get_ContentType, put_ContentType)
    ContentUri = property(get_ContentUri, put_ContentUri)
    FallbackUri = property(get_FallbackUri, put_FallbackUri)
    State = property(get_State, None)
    VisualElements = property(get_VisualElements, None)
class IUserActivity2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivity2'
    _iid_ = Guid('{9dc40c62-08c4-47ac-aa9c-2bb2221c55fd}')
    @winrt_commethod(6)
    def ToJson(self) -> WinRT_String: ...
class IUserActivity3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivity3'
    _iid_ = Guid('{e7697744-e1a2-5147-8e06-55f1eeef271c}')
    @winrt_commethod(6)
    def get_IsRoamable(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsRoamable(self, value: Boolean) -> Void: ...
    IsRoamable = property(get_IsRoamable, put_IsRoamable)
class IUserActivityAttribution(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityAttribution'
    _iid_ = Guid('{34a5c8b5-86dd-4aec-a491-6a4faea5d22e}')
    @winrt_commethod(6)
    def get_IconUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_IconUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_AlternateText(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_AlternateText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_AddImageQuery(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_AddImageQuery(self, value: Boolean) -> Void: ...
    AddImageQuery = property(get_AddImageQuery, put_AddImageQuery)
    AlternateText = property(get_AlternateText, put_AlternateText)
    IconUri = property(get_IconUri, put_IconUri)
class IUserActivityAttributionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityAttributionFactory'
    _iid_ = Guid('{e62bd252-c566-4f42-9974-916c4d76377e}')
    @winrt_commethod(6)
    def CreateWithUri(self, iconUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityAttribution: ...
class IUserActivityChannel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityChannel'
    _iid_ = Guid('{bac0f8b8-a0e4-483b-b948-9cbabd06070c}')
    @winrt_commethod(6)
    def GetOrCreateUserActivityAsync(self, activityId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserActivities.UserActivity]: ...
    @winrt_commethod(7)
    def DeleteActivityAsync(self, activityId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def DeleteAllActivitiesAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class IUserActivityChannel2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityChannel2'
    _iid_ = Guid('{1698e35b-eb7e-4ea0-bf17-a459e8be706c}')
    @winrt_commethod(6)
    def GetRecentUserActivitiesAsync(self, maxUniqueActivities: Int32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.UserActivities.UserActivitySessionHistoryItem]]: ...
    @winrt_commethod(7)
    def GetSessionHistoryItemsForUserActivityAsync(self, activityId: WinRT_String, startTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.UserActivities.UserActivitySessionHistoryItem]]: ...
class IUserActivityChannelStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityChannelStatics'
    _iid_ = Guid('{c8c005ab-198d-4d80-abb2-c9775ec4a729}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityChannel: ...
class IUserActivityChannelStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityChannelStatics2'
    _iid_ = Guid('{8e87de30-aa4f-4624-9ad0-d40f3ba0317c}')
    @winrt_commethod(6)
    def DisableAutoSessionCreation(self) -> Void: ...
    @winrt_commethod(7)
    def TryGetForWebAccount(self, account: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityChannel: ...
class IUserActivityChannelStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityChannelStatics3'
    _iid_ = Guid('{53bc4ddb-bbdf-5984-802a-5305874e205c}')
    @winrt_commethod(6)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityChannel: ...
class IUserActivityContentInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityContentInfo'
    _iid_ = Guid('{b399e5ad-137f-409d-822d-e1af27ce08dc}')
    @winrt_commethod(6)
    def ToJson(self) -> WinRT_String: ...
class IUserActivityContentInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityContentInfoStatics'
    _iid_ = Guid('{9988c34b-0386-4bc9-968a-8200b004144f}')
    @winrt_commethod(6)
    def FromJson(self, value: WinRT_String) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityContentInfo: ...
class IUserActivityFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityFactory'
    _iid_ = Guid('{7c385758-361d-4a67-8a3b-34ca2978f9a3}')
    @winrt_commethod(6)
    def CreateWithActivityId(self, activityId: WinRT_String) -> win32more.Windows.ApplicationModel.UserActivities.UserActivity: ...
class IUserActivityRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityRequest'
    _iid_ = Guid('{a0ef6355-cf35-4ff0-8833-50cb4b72e06d}')
    @winrt_commethod(6)
    def SetUserActivity(self, activity: win32more.Windows.ApplicationModel.UserActivities.UserActivity) -> Void: ...
class IUserActivityRequestManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityRequestManager'
    _iid_ = Guid('{0c30be4e-903d-48d6-82d4-4043ed57791b}')
    @winrt_commethod(6)
    def add_UserActivityRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.UserActivities.UserActivityRequestManager, win32more.Windows.ApplicationModel.UserActivities.UserActivityRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_UserActivityRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    UserActivityRequested = event()
class IUserActivityRequestManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityRequestManagerStatics'
    _iid_ = Guid('{c0392df1-224a-432c-81e5-0c76b4c4cefa}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityRequestManager: ...
class IUserActivityRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityRequestedEventArgs'
    _iid_ = Guid('{a4cc7a4c-8229-4cfd-a3bc-c61d318575a4}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IUserActivitySession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivitySession'
    _iid_ = Guid('{ae434d78-24fa-44a3-ad48-6eda61aa1924}')
    @winrt_commethod(6)
    def get_ActivityId(self) -> WinRT_String: ...
    ActivityId = property(get_ActivityId, None)
class IUserActivitySessionHistoryItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivitySessionHistoryItem'
    _iid_ = Guid('{e8d59bd3-3e5d-49fd-98d7-6da97521e255}')
    @winrt_commethod(6)
    def get_UserActivity(self) -> win32more.Windows.ApplicationModel.UserActivities.UserActivity: ...
    @winrt_commethod(7)
    def get_StartTime(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_EndTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    EndTime = property(get_EndTime, None)
    StartTime = property(get_StartTime, None)
    UserActivity = property(get_UserActivity, None)
class IUserActivityStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityStatics'
    _iid_ = Guid('{8c8fd333-0e09-47f6-9ac7-95cf5c39367b}')
    @winrt_commethod(6)
    def TryParseFromJson(self, json: WinRT_String) -> win32more.Windows.ApplicationModel.UserActivities.UserActivity: ...
    @winrt_commethod(7)
    def TryParseFromJsonArray(self, json: WinRT_String) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.UserActivities.UserActivity]: ...
    @winrt_commethod(8)
    def ToJsonArray(self, activities: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.UserActivities.UserActivity]) -> WinRT_String: ...
class IUserActivityVisualElements(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityVisualElements'
    _iid_ = Guid('{94757513-262f-49ef-bbbf-9b75d2e85250}')
    @winrt_commethod(6)
    def get_DisplayText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_DisplayText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Description(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_BackgroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(11)
    def put_BackgroundColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(12)
    def get_Attribution(self) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityAttribution: ...
    @winrt_commethod(13)
    def put_Attribution(self, value: win32more.Windows.ApplicationModel.UserActivities.UserActivityAttribution) -> Void: ...
    @winrt_commethod(14)
    def put_Content(self, value: win32more.Windows.UI.Shell.IAdaptiveCard) -> Void: ...
    @winrt_commethod(15)
    def get_Content(self) -> win32more.Windows.UI.Shell.IAdaptiveCard: ...
    Attribution = property(get_Attribution, put_Attribution)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    Content = property(get_Content, put_Content)
    Description = property(get_Description, put_Description)
    DisplayText = property(get_DisplayText, put_DisplayText)
class IUserActivityVisualElements2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.UserActivities.IUserActivityVisualElements2'
    _iid_ = Guid('{caae7fc7-3eef-4359-825c-9d51b9220de3}')
    @winrt_commethod(6)
    def get_AttributionDisplayText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_AttributionDisplayText(self, value: WinRT_String) -> Void: ...
    AttributionDisplayText = property(get_AttributionDisplayText, put_AttributionDisplayText)
class UserActivity(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserActivities.IUserActivity
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivity'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.UserActivities.UserActivity.CreateWithActivityId(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateWithActivityId(cls: win32more.Windows.ApplicationModel.UserActivities.IUserActivityFactory, activityId: WinRT_String) -> win32more.Windows.ApplicationModel.UserActivities.UserActivity: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivity) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityState: ...
    @winrt_mixinmethod
    def get_ActivityId(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivity) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_VisualElements(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivity) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityVisualElements: ...
    @winrt_mixinmethod
    def get_ContentUri(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivity) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_ContentUri(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivity, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ContentType(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivity) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ContentType(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivity, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FallbackUri(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivity) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_FallbackUri(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivity, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ActivationUri(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivity) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_ActivationUri(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivity, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_ContentInfo(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivity) -> win32more.Windows.ApplicationModel.UserActivities.IUserActivityContentInfo: ...
    @winrt_mixinmethod
    def put_ContentInfo(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivity, value: win32more.Windows.ApplicationModel.UserActivities.IUserActivityContentInfo) -> Void: ...
    @winrt_mixinmethod
    def SaveAsync(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivity) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CreateSession(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivity) -> win32more.Windows.ApplicationModel.UserActivities.UserActivitySession: ...
    @winrt_mixinmethod
    def ToJson(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivity2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsRoamable(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivity3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsRoamable(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivity3, value: Boolean) -> Void: ...
    @winrt_classmethod
    def TryParseFromJson(cls: win32more.Windows.ApplicationModel.UserActivities.IUserActivityStatics, json: WinRT_String) -> win32more.Windows.ApplicationModel.UserActivities.UserActivity: ...
    @winrt_classmethod
    def TryParseFromJsonArray(cls: win32more.Windows.ApplicationModel.UserActivities.IUserActivityStatics, json: WinRT_String) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.UserActivities.UserActivity]: ...
    @winrt_classmethod
    def ToJsonArray(cls: win32more.Windows.ApplicationModel.UserActivities.IUserActivityStatics, activities: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.ApplicationModel.UserActivities.UserActivity]) -> WinRT_String: ...
    ActivationUri = property(get_ActivationUri, put_ActivationUri)
    ActivityId = property(get_ActivityId, None)
    ContentInfo = property(get_ContentInfo, put_ContentInfo)
    ContentType = property(get_ContentType, put_ContentType)
    ContentUri = property(get_ContentUri, put_ContentUri)
    FallbackUri = property(get_FallbackUri, put_FallbackUri)
    IsRoamable = property(get_IsRoamable, put_IsRoamable)
    State = property(get_State, None)
    VisualElements = property(get_VisualElements, None)
class UserActivityAttribution(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserActivities.IUserActivityAttribution
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivityAttribution'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.UserActivities.UserActivityAttribution.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.UserActivities.UserActivityAttribution.CreateWithUri(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityAttribution: ...
    @winrt_factorymethod
    def CreateWithUri(cls: win32more.Windows.ApplicationModel.UserActivities.IUserActivityAttributionFactory, iconUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityAttribution: ...
    @winrt_mixinmethod
    def get_IconUri(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityAttribution) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_IconUri(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityAttribution, value: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_AlternateText(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityAttribution) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AlternateText(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityAttribution, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AddImageQuery(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityAttribution) -> Boolean: ...
    @winrt_mixinmethod
    def put_AddImageQuery(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityAttribution, value: Boolean) -> Void: ...
    AddImageQuery = property(get_AddImageQuery, put_AddImageQuery)
    AlternateText = property(get_AlternateText, put_AlternateText)
    IconUri = property(get_IconUri, put_IconUri)
class UserActivityChannel(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserActivities.IUserActivityChannel
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivityChannel'
    @winrt_mixinmethod
    def GetOrCreateUserActivityAsync(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityChannel, activityId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.UserActivities.UserActivity]: ...
    @winrt_mixinmethod
    def DeleteActivityAsync(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityChannel, activityId: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeleteAllActivitiesAsync(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityChannel) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetRecentUserActivitiesAsync(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityChannel2, maxUniqueActivities: Int32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.UserActivities.UserActivitySessionHistoryItem]]: ...
    @winrt_mixinmethod
    def GetSessionHistoryItemsForUserActivityAsync(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityChannel2, activityId: WinRT_String, startTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.UserActivities.UserActivitySessionHistoryItem]]: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.ApplicationModel.UserActivities.IUserActivityChannelStatics3, user: win32more.Windows.System.User) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityChannel: ...
    @winrt_classmethod
    def DisableAutoSessionCreation(cls: win32more.Windows.ApplicationModel.UserActivities.IUserActivityChannelStatics2) -> Void: ...
    @winrt_classmethod
    def TryGetForWebAccount(cls: win32more.Windows.ApplicationModel.UserActivities.IUserActivityChannelStatics2, account: win32more.Windows.Security.Credentials.WebAccount) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityChannel: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.ApplicationModel.UserActivities.IUserActivityChannelStatics) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityChannel: ...
class UserActivityContentInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserActivities.IUserActivityContentInfo
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivityContentInfo'
    @winrt_mixinmethod
    def ToJson(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityContentInfo) -> WinRT_String: ...
    @winrt_classmethod
    def FromJson(cls: win32more.Windows.ApplicationModel.UserActivities.IUserActivityContentInfoStatics, value: WinRT_String) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityContentInfo: ...
class UserActivityRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserActivities.IUserActivityRequest
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivityRequest'
    @winrt_mixinmethod
    def SetUserActivity(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityRequest, activity: win32more.Windows.ApplicationModel.UserActivities.UserActivity) -> Void: ...
class UserActivityRequestManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserActivities.IUserActivityRequestManager
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivityRequestManager'
    @winrt_mixinmethod
    def add_UserActivityRequested(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityRequestManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.UserActivities.UserActivityRequestManager, win32more.Windows.ApplicationModel.UserActivities.UserActivityRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserActivityRequested(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityRequestManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.ApplicationModel.UserActivities.IUserActivityRequestManagerStatics) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityRequestManager: ...
    UserActivityRequested = event()
class UserActivityRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserActivities.IUserActivityRequestedEventArgs
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivityRequestedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityRequestedEventArgs) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class UserActivitySession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.ApplicationModel.UserActivities.IUserActivitySession
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivitySession'
    @winrt_mixinmethod
    def get_ActivityId(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivitySession) -> WinRT_String: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    ActivityId = property(get_ActivityId, None)
class UserActivitySessionHistoryItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserActivities.IUserActivitySessionHistoryItem
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivitySessionHistoryItem'
    @winrt_mixinmethod
    def get_UserActivity(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivitySessionHistoryItem) -> win32more.Windows.ApplicationModel.UserActivities.UserActivity: ...
    @winrt_mixinmethod
    def get_StartTime(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivitySessionHistoryItem) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_EndTime(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivitySessionHistoryItem) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    EndTime = property(get_EndTime, None)
    StartTime = property(get_StartTime, None)
    UserActivity = property(get_UserActivity, None)
class UserActivityState(Enum, Int32):
    New = 0
    Published = 1
class UserActivityVisualElements(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.UserActivities.IUserActivityVisualElements
    _classid_ = 'Windows.ApplicationModel.UserActivities.UserActivityVisualElements'
    @winrt_mixinmethod
    def get_DisplayText(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityVisualElements) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayText(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityVisualElements, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityVisualElements) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Description(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityVisualElements, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityVisualElements) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityVisualElements, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Attribution(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityVisualElements) -> win32more.Windows.ApplicationModel.UserActivities.UserActivityAttribution: ...
    @winrt_mixinmethod
    def put_Attribution(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityVisualElements, value: win32more.Windows.ApplicationModel.UserActivities.UserActivityAttribution) -> Void: ...
    @winrt_mixinmethod
    def put_Content(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityVisualElements, value: win32more.Windows.UI.Shell.IAdaptiveCard) -> Void: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityVisualElements) -> win32more.Windows.UI.Shell.IAdaptiveCard: ...
    @winrt_mixinmethod
    def get_AttributionDisplayText(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityVisualElements2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AttributionDisplayText(self: win32more.Windows.ApplicationModel.UserActivities.IUserActivityVisualElements2, value: WinRT_String) -> Void: ...
    Attribution = property(get_Attribution, put_Attribution)
    AttributionDisplayText = property(get_AttributionDisplayText, put_AttributionDisplayText)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    Content = property(get_Content, put_Content)
    Description = property(get_Description, put_Description)
    DisplayText = property(get_DisplayText, put_DisplayText)


make_ready(__name__)
