from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Microsoft.UI.Xaml.Resources
class _CustomXamlResourceLoader_Meta_(ComPtr.__class__):
    pass
class CustomXamlResourceLoader(ComPtr, metaclass=_CustomXamlResourceLoader_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Resources.ICustomXamlResourceLoader
    _classid_ = 'Microsoft.UI.Xaml.Resources.CustomXamlResourceLoader'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Microsoft.UI.Xaml.Resources.CustomXamlResourceLoader.CreateInstance(*args, None, None)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Resources.ICustomXamlResourceLoaderFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Resources.CustomXamlResourceLoader: ...
    @winrt_mixinmethod
    def GetResource(self: win32more.Microsoft.UI.Xaml.Resources.ICustomXamlResourceLoaderOverrides, resourceId: WinRT_String, objectType: WinRT_String, propertyName: WinRT_String, propertyType: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_classmethod
    def get_Current(cls: win32more.Microsoft.UI.Xaml.Resources.ICustomXamlResourceLoaderStatics) -> win32more.Microsoft.UI.Xaml.Resources.CustomXamlResourceLoader: ...
    @winrt_classmethod
    def put_Current(cls: win32more.Microsoft.UI.Xaml.Resources.ICustomXamlResourceLoaderStatics, value: win32more.Microsoft.UI.Xaml.Resources.CustomXamlResourceLoader) -> Void: ...
    _CustomXamlResourceLoader_Meta_.Current = property(get_Current.__wrapped__, put_Current.__wrapped__)
class ICustomXamlResourceLoader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Resources.ICustomXamlResourceLoader'
    _iid_ = Guid('{2832c2e5-2ace-5993-a173-3c9c3b992b2e}')
class ICustomXamlResourceLoaderFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Resources.ICustomXamlResourceLoaderFactory'
    _iid_ = Guid('{174d49a6-e1e2-5f7b-a618-a8a953d1b5a0}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Resources.CustomXamlResourceLoader: ...
class ICustomXamlResourceLoaderOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Resources.ICustomXamlResourceLoaderOverrides'
    _iid_ = Guid('{84bb504c-6730-586a-bd04-9198264b2dc7}')
    @winrt_commethod(6)
    def GetResource(self, resourceId: WinRT_String, objectType: WinRT_String, propertyName: WinRT_String, propertyType: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
class ICustomXamlResourceLoaderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Resources.ICustomXamlResourceLoaderStatics'
    _iid_ = Guid('{e08a5a92-b1a2-539a-9d4a-7994e4468cd7}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Microsoft.UI.Xaml.Resources.CustomXamlResourceLoader: ...
    @winrt_commethod(7)
    def put_Current(self, value: win32more.Microsoft.UI.Xaml.Resources.CustomXamlResourceLoader) -> Void: ...
    Current = property(get_Current, put_Current)
make_ready(__name__)
