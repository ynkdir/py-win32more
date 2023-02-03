from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Devices.Geolocation
import Windows.Win32.Devices.Sensors
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import Windows.Win32.UI.Shell.PropertiesSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
GNSS_DRIVER_VERSION_1: UInt32 = 1
GNSS_DRIVER_VERSION_2: UInt32 = 2
GNSS_DRIVER_VERSION_3: UInt32 = 3
GNSS_DRIVER_VERSION_4: UInt32 = 4
GNSS_DRIVER_VERSION_5: UInt32 = 5
GNSS_DRIVER_VERSION_6: UInt32 = 6
IOCTL_GNSS_SEND_PLATFORM_CAPABILITY: UInt32 = 2228228
IOCTL_GNSS_GET_DEVICE_CAPABILITY: UInt32 = 2228232
IOCTL_GNSS_SEND_DRIVERCOMMAND: UInt32 = 2228236
IOCTL_GNSS_START_FIXSESSION: UInt32 = 2228288
IOCTL_GNSS_MODIFY_FIXSESSION: UInt32 = 2228292
IOCTL_GNSS_STOP_FIXSESSION: UInt32 = 2228296
IOCTL_GNSS_GET_FIXDATA: UInt32 = 2228300
IOCTL_GNSS_INJECT_AGNSS: UInt32 = 2228352
IOCTL_GNSS_LISTEN_AGNSS: UInt32 = 2228416
IOCTL_GNSS_LISTEN_ERROR: UInt32 = 2228420
IOCTL_GNSS_LISTEN_NI: UInt32 = 2228480
IOCTL_GNSS_SET_SUPL_HSLP: UInt32 = 2228484
IOCTL_GNSS_CONFIG_SUPL_CERT: UInt32 = 2228488
IOCTL_GNSS_RESPOND_NI: UInt32 = 2228492
IOCTL_GNSS_EXECUTE_CWTEST: UInt32 = 2228496
IOCTL_GNSS_EXECUTE_SELFTEST: UInt32 = 2228500
IOCTL_GNSS_GET_CHIPSETINFO: UInt32 = 2228504
IOCTL_GNSS_LISTEN_NMEA: UInt32 = 2228508
IOCTL_GNSS_SET_V2UPL_CONFIG: UInt32 = 2228512
IOCTL_GNSS_CREATE_GEOFENCE: UInt32 = 2228544
IOCTL_GNSS_DELETE_GEOFENCE: UInt32 = 2228548
IOCTL_GNSS_LISTEN_GEOFENCE_ALERT: UInt32 = 2228552
IOCTL_GNSS_LISTEN_GEOFENCES_TRACKINGSTATUS: UInt32 = 2228556
IOCTL_GNSS_LISTEN_DRIVER_REQUEST: UInt32 = 2228608
IOCTL_GNSS_START_BREADCRUMBING: UInt32 = 2228672
IOCTL_GNSS_STOP_BREADCRUMBING: UInt32 = 2228676
IOCTL_GNSS_LISTEN_BREADCRUMBING_ALERT: UInt32 = 2228680
IOCTL_GNSS_POP_BREADCRUMBS: UInt32 = 2228684
GNSS_AGNSSFORMAT_XTRA1: UInt32 = 1
GNSS_AGNSSFORMAT_XTRA2: UInt32 = 2
GNSS_AGNSSFORMAT_LTO: UInt32 = 4
GNSS_AGNSSFORMAT_XTRA3: UInt32 = 8
GNSS_AGNSSFORMAT_XTRA3_1: UInt32 = 16
GNSS_AGNSSFORMAT_XTRA3_2: UInt32 = 32
GNSS_AGNSSFORMAT_XTRA_INT: UInt32 = 64
MAX_SERVER_URL_NAME: UInt32 = 260
MIN_GEOFENCES_REQUIRED: UInt32 = 100
BREADCRUMBING_UNSUPPORTED: UInt32 = 0
BREADCRUMBING_VERSION_1: UInt32 = 1
MIN_BREADCRUMBS_SUPPORTED: UInt32 = 120
GNSS_SATELLITE_ANY: UInt32 = 0
GNSS_SATELLITE_GPS: UInt32 = 1
GNSS_SATELLITE_GLONASS: UInt32 = 2
GNSS_SATELLITE_BEIDOU: UInt32 = 4
GNSS_SATELLITE_GALILEO: UInt32 = 8
GNSS_OPERMODE_ANY: UInt32 = 0
GNSS_OPERMODE_MSA: UInt32 = 1
GNSS_OPERMODE_MSB: UInt32 = 2
GNSS_OPERMODE_MSS: UInt32 = 4
GNSS_OPERMODE_CELLID: UInt32 = 8
GNSS_OPERMODE_AFLT: UInt32 = 16
GNSS_OPERMODE_OTDOA: UInt32 = 32
GNSS_NMEALOGGING_NONE: UInt32 = 0
GNSS_NMEALOGGING_ALL: UInt32 = 255
GNSS_FIXDETAIL_BASIC: UInt32 = 1
GNSS_FIXDETAIL_ACCURACY: UInt32 = 2
GNSS_FIXDETAIL_SATELLITE: UInt32 = 4
GNSS_MAXSATELLITE: UInt32 = 64
GNSS_GEOFENCESUPPORT_SUPPORTED: UInt32 = 1
GNSS_GEOFENCESUPPORT_CIRCLE: UInt32 = 2
LOCATION_API_VERSION: UInt32 = 1
GUID_DEVINTERFACE_GNSS: Guid = Guid('3336e5e4-018a-4669-84-c5-bd-05-f3-bd-36-8b')
CivicAddressReport = Guid('d39e7bdd-7d05-46b8-87-21-80-cf-03-5f-57-d7')
CivicAddressReportFactory = Guid('2a11f42c-3e81-4ad4-9c-be-45-57-9d-89-67-1a')
DefaultLocation = Guid('8b7fbfe0-5cd7-494a-af-8c-28-3a-65-70-75-06')
DispCivicAddressReport = Guid('4c596aec-8544-4082-ba-9f-eb-0a-7d-8e-65-c6')
DispLatLongReport = Guid('7a7c3277-8f84-4636-95-b2-eb-b5-50-7f-f7-7e')
class GNSS_AGNSS_INJECT(Structure):
    Size: UInt32
    Version: UInt32
    InjectionType: Windows.Win32.Devices.Geolocation.GNSS_AGNSS_REQUEST_TYPE
    InjectionStatus: Windows.Win32.Foundation.NTSTATUS
    InjectionDataSize: UInt32
    Unused: Byte * 512
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Time: Windows.Win32.Devices.Geolocation.GNSS_AGNSS_INJECTTIME
        Position: Windows.Win32.Devices.Geolocation.GNSS_AGNSS_INJECTPOSITION
        BlobData: Windows.Win32.Devices.Geolocation.GNSS_AGNSS_INJECTBLOB
