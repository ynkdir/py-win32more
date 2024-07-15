from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Windows.AppLifecycle
import win32more.Windows.ApplicationModel.Core
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class ActivationRegistrationManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AppLifecycle.ActivationRegistrationManager'
    @winrt_classmethod
    def RegisterForFileTypeActivation(cls: win32more.Microsoft.Windows.AppLifecycle.IActivationRegistrationManagerStatics, supportedFileTypes: PassArray[WinRT_String], logo: WinRT_String, displayName: WinRT_String, supportedVerbs: PassArray[WinRT_String], exePath: WinRT_String) -> Void: ...
    @winrt_classmethod
    def RegisterForProtocolActivation(cls: win32more.Microsoft.Windows.AppLifecycle.IActivationRegistrationManagerStatics, scheme: WinRT_String, logo: WinRT_String, displayName: WinRT_String, exePath: WinRT_String) -> Void: ...
    @winrt_classmethod
    def RegisterForStartupActivation(cls: win32more.Microsoft.Windows.AppLifecycle.IActivationRegistrationManagerStatics, taskId: WinRT_String, exePath: WinRT_String) -> Void: ...
    @winrt_classmethod
    def UnregisterForFileTypeActivation(cls: win32more.Microsoft.Windows.AppLifecycle.IActivationRegistrationManagerStatics, fileTypes: PassArray[WinRT_String], exePath: WinRT_String) -> Void: ...
    @winrt_classmethod
    def UnregisterForProtocolActivation(cls: win32more.Microsoft.Windows.AppLifecycle.IActivationRegistrationManagerStatics, scheme: WinRT_String, exePath: WinRT_String) -> Void: ...
    @winrt_classmethod
    def UnregisterForStartupActivation(cls: win32more.Microsoft.Windows.AppLifecycle.IActivationRegistrationManagerStatics, taskId: WinRT_String) -> Void: ...
class AppActivationArguments(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.AppLifecycle.IAppActivationArguments
    _classid_ = 'Microsoft.Windows.AppLifecycle.AppActivationArguments'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Microsoft.Windows.AppLifecycle.IAppActivationArguments) -> win32more.Microsoft.Windows.AppLifecycle.ExtendedActivationKind: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Microsoft.Windows.AppLifecycle.IAppActivationArguments) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    Data = property(get_Data, None)
    Kind = property(get_Kind, None)
