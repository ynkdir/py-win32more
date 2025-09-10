from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Microsoft.Windows.Widgets
import win32more.Microsoft.Windows.Widgets.Providers
import win32more.Windows.Foundation
class IWidgetActionInvokedArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Providers.IWidgetActionInvokedArgs'
    _iid_ = Guid('{c593cc57-04b9-52ca-88ad-46fea21ea340}')
    @winrt_commethod(6)
    def get_WidgetContext(self) -> win32more.Microsoft.Windows.Widgets.Providers.WidgetContext: ...
    @winrt_commethod(7)
    def get_Verb(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Data(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_CustomState(self) -> WinRT_String: ...
    CustomState = property(get_CustomState, None)
    Data = property(get_Data, None)
    Verb = property(get_Verb, None)
    WidgetContext = property(get_WidgetContext, None)
class IWidgetAnalyticsInfoReportedArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Providers.IWidgetAnalyticsInfoReportedArgs'
    _iid_ = Guid('{1d9e5fb5-2bce-5350-87b1-d63199526639}')
    @winrt_commethod(6)
    def get_WidgetContext(self) -> win32more.Microsoft.Windows.Widgets.Providers.WidgetContext: ...
    @winrt_commethod(7)
    def get_AnalyticsJson(self) -> WinRT_String: ...
    AnalyticsJson = property(get_AnalyticsJson, None)
    WidgetContext = property(get_WidgetContext, None)
class IWidgetContext(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Providers.IWidgetContext'
    _iid_ = Guid('{903c518b-40bc-5bc6-88f7-af9d81c0cdc1}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Size(self) -> win32more.Microsoft.Windows.Widgets.WidgetSize: ...
    @winrt_commethod(9)
    def get_IsActive(self) -> Boolean: ...
    DefinitionId = property(get_DefinitionId, None)
    Id = property(get_Id, None)
    IsActive = property(get_IsActive, None)
    Size = property(get_Size, None)
class IWidgetContextChangedArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Providers.IWidgetContextChangedArgs'
    _iid_ = Guid('{2c226d54-2252-576b-a197-370b28d25c2f}')
    @winrt_commethod(6)
    def get_WidgetContext(self) -> win32more.Microsoft.Windows.Widgets.Providers.WidgetContext: ...
    WidgetContext = property(get_WidgetContext, None)
class IWidgetCustomizationRequestedArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Providers.IWidgetCustomizationRequestedArgs'
    _iid_ = Guid('{41dea311-dd9b-5b8b-b493-3a30552116b8}')
    @winrt_commethod(6)
    def get_WidgetContext(self) -> win32more.Microsoft.Windows.Widgets.Providers.WidgetContext: ...
    @winrt_commethod(7)
    def get_CustomState(self) -> WinRT_String: ...
    CustomState = property(get_CustomState, None)
    WidgetContext = property(get_WidgetContext, None)
class IWidgetErrorInfoReportedArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Providers.IWidgetErrorInfoReportedArgs'
    _iid_ = Guid('{30efa627-b21f-55d5-b91a-b23b4aa13645}')
    @winrt_commethod(6)
    def get_WidgetContext(self) -> win32more.Microsoft.Windows.Widgets.Providers.WidgetContext: ...
    @winrt_commethod(7)
    def get_ErrorJson(self) -> WinRT_String: ...
    ErrorJson = property(get_ErrorJson, None)
    WidgetContext = property(get_WidgetContext, None)
class IWidgetInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Providers.IWidgetInfo'
    _iid_ = Guid('{cea11f42-a020-5db5-89e2-b7dece4ae5cb}')
    @winrt_commethod(6)
    def get_WidgetContext(self) -> win32more.Microsoft.Windows.Widgets.Providers.WidgetContext: ...
    @winrt_commethod(7)
    def get_Template(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Data(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_CustomState(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_LastUpdateTime(self) -> win32more.Windows.Foundation.DateTime: ...
    CustomState = property(get_CustomState, None)
    Data = property(get_Data, None)
    LastUpdateTime = property(get_LastUpdateTime, None)
    Template = property(get_Template, None)
    WidgetContext = property(get_WidgetContext, None)
class IWidgetManager(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Providers.IWidgetManager'
    _iid_ = Guid('{71cb10c0-671e-48e3-b995-207940397123}')
    @winrt_commethod(6)
    def UpdateWidget(self, widgetUpdateRequestOptions: win32more.Microsoft.Windows.Widgets.Providers.WidgetUpdateRequestOptions) -> Void: ...
    @winrt_commethod(7)
    def GetWidgetIds(self) -> ReceiveArray[WinRT_String]: ...
    @winrt_commethod(8)
    def GetWidgetInfo(self, widgetId: WinRT_String) -> win32more.Microsoft.Windows.Widgets.Providers.WidgetInfo: ...
    @winrt_commethod(9)
    def GetWidgetInfos(self) -> ReceiveArray[win32more.Microsoft.Windows.Widgets.Providers.WidgetInfo]: ...
    @winrt_commethod(10)
    def DeleteWidget(self, widgetId: WinRT_String) -> Void: ...
class IWidgetManagerStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Providers.IWidgetManagerStatics'
    _iid_ = Guid('{7f233b06-28e5-5e2b-8c04-a4fa747c28c7}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Microsoft.Windows.Widgets.Providers.WidgetManager: ...
class IWidgetProvider(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Providers.IWidgetProvider'
    _iid_ = Guid('{5c5774cc-72a0-452d-b9ed-075c0dd25eed}')
    @winrt_commethod(6)
    def CreateWidget(self, widgetContext: win32more.Microsoft.Windows.Widgets.Providers.WidgetContext) -> Void: ...
    @winrt_commethod(7)
    def DeleteWidget(self, widgetId: WinRT_String, customState: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def OnActionInvoked(self, actionInvokedArgs: win32more.Microsoft.Windows.Widgets.Providers.WidgetActionInvokedArgs) -> Void: ...
    @winrt_commethod(9)
    def OnWidgetContextChanged(self, contextChangedArgs: win32more.Microsoft.Windows.Widgets.Providers.WidgetContextChangedArgs) -> Void: ...
    @winrt_commethod(10)
    def Activate(self, widgetContext: win32more.Microsoft.Windows.Widgets.Providers.WidgetContext) -> Void: ...
    @winrt_commethod(11)
    def Deactivate(self, widgetId: WinRT_String) -> Void: ...
class IWidgetProvider2(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Providers.IWidgetProvider2'
    _iid_ = Guid('{38c3a963-dd93-479d-9276-04bf84ee1816}')
    @winrt_commethod(6)
    def OnCustomizationRequested(self, customizationRequestedArgs: win32more.Microsoft.Windows.Widgets.Providers.WidgetCustomizationRequestedArgs) -> Void: ...
class IWidgetProviderAnalytics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Providers.IWidgetProviderAnalytics'
    _iid_ = Guid('{661985a5-d187-482d-9eef-6fda05d21845}')
    @winrt_commethod(6)
    def OnAnalyticsInfoReported(self, args: win32more.Microsoft.Windows.Widgets.Providers.WidgetAnalyticsInfoReportedArgs) -> Void: ...
class IWidgetProviderErrors(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Providers.IWidgetProviderErrors'
    _iid_ = Guid('{90c1b5f0-0d3a-4ac6-abb7-c97b367b8fcc}')
    @winrt_commethod(6)
    def OnErrorInfoReported(self, args: win32more.Microsoft.Windows.Widgets.Providers.WidgetErrorInfoReportedArgs) -> Void: ...
class IWidgetUpdateRequestOptions(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Providers.IWidgetUpdateRequestOptions'
    _iid_ = Guid('{b09ca8f7-7424-5687-baaf-7dd6fa639672}')
    @winrt_commethod(6)
    def get_WidgetId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Template(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Template(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Data(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_Data(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_CustomState(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_CustomState(self, value: WinRT_String) -> Void: ...
    CustomState = property(get_CustomState, put_CustomState)
    Data = property(get_Data, put_Data)
    Template = property(get_Template, put_Template)
    WidgetId = property(get_WidgetId, None)
class IWidgetUpdateRequestOptionsFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Providers.IWidgetUpdateRequestOptionsFactory'
    _iid_ = Guid('{e0e00af8-1d10-57a8-9419-3f568e854daa}')
    @winrt_commethod(6)
    def CreateInstance(self, widgetId: WinRT_String) -> win32more.Microsoft.Windows.Widgets.Providers.WidgetUpdateRequestOptions: ...
class IWidgetUpdateRequestOptionsStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Providers.IWidgetUpdateRequestOptionsStatics'
    _iid_ = Guid('{4645b5e3-d332-5d11-82f0-3607e5df6018}')
    @winrt_commethod(6)
    def get_UnsetValue(self) -> WinRT_String: ...
    UnsetValue = property(get_UnsetValue, None)
class WidgetActionInvokedArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Providers.IWidgetActionInvokedArgs
    _classid_ = 'Microsoft.Windows.Widgets.Providers.WidgetActionInvokedArgs'
    @winrt_mixinmethod
    def get_WidgetContext(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetActionInvokedArgs) -> win32more.Microsoft.Windows.Widgets.Providers.WidgetContext: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetActionInvokedArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetActionInvokedArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CustomState(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetActionInvokedArgs) -> WinRT_String: ...
    CustomState = property(get_CustomState, None)
    Data = property(get_Data, None)
    Verb = property(get_Verb, None)
    WidgetContext = property(get_WidgetContext, None)
class WidgetAnalyticsInfoReportedArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Providers.IWidgetAnalyticsInfoReportedArgs
    _classid_ = 'Microsoft.Windows.Widgets.Providers.WidgetAnalyticsInfoReportedArgs'
    @winrt_mixinmethod
    def get_WidgetContext(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetAnalyticsInfoReportedArgs) -> win32more.Microsoft.Windows.Widgets.Providers.WidgetContext: ...
    @winrt_mixinmethod
    def get_AnalyticsJson(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetAnalyticsInfoReportedArgs) -> WinRT_String: ...
    AnalyticsJson = property(get_AnalyticsJson, None)
    WidgetContext = property(get_WidgetContext, None)
class WidgetContext(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Providers.IWidgetContext
    _classid_ = 'Microsoft.Windows.Widgets.Providers.WidgetContext'
    @winrt_mixinmethod
    def get_Id(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetContext) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DefinitionId(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetContext) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetContext) -> win32more.Microsoft.Windows.Widgets.WidgetSize: ...
    @winrt_mixinmethod
    def get_IsActive(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetContext) -> Boolean: ...
    DefinitionId = property(get_DefinitionId, None)
    Id = property(get_Id, None)
    IsActive = property(get_IsActive, None)
    Size = property(get_Size, None)
class WidgetContextChangedArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Providers.IWidgetContextChangedArgs
    _classid_ = 'Microsoft.Windows.Widgets.Providers.WidgetContextChangedArgs'
    @winrt_mixinmethod
    def get_WidgetContext(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetContextChangedArgs) -> win32more.Microsoft.Windows.Widgets.Providers.WidgetContext: ...
    WidgetContext = property(get_WidgetContext, None)
class WidgetCustomizationRequestedArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Providers.IWidgetCustomizationRequestedArgs
    _classid_ = 'Microsoft.Windows.Widgets.Providers.WidgetCustomizationRequestedArgs'
    @winrt_mixinmethod
    def get_WidgetContext(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetCustomizationRequestedArgs) -> win32more.Microsoft.Windows.Widgets.Providers.WidgetContext: ...
    @winrt_mixinmethod
    def get_CustomState(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetCustomizationRequestedArgs) -> WinRT_String: ...
    CustomState = property(get_CustomState, None)
    WidgetContext = property(get_WidgetContext, None)
class WidgetErrorInfoReportedArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Providers.IWidgetErrorInfoReportedArgs
    _classid_ = 'Microsoft.Windows.Widgets.Providers.WidgetErrorInfoReportedArgs'
    @winrt_mixinmethod
    def get_WidgetContext(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetErrorInfoReportedArgs) -> win32more.Microsoft.Windows.Widgets.Providers.WidgetContext: ...
    @winrt_mixinmethod
    def get_ErrorJson(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetErrorInfoReportedArgs) -> WinRT_String: ...
    ErrorJson = property(get_ErrorJson, None)
    WidgetContext = property(get_WidgetContext, None)
class WidgetInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Providers.IWidgetInfo
    _classid_ = 'Microsoft.Windows.Widgets.Providers.WidgetInfo'
    @winrt_mixinmethod
    def get_WidgetContext(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetInfo) -> win32more.Microsoft.Windows.Widgets.Providers.WidgetContext: ...
    @winrt_mixinmethod
    def get_Template(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CustomState(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LastUpdateTime(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetInfo) -> win32more.Windows.Foundation.DateTime: ...
    CustomState = property(get_CustomState, None)
    Data = property(get_Data, None)
    LastUpdateTime = property(get_LastUpdateTime, None)
    Template = property(get_Template, None)
    WidgetContext = property(get_WidgetContext, None)
class WidgetManager(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Providers.IWidgetManager
    _classid_ = 'Microsoft.Windows.Widgets.Providers.WidgetManager'
    @winrt_mixinmethod
    def UpdateWidget(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetManager, widgetUpdateRequestOptions: win32more.Microsoft.Windows.Widgets.Providers.WidgetUpdateRequestOptions) -> Void: ...
    @winrt_mixinmethod
    def GetWidgetIds(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetManager) -> ReceiveArray[WinRT_String]: ...
    @winrt_mixinmethod
    def GetWidgetInfo(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetManager, widgetId: WinRT_String) -> win32more.Microsoft.Windows.Widgets.Providers.WidgetInfo: ...
    @winrt_mixinmethod
    def GetWidgetInfos(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetManager) -> ReceiveArray[win32more.Microsoft.Windows.Widgets.Providers.WidgetInfo]: ...
    @winrt_mixinmethod
    def DeleteWidget(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetManager, widgetId: WinRT_String) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Microsoft.Windows.Widgets.Providers.IWidgetManagerStatics) -> win32more.Microsoft.Windows.Widgets.Providers.WidgetManager: ...
class _WidgetUpdateRequestOptions_Meta_(ComPtr.__class__):
    pass
class WidgetUpdateRequestOptions(ComPtr, metaclass=_WidgetUpdateRequestOptions_Meta_):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Providers.IWidgetUpdateRequestOptions
    _classid_ = 'Microsoft.Windows.Widgets.Providers.WidgetUpdateRequestOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Windows.Widgets.Providers.WidgetUpdateRequestOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.Widgets.Providers.IWidgetUpdateRequestOptionsFactory, widgetId: WinRT_String) -> win32more.Microsoft.Windows.Widgets.Providers.WidgetUpdateRequestOptions: ...
    @winrt_mixinmethod
    def get_WidgetId(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetUpdateRequestOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Template(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetUpdateRequestOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Template(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetUpdateRequestOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetUpdateRequestOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Data(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetUpdateRequestOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CustomState(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetUpdateRequestOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CustomState(self: win32more.Microsoft.Windows.Widgets.Providers.IWidgetUpdateRequestOptions, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_UnsetValue(cls: win32more.Microsoft.Windows.Widgets.Providers.IWidgetUpdateRequestOptionsStatics) -> WinRT_String: ...
    CustomState = property(get_CustomState, put_CustomState)
    Data = property(get_Data, put_Data)
    Template = property(get_Template, put_Template)
    WidgetId = property(get_WidgetId, None)
    _WidgetUpdateRequestOptions_Meta_.UnsetValue = property(get_UnsetValue, None)


make_ready(__name__)