class GNSS_AGNSS_INJECTBLOB(Structure):
    Size: UInt32
    Version: UInt32
    BlobOui: UInt32
    BlobVersion: UInt32
    AgnssFormat: UInt32
    BlobSize: UInt32
    BlobData: Byte * 1
class GNSS_AGNSS_INJECTPOSITION(Structure):
    Size: UInt32
    Version: UInt32
    Age: UInt32
    BasicData: Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_BASIC
    AccuracyData: Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_ACCURACY
class GNSS_AGNSS_INJECTTIME(Structure):
    Size: UInt32
    Version: UInt32
    UtcTime: Windows.Win32.Foundation.FILETIME
    TimeUncertainty: UInt32
class GNSS_AGNSS_REQUEST_PARAM(Structure):
    Size: UInt32
    Version: UInt32
    RequestType: Windows.Win32.Devices.Geolocation.GNSS_AGNSS_REQUEST_TYPE
    BlobFormat: UInt32
GNSS_AGNSS_REQUEST_TYPE = Int32
GNSS_AGNSS_TimeInjection: GNSS_AGNSS_REQUEST_TYPE = 1
GNSS_AGNSS_PositionInjection: GNSS_AGNSS_REQUEST_TYPE = 2
GNSS_AGNSS_BlobInjection: GNSS_AGNSS_REQUEST_TYPE = 3
class GNSS_BREADCRUMBING_ALERT_DATA(Structure):
    Size: UInt32
    Version: UInt32
    Unused: Byte * 512
class GNSS_BREADCRUMBING_PARAM(Structure):
    Size: UInt32
    Version: UInt32
    MaximumHorizontalUncertainty: UInt32
    MinDistanceBetweenFixes: UInt32
    MaximumErrorTimeoutMs: UInt32
    Unused: Byte * 512
class GNSS_BREADCRUMB_LIST(Structure):
    Size: UInt32
    Version: UInt32
    NumCrumbs: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        v1: Windows.Win32.Devices.Geolocation.GNSS_BREADCRUMB_V1 * 50
class GNSS_BREADCRUMB_V1(Structure):
    FixTimeStamp: Windows.Win32.Foundation.FILETIME
    Latitude: Double
    Longitude: Double
    HorizontalAccuracy: UInt32
    Speed: UInt16
    SpeedAccuracy: UInt16
    Altitude: Int16
    AltitudeAccuracy: UInt16
    Heading: Int16
    HeadingAccuracy: Byte
    FixSuccess: Byte
class GNSS_CHIPSETINFO(Structure):
    Size: UInt32
    Version: UInt32
    ManufacturerID: Char * 25
    HardwareID: Char * 25
    FirmwareVersion: Char * 20
    Unused: Byte * 512
class GNSS_CONTINUOUSTRACKING_PARAM(Structure):
    Size: UInt32
    Version: UInt32
    PreferredInterval: UInt32
class GNSS_CP_NI_INFO(Structure):
    Size: UInt32
    Version: UInt32
    RequestorId: Char * 260
    NotificationText: Char * 260
class GNSS_CWTESTDATA(Structure):
    Size: UInt32
    Version: UInt32
    TestResultStatus: Windows.Win32.Foundation.NTSTATUS
    SignalToNoiseRatio: Double
    Frequency: Double
    Unused: Byte * 512
class GNSS_DEVICE_CAPABILITY(Structure):
    Size: UInt32
    Version: UInt32
    SupportMultipleFixSessions: Windows.Win32.Foundation.BOOL
    SupportMultipleAppSessions: Windows.Win32.Foundation.BOOL
    RequireAGnssInjection: Windows.Win32.Foundation.BOOL
    AgnssFormatSupported: UInt32
    AgnssFormatPreferred: UInt32
    SupportDistanceTracking: Windows.Win32.Foundation.BOOL
    SupportContinuousTracking: Windows.Win32.Foundation.BOOL
    Reserved1: UInt32
    Reserved2: Windows.Win32.Foundation.BOOL
    Reserved3: Windows.Win32.Foundation.BOOL
    Reserved4: Windows.Win32.Foundation.BOOL
    Reserved5: Windows.Win32.Foundation.BOOL
    GeofencingSupport: UInt32
    Reserved6: Windows.Win32.Foundation.BOOL
    Reserved7: Windows.Win32.Foundation.BOOL
    SupportCpLocation: Windows.Win32.Foundation.BOOL
    SupportUplV2: Windows.Win32.Foundation.BOOL
    SupportSuplV1: Windows.Win32.Foundation.BOOL
    SupportSuplV2: Windows.Win32.Foundation.BOOL
    SupportedSuplVersion: Windows.Win32.Devices.Geolocation.GNSS_SUPL_VERSION
    MaxGeofencesSupported: UInt32
    SupportMultipleSuplRootCert: Windows.Win32.Foundation.BOOL
    GnssBreadCrumbPayloadVersion: UInt32
    MaxGnssBreadCrumbFixes: UInt32
    Unused: Byte * 496
class GNSS_DISTANCETRACKING_PARAM(Structure):
    Size: UInt32
    Version: UInt32
    MovementThreshold: UInt32
class GNSS_DRIVERCOMMAND_PARAM(Structure):
    Size: UInt32
    Version: UInt32
    CommandType: Windows.Win32.Devices.Geolocation.GNSS_DRIVERCOMMAND_TYPE
    Reserved: UInt32
    CommandDataSize: UInt32
    Unused: Byte * 512
    CommandData: Byte * 1
GNSS_DRIVERCOMMAND_TYPE = Int32
GNSS_SetLocationServiceEnabled: GNSS_DRIVERCOMMAND_TYPE = 1
GNSS_SetLocationNIRequestAllowed: GNSS_DRIVERCOMMAND_TYPE = 2
GNSS_ForceSatelliteSystem: GNSS_DRIVERCOMMAND_TYPE = 3
GNSS_ForceOperationMode: GNSS_DRIVERCOMMAND_TYPE = 4
GNSS_ResetEngine: GNSS_DRIVERCOMMAND_TYPE = 9
GNSS_ClearAgnssData: GNSS_DRIVERCOMMAND_TYPE = 10
GNSS_SetSuplVersion: GNSS_DRIVERCOMMAND_TYPE = 12
GNSS_SetNMEALogging: GNSS_DRIVERCOMMAND_TYPE = 13
GNSS_SetUplServerAccessInterval: GNSS_DRIVERCOMMAND_TYPE = 14
GNSS_SetNiTimeoutInterval: GNSS_DRIVERCOMMAND_TYPE = 15
GNSS_ResetGeofencesTracking: GNSS_DRIVERCOMMAND_TYPE = 16
GNSS_SetSuplVersion2: GNSS_DRIVERCOMMAND_TYPE = 17
GNSS_CustomCommand: GNSS_DRIVERCOMMAND_TYPE = 256
GNSS_DRIVER_REQUEST = Int32
SUPL_CONFIG_DATA: GNSS_DRIVER_REQUEST = 1
class GNSS_DRIVER_REQUEST_DATA(Structure):
    Size: UInt32
    Version: UInt32
    Request: Windows.Win32.Devices.Geolocation.GNSS_DRIVER_REQUEST
    RequestFlag: UInt32
