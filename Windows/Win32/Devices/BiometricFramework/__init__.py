from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Devices.BiometricFramework
import Windows.Win32.Foundation
import Windows.Win32.System.IO
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
WINBIO_MAX_STRING_LEN: UInt32 = 256
WINBIO_SCP_VERSION_1: UInt32 = 1
WINBIO_SCP_RANDOM_SIZE_V1: UInt32 = 32
WINBIO_SCP_DIGEST_SIZE_V1: UInt32 = 32
WINBIO_SCP_CURVE_FIELD_SIZE_V1: UInt32 = 32
WINBIO_SCP_PUBLIC_KEY_SIZE_V1: UInt32 = 65
WINBIO_SCP_PRIVATE_KEY_SIZE_V1: UInt32 = 32
WINBIO_SCP_SIGNATURE_SIZE_V1: UInt32 = 64
WINBIO_SCP_ENCRYPTION_BLOCK_SIZE_V1: UInt32 = 16
WINBIO_SCP_ENCRYPTION_KEY_SIZE_V1: UInt32 = 32
WINBIO_BIR_ALIGN_SIZE: UInt32 = 8
WINBIO_BIR_ALGIN_SIZE: UInt32 = 8
FACILITY_WINBIO: UInt32 = 9
FACILITY_NONE: UInt32 = 0
WINBIO_E_UNSUPPORTED_FACTOR: Windows.Win32.Foundation.HRESULT = -2146861055
WINBIO_E_INVALID_UNIT: Windows.Win32.Foundation.HRESULT = -2146861054
WINBIO_E_UNKNOWN_ID: Windows.Win32.Foundation.HRESULT = -2146861053
WINBIO_E_CANCELED: Windows.Win32.Foundation.HRESULT = -2146861052
WINBIO_E_NO_MATCH: Windows.Win32.Foundation.HRESULT = -2146861051
WINBIO_E_CAPTURE_ABORTED: Windows.Win32.Foundation.HRESULT = -2146861050
WINBIO_E_ENROLLMENT_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = -2146861049
WINBIO_E_BAD_CAPTURE: Windows.Win32.Foundation.HRESULT = -2146861048
WINBIO_E_INVALID_CONTROL_CODE: Windows.Win32.Foundation.HRESULT = -2146861047
WINBIO_E_DATA_COLLECTION_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = -2146861045
WINBIO_E_UNSUPPORTED_DATA_FORMAT: Windows.Win32.Foundation.HRESULT = -2146861044
WINBIO_E_UNSUPPORTED_DATA_TYPE: Windows.Win32.Foundation.HRESULT = -2146861043
WINBIO_E_UNSUPPORTED_PURPOSE: Windows.Win32.Foundation.HRESULT = -2146861042
WINBIO_E_INVALID_DEVICE_STATE: Windows.Win32.Foundation.HRESULT = -2146861041
WINBIO_E_DEVICE_BUSY: Windows.Win32.Foundation.HRESULT = -2146861040
WINBIO_E_DATABASE_CANT_CREATE: Windows.Win32.Foundation.HRESULT = -2146861039
WINBIO_E_DATABASE_CANT_OPEN: Windows.Win32.Foundation.HRESULT = -2146861038
WINBIO_E_DATABASE_CANT_CLOSE: Windows.Win32.Foundation.HRESULT = -2146861037
WINBIO_E_DATABASE_CANT_ERASE: Windows.Win32.Foundation.HRESULT = -2146861036
WINBIO_E_DATABASE_CANT_FIND: Windows.Win32.Foundation.HRESULT = -2146861035
WINBIO_E_DATABASE_ALREADY_EXISTS: Windows.Win32.Foundation.HRESULT = -2146861034
WINBIO_E_DATABASE_FULL: Windows.Win32.Foundation.HRESULT = -2146861032
WINBIO_E_DATABASE_LOCKED: Windows.Win32.Foundation.HRESULT = -2146861031
WINBIO_E_DATABASE_CORRUPTED: Windows.Win32.Foundation.HRESULT = -2146861030
WINBIO_E_DATABASE_NO_SUCH_RECORD: Windows.Win32.Foundation.HRESULT = -2146861029
WINBIO_E_DUPLICATE_ENROLLMENT: Windows.Win32.Foundation.HRESULT = -2146861028
WINBIO_E_DATABASE_READ_ERROR: Windows.Win32.Foundation.HRESULT = -2146861027
WINBIO_E_DATABASE_WRITE_ERROR: Windows.Win32.Foundation.HRESULT = -2146861026
WINBIO_E_DATABASE_NO_RESULTS: Windows.Win32.Foundation.HRESULT = -2146861025
WINBIO_E_DATABASE_NO_MORE_RECORDS: Windows.Win32.Foundation.HRESULT = -2146861024
WINBIO_E_DATABASE_EOF: Windows.Win32.Foundation.HRESULT = -2146861023
WINBIO_E_DATABASE_BAD_INDEX_VECTOR: Windows.Win32.Foundation.HRESULT = -2146861022
WINBIO_E_INCORRECT_BSP: Windows.Win32.Foundation.HRESULT = -2146861020
WINBIO_E_INCORRECT_SENSOR_POOL: Windows.Win32.Foundation.HRESULT = -2146861019
WINBIO_E_NO_CAPTURE_DATA: Windows.Win32.Foundation.HRESULT = -2146861018
WINBIO_E_INVALID_SENSOR_MODE: Windows.Win32.Foundation.HRESULT = -2146861017
WINBIO_E_LOCK_VIOLATION: Windows.Win32.Foundation.HRESULT = -2146861014
WINBIO_E_DUPLICATE_TEMPLATE: Windows.Win32.Foundation.HRESULT = -2146861013
WINBIO_E_INVALID_OPERATION: Windows.Win32.Foundation.HRESULT = -2146861012
WINBIO_E_SESSION_BUSY: Windows.Win32.Foundation.HRESULT = -2146861011
WINBIO_E_CRED_PROV_DISABLED: Windows.Win32.Foundation.HRESULT = -2146861008
WINBIO_E_CRED_PROV_NO_CREDENTIAL: Windows.Win32.Foundation.HRESULT = -2146861007
WINBIO_E_DISABLED: Windows.Win32.Foundation.HRESULT = -2146861006
WINBIO_E_CONFIGURATION_FAILURE: Windows.Win32.Foundation.HRESULT = -2146861005
WINBIO_E_SENSOR_UNAVAILABLE: Windows.Win32.Foundation.HRESULT = -2146861004
WINBIO_E_SAS_ENABLED: Windows.Win32.Foundation.HRESULT = -2146861003
WINBIO_E_DEVICE_FAILURE: Windows.Win32.Foundation.HRESULT = -2146861002
WINBIO_E_FAST_USER_SWITCH_DISABLED: Windows.Win32.Foundation.HRESULT = -2146861001
WINBIO_E_NOT_ACTIVE_CONSOLE: Windows.Win32.Foundation.HRESULT = -2146861000
WINBIO_E_EVENT_MONITOR_ACTIVE: Windows.Win32.Foundation.HRESULT = -2146860999
WINBIO_E_INVALID_PROPERTY_TYPE: Windows.Win32.Foundation.HRESULT = -2146860998
WINBIO_E_INVALID_PROPERTY_ID: Windows.Win32.Foundation.HRESULT = -2146860997
WINBIO_E_UNSUPPORTED_PROPERTY: Windows.Win32.Foundation.HRESULT = -2146860996
WINBIO_E_ADAPTER_INTEGRITY_FAILURE: Windows.Win32.Foundation.HRESULT = -2146860995
WINBIO_E_INCORRECT_SESSION_TYPE: Windows.Win32.Foundation.HRESULT = -2146860994
WINBIO_E_SESSION_HANDLE_CLOSED: Windows.Win32.Foundation.HRESULT = -2146860993
WINBIO_E_DEADLOCK_DETECTED: Windows.Win32.Foundation.HRESULT = -2146860992
WINBIO_E_NO_PREBOOT_IDENTITY: Windows.Win32.Foundation.HRESULT = -2146860991
WINBIO_E_MAX_ERROR_COUNT_EXCEEDED: Windows.Win32.Foundation.HRESULT = -2146860990
WINBIO_E_AUTO_LOGON_DISABLED: Windows.Win32.Foundation.HRESULT = -2146860989
WINBIO_E_INVALID_TICKET: Windows.Win32.Foundation.HRESULT = -2146860988
WINBIO_E_TICKET_QUOTA_EXCEEDED: Windows.Win32.Foundation.HRESULT = -2146860987
WINBIO_E_DATA_PROTECTION_FAILURE: Windows.Win32.Foundation.HRESULT = -2146860986
WINBIO_E_CRED_PROV_SECURITY_LOCKOUT: Windows.Win32.Foundation.HRESULT = -2146860985
WINBIO_E_UNSUPPORTED_POOL_TYPE: Windows.Win32.Foundation.HRESULT = -2146860984
WINBIO_E_SELECTION_REQUIRED: Windows.Win32.Foundation.HRESULT = -2146860983
WINBIO_E_PRESENCE_MONITOR_ACTIVE: Windows.Win32.Foundation.HRESULT = -2146860982
WINBIO_E_INVALID_SUBFACTOR: Windows.Win32.Foundation.HRESULT = -2146860981
WINBIO_E_INVALID_CALIBRATION_FORMAT_ARRAY: Windows.Win32.Foundation.HRESULT = -2146860980
WINBIO_E_NO_SUPPORTED_CALIBRATION_FORMAT: Windows.Win32.Foundation.HRESULT = -2146860979
WINBIO_E_UNSUPPORTED_SENSOR_CALIBRATION_FORMAT: Windows.Win32.Foundation.HRESULT = -2146860978
WINBIO_E_CALIBRATION_BUFFER_TOO_SMALL: Windows.Win32.Foundation.HRESULT = -2146860977
WINBIO_E_CALIBRATION_BUFFER_TOO_LARGE: Windows.Win32.Foundation.HRESULT = -2146860976
WINBIO_E_CALIBRATION_BUFFER_INVALID: Windows.Win32.Foundation.HRESULT = -2146860975
WINBIO_E_INVALID_KEY_IDENTIFIER: Windows.Win32.Foundation.HRESULT = -2146860974
WINBIO_E_KEY_CREATION_FAILED: Windows.Win32.Foundation.HRESULT = -2146860973
WINBIO_E_KEY_IDENTIFIER_BUFFER_TOO_SMALL: Windows.Win32.Foundation.HRESULT = -2146860972
WINBIO_E_PROPERTY_UNAVAILABLE: Windows.Win32.Foundation.HRESULT = -2146860971
WINBIO_E_POLICY_PROTECTION_UNAVAILABLE: Windows.Win32.Foundation.HRESULT = -2146860970
WINBIO_E_INSECURE_SENSOR: Windows.Win32.Foundation.HRESULT = -2146860969
WINBIO_E_INVALID_BUFFER_ID: Windows.Win32.Foundation.HRESULT = -2146860968
WINBIO_E_INVALID_BUFFER: Windows.Win32.Foundation.HRESULT = -2146860967
WINBIO_E_TRUSTLET_INTEGRITY_FAIL: Windows.Win32.Foundation.HRESULT = -2146860966
WINBIO_E_ENROLLMENT_CANCELED_BY_SUSPEND: Windows.Win32.Foundation.HRESULT = -2146860965
WINBIO_I_MORE_DATA: Windows.Win32.Foundation.HRESULT = 589825
WINBIO_I_EXTENDED_STATUS_INFORMATION: Windows.Win32.Foundation.HRESULT = 589826
GUID_DEVINTERFACE_BIOMETRIC_READER: Guid = Guid('{e2b5183a-99ea-4cc3-ad6b-80ca8d715b80}')
IOCTL_BIOMETRIC_VENDOR: UInt32 = 4464640
WINBIO_WBDI_MAJOR_VERSION: UInt32 = 1
WINBIO_WBDI_MINOR_VERSION: UInt32 = 0
@winfunctype('winbio.dll')
def WinBioEnumServiceProviders(Factor: UInt32, BspSchemaArray: POINTER(POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_BSP_SCHEMA_head)), BspCount: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioEnumBiometricUnits(Factor: UInt32, UnitSchemaArray: POINTER(POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_UNIT_SCHEMA_head)), UnitCount: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioEnumDatabases(Factor: UInt32, StorageSchemaArray: POINTER(POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_STORAGE_SCHEMA_head)), StorageCount: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioAsyncOpenFramework(NotificationMethod: Windows.Win32.Devices.BiometricFramework.WINBIO_ASYNC_NOTIFICATION_METHOD, TargetWindow: Windows.Win32.Foundation.HWND, MessageCode: UInt32, CallbackRoutine: Windows.Win32.Devices.BiometricFramework.PWINBIO_ASYNC_COMPLETION_CALLBACK, UserData: c_void_p, AsynchronousOpen: Windows.Win32.Foundation.BOOL, FrameworkHandle: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioCloseFramework(FrameworkHandle: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioAsyncEnumServiceProviders(FrameworkHandle: UInt32, Factor: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioAsyncEnumBiometricUnits(FrameworkHandle: UInt32, Factor: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioAsyncEnumDatabases(FrameworkHandle: UInt32, Factor: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioAsyncMonitorFrameworkChanges(FrameworkHandle: UInt32, ChangeTypes: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioOpenSession(Factor: UInt32, PoolType: Windows.Win32.Devices.BiometricFramework.WINBIO_POOL, Flags: UInt32, UnitArray: POINTER(UInt32), UnitCount: UIntPtr, DatabaseId: POINTER(Guid), SessionHandle: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioAsyncOpenSession(Factor: UInt32, PoolType: Windows.Win32.Devices.BiometricFramework.WINBIO_POOL, Flags: UInt32, UnitArray: POINTER(UInt32), UnitCount: UIntPtr, DatabaseId: POINTER(Guid), NotificationMethod: Windows.Win32.Devices.BiometricFramework.WINBIO_ASYNC_NOTIFICATION_METHOD, TargetWindow: Windows.Win32.Foundation.HWND, MessageCode: UInt32, CallbackRoutine: Windows.Win32.Devices.BiometricFramework.PWINBIO_ASYNC_COMPLETION_CALLBACK, UserData: c_void_p, AsynchronousOpen: Windows.Win32.Foundation.BOOL, SessionHandle: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioCloseSession(SessionHandle: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioVerify(SessionHandle: UInt32, Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte, UnitId: POINTER(UInt32), Match: POINTER(Byte), RejectDetail: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioVerifyWithCallback(SessionHandle: UInt32, Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte, VerifyCallback: Windows.Win32.Devices.BiometricFramework.PWINBIO_VERIFY_CALLBACK, VerifyCallbackContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioIdentify(SessionHandle: UInt32, UnitId: POINTER(UInt32), Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: POINTER(Byte), RejectDetail: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioIdentifyWithCallback(SessionHandle: UInt32, IdentifyCallback: Windows.Win32.Devices.BiometricFramework.PWINBIO_IDENTIFY_CALLBACK, IdentifyCallbackContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioWait(SessionHandle: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioCancel(SessionHandle: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioLocateSensor(SessionHandle: UInt32, UnitId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioLocateSensorWithCallback(SessionHandle: UInt32, LocateCallback: Windows.Win32.Devices.BiometricFramework.PWINBIO_LOCATE_SENSOR_CALLBACK, LocateCallbackContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioEnrollBegin(SessionHandle: UInt32, SubFactor: Byte, UnitId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioEnrollSelect(SessionHandle: UInt32, SelectorValue: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioEnrollCapture(SessionHandle: UInt32, RejectDetail: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioEnrollCaptureWithCallback(SessionHandle: UInt32, EnrollCallback: Windows.Win32.Devices.BiometricFramework.PWINBIO_ENROLL_CAPTURE_CALLBACK, EnrollCallbackContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioEnrollCommit(SessionHandle: UInt32, Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), IsNewTemplate: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioEnrollDiscard(SessionHandle: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioEnumEnrollments(SessionHandle: UInt32, UnitId: UInt32, Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactorArray: POINTER(POINTER(Byte)), SubFactorCount: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioImproveBegin(SessionHandle: UInt32, UnitId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioImproveEnd(SessionHandle: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioRegisterEventMonitor(SessionHandle: UInt32, EventMask: UInt32, EventCallback: Windows.Win32.Devices.BiometricFramework.PWINBIO_EVENT_CALLBACK, EventCallbackContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioUnregisterEventMonitor(SessionHandle: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioMonitorPresence(SessionHandle: UInt32, UnitId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioCaptureSample(SessionHandle: UInt32, Purpose: Byte, Flags: Byte, UnitId: POINTER(UInt32), Sample: POINTER(POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_head)), SampleSize: POINTER(UIntPtr), RejectDetail: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioCaptureSampleWithCallback(SessionHandle: UInt32, Purpose: Byte, Flags: Byte, CaptureCallback: Windows.Win32.Devices.BiometricFramework.PWINBIO_CAPTURE_CALLBACK, CaptureCallbackContext: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioDeleteTemplate(SessionHandle: UInt32, UnitId: UInt32, Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioLockUnit(SessionHandle: UInt32, UnitId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioUnlockUnit(SessionHandle: UInt32, UnitId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioControlUnit(SessionHandle: UInt32, UnitId: UInt32, Component: Windows.Win32.Devices.BiometricFramework.WINBIO_COMPONENT, ControlCode: UInt32, SendBuffer: POINTER(Byte), SendBufferSize: UIntPtr, ReceiveBuffer: POINTER(Byte), ReceiveBufferSize: UIntPtr, ReceiveDataSize: POINTER(UIntPtr), OperationStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioControlUnitPrivileged(SessionHandle: UInt32, UnitId: UInt32, Component: Windows.Win32.Devices.BiometricFramework.WINBIO_COMPONENT, ControlCode: UInt32, SendBuffer: POINTER(Byte), SendBufferSize: UIntPtr, ReceiveBuffer: POINTER(Byte), ReceiveBufferSize: UIntPtr, ReceiveDataSize: POINTER(UIntPtr), OperationStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioGetProperty(SessionHandle: UInt32, PropertyType: UInt32, PropertyId: UInt32, UnitId: UInt32, Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte, PropertyBuffer: POINTER(c_void_p), PropertyBufferSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioSetProperty(SessionHandle: UInt32, PropertyType: UInt32, PropertyId: UInt32, UnitId: UInt32, Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte, PropertyBuffer: c_void_p, PropertyBufferSize: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioFree(Address: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioSetCredential(Type: Windows.Win32.Devices.BiometricFramework.WINBIO_CREDENTIAL_TYPE, Credential: POINTER(Byte), CredentialSize: UIntPtr, Format: Windows.Win32.Devices.BiometricFramework.WINBIO_CREDENTIAL_FORMAT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioRemoveCredential(Identity: Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY, Type: Windows.Win32.Devices.BiometricFramework.WINBIO_CREDENTIAL_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioRemoveAllCredentials() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioRemoveAllDomainCredentials() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioGetCredentialState(Identity: Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY, Type: Windows.Win32.Devices.BiometricFramework.WINBIO_CREDENTIAL_TYPE, CredentialState: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_CREDENTIAL_STATE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioLogonIdentifiedUser(SessionHandle: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioGetEnrolledFactors(AccountOwner: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), EnrolledFactors: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioGetEnabledSetting(Value: POINTER(Byte), Source: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_SETTING_SOURCE)) -> Void: ...
@winfunctype('winbio.dll')
def WinBioGetLogonSetting(Value: POINTER(Byte), Source: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_SETTING_SOURCE)) -> Void: ...
@winfunctype('winbio.dll')
def WinBioGetDomainLogonSetting(Value: POINTER(Byte), Source: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_SETTING_SOURCE)) -> Void: ...
@winfunctype('winbio.dll')
def WinBioAcquireFocus() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('winbio.dll')
def WinBioReleaseFocus() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_ACCEPT_PRIVATE_SENSOR_TYPE_INFO_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), TypeInfoBufferAddress: POINTER(Byte), TypeInfoBufferSize: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_ACCEPT_SAMPLE_DATA_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), SampleBuffer: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_head), SampleSize: UIntPtr, Purpose: Byte, RejectDetail: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_ACTIVATE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_ATTACH_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_CHECK_FOR_DUPLICATE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: POINTER(Byte), Duplicate: POINTER(Windows.Win32.Foundation.BOOLEAN)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_CLEAR_CONTEXT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_COMMIT_ENROLLMENT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte, PayloadBlob: POINTER(Byte), PayloadBlobSize: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_CONTROL_UNIT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), ControlCode: UInt32, SendBuffer: POINTER(Byte), SendBufferSize: UIntPtr, ReceiveBuffer: POINTER(Byte), ReceiveBufferSize: UIntPtr, ReceiveDataSize: POINTER(UIntPtr), OperationStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_CONTROL_UNIT_PRIVILEGED_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), ControlCode: UInt32, SendBuffer: POINTER(Byte), SendBufferSize: UIntPtr, ReceiveBuffer: POINTER(Byte), ReceiveBufferSize: UIntPtr, ReceiveDataSize: POINTER(UIntPtr), OperationStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_CREATE_ENROLLMENT_AUTHENTICATED_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Nonce: POINTER(POINTER(Byte)), NonceSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_CREATE_ENROLLMENT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_CREATE_KEY_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Key: POINTER(Byte), KeySize: UIntPtr, KeyIdentifier: POINTER(Byte), KeyIdentifierSize: UIntPtr, ResultSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_DEACTIVATE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_DETACH_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_DISCARD_ENROLLMENT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_EXPORT_ENGINE_DATA_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Flags: Byte, SampleBuffer: POINTER(POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_head)), SampleSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_GET_ENROLLMENT_HASH_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), HashValue: POINTER(POINTER(Byte)), HashSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_GET_ENROLLMENT_STATUS_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RejectDetail: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_IDENTIFY_ALL_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), PresenceCount: POINTER(UIntPtr), PresenceArray: POINTER(POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PRESENCE_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_IDENTIFY_FEATURE_SET_AUTHENTICATED_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Nonce: POINTER(Byte), NonceSize: UIntPtr, Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: POINTER(Byte), RejectDetail: POINTER(UInt32), Authentication: POINTER(POINTER(Byte)), AuthenticationSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_IDENTIFY_FEATURE_SET_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: POINTER(Byte), PayloadBlob: POINTER(POINTER(Byte)), PayloadBlobSize: POINTER(UIntPtr), HashValue: POINTER(POINTER(Byte)), HashSize: POINTER(UIntPtr), RejectDetail: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_IDENTIFY_FEATURE_SET_SECURE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Nonce: POINTER(Byte), NonceSize: UIntPtr, KeyIdentifier: POINTER(Byte), KeyIdentifierSize: UIntPtr, Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: POINTER(Byte), RejectDetail: POINTER(UInt32), Authorization: POINTER(POINTER(Byte)), AuthorizationSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_NOTIFY_POWER_CHANGE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), PowerEventType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_PIPELINE_CLEANUP_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_PIPELINE_INIT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_QUERY_CALIBRATION_DATA_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), DiscardAndRepeatCapture: POINTER(Windows.Win32.Foundation.BOOLEAN), CalibrationBuffer: POINTER(Byte), CalibrationBufferSize: POINTER(UIntPtr), MaxBufferSize: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_QUERY_EXTENDED_ENROLLMENT_STATUS_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), EnrollmentStatus: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_EXTENDED_ENROLLMENT_STATUS_head), EnrollmentStatusSize: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_QUERY_EXTENDED_INFO_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), EngineInfo: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_EXTENDED_ENGINE_INFO_head), EngineInfoSize: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_QUERY_HASH_ALGORITHMS_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), AlgorithmCount: POINTER(UIntPtr), AlgorithmBufferSize: POINTER(UIntPtr), AlgorithmBuffer: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_QUERY_INDEX_VECTOR_SIZE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), IndexElementCount: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_QUERY_PREFERRED_FORMAT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), StandardFormat: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT_head), VendorFormat: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_QUERY_SAMPLE_HINT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), SampleHint: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_REFRESH_CACHE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_RESERVED_1_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_SELECT_CALIBRATION_FORMAT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), FormatArray: POINTER(Guid), FormatCount: UIntPtr, SelectedFormat: POINTER(Guid), MaxBufferSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_SET_ACCOUNT_POLICY_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), PolicyItemArray: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_ACCOUNT_POLICY_head), PolicyItemCount: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_SET_ENROLLMENT_PARAMETERS_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Parameters: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_EXTENDED_ENROLLMENT_PARAMETERS_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_SET_ENROLLMENT_SELECTOR_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), SelectorValue: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_SET_HASH_ALGORITHM_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), AlgorithmBufferSize: UIntPtr, AlgorithmBuffer: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_UPDATE_ENROLLMENT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RejectDetail: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_ENGINE_VERIFY_FEATURE_SET_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte, Match: POINTER(Windows.Win32.Foundation.BOOLEAN), PayloadBlob: POINTER(POINTER(Byte)), PayloadBlobSize: POINTER(UIntPtr), HashValue: POINTER(POINTER(Byte)), HashSize: POINTER(UIntPtr), RejectDetail: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_ALLOCATE_MEMORY_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), AllocationSize: UIntPtr, Address: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_FREE_MEMORY_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Address: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_GET_PROPERTY_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), PropertyType: UInt32, PropertyId: UInt32, Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte, PropertyBuffer: POINTER(c_void_p), PropertyBufferSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_LOCK_AND_VALIDATE_SECURE_BUFFER_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), SecureBufferIdentifier: Guid, SecureBufferAddress: POINTER(c_void_p), SecureBufferSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_RELEASE_SECURE_BUFFER_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), SecureBufferIdentifier: Guid) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_SET_UNIT_STATUS_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), ExtendedStatus: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_EXTENDED_UNIT_STATUS_head), ExtendedStatusSize: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_CACHE_CLEAR_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_BEGIN_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RequiredCapacity: POINTER(UIntPtr), MaxBufferSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_END_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_NEXT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), BufferAddress: POINTER(Byte), BufferSize: UIntPtr, ReturnedDataSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_BEGIN_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RequiredCapacity: UIntPtr, MaxBufferSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_END_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_NEXT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), BufferAddress: POINTER(Byte), BufferSize: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_DECRYPT_SAMPLE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Authentication: POINTER(Byte), AuthenticationSize: UIntPtr, Iv: POINTER(Byte), IvSize: UIntPtr, EncryptedData: POINTER(Byte), EncryptedDataSize: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_QUERY_AUTHORIZED_ENROLLMENTS_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SecureIdentityCount: POINTER(UIntPtr), SecureIdentities: POINTER(POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_1_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Reserved1: UIntPtr, Reserved2: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_2_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Reserved1: POINTER(Byte), Reserved2: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_3_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_ACCEPT_CALIBRATION_DATA_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), CalibrationBuffer: POINTER(Byte), CalibrationBufferSize: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_ACTIVATE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_ASYNC_IMPORT_RAW_BUFFER_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RawBufferAddress: POINTER(Byte), RawBufferSize: UIntPtr, ResultBufferAddress: POINTER(POINTER(Byte)), ResultBufferSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_ASYNC_IMPORT_SECURE_BUFFER_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), SecureBufferIdentifier: Guid, MetadataBufferAddress: POINTER(Byte), MetadataBufferSize: UIntPtr, ResultBufferAddress: POINTER(POINTER(Byte)), ResultBufferSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_ATTACH_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_CANCEL_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_CLEAR_CONTEXT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_CONNECT_SECURE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), ConnectionParams: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_SECURE_CONNECTION_PARAMS_head), ConnectionData: POINTER(POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_SECURE_CONNECTION_DATA_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_CONTROL_UNIT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), ControlCode: UInt32, SendBuffer: POINTER(Byte), SendBufferSize: UIntPtr, ReceiveBuffer: POINTER(Byte), ReceiveBufferSize: UIntPtr, ReceiveDataSize: POINTER(UIntPtr), OperationStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_CONTROL_UNIT_PRIVILEGED_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), ControlCode: UInt32, SendBuffer: POINTER(Byte), SendBufferSize: UIntPtr, ReceiveBuffer: POINTER(Byte), ReceiveBufferSize: UIntPtr, ReceiveDataSize: POINTER(UIntPtr), OperationStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_DEACTIVATE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_DETACH_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_EXPORT_SENSOR_DATA_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), SampleBuffer: POINTER(POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_head)), SampleSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_FINISH_CAPTURE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RejectDetail: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_FINISH_NOTIFY_WAKE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Reason: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_GET_INDICATOR_STATUS_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), IndicatorStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_NOTIFY_POWER_CHANGE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), PowerEventType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_PIPELINE_CLEANUP_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_PIPELINE_INIT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_PUSH_DATA_TO_ENGINE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Purpose: Byte, Flags: Byte, RejectDetail: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_QUERY_CALIBRATION_FORMATS_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), FormatArray: POINTER(Guid), FormatArraySize: UIntPtr, FormatCount: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_QUERY_EXTENDED_INFO_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), SensorInfo: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_EXTENDED_SENSOR_INFO_head), SensorInfoSize: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_QUERY_PRIVATE_SENSOR_TYPE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), TypeInfoBufferAddress: POINTER(Byte), TypeInfoBufferSize: UIntPtr, TypeInfoDataSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_QUERY_STATUS_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Status: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_RESET_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_SET_CALIBRATION_FORMAT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Format: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_SET_INDICATOR_STATUS_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), IndicatorStatus: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_SET_MODE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Mode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_START_CAPTURE_EX_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Purpose: Byte, Nonce: POINTER(Byte), NonceSize: UIntPtr, Flags: Byte, Overlapped: POINTER(POINTER(Windows.Win32.System.IO.OVERLAPPED_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_START_CAPTURE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Purpose: Byte, Overlapped: POINTER(POINTER(Windows.Win32.System.IO.OVERLAPPED_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_SENSOR_START_NOTIFY_WAKE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Overlapped: POINTER(POINTER(Windows.Win32.System.IO.OVERLAPPED_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_ACTIVATE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_ADD_RECORD_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RecordContents: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_STORAGE_RECORD_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_ATTACH_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_CLEAR_CONTEXT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_CLOSE_DATABASE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_CONTROL_UNIT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), ControlCode: UInt32, SendBuffer: POINTER(Byte), SendBufferSize: UIntPtr, ReceiveBuffer: POINTER(Byte), ReceiveBufferSize: UIntPtr, ReceiveDataSize: POINTER(UIntPtr), OperationStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_CONTROL_UNIT_PRIVILEGED_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), ControlCode: UInt32, SendBuffer: POINTER(Byte), SendBufferSize: UIntPtr, ReceiveBuffer: POINTER(Byte), ReceiveBufferSize: UIntPtr, ReceiveDataSize: POINTER(UIntPtr), OperationStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_CREATE_DATABASE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), DatabaseId: POINTER(Guid), Factor: UInt32, Format: POINTER(Guid), FilePath: Windows.Win32.Foundation.PWSTR, ConnectString: Windows.Win32.Foundation.PWSTR, IndexElementCount: UIntPtr, InitialSize: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_DEACTIVATE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_DELETE_RECORD_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_DETACH_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_ERASE_DATABASE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), DatabaseId: POINTER(Guid), FilePath: Windows.Win32.Foundation.PWSTR, ConnectString: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_FIRST_RECORD_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_GET_CURRENT_RECORD_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RecordContents: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_STORAGE_RECORD_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_GET_DATABASE_SIZE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), AvailableRecordCount: POINTER(UIntPtr), TotalRecordCount: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_GET_DATA_FORMAT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Format: POINTER(Guid), Version: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_VERSION_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_GET_RECORD_COUNT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RecordCount: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_NEXT_RECORD_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_NOTIFY_DATABASE_CHANGE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RecordsAdded: Windows.Win32.Foundation.BOOLEAN) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_NOTIFY_POWER_CHANGE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), PowerEventType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_OPEN_DATABASE_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), DatabaseId: POINTER(Guid), FilePath: Windows.Win32.Foundation.PWSTR, ConnectString: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_PIPELINE_CLEANUP_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_PIPELINE_INIT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_QUERY_BY_CONTENT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), SubFactor: Byte, IndexVector: POINTER(UInt32), IndexElementCount: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_QUERY_BY_SUBJECT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_QUERY_EXTENDED_INFO_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), StorageInfo: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_EXTENDED_STORAGE_INFO_head), StorageInfoSize: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_RESERVED_1_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), Reserved1: POINTER(UInt64), Reserved2: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_RESERVED_2_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_UPDATE_RECORD_BEGIN_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte, RecordContents: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_STORAGE_RECORD_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PIBIO_STORAGE_UPDATE_RECORD_COMMIT_FN(Pipeline: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PIPELINE_head), RecordContents: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_STORAGE_RECORD_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWINBIO_ASYNC_COMPLETION_CALLBACK(AsyncResult: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_ASYNC_RESULT_head)) -> Void: ...
@winfunctype_pointer
def PWINBIO_CAPTURE_CALLBACK(CaptureCallbackContext: c_void_p, OperationStatus: Windows.Win32.Foundation.HRESULT, UnitId: UInt32, Sample: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_head), SampleSize: UIntPtr, RejectDetail: UInt32) -> Void: ...
@winfunctype_pointer
def PWINBIO_ENROLL_CAPTURE_CALLBACK(EnrollCallbackContext: c_void_p, OperationStatus: Windows.Win32.Foundation.HRESULT, RejectDetail: UInt32) -> Void: ...
@winfunctype_pointer
def PWINBIO_EVENT_CALLBACK(EventCallbackContext: c_void_p, OperationStatus: Windows.Win32.Foundation.HRESULT, Event: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_EVENT_head)) -> Void: ...
@winfunctype_pointer
def PWINBIO_IDENTIFY_CALLBACK(IdentifyCallbackContext: c_void_p, OperationStatus: Windows.Win32.Foundation.HRESULT, UnitId: UInt32, Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head), SubFactor: Byte, RejectDetail: UInt32) -> Void: ...
@winfunctype_pointer
def PWINBIO_LOCATE_SENSOR_CALLBACK(LocateCallbackContext: c_void_p, OperationStatus: Windows.Win32.Foundation.HRESULT, UnitId: UInt32) -> Void: ...
@winfunctype_pointer
def PWINBIO_QUERY_ENGINE_INTERFACE_FN(EngineInterface: POINTER(POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_ENGINE_INTERFACE_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWINBIO_QUERY_SENSOR_INTERFACE_FN(SensorInterface: POINTER(POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_SENSOR_INTERFACE_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWINBIO_QUERY_STORAGE_INTERFACE_FN(StorageInterface: POINTER(POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_STORAGE_INTERFACE_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PWINBIO_VERIFY_CALLBACK(VerifyCallbackContext: c_void_p, OperationStatus: Windows.Win32.Foundation.HRESULT, UnitId: UInt32, Match: Windows.Win32.Foundation.BOOLEAN, RejectDetail: UInt32) -> Void: ...
class WINBIO_ACCOUNT_POLICY(EasyCastStructure):
    Identity: Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
    AntiSpoofBehavior: Windows.Win32.Devices.BiometricFramework.WINBIO_ANTI_SPOOF_POLICY_ACTION
class WINBIO_ADAPTER_INTERFACE_VERSION(EasyCastStructure):
    MajorVersion: UInt16
    MinorVersion: UInt16
class WINBIO_ANTI_SPOOF_POLICY(EasyCastStructure):
    Action: Windows.Win32.Devices.BiometricFramework.WINBIO_ANTI_SPOOF_POLICY_ACTION
    Source: Windows.Win32.Devices.BiometricFramework.WINBIO_POLICY_SOURCE
WINBIO_ANTI_SPOOF_POLICY_ACTION = Int32
WINBIO_ANTI_SPOOF_DISABLE: WINBIO_ANTI_SPOOF_POLICY_ACTION = 0
WINBIO_ANTI_SPOOF_ENABLE: WINBIO_ANTI_SPOOF_POLICY_ACTION = 1
WINBIO_ANTI_SPOOF_REMOVE: WINBIO_ANTI_SPOOF_POLICY_ACTION = 2
WINBIO_ASYNC_NOTIFICATION_METHOD = Int32
WINBIO_ASYNC_NOTIFY_NONE: WINBIO_ASYNC_NOTIFICATION_METHOD = 0
WINBIO_ASYNC_NOTIFY_CALLBACK: WINBIO_ASYNC_NOTIFICATION_METHOD = 1
WINBIO_ASYNC_NOTIFY_MESSAGE: WINBIO_ASYNC_NOTIFICATION_METHOD = 2
WINBIO_ASYNC_NOTIFY_MAXIMUM_VALUE: WINBIO_ASYNC_NOTIFICATION_METHOD = 3
class WINBIO_ASYNC_RESULT(EasyCastStructure):
    SessionHandle: UInt32
    Operation: UInt32
    SequenceNumber: UInt64
    TimeStamp: Int64
    ApiStatus: Windows.Win32.Foundation.HRESULT
    UnitId: UInt32
    UserData: c_void_p
    Parameters: _Parameters_e__Union
    class _Parameters_e__Union(EasyCastUnion):
        Verify: _Verify_e__Struct
        Identify: _Identify_e__Struct
        EnrollBegin: _EnrollBegin_e__Struct
        EnrollCapture: _EnrollCapture_e__Struct
        EnrollCommit: _EnrollCommit_e__Struct
        EnumEnrollments: _EnumEnrollments_e__Struct
        CaptureSample: _CaptureSample_e__Struct
        DeleteTemplate: _DeleteTemplate_e__Struct
        GetProperty: _GetProperty_e__Struct
        SetProperty: _SetProperty_e__Struct
        GetEvent: _GetEvent_e__Struct
        ControlUnit: _ControlUnit_e__Struct
        EnumServiceProviders: _EnumServiceProviders_e__Struct
        EnumBiometricUnits: _EnumBiometricUnits_e__Struct
        EnumDatabases: _EnumDatabases_e__Struct
        VerifyAndReleaseTicket: _VerifyAndReleaseTicket_e__Struct
        IdentifyAndReleaseTicket: _IdentifyAndReleaseTicket_e__Struct
        EnrollSelect: _EnrollSelect_e__Struct
        MonitorPresence: _MonitorPresence_e__Struct
        GetProtectionPolicy: _GetProtectionPolicy_e__Struct
        NotifyUnitStatusChange: _NotifyUnitStatusChange_e__Struct
        class _Verify_e__Struct(EasyCastStructure):
            Match: Windows.Win32.Foundation.BOOLEAN
            RejectDetail: UInt32
        class _Identify_e__Struct(EasyCastStructure):
            Identity: Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
            SubFactor: Byte
            RejectDetail: UInt32
        class _EnrollBegin_e__Struct(EasyCastStructure):
            SubFactor: Byte
        class _EnrollCapture_e__Struct(EasyCastStructure):
            RejectDetail: UInt32
        class _EnrollCommit_e__Struct(EasyCastStructure):
            Identity: Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
            IsNewTemplate: Windows.Win32.Foundation.BOOLEAN
        class _EnumEnrollments_e__Struct(EasyCastStructure):
            Identity: Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
            SubFactorCount: UIntPtr
            SubFactorArray: POINTER(Byte)
        class _CaptureSample_e__Struct(EasyCastStructure):
            Sample: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_head)
            SampleSize: UIntPtr
            RejectDetail: UInt32
        class _DeleteTemplate_e__Struct(EasyCastStructure):
            Identity: Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
            SubFactor: Byte
        class _GetProperty_e__Struct(EasyCastStructure):
            PropertyType: UInt32
            PropertyId: UInt32
            Identity: Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
            SubFactor: Byte
            PropertyBufferSize: UIntPtr
            PropertyBuffer: c_void_p
        class _SetProperty_e__Struct(EasyCastStructure):
            PropertyType: UInt32
            PropertyId: UInt32
            Identity: Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
            SubFactor: Byte
            PropertyBufferSize: UIntPtr
            PropertyBuffer: c_void_p
        class _GetEvent_e__Struct(EasyCastStructure):
            Event: Windows.Win32.Devices.BiometricFramework.WINBIO_EVENT
        class _ControlUnit_e__Struct(EasyCastStructure):
            Component: Windows.Win32.Devices.BiometricFramework.WINBIO_COMPONENT
            ControlCode: UInt32
            OperationStatus: UInt32
            SendBuffer: POINTER(Byte)
            SendBufferSize: UIntPtr
            ReceiveBuffer: POINTER(Byte)
            ReceiveBufferSize: UIntPtr
            ReceiveDataSize: UIntPtr
        class _EnumServiceProviders_e__Struct(EasyCastStructure):
            BspCount: UIntPtr
            BspSchemaArray: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_BSP_SCHEMA_head)
        class _EnumBiometricUnits_e__Struct(EasyCastStructure):
            UnitCount: UIntPtr
            UnitSchemaArray: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_UNIT_SCHEMA_head)
        class _EnumDatabases_e__Struct(EasyCastStructure):
            StorageCount: UIntPtr
            StorageSchemaArray: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_STORAGE_SCHEMA_head)
        class _VerifyAndReleaseTicket_e__Struct(EasyCastStructure):
            Match: Windows.Win32.Foundation.BOOLEAN
            RejectDetail: UInt32
            Ticket: UInt64
        class _IdentifyAndReleaseTicket_e__Struct(EasyCastStructure):
            Identity: Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
            SubFactor: Byte
            RejectDetail: UInt32
            Ticket: UInt64
        class _EnrollSelect_e__Struct(EasyCastStructure):
            SelectorValue: UInt64
        class _MonitorPresence_e__Struct(EasyCastStructure):
            ChangeType: UInt32
            PresenceCount: UIntPtr
            PresenceArray: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_PRESENCE_head)
        class _GetProtectionPolicy_e__Struct(EasyCastStructure):
            Identity: Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
            Policy: Windows.Win32.Devices.BiometricFramework.WINBIO_PROTECTION_POLICY
        class _NotifyUnitStatusChange_e__Struct(EasyCastStructure):
            ExtendedStatus: Windows.Win32.Devices.BiometricFramework.WINBIO_EXTENDED_UNIT_STATUS
class WINBIO_BDB_ANSI_381_HEADER(EasyCastStructure):
    RecordLength: UInt64
    FormatIdentifier: UInt32
    VersionNumber: UInt32
    ProductId: Windows.Win32.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT
    CaptureDeviceId: UInt16
    ImageAcquisitionLevel: UInt16
    HorizontalScanResolution: UInt16
    VerticalScanResolution: UInt16
    HorizontalImageResolution: UInt16
    VerticalImageResolution: UInt16
    ElementCount: Byte
    ScaleUnits: Byte
    PixelDepth: Byte
    ImageCompressionAlg: Byte
    Reserved: UInt16
class WINBIO_BDB_ANSI_381_RECORD(EasyCastStructure):
    BlockLength: UInt32
    HorizontalLineLength: UInt16
    VerticalLineLength: UInt16
    Position: Byte
    CountOfViews: Byte
    ViewNumber: Byte
    ImageQuality: Byte
    ImpressionType: Byte
    Reserved: Byte
class WINBIO_BIR(EasyCastStructure):
    HeaderBlock: Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_DATA
    StandardDataBlock: Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_DATA
    VendorDataBlock: Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_DATA
    SignatureBlock: Windows.Win32.Devices.BiometricFramework.WINBIO_BIR_DATA
class WINBIO_BIR_DATA(EasyCastStructure):
    Size: UInt32
    Offset: UInt32
class WINBIO_BIR_HEADER(EasyCastStructure):
    ValidFields: UInt16
    HeaderVersion: Byte
    PatronHeaderVersion: Byte
    DataFlags: Byte
    Type: UInt32
    Subtype: Byte
    Purpose: Byte
    DataQuality: SByte
    CreationDate: Int64
    ValidityPeriod: _ValidityPeriod_e__Struct
    BiometricDataFormat: Windows.Win32.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT
    ProductId: Windows.Win32.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT
    class _ValidityPeriod_e__Struct(EasyCastStructure):
        BeginDate: Int64
        EndDate: Int64
class WINBIO_BLANK_PAYLOAD(EasyCastStructure):
    PayloadSize: UInt32
    WinBioHresult: Windows.Win32.Foundation.HRESULT
class WINBIO_BSP_SCHEMA(EasyCastStructure):
    BiometricFactor: UInt32
    BspId: Guid
    Description: UInt16 * 256
    Vendor: UInt16 * 256
    Version: Windows.Win32.Devices.BiometricFramework.WINBIO_VERSION
class WINBIO_CALIBRATION_INFO(EasyCastStructure):
    PayloadSize: UInt32
    WinBioHresult: Windows.Win32.Foundation.HRESULT
    CalibrationData: Windows.Win32.Devices.BiometricFramework.WINBIO_DATA
class WINBIO_CAPTURE_DATA(EasyCastStructure):
    PayloadSize: UInt32
    WinBioHresult: Windows.Win32.Foundation.HRESULT
    SensorStatus: UInt32
    RejectDetail: UInt32
    CaptureData: Windows.Win32.Devices.BiometricFramework.WINBIO_DATA
class WINBIO_CAPTURE_PARAMETERS(EasyCastStructure):
    PayloadSize: UInt32
    Purpose: Byte
    Format: Windows.Win32.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT
    VendorFormat: Guid
    Flags: Byte
WINBIO_COMPONENT = UInt32
WINBIO_COMPONENT_SENSOR: WINBIO_COMPONENT = 1
WINBIO_COMPONENT_ENGINE: WINBIO_COMPONENT = 2
WINBIO_COMPONENT_STORAGE: WINBIO_COMPONENT = 3
WINBIO_CREDENTIAL_FORMAT = Int32
WINBIO_PASSWORD_GENERIC: WINBIO_CREDENTIAL_FORMAT = 1
WINBIO_PASSWORD_PACKED: WINBIO_CREDENTIAL_FORMAT = 2
WINBIO_PASSWORD_PROTECTED: WINBIO_CREDENTIAL_FORMAT = 3
WINBIO_CREDENTIAL_STATE = Int32
WINBIO_CREDENTIAL_NOT_SET: WINBIO_CREDENTIAL_STATE = 1
WINBIO_CREDENTIAL_SET: WINBIO_CREDENTIAL_STATE = 2
WINBIO_CREDENTIAL_TYPE = Int32
WINBIO_CREDENTIAL_PASSWORD: WINBIO_CREDENTIAL_TYPE = 1
WINBIO_CREDENTIAL_ALL: WINBIO_CREDENTIAL_TYPE = -1
class WINBIO_DATA(EasyCastStructure):
    Size: UInt32
    Data: Byte * 1
class WINBIO_DIAGNOSTICS(EasyCastStructure):
    PayloadSize: UInt32
    WinBioHresult: Windows.Win32.Foundation.HRESULT
    SensorStatus: UInt32
    VendorDiagnostics: Windows.Win32.Devices.BiometricFramework.WINBIO_DATA
class WINBIO_ENCRYPTED_CAPTURE_PARAMS(EasyCastStructure):
    PayloadSize: UInt32
    Purpose: Byte
    Format: Windows.Win32.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT
    VendorFormat: Guid
    Flags: Byte
    NonceSize: UInt32
class WINBIO_ENGINE_INTERFACE(EasyCastStructure):
    Version: Windows.Win32.Devices.BiometricFramework.WINBIO_ADAPTER_INTERFACE_VERSION
    Type: UInt32
    Size: UIntPtr
    AdapterId: Guid
    Attach: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_ATTACH_FN
    Detach: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_DETACH_FN
    ClearContext: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_CLEAR_CONTEXT_FN
    QueryPreferredFormat: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_PREFERRED_FORMAT_FN
    QueryIndexVectorSize: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_INDEX_VECTOR_SIZE_FN
    QueryHashAlgorithms: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_HASH_ALGORITHMS_FN
    SetHashAlgorithm: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_SET_HASH_ALGORITHM_FN
    QuerySampleHint: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_SAMPLE_HINT_FN
    AcceptSampleData: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_ACCEPT_SAMPLE_DATA_FN
    ExportEngineData: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_EXPORT_ENGINE_DATA_FN
    VerifyFeatureSet: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_VERIFY_FEATURE_SET_FN
    IdentifyFeatureSet: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_IDENTIFY_FEATURE_SET_FN
    CreateEnrollment: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_CREATE_ENROLLMENT_FN
    UpdateEnrollment: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_UPDATE_ENROLLMENT_FN
    GetEnrollmentStatus: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_GET_ENROLLMENT_STATUS_FN
    GetEnrollmentHash: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_GET_ENROLLMENT_HASH_FN
    CheckForDuplicate: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_CHECK_FOR_DUPLICATE_FN
    CommitEnrollment: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_COMMIT_ENROLLMENT_FN
    DiscardEnrollment: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_DISCARD_ENROLLMENT_FN
    ControlUnit: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_CONTROL_UNIT_FN
    ControlUnitPrivileged: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_CONTROL_UNIT_PRIVILEGED_FN
    NotifyPowerChange: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_NOTIFY_POWER_CHANGE_FN
    Reserved_1: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_RESERVED_1_FN
    PipelineInit: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_PIPELINE_INIT_FN
    PipelineCleanup: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_PIPELINE_CLEANUP_FN
    Activate: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_ACTIVATE_FN
    Deactivate: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_DEACTIVATE_FN
    QueryExtendedInfo: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_EXTENDED_INFO_FN
    IdentifyAll: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_IDENTIFY_ALL_FN
    SetEnrollmentSelector: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_SET_ENROLLMENT_SELECTOR_FN
    SetEnrollmentParameters: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_SET_ENROLLMENT_PARAMETERS_FN
    QueryExtendedEnrollmentStatus: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_EXTENDED_ENROLLMENT_STATUS_FN
    RefreshCache: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_REFRESH_CACHE_FN
    SelectCalibrationFormat: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_SELECT_CALIBRATION_FORMAT_FN
    QueryCalibrationData: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_CALIBRATION_DATA_FN
    SetAccountPolicy: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_SET_ACCOUNT_POLICY_FN
    CreateKey: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_CREATE_KEY_FN
    IdentifyFeatureSetSecure: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_IDENTIFY_FEATURE_SET_SECURE_FN
    AcceptPrivateSensorTypeInfo: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_ACCEPT_PRIVATE_SENSOR_TYPE_INFO_FN
    CreateEnrollmentAuthenticated: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_CREATE_ENROLLMENT_AUTHENTICATED_FN
    IdentifyFeatureSetAuthenticated: Windows.Win32.Devices.BiometricFramework.PIBIO_ENGINE_IDENTIFY_FEATURE_SET_AUTHENTICATED_FN
class WINBIO_EVENT(EasyCastStructure):
    Type: UInt32
    Parameters: _Parameters_e__Union
    class _Parameters_e__Union(EasyCastUnion):
        Unclaimed: _Unclaimed_e__Struct
        UnclaimedIdentify: _UnclaimedIdentify_e__Struct
        Error: _Error_e__Struct
        class _Unclaimed_e__Struct(EasyCastStructure):
            UnitId: UInt32
            RejectDetail: UInt32
        class _UnclaimedIdentify_e__Struct(EasyCastStructure):
            UnitId: UInt32
            Identity: Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
            SubFactor: Byte
            RejectDetail: UInt32
        class _Error_e__Struct(EasyCastStructure):
            ErrorCode: Windows.Win32.Foundation.HRESULT
class WINBIO_EXTENDED_ENGINE_INFO(EasyCastStructure):
    GenericEngineCapabilities: UInt32
    Factor: UInt32
    Specific: _Specific_e__Union
    class _Specific_e__Union(EasyCastUnion):
        Null: UInt32
        FacialFeatures: _FacialFeatures_e__Struct
        Fingerprint: _Fingerprint_e__Struct
        Iris: _Iris_e__Struct
        Voice: _Voice_e__Struct
        class _FacialFeatures_e__Struct(EasyCastStructure):
            Capabilities: UInt32
            EnrollmentRequirements: _EnrollmentRequirements_e__Struct
            class _EnrollmentRequirements_e__Struct(EasyCastStructure):
                Null: UInt32
        class _Fingerprint_e__Struct(EasyCastStructure):
            Capabilities: UInt32
            EnrollmentRequirements: _EnrollmentRequirements_e__Struct
            class _EnrollmentRequirements_e__Struct(EasyCastStructure):
                GeneralSamples: UInt32
                Center: UInt32
                TopEdge: UInt32
                BottomEdge: UInt32
                LeftEdge: UInt32
                RightEdge: UInt32
        class _Iris_e__Struct(EasyCastStructure):
            Capabilities: UInt32
            EnrollmentRequirements: _EnrollmentRequirements_e__Struct
            class _EnrollmentRequirements_e__Struct(EasyCastStructure):
                Null: UInt32
        class _Voice_e__Struct(EasyCastStructure):
            Capabilities: UInt32
            EnrollmentRequirements: _EnrollmentRequirements_e__Struct
            class _EnrollmentRequirements_e__Struct(EasyCastStructure):
                Null: UInt32
class WINBIO_EXTENDED_ENROLLMENT_PARAMETERS(EasyCastStructure):
    Size: UIntPtr
    SubFactor: Byte
class WINBIO_EXTENDED_ENROLLMENT_STATUS(EasyCastStructure):
    TemplateStatus: Windows.Win32.Foundation.HRESULT
    RejectDetail: UInt32
    PercentComplete: UInt32
    Factor: UInt32
    SubFactor: Byte
    Specific: _Specific_e__Union
    class _Specific_e__Union(EasyCastUnion):
        Null: UInt32
        FacialFeatures: _FacialFeatures_e__Struct
        Fingerprint: _Fingerprint_e__Struct
        Iris: _Iris_e__Struct
        Voice: _Voice_e__Struct
        class _FacialFeatures_e__Struct(EasyCastStructure):
            BoundingBox: Windows.Win32.Foundation.RECT
            Distance: Int32
            OpaqueEngineData: _OpaqueEngineData_e__Struct
            class _OpaqueEngineData_e__Struct(EasyCastStructure):
                AdapterId: Guid
                Data: UInt32 * 78
        class _Fingerprint_e__Struct(EasyCastStructure):
            GeneralSamples: UInt32
            Center: UInt32
            TopEdge: UInt32
            BottomEdge: UInt32
            LeftEdge: UInt32
            RightEdge: UInt32
        class _Iris_e__Struct(EasyCastStructure):
            EyeBoundingBox_1: Windows.Win32.Foundation.RECT
            EyeBoundingBox_2: Windows.Win32.Foundation.RECT
            PupilCenter_1: Windows.Win32.Foundation.POINT
            PupilCenter_2: Windows.Win32.Foundation.POINT
            Distance: Int32
            GridPointCompletionPercent: UInt32
            GridPointIndex: UInt16
            Point3D: _Point3D_e__Struct
            StopCaptureAndShowCriticalFeedback: Windows.Win32.Foundation.BOOL
            class _Point3D_e__Struct(EasyCastStructure):
                X: Double
                Y: Double
                Z: Double
        class _Voice_e__Struct(EasyCastStructure):
            Reserved: UInt32
class WINBIO_EXTENDED_SENSOR_INFO(EasyCastStructure):
    GenericSensorCapabilities: UInt32
    Factor: UInt32
    Specific: _Specific_e__Union
    class _Specific_e__Union(EasyCastUnion):
        Null: UInt32
        FacialFeatures: _FacialFeatures_e__Struct
        Fingerprint: _Fingerprint_e__Struct
        Iris: _Iris_e__Struct
        Voice: _Voice_e__Struct
        class _FacialFeatures_e__Struct(EasyCastStructure):
            FrameSize: Windows.Win32.Foundation.RECT
            FrameOffset: Windows.Win32.Foundation.POINT
            MandatoryOrientation: UInt32
            HardwareInfo: _HardwareInfo_e__Struct
            class _HardwareInfo_e__Struct(EasyCastStructure):
                ColorSensorId: Char * 260
                InfraredSensorId: Char * 260
                InfraredSensorRotationAngle: UInt32
        class _Fingerprint_e__Struct(EasyCastStructure):
            Reserved: UInt32
        class _Iris_e__Struct(EasyCastStructure):
            FrameSize: Windows.Win32.Foundation.RECT
            FrameOffset: Windows.Win32.Foundation.POINT
            MandatoryOrientation: UInt32
        class _Voice_e__Struct(EasyCastStructure):
            Reserved: UInt32
class WINBIO_EXTENDED_STORAGE_INFO(EasyCastStructure):
    GenericStorageCapabilities: UInt32
    Factor: UInt32
    Specific: _Specific_e__Union
    class _Specific_e__Union(EasyCastUnion):
        Null: UInt32
        FacialFeatures: _FacialFeatures_e__Struct
        Fingerprint: _Fingerprint_e__Struct
        Iris: _Iris_e__Struct
        Voice: _Voice_e__Struct
        class _FacialFeatures_e__Struct(EasyCastStructure):
            Capabilities: UInt32
        class _Fingerprint_e__Struct(EasyCastStructure):
            Capabilities: UInt32
        class _Iris_e__Struct(EasyCastStructure):
            Capabilities: UInt32
        class _Voice_e__Struct(EasyCastStructure):
            Capabilities: UInt32
class WINBIO_EXTENDED_UNIT_STATUS(EasyCastStructure):
    Availability: UInt32
    ReasonCode: UInt32
class WINBIO_FP_BU_STATE(EasyCastStructure):
    SensorAttached: Windows.Win32.Foundation.BOOL
    CreationResult: Windows.Win32.Foundation.HRESULT
class WINBIO_FRAMEWORK_INTERFACE(EasyCastStructure):
    Version: Windows.Win32.Devices.BiometricFramework.WINBIO_ADAPTER_INTERFACE_VERSION
    Type: UInt32
    Size: UIntPtr
    AdapterId: Guid
    SetUnitStatus: Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_SET_UNIT_STATUS_FN
    VsmStorageAttach: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_ATTACH_FN
    VsmStorageDetach: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_DETACH_FN
    VsmStorageClearContext: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_CLEAR_CONTEXT_FN
    VsmStorageCreateDatabase: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_CREATE_DATABASE_FN
    VsmStorageOpenDatabase: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_OPEN_DATABASE_FN
    VsmStorageCloseDatabase: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_CLOSE_DATABASE_FN
    VsmStorageDeleteRecord: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_DELETE_RECORD_FN
    VsmStorageNotifyPowerChange: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_NOTIFY_POWER_CHANGE_FN
    VsmStoragePipelineInit: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_PIPELINE_INIT_FN
    VsmStoragePipelineCleanup: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_PIPELINE_CLEANUP_FN
    VsmStorageActivate: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_ACTIVATE_FN
    VsmStorageDeactivate: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_DEACTIVATE_FN
    VsmStorageQueryExtendedInfo: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_QUERY_EXTENDED_INFO_FN
    VsmStorageCacheClear: Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_CLEAR_FN
    VsmStorageCacheImportBegin: Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_BEGIN_FN
    VsmStorageCacheImportNext: Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_NEXT_FN
    VsmStorageCacheImportEnd: Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_END_FN
    VsmStorageCacheExportBegin: Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_BEGIN_FN
    VsmStorageCacheExportNext: Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_NEXT_FN
    VsmStorageCacheExportEnd: Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_END_FN
    VsmSensorAttach: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_ATTACH_FN
    VsmSensorDetach: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_DETACH_FN
    VsmSensorClearContext: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_CLEAR_CONTEXT_FN
    VsmSensorPushDataToEngine: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_PUSH_DATA_TO_ENGINE_FN
    VsmSensorNotifyPowerChange: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_NOTIFY_POWER_CHANGE_FN
    VsmSensorPipelineInit: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_PIPELINE_INIT_FN
    VsmSensorPipelineCleanup: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_PIPELINE_CLEANUP_FN
    VsmSensorActivate: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_ACTIVATE_FN
    VsmSensorDeactivate: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_DEACTIVATE_FN
    VsmSensorAsyncImportRawBuffer: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_ASYNC_IMPORT_RAW_BUFFER_FN
    VsmSensorAsyncImportSecureBuffer: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_ASYNC_IMPORT_SECURE_BUFFER_FN
    Reserved1: Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_1_FN
    Reserved2: Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_2_FN
    Reserved3: Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_3_FN
    Reserved4: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_RESERVED_1_FN
    Reserved5: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_RESERVED_2_FN
    AllocateMemory: Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_ALLOCATE_MEMORY_FN
    FreeMemory: Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_FREE_MEMORY_FN
    GetProperty: Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_GET_PROPERTY_FN
    LockAndValidateSecureBuffer: Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_LOCK_AND_VALIDATE_SECURE_BUFFER_FN
    ReleaseSecureBuffer: Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_RELEASE_SECURE_BUFFER_FN
    QueryAuthorizedEnrollments: Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_QUERY_AUTHORIZED_ENROLLMENTS_FN
    DecryptSample: Windows.Win32.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_DECRYPT_SAMPLE_FN
class WINBIO_GESTURE_METADATA(EasyCastStructure):
    Size: UIntPtr
    BiometricType: UInt32
    MatchType: UInt32
    ProtectionType: UInt32
class WINBIO_GET_INDICATOR(EasyCastStructure):
    PayloadSize: UInt32
    WinBioHresult: Windows.Win32.Foundation.HRESULT
    IndicatorStatus: UInt32
class WINBIO_IDENTITY(EasyCastStructure):
    Type: UInt32
    Value: _Value_e__Union
    class _Value_e__Union(EasyCastUnion):
        Null: UInt32
        Wildcard: UInt32
        TemplateGuid: Guid
        AccountSid: _AccountSid_e__Struct
        SecureId: Byte * 32
        class _AccountSid_e__Struct(EasyCastStructure):
            Size: UInt32
            Data: Byte * 68
class WINBIO_NOTIFY_WAKE(EasyCastStructure):
    PayloadSize: UInt32
    WinBioHresult: Windows.Win32.Foundation.HRESULT
    Reason: UInt32
class WINBIO_PIPELINE(EasyCastStructure):
    SensorHandle: Windows.Win32.Foundation.HANDLE
    EngineHandle: Windows.Win32.Foundation.HANDLE
    StorageHandle: Windows.Win32.Foundation.HANDLE
    SensorInterface: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_SENSOR_INTERFACE_head)
    EngineInterface: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_ENGINE_INTERFACE_head)
    StorageInterface: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_STORAGE_INTERFACE_head)
    SensorContext: POINTER(Windows.Win32.Devices.BiometricFramework.WINIBIO_SENSOR_CONTEXT)
    EngineContext: POINTER(Windows.Win32.Devices.BiometricFramework.WINIBIO_ENGINE_CONTEXT)
    StorageContext: POINTER(Windows.Win32.Devices.BiometricFramework.WINIBIO_STORAGE_CONTEXT)
    FrameworkInterface: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_FRAMEWORK_INTERFACE_head)
