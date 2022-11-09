from win32more.base import *
import win32more.Devices.BiometricFramework
import win32more.Foundation
import win32more.System.IO

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
WINBIO_MAX_STRING_LEN = 256
WINBIO_SCP_VERSION_1 = 1
WINBIO_SCP_RANDOM_SIZE_V1 = 32
WINBIO_SCP_DIGEST_SIZE_V1 = 32
WINBIO_SCP_CURVE_FIELD_SIZE_V1 = 32
WINBIO_SCP_PUBLIC_KEY_SIZE_V1 = 65
WINBIO_SCP_PRIVATE_KEY_SIZE_V1 = 32
WINBIO_SCP_SIGNATURE_SIZE_V1 = 64
WINBIO_SCP_ENCRYPTION_BLOCK_SIZE_V1 = 16
WINBIO_SCP_ENCRYPTION_KEY_SIZE_V1 = 32
WINBIO_BIR_ALIGN_SIZE = 8
WINBIO_BIR_ALGIN_SIZE = 8
FACILITY_WINBIO = 9
FACILITY_NONE = 0
WINBIO_E_UNSUPPORTED_FACTOR = -2146861055
WINBIO_E_INVALID_UNIT = -2146861054
WINBIO_E_UNKNOWN_ID = -2146861053
WINBIO_E_CANCELED = -2146861052
WINBIO_E_NO_MATCH = -2146861051
WINBIO_E_CAPTURE_ABORTED = -2146861050
WINBIO_E_ENROLLMENT_IN_PROGRESS = -2146861049
WINBIO_E_BAD_CAPTURE = -2146861048
WINBIO_E_INVALID_CONTROL_CODE = -2146861047
WINBIO_E_DATA_COLLECTION_IN_PROGRESS = -2146861045
WINBIO_E_UNSUPPORTED_DATA_FORMAT = -2146861044
WINBIO_E_UNSUPPORTED_DATA_TYPE = -2146861043
WINBIO_E_UNSUPPORTED_PURPOSE = -2146861042
WINBIO_E_INVALID_DEVICE_STATE = -2146861041
WINBIO_E_DEVICE_BUSY = -2146861040
WINBIO_E_DATABASE_CANT_CREATE = -2146861039
WINBIO_E_DATABASE_CANT_OPEN = -2146861038
WINBIO_E_DATABASE_CANT_CLOSE = -2146861037
WINBIO_E_DATABASE_CANT_ERASE = -2146861036
WINBIO_E_DATABASE_CANT_FIND = -2146861035
WINBIO_E_DATABASE_ALREADY_EXISTS = -2146861034
WINBIO_E_DATABASE_FULL = -2146861032
WINBIO_E_DATABASE_LOCKED = -2146861031
WINBIO_E_DATABASE_CORRUPTED = -2146861030
WINBIO_E_DATABASE_NO_SUCH_RECORD = -2146861029
WINBIO_E_DUPLICATE_ENROLLMENT = -2146861028
WINBIO_E_DATABASE_READ_ERROR = -2146861027
WINBIO_E_DATABASE_WRITE_ERROR = -2146861026
WINBIO_E_DATABASE_NO_RESULTS = -2146861025
WINBIO_E_DATABASE_NO_MORE_RECORDS = -2146861024
WINBIO_E_DATABASE_EOF = -2146861023
WINBIO_E_DATABASE_BAD_INDEX_VECTOR = -2146861022
WINBIO_E_INCORRECT_BSP = -2146861020
WINBIO_E_INCORRECT_SENSOR_POOL = -2146861019
WINBIO_E_NO_CAPTURE_DATA = -2146861018
WINBIO_E_INVALID_SENSOR_MODE = -2146861017
WINBIO_E_LOCK_VIOLATION = -2146861014
WINBIO_E_DUPLICATE_TEMPLATE = -2146861013
WINBIO_E_INVALID_OPERATION = -2146861012
WINBIO_E_SESSION_BUSY = -2146861011
WINBIO_E_CRED_PROV_DISABLED = -2146861008
WINBIO_E_CRED_PROV_NO_CREDENTIAL = -2146861007
WINBIO_E_DISABLED = -2146861006
WINBIO_E_CONFIGURATION_FAILURE = -2146861005
WINBIO_E_SENSOR_UNAVAILABLE = -2146861004
WINBIO_E_SAS_ENABLED = -2146861003
WINBIO_E_DEVICE_FAILURE = -2146861002
WINBIO_E_FAST_USER_SWITCH_DISABLED = -2146861001
WINBIO_E_NOT_ACTIVE_CONSOLE = -2146861000
WINBIO_E_EVENT_MONITOR_ACTIVE = -2146860999
WINBIO_E_INVALID_PROPERTY_TYPE = -2146860998
WINBIO_E_INVALID_PROPERTY_ID = -2146860997
WINBIO_E_UNSUPPORTED_PROPERTY = -2146860996
WINBIO_E_ADAPTER_INTEGRITY_FAILURE = -2146860995
WINBIO_E_INCORRECT_SESSION_TYPE = -2146860994
WINBIO_E_SESSION_HANDLE_CLOSED = -2146860993
WINBIO_E_DEADLOCK_DETECTED = -2146860992
WINBIO_E_NO_PREBOOT_IDENTITY = -2146860991
WINBIO_E_MAX_ERROR_COUNT_EXCEEDED = -2146860990
WINBIO_E_AUTO_LOGON_DISABLED = -2146860989
WINBIO_E_INVALID_TICKET = -2146860988
WINBIO_E_TICKET_QUOTA_EXCEEDED = -2146860987
WINBIO_E_DATA_PROTECTION_FAILURE = -2146860986
WINBIO_E_CRED_PROV_SECURITY_LOCKOUT = -2146860985
WINBIO_E_UNSUPPORTED_POOL_TYPE = -2146860984
WINBIO_E_SELECTION_REQUIRED = -2146860983
WINBIO_E_PRESENCE_MONITOR_ACTIVE = -2146860982
WINBIO_E_INVALID_SUBFACTOR = -2146860981
WINBIO_E_INVALID_CALIBRATION_FORMAT_ARRAY = -2146860980
WINBIO_E_NO_SUPPORTED_CALIBRATION_FORMAT = -2146860979
WINBIO_E_UNSUPPORTED_SENSOR_CALIBRATION_FORMAT = -2146860978
WINBIO_E_CALIBRATION_BUFFER_TOO_SMALL = -2146860977
WINBIO_E_CALIBRATION_BUFFER_TOO_LARGE = -2146860976
WINBIO_E_CALIBRATION_BUFFER_INVALID = -2146860975
WINBIO_E_INVALID_KEY_IDENTIFIER = -2146860974
WINBIO_E_KEY_CREATION_FAILED = -2146860973
WINBIO_E_KEY_IDENTIFIER_BUFFER_TOO_SMALL = -2146860972
WINBIO_E_PROPERTY_UNAVAILABLE = -2146860971
WINBIO_E_POLICY_PROTECTION_UNAVAILABLE = -2146860970
WINBIO_E_INSECURE_SENSOR = -2146860969
WINBIO_E_INVALID_BUFFER_ID = -2146860968
WINBIO_E_INVALID_BUFFER = -2146860967
WINBIO_E_TRUSTLET_INTEGRITY_FAIL = -2146860966
WINBIO_E_ENROLLMENT_CANCELED_BY_SUSPEND = -2146860965
WINBIO_I_MORE_DATA = 589825
WINBIO_I_EXTENDED_STATUS_INFORMATION = 589826
GUID_DEVINTERFACE_BIOMETRIC_READER = 'e2b5183a-99ea-4cc3-ad6b-80ca8d715b80'
IOCTL_BIOMETRIC_VENDOR = 4464640
WINBIO_WBDI_MAJOR_VERSION = 1
WINBIO_WBDI_MINOR_VERSION = 0
WINBIO_SETTING_SOURCE = UInt32
WINBIO_SETTING_SOURCE_INVALID = 0
WINBIO_SETTING_SOURCE_DEFAULT = 1
WINBIO_SETTING_SOURCE_LOCAL = 3
WINBIO_SETTING_SOURCE_POLICY = 2
WINBIO_COMPONENT = UInt32
WINBIO_COMPONENT_SENSOR = 1
WINBIO_COMPONENT_ENGINE = 2
WINBIO_COMPONENT_STORAGE = 3
WINBIO_POOL = UInt32
WINBIO_POOL_SYSTEM = 1
WINBIO_POOL_PRIVATE = 2
def _define_WINBIO_VERSION_head():
    class WINBIO_VERSION(Structure):
        pass
    return WINBIO_VERSION
def _define_WINBIO_VERSION():
    WINBIO_VERSION = win32more.Devices.BiometricFramework.WINBIO_VERSION_head
    WINBIO_VERSION._fields_ = [
        ("MajorVersion", UInt32),
        ("MinorVersion", UInt32),
    ]
    return WINBIO_VERSION
def _define_WINBIO_IDENTITY_head():
    class WINBIO_IDENTITY(Structure):
        pass
    return WINBIO_IDENTITY
def _define_WINBIO_IDENTITY():
    WINBIO_IDENTITY = win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head
    class WINBIO_IDENTITY__Value_e__Union(Union):
        pass
    class WINBIO_IDENTITY__Value_e__Union__AccountSid_e__Struct(Structure):
        pass
    WINBIO_IDENTITY__Value_e__Union__AccountSid_e__Struct._fields_ = [
        ("Size", UInt32),
        ("Data", Byte * 68),
    ]
    WINBIO_IDENTITY__Value_e__Union._fields_ = [
        ("Null", UInt32),
        ("Wildcard", UInt32),
        ("TemplateGuid", Guid),
        ("AccountSid", WINBIO_IDENTITY__Value_e__Union__AccountSid_e__Struct),
        ("SecureId", Byte * 32),
    ]
    WINBIO_IDENTITY._fields_ = [
        ("Type", UInt32),
        ("Value", WINBIO_IDENTITY__Value_e__Union),
    ]
    return WINBIO_IDENTITY
def _define_WINBIO_SECURE_CONNECTION_PARAMS_head():
    class WINBIO_SECURE_CONNECTION_PARAMS(Structure):
        pass
    return WINBIO_SECURE_CONNECTION_PARAMS
def _define_WINBIO_SECURE_CONNECTION_PARAMS():
    WINBIO_SECURE_CONNECTION_PARAMS = win32more.Devices.BiometricFramework.WINBIO_SECURE_CONNECTION_PARAMS_head
    WINBIO_SECURE_CONNECTION_PARAMS._fields_ = [
        ("PayloadSize", UInt32),
        ("Version", UInt16),
        ("Flags", UInt16),
    ]
    return WINBIO_SECURE_CONNECTION_PARAMS
def _define_WINBIO_SECURE_CONNECTION_DATA_head():
    class WINBIO_SECURE_CONNECTION_DATA(Structure):
        pass
    return WINBIO_SECURE_CONNECTION_DATA
def _define_WINBIO_SECURE_CONNECTION_DATA():
    WINBIO_SECURE_CONNECTION_DATA = win32more.Devices.BiometricFramework.WINBIO_SECURE_CONNECTION_DATA_head
    WINBIO_SECURE_CONNECTION_DATA._fields_ = [
        ("Size", UInt32),
        ("Version", UInt16),
        ("Flags", UInt16),
        ("ModelCertificateSize", UInt32),
        ("IntermediateCA1Size", UInt32),
        ("IntermediateCA2Size", UInt32),
    ]
    return WINBIO_SECURE_CONNECTION_DATA
def _define_WINBIO_BIR_DATA_head():
    class WINBIO_BIR_DATA(Structure):
        pass
    return WINBIO_BIR_DATA
def _define_WINBIO_BIR_DATA():
    WINBIO_BIR_DATA = win32more.Devices.BiometricFramework.WINBIO_BIR_DATA_head
    WINBIO_BIR_DATA._fields_ = [
        ("Size", UInt32),
        ("Offset", UInt32),
    ]
    return WINBIO_BIR_DATA
def _define_WINBIO_BIR_head():
    class WINBIO_BIR(Structure):
        pass
    return WINBIO_BIR
def _define_WINBIO_BIR():
    WINBIO_BIR = win32more.Devices.BiometricFramework.WINBIO_BIR_head
    WINBIO_BIR._fields_ = [
        ("HeaderBlock", win32more.Devices.BiometricFramework.WINBIO_BIR_DATA),
        ("StandardDataBlock", win32more.Devices.BiometricFramework.WINBIO_BIR_DATA),
        ("VendorDataBlock", win32more.Devices.BiometricFramework.WINBIO_BIR_DATA),
        ("SignatureBlock", win32more.Devices.BiometricFramework.WINBIO_BIR_DATA),
    ]
    return WINBIO_BIR
def _define_WINBIO_REGISTERED_FORMAT_head():
    class WINBIO_REGISTERED_FORMAT(Structure):
        pass
    return WINBIO_REGISTERED_FORMAT
def _define_WINBIO_REGISTERED_FORMAT():
    WINBIO_REGISTERED_FORMAT = win32more.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT_head
    WINBIO_REGISTERED_FORMAT._fields_ = [
        ("Owner", UInt16),
        ("Type", UInt16),
    ]
    return WINBIO_REGISTERED_FORMAT
def _define_WINBIO_BIR_HEADER_head():
    class WINBIO_BIR_HEADER(Structure):
        pass
    return WINBIO_BIR_HEADER
def _define_WINBIO_BIR_HEADER():
    WINBIO_BIR_HEADER = win32more.Devices.BiometricFramework.WINBIO_BIR_HEADER_head
    class WINBIO_BIR_HEADER__ValidityPeriod_e__Struct(Structure):
        pass
    WINBIO_BIR_HEADER__ValidityPeriod_e__Struct._fields_ = [
        ("BeginDate", win32more.Foundation.LARGE_INTEGER),
        ("EndDate", win32more.Foundation.LARGE_INTEGER),
    ]
    WINBIO_BIR_HEADER._fields_ = [
        ("ValidFields", UInt16),
        ("HeaderVersion", Byte),
        ("PatronHeaderVersion", Byte),
        ("DataFlags", Byte),
        ("Type", UInt32),
        ("Subtype", Byte),
        ("Purpose", Byte),
        ("DataQuality", SByte),
        ("CreationDate", win32more.Foundation.LARGE_INTEGER),
        ("ValidityPeriod", WINBIO_BIR_HEADER__ValidityPeriod_e__Struct),
        ("BiometricDataFormat", win32more.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT),
        ("ProductId", win32more.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT),
    ]
    return WINBIO_BIR_HEADER
def _define_WINBIO_BDB_ANSI_381_HEADER_head():
    class WINBIO_BDB_ANSI_381_HEADER(Structure):
        pass
    return WINBIO_BDB_ANSI_381_HEADER
def _define_WINBIO_BDB_ANSI_381_HEADER():
    WINBIO_BDB_ANSI_381_HEADER = win32more.Devices.BiometricFramework.WINBIO_BDB_ANSI_381_HEADER_head
    WINBIO_BDB_ANSI_381_HEADER._fields_ = [
        ("RecordLength", UInt64),
        ("FormatIdentifier", UInt32),
        ("VersionNumber", UInt32),
        ("ProductId", win32more.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT),
        ("CaptureDeviceId", UInt16),
        ("ImageAcquisitionLevel", UInt16),
        ("HorizontalScanResolution", UInt16),
        ("VerticalScanResolution", UInt16),
        ("HorizontalImageResolution", UInt16),
        ("VerticalImageResolution", UInt16),
        ("ElementCount", Byte),
        ("ScaleUnits", Byte),
        ("PixelDepth", Byte),
        ("ImageCompressionAlg", Byte),
        ("Reserved", UInt16),
    ]
    return WINBIO_BDB_ANSI_381_HEADER
def _define_WINBIO_BDB_ANSI_381_RECORD_head():
    class WINBIO_BDB_ANSI_381_RECORD(Structure):
        pass
    return WINBIO_BDB_ANSI_381_RECORD
def _define_WINBIO_BDB_ANSI_381_RECORD():
    WINBIO_BDB_ANSI_381_RECORD = win32more.Devices.BiometricFramework.WINBIO_BDB_ANSI_381_RECORD_head
    WINBIO_BDB_ANSI_381_RECORD._fields_ = [
        ("BlockLength", UInt32),
        ("HorizontalLineLength", UInt16),
        ("VerticalLineLength", UInt16),
        ("Position", Byte),
        ("CountOfViews", Byte),
        ("ViewNumber", Byte),
        ("ImageQuality", Byte),
        ("ImpressionType", Byte),
        ("Reserved", Byte),
    ]
    return WINBIO_BDB_ANSI_381_RECORD
def _define_WINBIO_SECURE_BUFFER_HEADER_V1_head():
    class WINBIO_SECURE_BUFFER_HEADER_V1(Structure):
        pass
    return WINBIO_SECURE_BUFFER_HEADER_V1
def _define_WINBIO_SECURE_BUFFER_HEADER_V1():
    WINBIO_SECURE_BUFFER_HEADER_V1 = win32more.Devices.BiometricFramework.WINBIO_SECURE_BUFFER_HEADER_V1_head
    WINBIO_SECURE_BUFFER_HEADER_V1._fields_ = [
        ("Type", UInt32),
        ("Size", UInt32),
        ("Flags", UInt32),
        ("ValidationTag", UInt64),
    ]
    return WINBIO_SECURE_BUFFER_HEADER_V1
def _define_WINBIO_EVENT_head():
    class WINBIO_EVENT(Structure):
        pass
    return WINBIO_EVENT