class GNSS_ERRORINFO(Structure):
    Size: UInt32
    Version: UInt32
    ErrorCode: UInt32
    IsRecoverable: Windows.Win32.Foundation.BOOL
    ErrorDescription: Char * 256
    Unused: Byte * 512
class GNSS_EVENT(Structure):
    Size: UInt32
    Version: UInt32
    EventType: Windows.Win32.Devices.Geolocation.GNSS_EVENT_TYPE
    EventDataSize: UInt32
    Unused: Byte * 512
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        FixData: Windows.Win32.Devices.Geolocation.GNSS_FIXDATA
        AgnssRequest: Windows.Win32.Devices.Geolocation.GNSS_AGNSS_REQUEST_PARAM
        NiRequest: Windows.Win32.Devices.Geolocation.GNSS_NI_REQUEST_PARAM
        ErrorInformation: Windows.Win32.Devices.Geolocation.GNSS_ERRORINFO
        NmeaData: Windows.Win32.Devices.Geolocation.GNSS_NMEA_DATA
        GeofenceAlertData: Windows.Win32.Devices.Geolocation.GNSS_GEOFENCE_ALERT_DATA
        BreadcrumbAlertData: Windows.Win32.Devices.Geolocation.GNSS_BREADCRUMBING_ALERT_DATA
        GeofencesTrackingStatus: Windows.Win32.Devices.Geolocation.GNSS_GEOFENCES_TRACKINGSTATUS_DATA
        DriverRequestData: Windows.Win32.Devices.Geolocation.GNSS_DRIVER_REQUEST_DATA
        CustomData: Byte * 1
class GNSS_EVENT_2(Structure):
    Size: UInt32
    Version: UInt32
    EventType: Windows.Win32.Devices.Geolocation.GNSS_EVENT_TYPE
    EventDataSize: UInt32
    Unused: Byte * 512
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        FixData: Windows.Win32.Devices.Geolocation.GNSS_FIXDATA
        FixData2: Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_2
        AgnssRequest: Windows.Win32.Devices.Geolocation.GNSS_AGNSS_REQUEST_PARAM
        NiRequest: Windows.Win32.Devices.Geolocation.GNSS_NI_REQUEST_PARAM
        ErrorInformation: Windows.Win32.Devices.Geolocation.GNSS_ERRORINFO
        NmeaData: Windows.Win32.Devices.Geolocation.GNSS_NMEA_DATA
        GeofenceAlertData: Windows.Win32.Devices.Geolocation.GNSS_GEOFENCE_ALERT_DATA
        BreadcrumbAlertData: Windows.Win32.Devices.Geolocation.GNSS_BREADCRUMBING_ALERT_DATA
        GeofencesTrackingStatus: Windows.Win32.Devices.Geolocation.GNSS_GEOFENCES_TRACKINGSTATUS_DATA
        DriverRequestData: Windows.Win32.Devices.Geolocation.GNSS_DRIVER_REQUEST_DATA
        CustomData: Byte * 1
GNSS_EVENT_TYPE = Int32
GNSS_Event_FixAvailable: GNSS_EVENT_TYPE = 1
GNSS_Event_RequireAgnss: GNSS_EVENT_TYPE = 2
GNSS_Event_Error: GNSS_EVENT_TYPE = 3
GNSS_Event_NiRequest: GNSS_EVENT_TYPE = 12
GNSS_Event_NmeaData: GNSS_EVENT_TYPE = 13
GNSS_Event_GeofenceAlertData: GNSS_EVENT_TYPE = 14
GNSS_Event_GeofencesTrackingStatus: GNSS_EVENT_TYPE = 15
GNSS_Event_DriverRequest: GNSS_EVENT_TYPE = 16
GNSS_Event_BreadcrumbAlertEvent: GNSS_EVENT_TYPE = 17
GNSS_Event_FixAvailable_2: GNSS_EVENT_TYPE = 18
GNSS_Event_Custom: GNSS_EVENT_TYPE = 32768
class GNSS_FIXDATA(Structure):
    Size: UInt32
    Version: UInt32
    FixSessionID: UInt32
    FixTimeStamp: Windows.Win32.Foundation.FILETIME
    IsFinalFix: Windows.Win32.Foundation.BOOL
    FixStatus: Windows.Win32.Foundation.NTSTATUS
    FixLevelOfDetails: UInt32
    BasicData: Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_BASIC
    AccuracyData: Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_ACCURACY
    SatelliteData: Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_SATELLITE
class GNSS_FIXDATA_2(Structure):
    Size: UInt32
    Version: UInt32
    FixSessionID: UInt32
    FixTimeStamp: Windows.Win32.Foundation.FILETIME
    IsFinalFix: Windows.Win32.Foundation.BOOL
    FixStatus: Windows.Win32.Foundation.NTSTATUS
    FixLevelOfDetails: UInt32
    BasicData: Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_BASIC_2
    AccuracyData: Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_ACCURACY_2
    SatelliteData: Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_SATELLITE
class GNSS_FIXDATA_ACCURACY(Structure):
    Size: UInt32
    Version: UInt32
    HorizontalAccuracy: UInt32
    HorizontalErrorMajorAxis: UInt32
    HorizontalErrorMinorAxis: UInt32
    HorizontalErrorAngle: UInt32
    HeadingAccuracy: UInt32
    AltitudeAccuracy: UInt32
    SpeedAccuracy: UInt32
    HorizontalConfidence: UInt32
    HeadingConfidence: UInt32
    AltitudeConfidence: UInt32
    SpeedConfidence: UInt32
    PositionDilutionOfPrecision: Single
    HorizontalDilutionOfPrecision: Single
    VerticalDilutionOfPrecision: Single
