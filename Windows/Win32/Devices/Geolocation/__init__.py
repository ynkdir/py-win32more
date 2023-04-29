from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
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
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
class GNSS_AGNSS_INJECT(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    InjectionType: Windows.Win32.Devices.Geolocation.GNSS_AGNSS_REQUEST_TYPE
    InjectionStatus: Windows.Win32.Foundation.NTSTATUS
    InjectionDataSize: UInt32
    Unused: Byte * 512
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Time: Windows.Win32.Devices.Geolocation.GNSS_AGNSS_INJECTTIME
        Position: Windows.Win32.Devices.Geolocation.GNSS_AGNSS_INJECTPOSITION
        BlobData: Windows.Win32.Devices.Geolocation.GNSS_AGNSS_INJECTBLOB
class GNSS_AGNSS_INJECTBLOB(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    BlobOui: UInt32
    BlobVersion: UInt32
    AgnssFormat: UInt32
    BlobSize: UInt32
    BlobData: Byte * 1
class GNSS_AGNSS_INJECTPOSITION(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    Age: UInt32
    BasicData: Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_BASIC
    AccuracyData: Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_ACCURACY
class GNSS_AGNSS_INJECTTIME(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    UtcTime: Windows.Win32.Foundation.FILETIME
    TimeUncertainty: UInt32
class GNSS_AGNSS_REQUEST_PARAM(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    RequestType: Windows.Win32.Devices.Geolocation.GNSS_AGNSS_REQUEST_TYPE
    BlobFormat: UInt32
GNSS_AGNSS_REQUEST_TYPE = Int32
GNSS_AGNSS_TimeInjection: GNSS_AGNSS_REQUEST_TYPE = 1
GNSS_AGNSS_PositionInjection: GNSS_AGNSS_REQUEST_TYPE = 2
GNSS_AGNSS_BlobInjection: GNSS_AGNSS_REQUEST_TYPE = 3
class GNSS_BREADCRUMBING_ALERT_DATA(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    Unused: Byte * 512
class GNSS_BREADCRUMBING_PARAM(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    MaximumHorizontalUncertainty: UInt32
    MinDistanceBetweenFixes: UInt32
    MaximumErrorTimeoutMs: UInt32
    Unused: Byte * 512
class GNSS_BREADCRUMB_LIST(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    NumCrumbs: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        v1: Windows.Win32.Devices.Geolocation.GNSS_BREADCRUMB_V1 * 50
class GNSS_BREADCRUMB_V1(EasyCastStructure):
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
class GNSS_CHIPSETINFO(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    ManufacturerID: Char * 25
    HardwareID: Char * 25
    FirmwareVersion: Char * 20
    Unused: Byte * 512
class GNSS_CONTINUOUSTRACKING_PARAM(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    PreferredInterval: UInt32
class GNSS_CP_NI_INFO(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    RequestorId: Char * 260
    NotificationText: Char * 260
class GNSS_CWTESTDATA(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    TestResultStatus: Windows.Win32.Foundation.NTSTATUS
    SignalToNoiseRatio: Double
    Frequency: Double
    Unused: Byte * 512
class GNSS_DEVICE_CAPABILITY(EasyCastStructure):
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
class GNSS_DISTANCETRACKING_PARAM(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    MovementThreshold: UInt32
class GNSS_DRIVERCOMMAND_PARAM(EasyCastStructure):
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
class GNSS_DRIVER_REQUEST_DATA(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    Request: Windows.Win32.Devices.Geolocation.GNSS_DRIVER_REQUEST
    RequestFlag: UInt32
class GNSS_ERRORINFO(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    ErrorCode: UInt32
    IsRecoverable: Windows.Win32.Foundation.BOOL
    ErrorDescription: Char * 256
    Unused: Byte * 512
class GNSS_EVENT(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    EventType: Windows.Win32.Devices.Geolocation.GNSS_EVENT_TYPE
    EventDataSize: UInt32
    Unused: Byte * 512
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
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
class GNSS_EVENT_2(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    EventType: Windows.Win32.Devices.Geolocation.GNSS_EVENT_TYPE
    EventDataSize: UInt32
    Unused: Byte * 512
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
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
class GNSS_FIXDATA(EasyCastStructure):
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
class GNSS_FIXDATA_2(EasyCastStructure):
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
class GNSS_FIXDATA_ACCURACY(EasyCastStructure):
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
class GNSS_FIXDATA_ACCURACY_2(EasyCastStructure):
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
class GNSS_FIXDATA_BASIC(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    Latitude: Double
    Longitude: Double
    Altitude: Double
    Speed: Double
    Heading: Double
class GNSS_FIXDATA_BASIC_2(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    Latitude: Double
    Longitude: Double
    Altitude: Double
    Speed: Double
    Heading: Double
    AltitudeEllipsoid: Double
class GNSS_FIXDATA_SATELLITE(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    SatelliteCount: UInt32
    SatelliteArray: Windows.Win32.Devices.Geolocation.GNSS_SATELLITEINFO * 64
GNSS_FIXSESSIONTYPE = Int32
GNSS_FixSession_SingleShot: GNSS_FIXSESSIONTYPE = 1
GNSS_FixSession_DistanceTracking: GNSS_FIXSESSIONTYPE = 2
GNSS_FixSession_ContinuousTracking: GNSS_FIXSESSIONTYPE = 3
GNSS_FixSession_LKG: GNSS_FIXSESSIONTYPE = 4
class GNSS_FIXSESSION_PARAM(EasyCastStructure):
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
    class _Anonymous_e__Union(EasyCastUnion):
        SingleShotParam: Windows.Win32.Devices.Geolocation.GNSS_SINGLESHOT_PARAM
        DistanceParam: Windows.Win32.Devices.Geolocation.GNSS_DISTANCETRACKING_PARAM
        ContinuousParam: Windows.Win32.Devices.Geolocation.GNSS_CONTINUOUSTRACKING_PARAM
        LkgFixParam: Windows.Win32.Devices.Geolocation.GNSS_LKGFIX_PARAM
        UnusedParam: Byte * 268
class GNSS_GEOFENCES_TRACKINGSTATUS_DATA(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    Status: Windows.Win32.Foundation.NTSTATUS
    StatusTimeStamp: Windows.Win32.Foundation.FILETIME
    Unused: Byte * 512
class GNSS_GEOFENCE_ALERT_DATA(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    GeofenceID: UInt32
    GeofenceState: Windows.Win32.Devices.Geolocation.GNSS_GEOFENCE_STATE
    FixBasicData: Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_BASIC
    FixAccuracyData: Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_ACCURACY
    Unused: Byte * 512
class GNSS_GEOFENCE_CREATE_PARAM(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    AlertTypes: UInt32
    InitialState: Windows.Win32.Devices.Geolocation.GNSS_GEOFENCE_STATE
    Boundary: Windows.Win32.Devices.Geolocation.GNSS_GEOREGION
    Unused: Byte * 512
class GNSS_GEOFENCE_CREATE_RESPONSE(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    CreationStatus: Windows.Win32.Foundation.NTSTATUS
    GeofenceID: UInt32
    Unused: Byte * 512
class GNSS_GEOFENCE_DELETE_PARAM(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    GeofenceID: UInt32
    Unused: Byte * 512
GNSS_GEOFENCE_STATE = Int32
GNSS_GeofenceState_Unknown: GNSS_GEOFENCE_STATE = 0
GNSS_GeofenceState_Entered: GNSS_GEOFENCE_STATE = 1
GNSS_GeofenceState_Exited: GNSS_GEOFENCE_STATE = 2
class GNSS_GEOREGION(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    GeoRegionType: Windows.Win32.Devices.Geolocation.GNSS_GEOREGIONTYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Circle: Windows.Win32.Devices.Geolocation.GNSS_GEOREGION_CIRCLE
        Unused: Byte * 512
GNSS_GEOREGIONTYPE = Int32
GNSS_GeoRegion_Circle: GNSS_GEOREGIONTYPE = 1
class GNSS_GEOREGION_CIRCLE(EasyCastStructure):
    Latitude: Double
    Longitude: Double
    RadiusInMeters: Double
class GNSS_LKGFIX_PARAM(EasyCastStructure):
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
class GNSS_NI_REQUEST_PARAM(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    RequestId: UInt32
    RequestType: Windows.Win32.Devices.Geolocation.GNSS_NI_REQUEST_TYPE
    NotificationType: Windows.Win32.Devices.Geolocation.GNSS_NI_NOTIFICATION_TYPE
    RequestPlaneType: Windows.Win32.Devices.Geolocation.GNSS_NI_PLANE_TYPE
    Anonymous: _Anonymous_e__Union
    ResponseTimeInSec: UInt32
    EmergencyLocation: Windows.Win32.Foundation.BOOL
    class _Anonymous_e__Union(EasyCastUnion):
        SuplNiInfo: Windows.Win32.Devices.Geolocation.GNSS_SUPL_NI_INFO
        CpNiInfo: Windows.Win32.Devices.Geolocation.GNSS_CP_NI_INFO
        V2UplNiInfo: Windows.Win32.Devices.Geolocation.GNSS_V2UPL_NI_INFO
GNSS_NI_REQUEST_TYPE = Int32
GNSS_NI_Request_SingleShot: GNSS_NI_REQUEST_TYPE = 1
GNSS_NI_Request_AreaTrigger: GNSS_NI_REQUEST_TYPE = 2
class GNSS_NI_RESPONSE(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    RequestId: UInt32
    UserResponse: Windows.Win32.Devices.Geolocation.GNSS_NI_USER_RESPONSE
GNSS_NI_USER_RESPONSE = Int32
GNSS_Ni_UserResponseAccept: GNSS_NI_USER_RESPONSE = 1
GNSS_Ni_UserResponseDeny: GNSS_NI_USER_RESPONSE = 2
GNSS_Ni_UserResponseTimeout: GNSS_NI_USER_RESPONSE = 3
class GNSS_NMEA_DATA(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    NmeaSentences: Windows.Win32.Foundation.CHAR * 256
class GNSS_PLATFORM_CAPABILITY(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    SupportAgnssInjection: Windows.Win32.Foundation.BOOL
    AgnssFormatSupported: UInt32
    Unused: Byte * 516
class GNSS_SATELLITEINFO(EasyCastStructure):
    SatelliteId: UInt32
    UsedInPositiong: Windows.Win32.Foundation.BOOL
    Elevation: Double
    Azimuth: Double
    SignalToNoiseRatio: Double
class GNSS_SELFTESTCONFIG(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    TestType: UInt32
    Unused: Byte * 512
    InBufLen: UInt32
    InBuffer: Byte * 1
class GNSS_SELFTESTRESULT(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    TestResultStatus: Windows.Win32.Foundation.NTSTATUS
    Result: UInt32
    PinFailedBitMask: UInt32
    Unused: Byte * 512
    OutBufLen: UInt32
    OutBuffer: Byte * 1
class GNSS_SINGLESHOT_PARAM(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    ResponseTime: UInt32
class GNSS_STOPFIXSESSION_PARAM(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    FixSessionID: UInt32
    Unused: Byte * 512
GNSS_SUPL_CERT_ACTION = Int32
GNSS_Supl_Cert_Inject: GNSS_SUPL_CERT_ACTION = 1
GNSS_Supl_Cert_Delete: GNSS_SUPL_CERT_ACTION = 2
GNSS_Supl_Cert_Purge: GNSS_SUPL_CERT_ACTION = 3
class GNSS_SUPL_CERT_CONFIG(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    CertAction: Windows.Win32.Devices.Geolocation.GNSS_SUPL_CERT_ACTION
    SuplCertName: Windows.Win32.Foundation.CHAR * 260
    CertSize: UInt32
    Unused: Byte * 512
    CertData: Byte * 1
class GNSS_SUPL_HSLP_CONFIG(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    SuplHslp: Windows.Win32.Foundation.CHAR * 260
    SuplHslpFromImsi: Windows.Win32.Foundation.CHAR * 260
    Reserved: UInt32
    Unused: Byte * 512
class GNSS_SUPL_NI_INFO(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    RequestorId: Char * 260
    ClientName: Char * 260
    SuplNiUrl: Windows.Win32.Foundation.CHAR * 260
class GNSS_SUPL_VERSION(EasyCastStructure):
    MajorVersion: UInt32
    MinorVersion: UInt32
class GNSS_SUPL_VERSION_2(EasyCastStructure):
    MajorVersion: UInt32
    MinorVersion: UInt32
    ServiceIndicator: UInt32
class GNSS_V2UPL_CONFIG(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    MPC: Windows.Win32.Foundation.CHAR * 260
    PDE: Windows.Win32.Foundation.CHAR * 260
    ApplicationTypeIndicator_MR: Byte
    Unused: Byte * 512
class GNSS_V2UPL_NI_INFO(EasyCastStructure):
    Size: UInt32
    Version: UInt32
    RequestorId: Char * 260
class ICivicAddressReport(ComPtr):
    extends: Windows.Win32.Devices.Geolocation.ILocationReport
    Guid = Guid('c0b19f70-4adf-445d-87-f2-ca-d8-fd-71-17-92')
    @commethod(6)
    def GetAddressLine1(self, pbstrAddress1: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAddressLine2(self, pbstrAddress2: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCity(self, pbstrCity: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStateProvince(self, pbstrStateProvince: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPostalCode(self, pbstrPostalCode: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCountryRegion(self, pbstrCountryRegion: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDetailLevel(self, pDetailLevel: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ICivicAddressReportFactory(ComPtr):
    extends: Windows.Win32.Devices.Geolocation.ILocationReportFactory
    Guid = Guid('bf773b93-c64f-4bee-be-b2-67-c0-b8-df-66-e0')
    @commethod(15)
    def get_CivicAddressReport(self, pVal: POINTER(Windows.Win32.Devices.Geolocation.IDispCivicAddressReport_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDefaultLocation(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a65af77e-969a-4a2e-8a-ca-33-bb-7c-bb-12-35')
    @commethod(3)
    def SetReport(self, reportType: POINTER(Guid), pLocationReport: Windows.Win32.Devices.Geolocation.ILocationReport_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetReport(self, reportType: POINTER(Guid), ppLocationReport: POINTER(Windows.Win32.Devices.Geolocation.ILocationReport_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDispCivicAddressReport(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('16ff1a34-9e30-42c3-b4-4d-e2-25-13-b5-76-7a')
    @commethod(7)
    def get_AddressLine1(self, pAddress1: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AddressLine2(self, pAddress2: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_City(self, pCity: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_StateProvince(self, pStateProvince: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PostalCode(self, pPostalCode: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CountryRegion(self, pCountryRegion: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_DetailLevel(self, pDetailLevel: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Timestamp(self, pVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
class IDispLatLongReport(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('8ae32723-389b-4a11-99-57-5b-dd-48-fc-96-17')
    @commethod(7)
    def get_Latitude(self, pVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Longitude(self, pVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ErrorRadius(self, pVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Altitude(self, pVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_AltitudeError(self, pVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Timestamp(self, pVal: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
class ILatLongReport(ComPtr):
    extends: Windows.Win32.Devices.Geolocation.ILocationReport
    Guid = Guid('7fed806d-0ef8-4f07-80-ac-36-a0-be-ae-31-34')
    @commethod(6)
    def GetLatitude(self, pLatitude: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLongitude(self, pLongitude: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetErrorRadius(self, pErrorRadius: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAltitude(self, pAltitude: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetAltitudeError(self, pAltitudeError: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
class ILatLongReportFactory(ComPtr):
    extends: Windows.Win32.Devices.Geolocation.ILocationReportFactory
    Guid = Guid('3f0804cb-b114-447d-83-dd-39-01-74-eb-b0-82')
    @commethod(15)
    def get_LatLongReport(self, pVal: POINTER(Windows.Win32.Devices.Geolocation.IDispLatLongReport_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ILocation(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ab2ece69-56d9-4f28-b5-25-de-1b-0e-e4-42-37')
    @commethod(3)
    def RegisterForReport(self, pEvents: Windows.Win32.Devices.Geolocation.ILocationEvents_head, reportType: POINTER(Guid), dwRequestedReportInterval: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterForReport(self, reportType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetReport(self, reportType: POINTER(Guid), ppLocationReport: POINTER(Windows.Win32.Devices.Geolocation.ILocationReport_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetReportStatus(self, reportType: POINTER(Guid), pStatus: POINTER(Windows.Win32.Devices.Geolocation.LOCATION_REPORT_STATUS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetReportInterval(self, reportType: POINTER(Guid), pMilliseconds: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetReportInterval(self, reportType: POINTER(Guid), millisecondsRequested: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDesiredAccuracy(self, reportType: POINTER(Guid), pDesiredAccuracy: POINTER(Windows.Win32.Devices.Sensors.LOCATION_DESIRED_ACCURACY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetDesiredAccuracy(self, reportType: POINTER(Guid), desiredAccuracy: Windows.Win32.Devices.Sensors.LOCATION_DESIRED_ACCURACY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RequestPermissions(self, hParent: Windows.Win32.Foundation.HWND, pReportTypes: POINTER(Guid), count: UInt32, fModal: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class ILocationEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('cae02bbf-798b-4508-a2-07-35-a7-90-6d-c7-3d')
    @commethod(3)
    def OnLocationChanged(self, reportType: POINTER(Guid), pLocationReport: Windows.Win32.Devices.Geolocation.ILocationReport_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnStatusChanged(self, reportType: POINTER(Guid), newStatus: Windows.Win32.Devices.Geolocation.LOCATION_REPORT_STATUS) -> Windows.Win32.Foundation.HRESULT: ...
class ILocationPower(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('193e7729-ab6b-4b12-86-17-75-96-e1-bb-19-1c')
    @commethod(3)
    def Connect(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Disconnect(self) -> Windows.Win32.Foundation.HRESULT: ...
class ILocationReport(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c8b7f7ee-75d0-4db9-b6-2d-7a-0f-36-9c-a4-56')
    @commethod(3)
    def GetSensorID(self, pSensorID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTimestamp(self, pCreationTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetValue(self, pKey: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY_head), pValue: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ILocationReportFactory(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('2daec322-90b2-47e4-bb-08-0d-a8-41-93-5a-6b')
    @commethod(7)
    def ListenForReports(self, requestedReportInterval: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def StopListeningForReports(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Status(self, pVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ReportInterval(self, pMilliseconds: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_ReportInterval(self, millisecondsRequested: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_DesiredAccuracy(self, pDesiredAccuracy: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_DesiredAccuracy(self, desiredAccuracy: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RequestPermissions(self, hWnd: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
LOCATION_REPORT_STATUS = Int32
REPORT_NOT_SUPPORTED: LOCATION_REPORT_STATUS = 0
REPORT_ERROR: LOCATION_REPORT_STATUS = 1
REPORT_ACCESS_DENIED: LOCATION_REPORT_STATUS = 2
REPORT_INITIALIZING: LOCATION_REPORT_STATUS = 3
REPORT_RUNNING: LOCATION_REPORT_STATUS = 4
LatLongReport = Guid('ed81c073-1f84-4ca8-a1-61-18-3c-77-6b-c6-51')
LatLongReportFactory = Guid('9dcc3cc8-8609-4863-ba-d4-03-60-1f-4c-65-e8')
Location = Guid('e5b8e079-ee6d-4e33-a4-38-c8-7f-2e-95-92-54')
class _ICivicAddressReportFactoryEvents(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('c96039ff-72ec-4617-89-bd-84-d8-8b-ed-c7-22')
class _ILatLongReportFactoryEvents(ComPtr):
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
