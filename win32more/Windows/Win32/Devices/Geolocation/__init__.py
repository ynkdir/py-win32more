from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.Geolocation
import win32more.Windows.Win32.Devices.Sensors
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
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
GUID_DEVINTERFACE_GNSS: Guid = Guid('{3336e5e4-018a-4669-84c5-bd05f3bd368b}')
CivicAddressReport = Guid('{d39e7bdd-7d05-46b8-8721-80cf035f57d7}')
CivicAddressReportFactory = Guid('{2a11f42c-3e81-4ad4-9cbe-45579d89671a}')
DefaultLocation = Guid('{8b7fbfe0-5cd7-494a-af8c-283a65707506}')
DispCivicAddressReport = Guid('{4c596aec-8544-4082-ba9f-eb0a7d8e65c6}')
DispLatLongReport = Guid('{7a7c3277-8f84-4636-95b2-ebb5507ff77e}')
class GNSS_AGNSS_INJECT(Structure):
    Size: UInt32
    Version: UInt32
    InjectionType: win32more.Windows.Win32.Devices.Geolocation.GNSS_AGNSS_REQUEST_TYPE
    InjectionStatus: win32more.Windows.Win32.Foundation.NTSTATUS
    InjectionDataSize: UInt32
    Unused: Byte * 512
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Time: win32more.Windows.Win32.Devices.Geolocation.GNSS_AGNSS_INJECTTIME
        Position: win32more.Windows.Win32.Devices.Geolocation.GNSS_AGNSS_INJECTPOSITION
        BlobData: win32more.Windows.Win32.Devices.Geolocation.GNSS_AGNSS_INJECTBLOB
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
    BasicData: win32more.Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_BASIC
    AccuracyData: win32more.Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_ACCURACY
class GNSS_AGNSS_INJECTTIME(Structure):
    Size: UInt32
    Version: UInt32
    UtcTime: win32more.Windows.Win32.Foundation.FILETIME
    TimeUncertainty: UInt32
class GNSS_AGNSS_REQUEST_PARAM(Structure):
    Size: UInt32
    Version: UInt32
    RequestType: win32more.Windows.Win32.Devices.Geolocation.GNSS_AGNSS_REQUEST_TYPE
    BlobFormat: UInt32
GNSS_AGNSS_REQUEST_TYPE = Int32
GNSS_AGNSS_TimeInjection: win32more.Windows.Win32.Devices.Geolocation.GNSS_AGNSS_REQUEST_TYPE = 1
GNSS_AGNSS_PositionInjection: win32more.Windows.Win32.Devices.Geolocation.GNSS_AGNSS_REQUEST_TYPE = 2
GNSS_AGNSS_BlobInjection: win32more.Windows.Win32.Devices.Geolocation.GNSS_AGNSS_REQUEST_TYPE = 3
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
        v1: win32more.Windows.Win32.Devices.Geolocation.GNSS_BREADCRUMB_V1 * 50
class GNSS_BREADCRUMB_V1(Structure):
    FixTimeStamp: win32more.Windows.Win32.Foundation.FILETIME
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
    TestResultStatus: win32more.Windows.Win32.Foundation.NTSTATUS
    SignalToNoiseRatio: Double
    Frequency: Double
    Unused: Byte * 512
class GNSS_DEVICE_CAPABILITY(Structure):
    Size: UInt32
    Version: UInt32
    SupportMultipleFixSessions: win32more.Windows.Win32.Foundation.BOOL
    SupportMultipleAppSessions: win32more.Windows.Win32.Foundation.BOOL
    RequireAGnssInjection: win32more.Windows.Win32.Foundation.BOOL
    AgnssFormatSupported: UInt32
    AgnssFormatPreferred: UInt32
    SupportDistanceTracking: win32more.Windows.Win32.Foundation.BOOL
    SupportContinuousTracking: win32more.Windows.Win32.Foundation.BOOL
    Reserved1: UInt32
    Reserved2: win32more.Windows.Win32.Foundation.BOOL
    Reserved3: win32more.Windows.Win32.Foundation.BOOL
    Reserved4: win32more.Windows.Win32.Foundation.BOOL
    Reserved5: win32more.Windows.Win32.Foundation.BOOL
    GeofencingSupport: UInt32
    Reserved6: win32more.Windows.Win32.Foundation.BOOL
    Reserved7: win32more.Windows.Win32.Foundation.BOOL
    SupportCpLocation: win32more.Windows.Win32.Foundation.BOOL
    SupportUplV2: win32more.Windows.Win32.Foundation.BOOL
    SupportSuplV1: win32more.Windows.Win32.Foundation.BOOL
    SupportSuplV2: win32more.Windows.Win32.Foundation.BOOL
    SupportedSuplVersion: win32more.Windows.Win32.Devices.Geolocation.GNSS_SUPL_VERSION
    MaxGeofencesSupported: UInt32
    SupportMultipleSuplRootCert: win32more.Windows.Win32.Foundation.BOOL
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
    CommandType: win32more.Windows.Win32.Devices.Geolocation.GNSS_DRIVERCOMMAND_TYPE
    Reserved: UInt32
    CommandDataSize: UInt32
    Unused: Byte * 512
    CommandData: Byte * 1
