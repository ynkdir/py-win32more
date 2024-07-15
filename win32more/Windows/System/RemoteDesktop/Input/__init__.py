from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.System.RemoteDesktop.Input
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class IRemoteTextConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.Input.IRemoteTextConnection'
    _iid_ = Guid('{4e7bb02a-183e-5e66-b5e4-3e6e5c570cf1}')
    @winrt_commethod(6)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def RegisterThread(self, threadId: UInt32) -> Void: ...
    @winrt_commethod(9)
    def UnregisterThread(self, threadId: UInt32) -> Void: ...
    @winrt_commethod(10)
    def ReportDataReceived(self, pduData: PassArray[Byte]) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
class IRemoteTextConnection2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.Input.IRemoteTextConnection2'
    _iid_ = Guid('{05f99345-84c8-56c5-934f-73ea00f8c2d5}')
    @winrt_commethod(6)
    def ReportPredictedKeyEvent(self, scanCode: UInt16, attributes: win32more.Windows.System.RemoteDesktop.Input.RemoteKeyEventAttributes) -> Void: ...
class IRemoteTextConnectionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.Input.IRemoteTextConnectionFactory'
    _iid_ = Guid('{88e075c2-0cae-596c-850f-78d345cd728b}')
    @winrt_commethod(6)
    def CreateInstance(self, connectionId: Guid, pduForwarder: win32more.Windows.System.RemoteDesktop.Input.RemoteTextConnectionDataHandler) -> win32more.Windows.System.RemoteDesktop.Input.RemoteTextConnection: ...
class IRemoteTextConnectionFactory2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.Input.IRemoteTextConnectionFactory2'
    _iid_ = Guid('{9425c7d9-ed9b-5d00-99cc-b0b8dc9e4c60}')
    @winrt_commethod(6)
    def CreateInstance(self, connectionId: Guid, pduForwarder: win32more.Windows.System.RemoteDesktop.Input.RemoteTextConnectionDataHandler, options: win32more.Windows.System.RemoteDesktop.Input.RemoteTextConnectionOptions) -> win32more.Windows.System.RemoteDesktop.Input.RemoteTextConnection: ...
class RemoteKeyEventAttributes(Enum, UInt32):
    None_ = 0
    KeyUp = 1
    Repeat = 2
    Extended = 4
    Extended1 = 8
class RemoteTextConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.System.RemoteDesktop.Input.IRemoteTextConnection
    _classid_ = 'Windows.System.RemoteDesktop.Input.RemoteTextConnection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.System.RemoteDesktop.Input.RemoteTextConnection.CreateInstance(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.System.RemoteDesktop.Input.RemoteTextConnection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_overload
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.System.RemoteDesktop.Input.IRemoteTextConnectionFactory, connectionId: Guid, pduForwarder: win32more.Windows.System.RemoteDesktop.Input.RemoteTextConnectionDataHandler) -> win32more.Windows.System.RemoteDesktop.Input.RemoteTextConnection: ...
    @CreateInstance.register
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.System.RemoteDesktop.Input.IRemoteTextConnectionFactory2, connectionId: Guid, pduForwarder: win32more.Windows.System.RemoteDesktop.Input.RemoteTextConnectionDataHandler, options: win32more.Windows.System.RemoteDesktop.Input.RemoteTextConnectionOptions) -> win32more.Windows.System.RemoteDesktop.Input.RemoteTextConnection: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Windows.System.RemoteDesktop.Input.IRemoteTextConnection) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Windows.System.RemoteDesktop.Input.IRemoteTextConnection, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def RegisterThread(self: win32more.Windows.System.RemoteDesktop.Input.IRemoteTextConnection, threadId: UInt32) -> Void: ...
    @winrt_mixinmethod
    def UnregisterThread(self: win32more.Windows.System.RemoteDesktop.Input.IRemoteTextConnection, threadId: UInt32) -> Void: ...
    @winrt_mixinmethod
    def ReportDataReceived(self: win32more.Windows.System.RemoteDesktop.Input.IRemoteTextConnection, pduData: PassArray[Byte]) -> Void: ...
    @winrt_mixinmethod
    def ReportPredictedKeyEvent(self: win32more.Windows.System.RemoteDesktop.Input.IRemoteTextConnection2, scanCode: UInt16, attributes: win32more.Windows.System.RemoteDesktop.Input.RemoteKeyEventAttributes) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
class RemoteTextConnectionDataHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{099ffbc8-8bcb-41b5-b056-57e77021bf1b}')
    @winrt_commethod(3)
    def Invoke(self, pduData: PassArray[Byte]) -> Boolean: ...
class RemoteTextConnectionOptions(Enum, UInt32):
    None_ = 0
    EnablePredictedKeyReporting = 1


make_ready(__name__)