WINBIO_POLICY_SOURCE = Int32
WINBIO_POLICY_UNKNOWN: WINBIO_POLICY_SOURCE = 0
WINBIO_POLICY_DEFAULT: WINBIO_POLICY_SOURCE = 1
WINBIO_POLICY_LOCAL: WINBIO_POLICY_SOURCE = 2
WINBIO_POLICY_ADMIN: WINBIO_POLICY_SOURCE = 3
WINBIO_POOL = UInt32
WINBIO_POOL_SYSTEM: WINBIO_POOL = 1
WINBIO_POOL_PRIVATE: WINBIO_POOL = 2
class WINBIO_PRESENCE(EasyCastStructure):
    Factor: UInt32
    SubFactor: Byte
    Status: Windows.Win32.Foundation.HRESULT
    RejectDetail: UInt32
    Identity: Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
    TrackingId: UInt64
    Ticket: UInt64
    Properties: Windows.Win32.Devices.BiometricFramework.WINBIO_PRESENCE_PROPERTIES
    Authorization: _Authorization_e__Struct
    class _Authorization_e__Struct(EasyCastStructure):
        Size: UInt32
        Data: Byte * 32
class WINBIO_PRESENCE_PROPERTIES(EasyCastUnion):
    FacialFeatures: _FacialFeatures_e__Struct
    Iris: _Iris_e__Struct
    class _FacialFeatures_e__Struct(EasyCastStructure):
        BoundingBox: Windows.Win32.Foundation.RECT
        Distance: Int32
        OpaqueEngineData: _OpaqueEngineData_e__Struct
        class _OpaqueEngineData_e__Struct(EasyCastStructure):
            AdapterId: Guid
            Data: UInt32 * 78
    class _Iris_e__Struct(EasyCastStructure):
        EyeBoundingBox_1: Windows.Win32.Foundation.RECT
        EyeBoundingBox_2: Windows.Win32.Foundation.RECT
        PupilCenter_1: Windows.Win32.Foundation.POINT
        PupilCenter_2: Windows.Win32.Foundation.POINT
        Distance: Int32