def _define_WINBIO_EVENT():
    WINBIO_EVENT = win32more.Devices.BiometricFramework.WINBIO_EVENT_head
    class WINBIO_EVENT__Parameters_e__Union(Union):
        pass
    class WINBIO_EVENT__Parameters_e__Union__UnclaimedIdentify_e__Struct(Structure):
        pass
    WINBIO_EVENT__Parameters_e__Union__UnclaimedIdentify_e__Struct._fields_ = [
        ("UnitId", UInt32),
        ("Identity", win32more.Devices.BiometricFramework.WINBIO_IDENTITY),
        ("SubFactor", Byte),
        ("RejectDetail", UInt32),
    ]
    class WINBIO_EVENT__Parameters_e__Union__Unclaimed_e__Struct(Structure):
        pass
    WINBIO_EVENT__Parameters_e__Union__Unclaimed_e__Struct._fields_ = [
        ("UnitId", UInt32),
        ("RejectDetail", UInt32),
    ]
    class WINBIO_EVENT__Parameters_e__Union__Error_e__Struct(Structure):
        pass
    WINBIO_EVENT__Parameters_e__Union__Error_e__Struct._fields_ = [
        ("ErrorCode", win32more.Foundation.HRESULT),
    ]
    WINBIO_EVENT__Parameters_e__Union._fields_ = [
        ("Unclaimed", WINBIO_EVENT__Parameters_e__Union__Unclaimed_e__Struct),
        ("UnclaimedIdentify", WINBIO_EVENT__Parameters_e__Union__UnclaimedIdentify_e__Struct),
        ("Error", WINBIO_EVENT__Parameters_e__Union__Error_e__Struct),
    ]
    WINBIO_EVENT._fields_ = [
        ("Type", UInt32),
        ("Parameters", WINBIO_EVENT__Parameters_e__Union),
    ]
    return WINBIO_EVENT
def _define_WINBIO_PRESENCE_PROPERTIES_head():
    class WINBIO_PRESENCE_PROPERTIES(Union):
        pass
    return WINBIO_PRESENCE_PROPERTIES
def _define_WINBIO_PRESENCE_PROPERTIES():
    WINBIO_PRESENCE_PROPERTIES = win32more.Devices.BiometricFramework.WINBIO_PRESENCE_PROPERTIES_head
    class WINBIO_PRESENCE_PROPERTIES__Iris_e__Struct(Structure):
        pass
    WINBIO_PRESENCE_PROPERTIES__Iris_e__Struct._fields_ = [
        ("EyeBoundingBox_1", win32more.Foundation.RECT),
        ("EyeBoundingBox_2", win32more.Foundation.RECT),
        ("PupilCenter_1", win32more.Foundation.POINT),
        ("PupilCenter_2", win32more.Foundation.POINT),
        ("Distance", Int32),
    ]
    class WINBIO_PRESENCE_PROPERTIES__FacialFeatures_e__Struct(Structure):
        pass
    class WINBIO_PRESENCE_PROPERTIES__FacialFeatures_e__Struct__OpaqueEngineData_e__Struct(Structure):
        pass
    WINBIO_PRESENCE_PROPERTIES__FacialFeatures_e__Struct__OpaqueEngineData_e__Struct._fields_ = [
        ("AdapterId", Guid),
        ("Data", UInt32 * 78),
    ]
    WINBIO_PRESENCE_PROPERTIES__FacialFeatures_e__Struct._fields_ = [
        ("BoundingBox", win32more.Foundation.RECT),
        ("Distance", Int32),
        ("OpaqueEngineData", WINBIO_PRESENCE_PROPERTIES__FacialFeatures_e__Struct__OpaqueEngineData_e__Struct),
    ]
    WINBIO_PRESENCE_PROPERTIES._fields_ = [
        ("FacialFeatures", WINBIO_PRESENCE_PROPERTIES__FacialFeatures_e__Struct),
        ("Iris", WINBIO_PRESENCE_PROPERTIES__Iris_e__Struct),
    ]
    return WINBIO_PRESENCE_PROPERTIES
def _define_WINBIO_PRESENCE_head():
    class WINBIO_PRESENCE(Structure):
        pass
    return WINBIO_PRESENCE
def _define_WINBIO_PRESENCE():
    WINBIO_PRESENCE = win32more.Devices.BiometricFramework.WINBIO_PRESENCE_head
    class WINBIO_PRESENCE__Authorization_e__Struct(Structure):
        pass
    WINBIO_PRESENCE__Authorization_e__Struct._fields_ = [
        ("Size", UInt32),
        ("Data", Byte * 32),
    ]
    WINBIO_PRESENCE._fields_ = [
        ("Factor", UInt32),
        ("SubFactor", Byte),
        ("Status", win32more.Foundation.HRESULT),
        ("RejectDetail", UInt32),
        ("Identity", win32more.Devices.BiometricFramework.WINBIO_IDENTITY),
        ("TrackingId", UInt64),
        ("Ticket", UInt64),
        ("Properties", win32more.Devices.BiometricFramework.WINBIO_PRESENCE_PROPERTIES),
        ("Authorization", WINBIO_PRESENCE__Authorization_e__Struct),
    ]
    return WINBIO_PRESENCE
def _define_WINBIO_BSP_SCHEMA_head():
    class WINBIO_BSP_SCHEMA(Structure):
        pass
    return WINBIO_BSP_SCHEMA
def _define_WINBIO_BSP_SCHEMA():
    WINBIO_BSP_SCHEMA = win32more.Devices.BiometricFramework.WINBIO_BSP_SCHEMA_head
    WINBIO_BSP_SCHEMA._fields_ = [
        ("BiometricFactor", UInt32),
        ("BspId", Guid),
        ("Description", UInt16 * 256),
        ("Vendor", UInt16 * 256),
        ("Version", win32more.Devices.BiometricFramework.WINBIO_VERSION),
    ]
    return WINBIO_BSP_SCHEMA
def _define_WINBIO_UNIT_SCHEMA_head():
    class WINBIO_UNIT_SCHEMA(Structure):
        pass
    return WINBIO_UNIT_SCHEMA
def _define_WINBIO_UNIT_SCHEMA():
    WINBIO_UNIT_SCHEMA = win32more.Devices.BiometricFramework.WINBIO_UNIT_SCHEMA_head
    WINBIO_UNIT_SCHEMA._fields_ = [
        ("UnitId", UInt32),
        ("PoolType", UInt32),
        ("BiometricFactor", UInt32),
        ("SensorSubType", UInt32),
        ("Capabilities", UInt32),
        ("DeviceInstanceId", UInt16 * 256),
        ("Description", UInt16 * 256),
        ("Manufacturer", UInt16 * 256),
        ("Model", UInt16 * 256),
        ("SerialNumber", UInt16 * 256),
        ("FirmwareVersion", win32more.Devices.BiometricFramework.WINBIO_VERSION),
    ]
    return WINBIO_UNIT_SCHEMA
def _define_WINBIO_STORAGE_SCHEMA_head():
    class WINBIO_STORAGE_SCHEMA(Structure):
        pass
    return WINBIO_STORAGE_SCHEMA
def _define_WINBIO_STORAGE_SCHEMA():
    WINBIO_STORAGE_SCHEMA = win32more.Devices.BiometricFramework.WINBIO_STORAGE_SCHEMA_head
    WINBIO_STORAGE_SCHEMA._fields_ = [
        ("BiometricFactor", UInt32),
        ("DatabaseId", Guid),
        ("DataFormat", Guid),
        ("Attributes", UInt32),
        ("FilePath", UInt16 * 256),
        ("ConnectionString", UInt16 * 256),
    ]
    return WINBIO_STORAGE_SCHEMA
def _define_WINBIO_EXTENDED_SENSOR_INFO_head():
    class WINBIO_EXTENDED_SENSOR_INFO(Structure):
        pass
    return WINBIO_EXTENDED_SENSOR_INFO
def _define_WINBIO_EXTENDED_SENSOR_INFO():
    WINBIO_EXTENDED_SENSOR_INFO = win32more.Devices.BiometricFramework.WINBIO_EXTENDED_SENSOR_INFO_head
    class WINBIO_EXTENDED_SENSOR_INFO__Specific_e__Union(Union):
        pass
    class WINBIO_EXTENDED_SENSOR_INFO__Specific_e__Union__Iris_e__Struct(Structure):
        pass
    WINBIO_EXTENDED_SENSOR_INFO__Specific_e__Union__Iris_e__Struct._fields_ = [
        ("FrameSize", win32more.Foundation.RECT),
        ("FrameOffset", win32more.Foundation.POINT),
        ("MandatoryOrientation", UInt32),
    ]
    class WINBIO_EXTENDED_SENSOR_INFO__Specific_e__Union__FacialFeatures_e__Struct(Structure):
        pass
    class WINBIO_EXTENDED_SENSOR_INFO__Specific_e__Union__FacialFeatures_e__Struct__HardwareInfo_e__Struct(Structure):
        pass
    WINBIO_EXTENDED_SENSOR_INFO__Specific_e__Union__FacialFeatures_e__Struct__HardwareInfo_e__Struct._fields_ = [
        ("ColorSensorId", Char * 260),
        ("InfraredSensorId", Char * 260),
        ("InfraredSensorRotationAngle", UInt32),
    ]
    WINBIO_EXTENDED_SENSOR_INFO__Specific_e__Union__FacialFeatures_e__Struct._fields_ = [
        ("FrameSize", win32more.Foundation.RECT),
        ("FrameOffset", win32more.Foundation.POINT),
        ("MandatoryOrientation", UInt32),
        ("HardwareInfo", WINBIO_EXTENDED_SENSOR_INFO__Specific_e__Union__FacialFeatures_e__Struct__HardwareInfo_e__Struct),
    ]
    class WINBIO_EXTENDED_SENSOR_INFO__Specific_e__Union__Fingerprint_e__Struct(Structure):
        pass
    WINBIO_EXTENDED_SENSOR_INFO__Specific_e__Union__Fingerprint_e__Struct._fields_ = [
        ("Reserved", UInt32),
    ]
    class WINBIO_EXTENDED_SENSOR_INFO__Specific_e__Union__Voice_e__Struct(Structure):
        pass
    WINBIO_EXTENDED_SENSOR_INFO__Specific_e__Union__Voice_e__Struct._fields_ = [
        ("Reserved", UInt32),
    ]
    WINBIO_EXTENDED_SENSOR_INFO__Specific_e__Union._fields_ = [
        ("Null", UInt32),
        ("FacialFeatures", WINBIO_EXTENDED_SENSOR_INFO__Specific_e__Union__FacialFeatures_e__Struct),
        ("Fingerprint", WINBIO_EXTENDED_SENSOR_INFO__Specific_e__Union__Fingerprint_e__Struct),
        ("Iris", WINBIO_EXTENDED_SENSOR_INFO__Specific_e__Union__Iris_e__Struct),
        ("Voice", WINBIO_EXTENDED_SENSOR_INFO__Specific_e__Union__Voice_e__Struct),
    ]
    WINBIO_EXTENDED_SENSOR_INFO._fields_ = [
        ("GenericSensorCapabilities", UInt32),
        ("Factor", UInt32),
        ("Specific", WINBIO_EXTENDED_SENSOR_INFO__Specific_e__Union),
    ]
    return WINBIO_EXTENDED_SENSOR_INFO
def _define_WINBIO_EXTENDED_ENGINE_INFO_head():
    class WINBIO_EXTENDED_ENGINE_INFO(Structure):
        pass
    return WINBIO_EXTENDED_ENGINE_INFO
def _define_WINBIO_EXTENDED_ENGINE_INFO():
    WINBIO_EXTENDED_ENGINE_INFO = win32more.Devices.BiometricFramework.WINBIO_EXTENDED_ENGINE_INFO_head
    class WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union(Union):
        pass
    class WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__Voice_e__Struct(Structure):
        pass
    class WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__Voice_e__Struct__EnrollmentRequirements_e__Struct(Structure):
        pass
    WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__Voice_e__Struct__EnrollmentRequirements_e__Struct._fields_ = [
        ("Null", UInt32),
    ]
    WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__Voice_e__Struct._fields_ = [
        ("Capabilities", UInt32),
        ("EnrollmentRequirements", WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__Voice_e__Struct__EnrollmentRequirements_e__Struct),
    ]
    class WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__Iris_e__Struct(Structure):
        pass
    class WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__Iris_e__Struct__EnrollmentRequirements_e__Struct(Structure):
        pass
    WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__Iris_e__Struct__EnrollmentRequirements_e__Struct._fields_ = [
        ("Null", UInt32),
    ]
    WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__Iris_e__Struct._fields_ = [
        ("Capabilities", UInt32),
        ("EnrollmentRequirements", WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__Iris_e__Struct__EnrollmentRequirements_e__Struct),
    ]
    class WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__Fingerprint_e__Struct(Structure):
        pass
    class WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__Fingerprint_e__Struct__EnrollmentRequirements_e__Struct(Structure):
        pass
    WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__Fingerprint_e__Struct__EnrollmentRequirements_e__Struct._fields_ = [
        ("GeneralSamples", UInt32),
        ("Center", UInt32),
        ("TopEdge", UInt32),
        ("BottomEdge", UInt32),
        ("LeftEdge", UInt32),
        ("RightEdge", UInt32),
    ]
    WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__Fingerprint_e__Struct._fields_ = [
        ("Capabilities", UInt32),
        ("EnrollmentRequirements", WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__Fingerprint_e__Struct__EnrollmentRequirements_e__Struct),
    ]
    class WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__FacialFeatures_e__Struct(Structure):
        pass
    class WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__FacialFeatures_e__Struct__EnrollmentRequirements_e__Struct(Structure):
        pass
    WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__FacialFeatures_e__Struct__EnrollmentRequirements_e__Struct._fields_ = [
        ("Null", UInt32),
    ]
    WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__FacialFeatures_e__Struct._fields_ = [
        ("Capabilities", UInt32),
        ("EnrollmentRequirements", WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__FacialFeatures_e__Struct__EnrollmentRequirements_e__Struct),
    ]
    WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union._fields_ = [
        ("Null", UInt32),
        ("FacialFeatures", WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__FacialFeatures_e__Struct),
        ("Fingerprint", WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__Fingerprint_e__Struct),
        ("Iris", WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__Iris_e__Struct),
        ("Voice", WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union__Voice_e__Struct),
    ]
    WINBIO_EXTENDED_ENGINE_INFO._fields_ = [
        ("GenericEngineCapabilities", UInt32),
        ("Factor", UInt32),
        ("Specific", WINBIO_EXTENDED_ENGINE_INFO__Specific_e__Union),
    ]
    return WINBIO_EXTENDED_ENGINE_INFO
def _define_WINBIO_EXTENDED_STORAGE_INFO_head():
    class WINBIO_EXTENDED_STORAGE_INFO(Structure):
        pass
    return WINBIO_EXTENDED_STORAGE_INFO
def _define_WINBIO_EXTENDED_STORAGE_INFO():
    WINBIO_EXTENDED_STORAGE_INFO = win32more.Devices.BiometricFramework.WINBIO_EXTENDED_STORAGE_INFO_head
    class WINBIO_EXTENDED_STORAGE_INFO__Specific_e__Union(Union):
        pass
    class WINBIO_EXTENDED_STORAGE_INFO__Specific_e__Union__Iris_e__Struct(Structure):
        pass
    WINBIO_EXTENDED_STORAGE_INFO__Specific_e__Union__Iris_e__Struct._fields_ = [
        ("Capabilities", UInt32),
    ]
    class WINBIO_EXTENDED_STORAGE_INFO__Specific_e__Union__FacialFeatures_e__Struct(Structure):
        pass
    WINBIO_EXTENDED_STORAGE_INFO__Specific_e__Union__FacialFeatures_e__Struct._fields_ = [
        ("Capabilities", UInt32),
    ]
    class WINBIO_EXTENDED_STORAGE_INFO__Specific_e__Union__Fingerprint_e__Struct(Structure):
        pass
    WINBIO_EXTENDED_STORAGE_INFO__Specific_e__Union__Fingerprint_e__Struct._fields_ = [
        ("Capabilities", UInt32),
    ]
    class WINBIO_EXTENDED_STORAGE_INFO__Specific_e__Union__Voice_e__Struct(Structure):
        pass
    WINBIO_EXTENDED_STORAGE_INFO__Specific_e__Union__Voice_e__Struct._fields_ = [
        ("Capabilities", UInt32),
    ]
    WINBIO_EXTENDED_STORAGE_INFO__Specific_e__Union._fields_ = [
        ("Null", UInt32),
        ("FacialFeatures", WINBIO_EXTENDED_STORAGE_INFO__Specific_e__Union__FacialFeatures_e__Struct),
        ("Fingerprint", WINBIO_EXTENDED_STORAGE_INFO__Specific_e__Union__Fingerprint_e__Struct),
        ("Iris", WINBIO_EXTENDED_STORAGE_INFO__Specific_e__Union__Iris_e__Struct),
        ("Voice", WINBIO_EXTENDED_STORAGE_INFO__Specific_e__Union__Voice_e__Struct),
    ]
    WINBIO_EXTENDED_STORAGE_INFO._fields_ = [
        ("GenericStorageCapabilities", UInt32),
        ("Factor", UInt32),
        ("Specific", WINBIO_EXTENDED_STORAGE_INFO__Specific_e__Union),
    ]
    return WINBIO_EXTENDED_STORAGE_INFO
def _define_WINBIO_EXTENDED_ENROLLMENT_STATUS_head():
    class WINBIO_EXTENDED_ENROLLMENT_STATUS(Structure):
        pass
    return WINBIO_EXTENDED_ENROLLMENT_STATUS
