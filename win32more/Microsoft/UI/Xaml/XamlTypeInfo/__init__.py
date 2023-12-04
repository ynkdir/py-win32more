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
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Microsoft.UI.Xaml.Markup
import win32more.Microsoft.UI.Xaml.XamlTypeInfo
import win32more.Windows.UI.Xaml.Interop
class IXamlControlsXamlMetaDataProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.XamlTypeInfo.IXamlControlsXamlMetaDataProvider'
    _iid_ = Guid('{17fa3f58-3472-5aa2-a0f8-1ab8a519573d}')
class IXamlControlsXamlMetaDataProviderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.XamlTypeInfo.IXamlControlsXamlMetaDataProviderStatics'
    _iid_ = Guid('{2d7eb3fd-ecdb-5084-b7e0-12f9598381ef}')
    @winrt_commethod(6)
    def Initialize(self) -> Void: ...
class XamlControlsXamlMetaDataProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Markup.IXamlMetadataProvider
    _classid_ = 'Microsoft.UI.Xaml.XamlTypeInfo.XamlControlsXamlMetaDataProvider'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Microsoft.UI.Xaml.XamlTypeInfo.XamlControlsXamlMetaDataProvider.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.XamlTypeInfo.XamlControlsXamlMetaDataProvider: ...
    @winrt_mixinmethod
    def GetXamlType(self: win32more.Microsoft.UI.Xaml.Markup.IXamlMetadataProvider, type: win32more.Windows.UI.Xaml.Interop.TypeName) -> win32more.Microsoft.UI.Xaml.Markup.IXamlType: ...
    @winrt_mixinmethod
    def GetXamlTypeByFullName(self: win32more.Microsoft.UI.Xaml.Markup.IXamlMetadataProvider, fullName: WinRT_String) -> win32more.Microsoft.UI.Xaml.Markup.IXamlType: ...
    @winrt_mixinmethod
    def GetXmlnsDefinitions(self: win32more.Microsoft.UI.Xaml.Markup.IXamlMetadataProvider) -> SZArray[win32more.Microsoft.UI.Xaml.Markup.XmlnsDefinition]: ...
    @winrt_classmethod
    def Initialize(cls: win32more.Microsoft.UI.Xaml.XamlTypeInfo.IXamlControlsXamlMetaDataProviderStatics) -> Void: ...
make_ready(__name__)
