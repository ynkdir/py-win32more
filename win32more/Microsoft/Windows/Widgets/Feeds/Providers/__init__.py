from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Windows.Widgets.Feeds.Providers
import win32more.Microsoft.Windows.Widgets.Notifications
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class CustomQueryParametersRequestedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.ICustomQueryParametersRequestedArgs
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.CustomQueryParametersRequestedArgs'
    @winrt_mixinmethod
    def get_FeedProviderDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.ICustomQueryParametersRequestedArgs) -> WinRT_String: ...
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class CustomQueryParametersUpdateOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.ICustomQueryParametersUpdateOptions
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.CustomQueryParametersUpdateOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.Windows.Widgets.Feeds.Providers.CustomQueryParametersUpdateOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.Widgets.Feeds.Providers.ICustomQueryParametersUpdateOptionsFactory, feedProviderDefinitionId: WinRT_String, customQueryParameters: WinRT_String) -> win32more.Microsoft.Windows.Widgets.Feeds.Providers.CustomQueryParametersUpdateOptions: ...
    @winrt_mixinmethod
    def get_FeedProviderDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.ICustomQueryParametersUpdateOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CustomQueryParameters(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.ICustomQueryParametersUpdateOptions) -> WinRT_String: ...
    CustomQueryParameters = property(get_CustomQueryParameters, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class FeedAnalyticsInfoReportedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedAnalyticsInfoReportedArgs
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.FeedAnalyticsInfoReportedArgs'
    @winrt_mixinmethod
    def get_FeedProviderDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedAnalyticsInfoReportedArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FeedDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedAnalyticsInfoReportedArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AnalyticsJson(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedAnalyticsInfoReportedArgs) -> WinRT_String: ...
    AnalyticsJson = property(get_AnalyticsJson, None)
    FeedDefinitionId = property(get_FeedDefinitionId, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class FeedDisabledArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedDisabledArgs
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.FeedDisabledArgs'
    @winrt_mixinmethod
    def get_FeedProviderDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedDisabledArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FeedDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedDisabledArgs) -> WinRT_String: ...
    FeedDefinitionId = property(get_FeedDefinitionId, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class FeedEnabledArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedEnabledArgs
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.FeedEnabledArgs'
    @winrt_mixinmethod
    def get_FeedProviderDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedEnabledArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FeedDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedEnabledArgs) -> WinRT_String: ...
    FeedDefinitionId = property(get_FeedDefinitionId, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class FeedErrorInfoReportedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedErrorInfoReportedArgs
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.FeedErrorInfoReportedArgs'
    @winrt_mixinmethod
    def get_FeedProviderDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedErrorInfoReportedArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FeedDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedErrorInfoReportedArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ErrorJson(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedErrorInfoReportedArgs) -> WinRT_String: ...
    ErrorJson = property(get_ErrorJson, None)
    FeedDefinitionId = property(get_FeedDefinitionId, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class FeedManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedManager
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.FeedManager'
    @winrt_mixinmethod
    def GetEnabledFeedProviders(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedManager) -> ReceiveArray[win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedProviderInfo]: ...
    @winrt_mixinmethod
    def SetCustomQueryParameters(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedManager, options: win32more.Microsoft.Windows.Widgets.Feeds.Providers.CustomQueryParametersUpdateOptions) -> Void: ...
    @winrt_mixinmethod
    def SendMessageToContent(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedManager2, feedProviderDefinitionId: WinRT_String, feedDefinitionId: WinRT_String, message: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def TryShowAnnouncement(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedManager2, feedProviderDefinitionId: WinRT_String, feedDefinitionId: WinRT_String, announcement: win32more.Microsoft.Windows.Widgets.Notifications.FeedAnnouncement) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedManagerStatics) -> win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedManager: ...
class FeedMessageReceivedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedMessageReceivedArgs
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.FeedMessageReceivedArgs'
    @winrt_mixinmethod
    def get_FeedProviderDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedMessageReceivedArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FeedDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedMessageReceivedArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedMessageReceivedArgs) -> WinRT_String: ...
    FeedDefinitionId = property(get_FeedDefinitionId, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
    Message = property(get_Message, None)
class FeedProviderDisabledArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderDisabledArgs
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.FeedProviderDisabledArgs'
    @winrt_mixinmethod
    def get_FeedProviderDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderDisabledArgs) -> WinRT_String: ...
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class FeedProviderEnabledArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderEnabledArgs
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.FeedProviderEnabledArgs'
    @winrt_mixinmethod
    def get_FeedProviderDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderEnabledArgs) -> WinRT_String: ...
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class FeedProviderInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderInfo
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.FeedProviderInfo'
    @winrt_mixinmethod
    def get_FeedProviderDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EnabledFeedDefinitionIds(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderInfo) -> ReceiveArray[WinRT_String]: ...
    EnabledFeedDefinitionIds = property(get_EnabledFeedDefinitionIds, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class FeedResourceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceRequest
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.FeedResourceRequest'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Method(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Method(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceRequest) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def put_Content(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceRequest, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_mixinmethod
    def get_Headers(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceRequest) -> win32more.Windows.Foundation.Collections.StringMap: ...
    @winrt_mixinmethod
    def put_Headers(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceRequest, value: win32more.Windows.Foundation.Collections.StringMap) -> Void: ...
    Content = property(get_Content, put_Content)
    Headers = property(get_Headers, put_Headers)
    Method = property(get_Method, put_Method)
    Uri = property(get_Uri, None)
class FeedResourceRequestedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceRequestedArgs
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.FeedResourceRequestedArgs'
    @winrt_mixinmethod
    def get_FeedProviderDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceRequestedArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FeedDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceRequestedArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Request(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceRequestedArgs) -> win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedResourceRequest: ...
    @winrt_mixinmethod
    def get_Response(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceRequestedArgs) -> win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedResourceResponse: ...
    @winrt_mixinmethod
    def put_Response(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceRequestedArgs, value: win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedResourceResponse) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceRequestedArgs) -> win32more.Windows.Foundation.Deferral: ...
    FeedDefinitionId = property(get_FeedDefinitionId, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
    Request = property(get_Request, None)
    Response = property(get_Response, put_Response)
class FeedResourceResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceResponse
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.FeedResourceResponse'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 3:
            super().__init__(move=win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedResourceResponse.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceResponseFactory, content: win32more.Windows.Storage.Streams.IRandomAccessStreamReference, reasonPhrase: WinRT_String, statusCode: Int32) -> win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedResourceResponse: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceResponse) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_mixinmethod
    def get_Headers(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceResponse) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]: ...
    @winrt_mixinmethod
    def put_Headers(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceResponse, value: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Void: ...
    @winrt_mixinmethod
    def get_ReasonPhrase(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_StatusCode(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceResponse) -> Int32: ...
    Content = property(get_Content, None)
    Headers = property(get_Headers, put_Headers)
    ReasonPhrase = property(get_ReasonPhrase, None)
    StatusCode = property(get_StatusCode, None)
class ICustomQueryParametersRequestedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.ICustomQueryParametersRequestedArgs'
    _iid_ = Guid('{dc2b0cd8-7936-5346-9371-b21484c7d859}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class ICustomQueryParametersUpdateOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.ICustomQueryParametersUpdateOptions'
    _iid_ = Guid('{753f1177-4909-568a-b070-98a3139205ec}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_CustomQueryParameters(self) -> WinRT_String: ...
    CustomQueryParameters = property(get_CustomQueryParameters, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class ICustomQueryParametersUpdateOptionsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.ICustomQueryParametersUpdateOptionsFactory'
    _iid_ = Guid('{34e318cd-3884-53c0-911c-225f32228fae}')
    @winrt_commethod(6)
    def CreateInstance(self, feedProviderDefinitionId: WinRT_String, customQueryParameters: WinRT_String) -> win32more.Microsoft.Windows.Widgets.Feeds.Providers.CustomQueryParametersUpdateOptions: ...
class IFeedAnalyticsInfoReportedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedAnalyticsInfoReportedArgs'
    _iid_ = Guid('{3c0e3d65-ed47-5b8a-b650-39a7edf18942}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FeedDefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_AnalyticsJson(self) -> WinRT_String: ...
    AnalyticsJson = property(get_AnalyticsJson, None)
    FeedDefinitionId = property(get_FeedDefinitionId, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class IFeedAnnouncementInvokedTarget(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedAnnouncementInvokedTarget'
    _iid_ = Guid('{5d44ae2a-072c-4df9-9fe5-34d5d2e9ff63}')
    @winrt_commethod(6)
    def OnAnnouncementInvoked(self, args: win32more.Microsoft.Windows.Widgets.Notifications.FeedAnnouncementInvokedArgs) -> Void: ...
class IFeedDisabledArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedDisabledArgs'
    _iid_ = Guid('{95300612-aca7-53c0-9cf6-d803689132c1}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FeedDefinitionId(self) -> WinRT_String: ...
    FeedDefinitionId = property(get_FeedDefinitionId, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class IFeedEnabledArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedEnabledArgs'
    _iid_ = Guid('{eff4b2d7-7347-5969-a77d-cac433f0fdae}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FeedDefinitionId(self) -> WinRT_String: ...
    FeedDefinitionId = property(get_FeedDefinitionId, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class IFeedErrorInfoReportedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedErrorInfoReportedArgs'
    _iid_ = Guid('{62de018c-161e-52d0-9dbe-aec106fb6600}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FeedDefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ErrorJson(self) -> WinRT_String: ...
    ErrorJson = property(get_ErrorJson, None)
    FeedDefinitionId = property(get_FeedDefinitionId, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class IFeedManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedManager'
    _iid_ = Guid('{87df6a84-15aa-45cb-8911-5cafab57f723}')
    @winrt_commethod(6)
    def GetEnabledFeedProviders(self) -> ReceiveArray[win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedProviderInfo]: ...
    @winrt_commethod(7)
    def SetCustomQueryParameters(self, options: win32more.Microsoft.Windows.Widgets.Feeds.Providers.CustomQueryParametersUpdateOptions) -> Void: ...
class IFeedManager2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedManager2'
    _iid_ = Guid('{5838300a-a069-455d-9943-ba078ada00d8}')
    @winrt_commethod(6)
    def SendMessageToContent(self, feedProviderDefinitionId: WinRT_String, feedDefinitionId: WinRT_String, message: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def TryShowAnnouncement(self, feedProviderDefinitionId: WinRT_String, feedDefinitionId: WinRT_String, announcement: win32more.Microsoft.Windows.Widgets.Notifications.FeedAnnouncement) -> Void: ...
class IFeedManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedManagerStatics'
    _iid_ = Guid('{4baf5174-77d6-5e2a-94ea-4f14ccdb1f2c}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedManager: ...
class IFeedMessageReceivedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedMessageReceivedArgs'
    _iid_ = Guid('{4ed6ecf9-4c74-5a0b-ae04-bef6dd776f8a}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FeedDefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Message(self) -> WinRT_String: ...
    FeedDefinitionId = property(get_FeedDefinitionId, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
    Message = property(get_Message, None)
class IFeedProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedProvider'
    _iid_ = Guid('{7293a12b-0329-458d-ac25-5332be478fde}')
    @winrt_commethod(6)
    def OnFeedProviderEnabled(self, args: win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedProviderEnabledArgs) -> Void: ...
    @winrt_commethod(7)
    def OnFeedProviderDisabled(self, args: win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedProviderDisabledArgs) -> Void: ...
    @winrt_commethod(8)
    def OnFeedEnabled(self, args: win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedEnabledArgs) -> Void: ...
    @winrt_commethod(9)
    def OnFeedDisabled(self, args: win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedDisabledArgs) -> Void: ...
    @winrt_commethod(10)
    def OnCustomQueryParametersRequested(self, args: win32more.Microsoft.Windows.Widgets.Feeds.Providers.CustomQueryParametersRequestedArgs) -> Void: ...
class IFeedProviderAnalytics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderAnalytics'
    _iid_ = Guid('{f6885791-3085-4bd7-9cb1-4f1354c3a687}')
    @winrt_commethod(6)
    def OnAnalyticsInfoReported(self, args: win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedAnalyticsInfoReportedArgs) -> Void: ...
class IFeedProviderDisabledArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderDisabledArgs'
    _iid_ = Guid('{19b65aec-e01d-5e8c-ab5f-324212e7cd30}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class IFeedProviderEnabledArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderEnabledArgs'
    _iid_ = Guid('{821fc9af-0de6-5a9b-9ae6-e179117b40e4}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class IFeedProviderErrors(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderErrors'
    _iid_ = Guid('{6611e00a-d86c-49a3-9381-b7da67ee62dc}')
    @winrt_commethod(6)
    def OnErrorInfoReported(self, args: win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedErrorInfoReportedArgs) -> Void: ...
class IFeedProviderInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderInfo'
    _iid_ = Guid('{73c37049-3c03-5896-8532-f9dfdaeb723f}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EnabledFeedDefinitionIds(self) -> ReceiveArray[WinRT_String]: ...
    EnabledFeedDefinitionIds = property(get_EnabledFeedDefinitionIds, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class IFeedProviderMessage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderMessage'
    _iid_ = Guid('{60c2442a-4c9d-4880-ba26-caca9e567dd4}')
    @winrt_commethod(6)
    def OnMessageReceived(self, args: win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedMessageReceivedArgs) -> Void: ...
class IFeedResourceProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceProvider'
    _iid_ = Guid('{e1b6266d-88a0-416c-9440-e341cb047cd3}')
    @winrt_commethod(6)
    def OnResourceRequested(self, args: win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedResourceRequestedArgs) -> Void: ...
class IFeedResourceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceRequest'
    _iid_ = Guid('{e62e479c-e21f-5863-b4c9-df1be2227981}')
    @winrt_commethod(6)
    def get_Uri(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Method(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Method(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Content(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(10)
    def put_Content(self, value: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> Void: ...
    @winrt_commethod(11)
    def get_Headers(self) -> win32more.Windows.Foundation.Collections.StringMap: ...
    @winrt_commethod(12)
    def put_Headers(self, value: win32more.Windows.Foundation.Collections.StringMap) -> Void: ...
    Content = property(get_Content, put_Content)
    Headers = property(get_Headers, put_Headers)
    Method = property(get_Method, put_Method)
    Uri = property(get_Uri, None)
class IFeedResourceRequestedArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceRequestedArgs'
    _iid_ = Guid('{360eb709-0bc9-52c1-9c70-3c7d413173d8}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FeedDefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Request(self) -> win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedResourceRequest: ...
    @winrt_commethod(9)
    def get_Response(self) -> win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedResourceResponse: ...
    @winrt_commethod(10)
    def put_Response(self, value: win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedResourceResponse) -> Void: ...
    @winrt_commethod(11)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    FeedDefinitionId = property(get_FeedDefinitionId, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
    Request = property(get_Request, None)
    Response = property(get_Response, put_Response)
class IFeedResourceResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceResponse'
    _iid_ = Guid('{f831824e-7aef-53fc-b7ee-32ade675a3ad}')
    @winrt_commethod(6)
    def get_Content(self) -> win32more.Windows.Storage.Streams.IRandomAccessStreamReference: ...
    @winrt_commethod(7)
    def get_Headers(self) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]: ...
    @winrt_commethod(8)
    def put_Headers(self, value: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Void: ...
    @winrt_commethod(9)
    def get_ReasonPhrase(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_StatusCode(self) -> Int32: ...
    Content = property(get_Content, None)
    Headers = property(get_Headers, put_Headers)
    ReasonPhrase = property(get_ReasonPhrase, None)
    StatusCode = property(get_StatusCode, None)
class IFeedResourceResponseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedResourceResponseFactory'
    _iid_ = Guid('{db01690d-2547-5d7a-b625-d1629f443c5c}')
    @winrt_commethod(6)
    def CreateInstance(self, content: win32more.Windows.Storage.Streams.IRandomAccessStreamReference, reasonPhrase: WinRT_String, statusCode: Int32) -> win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedResourceResponse: ...


make_ready(__name__)