def _define_WINBIO_EXTENDED_ENROLLMENT_STATUS():
    WINBIO_EXTENDED_ENROLLMENT_STATUS = win32more.Devices.BiometricFramework.WINBIO_EXTENDED_ENROLLMENT_STATUS_head
    class WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union(Union):
        pass
    class WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union__Voice_e__Struct(Structure):
        pass
    WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union__Voice_e__Struct._fields_ = [
        ("Reserved", UInt32),
    ]
    class WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union__Iris_e__Struct(Structure):
        pass
    class WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union__Iris_e__Struct__Point3D_e__Struct(Structure):
        pass
    WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union__Iris_e__Struct__Point3D_e__Struct._fields_ = [
        ("X", Double),
        ("Y", Double),
        ("Z", Double),
    ]
    WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union__Iris_e__Struct._fields_ = [
        ("EyeBoundingBox_1", win32more.Foundation.RECT),
        ("EyeBoundingBox_2", win32more.Foundation.RECT),
        ("PupilCenter_1", win32more.Foundation.POINT),
        ("PupilCenter_2", win32more.Foundation.POINT),
        ("Distance", Int32),
        ("GridPointCompletionPercent", UInt32),
        ("GridPointIndex", UInt16),
        ("Point3D", WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union__Iris_e__Struct__Point3D_e__Struct),
        ("StopCaptureAndShowCriticalFeedback", win32more.Foundation.BOOL),
    ]
    class WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union__FacialFeatures_e__Struct(Structure):
        pass
    class WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union__FacialFeatures_e__Struct__OpaqueEngineData_e__Struct(Structure):
        pass
    WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union__FacialFeatures_e__Struct__OpaqueEngineData_e__Struct._fields_ = [
        ("AdapterId", Guid),
        ("Data", UInt32 * 78),
    ]
    WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union__FacialFeatures_e__Struct._fields_ = [
        ("BoundingBox", win32more.Foundation.RECT),
        ("Distance", Int32),
        ("OpaqueEngineData", WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union__FacialFeatures_e__Struct__OpaqueEngineData_e__Struct),
    ]
    class WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union__Fingerprint_e__Struct(Structure):
        pass
    WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union__Fingerprint_e__Struct._fields_ = [
        ("GeneralSamples", UInt32),
        ("Center", UInt32),
        ("TopEdge", UInt32),
        ("BottomEdge", UInt32),
        ("LeftEdge", UInt32),
        ("RightEdge", UInt32),
    ]
    WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union._fields_ = [
        ("Null", UInt32),
        ("FacialFeatures", WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union__FacialFeatures_e__Struct),
        ("Fingerprint", WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union__Fingerprint_e__Struct),
        ("Iris", WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union__Iris_e__Struct),
        ("Voice", WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union__Voice_e__Struct),
    ]
    WINBIO_EXTENDED_ENROLLMENT_STATUS._fields_ = [
        ("TemplateStatus", win32more.Foundation.HRESULT),
        ("RejectDetail", UInt32),
        ("PercentComplete", UInt32),
        ("Factor", UInt32),
        ("SubFactor", Byte),
        ("Specific", WINBIO_EXTENDED_ENROLLMENT_STATUS__Specific_e__Union),
    ]
    return WINBIO_EXTENDED_ENROLLMENT_STATUS
def _define_WINBIO_EXTENDED_UNIT_STATUS_head():
    class WINBIO_EXTENDED_UNIT_STATUS(Structure):
        pass
    return WINBIO_EXTENDED_UNIT_STATUS
def _define_WINBIO_EXTENDED_UNIT_STATUS():
    WINBIO_EXTENDED_UNIT_STATUS = win32more.Devices.BiometricFramework.WINBIO_EXTENDED_UNIT_STATUS_head
    WINBIO_EXTENDED_UNIT_STATUS._fields_ = [
        ("Availability", UInt32),
        ("ReasonCode", UInt32),
    ]
    return WINBIO_EXTENDED_UNIT_STATUS
def _define_WINBIO_FP_BU_STATE_head():
    class WINBIO_FP_BU_STATE(Structure):
        pass
    return WINBIO_FP_BU_STATE
def _define_WINBIO_FP_BU_STATE():
    WINBIO_FP_BU_STATE = win32more.Devices.BiometricFramework.WINBIO_FP_BU_STATE_head
    WINBIO_FP_BU_STATE._fields_ = [
        ("SensorAttached", win32more.Foundation.BOOL),
        ("CreationResult", win32more.Foundation.HRESULT),
    ]
    return WINBIO_FP_BU_STATE
WINBIO_ANTI_SPOOF_POLICY_ACTION = Int32
WINBIO_ANTI_SPOOF_DISABLE = 0
WINBIO_ANTI_SPOOF_ENABLE = 1
WINBIO_ANTI_SPOOF_REMOVE = 2
WINBIO_POLICY_SOURCE = Int32
WINBIO_POLICY_UNKNOWN = 0
WINBIO_POLICY_DEFAULT = 1
WINBIO_POLICY_LOCAL = 2
WINBIO_POLICY_ADMIN = 3
def _define_WINBIO_ANTI_SPOOF_POLICY_head():
    class WINBIO_ANTI_SPOOF_POLICY(Structure):
        pass
    return WINBIO_ANTI_SPOOF_POLICY
def _define_WINBIO_ANTI_SPOOF_POLICY():
    WINBIO_ANTI_SPOOF_POLICY = win32more.Devices.BiometricFramework.WINBIO_ANTI_SPOOF_POLICY_head
    WINBIO_ANTI_SPOOF_POLICY._fields_ = [
        ("Action", win32more.Devices.BiometricFramework.WINBIO_ANTI_SPOOF_POLICY_ACTION),
        ("Source", win32more.Devices.BiometricFramework.WINBIO_POLICY_SOURCE),
    ]
    return WINBIO_ANTI_SPOOF_POLICY
WINBIO_CREDENTIAL_TYPE = Int32
WINBIO_CREDENTIAL_PASSWORD = 1
WINBIO_CREDENTIAL_ALL = -1
WINBIO_CREDENTIAL_FORMAT = Int32
WINBIO_PASSWORD_GENERIC = 1
WINBIO_PASSWORD_PACKED = 2
WINBIO_PASSWORD_PROTECTED = 3
WINBIO_CREDENTIAL_STATE = Int32
WINBIO_CREDENTIAL_NOT_SET = 1
WINBIO_CREDENTIAL_SET = 2
def _define_WINBIO_EXTENDED_ENROLLMENT_PARAMETERS_head():
    class WINBIO_EXTENDED_ENROLLMENT_PARAMETERS(Structure):
        pass
    return WINBIO_EXTENDED_ENROLLMENT_PARAMETERS
def _define_WINBIO_EXTENDED_ENROLLMENT_PARAMETERS():
    WINBIO_EXTENDED_ENROLLMENT_PARAMETERS = win32more.Devices.BiometricFramework.WINBIO_EXTENDED_ENROLLMENT_PARAMETERS_head
    WINBIO_EXTENDED_ENROLLMENT_PARAMETERS._fields_ = [
        ("Size", UIntPtr),
        ("SubFactor", Byte),
    ]
    return WINBIO_EXTENDED_ENROLLMENT_PARAMETERS
def _define_WINBIO_ACCOUNT_POLICY_head():
    class WINBIO_ACCOUNT_POLICY(Structure):
        pass
    return WINBIO_ACCOUNT_POLICY
def _define_WINBIO_ACCOUNT_POLICY():
    WINBIO_ACCOUNT_POLICY = win32more.Devices.BiometricFramework.WINBIO_ACCOUNT_POLICY_head
    WINBIO_ACCOUNT_POLICY._fields_ = [
        ("Identity", win32more.Devices.BiometricFramework.WINBIO_IDENTITY),
        ("AntiSpoofBehavior", win32more.Devices.BiometricFramework.WINBIO_ANTI_SPOOF_POLICY_ACTION),
    ]
    return WINBIO_ACCOUNT_POLICY
def _define_WINBIO_PROTECTION_POLICY_head():
    class WINBIO_PROTECTION_POLICY(Structure):
        pass
    return WINBIO_PROTECTION_POLICY
def _define_WINBIO_PROTECTION_POLICY():
    WINBIO_PROTECTION_POLICY = win32more.Devices.BiometricFramework.WINBIO_PROTECTION_POLICY_head
    WINBIO_PROTECTION_POLICY._fields_ = [
        ("Version", UInt32),
        ("Identity", win32more.Devices.BiometricFramework.WINBIO_IDENTITY),
        ("DatabaseId", Guid),
        ("UserState", UInt64),
        ("PolicySize", UIntPtr),
        ("Policy", Byte * 128),
    ]
    return WINBIO_PROTECTION_POLICY
def _define_WINBIO_GESTURE_METADATA_head():
    class WINBIO_GESTURE_METADATA(Structure):
        pass
    return WINBIO_GESTURE_METADATA
def _define_WINBIO_GESTURE_METADATA():
    WINBIO_GESTURE_METADATA = win32more.Devices.BiometricFramework.WINBIO_GESTURE_METADATA_head
    WINBIO_GESTURE_METADATA._fields_ = [
        ("Size", UIntPtr),
        ("BiometricType", UInt32),
        ("MatchType", UInt32),
        ("ProtectionType", UInt32),
    ]
    return WINBIO_GESTURE_METADATA
WINBIO_ASYNC_NOTIFICATION_METHOD = Int32
WINBIO_ASYNC_NOTIFY_NONE = 0
WINBIO_ASYNC_NOTIFY_CALLBACK = 1
WINBIO_ASYNC_NOTIFY_MESSAGE = 2
WINBIO_ASYNC_NOTIFY_MAXIMUM_VALUE = 3
def _define_WINBIO_ASYNC_RESULT_head():
    class WINBIO_ASYNC_RESULT(Structure):
        pass
    return WINBIO_ASYNC_RESULT
def _define_WINBIO_ASYNC_RESULT():
    WINBIO_ASYNC_RESULT = win32more.Devices.BiometricFramework.WINBIO_ASYNC_RESULT_head
    class WINBIO_ASYNC_RESULT__Parameters_e__Union(Union):
        pass
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__GetProtectionPolicy_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__GetProtectionPolicy_e__Struct._fields_ = [
        ("Identity", win32more.Devices.BiometricFramework.WINBIO_IDENTITY),
        ("Policy", win32more.Devices.BiometricFramework.WINBIO_PROTECTION_POLICY),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__EnrollSelect_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__EnrollSelect_e__Struct._fields_ = [
        ("SelectorValue", UInt64),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__VerifyAndReleaseTicket_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__VerifyAndReleaseTicket_e__Struct._fields_ = [
        ("Match", win32more.Foundation.BOOLEAN),
        ("RejectDetail", UInt32),
        ("Ticket", UInt64),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__EnumBiometricUnits_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__EnumBiometricUnits_e__Struct._fields_ = [
        ("UnitCount", UIntPtr),
        ("UnitSchemaArray", POINTER(win32more.Devices.BiometricFramework.WINBIO_UNIT_SCHEMA_head)),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__ControlUnit_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__ControlUnit_e__Struct._fields_ = [
        ("Component", win32more.Devices.BiometricFramework.WINBIO_COMPONENT),
        ("ControlCode", UInt32),
        ("OperationStatus", UInt32),
        ("SendBuffer", c_char_p_no),
        ("SendBufferSize", UIntPtr),
        ("ReceiveBuffer", c_char_p_no),
        ("ReceiveBufferSize", UIntPtr),
        ("ReceiveDataSize", UIntPtr),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__SetProperty_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__SetProperty_e__Struct._fields_ = [
        ("PropertyType", UInt32),
        ("PropertyId", UInt32),
        ("Identity", win32more.Devices.BiometricFramework.WINBIO_IDENTITY),
        ("SubFactor", Byte),
        ("PropertyBufferSize", UIntPtr),
        ("PropertyBuffer", c_void_p),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__DeleteTemplate_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__DeleteTemplate_e__Struct._fields_ = [
        ("Identity", win32more.Devices.BiometricFramework.WINBIO_IDENTITY),
        ("SubFactor", Byte),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__EnumEnrollments_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__EnumEnrollments_e__Struct._fields_ = [
        ("Identity", win32more.Devices.BiometricFramework.WINBIO_IDENTITY),
        ("SubFactorCount", UIntPtr),
        ("SubFactorArray", c_char_p_no),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__EnrollCapture_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__EnrollCapture_e__Struct._fields_ = [
        ("RejectDetail", UInt32),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__Identify_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__Identify_e__Struct._fields_ = [
        ("Identity", win32more.Devices.BiometricFramework.WINBIO_IDENTITY),
        ("SubFactor", Byte),
        ("RejectDetail", UInt32),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__MonitorPresence_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__MonitorPresence_e__Struct._fields_ = [
        ("ChangeType", UInt32),
        ("PresenceCount", UIntPtr),
        ("PresenceArray", POINTER(win32more.Devices.BiometricFramework.WINBIO_PRESENCE_head)),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__EnumDatabases_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__EnumDatabases_e__Struct._fields_ = [
        ("StorageCount", UIntPtr),
        ("StorageSchemaArray", POINTER(win32more.Devices.BiometricFramework.WINBIO_STORAGE_SCHEMA_head)),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__GetEvent_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__GetEvent_e__Struct._fields_ = [
        ("Event", win32more.Devices.BiometricFramework.WINBIO_EVENT),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__CaptureSample_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__CaptureSample_e__Struct._fields_ = [
        ("Sample", POINTER(win32more.Devices.BiometricFramework.WINBIO_BIR_head)),
        ("SampleSize", UIntPtr),
        ("RejectDetail", UInt32),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__EnrollBegin_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__EnrollBegin_e__Struct._fields_ = [
        ("SubFactor", Byte),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__NotifyUnitStatusChange_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__NotifyUnitStatusChange_e__Struct._fields_ = [
        ("ExtendedStatus", win32more.Devices.BiometricFramework.WINBIO_EXTENDED_UNIT_STATUS),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__EnumServiceProviders_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__EnumServiceProviders_e__Struct._fields_ = [
        ("BspCount", UIntPtr),
        ("BspSchemaArray", POINTER(win32more.Devices.BiometricFramework.WINBIO_BSP_SCHEMA_head)),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__EnrollCommit_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__EnrollCommit_e__Struct._fields_ = [
        ("Identity", win32more.Devices.BiometricFramework.WINBIO_IDENTITY),
        ("IsNewTemplate", win32more.Foundation.BOOLEAN),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__GetProperty_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__GetProperty_e__Struct._fields_ = [
        ("PropertyType", UInt32),
        ("PropertyId", UInt32),
        ("Identity", win32more.Devices.BiometricFramework.WINBIO_IDENTITY),
        ("SubFactor", Byte),
        ("PropertyBufferSize", UIntPtr),
        ("PropertyBuffer", c_void_p),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__IdentifyAndReleaseTicket_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__IdentifyAndReleaseTicket_e__Struct._fields_ = [
        ("Identity", win32more.Devices.BiometricFramework.WINBIO_IDENTITY),
        ("SubFactor", Byte),
        ("RejectDetail", UInt32),
        ("Ticket", UInt64),
    ]
    class WINBIO_ASYNC_RESULT__Parameters_e__Union__Verify_e__Struct(Structure):
        pass
    WINBIO_ASYNC_RESULT__Parameters_e__Union__Verify_e__Struct._fields_ = [
        ("Match", win32more.Foundation.BOOLEAN),
        ("RejectDetail", UInt32),
    ]
    WINBIO_ASYNC_RESULT__Parameters_e__Union._fields_ = [
        ("Verify", WINBIO_ASYNC_RESULT__Parameters_e__Union__Verify_e__Struct),
        ("Identify", WINBIO_ASYNC_RESULT__Parameters_e__Union__Identify_e__Struct),
        ("EnrollBegin", WINBIO_ASYNC_RESULT__Parameters_e__Union__EnrollBegin_e__Struct),
        ("EnrollCapture", WINBIO_ASYNC_RESULT__Parameters_e__Union__EnrollCapture_e__Struct),
        ("EnrollCommit", WINBIO_ASYNC_RESULT__Parameters_e__Union__EnrollCommit_e__Struct),
        ("EnumEnrollments", WINBIO_ASYNC_RESULT__Parameters_e__Union__EnumEnrollments_e__Struct),
        ("CaptureSample", WINBIO_ASYNC_RESULT__Parameters_e__Union__CaptureSample_e__Struct),
        ("DeleteTemplate", WINBIO_ASYNC_RESULT__Parameters_e__Union__DeleteTemplate_e__Struct),
        ("GetProperty", WINBIO_ASYNC_RESULT__Parameters_e__Union__GetProperty_e__Struct),
        ("SetProperty", WINBIO_ASYNC_RESULT__Parameters_e__Union__SetProperty_e__Struct),
        ("GetEvent", WINBIO_ASYNC_RESULT__Parameters_e__Union__GetEvent_e__Struct),
        ("ControlUnit", WINBIO_ASYNC_RESULT__Parameters_e__Union__ControlUnit_e__Struct),
        ("EnumServiceProviders", WINBIO_ASYNC_RESULT__Parameters_e__Union__EnumServiceProviders_e__Struct),
        ("EnumBiometricUnits", WINBIO_ASYNC_RESULT__Parameters_e__Union__EnumBiometricUnits_e__Struct),
        ("EnumDatabases", WINBIO_ASYNC_RESULT__Parameters_e__Union__EnumDatabases_e__Struct),
        ("VerifyAndReleaseTicket", WINBIO_ASYNC_RESULT__Parameters_e__Union__VerifyAndReleaseTicket_e__Struct),
        ("IdentifyAndReleaseTicket", WINBIO_ASYNC_RESULT__Parameters_e__Union__IdentifyAndReleaseTicket_e__Struct),
        ("EnrollSelect", WINBIO_ASYNC_RESULT__Parameters_e__Union__EnrollSelect_e__Struct),
        ("MonitorPresence", WINBIO_ASYNC_RESULT__Parameters_e__Union__MonitorPresence_e__Struct),
        ("GetProtectionPolicy", WINBIO_ASYNC_RESULT__Parameters_e__Union__GetProtectionPolicy_e__Struct),
        ("NotifyUnitStatusChange", WINBIO_ASYNC_RESULT__Parameters_e__Union__NotifyUnitStatusChange_e__Struct),
    ]
    WINBIO_ASYNC_RESULT._fields_ = [
        ("SessionHandle", UInt32),
        ("Operation", UInt32),
        ("SequenceNumber", UInt64),
        ("TimeStamp", Int64),
        ("ApiStatus", win32more.Foundation.HRESULT),
        ("UnitId", UInt32),
        ("UserData", c_void_p),
        ("Parameters", WINBIO_ASYNC_RESULT__Parameters_e__Union),
    ]
    return WINBIO_ASYNC_RESULT
def _define_PWINBIO_ASYNC_COMPLETION_CALLBACK():
    return CFUNCTYPE(Void,POINTER(win32more.Devices.BiometricFramework.WINBIO_ASYNC_RESULT_head), use_last_error=False)
def _define_PWINBIO_VERIFY_CALLBACK():
    return CFUNCTYPE(Void,c_void_p,win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BOOLEAN,UInt32, use_last_error=False)
def _define_PWINBIO_IDENTIFY_CALLBACK():
    return CFUNCTYPE(Void,c_void_p,win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),Byte,UInt32, use_last_error=False)
def _define_PWINBIO_LOCATE_SENSOR_CALLBACK():
    return CFUNCTYPE(Void,c_void_p,win32more.Foundation.HRESULT,UInt32, use_last_error=False)
def _define_PWINBIO_ENROLL_CAPTURE_CALLBACK():
    return CFUNCTYPE(Void,c_void_p,win32more.Foundation.HRESULT,UInt32, use_last_error=False)
def _define_PWINBIO_EVENT_CALLBACK():
    return CFUNCTYPE(Void,c_void_p,win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_EVENT_head), use_last_error=False)
def _define_PWINBIO_CAPTURE_CALLBACK():
    return CFUNCTYPE(Void,c_void_p,win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.BiometricFramework.WINBIO_BIR_head),UIntPtr,UInt32, use_last_error=False)
def _define__WINIBIO_SENSOR_CONTEXT_head():
    class _WINIBIO_SENSOR_CONTEXT(Structure):
        pass
    return _WINIBIO_SENSOR_CONTEXT
def _define__WINIBIO_SENSOR_CONTEXT():
    _WINIBIO_SENSOR_CONTEXT = win32more.Devices.BiometricFramework._WINIBIO_SENSOR_CONTEXT_head
    return _WINIBIO_SENSOR_CONTEXT
def _define__WINIBIO_ENGINE_CONTEXT_head():
    class _WINIBIO_ENGINE_CONTEXT(Structure):
        pass
    return _WINIBIO_ENGINE_CONTEXT
def _define__WINIBIO_ENGINE_CONTEXT():
    _WINIBIO_ENGINE_CONTEXT = win32more.Devices.BiometricFramework._WINIBIO_ENGINE_CONTEXT_head
    return _WINIBIO_ENGINE_CONTEXT
def _define__WINIBIO_STORAGE_CONTEXT_head():
    class _WINIBIO_STORAGE_CONTEXT(Structure):
        pass
    return _WINIBIO_STORAGE_CONTEXT
def _define__WINIBIO_STORAGE_CONTEXT():
    _WINIBIO_STORAGE_CONTEXT = win32more.Devices.BiometricFramework._WINIBIO_STORAGE_CONTEXT_head
    return _WINIBIO_STORAGE_CONTEXT
def _define_WINBIO_STORAGE_RECORD_head():
    class WINBIO_STORAGE_RECORD(Structure):
        pass
    return WINBIO_STORAGE_RECORD
def _define_WINBIO_STORAGE_RECORD():
    WINBIO_STORAGE_RECORD = win32more.Devices.BiometricFramework.WINBIO_STORAGE_RECORD_head
    WINBIO_STORAGE_RECORD._fields_ = [
        ("Identity", POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head)),
        ("SubFactor", Byte),
        ("IndexVector", POINTER(UInt32)),
        ("IndexElementCount", UIntPtr),
        ("TemplateBlob", c_char_p_no),
        ("TemplateBlobSize", UIntPtr),
        ("PayloadBlob", c_char_p_no),
        ("PayloadBlobSize", UIntPtr),
    ]
    return WINBIO_STORAGE_RECORD
def _define_WINBIO_PIPELINE_head():
    class WINBIO_PIPELINE(Structure):
        pass
    return WINBIO_PIPELINE
def _define_WINBIO_PIPELINE():
    WINBIO_PIPELINE = win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head
    WINBIO_PIPELINE._fields_ = [
        ("SensorHandle", win32more.Foundation.HANDLE),
        ("EngineHandle", win32more.Foundation.HANDLE),
        ("StorageHandle", win32more.Foundation.HANDLE),
        ("SensorInterface", POINTER(win32more.Devices.BiometricFramework.WINBIO_SENSOR_INTERFACE_head)),
        ("EngineInterface", POINTER(win32more.Devices.BiometricFramework.WINBIO_ENGINE_INTERFACE_head)),
        ("StorageInterface", POINTER(win32more.Devices.BiometricFramework.WINBIO_STORAGE_INTERFACE_head)),
        ("SensorContext", POINTER(win32more.Devices.BiometricFramework._WINIBIO_SENSOR_CONTEXT_head)),
        ("EngineContext", POINTER(win32more.Devices.BiometricFramework._WINIBIO_ENGINE_CONTEXT_head)),
        ("StorageContext", POINTER(win32more.Devices.BiometricFramework._WINIBIO_STORAGE_CONTEXT_head)),
        ("FrameworkInterface", POINTER(win32more.Devices.BiometricFramework.WINBIO_FRAMEWORK_INTERFACE_head)),
    ]
    return WINBIO_PIPELINE
def _define_WINBIO_ADAPTER_INTERFACE_VERSION_head():
    class WINBIO_ADAPTER_INTERFACE_VERSION(Structure):
        pass
    return WINBIO_ADAPTER_INTERFACE_VERSION
def _define_WINBIO_ADAPTER_INTERFACE_VERSION():
    WINBIO_ADAPTER_INTERFACE_VERSION = win32more.Devices.BiometricFramework.WINBIO_ADAPTER_INTERFACE_VERSION_head
    WINBIO_ADAPTER_INTERFACE_VERSION._fields_ = [
        ("MajorVersion", UInt16),
        ("MinorVersion", UInt16),
    ]
    return WINBIO_ADAPTER_INTERFACE_VERSION
def _define_PIBIO_SENSOR_ATTACH_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_SENSOR_DETACH_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_SENSOR_CLEAR_CONTEXT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_SENSOR_QUERY_STATUS_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(UInt32), use_last_error=False)
def _define_PIBIO_SENSOR_RESET_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_SENSOR_SET_MODE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),UInt32, use_last_error=False)
def _define_PIBIO_SENSOR_SET_INDICATOR_STATUS_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),UInt32, use_last_error=False)
def _define_PIBIO_SENSOR_GET_INDICATOR_STATUS_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(UInt32), use_last_error=False)
def _define_PIBIO_SENSOR_START_CAPTURE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),Byte,POINTER(POINTER(win32more.System.IO.OVERLAPPED_head)), use_last_error=False)
def _define_PIBIO_SENSOR_FINISH_CAPTURE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(UInt32), use_last_error=False)
def _define_PIBIO_SENSOR_EXPORT_SENSOR_DATA_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(POINTER(win32more.Devices.BiometricFramework.WINBIO_BIR_head)),POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_SENSOR_CANCEL_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_SENSOR_PUSH_DATA_TO_ENGINE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),Byte,Byte,POINTER(UInt32), use_last_error=False)
def _define_PIBIO_SENSOR_CONTROL_UNIT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),UInt32,c_char_p_no,UIntPtr,c_char_p_no,UIntPtr,POINTER(UIntPtr),POINTER(UInt32), use_last_error=False)
def _define_PIBIO_SENSOR_CONTROL_UNIT_PRIVILEGED_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),UInt32,c_char_p_no,UIntPtr,c_char_p_no,UIntPtr,POINTER(UIntPtr),POINTER(UInt32), use_last_error=False)
def _define_PIBIO_SENSOR_NOTIFY_POWER_CHANGE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),UInt32, use_last_error=False)
def _define_PIBIO_SENSOR_PIPELINE_INIT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_SENSOR_PIPELINE_CLEANUP_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_SENSOR_ACTIVATE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_SENSOR_DEACTIVATE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_SENSOR_QUERY_EXTENDED_INFO_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_EXTENDED_SENSOR_INFO_head),UIntPtr, use_last_error=False)
def _define_PIBIO_SENSOR_QUERY_CALIBRATION_FORMATS_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(Guid),UIntPtr,POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_SENSOR_SET_CALIBRATION_FORMAT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(Guid), use_last_error=False)
def _define_PIBIO_SENSOR_ACCEPT_CALIBRATION_DATA_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),c_char_p_no,UIntPtr, use_last_error=False)
def _define_PIBIO_SENSOR_ASYNC_IMPORT_RAW_BUFFER_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),c_char_p_no,UIntPtr,POINTER(c_char_p_no),POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_SENSOR_ASYNC_IMPORT_SECURE_BUFFER_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),Guid,c_char_p_no,UIntPtr,POINTER(c_char_p_no),POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_SENSOR_QUERY_PRIVATE_SENSOR_TYPE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),c_char_p_no,UIntPtr,POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_SENSOR_CONNECT_SECURE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_SECURE_CONNECTION_PARAMS_head),POINTER(POINTER(win32more.Devices.BiometricFramework.WINBIO_SECURE_CONNECTION_DATA_head)), use_last_error=False)
def _define_PIBIO_SENSOR_START_CAPTURE_EX_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),Byte,c_char_p_no,UIntPtr,Byte,POINTER(POINTER(win32more.System.IO.OVERLAPPED_head)), use_last_error=False)
def _define_PIBIO_SENSOR_START_NOTIFY_WAKE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(POINTER(win32more.System.IO.OVERLAPPED_head)), use_last_error=False)
def _define_PIBIO_SENSOR_FINISH_NOTIFY_WAKE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(UInt32), use_last_error=False)
def _define_WINBIO_SENSOR_INTERFACE_head():
    class WINBIO_SENSOR_INTERFACE(Structure):
        pass
    return WINBIO_SENSOR_INTERFACE
