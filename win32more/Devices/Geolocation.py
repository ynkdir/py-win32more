from win32more import *
import win32more.Devices.Geolocation
import win32more.Devices.Sensors
import win32more.Foundation
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.UI.Shell.PropertiesSystem

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
GNSS_DRIVER_VERSION_1 = 1
GNSS_DRIVER_VERSION_2 = 2
GNSS_DRIVER_VERSION_3 = 3
GNSS_DRIVER_VERSION_4 = 4
GNSS_DRIVER_VERSION_5 = 5
GNSS_DRIVER_VERSION_6 = 6
IOCTL_GNSS_SEND_PLATFORM_CAPABILITY = 2228228
IOCTL_GNSS_GET_DEVICE_CAPABILITY = 2228232
IOCTL_GNSS_SEND_DRIVERCOMMAND = 2228236
IOCTL_GNSS_START_FIXSESSION = 2228288
IOCTL_GNSS_MODIFY_FIXSESSION = 2228292
IOCTL_GNSS_STOP_FIXSESSION = 2228296
IOCTL_GNSS_GET_FIXDATA = 2228300
IOCTL_GNSS_INJECT_AGNSS = 2228352
IOCTL_GNSS_LISTEN_AGNSS = 2228416
IOCTL_GNSS_LISTEN_ERROR = 2228420
IOCTL_GNSS_LISTEN_NI = 2228480
IOCTL_GNSS_SET_SUPL_HSLP = 2228484
IOCTL_GNSS_CONFIG_SUPL_CERT = 2228488
IOCTL_GNSS_RESPOND_NI = 2228492
IOCTL_GNSS_EXECUTE_CWTEST = 2228496
IOCTL_GNSS_EXECUTE_SELFTEST = 2228500
IOCTL_GNSS_GET_CHIPSETINFO = 2228504
IOCTL_GNSS_LISTEN_NMEA = 2228508
IOCTL_GNSS_SET_V2UPL_CONFIG = 2228512
IOCTL_GNSS_CREATE_GEOFENCE = 2228544
IOCTL_GNSS_DELETE_GEOFENCE = 2228548
IOCTL_GNSS_LISTEN_GEOFENCE_ALERT = 2228552
IOCTL_GNSS_LISTEN_GEOFENCES_TRACKINGSTATUS = 2228556
IOCTL_GNSS_LISTEN_DRIVER_REQUEST = 2228608
IOCTL_GNSS_START_BREADCRUMBING = 2228672
IOCTL_GNSS_STOP_BREADCRUMBING = 2228676
IOCTL_GNSS_LISTEN_BREADCRUMBING_ALERT = 2228680
IOCTL_GNSS_POP_BREADCRUMBS = 2228684
GNSS_AGNSSFORMAT_XTRA1 = 1
GNSS_AGNSSFORMAT_XTRA2 = 2
GNSS_AGNSSFORMAT_LTO = 4
GNSS_AGNSSFORMAT_XTRA3 = 8
GNSS_AGNSSFORMAT_XTRA3_1 = 16
GNSS_AGNSSFORMAT_XTRA3_2 = 32
GNSS_AGNSSFORMAT_XTRA_INT = 64
MAX_SERVER_URL_NAME = 260
MIN_GEOFENCES_REQUIRED = 100
BREADCRUMBING_UNSUPPORTED = 0
BREADCRUMBING_VERSION_1 = 1
MIN_BREADCRUMBS_SUPPORTED = 120
GNSS_SATELLITE_ANY = 0
GNSS_SATELLITE_GPS = 1
GNSS_SATELLITE_GLONASS = 2
GNSS_SATELLITE_BEIDOU = 4
GNSS_SATELLITE_GALILEO = 8
GNSS_OPERMODE_ANY = 0
GNSS_OPERMODE_MSA = 1
GNSS_OPERMODE_MSB = 2
GNSS_OPERMODE_MSS = 4
GNSS_OPERMODE_CELLID = 8
GNSS_OPERMODE_AFLT = 16
GNSS_OPERMODE_OTDOA = 32
GNSS_NMEALOGGING_NONE = 0
GNSS_NMEALOGGING_ALL = 255
GNSS_FIXDETAIL_BASIC = 1
GNSS_FIXDETAIL_ACCURACY = 2
GNSS_FIXDETAIL_SATELLITE = 4
GNSS_MAXSATELLITE = 64
GNSS_GEOFENCESUPPORT_SUPPORTED = 1
GNSS_GEOFENCESUPPORT_CIRCLE = 2
LOCATION_API_VERSION = 1
GUID_DEVINTERFACE_GNSS = '3336e5e4-018a-4669-84c5-bd05f3bd368b'
Location = Guid('e5b8e079-ee6d-4e33-a438-c87f2e959254')
DefaultLocation = Guid('8b7fbfe0-5cd7-494a-af8c-283a65707506')
LatLongReport = Guid('ed81c073-1f84-4ca8-a161-183c776bc651')
CivicAddressReport = Guid('d39e7bdd-7d05-46b8-8721-80cf035f57d7')
LatLongReportFactory = Guid('9dcc3cc8-8609-4863-bad4-03601f4c65e8')
CivicAddressReportFactory = Guid('2a11f42c-3e81-4ad4-9cbe-45579d89671a')
DispLatLongReport = Guid('7a7c3277-8f84-4636-95b2-ebb5507ff77e')
DispCivicAddressReport = Guid('4c596aec-8544-4082-ba9f-eb0a7d8e65c6')
LOCATION_REPORT_STATUS = Int32
REPORT_NOT_SUPPORTED = 0
REPORT_ERROR = 1
REPORT_ACCESS_DENIED = 2
REPORT_INITIALIZING = 3
REPORT_RUNNING = 4
def _define_ILocationReport_head():
    class ILocationReport(win32more.System.Com.IUnknown_head):
        Guid = Guid('c8b7f7ee-75d0-4db9-b62d-7a0f369ca456')
    return ILocationReport
def _define_ILocationReport():
    ILocationReport = win32more.Devices.Geolocation.ILocationReport_head
    ILocationReport.GetSensorID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetSensorID', ((1, 'pSensorID'),)))
    ILocationReport.GetTimestamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SYSTEMTIME_head), use_last_error=False)(4, 'GetTimestamp', ((1, 'pCreationTime'),)))
    ILocationReport.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.PROPERTYKEY_head),POINTER(win32more.System.Com.StructuredStorage.PROPVARIANT_head), use_last_error=False)(5, 'GetValue', ((1, 'pKey'),(1, 'pValue'),)))
    return ILocationReport
def _define_ILatLongReport_head():
    class ILatLongReport(win32more.Devices.Geolocation.ILocationReport_head):
        Guid = Guid('7fed806d-0ef8-4f07-80ac-36a0beae3134')
    return ILatLongReport
def _define_ILatLongReport():
    ILatLongReport = win32more.Devices.Geolocation.ILatLongReport_head
    ILatLongReport.GetLatitude = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(6, 'GetLatitude', ((1, 'pLatitude'),)))
    ILatLongReport.GetLongitude = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(7, 'GetLongitude', ((1, 'pLongitude'),)))
    ILatLongReport.GetErrorRadius = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(8, 'GetErrorRadius', ((1, 'pErrorRadius'),)))
    ILatLongReport.GetAltitude = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(9, 'GetAltitude', ((1, 'pAltitude'),)))
    ILatLongReport.GetAltitudeError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(10, 'GetAltitudeError', ((1, 'pAltitudeError'),)))
    return ILatLongReport
def _define_ICivicAddressReport_head():
    class ICivicAddressReport(win32more.Devices.Geolocation.ILocationReport_head):
        Guid = Guid('c0b19f70-4adf-445d-87f2-cad8fd711792')
    return ICivicAddressReport
def _define_ICivicAddressReport():
    ICivicAddressReport = win32more.Devices.Geolocation.ICivicAddressReport_head
    ICivicAddressReport.GetAddressLine1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'GetAddressLine1', ((1, 'pbstrAddress1'),)))
    ICivicAddressReport.GetAddressLine2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'GetAddressLine2', ((1, 'pbstrAddress2'),)))
    ICivicAddressReport.GetCity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'GetCity', ((1, 'pbstrCity'),)))
    ICivicAddressReport.GetStateProvince = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'GetStateProvince', ((1, 'pbstrStateProvince'),)))
    ICivicAddressReport.GetPostalCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'GetPostalCode', ((1, 'pbstrPostalCode'),)))
    ICivicAddressReport.GetCountryRegion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'GetCountryRegion', ((1, 'pbstrCountryRegion'),)))
    ICivicAddressReport.GetDetailLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(12, 'GetDetailLevel', ((1, 'pDetailLevel'),)))
    return ICivicAddressReport
def _define_ILocation_head():
    class ILocation(win32more.System.Com.IUnknown_head):
        Guid = Guid('ab2ece69-56d9-4f28-b525-de1b0ee44237')
    return ILocation