class WINBIO_PRIVATE_SENSOR_TYPE_INFO(EasyCastStructure):
    PayloadSize: UInt32
    WinBioHresult: Windows.Win32.Foundation.HRESULT
    PrivateSensorTypeInfo: Windows.Win32.Devices.BiometricFramework.WINBIO_DATA
class WINBIO_PROTECTION_POLICY(EasyCastStructure):
    Version: UInt32
    Identity: Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY
    DatabaseId: Guid
    UserState: UInt64
    PolicySize: UIntPtr
    Policy: Byte * 128
class WINBIO_REGISTERED_FORMAT(EasyCastStructure):
    Owner: UInt16
    Type: UInt16
class WINBIO_SECURE_BUFFER_HEADER_V1(EasyCastStructure):
    Type: UInt32
    Size: UInt32
    Flags: UInt32
    ValidationTag: UInt64
class WINBIO_SECURE_CONNECTION_DATA(EasyCastStructure):
    Size: UInt32
    Version: UInt16
    Flags: UInt16
    ModelCertificateSize: UInt32
    IntermediateCA1Size: UInt32
    IntermediateCA2Size: UInt32
class WINBIO_SECURE_CONNECTION_PARAMS(EasyCastStructure):
    PayloadSize: UInt32
    Version: UInt16
    Flags: UInt16