GNSS_DRIVERCOMMAND_TYPE = Int32
GNSS_SetLocationServiceEnabled: win32more.Windows.Win32.Devices.Geolocation.GNSS_DRIVERCOMMAND_TYPE = 1
GNSS_SetLocationNIRequestAllowed: win32more.Windows.Win32.Devices.Geolocation.GNSS_DRIVERCOMMAND_TYPE = 2
GNSS_ForceSatelliteSystem: win32more.Windows.Win32.Devices.Geolocation.GNSS_DRIVERCOMMAND_TYPE = 3
GNSS_ForceOperationMode: win32more.Windows.Win32.Devices.Geolocation.GNSS_DRIVERCOMMAND_TYPE = 4
GNSS_ResetEngine: win32more.Windows.Win32.Devices.Geolocation.GNSS_DRIVERCOMMAND_TYPE = 9
GNSS_ClearAgnssData: win32more.Windows.Win32.Devices.Geolocation.GNSS_DRIVERCOMMAND_TYPE = 10
GNSS_SetSuplVersion: win32more.Windows.Win32.Devices.Geolocation.GNSS_DRIVERCOMMAND_TYPE = 12
GNSS_SetNMEALogging: win32more.Windows.Win32.Devices.Geolocation.GNSS_DRIVERCOMMAND_TYPE = 13
GNSS_SetUplServerAccessInterval: win32more.Windows.Win32.Devices.Geolocation.GNSS_DRIVERCOMMAND_TYPE = 14
GNSS_SetNiTimeoutInterval: win32more.Windows.Win32.Devices.Geolocation.GNSS_DRIVERCOMMAND_TYPE = 15
GNSS_ResetGeofencesTracking: win32more.Windows.Win32.Devices.Geolocation.GNSS_DRIVERCOMMAND_TYPE = 16
GNSS_SetSuplVersion2: win32more.Windows.Win32.Devices.Geolocation.GNSS_DRIVERCOMMAND_TYPE = 17
GNSS_CustomCommand: win32more.Windows.Win32.Devices.Geolocation.GNSS_DRIVERCOMMAND_TYPE = 256
GNSS_DRIVER_REQUEST = Int32
SUPL_CONFIG_DATA: win32more.Windows.Win32.Devices.Geolocation.GNSS_DRIVER_REQUEST = 1
class GNSS_DRIVER_REQUEST_DATA(Structure):
    Size: UInt32
    Version: UInt32
    Request: win32more.Windows.Win32.Devices.Geolocation.GNSS_DRIVER_REQUEST
    RequestFlag: UInt32
class GNSS_ERRORINFO(Structure):
    Size: UInt32
    Version: UInt32
    ErrorCode: UInt32
    IsRecoverable: win32more.Windows.Win32.Foundation.BOOL
    ErrorDescription: Char * 256
    Unused: Byte * 512