def _define_ILocation():
    ILocation = win32more.Devices.Geolocation.ILocation_head
    ILocation.RegisterForReport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Devices.Geolocation.ILocationEvents_head,POINTER(Guid),UInt32, use_last_error=False)(3, 'RegisterForReport', ((1, 'pEvents'),(1, 'reportType'),(1, 'dwRequestedReportInterval'),)))
    ILocation.UnregisterForReport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(4, 'UnregisterForReport', ((1, 'reportType'),)))
    ILocation.GetReport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.Geolocation.ILocationReport_head), use_last_error=False)(5, 'GetReport', ((1, 'reportType'),(1, 'ppLocationReport'),)))
    ILocation.GetReportStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.Geolocation.LOCATION_REPORT_STATUS), use_last_error=False)(6, 'GetReportStatus', ((1, 'reportType'),(1, 'pStatus'),)))
    ILocation.GetReportInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32), use_last_error=False)(7, 'GetReportInterval', ((1, 'reportType'),(1, 'pMilliseconds'),)))
    ILocation.SetReportInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32, use_last_error=False)(8, 'SetReportInterval', ((1, 'reportType'),(1, 'millisecondsRequested'),)))
    ILocation.GetDesiredAccuracy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.Sensors.LOCATION_DESIRED_ACCURACY), use_last_error=False)(9, 'GetDesiredAccuracy', ((1, 'reportType'),(1, 'pDesiredAccuracy'),)))
    ILocation.SetDesiredAccuracy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Devices.Sensors.LOCATION_DESIRED_ACCURACY, use_last_error=False)(10, 'SetDesiredAccuracy', ((1, 'reportType'),(1, 'desiredAccuracy'),)))
    ILocation.RequestPermissions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),UInt32,win32more.Foundation.BOOL, use_last_error=False)(11, 'RequestPermissions', ((1, 'hParent'),(1, 'pReportTypes'),(1, 'count'),(1, 'fModal'),)))
    return ILocation
def _define_ILocationPower_head():
    class ILocationPower(win32more.System.Com.IUnknown_head):
        Guid = Guid('193e7729-ab6b-4b12-8617-7596e1bb191c')
    return ILocationPower
def _define_ILocationPower():
    ILocationPower = win32more.Devices.Geolocation.ILocationPower_head
    ILocationPower.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Connect', ()))
    ILocationPower.Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Disconnect', ()))
    return ILocationPower
def _define_IDefaultLocation_head():
    class IDefaultLocation(win32more.System.Com.IUnknown_head):
        Guid = Guid('a65af77e-969a-4a2e-8aca-33bb7cbb1235')
    return IDefaultLocation
def _define_IDefaultLocation():
    IDefaultLocation = win32more.Devices.Geolocation.IDefaultLocation_head
    IDefaultLocation.SetReport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Devices.Geolocation.ILocationReport_head, use_last_error=False)(3, 'SetReport', ((1, 'reportType'),(1, 'pLocationReport'),)))
    IDefaultLocation.GetReport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Devices.Geolocation.ILocationReport_head), use_last_error=False)(4, 'GetReport', ((1, 'reportType'),(1, 'ppLocationReport'),)))
    return IDefaultLocation
def _define_ILocationEvents_head():
    class ILocationEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('cae02bbf-798b-4508-a207-35a7906dc73d')
    return ILocationEvents
def _define_ILocationEvents():
    ILocationEvents = win32more.Devices.Geolocation.ILocationEvents_head
    ILocationEvents.OnLocationChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Devices.Geolocation.ILocationReport_head, use_last_error=False)(3, 'OnLocationChanged', ((1, 'reportType'),(1, 'pLocationReport'),)))
    ILocationEvents.OnStatusChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Devices.Geolocation.LOCATION_REPORT_STATUS, use_last_error=False)(4, 'OnStatusChanged', ((1, 'reportType'),(1, 'newStatus'),)))
    return ILocationEvents
def _define_IDispLatLongReport_head():
    class IDispLatLongReport(win32more.System.Com.IDispatch_head):
        Guid = Guid('8ae32723-389b-4a11-9957-5bdd48fc9617')
    return IDispLatLongReport
def _define_IDispLatLongReport():
    IDispLatLongReport = win32more.Devices.Geolocation.IDispLatLongReport_head
    IDispLatLongReport.get_Latitude = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(7, 'get_Latitude', ((1, 'pVal'),)))
    IDispLatLongReport.get_Longitude = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(8, 'get_Longitude', ((1, 'pVal'),)))
    IDispLatLongReport.get_ErrorRadius = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(9, 'get_ErrorRadius', ((1, 'pVal'),)))
    IDispLatLongReport.get_Altitude = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(10, 'get_Altitude', ((1, 'pVal'),)))
    IDispLatLongReport.get_AltitudeError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(11, 'get_AltitudeError', ((1, 'pVal'),)))
    IDispLatLongReport.get_Timestamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(12, 'get_Timestamp', ((1, 'pVal'),)))
    return IDispLatLongReport
def _define_IDispCivicAddressReport_head():
    class IDispCivicAddressReport(win32more.System.Com.IDispatch_head):
        Guid = Guid('16ff1a34-9e30-42c3-b44d-e22513b5767a')
    return IDispCivicAddressReport
def _define_IDispCivicAddressReport():
    IDispCivicAddressReport = win32more.Devices.Geolocation.IDispCivicAddressReport_head
    IDispCivicAddressReport.get_AddressLine1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_AddressLine1', ((1, 'pAddress1'),)))
    IDispCivicAddressReport.get_AddressLine2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_AddressLine2', ((1, 'pAddress2'),)))
    IDispCivicAddressReport.get_City = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_City', ((1, 'pCity'),)))
    IDispCivicAddressReport.get_StateProvince = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_StateProvince', ((1, 'pStateProvince'),)))
    IDispCivicAddressReport.get_PostalCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_PostalCode', ((1, 'pPostalCode'),)))
    IDispCivicAddressReport.get_CountryRegion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'get_CountryRegion', ((1, 'pCountryRegion'),)))
    IDispCivicAddressReport.get_DetailLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(13, 'get_DetailLevel', ((1, 'pDetailLevel'),)))
    IDispCivicAddressReport.get_Timestamp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Double), use_last_error=False)(14, 'get_Timestamp', ((1, 'pVal'),)))
    return IDispCivicAddressReport
def _define_ILocationReportFactory_head():
    class ILocationReportFactory(win32more.System.Com.IDispatch_head):
        Guid = Guid('2daec322-90b2-47e4-bb08-0da841935a6b')
    return ILocationReportFactory
def _define_ILocationReportFactory():
    ILocationReportFactory = win32more.Devices.Geolocation.ILocationReportFactory_head
    ILocationReportFactory.ListenForReports = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(7, 'ListenForReports', ((1, 'requestedReportInterval'),)))
    ILocationReportFactory.StopListeningForReports = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'StopListeningForReports', ()))
    ILocationReportFactory.get_Status = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'get_Status', ((1, 'pVal'),)))
    ILocationReportFactory.get_ReportInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(10, 'get_ReportInterval', ((1, 'pMilliseconds'),)))
    ILocationReportFactory.put_ReportInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(11, 'put_ReportInterval', ((1, 'millisecondsRequested'),)))
    ILocationReportFactory.get_DesiredAccuracy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(12, 'get_DesiredAccuracy', ((1, 'pDesiredAccuracy'),)))
    ILocationReportFactory.put_DesiredAccuracy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(13, 'put_DesiredAccuracy', ((1, 'desiredAccuracy'),)))
    ILocationReportFactory.RequestPermissions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(14, 'RequestPermissions', ((1, 'hWnd'),)))
    return ILocationReportFactory
def _define_ILatLongReportFactory_head():
    class ILatLongReportFactory(win32more.Devices.Geolocation.ILocationReportFactory_head):
        Guid = Guid('3f0804cb-b114-447d-83dd-390174ebb082')
    return ILatLongReportFactory
def _define_ILatLongReportFactory():
    ILatLongReportFactory = win32more.Devices.Geolocation.ILatLongReportFactory_head
    ILatLongReportFactory.get_LatLongReport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Geolocation.IDispLatLongReport_head), use_last_error=False)(15, 'get_LatLongReport', ((1, 'pVal'),)))
    return ILatLongReportFactory
def _define_ICivicAddressReportFactory_head():
    class ICivicAddressReportFactory(win32more.Devices.Geolocation.ILocationReportFactory_head):
        Guid = Guid('bf773b93-c64f-4bee-beb2-67c0b8df66e0')
    return ICivicAddressReportFactory
def _define_ICivicAddressReportFactory():
    ICivicAddressReportFactory = win32more.Devices.Geolocation.ICivicAddressReportFactory_head
    ICivicAddressReportFactory.get_CivicAddressReport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Devices.Geolocation.IDispCivicAddressReport_head), use_last_error=False)(15, 'get_CivicAddressReport', ((1, 'pVal'),)))
    return ICivicAddressReportFactory
def _define__ILatLongReportFactoryEvents_head():
    class _ILatLongReportFactoryEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('16ee6cb7-ab3c-424b-849f-269be551fcbc')
    return _ILatLongReportFactoryEvents
def _define__ILatLongReportFactoryEvents():
    _ILatLongReportFactoryEvents = win32more.Devices.Geolocation._ILatLongReportFactoryEvents_head
    return _ILatLongReportFactoryEvents
def _define__ICivicAddressReportFactoryEvents_head():
    class _ICivicAddressReportFactoryEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('c96039ff-72ec-4617-89bd-84d88bedc722')
    return _ICivicAddressReportFactoryEvents
def _define__ICivicAddressReportFactoryEvents():
    _ICivicAddressReportFactoryEvents = win32more.Devices.Geolocation._ICivicAddressReportFactoryEvents_head
    return _ICivicAddressReportFactoryEvents
def _define_GNSS_SUPL_VERSION_head():
    class GNSS_SUPL_VERSION(Structure):
        pass
    return GNSS_SUPL_VERSION
def _define_GNSS_SUPL_VERSION():
    GNSS_SUPL_VERSION = win32more.Devices.Geolocation.GNSS_SUPL_VERSION_head
    GNSS_SUPL_VERSION._fields_ = [
        ("MajorVersion", UInt32),
        ("MinorVersion", UInt32),
    ]
    return GNSS_SUPL_VERSION