class WINBIO_SENSOR_ATTRIBUTES(EasyCastStructure):
    PayloadSize: UInt32
    WinBioHresult: Windows.Win32.Foundation.HRESULT
    WinBioVersion: Windows.Win32.Devices.BiometricFramework.WINBIO_VERSION
    SensorType: UInt32
    SensorSubType: UInt32
    Capabilities: UInt32
    ManufacturerName: UInt16 * 256
    ModelName: UInt16 * 256
    SerialNumber: UInt16 * 256
    FirmwareVersion: Windows.Win32.Devices.BiometricFramework.WINBIO_VERSION
    SupportedFormatEntries: UInt32
    SupportedFormat: Windows.Win32.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT * 1
class WINBIO_SENSOR_INTERFACE(EasyCastStructure):
    Version: Windows.Win32.Devices.BiometricFramework.WINBIO_ADAPTER_INTERFACE_VERSION
    Type: UInt32
    Size: UIntPtr
    AdapterId: Guid
    Attach: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_ATTACH_FN
    Detach: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_DETACH_FN
    ClearContext: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_CLEAR_CONTEXT_FN
    QueryStatus: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_QUERY_STATUS_FN
    Reset: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_RESET_FN
    SetMode: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_SET_MODE_FN
    SetIndicatorStatus: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_SET_INDICATOR_STATUS_FN
    GetIndicatorStatus: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_GET_INDICATOR_STATUS_FN
    StartCapture: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_START_CAPTURE_FN
    FinishCapture: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_FINISH_CAPTURE_FN
    ExportSensorData: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_EXPORT_SENSOR_DATA_FN
    Cancel: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_CANCEL_FN
    PushDataToEngine: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_PUSH_DATA_TO_ENGINE_FN
    ControlUnit: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_CONTROL_UNIT_FN
    ControlUnitPrivileged: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_CONTROL_UNIT_PRIVILEGED_FN
    NotifyPowerChange: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_NOTIFY_POWER_CHANGE_FN
    PipelineInit: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_PIPELINE_INIT_FN
    PipelineCleanup: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_PIPELINE_CLEANUP_FN
    Activate: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_ACTIVATE_FN
    Deactivate: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_DEACTIVATE_FN
    QueryExtendedInfo: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_QUERY_EXTENDED_INFO_FN
    QueryCalibrationFormats: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_QUERY_CALIBRATION_FORMATS_FN
    SetCalibrationFormat: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_SET_CALIBRATION_FORMAT_FN
    AcceptCalibrationData: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_ACCEPT_CALIBRATION_DATA_FN
    AsyncImportRawBuffer: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_ASYNC_IMPORT_RAW_BUFFER_FN
    AsyncImportSecureBuffer: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_ASYNC_IMPORT_SECURE_BUFFER_FN
    QueryPrivateSensorType: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_QUERY_PRIVATE_SENSOR_TYPE_FN
    ConnectSecure: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_CONNECT_SECURE_FN
    StartCaptureEx: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_START_CAPTURE_EX_FN
    StartNotifyWake: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_START_NOTIFY_WAKE_FN
    FinishNotifyWake: Windows.Win32.Devices.BiometricFramework.PIBIO_SENSOR_FINISH_NOTIFY_WAKE_FN
