from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Microsoft.UI.Xaml.Markup
import win32more.Microsoft.UI.Xaml.XamlTypeInfo
import win32more.Windows.UI.Xaml.Interop
class IXamlControlsXamlMetaDataProvider(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Xaml.XamlTypeInfo.IXamlControlsXamlMetaDataProvider'
    _iid_ = Guid('{17fa3f58-3472-5aa2-a0f8-1ab8a519573d}')
class IXamlControlsXamlMetaDataProviderStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Xaml.XamlTypeInfo.IXamlControlsXamlMetaDataProviderStatics'
    _iid_ = Guid('{2d7eb3fd-ecdb-5084-b7e0-12f9598381ef}')
    @winrt_commethod(6)
    def Initialize(self) -> Void: ...
class XamlControlsXamlMetaDataProvider(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Markup.IXamlMetadataProvider
    _classid_ = 'Microsoft.UI.Xaml.XamlTypeInfo.XamlControlsXamlMetaDataProvider'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.XamlTypeInfo.XamlControlsXamlMetaDataProvider.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.XamlTypeInfo.XamlControlsXamlMetaDataProvider: ...
    @winrt_mixinmethod
    def GetXamlType(self: win32more.Microsoft.UI.Xaml.Markup.IXamlMetadataProvider, type: win32more.Windows.UI.Xaml.Interop.TypeName) -> win32more.Microsoft.UI.Xaml.Markup.IXamlType: ...
    @winrt_mixinmethod
    def GetXamlTypeByFullName(self: win32more.Microsoft.UI.Xaml.Markup.IXamlMetadataProvider, fullName: WinRT_String) -> win32more.Microsoft.UI.Xaml.Markup.IXamlType: ...
    @winrt_mixinmethod
    def GetXmlnsDefinitions(self: win32more.Microsoft.UI.Xaml.Markup.IXamlMetadataProvider) -> ReceiveArray[win32more.Microsoft.UI.Xaml.Markup.XmlnsDefinition]: ...
    @winrt_classmethod
    def Initialize(cls: win32more.Microsoft.UI.Xaml.XamlTypeInfo.IXamlControlsXamlMetaDataProviderStatics) -> Void: ...


make_ready(__name__)