def _define_GNSS_SUPL_VERSION_2_head():
    class GNSS_SUPL_VERSION_2(Structure):
        pass
    return GNSS_SUPL_VERSION_2
def _define_GNSS_SUPL_VERSION_2():
    GNSS_SUPL_VERSION_2 = win32more.Devices.Geolocation.GNSS_SUPL_VERSION_2_head
    GNSS_SUPL_VERSION_2._fields_ = [
        ("MajorVersion", UInt32),
        ("MinorVersion", UInt32),
        ("ServiceIndicator", UInt32),
    ]
    return GNSS_SUPL_VERSION_2
def _define_GNSS_DEVICE_CAPABILITY_head():
    class GNSS_DEVICE_CAPABILITY(Structure):
        pass
    return GNSS_DEVICE_CAPABILITY
def _define_GNSS_DEVICE_CAPABILITY():
    GNSS_DEVICE_CAPABILITY = win32more.Devices.Geolocation.GNSS_DEVICE_CAPABILITY_head
    GNSS_DEVICE_CAPABILITY._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("SupportMultipleFixSessions", win32more.Foundation.BOOL),
        ("SupportMultipleAppSessions", win32more.Foundation.BOOL),
        ("RequireAGnssInjection", win32more.Foundation.BOOL),
        ("AgnssFormatSupported", UInt32),
        ("AgnssFormatPreferred", UInt32),
        ("SupportDistanceTracking", win32more.Foundation.BOOL),
        ("SupportContinuousTracking", win32more.Foundation.BOOL),
        ("Reserved1", UInt32),
        ("Reserved2", win32more.Foundation.BOOL),
        ("Reserved3", win32more.Foundation.BOOL),
        ("Reserved4", win32more.Foundation.BOOL),
        ("Reserved5", win32more.Foundation.BOOL),
        ("GeofencingSupport", UInt32),
        ("Reserved6", win32more.Foundation.BOOL),
        ("Reserved7", win32more.Foundation.BOOL),
        ("SupportCpLocation", win32more.Foundation.BOOL),
        ("SupportUplV2", win32more.Foundation.BOOL),
        ("SupportSuplV1", win32more.Foundation.BOOL),
        ("SupportSuplV2", win32more.Foundation.BOOL),
        ("SupportedSuplVersion", win32more.Devices.Geolocation.GNSS_SUPL_VERSION),
        ("MaxGeofencesSupported", UInt32),
        ("SupportMultipleSuplRootCert", win32more.Foundation.BOOL),
        ("GnssBreadCrumbPayloadVersion", UInt32),
        ("MaxGnssBreadCrumbFixes", UInt32),
        ("Unused", Byte * 496),
    ]
    return GNSS_DEVICE_CAPABILITY
def _define_GNSS_PLATFORM_CAPABILITY_head():
    class GNSS_PLATFORM_CAPABILITY(Structure):
        pass
    return GNSS_PLATFORM_CAPABILITY
def _define_GNSS_PLATFORM_CAPABILITY():
    GNSS_PLATFORM_CAPABILITY = win32more.Devices.Geolocation.GNSS_PLATFORM_CAPABILITY_head
    GNSS_PLATFORM_CAPABILITY._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("SupportAgnssInjection", win32more.Foundation.BOOL),
        ("AgnssFormatSupported", UInt32),
        ("Unused", Byte * 516),
    ]
    return GNSS_PLATFORM_CAPABILITY
GNSS_DRIVERCOMMAND_TYPE = Int32
GNSS_SetLocationServiceEnabled = 1
GNSS_SetLocationNIRequestAllowed = 2
GNSS_ForceSatelliteSystem = 3
GNSS_ForceOperationMode = 4
GNSS_ResetEngine = 9
GNSS_ClearAgnssData = 10
GNSS_SetSuplVersion = 12
GNSS_SetNMEALogging = 13
GNSS_SetUplServerAccessInterval = 14
GNSS_SetNiTimeoutInterval = 15
GNSS_ResetGeofencesTracking = 16
GNSS_SetSuplVersion2 = 17
GNSS_CustomCommand = 256
def _define_GNSS_DRIVERCOMMAND_PARAM_head():
    class GNSS_DRIVERCOMMAND_PARAM(Structure):
        pass
    return GNSS_DRIVERCOMMAND_PARAM
def _define_GNSS_DRIVERCOMMAND_PARAM():
    GNSS_DRIVERCOMMAND_PARAM = win32more.Devices.Geolocation.GNSS_DRIVERCOMMAND_PARAM_head
    GNSS_DRIVERCOMMAND_PARAM._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("CommandType", win32more.Devices.Geolocation.GNSS_DRIVERCOMMAND_TYPE),
        ("Reserved", UInt32),
        ("CommandDataSize", UInt32),
        ("Unused", Byte * 512),
        ("CommandData", Byte * 0),
    ]
    return GNSS_DRIVERCOMMAND_PARAM
GNSS_FIXSESSIONTYPE = Int32
GNSS_FixSession_SingleShot = 1
GNSS_FixSession_DistanceTracking = 2
GNSS_FixSession_ContinuousTracking = 3
GNSS_FixSession_LKG = 4
def _define_GNSS_SINGLESHOT_PARAM_head():
    class GNSS_SINGLESHOT_PARAM(Structure):
        pass
    return GNSS_SINGLESHOT_PARAM
def _define_GNSS_SINGLESHOT_PARAM():
    GNSS_SINGLESHOT_PARAM = win32more.Devices.Geolocation.GNSS_SINGLESHOT_PARAM_head
    GNSS_SINGLESHOT_PARAM._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("ResponseTime", UInt32),
    ]
    return GNSS_SINGLESHOT_PARAM
def _define_GNSS_DISTANCETRACKING_PARAM_head():
    class GNSS_DISTANCETRACKING_PARAM(Structure):
        pass
    return GNSS_DISTANCETRACKING_PARAM
def _define_GNSS_DISTANCETRACKING_PARAM():
    GNSS_DISTANCETRACKING_PARAM = win32more.Devices.Geolocation.GNSS_DISTANCETRACKING_PARAM_head
    GNSS_DISTANCETRACKING_PARAM._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("MovementThreshold", UInt32),
    ]
    return GNSS_DISTANCETRACKING_PARAM
def _define_GNSS_CONTINUOUSTRACKING_PARAM_head():
    class GNSS_CONTINUOUSTRACKING_PARAM(Structure):
        pass
    return GNSS_CONTINUOUSTRACKING_PARAM
def _define_GNSS_CONTINUOUSTRACKING_PARAM():
    GNSS_CONTINUOUSTRACKING_PARAM = win32more.Devices.Geolocation.GNSS_CONTINUOUSTRACKING_PARAM_head
    GNSS_CONTINUOUSTRACKING_PARAM._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("PreferredInterval", UInt32),
    ]
    return GNSS_CONTINUOUSTRACKING_PARAM
def _define_GNSS_LKGFIX_PARAM_head():
    class GNSS_LKGFIX_PARAM(Structure):
        pass
    return GNSS_LKGFIX_PARAM
def _define_GNSS_LKGFIX_PARAM():
    GNSS_LKGFIX_PARAM = win32more.Devices.Geolocation.GNSS_LKGFIX_PARAM_head
    GNSS_LKGFIX_PARAM._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
    ]
    return GNSS_LKGFIX_PARAM
def _define_GNSS_FIXSESSION_PARAM_head():
    class GNSS_FIXSESSION_PARAM(Structure):
        pass
    return GNSS_FIXSESSION_PARAM
def _define_GNSS_FIXSESSION_PARAM():
    GNSS_FIXSESSION_PARAM = win32more.Devices.Geolocation.GNSS_FIXSESSION_PARAM_head
    class GNSS_FIXSESSION_PARAM__Anonymous_e__Union(Union):
        pass
    GNSS_FIXSESSION_PARAM__Anonymous_e__Union._fields_ = [
        ("SingleShotParam", win32more.Devices.Geolocation.GNSS_SINGLESHOT_PARAM),
        ("DistanceParam", win32more.Devices.Geolocation.GNSS_DISTANCETRACKING_PARAM),
        ("ContinuousParam", win32more.Devices.Geolocation.GNSS_CONTINUOUSTRACKING_PARAM),
        ("LkgFixParam", win32more.Devices.Geolocation.GNSS_LKGFIX_PARAM),
        ("UnusedParam", Byte * 268),
    ]
    GNSS_FIXSESSION_PARAM._anonymous_ = [
        'Anonymous',
    ]
    GNSS_FIXSESSION_PARAM._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("FixSessionID", UInt32),
        ("SessionType", win32more.Devices.Geolocation.GNSS_FIXSESSIONTYPE),
        ("HorizontalAccuracy", UInt32),
        ("HorizontalConfidence", UInt32),
        ("Reserved", UInt32 * 9),
        ("FixLevelOfDetails", UInt32),
        ("Anonymous", GNSS_FIXSESSION_PARAM__Anonymous_e__Union),
        ("Unused", Byte * 256),
    ]
    return GNSS_FIXSESSION_PARAM
def _define_GNSS_STOPFIXSESSION_PARAM_head():
    class GNSS_STOPFIXSESSION_PARAM(Structure):
        pass
    return GNSS_STOPFIXSESSION_PARAM
def _define_GNSS_STOPFIXSESSION_PARAM():
    GNSS_STOPFIXSESSION_PARAM = win32more.Devices.Geolocation.GNSS_STOPFIXSESSION_PARAM_head
    GNSS_STOPFIXSESSION_PARAM._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("FixSessionID", UInt32),
        ("Unused", Byte * 512),
    ]
    return GNSS_STOPFIXSESSION_PARAM