WINBIO_SETTING_SOURCE = UInt32
WINBIO_SETTING_SOURCE_INVALID: WINBIO_SETTING_SOURCE = 0
WINBIO_SETTING_SOURCE_DEFAULT: WINBIO_SETTING_SOURCE = 1
WINBIO_SETTING_SOURCE_LOCAL: WINBIO_SETTING_SOURCE = 3
WINBIO_SETTING_SOURCE_POLICY: WINBIO_SETTING_SOURCE = 2
class WINBIO_SET_INDICATOR(EasyCastStructure):
    PayloadSize: UInt32
    IndicatorStatus: UInt32
class WINBIO_STORAGE_INTERFACE(EasyCastStructure):
    Version: Windows.Win32.Devices.BiometricFramework.WINBIO_ADAPTER_INTERFACE_VERSION
    Type: UInt32
    Size: UIntPtr
    AdapterId: Guid
    Attach: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_ATTACH_FN
    Detach: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_DETACH_FN
    ClearContext: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_CLEAR_CONTEXT_FN
    CreateDatabase: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_CREATE_DATABASE_FN
    EraseDatabase: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_ERASE_DATABASE_FN
    OpenDatabase: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_OPEN_DATABASE_FN
    CloseDatabase: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_CLOSE_DATABASE_FN
    GetDataFormat: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_GET_DATA_FORMAT_FN
    GetDatabaseSize: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_GET_DATABASE_SIZE_FN
    AddRecord: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_ADD_RECORD_FN
    DeleteRecord: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_DELETE_RECORD_FN
    QueryBySubject: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_QUERY_BY_SUBJECT_FN
    QueryByContent: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_QUERY_BY_CONTENT_FN
    GetRecordCount: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_GET_RECORD_COUNT_FN
    FirstRecord: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_FIRST_RECORD_FN
    NextRecord: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_NEXT_RECORD_FN
    GetCurrentRecord: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_GET_CURRENT_RECORD_FN
    ControlUnit: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_CONTROL_UNIT_FN
    ControlUnitPrivileged: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_CONTROL_UNIT_PRIVILEGED_FN
    NotifyPowerChange: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_NOTIFY_POWER_CHANGE_FN
    PipelineInit: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_PIPELINE_INIT_FN
    PipelineCleanup: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_PIPELINE_CLEANUP_FN
    Activate: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_ACTIVATE_FN
    Deactivate: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_DEACTIVATE_FN
    QueryExtendedInfo: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_QUERY_EXTENDED_INFO_FN
    NotifyDatabaseChange: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_NOTIFY_DATABASE_CHANGE_FN
    Reserved1: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_RESERVED_1_FN
    Reserved2: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_RESERVED_2_FN
    UpdateRecordBegin: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_UPDATE_RECORD_BEGIN_FN
    UpdateRecordCommit: Windows.Win32.Devices.BiometricFramework.PIBIO_STORAGE_UPDATE_RECORD_COMMIT_FN
