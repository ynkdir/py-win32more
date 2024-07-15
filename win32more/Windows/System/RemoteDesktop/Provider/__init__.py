from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.System.RemoteDesktop.Provider
import win32more.Windows.UI
import win32more.Windows.Win32.System.WinRT
class IPerformLocalActionRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.Provider.IPerformLocalActionRequestedEventArgs'
    _iid_ = Guid('{59359f4f-0862-53a3-a3b3-c932fb718cdc}')
    @winrt_commethod(6)
    def get_Action(self) -> win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopLocalAction: ...
    Action = property(get_Action, None)
class IRemoteDesktopConnectionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.Provider.IRemoteDesktopConnectionInfo'
    _iid_ = Guid('{68bd69d6-6dea-543b-b737-f347919f5093}')
    @winrt_commethod(6)
    def SetConnectionStatus(self, value: win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopConnectionStatus) -> Void: ...
    @winrt_commethod(7)
    def SwitchToLocalSession(self) -> Void: ...
class IRemoteDesktopConnectionInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.Provider.IRemoteDesktopConnectionInfo2'
    _iid_ = Guid('{871c0b26-23bf-5d3c-bc35-a85c405e25e6}')
    @winrt_commethod(6)
    def PerformLocalActionFromRemote(self, action: win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopLocalAction) -> Void: ...
class IRemoteDesktopConnectionInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.Provider.IRemoteDesktopConnectionInfoStatics'
    _iid_ = Guid('{4a7dc5a1-3368-5a75-bb78-807df7ebc439}')
    @winrt_commethod(6)
    def GetForLaunchUri(self, launchUri: win32more.Windows.Foundation.Uri, windowId: win32more.Windows.UI.WindowId) -> win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopConnectionInfo: ...
class IRemoteDesktopConnectionRemoteInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.Provider.IRemoteDesktopConnectionRemoteInfo'
    _iid_ = Guid('{2a3dfa7e-a7ab-547e-9a6a-4c565bbb8d71}')
    @winrt_commethod(6)
    def ReportSwitched(self) -> Void: ...
    @winrt_commethod(7)
    def add_SwitchToLocalSessionRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopConnectionRemoteInfo, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_SwitchToLocalSessionRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_PerformLocalActionRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopConnectionRemoteInfo, win32more.Windows.System.RemoteDesktop.Provider.PerformLocalActionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PerformLocalActionRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    SwitchToLocalSessionRequested = event()
    PerformLocalActionRequested = event()
class IRemoteDesktopConnectionRemoteInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.Provider.IRemoteDesktopConnectionRemoteInfoStatics'
    _iid_ = Guid('{b590e64a-e4c9-53e8-b83d-a0db3676246a}')
    @winrt_commethod(6)
    def IsSwitchSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def GetForLaunchUri(self, launchUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopConnectionRemoteInfo: ...
class IRemoteDesktopInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.Provider.IRemoteDesktopInfo'
    _iid_ = Guid('{d185bb25-2f1e-5098-b9e0-f46d6358c5c4}')
    @winrt_commethod(6)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Id(self) -> WinRT_String: ...
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
class IRemoteDesktopInfoFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.Provider.IRemoteDesktopInfoFactory'
    _iid_ = Guid('{ad0e8d58-b56f-5a8b-b419-8002ee0c5ee9}')
    @winrt_commethod(6)
    def CreateInstance(self, id: WinRT_String, displayName: WinRT_String) -> win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopInfo: ...
class IRemoteDesktopRegistrarStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.Provider.IRemoteDesktopRegistrarStatics'
    _iid_ = Guid('{687c2750-46d9-5de3-8dc3-84a9202cecfb}')
    @winrt_commethod(6)
    def get_DesktopInfos(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopInfo]: ...
    @winrt_commethod(7)
    def IsSwitchToLocalSessionEnabled(self) -> Boolean: ...
    DesktopInfos = property(get_DesktopInfos, None)
class PerformLocalActionRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteDesktop.Provider.IPerformLocalActionRequestedEventArgs
    _classid_ = 'Windows.System.RemoteDesktop.Provider.PerformLocalActionRequestedEventArgs'
    @winrt_mixinmethod
    def get_Action(self: win32more.Windows.System.RemoteDesktop.Provider.IPerformLocalActionRequestedEventArgs) -> win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopLocalAction: ...
    Action = property(get_Action, None)
class RemoteDesktopConnectionInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopConnectionInfo
    _classid_ = 'Windows.System.RemoteDesktop.Provider.RemoteDesktopConnectionInfo'
    @winrt_mixinmethod
    def SetConnectionStatus(self: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopConnectionInfo, value: win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopConnectionStatus) -> Void: ...
    @winrt_mixinmethod
    def SwitchToLocalSession(self: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopConnectionInfo) -> Void: ...
    @winrt_mixinmethod
    def PerformLocalActionFromRemote(self: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopConnectionInfo2, action: win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopLocalAction) -> Void: ...
    @winrt_classmethod
    def GetForLaunchUri(cls: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopConnectionInfoStatics, launchUri: win32more.Windows.Foundation.Uri, windowId: win32more.Windows.UI.WindowId) -> win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopConnectionInfo: ...
class RemoteDesktopConnectionRemoteInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopConnectionRemoteInfo
    _classid_ = 'Windows.System.RemoteDesktop.Provider.RemoteDesktopConnectionRemoteInfo'
    @winrt_mixinmethod
    def ReportSwitched(self: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopConnectionRemoteInfo) -> Void: ...
    @winrt_mixinmethod
    def add_SwitchToLocalSessionRequested(self: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopConnectionRemoteInfo, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopConnectionRemoteInfo, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SwitchToLocalSessionRequested(self: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopConnectionRemoteInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PerformLocalActionRequested(self: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopConnectionRemoteInfo, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopConnectionRemoteInfo, win32more.Windows.System.RemoteDesktop.Provider.PerformLocalActionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PerformLocalActionRequested(self: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopConnectionRemoteInfo, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def IsSwitchSupported(cls: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopConnectionRemoteInfoStatics) -> Boolean: ...
    @winrt_classmethod
    def GetForLaunchUri(cls: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopConnectionRemoteInfoStatics, launchUri: win32more.Windows.Foundation.Uri) -> win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopConnectionRemoteInfo: ...
    SwitchToLocalSessionRequested = event()
    PerformLocalActionRequested = event()
class RemoteDesktopConnectionStatus(Enum, Int32):
    Connecting = 0
    Connected = 1
    UserInputNeeded = 2
    Disconnected = 3
class RemoteDesktopInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopInfo
    _classid_ = 'Windows.System.RemoteDesktop.Provider.RemoteDesktopInfo'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopInfo.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopInfoFactory, id: WinRT_String, displayName: WinRT_String) -> win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopInfo: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopInfo) -> WinRT_String: ...
    DisplayName = property(get_DisplayName, None)
    Id = property(get_Id, None)
class RemoteDesktopLocalAction(Enum, Int32):
    ShowBluetoothSettings = 0
    ShowSystemSoundSettings = 1
    ShowSystemDisplaySettings = 2
    ShowSystemAccountSettings = 3
    ShowLocalSettings = 4
class _RemoteDesktopRegistrar_Meta_(ComPtr.__class__):
    pass
class RemoteDesktopRegistrar(ComPtr, metaclass=_RemoteDesktopRegistrar_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.Provider.RemoteDesktopRegistrar'
    @winrt_classmethod
    def get_DesktopInfos(cls: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopRegistrarStatics) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.System.RemoteDesktop.Provider.RemoteDesktopInfo]: ...
    @winrt_classmethod
    def IsSwitchToLocalSessionEnabled(cls: win32more.Windows.System.RemoteDesktop.Provider.IRemoteDesktopRegistrarStatics) -> Boolean: ...
    _RemoteDesktopRegistrar_Meta_.DesktopInfos = property(get_DesktopInfos, None)


make_ready(__name__)