class GNSS_EVENT(Structure):
    Size: UInt32
    Version: UInt32
    EventType: win32more.Windows.Win32.Devices.Geolocation.GNSS_EVENT_TYPE
    EventDataSize: UInt32
    Unused: Byte * 512
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        FixData: win32more.Windows.Win32.Devices.Geolocation.GNSS_FIXDATA
        AgnssRequest: win32more.Windows.Win32.Devices.Geolocation.GNSS_AGNSS_REQUEST_PARAM
        NiRequest: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_REQUEST_PARAM
        ErrorInformation: win32more.Windows.Win32.Devices.Geolocation.GNSS_ERRORINFO
        NmeaData: win32more.Windows.Win32.Devices.Geolocation.GNSS_NMEA_DATA
        GeofenceAlertData: win32more.Windows.Win32.Devices.Geolocation.GNSS_GEOFENCE_ALERT_DATA
        BreadcrumbAlertData: win32more.Windows.Win32.Devices.Geolocation.GNSS_BREADCRUMBING_ALERT_DATA
        GeofencesTrackingStatus: win32more.Windows.Win32.Devices.Geolocation.GNSS_GEOFENCES_TRACKINGSTATUS_DATA
        DriverRequestData: win32more.Windows.Win32.Devices.Geolocation.GNSS_DRIVER_REQUEST_DATA
        CustomData: Byte * 1
class GNSS_EVENT_2(Structure):
    Size: UInt32
    Version: UInt32
    EventType: win32more.Windows.Win32.Devices.Geolocation.GNSS_EVENT_TYPE
    EventDataSize: UInt32
    Unused: Byte * 512
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        FixData: win32more.Windows.Win32.Devices.Geolocation.GNSS_FIXDATA
        FixData2: win32more.Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_2
        AgnssRequest: win32more.Windows.Win32.Devices.Geolocation.GNSS_AGNSS_REQUEST_PARAM
        NiRequest: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_REQUEST_PARAM
        ErrorInformation: win32more.Windows.Win32.Devices.Geolocation.GNSS_ERRORINFO
        NmeaData: win32more.Windows.Win32.Devices.Geolocation.GNSS_NMEA_DATA
        GeofenceAlertData: win32more.Windows.Win32.Devices.Geolocation.GNSS_GEOFENCE_ALERT_DATA
        BreadcrumbAlertData: win32more.Windows.Win32.Devices.Geolocation.GNSS_BREADCRUMBING_ALERT_DATA
        GeofencesTrackingStatus: win32more.Windows.Win32.Devices.Geolocation.GNSS_GEOFENCES_TRACKINGSTATUS_DATA
        DriverRequestData: win32more.Windows.Win32.Devices.Geolocation.GNSS_DRIVER_REQUEST_DATA
        CustomData: Byte * 1
GNSS_EVENT_TYPE = Int32
GNSS_Event_FixAvailable: win32more.Windows.Win32.Devices.Geolocation.GNSS_EVENT_TYPE = 1
GNSS_Event_RequireAgnss: win32more.Windows.Win32.Devices.Geolocation.GNSS_EVENT_TYPE = 2
GNSS_Event_Error: win32more.Windows.Win32.Devices.Geolocation.GNSS_EVENT_TYPE = 3
GNSS_Event_NiRequest: win32more.Windows.Win32.Devices.Geolocation.GNSS_EVENT_TYPE = 12
GNSS_Event_NmeaData: win32more.Windows.Win32.Devices.Geolocation.GNSS_EVENT_TYPE = 13
GNSS_Event_GeofenceAlertData: win32more.Windows.Win32.Devices.Geolocation.GNSS_EVENT_TYPE = 14
GNSS_Event_GeofencesTrackingStatus: win32more.Windows.Win32.Devices.Geolocation.GNSS_EVENT_TYPE = 15
GNSS_Event_DriverRequest: win32more.Windows.Win32.Devices.Geolocation.GNSS_EVENT_TYPE = 16
GNSS_Event_BreadcrumbAlertEvent: win32more.Windows.Win32.Devices.Geolocation.GNSS_EVENT_TYPE = 17
GNSS_Event_FixAvailable_2: win32more.Windows.Win32.Devices.Geolocation.GNSS_EVENT_TYPE = 18
GNSS_Event_Custom: win32more.Windows.Win32.Devices.Geolocation.GNSS_EVENT_TYPE = 32768
class GNSS_FIXDATA(Structure):
    Size: UInt32
    Version: UInt32
    FixSessionID: UInt32
    FixTimeStamp: win32more.Windows.Win32.Foundation.FILETIME
    IsFinalFix: win32more.Windows.Win32.Foundation.BOOL
    FixStatus: win32more.Windows.Win32.Foundation.NTSTATUS
    FixLevelOfDetails: UInt32
    BasicData: win32more.Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_BASIC
    AccuracyData: win32more.Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_ACCURACY
    SatelliteData: win32more.Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_SATELLITE