def _define_WINBIO_SENSOR_INTERFACE():
    WINBIO_SENSOR_INTERFACE = win32more.Devices.BiometricFramework.WINBIO_SENSOR_INTERFACE_head
    WINBIO_SENSOR_INTERFACE._fields_ = [
        ("Version", win32more.Devices.BiometricFramework.WINBIO_ADAPTER_INTERFACE_VERSION),
        ("Type", UInt32),
        ("Size", UIntPtr),
        ("AdapterId", Guid),
        ("Attach", win32more.Devices.BiometricFramework.PIBIO_SENSOR_ATTACH_FN),
        ("Detach", win32more.Devices.BiometricFramework.PIBIO_SENSOR_DETACH_FN),
        ("ClearContext", win32more.Devices.BiometricFramework.PIBIO_SENSOR_CLEAR_CONTEXT_FN),
        ("QueryStatus", win32more.Devices.BiometricFramework.PIBIO_SENSOR_QUERY_STATUS_FN),
        ("Reset", win32more.Devices.BiometricFramework.PIBIO_SENSOR_RESET_FN),
        ("SetMode", win32more.Devices.BiometricFramework.PIBIO_SENSOR_SET_MODE_FN),
        ("SetIndicatorStatus", win32more.Devices.BiometricFramework.PIBIO_SENSOR_SET_INDICATOR_STATUS_FN),
        ("GetIndicatorStatus", win32more.Devices.BiometricFramework.PIBIO_SENSOR_GET_INDICATOR_STATUS_FN),
        ("StartCapture", win32more.Devices.BiometricFramework.PIBIO_SENSOR_START_CAPTURE_FN),
        ("FinishCapture", win32more.Devices.BiometricFramework.PIBIO_SENSOR_FINISH_CAPTURE_FN),
        ("ExportSensorData", win32more.Devices.BiometricFramework.PIBIO_SENSOR_EXPORT_SENSOR_DATA_FN),
        ("Cancel", win32more.Devices.BiometricFramework.PIBIO_SENSOR_CANCEL_FN),
        ("PushDataToEngine", win32more.Devices.BiometricFramework.PIBIO_SENSOR_PUSH_DATA_TO_ENGINE_FN),
        ("ControlUnit", win32more.Devices.BiometricFramework.PIBIO_SENSOR_CONTROL_UNIT_FN),
        ("ControlUnitPrivileged", win32more.Devices.BiometricFramework.PIBIO_SENSOR_CONTROL_UNIT_PRIVILEGED_FN),
        ("NotifyPowerChange", win32more.Devices.BiometricFramework.PIBIO_SENSOR_NOTIFY_POWER_CHANGE_FN),
        ("PipelineInit", win32more.Devices.BiometricFramework.PIBIO_SENSOR_PIPELINE_INIT_FN),
        ("PipelineCleanup", win32more.Devices.BiometricFramework.PIBIO_SENSOR_PIPELINE_CLEANUP_FN),
        ("Activate", win32more.Devices.BiometricFramework.PIBIO_SENSOR_ACTIVATE_FN),
        ("Deactivate", win32more.Devices.BiometricFramework.PIBIO_SENSOR_DEACTIVATE_FN),
        ("QueryExtendedInfo", win32more.Devices.BiometricFramework.PIBIO_SENSOR_QUERY_EXTENDED_INFO_FN),
        ("QueryCalibrationFormats", win32more.Devices.BiometricFramework.PIBIO_SENSOR_QUERY_CALIBRATION_FORMATS_FN),
        ("SetCalibrationFormat", win32more.Devices.BiometricFramework.PIBIO_SENSOR_SET_CALIBRATION_FORMAT_FN),
        ("AcceptCalibrationData", win32more.Devices.BiometricFramework.PIBIO_SENSOR_ACCEPT_CALIBRATION_DATA_FN),
        ("AsyncImportRawBuffer", win32more.Devices.BiometricFramework.PIBIO_SENSOR_ASYNC_IMPORT_RAW_BUFFER_FN),
        ("AsyncImportSecureBuffer", win32more.Devices.BiometricFramework.PIBIO_SENSOR_ASYNC_IMPORT_SECURE_BUFFER_FN),
        ("QueryPrivateSensorType", win32more.Devices.BiometricFramework.PIBIO_SENSOR_QUERY_PRIVATE_SENSOR_TYPE_FN),
        ("ConnectSecure", win32more.Devices.BiometricFramework.PIBIO_SENSOR_CONNECT_SECURE_FN),
        ("StartCaptureEx", win32more.Devices.BiometricFramework.PIBIO_SENSOR_START_CAPTURE_EX_FN),
        ("StartNotifyWake", win32more.Devices.BiometricFramework.PIBIO_SENSOR_START_NOTIFY_WAKE_FN),
        ("FinishNotifyWake", win32more.Devices.BiometricFramework.PIBIO_SENSOR_FINISH_NOTIFY_WAKE_FN),
    ]
    return WINBIO_SENSOR_INTERFACE
def _define_PWINBIO_QUERY_SENSOR_INTERFACE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Devices.BiometricFramework.WINBIO_SENSOR_INTERFACE_head)), use_last_error=False)
def _define_PIBIO_ENGINE_ATTACH_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_ENGINE_DETACH_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_ENGINE_CLEAR_CONTEXT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_ENGINE_QUERY_PREFERRED_FORMAT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT_head),POINTER(Guid), use_last_error=False)
def _define_PIBIO_ENGINE_QUERY_INDEX_VECTOR_SIZE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_ENGINE_QUERY_HASH_ALGORITHMS_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(UIntPtr),POINTER(UIntPtr),POINTER(c_char_p_no), use_last_error=False)
def _define_PIBIO_ENGINE_SET_HASH_ALGORITHM_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),UIntPtr,POINTER(Byte), use_last_error=False)
def _define_PIBIO_ENGINE_QUERY_SAMPLE_HINT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_ENGINE_ACCEPT_SAMPLE_DATA_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_BIR_head),UIntPtr,Byte,POINTER(UInt32), use_last_error=False)
def _define_PIBIO_ENGINE_EXPORT_ENGINE_DATA_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),Byte,POINTER(POINTER(win32more.Devices.BiometricFramework.WINBIO_BIR_head)),POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_ENGINE_VERIFY_FEATURE_SET_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),Byte,POINTER(win32more.Foundation.BOOLEAN),POINTER(c_char_p_no),POINTER(UIntPtr),POINTER(c_char_p_no),POINTER(UIntPtr),POINTER(UInt32), use_last_error=False)
def _define_PIBIO_ENGINE_IDENTIFY_FEATURE_SET_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),c_char_p_no,POINTER(c_char_p_no),POINTER(UIntPtr),POINTER(c_char_p_no),POINTER(UIntPtr),POINTER(UInt32), use_last_error=False)
def _define_PIBIO_ENGINE_CREATE_ENROLLMENT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_ENGINE_UPDATE_ENROLLMENT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(UInt32), use_last_error=False)
def _define_PIBIO_ENGINE_GET_ENROLLMENT_STATUS_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(UInt32), use_last_error=False)
def _define_PIBIO_ENGINE_GET_ENROLLMENT_HASH_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(c_char_p_no),POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_ENGINE_CHECK_FOR_DUPLICATE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),c_char_p_no,POINTER(win32more.Foundation.BOOLEAN), use_last_error=False)
def _define_PIBIO_ENGINE_COMMIT_ENROLLMENT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),Byte,c_char_p_no,UIntPtr, use_last_error=False)
def _define_PIBIO_ENGINE_DISCARD_ENROLLMENT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_ENGINE_CONTROL_UNIT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),UInt32,c_char_p_no,UIntPtr,c_char_p_no,UIntPtr,POINTER(UIntPtr),POINTER(UInt32), use_last_error=False)
def _define_PIBIO_ENGINE_CONTROL_UNIT_PRIVILEGED_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),UInt32,c_char_p_no,UIntPtr,c_char_p_no,UIntPtr,POINTER(UIntPtr),POINTER(UInt32), use_last_error=False)
def _define_PIBIO_ENGINE_NOTIFY_POWER_CHANGE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),UInt32, use_last_error=False)
def _define_PIBIO_ENGINE_RESERVED_1_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head), use_last_error=False)
def _define_PIBIO_ENGINE_PIPELINE_INIT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_ENGINE_PIPELINE_CLEANUP_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_ENGINE_ACTIVATE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_ENGINE_DEACTIVATE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_ENGINE_QUERY_EXTENDED_INFO_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_EXTENDED_ENGINE_INFO_head),UIntPtr, use_last_error=False)
def _define_PIBIO_ENGINE_IDENTIFY_ALL_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(UIntPtr),POINTER(POINTER(win32more.Devices.BiometricFramework.WINBIO_PRESENCE_head)), use_last_error=False)
def _define_PIBIO_ENGINE_SET_ENROLLMENT_SELECTOR_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),UInt64, use_last_error=False)
def _define_PIBIO_ENGINE_SET_ENROLLMENT_PARAMETERS_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_EXTENDED_ENROLLMENT_PARAMETERS_head), use_last_error=False)
def _define_PIBIO_ENGINE_QUERY_EXTENDED_ENROLLMENT_STATUS_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_EXTENDED_ENROLLMENT_STATUS_head),UIntPtr, use_last_error=False)
def _define_PIBIO_ENGINE_REFRESH_CACHE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_ENGINE_SELECT_CALIBRATION_FORMAT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(Guid),UIntPtr,POINTER(Guid),POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_ENGINE_QUERY_CALIBRATION_DATA_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Foundation.BOOLEAN),c_char_p_no,POINTER(UIntPtr),UIntPtr, use_last_error=False)
def _define_PIBIO_ENGINE_SET_ACCOUNT_POLICY_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_ACCOUNT_POLICY),UIntPtr, use_last_error=False)
def _define_PIBIO_ENGINE_CREATE_KEY_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(Byte),UIntPtr,c_char_p_no,UIntPtr,POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_ENGINE_IDENTIFY_FEATURE_SET_SECURE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(Byte),UIntPtr,POINTER(Byte),UIntPtr,POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),c_char_p_no,POINTER(UInt32),POINTER(c_char_p_no),POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_ENGINE_ACCEPT_PRIVATE_SENSOR_TYPE_INFO_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(Byte),UIntPtr, use_last_error=False)
def _define_PIBIO_ENGINE_CREATE_ENROLLMENT_AUTHENTICATED_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(c_char_p_no),POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_ENGINE_IDENTIFY_FEATURE_SET_AUTHENTICATED_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),c_char_p_no,UIntPtr,POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),c_char_p_no,POINTER(UInt32),POINTER(c_char_p_no),POINTER(UIntPtr), use_last_error=False)
def _define_WINBIO_ENGINE_INTERFACE_head():
    class WINBIO_ENGINE_INTERFACE(Structure):
        pass
    return WINBIO_ENGINE_INTERFACE
