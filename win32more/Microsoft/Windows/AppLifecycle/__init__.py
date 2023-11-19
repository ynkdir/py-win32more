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
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Microsoft.Windows.AppLifecycle
import win32more.Windows.ApplicationModel.Core
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
class ActivationRegistrationManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AppLifecycle.ActivationRegistrationManager'
    @winrt_classmethod
    def RegisterForFileTypeActivation(cls: win32more.Microsoft.Windows.AppLifecycle.IActivationRegistrationManagerStatics, supportedFileTypes: Annotated[SZArray[WinRT_String], 'In'], logo: WinRT_String, displayName: WinRT_String, supportedVerbs: Annotated[SZArray[WinRT_String], 'In'], exePath: WinRT_String) -> Void: ...
    @winrt_classmethod
    def RegisterForProtocolActivation(cls: win32more.Microsoft.Windows.AppLifecycle.IActivationRegistrationManagerStatics, scheme: WinRT_String, logo: WinRT_String, displayName: WinRT_String, exePath: WinRT_String) -> Void: ...
    @winrt_classmethod
    def RegisterForStartupActivation(cls: win32more.Microsoft.Windows.AppLifecycle.IActivationRegistrationManagerStatics, taskId: WinRT_String, exePath: WinRT_String) -> Void: ...
    @winrt_classmethod
    def UnregisterForFileTypeActivation(cls: win32more.Microsoft.Windows.AppLifecycle.IActivationRegistrationManagerStatics, fileTypes: Annotated[SZArray[WinRT_String], 'In'], exePath: WinRT_String) -> Void: ...
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
    Kind = property(get_Kind, None)
    Data = property(get_Data, None)
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
    Key = property(get_Key, None)
    IsCurrent = property(get_IsCurrent, None)
    ProcessId = property(get_ProcessId, None)
AppLifecycleContract: UInt32 = 131072
ExtendedActivationKind = Int32
ExtendedActivationKind_Launch: ExtendedActivationKind = 0
ExtendedActivationKind_Search: ExtendedActivationKind = 1
ExtendedActivationKind_ShareTarget: ExtendedActivationKind = 2
ExtendedActivationKind_File: ExtendedActivationKind = 3
ExtendedActivationKind_Protocol: ExtendedActivationKind = 4
ExtendedActivationKind_FileOpenPicker: ExtendedActivationKind = 5
ExtendedActivationKind_FileSavePicker: ExtendedActivationKind = 6
ExtendedActivationKind_CachedFileUpdater: ExtendedActivationKind = 7
ExtendedActivationKind_ContactPicker: ExtendedActivationKind = 8
ExtendedActivationKind_Device: ExtendedActivationKind = 9
ExtendedActivationKind_PrintTaskSettings: ExtendedActivationKind = 10
ExtendedActivationKind_CameraSettings: ExtendedActivationKind = 11
ExtendedActivationKind_RestrictedLaunch: ExtendedActivationKind = 12
ExtendedActivationKind_AppointmentsProvider: ExtendedActivationKind = 13
ExtendedActivationKind_Contact: ExtendedActivationKind = 14
ExtendedActivationKind_LockScreenCall: ExtendedActivationKind = 15
ExtendedActivationKind_VoiceCommand: ExtendedActivationKind = 16
ExtendedActivationKind_LockScreen: ExtendedActivationKind = 17
ExtendedActivationKind_PickerReturned: ExtendedActivationKind = 1000
ExtendedActivationKind_WalletAction: ExtendedActivationKind = 1001
ExtendedActivationKind_PickFileContinuation: ExtendedActivationKind = 1002
ExtendedActivationKind_PickSaveFileContinuation: ExtendedActivationKind = 1003
ExtendedActivationKind_PickFolderContinuation: ExtendedActivationKind = 1004
ExtendedActivationKind_WebAuthenticationBrokerContinuation: ExtendedActivationKind = 1005
ExtendedActivationKind_WebAccountProvider: ExtendedActivationKind = 1006
ExtendedActivationKind_ComponentUI: ExtendedActivationKind = 1007
ExtendedActivationKind_ProtocolForResults: ExtendedActivationKind = 1009
ExtendedActivationKind_ToastNotification: ExtendedActivationKind = 1010
ExtendedActivationKind_Print3DWorkflow: ExtendedActivationKind = 1011
ExtendedActivationKind_DialReceiver: ExtendedActivationKind = 1012
ExtendedActivationKind_DevicePairing: ExtendedActivationKind = 1013
ExtendedActivationKind_UserDataAccountsProvider: ExtendedActivationKind = 1014
ExtendedActivationKind_FilePickerExperience: ExtendedActivationKind = 1015
ExtendedActivationKind_LockScreenComponent: ExtendedActivationKind = 1016
ExtendedActivationKind_ContactPanel: ExtendedActivationKind = 1017
ExtendedActivationKind_PrintWorkflowForegroundTask: ExtendedActivationKind = 1018
ExtendedActivationKind_GameUIProvider: ExtendedActivationKind = 1019
ExtendedActivationKind_StartupTask: ExtendedActivationKind = 1020
ExtendedActivationKind_CommandLineLaunch: ExtendedActivationKind = 1021
ExtendedActivationKind_BarcodeScannerProvider: ExtendedActivationKind = 1022
ExtendedActivationKind_PrintSupportJobUI: ExtendedActivationKind = 1023
ExtendedActivationKind_PrintSupportSettingsUI: ExtendedActivationKind = 1024
ExtendedActivationKind_PhoneCallActivation: ExtendedActivationKind = 1025
ExtendedActivationKind_VpnForeground: ExtendedActivationKind = 1026
ExtendedActivationKind_Push: ExtendedActivationKind = 5000
ExtendedActivationKind_AppNotification: ExtendedActivationKind = 5001
class IActivationRegistrationManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.AppLifecycle.IActivationRegistrationManagerStatics'
    _iid_ = Guid('{5ac4e92e-017b-5d68-8198-f68636ab99d3}')
    @winrt_commethod(6)
    def RegisterForFileTypeActivation(self, supportedFileTypes: Annotated[SZArray[WinRT_String], 'In'], logo: WinRT_String, displayName: WinRT_String, supportedVerbs: Annotated[SZArray[WinRT_String], 'In'], exePath: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def RegisterForProtocolActivation(self, scheme: WinRT_String, logo: WinRT_String, displayName: WinRT_String, exePath: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def RegisterForStartupActivation(self, taskId: WinRT_String, exePath: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def UnregisterForFileTypeActivation(self, fileTypes: Annotated[SZArray[WinRT_String], 'In'], exePath: WinRT_String) -> Void: ...
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
    Kind = property(get_Kind, None)
    Data = property(get_Data, None)
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
    Key = property(get_Key, None)
    IsCurrent = property(get_IsCurrent, None)
    ProcessId = property(get_ProcessId, None)
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
