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
import Windows.ApplicationModel.Resources
import Windows.Foundation
import Windows.UI
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IResourceLoader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{08524908-16ef-45ad-a602-293637d7e61a}')
    @winrt_commethod(6)
    def GetString(self, resource: WinRT_String) -> WinRT_String: ...
class IResourceLoader2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{10eb6ec6-8138-48c1-bc65-e1f14207367c}')
    @winrt_commethod(6)
    def GetStringForUri(self, uri: Windows.Foundation.Uri) -> WinRT_String: ...
class IResourceLoaderFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c33a3603-69dc-4285-a077-d5c0e47ccbe8}')
    @winrt_commethod(6)
    def CreateResourceLoaderByName(self, name: WinRT_String) -> Windows.ApplicationModel.Resources.ResourceLoader: ...
class IResourceLoaderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{bf777ce1-19c8-49c2-953c-47e9227b334e}')
    @winrt_commethod(6)
    def GetStringForReference(self, uri: Windows.Foundation.Uri) -> WinRT_String: ...
class IResourceLoaderStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0cc04141-6466-4989-9494-0b82dfc53f1f}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_commethod(7)
    def GetForCurrentViewWithName(self, name: WinRT_String) -> Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_commethod(8)
    def GetForViewIndependentUse(self) -> Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_commethod(9)
    def GetForViewIndependentUseWithName(self, name: WinRT_String) -> Windows.ApplicationModel.Resources.ResourceLoader: ...
class IResourceLoaderStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{64609dfb-64ac-491b-8100-0e558d61c1d0}')
    @winrt_commethod(6)
    def GetForUIContext(self, context: Windows.UI.UIContext) -> Windows.ApplicationModel.Resources.ResourceLoader: ...
class IResourceLoaderStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9fb36c32-6c8c-4316-962e-909539b5c259}')
    @winrt_commethod(6)
    def GetDefaultPriPath(self, packageFullName: WinRT_String) -> WinRT_String: ...
class ResourceLoader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Resources.ResourceLoader'
    @winrt_activatemethod
    def New(cls) -> Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_factorymethod
    def CreateResourceLoaderByName(cls: Windows.ApplicationModel.Resources.IResourceLoaderFactory, name: WinRT_String) -> Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_mixinmethod
    def GetString(self: Windows.ApplicationModel.Resources.IResourceLoader, resource: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetStringForUri(self: Windows.ApplicationModel.Resources.IResourceLoader2, uri: Windows.Foundation.Uri) -> WinRT_String: ...
    @winrt_classmethod
    def GetDefaultPriPath(cls: Windows.ApplicationModel.Resources.IResourceLoaderStatics4, packageFullName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def GetForUIContext(cls: Windows.ApplicationModel.Resources.IResourceLoaderStatics3, context: Windows.UI.UIContext) -> Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.ApplicationModel.Resources.IResourceLoaderStatics2) -> Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_classmethod
    def GetForCurrentViewWithName(cls: Windows.ApplicationModel.Resources.IResourceLoaderStatics2, name: WinRT_String) -> Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_classmethod
    def GetForViewIndependentUse(cls: Windows.ApplicationModel.Resources.IResourceLoaderStatics2) -> Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_classmethod
    def GetForViewIndependentUseWithName(cls: Windows.ApplicationModel.Resources.IResourceLoaderStatics2, name: WinRT_String) -> Windows.ApplicationModel.Resources.ResourceLoader: ...
    @winrt_classmethod
    def GetStringForReference(cls: Windows.ApplicationModel.Resources.IResourceLoaderStatics, uri: Windows.Foundation.Uri) -> WinRT_String: ...
make_head(_module, 'IResourceLoader')
make_head(_module, 'IResourceLoader2')
make_head(_module, 'IResourceLoaderFactory')
make_head(_module, 'IResourceLoaderStatics')
make_head(_module, 'IResourceLoaderStatics2')
make_head(_module, 'IResourceLoaderStatics3')
make_head(_module, 'IResourceLoaderStatics4')
make_head(_module, 'ResourceLoader')