class GNSS_FIXDATA_ACCURACY_2(Structure):
    Size: UInt32
    Version: UInt32
    HorizontalAccuracy: Double
    HorizontalErrorMajorAxis: Double
    HorizontalErrorMinorAxis: Double
    HorizontalErrorAngle: Double
    HeadingAccuracy: Double
    AltitudeAccuracy: Double
    SpeedAccuracy: Double
    HorizontalConfidence: UInt32
    HeadingConfidence: UInt32
    AltitudeConfidence: UInt32
    SpeedConfidence: UInt32
    PositionDilutionOfPrecision: Double
    HorizontalDilutionOfPrecision: Double
    VerticalDilutionOfPrecision: Double
    GeometricDilutionOfPrecision: Double
    TimeDilutionOfPrecision: Double
class GNSS_FIXDATA_BASIC(Structure):
    Size: UInt32
    Version: UInt32
    Latitude: Double
    Longitude: Double
    Altitude: Double
    Speed: Double
    Heading: Double
class GNSS_FIXDATA_BASIC_2(Structure):
    Size: UInt32
    Version: UInt32
    Latitude: Double
    Longitude: Double
    Altitude: Double
    Speed: Double
    Heading: Double
    AltitudeEllipsoid: Double
class GNSS_FIXDATA_SATELLITE(Structure):
    Size: UInt32
    Version: UInt32
    SatelliteCount: UInt32
    SatelliteArray: Windows.Win32.Devices.Geolocation.GNSS_SATELLITEINFO * 64
GNSS_FIXSESSIONTYPE = Int32
GNSS_FixSession_SingleShot: GNSS_FIXSESSIONTYPE = 1
GNSS_FixSession_DistanceTracking: GNSS_FIXSESSIONTYPE = 2
GNSS_FixSession_ContinuousTracking: GNSS_FIXSESSIONTYPE = 3
GNSS_FixSession_LKG: GNSS_FIXSESSIONTYPE = 4
class GNSS_FIXSESSION_PARAM(Structure):
    Size: UInt32
    Version: UInt32
    FixSessionID: UInt32
    SessionType: Windows.Win32.Devices.Geolocation.GNSS_FIXSESSIONTYPE
    HorizontalAccuracy: UInt32
    HorizontalConfidence: UInt32
    Reserved: UInt32 * 9
    FixLevelOfDetails: UInt32
    Anonymous: _Anonymous_e__Union
    Unused: Byte * 256
    class _Anonymous_e__Union(Union):
        SingleShotParam: Windows.Win32.Devices.Geolocation.GNSS_SINGLESHOT_PARAM
        DistanceParam: Windows.Win32.Devices.Geolocation.GNSS_DISTANCETRACKING_PARAM
        ContinuousParam: Windows.Win32.Devices.Geolocation.GNSS_CONTINUOUSTRACKING_PARAM
        LkgFixParam: Windows.Win32.Devices.Geolocation.GNSS_LKGFIX_PARAM
        UnusedParam: Byte * 268
class GNSS_GEOFENCES_TRACKINGSTATUS_DATA(Structure):
    Size: UInt32
    Version: UInt32
    Status: Windows.Win32.Foundation.NTSTATUS
    StatusTimeStamp: Windows.Win32.Foundation.FILETIME
    Unused: Byte * 512
class GNSS_GEOFENCE_ALERT_DATA(Structure):
    Size: UInt32
    Version: UInt32
    GeofenceID: UInt32
    GeofenceState: Windows.Win32.Devices.Geolocation.GNSS_GEOFENCE_STATE
    FixBasicData: Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_BASIC
    FixAccuracyData: Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_ACCURACY
    Unused: Byte * 512
class GNSS_GEOFENCE_CREATE_PARAM(Structure):
    Size: UInt32
    Version: UInt32
    AlertTypes: UInt32
    InitialState: Windows.Win32.Devices.Geolocation.GNSS_GEOFENCE_STATE
    Boundary: Windows.Win32.Devices.Geolocation.GNSS_GEOREGION
    Unused: Byte * 512
class GNSS_GEOFENCE_CREATE_RESPONSE(Structure):
    Size: UInt32
    Version: UInt32
    CreationStatus: Windows.Win32.Foundation.NTSTATUS
    GeofenceID: UInt32
    Unused: Byte * 512
class GNSS_GEOFENCE_DELETE_PARAM(Structure):
    Size: UInt32
    Version: UInt32
    GeofenceID: UInt32
    Unused: Byte * 512
GNSS_GEOFENCE_STATE = Int32
GNSS_GeofenceState_Unknown: GNSS_GEOFENCE_STATE = 0
GNSS_GeofenceState_Entered: GNSS_GEOFENCE_STATE = 1
GNSS_GeofenceState_Exited: GNSS_GEOFENCE_STATE = 2
class GNSS_GEOREGION(Structure):
    Size: UInt32
    Version: UInt32
    GeoRegionType: Windows.Win32.Devices.Geolocation.GNSS_GEOREGIONTYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Circle: Windows.Win32.Devices.Geolocation.GNSS_GEOREGION_CIRCLE
        Unused: Byte * 512
GNSS_GEOREGIONTYPE = Int32
GNSS_GeoRegion_Circle: GNSS_GEOREGIONTYPE = 1
class GNSS_GEOREGION_CIRCLE(Structure):
    Latitude: Double
    Longitude: Double
    RadiusInMeters: Double
class GNSS_LKGFIX_PARAM(Structure):
    Size: UInt32
    Version: UInt32
GNSS_NI_NOTIFICATION_TYPE = Int32
GNSS_NI_NoNotifyNoVerify: GNSS_NI_NOTIFICATION_TYPE = 1
GNSS_NI_NotifyOnly: GNSS_NI_NOTIFICATION_TYPE = 2
GNSS_NI_NotifyVerifyDefaultAllow: GNSS_NI_NOTIFICATION_TYPE = 3
GNSS_NI_NotifyVerifyDefaultNotAllow: GNSS_NI_NOTIFICATION_TYPE = 4
GNSS_NI_PrivacyOverride: GNSS_NI_NOTIFICATION_TYPE = 5
GNSS_NI_PLANE_TYPE = Int32
GNSS_NI_SUPL: GNSS_NI_PLANE_TYPE = 1
GNSS_NI_CP: GNSS_NI_PLANE_TYPE = 2
GNSS_NI_V2UPL: GNSS_NI_PLANE_TYPE = 3
class GNSS_NI_REQUEST_PARAM(Structure):
    Size: UInt32
    Version: UInt32
    RequestId: UInt32
    RequestType: Windows.Win32.Devices.Geolocation.GNSS_NI_REQUEST_TYPE
    NotificationType: Windows.Win32.Devices.Geolocation.GNSS_NI_NOTIFICATION_TYPE
    RequestPlaneType: Windows.Win32.Devices.Geolocation.GNSS_NI_PLANE_TYPE
    Anonymous: _Anonymous_e__Union
    ResponseTimeInSec: UInt32
    EmergencyLocation: Windows.Win32.Foundation.BOOL
    class _Anonymous_e__Union(Union):
        SuplNiInfo: Windows.Win32.Devices.Geolocation.GNSS_SUPL_NI_INFO
        CpNiInfo: Windows.Win32.Devices.Geolocation.GNSS_CP_NI_INFO
        V2UplNiInfo: Windows.Win32.Devices.Geolocation.GNSS_V2UPL_NI_INFO