class GNSS_FIXDATA_2(Structure):
    Size: UInt32
    Version: UInt32
    FixSessionID: UInt32
    FixTimeStamp: win32more.Windows.Win32.Foundation.FILETIME
    IsFinalFix: win32more.Windows.Win32.Foundation.BOOL
    FixStatus: win32more.Windows.Win32.Foundation.NTSTATUS
    FixLevelOfDetails: UInt32
    BasicData: win32more.Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_BASIC_2
    AccuracyData: win32more.Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_ACCURACY_2
    SatelliteData: win32more.Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_SATELLITE
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
    SatelliteArray: win32more.Windows.Win32.Devices.Geolocation.GNSS_SATELLITEINFO * 64
GNSS_FIXSESSIONTYPE = Int32
GNSS_FixSession_SingleShot: win32more.Windows.Win32.Devices.Geolocation.GNSS_FIXSESSIONTYPE = 1
GNSS_FixSession_DistanceTracking: win32more.Windows.Win32.Devices.Geolocation.GNSS_FIXSESSIONTYPE = 2
GNSS_FixSession_ContinuousTracking: win32more.Windows.Win32.Devices.Geolocation.GNSS_FIXSESSIONTYPE = 3
GNSS_FixSession_LKG: win32more.Windows.Win32.Devices.Geolocation.GNSS_FIXSESSIONTYPE = 4
class GNSS_FIXSESSION_PARAM(Structure):
    Size: UInt32
    Version: UInt32
    FixSessionID: UInt32
    SessionType: win32more.Windows.Win32.Devices.Geolocation.GNSS_FIXSESSIONTYPE
    HorizontalAccuracy: UInt32
    HorizontalConfidence: UInt32
    Reserved: UInt32 * 9
    FixLevelOfDetails: UInt32
    Anonymous: _Anonymous_e__Union
    Unused: Byte * 256
    class _Anonymous_e__Union(Union):
        SingleShotParam: win32more.Windows.Win32.Devices.Geolocation.GNSS_SINGLESHOT_PARAM
        DistanceParam: win32more.Windows.Win32.Devices.Geolocation.GNSS_DISTANCETRACKING_PARAM
        ContinuousParam: win32more.Windows.Win32.Devices.Geolocation.GNSS_CONTINUOUSTRACKING_PARAM
        LkgFixParam: win32more.Windows.Win32.Devices.Geolocation.GNSS_LKGFIX_PARAM
        UnusedParam: Byte * 268
class GNSS_GEOFENCES_TRACKINGSTATUS_DATA(Structure):
    Size: UInt32
    Version: UInt32
    Status: win32more.Windows.Win32.Foundation.NTSTATUS
    StatusTimeStamp: win32more.Windows.Win32.Foundation.FILETIME
    Unused: Byte * 512
class GNSS_GEOFENCE_ALERT_DATA(Structure):
    Size: UInt32
    Version: UInt32
    GeofenceID: UInt32
    GeofenceState: win32more.Windows.Win32.Devices.Geolocation.GNSS_GEOFENCE_STATE
    FixBasicData: win32more.Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_BASIC
    FixAccuracyData: win32more.Windows.Win32.Devices.Geolocation.GNSS_FIXDATA_ACCURACY
    Unused: Byte * 512
class GNSS_GEOFENCE_CREATE_PARAM(Structure):
    Size: UInt32
    Version: UInt32
    AlertTypes: UInt32
    InitialState: win32more.Windows.Win32.Devices.Geolocation.GNSS_GEOFENCE_STATE
    Boundary: win32more.Windows.Win32.Devices.Geolocation.GNSS_GEOREGION
    Unused: Byte * 512
class GNSS_GEOFENCE_CREATE_RESPONSE(Structure):
    Size: UInt32
    Version: UInt32
    CreationStatus: win32more.Windows.Win32.Foundation.NTSTATUS
    GeofenceID: UInt32
    Unused: Byte * 512
class GNSS_GEOFENCE_DELETE_PARAM(Structure):
    Size: UInt32
    Version: UInt32
    GeofenceID: UInt32
    Unused: Byte * 512
