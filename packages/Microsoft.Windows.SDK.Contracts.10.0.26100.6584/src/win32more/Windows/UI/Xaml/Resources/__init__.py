from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.UI.Xaml.Resources
class _CustomXamlResourceLoader_Meta_(ComPtr.__class__):
    pass
class CustomXamlResourceLoader(ComPtr, metaclass=_CustomXamlResourceLoader_Meta_):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Xaml.Resources.ICustomXamlResourceLoader
    _classid_ = 'Windows.UI.Xaml.Resources.CustomXamlResourceLoader'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Resources.CustomXamlResourceLoader.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderFactory, baseInterface: IInspectable, innerInterface: POINTER(IInspectable)) -> win32more.Windows.UI.Xaml.Resources.CustomXamlResourceLoader: ...
    @winrt_mixinmethod
    def GetResource(self: win32more.Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderOverrides, resourceId: WinRT_String, objectType: WinRT_String, propertyName: WinRT_String, propertyType: WinRT_String) -> IInspectable: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderStatics) -> win32more.Windows.UI.Xaml.Resources.CustomXamlResourceLoader: ...
    @winrt_classmethod
    def put_Current(cls: win32more.Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderStatics, value: win32more.Windows.UI.Xaml.Resources.CustomXamlResourceLoader) -> Void: ...
    _CustomXamlResourceLoader_Meta_.Current = property(get_Current, put_Current)
class ICustomXamlResourceLoader(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Xaml.Resources.ICustomXamlResourceLoader'
    _iid_ = Guid('{511a84ab-4a88-419f-852e-54083b90b078}')
class ICustomXamlResourceLoaderFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderFactory'
    _iid_ = Guid('{5bfd7e49-7886-44f3-8ed3-6fec0463ed69}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: IInspectable, innerInterface: POINTER(IInspectable)) -> win32more.Windows.UI.Xaml.Resources.CustomXamlResourceLoader: ...
class ICustomXamlResourceLoaderOverrides(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderOverrides'
    _iid_ = Guid('{f851e991-af02-46e8-9af8-427b7ebfe9f8}')
    @winrt_commethod(6)
    def GetResource(self, resourceId: WinRT_String, objectType: WinRT_String, propertyName: WinRT_String, propertyType: WinRT_String) -> IInspectable: ...
class ICustomXamlResourceLoaderStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderStatics'
    _iid_ = Guid('{224ff617-e4dc-4c27-ad32-db93d5d0e5da}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.UI.Xaml.Resources.CustomXamlResourceLoader: ...
    @winrt_commethod(7)
    def put_Current(self, value: win32more.Windows.UI.Xaml.Resources.CustomXamlResourceLoader) -> Void: ...
    Current = property(get_Current, put_Current)


make_ready(__name__)