GNSS_NI_REQUEST_TYPE = Int32
GNSS_NI_Request_SingleShot: GNSS_NI_REQUEST_TYPE = 1
GNSS_NI_Request_AreaTrigger: GNSS_NI_REQUEST_TYPE = 2
class GNSS_NI_RESPONSE(Structure):
    Size: UInt32
    Version: UInt32
    RequestId: UInt32
    UserResponse: Windows.Win32.Devices.Geolocation.GNSS_NI_USER_RESPONSE
GNSS_NI_USER_RESPONSE = Int32
GNSS_Ni_UserResponseAccept: GNSS_NI_USER_RESPONSE = 1
GNSS_Ni_UserResponseDeny: GNSS_NI_USER_RESPONSE = 2
GNSS_Ni_UserResponseTimeout: GNSS_NI_USER_RESPONSE = 3
class GNSS_NMEA_DATA(Structure):
    Size: UInt32
    Version: UInt32
    NmeaSentences: Windows.Win32.Foundation.CHAR * 256
class GNSS_PLATFORM_CAPABILITY(Structure):
    Size: UInt32
    Version: UInt32
    SupportAgnssInjection: Windows.Win32.Foundation.BOOL
    AgnssFormatSupported: UInt32
    Unused: Byte * 516
class GNSS_SATELLITEINFO(Structure):
    SatelliteId: UInt32
    UsedInPositiong: Windows.Win32.Foundation.BOOL
    Elevation: Double
    Azimuth: Double
    SignalToNoiseRatio: Double
class GNSS_SELFTESTCONFIG(Structure):
    Size: UInt32
    Version: UInt32
    TestType: UInt32
    Unused: Byte * 512
    InBufLen: UInt32
    InBuffer: Byte * 1
class GNSS_SELFTESTRESULT(Structure):
    Size: UInt32
    Version: UInt32
    TestResultStatus: Windows.Win32.Foundation.NTSTATUS
    Result: UInt32
    PinFailedBitMask: UInt32
    Unused: Byte * 512
    OutBufLen: UInt32
    OutBuffer: Byte * 1
class GNSS_SINGLESHOT_PARAM(Structure):
    Size: UInt32
    Version: UInt32
    ResponseTime: UInt32
class GNSS_STOPFIXSESSION_PARAM(Structure):
    Size: UInt32
    Version: UInt32
    FixSessionID: UInt32
    Unused: Byte * 512
GNSS_SUPL_CERT_ACTION = Int32
GNSS_Supl_Cert_Inject: GNSS_SUPL_CERT_ACTION = 1
GNSS_Supl_Cert_Delete: GNSS_SUPL_CERT_ACTION = 2
GNSS_Supl_Cert_Purge: GNSS_SUPL_CERT_ACTION = 3
class GNSS_SUPL_CERT_CONFIG(Structure):
    Size: UInt32
    Version: UInt32
    CertAction: Windows.Win32.Devices.Geolocation.GNSS_SUPL_CERT_ACTION
    SuplCertName: Windows.Win32.Foundation.CHAR * 260
    CertSize: UInt32
    Unused: Byte * 512
    CertData: Byte * 1
class GNSS_SUPL_HSLP_CONFIG(Structure):
    Size: UInt32
    Version: UInt32
    SuplHslp: Windows.Win32.Foundation.CHAR * 260
    SuplHslpFromImsi: Windows.Win32.Foundation.CHAR * 260
    Reserved: UInt32
    Unused: Byte * 512
class GNSS_SUPL_NI_INFO(Structure):
    Size: UInt32
    Version: UInt32
    RequestorId: Char * 260
    ClientName: Char * 260
    SuplNiUrl: Windows.Win32.Foundation.CHAR * 260
class GNSS_SUPL_VERSION(Structure):
    MajorVersion: UInt32
    MinorVersion: UInt32
class GNSS_SUPL_VERSION_2(Structure):
    MajorVersion: UInt32
    MinorVersion: UInt32
    ServiceIndicator: UInt32
class GNSS_V2UPL_CONFIG(Structure):
    Size: UInt32
    Version: UInt32
    MPC: Windows.Win32.Foundation.CHAR * 260
    PDE: Windows.Win32.Foundation.CHAR * 260
    ApplicationTypeIndicator_MR: Byte
    Unused: Byte * 512
class GNSS_V2UPL_NI_INFO(Structure):
    Size: UInt32
    Version: UInt32
    RequestorId: Char * 260
