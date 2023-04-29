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
import Windows.Foundation
import Windows.System.RemoteDesktop.Input
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IRemoteTextConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4e7bb02a-183e-5e66-b5-e4-3e-6e-5c-57-0c-f1')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def RegisterThread(self, threadId: UInt32) -> Void: ...
    @winrt_commethod(9)
    def UnregisterThread(self, threadId: UInt32) -> Void: ...
    @winrt_commethod(10)
    def ReportDataReceived(self, pduData: c_char_p_no) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
class IRemoteTextConnectionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('88e075c2-0cae-596c-85-0f-78-d3-45-cd-72-8b')
    @winrt_commethod(6)
    def CreateInstance(self, connectionId: Guid, pduForwarder: Windows.System.RemoteDesktop.Input.RemoteTextConnectionDataHandler) -> Windows.System.RemoteDesktop.Input.RemoteTextConnection: ...
class RemoteTextConnection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.RemoteDesktop.Input.RemoteTextConnection'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.System.RemoteDesktop.Input.IRemoteTextConnectionFactory, connectionId: Guid, pduForwarder: Windows.System.RemoteDesktop.Input.RemoteTextConnectionDataHandler) -> Windows.System.RemoteDesktop.Input.RemoteTextConnection: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.System.RemoteDesktop.Input.IRemoteTextConnection) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: Windows.System.RemoteDesktop.Input.IRemoteTextConnection, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def RegisterThread(self: Windows.System.RemoteDesktop.Input.IRemoteTextConnection, threadId: UInt32) -> Void: ...
    @winrt_mixinmethod
    def UnregisterThread(self: Windows.System.RemoteDesktop.Input.IRemoteTextConnection, threadId: UInt32) -> Void: ...
    @winrt_mixinmethod
    def ReportDataReceived(self: Windows.System.RemoteDesktop.Input.IRemoteTextConnection, pduData: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
class RemoteTextConnectionDataHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('099ffbc8-8bcb-41b5-b0-56-57-e7-70-21-bf-1b')
    ClassId = 'Windows.System.RemoteDesktop.Input.RemoteTextConnectionDataHandler'
    @winrt_commethod(3)
    def Invoke(self, pduData: c_char_p_no) -> Boolean: ...
make_head(_module, 'IRemoteTextConnection')
make_head(_module, 'IRemoteTextConnectionFactory')
make_head(_module, 'RemoteTextConnection')
make_head(_module, 'RemoteTextConnectionDataHandler')