GNSS_GEOFENCE_STATE = Int32
GNSS_GeofenceState_Unknown: win32more.Windows.Win32.Devices.Geolocation.GNSS_GEOFENCE_STATE = 0
GNSS_GeofenceState_Entered: win32more.Windows.Win32.Devices.Geolocation.GNSS_GEOFENCE_STATE = 1
GNSS_GeofenceState_Exited: win32more.Windows.Win32.Devices.Geolocation.GNSS_GEOFENCE_STATE = 2
class GNSS_GEOREGION(Structure):
    Size: UInt32
    Version: UInt32
    GeoRegionType: win32more.Windows.Win32.Devices.Geolocation.GNSS_GEOREGIONTYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Circle: win32more.Windows.Win32.Devices.Geolocation.GNSS_GEOREGION_CIRCLE
        Unused: Byte * 512
GNSS_GEOREGIONTYPE = Int32
GNSS_GeoRegion_Circle: win32more.Windows.Win32.Devices.Geolocation.GNSS_GEOREGIONTYPE = 1
class GNSS_GEOREGION_CIRCLE(Structure):
    Latitude: Double
    Longitude: Double
    RadiusInMeters: Double
class GNSS_LKGFIX_PARAM(Structure):
    Size: UInt32
    Version: UInt32
GNSS_NI_NOTIFICATION_TYPE = Int32
GNSS_NI_NoNotifyNoVerify: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_NOTIFICATION_TYPE = 1
GNSS_NI_NotifyOnly: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_NOTIFICATION_TYPE = 2
GNSS_NI_NotifyVerifyDefaultAllow: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_NOTIFICATION_TYPE = 3
GNSS_NI_NotifyVerifyDefaultNotAllow: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_NOTIFICATION_TYPE = 4
GNSS_NI_PrivacyOverride: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_NOTIFICATION_TYPE = 5
GNSS_NI_PLANE_TYPE = Int32
GNSS_NI_SUPL: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_PLANE_TYPE = 1
GNSS_NI_CP: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_PLANE_TYPE = 2
GNSS_NI_V2UPL: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_PLANE_TYPE = 3
class GNSS_NI_REQUEST_PARAM(Structure):
    Size: UInt32
    Version: UInt32
    RequestId: UInt32
    RequestType: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_REQUEST_TYPE
    NotificationType: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_NOTIFICATION_TYPE
    RequestPlaneType: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_PLANE_TYPE
    Anonymous: _Anonymous_e__Union
    ResponseTimeInSec: UInt32
    EmergencyLocation: win32more.Windows.Win32.Foundation.BOOL
    class _Anonymous_e__Union(Union):
        SuplNiInfo: win32more.Windows.Win32.Devices.Geolocation.GNSS_SUPL_NI_INFO
        CpNiInfo: win32more.Windows.Win32.Devices.Geolocation.GNSS_CP_NI_INFO
        V2UplNiInfo: win32more.Windows.Win32.Devices.Geolocation.GNSS_V2UPL_NI_INFO
GNSS_NI_REQUEST_TYPE = Int32
GNSS_NI_Request_SingleShot: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_REQUEST_TYPE = 1
GNSS_NI_Request_AreaTrigger: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_REQUEST_TYPE = 2
class GNSS_NI_RESPONSE(Structure):
    Size: UInt32
    Version: UInt32
    RequestId: UInt32
    UserResponse: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_USER_RESPONSE
GNSS_NI_USER_RESPONSE = Int32
GNSS_Ni_UserResponseAccept: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_USER_RESPONSE = 1
GNSS_Ni_UserResponseDeny: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_USER_RESPONSE = 2
GNSS_Ni_UserResponseTimeout: win32more.Windows.Win32.Devices.Geolocation.GNSS_NI_USER_RESPONSE = 3
class GNSS_NMEA_DATA(Structure):
    Size: UInt32
    Version: UInt32
    NmeaSentences: win32more.Windows.Win32.Foundation.CHAR * 256
class GNSS_PLATFORM_CAPABILITY(Structure):
    Size: UInt32
    Version: UInt32
    SupportAgnssInjection: win32more.Windows.Win32.Foundation.BOOL
    AgnssFormatSupported: UInt32
    Unused: Byte * 516
