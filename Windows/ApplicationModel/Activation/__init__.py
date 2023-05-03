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
import Windows.ApplicationModel.Activation
import Windows.ApplicationModel.Appointments.AppointmentsProvider
import Windows.ApplicationModel.Background
import Windows.ApplicationModel.Calls
import Windows.ApplicationModel.Contacts
import Windows.ApplicationModel.Contacts.Provider
import Windows.ApplicationModel.DataTransfer.ShareTarget
import Windows.ApplicationModel.Search
import Windows.ApplicationModel.UserDataAccounts.Provider
import Windows.ApplicationModel.Wallet
import Windows.Devices.Enumeration
import Windows.Devices.Printers.Extensions
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Media.SpeechRecognition
import Windows.Security.Authentication.Web
import Windows.Security.Authentication.Web.Provider
import Windows.Storage
import Windows.Storage.Pickers.Provider
import Windows.Storage.Provider
import Windows.Storage.Search
import Windows.System
import Windows.UI.Notifications
import Windows.UI.ViewManagement
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ActivatedEventsContract: UInt32 = 65536
ActivationCameraSettingsContract: UInt32 = 65536
ActivationKind = Int32
ActivationKind_Launch: ActivationKind = 0
ActivationKind_Search: ActivationKind = 1
ActivationKind_ShareTarget: ActivationKind = 2
ActivationKind_File: ActivationKind = 3
ActivationKind_Protocol: ActivationKind = 4
ActivationKind_FileOpenPicker: ActivationKind = 5
ActivationKind_FileSavePicker: ActivationKind = 6
ActivationKind_CachedFileUpdater: ActivationKind = 7
ActivationKind_ContactPicker: ActivationKind = 8
ActivationKind_Device: ActivationKind = 9
ActivationKind_PrintTaskSettings: ActivationKind = 10
ActivationKind_CameraSettings: ActivationKind = 11
ActivationKind_RestrictedLaunch: ActivationKind = 12
ActivationKind_AppointmentsProvider: ActivationKind = 13
ActivationKind_Contact: ActivationKind = 14
ActivationKind_LockScreenCall: ActivationKind = 15
ActivationKind_VoiceCommand: ActivationKind = 16
ActivationKind_LockScreen: ActivationKind = 17
ActivationKind_PickerReturned: ActivationKind = 1000
ActivationKind_WalletAction: ActivationKind = 1001
ActivationKind_PickFileContinuation: ActivationKind = 1002
ActivationKind_PickSaveFileContinuation: ActivationKind = 1003
ActivationKind_PickFolderContinuation: ActivationKind = 1004
ActivationKind_WebAuthenticationBrokerContinuation: ActivationKind = 1005
ActivationKind_WebAccountProvider: ActivationKind = 1006
ActivationKind_ComponentUI: ActivationKind = 1007
ActivationKind_ProtocolForResults: ActivationKind = 1009
ActivationKind_ToastNotification: ActivationKind = 1010
ActivationKind_Print3DWorkflow: ActivationKind = 1011
ActivationKind_DialReceiver: ActivationKind = 1012
ActivationKind_DevicePairing: ActivationKind = 1013
ActivationKind_UserDataAccountsProvider: ActivationKind = 1014
ActivationKind_FilePickerExperience: ActivationKind = 1015
ActivationKind_LockScreenComponent: ActivationKind = 1016
ActivationKind_ContactPanel: ActivationKind = 1017
ActivationKind_PrintWorkflowForegroundTask: ActivationKind = 1018
ActivationKind_GameUIProvider: ActivationKind = 1019
ActivationKind_StartupTask: ActivationKind = 1020
ActivationKind_CommandLineLaunch: ActivationKind = 1021
ActivationKind_BarcodeScannerProvider: ActivationKind = 1022
ActivationKind_PrintSupportJobUI: ActivationKind = 1023
ActivationKind_PrintSupportSettingsUI: ActivationKind = 1024
ActivationKind_PhoneCallActivation: ActivationKind = 1025
ActivationKind_VpnForeground: ActivationKind = 1026
ApplicationExecutionState = Int32
ApplicationExecutionState_NotRunning: ApplicationExecutionState = 0
ApplicationExecutionState_Running: ApplicationExecutionState = 1
ApplicationExecutionState_Suspended: ApplicationExecutionState = 2
ApplicationExecutionState_Terminated: ApplicationExecutionState = 3
ApplicationExecutionState_ClosedByUser: ApplicationExecutionState = 4
class AppointmentsProviderAddAppointmentActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.AppointmentsProviderAddAppointmentActivatedEventArgs'
    @winrt_mixinmethod
    def get_AddAppointmentOperation(self: Windows.ApplicationModel.Activation.IAppointmentsProviderAddAppointmentActivatedEventArgs) -> Windows.ApplicationModel.Appointments.AppointmentsProvider.AddAppointmentOperation: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    AddAppointmentOperation = property(get_AddAppointmentOperation, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class AppointmentsProviderRemoveAppointmentActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.AppointmentsProviderRemoveAppointmentActivatedEventArgs'
    @winrt_mixinmethod
    def get_RemoveAppointmentOperation(self: Windows.ApplicationModel.Activation.IAppointmentsProviderRemoveAppointmentActivatedEventArgs) -> Windows.ApplicationModel.Appointments.AppointmentsProvider.RemoveAppointmentOperation: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    RemoveAppointmentOperation = property(get_RemoveAppointmentOperation, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class AppointmentsProviderReplaceAppointmentActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.AppointmentsProviderReplaceAppointmentActivatedEventArgs'
    @winrt_mixinmethod
    def get_ReplaceAppointmentOperation(self: Windows.ApplicationModel.Activation.IAppointmentsProviderReplaceAppointmentActivatedEventArgs) -> Windows.ApplicationModel.Appointments.AppointmentsProvider.ReplaceAppointmentOperation: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    ReplaceAppointmentOperation = property(get_ReplaceAppointmentOperation, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class AppointmentsProviderShowAppointmentDetailsActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.AppointmentsProviderShowAppointmentDetailsActivatedEventArgs'
    @winrt_mixinmethod
    def get_InstanceStartDate(self: Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_LocalId(self: Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RoamingId(self: Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    InstanceStartDate = property(get_InstanceStartDate, None)
    LocalId = property(get_LocalId, None)
    RoamingId = property(get_RoamingId, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class AppointmentsProviderShowTimeFrameActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.AppointmentsProviderShowTimeFrameActivatedEventArgs'
    @winrt_mixinmethod
    def get_TimeToShow(self: Windows.ApplicationModel.Activation.IAppointmentsProviderShowTimeFrameActivatedEventArgs) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.ApplicationModel.Activation.IAppointmentsProviderShowTimeFrameActivatedEventArgs) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    TimeToShow = property(get_TimeToShow, None)
    Duration = property(get_Duration, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class BackgroundActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.BackgroundActivatedEventArgs'
    @winrt_mixinmethod
    def get_TaskInstance(self: Windows.ApplicationModel.Activation.IBackgroundActivatedEventArgs) -> Windows.ApplicationModel.Background.IBackgroundTaskInstance: ...
    TaskInstance = property(get_TaskInstance, None)
class BarcodeScannerPreviewActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.BarcodeScannerPreviewActivatedEventArgs'
    @winrt_mixinmethod
    def get_ConnectionId(self: Windows.ApplicationModel.Activation.IBarcodeScannerPreviewActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    ConnectionId = property(get_ConnectionId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class CachedFileUpdaterActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.CachedFileUpdaterActivatedEventArgs'
    @winrt_mixinmethod
    def get_CachedFileUpdaterUI(self: Windows.ApplicationModel.Activation.ICachedFileUpdaterActivatedEventArgs) -> Windows.Storage.Provider.CachedFileUpdaterUI: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    CachedFileUpdaterUI = property(get_CachedFileUpdaterUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class CameraSettingsActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.CameraSettingsActivatedEventArgs'
    @winrt_mixinmethod
    def get_VideoDeviceController(self: Windows.ApplicationModel.Activation.ICameraSettingsActivatedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_VideoDeviceExtension(self: Windows.ApplicationModel.Activation.ICameraSettingsActivatedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    VideoDeviceController = property(get_VideoDeviceController, None)
    VideoDeviceExtension = property(get_VideoDeviceExtension, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class CommandLineActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.CommandLineActivatedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: Windows.ApplicationModel.Activation.ICommandLineActivatedEventArgs) -> Windows.ApplicationModel.Activation.CommandLineActivationOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Operation = property(get_Operation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class CommandLineActivationOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.CommandLineActivationOperation'
    @winrt_mixinmethod
    def get_Arguments(self: Windows.ApplicationModel.Activation.ICommandLineActivationOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CurrentDirectoryPath(self: Windows.ApplicationModel.Activation.ICommandLineActivationOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ExitCode(self: Windows.ApplicationModel.Activation.ICommandLineActivationOperation, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ExitCode(self: Windows.ApplicationModel.Activation.ICommandLineActivationOperation) -> Int32: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Activation.ICommandLineActivationOperation) -> Windows.Foundation.Deferral: ...
    Arguments = property(get_Arguments, None)
    CurrentDirectoryPath = property(get_CurrentDirectoryPath, None)
    ExitCode = property(get_ExitCode, put_ExitCode)
ContactActivatedEventsContract: UInt32 = 65536
class ContactCallActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ContactCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs) -> Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    Contact = property(get_Contact, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class ContactMapActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ContactMapActivatedEventArgs'
    @winrt_mixinmethod
    def get_Address(self: Windows.ApplicationModel.Activation.IContactMapActivatedEventArgs) -> Windows.ApplicationModel.Contacts.ContactAddress: ...
    @winrt_mixinmethod
    def get_Contact(self: Windows.ApplicationModel.Activation.IContactMapActivatedEventArgs) -> Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    Address = property(get_Address, None)
    Contact = property(get_Contact, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class ContactMessageActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ContactMessageActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs) -> Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    Contact = property(get_Contact, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class ContactPanelActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ContactPanelActivatedEventArgs'
    @winrt_mixinmethod
    def get_ContactPanel(self: Windows.ApplicationModel.Activation.IContactPanelActivatedEventArgs) -> Windows.ApplicationModel.Contacts.ContactPanel: ...
    @winrt_mixinmethod
    def get_Contact(self: Windows.ApplicationModel.Activation.IContactPanelActivatedEventArgs) -> Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    ContactPanel = property(get_ContactPanel, None)
    Contact = property(get_Contact, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class ContactPickerActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ContactPickerActivatedEventArgs'
    @winrt_mixinmethod
    def get_ContactPickerUI(self: Windows.ApplicationModel.Activation.IContactPickerActivatedEventArgs) -> Windows.ApplicationModel.Contacts.Provider.ContactPickerUI: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    ContactPickerUI = property(get_ContactPickerUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class ContactPostActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ContactPostActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs) -> Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    Contact = property(get_Contact, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class ContactVideoCallActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ContactVideoCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs) -> Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    Contact = property(get_Contact, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class DeviceActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.DeviceActivatedEventArgs'
    @winrt_mixinmethod
    def get_DeviceInformationId(self: Windows.ApplicationModel.Activation.IDeviceActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IDeviceActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    DeviceInformationId = property(get_DeviceInformationId, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
    User = property(get_User, None)
class DevicePairingActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.DevicePairingActivatedEventArgs'
    @winrt_mixinmethod
    def get_DeviceInformation(self: Windows.ApplicationModel.Activation.IDevicePairingActivatedEventArgs) -> Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    DeviceInformation = property(get_DeviceInformation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class DialReceiverActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.DialReceiverActivatedEventArgs'
    @winrt_mixinmethod
    def get_AppName(self: Windows.ApplicationModel.Activation.IDialReceiverActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Arguments(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TileId(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    AppName = property(get_AppName, None)
    Arguments = property(get_Arguments, None)
    TileId = property(get_TileId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
    User = property(get_User, None)
class FileActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.FileActivatedEventArgs'
    @winrt_mixinmethod
    def get_Files(self: Windows.ApplicationModel.Activation.IFileActivatedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IFileActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_NeighboringFilesQuery(self: Windows.ApplicationModel.Activation.IFileActivatedEventArgsWithNeighboringFiles) -> Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: Windows.ApplicationModel.Activation.IFileActivatedEventArgsWithCallerPackageFamilyName) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Files = property(get_Files, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    NeighboringFilesQuery = property(get_NeighboringFilesQuery, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
    User = property(get_User, None)
class FileOpenPickerActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.FileOpenPickerActivatedEventArgs'
    @winrt_mixinmethod
    def get_FileOpenPickerUI(self: Windows.ApplicationModel.Activation.IFileOpenPickerActivatedEventArgs) -> Windows.Storage.Pickers.Provider.FileOpenPickerUI: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: Windows.ApplicationModel.Activation.IFileOpenPickerActivatedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    FileOpenPickerUI = property(get_FileOpenPickerUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    User = property(get_User, None)
class FileOpenPickerContinuationEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.FileOpenPickerContinuationEventArgs'
    @winrt_mixinmethod
    def get_Files(self: Windows.ApplicationModel.Activation.IFileOpenPickerContinuationEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Files = property(get_Files, None)
    ContinuationData = property(get_ContinuationData, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class FileSavePickerActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.FileSavePickerActivatedEventArgs'
    @winrt_mixinmethod
    def get_FileSavePickerUI(self: Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs) -> Windows.Storage.Pickers.Provider.FileSavePickerUI: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EnterpriseId(self: Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    FileSavePickerUI = property(get_FileSavePickerUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    EnterpriseId = property(get_EnterpriseId, None)
    User = property(get_User, None)
class FileSavePickerContinuationEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.FileSavePickerContinuationEventArgs'
    @winrt_mixinmethod
    def get_File(self: Windows.ApplicationModel.Activation.IFileSavePickerContinuationEventArgs) -> Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    File = property(get_File, None)
    ContinuationData = property(get_ContinuationData, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class FolderPickerContinuationEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.FolderPickerContinuationEventArgs'
    @winrt_mixinmethod
    def get_Folder(self: Windows.ApplicationModel.Activation.IFolderPickerContinuationEventArgs) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Folder = property(get_Folder, None)
    ContinuationData = property(get_ContinuationData, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class IActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('cf651713-cd08-4fd8-b6-97-a2-81-b6-54-4e-2e')
    @winrt_commethod(6)
    def get_Kind(self) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_commethod(7)
    def get_PreviousExecutionState(self) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_commethod(8)
    def get_SplashScreen(self) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class IActivatedEventArgsWithUser(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('1cf09b9e-9962-4936-80-ff-af-c8-e8-ae-5c-8c')
    @winrt_commethod(6)
    def get_User(self) -> Windows.System.User: ...
    User = property(get_User, None)
class IApplicationViewActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('930cef4b-b829-40fc-88-f4-85-13-e8-a6-47-38')
    @winrt_commethod(6)
    def get_CurrentlyShownApplicationViewId(self) -> Int32: ...
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
class IAppointmentsProviderActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3364c405-933c-4e7d-a0-34-50-0f-b8-dc-d9-f3')
    @winrt_commethod(6)
    def get_Verb(self) -> WinRT_String: ...
    Verb = property(get_Verb, None)
class IAppointmentsProviderAddAppointmentActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a2861367-cee5-4e4d-9e-d7-41-c3-4e-c1-8b-02')
    @winrt_commethod(6)
    def get_AddAppointmentOperation(self) -> Windows.ApplicationModel.Appointments.AppointmentsProvider.AddAppointmentOperation: ...
    AddAppointmentOperation = property(get_AddAppointmentOperation, None)
class IAppointmentsProviderRemoveAppointmentActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('751f3ab8-0b8e-451c-9f-15-96-6e-69-9b-ac-25')
    @winrt_commethod(6)
    def get_RemoveAppointmentOperation(self) -> Windows.ApplicationModel.Appointments.AppointmentsProvider.RemoveAppointmentOperation: ...
    RemoveAppointmentOperation = property(get_RemoveAppointmentOperation, None)
class IAppointmentsProviderReplaceAppointmentActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('1551b7d4-a981-4067-8a-62-05-24-e4-ad-e1-21')
    @winrt_commethod(6)
    def get_ReplaceAppointmentOperation(self) -> Windows.ApplicationModel.Appointments.AppointmentsProvider.ReplaceAppointmentOperation: ...
    ReplaceAppointmentOperation = property(get_ReplaceAppointmentOperation, None)
class IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3958f065-9841-4ca5-99-9b-88-51-98-b9-ef-2a')
    @winrt_commethod(6)
    def get_InstanceStartDate(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(7)
    def get_LocalId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_RoamingId(self) -> WinRT_String: ...
    InstanceStartDate = property(get_InstanceStartDate, None)
    LocalId = property(get_LocalId, None)
    RoamingId = property(get_RoamingId, None)
class IAppointmentsProviderShowTimeFrameActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9baeaba6-0e0b-49aa-ba-bc-12-b1-dc-77-49-86')
    @winrt_commethod(6)
    def get_TimeToShow(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_Duration(self) -> Windows.Foundation.TimeSpan: ...
    TimeToShow = property(get_TimeToShow, None)
    Duration = property(get_Duration, None)
class IBackgroundActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ab14bee0-e760-440e-a9-1c-44-79-6d-e3-a9-2d')
    @winrt_commethod(6)
    def get_TaskInstance(self) -> Windows.ApplicationModel.Background.IBackgroundTaskInstance: ...
    TaskInstance = property(get_TaskInstance, None)
class IBarcodeScannerPreviewActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6772797c-99bf-4349-af-22-e4-12-35-60-37-1c')
    @winrt_commethod(6)
    def get_ConnectionId(self) -> WinRT_String: ...
    ConnectionId = property(get_ConnectionId, None)
class ICachedFileUpdaterActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d06eb1c7-3805-4ecb-b7-57-6c-f1-5e-26-fe-f3')
    @winrt_commethod(6)
    def get_CachedFileUpdaterUI(self) -> Windows.Storage.Provider.CachedFileUpdaterUI: ...
    CachedFileUpdaterUI = property(get_CachedFileUpdaterUI, None)
class ICameraSettingsActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fb67a508-2dad-490a-91-70-dc-a0-36-eb-11-4b')
    @winrt_commethod(6)
    def get_VideoDeviceController(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def get_VideoDeviceExtension(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    VideoDeviceController = property(get_VideoDeviceController, None)
    VideoDeviceExtension = property(get_VideoDeviceExtension, None)
class ICommandLineActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4506472c-006a-48eb-8a-fb-d0-7a-b2-5e-33-66')
    @winrt_commethod(6)
    def get_Operation(self) -> Windows.ApplicationModel.Activation.CommandLineActivationOperation: ...
    Operation = property(get_Operation, None)
class ICommandLineActivationOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('994b2841-c59e-4f69-bc-fd-b6-1e-d4-e6-22-eb')
    @winrt_commethod(6)
    def get_Arguments(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_CurrentDirectoryPath(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_ExitCode(self, value: Int32) -> Void: ...
    @winrt_commethod(9)
    def get_ExitCode(self) -> Int32: ...
    @winrt_commethod(10)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Arguments = property(get_Arguments, None)
    CurrentDirectoryPath = property(get_CurrentDirectoryPath, None)
    ExitCode = property(get_ExitCode, put_ExitCode)
class IContactActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d627a1c4-c025-4c41-9d-ef-f1-ea-fa-d0-75-e7')
    @winrt_commethod(6)
    def get_Verb(self) -> WinRT_String: ...
    Verb = property(get_Verb, None)
class IContactCallActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c2df14c7-30eb-41c6-b3-bc-5b-16-94-f9-da-b3')
    @winrt_commethod(6)
    def get_ServiceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ServiceUserId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Contact(self) -> Windows.ApplicationModel.Contacts.Contact: ...
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    Contact = property(get_Contact, None)
class IContactMapActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b32bf870-eee7-4ad2-aa-f1-a8-7e-ff-cf-00-a4')
    @winrt_commethod(6)
    def get_Address(self) -> Windows.ApplicationModel.Contacts.ContactAddress: ...
    @winrt_commethod(7)
    def get_Contact(self) -> Windows.ApplicationModel.Contacts.Contact: ...
    Address = property(get_Address, None)
    Contact = property(get_Contact, None)
class IContactMessageActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('de598db2-0e03-43b0-bf-56-bc-c4-0b-31-62-df')
    @winrt_commethod(6)
    def get_ServiceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ServiceUserId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Contact(self) -> Windows.ApplicationModel.Contacts.Contact: ...
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    Contact = property(get_Contact, None)
class IContactPanelActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('52bb63e4-d3d4-4b63-80-51-4a-f2-08-2c-ab-80')
    @winrt_commethod(6)
    def get_ContactPanel(self) -> Windows.ApplicationModel.Contacts.ContactPanel: ...
    @winrt_commethod(7)
    def get_Contact(self) -> Windows.ApplicationModel.Contacts.Contact: ...
    ContactPanel = property(get_ContactPanel, None)
    Contact = property(get_Contact, None)
class IContactPickerActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ce57aae7-6449-45a7-97-1f-d1-13-be-7a-89-36')
    @winrt_commethod(6)
    def get_ContactPickerUI(self) -> Windows.ApplicationModel.Contacts.Provider.ContactPickerUI: ...
    ContactPickerUI = property(get_ContactPickerUI, None)
class IContactPostActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('b35a3c67-f1e7-4655-ad-6e-48-57-58-8f-55-2f')
    @winrt_commethod(6)
    def get_ServiceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ServiceUserId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Contact(self) -> Windows.ApplicationModel.Contacts.Contact: ...
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    Contact = property(get_Contact, None)
class IContactVideoCallActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('61079db8-e3e7-4b4f-85-8d-5c-63-a9-6e-f6-84')
    @winrt_commethod(6)
    def get_ServiceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ServiceUserId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Contact(self) -> Windows.ApplicationModel.Contacts.Contact: ...
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    Contact = property(get_Contact, None)
class IContactsProviderActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4580dca8-5750-4916-aa-52-c0-82-95-21-eb-94')
    @winrt_commethod(6)
    def get_Verb(self) -> WinRT_String: ...
    Verb = property(get_Verb, None)
class IContinuationActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e58106b5-155f-4a94-a7-42-c7-e0-8f-4e-18-8c')
    @winrt_commethod(6)
    def get_ContinuationData(self) -> Windows.Foundation.Collections.ValueSet: ...
    ContinuationData = property(get_ContinuationData, None)
class IDeviceActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('cd50b9a9-ce10-44d2-82-34-c3-55-a0-73-ef-33')
    @winrt_commethod(6)
    def get_DeviceInformationId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Verb(self) -> WinRT_String: ...
    DeviceInformationId = property(get_DeviceInformationId, None)
    Verb = property(get_Verb, None)
class IDevicePairingActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('eba0d1e4-ecc6-4148-94-ed-f4-b3-7e-c0-5b-3e')
    @winrt_commethod(6)
    def get_DeviceInformation(self) -> Windows.Devices.Enumeration.DeviceInformation: ...
    DeviceInformation = property(get_DeviceInformation, None)
class IDialReceiverActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fb777ed7-85ee-456e-a4-4d-85-d7-30-e7-0a-ed')
    @winrt_commethod(6)
    def get_AppName(self) -> WinRT_String: ...
    AppName = property(get_AppName, None)
class IFileActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('bb2afc33-93b1-42ed-8b-26-23-6d-d9-c7-84-96')
    @winrt_commethod(6)
    def get_Files(self) -> Windows.Foundation.Collections.IVectorView[Windows.Storage.IStorageItem]: ...
    @winrt_commethod(7)
    def get_Verb(self) -> WinRT_String: ...
    Files = property(get_Files, None)
    Verb = property(get_Verb, None)
class IFileActivatedEventArgsWithCallerPackageFamilyName(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2d60f06b-d25f-4d25-86-53-e1-c5-e1-10-83-09')
    @winrt_commethod(6)
    def get_CallerPackageFamilyName(self) -> WinRT_String: ...
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
class IFileActivatedEventArgsWithNeighboringFiles(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('433ba1a4-e1e2-48fd-b7-fc-b5-d6-ee-e6-50-33')
    @winrt_commethod(6)
    def get_NeighboringFilesQuery(self) -> Windows.Storage.Search.StorageFileQueryResult: ...
    NeighboringFilesQuery = property(get_NeighboringFilesQuery, None)
class IFileOpenPickerActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('72827082-5525-4bf2-bc-09-1f-50-95-d4-96-4d')
    @winrt_commethod(6)
    def get_FileOpenPickerUI(self) -> Windows.Storage.Pickers.Provider.FileOpenPickerUI: ...
    FileOpenPickerUI = property(get_FileOpenPickerUI, None)
class IFileOpenPickerActivatedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('5e731f66-8d1f-45fb-af-1d-73-20-5c-8f-c7-a1')
    @winrt_commethod(6)
    def get_CallerPackageFamilyName(self) -> WinRT_String: ...
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
class IFileOpenPickerContinuationEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f0fa3f3a-d4e8-4ad3-9c-34-23-08-f3-2f-ce-c9')
    @winrt_commethod(6)
    def get_Files(self) -> Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFile]: ...
    Files = property(get_Files, None)
class IFileSavePickerActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('81c19cf1-74e6-4387-82-eb-bb-8f-d6-4b-43-46')
    @winrt_commethod(6)
    def get_FileSavePickerUI(self) -> Windows.Storage.Pickers.Provider.FileSavePickerUI: ...
    FileSavePickerUI = property(get_FileSavePickerUI, None)
class IFileSavePickerActivatedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6b73fe13-2cf2-4d48-8c-bc-af-67-d2-3f-1c-e7')
    @winrt_commethod(6)
    def get_CallerPackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EnterpriseId(self) -> WinRT_String: ...
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    EnterpriseId = property(get_EnterpriseId, None)
class IFileSavePickerContinuationEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2c846fe1-3bad-4f33-8c-8b-e4-6f-ae-82-4b-4b')
    @winrt_commethod(6)
    def get_File(self) -> Windows.Storage.StorageFile: ...
    File = property(get_File, None)
class IFolderPickerContinuationEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('51882366-9f4b-498f-be-b0-42-68-4f-6e-1c-29')
    @winrt_commethod(6)
    def get_Folder(self) -> Windows.Storage.StorageFolder: ...
    Folder = property(get_Folder, None)
class ILaunchActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fbc93e26-a14a-4b4f-82-b0-33-be-d9-20-af-52')
    @winrt_commethod(6)
    def get_Arguments(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TileId(self) -> WinRT_String: ...
    Arguments = property(get_Arguments, None)
    TileId = property(get_TileId, None)
class ILaunchActivatedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0fd37ebc-9dc9-46b5-9a-ce-bd-95-d4-56-53-45')
    @winrt_commethod(6)
    def get_TileActivatedInfo(self) -> Windows.ApplicationModel.Activation.TileActivatedInfo: ...
    TileActivatedInfo = property(get_TileActivatedInfo, None)
class ILockScreenActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3ca77966-6108-4a41-82-20-ee-7d-13-3c-85-32')
    @winrt_commethod(6)
    def get_Info(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    Info = property(get_Info, None)
class ILockScreenCallActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('06f37fbe-b5f2-448b-b1-3e-e3-28-ac-1c-51-6a')
    @winrt_commethod(6)
    def get_CallUI(self) -> Windows.ApplicationModel.Calls.LockScreenCallUI: ...
    CallUI = property(get_CallUI, None)
class IPhoneCallActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('54615221-a3c1-4ced-b6-2f-8c-60-52-36-19-ad')
    @winrt_commethod(6)
    def get_LineId(self) -> Guid: ...
    LineId = property(get_LineId, None)
class IPickerReturnedActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('360defb9-a9d3-4984-a4-ed-9e-c7-34-60-49-21')
    @winrt_commethod(6)
    def get_PickerOperationId(self) -> WinRT_String: ...
    PickerOperationId = property(get_PickerOperationId, None)
class IPrelaunchActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0c44717b-19f7-48d6-b0-46-cf-22-82-6e-aa-74')
    @winrt_commethod(6)
    def get_PrelaunchActivated(self) -> Boolean: ...
    PrelaunchActivated = property(get_PrelaunchActivated, None)
class IPrint3DWorkflowActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('3f57e78b-f2ac-4619-83-02-ef-85-5e-1c-9b-90')
    @winrt_commethod(6)
    def get_Workflow(self) -> Windows.Devices.Printers.Extensions.Print3DWorkflow: ...
    Workflow = property(get_Workflow, None)
class IPrintTaskSettingsActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ee30a0c9-ce56-4865-ba-8e-89-54-ac-27-11-07')
    @winrt_commethod(6)
    def get_Configuration(self) -> Windows.Devices.Printers.Extensions.PrintTaskConfiguration: ...
    Configuration = property(get_Configuration, None)
class IProtocolActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6095f4dd-b7c0-46ab-81-fe-d9-0f-36-d0-0d-24')
    @winrt_commethod(6)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    Uri = property(get_Uri, None)
class IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d84a0c12-5c8f-438c-83-cb-c2-8f-cc-0b-2f-db')
    @winrt_commethod(6)
    def get_CallerPackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Data(self) -> Windows.Foundation.Collections.ValueSet: ...
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    Data = property(get_Data, None)
class IProtocolForResultsActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e75132c2-7ae7-4517-80-ac-db-e8-d7-cc-5b-9c')
    @winrt_commethod(6)
    def get_ProtocolForResultsOperation(self) -> Windows.System.ProtocolForResultsOperation: ...
    ProtocolForResultsOperation = property(get_ProtocolForResultsOperation, None)
class IRestrictedLaunchActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('e0b7ac81-bfc3-4344-a5-da-19-fd-5a-27-ba-ae')
    @winrt_commethod(6)
    def get_SharedContext(self) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    SharedContext = property(get_SharedContext, None)
class ISearchActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('8cb36951-58c8-43e3-94-bc-41-d3-3f-8b-63-0e')
    @winrt_commethod(6)
    def get_QueryText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Language(self) -> WinRT_String: ...
    QueryText = property(get_QueryText, None)
    Language = property(get_Language, None)
class ISearchActivatedEventArgsWithLinguisticDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c09f33da-08ab-4931-9b-7c-45-10-25-f2-1f-81')
    @winrt_commethod(6)
    def get_LinguisticDetails(self) -> Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    LinguisticDetails = property(get_LinguisticDetails, None)
class IShareTargetActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4bdaf9c8-cdb2-4acb-bf-c3-66-48-56-33-78-ec')
    @winrt_commethod(6)
    def get_ShareOperation(self) -> Windows.ApplicationModel.DataTransfer.ShareTarget.ShareOperation: ...
    ShareOperation = property(get_ShareOperation, None)
class ISplashScreen(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ca4d975c-d4d6-43f0-97-c0-08-33-c6-39-1c-24')
    @winrt_commethod(6)
    def get_ImageLocation(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def add_Dismissed(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Activation.SplashScreen, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Dismissed(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ImageLocation = property(get_ImageLocation, None)
class IStartupTaskActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('03b11a58-5276-4d91-86-21-54-61-18-64-d5-fa')
    @winrt_commethod(6)
    def get_TaskId(self) -> WinRT_String: ...
    TaskId = property(get_TaskId, None)
class ITileActivatedInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('80e4a3b1-3980-4f17-b7-38-89-19-4e-0b-8f-65')
    @winrt_commethod(6)
    def get_RecentlyShownNotifications(self) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Notifications.ShownTileNotification]: ...
    RecentlyShownNotifications = property(get_RecentlyShownNotifications, None)
class IToastNotificationActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('92a86f82-5290-431d-be-85-c4-aa-ee-b8-68-5f')
    @winrt_commethod(6)
    def get_Argument(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_UserInput(self) -> Windows.Foundation.Collections.ValueSet: ...
    Argument = property(get_Argument, None)
    UserInput = property(get_UserInput, None)
class IUserDataAccountProviderActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('1bc9f723-8ef1-4a51-a6-3a-fe-71-1e-ea-b6-07')
    @winrt_commethod(6)
    def get_Operation(self) -> Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderOperation: ...
    Operation = property(get_Operation, None)
class IViewSwitcherProvider(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('33f288a6-5c2c-4d27-ba-c7-75-36-08-8f-12-19')
    @winrt_commethod(6)
    def get_ViewSwitcher(self) -> Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    ViewSwitcher = property(get_ViewSwitcher, None)
class IVoiceCommandActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ab92dcfd-8d43-4de6-97-75-20-70-4b-58-1b-00')
    @winrt_commethod(6)
    def get_Result(self) -> Windows.Media.SpeechRecognition.SpeechRecognitionResult: ...
    Result = property(get_Result, None)
class IWalletActionActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('fcfc027b-1a1a-4d22-92-3f-ae-6f-45-fa-52-d9')
    @winrt_commethod(6)
    def get_ItemId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ActionKind(self) -> Windows.ApplicationModel.Wallet.WalletActionKind: ...
    @winrt_commethod(8)
    def get_ActionId(self) -> WinRT_String: ...
    ItemId = property(get_ItemId, None)
    ActionKind = property(get_ActionKind, None)
    ActionId = property(get_ActionId, None)
class IWebAccountProviderActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('72b71774-98ea-4ccf-97-52-46-d9-05-10-04-f1')
    @winrt_commethod(6)
    def get_Operation(self) -> Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation: ...
    Operation = property(get_Operation, None)
class IWebAuthenticationBrokerContinuationEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('75dda3d4-7714-453d-b7-ff-b9-5e-3a-17-09-da')
    @winrt_commethod(6)
    def get_WebAuthenticationResult(self) -> Windows.Security.Authentication.Web.WebAuthenticationResult: ...
    WebAuthenticationResult = property(get_WebAuthenticationResult, None)
class LaunchActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.LaunchActivatedEventArgs'
    @winrt_mixinmethod
    def get_Arguments(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TileId(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_PrelaunchActivated(self: Windows.ApplicationModel.Activation.IPrelaunchActivatedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_TileActivatedInfo(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs2) -> Windows.ApplicationModel.Activation.TileActivatedInfo: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Arguments = property(get_Arguments, None)
    TileId = property(get_TileId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    PrelaunchActivated = property(get_PrelaunchActivated, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
    TileActivatedInfo = property(get_TileActivatedInfo, None)
    User = property(get_User, None)
class LockScreenActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.LockScreenActivatedEventArgs'
    @winrt_mixinmethod
    def get_Info(self: Windows.ApplicationModel.Activation.ILockScreenActivatedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Info = property(get_Info, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class LockScreenCallActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.LockScreenCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_CallUI(self: Windows.ApplicationModel.Activation.ILockScreenCallActivatedEventArgs) -> Windows.ApplicationModel.Calls.LockScreenCallUI: ...
    @winrt_mixinmethod
    def get_Arguments(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TileId(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    CallUI = property(get_CallUI, None)
    Arguments = property(get_Arguments, None)
    TileId = property(get_TileId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
class LockScreenComponentActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.LockScreenComponentActivatedEventArgs'
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class PhoneCallActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.PhoneCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_LineId(self: Windows.ApplicationModel.Activation.IPhoneCallActivatedEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    LineId = property(get_LineId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class PickerReturnedActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.PickerReturnedActivatedEventArgs'
    @winrt_mixinmethod
    def get_PickerOperationId(self: Windows.ApplicationModel.Activation.IPickerReturnedActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    PickerOperationId = property(get_PickerOperationId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class Print3DWorkflowActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.Print3DWorkflowActivatedEventArgs'
    @winrt_mixinmethod
    def get_Workflow(self: Windows.ApplicationModel.Activation.IPrint3DWorkflowActivatedEventArgs) -> Windows.Devices.Printers.Extensions.Print3DWorkflow: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    Workflow = property(get_Workflow, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class PrintTaskSettingsActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.PrintTaskSettingsActivatedEventArgs'
    @winrt_mixinmethod
    def get_Configuration(self: Windows.ApplicationModel.Activation.IPrintTaskSettingsActivatedEventArgs) -> Windows.Devices.Printers.Extensions.PrintTaskConfiguration: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    Configuration = property(get_Configuration, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class ProtocolActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ProtocolActivatedEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Uri = property(get_Uri, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    Data = property(get_Data, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
    User = property(get_User, None)
class ProtocolForResultsActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ProtocolForResultsActivatedEventArgs'
    @winrt_mixinmethod
    def get_ProtocolForResultsOperation(self: Windows.ApplicationModel.Activation.IProtocolForResultsActivatedEventArgs) -> Windows.System.ProtocolForResultsOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    ProtocolForResultsOperation = property(get_ProtocolForResultsOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    Uri = property(get_Uri, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    Data = property(get_Data, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
    User = property(get_User, None)
class RestrictedLaunchActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.RestrictedLaunchActivatedEventArgs'
    @winrt_mixinmethod
    def get_SharedContext(self: Windows.ApplicationModel.Activation.IRestrictedLaunchActivatedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    SharedContext = property(get_SharedContext, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class SearchActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.SearchActivatedEventArgs'
    @winrt_mixinmethod
    def get_QueryText(self: Windows.ApplicationModel.Activation.ISearchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.ApplicationModel.Activation.ISearchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_LinguisticDetails(self: Windows.ApplicationModel.Activation.ISearchActivatedEventArgsWithLinguisticDetails) -> Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    QueryText = property(get_QueryText, None)
    Language = property(get_Language, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    LinguisticDetails = property(get_LinguisticDetails, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
    User = property(get_User, None)
class ShareTargetActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ShareTargetActivatedEventArgs'
    @winrt_mixinmethod
    def get_ShareOperation(self: Windows.ApplicationModel.Activation.IShareTargetActivatedEventArgs) -> Windows.ApplicationModel.DataTransfer.ShareTarget.ShareOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    ShareOperation = property(get_ShareOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class SplashScreen(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.SplashScreen'
    @winrt_mixinmethod
    def get_ImageLocation(self: Windows.ApplicationModel.Activation.ISplashScreen) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def add_Dismissed(self: Windows.ApplicationModel.Activation.ISplashScreen, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Activation.SplashScreen, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Dismissed(self: Windows.ApplicationModel.Activation.ISplashScreen, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ImageLocation = property(get_ImageLocation, None)
class StartupTaskActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.StartupTaskActivatedEventArgs'
    @winrt_mixinmethod
    def get_TaskId(self: Windows.ApplicationModel.Activation.IStartupTaskActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    TaskId = property(get_TaskId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class TileActivatedInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.TileActivatedInfo'
    @winrt_mixinmethod
    def get_RecentlyShownNotifications(self: Windows.ApplicationModel.Activation.ITileActivatedInfo) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Notifications.ShownTileNotification]: ...
    RecentlyShownNotifications = property(get_RecentlyShownNotifications, None)
class ToastNotificationActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ToastNotificationActivatedEventArgs'
    @winrt_mixinmethod
    def get_Argument(self: Windows.ApplicationModel.Activation.IToastNotificationActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserInput(self: Windows.ApplicationModel.Activation.IToastNotificationActivatedEventArgs) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    Argument = property(get_Argument, None)
    UserInput = property(get_UserInput, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
class UserDataAccountProviderActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.UserDataAccountProviderActivatedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: Windows.ApplicationModel.Activation.IUserDataAccountProviderActivatedEventArgs) -> Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    Operation = property(get_Operation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class VoiceCommandActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.VoiceCommandActivatedEventArgs'
    @winrt_mixinmethod
    def get_Result(self: Windows.ApplicationModel.Activation.IVoiceCommandActivatedEventArgs) -> Windows.Media.SpeechRecognition.SpeechRecognitionResult: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Result = property(get_Result, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WalletActionActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.WalletActionActivatedEventArgs'
    @winrt_mixinmethod
    def get_ItemId(self: Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ActionKind(self: Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs) -> Windows.ApplicationModel.Wallet.WalletActionKind: ...
    @winrt_mixinmethod
    def get_ActionId(self: Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    ItemId = property(get_ItemId, None)
    ActionKind = property(get_ActionKind, None)
    ActionId = property(get_ActionId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class WebAccountProviderActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.WebAccountProviderActivatedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: Windows.ApplicationModel.Activation.IWebAccountProviderActivatedEventArgs) -> Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Operation = property(get_Operation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebAuthenticationBrokerContinuationEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.WebAuthenticationBrokerContinuationEventArgs'
    @winrt_mixinmethod
    def get_WebAuthenticationResult(self: Windows.ApplicationModel.Activation.IWebAuthenticationBrokerContinuationEventArgs) -> Windows.Security.Authentication.Web.WebAuthenticationResult: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    WebAuthenticationResult = property(get_WebAuthenticationResult, None)
    ContinuationData = property(get_ContinuationData, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
WebUISearchActivatedEventsContract: UInt32 = 65536
make_head(_module, 'AppointmentsProviderAddAppointmentActivatedEventArgs')
make_head(_module, 'AppointmentsProviderRemoveAppointmentActivatedEventArgs')
make_head(_module, 'AppointmentsProviderReplaceAppointmentActivatedEventArgs')
make_head(_module, 'AppointmentsProviderShowAppointmentDetailsActivatedEventArgs')
make_head(_module, 'AppointmentsProviderShowTimeFrameActivatedEventArgs')
make_head(_module, 'BackgroundActivatedEventArgs')
make_head(_module, 'BarcodeScannerPreviewActivatedEventArgs')
make_head(_module, 'CachedFileUpdaterActivatedEventArgs')
make_head(_module, 'CameraSettingsActivatedEventArgs')
make_head(_module, 'CommandLineActivatedEventArgs')
make_head(_module, 'CommandLineActivationOperation')
make_head(_module, 'ContactCallActivatedEventArgs')
make_head(_module, 'ContactMapActivatedEventArgs')
make_head(_module, 'ContactMessageActivatedEventArgs')
make_head(_module, 'ContactPanelActivatedEventArgs')
make_head(_module, 'ContactPickerActivatedEventArgs')
make_head(_module, 'ContactPostActivatedEventArgs')
make_head(_module, 'ContactVideoCallActivatedEventArgs')
make_head(_module, 'DeviceActivatedEventArgs')
make_head(_module, 'DevicePairingActivatedEventArgs')
make_head(_module, 'DialReceiverActivatedEventArgs')
make_head(_module, 'FileActivatedEventArgs')
make_head(_module, 'FileOpenPickerActivatedEventArgs')
make_head(_module, 'FileOpenPickerContinuationEventArgs')
make_head(_module, 'FileSavePickerActivatedEventArgs')
make_head(_module, 'FileSavePickerContinuationEventArgs')
make_head(_module, 'FolderPickerContinuationEventArgs')
make_head(_module, 'IActivatedEventArgs')
make_head(_module, 'IActivatedEventArgsWithUser')
make_head(_module, 'IApplicationViewActivatedEventArgs')
make_head(_module, 'IAppointmentsProviderActivatedEventArgs')
make_head(_module, 'IAppointmentsProviderAddAppointmentActivatedEventArgs')
make_head(_module, 'IAppointmentsProviderRemoveAppointmentActivatedEventArgs')
make_head(_module, 'IAppointmentsProviderReplaceAppointmentActivatedEventArgs')
make_head(_module, 'IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs')
make_head(_module, 'IAppointmentsProviderShowTimeFrameActivatedEventArgs')
make_head(_module, 'IBackgroundActivatedEventArgs')
make_head(_module, 'IBarcodeScannerPreviewActivatedEventArgs')
make_head(_module, 'ICachedFileUpdaterActivatedEventArgs')
make_head(_module, 'ICameraSettingsActivatedEventArgs')
make_head(_module, 'ICommandLineActivatedEventArgs')
make_head(_module, 'ICommandLineActivationOperation')
make_head(_module, 'IContactActivatedEventArgs')
make_head(_module, 'IContactCallActivatedEventArgs')
make_head(_module, 'IContactMapActivatedEventArgs')
make_head(_module, 'IContactMessageActivatedEventArgs')
make_head(_module, 'IContactPanelActivatedEventArgs')
make_head(_module, 'IContactPickerActivatedEventArgs')
make_head(_module, 'IContactPostActivatedEventArgs')
make_head(_module, 'IContactVideoCallActivatedEventArgs')
make_head(_module, 'IContactsProviderActivatedEventArgs')
make_head(_module, 'IContinuationActivatedEventArgs')
make_head(_module, 'IDeviceActivatedEventArgs')
make_head(_module, 'IDevicePairingActivatedEventArgs')
make_head(_module, 'IDialReceiverActivatedEventArgs')
make_head(_module, 'IFileActivatedEventArgs')
make_head(_module, 'IFileActivatedEventArgsWithCallerPackageFamilyName')
make_head(_module, 'IFileActivatedEventArgsWithNeighboringFiles')
make_head(_module, 'IFileOpenPickerActivatedEventArgs')
make_head(_module, 'IFileOpenPickerActivatedEventArgs2')
make_head(_module, 'IFileOpenPickerContinuationEventArgs')
make_head(_module, 'IFileSavePickerActivatedEventArgs')
make_head(_module, 'IFileSavePickerActivatedEventArgs2')
make_head(_module, 'IFileSavePickerContinuationEventArgs')
make_head(_module, 'IFolderPickerContinuationEventArgs')
make_head(_module, 'ILaunchActivatedEventArgs')
make_head(_module, 'ILaunchActivatedEventArgs2')
make_head(_module, 'ILockScreenActivatedEventArgs')
make_head(_module, 'ILockScreenCallActivatedEventArgs')
make_head(_module, 'IPhoneCallActivatedEventArgs')
make_head(_module, 'IPickerReturnedActivatedEventArgs')
make_head(_module, 'IPrelaunchActivatedEventArgs')
make_head(_module, 'IPrint3DWorkflowActivatedEventArgs')
make_head(_module, 'IPrintTaskSettingsActivatedEventArgs')
make_head(_module, 'IProtocolActivatedEventArgs')
make_head(_module, 'IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData')
make_head(_module, 'IProtocolForResultsActivatedEventArgs')
make_head(_module, 'IRestrictedLaunchActivatedEventArgs')
make_head(_module, 'ISearchActivatedEventArgs')
make_head(_module, 'ISearchActivatedEventArgsWithLinguisticDetails')
make_head(_module, 'IShareTargetActivatedEventArgs')
make_head(_module, 'ISplashScreen')
make_head(_module, 'IStartupTaskActivatedEventArgs')
make_head(_module, 'ITileActivatedInfo')
make_head(_module, 'IToastNotificationActivatedEventArgs')
make_head(_module, 'IUserDataAccountProviderActivatedEventArgs')
make_head(_module, 'IViewSwitcherProvider')
make_head(_module, 'IVoiceCommandActivatedEventArgs')
make_head(_module, 'IWalletActionActivatedEventArgs')
make_head(_module, 'IWebAccountProviderActivatedEventArgs')
make_head(_module, 'IWebAuthenticationBrokerContinuationEventArgs')
make_head(_module, 'LaunchActivatedEventArgs')
make_head(_module, 'LockScreenActivatedEventArgs')
make_head(_module, 'LockScreenCallActivatedEventArgs')
make_head(_module, 'LockScreenComponentActivatedEventArgs')
make_head(_module, 'PhoneCallActivatedEventArgs')
make_head(_module, 'PickerReturnedActivatedEventArgs')
make_head(_module, 'Print3DWorkflowActivatedEventArgs')
make_head(_module, 'PrintTaskSettingsActivatedEventArgs')
make_head(_module, 'ProtocolActivatedEventArgs')
make_head(_module, 'ProtocolForResultsActivatedEventArgs')
make_head(_module, 'RestrictedLaunchActivatedEventArgs')
make_head(_module, 'SearchActivatedEventArgs')
make_head(_module, 'ShareTargetActivatedEventArgs')
make_head(_module, 'SplashScreen')
make_head(_module, 'StartupTaskActivatedEventArgs')
make_head(_module, 'TileActivatedInfo')
make_head(_module, 'ToastNotificationActivatedEventArgs')
make_head(_module, 'UserDataAccountProviderActivatedEventArgs')
make_head(_module, 'VoiceCommandActivatedEventArgs')
make_head(_module, 'WalletActionActivatedEventArgs')
make_head(_module, 'WebAccountProviderActivatedEventArgs')
make_head(_module, 'WebAuthenticationBrokerContinuationEventArgs')