def _define_WINBIO_ENGINE_INTERFACE():
    WINBIO_ENGINE_INTERFACE = win32more.Devices.BiometricFramework.WINBIO_ENGINE_INTERFACE_head
    WINBIO_ENGINE_INTERFACE._fields_ = [
        ("Version", win32more.Devices.BiometricFramework.WINBIO_ADAPTER_INTERFACE_VERSION),
        ("Type", UInt32),
        ("Size", UIntPtr),
        ("AdapterId", Guid),
        ("Attach", win32more.Devices.BiometricFramework.PIBIO_ENGINE_ATTACH_FN),
        ("Detach", win32more.Devices.BiometricFramework.PIBIO_ENGINE_DETACH_FN),
        ("ClearContext", win32more.Devices.BiometricFramework.PIBIO_ENGINE_CLEAR_CONTEXT_FN),
        ("QueryPreferredFormat", win32more.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_PREFERRED_FORMAT_FN),
        ("QueryIndexVectorSize", win32more.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_INDEX_VECTOR_SIZE_FN),
        ("QueryHashAlgorithms", win32more.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_HASH_ALGORITHMS_FN),
        ("SetHashAlgorithm", win32more.Devices.BiometricFramework.PIBIO_ENGINE_SET_HASH_ALGORITHM_FN),
        ("QuerySampleHint", win32more.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_SAMPLE_HINT_FN),
        ("AcceptSampleData", win32more.Devices.BiometricFramework.PIBIO_ENGINE_ACCEPT_SAMPLE_DATA_FN),
        ("ExportEngineData", win32more.Devices.BiometricFramework.PIBIO_ENGINE_EXPORT_ENGINE_DATA_FN),
        ("VerifyFeatureSet", win32more.Devices.BiometricFramework.PIBIO_ENGINE_VERIFY_FEATURE_SET_FN),
        ("IdentifyFeatureSet", win32more.Devices.BiometricFramework.PIBIO_ENGINE_IDENTIFY_FEATURE_SET_FN),
        ("CreateEnrollment", win32more.Devices.BiometricFramework.PIBIO_ENGINE_CREATE_ENROLLMENT_FN),
        ("UpdateEnrollment", win32more.Devices.BiometricFramework.PIBIO_ENGINE_UPDATE_ENROLLMENT_FN),
        ("GetEnrollmentStatus", win32more.Devices.BiometricFramework.PIBIO_ENGINE_GET_ENROLLMENT_STATUS_FN),
        ("GetEnrollmentHash", win32more.Devices.BiometricFramework.PIBIO_ENGINE_GET_ENROLLMENT_HASH_FN),
        ("CheckForDuplicate", win32more.Devices.BiometricFramework.PIBIO_ENGINE_CHECK_FOR_DUPLICATE_FN),
        ("CommitEnrollment", win32more.Devices.BiometricFramework.PIBIO_ENGINE_COMMIT_ENROLLMENT_FN),
        ("DiscardEnrollment", win32more.Devices.BiometricFramework.PIBIO_ENGINE_DISCARD_ENROLLMENT_FN),
        ("ControlUnit", win32more.Devices.BiometricFramework.PIBIO_ENGINE_CONTROL_UNIT_FN),
        ("ControlUnitPrivileged", win32more.Devices.BiometricFramework.PIBIO_ENGINE_CONTROL_UNIT_PRIVILEGED_FN),
        ("NotifyPowerChange", win32more.Devices.BiometricFramework.PIBIO_ENGINE_NOTIFY_POWER_CHANGE_FN),
        ("Reserved_1", win32more.Devices.BiometricFramework.PIBIO_ENGINE_RESERVED_1_FN),
        ("PipelineInit", win32more.Devices.BiometricFramework.PIBIO_ENGINE_PIPELINE_INIT_FN),
        ("PipelineCleanup", win32more.Devices.BiometricFramework.PIBIO_ENGINE_PIPELINE_CLEANUP_FN),
        ("Activate", win32more.Devices.BiometricFramework.PIBIO_ENGINE_ACTIVATE_FN),
        ("Deactivate", win32more.Devices.BiometricFramework.PIBIO_ENGINE_DEACTIVATE_FN),
        ("QueryExtendedInfo", win32more.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_EXTENDED_INFO_FN),
        ("IdentifyAll", win32more.Devices.BiometricFramework.PIBIO_ENGINE_IDENTIFY_ALL_FN),
        ("SetEnrollmentSelector", win32more.Devices.BiometricFramework.PIBIO_ENGINE_SET_ENROLLMENT_SELECTOR_FN),
        ("SetEnrollmentParameters", win32more.Devices.BiometricFramework.PIBIO_ENGINE_SET_ENROLLMENT_PARAMETERS_FN),
        ("QueryExtendedEnrollmentStatus", win32more.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_EXTENDED_ENROLLMENT_STATUS_FN),
        ("RefreshCache", win32more.Devices.BiometricFramework.PIBIO_ENGINE_REFRESH_CACHE_FN),
        ("SelectCalibrationFormat", win32more.Devices.BiometricFramework.PIBIO_ENGINE_SELECT_CALIBRATION_FORMAT_FN),
        ("QueryCalibrationData", win32more.Devices.BiometricFramework.PIBIO_ENGINE_QUERY_CALIBRATION_DATA_FN),
        ("SetAccountPolicy", win32more.Devices.BiometricFramework.PIBIO_ENGINE_SET_ACCOUNT_POLICY_FN),
        ("CreateKey", win32more.Devices.BiometricFramework.PIBIO_ENGINE_CREATE_KEY_FN),
        ("IdentifyFeatureSetSecure", win32more.Devices.BiometricFramework.PIBIO_ENGINE_IDENTIFY_FEATURE_SET_SECURE_FN),
        ("AcceptPrivateSensorTypeInfo", win32more.Devices.BiometricFramework.PIBIO_ENGINE_ACCEPT_PRIVATE_SENSOR_TYPE_INFO_FN),
        ("CreateEnrollmentAuthenticated", win32more.Devices.BiometricFramework.PIBIO_ENGINE_CREATE_ENROLLMENT_AUTHENTICATED_FN),
        ("IdentifyFeatureSetAuthenticated", win32more.Devices.BiometricFramework.PIBIO_ENGINE_IDENTIFY_FEATURE_SET_AUTHENTICATED_FN),
    ]
    return WINBIO_ENGINE_INTERFACE
def _define_PWINBIO_QUERY_ENGINE_INTERFACE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Devices.BiometricFramework.WINBIO_ENGINE_INTERFACE_head)), use_last_error=False)
def _define_PIBIO_STORAGE_ATTACH_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_STORAGE_DETACH_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_STORAGE_CLEAR_CONTEXT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_STORAGE_CREATE_DATABASE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(Guid),UInt32,POINTER(Guid),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UIntPtr,UIntPtr, use_last_error=False)
def _define_PIBIO_STORAGE_ERASE_DATABASE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(Guid),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)
def _define_PIBIO_STORAGE_OPEN_DATABASE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(Guid),win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)
def _define_PIBIO_STORAGE_CLOSE_DATABASE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_STORAGE_GET_DATA_FORMAT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(Guid),POINTER(win32more.Devices.BiometricFramework.WINBIO_VERSION_head), use_last_error=False)
def _define_PIBIO_STORAGE_GET_DATABASE_SIZE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(UIntPtr),POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_STORAGE_ADD_RECORD_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_STORAGE_RECORD_head), use_last_error=False)
def _define_PIBIO_STORAGE_DELETE_RECORD_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),Byte, use_last_error=False)
def _define_PIBIO_STORAGE_QUERY_BY_SUBJECT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),Byte, use_last_error=False)
def _define_PIBIO_STORAGE_QUERY_BY_CONTENT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),Byte,POINTER(UInt32),UIntPtr, use_last_error=False)
def _define_PIBIO_STORAGE_GET_RECORD_COUNT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_STORAGE_FIRST_RECORD_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_STORAGE_NEXT_RECORD_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_STORAGE_GET_CURRENT_RECORD_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_STORAGE_RECORD_head), use_last_error=False)
def _define_PIBIO_STORAGE_CONTROL_UNIT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),UInt32,c_char_p_no,UIntPtr,c_char_p_no,UIntPtr,POINTER(UIntPtr),POINTER(UInt32), use_last_error=False)
def _define_PIBIO_STORAGE_CONTROL_UNIT_PRIVILEGED_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),UInt32,c_char_p_no,UIntPtr,c_char_p_no,UIntPtr,POINTER(UIntPtr),POINTER(UInt32), use_last_error=False)
def _define_PIBIO_STORAGE_NOTIFY_POWER_CHANGE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),UInt32, use_last_error=False)
def _define_PIBIO_STORAGE_PIPELINE_INIT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_STORAGE_PIPELINE_CLEANUP_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_STORAGE_ACTIVATE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_STORAGE_DEACTIVATE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_STORAGE_QUERY_EXTENDED_INFO_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_EXTENDED_STORAGE_INFO_head),UIntPtr, use_last_error=False)
def _define_PIBIO_STORAGE_NOTIFY_DATABASE_CHANGE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),win32more.Foundation.BOOLEAN, use_last_error=False)
def _define_PIBIO_STORAGE_RESERVED_1_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),POINTER(UInt64),POINTER(UInt64), use_last_error=False)
def _define_PIBIO_STORAGE_RESERVED_2_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head), use_last_error=False)
def _define_PIBIO_STORAGE_UPDATE_RECORD_BEGIN_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),Byte,POINTER(win32more.Devices.BiometricFramework.WINBIO_STORAGE_RECORD_head), use_last_error=False)
def _define_PIBIO_STORAGE_UPDATE_RECORD_COMMIT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_STORAGE_RECORD_head), use_last_error=False)
def _define_WINBIO_STORAGE_INTERFACE_head():
    class WINBIO_STORAGE_INTERFACE(Structure):
        pass
    return WINBIO_STORAGE_INTERFACE
def _define_WINBIO_STORAGE_INTERFACE():
    WINBIO_STORAGE_INTERFACE = win32more.Devices.BiometricFramework.WINBIO_STORAGE_INTERFACE_head
    WINBIO_STORAGE_INTERFACE._fields_ = [
        ("Version", win32more.Devices.BiometricFramework.WINBIO_ADAPTER_INTERFACE_VERSION),
        ("Type", UInt32),
        ("Size", UIntPtr),
        ("AdapterId", Guid),
        ("Attach", win32more.Devices.BiometricFramework.PIBIO_STORAGE_ATTACH_FN),
        ("Detach", win32more.Devices.BiometricFramework.PIBIO_STORAGE_DETACH_FN),
        ("ClearContext", win32more.Devices.BiometricFramework.PIBIO_STORAGE_CLEAR_CONTEXT_FN),
        ("CreateDatabase", win32more.Devices.BiometricFramework.PIBIO_STORAGE_CREATE_DATABASE_FN),
        ("EraseDatabase", win32more.Devices.BiometricFramework.PIBIO_STORAGE_ERASE_DATABASE_FN),
        ("OpenDatabase", win32more.Devices.BiometricFramework.PIBIO_STORAGE_OPEN_DATABASE_FN),
        ("CloseDatabase", win32more.Devices.BiometricFramework.PIBIO_STORAGE_CLOSE_DATABASE_FN),
        ("GetDataFormat", win32more.Devices.BiometricFramework.PIBIO_STORAGE_GET_DATA_FORMAT_FN),
        ("GetDatabaseSize", win32more.Devices.BiometricFramework.PIBIO_STORAGE_GET_DATABASE_SIZE_FN),
        ("AddRecord", win32more.Devices.BiometricFramework.PIBIO_STORAGE_ADD_RECORD_FN),
        ("DeleteRecord", win32more.Devices.BiometricFramework.PIBIO_STORAGE_DELETE_RECORD_FN),
        ("QueryBySubject", win32more.Devices.BiometricFramework.PIBIO_STORAGE_QUERY_BY_SUBJECT_FN),
        ("QueryByContent", win32more.Devices.BiometricFramework.PIBIO_STORAGE_QUERY_BY_CONTENT_FN),
        ("GetRecordCount", win32more.Devices.BiometricFramework.PIBIO_STORAGE_GET_RECORD_COUNT_FN),
        ("FirstRecord", win32more.Devices.BiometricFramework.PIBIO_STORAGE_FIRST_RECORD_FN),
        ("NextRecord", win32more.Devices.BiometricFramework.PIBIO_STORAGE_NEXT_RECORD_FN),
        ("GetCurrentRecord", win32more.Devices.BiometricFramework.PIBIO_STORAGE_GET_CURRENT_RECORD_FN),
        ("ControlUnit", win32more.Devices.BiometricFramework.PIBIO_STORAGE_CONTROL_UNIT_FN),
        ("ControlUnitPrivileged", win32more.Devices.BiometricFramework.PIBIO_STORAGE_CONTROL_UNIT_PRIVILEGED_FN),
        ("NotifyPowerChange", win32more.Devices.BiometricFramework.PIBIO_STORAGE_NOTIFY_POWER_CHANGE_FN),
        ("PipelineInit", win32more.Devices.BiometricFramework.PIBIO_STORAGE_PIPELINE_INIT_FN),
        ("PipelineCleanup", win32more.Devices.BiometricFramework.PIBIO_STORAGE_PIPELINE_CLEANUP_FN),
        ("Activate", win32more.Devices.BiometricFramework.PIBIO_STORAGE_ACTIVATE_FN),
        ("Deactivate", win32more.Devices.BiometricFramework.PIBIO_STORAGE_DEACTIVATE_FN),
        ("QueryExtendedInfo", win32more.Devices.BiometricFramework.PIBIO_STORAGE_QUERY_EXTENDED_INFO_FN),
        ("NotifyDatabaseChange", win32more.Devices.BiometricFramework.PIBIO_STORAGE_NOTIFY_DATABASE_CHANGE_FN),
        ("Reserved1", win32more.Devices.BiometricFramework.PIBIO_STORAGE_RESERVED_1_FN),
        ("Reserved2", win32more.Devices.BiometricFramework.PIBIO_STORAGE_RESERVED_2_FN),
        ("UpdateRecordBegin", win32more.Devices.BiometricFramework.PIBIO_STORAGE_UPDATE_RECORD_BEGIN_FN),
        ("UpdateRecordCommit", win32more.Devices.BiometricFramework.PIBIO_STORAGE_UPDATE_RECORD_COMMIT_FN),
    ]
    return WINBIO_STORAGE_INTERFACE
def _define_PWINBIO_QUERY_STORAGE_INTERFACE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Devices.BiometricFramework.WINBIO_STORAGE_INTERFACE_head)), use_last_error=False)
def _define_PIBIO_FRAMEWORK_SET_UNIT_STATUS_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_EXTENDED_UNIT_STATUS_head),UIntPtr, use_last_error=False)
def _define_PIBIO_FRAMEWORK_VSM_CACHE_CLEAR_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_BEGIN_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),UIntPtr,POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_NEXT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),c_char_p_no,UIntPtr, use_last_error=False)
def _define_PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_END_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_BEGIN_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(UIntPtr),POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_NEXT_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),c_char_p_no,UIntPtr,POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_END_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_1_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),UIntPtr,POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_2_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),c_char_p_no,UIntPtr, use_last_error=False)
def _define_PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_3_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head), use_last_error=False)
def _define_PIBIO_FRAMEWORK_ALLOCATE_MEMORY_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),UIntPtr,POINTER(c_void_p), use_last_error=False)
def _define_PIBIO_FRAMEWORK_FREE_MEMORY_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),c_void_p, use_last_error=False)
def _define_PIBIO_FRAMEWORK_GET_PROPERTY_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),UInt32,UInt32,POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),Byte,POINTER(c_void_p),POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_FRAMEWORK_LOCK_AND_VALIDATE_SECURE_BUFFER_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),Guid,POINTER(c_void_p),POINTER(UIntPtr), use_last_error=False)
def _define_PIBIO_FRAMEWORK_RELEASE_SECURE_BUFFER_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),Guid, use_last_error=False)
def _define_PIBIO_FRAMEWORK_VSM_QUERY_AUTHORIZED_ENROLLMENTS_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),POINTER(UIntPtr),POINTER(POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head)), use_last_error=False)
def _define_PIBIO_FRAMEWORK_VSM_DECRYPT_SAMPLE_FN():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_PIPELINE_head),c_char_p_no,UIntPtr,c_char_p_no,UIntPtr,c_char_p_no,UIntPtr, use_last_error=False)
def _define_WINBIO_FRAMEWORK_INTERFACE_head():
    class WINBIO_FRAMEWORK_INTERFACE(Structure):
        pass
    return WINBIO_FRAMEWORK_INTERFACE