class GNSS_SATELLITEINFO(Structure):
    SatelliteId: UInt32
    UsedInPositiong: win32more.Windows.Win32.Foundation.BOOL
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
    TestResultStatus: win32more.Windows.Win32.Foundation.NTSTATUS
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
GNSS_Supl_Cert_Inject: win32more.Windows.Win32.Devices.Geolocation.GNSS_SUPL_CERT_ACTION = 1
GNSS_Supl_Cert_Delete: win32more.Windows.Win32.Devices.Geolocation.GNSS_SUPL_CERT_ACTION = 2
GNSS_Supl_Cert_Purge: win32more.Windows.Win32.Devices.Geolocation.GNSS_SUPL_CERT_ACTION = 3
class GNSS_SUPL_CERT_CONFIG(Structure):
    Size: UInt32
    Version: UInt32
    CertAction: win32more.Windows.Win32.Devices.Geolocation.GNSS_SUPL_CERT_ACTION
    SuplCertName: win32more.Windows.Win32.Foundation.CHAR * 260
    CertSize: UInt32
    Unused: Byte * 512
    CertData: Byte * 1
class GNSS_SUPL_HSLP_CONFIG(Structure):
    Size: UInt32
    Version: UInt32
    SuplHslp: win32more.Windows.Win32.Foundation.CHAR * 260
    SuplHslpFromImsi: win32more.Windows.Win32.Foundation.CHAR * 260
    Reserved: UInt32
    Unused: Byte * 512
class GNSS_SUPL_NI_INFO(Structure):
    Size: UInt32
    Version: UInt32
    RequestorId: Char * 260
    ClientName: Char * 260
    SuplNiUrl: win32more.Windows.Win32.Foundation.CHAR * 260
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
    MPC: win32more.Windows.Win32.Foundation.CHAR * 260
    PDE: win32more.Windows.Win32.Foundation.CHAR * 260
    ApplicationTypeIndicator_MR: Byte
    Unused: Byte * 512
class GNSS_V2UPL_NI_INFO(Structure):
    Size: UInt32
    Version: UInt32
    RequestorId: Char * 260