def _define_GNSS_FIXDATA_BASIC_head():
    class GNSS_FIXDATA_BASIC(Structure):
        pass
    return GNSS_FIXDATA_BASIC
def _define_GNSS_FIXDATA_BASIC():
    GNSS_FIXDATA_BASIC = win32more.Devices.Geolocation.GNSS_FIXDATA_BASIC_head
    GNSS_FIXDATA_BASIC._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("Latitude", Double),
        ("Longitude", Double),
        ("Altitude", Double),
        ("Speed", Double),
        ("Heading", Double),
    ]
    return GNSS_FIXDATA_BASIC
def _define_GNSS_FIXDATA_BASIC_2_head():
    class GNSS_FIXDATA_BASIC_2(Structure):
        pass
    return GNSS_FIXDATA_BASIC_2
def _define_GNSS_FIXDATA_BASIC_2():
    GNSS_FIXDATA_BASIC_2 = win32more.Devices.Geolocation.GNSS_FIXDATA_BASIC_2_head
    GNSS_FIXDATA_BASIC_2._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("Latitude", Double),
        ("Longitude", Double),
        ("Altitude", Double),
        ("Speed", Double),
        ("Heading", Double),
        ("AltitudeEllipsoid", Double),
    ]
    return GNSS_FIXDATA_BASIC_2
def _define_GNSS_FIXDATA_ACCURACY_head():
    class GNSS_FIXDATA_ACCURACY(Structure):
        pass
    return GNSS_FIXDATA_ACCURACY
def _define_GNSS_FIXDATA_ACCURACY():
    GNSS_FIXDATA_ACCURACY = win32more.Devices.Geolocation.GNSS_FIXDATA_ACCURACY_head
    GNSS_FIXDATA_ACCURACY._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("HorizontalAccuracy", UInt32),
        ("HorizontalErrorMajorAxis", UInt32),
        ("HorizontalErrorMinorAxis", UInt32),
        ("HorizontalErrorAngle", UInt32),
        ("HeadingAccuracy", UInt32),
        ("AltitudeAccuracy", UInt32),
        ("SpeedAccuracy", UInt32),
        ("HorizontalConfidence", UInt32),
        ("HeadingConfidence", UInt32),
        ("AltitudeConfidence", UInt32),
        ("SpeedConfidence", UInt32),
        ("PositionDilutionOfPrecision", Single),
        ("HorizontalDilutionOfPrecision", Single),
        ("VerticalDilutionOfPrecision", Single),
    ]
    return GNSS_FIXDATA_ACCURACY
def _define_GNSS_FIXDATA_ACCURACY_2_head():
    class GNSS_FIXDATA_ACCURACY_2(Structure):
        pass
    return GNSS_FIXDATA_ACCURACY_2
def _define_GNSS_FIXDATA_ACCURACY_2():
    GNSS_FIXDATA_ACCURACY_2 = win32more.Devices.Geolocation.GNSS_FIXDATA_ACCURACY_2_head
    GNSS_FIXDATA_ACCURACY_2._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("HorizontalAccuracy", Double),
        ("HorizontalErrorMajorAxis", Double),
        ("HorizontalErrorMinorAxis", Double),
        ("HorizontalErrorAngle", Double),
        ("HeadingAccuracy", Double),
        ("AltitudeAccuracy", Double),
        ("SpeedAccuracy", Double),
        ("HorizontalConfidence", UInt32),
        ("HeadingConfidence", UInt32),
        ("AltitudeConfidence", UInt32),
        ("SpeedConfidence", UInt32),
        ("PositionDilutionOfPrecision", Double),
        ("HorizontalDilutionOfPrecision", Double),
        ("VerticalDilutionOfPrecision", Double),
        ("GeometricDilutionOfPrecision", Double),
        ("TimeDilutionOfPrecision", Double),
    ]
    return GNSS_FIXDATA_ACCURACY_2
def _define_GNSS_SATELLITEINFO_head():
    class GNSS_SATELLITEINFO(Structure):
        pass
    return GNSS_SATELLITEINFO
def _define_GNSS_SATELLITEINFO():
    GNSS_SATELLITEINFO = win32more.Devices.Geolocation.GNSS_SATELLITEINFO_head
    GNSS_SATELLITEINFO._fields_ = [
        ("SatelliteId", UInt32),
        ("UsedInPositiong", win32more.Foundation.BOOL),
        ("Elevation", Double),
        ("Azimuth", Double),
        ("SignalToNoiseRatio", Double),
    ]
    return GNSS_SATELLITEINFO
def _define_GNSS_FIXDATA_SATELLITE_head():
    class GNSS_FIXDATA_SATELLITE(Structure):
        pass
    return GNSS_FIXDATA_SATELLITE
def _define_GNSS_FIXDATA_SATELLITE():
    GNSS_FIXDATA_SATELLITE = win32more.Devices.Geolocation.GNSS_FIXDATA_SATELLITE_head
    GNSS_FIXDATA_SATELLITE._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("SatelliteCount", UInt32),
        ("SatelliteArray", win32more.Devices.Geolocation.GNSS_SATELLITEINFO * 64),
    ]
    return GNSS_FIXDATA_SATELLITE
def _define_GNSS_FIXDATA_head():
    class GNSS_FIXDATA(Structure):
        pass
    return GNSS_FIXDATA
def _define_GNSS_FIXDATA():
    GNSS_FIXDATA = win32more.Devices.Geolocation.GNSS_FIXDATA_head
    GNSS_FIXDATA._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("FixSessionID", UInt32),
        ("FixTimeStamp", win32more.Foundation.FILETIME),
        ("IsFinalFix", win32more.Foundation.BOOL),
        ("FixStatus", win32more.Foundation.NTSTATUS),
        ("FixLevelOfDetails", UInt32),
        ("BasicData", win32more.Devices.Geolocation.GNSS_FIXDATA_BASIC),
        ("AccuracyData", win32more.Devices.Geolocation.GNSS_FIXDATA_ACCURACY),
        ("SatelliteData", win32more.Devices.Geolocation.GNSS_FIXDATA_SATELLITE),
    ]
    return GNSS_FIXDATA
def _define_GNSS_FIXDATA_2_head():
    class GNSS_FIXDATA_2(Structure):
        pass
    return GNSS_FIXDATA_2
def _define_GNSS_FIXDATA_2():
    GNSS_FIXDATA_2 = win32more.Devices.Geolocation.GNSS_FIXDATA_2_head
    GNSS_FIXDATA_2._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("FixSessionID", UInt32),
        ("FixTimeStamp", win32more.Foundation.FILETIME),
        ("IsFinalFix", win32more.Foundation.BOOL),
        ("FixStatus", win32more.Foundation.NTSTATUS),
        ("FixLevelOfDetails", UInt32),
        ("BasicData", win32more.Devices.Geolocation.GNSS_FIXDATA_BASIC_2),
        ("AccuracyData", win32more.Devices.Geolocation.GNSS_FIXDATA_ACCURACY_2),
        ("SatelliteData", win32more.Devices.Geolocation.GNSS_FIXDATA_SATELLITE),
    ]
    return GNSS_FIXDATA_2
def _define_GNSS_BREADCRUMBING_PARAM_head():
    class GNSS_BREADCRUMBING_PARAM(Structure):
        pass
    return GNSS_BREADCRUMBING_PARAM
def _define_GNSS_BREADCRUMBING_PARAM():
    GNSS_BREADCRUMBING_PARAM = win32more.Devices.Geolocation.GNSS_BREADCRUMBING_PARAM_head
    GNSS_BREADCRUMBING_PARAM._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("MaximumHorizontalUncertainty", UInt32),
        ("MinDistanceBetweenFixes", UInt32),
        ("MaximumErrorTimeoutMs", UInt32),
        ("Unused", Byte * 512),
    ]
    return GNSS_BREADCRUMBING_PARAM
def _define_GNSS_BREADCRUMBING_ALERT_DATA_head():
    class GNSS_BREADCRUMBING_ALERT_DATA(Structure):
        pass
    return GNSS_BREADCRUMBING_ALERT_DATA
def _define_GNSS_BREADCRUMBING_ALERT_DATA():
    GNSS_BREADCRUMBING_ALERT_DATA = win32more.Devices.Geolocation.GNSS_BREADCRUMBING_ALERT_DATA_head
    GNSS_BREADCRUMBING_ALERT_DATA._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("Unused", Byte * 512),
    ]
    return GNSS_BREADCRUMBING_ALERT_DATA
def _define_GNSS_BREADCRUMB_V1_head():
    class GNSS_BREADCRUMB_V1(Structure):
        pass
    return GNSS_BREADCRUMB_V1
def _define_GNSS_BREADCRUMB_V1():
    GNSS_BREADCRUMB_V1 = win32more.Devices.Geolocation.GNSS_BREADCRUMB_V1_head
    GNSS_BREADCRUMB_V1._fields_ = [
        ("FixTimeStamp", win32more.Foundation.FILETIME),
        ("Latitude", Double),
        ("Longitude", Double),
        ("HorizontalAccuracy", UInt32),
        ("Speed", UInt16),
        ("SpeedAccuracy", UInt16),
        ("Altitude", Int16),
        ("AltitudeAccuracy", UInt16),
        ("Heading", Int16),
        ("HeadingAccuracy", Byte),
        ("FixSuccess", Byte),
    ]
    return GNSS_BREADCRUMB_V1
