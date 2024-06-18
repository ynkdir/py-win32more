from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.HostComputeSystem
@winfunctype('computecore.dll')
def HcsEnumerateComputeSystems(query: win32more.Windows.Win32.Foundation.PWSTR, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsEnumerateComputeSystemsInNamespace(idNamespace: win32more.Windows.Win32.Foundation.PWSTR, query: win32more.Windows.Win32.Foundation.PWSTR, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCreateOperation(context: VoidPtr, callback: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_COMPLETION) -> win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION: ...
@winfunctype('computecore.dll')
def HcsCreateOperationWithNotifications(eventTypes: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_OPTIONS, context: VoidPtr, callback: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_CALLBACK) -> win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION: ...
@winfunctype('computecore.dll')
def HcsCloseOperation(operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION) -> Void: ...
@winfunctype('computecore.dll')
def HcsGetOperationContext(operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION) -> VoidPtr: ...
@winfunctype('computecore.dll')
def HcsSetOperationContext(operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, context: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsGetComputeSystemFromOperation(operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION) -> win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM: ...
@winfunctype('computecore.dll')
def HcsGetProcessFromOperation(operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION) -> win32more.Windows.Win32.System.HostComputeSystem.HCS_PROCESS: ...
@winfunctype('computecore.dll')
def HcsGetOperationType(operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION) -> win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_TYPE: ...
@winfunctype('computecore.dll')
def HcsGetOperationId(operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION) -> UInt64: ...
@winfunctype('computecore.dll')
def HcsGetOperationResult(operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, resultDocument: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsGetOperationResultAndProcessInfo(operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, processInformation: POINTER(win32more.Windows.Win32.System.HostComputeSystem.HCS_PROCESS_INFORMATION), resultDocument: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsAddResourceToOperation(operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, type: win32more.Windows.Win32.System.HostComputeSystem.HCS_RESOURCE_TYPE, uri: win32more.Windows.Win32.Foundation.PWSTR, handle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsGetProcessorCompatibilityFromSavedState(RuntimeFileName: win32more.Windows.Win32.Foundation.PWSTR, ProcessorFeaturesString: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsWaitForOperationResult(operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, timeoutMs: UInt32, resultDocument: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsWaitForOperationResultAndProcessInfo(operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, timeoutMs: UInt32, processInformation: POINTER(win32more.Windows.Win32.System.HostComputeSystem.HCS_PROCESS_INFORMATION), resultDocument: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsSetOperationCallback(operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, context: VoidPtr, callback: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_COMPLETION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCancelOperation(operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCreateComputeSystem(id: win32more.Windows.Win32.Foundation.PWSTR, configuration: win32more.Windows.Win32.Foundation.PWSTR, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, securityDescriptor: POINTER(win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR), computeSystem: POINTER(win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCreateComputeSystemInNamespace(idNamespace: win32more.Windows.Win32.Foundation.PWSTR, id: win32more.Windows.Win32.Foundation.PWSTR, configuration: win32more.Windows.Win32.Foundation.PWSTR, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, options: POINTER(win32more.Windows.Win32.System.HostComputeSystem.HCS_CREATE_OPTIONS), computeSystem: POINTER(win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsOpenComputeSystem(id: win32more.Windows.Win32.Foundation.PWSTR, requestedAccess: UInt32, computeSystem: POINTER(win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsOpenComputeSystemInNamespace(idNamespace: win32more.Windows.Win32.Foundation.PWSTR, id: win32more.Windows.Win32.Foundation.PWSTR, requestedAccess: UInt32, computeSystem: POINTER(win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCloseComputeSystem(computeSystem: win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM) -> Void: ...
@winfunctype('computecore.dll')
def HcsStartComputeSystem(computeSystem: win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, options: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsShutDownComputeSystem(computeSystem: win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, options: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsTerminateComputeSystem(computeSystem: win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, options: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCrashComputeSystem(computeSystem: win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, options: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsPauseComputeSystem(computeSystem: win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, options: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsResumeComputeSystem(computeSystem: win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, options: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsSaveComputeSystem(computeSystem: win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, options: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsGetComputeSystemProperties(computeSystem: win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, propertyQuery: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsModifyComputeSystem(computeSystem: win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, configuration: win32more.Windows.Win32.Foundation.PWSTR, identity: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsWaitForComputeSystemExit(computeSystem: win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM, timeoutMs: UInt32, result: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsSetComputeSystemCallback(computeSystem: win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM, callbackOptions: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_OPTIONS, context: VoidPtr, callback: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_CALLBACK) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCreateProcess(computeSystem: win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM, processParameters: win32more.Windows.Win32.Foundation.PWSTR, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, securityDescriptor: POINTER(win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR), process: POINTER(win32more.Windows.Win32.System.HostComputeSystem.HCS_PROCESS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsOpenProcess(computeSystem: win32more.Windows.Win32.System.HostComputeSystem.HCS_SYSTEM, processId: UInt32, requestedAccess: UInt32, process: POINTER(win32more.Windows.Win32.System.HostComputeSystem.HCS_PROCESS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCloseProcess(process: win32more.Windows.Win32.System.HostComputeSystem.HCS_PROCESS) -> Void: ...
@winfunctype('computecore.dll')
def HcsTerminateProcess(process: win32more.Windows.Win32.System.HostComputeSystem.HCS_PROCESS, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, options: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsSignalProcess(process: win32more.Windows.Win32.System.HostComputeSystem.HCS_PROCESS, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, options: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsGetProcessInfo(process: win32more.Windows.Win32.System.HostComputeSystem.HCS_PROCESS, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsGetProcessProperties(process: win32more.Windows.Win32.System.HostComputeSystem.HCS_PROCESS, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, propertyQuery: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsModifyProcess(process: win32more.Windows.Win32.System.HostComputeSystem.HCS_PROCESS, operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, settings: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsSetProcessCallback(process: win32more.Windows.Win32.System.HostComputeSystem.HCS_PROCESS, callbackOptions: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_OPTIONS, context: VoidPtr, callback: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_CALLBACK) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsWaitForProcessExit(computeSystem: win32more.Windows.Win32.System.HostComputeSystem.HCS_PROCESS, timeoutMs: UInt32, result: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsGetServiceProperties(propertyQuery: win32more.Windows.Win32.Foundation.PWSTR, result: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsModifyServiceSettings(settings: win32more.Windows.Win32.Foundation.PWSTR, result: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsSubmitWerReport(settings: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCreateEmptyGuestStateFile(guestStateFilePath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsCreateEmptyRuntimeStateFile(runtimeStateFilePath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsGrantVmAccess(vmId: win32more.Windows.Win32.Foundation.PWSTR, filePath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsRevokeVmAccess(vmId: win32more.Windows.Win32.Foundation.PWSTR, filePath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsGrantVmGroupAccess(filePath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computecore.dll')
def HcsRevokeVmGroupAccess(filePath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsImportLayer(layerPath: win32more.Windows.Win32.Foundation.PWSTR, sourceFolderPath: win32more.Windows.Win32.Foundation.PWSTR, layerData: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsExportLayer(layerPath: win32more.Windows.Win32.Foundation.PWSTR, exportFolderPath: win32more.Windows.Win32.Foundation.PWSTR, layerData: win32more.Windows.Win32.Foundation.PWSTR, options: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsExportLegacyWritableLayer(writableLayerMountPath: win32more.Windows.Win32.Foundation.PWSTR, writableLayerFolderPath: win32more.Windows.Win32.Foundation.PWSTR, exportFolderPath: win32more.Windows.Win32.Foundation.PWSTR, layerData: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsDestroyLayer(layerPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsSetupBaseOSLayer(layerPath: win32more.Windows.Win32.Foundation.PWSTR, vhdHandle: win32more.Windows.Win32.Foundation.HANDLE, options: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsInitializeWritableLayer(writableLayerPath: win32more.Windows.Win32.Foundation.PWSTR, layerData: win32more.Windows.Win32.Foundation.PWSTR, options: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsInitializeLegacyWritableLayer(writableLayerMountPath: win32more.Windows.Win32.Foundation.PWSTR, writableLayerFolderPath: win32more.Windows.Win32.Foundation.PWSTR, layerData: win32more.Windows.Win32.Foundation.PWSTR, options: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsAttachLayerStorageFilter(layerPath: win32more.Windows.Win32.Foundation.PWSTR, layerData: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsDetachLayerStorageFilter(layerPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsFormatWritableLayerVhd(vhdHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsGetLayerVhdMountPath(vhdHandle: win32more.Windows.Win32.Foundation.HANDLE, mountPath: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('computestorage.dll')
def HcsSetupBaseOSVolume(layerPath: win32more.Windows.Win32.Foundation.PWSTR, volumePath: win32more.Windows.Win32.Foundation.PWSTR, options: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
HCS_CREATE_OPTIONS = Int32
HcsCreateOptions_1: win32more.Windows.Win32.System.HostComputeSystem.HCS_CREATE_OPTIONS = 65536
class HCS_CREATE_OPTIONS_1(Structure):
    Version: win32more.Windows.Win32.System.HostComputeSystem.HCS_CREATE_OPTIONS
    UserToken: win32more.Windows.Win32.Foundation.HANDLE
    SecurityDescriptor: POINTER(win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR)
    CallbackOptions: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_OPTIONS
    CallbackContext: VoidPtr
    Callback: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_CALLBACK
class HCS_EVENT(Structure):
    Type: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_TYPE
    EventData: win32more.Windows.Win32.Foundation.PWSTR
    Operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION
@winfunctype_pointer
def HCS_EVENT_CALLBACK(event: POINTER(win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT), context: VoidPtr) -> Void: ...
HCS_EVENT_OPTIONS = Int32
HcsEventOptionNone: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_OPTIONS = 0
HcsEventOptionEnableOperationCallbacks: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_OPTIONS = 1
HcsEventOptionEnableVmLifecycle: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_OPTIONS = 2
HCS_EVENT_TYPE = Int32
HcsEventInvalid: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_TYPE = 0
HcsEventSystemExited: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_TYPE = 1
HcsEventSystemCrashInitiated: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_TYPE = 2
HcsEventSystemCrashReport: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_TYPE = 3
HcsEventSystemRdpEnhancedModeStateChanged: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_TYPE = 4
HcsEventSystemSiloJobCreated: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_TYPE = 5
HcsEventSystemGuestConnectionClosed: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_TYPE = 6
HcsEventProcessExited: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_TYPE = 65536
HcsEventOperationCallback: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_TYPE = 16777216
HcsEventServiceDisconnect: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_TYPE = 33554432
HcsEventGroupVmLifecycle: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_TYPE = -2147483646
HcsEventGroupOperationInfo: win32more.Windows.Win32.System.HostComputeSystem.HCS_EVENT_TYPE = -1073741823
HCS_NOTIFICATIONS = Int32
HcsNotificationInvalid: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 0
HcsNotificationSystemExited: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 1
HcsNotificationSystemCreateCompleted: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 2
HcsNotificationSystemStartCompleted: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 3
HcsNotificationSystemPauseCompleted: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 4
HcsNotificationSystemResumeCompleted: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 5
HcsNotificationSystemCrashReport: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 6
HcsNotificationSystemSiloJobCreated: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 7
HcsNotificationSystemSaveCompleted: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 8
HcsNotificationSystemRdpEnhancedModeStateChanged: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 9
HcsNotificationSystemShutdownFailed: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 10
HcsNotificationSystemShutdownCompleted: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 10
HcsNotificationSystemGetPropertiesCompleted: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 11
HcsNotificationSystemModifyCompleted: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 12
HcsNotificationSystemCrashInitiated: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 13
HcsNotificationSystemGuestConnectionClosed: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 14
HcsNotificationSystemOperationCompletion: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 15
HcsNotificationSystemPassThru: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 16
HcsNotificationOperationProgressUpdate: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 256
HcsNotificationProcessExited: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 65536
HcsNotificationServiceDisconnect: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = 16777216
HcsNotificationFlagsReserved: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATIONS = -268435456
@winfunctype_pointer
def HCS_NOTIFICATION_CALLBACK(notificationType: UInt32, context: VoidPtr, notificationStatus: win32more.Windows.Win32.Foundation.HRESULT, notificationData: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
HCS_NOTIFICATION_FLAGS = Int32
HcsNotificationFlagSuccess: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATION_FLAGS = 0
HcsNotificationFlagFailure: win32more.Windows.Win32.System.HostComputeSystem.HCS_NOTIFICATION_FLAGS = -2147483648
HCS_OPERATION = VoidPtr
@winfunctype_pointer
def HCS_OPERATION_COMPLETION(operation: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION, context: VoidPtr) -> Void: ...
HCS_OPERATION_OPTIONS = Int32
HcsOperationOptionNone: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_OPTIONS = 0
HcsOperationOptionProgressUpdate: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_OPTIONS = 1
HCS_OPERATION_TYPE = Int32
HcsOperationTypeNone: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_TYPE = -1
HcsOperationTypeEnumerate: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_TYPE = 0
HcsOperationTypeCreate: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_TYPE = 1
HcsOperationTypeStart: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_TYPE = 2
HcsOperationTypeShutdown: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_TYPE = 3
HcsOperationTypePause: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_TYPE = 4
HcsOperationTypeResume: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_TYPE = 5
HcsOperationTypeSave: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_TYPE = 6
HcsOperationTypeTerminate: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_TYPE = 7
HcsOperationTypeModify: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_TYPE = 8
HcsOperationTypeGetProperties: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_TYPE = 9
HcsOperationTypeCreateProcess: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_TYPE = 10
HcsOperationTypeSignalProcess: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_TYPE = 11
HcsOperationTypeGetProcessInfo: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_TYPE = 12
HcsOperationTypeGetProcessProperties: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_TYPE = 13
HcsOperationTypeModifyProcess: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_TYPE = 14
HcsOperationTypeCrash: win32more.Windows.Win32.System.HostComputeSystem.HCS_OPERATION_TYPE = 15
HCS_PROCESS = VoidPtr
class HCS_PROCESS_INFORMATION(Structure):
    ProcessId: UInt32
    Reserved: UInt32
    StdInput: win32more.Windows.Win32.Foundation.HANDLE
    StdOutput: win32more.Windows.Win32.Foundation.HANDLE
    StdError: win32more.Windows.Win32.Foundation.HANDLE
HCS_RESOURCE_TYPE = Int32
HcsResourceTypeNone: win32more.Windows.Win32.System.HostComputeSystem.HCS_RESOURCE_TYPE = 0
HcsResourceTypeFile: win32more.Windows.Win32.System.HostComputeSystem.HCS_RESOURCE_TYPE = 1
HcsResourceTypeJob: win32more.Windows.Win32.System.HostComputeSystem.HCS_RESOURCE_TYPE = 2
HCS_SYSTEM = VoidPtr


make_ready(__name__)
