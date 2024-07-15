from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.Activation
import win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider
import win32more.Windows.ApplicationModel.Background
import win32more.Windows.ApplicationModel.Calls
import win32more.Windows.ApplicationModel.Contacts
import win32more.Windows.ApplicationModel.Contacts.Provider
import win32more.Windows.ApplicationModel.DataTransfer.ShareTarget
import win32more.Windows.ApplicationModel.Search
import win32more.Windows.ApplicationModel.UserDataAccounts.Provider
import win32more.Windows.ApplicationModel.Wallet
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Devices.Printers.Extensions
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Media.SpeechRecognition
import win32more.Windows.Security.Authentication.Web
import win32more.Windows.Security.Authentication.Web.Provider
import win32more.Windows.Storage
import win32more.Windows.Storage.Pickers.Provider
import win32more.Windows.Storage.Provider
import win32more.Windows.Storage.Search
import win32more.Windows.System
import win32more.Windows.UI.Notifications
import win32more.Windows.UI.ViewManagement
import win32more.Windows.Win32.System.WinRT
ActivatedEventsContract: UInt32 = 65536
ActivationCameraSettingsContract: UInt32 = 65536
class ActivationKind(Enum, Int32):
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
class ApplicationExecutionState(Enum, Int32):
    NotRunning = 0
    Running = 1
    Suspended = 2
    Terminated = 3
    ClosedByUser = 4
class AppointmentsProviderAddAppointmentActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderAddAppointmentActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.AppointmentsProviderAddAppointmentActivatedEventArgs'
    @winrt_mixinmethod
    def get_AddAppointmentOperation(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderAddAppointmentActivatedEventArgs) -> win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.AddAppointmentOperation: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    AddAppointmentOperation = property(get_AddAppointmentOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    Verb = property(get_Verb, None)
class AppointmentsProviderRemoveAppointmentActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderRemoveAppointmentActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.AppointmentsProviderRemoveAppointmentActivatedEventArgs'
    @winrt_mixinmethod
    def get_RemoveAppointmentOperation(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderRemoveAppointmentActivatedEventArgs) -> win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.RemoveAppointmentOperation: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    RemoveAppointmentOperation = property(get_RemoveAppointmentOperation, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    Verb = property(get_Verb, None)
class AppointmentsProviderReplaceAppointmentActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderReplaceAppointmentActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.AppointmentsProviderReplaceAppointmentActivatedEventArgs'
    @winrt_mixinmethod
    def get_ReplaceAppointmentOperation(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderReplaceAppointmentActivatedEventArgs) -> win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.ReplaceAppointmentOperation: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    ReplaceAppointmentOperation = property(get_ReplaceAppointmentOperation, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    Verb = property(get_Verb, None)
class AppointmentsProviderShowAppointmentDetailsActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.AppointmentsProviderShowAppointmentDetailsActivatedEventArgs'
    @winrt_mixinmethod
    def get_InstanceStartDate(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_LocalId(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RoamingId(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    InstanceStartDate = property(get_InstanceStartDate, None)
    Kind = property(get_Kind, None)
    LocalId = property(get_LocalId, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    RoamingId = property(get_RoamingId, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    Verb = property(get_Verb, None)
class AppointmentsProviderShowTimeFrameActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowTimeFrameActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.AppointmentsProviderShowTimeFrameActivatedEventArgs'
    @winrt_mixinmethod
    def get_TimeToShow(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowTimeFrameActivatedEventArgs) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowTimeFrameActivatedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Duration = property(get_Duration, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    TimeToShow = property(get_TimeToShow, None)
    User = property(get_User, None)
    Verb = property(get_Verb, None)
class BackgroundActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IBackgroundActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.BackgroundActivatedEventArgs'
    @winrt_mixinmethod
    def get_TaskInstance(self: win32more.Windows.ApplicationModel.Activation.IBackgroundActivatedEventArgs) -> win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance: ...
    TaskInstance = property(get_TaskInstance, None)
class BarcodeScannerPreviewActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IBarcodeScannerPreviewActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.BarcodeScannerPreviewActivatedEventArgs'
    @winrt_mixinmethod
    def get_ConnectionId(self: win32more.Windows.ApplicationModel.Activation.IBarcodeScannerPreviewActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ConnectionId = property(get_ConnectionId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class CachedFileUpdaterActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ICachedFileUpdaterActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.CachedFileUpdaterActivatedEventArgs'
    @winrt_mixinmethod
    def get_CachedFileUpdaterUI(self: win32more.Windows.ApplicationModel.Activation.ICachedFileUpdaterActivatedEventArgs) -> win32more.Windows.Storage.Provider.CachedFileUpdaterUI: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    CachedFileUpdaterUI = property(get_CachedFileUpdaterUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class CameraSettingsActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ICameraSettingsActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.CameraSettingsActivatedEventArgs'
    @winrt_mixinmethod
    def get_VideoDeviceController(self: win32more.Windows.ApplicationModel.Activation.ICameraSettingsActivatedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_VideoDeviceExtension(self: win32more.Windows.ApplicationModel.Activation.ICameraSettingsActivatedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    VideoDeviceController = property(get_VideoDeviceController, None)
    VideoDeviceExtension = property(get_VideoDeviceExtension, None)
class CommandLineActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ICommandLineActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.CommandLineActivatedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: win32more.Windows.ApplicationModel.Activation.ICommandLineActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.CommandLineActivationOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Kind = property(get_Kind, None)
    Operation = property(get_Operation, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class CommandLineActivationOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ICommandLineActivationOperation
    _classid_ = 'Windows.ApplicationModel.Activation.CommandLineActivationOperation'
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.ApplicationModel.Activation.ICommandLineActivationOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CurrentDirectoryPath(self: win32more.Windows.ApplicationModel.Activation.ICommandLineActivationOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ExitCode(self: win32more.Windows.ApplicationModel.Activation.ICommandLineActivationOperation, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ExitCode(self: win32more.Windows.ApplicationModel.Activation.ICommandLineActivationOperation) -> Int32: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Activation.ICommandLineActivationOperation) -> win32more.Windows.Foundation.Deferral: ...
    Arguments = property(get_Arguments, None)
    CurrentDirectoryPath = property(get_CurrentDirectoryPath, None)
    ExitCode = property(get_ExitCode, put_ExitCode)
ContactActivatedEventsContract: UInt32 = 65536
class ContactCallActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.ContactCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: win32more.Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: win32more.Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    Contact = property(get_Contact, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    SplashScreen = property(get_SplashScreen, None)
    Verb = property(get_Verb, None)
class ContactMapActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactMapActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.ContactMapActivatedEventArgs'
    @winrt_mixinmethod
    def get_Address(self: win32more.Windows.ApplicationModel.Activation.IContactMapActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.ContactAddress: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Activation.IContactMapActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    Address = property(get_Address, None)
    Contact = property(get_Contact, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    Verb = property(get_Verb, None)
class ContactMessageActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.ContactMessageActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: win32more.Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: win32more.Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    Contact = property(get_Contact, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    SplashScreen = property(get_SplashScreen, None)
    Verb = property(get_Verb, None)
class ContactPanelActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactPanelActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.ContactPanelActivatedEventArgs'
    @winrt_mixinmethod
    def get_ContactPanel(self: win32more.Windows.ApplicationModel.Activation.IContactPanelActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.ContactPanel: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Activation.IContactPanelActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Contact = property(get_Contact, None)
    ContactPanel = property(get_ContactPanel, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class ContactPickerActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactPickerActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.ContactPickerActivatedEventArgs'
    @winrt_mixinmethod
    def get_ContactPickerUI(self: win32more.Windows.ApplicationModel.Activation.IContactPickerActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Provider.ContactPickerUI: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    ContactPickerUI = property(get_ContactPickerUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class ContactPostActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.ContactPostActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: win32more.Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: win32more.Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    Contact = property(get_Contact, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    SplashScreen = property(get_SplashScreen, None)
    Verb = property(get_Verb, None)
class ContactVideoCallActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.ContactVideoCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: win32more.Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: win32more.Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    Contact = property(get_Contact, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    SplashScreen = property(get_SplashScreen, None)
    Verb = property(get_Verb, None)
class DeviceActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IDeviceActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.DeviceActivatedEventArgs'
    @winrt_mixinmethod
    def get_DeviceInformationId(self: win32more.Windows.ApplicationModel.Activation.IDeviceActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IDeviceActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: win32more.Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> win32more.Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    DeviceInformationId = property(get_DeviceInformationId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    Verb = property(get_Verb, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
class DevicePairingActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IDevicePairingActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.DevicePairingActivatedEventArgs'
    @winrt_mixinmethod
    def get_DeviceInformation(self: win32more.Windows.ApplicationModel.Activation.IDevicePairingActivatedEventArgs) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    DeviceInformation = property(get_DeviceInformation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class DialReceiverActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IDialReceiverActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.DialReceiverActivatedEventArgs'
    @winrt_mixinmethod
    def get_AppName(self: win32more.Windows.ApplicationModel.Activation.IDialReceiverActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TileId(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: win32more.Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> win32more.Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    AppName = property(get_AppName, None)
    Arguments = property(get_Arguments, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    TileId = property(get_TileId, None)
    User = property(get_User, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
class FileActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IFileActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.FileActivatedEventArgs'
    @winrt_mixinmethod
    def get_Files(self: win32more.Windows.ApplicationModel.Activation.IFileActivatedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IFileActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_NeighboringFilesQuery(self: win32more.Windows.ApplicationModel.Activation.IFileActivatedEventArgsWithNeighboringFiles) -> win32more.Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: win32more.Windows.ApplicationModel.Activation.IFileActivatedEventArgsWithCallerPackageFamilyName) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: win32more.Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> win32more.Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    Files = property(get_Files, None)
    Kind = property(get_Kind, None)
    NeighboringFilesQuery = property(get_NeighboringFilesQuery, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    Verb = property(get_Verb, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
class FileOpenPickerActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IFileOpenPickerActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.FileOpenPickerActivatedEventArgs'
    @winrt_mixinmethod
    def get_FileOpenPickerUI(self: win32more.Windows.ApplicationModel.Activation.IFileOpenPickerActivatedEventArgs) -> win32more.Windows.Storage.Pickers.Provider.FileOpenPickerUI: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: win32more.Windows.ApplicationModel.Activation.IFileOpenPickerActivatedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    FileOpenPickerUI = property(get_FileOpenPickerUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class FileOpenPickerContinuationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IFileOpenPickerContinuationEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.FileOpenPickerContinuationEventArgs'
    @winrt_mixinmethod
    def get_Files(self: win32more.Windows.ApplicationModel.Activation.IFileOpenPickerContinuationEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: win32more.Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ContinuationData = property(get_ContinuationData, None)
    Files = property(get_Files, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class FileSavePickerActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.FileSavePickerActivatedEventArgs'
    @winrt_mixinmethod
    def get_FileSavePickerUI(self: win32more.Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs) -> win32more.Windows.Storage.Pickers.Provider.FileSavePickerUI: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: win32more.Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EnterpriseId(self: win32more.Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    EnterpriseId = property(get_EnterpriseId, None)
    FileSavePickerUI = property(get_FileSavePickerUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class FileSavePickerContinuationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IFileSavePickerContinuationEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.FileSavePickerContinuationEventArgs'
    @winrt_mixinmethod
    def get_File(self: win32more.Windows.ApplicationModel.Activation.IFileSavePickerContinuationEventArgs) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: win32more.Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ContinuationData = property(get_ContinuationData, None)
    File = property(get_File, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class FolderPickerContinuationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IFolderPickerContinuationEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.FolderPickerContinuationEventArgs'
    @winrt_mixinmethod
    def get_Folder(self: win32more.Windows.ApplicationModel.Activation.IFolderPickerContinuationEventArgs) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: win32more.Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ContinuationData = property(get_ContinuationData, None)
    Folder = property(get_Folder, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class IActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IActivatedEventArgs'
    _iid_ = Guid('{cf651713-cd08-4fd8-b697-a281b6544e2e}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_commethod(7)
    def get_PreviousExecutionState(self) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_commethod(8)
    def get_SplashScreen(self) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class IActivatedEventArgsWithUser(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser'
    _iid_ = Guid('{1cf09b9e-9962-4936-80ff-afc8e8ae5c8c}')
    @winrt_commethod(6)
    def get_User(self) -> win32more.Windows.System.User: ...
    User = property(get_User, None)
class IApplicationViewActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs'
    _iid_ = Guid('{930cef4b-b829-40fc-88f4-8513e8a64738}')
    @winrt_commethod(6)
    def get_CurrentlyShownApplicationViewId(self) -> Int32: ...
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
class IAppointmentsProviderActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs'
    _iid_ = Guid('{3364c405-933c-4e7d-a034-500fb8dcd9f3}')
    @winrt_commethod(6)
    def get_Verb(self) -> WinRT_String: ...
    Verb = property(get_Verb, None)
class IAppointmentsProviderAddAppointmentActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IAppointmentsProviderAddAppointmentActivatedEventArgs'
    _iid_ = Guid('{a2861367-cee5-4e4d-9ed7-41c34ec18b02}')
    @winrt_commethod(6)
    def get_AddAppointmentOperation(self) -> win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.AddAppointmentOperation: ...
    AddAppointmentOperation = property(get_AddAppointmentOperation, None)
class IAppointmentsProviderRemoveAppointmentActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IAppointmentsProviderRemoveAppointmentActivatedEventArgs'
    _iid_ = Guid('{751f3ab8-0b8e-451c-9f15-966e699bac25}')
    @winrt_commethod(6)
    def get_RemoveAppointmentOperation(self) -> win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.RemoveAppointmentOperation: ...
    RemoveAppointmentOperation = property(get_RemoveAppointmentOperation, None)
class IAppointmentsProviderReplaceAppointmentActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IAppointmentsProviderReplaceAppointmentActivatedEventArgs'
    _iid_ = Guid('{1551b7d4-a981-4067-8a62-0524e4ade121}')
    @winrt_commethod(6)
    def get_ReplaceAppointmentOperation(self) -> win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.ReplaceAppointmentOperation: ...
    ReplaceAppointmentOperation = property(get_ReplaceAppointmentOperation, None)
class IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs'
    _iid_ = Guid('{3958f065-9841-4ca5-999b-885198b9ef2a}')
    @winrt_commethod(6)
    def get_InstanceStartDate(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(7)
    def get_LocalId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_RoamingId(self) -> WinRT_String: ...
    InstanceStartDate = property(get_InstanceStartDate, None)
    LocalId = property(get_LocalId, None)
    RoamingId = property(get_RoamingId, None)
class IAppointmentsProviderShowTimeFrameActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IAppointmentsProviderShowTimeFrameActivatedEventArgs'
    _iid_ = Guid('{9baeaba6-0e0b-49aa-babc-12b1dc774986}')
    @winrt_commethod(6)
    def get_TimeToShow(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    Duration = property(get_Duration, None)
    TimeToShow = property(get_TimeToShow, None)
class IBackgroundActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IBackgroundActivatedEventArgs'
    _iid_ = Guid('{ab14bee0-e760-440e-a91c-44796de3a92d}')
    @winrt_commethod(6)
    def get_TaskInstance(self) -> win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance: ...
    TaskInstance = property(get_TaskInstance, None)
class IBarcodeScannerPreviewActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IBarcodeScannerPreviewActivatedEventArgs'
    _iid_ = Guid('{6772797c-99bf-4349-af22-e4123560371c}')
    @winrt_commethod(6)
    def get_ConnectionId(self) -> WinRT_String: ...
    ConnectionId = property(get_ConnectionId, None)
class ICachedFileUpdaterActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ICachedFileUpdaterActivatedEventArgs'
    _iid_ = Guid('{d06eb1c7-3805-4ecb-b757-6cf15e26fef3}')
    @winrt_commethod(6)
    def get_CachedFileUpdaterUI(self) -> win32more.Windows.Storage.Provider.CachedFileUpdaterUI: ...
    CachedFileUpdaterUI = property(get_CachedFileUpdaterUI, None)
class ICameraSettingsActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ICameraSettingsActivatedEventArgs'
    _iid_ = Guid('{fb67a508-2dad-490a-9170-dca036eb114b}')
    @winrt_commethod(6)
    def get_VideoDeviceController(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def get_VideoDeviceExtension(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    VideoDeviceController = property(get_VideoDeviceController, None)
    VideoDeviceExtension = property(get_VideoDeviceExtension, None)
class ICommandLineActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ICommandLineActivatedEventArgs'
    _iid_ = Guid('{4506472c-006a-48eb-8afb-d07ab25e3366}')
    @winrt_commethod(6)
    def get_Operation(self) -> win32more.Windows.ApplicationModel.Activation.CommandLineActivationOperation: ...
    Operation = property(get_Operation, None)
class ICommandLineActivationOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ICommandLineActivationOperation'
    _iid_ = Guid('{994b2841-c59e-4f69-bcfd-b61ed4e622eb}')
    @winrt_commethod(6)
    def get_Arguments(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_CurrentDirectoryPath(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_ExitCode(self, value: Int32) -> Void: ...
    @winrt_commethod(9)
    def get_ExitCode(self) -> Int32: ...
    @winrt_commethod(10)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Arguments = property(get_Arguments, None)
    CurrentDirectoryPath = property(get_CurrentDirectoryPath, None)
    ExitCode = property(get_ExitCode, put_ExitCode)
class IContactActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IContactActivatedEventArgs'
    _iid_ = Guid('{d627a1c4-c025-4c41-9def-f1eafad075e7}')
    @winrt_commethod(6)
    def get_Verb(self) -> WinRT_String: ...
    Verb = property(get_Verb, None)
class IContactCallActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs'
    _iid_ = Guid('{c2df14c7-30eb-41c6-b3bc-5b1694f9dab3}')
    @winrt_commethod(6)
    def get_ServiceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ServiceUserId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Contact(self) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    Contact = property(get_Contact, None)
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
class IContactMapActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IContactMapActivatedEventArgs'
    _iid_ = Guid('{b32bf870-eee7-4ad2-aaf1-a87effcf00a4}')
    @winrt_commethod(6)
    def get_Address(self) -> win32more.Windows.ApplicationModel.Contacts.ContactAddress: ...
    @winrt_commethod(7)
    def get_Contact(self) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    Address = property(get_Address, None)
    Contact = property(get_Contact, None)
class IContactMessageActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs'
    _iid_ = Guid('{de598db2-0e03-43b0-bf56-bcc40b3162df}')
    @winrt_commethod(6)
    def get_ServiceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ServiceUserId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Contact(self) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    Contact = property(get_Contact, None)
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
class IContactPanelActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IContactPanelActivatedEventArgs'
    _iid_ = Guid('{52bb63e4-d3d4-4b63-8051-4af2082cab80}')
    @winrt_commethod(6)
    def get_ContactPanel(self) -> win32more.Windows.ApplicationModel.Contacts.ContactPanel: ...
    @winrt_commethod(7)
    def get_Contact(self) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    Contact = property(get_Contact, None)
    ContactPanel = property(get_ContactPanel, None)
class IContactPickerActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IContactPickerActivatedEventArgs'
    _iid_ = Guid('{ce57aae7-6449-45a7-971f-d113be7a8936}')
    @winrt_commethod(6)
    def get_ContactPickerUI(self) -> win32more.Windows.ApplicationModel.Contacts.Provider.ContactPickerUI: ...
    ContactPickerUI = property(get_ContactPickerUI, None)
class IContactPostActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs'
    _iid_ = Guid('{b35a3c67-f1e7-4655-ad6e-4857588f552f}')
    @winrt_commethod(6)
    def get_ServiceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ServiceUserId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Contact(self) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    Contact = property(get_Contact, None)
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
class IContactVideoCallActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs'
    _iid_ = Guid('{61079db8-e3e7-4b4f-858d-5c63a96ef684}')
    @winrt_commethod(6)
    def get_ServiceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ServiceUserId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Contact(self) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    Contact = property(get_Contact, None)
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
class IContactsProviderActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IContactsProviderActivatedEventArgs'
    _iid_ = Guid('{4580dca8-5750-4916-aa52-c0829521eb94}')
    @winrt_commethod(6)
    def get_Verb(self) -> WinRT_String: ...
    Verb = property(get_Verb, None)
class IContinuationActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs'
    _iid_ = Guid('{e58106b5-155f-4a94-a742-c7e08f4e188c}')
    @winrt_commethod(6)
    def get_ContinuationData(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    ContinuationData = property(get_ContinuationData, None)
class IDeviceActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IDeviceActivatedEventArgs'
    _iid_ = Guid('{cd50b9a9-ce10-44d2-8234-c355a073ef33}')
    @winrt_commethod(6)
    def get_DeviceInformationId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Verb(self) -> WinRT_String: ...
    DeviceInformationId = property(get_DeviceInformationId, None)
    Verb = property(get_Verb, None)
class IDevicePairingActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IDevicePairingActivatedEventArgs'
    _iid_ = Guid('{eba0d1e4-ecc6-4148-94ed-f4b37ec05b3e}')
    @winrt_commethod(6)
    def get_DeviceInformation(self) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    DeviceInformation = property(get_DeviceInformation, None)
class IDialReceiverActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IDialReceiverActivatedEventArgs'
    _iid_ = Guid('{fb777ed7-85ee-456e-a44d-85d730e70aed}')
    @winrt_commethod(6)
    def get_AppName(self) -> WinRT_String: ...
    AppName = property(get_AppName, None)
class IFileActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IFileActivatedEventArgs'
    _iid_ = Guid('{bb2afc33-93b1-42ed-8b26-236dd9c78496}')
    @winrt_commethod(6)
    def get_Files(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]: ...
    @winrt_commethod(7)
    def get_Verb(self) -> WinRT_String: ...
    Files = property(get_Files, None)
    Verb = property(get_Verb, None)
class IFileActivatedEventArgsWithCallerPackageFamilyName(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IFileActivatedEventArgsWithCallerPackageFamilyName'
    _iid_ = Guid('{2d60f06b-d25f-4d25-8653-e1c5e1108309}')
    @winrt_commethod(6)
    def get_CallerPackageFamilyName(self) -> WinRT_String: ...
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
class IFileActivatedEventArgsWithNeighboringFiles(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IFileActivatedEventArgsWithNeighboringFiles'
    _iid_ = Guid('{433ba1a4-e1e2-48fd-b7fc-b5d6eee65033}')
    @winrt_commethod(6)
    def get_NeighboringFilesQuery(self) -> win32more.Windows.Storage.Search.StorageFileQueryResult: ...
    NeighboringFilesQuery = property(get_NeighboringFilesQuery, None)
class IFileOpenPickerActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IFileOpenPickerActivatedEventArgs'
    _iid_ = Guid('{72827082-5525-4bf2-bc09-1f5095d4964d}')
    @winrt_commethod(6)
    def get_FileOpenPickerUI(self) -> win32more.Windows.Storage.Pickers.Provider.FileOpenPickerUI: ...
    FileOpenPickerUI = property(get_FileOpenPickerUI, None)
class IFileOpenPickerActivatedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IFileOpenPickerActivatedEventArgs2'
    _iid_ = Guid('{5e731f66-8d1f-45fb-af1d-73205c8fc7a1}')
    @winrt_commethod(6)
    def get_CallerPackageFamilyName(self) -> WinRT_String: ...
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
class IFileOpenPickerContinuationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IFileOpenPickerContinuationEventArgs'
    _iid_ = Guid('{f0fa3f3a-d4e8-4ad3-9c34-2308f32fcec9}')
    @winrt_commethod(6)
    def get_Files(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]: ...
    Files = property(get_Files, None)
class IFileSavePickerActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs'
    _iid_ = Guid('{81c19cf1-74e6-4387-82eb-bb8fd64b4346}')
    @winrt_commethod(6)
    def get_FileSavePickerUI(self) -> win32more.Windows.Storage.Pickers.Provider.FileSavePickerUI: ...
    FileSavePickerUI = property(get_FileSavePickerUI, None)
class IFileSavePickerActivatedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs2'
    _iid_ = Guid('{6b73fe13-2cf2-4d48-8cbc-af67d23f1ce7}')
    @winrt_commethod(6)
    def get_CallerPackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EnterpriseId(self) -> WinRT_String: ...
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    EnterpriseId = property(get_EnterpriseId, None)
class IFileSavePickerContinuationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IFileSavePickerContinuationEventArgs'
    _iid_ = Guid('{2c846fe1-3bad-4f33-8c8b-e46fae824b4b}')
    @winrt_commethod(6)
    def get_File(self) -> win32more.Windows.Storage.StorageFile: ...
    File = property(get_File, None)
class IFolderPickerContinuationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IFolderPickerContinuationEventArgs'
    _iid_ = Guid('{51882366-9f4b-498f-beb0-42684f6e1c29}')
    @winrt_commethod(6)
    def get_Folder(self) -> win32more.Windows.Storage.StorageFolder: ...
    Folder = property(get_Folder, None)
class ILaunchActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs'
    _iid_ = Guid('{fbc93e26-a14a-4b4f-82b0-33bed920af52}')
    @winrt_commethod(6)
    def get_Arguments(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_TileId(self) -> WinRT_String: ...
    Arguments = property(get_Arguments, None)
    TileId = property(get_TileId, None)
class ILaunchActivatedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs2'
    _iid_ = Guid('{0fd37ebc-9dc9-46b5-9ace-bd95d4565345}')
    @winrt_commethod(6)
    def get_TileActivatedInfo(self) -> win32more.Windows.ApplicationModel.Activation.TileActivatedInfo: ...
    TileActivatedInfo = property(get_TileActivatedInfo, None)
class ILockScreenActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ILockScreenActivatedEventArgs'
    _iid_ = Guid('{3ca77966-6108-4a41-8220-ee7d133c8532}')
    @winrt_commethod(6)
    def get_Info(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    Info = property(get_Info, None)
class ILockScreenCallActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ILockScreenCallActivatedEventArgs'
    _iid_ = Guid('{06f37fbe-b5f2-448b-b13e-e328ac1c516a}')
    @winrt_commethod(6)
    def get_CallUI(self) -> win32more.Windows.ApplicationModel.Calls.LockScreenCallUI: ...
    CallUI = property(get_CallUI, None)
class IPhoneCallActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IPhoneCallActivatedEventArgs'
    _iid_ = Guid('{54615221-a3c1-4ced-b62f-8c60523619ad}')
    @winrt_commethod(6)
    def get_LineId(self) -> Guid: ...
    LineId = property(get_LineId, None)
class IPickerReturnedActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IPickerReturnedActivatedEventArgs'
    _iid_ = Guid('{360defb9-a9d3-4984-a4ed-9ec734604921}')
    @winrt_commethod(6)
    def get_PickerOperationId(self) -> WinRT_String: ...
    PickerOperationId = property(get_PickerOperationId, None)
class IPrelaunchActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IPrelaunchActivatedEventArgs'
    _iid_ = Guid('{0c44717b-19f7-48d6-b046-cf22826eaa74}')
    @winrt_commethod(6)
    def get_PrelaunchActivated(self) -> Boolean: ...
    PrelaunchActivated = property(get_PrelaunchActivated, None)
class IPrint3DWorkflowActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IPrint3DWorkflowActivatedEventArgs'
    _iid_ = Guid('{3f57e78b-f2ac-4619-8302-ef855e1c9b90}')
    @winrt_commethod(6)
    def get_Workflow(self) -> win32more.Windows.Devices.Printers.Extensions.Print3DWorkflow: ...
    Workflow = property(get_Workflow, None)
class IPrintTaskSettingsActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IPrintTaskSettingsActivatedEventArgs'
    _iid_ = Guid('{ee30a0c9-ce56-4865-ba8e-8954ac271107}')
    @winrt_commethod(6)
    def get_Configuration(self) -> win32more.Windows.Devices.Printers.Extensions.PrintTaskConfiguration: ...
    Configuration = property(get_Configuration, None)
class IProtocolActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IProtocolActivatedEventArgs'
    _iid_ = Guid('{6095f4dd-b7c0-46ab-81fe-d90f36d00d24}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    Uri = property(get_Uri, None)
class IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData'
    _iid_ = Guid('{d84a0c12-5c8f-438c-83cb-c28fcc0b2fdb}')
    @winrt_commethod(6)
    def get_CallerPackageFamilyName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Data(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    Data = property(get_Data, None)
class IProtocolForResultsActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IProtocolForResultsActivatedEventArgs'
    _iid_ = Guid('{e75132c2-7ae7-4517-80ac-dbe8d7cc5b9c}')
    @winrt_commethod(6)
    def get_ProtocolForResultsOperation(self) -> win32more.Windows.System.ProtocolForResultsOperation: ...
    ProtocolForResultsOperation = property(get_ProtocolForResultsOperation, None)
class IRestrictedLaunchActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IRestrictedLaunchActivatedEventArgs'
    _iid_ = Guid('{e0b7ac81-bfc3-4344-a5da-19fd5a27baae}')
    @winrt_commethod(6)
    def get_SharedContext(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    SharedContext = property(get_SharedContext, None)
class ISearchActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ISearchActivatedEventArgs'
    _iid_ = Guid('{8cb36951-58c8-43e3-94bc-41d33f8b630e}')
    @winrt_commethod(6)
    def get_QueryText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Language(self) -> WinRT_String: ...
    Language = property(get_Language, None)
    QueryText = property(get_QueryText, None)
class ISearchActivatedEventArgsWithLinguisticDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ISearchActivatedEventArgsWithLinguisticDetails'
    _iid_ = Guid('{c09f33da-08ab-4931-9b7c-451025f21f81}')
    @winrt_commethod(6)
    def get_LinguisticDetails(self) -> win32more.Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    LinguisticDetails = property(get_LinguisticDetails, None)
class IShareTargetActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IShareTargetActivatedEventArgs'
    _iid_ = Guid('{4bdaf9c8-cdb2-4acb-bfc3-6648563378ec}')
    @winrt_commethod(6)
    def get_ShareOperation(self) -> win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.ShareOperation: ...
    ShareOperation = property(get_ShareOperation, None)
class ISplashScreen(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ISplashScreen'
    _iid_ = Guid('{ca4d975c-d4d6-43f0-97c0-0833c6391c24}')
    @winrt_commethod(6)
    def get_ImageLocation(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def add_Dismissed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Activation.SplashScreen, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Dismissed(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ImageLocation = property(get_ImageLocation, None)
    Dismissed = event()
class IStartupTaskActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IStartupTaskActivatedEventArgs'
    _iid_ = Guid('{03b11a58-5276-4d91-8621-54611864d5fa}')
    @winrt_commethod(6)
    def get_TaskId(self) -> WinRT_String: ...
    TaskId = property(get_TaskId, None)
class ITileActivatedInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.ITileActivatedInfo'
    _iid_ = Guid('{80e4a3b1-3980-4f17-b738-89194e0b8f65}')
    @winrt_commethod(6)
    def get_RecentlyShownNotifications(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Notifications.ShownTileNotification]: ...
    RecentlyShownNotifications = property(get_RecentlyShownNotifications, None)
class IToastNotificationActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IToastNotificationActivatedEventArgs'
    _iid_ = Guid('{92a86f82-5290-431d-be85-c4aaeeb8685f}')
    @winrt_commethod(6)
    def get_Argument(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_UserInput(self) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    Argument = property(get_Argument, None)
    UserInput = property(get_UserInput, None)
class IUserDataAccountProviderActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IUserDataAccountProviderActivatedEventArgs'
    _iid_ = Guid('{1bc9f723-8ef1-4a51-a63a-fe711eeab607}')
    @winrt_commethod(6)
    def get_Operation(self) -> win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderOperation: ...
    Operation = property(get_Operation, None)
class IViewSwitcherProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IViewSwitcherProvider'
    _iid_ = Guid('{33f288a6-5c2c-4d27-bac7-7536088f1219}')
    @winrt_commethod(6)
    def get_ViewSwitcher(self) -> win32more.Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    ViewSwitcher = property(get_ViewSwitcher, None)
class IVoiceCommandActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IVoiceCommandActivatedEventArgs'
    _iid_ = Guid('{ab92dcfd-8d43-4de6-9775-20704b581b00}')
    @winrt_commethod(6)
    def get_Result(self) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResult: ...
    Result = property(get_Result, None)
class IWalletActionActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs'
    _iid_ = Guid('{fcfc027b-1a1a-4d22-923f-ae6f45fa52d9}')
    @winrt_commethod(6)
    def get_ItemId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ActionKind(self) -> win32more.Windows.ApplicationModel.Wallet.WalletActionKind: ...
    @winrt_commethod(8)
    def get_ActionId(self) -> WinRT_String: ...
    ActionId = property(get_ActionId, None)
    ActionKind = property(get_ActionKind, None)
    ItemId = property(get_ItemId, None)
class IWebAccountProviderActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IWebAccountProviderActivatedEventArgs'
    _iid_ = Guid('{72b71774-98ea-4ccf-9752-46d9051004f1}')
    @winrt_commethod(6)
    def get_Operation(self) -> win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation: ...
    Operation = property(get_Operation, None)
class IWebAuthenticationBrokerContinuationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Activation.IWebAuthenticationBrokerContinuationEventArgs'
    _iid_ = Guid('{75dda3d4-7714-453d-b7ff-b95e3a1709da}')
    @winrt_commethod(6)
    def get_WebAuthenticationResult(self) -> win32more.Windows.Security.Authentication.Web.WebAuthenticationResult: ...
    WebAuthenticationResult = property(get_WebAuthenticationResult, None)
class LaunchActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.LaunchActivatedEventArgs'
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TileId(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_PrelaunchActivated(self: win32more.Windows.ApplicationModel.Activation.IPrelaunchActivatedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: win32more.Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> win32more.Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_TileActivatedInfo(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs2) -> win32more.Windows.ApplicationModel.Activation.TileActivatedInfo: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Arguments = property(get_Arguments, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    Kind = property(get_Kind, None)
    PrelaunchActivated = property(get_PrelaunchActivated, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    TileActivatedInfo = property(get_TileActivatedInfo, None)
    TileId = property(get_TileId, None)
    User = property(get_User, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
class LockScreenActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ILockScreenActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.LockScreenActivatedEventArgs'
    @winrt_mixinmethod
    def get_Info(self: win32more.Windows.ApplicationModel.Activation.ILockScreenActivatedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Info = property(get_Info, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class LockScreenCallActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ILockScreenCallActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.LockScreenCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_CallUI(self: win32more.Windows.ApplicationModel.Activation.ILockScreenCallActivatedEventArgs) -> win32more.Windows.ApplicationModel.Calls.LockScreenCallUI: ...
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TileId(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: win32more.Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> win32more.Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    Arguments = property(get_Arguments, None)
    CallUI = property(get_CallUI, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    TileId = property(get_TileId, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
class LockScreenComponentActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.LockScreenComponentActivatedEventArgs'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class PhoneCallActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IPhoneCallActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.PhoneCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_LineId(self: win32more.Windows.ApplicationModel.Activation.IPhoneCallActivatedEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Kind = property(get_Kind, None)
    LineId = property(get_LineId, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class PickerReturnedActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IPickerReturnedActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.PickerReturnedActivatedEventArgs'
    @winrt_mixinmethod
    def get_PickerOperationId(self: win32more.Windows.ApplicationModel.Activation.IPickerReturnedActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    Kind = property(get_Kind, None)
    PickerOperationId = property(get_PickerOperationId, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class Print3DWorkflowActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IPrint3DWorkflowActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.Print3DWorkflowActivatedEventArgs'
    @winrt_mixinmethod
    def get_Workflow(self: win32more.Windows.ApplicationModel.Activation.IPrint3DWorkflowActivatedEventArgs) -> win32more.Windows.Devices.Printers.Extensions.Print3DWorkflow: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    Workflow = property(get_Workflow, None)
class PrintTaskSettingsActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IPrintTaskSettingsActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.PrintTaskSettingsActivatedEventArgs'
    @winrt_mixinmethod
    def get_Configuration(self: win32more.Windows.ApplicationModel.Activation.IPrintTaskSettingsActivatedEventArgs) -> win32more.Windows.Devices.Printers.Extensions.PrintTaskConfiguration: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    Configuration = property(get_Configuration, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class ProtocolActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.ProtocolActivatedEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgs) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: win32more.Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> win32more.Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    Data = property(get_Data, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    Uri = property(get_Uri, None)
    User = property(get_User, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
class ProtocolForResultsActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IProtocolForResultsActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.ProtocolForResultsActivatedEventArgs'
    @winrt_mixinmethod
    def get_ProtocolForResultsOperation(self: win32more.Windows.ApplicationModel.Activation.IProtocolForResultsActivatedEventArgs) -> win32more.Windows.System.ProtocolForResultsOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgs) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: win32more.Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> win32more.Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    Data = property(get_Data, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    ProtocolForResultsOperation = property(get_ProtocolForResultsOperation, None)
    SplashScreen = property(get_SplashScreen, None)
    Uri = property(get_Uri, None)
    User = property(get_User, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
class RestrictedLaunchActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IRestrictedLaunchActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.RestrictedLaunchActivatedEventArgs'
    @winrt_mixinmethod
    def get_SharedContext(self: win32more.Windows.ApplicationModel.Activation.IRestrictedLaunchActivatedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SharedContext = property(get_SharedContext, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class SearchActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ISearchActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.SearchActivatedEventArgs'
    @winrt_mixinmethod
    def get_QueryText(self: win32more.Windows.ApplicationModel.Activation.ISearchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.ApplicationModel.Activation.ISearchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_LinguisticDetails(self: win32more.Windows.ApplicationModel.Activation.ISearchActivatedEventArgsWithLinguisticDetails) -> win32more.Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    @winrt_mixinmethod
    def get_ViewSwitcher(self: win32more.Windows.ApplicationModel.Activation.IViewSwitcherProvider) -> win32more.Windows.UI.ViewManagement.ActivationViewSwitcher: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    Kind = property(get_Kind, None)
    Language = property(get_Language, None)
    LinguisticDetails = property(get_LinguisticDetails, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    QueryText = property(get_QueryText, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    ViewSwitcher = property(get_ViewSwitcher, None)
class ShareTargetActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IShareTargetActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.ShareTargetActivatedEventArgs'
    @winrt_mixinmethod
    def get_ShareOperation(self: win32more.Windows.ApplicationModel.Activation.IShareTargetActivatedEventArgs) -> win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.ShareOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    ShareOperation = property(get_ShareOperation, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class SplashScreen(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ISplashScreen
    _classid_ = 'Windows.ApplicationModel.Activation.SplashScreen'
    @winrt_mixinmethod
    def get_ImageLocation(self: win32more.Windows.ApplicationModel.Activation.ISplashScreen) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def add_Dismissed(self: win32more.Windows.ApplicationModel.Activation.ISplashScreen, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.ApplicationModel.Activation.SplashScreen, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Dismissed(self: win32more.Windows.ApplicationModel.Activation.ISplashScreen, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ImageLocation = property(get_ImageLocation, None)
    Dismissed = event()
class StartupTaskActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IStartupTaskActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.StartupTaskActivatedEventArgs'
    @winrt_mixinmethod
    def get_TaskId(self: win32more.Windows.ApplicationModel.Activation.IStartupTaskActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    TaskId = property(get_TaskId, None)
    User = property(get_User, None)
class TileActivatedInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ITileActivatedInfo
    _classid_ = 'Windows.ApplicationModel.Activation.TileActivatedInfo'
    @winrt_mixinmethod
    def get_RecentlyShownNotifications(self: win32more.Windows.ApplicationModel.Activation.ITileActivatedInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Notifications.ShownTileNotification]: ...
    RecentlyShownNotifications = property(get_RecentlyShownNotifications, None)
class ToastNotificationActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IToastNotificationActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.ToastNotificationActivatedEventArgs'
    @winrt_mixinmethod
    def get_Argument(self: win32more.Windows.ApplicationModel.Activation.IToastNotificationActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserInput(self: win32more.Windows.ApplicationModel.Activation.IToastNotificationActivatedEventArgs) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    Argument = property(get_Argument, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    UserInput = property(get_UserInput, None)
class UserDataAccountProviderActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IUserDataAccountProviderActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.UserDataAccountProviderActivatedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: win32more.Windows.ApplicationModel.Activation.IUserDataAccountProviderActivatedEventArgs) -> win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    Kind = property(get_Kind, None)
    Operation = property(get_Operation, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class VoiceCommandActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IVoiceCommandActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.VoiceCommandActivatedEventArgs'
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.ApplicationModel.Activation.IVoiceCommandActivatedEventArgs) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResult: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    Result = property(get_Result, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WalletActionActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.WalletActionActivatedEventArgs'
    @winrt_mixinmethod
    def get_ItemId(self: win32more.Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ActionKind(self: win32more.Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs) -> win32more.Windows.ApplicationModel.Wallet.WalletActionKind: ...
    @winrt_mixinmethod
    def get_ActionId(self: win32more.Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    ActionId = property(get_ActionId, None)
    ActionKind = property(get_ActionKind, None)
    ItemId = property(get_ItemId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class WebAccountProviderActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IWebAccountProviderActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.WebAccountProviderActivatedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: win32more.Windows.ApplicationModel.Activation.IWebAccountProviderActivatedEventArgs) -> win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    Kind = property(get_Kind, None)
    Operation = property(get_Operation, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebAuthenticationBrokerContinuationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IWebAuthenticationBrokerContinuationEventArgs
    _classid_ = 'Windows.ApplicationModel.Activation.WebAuthenticationBrokerContinuationEventArgs'
    @winrt_mixinmethod
    def get_WebAuthenticationResult(self: win32more.Windows.ApplicationModel.Activation.IWebAuthenticationBrokerContinuationEventArgs) -> win32more.Windows.Security.Authentication.Web.WebAuthenticationResult: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: win32more.Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    ContinuationData = property(get_ContinuationData, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    WebAuthenticationResult = property(get_WebAuthenticationResult, None)
WebUISearchActivatedEventsContract: UInt32 = 65536


make_ready(__name__)
