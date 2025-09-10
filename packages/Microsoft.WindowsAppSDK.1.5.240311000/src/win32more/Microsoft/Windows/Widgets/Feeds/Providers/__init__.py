from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Microsoft.Windows.Widgets.Feeds.Providers
class CustomQueryParametersRequestedArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.ICustomQueryParametersRequestedArgs
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.CustomQueryParametersRequestedArgs'
    @winrt_mixinmethod
    def get_FeedProviderDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.ICustomQueryParametersRequestedArgs) -> WinRT_String: ...
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class CustomQueryParametersUpdateOptions(ComPtr):
    extends: IInspectable
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
class FeedDisabledArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedDisabledArgs
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.FeedDisabledArgs'
    @winrt_mixinmethod
    def get_FeedProviderDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedDisabledArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FeedDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedDisabledArgs) -> WinRT_String: ...
    FeedDefinitionId = property(get_FeedDefinitionId, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class FeedEnabledArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedEnabledArgs
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.FeedEnabledArgs'
    @winrt_mixinmethod
    def get_FeedProviderDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedEnabledArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FeedDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedEnabledArgs) -> WinRT_String: ...
    FeedDefinitionId = property(get_FeedDefinitionId, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class FeedManager(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedManager
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.FeedManager'
    @winrt_mixinmethod
    def GetEnabledFeedProviders(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedManager) -> ReceiveArray[win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedProviderInfo]: ...
    @winrt_mixinmethod
    def SetCustomQueryParameters(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedManager, options: win32more.Microsoft.Windows.Widgets.Feeds.Providers.CustomQueryParametersUpdateOptions) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedManagerStatics) -> win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedManager: ...
class FeedProviderDisabledArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderDisabledArgs
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.FeedProviderDisabledArgs'
    @winrt_mixinmethod
    def get_FeedProviderDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderDisabledArgs) -> WinRT_String: ...
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class FeedProviderEnabledArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderEnabledArgs
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.FeedProviderEnabledArgs'
    @winrt_mixinmethod
    def get_FeedProviderDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderEnabledArgs) -> WinRT_String: ...
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class FeedProviderInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderInfo
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.FeedProviderInfo'
    @winrt_mixinmethod
    def get_FeedProviderDefinitionId(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EnabledFeedDefinitionIds(self: win32more.Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderInfo) -> ReceiveArray[WinRT_String]: ...
    EnabledFeedDefinitionIds = property(get_EnabledFeedDefinitionIds, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class ICustomQueryParametersRequestedArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.ICustomQueryParametersRequestedArgs'
    _iid_ = Guid('{dc2b0cd8-7936-5346-9371-b21484c7d859}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class ICustomQueryParametersUpdateOptions(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.ICustomQueryParametersUpdateOptions'
    _iid_ = Guid('{753f1177-4909-568a-b070-98a3139205ec}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_CustomQueryParameters(self) -> WinRT_String: ...
    CustomQueryParameters = property(get_CustomQueryParameters, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class ICustomQueryParametersUpdateOptionsFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.ICustomQueryParametersUpdateOptionsFactory'
    _iid_ = Guid('{34e318cd-3884-53c0-911c-225f32228fae}')
    @winrt_commethod(6)
    def CreateInstance(self, feedProviderDefinitionId: WinRT_String, customQueryParameters: WinRT_String) -> win32more.Microsoft.Windows.Widgets.Feeds.Providers.CustomQueryParametersUpdateOptions: ...
class IFeedDisabledArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedDisabledArgs'
    _iid_ = Guid('{95300612-aca7-53c0-9cf6-d803689132c1}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FeedDefinitionId(self) -> WinRT_String: ...
    FeedDefinitionId = property(get_FeedDefinitionId, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class IFeedEnabledArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedEnabledArgs'
    _iid_ = Guid('{eff4b2d7-7347-5969-a77d-cac433f0fdae}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_FeedDefinitionId(self) -> WinRT_String: ...
    FeedDefinitionId = property(get_FeedDefinitionId, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class IFeedManager(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedManager'
    _iid_ = Guid('{87df6a84-15aa-45cb-8911-5cafab57f723}')
    @winrt_commethod(6)
    def GetEnabledFeedProviders(self) -> ReceiveArray[win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedProviderInfo]: ...
    @winrt_commethod(7)
    def SetCustomQueryParameters(self, options: win32more.Microsoft.Windows.Widgets.Feeds.Providers.CustomQueryParametersUpdateOptions) -> Void: ...
class IFeedManagerStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedManagerStatics'
    _iid_ = Guid('{4baf5174-77d6-5e2a-94ea-4f14ccdb1f2c}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Microsoft.Windows.Widgets.Feeds.Providers.FeedManager: ...
class IFeedProvider(ComPtr):
    extends: IInspectable
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
class IFeedProviderDisabledArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderDisabledArgs'
    _iid_ = Guid('{19b65aec-e01d-5e8c-ab5f-324212e7cd30}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class IFeedProviderEnabledArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderEnabledArgs'
    _iid_ = Guid('{821fc9af-0de6-5a9b-9ae6-e179117b40e4}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)
class IFeedProviderInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.Widgets.Feeds.Providers.IFeedProviderInfo'
    _iid_ = Guid('{73c37049-3c03-5896-8532-f9dfdaeb723f}')
    @winrt_commethod(6)
    def get_FeedProviderDefinitionId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EnabledFeedDefinitionIds(self) -> ReceiveArray[WinRT_String]: ...
    EnabledFeedDefinitionIds = property(get_EnabledFeedDefinitionIds, None)
    FeedProviderDefinitionId = property(get_FeedProviderDefinitionId, None)


make_ready(__name__)