def _define_GNSS_BREADCRUMB_LIST_head():
    class GNSS_BREADCRUMB_LIST(Structure):
        pass
    return GNSS_BREADCRUMB_LIST
def _define_GNSS_BREADCRUMB_LIST():
    GNSS_BREADCRUMB_LIST = win32more.Devices.Geolocation.GNSS_BREADCRUMB_LIST_head
    class GNSS_BREADCRUMB_LIST__Anonymous_e__Union(Union):
        pass
    GNSS_BREADCRUMB_LIST__Anonymous_e__Union._fields_ = [
        ("v1", win32more.Devices.Geolocation.GNSS_BREADCRUMB_V1 * 50),
    ]
    GNSS_BREADCRUMB_LIST._anonymous_ = [
        'Anonymous',
    ]
    GNSS_BREADCRUMB_LIST._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("NumCrumbs", UInt32),
        ("Anonymous", GNSS_BREADCRUMB_LIST__Anonymous_e__Union),
    ]
    return GNSS_BREADCRUMB_LIST
GNSS_GEOREGIONTYPE = Int32
GNSS_GeoRegion_Circle = 1
def _define_GNSS_GEOREGION_CIRCLE_head():
    class GNSS_GEOREGION_CIRCLE(Structure):
        pass
    return GNSS_GEOREGION_CIRCLE
def _define_GNSS_GEOREGION_CIRCLE():
    GNSS_GEOREGION_CIRCLE = win32more.Devices.Geolocation.GNSS_GEOREGION_CIRCLE_head
    GNSS_GEOREGION_CIRCLE._fields_ = [
        ("Latitude", Double),
        ("Longitude", Double),
        ("RadiusInMeters", Double),
    ]
    return GNSS_GEOREGION_CIRCLE
def _define_GNSS_GEOREGION_head():
    class GNSS_GEOREGION(Structure):
        pass
    return GNSS_GEOREGION
def _define_GNSS_GEOREGION():
    GNSS_GEOREGION = win32more.Devices.Geolocation.GNSS_GEOREGION_head
    class GNSS_GEOREGION__Anonymous_e__Union(Union):
        pass
    GNSS_GEOREGION__Anonymous_e__Union._fields_ = [
        ("Circle", win32more.Devices.Geolocation.GNSS_GEOREGION_CIRCLE),
        ("Unused", Byte * 512),
    ]
    GNSS_GEOREGION._anonymous_ = [
        'Anonymous',
    ]
    GNSS_GEOREGION._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("GeoRegionType", win32more.Devices.Geolocation.GNSS_GEOREGIONTYPE),
        ("Anonymous", GNSS_GEOREGION__Anonymous_e__Union),
    ]
    return GNSS_GEOREGION
GNSS_GEOFENCE_STATE = Int32
GNSS_GeofenceState_Unknown = 0
GNSS_GeofenceState_Entered = 1
GNSS_GeofenceState_Exited = 2
def _define_GNSS_GEOFENCE_CREATE_PARAM_head():
    class GNSS_GEOFENCE_CREATE_PARAM(Structure):
        pass
    return GNSS_GEOFENCE_CREATE_PARAM
def _define_GNSS_GEOFENCE_CREATE_PARAM():
    GNSS_GEOFENCE_CREATE_PARAM = win32more.Devices.Geolocation.GNSS_GEOFENCE_CREATE_PARAM_head
    GNSS_GEOFENCE_CREATE_PARAM._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("AlertTypes", UInt32),
        ("InitialState", win32more.Devices.Geolocation.GNSS_GEOFENCE_STATE),
        ("Boundary", win32more.Devices.Geolocation.GNSS_GEOREGION),
        ("Unused", Byte * 512),
    ]
    return GNSS_GEOFENCE_CREATE_PARAM
def _define_GNSS_GEOFENCE_CREATE_RESPONSE_head():
    class GNSS_GEOFENCE_CREATE_RESPONSE(Structure):
        pass
    return GNSS_GEOFENCE_CREATE_RESPONSE
def _define_GNSS_GEOFENCE_CREATE_RESPONSE():
    GNSS_GEOFENCE_CREATE_RESPONSE = win32more.Devices.Geolocation.GNSS_GEOFENCE_CREATE_RESPONSE_head
    GNSS_GEOFENCE_CREATE_RESPONSE._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("CreationStatus", win32more.Foundation.NTSTATUS),
        ("GeofenceID", UInt32),
        ("Unused", Byte * 512),
    ]
    return GNSS_GEOFENCE_CREATE_RESPONSE
def _define_GNSS_GEOFENCE_DELETE_PARAM_head():
    class GNSS_GEOFENCE_DELETE_PARAM(Structure):
        pass
    return GNSS_GEOFENCE_DELETE_PARAM
def _define_GNSS_GEOFENCE_DELETE_PARAM():
    GNSS_GEOFENCE_DELETE_PARAM = win32more.Devices.Geolocation.GNSS_GEOFENCE_DELETE_PARAM_head
    GNSS_GEOFENCE_DELETE_PARAM._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("GeofenceID", UInt32),
        ("Unused", Byte * 512),
    ]
    return GNSS_GEOFENCE_DELETE_PARAM
def _define_GNSS_GEOFENCE_ALERT_DATA_head():
    class GNSS_GEOFENCE_ALERT_DATA(Structure):
        pass
    return GNSS_GEOFENCE_ALERT_DATA
def _define_GNSS_GEOFENCE_ALERT_DATA():
    GNSS_GEOFENCE_ALERT_DATA = win32more.Devices.Geolocation.GNSS_GEOFENCE_ALERT_DATA_head
    GNSS_GEOFENCE_ALERT_DATA._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("GeofenceID", UInt32),
        ("GeofenceState", win32more.Devices.Geolocation.GNSS_GEOFENCE_STATE),
        ("FixBasicData", win32more.Devices.Geolocation.GNSS_FIXDATA_BASIC),
        ("FixAccuracyData", win32more.Devices.Geolocation.GNSS_FIXDATA_ACCURACY),
        ("Unused", Byte * 512),
    ]
    return GNSS_GEOFENCE_ALERT_DATA
def _define_GNSS_GEOFENCES_TRACKINGSTATUS_DATA_head():
    class GNSS_GEOFENCES_TRACKINGSTATUS_DATA(Structure):
        pass
    return GNSS_GEOFENCES_TRACKINGSTATUS_DATA
def _define_GNSS_GEOFENCES_TRACKINGSTATUS_DATA():
    GNSS_GEOFENCES_TRACKINGSTATUS_DATA = win32more.Devices.Geolocation.GNSS_GEOFENCES_TRACKINGSTATUS_DATA_head
    GNSS_GEOFENCES_TRACKINGSTATUS_DATA._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("Status", win32more.Foundation.NTSTATUS),
        ("StatusTimeStamp", win32more.Foundation.FILETIME),
        ("Unused", Byte * 512),
    ]
    return GNSS_GEOFENCES_TRACKINGSTATUS_DATA
GNSS_EVENT_TYPE = Int32
GNSS_Event_FixAvailable = 1
GNSS_Event_RequireAgnss = 2
GNSS_Event_Error = 3
GNSS_Event_NiRequest = 12
GNSS_Event_NmeaData = 13
GNSS_Event_GeofenceAlertData = 14
GNSS_Event_GeofencesTrackingStatus = 15
GNSS_Event_DriverRequest = 16
GNSS_Event_BreadcrumbAlertEvent = 17
GNSS_Event_FixAvailable_2 = 18
GNSS_Event_Custom = 32768
def _define_GNSS_ERRORINFO_head():
    class GNSS_ERRORINFO(Structure):
        pass
    return GNSS_ERRORINFO
def _define_GNSS_ERRORINFO():
    GNSS_ERRORINFO = win32more.Devices.Geolocation.GNSS_ERRORINFO_head
    GNSS_ERRORINFO._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("ErrorCode", UInt32),
        ("IsRecoverable", win32more.Foundation.BOOL),
        ("ErrorDescription", Char * 256),
        ("Unused", Byte * 512),
    ]
    return GNSS_ERRORINFO
def _define_GNSS_NMEA_DATA_head():
    class GNSS_NMEA_DATA(Structure):
        pass
    return GNSS_NMEA_DATA
def _define_GNSS_NMEA_DATA():
    GNSS_NMEA_DATA = win32more.Devices.Geolocation.GNSS_NMEA_DATA_head
    GNSS_NMEA_DATA._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("NmeaSentences", win32more.Foundation.CHAR * 256),
    ]
    return GNSS_NMEA_DATA
GNSS_AGNSS_REQUEST_TYPE = Int32
GNSS_AGNSS_TimeInjection = 1
GNSS_AGNSS_PositionInjection = 2
GNSS_AGNSS_BlobInjection = 3
def _define_GNSS_AGNSS_REQUEST_PARAM_head():
    class GNSS_AGNSS_REQUEST_PARAM(Structure):
        pass
    return GNSS_AGNSS_REQUEST_PARAM
def _define_GNSS_AGNSS_REQUEST_PARAM():
    GNSS_AGNSS_REQUEST_PARAM = win32more.Devices.Geolocation.GNSS_AGNSS_REQUEST_PARAM_head
    GNSS_AGNSS_REQUEST_PARAM._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("RequestType", win32more.Devices.Geolocation.GNSS_AGNSS_REQUEST_TYPE),
        ("BlobFormat", UInt32),
    ]
    return GNSS_AGNSS_REQUEST_PARAM
