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
import win32more.Windows.Foundation
import win32more.Windows.System.Implementation.FileExplorer
import win32more.Windows.Web.Http
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
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 1:
            instance = win32more.Windows.System.Implementation.FileExplorer.SysStorageProviderEventReceivedEventArgs.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.System.Implementation.FileExplorer.ISysStorageProviderEventReceivedEventArgsFactory, json: WinRT_String) -> win32more.Windows.System.Implementation.FileExplorer.SysStorageProviderEventReceivedEventArgs: ...
    @winrt_mixinmethod
    def get_Json(self: win32more.Windows.System.Implementation.FileExplorer.ISysStorageProviderEventReceivedEventArgs) -> WinRT_String: ...
    Json = property(get_Json, None)
make_ready(__name__)