class ICivicAddressReport(ComPtr):
    extends: win32more.Windows.Win32.Devices.Geolocation.ILocationReport
    _iid_ = Guid('{c0b19f70-4adf-445d-87f2-cad8fd711792}')
    @commethod(6)
    def GetAddressLine1(self, pbstrAddress1: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAddressLine2(self, pbstrAddress2: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCity(self, pbstrCity: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStateProvince(self, pbstrStateProvince: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPostalCode(self, pbstrPostalCode: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCountryRegion(self, pbstrCountryRegion: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDetailLevel(self, pDetailLevel: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICivicAddressReportFactory(ComPtr):
    extends: win32more.Windows.Win32.Devices.Geolocation.ILocationReportFactory
    _iid_ = Guid('{bf773b93-c64f-4bee-beb2-67c0b8df66e0}')
    @commethod(15)
    def get_CivicAddressReport(self, pVal: POINTER(win32more.Windows.Win32.Devices.Geolocation.IDispCivicAddressReport)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDefaultLocation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a65af77e-969a-4a2e-8aca-33bb7cbb1235}')
    @commethod(3)
    def SetReport(self, reportType: POINTER(Guid), pLocationReport: win32more.Windows.Win32.Devices.Geolocation.ILocationReport) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetReport(self, reportType: POINTER(Guid), ppLocationReport: POINTER(win32more.Windows.Win32.Devices.Geolocation.ILocationReport)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDispCivicAddressReport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{16ff1a34-9e30-42c3-b44d-e22513b5767a}')
    @commethod(7)
    def get_AddressLine1(self, pAddress1: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AddressLine2(self, pAddress2: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_City(self, pCity: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_StateProvince(self, pStateProvince: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PostalCode(self, pPostalCode: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CountryRegion(self, pCountryRegion: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_DetailLevel(self, pDetailLevel: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Timestamp(self, pVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDispLatLongReport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8ae32723-389b-4a11-9957-5bdd48fc9617}')
    @commethod(7)
    def get_Latitude(self, pVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Longitude(self, pVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ErrorRadius(self, pVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Altitude(self, pVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_AltitudeError(self, pVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Timestamp(self, pVal: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILatLongReport(ComPtr):
    extends: win32more.Windows.Win32.Devices.Geolocation.ILocationReport
    _iid_ = Guid('{7fed806d-0ef8-4f07-80ac-36a0beae3134}')
    @commethod(6)
    def GetLatitude(self, pLatitude: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLongitude(self, pLongitude: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetErrorRadius(self, pErrorRadius: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAltitude(self, pAltitude: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetAltitudeError(self, pAltitudeError: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILatLongReportFactory(ComPtr):
    extends: win32more.Windows.Win32.Devices.Geolocation.ILocationReportFactory
    _iid_ = Guid('{3f0804cb-b114-447d-83dd-390174ebb082}')
    @commethod(15)
    def get_LatLongReport(self, pVal: POINTER(win32more.Windows.Win32.Devices.Geolocation.IDispLatLongReport)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILocation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ab2ece69-56d9-4f28-b525-de1b0ee44237}')
    @commethod(3)
    def RegisterForReport(self, pEvents: win32more.Windows.Win32.Devices.Geolocation.ILocationEvents, reportType: POINTER(Guid), dwRequestedReportInterval: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterForReport(self, reportType: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetReport(self, reportType: POINTER(Guid), ppLocationReport: POINTER(win32more.Windows.Win32.Devices.Geolocation.ILocationReport)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetReportStatus(self, reportType: POINTER(Guid), pStatus: POINTER(win32more.Windows.Win32.Devices.Geolocation.LOCATION_REPORT_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetReportInterval(self, reportType: POINTER(Guid), pMilliseconds: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetReportInterval(self, reportType: POINTER(Guid), millisecondsRequested: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDesiredAccuracy(self, reportType: POINTER(Guid), pDesiredAccuracy: POINTER(win32more.Windows.Win32.Devices.Sensors.LOCATION_DESIRED_ACCURACY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetDesiredAccuracy(self, reportType: POINTER(Guid), desiredAccuracy: win32more.Windows.Win32.Devices.Sensors.LOCATION_DESIRED_ACCURACY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RequestPermissions(self, hParent: win32more.Windows.Win32.Foundation.HWND, pReportTypes: POINTER(Guid), count: UInt32, fModal: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILocationEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cae02bbf-798b-4508-a207-35a7906dc73d}')
    @commethod(3)
    def OnLocationChanged(self, reportType: POINTER(Guid), pLocationReport: win32more.Windows.Win32.Devices.Geolocation.ILocationReport) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnStatusChanged(self, reportType: POINTER(Guid), newStatus: win32more.Windows.Win32.Devices.Geolocation.LOCATION_REPORT_STATUS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILocationPower(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{193e7729-ab6b-4b12-8617-7596e1bb191c}')
    @commethod(3)
    def Connect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Disconnect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILocationReport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c8b7f7ee-75d0-4db9-b62d-7a0f369ca456}')
    @commethod(3)
    def GetSensorID(self, pSensorID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTimestamp(self, pCreationTime: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetValue(self, pKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pValue: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILocationReportFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2daec322-90b2-47e4-bb08-0da841935a6b}')
    @commethod(7)
    def ListenForReports(self, requestedReportInterval: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def StopListeningForReports(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Status(self, pVal: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ReportInterval(self, pMilliseconds: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_ReportInterval(self, millisecondsRequested: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_DesiredAccuracy(self, pDesiredAccuracy: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_DesiredAccuracy(self, desiredAccuracy: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RequestPermissions(self, hWnd: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
LOCATION_REPORT_STATUS = Int32
REPORT_NOT_SUPPORTED: win32more.Windows.Win32.Devices.Geolocation.LOCATION_REPORT_STATUS = 0
REPORT_ERROR: win32more.Windows.Win32.Devices.Geolocation.LOCATION_REPORT_STATUS = 1
REPORT_ACCESS_DENIED: win32more.Windows.Win32.Devices.Geolocation.LOCATION_REPORT_STATUS = 2
REPORT_INITIALIZING: win32more.Windows.Win32.Devices.Geolocation.LOCATION_REPORT_STATUS = 3
REPORT_RUNNING: win32more.Windows.Win32.Devices.Geolocation.LOCATION_REPORT_STATUS = 4
LatLongReport = Guid('{ed81c073-1f84-4ca8-a161-183c776bc651}')
LatLongReportFactory = Guid('{9dcc3cc8-8609-4863-bad4-03601f4c65e8}')
Location = Guid('{e5b8e079-ee6d-4e33-a438-c87f2e959254}')
class _ICivicAddressReportFactoryEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c96039ff-72ec-4617-89bd-84d88bedc722}')
class _ILatLongReportFactoryEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{16ee6cb7-ab3c-424b-849f-269be551fcbc}')


make_ready(__name__)