GNSS_NI_PLANE_TYPE = Int32
GNSS_NI_SUPL = 1
GNSS_NI_CP = 2
GNSS_NI_V2UPL = 3
GNSS_NI_REQUEST_TYPE = Int32
GNSS_NI_Request_SingleShot = 1
GNSS_NI_Request_AreaTrigger = 2
GNSS_NI_NOTIFICATION_TYPE = Int32
GNSS_NI_NoNotifyNoVerify = 1
GNSS_NI_NotifyOnly = 2
GNSS_NI_NotifyVerifyDefaultAllow = 3
GNSS_NI_NotifyVerifyDefaultNotAllow = 4
GNSS_NI_PrivacyOverride = 5
def _define_GNSS_SUPL_NI_INFO_head():
    class GNSS_SUPL_NI_INFO(Structure):
        pass
    return GNSS_SUPL_NI_INFO
def _define_GNSS_SUPL_NI_INFO():
    GNSS_SUPL_NI_INFO = win32more.Devices.Geolocation.GNSS_SUPL_NI_INFO_head
    GNSS_SUPL_NI_INFO._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("RequestorId", Char * 260),
        ("ClientName", Char * 260),
        ("SuplNiUrl", win32more.Foundation.CHAR * 260),
    ]
    return GNSS_SUPL_NI_INFO
def _define_GNSS_CP_NI_INFO_head():
    class GNSS_CP_NI_INFO(Structure):
        pass
    return GNSS_CP_NI_INFO
def _define_GNSS_CP_NI_INFO():
    GNSS_CP_NI_INFO = win32more.Devices.Geolocation.GNSS_CP_NI_INFO_head
    GNSS_CP_NI_INFO._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("RequestorId", Char * 260),
        ("NotificationText", Char * 260),
    ]
    return GNSS_CP_NI_INFO
def _define_GNSS_V2UPL_NI_INFO_head():
    class GNSS_V2UPL_NI_INFO(Structure):
        pass
    return GNSS_V2UPL_NI_INFO
def _define_GNSS_V2UPL_NI_INFO():
    GNSS_V2UPL_NI_INFO = win32more.Devices.Geolocation.GNSS_V2UPL_NI_INFO_head
    GNSS_V2UPL_NI_INFO._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("RequestorId", Char * 260),
    ]
    return GNSS_V2UPL_NI_INFO
def _define_GNSS_NI_REQUEST_PARAM_head():
    class GNSS_NI_REQUEST_PARAM(Structure):
        pass
    return GNSS_NI_REQUEST_PARAM
def _define_GNSS_NI_REQUEST_PARAM():
    GNSS_NI_REQUEST_PARAM = win32more.Devices.Geolocation.GNSS_NI_REQUEST_PARAM_head
    class GNSS_NI_REQUEST_PARAM__Anonymous_e__Union(Union):
        pass
    GNSS_NI_REQUEST_PARAM__Anonymous_e__Union._fields_ = [
        ("SuplNiInfo", win32more.Devices.Geolocation.GNSS_SUPL_NI_INFO),
        ("CpNiInfo", win32more.Devices.Geolocation.GNSS_CP_NI_INFO),
        ("V2UplNiInfo", win32more.Devices.Geolocation.GNSS_V2UPL_NI_INFO),
    ]
    GNSS_NI_REQUEST_PARAM._anonymous_ = [
        'Anonymous',
    ]
    GNSS_NI_REQUEST_PARAM._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("RequestId", UInt32),
        ("RequestType", win32more.Devices.Geolocation.GNSS_NI_REQUEST_TYPE),
        ("NotificationType", win32more.Devices.Geolocation.GNSS_NI_NOTIFICATION_TYPE),
        ("RequestPlaneType", win32more.Devices.Geolocation.GNSS_NI_PLANE_TYPE),
        ("Anonymous", GNSS_NI_REQUEST_PARAM__Anonymous_e__Union),
        ("ResponseTimeInSec", UInt32),
        ("EmergencyLocation", win32more.Foundation.BOOL),
    ]
    return GNSS_NI_REQUEST_PARAM
GNSS_DRIVER_REQUEST = Int32
SUPL_CONFIG_DATA = 1
def _define_GNSS_DRIVER_REQUEST_DATA_head():
    class GNSS_DRIVER_REQUEST_DATA(Structure):
        pass
    return GNSS_DRIVER_REQUEST_DATA
def _define_GNSS_DRIVER_REQUEST_DATA():
    GNSS_DRIVER_REQUEST_DATA = win32more.Devices.Geolocation.GNSS_DRIVER_REQUEST_DATA_head
    GNSS_DRIVER_REQUEST_DATA._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("Request", win32more.Devices.Geolocation.GNSS_DRIVER_REQUEST),
        ("RequestFlag", UInt32),
    ]
    return GNSS_DRIVER_REQUEST_DATA
def _define_GNSS_EVENT_head():
    class GNSS_EVENT(Structure):
        pass
    return GNSS_EVENT
def _define_GNSS_EVENT():
    GNSS_EVENT = win32more.Devices.Geolocation.GNSS_EVENT_head
    class GNSS_EVENT__Anonymous_e__Union(Union):
        pass
    GNSS_EVENT__Anonymous_e__Union._fields_ = [
        ("FixData", win32more.Devices.Geolocation.GNSS_FIXDATA),
        ("AgnssRequest", win32more.Devices.Geolocation.GNSS_AGNSS_REQUEST_PARAM),
        ("NiRequest", win32more.Devices.Geolocation.GNSS_NI_REQUEST_PARAM),
        ("ErrorInformation", win32more.Devices.Geolocation.GNSS_ERRORINFO),
        ("NmeaData", win32more.Devices.Geolocation.GNSS_NMEA_DATA),
        ("GeofenceAlertData", win32more.Devices.Geolocation.GNSS_GEOFENCE_ALERT_DATA),
        ("BreadcrumbAlertData", win32more.Devices.Geolocation.GNSS_BREADCRUMBING_ALERT_DATA),
        ("GeofencesTrackingStatus", win32more.Devices.Geolocation.GNSS_GEOFENCES_TRACKINGSTATUS_DATA),
        ("DriverRequestData", win32more.Devices.Geolocation.GNSS_DRIVER_REQUEST_DATA),
        ("CustomData", Byte * 0),
    ]
    GNSS_EVENT._anonymous_ = [
        'Anonymous',
    ]
    GNSS_EVENT._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("EventType", win32more.Devices.Geolocation.GNSS_EVENT_TYPE),
        ("EventDataSize", UInt32),
        ("Unused", Byte * 512),
        ("Anonymous", GNSS_EVENT__Anonymous_e__Union),
    ]
    return GNSS_EVENT
def _define_GNSS_EVENT_2_head():
    class GNSS_EVENT_2(Structure):
        pass
    return GNSS_EVENT_2
def _define_GNSS_EVENT_2():
    GNSS_EVENT_2 = win32more.Devices.Geolocation.GNSS_EVENT_2_head
    class GNSS_EVENT_2__Anonymous_e__Union(Union):
        pass
    GNSS_EVENT_2__Anonymous_e__Union._fields_ = [
        ("FixData", win32more.Devices.Geolocation.GNSS_FIXDATA),
        ("FixData2", win32more.Devices.Geolocation.GNSS_FIXDATA_2),
        ("AgnssRequest", win32more.Devices.Geolocation.GNSS_AGNSS_REQUEST_PARAM),
        ("NiRequest", win32more.Devices.Geolocation.GNSS_NI_REQUEST_PARAM),
        ("ErrorInformation", win32more.Devices.Geolocation.GNSS_ERRORINFO),
        ("NmeaData", win32more.Devices.Geolocation.GNSS_NMEA_DATA),
        ("GeofenceAlertData", win32more.Devices.Geolocation.GNSS_GEOFENCE_ALERT_DATA),
        ("BreadcrumbAlertData", win32more.Devices.Geolocation.GNSS_BREADCRUMBING_ALERT_DATA),
        ("GeofencesTrackingStatus", win32more.Devices.Geolocation.GNSS_GEOFENCES_TRACKINGSTATUS_DATA),
        ("DriverRequestData", win32more.Devices.Geolocation.GNSS_DRIVER_REQUEST_DATA),
        ("CustomData", Byte * 0),
    ]
    GNSS_EVENT_2._anonymous_ = [
        'Anonymous',
    ]
    GNSS_EVENT_2._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("EventType", win32more.Devices.Geolocation.GNSS_EVENT_TYPE),
        ("EventDataSize", UInt32),
        ("Unused", Byte * 512),
        ("Anonymous", GNSS_EVENT_2__Anonymous_e__Union),
    ]
    return GNSS_EVENT_2
def _define_GNSS_AGNSS_INJECTTIME_head():
    class GNSS_AGNSS_INJECTTIME(Structure):
        pass
    return GNSS_AGNSS_INJECTTIME
def _define_GNSS_AGNSS_INJECTTIME():
    GNSS_AGNSS_INJECTTIME = win32more.Devices.Geolocation.GNSS_AGNSS_INJECTTIME_head
    GNSS_AGNSS_INJECTTIME._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("UtcTime", win32more.Foundation.FILETIME),
        ("TimeUncertainty", UInt32),
    ]
    return GNSS_AGNSS_INJECTTIME
def _define_GNSS_AGNSS_INJECTPOSITION_head():
    class GNSS_AGNSS_INJECTPOSITION(Structure):
        pass
    return GNSS_AGNSS_INJECTPOSITION
