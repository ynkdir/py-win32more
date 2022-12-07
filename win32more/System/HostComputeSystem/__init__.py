from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security
import win32more.System.HostComputeSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
@winfunctype('computecore.dll')
def HcsEnumerateComputeSystems(query: win32more.Foundation.PWSTR, operation: win32more.System.HostComputeSystem.HCS_OPERATION) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsEnumerateComputeSystemsInNamespace(idNamespace: win32more.Foundation.PWSTR, query: win32more.Foundation.PWSTR, operation: win32more.System.HostComputeSystem.HCS_OPERATION) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCreateOperation(context: c_void_p, callback: win32more.System.HostComputeSystem.HCS_OPERATION_COMPLETION) -> win32more.System.HostComputeSystem.HCS_OPERATION: ...
@winfunctype('computecore.dll')
def HcsCloseOperation(operation: win32more.System.HostComputeSystem.HCS_OPERATION) -> Void: ...
@winfunctype('computecore.dll')
def HcsGetOperationContext(operation: win32more.System.HostComputeSystem.HCS_OPERATION) -> c_void_p: ...
@winfunctype('computecore.dll')
def HcsSetOperationContext(operation: win32more.System.HostComputeSystem.HCS_OPERATION, context: c_void_p) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsGetComputeSystemFromOperation(operation: win32more.System.HostComputeSystem.HCS_OPERATION) -> win32more.System.HostComputeSystem.HCS_SYSTEM: ...
@winfunctype('computecore.dll')
def HcsGetProcessFromOperation(operation: win32more.System.HostComputeSystem.HCS_OPERATION) -> win32more.System.HostComputeSystem.HCS_PROCESS: ...
@winfunctype('computecore.dll')
def HcsGetOperationType(operation: win32more.System.HostComputeSystem.HCS_OPERATION) -> win32more.System.HostComputeSystem.HCS_OPERATION_TYPE: ...
@winfunctype('computecore.dll')
def HcsGetOperationId(operation: win32more.System.HostComputeSystem.HCS_OPERATION) -> UInt64: ...
@winfunctype('computecore.dll')
def HcsGetOperationResult(operation: win32more.System.HostComputeSystem.HCS_OPERATION, resultDocument: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsGetOperationResultAndProcessInfo(operation: win32more.System.HostComputeSystem.HCS_OPERATION, processInformation: POINTER(win32more.System.HostComputeSystem.HCS_PROCESS_INFORMATION_head), resultDocument: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsGetProcessorCompatibilityFromSavedState(RuntimeFileName: win32more.Foundation.PWSTR, ProcessorFeaturesString: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsWaitForOperationResult(operation: win32more.System.HostComputeSystem.HCS_OPERATION, timeoutMs: UInt32, resultDocument: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsWaitForOperationResultAndProcessInfo(operation: win32more.System.HostComputeSystem.HCS_OPERATION, timeoutMs: UInt32, processInformation: POINTER(win32more.System.HostComputeSystem.HCS_PROCESS_INFORMATION_head), resultDocument: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsSetOperationCallback(operation: win32more.System.HostComputeSystem.HCS_OPERATION, context: c_void_p, callback: win32more.System.HostComputeSystem.HCS_OPERATION_COMPLETION) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCancelOperation(operation: win32more.System.HostComputeSystem.HCS_OPERATION) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCreateComputeSystem(id: win32more.Foundation.PWSTR, configuration: win32more.Foundation.PWSTR, operation: win32more.System.HostComputeSystem.HCS_OPERATION, securityDescriptor: POINTER(win32more.Security.SECURITY_DESCRIPTOR_head), computeSystem: POINTER(win32more.System.HostComputeSystem.HCS_SYSTEM)) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCreateComputeSystemInNamespace(idNamespace: win32more.Foundation.PWSTR, id: win32more.Foundation.PWSTR, configuration: win32more.Foundation.PWSTR, operation: win32more.System.HostComputeSystem.HCS_OPERATION, options: POINTER(win32more.System.HostComputeSystem.HCS_CREATE_OPTIONS), computeSystem: POINTER(win32more.System.HostComputeSystem.HCS_SYSTEM)) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsOpenComputeSystem(id: win32more.Foundation.PWSTR, requestedAccess: UInt32, computeSystem: POINTER(win32more.System.HostComputeSystem.HCS_SYSTEM)) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsOpenComputeSystemInNamespace(idNamespace: win32more.Foundation.PWSTR, id: win32more.Foundation.PWSTR, requestedAccess: UInt32, computeSystem: POINTER(win32more.System.HostComputeSystem.HCS_SYSTEM)) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCloseComputeSystem(computeSystem: win32more.System.HostComputeSystem.HCS_SYSTEM) -> Void: ...
@winfunctype('computecore.dll')
def HcsStartComputeSystem(computeSystem: win32more.System.HostComputeSystem.HCS_SYSTEM, operation: win32more.System.HostComputeSystem.HCS_OPERATION, options: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsShutDownComputeSystem(computeSystem: win32more.System.HostComputeSystem.HCS_SYSTEM, operation: win32more.System.HostComputeSystem.HCS_OPERATION, options: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsTerminateComputeSystem(computeSystem: win32more.System.HostComputeSystem.HCS_SYSTEM, operation: win32more.System.HostComputeSystem.HCS_OPERATION, options: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCrashComputeSystem(computeSystem: win32more.System.HostComputeSystem.HCS_SYSTEM, operation: win32more.System.HostComputeSystem.HCS_OPERATION, options: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsPauseComputeSystem(computeSystem: win32more.System.HostComputeSystem.HCS_SYSTEM, operation: win32more.System.HostComputeSystem.HCS_OPERATION, options: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsResumeComputeSystem(computeSystem: win32more.System.HostComputeSystem.HCS_SYSTEM, operation: win32more.System.HostComputeSystem.HCS_OPERATION, options: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsSaveComputeSystem(computeSystem: win32more.System.HostComputeSystem.HCS_SYSTEM, operation: win32more.System.HostComputeSystem.HCS_OPERATION, options: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsGetComputeSystemProperties(computeSystem: win32more.System.HostComputeSystem.HCS_SYSTEM, operation: win32more.System.HostComputeSystem.HCS_OPERATION, propertyQuery: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsModifyComputeSystem(computeSystem: win32more.System.HostComputeSystem.HCS_SYSTEM, operation: win32more.System.HostComputeSystem.HCS_OPERATION, configuration: win32more.Foundation.PWSTR, identity: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsWaitForComputeSystemExit(computeSystem: win32more.System.HostComputeSystem.HCS_SYSTEM, timeoutMs: UInt32, result: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsSetComputeSystemCallback(computeSystem: win32more.System.HostComputeSystem.HCS_SYSTEM, callbackOptions: win32more.System.HostComputeSystem.HCS_EVENT_OPTIONS, context: c_void_p, callback: win32more.System.HostComputeSystem.HCS_EVENT_CALLBACK) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCreateProcess(computeSystem: win32more.System.HostComputeSystem.HCS_SYSTEM, processParameters: win32more.Foundation.PWSTR, operation: win32more.System.HostComputeSystem.HCS_OPERATION, securityDescriptor: POINTER(win32more.Security.SECURITY_DESCRIPTOR_head), process: POINTER(win32more.System.HostComputeSystem.HCS_PROCESS)) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsOpenProcess(computeSystem: win32more.System.HostComputeSystem.HCS_SYSTEM, processId: UInt32, requestedAccess: UInt32, process: POINTER(win32more.System.HostComputeSystem.HCS_PROCESS)) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCloseProcess(process: win32more.System.HostComputeSystem.HCS_PROCESS) -> Void: ...
@winfunctype('computecore.dll')
def HcsTerminateProcess(process: win32more.System.HostComputeSystem.HCS_PROCESS, operation: win32more.System.HostComputeSystem.HCS_OPERATION, options: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsSignalProcess(process: win32more.System.HostComputeSystem.HCS_PROCESS, operation: win32more.System.HostComputeSystem.HCS_OPERATION, options: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsGetProcessInfo(process: win32more.System.HostComputeSystem.HCS_PROCESS, operation: win32more.System.HostComputeSystem.HCS_OPERATION) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsGetProcessProperties(process: win32more.System.HostComputeSystem.HCS_PROCESS, operation: win32more.System.HostComputeSystem.HCS_OPERATION, propertyQuery: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsModifyProcess(process: win32more.System.HostComputeSystem.HCS_PROCESS, operation: win32more.System.HostComputeSystem.HCS_OPERATION, settings: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsSetProcessCallback(process: win32more.System.HostComputeSystem.HCS_PROCESS, callbackOptions: win32more.System.HostComputeSystem.HCS_EVENT_OPTIONS, context: c_void_p, callback: win32more.System.HostComputeSystem.HCS_EVENT_CALLBACK) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsWaitForProcessExit(computeSystem: win32more.System.HostComputeSystem.HCS_PROCESS, timeoutMs: UInt32, result: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsGetServiceProperties(propertyQuery: win32more.Foundation.PWSTR, result: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsModifyServiceSettings(settings: win32more.Foundation.PWSTR, result: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsSubmitWerReport(settings: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCreateEmptyGuestStateFile(guestStateFilePath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCreateEmptyRuntimeStateFile(runtimeStateFilePath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsGrantVmAccess(vmId: win32more.Foundation.PWSTR, filePath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsRevokeVmAccess(vmId: win32more.Foundation.PWSTR, filePath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsGrantVmGroupAccess(filePath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsRevokeVmGroupAccess(filePath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsImportLayer(layerPath: win32more.Foundation.PWSTR, sourceFolderPath: win32more.Foundation.PWSTR, layerData: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsExportLayer(layerPath: win32more.Foundation.PWSTR, exportFolderPath: win32more.Foundation.PWSTR, layerData: win32more.Foundation.PWSTR, options: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsExportLegacyWritableLayer(writableLayerMountPath: win32more.Foundation.PWSTR, writableLayerFolderPath: win32more.Foundation.PWSTR, exportFolderPath: win32more.Foundation.PWSTR, layerData: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsDestroyLayer(layerPath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsSetupBaseOSLayer(layerPath: win32more.Foundation.PWSTR, vhdHandle: win32more.Foundation.HANDLE, options: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsInitializeWritableLayer(writableLayerPath: win32more.Foundation.PWSTR, layerData: win32more.Foundation.PWSTR, options: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsInitializeLegacyWritableLayer(writableLayerMountPath: win32more.Foundation.PWSTR, writableLayerFolderPath: win32more.Foundation.PWSTR, layerData: win32more.Foundation.PWSTR, options: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsAttachLayerStorageFilter(layerPath: win32more.Foundation.PWSTR, layerData: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsDetachLayerStorageFilter(layerPath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsFormatWritableLayerVhd(vhdHandle: win32more.Foundation.HANDLE) -> win32more.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsGetLayerVhdMountPath(vhdHandle: win32more.Foundation.HANDLE, mountPath: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsSetupBaseOSVolume(layerPath: win32more.Foundation.PWSTR, volumePath: win32more.Foundation.PWSTR, options: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
HCS_CREATE_OPTIONS = Int32
HcsCreateOptions_1: HCS_CREATE_OPTIONS = 65536
class HCS_CREATE_OPTIONS_1(Structure):
    Version: win32more.System.HostComputeSystem.HCS_CREATE_OPTIONS
    UserToken: win32more.Foundation.HANDLE
    SecurityDescriptor: POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)
    CallbackOptions: win32more.System.HostComputeSystem.HCS_EVENT_OPTIONS
    CallbackContext: c_void_p
    Callback: win32more.System.HostComputeSystem.HCS_EVENT_CALLBACK
class HCS_EVENT(Structure):
    Type: win32more.System.HostComputeSystem.HCS_EVENT_TYPE
    EventData: win32more.Foundation.PWSTR
    Operation: win32more.System.HostComputeSystem.HCS_OPERATION
@winfunctype_pointer
def HCS_EVENT_CALLBACK(event: POINTER(win32more.System.HostComputeSystem.HCS_EVENT_head), context: c_void_p) -> Void: ...
HCS_EVENT_OPTIONS = UInt32
HCS_EVENT_OPTIONS_HcsEventOptionNone: HCS_EVENT_OPTIONS = 0
HCS_EVENT_OPTIONS_HcsEventOptionEnableOperationCallbacks: HCS_EVENT_OPTIONS = 1
HCS_EVENT_TYPE = Int32
HCS_EVENT_TYPE_HcsEventInvalid: HCS_EVENT_TYPE = 0
HCS_EVENT_TYPE_HcsEventSystemExited: HCS_EVENT_TYPE = 1
HCS_EVENT_TYPE_HcsEventSystemCrashInitiated: HCS_EVENT_TYPE = 2
HCS_EVENT_TYPE_HcsEventSystemCrashReport: HCS_EVENT_TYPE = 3
HCS_EVENT_TYPE_HcsEventSystemRdpEnhancedModeStateChanged: HCS_EVENT_TYPE = 4
HCS_EVENT_TYPE_HcsEventSystemSiloJobCreated: HCS_EVENT_TYPE = 5
HCS_EVENT_TYPE_HcsEventSystemGuestConnectionClosed: HCS_EVENT_TYPE = 6
HCS_EVENT_TYPE_HcsEventProcessExited: HCS_EVENT_TYPE = 65536
HCS_EVENT_TYPE_HcsEventOperationCallback: HCS_EVENT_TYPE = 16777216
HCS_EVENT_TYPE_HcsEventServiceDisconnect: HCS_EVENT_TYPE = 33554432
@winfunctype_pointer
def HCS_NOTIFICATION_CALLBACK(notificationType: UInt32, context: c_void_p, notificationStatus: win32more.Foundation.HRESULT, notificationData: win32more.Foundation.PWSTR) -> Void: ...
HCS_NOTIFICATION_FLAGS = Int32
HCS_NOTIFICATION_FLAGS_HcsNotificationFlagSuccess: HCS_NOTIFICATION_FLAGS = 0
HCS_NOTIFICATION_FLAGS_HcsNotificationFlagFailure: HCS_NOTIFICATION_FLAGS = -2147483648
HCS_NOTIFICATIONS = Int32
HCS_NOTIFICATIONS_HcsNotificationInvalid: HCS_NOTIFICATIONS = 0
HCS_NOTIFICATIONS_HcsNotificationSystemExited: HCS_NOTIFICATIONS = 1
HCS_NOTIFICATIONS_HcsNotificationSystemCreateCompleted: HCS_NOTIFICATIONS = 2
HCS_NOTIFICATIONS_HcsNotificationSystemStartCompleted: HCS_NOTIFICATIONS = 3
HCS_NOTIFICATIONS_HcsNotificationSystemPauseCompleted: HCS_NOTIFICATIONS = 4
HCS_NOTIFICATIONS_HcsNotificationSystemResumeCompleted: HCS_NOTIFICATIONS = 5
HCS_NOTIFICATIONS_HcsNotificationSystemCrashReport: HCS_NOTIFICATIONS = 6
HCS_NOTIFICATIONS_HcsNotificationSystemSiloJobCreated: HCS_NOTIFICATIONS = 7
HCS_NOTIFICATIONS_HcsNotificationSystemSaveCompleted: HCS_NOTIFICATIONS = 8
HCS_NOTIFICATIONS_HcsNotificationSystemRdpEnhancedModeStateChanged: HCS_NOTIFICATIONS = 9
HCS_NOTIFICATIONS_HcsNotificationSystemShutdownFailed: HCS_NOTIFICATIONS = 10
HCS_NOTIFICATIONS_HcsNotificationSystemShutdownCompleted: HCS_NOTIFICATIONS = 10
HCS_NOTIFICATIONS_HcsNotificationSystemGetPropertiesCompleted: HCS_NOTIFICATIONS = 11
HCS_NOTIFICATIONS_HcsNotificationSystemModifyCompleted: HCS_NOTIFICATIONS = 12
HCS_NOTIFICATIONS_HcsNotificationSystemCrashInitiated: HCS_NOTIFICATIONS = 13
HCS_NOTIFICATIONS_HcsNotificationSystemGuestConnectionClosed: HCS_NOTIFICATIONS = 14
HCS_NOTIFICATIONS_HcsNotificationSystemOperationCompletion: HCS_NOTIFICATIONS = 15
HCS_NOTIFICATIONS_HcsNotificationSystemPassThru: HCS_NOTIFICATIONS = 16
HCS_NOTIFICATIONS_HcsNotificationProcessExited: HCS_NOTIFICATIONS = 65536
HCS_NOTIFICATIONS_HcsNotificationServiceDisconnect: HCS_NOTIFICATIONS = 16777216
HCS_NOTIFICATIONS_HcsNotificationFlagsReserved: HCS_NOTIFICATIONS = -268435456
HCS_OPERATION = IntPtr
@winfunctype_pointer
def HCS_OPERATION_COMPLETION(operation: win32more.System.HostComputeSystem.HCS_OPERATION, context: c_void_p) -> Void: ...
HCS_OPERATION_TYPE = Int32
HCS_OPERATION_TYPE_HcsOperationTypeNone: HCS_OPERATION_TYPE = -1
HCS_OPERATION_TYPE_HcsOperationTypeEnumerate: HCS_OPERATION_TYPE = 0
HCS_OPERATION_TYPE_HcsOperationTypeCreate: HCS_OPERATION_TYPE = 1
HCS_OPERATION_TYPE_HcsOperationTypeStart: HCS_OPERATION_TYPE = 2
HCS_OPERATION_TYPE_HcsOperationTypeShutdown: HCS_OPERATION_TYPE = 3
HCS_OPERATION_TYPE_HcsOperationTypePause: HCS_OPERATION_TYPE = 4
HCS_OPERATION_TYPE_HcsOperationTypeResume: HCS_OPERATION_TYPE = 5
HCS_OPERATION_TYPE_HcsOperationTypeSave: HCS_OPERATION_TYPE = 6
HCS_OPERATION_TYPE_HcsOperationTypeTerminate: HCS_OPERATION_TYPE = 7
HCS_OPERATION_TYPE_HcsOperationTypeModify: HCS_OPERATION_TYPE = 8
HCS_OPERATION_TYPE_HcsOperationTypeGetProperties: HCS_OPERATION_TYPE = 9
HCS_OPERATION_TYPE_HcsOperationTypeCreateProcess: HCS_OPERATION_TYPE = 10
HCS_OPERATION_TYPE_HcsOperationTypeSignalProcess: HCS_OPERATION_TYPE = 11
HCS_OPERATION_TYPE_HcsOperationTypeGetProcessInfo: HCS_OPERATION_TYPE = 12
HCS_OPERATION_TYPE_HcsOperationTypeGetProcessProperties: HCS_OPERATION_TYPE = 13
HCS_OPERATION_TYPE_HcsOperationTypeModifyProcess: HCS_OPERATION_TYPE = 14
HCS_OPERATION_TYPE_HcsOperationTypeCrash: HCS_OPERATION_TYPE = 15
HCS_PROCESS = IntPtr
class HCS_PROCESS_INFORMATION(Structure):
    ProcessId: UInt32
    Reserved: UInt32
    StdInput: win32more.Foundation.HANDLE
    StdOutput: win32more.Foundation.HANDLE
    StdError: win32more.Foundation.HANDLE
HCS_SYSTEM = IntPtr
make_head(_module, 'HCS_CREATE_OPTIONS_1')
make_head(_module, 'HCS_EVENT')
make_head(_module, 'HCS_EVENT_CALLBACK')
make_head(_module, 'HCS_NOTIFICATION_CALLBACK')
make_head(_module, 'HCS_OPERATION_COMPLETION')
make_head(_module, 'HCS_PROCESS_INFORMATION')
__all__ = [
    "HCS_CREATE_OPTIONS",
    "HCS_CREATE_OPTIONS_1",
    "HCS_EVENT",
    "HCS_EVENT_CALLBACK",
    "HCS_EVENT_OPTIONS",
    "HCS_EVENT_OPTIONS_HcsEventOptionEnableOperationCallbacks",
    "HCS_EVENT_OPTIONS_HcsEventOptionNone",
    "HCS_EVENT_TYPE",
    "HCS_EVENT_TYPE_HcsEventInvalid",
    "HCS_EVENT_TYPE_HcsEventOperationCallback",
    "HCS_EVENT_TYPE_HcsEventProcessExited",
    "HCS_EVENT_TYPE_HcsEventServiceDisconnect",
    "HCS_EVENT_TYPE_HcsEventSystemCrashInitiated",
    "HCS_EVENT_TYPE_HcsEventSystemCrashReport",
    "HCS_EVENT_TYPE_HcsEventSystemExited",
    "HCS_EVENT_TYPE_HcsEventSystemGuestConnectionClosed",
    "HCS_EVENT_TYPE_HcsEventSystemRdpEnhancedModeStateChanged",
    "HCS_EVENT_TYPE_HcsEventSystemSiloJobCreated",
    "HCS_NOTIFICATIONS",
    "HCS_NOTIFICATIONS_HcsNotificationFlagsReserved",
    "HCS_NOTIFICATIONS_HcsNotificationInvalid",
    "HCS_NOTIFICATIONS_HcsNotificationProcessExited",
    "HCS_NOTIFICATIONS_HcsNotificationServiceDisconnect",
    "HCS_NOTIFICATIONS_HcsNotificationSystemCrashInitiated",
    "HCS_NOTIFICATIONS_HcsNotificationSystemCrashReport",
    "HCS_NOTIFICATIONS_HcsNotificationSystemCreateCompleted",
    "HCS_NOTIFICATIONS_HcsNotificationSystemExited",
    "HCS_NOTIFICATIONS_HcsNotificationSystemGetPropertiesCompleted",
    "HCS_NOTIFICATIONS_HcsNotificationSystemGuestConnectionClosed",
    "HCS_NOTIFICATIONS_HcsNotificationSystemModifyCompleted",
    "HCS_NOTIFICATIONS_HcsNotificationSystemOperationCompletion",
    "HCS_NOTIFICATIONS_HcsNotificationSystemPassThru",
    "HCS_NOTIFICATIONS_HcsNotificationSystemPauseCompleted",
    "HCS_NOTIFICATIONS_HcsNotificationSystemRdpEnhancedModeStateChanged",
    "HCS_NOTIFICATIONS_HcsNotificationSystemResumeCompleted",
    "HCS_NOTIFICATIONS_HcsNotificationSystemSaveCompleted",
    "HCS_NOTIFICATIONS_HcsNotificationSystemShutdownCompleted",
    "HCS_NOTIFICATIONS_HcsNotificationSystemShutdownFailed",
    "HCS_NOTIFICATIONS_HcsNotificationSystemSiloJobCreated",
    "HCS_NOTIFICATIONS_HcsNotificationSystemStartCompleted",
    "HCS_NOTIFICATION_CALLBACK",
    "HCS_NOTIFICATION_FLAGS",
    "HCS_NOTIFICATION_FLAGS_HcsNotificationFlagFailure",
    "HCS_NOTIFICATION_FLAGS_HcsNotificationFlagSuccess",
    "HCS_OPERATION",
    "HCS_OPERATION_COMPLETION",
    "HCS_OPERATION_TYPE",
    "HCS_OPERATION_TYPE_HcsOperationTypeCrash",
    "HCS_OPERATION_TYPE_HcsOperationTypeCreate",
    "HCS_OPERATION_TYPE_HcsOperationTypeCreateProcess",
    "HCS_OPERATION_TYPE_HcsOperationTypeEnumerate",
    "HCS_OPERATION_TYPE_HcsOperationTypeGetProcessInfo",
    "HCS_OPERATION_TYPE_HcsOperationTypeGetProcessProperties",
    "HCS_OPERATION_TYPE_HcsOperationTypeGetProperties",
    "HCS_OPERATION_TYPE_HcsOperationTypeModify",
    "HCS_OPERATION_TYPE_HcsOperationTypeModifyProcess",
    "HCS_OPERATION_TYPE_HcsOperationTypeNone",
    "HCS_OPERATION_TYPE_HcsOperationTypePause",
    "HCS_OPERATION_TYPE_HcsOperationTypeResume",
    "HCS_OPERATION_TYPE_HcsOperationTypeSave",
    "HCS_OPERATION_TYPE_HcsOperationTypeShutdown",
    "HCS_OPERATION_TYPE_HcsOperationTypeSignalProcess",
    "HCS_OPERATION_TYPE_HcsOperationTypeStart",
    "HCS_OPERATION_TYPE_HcsOperationTypeTerminate",
    "HCS_PROCESS",
    "HCS_PROCESS_INFORMATION",
    "HCS_SYSTEM",
    "HcsAttachLayerStorageFilter",
    "HcsCancelOperation",
    "HcsCloseComputeSystem",
    "HcsCloseOperation",
    "HcsCloseProcess",
    "HcsCrashComputeSystem",
    "HcsCreateComputeSystem",
    "HcsCreateComputeSystemInNamespace",
    "HcsCreateEmptyGuestStateFile",
    "HcsCreateEmptyRuntimeStateFile",
    "HcsCreateOperation",
    "HcsCreateOptions_1",
    "HcsCreateProcess",
    "HcsDestroyLayer",
    "HcsDetachLayerStorageFilter",
    "HcsEnumerateComputeSystems",
    "HcsEnumerateComputeSystemsInNamespace",
    "HcsExportLayer",
    "HcsExportLegacyWritableLayer",
    "HcsFormatWritableLayerVhd",
    "HcsGetComputeSystemFromOperation",
    "HcsGetComputeSystemProperties",
    "HcsGetLayerVhdMountPath",
    "HcsGetOperationContext",
    "HcsGetOperationId",
    "HcsGetOperationResult",
    "HcsGetOperationResultAndProcessInfo",
    "HcsGetOperationType",
    "HcsGetProcessFromOperation",
    "HcsGetProcessInfo",
    "HcsGetProcessProperties",
    "HcsGetProcessorCompatibilityFromSavedState",
    "HcsGetServiceProperties",
    "HcsGrantVmAccess",
    "HcsGrantVmGroupAccess",
    "HcsImportLayer",
    "HcsInitializeLegacyWritableLayer",
    "HcsInitializeWritableLayer",
    "HcsModifyComputeSystem",
    "HcsModifyProcess",
    "HcsModifyServiceSettings",
    "HcsOpenComputeSystem",
    "HcsOpenComputeSystemInNamespace",
    "HcsOpenProcess",
    "HcsPauseComputeSystem",
    "HcsResumeComputeSystem",
    "HcsRevokeVmAccess",
    "HcsRevokeVmGroupAccess",
    "HcsSaveComputeSystem",
    "HcsSetComputeSystemCallback",
    "HcsSetOperationCallback",
    "HcsSetOperationContext",
    "HcsSetProcessCallback",
    "HcsSetupBaseOSLayer",
    "HcsSetupBaseOSVolume",
    "HcsShutDownComputeSystem",
    "HcsSignalProcess",
    "HcsStartComputeSystem",
    "HcsSubmitWerReport",
    "HcsTerminateComputeSystem",
    "HcsTerminateProcess",
    "HcsWaitForComputeSystemExit",
    "HcsWaitForOperationResult",
    "HcsWaitForOperationResultAndProcessInfo",
    "HcsWaitForProcessExit",
]