def _define_WINBIO_FRAMEWORK_INTERFACE():
    WINBIO_FRAMEWORK_INTERFACE = win32more.Devices.BiometricFramework.WINBIO_FRAMEWORK_INTERFACE_head
    WINBIO_FRAMEWORK_INTERFACE._fields_ = [
        ("Version", win32more.Devices.BiometricFramework.WINBIO_ADAPTER_INTERFACE_VERSION),
        ("Type", UInt32),
        ("Size", UIntPtr),
        ("AdapterId", Guid),
        ("SetUnitStatus", win32more.Devices.BiometricFramework.PIBIO_FRAMEWORK_SET_UNIT_STATUS_FN),
        ("VsmStorageAttach", win32more.Devices.BiometricFramework.PIBIO_STORAGE_ATTACH_FN),
        ("VsmStorageDetach", win32more.Devices.BiometricFramework.PIBIO_STORAGE_DETACH_FN),
        ("VsmStorageClearContext", win32more.Devices.BiometricFramework.PIBIO_STORAGE_CLEAR_CONTEXT_FN),
        ("VsmStorageCreateDatabase", win32more.Devices.BiometricFramework.PIBIO_STORAGE_CREATE_DATABASE_FN),
        ("VsmStorageOpenDatabase", win32more.Devices.BiometricFramework.PIBIO_STORAGE_OPEN_DATABASE_FN),
        ("VsmStorageCloseDatabase", win32more.Devices.BiometricFramework.PIBIO_STORAGE_CLOSE_DATABASE_FN),
        ("VsmStorageDeleteRecord", win32more.Devices.BiometricFramework.PIBIO_STORAGE_DELETE_RECORD_FN),
        ("VsmStorageNotifyPowerChange", win32more.Devices.BiometricFramework.PIBIO_STORAGE_NOTIFY_POWER_CHANGE_FN),
        ("VsmStoragePipelineInit", win32more.Devices.BiometricFramework.PIBIO_STORAGE_PIPELINE_INIT_FN),
        ("VsmStoragePipelineCleanup", win32more.Devices.BiometricFramework.PIBIO_STORAGE_PIPELINE_CLEANUP_FN),
        ("VsmStorageActivate", win32more.Devices.BiometricFramework.PIBIO_STORAGE_ACTIVATE_FN),
        ("VsmStorageDeactivate", win32more.Devices.BiometricFramework.PIBIO_STORAGE_DEACTIVATE_FN),
        ("VsmStorageQueryExtendedInfo", win32more.Devices.BiometricFramework.PIBIO_STORAGE_QUERY_EXTENDED_INFO_FN),
        ("VsmStorageCacheClear", win32more.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_CLEAR_FN),
        ("VsmStorageCacheImportBegin", win32more.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_BEGIN_FN),
        ("VsmStorageCacheImportNext", win32more.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_NEXT_FN),
        ("VsmStorageCacheImportEnd", win32more.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_END_FN),
        ("VsmStorageCacheExportBegin", win32more.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_BEGIN_FN),
        ("VsmStorageCacheExportNext", win32more.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_NEXT_FN),
        ("VsmStorageCacheExportEnd", win32more.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_END_FN),
        ("VsmSensorAttach", win32more.Devices.BiometricFramework.PIBIO_SENSOR_ATTACH_FN),
        ("VsmSensorDetach", win32more.Devices.BiometricFramework.PIBIO_SENSOR_DETACH_FN),
        ("VsmSensorClearContext", win32more.Devices.BiometricFramework.PIBIO_SENSOR_CLEAR_CONTEXT_FN),
        ("VsmSensorPushDataToEngine", win32more.Devices.BiometricFramework.PIBIO_SENSOR_PUSH_DATA_TO_ENGINE_FN),
        ("VsmSensorNotifyPowerChange", win32more.Devices.BiometricFramework.PIBIO_SENSOR_NOTIFY_POWER_CHANGE_FN),
        ("VsmSensorPipelineInit", win32more.Devices.BiometricFramework.PIBIO_SENSOR_PIPELINE_INIT_FN),
        ("VsmSensorPipelineCleanup", win32more.Devices.BiometricFramework.PIBIO_SENSOR_PIPELINE_CLEANUP_FN),
        ("VsmSensorActivate", win32more.Devices.BiometricFramework.PIBIO_SENSOR_ACTIVATE_FN),
        ("VsmSensorDeactivate", win32more.Devices.BiometricFramework.PIBIO_SENSOR_DEACTIVATE_FN),
        ("VsmSensorAsyncImportRawBuffer", win32more.Devices.BiometricFramework.PIBIO_SENSOR_ASYNC_IMPORT_RAW_BUFFER_FN),
        ("VsmSensorAsyncImportSecureBuffer", win32more.Devices.BiometricFramework.PIBIO_SENSOR_ASYNC_IMPORT_SECURE_BUFFER_FN),
        ("Reserved1", win32more.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_1_FN),
        ("Reserved2", win32more.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_2_FN),
        ("Reserved3", win32more.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_3_FN),
        ("Reserved4", win32more.Devices.BiometricFramework.PIBIO_STORAGE_RESERVED_1_FN),
        ("Reserved5", win32more.Devices.BiometricFramework.PIBIO_STORAGE_RESERVED_2_FN),
        ("AllocateMemory", win32more.Devices.BiometricFramework.PIBIO_FRAMEWORK_ALLOCATE_MEMORY_FN),
        ("FreeMemory", win32more.Devices.BiometricFramework.PIBIO_FRAMEWORK_FREE_MEMORY_FN),
        ("GetProperty", win32more.Devices.BiometricFramework.PIBIO_FRAMEWORK_GET_PROPERTY_FN),
        ("LockAndValidateSecureBuffer", win32more.Devices.BiometricFramework.PIBIO_FRAMEWORK_LOCK_AND_VALIDATE_SECURE_BUFFER_FN),
        ("ReleaseSecureBuffer", win32more.Devices.BiometricFramework.PIBIO_FRAMEWORK_RELEASE_SECURE_BUFFER_FN),
        ("QueryAuthorizedEnrollments", win32more.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_QUERY_AUTHORIZED_ENROLLMENTS_FN),
        ("DecryptSample", win32more.Devices.BiometricFramework.PIBIO_FRAMEWORK_VSM_DECRYPT_SAMPLE_FN),
    ]
    return WINBIO_FRAMEWORK_INTERFACE
def _define_WINBIO_SENSOR_ATTRIBUTES_head():
    class WINBIO_SENSOR_ATTRIBUTES(Structure):
        pass
    return WINBIO_SENSOR_ATTRIBUTES
def _define_WINBIO_SENSOR_ATTRIBUTES():
    WINBIO_SENSOR_ATTRIBUTES = win32more.Devices.BiometricFramework.WINBIO_SENSOR_ATTRIBUTES_head
    WINBIO_SENSOR_ATTRIBUTES._fields_ = [
        ("PayloadSize", UInt32),
        ("WinBioHresult", win32more.Foundation.HRESULT),
        ("WinBioVersion", win32more.Devices.BiometricFramework.WINBIO_VERSION),
        ("SensorType", UInt32),
        ("SensorSubType", UInt32),
        ("Capabilities", UInt32),
        ("ManufacturerName", UInt16 * 256),
        ("ModelName", UInt16 * 256),
        ("SerialNumber", UInt16 * 256),
        ("FirmwareVersion", win32more.Devices.BiometricFramework.WINBIO_VERSION),
        ("SupportedFormatEntries", UInt32),
        ("SupportedFormat", win32more.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT * 0),
    ]
    return WINBIO_SENSOR_ATTRIBUTES
def _define_WINBIO_DATA_head():
    class WINBIO_DATA(Structure):
        pass
    return WINBIO_DATA
def _define_WINBIO_DATA():
    WINBIO_DATA = win32more.Devices.BiometricFramework.WINBIO_DATA_head
    WINBIO_DATA._fields_ = [
        ("Size", UInt32),
        ("Data", Byte * 0),
    ]
    return WINBIO_DATA
def _define_WINBIO_UPDATE_FIRMWARE_head():
    class WINBIO_UPDATE_FIRMWARE(Structure):
        pass
    return WINBIO_UPDATE_FIRMWARE
def _define_WINBIO_UPDATE_FIRMWARE():
    WINBIO_UPDATE_FIRMWARE = win32more.Devices.BiometricFramework.WINBIO_UPDATE_FIRMWARE_head
    WINBIO_UPDATE_FIRMWARE._fields_ = [
        ("PayloadSize", UInt32),
        ("FirmwareData", win32more.Devices.BiometricFramework.WINBIO_DATA),
    ]
    return WINBIO_UPDATE_FIRMWARE
def _define_WINBIO_CALIBRATION_INFO_head():
    class WINBIO_CALIBRATION_INFO(Structure):
        pass
    return WINBIO_CALIBRATION_INFO
def _define_WINBIO_CALIBRATION_INFO():
    WINBIO_CALIBRATION_INFO = win32more.Devices.BiometricFramework.WINBIO_CALIBRATION_INFO_head
    WINBIO_CALIBRATION_INFO._fields_ = [
        ("PayloadSize", UInt32),
        ("WinBioHresult", win32more.Foundation.HRESULT),
        ("CalibrationData", win32more.Devices.BiometricFramework.WINBIO_DATA),
    ]
    return WINBIO_CALIBRATION_INFO
def _define_WINBIO_DIAGNOSTICS_head():
    class WINBIO_DIAGNOSTICS(Structure):
        pass
    return WINBIO_DIAGNOSTICS
def _define_WINBIO_DIAGNOSTICS():
    WINBIO_DIAGNOSTICS = win32more.Devices.BiometricFramework.WINBIO_DIAGNOSTICS_head
    WINBIO_DIAGNOSTICS._fields_ = [
        ("PayloadSize", UInt32),
        ("WinBioHresult", win32more.Foundation.HRESULT),
        ("SensorStatus", UInt32),
        ("VendorDiagnostics", win32more.Devices.BiometricFramework.WINBIO_DATA),
    ]
    return WINBIO_DIAGNOSTICS
def _define_WINBIO_BLANK_PAYLOAD_head():
    class WINBIO_BLANK_PAYLOAD(Structure):
        pass
    return WINBIO_BLANK_PAYLOAD
def _define_WINBIO_BLANK_PAYLOAD():
    WINBIO_BLANK_PAYLOAD = win32more.Devices.BiometricFramework.WINBIO_BLANK_PAYLOAD_head
    WINBIO_BLANK_PAYLOAD._fields_ = [
        ("PayloadSize", UInt32),
        ("WinBioHresult", win32more.Foundation.HRESULT),
    ]
    return WINBIO_BLANK_PAYLOAD
def _define_WINBIO_CAPTURE_PARAMETERS_head():
    class WINBIO_CAPTURE_PARAMETERS(Structure):
        pass
    return WINBIO_CAPTURE_PARAMETERS
def _define_WINBIO_CAPTURE_PARAMETERS():
    WINBIO_CAPTURE_PARAMETERS = win32more.Devices.BiometricFramework.WINBIO_CAPTURE_PARAMETERS_head
    WINBIO_CAPTURE_PARAMETERS._fields_ = [
        ("PayloadSize", UInt32),
        ("Purpose", Byte),
        ("Format", win32more.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT),
        ("VendorFormat", Guid),
        ("Flags", Byte),
    ]
    return WINBIO_CAPTURE_PARAMETERS
def _define_WINBIO_CAPTURE_DATA_head():
    class WINBIO_CAPTURE_DATA(Structure):
        pass
    return WINBIO_CAPTURE_DATA
def _define_WINBIO_CAPTURE_DATA():
    WINBIO_CAPTURE_DATA = win32more.Devices.BiometricFramework.WINBIO_CAPTURE_DATA_head
    WINBIO_CAPTURE_DATA._fields_ = [
        ("PayloadSize", UInt32),
        ("WinBioHresult", win32more.Foundation.HRESULT),
        ("SensorStatus", UInt32),
        ("RejectDetail", UInt32),
        ("CaptureData", win32more.Devices.BiometricFramework.WINBIO_DATA),
    ]
    return WINBIO_CAPTURE_DATA
def _define_WINBIO_SUPPORTED_ALGORITHMS_head():
    class WINBIO_SUPPORTED_ALGORITHMS(Structure):
        pass
    return WINBIO_SUPPORTED_ALGORITHMS
def _define_WINBIO_SUPPORTED_ALGORITHMS():
    WINBIO_SUPPORTED_ALGORITHMS = win32more.Devices.BiometricFramework.WINBIO_SUPPORTED_ALGORITHMS_head
    WINBIO_SUPPORTED_ALGORITHMS._fields_ = [
        ("PayloadSize", UInt32),
        ("WinBioHresult", win32more.Foundation.HRESULT),
        ("NumberOfAlgorithms", UInt32),
        ("AlgorithmData", win32more.Devices.BiometricFramework.WINBIO_DATA),
    ]
    return WINBIO_SUPPORTED_ALGORITHMS
def _define_WINBIO_GET_INDICATOR_head():
    class WINBIO_GET_INDICATOR(Structure):
        pass
    return WINBIO_GET_INDICATOR
def _define_WINBIO_GET_INDICATOR():
    WINBIO_GET_INDICATOR = win32more.Devices.BiometricFramework.WINBIO_GET_INDICATOR_head
    WINBIO_GET_INDICATOR._fields_ = [
        ("PayloadSize", UInt32),
        ("WinBioHresult", win32more.Foundation.HRESULT),
        ("IndicatorStatus", UInt32),
    ]
    return WINBIO_GET_INDICATOR
def _define_WINBIO_SET_INDICATOR_head():
    class WINBIO_SET_INDICATOR(Structure):
        pass
    return WINBIO_SET_INDICATOR
def _define_WINBIO_SET_INDICATOR():
    WINBIO_SET_INDICATOR = win32more.Devices.BiometricFramework.WINBIO_SET_INDICATOR_head
    WINBIO_SET_INDICATOR._fields_ = [
        ("PayloadSize", UInt32),
        ("IndicatorStatus", UInt32),
    ]
    return WINBIO_SET_INDICATOR
def _define_WINBIO_PRIVATE_SENSOR_TYPE_INFO_head():
    class WINBIO_PRIVATE_SENSOR_TYPE_INFO(Structure):
        pass
    return WINBIO_PRIVATE_SENSOR_TYPE_INFO
def _define_WINBIO_PRIVATE_SENSOR_TYPE_INFO():
    WINBIO_PRIVATE_SENSOR_TYPE_INFO = win32more.Devices.BiometricFramework.WINBIO_PRIVATE_SENSOR_TYPE_INFO_head
    WINBIO_PRIVATE_SENSOR_TYPE_INFO._fields_ = [
        ("PayloadSize", UInt32),
        ("WinBioHresult", win32more.Foundation.HRESULT),
        ("PrivateSensorTypeInfo", win32more.Devices.BiometricFramework.WINBIO_DATA),
    ]
    return WINBIO_PRIVATE_SENSOR_TYPE_INFO
def _define_WINBIO_ENCRYPTED_CAPTURE_PARAMS_head():
    class WINBIO_ENCRYPTED_CAPTURE_PARAMS(Structure):
        pass
    return WINBIO_ENCRYPTED_CAPTURE_PARAMS
def _define_WINBIO_ENCRYPTED_CAPTURE_PARAMS():
    WINBIO_ENCRYPTED_CAPTURE_PARAMS = win32more.Devices.BiometricFramework.WINBIO_ENCRYPTED_CAPTURE_PARAMS_head
    WINBIO_ENCRYPTED_CAPTURE_PARAMS._fields_ = [
        ("PayloadSize", UInt32),
        ("Purpose", Byte),
        ("Format", win32more.Devices.BiometricFramework.WINBIO_REGISTERED_FORMAT),
        ("VendorFormat", Guid),
        ("Flags", Byte),
        ("NonceSize", UInt32),
    ]
    return WINBIO_ENCRYPTED_CAPTURE_PARAMS
def _define_WINBIO_NOTIFY_WAKE_head():
    class WINBIO_NOTIFY_WAKE(Structure):
        pass
    return WINBIO_NOTIFY_WAKE
def _define_WINBIO_NOTIFY_WAKE():
    WINBIO_NOTIFY_WAKE = win32more.Devices.BiometricFramework.WINBIO_NOTIFY_WAKE_head
    WINBIO_NOTIFY_WAKE._fields_ = [
        ("PayloadSize", UInt32),
        ("WinBioHresult", win32more.Foundation.HRESULT),
        ("Reason", UInt32),
    ]
    return WINBIO_NOTIFY_WAKE
