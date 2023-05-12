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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.System.Implementation.FileExplorer
import Windows.Web.Http
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ISysStorageProviderEventReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Implementation.FileExplorer.ISysStorageProviderEventReceivedEventArgs'
    _iid_ = Guid('{e132d1b9-7b9d-5820-9728-4262b5289142}')
    @winrt_commethod(6)
    def get_Json(self) -> WinRT_String: ...
    Json = property(get_Json, None)
class ISysStorageProviderEventReceivedEventArgsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Implementation.FileExplorer.ISysStorageProviderEventReceivedEventArgsFactory'
    _iid_ = Guid('{de1a780e-e975-5f68-bcc6-fb46281c6a61}')
    @winrt_commethod(6)
    def CreateInstance(self, json: WinRT_String) -> Windows.System.Implementation.FileExplorer.SysStorageProviderEventReceivedEventArgs: ...
class ISysStorageProviderEventSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Implementation.FileExplorer.ISysStorageProviderEventSource'
    _iid_ = Guid('{1f36c476-9546-536a-8381-2f9a2c08cedd}')
    @winrt_commethod(6)
    def add_EventReceived(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.Implementation.FileExplorer.ISysStorageProviderEventSource, Windows.System.Implementation.FileExplorer.SysStorageProviderEventReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_EventReceived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ISysStorageProviderHandlerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Implementation.FileExplorer.ISysStorageProviderHandlerFactory'
    _iid_ = Guid('{ee798431-8213-5e89-a623-14d8c72b8a61}')
    @winrt_commethod(6)
    def GetHttpRequestProvider(self, syncRootId: WinRT_String) -> Windows.System.Implementation.FileExplorer.ISysStorageProviderHttpRequestProvider: ...
    @winrt_commethod(7)
    def GetEventSource(self, syncRootId: WinRT_String, eventName: WinRT_String) -> Windows.System.Implementation.FileExplorer.ISysStorageProviderEventSource: ...
class ISysStorageProviderHttpRequestProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Implementation.FileExplorer.ISysStorageProviderHttpRequestProvider'
    _iid_ = Guid('{cb6fefb6-e76a-5c25-a33e-3e78a6e0e0ce}')
    @winrt_commethod(6)
    def SendRequestAsync(self, request: Windows.Web.Http.HttpRequestMessage) -> Windows.Foundation.IAsyncOperation[Windows.Web.Http.HttpResponseMessage]: ...
class SysStorageProviderEventReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.System.Implementation.FileExplorer.ISysStorageProviderEventReceivedEventArgs
    _classid_ = 'Windows.System.Implementation.FileExplorer.SysStorageProviderEventReceivedEventArgs'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.System.Implementation.FileExplorer.ISysStorageProviderEventReceivedEventArgsFactory, json: WinRT_String) -> Windows.System.Implementation.FileExplorer.SysStorageProviderEventReceivedEventArgs: ...
    @winrt_mixinmethod
    def get_Json(self: Windows.System.Implementation.FileExplorer.ISysStorageProviderEventReceivedEventArgs) -> WinRT_String: ...
    Json = property(get_Json, None)
make_head(_module, 'ISysStorageProviderEventReceivedEventArgs')
make_head(_module, 'ISysStorageProviderEventReceivedEventArgsFactory')
make_head(_module, 'ISysStorageProviderEventSource')
make_head(_module, 'ISysStorageProviderHandlerFactory')
make_head(_module, 'ISysStorageProviderHttpRequestProvider')
make_head(_module, 'SysStorageProviderEventReceivedEventArgs')