class ICivicAddressReport(c_void_p):
    extends: Windows.Win32.Devices.Geolocation.ILocationReport
    Guid = Guid('c0b19f70-4adf-445d-87-f2-ca-d8-fd-71-17-92')
    @commethod(6)
    def GetAddressLine1(pbstrAddress1: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAddressLine2(pbstrAddress2: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCity(pbstrCity: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStateProvince(pbstrStateProvince: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPostalCode(pbstrPostalCode: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCountryRegion(pbstrCountryRegion: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDetailLevel(pDetailLevel: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ICivicAddressReportFactory(c_void_p):
    extends: Windows.Win32.Devices.Geolocation.ILocationReportFactory
    Guid = Guid('bf773b93-c64f-4bee-be-b2-67-c0-b8-df-66-e0')
    @commethod(15)
    def get_CivicAddressReport(pVal: POINTER(Windows.Win32.Devices.Geolocation.IDispCivicAddressReport_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDefaultLocation(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a65af77e-969a-4a2e-8a-ca-33-bb-7c-bb-12-35')
    @commethod(3)
    def SetReport(reportType: POINTER(Guid), pLocationReport: Windows.Win32.Devices.Geolocation.ILocationReport_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetReport(reportType: POINTER(Guid), ppLocationReport: POINTER(Windows.Win32.Devices.Geolocation.ILocationReport_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDispCivicAddressReport(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('16ff1a34-9e30-42c3-b4-4d-e2-25-13-b5-76-7a')
    @commethod(7)
    def get_AddressLine1(pAddress1: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AddressLine2(pAddress2: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_City(pCity: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_StateProvince(pStateProvince: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PostalCode(pPostalCode: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CountryRegion(pCountryRegion: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_DetailLevel(pDetailLevel: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Timestamp(pVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
class IDispLatLongReport(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('8ae32723-389b-4a11-99-57-5b-dd-48-fc-96-17')
    @commethod(7)
    def get_Latitude(pVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Longitude(pVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ErrorRadius(pVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Altitude(pVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_AltitudeError(pVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Timestamp(pVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
class ILatLongReport(c_void_p):
    extends: Windows.Win32.Devices.Geolocation.ILocationReport
    Guid = Guid('7fed806d-0ef8-4f07-80-ac-36-a0-be-ae-31-34')
    @commethod(6)
    def GetLatitude(pLatitude: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLongitude(pLongitude: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetErrorRadius(pErrorRadius: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAltitude(pAltitude: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetAltitudeError(pAltitudeError: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
class ILatLongReportFactory(c_void_p):
    extends: Windows.Win32.Devices.Geolocation.ILocationReportFactory
    Guid = Guid('3f0804cb-b114-447d-83-dd-39-01-74-eb-b0-82')
    @commethod(15)
    def get_LatLongReport(pVal: POINTER(Windows.Win32.Devices.Geolocation.IDispLatLongReport_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ILocation(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ab2ece69-56d9-4f28-b5-25-de-1b-0e-e4-42-37')
    @commethod(3)
    def RegisterForReport(pEvents: Windows.Win32.Devices.Geolocation.ILocationEvents_head, reportType: POINTER(Guid), dwRequestedReportInterval: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterForReport(reportType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetReport(reportType: POINTER(Guid), ppLocationReport: POINTER(Windows.Win32.Devices.Geolocation.ILocationReport_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetReportStatus(reportType: POINTER(Guid), pStatus: POINTER(Windows.Win32.Devices.Geolocation.LOCATION_REPORT_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetReportInterval(reportType: POINTER(Guid), pMilliseconds: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetReportInterval(reportType: POINTER(Guid), millisecondsRequested: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDesiredAccuracy(reportType: POINTER(Guid), pDesiredAccuracy: POINTER(Windows.Win32.Devices.Sensors.LOCATION_DESIRED_ACCURACY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetDesiredAccuracy(reportType: POINTER(Guid), desiredAccuracy: Windows.Win32.Devices.Sensors.LOCATION_DESIRED_ACCURACY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RequestPermissions(hParent: Windows.Win32.Foundation.HWND, pReportTypes: POINTER(Guid), count: UInt32, fModal: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ILocationEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('cae02bbf-798b-4508-a2-07-35-a7-90-6d-c7-3d')
    @commethod(3)
    def OnLocationChanged(reportType: POINTER(Guid), pLocationReport: Windows.Win32.Devices.Geolocation.ILocationReport_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnStatusChanged(reportType: POINTER(Guid), newStatus: Windows.Win32.Devices.Geolocation.LOCATION_REPORT_STATUS) -> Windows.Win32.Foundation.HRESULT: ...
class ILocationPower(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('193e7729-ab6b-4b12-86-17-75-96-e1-bb-19-1c')
    @commethod(3)
    def Connect() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Disconnect() -> Windows.Win32.Foundation.HRESULT: ...
class ILocationReport(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c8b7f7ee-75d0-4db9-b6-2d-7a-0f-36-9c-a4-56')
    @commethod(3)
    def GetSensorID(pSensorID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTimestamp(pCreationTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetValue(pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ILocationReportFactory(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('2daec322-90b2-47e4-bb-08-0d-a8-41-93-5a-6b')
    @commethod(7)
    def ListenForReports(requestedReportInterval: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def StopListeningForReports() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Status(pVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ReportInterval(pMilliseconds: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_ReportInterval(millisecondsRequested: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_DesiredAccuracy(pDesiredAccuracy: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_DesiredAccuracy(desiredAccuracy: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RequestPermissions(hWnd: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
LOCATION_REPORT_STATUS = Int32
REPORT_NOT_SUPPORTED: LOCATION_REPORT_STATUS = 0
REPORT_ERROR: LOCATION_REPORT_STATUS = 1
REPORT_ACCESS_DENIED: LOCATION_REPORT_STATUS = 2
REPORT_INITIALIZING: LOCATION_REPORT_STATUS = 3
REPORT_RUNNING: LOCATION_REPORT_STATUS = 4
LatLongReport = Guid('ed81c073-1f84-4ca8-a1-61-18-3c-77-6b-c6-51')
LatLongReportFactory = Guid('9dcc3cc8-8609-4863-ba-d4-03-60-1f-4c-65-e8')
Location = Guid('e5b8e079-ee6d-4e33-a4-38-c8-7f-2e-95-92-54')
class _ICivicAddressReportFactoryEvents(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('c96039ff-72ec-4617-89-bd-84-d8-8b-ed-c7-22')
class _ILatLongReportFactoryEvents(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('16ee6cb7-ab3c-424b-84-9f-26-9b-e5-51-fc-bc')
make_head(_module, 'GNSS_AGNSS_INJECT')
make_head(_module, 'GNSS_AGNSS_INJECTBLOB')
make_head(_module, 'GNSS_AGNSS_INJECTPOSITION')
make_head(_module, 'GNSS_AGNSS_INJECTTIME')
make_head(_module, 'GNSS_AGNSS_REQUEST_PARAM')
make_head(_module, 'GNSS_BREADCRUMBING_ALERT_DATA')
make_head(_module, 'GNSS_BREADCRUMBING_PARAM')
make_head(_module, 'GNSS_BREADCRUMB_LIST')
make_head(_module, 'GNSS_BREADCRUMB_V1')
make_head(_module, 'GNSS_CHIPSETINFO')
make_head(_module, 'GNSS_CONTINUOUSTRACKING_PARAM')
make_head(_module, 'GNSS_CP_NI_INFO')
make_head(_module, 'GNSS_CWTESTDATA')
make_head(_module, 'GNSS_DEVICE_CAPABILITY')
make_head(_module, 'GNSS_DISTANCETRACKING_PARAM')
make_head(_module, 'GNSS_DRIVERCOMMAND_PARAM')
make_head(_module, 'GNSS_DRIVER_REQUEST_DATA')
make_head(_module, 'GNSS_ERRORINFO')
make_head(_module, 'GNSS_EVENT')
make_head(_module, 'GNSS_EVENT_2')
make_head(_module, 'GNSS_FIXDATA')
make_head(_module, 'GNSS_FIXDATA_2')
make_head(_module, 'GNSS_FIXDATA_ACCURACY')
make_head(_module, 'GNSS_FIXDATA_ACCURACY_2')
make_head(_module, 'GNSS_FIXDATA_BASIC')
make_head(_module, 'GNSS_FIXDATA_BASIC_2')
make_head(_module, 'GNSS_FIXDATA_SATELLITE')
make_head(_module, 'GNSS_FIXSESSION_PARAM')
make_head(_module, 'GNSS_GEOFENCES_TRACKINGSTATUS_DATA')
make_head(_module, 'GNSS_GEOFENCE_ALERT_DATA')
make_head(_module, 'GNSS_GEOFENCE_CREATE_PARAM')
make_head(_module, 'GNSS_GEOFENCE_CREATE_RESPONSE')
make_head(_module, 'GNSS_GEOFENCE_DELETE_PARAM')
make_head(_module, 'GNSS_GEOREGION')
make_head(_module, 'GNSS_GEOREGION_CIRCLE')
make_head(_module, 'GNSS_LKGFIX_PARAM')
make_head(_module, 'GNSS_NI_REQUEST_PARAM')
make_head(_module, 'GNSS_NI_RESPONSE')
make_head(_module, 'GNSS_NMEA_DATA')
make_head(_module, 'GNSS_PLATFORM_CAPABILITY')
make_head(_module, 'GNSS_SATELLITEINFO')
make_head(_module, 'GNSS_SELFTESTCONFIG')
make_head(_module, 'GNSS_SELFTESTRESULT')
make_head(_module, 'GNSS_SINGLESHOT_PARAM')
make_head(_module, 'GNSS_STOPFIXSESSION_PARAM')
make_head(_module, 'GNSS_SUPL_CERT_CONFIG')
make_head(_module, 'GNSS_SUPL_HSLP_CONFIG')
make_head(_module, 'GNSS_SUPL_NI_INFO')
make_head(_module, 'GNSS_SUPL_VERSION')
make_head(_module, 'GNSS_SUPL_VERSION_2')
make_head(_module, 'GNSS_V2UPL_CONFIG')
make_head(_module, 'GNSS_V2UPL_NI_INFO')
make_head(_module, 'ICivicAddressReport')
make_head(_module, 'ICivicAddressReportFactory')
make_head(_module, 'IDefaultLocation')
make_head(_module, 'IDispCivicAddressReport')
make_head(_module, 'IDispLatLongReport')
make_head(_module, 'ILatLongReport')
make_head(_module, 'ILatLongReportFactory')
make_head(_module, 'ILocation')
make_head(_module, 'ILocationEvents')
make_head(_module, 'ILocationPower')
make_head(_module, 'ILocationReport')
make_head(_module, 'ILocationReportFactory')
make_head(_module, '_ICivicAddressReportFactoryEvents')
make_head(_module, '_ILatLongReportFactoryEvents')
__all__ = [
    "BREADCRUMBING_UNSUPPORTED",
    "BREADCRUMBING_VERSION_1",
    "CivicAddressReport",
    "CivicAddressReportFactory",
    "DefaultLocation",
    "DispCivicAddressReport",
    "DispLatLongReport",
    "GNSS_AGNSSFORMAT_LTO",
    "GNSS_AGNSSFORMAT_XTRA1",
    "GNSS_AGNSSFORMAT_XTRA2",
    "GNSS_AGNSSFORMAT_XTRA3",
    "GNSS_AGNSSFORMAT_XTRA3_1",
    "GNSS_AGNSSFORMAT_XTRA3_2",
    "GNSS_AGNSSFORMAT_XTRA_INT",
    "GNSS_AGNSS_BlobInjection",
    "GNSS_AGNSS_INJECT",
    "GNSS_AGNSS_INJECTBLOB",
    "GNSS_AGNSS_INJECTPOSITION",
    "GNSS_AGNSS_INJECTTIME",
    "GNSS_AGNSS_PositionInjection",
    "GNSS_AGNSS_REQUEST_PARAM",
    "GNSS_AGNSS_REQUEST_TYPE",
    "GNSS_AGNSS_TimeInjection",
    "GNSS_BREADCRUMBING_ALERT_DATA",
    "GNSS_BREADCRUMBING_PARAM",
    "GNSS_BREADCRUMB_LIST",
    "GNSS_BREADCRUMB_V1",
    "GNSS_CHIPSETINFO",
    "GNSS_CONTINUOUSTRACKING_PARAM",
    "GNSS_CP_NI_INFO",
    "GNSS_CWTESTDATA",
    "GNSS_ClearAgnssData",
    "GNSS_CustomCommand",
    "GNSS_DEVICE_CAPABILITY",
    "GNSS_DISTANCETRACKING_PARAM",
    "GNSS_DRIVERCOMMAND_PARAM",
    "GNSS_DRIVERCOMMAND_TYPE",
    "GNSS_DRIVER_REQUEST",
    "GNSS_DRIVER_REQUEST_DATA",
    "GNSS_DRIVER_VERSION_1",
    "GNSS_DRIVER_VERSION_2",
    "GNSS_DRIVER_VERSION_3",
    "GNSS_DRIVER_VERSION_4",
    "GNSS_DRIVER_VERSION_5",
    "GNSS_DRIVER_VERSION_6",
    "GNSS_ERRORINFO",
    "GNSS_EVENT",
    "GNSS_EVENT_2",
    "GNSS_EVENT_TYPE",
    "GNSS_Event_BreadcrumbAlertEvent",
    "GNSS_Event_Custom",
    "GNSS_Event_DriverRequest",
    "GNSS_Event_Error",
    "GNSS_Event_FixAvailable",
    "GNSS_Event_FixAvailable_2",
    "GNSS_Event_GeofenceAlertData",
    "GNSS_Event_GeofencesTrackingStatus",
    "GNSS_Event_NiRequest",
    "GNSS_Event_NmeaData",
    "GNSS_Event_RequireAgnss",
    "GNSS_FIXDATA",
    "GNSS_FIXDATA_2",
    "GNSS_FIXDATA_ACCURACY",
    "GNSS_FIXDATA_ACCURACY_2",
    "GNSS_FIXDATA_BASIC",
    "GNSS_FIXDATA_BASIC_2",
    "GNSS_FIXDATA_SATELLITE",
    "GNSS_FIXDETAIL_ACCURACY",
    "GNSS_FIXDETAIL_BASIC",
    "GNSS_FIXDETAIL_SATELLITE",
    "GNSS_FIXSESSIONTYPE",
    "GNSS_FIXSESSION_PARAM",
    "GNSS_FixSession_ContinuousTracking",
    "GNSS_FixSession_DistanceTracking",
    "GNSS_FixSession_LKG",
    "GNSS_FixSession_SingleShot",
    "GNSS_ForceOperationMode",
    "GNSS_ForceSatelliteSystem",
    "GNSS_GEOFENCESUPPORT_CIRCLE",
    "GNSS_GEOFENCESUPPORT_SUPPORTED",
    "GNSS_GEOFENCES_TRACKINGSTATUS_DATA",
    "GNSS_GEOFENCE_ALERT_DATA",
    "GNSS_GEOFENCE_CREATE_PARAM",
    "GNSS_GEOFENCE_CREATE_RESPONSE",
    "GNSS_GEOFENCE_DELETE_PARAM",
    "GNSS_GEOFENCE_STATE",
    "GNSS_GEOREGION",
    "GNSS_GEOREGIONTYPE",
    "GNSS_GEOREGION_CIRCLE",
    "GNSS_GeoRegion_Circle",
    "GNSS_GeofenceState_Entered",
    "GNSS_GeofenceState_Exited",
    "GNSS_GeofenceState_Unknown",
    "GNSS_LKGFIX_PARAM",
    "GNSS_MAXSATELLITE",
    "GNSS_NI_CP",
    "GNSS_NI_NOTIFICATION_TYPE",
    "GNSS_NI_NoNotifyNoVerify",
    "GNSS_NI_NotifyOnly",
    "GNSS_NI_NotifyVerifyDefaultAllow",
    "GNSS_NI_NotifyVerifyDefaultNotAllow",
    "GNSS_NI_PLANE_TYPE",
    "GNSS_NI_PrivacyOverride",
    "GNSS_NI_REQUEST_PARAM",
    "GNSS_NI_REQUEST_TYPE",
    "GNSS_NI_RESPONSE",
    "GNSS_NI_Request_AreaTrigger",
    "GNSS_NI_Request_SingleShot",
    "GNSS_NI_SUPL",
    "GNSS_NI_USER_RESPONSE",
    "GNSS_NI_V2UPL",
    "GNSS_NMEALOGGING_ALL",
    "GNSS_NMEALOGGING_NONE",
    "GNSS_NMEA_DATA",
    "GNSS_Ni_UserResponseAccept",
    "GNSS_Ni_UserResponseDeny",
    "GNSS_Ni_UserResponseTimeout",
    "GNSS_OPERMODE_AFLT",
    "GNSS_OPERMODE_ANY",
    "GNSS_OPERMODE_CELLID",
    "GNSS_OPERMODE_MSA",
    "GNSS_OPERMODE_MSB",
    "GNSS_OPERMODE_MSS",
    "GNSS_OPERMODE_OTDOA",
    "GNSS_PLATFORM_CAPABILITY",
    "GNSS_ResetEngine",
    "GNSS_ResetGeofencesTracking",
    "GNSS_SATELLITEINFO",
    "GNSS_SATELLITE_ANY",
    "GNSS_SATELLITE_BEIDOU",
    "GNSS_SATELLITE_GALILEO",
    "GNSS_SATELLITE_GLONASS",
    "GNSS_SATELLITE_GPS",
    "GNSS_SELFTESTCONFIG",
    "GNSS_SELFTESTRESULT",
    "GNSS_SINGLESHOT_PARAM",
    "GNSS_STOPFIXSESSION_PARAM",
    "GNSS_SUPL_CERT_ACTION",
    "GNSS_SUPL_CERT_CONFIG",
    "GNSS_SUPL_HSLP_CONFIG",
    "GNSS_SUPL_NI_INFO",
    "GNSS_SUPL_VERSION",
    "GNSS_SUPL_VERSION_2",
    "GNSS_SetLocationNIRequestAllowed",
    "GNSS_SetLocationServiceEnabled",
    "GNSS_SetNMEALogging",
    "GNSS_SetNiTimeoutInterval",
    "GNSS_SetSuplVersion",
    "GNSS_SetSuplVersion2",
    "GNSS_SetUplServerAccessInterval",
    "GNSS_Supl_Cert_Delete",
    "GNSS_Supl_Cert_Inject",
    "GNSS_Supl_Cert_Purge",
    "GNSS_V2UPL_CONFIG",
    "GNSS_V2UPL_NI_INFO",
    "GUID_DEVINTERFACE_GNSS",
    "ICivicAddressReport",
    "ICivicAddressReportFactory",
    "IDefaultLocation",
    "IDispCivicAddressReport",
    "IDispLatLongReport",
    "ILatLongReport",
    "ILatLongReportFactory",
    "ILocation",
    "ILocationEvents",
    "ILocationPower",
    "ILocationReport",
    "ILocationReportFactory",
    "IOCTL_GNSS_CONFIG_SUPL_CERT",
    "IOCTL_GNSS_CREATE_GEOFENCE",
    "IOCTL_GNSS_DELETE_GEOFENCE",
    "IOCTL_GNSS_EXECUTE_CWTEST",
    "IOCTL_GNSS_EXECUTE_SELFTEST",
    "IOCTL_GNSS_GET_CHIPSETINFO",
    "IOCTL_GNSS_GET_DEVICE_CAPABILITY",
    "IOCTL_GNSS_GET_FIXDATA",
    "IOCTL_GNSS_INJECT_AGNSS",
    "IOCTL_GNSS_LISTEN_AGNSS",
    "IOCTL_GNSS_LISTEN_BREADCRUMBING_ALERT",
    "IOCTL_GNSS_LISTEN_DRIVER_REQUEST",
    "IOCTL_GNSS_LISTEN_ERROR",
    "IOCTL_GNSS_LISTEN_GEOFENCES_TRACKINGSTATUS",
    "IOCTL_GNSS_LISTEN_GEOFENCE_ALERT",
    "IOCTL_GNSS_LISTEN_NI",
    "IOCTL_GNSS_LISTEN_NMEA",
    "IOCTL_GNSS_MODIFY_FIXSESSION",
    "IOCTL_GNSS_POP_BREADCRUMBS",
    "IOCTL_GNSS_RESPOND_NI",
    "IOCTL_GNSS_SEND_DRIVERCOMMAND",
    "IOCTL_GNSS_SEND_PLATFORM_CAPABILITY",
    "IOCTL_GNSS_SET_SUPL_HSLP",
    "IOCTL_GNSS_SET_V2UPL_CONFIG",
    "IOCTL_GNSS_START_BREADCRUMBING",
    "IOCTL_GNSS_START_FIXSESSION",
    "IOCTL_GNSS_STOP_BREADCRUMBING",
    "IOCTL_GNSS_STOP_FIXSESSION",
    "LOCATION_API_VERSION",
    "LOCATION_REPORT_STATUS",
    "LatLongReport",
    "LatLongReportFactory",
    "Location",
    "MAX_SERVER_URL_NAME",
    "MIN_BREADCRUMBS_SUPPORTED",
    "MIN_GEOFENCES_REQUIRED",
    "REPORT_ACCESS_DENIED",
    "REPORT_ERROR",
    "REPORT_INITIALIZING",
    "REPORT_NOT_SUPPORTED",
    "REPORT_RUNNING",
    "SUPL_CONFIG_DATA",
    "_ICivicAddressReportFactoryEvents",
    "_ILatLongReportFactoryEvents",
]
_arch_optional = [
]
