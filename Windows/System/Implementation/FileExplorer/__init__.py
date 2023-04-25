from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
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
class ISysStorageProviderEventReceivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e132d1b9-7b9d-5820-97-28-42-62-b5-28-91-42')
    @winrt_commethod(6)
    def get_Json(self) -> WinRT_String: ...
    Json = property(get_Json, None)
class ISysStorageProviderEventReceivedEventArgsFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('de1a780e-e975-5f68-bc-c6-fb-46-28-1c-6a-61')
    @winrt_commethod(6)
    def CreateInstance(self, json: WinRT_String) -> Windows.System.Implementation.FileExplorer.SysStorageProviderEventReceivedEventArgs: ...
class ISysStorageProviderEventSource(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1f36c476-9546-536a-83-81-2f-9a-2c-08-ce-dd')
    @winrt_commethod(6)
    def add_EventReceived(self, handler: Windows.Foundation.TypedEventHandler[Windows.System.Implementation.FileExplorer.ISysStorageProviderEventSource, Windows.System.Implementation.FileExplorer.SysStorageProviderEventReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_EventReceived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ISysStorageProviderHandlerFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ee798431-8213-5e89-a6-23-14-d8-c7-2b-8a-61')
    @winrt_commethod(6)
    def GetHttpRequestProvider(self, syncRootId: WinRT_String) -> Windows.System.Implementation.FileExplorer.ISysStorageProviderHttpRequestProvider: ...
    @winrt_commethod(7)
    def GetEventSource(self, syncRootId: WinRT_String, eventName: WinRT_String) -> Windows.System.Implementation.FileExplorer.ISysStorageProviderEventSource: ...
class ISysStorageProviderHttpRequestProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cb6fefb6-e76a-5c25-a3-3e-3e-78-a6-e0-e0-ce')
    @winrt_commethod(6)
    def SendRequestAsync(self, request: Windows.Web.Http.HttpRequestMessage) -> Windows.Foundation.IAsyncOperation[Windows.Web.Http.HttpResponseMessage]: ...
class SysStorageProviderEventReceivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Implementation.FileExplorer.SysStorageProviderEventReceivedEventArgs'
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
