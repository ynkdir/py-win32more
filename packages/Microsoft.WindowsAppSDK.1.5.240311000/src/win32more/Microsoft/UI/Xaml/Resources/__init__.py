from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Microsoft.UI.Xaml.Resources
class _CustomXamlResourceLoader_Meta_(ComPtr.__class__):
    pass
class CustomXamlResourceLoader(ComPtr, metaclass=_CustomXamlResourceLoader_Meta_):
    extends: IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Resources.ICustomXamlResourceLoader
    _classid_ = 'Microsoft.UI.Xaml.Resources.CustomXamlResourceLoader'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Resources.CustomXamlResourceLoader.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Resources.ICustomXamlResourceLoaderFactory, baseInterface: IInspectable, innerInterface: POINTER(IInspectable)) -> win32more.Microsoft.UI.Xaml.Resources.CustomXamlResourceLoader: ...
    @winrt_mixinmethod
    def GetResource(self: win32more.Microsoft.UI.Xaml.Resources.ICustomXamlResourceLoaderOverrides, resourceId: WinRT_String, objectType: WinRT_String, propertyName: WinRT_String, propertyType: WinRT_String) -> IInspectable: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Microsoft.UI.Xaml.Resources.ICustomXamlResourceLoaderStatics) -> win32more.Microsoft.UI.Xaml.Resources.CustomXamlResourceLoader: ...
    @winrt_classmethod
    def put_Current(cls: win32more.Microsoft.UI.Xaml.Resources.ICustomXamlResourceLoaderStatics, value: win32more.Microsoft.UI.Xaml.Resources.CustomXamlResourceLoader) -> Void: ...
    _CustomXamlResourceLoader_Meta_.Current = property(get_Current, put_Current)
class ICustomXamlResourceLoader(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Resources.ICustomXamlResourceLoader'
    _iid_ = Guid('{2832c2e5-2ace-5993-a173-3c9c3b992b2e}')
class ICustomXamlResourceLoaderFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Resources.ICustomXamlResourceLoaderFactory'
    _iid_ = Guid('{174d49a6-e1e2-5f7b-a618-a8a953d1b5a0}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: IInspectable, innerInterface: POINTER(IInspectable)) -> win32more.Microsoft.UI.Xaml.Resources.CustomXamlResourceLoader: ...
class ICustomXamlResourceLoaderOverrides(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Resources.ICustomXamlResourceLoaderOverrides'
    _iid_ = Guid('{84bb504c-6730-586a-bd04-9198264b2dc7}')
    @winrt_commethod(6)
    def GetResource(self, resourceId: WinRT_String, objectType: WinRT_String, propertyName: WinRT_String, propertyType: WinRT_String) -> IInspectable: ...
class ICustomXamlResourceLoaderStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Resources.ICustomXamlResourceLoaderStatics'
    _iid_ = Guid('{e08a5a92-b1a2-539a-9d4a-7994e4468cd7}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Microsoft.UI.Xaml.Resources.CustomXamlResourceLoader: ...
    @winrt_commethod(7)
    def put_Current(self, value: win32more.Microsoft.UI.Xaml.Resources.CustomXamlResourceLoader) -> Void: ...
    Current = property(get_Current, put_Current)


make_ready(__name__)
