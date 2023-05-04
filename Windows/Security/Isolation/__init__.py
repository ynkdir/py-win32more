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
import Windows.Foundation.Collections
import Windows.Security.Isolation
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class HostMessageReceivedCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{faf26ffa-8ce1-4cc1-b278-322d31a5e4a3}')
    _classid_ = 'Windows.Security.Isolation.HostMessageReceivedCallback'
    @winrt_commethod(3)
    def Invoke(self, receiverId: Guid, message: Windows.Foundation.Collections.IVectorView[Windows.Win32.System.WinRT.IInspectable_head]) -> Void: ...
class IIsolatedWindowsEnvironment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{41d24597-c328-4467-b37f-4dfc6f60b6bc}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def StartProcessSilentlyAsync(self, hostExePath: WinRT_String, arguments: WinRT_String, activator: Windows.Security.Isolation.IsolatedWindowsEnvironmentActivator) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentStartProcessResult]: ...
    @winrt_commethod(8)
    def StartProcessSilentlyWithTelemetryAsync(self, hostExePath: WinRT_String, arguments: WinRT_String, activator: Windows.Security.Isolation.IsolatedWindowsEnvironmentActivator, telemetryParameters: Windows.Security.Isolation.IsolatedWindowsEnvironmentTelemetryParameters) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentStartProcessResult]: ...
    @winrt_commethod(9)
    def ShareFolderAsync(self, hostFolder: WinRT_String, requestOptions: Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFolderRequestOptions) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFolderResult]: ...
    @winrt_commethod(10)
    def ShareFolderWithTelemetryAsync(self, hostFolder: WinRT_String, requestOptions: Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFolderRequestOptions, telemetryParameters: Windows.Security.Isolation.IsolatedWindowsEnvironmentTelemetryParameters) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFolderResult]: ...
    @winrt_commethod(11)
    def LaunchFileWithUIAsync(self, appExePath: WinRT_String, argumentsTemplate: WinRT_String, filePath: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentLaunchFileResult]: ...
    @winrt_commethod(12)
    def LaunchFileWithUIAndTelemetryAsync(self, appExePath: WinRT_String, argumentsTemplate: WinRT_String, filePath: WinRT_String, telemetryParameters: Windows.Security.Isolation.IsolatedWindowsEnvironmentTelemetryParameters) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentLaunchFileResult]: ...
    @winrt_commethod(13)
    def TerminateAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def TerminateWithTelemetryAsync(self, telemetryParameters: Windows.Security.Isolation.IsolatedWindowsEnvironmentTelemetryParameters) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(15)
    def RegisterMessageReceiver(self, receiverId: Guid, messageReceivedCallback: Windows.Security.Isolation.MessageReceivedCallback) -> Void: ...
    @winrt_commethod(16)
    def UnregisterMessageReceiver(self, receiverId: Guid) -> Void: ...
    Id = property(get_Id, None)
class IIsolatedWindowsEnvironment2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2d365f39-88bd-4ab4-93cf-7e2bcef337c0}')
    @winrt_commethod(6)
    def PostMessageToReceiverAsync(self, receiverId: Guid, message: Windows.Foundation.Collections.IIterable[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentPostMessageResult]: ...
    @winrt_commethod(7)
    def PostMessageToReceiverWithTelemetryAsync(self, receiverId: Guid, message: Windows.Foundation.Collections.IIterable[Windows.Win32.System.WinRT.IInspectable_head], telemetryParameters: Windows.Security.Isolation.IsolatedWindowsEnvironmentTelemetryParameters) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentPostMessageResult]: ...
class IIsolatedWindowsEnvironment3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{cb7fc7d2-d06e-4c26-8ada-dacdaaad03f5}')
    @winrt_commethod(6)
    def GetUserInfo(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentUserInfo: ...
    @winrt_commethod(7)
    def ShareFileAsync(self, filePath: WinRT_String, options: Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFileRequestOptions) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFileResult]: ...
    @winrt_commethod(8)
    def ShareFileWithTelemetryAsync(self, filePath: WinRT_String, options: Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFileRequestOptions, telemetryParameters: Windows.Security.Isolation.IsolatedWindowsEnvironmentTelemetryParameters) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFileResult]: ...
class IIsolatedWindowsEnvironment4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{11e3701a-dd9e-4f1b-812c-4020f307f93c}')
    @winrt_commethod(6)
    def ChangePriority(self, Priority: Windows.Security.Isolation.IsolatedWindowsEnvironmentCreationPriority) -> Void: ...
class IIsolatedWindowsEnvironmentCreateResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ef9a5e58-dcd7-45c2-9c85-ab642a715e8e}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentCreateStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_Environment(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironment: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
    Environment = property(get_Environment, None)
class IIsolatedWindowsEnvironmentCreateResult2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a547dbc7-61d4-4fb8-ab5c-edefa3d388ad}')
    @winrt_commethod(6)
    def ChangeCreationPriority(self, priority: Windows.Security.Isolation.IsolatedWindowsEnvironmentCreationPriority) -> Void: ...
class IIsolatedWindowsEnvironmentFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1aca93e7-e804-454d-8466-f9897c20b0f6}')
    @winrt_commethod(6)
    def CreateAsync(self, options: Windows.Security.Isolation.IsolatedWindowsEnvironmentOptions) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Security.Isolation.IsolatedWindowsEnvironmentCreateResult, Windows.Security.Isolation.IsolatedWindowsEnvironmentCreateProgress]: ...
    @winrt_commethod(7)
    def CreateWithTelemetryAsync(self, options: Windows.Security.Isolation.IsolatedWindowsEnvironmentOptions, telemetryParameters: Windows.Security.Isolation.IsolatedWindowsEnvironmentTelemetryParameters) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Security.Isolation.IsolatedWindowsEnvironmentCreateResult, Windows.Security.Isolation.IsolatedWindowsEnvironmentCreateProgress]: ...
    @winrt_commethod(8)
    def GetById(self, environmentId: WinRT_String) -> Windows.Security.Isolation.IsolatedWindowsEnvironment: ...
    @winrt_commethod(9)
    def FindByOwnerId(self, environmentOwnerId: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Isolation.IsolatedWindowsEnvironment]: ...
class IIsolatedWindowsEnvironmentFile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4d5ae1ef-029f-4101-8c35-fe91bf9cd5f0}')
    @winrt_commethod(6)
    def get_Id(self) -> Guid: ...
    @winrt_commethod(7)
    def get_HostPath(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def Close(self) -> Void: ...
    Id = property(get_Id, None)
    HostPath = property(get_HostPath, None)
class IIsolatedWindowsEnvironmentFile2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4eeb8dec-ad5d-4b0a-b754-f36c3d46d684}')
    @winrt_commethod(6)
    def get_GuestPath(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsReadOnly(self) -> Boolean: ...
    GuestPath = property(get_GuestPath, None)
    IsReadOnly = property(get_IsReadOnly, None)
class IIsolatedWindowsEnvironmentHostStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2c0e22c7-05a0-517a-b81c-6ee8790c381f}')
    @winrt_commethod(6)
    def get_IsReady(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_HostErrors(self) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Isolation.IsolatedWindowsEnvironmentHostError]: ...
    IsReady = property(get_IsReady, None)
    HostErrors = property(get_HostErrors, None)