def _define_WinBioEnumServiceProviders():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.Devices.BiometricFramework.WINBIO_BSP_SCHEMA_head)),POINTER(UIntPtr), use_last_error=False)(("WinBioEnumServiceProviders", windll["winbio"]), ((1, 'Factor'),(1, 'BspSchemaArray'),(1, 'BspCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioEnumBiometricUnits():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.Devices.BiometricFramework.WINBIO_UNIT_SCHEMA_head)),POINTER(UIntPtr), use_last_error=False)(("WinBioEnumBiometricUnits", windll["winbio"]), ((1, 'Factor'),(1, 'UnitSchemaArray'),(1, 'UnitCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioEnumDatabases():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.Devices.BiometricFramework.WINBIO_STORAGE_SCHEMA_head)),POINTER(UIntPtr), use_last_error=False)(("WinBioEnumDatabases", windll["winbio"]), ((1, 'Factor'),(1, 'StorageSchemaArray'),(1, 'StorageCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioAsyncOpenFramework():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.BiometricFramework.WINBIO_ASYNC_NOTIFICATION_METHOD,win32more.Foundation.HWND,UInt32,win32more.Devices.BiometricFramework.PWINBIO_ASYNC_COMPLETION_CALLBACK,c_void_p,win32more.Foundation.BOOL,POINTER(UInt32), use_last_error=False)(("WinBioAsyncOpenFramework", windll["winbio"]), ((1, 'NotificationMethod'),(1, 'TargetWindow'),(1, 'MessageCode'),(1, 'CallbackRoutine'),(1, 'UserData'),(1, 'AsynchronousOpen'),(1, 'FrameworkHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioCloseFramework():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("WinBioCloseFramework", windll["winbio"]), ((1, 'FrameworkHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioAsyncEnumServiceProviders():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(("WinBioAsyncEnumServiceProviders", windll["winbio"]), ((1, 'FrameworkHandle'),(1, 'Factor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioAsyncEnumBiometricUnits():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(("WinBioAsyncEnumBiometricUnits", windll["winbio"]), ((1, 'FrameworkHandle'),(1, 'Factor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioAsyncEnumDatabases():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(("WinBioAsyncEnumDatabases", windll["winbio"]), ((1, 'FrameworkHandle'),(1, 'Factor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioAsyncMonitorFrameworkChanges():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(("WinBioAsyncMonitorFrameworkChanges", windll["winbio"]), ((1, 'FrameworkHandle'),(1, 'ChangeTypes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioOpenSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Devices.BiometricFramework.WINBIO_POOL,UInt32,POINTER(UInt32),UIntPtr,POINTER(Guid),POINTER(UInt32), use_last_error=False)(("WinBioOpenSession", windll["winbio"]), ((1, 'Factor'),(1, 'PoolType'),(1, 'Flags'),(1, 'UnitArray'),(1, 'UnitCount'),(1, 'DatabaseId'),(1, 'SessionHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioAsyncOpenSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Devices.BiometricFramework.WINBIO_POOL,UInt32,POINTER(UInt32),UIntPtr,POINTER(Guid),win32more.Devices.BiometricFramework.WINBIO_ASYNC_NOTIFICATION_METHOD,win32more.Foundation.HWND,UInt32,win32more.Devices.BiometricFramework.PWINBIO_ASYNC_COMPLETION_CALLBACK,c_void_p,win32more.Foundation.BOOL,POINTER(UInt32), use_last_error=False)(("WinBioAsyncOpenSession", windll["winbio"]), ((1, 'Factor'),(1, 'PoolType'),(1, 'Flags'),(1, 'UnitArray'),(1, 'UnitCount'),(1, 'DatabaseId'),(1, 'NotificationMethod'),(1, 'TargetWindow'),(1, 'MessageCode'),(1, 'CallbackRoutine'),(1, 'UserData'),(1, 'AsynchronousOpen'),(1, 'SessionHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioCloseSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("WinBioCloseSession", windll["winbio"]), ((1, 'SessionHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioVerify():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),Byte,POINTER(UInt32),c_char_p_no,POINTER(UInt32), use_last_error=False)(("WinBioVerify", windll["winbio"]), ((1, 'SessionHandle'),(1, 'Identity'),(1, 'SubFactor'),(1, 'UnitId'),(1, 'Match'),(1, 'RejectDetail'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioVerifyWithCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),Byte,win32more.Devices.BiometricFramework.PWINBIO_VERIFY_CALLBACK,c_void_p, use_last_error=False)(("WinBioVerifyWithCallback", windll["winbio"]), ((1, 'SessionHandle'),(1, 'Identity'),(1, 'SubFactor'),(1, 'VerifyCallback'),(1, 'VerifyCallbackContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioIdentify():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),c_char_p_no,POINTER(UInt32), use_last_error=False)(("WinBioIdentify", windll["winbio"]), ((1, 'SessionHandle'),(1, 'UnitId'),(1, 'Identity'),(1, 'SubFactor'),(1, 'RejectDetail'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioIdentifyWithCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Devices.BiometricFramework.PWINBIO_IDENTIFY_CALLBACK,c_void_p, use_last_error=False)(("WinBioIdentifyWithCallback", windll["winbio"]), ((1, 'SessionHandle'),(1, 'IdentifyCallback'),(1, 'IdentifyCallbackContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioWait():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("WinBioWait", windll["winbio"]), ((1, 'SessionHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioCancel():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("WinBioCancel", windll["winbio"]), ((1, 'SessionHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioLocateSensor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(("WinBioLocateSensor", windll["winbio"]), ((1, 'SessionHandle'),(1, 'UnitId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioLocateSensorWithCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Devices.BiometricFramework.PWINBIO_LOCATE_SENSOR_CALLBACK,c_void_p, use_last_error=False)(("WinBioLocateSensorWithCallback", windll["winbio"]), ((1, 'SessionHandle'),(1, 'LocateCallback'),(1, 'LocateCallbackContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioEnrollBegin():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Byte,UInt32, use_last_error=False)(("WinBioEnrollBegin", windll["winbio"]), ((1, 'SessionHandle'),(1, 'SubFactor'),(1, 'UnitId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioEnrollSelect():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt64, use_last_error=False)(("WinBioEnrollSelect", windll["winbio"]), ((1, 'SessionHandle'),(1, 'SelectorValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioEnrollCapture():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(("WinBioEnrollCapture", windll["winbio"]), ((1, 'SessionHandle'),(1, 'RejectDetail'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioEnrollCaptureWithCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Devices.BiometricFramework.PWINBIO_ENROLL_CAPTURE_CALLBACK,c_void_p, use_last_error=False)(("WinBioEnrollCaptureWithCallback", windll["winbio"]), ((1, 'SessionHandle'),(1, 'EnrollCallback'),(1, 'EnrollCallbackContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioEnrollCommit():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),c_char_p_no, use_last_error=False)(("WinBioEnrollCommit", windll["winbio"]), ((1, 'SessionHandle'),(1, 'Identity'),(1, 'IsNewTemplate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioEnrollDiscard():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("WinBioEnrollDiscard", windll["winbio"]), ((1, 'SessionHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioEnumEnrollments():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),POINTER(c_char_p_no),POINTER(UIntPtr), use_last_error=False)(("WinBioEnumEnrollments", windll["winbio"]), ((1, 'SessionHandle'),(1, 'UnitId'),(1, 'Identity'),(1, 'SubFactorArray'),(1, 'SubFactorCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioImproveBegin():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(("WinBioImproveBegin", windll["winbio"]), ((1, 'SessionHandle'),(1, 'UnitId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioImproveEnd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("WinBioImproveEnd", windll["winbio"]), ((1, 'SessionHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioRegisterEventMonitor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Devices.BiometricFramework.PWINBIO_EVENT_CALLBACK,c_void_p, use_last_error=False)(("WinBioRegisterEventMonitor", windll["winbio"]), ((1, 'SessionHandle'),(1, 'EventMask'),(1, 'EventCallback'),(1, 'EventCallbackContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioUnregisterEventMonitor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("WinBioUnregisterEventMonitor", windll["winbio"]), ((1, 'SessionHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioMonitorPresence():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(("WinBioMonitorPresence", windll["winbio"]), ((1, 'SessionHandle'),(1, 'UnitId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioCaptureSample():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Byte,Byte,POINTER(UInt32),POINTER(POINTER(win32more.Devices.BiometricFramework.WINBIO_BIR_head)),POINTER(UIntPtr),POINTER(UInt32), use_last_error=False)(("WinBioCaptureSample", windll["winbio"]), ((1, 'SessionHandle'),(1, 'Purpose'),(1, 'Flags'),(1, 'UnitId'),(1, 'Sample'),(1, 'SampleSize'),(1, 'RejectDetail'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioCaptureSampleWithCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Byte,Byte,win32more.Devices.BiometricFramework.PWINBIO_CAPTURE_CALLBACK,c_void_p, use_last_error=False)(("WinBioCaptureSampleWithCallback", windll["winbio"]), ((1, 'SessionHandle'),(1, 'Purpose'),(1, 'Flags'),(1, 'CaptureCallback'),(1, 'CaptureCallbackContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioDeleteTemplate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),Byte, use_last_error=False)(("WinBioDeleteTemplate", windll["winbio"]), ((1, 'SessionHandle'),(1, 'UnitId'),(1, 'Identity'),(1, 'SubFactor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioLockUnit():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(("WinBioLockUnit", windll["winbio"]), ((1, 'SessionHandle'),(1, 'UnitId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioUnlockUnit():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(("WinBioUnlockUnit", windll["winbio"]), ((1, 'SessionHandle'),(1, 'UnitId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioControlUnit():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Devices.BiometricFramework.WINBIO_COMPONENT,UInt32,c_char_p_no,UIntPtr,c_char_p_no,UIntPtr,POINTER(UIntPtr),POINTER(UInt32), use_last_error=False)(("WinBioControlUnit", windll["winbio"]), ((1, 'SessionHandle'),(1, 'UnitId'),(1, 'Component'),(1, 'ControlCode'),(1, 'SendBuffer'),(1, 'SendBufferSize'),(1, 'ReceiveBuffer'),(1, 'ReceiveBufferSize'),(1, 'ReceiveDataSize'),(1, 'OperationStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioControlUnitPrivileged():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Devices.BiometricFramework.WINBIO_COMPONENT,UInt32,c_char_p_no,UIntPtr,c_char_p_no,UIntPtr,POINTER(UIntPtr),POINTER(UInt32), use_last_error=False)(("WinBioControlUnitPrivileged", windll["winbio"]), ((1, 'SessionHandle'),(1, 'UnitId'),(1, 'Component'),(1, 'ControlCode'),(1, 'SendBuffer'),(1, 'SendBufferSize'),(1, 'ReceiveBuffer'),(1, 'ReceiveBufferSize'),(1, 'ReceiveDataSize'),(1, 'OperationStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioGetProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,UInt32,POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),Byte,POINTER(c_void_p),POINTER(UIntPtr), use_last_error=False)(("WinBioGetProperty", windll["winbio"]), ((1, 'SessionHandle'),(1, 'PropertyType'),(1, 'PropertyId'),(1, 'UnitId'),(1, 'Identity'),(1, 'SubFactor'),(1, 'PropertyBuffer'),(1, 'PropertyBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioSetProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,UInt32,POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),Byte,c_void_p,UIntPtr, use_last_error=False)(("WinBioSetProperty", windll["winbio"]), ((1, 'SessionHandle'),(1, 'PropertyType'),(1, 'PropertyId'),(1, 'UnitId'),(1, 'Identity'),(1, 'SubFactor'),(1, 'PropertyBuffer'),(1, 'PropertyBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioFree():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("WinBioFree", windll["winbio"]), ((1, 'Address'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioSetCredential():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.BiometricFramework.WINBIO_CREDENTIAL_TYPE,c_char_p_no,UIntPtr,win32more.Devices.BiometricFramework.WINBIO_CREDENTIAL_FORMAT, use_last_error=False)(("WinBioSetCredential", windll["winbio"]), ((1, 'Type'),(1, 'Credential'),(1, 'CredentialSize'),(1, 'Format'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioRemoveCredential():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.BiometricFramework.WINBIO_IDENTITY,win32more.Devices.BiometricFramework.WINBIO_CREDENTIAL_TYPE, use_last_error=False)(("WinBioRemoveCredential", windll["winbio"]), ((1, 'Identity'),(1, 'Type'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioRemoveAllCredentials():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("WinBioRemoveAllCredentials", windll["winbio"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioRemoveAllDomainCredentials():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("WinBioRemoveAllDomainCredentials", windll["winbio"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioGetCredentialState():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.BiometricFramework.WINBIO_IDENTITY,win32more.Devices.BiometricFramework.WINBIO_CREDENTIAL_TYPE,POINTER(win32more.Devices.BiometricFramework.WINBIO_CREDENTIAL_STATE), use_last_error=False)(("WinBioGetCredentialState", windll["winbio"]), ((1, 'Identity'),(1, 'Type'),(1, 'CredentialState'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioLogonIdentifiedUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(("WinBioLogonIdentifiedUser", windll["winbio"]), ((1, 'SessionHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioGetEnrolledFactors():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.BiometricFramework.WINBIO_IDENTITY_head),POINTER(UInt32), use_last_error=False)(("WinBioGetEnrolledFactors", windll["winbio"]), ((1, 'AccountOwner'),(1, 'EnrolledFactors'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioGetEnabledSetting():
    try:
        return WINFUNCTYPE(Void,c_char_p_no,POINTER(win32more.Devices.BiometricFramework.WINBIO_SETTING_SOURCE), use_last_error=False)(("WinBioGetEnabledSetting", windll["winbio"]), ((1, 'Value'),(1, 'Source'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioGetLogonSetting():
    try:
        return WINFUNCTYPE(Void,c_char_p_no,POINTER(win32more.Devices.BiometricFramework.WINBIO_SETTING_SOURCE), use_last_error=False)(("WinBioGetLogonSetting", windll["winbio"]), ((1, 'Value'),(1, 'Source'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioGetDomainLogonSetting():
    try:
        return WINFUNCTYPE(Void,c_char_p_no,POINTER(win32more.Devices.BiometricFramework.WINBIO_SETTING_SOURCE), use_last_error=False)(("WinBioGetDomainLogonSetting", windll["winbio"]), ((1, 'Value'),(1, 'Source'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioAcquireFocus():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("WinBioAcquireFocus", windll["winbio"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinBioReleaseFocus():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("WinBioReleaseFocus", windll["winbio"]), ())
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "WINBIO_MAX_STRING_LEN",
    "WINBIO_SCP_VERSION_1",
    "WINBIO_SCP_RANDOM_SIZE_V1",
    "WINBIO_SCP_DIGEST_SIZE_V1",
    "WINBIO_SCP_CURVE_FIELD_SIZE_V1",
    "WINBIO_SCP_PUBLIC_KEY_SIZE_V1",
    "WINBIO_SCP_PRIVATE_KEY_SIZE_V1",
    "WINBIO_SCP_SIGNATURE_SIZE_V1",
    "WINBIO_SCP_ENCRYPTION_BLOCK_SIZE_V1",
    "WINBIO_SCP_ENCRYPTION_KEY_SIZE_V1",
    "WINBIO_BIR_ALIGN_SIZE",
    "WINBIO_BIR_ALGIN_SIZE",
    "FACILITY_WINBIO",
    "FACILITY_NONE",
    "WINBIO_E_UNSUPPORTED_FACTOR",
    "WINBIO_E_INVALID_UNIT",
    "WINBIO_E_UNKNOWN_ID",
    "WINBIO_E_CANCELED",
    "WINBIO_E_NO_MATCH",
    "WINBIO_E_CAPTURE_ABORTED",
    "WINBIO_E_ENROLLMENT_IN_PROGRESS",
    "WINBIO_E_BAD_CAPTURE",
    "WINBIO_E_INVALID_CONTROL_CODE",
    "WINBIO_E_DATA_COLLECTION_IN_PROGRESS",
    "WINBIO_E_UNSUPPORTED_DATA_FORMAT",
    "WINBIO_E_UNSUPPORTED_DATA_TYPE",
    "WINBIO_E_UNSUPPORTED_PURPOSE",
    "WINBIO_E_INVALID_DEVICE_STATE",
    "WINBIO_E_DEVICE_BUSY",
    "WINBIO_E_DATABASE_CANT_CREATE",
    "WINBIO_E_DATABASE_CANT_OPEN",
    "WINBIO_E_DATABASE_CANT_CLOSE",
    "WINBIO_E_DATABASE_CANT_ERASE",
    "WINBIO_E_DATABASE_CANT_FIND",
    "WINBIO_E_DATABASE_ALREADY_EXISTS",
    "WINBIO_E_DATABASE_FULL",
    "WINBIO_E_DATABASE_LOCKED",
    "WINBIO_E_DATABASE_CORRUPTED",
    "WINBIO_E_DATABASE_NO_SUCH_RECORD",
    "WINBIO_E_DUPLICATE_ENROLLMENT",
    "WINBIO_E_DATABASE_READ_ERROR",
    "WINBIO_E_DATABASE_WRITE_ERROR",
    "WINBIO_E_DATABASE_NO_RESULTS",
    "WINBIO_E_DATABASE_NO_MORE_RECORDS",
    "WINBIO_E_DATABASE_EOF",
    "WINBIO_E_DATABASE_BAD_INDEX_VECTOR",
    "WINBIO_E_INCORRECT_BSP",
    "WINBIO_E_INCORRECT_SENSOR_POOL",
    "WINBIO_E_NO_CAPTURE_DATA",
    "WINBIO_E_INVALID_SENSOR_MODE",
    "WINBIO_E_LOCK_VIOLATION",
    "WINBIO_E_DUPLICATE_TEMPLATE",
    "WINBIO_E_INVALID_OPERATION",
    "WINBIO_E_SESSION_BUSY",
    "WINBIO_E_CRED_PROV_DISABLED",
    "WINBIO_E_CRED_PROV_NO_CREDENTIAL",
    "WINBIO_E_DISABLED",
    "WINBIO_E_CONFIGURATION_FAILURE",
    "WINBIO_E_SENSOR_UNAVAILABLE",
    "WINBIO_E_SAS_ENABLED",
    "WINBIO_E_DEVICE_FAILURE",
    "WINBIO_E_FAST_USER_SWITCH_DISABLED",
    "WINBIO_E_NOT_ACTIVE_CONSOLE",
    "WINBIO_E_EVENT_MONITOR_ACTIVE",
    "WINBIO_E_INVALID_PROPERTY_TYPE",
    "WINBIO_E_INVALID_PROPERTY_ID",
    "WINBIO_E_UNSUPPORTED_PROPERTY",
    "WINBIO_E_ADAPTER_INTEGRITY_FAILURE",
    "WINBIO_E_INCORRECT_SESSION_TYPE",
    "WINBIO_E_SESSION_HANDLE_CLOSED",
    "WINBIO_E_DEADLOCK_DETECTED",
    "WINBIO_E_NO_PREBOOT_IDENTITY",
    "WINBIO_E_MAX_ERROR_COUNT_EXCEEDED",
    "WINBIO_E_AUTO_LOGON_DISABLED",
    "WINBIO_E_INVALID_TICKET",
    "WINBIO_E_TICKET_QUOTA_EXCEEDED",
    "WINBIO_E_DATA_PROTECTION_FAILURE",
    "WINBIO_E_CRED_PROV_SECURITY_LOCKOUT",
    "WINBIO_E_UNSUPPORTED_POOL_TYPE",
    "WINBIO_E_SELECTION_REQUIRED",
    "WINBIO_E_PRESENCE_MONITOR_ACTIVE",
    "WINBIO_E_INVALID_SUBFACTOR",
    "WINBIO_E_INVALID_CALIBRATION_FORMAT_ARRAY",
    "WINBIO_E_NO_SUPPORTED_CALIBRATION_FORMAT",
    "WINBIO_E_UNSUPPORTED_SENSOR_CALIBRATION_FORMAT",
    "WINBIO_E_CALIBRATION_BUFFER_TOO_SMALL",
    "WINBIO_E_CALIBRATION_BUFFER_TOO_LARGE",
    "WINBIO_E_CALIBRATION_BUFFER_INVALID",
    "WINBIO_E_INVALID_KEY_IDENTIFIER",
    "WINBIO_E_KEY_CREATION_FAILED",
    "WINBIO_E_KEY_IDENTIFIER_BUFFER_TOO_SMALL",
    "WINBIO_E_PROPERTY_UNAVAILABLE",
    "WINBIO_E_POLICY_PROTECTION_UNAVAILABLE",
    "WINBIO_E_INSECURE_SENSOR",
    "WINBIO_E_INVALID_BUFFER_ID",
    "WINBIO_E_INVALID_BUFFER",
    "WINBIO_E_TRUSTLET_INTEGRITY_FAIL",
    "WINBIO_E_ENROLLMENT_CANCELED_BY_SUSPEND",
    "WINBIO_I_MORE_DATA",
    "WINBIO_I_EXTENDED_STATUS_INFORMATION",
    "GUID_DEVINTERFACE_BIOMETRIC_READER",
    "IOCTL_BIOMETRIC_VENDOR",
    "WINBIO_WBDI_MAJOR_VERSION",
    "WINBIO_WBDI_MINOR_VERSION",
    "WINBIO_SETTING_SOURCE",
    "WINBIO_SETTING_SOURCE_INVALID",
    "WINBIO_SETTING_SOURCE_DEFAULT",
    "WINBIO_SETTING_SOURCE_LOCAL",
    "WINBIO_SETTING_SOURCE_POLICY",
    "WINBIO_COMPONENT",
    "WINBIO_COMPONENT_SENSOR",
    "WINBIO_COMPONENT_ENGINE",
    "WINBIO_COMPONENT_STORAGE",
    "WINBIO_POOL",
    "WINBIO_POOL_SYSTEM",
    "WINBIO_POOL_PRIVATE",
    "WINBIO_VERSION",
    "WINBIO_IDENTITY",
    "WINBIO_SECURE_CONNECTION_PARAMS",
    "WINBIO_SECURE_CONNECTION_DATA",
    "WINBIO_BIR_DATA",
    "WINBIO_BIR",
    "WINBIO_REGISTERED_FORMAT",
    "WINBIO_BIR_HEADER",
    "WINBIO_BDB_ANSI_381_HEADER",
    "WINBIO_BDB_ANSI_381_RECORD",
    "WINBIO_SECURE_BUFFER_HEADER_V1",
    "WINBIO_EVENT",
    "WINBIO_PRESENCE_PROPERTIES",
    "WINBIO_PRESENCE",
    "WINBIO_BSP_SCHEMA",
    "WINBIO_UNIT_SCHEMA",
    "WINBIO_STORAGE_SCHEMA",
    "WINBIO_EXTENDED_SENSOR_INFO",
    "WINBIO_EXTENDED_ENGINE_INFO",
    "WINBIO_EXTENDED_STORAGE_INFO",
    "WINBIO_EXTENDED_ENROLLMENT_STATUS",
    "WINBIO_EXTENDED_UNIT_STATUS",
    "WINBIO_FP_BU_STATE",
    "WINBIO_ANTI_SPOOF_POLICY_ACTION",
    "WINBIO_ANTI_SPOOF_DISABLE",
    "WINBIO_ANTI_SPOOF_ENABLE",
    "WINBIO_ANTI_SPOOF_REMOVE",
    "WINBIO_POLICY_SOURCE",
    "WINBIO_POLICY_UNKNOWN",
    "WINBIO_POLICY_DEFAULT",
    "WINBIO_POLICY_LOCAL",
    "WINBIO_POLICY_ADMIN",
    "WINBIO_ANTI_SPOOF_POLICY",
    "WINBIO_CREDENTIAL_TYPE",
    "WINBIO_CREDENTIAL_PASSWORD",
    "WINBIO_CREDENTIAL_ALL",
    "WINBIO_CREDENTIAL_FORMAT",
    "WINBIO_PASSWORD_GENERIC",
    "WINBIO_PASSWORD_PACKED",
    "WINBIO_PASSWORD_PROTECTED",
    "WINBIO_CREDENTIAL_STATE",
    "WINBIO_CREDENTIAL_NOT_SET",
    "WINBIO_CREDENTIAL_SET",
    "WINBIO_EXTENDED_ENROLLMENT_PARAMETERS",
    "WINBIO_ACCOUNT_POLICY",
    "WINBIO_PROTECTION_POLICY",
    "WINBIO_GESTURE_METADATA",
    "WINBIO_ASYNC_NOTIFICATION_METHOD",
    "WINBIO_ASYNC_NOTIFY_NONE",
    "WINBIO_ASYNC_NOTIFY_CALLBACK",
    "WINBIO_ASYNC_NOTIFY_MESSAGE",
    "WINBIO_ASYNC_NOTIFY_MAXIMUM_VALUE",
    "WINBIO_ASYNC_RESULT",
    "PWINBIO_ASYNC_COMPLETION_CALLBACK",
    "PWINBIO_VERIFY_CALLBACK",
    "PWINBIO_IDENTIFY_CALLBACK",
    "PWINBIO_LOCATE_SENSOR_CALLBACK",
    "PWINBIO_ENROLL_CAPTURE_CALLBACK",
    "PWINBIO_EVENT_CALLBACK",
    "PWINBIO_CAPTURE_CALLBACK",
    "_WINIBIO_SENSOR_CONTEXT",
    "_WINIBIO_ENGINE_CONTEXT",
    "_WINIBIO_STORAGE_CONTEXT",
    "WINBIO_STORAGE_RECORD",
    "WINBIO_PIPELINE",
    "WINBIO_ADAPTER_INTERFACE_VERSION",
    "PIBIO_SENSOR_ATTACH_FN",
    "PIBIO_SENSOR_DETACH_FN",
    "PIBIO_SENSOR_CLEAR_CONTEXT_FN",
    "PIBIO_SENSOR_QUERY_STATUS_FN",
    "PIBIO_SENSOR_RESET_FN",
    "PIBIO_SENSOR_SET_MODE_FN",
    "PIBIO_SENSOR_SET_INDICATOR_STATUS_FN",
    "PIBIO_SENSOR_GET_INDICATOR_STATUS_FN",
    "PIBIO_SENSOR_START_CAPTURE_FN",
    "PIBIO_SENSOR_FINISH_CAPTURE_FN",
    "PIBIO_SENSOR_EXPORT_SENSOR_DATA_FN",
    "PIBIO_SENSOR_CANCEL_FN",
    "PIBIO_SENSOR_PUSH_DATA_TO_ENGINE_FN",
    "PIBIO_SENSOR_CONTROL_UNIT_FN",
    "PIBIO_SENSOR_CONTROL_UNIT_PRIVILEGED_FN",
    "PIBIO_SENSOR_NOTIFY_POWER_CHANGE_FN",
    "PIBIO_SENSOR_PIPELINE_INIT_FN",
    "PIBIO_SENSOR_PIPELINE_CLEANUP_FN",
    "PIBIO_SENSOR_ACTIVATE_FN",
    "PIBIO_SENSOR_DEACTIVATE_FN",
    "PIBIO_SENSOR_QUERY_EXTENDED_INFO_FN",
    "PIBIO_SENSOR_QUERY_CALIBRATION_FORMATS_FN",
    "PIBIO_SENSOR_SET_CALIBRATION_FORMAT_FN",
    "PIBIO_SENSOR_ACCEPT_CALIBRATION_DATA_FN",
    "PIBIO_SENSOR_ASYNC_IMPORT_RAW_BUFFER_FN",
    "PIBIO_SENSOR_ASYNC_IMPORT_SECURE_BUFFER_FN",
    "PIBIO_SENSOR_QUERY_PRIVATE_SENSOR_TYPE_FN",
    "PIBIO_SENSOR_CONNECT_SECURE_FN",
    "PIBIO_SENSOR_START_CAPTURE_EX_FN",
    "PIBIO_SENSOR_START_NOTIFY_WAKE_FN",
    "PIBIO_SENSOR_FINISH_NOTIFY_WAKE_FN",
    "WINBIO_SENSOR_INTERFACE",
    "PWINBIO_QUERY_SENSOR_INTERFACE_FN",
    "PIBIO_ENGINE_ATTACH_FN",
    "PIBIO_ENGINE_DETACH_FN",
    "PIBIO_ENGINE_CLEAR_CONTEXT_FN",
    "PIBIO_ENGINE_QUERY_PREFERRED_FORMAT_FN",
    "PIBIO_ENGINE_QUERY_INDEX_VECTOR_SIZE_FN",
    "PIBIO_ENGINE_QUERY_HASH_ALGORITHMS_FN",
    "PIBIO_ENGINE_SET_HASH_ALGORITHM_FN",
    "PIBIO_ENGINE_QUERY_SAMPLE_HINT_FN",
    "PIBIO_ENGINE_ACCEPT_SAMPLE_DATA_FN",
    "PIBIO_ENGINE_EXPORT_ENGINE_DATA_FN",
    "PIBIO_ENGINE_VERIFY_FEATURE_SET_FN",
    "PIBIO_ENGINE_IDENTIFY_FEATURE_SET_FN",
    "PIBIO_ENGINE_CREATE_ENROLLMENT_FN",
    "PIBIO_ENGINE_UPDATE_ENROLLMENT_FN",
    "PIBIO_ENGINE_GET_ENROLLMENT_STATUS_FN",
    "PIBIO_ENGINE_GET_ENROLLMENT_HASH_FN",
    "PIBIO_ENGINE_CHECK_FOR_DUPLICATE_FN",
    "PIBIO_ENGINE_COMMIT_ENROLLMENT_FN",
    "PIBIO_ENGINE_DISCARD_ENROLLMENT_FN",
    "PIBIO_ENGINE_CONTROL_UNIT_FN",
    "PIBIO_ENGINE_CONTROL_UNIT_PRIVILEGED_FN",
    "PIBIO_ENGINE_NOTIFY_POWER_CHANGE_FN",
    "PIBIO_ENGINE_RESERVED_1_FN",
    "PIBIO_ENGINE_PIPELINE_INIT_FN",
    "PIBIO_ENGINE_PIPELINE_CLEANUP_FN",
    "PIBIO_ENGINE_ACTIVATE_FN",
    "PIBIO_ENGINE_DEACTIVATE_FN",
    "PIBIO_ENGINE_QUERY_EXTENDED_INFO_FN",
    "PIBIO_ENGINE_IDENTIFY_ALL_FN",
    "PIBIO_ENGINE_SET_ENROLLMENT_SELECTOR_FN",
    "PIBIO_ENGINE_SET_ENROLLMENT_PARAMETERS_FN",
    "PIBIO_ENGINE_QUERY_EXTENDED_ENROLLMENT_STATUS_FN",
    "PIBIO_ENGINE_REFRESH_CACHE_FN",
    "PIBIO_ENGINE_SELECT_CALIBRATION_FORMAT_FN",
    "PIBIO_ENGINE_QUERY_CALIBRATION_DATA_FN",
    "PIBIO_ENGINE_SET_ACCOUNT_POLICY_FN",
    "PIBIO_ENGINE_CREATE_KEY_FN",
    "PIBIO_ENGINE_IDENTIFY_FEATURE_SET_SECURE_FN",
    "PIBIO_ENGINE_ACCEPT_PRIVATE_SENSOR_TYPE_INFO_FN",
    "PIBIO_ENGINE_CREATE_ENROLLMENT_AUTHENTICATED_FN",
    "PIBIO_ENGINE_IDENTIFY_FEATURE_SET_AUTHENTICATED_FN",
    "WINBIO_ENGINE_INTERFACE",
    "PWINBIO_QUERY_ENGINE_INTERFACE_FN",
    "PIBIO_STORAGE_ATTACH_FN",
    "PIBIO_STORAGE_DETACH_FN",
    "PIBIO_STORAGE_CLEAR_CONTEXT_FN",
    "PIBIO_STORAGE_CREATE_DATABASE_FN",
    "PIBIO_STORAGE_ERASE_DATABASE_FN",
    "PIBIO_STORAGE_OPEN_DATABASE_FN",
    "PIBIO_STORAGE_CLOSE_DATABASE_FN",
    "PIBIO_STORAGE_GET_DATA_FORMAT_FN",
    "PIBIO_STORAGE_GET_DATABASE_SIZE_FN",
    "PIBIO_STORAGE_ADD_RECORD_FN",
    "PIBIO_STORAGE_DELETE_RECORD_FN",
    "PIBIO_STORAGE_QUERY_BY_SUBJECT_FN",
    "PIBIO_STORAGE_QUERY_BY_CONTENT_FN",
    "PIBIO_STORAGE_GET_RECORD_COUNT_FN",
    "PIBIO_STORAGE_FIRST_RECORD_FN",
    "PIBIO_STORAGE_NEXT_RECORD_FN",
    "PIBIO_STORAGE_GET_CURRENT_RECORD_FN",
    "PIBIO_STORAGE_CONTROL_UNIT_FN",
    "PIBIO_STORAGE_CONTROL_UNIT_PRIVILEGED_FN",
    "PIBIO_STORAGE_NOTIFY_POWER_CHANGE_FN",
    "PIBIO_STORAGE_PIPELINE_INIT_FN",
    "PIBIO_STORAGE_PIPELINE_CLEANUP_FN",
    "PIBIO_STORAGE_ACTIVATE_FN",
    "PIBIO_STORAGE_DEACTIVATE_FN",
    "PIBIO_STORAGE_QUERY_EXTENDED_INFO_FN",
    "PIBIO_STORAGE_NOTIFY_DATABASE_CHANGE_FN",
    "PIBIO_STORAGE_RESERVED_1_FN",
    "PIBIO_STORAGE_RESERVED_2_FN",
    "PIBIO_STORAGE_UPDATE_RECORD_BEGIN_FN",
    "PIBIO_STORAGE_UPDATE_RECORD_COMMIT_FN",
    "WINBIO_STORAGE_INTERFACE",
    "PWINBIO_QUERY_STORAGE_INTERFACE_FN",
    "PIBIO_FRAMEWORK_SET_UNIT_STATUS_FN",
    "PIBIO_FRAMEWORK_VSM_CACHE_CLEAR_FN",
    "PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_BEGIN_FN",
    "PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_NEXT_FN",
    "PIBIO_FRAMEWORK_VSM_CACHE_IMPORT_END_FN",
    "PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_BEGIN_FN",
    "PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_NEXT_FN",
    "PIBIO_FRAMEWORK_VSM_CACHE_EXPORT_END_FN",
    "PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_1_FN",
    "PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_2_FN",
    "PIBIO_FRAMEWORK_VSM_STORAGE_RESERVED_3_FN",
    "PIBIO_FRAMEWORK_ALLOCATE_MEMORY_FN",
    "PIBIO_FRAMEWORK_FREE_MEMORY_FN",
    "PIBIO_FRAMEWORK_GET_PROPERTY_FN",
    "PIBIO_FRAMEWORK_LOCK_AND_VALIDATE_SECURE_BUFFER_FN",
    "PIBIO_FRAMEWORK_RELEASE_SECURE_BUFFER_FN",
    "PIBIO_FRAMEWORK_VSM_QUERY_AUTHORIZED_ENROLLMENTS_FN",
    "PIBIO_FRAMEWORK_VSM_DECRYPT_SAMPLE_FN",
    "WINBIO_FRAMEWORK_INTERFACE",
    "WINBIO_SENSOR_ATTRIBUTES",
    "WINBIO_DATA",
    "WINBIO_UPDATE_FIRMWARE",
    "WINBIO_CALIBRATION_INFO",
    "WINBIO_DIAGNOSTICS",
    "WINBIO_BLANK_PAYLOAD",
    "WINBIO_CAPTURE_PARAMETERS",
    "WINBIO_CAPTURE_DATA",
    "WINBIO_SUPPORTED_ALGORITHMS",
    "WINBIO_GET_INDICATOR",
    "WINBIO_SET_INDICATOR",
    "WINBIO_PRIVATE_SENSOR_TYPE_INFO",
    "WINBIO_ENCRYPTED_CAPTURE_PARAMS",
    "WINBIO_NOTIFY_WAKE",
    "WinBioEnumServiceProviders",
    "WinBioEnumBiometricUnits",
    "WinBioEnumDatabases",
    "WinBioAsyncOpenFramework",
    "WinBioCloseFramework",
    "WinBioAsyncEnumServiceProviders",
    "WinBioAsyncEnumBiometricUnits",
    "WinBioAsyncEnumDatabases",
    "WinBioAsyncMonitorFrameworkChanges",
    "WinBioOpenSession",
    "WinBioAsyncOpenSession",
    "WinBioCloseSession",
    "WinBioVerify",
    "WinBioVerifyWithCallback",
    "WinBioIdentify",
    "WinBioIdentifyWithCallback",
    "WinBioWait",
    "WinBioCancel",
    "WinBioLocateSensor",
    "WinBioLocateSensorWithCallback",
    "WinBioEnrollBegin",
    "WinBioEnrollSelect",
    "WinBioEnrollCapture",
    "WinBioEnrollCaptureWithCallback",
    "WinBioEnrollCommit",
    "WinBioEnrollDiscard",
    "WinBioEnumEnrollments",
    "WinBioImproveBegin",
    "WinBioImproveEnd",
    "WinBioRegisterEventMonitor",
    "WinBioUnregisterEventMonitor",
    "WinBioMonitorPresence",
    "WinBioCaptureSample",
    "WinBioCaptureSampleWithCallback",
    "WinBioDeleteTemplate",
    "WinBioLockUnit",
    "WinBioUnlockUnit",
    "WinBioControlUnit",
    "WinBioControlUnitPrivileged",
    "WinBioGetProperty",
    "WinBioSetProperty",
    "WinBioFree",
    "WinBioSetCredential",
    "WinBioRemoveCredential",
    "WinBioRemoveAllCredentials",
    "WinBioRemoveAllDomainCredentials",
    "WinBioGetCredentialState",
    "WinBioLogonIdentifiedUser",
    "WinBioGetEnrolledFactors",
    "WinBioGetEnabledSetting",
    "WinBioGetLogonSetting",
    "WinBioGetDomainLogonSetting",
    "WinBioAcquireFocus",
    "WinBioReleaseFocus",
]