def _define_GNSS_AGNSS_INJECTPOSITION():
    GNSS_AGNSS_INJECTPOSITION = win32more.Devices.Geolocation.GNSS_AGNSS_INJECTPOSITION_head
    GNSS_AGNSS_INJECTPOSITION._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("Age", UInt32),
        ("BasicData", win32more.Devices.Geolocation.GNSS_FIXDATA_BASIC),
        ("AccuracyData", win32more.Devices.Geolocation.GNSS_FIXDATA_ACCURACY),
    ]
    return GNSS_AGNSS_INJECTPOSITION
def _define_GNSS_AGNSS_INJECTBLOB_head():
    class GNSS_AGNSS_INJECTBLOB(Structure):
        pass
    return GNSS_AGNSS_INJECTBLOB
def _define_GNSS_AGNSS_INJECTBLOB():
    GNSS_AGNSS_INJECTBLOB = win32more.Devices.Geolocation.GNSS_AGNSS_INJECTBLOB_head
    GNSS_AGNSS_INJECTBLOB._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("BlobOui", UInt32),
        ("BlobVersion", UInt32),
        ("AgnssFormat", UInt32),
        ("BlobSize", UInt32),
        ("BlobData", Byte * 0),
    ]
    return GNSS_AGNSS_INJECTBLOB
def _define_GNSS_AGNSS_INJECT_head():
    class GNSS_AGNSS_INJECT(Structure):
        pass
    return GNSS_AGNSS_INJECT
def _define_GNSS_AGNSS_INJECT():
    GNSS_AGNSS_INJECT = win32more.Devices.Geolocation.GNSS_AGNSS_INJECT_head
    class GNSS_AGNSS_INJECT__Anonymous_e__Union(Union):
        pass
    GNSS_AGNSS_INJECT__Anonymous_e__Union._fields_ = [
        ("Time", win32more.Devices.Geolocation.GNSS_AGNSS_INJECTTIME),
        ("Position", win32more.Devices.Geolocation.GNSS_AGNSS_INJECTPOSITION),
        ("BlobData", win32more.Devices.Geolocation.GNSS_AGNSS_INJECTBLOB),
    ]
    GNSS_AGNSS_INJECT._anonymous_ = [
        'Anonymous',
    ]
    GNSS_AGNSS_INJECT._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("InjectionType", win32more.Devices.Geolocation.GNSS_AGNSS_REQUEST_TYPE),
        ("InjectionStatus", win32more.Foundation.NTSTATUS),
        ("InjectionDataSize", UInt32),
        ("Unused", Byte * 512),
        ("Anonymous", GNSS_AGNSS_INJECT__Anonymous_e__Union),
    ]
    return GNSS_AGNSS_INJECT
def _define_GNSS_SUPL_HSLP_CONFIG_head():
    class GNSS_SUPL_HSLP_CONFIG(Structure):
        pass
    return GNSS_SUPL_HSLP_CONFIG
def _define_GNSS_SUPL_HSLP_CONFIG():
    GNSS_SUPL_HSLP_CONFIG = win32more.Devices.Geolocation.GNSS_SUPL_HSLP_CONFIG_head
    GNSS_SUPL_HSLP_CONFIG._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("SuplHslp", win32more.Foundation.CHAR * 260),
        ("SuplHslpFromImsi", win32more.Foundation.CHAR * 260),
        ("Reserved", UInt32),
        ("Unused", Byte * 512),
    ]
    return GNSS_SUPL_HSLP_CONFIG
GNSS_SUPL_CERT_ACTION = Int32
GNSS_Supl_Cert_Inject = 1
GNSS_Supl_Cert_Delete = 2
GNSS_Supl_Cert_Purge = 3
def _define_GNSS_SUPL_CERT_CONFIG_head():
    class GNSS_SUPL_CERT_CONFIG(Structure):
        pass
    return GNSS_SUPL_CERT_CONFIG
def _define_GNSS_SUPL_CERT_CONFIG():
    GNSS_SUPL_CERT_CONFIG = win32more.Devices.Geolocation.GNSS_SUPL_CERT_CONFIG_head
    GNSS_SUPL_CERT_CONFIG._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("CertAction", win32more.Devices.Geolocation.GNSS_SUPL_CERT_ACTION),
        ("SuplCertName", win32more.Foundation.CHAR * 260),
        ("CertSize", UInt32),
        ("Unused", Byte * 512),
        ("CertData", Byte * 0),
    ]
    return GNSS_SUPL_CERT_CONFIG
def _define_GNSS_V2UPL_CONFIG_head():
    class GNSS_V2UPL_CONFIG(Structure):
        pass
    return GNSS_V2UPL_CONFIG
def _define_GNSS_V2UPL_CONFIG():
    GNSS_V2UPL_CONFIG = win32more.Devices.Geolocation.GNSS_V2UPL_CONFIG_head
    GNSS_V2UPL_CONFIG._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("MPC", win32more.Foundation.CHAR * 260),
        ("PDE", win32more.Foundation.CHAR * 260),
        ("ApplicationTypeIndicator_MR", Byte),
        ("Unused", Byte * 512),
    ]
    return GNSS_V2UPL_CONFIG
GNSS_NI_USER_RESPONSE = Int32
GNSS_Ni_UserResponseAccept = 1
GNSS_Ni_UserResponseDeny = 2
GNSS_Ni_UserResponseTimeout = 3
def _define_GNSS_NI_RESPONSE_head():
    class GNSS_NI_RESPONSE(Structure):
        pass
    return GNSS_NI_RESPONSE
def _define_GNSS_NI_RESPONSE():
    GNSS_NI_RESPONSE = win32more.Devices.Geolocation.GNSS_NI_RESPONSE_head
    GNSS_NI_RESPONSE._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("RequestId", UInt32),
        ("UserResponse", win32more.Devices.Geolocation.GNSS_NI_USER_RESPONSE),
    ]
    return GNSS_NI_RESPONSE
def _define_GNSS_CWTESTDATA_head():
    class GNSS_CWTESTDATA(Structure):
        pass
    return GNSS_CWTESTDATA
def _define_GNSS_CWTESTDATA():
    GNSS_CWTESTDATA = win32more.Devices.Geolocation.GNSS_CWTESTDATA_head
    GNSS_CWTESTDATA._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("TestResultStatus", win32more.Foundation.NTSTATUS),
        ("SignalToNoiseRatio", Double),
        ("Frequency", Double),
        ("Unused", Byte * 512),
    ]
    return GNSS_CWTESTDATA
def _define_GNSS_SELFTESTCONFIG_head():
    class GNSS_SELFTESTCONFIG(Structure):
        pass
    return GNSS_SELFTESTCONFIG
def _define_GNSS_SELFTESTCONFIG():
    GNSS_SELFTESTCONFIG = win32more.Devices.Geolocation.GNSS_SELFTESTCONFIG_head
    GNSS_SELFTESTCONFIG._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("TestType", UInt32),
        ("Unused", Byte * 512),
        ("InBufLen", UInt32),
        ("InBuffer", Byte * 0),
    ]
    return GNSS_SELFTESTCONFIG
def _define_GNSS_SELFTESTRESULT_head():
    class GNSS_SELFTESTRESULT(Structure):
        pass
    return GNSS_SELFTESTRESULT
def _define_GNSS_SELFTESTRESULT():
    GNSS_SELFTESTRESULT = win32more.Devices.Geolocation.GNSS_SELFTESTRESULT_head
    GNSS_SELFTESTRESULT._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("TestResultStatus", win32more.Foundation.NTSTATUS),
        ("Result", UInt32),
        ("PinFailedBitMask", UInt32),
        ("Unused", Byte * 512),
        ("OutBufLen", UInt32),
        ("OutBuffer", Byte * 0),
    ]
    return GNSS_SELFTESTRESULT
def _define_GNSS_CHIPSETINFO_head():
    class GNSS_CHIPSETINFO(Structure):
        pass
    return GNSS_CHIPSETINFO
def _define_GNSS_CHIPSETINFO():
    GNSS_CHIPSETINFO = win32more.Devices.Geolocation.GNSS_CHIPSETINFO_head
    GNSS_CHIPSETINFO._fields_ = [
        ("Size", UInt32),
        ("Version", UInt32),
        ("ManufacturerID", Char * 25),
        ("HardwareID", Char * 25),
        ("FirmwareVersion", Char * 20),
        ("Unused", Byte * 512),
    ]
    return GNSS_CHIPSETINFO