class IIsolatedWindowsEnvironmentLaunchFileResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{685d4176-f6e0-4569-b1aa-215c0ff5b257}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentLaunchFileStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_File(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentFile: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
    File = property(get_File, None)
class IIsolatedWindowsEnvironmentOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b71d98f7-61f0-4008-b207-0bf9eb2d76f2}')
    @winrt_commethod(6)
    def get_EnvironmentOwnerId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_EnvironmentOwnerId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_AllowedClipboardFormats(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentAllowedClipboardFormats: ...
    @winrt_commethod(9)
    def put_AllowedClipboardFormats(self, value: Windows.Security.Isolation.IsolatedWindowsEnvironmentAllowedClipboardFormats) -> Void: ...
    @winrt_commethod(10)
    def get_ClipboardCopyPasteDirections(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentClipboardCopyPasteDirections: ...
    @winrt_commethod(11)
    def put_ClipboardCopyPasteDirections(self, value: Windows.Security.Isolation.IsolatedWindowsEnvironmentClipboardCopyPasteDirections) -> Void: ...
    @winrt_commethod(12)
    def get_AvailablePrinters(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentAvailablePrinters: ...
    @winrt_commethod(13)
    def put_AvailablePrinters(self, value: Windows.Security.Isolation.IsolatedWindowsEnvironmentAvailablePrinters) -> Void: ...
    @winrt_commethod(14)
    def get_SharedHostFolderPath(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_SharedFolderNameInEnvironment(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def ShareHostFolderForUntrustedItems(self, SharedHostFolderPath: WinRT_String, ShareFolderNameInEnvironment: WinRT_String) -> Void: ...
    @winrt_commethod(17)
    def get_PersistUserProfile(self) -> Boolean: ...
    @winrt_commethod(18)
    def put_PersistUserProfile(self, value: Boolean) -> Void: ...
    @winrt_commethod(19)
    def get_AllowGraphicsHardwareAcceleration(self) -> Boolean: ...
    @winrt_commethod(20)
    def put_AllowGraphicsHardwareAcceleration(self, value: Boolean) -> Void: ...
    @winrt_commethod(21)
    def get_AllowCameraAndMicrophoneAccess(self) -> Boolean: ...
    @winrt_commethod(22)
    def put_AllowCameraAndMicrophoneAccess(self, value: Boolean) -> Void: ...
    EnvironmentOwnerId = property(get_EnvironmentOwnerId, put_EnvironmentOwnerId)
    AllowedClipboardFormats = property(get_AllowedClipboardFormats, put_AllowedClipboardFormats)
    ClipboardCopyPasteDirections = property(get_ClipboardCopyPasteDirections, put_ClipboardCopyPasteDirections)
    AvailablePrinters = property(get_AvailablePrinters, put_AvailablePrinters)
    SharedHostFolderPath = property(get_SharedHostFolderPath, None)
    SharedFolderNameInEnvironment = property(get_SharedFolderNameInEnvironment, None)
    PersistUserProfile = property(get_PersistUserProfile, put_PersistUserProfile)
    AllowGraphicsHardwareAcceleration = property(get_AllowGraphicsHardwareAcceleration, put_AllowGraphicsHardwareAcceleration)
    AllowCameraAndMicrophoneAccess = property(get_AllowCameraAndMicrophoneAccess, put_AllowCameraAndMicrophoneAccess)
class IIsolatedWindowsEnvironmentOptions2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{10d7cc31-8b8f-4b9d-b22c-617103b55b08}')
    @winrt_commethod(6)
    def get_WindowAnnotationOverride(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_WindowAnnotationOverride(self, value: WinRT_String) -> Void: ...
    WindowAnnotationOverride = property(get_WindowAnnotationOverride, put_WindowAnnotationOverride)
class IIsolatedWindowsEnvironmentOptions3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{98d5aa23-161f-4cd9-8a9c-269b30122b0d}')
    @winrt_commethod(6)
    def get_AllowedClipboardFormatsToEnvironment(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentAllowedClipboardFormats: ...
    @winrt_commethod(7)
    def put_AllowedClipboardFormatsToEnvironment(self, value: Windows.Security.Isolation.IsolatedWindowsEnvironmentAllowedClipboardFormats) -> Void: ...
    @winrt_commethod(8)
    def get_AllowedClipboardFormatsToHost(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentAllowedClipboardFormats: ...
    @winrt_commethod(9)
    def put_AllowedClipboardFormatsToHost(self, value: Windows.Security.Isolation.IsolatedWindowsEnvironmentAllowedClipboardFormats) -> Void: ...
    @winrt_commethod(10)
    def get_CreationPriority(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentCreationPriority: ...
    @winrt_commethod(11)
    def put_CreationPriority(self, value: Windows.Security.Isolation.IsolatedWindowsEnvironmentCreationPriority) -> Void: ...
    AllowedClipboardFormatsToEnvironment = property(get_AllowedClipboardFormatsToEnvironment, put_AllowedClipboardFormatsToEnvironment)
    AllowedClipboardFormatsToHost = property(get_AllowedClipboardFormatsToHost, put_AllowedClipboardFormatsToHost)
    CreationPriority = property(get_CreationPriority, put_CreationPriority)
class IIsolatedWindowsEnvironmentOwnerRegistrationData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f888ec22-e8cf-56c0-b1df-90af4ad80e84}')
    @winrt_commethod(6)
    def get_ShareableFolders(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_ProcessesRunnableAsSystem(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(8)
    def get_ProcessesRunnableAsUser(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(9)
    def get_ActivationFileExtensions(self) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    ShareableFolders = property(get_ShareableFolders, None)
    ProcessesRunnableAsSystem = property(get_ProcessesRunnableAsSystem, None)
    ProcessesRunnableAsUser = property(get_ProcessesRunnableAsUser, None)
    ActivationFileExtensions = property(get_ActivationFileExtensions, None)
class IIsolatedWindowsEnvironmentOwnerRegistrationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{6dab9451-6169-55df-8f51-790e99d7277d}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentOwnerRegistrationStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
class IIsolatedWindowsEnvironmentOwnerRegistrationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{10951754-204b-5ec9-9de3-df792d074a61}')
    @winrt_commethod(6)
    def Register(self, ownerName: WinRT_String, ownerRegistrationData: Windows.Security.Isolation.IsolatedWindowsEnvironmentOwnerRegistrationData) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentOwnerRegistrationResult: ...
    @winrt_commethod(7)
    def Unregister(self, ownerName: WinRT_String) -> Void: ...
class IIsolatedWindowsEnvironmentPostMessageResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0dfa28fa-2ef0-4d8f-b341-3171b2df93b1}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentPostMessageStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
class IIsolatedWindowsEnvironmentProcess(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a858c3ef-8172-4f10-af93-cbe60af88d09}')
    @winrt_commethod(6)
    def get_State(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentProcessState: ...
    @winrt_commethod(7)
    def get_ExitCode(self) -> UInt32: ...
    @winrt_commethod(8)
    def WaitForExit(self) -> Void: ...
    @winrt_commethod(9)
    def WaitForExitWithTimeout(self, timeoutMilliseconds: UInt32) -> Void: ...
    @winrt_commethod(10)
    def WaitForExitAsync(self) -> Windows.Foundation.IAsyncAction: ...
    State = property(get_State, None)
    ExitCode = property(get_ExitCode, None)
class IIsolatedWindowsEnvironmentShareFileRequestOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c9190ed8-0fd0-4946-bb88-117a60737b61}')
    @winrt_commethod(6)
    def get_AllowWrite(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowWrite(self, value: Boolean) -> Void: ...
    AllowWrite = property(get_AllowWrite, put_AllowWrite)
class IIsolatedWindowsEnvironmentShareFileResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{aec7caa7-9ac6-4bf5-8b91-5c1adf0d7d00}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFileStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_File(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentFile: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
    File = property(get_File, None)
class IIsolatedWindowsEnvironmentShareFolderRequestOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c405eb7d-7053-4f6a-9b87-746846ed19b2}')
    @winrt_commethod(6)
    def get_AllowWrite(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowWrite(self, value: Boolean) -> Void: ...
    AllowWrite = property(get_AllowWrite, put_AllowWrite)
class IIsolatedWindowsEnvironmentShareFolderResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{556ba72e-ca9d-4211-b143-1cedc86eb2fe}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFolderStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
class IIsolatedWindowsEnvironmentStartProcessResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{8fa1dc2f-57da-4bb5-9c06-fa072d2032e2}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentStartProcessStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_Process(self) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentProcess: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
    Process = property(get_Process, None)
class IIsolatedWindowsEnvironmentTelemetryParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ebdb3cab-7a3a-4524-a0f4-f96e284d33cd}')
    @winrt_commethod(6)
    def get_CorrelationId(self) -> Guid: ...
    @winrt_commethod(7)
    def put_CorrelationId(self, value: Guid) -> Void: ...
    CorrelationId = property(get_CorrelationId, put_CorrelationId)
class IIsolatedWindowsEnvironmentUserInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{8a9c75ae-69ba-4001-96fc-19a02703b340}')
    @winrt_commethod(6)
    def get_EnvironmentUserSid(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_EnvironmentUserName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def TryWaitForSignInAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    EnvironmentUserSid = property(get_EnvironmentUserSid, None)
    EnvironmentUserName = property(get_EnvironmentUserName, None)
class IIsolatedWindowsEnvironmentUserInfo2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b0bdd5dd-91d7-481e-94f2-2a5a6bdf9383}')
    @winrt_commethod(6)
    def TryWaitForSignInWithProgressAsync(self) -> Windows.Foundation.IAsyncOperationWithProgress[Boolean, Windows.Security.Isolation.IsolatedWindowsEnvironmentSignInProgress]: ...
class IIsolatedWindowsHostMessengerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{06e444bb-53c0-4889-8fa3-53592e37cf21}')
    @winrt_commethod(6)
    def PostMessageToReceiver(self, receiverId: Guid, message: Windows.Foundation.Collections.IVectorView[Windows.Win32.System.WinRT.IInspectable_head]) -> Void: ...
    @winrt_commethod(7)
    def GetFileId(self, filePath: WinRT_String) -> Guid: ...
class IIsolatedWindowsHostMessengerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{55ef9ebc-0444-42ad-832d-1b89c089d1ca}')
    @winrt_commethod(6)
    def RegisterHostMessageReceiver(self, receiverId: Guid, hostMessageReceivedCallback: Windows.Security.Isolation.HostMessageReceivedCallback) -> Void: ...
    @winrt_commethod(7)
    def UnregisterHostMessageReceiver(self, receiverId: Guid) -> Void: ...
class IsolatedWindowsEnvironment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Isolation.IIsolatedWindowsEnvironment
    _classid_ = 'Windows.Security.Isolation.IsolatedWindowsEnvironment'
    @winrt_mixinmethod
    def get_Id(self: Windows.Security.Isolation.IIsolatedWindowsEnvironment) -> WinRT_String: ...
    @winrt_mixinmethod
    def StartProcessSilentlyAsync(self: Windows.Security.Isolation.IIsolatedWindowsEnvironment, hostExePath: WinRT_String, arguments: WinRT_String, activator: Windows.Security.Isolation.IsolatedWindowsEnvironmentActivator) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentStartProcessResult]: ...
    @winrt_mixinmethod
    def StartProcessSilentlyWithTelemetryAsync(self: Windows.Security.Isolation.IIsolatedWindowsEnvironment, hostExePath: WinRT_String, arguments: WinRT_String, activator: Windows.Security.Isolation.IsolatedWindowsEnvironmentActivator, telemetryParameters: Windows.Security.Isolation.IsolatedWindowsEnvironmentTelemetryParameters) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentStartProcessResult]: ...
    @winrt_mixinmethod
    def ShareFolderAsync(self: Windows.Security.Isolation.IIsolatedWindowsEnvironment, hostFolder: WinRT_String, requestOptions: Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFolderRequestOptions) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFolderResult]: ...
    @winrt_mixinmethod
    def ShareFolderWithTelemetryAsync(self: Windows.Security.Isolation.IIsolatedWindowsEnvironment, hostFolder: WinRT_String, requestOptions: Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFolderRequestOptions, telemetryParameters: Windows.Security.Isolation.IsolatedWindowsEnvironmentTelemetryParameters) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFolderResult]: ...
    @winrt_mixinmethod
    def LaunchFileWithUIAsync(self: Windows.Security.Isolation.IIsolatedWindowsEnvironment, appExePath: WinRT_String, argumentsTemplate: WinRT_String, filePath: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentLaunchFileResult]: ...
    @winrt_mixinmethod
    def LaunchFileWithUIAndTelemetryAsync(self: Windows.Security.Isolation.IIsolatedWindowsEnvironment, appExePath: WinRT_String, argumentsTemplate: WinRT_String, filePath: WinRT_String, telemetryParameters: Windows.Security.Isolation.IsolatedWindowsEnvironmentTelemetryParameters) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentLaunchFileResult]: ...
    @winrt_mixinmethod
    def TerminateAsync(self: Windows.Security.Isolation.IIsolatedWindowsEnvironment) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def TerminateWithTelemetryAsync(self: Windows.Security.Isolation.IIsolatedWindowsEnvironment, telemetryParameters: Windows.Security.Isolation.IsolatedWindowsEnvironmentTelemetryParameters) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RegisterMessageReceiver(self: Windows.Security.Isolation.IIsolatedWindowsEnvironment, receiverId: Guid, messageReceivedCallback: Windows.Security.Isolation.MessageReceivedCallback) -> Void: ...
    @winrt_mixinmethod
    def UnregisterMessageReceiver(self: Windows.Security.Isolation.IIsolatedWindowsEnvironment, receiverId: Guid) -> Void: ...
    @winrt_mixinmethod
    def PostMessageToReceiverAsync(self: Windows.Security.Isolation.IIsolatedWindowsEnvironment2, receiverId: Guid, message: Windows.Foundation.Collections.IIterable[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentPostMessageResult]: ...
    @winrt_mixinmethod
    def PostMessageToReceiverWithTelemetryAsync(self: Windows.Security.Isolation.IIsolatedWindowsEnvironment2, receiverId: Guid, message: Windows.Foundation.Collections.IIterable[Windows.Win32.System.WinRT.IInspectable_head], telemetryParameters: Windows.Security.Isolation.IsolatedWindowsEnvironmentTelemetryParameters) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentPostMessageResult]: ...
    @winrt_mixinmethod
    def GetUserInfo(self: Windows.Security.Isolation.IIsolatedWindowsEnvironment3) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentUserInfo: ...
    @winrt_mixinmethod
    def ShareFileAsync(self: Windows.Security.Isolation.IIsolatedWindowsEnvironment3, filePath: WinRT_String, options: Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFileRequestOptions) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFileResult]: ...
    @winrt_mixinmethod
    def ShareFileWithTelemetryAsync(self: Windows.Security.Isolation.IIsolatedWindowsEnvironment3, filePath: WinRT_String, options: Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFileRequestOptions, telemetryParameters: Windows.Security.Isolation.IsolatedWindowsEnvironmentTelemetryParameters) -> Windows.Foundation.IAsyncOperation[Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFileResult]: ...
    @winrt_mixinmethod
    def ChangePriority(self: Windows.Security.Isolation.IIsolatedWindowsEnvironment4, Priority: Windows.Security.Isolation.IsolatedWindowsEnvironmentCreationPriority) -> Void: ...
    @winrt_classmethod
    def CreateAsync(cls: Windows.Security.Isolation.IIsolatedWindowsEnvironmentFactory, options: Windows.Security.Isolation.IsolatedWindowsEnvironmentOptions) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Security.Isolation.IsolatedWindowsEnvironmentCreateResult, Windows.Security.Isolation.IsolatedWindowsEnvironmentCreateProgress]: ...
    @winrt_classmethod
    def CreateWithTelemetryAsync(cls: Windows.Security.Isolation.IIsolatedWindowsEnvironmentFactory, options: Windows.Security.Isolation.IsolatedWindowsEnvironmentOptions, telemetryParameters: Windows.Security.Isolation.IsolatedWindowsEnvironmentTelemetryParameters) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Security.Isolation.IsolatedWindowsEnvironmentCreateResult, Windows.Security.Isolation.IsolatedWindowsEnvironmentCreateProgress]: ...
    @winrt_classmethod
    def GetById(cls: Windows.Security.Isolation.IIsolatedWindowsEnvironmentFactory, environmentId: WinRT_String) -> Windows.Security.Isolation.IsolatedWindowsEnvironment: ...
    @winrt_classmethod
    def FindByOwnerId(cls: Windows.Security.Isolation.IIsolatedWindowsEnvironmentFactory, environmentOwnerId: WinRT_String) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Isolation.IsolatedWindowsEnvironment]: ...
    Id = property(get_Id, None)
IsolatedWindowsEnvironmentActivator = Int32
IsolatedWindowsEnvironmentActivator_System: IsolatedWindowsEnvironmentActivator = 0
IsolatedWindowsEnvironmentActivator_User: IsolatedWindowsEnvironmentActivator = 1
IsolatedWindowsEnvironmentAllowedClipboardFormats = UInt32
IsolatedWindowsEnvironmentAllowedClipboardFormats_None: IsolatedWindowsEnvironmentAllowedClipboardFormats = 0
IsolatedWindowsEnvironmentAllowedClipboardFormats_Text: IsolatedWindowsEnvironmentAllowedClipboardFormats = 1
IsolatedWindowsEnvironmentAllowedClipboardFormats_Image: IsolatedWindowsEnvironmentAllowedClipboardFormats = 2
IsolatedWindowsEnvironmentAllowedClipboardFormats_Rtf: IsolatedWindowsEnvironmentAllowedClipboardFormats = 4
IsolatedWindowsEnvironmentAvailablePrinters = UInt32
IsolatedWindowsEnvironmentAvailablePrinters_None: IsolatedWindowsEnvironmentAvailablePrinters = 0
IsolatedWindowsEnvironmentAvailablePrinters_Local: IsolatedWindowsEnvironmentAvailablePrinters = 1
IsolatedWindowsEnvironmentAvailablePrinters_Network: IsolatedWindowsEnvironmentAvailablePrinters = 2
IsolatedWindowsEnvironmentAvailablePrinters_SystemPrintToPdf: IsolatedWindowsEnvironmentAvailablePrinters = 4
IsolatedWindowsEnvironmentAvailablePrinters_SystemPrintToXps: IsolatedWindowsEnvironmentAvailablePrinters = 8
IsolatedWindowsEnvironmentClipboardCopyPasteDirections = UInt32
IsolatedWindowsEnvironmentClipboardCopyPasteDirections_None: IsolatedWindowsEnvironmentClipboardCopyPasteDirections = 0
IsolatedWindowsEnvironmentClipboardCopyPasteDirections_HostToIsolatedWindowsEnvironment: IsolatedWindowsEnvironmentClipboardCopyPasteDirections = 1
IsolatedWindowsEnvironmentClipboardCopyPasteDirections_IsolatedWindowsEnvironmentToHost: IsolatedWindowsEnvironmentClipboardCopyPasteDirections = 2
IsolatedWindowsEnvironmentContract: UInt32 = 262144
class IsolatedWindowsEnvironmentCreateProgress(EasyCastStructure):
    State: Windows.Security.Isolation.IsolatedWindowsEnvironmentProgressState
    PercentComplete: UInt32
class IsolatedWindowsEnvironmentCreateResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Isolation.IIsolatedWindowsEnvironmentCreateResult
    _classid_ = 'Windows.Security.Isolation.IsolatedWindowsEnvironmentCreateResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentCreateResult) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentCreateStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentCreateResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Environment(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentCreateResult) -> Windows.Security.Isolation.IsolatedWindowsEnvironment: ...
    @winrt_mixinmethod
    def ChangeCreationPriority(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentCreateResult2, priority: Windows.Security.Isolation.IsolatedWindowsEnvironmentCreationPriority) -> Void: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
    Environment = property(get_Environment, None)
IsolatedWindowsEnvironmentCreateStatus = Int32
IsolatedWindowsEnvironmentCreateStatus_Success: IsolatedWindowsEnvironmentCreateStatus = 0
IsolatedWindowsEnvironmentCreateStatus_FailureByPolicy: IsolatedWindowsEnvironmentCreateStatus = 1
IsolatedWindowsEnvironmentCreateStatus_UnknownFailure: IsolatedWindowsEnvironmentCreateStatus = 2
IsolatedWindowsEnvironmentCreationPriority = Int32
IsolatedWindowsEnvironmentCreationPriority_Low: IsolatedWindowsEnvironmentCreationPriority = 0
IsolatedWindowsEnvironmentCreationPriority_Normal: IsolatedWindowsEnvironmentCreationPriority = 1
class IsolatedWindowsEnvironmentFile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Isolation.IIsolatedWindowsEnvironmentFile
    _classid_ = 'Windows.Security.Isolation.IsolatedWindowsEnvironmentFile'
    @winrt_mixinmethod
    def get_Id(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentFile) -> Guid: ...
    @winrt_mixinmethod
    def get_HostPath(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentFile) -> WinRT_String: ...
    @winrt_mixinmethod
    def Close(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentFile) -> Void: ...
    @winrt_mixinmethod
    def get_GuestPath(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentFile2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsReadOnly(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentFile2) -> Boolean: ...
    Id = property(get_Id, None)
    HostPath = property(get_HostPath, None)
    GuestPath = property(get_GuestPath, None)
    IsReadOnly = property(get_IsReadOnly, None)
class IsolatedWindowsEnvironmentHost(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    @winrt_classmethod
    def get_IsReady(cls: Windows.Security.Isolation.IIsolatedWindowsEnvironmentHostStatics) -> Boolean: ...
    @winrt_classmethod
    def get_HostErrors(cls: Windows.Security.Isolation.IIsolatedWindowsEnvironmentHostStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Security.Isolation.IsolatedWindowsEnvironmentHostError]: ...
    IsReady = property(get_IsReady, None)
    HostErrors = property(get_HostErrors, None)
IsolatedWindowsEnvironmentHostError = Int32
IsolatedWindowsEnvironmentHostError_AdminPolicyIsDisabledOrNotPresent: IsolatedWindowsEnvironmentHostError = 0
IsolatedWindowsEnvironmentHostError_FeatureNotInstalled: IsolatedWindowsEnvironmentHostError = 1
IsolatedWindowsEnvironmentHostError_HardwareRequirementsNotMet: IsolatedWindowsEnvironmentHostError = 2
IsolatedWindowsEnvironmentHostError_RebootRequired: IsolatedWindowsEnvironmentHostError = 3
IsolatedWindowsEnvironmentHostError_UnknownError: IsolatedWindowsEnvironmentHostError = 4
class IsolatedWindowsEnvironmentLaunchFileResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Isolation.IIsolatedWindowsEnvironmentLaunchFileResult
    _classid_ = 'Windows.Security.Isolation.IsolatedWindowsEnvironmentLaunchFileResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentLaunchFileResult) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentLaunchFileStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentLaunchFileResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_File(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentLaunchFileResult) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentFile: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
    File = property(get_File, None)
IsolatedWindowsEnvironmentLaunchFileStatus = Int32
IsolatedWindowsEnvironmentLaunchFileStatus_Success: IsolatedWindowsEnvironmentLaunchFileStatus = 0
IsolatedWindowsEnvironmentLaunchFileStatus_UnknownFailure: IsolatedWindowsEnvironmentLaunchFileStatus = 1
IsolatedWindowsEnvironmentLaunchFileStatus_EnvironmentUnavailable: IsolatedWindowsEnvironmentLaunchFileStatus = 2
IsolatedWindowsEnvironmentLaunchFileStatus_FileNotFound: IsolatedWindowsEnvironmentLaunchFileStatus = 3
IsolatedWindowsEnvironmentLaunchFileStatus_TimedOut: IsolatedWindowsEnvironmentLaunchFileStatus = 4
IsolatedWindowsEnvironmentLaunchFileStatus_AlreadySharedWithConflictingOptions: IsolatedWindowsEnvironmentLaunchFileStatus = 5
class IsolatedWindowsEnvironmentOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions
    _classid_ = 'Windows.Security.Isolation.IsolatedWindowsEnvironmentOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentOptions: ...
    @winrt_mixinmethod
    def get_EnvironmentOwnerId(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_EnvironmentOwnerId(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AllowedClipboardFormats(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentAllowedClipboardFormats: ...
    @winrt_mixinmethod
    def put_AllowedClipboardFormats(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions, value: Windows.Security.Isolation.IsolatedWindowsEnvironmentAllowedClipboardFormats) -> Void: ...
    @winrt_mixinmethod
    def get_ClipboardCopyPasteDirections(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentClipboardCopyPasteDirections: ...
    @winrt_mixinmethod
    def put_ClipboardCopyPasteDirections(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions, value: Windows.Security.Isolation.IsolatedWindowsEnvironmentClipboardCopyPasteDirections) -> Void: ...
    @winrt_mixinmethod
    def get_AvailablePrinters(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentAvailablePrinters: ...
    @winrt_mixinmethod
    def put_AvailablePrinters(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions, value: Windows.Security.Isolation.IsolatedWindowsEnvironmentAvailablePrinters) -> Void: ...
    @winrt_mixinmethod
    def get_SharedHostFolderPath(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SharedFolderNameInEnvironment(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def ShareHostFolderForUntrustedItems(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions, SharedHostFolderPath: WinRT_String, ShareFolderNameInEnvironment: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PersistUserProfile(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_PersistUserProfile(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AllowGraphicsHardwareAcceleration(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowGraphicsHardwareAcceleration(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AllowCameraAndMicrophoneAccess(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowCameraAndMicrophoneAccess(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_WindowAnnotationOverride(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_WindowAnnotationOverride(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AllowedClipboardFormatsToEnvironment(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions3) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentAllowedClipboardFormats: ...
    @winrt_mixinmethod
    def put_AllowedClipboardFormatsToEnvironment(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions3, value: Windows.Security.Isolation.IsolatedWindowsEnvironmentAllowedClipboardFormats) -> Void: ...
    @winrt_mixinmethod
    def get_AllowedClipboardFormatsToHost(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions3) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentAllowedClipboardFormats: ...
    @winrt_mixinmethod
    def put_AllowedClipboardFormatsToHost(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions3, value: Windows.Security.Isolation.IsolatedWindowsEnvironmentAllowedClipboardFormats) -> Void: ...
    @winrt_mixinmethod
    def get_CreationPriority(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions3) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentCreationPriority: ...
    @winrt_mixinmethod
    def put_CreationPriority(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOptions3, value: Windows.Security.Isolation.IsolatedWindowsEnvironmentCreationPriority) -> Void: ...
    EnvironmentOwnerId = property(get_EnvironmentOwnerId, put_EnvironmentOwnerId)
    AllowedClipboardFormats = property(get_AllowedClipboardFormats, put_AllowedClipboardFormats)
    ClipboardCopyPasteDirections = property(get_ClipboardCopyPasteDirections, put_ClipboardCopyPasteDirections)
    AvailablePrinters = property(get_AvailablePrinters, put_AvailablePrinters)
    SharedHostFolderPath = property(get_SharedHostFolderPath, None)
    SharedFolderNameInEnvironment = property(get_SharedFolderNameInEnvironment, None)
    PersistUserProfile = property(get_PersistUserProfile, put_PersistUserProfile)
    AllowGraphicsHardwareAcceleration = property(get_AllowGraphicsHardwareAcceleration, put_AllowGraphicsHardwareAcceleration)
    AllowCameraAndMicrophoneAccess = property(get_AllowCameraAndMicrophoneAccess, put_AllowCameraAndMicrophoneAccess)
    WindowAnnotationOverride = property(get_WindowAnnotationOverride, put_WindowAnnotationOverride)
    AllowedClipboardFormatsToEnvironment = property(get_AllowedClipboardFormatsToEnvironment, put_AllowedClipboardFormatsToEnvironment)
    AllowedClipboardFormatsToHost = property(get_AllowedClipboardFormatsToHost, put_AllowedClipboardFormatsToHost)
    CreationPriority = property(get_CreationPriority, put_CreationPriority)
class IsolatedWindowsEnvironmentOwnerRegistration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    @winrt_classmethod
    def Register(cls: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOwnerRegistrationStatics, ownerName: WinRT_String, ownerRegistrationData: Windows.Security.Isolation.IsolatedWindowsEnvironmentOwnerRegistrationData) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentOwnerRegistrationResult: ...
    @winrt_classmethod
    def Unregister(cls: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOwnerRegistrationStatics, ownerName: WinRT_String) -> Void: ...
class IsolatedWindowsEnvironmentOwnerRegistrationData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOwnerRegistrationData
    _classid_ = 'Windows.Security.Isolation.IsolatedWindowsEnvironmentOwnerRegistrationData'
    @winrt_activatemethod
    def New(cls) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentOwnerRegistrationData: ...
    @winrt_mixinmethod
    def get_ShareableFolders(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOwnerRegistrationData) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ProcessesRunnableAsSystem(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOwnerRegistrationData) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ProcessesRunnableAsUser(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOwnerRegistrationData) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ActivationFileExtensions(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOwnerRegistrationData) -> Windows.Foundation.Collections.IVector[WinRT_String]: ...
    ShareableFolders = property(get_ShareableFolders, None)
    ProcessesRunnableAsSystem = property(get_ProcessesRunnableAsSystem, None)
    ProcessesRunnableAsUser = property(get_ProcessesRunnableAsUser, None)
    ActivationFileExtensions = property(get_ActivationFileExtensions, None)
class IsolatedWindowsEnvironmentOwnerRegistrationResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOwnerRegistrationResult
    _classid_ = 'Windows.Security.Isolation.IsolatedWindowsEnvironmentOwnerRegistrationResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOwnerRegistrationResult) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentOwnerRegistrationStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentOwnerRegistrationResult) -> Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
IsolatedWindowsEnvironmentOwnerRegistrationStatus = Int32
IsolatedWindowsEnvironmentOwnerRegistrationStatus_Success: IsolatedWindowsEnvironmentOwnerRegistrationStatus = 0
IsolatedWindowsEnvironmentOwnerRegistrationStatus_InvalidArgument: IsolatedWindowsEnvironmentOwnerRegistrationStatus = 1
IsolatedWindowsEnvironmentOwnerRegistrationStatus_AccessDenied: IsolatedWindowsEnvironmentOwnerRegistrationStatus = 2
IsolatedWindowsEnvironmentOwnerRegistrationStatus_InsufficientMemory: IsolatedWindowsEnvironmentOwnerRegistrationStatus = 3
IsolatedWindowsEnvironmentOwnerRegistrationStatus_UnknownFailure: IsolatedWindowsEnvironmentOwnerRegistrationStatus = 4
class IsolatedWindowsEnvironmentPostMessageResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Isolation.IIsolatedWindowsEnvironmentPostMessageResult
    _classid_ = 'Windows.Security.Isolation.IsolatedWindowsEnvironmentPostMessageResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentPostMessageResult) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentPostMessageStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentPostMessageResult) -> Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
IsolatedWindowsEnvironmentPostMessageStatus = Int32
IsolatedWindowsEnvironmentPostMessageStatus_Success: IsolatedWindowsEnvironmentPostMessageStatus = 0
IsolatedWindowsEnvironmentPostMessageStatus_UnknownFailure: IsolatedWindowsEnvironmentPostMessageStatus = 1
IsolatedWindowsEnvironmentPostMessageStatus_EnvironmentUnavailable: IsolatedWindowsEnvironmentPostMessageStatus = 2
class IsolatedWindowsEnvironmentProcess(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Isolation.IIsolatedWindowsEnvironmentProcess
    _classid_ = 'Windows.Security.Isolation.IsolatedWindowsEnvironmentProcess'
    @winrt_mixinmethod
    def get_State(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentProcess) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentProcessState: ...
    @winrt_mixinmethod
    def get_ExitCode(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentProcess) -> UInt32: ...
    @winrt_mixinmethod
    def WaitForExit(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentProcess) -> Void: ...
    @winrt_mixinmethod
    def WaitForExitWithTimeout(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentProcess, timeoutMilliseconds: UInt32) -> Void: ...
    @winrt_mixinmethod
    def WaitForExitAsync(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentProcess) -> Windows.Foundation.IAsyncAction: ...
    State = property(get_State, None)
    ExitCode = property(get_ExitCode, None)
IsolatedWindowsEnvironmentProcessState = Int32
IsolatedWindowsEnvironmentProcessState_Running: IsolatedWindowsEnvironmentProcessState = 1
IsolatedWindowsEnvironmentProcessState_Aborted: IsolatedWindowsEnvironmentProcessState = 2
IsolatedWindowsEnvironmentProcessState_Completed: IsolatedWindowsEnvironmentProcessState = 3
IsolatedWindowsEnvironmentProgressState = Int32
IsolatedWindowsEnvironmentProgressState_Queued: IsolatedWindowsEnvironmentProgressState = 0
IsolatedWindowsEnvironmentProgressState_Processing: IsolatedWindowsEnvironmentProgressState = 1
IsolatedWindowsEnvironmentProgressState_Completed: IsolatedWindowsEnvironmentProgressState = 2
IsolatedWindowsEnvironmentProgressState_Creating: IsolatedWindowsEnvironmentProgressState = 3
IsolatedWindowsEnvironmentProgressState_Retrying: IsolatedWindowsEnvironmentProgressState = 4
IsolatedWindowsEnvironmentProgressState_Starting: IsolatedWindowsEnvironmentProgressState = 5
IsolatedWindowsEnvironmentProgressState_Finalizing: IsolatedWindowsEnvironmentProgressState = 6
class IsolatedWindowsEnvironmentShareFileRequestOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Isolation.IIsolatedWindowsEnvironmentShareFileRequestOptions
    _classid_ = 'Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFileRequestOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFileRequestOptions: ...
    @winrt_mixinmethod
    def get_AllowWrite(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentShareFileRequestOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowWrite(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentShareFileRequestOptions, value: Boolean) -> Void: ...
    AllowWrite = property(get_AllowWrite, put_AllowWrite)
class IsolatedWindowsEnvironmentShareFileResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Isolation.IIsolatedWindowsEnvironmentShareFileResult
    _classid_ = 'Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFileResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentShareFileResult) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFileStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentShareFileResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_File(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentShareFileResult) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentFile: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
    File = property(get_File, None)
IsolatedWindowsEnvironmentShareFileStatus = Int32
IsolatedWindowsEnvironmentShareFileStatus_Success: IsolatedWindowsEnvironmentShareFileStatus = 0
IsolatedWindowsEnvironmentShareFileStatus_UnknownFailure: IsolatedWindowsEnvironmentShareFileStatus = 1
IsolatedWindowsEnvironmentShareFileStatus_EnvironmentUnavailable: IsolatedWindowsEnvironmentShareFileStatus = 2
IsolatedWindowsEnvironmentShareFileStatus_AlreadySharedWithConflictingOptions: IsolatedWindowsEnvironmentShareFileStatus = 3
IsolatedWindowsEnvironmentShareFileStatus_FileNotFound: IsolatedWindowsEnvironmentShareFileStatus = 4
IsolatedWindowsEnvironmentShareFileStatus_AccessDenied: IsolatedWindowsEnvironmentShareFileStatus = 5
class IsolatedWindowsEnvironmentShareFolderRequestOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Isolation.IIsolatedWindowsEnvironmentShareFolderRequestOptions
    _classid_ = 'Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFolderRequestOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFolderRequestOptions: ...
    @winrt_mixinmethod
    def get_AllowWrite(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentShareFolderRequestOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowWrite(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentShareFolderRequestOptions, value: Boolean) -> Void: ...
    AllowWrite = property(get_AllowWrite, put_AllowWrite)
class IsolatedWindowsEnvironmentShareFolderResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Isolation.IIsolatedWindowsEnvironmentShareFolderResult
    _classid_ = 'Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFolderResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentShareFolderResult) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentShareFolderStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentShareFolderResult) -> Windows.Foundation.HResult: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
IsolatedWindowsEnvironmentShareFolderStatus = Int32
IsolatedWindowsEnvironmentShareFolderStatus_Success: IsolatedWindowsEnvironmentShareFolderStatus = 0
IsolatedWindowsEnvironmentShareFolderStatus_UnknownFailure: IsolatedWindowsEnvironmentShareFolderStatus = 1
IsolatedWindowsEnvironmentShareFolderStatus_EnvironmentUnavailable: IsolatedWindowsEnvironmentShareFolderStatus = 2
IsolatedWindowsEnvironmentShareFolderStatus_FolderNotFound: IsolatedWindowsEnvironmentShareFolderStatus = 3
IsolatedWindowsEnvironmentShareFolderStatus_AccessDenied: IsolatedWindowsEnvironmentShareFolderStatus = 4
IsolatedWindowsEnvironmentSignInProgress = Int32
IsolatedWindowsEnvironmentSignInProgress_Connecting: IsolatedWindowsEnvironmentSignInProgress = 0
IsolatedWindowsEnvironmentSignInProgress_Connected: IsolatedWindowsEnvironmentSignInProgress = 1
IsolatedWindowsEnvironmentSignInProgress_Authenticating: IsolatedWindowsEnvironmentSignInProgress = 2
IsolatedWindowsEnvironmentSignInProgress_SettingUpAccount: IsolatedWindowsEnvironmentSignInProgress = 3
IsolatedWindowsEnvironmentSignInProgress_Finalizing: IsolatedWindowsEnvironmentSignInProgress = 4
IsolatedWindowsEnvironmentSignInProgress_Completed: IsolatedWindowsEnvironmentSignInProgress = 5
class IsolatedWindowsEnvironmentStartProcessResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Isolation.IIsolatedWindowsEnvironmentStartProcessResult
    _classid_ = 'Windows.Security.Isolation.IsolatedWindowsEnvironmentStartProcessResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentStartProcessResult) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentStartProcessStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentStartProcessResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Process(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentStartProcessResult) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentProcess: ...
    Status = property(get_Status, None)
    ExtendedError = property(get_ExtendedError, None)
    Process = property(get_Process, None)
IsolatedWindowsEnvironmentStartProcessStatus = Int32
IsolatedWindowsEnvironmentStartProcessStatus_Success: IsolatedWindowsEnvironmentStartProcessStatus = 0
IsolatedWindowsEnvironmentStartProcessStatus_UnknownFailure: IsolatedWindowsEnvironmentStartProcessStatus = 1
IsolatedWindowsEnvironmentStartProcessStatus_EnvironmentUnavailable: IsolatedWindowsEnvironmentStartProcessStatus = 2
IsolatedWindowsEnvironmentStartProcessStatus_FileNotFound: IsolatedWindowsEnvironmentStartProcessStatus = 3
IsolatedWindowsEnvironmentStartProcessStatus_AppNotRegistered: IsolatedWindowsEnvironmentStartProcessStatus = 4
class IsolatedWindowsEnvironmentTelemetryParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Isolation.IIsolatedWindowsEnvironmentTelemetryParameters
    _classid_ = 'Windows.Security.Isolation.IsolatedWindowsEnvironmentTelemetryParameters'
    @winrt_activatemethod
    def New(cls) -> Windows.Security.Isolation.IsolatedWindowsEnvironmentTelemetryParameters: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentTelemetryParameters) -> Guid: ...
    @winrt_mixinmethod
    def put_CorrelationId(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentTelemetryParameters, value: Guid) -> Void: ...
    CorrelationId = property(get_CorrelationId, put_CorrelationId)
class IsolatedWindowsEnvironmentUserInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Security.Isolation.IIsolatedWindowsEnvironmentUserInfo
    _classid_ = 'Windows.Security.Isolation.IsolatedWindowsEnvironmentUserInfo'
    @winrt_mixinmethod
    def get_EnvironmentUserSid(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentUserInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EnvironmentUserName(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentUserInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def TryWaitForSignInAsync(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentUserInfo) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryWaitForSignInWithProgressAsync(self: Windows.Security.Isolation.IIsolatedWindowsEnvironmentUserInfo2) -> Windows.Foundation.IAsyncOperationWithProgress[Boolean, Windows.Security.Isolation.IsolatedWindowsEnvironmentSignInProgress]: ...
    EnvironmentUserSid = property(get_EnvironmentUserSid, None)
    EnvironmentUserName = property(get_EnvironmentUserName, None)
class IsolatedWindowsHostMessenger(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    @winrt_classmethod
    def RegisterHostMessageReceiver(cls: Windows.Security.Isolation.IIsolatedWindowsHostMessengerStatics2, receiverId: Guid, hostMessageReceivedCallback: Windows.Security.Isolation.HostMessageReceivedCallback) -> Void: ...
    @winrt_classmethod
    def UnregisterHostMessageReceiver(cls: Windows.Security.Isolation.IIsolatedWindowsHostMessengerStatics2, receiverId: Guid) -> Void: ...
    @winrt_classmethod
    def PostMessageToReceiver(cls: Windows.Security.Isolation.IIsolatedWindowsHostMessengerStatics, receiverId: Guid, message: Windows.Foundation.Collections.IVectorView[Windows.Win32.System.WinRT.IInspectable_head]) -> Void: ...
    @winrt_classmethod
    def GetFileId(cls: Windows.Security.Isolation.IIsolatedWindowsHostMessengerStatics, filePath: WinRT_String) -> Guid: ...
class MessageReceivedCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f5b4c8ff-1d9d-4995-9fea-4d15257c0757}')
    _classid_ = 'Windows.Security.Isolation.MessageReceivedCallback'
    @winrt_commethod(3)
    def Invoke(self, receiverId: Guid, message: Windows.Foundation.Collections.IVectorView[Windows.Win32.System.WinRT.IInspectable_head]) -> Void: ...
make_head(_module, 'HostMessageReceivedCallback')
make_head(_module, 'IIsolatedWindowsEnvironment')
make_head(_module, 'IIsolatedWindowsEnvironment2')
make_head(_module, 'IIsolatedWindowsEnvironment3')
make_head(_module, 'IIsolatedWindowsEnvironment4')
make_head(_module, 'IIsolatedWindowsEnvironmentCreateResult')
make_head(_module, 'IIsolatedWindowsEnvironmentCreateResult2')
make_head(_module, 'IIsolatedWindowsEnvironmentFactory')
make_head(_module, 'IIsolatedWindowsEnvironmentFile')
make_head(_module, 'IIsolatedWindowsEnvironmentFile2')
make_head(_module, 'IIsolatedWindowsEnvironmentHostStatics')
make_head(_module, 'IIsolatedWindowsEnvironmentLaunchFileResult')
make_head(_module, 'IIsolatedWindowsEnvironmentOptions')
make_head(_module, 'IIsolatedWindowsEnvironmentOptions2')
make_head(_module, 'IIsolatedWindowsEnvironmentOptions3')
make_head(_module, 'IIsolatedWindowsEnvironmentOwnerRegistrationData')
make_head(_module, 'IIsolatedWindowsEnvironmentOwnerRegistrationResult')
make_head(_module, 'IIsolatedWindowsEnvironmentOwnerRegistrationStatics')
make_head(_module, 'IIsolatedWindowsEnvironmentPostMessageResult')
make_head(_module, 'IIsolatedWindowsEnvironmentProcess')
make_head(_module, 'IIsolatedWindowsEnvironmentShareFileRequestOptions')
make_head(_module, 'IIsolatedWindowsEnvironmentShareFileResult')
make_head(_module, 'IIsolatedWindowsEnvironmentShareFolderRequestOptions')
make_head(_module, 'IIsolatedWindowsEnvironmentShareFolderResult')
make_head(_module, 'IIsolatedWindowsEnvironmentStartProcessResult')
make_head(_module, 'IIsolatedWindowsEnvironmentTelemetryParameters')
make_head(_module, 'IIsolatedWindowsEnvironmentUserInfo')
make_head(_module, 'IIsolatedWindowsEnvironmentUserInfo2')
make_head(_module, 'IIsolatedWindowsHostMessengerStatics')
make_head(_module, 'IIsolatedWindowsHostMessengerStatics2')
make_head(_module, 'IsolatedWindowsEnvironment')
make_head(_module, 'IsolatedWindowsEnvironmentCreateProgress')
make_head(_module, 'IsolatedWindowsEnvironmentCreateResult')
make_head(_module, 'IsolatedWindowsEnvironmentFile')
make_head(_module, 'IsolatedWindowsEnvironmentHost')
make_head(_module, 'IsolatedWindowsEnvironmentLaunchFileResult')
make_head(_module, 'IsolatedWindowsEnvironmentOptions')
make_head(_module, 'IsolatedWindowsEnvironmentOwnerRegistration')
make_head(_module, 'IsolatedWindowsEnvironmentOwnerRegistrationData')
make_head(_module, 'IsolatedWindowsEnvironmentOwnerRegistrationResult')
make_head(_module, 'IsolatedWindowsEnvironmentPostMessageResult')
make_head(_module, 'IsolatedWindowsEnvironmentProcess')
make_head(_module, 'IsolatedWindowsEnvironmentShareFileRequestOptions')
make_head(_module, 'IsolatedWindowsEnvironmentShareFileResult')
make_head(_module, 'IsolatedWindowsEnvironmentShareFolderRequestOptions')
make_head(_module, 'IsolatedWindowsEnvironmentShareFolderResult')
make_head(_module, 'IsolatedWindowsEnvironmentStartProcessResult')
make_head(_module, 'IsolatedWindowsEnvironmentTelemetryParameters')
make_head(_module, 'IsolatedWindowsEnvironmentUserInfo')
make_head(_module, 'IsolatedWindowsHostMessenger')
make_head(_module, 'MessageReceivedCallback')