class WINBIO_STORAGE_RECORD(EasyCastStructure):
    Identity: POINTER(Windows.Win32.Devices.BiometricFramework.WINBIO_IDENTITY_head)
    SubFactor: Byte
    IndexVector: POINTER(UInt32)
    IndexElementCount: UIntPtr
    TemplateBlob: POINTER(Byte)
    TemplateBlobSize: UIntPtr
    PayloadBlob: POINTER(Byte)
    PayloadBlobSize: UIntPtr
class WINBIO_STORAGE_SCHEMA(EasyCastStructure):
    BiometricFactor: UInt32
    DatabaseId: Guid
    DataFormat: Guid
    Attributes: UInt32
    FilePath: UInt16 * 256
    ConnectionString: UInt16 * 256
class WINBIO_SUPPORTED_ALGORITHMS(EasyCastStructure):
    PayloadSize: UInt32
    WinBioHresult: Windows.Win32.Foundation.HRESULT
    NumberOfAlgorithms: UInt32
    AlgorithmData: Windows.Win32.Devices.BiometricFramework.WINBIO_DATA
class WINBIO_UNIT_SCHEMA(EasyCastStructure):
    UnitId: UInt32
    PoolType: UInt32
    BiometricFactor: UInt32
    SensorSubType: UInt32
    Capabilities: UInt32
    DeviceInstanceId: UInt16 * 256
    Description: UInt16 * 256
    Manufacturer: UInt16 * 256
    Model: UInt16 * 256
    SerialNumber: UInt16 * 256
    FirmwareVersion: Windows.Win32.Devices.BiometricFramework.WINBIO_VERSION
