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
import Windows.UI.Xaml.Resources
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class CustomXamlResourceLoader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Resources.ICustomXamlResourceLoader
    _classid_ = 'Windows.UI.Xaml.Resources.CustomXamlResourceLoader'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderFactory, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Resources.CustomXamlResourceLoader: ...
    @winrt_mixinmethod
    def GetResource(self: Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderOverrides, resourceId: WinRT_String, objectType: WinRT_String, propertyName: WinRT_String, propertyType: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_classmethod
    def get_Current(cls: Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderStatics) -> Windows.UI.Xaml.Resources.CustomXamlResourceLoader: ...
    @winrt_classmethod
    def put_Current(cls: Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderStatics, value: Windows.UI.Xaml.Resources.CustomXamlResourceLoader) -> Void: ...
    Current = property(get_Current, put_Current)
class ICustomXamlResourceLoader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Resources.ICustomXamlResourceLoader'
    _iid_ = Guid('{511a84ab-4a88-419f-852e-54083b90b078}')
class ICustomXamlResourceLoaderFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderFactory'
    _iid_ = Guid('{5bfd7e49-7886-44f3-8ed3-6fec0463ed69}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Resources.CustomXamlResourceLoader: ...
class ICustomXamlResourceLoaderOverrides(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderOverrides'
    _iid_ = Guid('{f851e991-af02-46e8-9af8-427b7ebfe9f8}')
    @winrt_commethod(6)
    def GetResource(self, resourceId: WinRT_String, objectType: WinRT_String, propertyName: WinRT_String, propertyType: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
class ICustomXamlResourceLoaderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Resources.ICustomXamlResourceLoaderStatics'
    _iid_ = Guid('{224ff617-e4dc-4c27-ad32-db93d5d0e5da}')
    @winrt_commethod(6)
    def get_Current(self) -> Windows.UI.Xaml.Resources.CustomXamlResourceLoader: ...
    @winrt_commethod(7)
    def put_Current(self, value: Windows.UI.Xaml.Resources.CustomXamlResourceLoader) -> Void: ...
    Current = property(get_Current, put_Current)
make_head(_module, 'CustomXamlResourceLoader')
make_head(_module, 'ICustomXamlResourceLoader')
make_head(_module, 'ICustomXamlResourceLoaderFactory')
make_head(_module, 'ICustomXamlResourceLoaderOverrides')
make_head(_module, 'ICustomXamlResourceLoaderStatics')