class AppInstance(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.AppLifecycle.IAppInstance
    _classid_ = 'Microsoft.Windows.AppLifecycle.AppInstance'
    @winrt_mixinmethod
    def UnregisterKey(self: win32more.Microsoft.Windows.AppLifecycle.IAppInstance) -> Void: ...
    @winrt_mixinmethod
    def RedirectActivationToAsync(self: win32more.Microsoft.Windows.AppLifecycle.IAppInstance, args: win32more.Microsoft.Windows.AppLifecycle.AppActivationArguments) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetActivatedEventArgs(self: win32more.Microsoft.Windows.AppLifecycle.IAppInstance) -> win32more.Microsoft.Windows.AppLifecycle.AppActivationArguments: ...
    @winrt_mixinmethod
    def add_Activated(self: win32more.Microsoft.Windows.AppLifecycle.IAppInstance, handler: win32more.Windows.Foundation.EventHandler[win32more.Microsoft.Windows.AppLifecycle.AppActivationArguments]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Activated(self: win32more.Microsoft.Windows.AppLifecycle.IAppInstance, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Key(self: win32more.Microsoft.Windows.AppLifecycle.IAppInstance) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsCurrent(self: win32more.Microsoft.Windows.AppLifecycle.IAppInstance) -> Boolean: ...
    @winrt_mixinmethod
    def get_ProcessId(self: win32more.Microsoft.Windows.AppLifecycle.IAppInstance) -> UInt32: ...
    @winrt_classmethod
    def Restart(cls: win32more.Microsoft.Windows.AppLifecycle.IAppInstanceStatics2, arguments: WinRT_String) -> win32more.Windows.ApplicationModel.Core.AppRestartFailureReason: ...
    @winrt_classmethod
    def GetCurrent(cls: win32more.Microsoft.Windows.AppLifecycle.IAppInstanceStatics) -> win32more.Microsoft.Windows.AppLifecycle.AppInstance: ...
    @winrt_classmethod
    def GetInstances(cls: win32more.Microsoft.Windows.AppLifecycle.IAppInstanceStatics) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Windows.AppLifecycle.AppInstance]: ...
    @winrt_classmethod
    def FindOrRegisterForKey(cls: win32more.Microsoft.Windows.AppLifecycle.IAppInstanceStatics, key: WinRT_String) -> win32more.Microsoft.Windows.AppLifecycle.AppInstance: ...
    IsCurrent = property(get_IsCurrent, None)
    Key = property(get_Key, None)
    ProcessId = property(get_ProcessId, None)
    Activated = event()
AppLifecycleContract: UInt32 = 131072
class ExtendedActivationKind(Enum, Int32):
    Launch = 0
    Search = 1
    ShareTarget = 2
    File = 3
    Protocol = 4
    FileOpenPicker = 5
    FileSavePicker = 6
    CachedFileUpdater = 7
    ContactPicker = 8
    Device = 9
    PrintTaskSettings = 10
    CameraSettings = 11
    RestrictedLaunch = 12
    AppointmentsProvider = 13
    Contact = 14
    LockScreenCall = 15
    VoiceCommand = 16
    LockScreen = 17
    PickerReturned = 1000
    WalletAction = 1001
    PickFileContinuation = 1002
    PickSaveFileContinuation = 1003
    PickFolderContinuation = 1004
    WebAuthenticationBrokerContinuation = 1005
    WebAccountProvider = 1006
    ComponentUI = 1007
    ProtocolForResults = 1009
    ToastNotification = 1010
    Print3DWorkflow = 1011
    DialReceiver = 1012
    DevicePairing = 1013
    UserDataAccountsProvider = 1014
    FilePickerExperience = 1015
    LockScreenComponent = 1016
    ContactPanel = 1017
    PrintWorkflowForegroundTask = 1018
    GameUIProvider = 1019
    StartupTask = 1020
    CommandLineLaunch = 1021
    BarcodeScannerProvider = 1022
    PrintSupportJobUI = 1023
    PrintSupportSettingsUI = 1024
    PhoneCallActivation = 1025
    VpnForeground = 1026
    Push = 5000
    AppNotification = 5001
class IActivationRegistrationManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AppLifecycle.IActivationRegistrationManagerStatics'
    _iid_ = Guid('{5ac4e92e-017b-5d68-8198-f68636ab99d3}')
    @winrt_commethod(6)
    def RegisterForFileTypeActivation(self, supportedFileTypes: PassArray[WinRT_String], logo: WinRT_String, displayName: WinRT_String, supportedVerbs: PassArray[WinRT_String], exePath: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def RegisterForProtocolActivation(self, scheme: WinRT_String, logo: WinRT_String, displayName: WinRT_String, exePath: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def RegisterForStartupActivation(self, taskId: WinRT_String, exePath: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def UnregisterForFileTypeActivation(self, fileTypes: PassArray[WinRT_String], exePath: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def UnregisterForProtocolActivation(self, scheme: WinRT_String, exePath: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def UnregisterForStartupActivation(self, taskId: WinRT_String) -> Void: ...
class IAppActivationArguments(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AppLifecycle.IAppActivationArguments'
    _iid_ = Guid('{14f99eaf-1580-5062-bdc8-d5d1c31138fb}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Microsoft.Windows.AppLifecycle.ExtendedActivationKind: ...
    @winrt_commethod(7)
    def get_Data(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    Data = property(get_Data, None)
    Kind = property(get_Kind, None)
class IAppInstance(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AppLifecycle.IAppInstance'
    _iid_ = Guid('{75766ae4-0239-5a26-b9da-d5bfc75a4866}')
    @winrt_commethod(6)
    def UnregisterKey(self) -> Void: ...
    @winrt_commethod(7)
    def RedirectActivationToAsync(self, args: win32more.Microsoft.Windows.AppLifecycle.AppActivationArguments) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def GetActivatedEventArgs(self) -> win32more.Microsoft.Windows.AppLifecycle.AppActivationArguments: ...
    @winrt_commethod(9)
    def add_Activated(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Microsoft.Windows.AppLifecycle.AppActivationArguments]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Activated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def get_Key(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_IsCurrent(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_ProcessId(self) -> UInt32: ...
    IsCurrent = property(get_IsCurrent, None)
    Key = property(get_Key, None)
    ProcessId = property(get_ProcessId, None)
    Activated = event()
class IAppInstanceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AppLifecycle.IAppInstanceStatics'
    _iid_ = Guid('{4f414b25-8330-5a9b-bbc1-8229d479649d}')
    @winrt_commethod(6)
    def GetCurrent(self) -> win32more.Microsoft.Windows.AppLifecycle.AppInstance: ...
    @winrt_commethod(7)
    def GetInstances(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Windows.AppLifecycle.AppInstance]: ...
    @winrt_commethod(8)
    def FindOrRegisterForKey(self, key: WinRT_String) -> win32more.Microsoft.Windows.AppLifecycle.AppInstance: ...
class IAppInstanceStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AppLifecycle.IAppInstanceStatics2'
    _iid_ = Guid('{fe9f1885-7160-5397-ba9b-5890b24fdc04}')
    @winrt_commethod(6)
    def Restart(self, arguments: WinRT_String) -> win32more.Windows.ApplicationModel.Core.AppRestartFailureReason: ...


make_ready(__name__)