__all__ = [
    "GNSS_DRIVER_VERSION_1",
    "GNSS_DRIVER_VERSION_2",
    "GNSS_DRIVER_VERSION_3",
    "GNSS_DRIVER_VERSION_4",
    "GNSS_DRIVER_VERSION_5",
    "GNSS_DRIVER_VERSION_6",
    "IOCTL_GNSS_SEND_PLATFORM_CAPABILITY",
    "IOCTL_GNSS_GET_DEVICE_CAPABILITY",
    "IOCTL_GNSS_SEND_DRIVERCOMMAND",
    "IOCTL_GNSS_START_FIXSESSION",
    "IOCTL_GNSS_MODIFY_FIXSESSION",
    "IOCTL_GNSS_STOP_FIXSESSION",
    "IOCTL_GNSS_GET_FIXDATA",
    "IOCTL_GNSS_INJECT_AGNSS",
    "IOCTL_GNSS_LISTEN_AGNSS",
    "IOCTL_GNSS_LISTEN_ERROR",
    "IOCTL_GNSS_LISTEN_NI",
    "IOCTL_GNSS_SET_SUPL_HSLP",
    "IOCTL_GNSS_CONFIG_SUPL_CERT",
    "IOCTL_GNSS_RESPOND_NI",
    "IOCTL_GNSS_EXECUTE_CWTEST",
    "IOCTL_GNSS_EXECUTE_SELFTEST",
    "IOCTL_GNSS_GET_CHIPSETINFO",
    "IOCTL_GNSS_LISTEN_NMEA",
    "IOCTL_GNSS_SET_V2UPL_CONFIG",
    "IOCTL_GNSS_CREATE_GEOFENCE",
    "IOCTL_GNSS_DELETE_GEOFENCE",
    "IOCTL_GNSS_LISTEN_GEOFENCE_ALERT",
    "IOCTL_GNSS_LISTEN_GEOFENCES_TRACKINGSTATUS",
    "IOCTL_GNSS_LISTEN_DRIVER_REQUEST",
    "IOCTL_GNSS_START_BREADCRUMBING",
    "IOCTL_GNSS_STOP_BREADCRUMBING",
    "IOCTL_GNSS_LISTEN_BREADCRUMBING_ALERT",
    "IOCTL_GNSS_POP_BREADCRUMBS",
    "GNSS_AGNSSFORMAT_XTRA1",
    "GNSS_AGNSSFORMAT_XTRA2",
    "GNSS_AGNSSFORMAT_LTO",
    "GNSS_AGNSSFORMAT_XTRA3",
    "GNSS_AGNSSFORMAT_XTRA3_1",
    "GNSS_AGNSSFORMAT_XTRA3_2",
    "GNSS_AGNSSFORMAT_XTRA_INT",
    "MAX_SERVER_URL_NAME",
    "MIN_GEOFENCES_REQUIRED",
    "BREADCRUMBING_UNSUPPORTED",
    "BREADCRUMBING_VERSION_1",
    "MIN_BREADCRUMBS_SUPPORTED",
    "GNSS_SATELLITE_ANY",
    "GNSS_SATELLITE_GPS",
    "GNSS_SATELLITE_GLONASS",
    "GNSS_SATELLITE_BEIDOU",
    "GNSS_SATELLITE_GALILEO",
    "GNSS_OPERMODE_ANY",
    "GNSS_OPERMODE_MSA",
    "GNSS_OPERMODE_MSB",
    "GNSS_OPERMODE_MSS",
    "GNSS_OPERMODE_CELLID",
    "GNSS_OPERMODE_AFLT",
    "GNSS_OPERMODE_OTDOA",
    "GNSS_NMEALOGGING_NONE",
    "GNSS_NMEALOGGING_ALL",
    "GNSS_FIXDETAIL_BASIC",
    "GNSS_FIXDETAIL_ACCURACY",
    "GNSS_FIXDETAIL_SATELLITE",
    "GNSS_MAXSATELLITE",
    "GNSS_GEOFENCESUPPORT_SUPPORTED",
    "GNSS_GEOFENCESUPPORT_CIRCLE",
    "LOCATION_API_VERSION",
    "GUID_DEVINTERFACE_GNSS",
    "Location",
    "DefaultLocation",
    "LatLongReport",
    "CivicAddressReport",
    "LatLongReportFactory",
    "CivicAddressReportFactory",
    "DispLatLongReport",
    "DispCivicAddressReport",
    "LOCATION_REPORT_STATUS",
    "REPORT_NOT_SUPPORTED",
    "REPORT_ERROR",
    "REPORT_ACCESS_DENIED",
    "REPORT_INITIALIZING",
    "REPORT_RUNNING",
    "ILocationReport",
    "ILatLongReport",
    "ICivicAddressReport",
    "ILocation",
    "ILocationPower",
    "IDefaultLocation",
    "ILocationEvents",
    "IDispLatLongReport",
    "IDispCivicAddressReport",
    "ILocationReportFactory",
    "ILatLongReportFactory",
    "ICivicAddressReportFactory",
    "_ILatLongReportFactoryEvents",
    "_ICivicAddressReportFactoryEvents",
    "GNSS_SUPL_VERSION",
    "GNSS_SUPL_VERSION_2",
    "GNSS_DEVICE_CAPABILITY",
    "GNSS_PLATFORM_CAPABILITY",
    "GNSS_DRIVERCOMMAND_TYPE",
    "GNSS_SetLocationServiceEnabled",
    "GNSS_SetLocationNIRequestAllowed",
    "GNSS_ForceSatelliteSystem",
    "GNSS_ForceOperationMode",
    "GNSS_ResetEngine",
    "GNSS_ClearAgnssData",
    "GNSS_SetSuplVersion",
    "GNSS_SetNMEALogging",
    "GNSS_SetUplServerAccessInterval",
    "GNSS_SetNiTimeoutInterval",
    "GNSS_ResetGeofencesTracking",
    "GNSS_SetSuplVersion2",
    "GNSS_CustomCommand",
    "GNSS_DRIVERCOMMAND_PARAM",
    "GNSS_FIXSESSIONTYPE",
    "GNSS_FixSession_SingleShot",
    "GNSS_FixSession_DistanceTracking",
    "GNSS_FixSession_ContinuousTracking",
    "GNSS_FixSession_LKG",
    "GNSS_SINGLESHOT_PARAM",
    "GNSS_DISTANCETRACKING_PARAM",
    "GNSS_CONTINUOUSTRACKING_PARAM",
    "GNSS_LKGFIX_PARAM",
    "GNSS_FIXSESSION_PARAM",
    "GNSS_STOPFIXSESSION_PARAM",
    "GNSS_FIXDATA_BASIC",
    "GNSS_FIXDATA_BASIC_2",
    "GNSS_FIXDATA_ACCURACY",
    "GNSS_FIXDATA_ACCURACY_2",
    "GNSS_SATELLITEINFO",
    "GNSS_FIXDATA_SATELLITE",
    "GNSS_FIXDATA",
    "GNSS_FIXDATA_2",
    "GNSS_BREADCRUMBING_PARAM",
    "GNSS_BREADCRUMBING_ALERT_DATA",
    "GNSS_BREADCRUMB_V1",
    "GNSS_BREADCRUMB_LIST",
    "GNSS_GEOREGIONTYPE",
    "GNSS_GeoRegion_Circle",
    "GNSS_GEOREGION_CIRCLE",
    "GNSS_GEOREGION",
    "GNSS_GEOFENCE_STATE",
    "GNSS_GeofenceState_Unknown",
    "GNSS_GeofenceState_Entered",
    "GNSS_GeofenceState_Exited",
    "GNSS_GEOFENCE_CREATE_PARAM",
    "GNSS_GEOFENCE_CREATE_RESPONSE",
    "GNSS_GEOFENCE_DELETE_PARAM",
    "GNSS_GEOFENCE_ALERT_DATA",
    "GNSS_GEOFENCES_TRACKINGSTATUS_DATA",
    "GNSS_EVENT_TYPE",
    "GNSS_Event_FixAvailable",
    "GNSS_Event_RequireAgnss",
    "GNSS_Event_Error",
    "GNSS_Event_NiRequest",
    "GNSS_Event_NmeaData",
    "GNSS_Event_GeofenceAlertData",
    "GNSS_Event_GeofencesTrackingStatus",
    "GNSS_Event_DriverRequest",
    "GNSS_Event_BreadcrumbAlertEvent",
    "GNSS_Event_FixAvailable_2",
    "GNSS_Event_Custom",
    "GNSS_ERRORINFO",
    "GNSS_NMEA_DATA",
    "GNSS_AGNSS_REQUEST_TYPE",
    "GNSS_AGNSS_TimeInjection",
    "GNSS_AGNSS_PositionInjection",
    "GNSS_AGNSS_BlobInjection",
    "GNSS_AGNSS_REQUEST_PARAM",
    "GNSS_NI_PLANE_TYPE",
    "GNSS_NI_SUPL",
    "GNSS_NI_CP",
    "GNSS_NI_V2UPL",
    "GNSS_NI_REQUEST_TYPE",
    "GNSS_NI_Request_SingleShot",
    "GNSS_NI_Request_AreaTrigger",
    "GNSS_NI_NOTIFICATION_TYPE",
    "GNSS_NI_NoNotifyNoVerify",
    "GNSS_NI_NotifyOnly",
    "GNSS_NI_NotifyVerifyDefaultAllow",
    "GNSS_NI_NotifyVerifyDefaultNotAllow",
    "GNSS_NI_PrivacyOverride",
    "GNSS_SUPL_NI_INFO",
    "GNSS_CP_NI_INFO",
    "GNSS_V2UPL_NI_INFO",
    "GNSS_NI_REQUEST_PARAM",
    "GNSS_DRIVER_REQUEST",
    "SUPL_CONFIG_DATA",
    "GNSS_DRIVER_REQUEST_DATA",
    "GNSS_EVENT",
    "GNSS_EVENT_2",
    "GNSS_AGNSS_INJECTTIME",
    "GNSS_AGNSS_INJECTPOSITION",
    "GNSS_AGNSS_INJECTBLOB",
    "GNSS_AGNSS_INJECT",
    "GNSS_SUPL_HSLP_CONFIG",
    "GNSS_SUPL_CERT_ACTION",
    "GNSS_Supl_Cert_Inject",
    "GNSS_Supl_Cert_Delete",
    "GNSS_Supl_Cert_Purge",
    "GNSS_SUPL_CERT_CONFIG",
    "GNSS_V2UPL_CONFIG",
    "GNSS_NI_USER_RESPONSE",
    "GNSS_Ni_UserResponseAccept",
    "GNSS_Ni_UserResponseDeny",
    "GNSS_Ni_UserResponseTimeout",
    "GNSS_NI_RESPONSE",
    "GNSS_CWTESTDATA",
    "GNSS_SELFTESTCONFIG",
    "GNSS_SELFTESTRESULT",
    "GNSS_CHIPSETINFO",
]
