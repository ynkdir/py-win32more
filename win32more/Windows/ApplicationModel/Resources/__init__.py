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
import win32more.Windows.ApplicationModel.Resources
import win32more.Windows.Foundation
import win32more.Windows.UI
class IResourceLoader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.IResourceLoader'
    _iid_ = Guid('{08524908-16ef-45ad-a602-293637d7e61a}')
    @winrt_commethod(6)
    def GetString(self, resource: WinRT_String) -> WinRT_String: ...
class IResourceLoader2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.IResourceLoader2'
    _iid_ = Guid('{10eb6ec6-8138-48c1-bc65-e1f14207367c}')
    @winrt_commethod(6)
    def GetStringForUri(self, uri: win32more.Windows.Foundation.Uri) -> WinRT_String: ...
class IResourceLoaderFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.IResourceLoaderFactory'
    _iid_ = Guid('{c33a3603-69dc-4285-a077-d5c0e47ccbe8}')
    @winrt_commethod(6)
    def CreateResourceLoaderByName(self, name: WinRT_String) -> win32more.Windows.ApplicationModel.Resources.ResourceLoader: ...
class IResourceLoaderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.IResourceLoaderStatics'
    _iid_ = Guid('{bf777ce1-19c8-49c2-953c-47e9227b334e}')
    @winrt_commethod(6)
    def GetStringForReference(self, uri: win32more.Windows.Foundation.Uri) -> WinRT_String: ...
class IResourceLoaderStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.IResourceLoaderStatics2'
    _iid_ = Guid('{0cc04141-6466-4989-9494-0b82dfc53f1f}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_commethod(7)
    def GetForCurrentViewWithName(self, name: WinRT_String) -> win32more.Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_commethod(8)
    def GetForViewIndependentUse(self) -> win32more.Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_commethod(9)
    def GetForViewIndependentUseWithName(self, name: WinRT_String) -> win32more.Windows.ApplicationModel.Resources.ResourceLoader: ...
class IResourceLoaderStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.IResourceLoaderStatics3'
    _iid_ = Guid('{64609dfb-64ac-491b-8100-0e558d61c1d0}')
    @winrt_commethod(6)
    def GetForUIContext(self, context: win32more.Windows.UI.UIContext) -> win32more.Windows.ApplicationModel.Resources.ResourceLoader: ...
class IResourceLoaderStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.IResourceLoaderStatics4'
    _iid_ = Guid('{9fb36c32-6c8c-4316-962e-909539b5c259}')
    @winrt_commethod(6)
    def GetDefaultPriPath(self, packageFullName: WinRT_String) -> WinRT_String: ...
class ResourceLoader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Resources.IResourceLoader
    _classid_ = 'Windows.ApplicationModel.Resources.ResourceLoader'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.ApplicationModel.Resources.ResourceLoader.CreateInstance(*args)
        elif len(args) == 1:
            instance = win32more.Windows.ApplicationModel.Resources.ResourceLoader.CreateResourceLoaderByName(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_factorymethod
    def CreateResourceLoaderByName(cls: win32more.Windows.ApplicationModel.Resources.IResourceLoaderFactory, name: WinRT_String) -> win32more.Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_mixinmethod
    def GetString(self: win32more.Windows.ApplicationModel.Resources.IResourceLoader, resource: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetStringForUri(self: win32more.Windows.ApplicationModel.Resources.IResourceLoader2, uri: win32more.Windows.Foundation.Uri) -> WinRT_String: ...
    @winrt_classmethod
    def GetDefaultPriPath(cls: win32more.Windows.ApplicationModel.Resources.IResourceLoaderStatics4, packageFullName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def GetForUIContext(cls: win32more.Windows.ApplicationModel.Resources.IResourceLoaderStatics3, context: win32more.Windows.UI.UIContext) -> win32more.Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.ApplicationModel.Resources.IResourceLoaderStatics2) -> win32more.Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_classmethod
    def GetForCurrentViewWithName(cls: win32more.Windows.ApplicationModel.Resources.IResourceLoaderStatics2, name: WinRT_String) -> win32more.Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_classmethod
    def GetForViewIndependentUse(cls: win32more.Windows.ApplicationModel.Resources.IResourceLoaderStatics2) -> win32more.Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_classmethod
    def GetForViewIndependentUseWithName(cls: win32more.Windows.ApplicationModel.Resources.IResourceLoaderStatics2, name: WinRT_String) -> win32more.Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_classmethod
    def GetStringForReference(cls: win32more.Windows.ApplicationModel.Resources.IResourceLoaderStatics, uri: win32more.Windows.Foundation.Uri) -> WinRT_String: ...
make_ready(__name__)
