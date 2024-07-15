from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Resources
import win32more.Windows.Foundation
import win32more.Windows.UI
import win32more.Windows.Win32.System.WinRT
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
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Resources.ResourceLoader.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.ApplicationModel.Resources.ResourceLoader.CreateResourceLoaderByName(*args))
        else:
            raise ValueError('no matched constructor')
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
