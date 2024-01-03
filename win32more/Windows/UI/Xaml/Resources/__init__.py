from __future__ import annotations
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.UI.Xaml.Resources
class _CustomXamlResourceLoader_Meta_(ComPtr.__class__):
    pass
class CustomXamlResourceLoader(ComPtr, metaclass=_CustomXamlResourceLoader_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Resources.ICustomXamlResourceLoader
    _classid_ = 'Windows.UI.Xaml.Resources.CustomXamlResourceLoader'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.UI.Xaml.Resources.CustomXamlResourceLoader.CreateInstance(*args, None, None)
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Resources.CustomXamlResourceLoader: ...
    @winrt_mixinmethod
    def GetResource(self: win32more.Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderOverrides, resourceId: WinRT_String, objectType: WinRT_String, propertyName: WinRT_String, propertyType: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderStatics) -> win32more.Windows.UI.Xaml.Resources.CustomXamlResourceLoader: ...
    @winrt_classmethod
    def put_Current(cls: win32more.Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderStatics, value: win32more.Windows.UI.Xaml.Resources.CustomXamlResourceLoader) -> Void: ...
    _CustomXamlResourceLoader_Meta_.Current = property(get_Current.__wrapped__, put_Current.__wrapped__)
class ICustomXamlResourceLoader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Resources.ICustomXamlResourceLoader'
    _iid_ = Guid('{511a84ab-4a88-419f-852e-54083b90b078}')
class ICustomXamlResourceLoaderFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderFactory'
    _iid_ = Guid('{5bfd7e49-7886-44f3-8ed3-6fec0463ed69}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Resources.CustomXamlResourceLoader: ...
class ICustomXamlResourceLoaderOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderOverrides'
    _iid_ = Guid('{f851e991-af02-46e8-9af8-427b7ebfe9f8}')
    @winrt_commethod(6)
    def GetResource(self, resourceId: WinRT_String, objectType: WinRT_String, propertyName: WinRT_String, propertyType: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class ICustomXamlResourceLoaderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderStatics'
    _iid_ = Guid('{224ff617-e4dc-4c27-ad32-db93d5d0e5da}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.UI.Xaml.Resources.CustomXamlResourceLoader: ...
    @winrt_commethod(7)
    def put_Current(self, value: win32more.Windows.UI.Xaml.Resources.CustomXamlResourceLoader) -> Void: ...
    Current = property(get_Current, put_Current)


make_ready(__name__)
