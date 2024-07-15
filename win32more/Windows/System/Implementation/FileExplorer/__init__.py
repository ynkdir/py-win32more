from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.System.Implementation.FileExplorer
import win32more.Windows.Web.Http
import win32more.Windows.Win32.System.WinRT
class ISysStorageProviderEventReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Implementation.FileExplorer.ISysStorageProviderEventReceivedEventArgs'
    _iid_ = Guid('{e132d1b9-7b9d-5820-9728-4262b5289142}')
    @winrt_commethod(6)
    def get_Json(self) -> WinRT_String: ...
    Json = property(get_Json, None)
class ISysStorageProviderEventReceivedEventArgsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Implementation.FileExplorer.ISysStorageProviderEventReceivedEventArgsFactory'
    _iid_ = Guid('{de1a780e-e975-5f68-bcc6-fb46281c6a61}')
    @winrt_commethod(6)
    def CreateInstance(self, json: WinRT_String) -> win32more.Windows.System.Implementation.FileExplorer.SysStorageProviderEventReceivedEventArgs: ...
class ISysStorageProviderEventSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Implementation.FileExplorer.ISysStorageProviderEventSource'
    _iid_ = Guid('{1f36c476-9546-536a-8381-2f9a2c08cedd}')
    @winrt_commethod(6)
    def add_EventReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.Implementation.FileExplorer.ISysStorageProviderEventSource, win32more.Windows.System.Implementation.FileExplorer.SysStorageProviderEventReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_EventReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    EventReceived = event()
class ISysStorageProviderHandlerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Implementation.FileExplorer.ISysStorageProviderHandlerFactory'
    _iid_ = Guid('{ee798431-8213-5e89-a623-14d8c72b8a61}')
    @winrt_commethod(6)
    def GetHttpRequestProvider(self, syncRootId: WinRT_String) -> win32more.Windows.System.Implementation.FileExplorer.ISysStorageProviderHttpRequestProvider: ...
    @winrt_commethod(7)
    def GetEventSource(self, syncRootId: WinRT_String, eventName: WinRT_String) -> win32more.Windows.System.Implementation.FileExplorer.ISysStorageProviderEventSource: ...
class ISysStorageProviderHttpRequestProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Implementation.FileExplorer.ISysStorageProviderHttpRequestProvider'
    _iid_ = Guid('{cb6fefb6-e76a-5c25-a33e-3e78a6e0e0ce}')
    @winrt_commethod(6)
    def SendRequestAsync(self, request: win32more.Windows.Web.Http.HttpRequestMessage) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Web.Http.HttpResponseMessage]: ...
class SysStorageProviderEventReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Implementation.FileExplorer.ISysStorageProviderEventReceivedEventArgs
    _classid_ = 'Windows.System.Implementation.FileExplorer.SysStorageProviderEventReceivedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.System.Implementation.FileExplorer.SysStorageProviderEventReceivedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.System.Implementation.FileExplorer.ISysStorageProviderEventReceivedEventArgsFactory, json: WinRT_String) -> win32more.Windows.System.Implementation.FileExplorer.SysStorageProviderEventReceivedEventArgs: ...
    @winrt_mixinmethod
    def get_Json(self: win32more.Windows.System.Implementation.FileExplorer.ISysStorageProviderEventReceivedEventArgs) -> WinRT_String: ...
    Json = property(get_Json, None)


make_ready(__name__)
