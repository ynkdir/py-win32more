from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Security
import win32more.System.HostComputeSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_HcsEnumerateComputeSystems():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.HostComputeSystem.HCS_OPERATION)(('HcsEnumerateComputeSystems', windll['computecore.dll']), ((1, 'query'),(1, 'operation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsEnumerateComputeSystemsInNamespace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.HostComputeSystem.HCS_OPERATION)(('HcsEnumerateComputeSystemsInNamespace', windll['computecore.dll']), ((1, 'idNamespace'),(1, 'query'),(1, 'operation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsCreateOperation():
    try:
        return WINFUNCTYPE(win32more.System.HostComputeSystem.HCS_OPERATION,c_void_p,win32more.System.HostComputeSystem.HCS_OPERATION_COMPLETION)(('HcsCreateOperation', windll['computecore.dll']), ((1, 'context'),(1, 'callback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsCloseOperation():
    try:
        return WINFUNCTYPE(Void,win32more.System.HostComputeSystem.HCS_OPERATION)(('HcsCloseOperation', windll['computecore.dll']), ((1, 'operation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsGetOperationContext():
    try:
        return WINFUNCTYPE(c_void_p,win32more.System.HostComputeSystem.HCS_OPERATION)(('HcsGetOperationContext', windll['computecore.dll']), ((1, 'operation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsSetOperationContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_OPERATION,c_void_p)(('HcsSetOperationContext', windll['computecore.dll']), ((1, 'operation'),(1, 'context'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsGetComputeSystemFromOperation():
    try:
        return WINFUNCTYPE(win32more.System.HostComputeSystem.HCS_SYSTEM,win32more.System.HostComputeSystem.HCS_OPERATION)(('HcsGetComputeSystemFromOperation', windll['computecore.dll']), ((1, 'operation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsGetProcessFromOperation():
    try:
        return WINFUNCTYPE(win32more.System.HostComputeSystem.HCS_PROCESS,win32more.System.HostComputeSystem.HCS_OPERATION)(('HcsGetProcessFromOperation', windll['computecore.dll']), ((1, 'operation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsGetOperationType():
    try:
        return WINFUNCTYPE(win32more.System.HostComputeSystem.HCS_OPERATION_TYPE,win32more.System.HostComputeSystem.HCS_OPERATION)(('HcsGetOperationType', windll['computecore.dll']), ((1, 'operation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsGetOperationId():
    try:
        return WINFUNCTYPE(UInt64,win32more.System.HostComputeSystem.HCS_OPERATION)(('HcsGetOperationId', windll['computecore.dll']), ((1, 'operation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsGetOperationResult():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_OPERATION,POINTER(win32more.Foundation.PWSTR))(('HcsGetOperationResult', windll['computecore.dll']), ((1, 'operation'),(1, 'resultDocument'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsGetOperationResultAndProcessInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_OPERATION,POINTER(win32more.System.HostComputeSystem.HCS_PROCESS_INFORMATION_head),POINTER(win32more.Foundation.PWSTR))(('HcsGetOperationResultAndProcessInfo', windll['computecore.dll']), ((1, 'operation'),(1, 'processInformation'),(1, 'resultDocument'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsGetProcessorCompatibilityFromSavedState():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR))(('HcsGetProcessorCompatibilityFromSavedState', windll['computecore.dll']), ((1, 'RuntimeFileName'),(1, 'ProcessorFeaturesString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsWaitForOperationResult():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_OPERATION,UInt32,POINTER(win32more.Foundation.PWSTR))(('HcsWaitForOperationResult', windll['computecore.dll']), ((1, 'operation'),(1, 'timeoutMs'),(1, 'resultDocument'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsWaitForOperationResultAndProcessInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_OPERATION,UInt32,POINTER(win32more.System.HostComputeSystem.HCS_PROCESS_INFORMATION_head),POINTER(win32more.Foundation.PWSTR))(('HcsWaitForOperationResultAndProcessInfo', windll['computecore.dll']), ((1, 'operation'),(1, 'timeoutMs'),(1, 'processInformation'),(1, 'resultDocument'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsSetOperationCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_OPERATION,c_void_p,win32more.System.HostComputeSystem.HCS_OPERATION_COMPLETION)(('HcsSetOperationCallback', windll['computecore.dll']), ((1, 'operation'),(1, 'context'),(1, 'callback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsCancelOperation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_OPERATION)(('HcsCancelOperation', windll['computecore.dll']), ((1, 'operation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsCreateComputeSystem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.HostComputeSystem.HCS_OPERATION,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(win32more.System.HostComputeSystem.HCS_SYSTEM))(('HcsCreateComputeSystem', windll['computecore.dll']), ((1, 'id'),(1, 'configuration'),(1, 'operation'),(1, 'securityDescriptor'),(1, 'computeSystem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsCreateComputeSystemInNamespace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.HostComputeSystem.HCS_OPERATION,POINTER(win32more.System.HostComputeSystem.HCS_CREATE_OPTIONS),POINTER(win32more.System.HostComputeSystem.HCS_SYSTEM))(('HcsCreateComputeSystemInNamespace', windll['computecore.dll']), ((1, 'idNamespace'),(1, 'id'),(1, 'configuration'),(1, 'operation'),(1, 'options'),(1, 'computeSystem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsOpenComputeSystem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.System.HostComputeSystem.HCS_SYSTEM))(('HcsOpenComputeSystem', windll['computecore.dll']), ((1, 'id'),(1, 'requestedAccess'),(1, 'computeSystem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsOpenComputeSystemInNamespace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.System.HostComputeSystem.HCS_SYSTEM))(('HcsOpenComputeSystemInNamespace', windll['computecore.dll']), ((1, 'idNamespace'),(1, 'id'),(1, 'requestedAccess'),(1, 'computeSystem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsCloseComputeSystem():
    try:
        return WINFUNCTYPE(Void,win32more.System.HostComputeSystem.HCS_SYSTEM)(('HcsCloseComputeSystem', windll['computecore.dll']), ((1, 'computeSystem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsStartComputeSystem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_SYSTEM,win32more.System.HostComputeSystem.HCS_OPERATION,win32more.Foundation.PWSTR)(('HcsStartComputeSystem', windll['computecore.dll']), ((1, 'computeSystem'),(1, 'operation'),(1, 'options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsShutDownComputeSystem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_SYSTEM,win32more.System.HostComputeSystem.HCS_OPERATION,win32more.Foundation.PWSTR)(('HcsShutDownComputeSystem', windll['computecore.dll']), ((1, 'computeSystem'),(1, 'operation'),(1, 'options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsTerminateComputeSystem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_SYSTEM,win32more.System.HostComputeSystem.HCS_OPERATION,win32more.Foundation.PWSTR)(('HcsTerminateComputeSystem', windll['computecore.dll']), ((1, 'computeSystem'),(1, 'operation'),(1, 'options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsCrashComputeSystem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_SYSTEM,win32more.System.HostComputeSystem.HCS_OPERATION,win32more.Foundation.PWSTR)(('HcsCrashComputeSystem', windll['computecore.dll']), ((1, 'computeSystem'),(1, 'operation'),(1, 'options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsPauseComputeSystem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_SYSTEM,win32more.System.HostComputeSystem.HCS_OPERATION,win32more.Foundation.PWSTR)(('HcsPauseComputeSystem', windll['computecore.dll']), ((1, 'computeSystem'),(1, 'operation'),(1, 'options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsResumeComputeSystem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_SYSTEM,win32more.System.HostComputeSystem.HCS_OPERATION,win32more.Foundation.PWSTR)(('HcsResumeComputeSystem', windll['computecore.dll']), ((1, 'computeSystem'),(1, 'operation'),(1, 'options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsSaveComputeSystem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_SYSTEM,win32more.System.HostComputeSystem.HCS_OPERATION,win32more.Foundation.PWSTR)(('HcsSaveComputeSystem', windll['computecore.dll']), ((1, 'computeSystem'),(1, 'operation'),(1, 'options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsGetComputeSystemProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_SYSTEM,win32more.System.HostComputeSystem.HCS_OPERATION,win32more.Foundation.PWSTR)(('HcsGetComputeSystemProperties', windll['computecore.dll']), ((1, 'computeSystem'),(1, 'operation'),(1, 'propertyQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsModifyComputeSystem():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_SYSTEM,win32more.System.HostComputeSystem.HCS_OPERATION,win32more.Foundation.PWSTR,win32more.Foundation.HANDLE)(('HcsModifyComputeSystem', windll['computecore.dll']), ((1, 'computeSystem'),(1, 'operation'),(1, 'configuration'),(1, 'identity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsWaitForComputeSystemExit():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_SYSTEM,UInt32,POINTER(win32more.Foundation.PWSTR))(('HcsWaitForComputeSystemExit', windll['computecore.dll']), ((1, 'computeSystem'),(1, 'timeoutMs'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsSetComputeSystemCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_SYSTEM,win32more.System.HostComputeSystem.HCS_EVENT_OPTIONS,c_void_p,win32more.System.HostComputeSystem.HCS_EVENT_CALLBACK)(('HcsSetComputeSystemCallback', windll['computecore.dll']), ((1, 'computeSystem'),(1, 'callbackOptions'),(1, 'context'),(1, 'callback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsCreateProcess():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_SYSTEM,win32more.Foundation.PWSTR,win32more.System.HostComputeSystem.HCS_OPERATION,POINTER(win32more.Security.SECURITY_DESCRIPTOR_head),POINTER(win32more.System.HostComputeSystem.HCS_PROCESS))(('HcsCreateProcess', windll['computecore.dll']), ((1, 'computeSystem'),(1, 'processParameters'),(1, 'operation'),(1, 'securityDescriptor'),(1, 'process'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsOpenProcess():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_SYSTEM,UInt32,UInt32,POINTER(win32more.System.HostComputeSystem.HCS_PROCESS))(('HcsOpenProcess', windll['computecore.dll']), ((1, 'computeSystem'),(1, 'processId'),(1, 'requestedAccess'),(1, 'process'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsCloseProcess():
    try:
        return WINFUNCTYPE(Void,win32more.System.HostComputeSystem.HCS_PROCESS)(('HcsCloseProcess', windll['computecore.dll']), ((1, 'process'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsTerminateProcess():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_PROCESS,win32more.System.HostComputeSystem.HCS_OPERATION,win32more.Foundation.PWSTR)(('HcsTerminateProcess', windll['computecore.dll']), ((1, 'process'),(1, 'operation'),(1, 'options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsSignalProcess():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_PROCESS,win32more.System.HostComputeSystem.HCS_OPERATION,win32more.Foundation.PWSTR)(('HcsSignalProcess', windll['computecore.dll']), ((1, 'process'),(1, 'operation'),(1, 'options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsGetProcessInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_PROCESS,win32more.System.HostComputeSystem.HCS_OPERATION)(('HcsGetProcessInfo', windll['computecore.dll']), ((1, 'process'),(1, 'operation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsGetProcessProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_PROCESS,win32more.System.HostComputeSystem.HCS_OPERATION,win32more.Foundation.PWSTR)(('HcsGetProcessProperties', windll['computecore.dll']), ((1, 'process'),(1, 'operation'),(1, 'propertyQuery'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsModifyProcess():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_PROCESS,win32more.System.HostComputeSystem.HCS_OPERATION,win32more.Foundation.PWSTR)(('HcsModifyProcess', windll['computecore.dll']), ((1, 'process'),(1, 'operation'),(1, 'settings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsSetProcessCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_PROCESS,win32more.System.HostComputeSystem.HCS_EVENT_OPTIONS,c_void_p,win32more.System.HostComputeSystem.HCS_EVENT_CALLBACK)(('HcsSetProcessCallback', windll['computecore.dll']), ((1, 'process'),(1, 'callbackOptions'),(1, 'context'),(1, 'callback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsWaitForProcessExit():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.HostComputeSystem.HCS_PROCESS,UInt32,POINTER(win32more.Foundation.PWSTR))(('HcsWaitForProcessExit', windll['computecore.dll']), ((1, 'computeSystem'),(1, 'timeoutMs'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsGetServiceProperties():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR))(('HcsGetServiceProperties', windll['computecore.dll']), ((1, 'propertyQuery'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsModifyServiceSettings():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR))(('HcsModifyServiceSettings', windll['computecore.dll']), ((1, 'settings'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsSubmitWerReport():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(('HcsSubmitWerReport', windll['computecore.dll']), ((1, 'settings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsCreateEmptyGuestStateFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(('HcsCreateEmptyGuestStateFile', windll['computecore.dll']), ((1, 'guestStateFilePath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsCreateEmptyRuntimeStateFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(('HcsCreateEmptyRuntimeStateFile', windll['computecore.dll']), ((1, 'runtimeStateFilePath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsGrantVmAccess():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('HcsGrantVmAccess', windll['computecore.dll']), ((1, 'vmId'),(1, 'filePath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsRevokeVmAccess():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('HcsRevokeVmAccess', windll['computecore.dll']), ((1, 'vmId'),(1, 'filePath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsGrantVmGroupAccess():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(('HcsGrantVmGroupAccess', windll['computecore.dll']), ((1, 'filePath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsRevokeVmGroupAccess():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(('HcsRevokeVmGroupAccess', windll['computecore.dll']), ((1, 'filePath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsImportLayer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('HcsImportLayer', windll['computestorage.dll']), ((1, 'layerPath'),(1, 'sourceFolderPath'),(1, 'layerData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsExportLayer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('HcsExportLayer', windll['computestorage.dll']), ((1, 'layerPath'),(1, 'exportFolderPath'),(1, 'layerData'),(1, 'options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsExportLegacyWritableLayer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('HcsExportLegacyWritableLayer', windll['computestorage.dll']), ((1, 'writableLayerMountPath'),(1, 'writableLayerFolderPath'),(1, 'exportFolderPath'),(1, 'layerData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsDestroyLayer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(('HcsDestroyLayer', windll['computestorage.dll']), ((1, 'layerPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsSetupBaseOSLayer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR)(('HcsSetupBaseOSLayer', windll['computestorage.dll']), ((1, 'layerPath'),(1, 'vhdHandle'),(1, 'options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsInitializeWritableLayer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('HcsInitializeWritableLayer', windll['computestorage.dll']), ((1, 'writableLayerPath'),(1, 'layerData'),(1, 'options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsInitializeLegacyWritableLayer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('HcsInitializeLegacyWritableLayer', windll['computestorage.dll']), ((1, 'writableLayerMountPath'),(1, 'writableLayerFolderPath'),(1, 'layerData'),(1, 'options'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsAttachLayerStorageFilter():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('HcsAttachLayerStorageFilter', windll['computestorage.dll']), ((1, 'layerPath'),(1, 'layerData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsDetachLayerStorageFilter():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(('HcsDetachLayerStorageFilter', windll['computestorage.dll']), ((1, 'layerPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsFormatWritableLayerVhd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE)(('HcsFormatWritableLayerVhd', windll['computestorage.dll']), ((1, 'vhdHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsGetLayerVhdMountPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.PWSTR))(('HcsGetLayerVhdMountPath', windll['computestorage.dll']), ((1, 'vhdHandle'),(1, 'mountPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HcsSetupBaseOSVolume():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('HcsSetupBaseOSVolume', windll['computestorage.dll']), ((1, 'layerPath'),(1, 'volumePath'),(1, 'options'),))
    except (FileNotFoundError, AttributeError):
        return None
HCS_CREATE_OPTIONS = Int32
HcsCreateOptions_1 = 65536
def _define_HCS_CREATE_OPTIONS_1_head():
    class HCS_CREATE_OPTIONS_1(Structure):
        pass
    return HCS_CREATE_OPTIONS_1
def _define_HCS_CREATE_OPTIONS_1():
    HCS_CREATE_OPTIONS_1 = win32more.System.HostComputeSystem.HCS_CREATE_OPTIONS_1_head
    HCS_CREATE_OPTIONS_1._fields_ = [
        ('Version', win32more.System.HostComputeSystem.HCS_CREATE_OPTIONS),
        ('UserToken', win32more.Foundation.HANDLE),
        ('SecurityDescriptor', POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),
        ('CallbackOptions', win32more.System.HostComputeSystem.HCS_EVENT_OPTIONS),
        ('CallbackContext', c_void_p),
        ('Callback', win32more.System.HostComputeSystem.HCS_EVENT_CALLBACK),
    ]
    return HCS_CREATE_OPTIONS_1
def _define_HCS_EVENT_head():
    class HCS_EVENT(Structure):
        pass
    return HCS_EVENT
def _define_HCS_EVENT():
    HCS_EVENT = win32more.System.HostComputeSystem.HCS_EVENT_head
    HCS_EVENT._fields_ = [
        ('Type', win32more.System.HostComputeSystem.HCS_EVENT_TYPE),
        ('EventData', win32more.Foundation.PWSTR),
        ('Operation', win32more.System.HostComputeSystem.HCS_OPERATION),
    ]
    return HCS_EVENT
def _define_HCS_EVENT_CALLBACK():
    return WINFUNCTYPE(Void,POINTER(win32more.System.HostComputeSystem.HCS_EVENT_head),c_void_p)
HCS_EVENT_OPTIONS = UInt32
HCS_EVENT_OPTIONS_HcsEventOptionNone = 0
HCS_EVENT_OPTIONS_HcsEventOptionEnableOperationCallbacks = 1
HCS_EVENT_TYPE = Int32
HCS_EVENT_TYPE_HcsEventInvalid = 0
HCS_EVENT_TYPE_HcsEventSystemExited = 1
HCS_EVENT_TYPE_HcsEventSystemCrashInitiated = 2
HCS_EVENT_TYPE_HcsEventSystemCrashReport = 3
HCS_EVENT_TYPE_HcsEventSystemRdpEnhancedModeStateChanged = 4
HCS_EVENT_TYPE_HcsEventSystemSiloJobCreated = 5
HCS_EVENT_TYPE_HcsEventSystemGuestConnectionClosed = 6
HCS_EVENT_TYPE_HcsEventProcessExited = 65536
HCS_EVENT_TYPE_HcsEventOperationCallback = 16777216
HCS_EVENT_TYPE_HcsEventServiceDisconnect = 33554432
def _define_HCS_NOTIFICATION_CALLBACK():
    return WINFUNCTYPE(Void,UInt32,c_void_p,win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)
HCS_NOTIFICATION_FLAGS = Int32
HCS_NOTIFICATION_FLAGS_HcsNotificationFlagSuccess = 0
HCS_NOTIFICATION_FLAGS_HcsNotificationFlagFailure = -2147483648
HCS_NOTIFICATIONS = Int32
HCS_NOTIFICATIONS_HcsNotificationInvalid = 0
HCS_NOTIFICATIONS_HcsNotificationSystemExited = 1
HCS_NOTIFICATIONS_HcsNotificationSystemCreateCompleted = 2
HCS_NOTIFICATIONS_HcsNotificationSystemStartCompleted = 3
HCS_NOTIFICATIONS_HcsNotificationSystemPauseCompleted = 4
HCS_NOTIFICATIONS_HcsNotificationSystemResumeCompleted = 5
HCS_NOTIFICATIONS_HcsNotificationSystemCrashReport = 6
HCS_NOTIFICATIONS_HcsNotificationSystemSiloJobCreated = 7
HCS_NOTIFICATIONS_HcsNotificationSystemSaveCompleted = 8
HCS_NOTIFICATIONS_HcsNotificationSystemRdpEnhancedModeStateChanged = 9
HCS_NOTIFICATIONS_HcsNotificationSystemShutdownFailed = 10
HCS_NOTIFICATIONS_HcsNotificationSystemShutdownCompleted = 10
HCS_NOTIFICATIONS_HcsNotificationSystemGetPropertiesCompleted = 11
HCS_NOTIFICATIONS_HcsNotificationSystemModifyCompleted = 12
HCS_NOTIFICATIONS_HcsNotificationSystemCrashInitiated = 13
HCS_NOTIFICATIONS_HcsNotificationSystemGuestConnectionClosed = 14
HCS_NOTIFICATIONS_HcsNotificationSystemOperationCompletion = 15
HCS_NOTIFICATIONS_HcsNotificationSystemPassThru = 16
HCS_NOTIFICATIONS_HcsNotificationProcessExited = 65536
HCS_NOTIFICATIONS_HcsNotificationServiceDisconnect = 16777216
HCS_NOTIFICATIONS_HcsNotificationFlagsReserved = -268435456
HCS_OPERATION = IntPtr
def _define_HCS_OPERATION_COMPLETION():
    return WINFUNCTYPE(Void,win32more.System.HostComputeSystem.HCS_OPERATION,c_void_p)
HCS_OPERATION_TYPE = Int32
HCS_OPERATION_TYPE_HcsOperationTypeNone = -1
HCS_OPERATION_TYPE_HcsOperationTypeEnumerate = 0
HCS_OPERATION_TYPE_HcsOperationTypeCreate = 1
HCS_OPERATION_TYPE_HcsOperationTypeStart = 2
HCS_OPERATION_TYPE_HcsOperationTypeShutdown = 3
HCS_OPERATION_TYPE_HcsOperationTypePause = 4
HCS_OPERATION_TYPE_HcsOperationTypeResume = 5
HCS_OPERATION_TYPE_HcsOperationTypeSave = 6
HCS_OPERATION_TYPE_HcsOperationTypeTerminate = 7
HCS_OPERATION_TYPE_HcsOperationTypeModify = 8
HCS_OPERATION_TYPE_HcsOperationTypeGetProperties = 9
HCS_OPERATION_TYPE_HcsOperationTypeCreateProcess = 10
HCS_OPERATION_TYPE_HcsOperationTypeSignalProcess = 11
HCS_OPERATION_TYPE_HcsOperationTypeGetProcessInfo = 12
HCS_OPERATION_TYPE_HcsOperationTypeGetProcessProperties = 13
HCS_OPERATION_TYPE_HcsOperationTypeModifyProcess = 14
HCS_OPERATION_TYPE_HcsOperationTypeCrash = 15
HCS_PROCESS = IntPtr
def _define_HCS_PROCESS_INFORMATION_head():
    class HCS_PROCESS_INFORMATION(Structure):
        pass
    return HCS_PROCESS_INFORMATION
def _define_HCS_PROCESS_INFORMATION():
    HCS_PROCESS_INFORMATION = win32more.System.HostComputeSystem.HCS_PROCESS_INFORMATION_head
    HCS_PROCESS_INFORMATION._fields_ = [
        ('ProcessId', UInt32),
        ('Reserved', UInt32),
        ('StdInput', win32more.Foundation.HANDLE),
        ('StdOutput', win32more.Foundation.HANDLE),
        ('StdError', win32more.Foundation.HANDLE),
    ]
    return HCS_PROCESS_INFORMATION
HCS_SYSTEM = IntPtr
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