class WINBIO_UPDATE_FIRMWARE(EasyCastStructure):
    PayloadSize: UInt32
    FirmwareData: Windows.Win32.Devices.BiometricFramework.WINBIO_DATA
class WINBIO_VERSION(EasyCastStructure):
    MajorVersion: UInt32
    MinorVersion: UInt32
WINIBIO_ENGINE_CONTEXT = IntPtr
WINIBIO_SENSOR_CONTEXT = IntPtr
WINIBIO_STORAGE_CONTEXT = IntPtr
make_head(_module, 'PIBIO_ENGINE_ACCEPT_PRIVATE_SENSOR_TYPE_INFO_FN')
make_head(_module, 'PIBIO_ENGINE_ACCEPT_SAMPLE_DATA_FN')
make_head(_module, 'PIBIO_ENGINE_ACTIVATE_FN')
make_head(_module, 'PIBIO_ENGINE_ATTACH_FN')
make_head(_module, 'PIBIO_ENGINE_CHECK_FOR_DUPLICATE_FN')
make_head(_module, 'PIBIO_ENGINE_CLEAR_CONTEXT_FN')
make_head(_module, 'PIBIO_ENGINE_COMMIT_ENROLLMENT_FN')
make_head(_module, 'PIBIO_ENGINE_CONTROL_UNIT_FN')
make_head(_module, 'PIBIO_ENGINE_CONTROL_UNIT_PRIVILEGED_FN')
make_head(_module, 'PIBIO_ENGINE_CREATE_ENROLLMENT_AUTHENTICATED_FN')
make_head(_module, 'PIBIO_ENGINE_CREATE_ENROLLMENT_FN')
make_head(_module, 'PIBIO_ENGINE_CREATE_KEY_FN')
make_head(_module, 'PIBIO_ENGINE_DEACTIVATE_FN')
make_head(_module, 'PIBIO_ENGINE_DETACH_FN')
make_head(_module, 'PIBIO_ENGINE_DISCARD_ENROLLMENT_FN')
make_head(_module, 'PIBIO_ENGINE_EXPORT_ENGINE_DATA_FN')
make_head(_module, 'PIBIO_ENGINE_GET_ENROLLMENT_HASH_FN')
make_head(_module, 'PIBIO_ENGINE_GET_ENROLLMENT_STATUS_FN')
make_head(_module, 'PIBIO_ENGINE_IDENTIFY_ALL_FN')
make_head(_module, 'PIBIO_ENGINE_IDENTIFY_FEATURE_SET_AUTHENTICATED_FN')
make_head(_module, 'PIBIO_ENGINE_IDENTIFY_FEATURE_SET_FN')
make_head(_module, 'PIBIO_ENGINE_IDENTIFY_FEATURE_SET_SECURE_FN')
make_head(_module, 'PIBIO_ENGINE_NOTIFY_POWER_CHANGE_FN')
make_head(_module, 'PIBIO_ENGINE_PIPELINE_CLEANUP_FN')
make_head(_module, 'PIBIO_ENGINE_PIPELINE_INIT_FN')
make_head(_module, 'PIBIO_ENGINE_QUERY_CALIBRATION_DATA_FN')
make_head(_module, 'PIBIO_ENGINE_QUERY_EXTENDED_ENROLLMENT_STATUS_FN')
make_head(_module, 'PIBIO_ENGINE_QUERY_EXTENDED_INFO_FN')
make_head(_module, 'PIBIO_ENGINE_QUERY_HASH_ALGORITHMS_FN')
make_head(_module, 'PIBIO_ENGINE_QUERY_INDEX_VECTOR_SIZE_FN')
make_head(_module, 'PIBIO_ENGINE_QUERY_PREFERRED_FORMAT_FN')
make_head(_module, 'PIBIO_ENGINE_QUERY_SAMPLE_HINT_FN')
make_head(_module, 'PIBIO_ENGINE_REFRESH_CACHE_FN')
make_head(_module, 'PIBIO_ENGINE_RESERVED_1_FN')
make_head(_module, 'PIBIO_ENGINE_SELECT_CALIBRATION_FORMAT_FN')
make_head(_module, 'PIBIO_ENGINE_SET_ACCOUNT_POLICY_FN')
make_head(_module, 'PIBIO_ENGINE_SET_ENROLLMENT_PARAMETERS_FN')
make_head(_module, 'PIBIO_ENGINE_SET_ENROLLMENT_SELECTOR_FN')
make_head(_module, 'PIBIO_ENGINE_SET_HASH_ALGORITHM_FN')
make_head(_module, 'PIBIO_ENGINE_UPDATE_ENROLLMENT_FN')
make_head(_module, 'PIBIO_ENGINE_VERIFY_FEATURE_SET_FN')
make_head(_module, 'PIBIO_FRAMEWORK_ALLOCATE_MEMORY_FN')
make_head(_module, 'PIBIO_FRAMEWORK_FREE_MEMORY_FN')
make_head(_module, 'PIBIO_FRAMEWORK_GET_PROPERTY_FN')
make_head(_module, 'PIBIO_FRAMEWORK_LOCK_AND_VALIDATE_SECURE_BUFFER_FN')
make_head(_module, 'PIBIO_FRAMEWORK_RELEASE_SECURE_BUFFER_FN')
make_head(_module, 'PIBIO_FRAMEWORK_SET_UNIT_STATUS_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_CACHE_CLEAR_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_BEGIN_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_END_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_NEXT_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_BEGIN_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_END_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_NEXT_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_DECRYPT_SAMPLE_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_QUERY_AUTHORIZED_ENROLLMENTS_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_1_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_2_FN')
make_head(_module, 'PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_3_FN')
make_head(_module, 'PIBIO_SENSOR_ACCEPT_CALIBRATION_DATA_FN')
make_head(_module, 'PIBIO_SENSOR_ACTIVATE_FN')
make_head(_module, 'PIBIO_SENSOR_ASYNC_IMPORT_RAW_BUFFER_FN')
make_head(_module, 'PIBIO_SENSOR_ASYNC_IMPORT_SECURE_BUFFER_FN')
make_head(_module, 'PIBIO_SENSOR_ATTACH_FN')
make_head(_module, 'PIBIO_SENSOR_CANCEL_FN')
make_head(_module, 'PIBIO_SENSOR_CLEAR_CONTEXT_FN')
make_head(_module, 'PIBIO_SENSOR_CONNECT_SECURE_FN')
make_head(_module, 'PIBIO_SENSOR_CONTROL_UNIT_FN')
make_head(_module, 'PIBIO_SENSOR_CONTROL_UNIT_PRIVILEGED_FN')
make_head(_module, 'PIBIO_SENSOR_DEACTIVATE_FN')
make_head(_module, 'PIBIO_SENSOR_DETACH_FN')
make_head(_module, 'PIBIO_SENSOR_EXPORT_SENSOR_DATA_FN')
make_head(_module, 'PIBIO_SENSOR_FINISH_CAPTURE_FN')
make_head(_module, 'PIBIO_SENSOR_FINISH_NOTIFY_WAKE_FN')
make_head(_module, 'PIBIO_SENSOR_GET_INDICATOR_STATUS_FN')
make_head(_module, 'PIBIO_SENSOR_NOTIFY_POWER_CHANGE_FN')
make_head(_module, 'PIBIO_SENSOR_PIPELINE_CLEANUP_FN')
make_head(_module, 'PIBIO_SENSOR_PIPELINE_INIT_FN')
make_head(_module, 'PIBIO_SENSOR_PUSH_DATA_TO_ENGINE_FN')
make_head(_module, 'PIBIO_SENSOR_QUERY_CALIBRATION_FORMATS_FN')
make_head(_module, 'PIBIO_SENSOR_QUERY_EXTENDED_INFO_FN')
make_head(_module, 'PIBIO_SENSOR_QUERY_PRIVATE_SENSOR_TYPE_FN')
make_head(_module, 'PIBIO_SENSOR_QUERY_STATUS_FN')
make_head(_module, 'PIBIO_SENSOR_RESET_FN')
make_head(_module, 'PIBIO_SENSOR_SET_CALIBRATION_FORMAT_FN')
make_head(_module, 'PIBIO_SENSOR_SET_INDICATOR_STATUS_FN')
make_head(_module, 'PIBIO_SENSOR_SET_MODE_FN')
make_head(_module, 'PIBIO_SENSOR_START_CAPTURE_EX_FN')
make_head(_module, 'PIBIO_SENSOR_START_CAPTURE_FN')
make_head(_module, 'PIBIO_SENSOR_START_NOTIFY_WAKE_FN')
make_head(_module, 'PIBIO_STORAGE_ACTIVATE_FN')
make_head(_module, 'PIBIO_STORAGE_ADD_RECORD_FN')
make_head(_module, 'PIBIO_STORAGE_ATTACH_FN')
make_head(_module, 'PIBIO_STORAGE_CLEAR_CONTEXT_FN')
make_head(_module, 'PIBIO_STORAGE_CLOSE_DATABASE_FN')
make_head(_module, 'PIBIO_STORAGE_CONTROL_UNIT_FN')
make_head(_module, 'PIBIO_STORAGE_CONTROL_UNIT_PRIVILEGED_FN')
make_head(_module, 'PIBIO_STORAGE_CREATE_DATABASE_FN')
make_head(_module, 'PIBIO_STORAGE_DEACTIVATE_FN')
make_head(_module, 'PIBIO_STORAGE_DELETE_RECORD_FN')
make_head(_module, 'PIBIO_STORAGE_DETACH_FN')
make_head(_module, 'PIBIO_STORAGE_ERASE_DATABASE_FN')
make_head(_module, 'PIBIO_STORAGE_FIRST_RECORD_FN')
make_head(_module, 'PIBIO_STORAGE_GET_CURRENT_RECORD_FN')
make_head(_module, 'PIBIO_STORAGE_GET_DATABASE_SIZE_FN')
make_head(_module, 'PIBIO_STORAGE_GET_DATA_FORMAT_FN')
make_head(_module, 'PIBIO_STORAGE_GET_RECORD_COUNT_FN')
make_head(_module, 'PIBIO_STORAGE_NEXT_RECORD_FN')
make_head(_module, 'PIBIO_STORAGE_NOTIFY_DATABASE_CHANGE_FN')
make_head(_module, 'PIBIO_STORAGE_NOTIFY_POWER_CHANGE_FN')
make_head(_module, 'PIBIO_STORAGE_OPEN_DATABASE_FN')
make_head(_module, 'PIBIO_STORAGE_PIPELINE_CLEANUP_FN')
make_head(_module, 'PIBIO_STORAGE_PIPELINE_INIT_FN')
make_head(_module, 'PIBIO_STORAGE_QUERY_BY_CONTENT_FN')
make_head(_module, 'PIBIO_STORAGE_QUERY_BY_SUBJECT_FN')
make_head(_module, 'PIBIO_STORAGE_QUERY_EXTENDED_INFO_FN')
make_head(_module, 'PIBIO_STORAGE_RESERVED_1_FN')
make_head(_module, 'PIBIO_STORAGE_RESERVED_2_FN')
make_head(_module, 'PIBIO_STORAGE_UPDATE_RECORD_BEGIN_FN')
make_head(_module, 'PIBIO_STORAGE_UPDATE_RECORD_COMMIT_FN')
make_head(_module, 'PWINBIO_ASYNC_COMPLETION_CALLBACK')
make_head(_module, 'PWINBIO_CAPTURE_CALLBACK')
make_head(_module, 'PWINBIO_ENROLL_CAPTURE_CALLBACK')
make_head(_module, 'PWINBIO_EVENT_CALLBACK')
make_head(_module, 'PWINBIO_IDENTIFY_CALLBACK')
make_head(_module, 'PWINBIO_LOCATE_SENSOR_CALLBACK')
make_head(_module, 'PWINBIO_QUERY_ENGINE_INTERFACE_FN')
make_head(_module, 'PWINBIO_QUERY_SENSOR_INTERFACE_FN')
make_head(_module, 'PWINBIO_QUERY_STORAGE_INTERFACE_FN')
make_head(_module, 'PWINBIO_VERIFY_CALLBACK')
make_head(_module, 'WINBIO_ACCOUNT_POLICY')
make_head(_module, 'WINBIO_ADAPTER_INTERFACE_VERSION')
make_head(_module, 'WINBIO_ANTI_SPOOF_POLICY')
make_head(_module, 'WINBIO_ASYNC_RESULT')
make_head(_module, 'WINBIO_BDB_ANSI_381_HEADER')
make_head(_module, 'WINBIO_BDB_ANSI_381_RECORD')
make_head(_module, 'WINBIO_BIR')
make_head(_module, 'WINBIO_BIR_DATA')
make_head(_module, 'WINBIO_BIR_HEADER')
make_head(_module, 'WINBIO_BLANK_PAYLOAD')
make_head(_module, 'WINBIO_BSP_SCHEMA')
make_head(_module, 'WINBIO_CALIBRATION_INFO')
make_head(_module, 'WINBIO_CAPTURE_DATA')
make_head(_module, 'WINBIO_CAPTURE_PARAMETERS')
make_head(_module, 'WINBIO_DATA')
make_head(_module, 'WINBIO_DIAGNOSTICS')
make_head(_module, 'WINBIO_ENCRYPTED_CAPTURE_PARAMS')
make_head(_module, 'WINBIO_ENGINE_INTERFACE')
make_head(_module, 'WINBIO_EVENT')
make_head(_module, 'WINBIO_EXTENDED_ENGINE_INFO')
make_head(_module, 'WINBIO_EXTENDED_ENROLLMENT_PARAMETERS')
make_head(_module, 'WINBIO_EXTENDED_ENROLLMENT_STATUS')
make_head(_module, 'WINBIO_EXTENDED_SENSOR_INFO')
make_head(_module, 'WINBIO_EXTENDED_STORAGE_INFO')
make_head(_module, 'WINBIO_EXTENDED_UNIT_STATUS')
make_head(_module, 'WINBIO_FP_BU_STATE')
make_head(_module, 'WINBIO_FRAMEWORK_INTERFACE')
make_head(_module, 'WINBIO_GESTURE_METADATA')
make_head(_module, 'WINBIO_GET_INDICATOR')
make_head(_module, 'WINBIO_IDENTITY')
make_head(_module, 'WINBIO_NOTIFY_WAKE')
make_head(_module, 'WINBIO_PIPELINE')
make_head(_module, 'WINBIO_PRESENCE')
make_head(_module, 'WINBIO_PRESENCE_PROPERTIES')
make_head(_module, 'WINBIO_PRIVATE_SENSOR_TYPE_INFO')
make_head(_module, 'WINBIO_PROTECTION_POLICY')
make_head(_module, 'WINBIO_REGISTERED_FORMAT')
make_head(_module, 'WINBIO_SECURE_BUFFER_HEADER_V1')
make_head(_module, 'WINBIO_SECURE_CONNECTION_DATA')
make_head(_module, 'WINBIO_SECURE_CONNECTION_PARAMS')
make_head(_module, 'WINBIO_SENSOR_ATTRIBUTES')
make_head(_module, 'WINBIO_SENSOR_INTERFACE')
make_head(_module, 'WINBIO_SET_INDICATOR')
make_head(_module, 'WINBIO_STORAGE_INTERFACE')
make_head(_module, 'WINBIO_STORAGE_RECORD')
make_head(_module, 'WINBIO_STORAGE_SCHEMA')
make_head(_module, 'WINBIO_SUPPORTED_ALGORITHMS')
make_head(_module, 'WINBIO_UNIT_SCHEMA')
make_head(_module, 'WINBIO_UPDATE_FIRMWARE')
make_head(_module, 'WINBIO_VERSION')
