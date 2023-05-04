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
import Windows.Devices.Sensors
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics.Display
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class Accelerometer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IAccelerometer
    _classid_ = 'Windows.Devices.Sensors.Accelerometer'
    @winrt_mixinmethod
    def GetCurrentReading(self: Windows.Devices.Sensors.IAccelerometer) -> Windows.Devices.Sensors.AccelerometerReading: ...
    @winrt_mixinmethod
    def get_MinimumReportInterval(self: Windows.Devices.Sensors.IAccelerometer) -> UInt32: ...
    @winrt_mixinmethod
    def put_ReportInterval(self: Windows.Devices.Sensors.IAccelerometer, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportInterval(self: Windows.Devices.Sensors.IAccelerometer) -> UInt32: ...
    @winrt_mixinmethod
    def add_ReadingChanged(self: Windows.Devices.Sensors.IAccelerometer, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Accelerometer, Windows.Devices.Sensors.AccelerometerReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadingChanged(self: Windows.Devices.Sensors.IAccelerometer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Shaken(self: Windows.Devices.Sensors.IAccelerometer, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Accelerometer, Windows.Devices.Sensors.AccelerometerShakenEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Shaken(self: Windows.Devices.Sensors.IAccelerometer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sensors.IAccelerometerDeviceId) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ReadingTransform(self: Windows.Devices.Sensors.IAccelerometer2, value: Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_mixinmethod
    def get_ReadingTransform(self: Windows.Devices.Sensors.IAccelerometer2) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_mixinmethod
    def put_ReportLatency(self: Windows.Devices.Sensors.IAccelerometer3, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportLatency(self: Windows.Devices.Sensors.IAccelerometer3) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxBatchSize(self: Windows.Devices.Sensors.IAccelerometer3) -> UInt32: ...
    @winrt_mixinmethod
    def get_ReadingType(self: Windows.Devices.Sensors.IAccelerometer4) -> Windows.Devices.Sensors.AccelerometerReadingType: ...
    @winrt_mixinmethod
    def get_ReportThreshold(self: Windows.Devices.Sensors.IAccelerometer5) -> Windows.Devices.Sensors.AccelerometerDataThreshold: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Sensors.IAccelerometerStatics3, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.Accelerometer]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Sensors.IAccelerometerStatics3, readingType: Windows.Devices.Sensors.AccelerometerReadingType) -> WinRT_String: ...
    @winrt_classmethod
    def GetDefaultWithAccelerometerReadingType(cls: Windows.Devices.Sensors.IAccelerometerStatics2, readingType: Windows.Devices.Sensors.AccelerometerReadingType) -> Windows.Devices.Sensors.Accelerometer: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Devices.Sensors.IAccelerometerStatics) -> Windows.Devices.Sensors.Accelerometer: ...
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
    DeviceId = property(get_DeviceId, None)
    ReadingTransform = property(get_ReadingTransform, put_ReadingTransform)
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
    ReadingType = property(get_ReadingType, None)
    ReportThreshold = property(get_ReportThreshold, None)
class AccelerometerDataThreshold(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IAccelerometerDataThreshold
    _classid_ = 'Windows.Devices.Sensors.AccelerometerDataThreshold'
    @winrt_mixinmethod
    def get_XAxisInGForce(self: Windows.Devices.Sensors.IAccelerometerDataThreshold) -> Double: ...
    @winrt_mixinmethod
    def put_XAxisInGForce(self: Windows.Devices.Sensors.IAccelerometerDataThreshold, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_YAxisInGForce(self: Windows.Devices.Sensors.IAccelerometerDataThreshold) -> Double: ...
    @winrt_mixinmethod
    def put_YAxisInGForce(self: Windows.Devices.Sensors.IAccelerometerDataThreshold, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ZAxisInGForce(self: Windows.Devices.Sensors.IAccelerometerDataThreshold) -> Double: ...
    @winrt_mixinmethod
    def put_ZAxisInGForce(self: Windows.Devices.Sensors.IAccelerometerDataThreshold, value: Double) -> Void: ...
    XAxisInGForce = property(get_XAxisInGForce, put_XAxisInGForce)
    YAxisInGForce = property(get_YAxisInGForce, put_YAxisInGForce)
    ZAxisInGForce = property(get_ZAxisInGForce, put_ZAxisInGForce)
class AccelerometerReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IAccelerometerReading
    _classid_ = 'Windows.Devices.Sensors.AccelerometerReading'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sensors.IAccelerometerReading) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_AccelerationX(self: Windows.Devices.Sensors.IAccelerometerReading) -> Double: ...
    @winrt_mixinmethod
    def get_AccelerationY(self: Windows.Devices.Sensors.IAccelerometerReading) -> Double: ...
    @winrt_mixinmethod
    def get_AccelerationZ(self: Windows.Devices.Sensors.IAccelerometerReading) -> Double: ...
    @winrt_mixinmethod
    def get_PerformanceCount(self: Windows.Devices.Sensors.IAccelerometerReading2) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Sensors.IAccelerometerReading2) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Timestamp = property(get_Timestamp, None)
    AccelerationX = property(get_AccelerationX, None)
    AccelerationY = property(get_AccelerationY, None)
    AccelerationZ = property(get_AccelerationZ, None)
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
class AccelerometerReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IAccelerometerReadingChangedEventArgs
    _classid_ = 'Windows.Devices.Sensors.AccelerometerReadingChangedEventArgs'
    @winrt_mixinmethod
    def get_Reading(self: Windows.Devices.Sensors.IAccelerometerReadingChangedEventArgs) -> Windows.Devices.Sensors.AccelerometerReading: ...
    Reading = property(get_Reading, None)
AccelerometerReadingType = Int32
AccelerometerReadingType_Standard: AccelerometerReadingType = 0
AccelerometerReadingType_Linear: AccelerometerReadingType = 1
AccelerometerReadingType_Gravity: AccelerometerReadingType = 2
class AccelerometerShakenEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IAccelerometerShakenEventArgs
    _classid_ = 'Windows.Devices.Sensors.AccelerometerShakenEventArgs'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sensors.IAccelerometerShakenEventArgs) -> Windows.Foundation.DateTime: ...
    Timestamp = property(get_Timestamp, None)
class ActivitySensor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IActivitySensor
    _classid_ = 'Windows.Devices.Sensors.ActivitySensor'
    @winrt_mixinmethod
    def GetCurrentReadingAsync(self: Windows.Devices.Sensors.IActivitySensor) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.ActivitySensorReading]: ...
    @winrt_mixinmethod
    def get_SubscribedActivities(self: Windows.Devices.Sensors.IActivitySensor) -> Windows.Foundation.Collections.IVector[Windows.Devices.Sensors.ActivityType]: ...
    @winrt_mixinmethod
    def get_PowerInMilliwatts(self: Windows.Devices.Sensors.IActivitySensor) -> Double: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sensors.IActivitySensor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SupportedActivities(self: Windows.Devices.Sensors.IActivitySensor) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Sensors.ActivityType]: ...
    @winrt_mixinmethod
    def get_MinimumReportInterval(self: Windows.Devices.Sensors.IActivitySensor) -> UInt32: ...
    @winrt_mixinmethod
    def add_ReadingChanged(self: Windows.Devices.Sensors.IActivitySensor, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.ActivitySensor, Windows.Devices.Sensors.ActivitySensorReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadingChanged(self: Windows.Devices.Sensors.IActivitySensor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.Sensors.IActivitySensorStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.ActivitySensor]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Sensors.IActivitySensorStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Sensors.IActivitySensorStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.ActivitySensor]: ...
    @winrt_classmethod
    def GetSystemHistoryAsync(cls: Windows.Devices.Sensors.IActivitySensorStatics, fromTime: Windows.Foundation.DateTime) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sensors.ActivitySensorReading]]: ...
    @winrt_classmethod
    def GetSystemHistoryWithDurationAsync(cls: Windows.Devices.Sensors.IActivitySensorStatics, fromTime: Windows.Foundation.DateTime, duration: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sensors.ActivitySensorReading]]: ...
    SubscribedActivities = property(get_SubscribedActivities, None)
    PowerInMilliwatts = property(get_PowerInMilliwatts, None)
    DeviceId = property(get_DeviceId, None)
    SupportedActivities = property(get_SupportedActivities, None)
    MinimumReportInterval = property(get_MinimumReportInterval, None)
class ActivitySensorReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IActivitySensorReading
    _classid_ = 'Windows.Devices.Sensors.ActivitySensorReading'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sensors.IActivitySensorReading) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Activity(self: Windows.Devices.Sensors.IActivitySensorReading) -> Windows.Devices.Sensors.ActivityType: ...
    @winrt_mixinmethod
    def get_Confidence(self: Windows.Devices.Sensors.IActivitySensorReading) -> Windows.Devices.Sensors.ActivitySensorReadingConfidence: ...
    Timestamp = property(get_Timestamp, None)
    Activity = property(get_Activity, None)
    Confidence = property(get_Confidence, None)
class ActivitySensorReadingChangeReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IActivitySensorReadingChangeReport
    _classid_ = 'Windows.Devices.Sensors.ActivitySensorReadingChangeReport'
    @winrt_mixinmethod
    def get_Reading(self: Windows.Devices.Sensors.IActivitySensorReadingChangeReport) -> Windows.Devices.Sensors.ActivitySensorReading: ...
    Reading = property(get_Reading, None)
class ActivitySensorReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IActivitySensorReadingChangedEventArgs
    _classid_ = 'Windows.Devices.Sensors.ActivitySensorReadingChangedEventArgs'
    @winrt_mixinmethod
    def get_Reading(self: Windows.Devices.Sensors.IActivitySensorReadingChangedEventArgs) -> Windows.Devices.Sensors.ActivitySensorReading: ...
    Reading = property(get_Reading, None)
ActivitySensorReadingConfidence = Int32
ActivitySensorReadingConfidence_High: ActivitySensorReadingConfidence = 0
ActivitySensorReadingConfidence_Low: ActivitySensorReadingConfidence = 1
class ActivitySensorTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IActivitySensorTriggerDetails
    _classid_ = 'Windows.Devices.Sensors.ActivitySensorTriggerDetails'
    @winrt_mixinmethod
    def ReadReports(self: Windows.Devices.Sensors.IActivitySensorTriggerDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Sensors.ActivitySensorReadingChangeReport]: ...
ActivityType = Int32
ActivityType_Unknown: ActivityType = 0
ActivityType_Idle: ActivityType = 1
ActivityType_Stationary: ActivityType = 2
ActivityType_Fidgeting: ActivityType = 3
ActivityType_Walking: ActivityType = 4
ActivityType_Running: ActivityType = 5
ActivityType_InVehicle: ActivityType = 6
ActivityType_Biking: ActivityType = 7
class Altimeter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IAltimeter
    _classid_ = 'Windows.Devices.Sensors.Altimeter'
    @winrt_mixinmethod
    def GetCurrentReading(self: Windows.Devices.Sensors.IAltimeter) -> Windows.Devices.Sensors.AltimeterReading: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sensors.IAltimeter) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MinimumReportInterval(self: Windows.Devices.Sensors.IAltimeter) -> UInt32: ...
    @winrt_mixinmethod
    def put_ReportInterval(self: Windows.Devices.Sensors.IAltimeter, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportInterval(self: Windows.Devices.Sensors.IAltimeter) -> UInt32: ...
    @winrt_mixinmethod
    def add_ReadingChanged(self: Windows.Devices.Sensors.IAltimeter, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Altimeter, Windows.Devices.Sensors.AltimeterReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadingChanged(self: Windows.Devices.Sensors.IAltimeter, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_ReportLatency(self: Windows.Devices.Sensors.IAltimeter2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportLatency(self: Windows.Devices.Sensors.IAltimeter2) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxBatchSize(self: Windows.Devices.Sensors.IAltimeter2) -> UInt32: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Devices.Sensors.IAltimeterStatics) -> Windows.Devices.Sensors.Altimeter: ...
    DeviceId = property(get_DeviceId, None)
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
class AltimeterReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IAltimeterReading
    _classid_ = 'Windows.Devices.Sensors.AltimeterReading'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sensors.IAltimeterReading) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_AltitudeChangeInMeters(self: Windows.Devices.Sensors.IAltimeterReading) -> Double: ...
    @winrt_mixinmethod
    def get_PerformanceCount(self: Windows.Devices.Sensors.IAltimeterReading2) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Sensors.IAltimeterReading2) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Timestamp = property(get_Timestamp, None)
    AltitudeChangeInMeters = property(get_AltitudeChangeInMeters, None)
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
class AltimeterReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IAltimeterReadingChangedEventArgs
    _classid_ = 'Windows.Devices.Sensors.AltimeterReadingChangedEventArgs'
    @winrt_mixinmethod
    def get_Reading(self: Windows.Devices.Sensors.IAltimeterReadingChangedEventArgs) -> Windows.Devices.Sensors.AltimeterReading: ...
    Reading = property(get_Reading, None)
class Barometer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IBarometer
    _classid_ = 'Windows.Devices.Sensors.Barometer'
    @winrt_mixinmethod
    def GetCurrentReading(self: Windows.Devices.Sensors.IBarometer) -> Windows.Devices.Sensors.BarometerReading: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sensors.IBarometer) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MinimumReportInterval(self: Windows.Devices.Sensors.IBarometer) -> UInt32: ...
    @winrt_mixinmethod
    def put_ReportInterval(self: Windows.Devices.Sensors.IBarometer, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportInterval(self: Windows.Devices.Sensors.IBarometer) -> UInt32: ...
    @winrt_mixinmethod
    def add_ReadingChanged(self: Windows.Devices.Sensors.IBarometer, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Barometer, Windows.Devices.Sensors.BarometerReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadingChanged(self: Windows.Devices.Sensors.IBarometer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_ReportLatency(self: Windows.Devices.Sensors.IBarometer2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportLatency(self: Windows.Devices.Sensors.IBarometer2) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxBatchSize(self: Windows.Devices.Sensors.IBarometer2) -> UInt32: ...
    @winrt_mixinmethod
    def get_ReportThreshold(self: Windows.Devices.Sensors.IBarometer3) -> Windows.Devices.Sensors.BarometerDataThreshold: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Sensors.IBarometerStatics2, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.Barometer]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Sensors.IBarometerStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Devices.Sensors.IBarometerStatics) -> Windows.Devices.Sensors.Barometer: ...
    DeviceId = property(get_DeviceId, None)
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
    ReportThreshold = property(get_ReportThreshold, None)
class BarometerDataThreshold(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IBarometerDataThreshold
    _classid_ = 'Windows.Devices.Sensors.BarometerDataThreshold'
    @winrt_mixinmethod
    def get_Hectopascals(self: Windows.Devices.Sensors.IBarometerDataThreshold) -> Double: ...
    @winrt_mixinmethod
    def put_Hectopascals(self: Windows.Devices.Sensors.IBarometerDataThreshold, value: Double) -> Void: ...
    Hectopascals = property(get_Hectopascals, put_Hectopascals)
class BarometerReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IBarometerReading
    _classid_ = 'Windows.Devices.Sensors.BarometerReading'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sensors.IBarometerReading) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_StationPressureInHectopascals(self: Windows.Devices.Sensors.IBarometerReading) -> Double: ...
    @winrt_mixinmethod
    def get_PerformanceCount(self: Windows.Devices.Sensors.IBarometerReading2) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Sensors.IBarometerReading2) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Timestamp = property(get_Timestamp, None)
    StationPressureInHectopascals = property(get_StationPressureInHectopascals, None)
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
class BarometerReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IBarometerReadingChangedEventArgs
    _classid_ = 'Windows.Devices.Sensors.BarometerReadingChangedEventArgs'
    @winrt_mixinmethod
    def get_Reading(self: Windows.Devices.Sensors.IBarometerReadingChangedEventArgs) -> Windows.Devices.Sensors.BarometerReading: ...
    Reading = property(get_Reading, None)
class Compass(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.ICompass
    _classid_ = 'Windows.Devices.Sensors.Compass'
    @winrt_mixinmethod
    def GetCurrentReading(self: Windows.Devices.Sensors.ICompass) -> Windows.Devices.Sensors.CompassReading: ...
    @winrt_mixinmethod
    def get_MinimumReportInterval(self: Windows.Devices.Sensors.ICompass) -> UInt32: ...
    @winrt_mixinmethod
    def put_ReportInterval(self: Windows.Devices.Sensors.ICompass, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportInterval(self: Windows.Devices.Sensors.ICompass) -> UInt32: ...
    @winrt_mixinmethod
    def add_ReadingChanged(self: Windows.Devices.Sensors.ICompass, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Compass, Windows.Devices.Sensors.CompassReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadingChanged(self: Windows.Devices.Sensors.ICompass, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sensors.ICompassDeviceId) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ReadingTransform(self: Windows.Devices.Sensors.ICompass2, value: Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_mixinmethod
    def get_ReadingTransform(self: Windows.Devices.Sensors.ICompass2) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_mixinmethod
    def put_ReportLatency(self: Windows.Devices.Sensors.ICompass3, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportLatency(self: Windows.Devices.Sensors.ICompass3) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxBatchSize(self: Windows.Devices.Sensors.ICompass3) -> UInt32: ...
    @winrt_mixinmethod
    def get_ReportThreshold(self: Windows.Devices.Sensors.ICompass4) -> Windows.Devices.Sensors.CompassDataThreshold: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Sensors.ICompassStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Sensors.ICompassStatics2, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.Compass]: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Devices.Sensors.ICompassStatics) -> Windows.Devices.Sensors.Compass: ...
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
    DeviceId = property(get_DeviceId, None)
    ReadingTransform = property(get_ReadingTransform, put_ReadingTransform)
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
    ReportThreshold = property(get_ReportThreshold, None)
class CompassDataThreshold(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.ICompassDataThreshold
    _classid_ = 'Windows.Devices.Sensors.CompassDataThreshold'
    @winrt_mixinmethod
    def get_Degrees(self: Windows.Devices.Sensors.ICompassDataThreshold) -> Double: ...
    @winrt_mixinmethod
    def put_Degrees(self: Windows.Devices.Sensors.ICompassDataThreshold, value: Double) -> Void: ...
    Degrees = property(get_Degrees, put_Degrees)
class CompassReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.ICompassReading
    _classid_ = 'Windows.Devices.Sensors.CompassReading'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sensors.ICompassReading) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_HeadingMagneticNorth(self: Windows.Devices.Sensors.ICompassReading) -> Double: ...
    @winrt_mixinmethod
    def get_HeadingTrueNorth(self: Windows.Devices.Sensors.ICompassReading) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_HeadingAccuracy(self: Windows.Devices.Sensors.ICompassReadingHeadingAccuracy) -> Windows.Devices.Sensors.MagnetometerAccuracy: ...
    @winrt_mixinmethod
    def get_PerformanceCount(self: Windows.Devices.Sensors.ICompassReading2) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Sensors.ICompassReading2) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Timestamp = property(get_Timestamp, None)
    HeadingMagneticNorth = property(get_HeadingMagneticNorth, None)
    HeadingTrueNorth = property(get_HeadingTrueNorth, None)
    HeadingAccuracy = property(get_HeadingAccuracy, None)
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
class CompassReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.ICompassReadingChangedEventArgs
    _classid_ = 'Windows.Devices.Sensors.CompassReadingChangedEventArgs'
    @winrt_mixinmethod
    def get_Reading(self: Windows.Devices.Sensors.ICompassReadingChangedEventArgs) -> Windows.Devices.Sensors.CompassReading: ...
    Reading = property(get_Reading, None)
class Gyrometer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IGyrometer
    _classid_ = 'Windows.Devices.Sensors.Gyrometer'
    @winrt_mixinmethod
    def GetCurrentReading(self: Windows.Devices.Sensors.IGyrometer) -> Windows.Devices.Sensors.GyrometerReading: ...
    @winrt_mixinmethod
    def get_MinimumReportInterval(self: Windows.Devices.Sensors.IGyrometer) -> UInt32: ...
    @winrt_mixinmethod
    def put_ReportInterval(self: Windows.Devices.Sensors.IGyrometer, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportInterval(self: Windows.Devices.Sensors.IGyrometer) -> UInt32: ...
    @winrt_mixinmethod
    def add_ReadingChanged(self: Windows.Devices.Sensors.IGyrometer, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Gyrometer, Windows.Devices.Sensors.GyrometerReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadingChanged(self: Windows.Devices.Sensors.IGyrometer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sensors.IGyrometerDeviceId) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ReadingTransform(self: Windows.Devices.Sensors.IGyrometer2, value: Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_mixinmethod
    def get_ReadingTransform(self: Windows.Devices.Sensors.IGyrometer2) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_mixinmethod
    def put_ReportLatency(self: Windows.Devices.Sensors.IGyrometer3, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportLatency(self: Windows.Devices.Sensors.IGyrometer3) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxBatchSize(self: Windows.Devices.Sensors.IGyrometer3) -> UInt32: ...
    @winrt_mixinmethod
    def get_ReportThreshold(self: Windows.Devices.Sensors.IGyrometer4) -> Windows.Devices.Sensors.GyrometerDataThreshold: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Sensors.IGyrometerStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Sensors.IGyrometerStatics2, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.Gyrometer]: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Devices.Sensors.IGyrometerStatics) -> Windows.Devices.Sensors.Gyrometer: ...
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
    DeviceId = property(get_DeviceId, None)
    ReadingTransform = property(get_ReadingTransform, put_ReadingTransform)
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
    ReportThreshold = property(get_ReportThreshold, None)
class GyrometerDataThreshold(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IGyrometerDataThreshold
    _classid_ = 'Windows.Devices.Sensors.GyrometerDataThreshold'
    @winrt_mixinmethod
    def get_XAxisInDegreesPerSecond(self: Windows.Devices.Sensors.IGyrometerDataThreshold) -> Double: ...
    @winrt_mixinmethod
    def put_XAxisInDegreesPerSecond(self: Windows.Devices.Sensors.IGyrometerDataThreshold, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_YAxisInDegreesPerSecond(self: Windows.Devices.Sensors.IGyrometerDataThreshold) -> Double: ...
    @winrt_mixinmethod
    def put_YAxisInDegreesPerSecond(self: Windows.Devices.Sensors.IGyrometerDataThreshold, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ZAxisInDegreesPerSecond(self: Windows.Devices.Sensors.IGyrometerDataThreshold) -> Double: ...
    @winrt_mixinmethod
    def put_ZAxisInDegreesPerSecond(self: Windows.Devices.Sensors.IGyrometerDataThreshold, value: Double) -> Void: ...
    XAxisInDegreesPerSecond = property(get_XAxisInDegreesPerSecond, put_XAxisInDegreesPerSecond)
    YAxisInDegreesPerSecond = property(get_YAxisInDegreesPerSecond, put_YAxisInDegreesPerSecond)
    ZAxisInDegreesPerSecond = property(get_ZAxisInDegreesPerSecond, put_ZAxisInDegreesPerSecond)
class GyrometerReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IGyrometerReading
    _classid_ = 'Windows.Devices.Sensors.GyrometerReading'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sensors.IGyrometerReading) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_AngularVelocityX(self: Windows.Devices.Sensors.IGyrometerReading) -> Double: ...
    @winrt_mixinmethod
    def get_AngularVelocityY(self: Windows.Devices.Sensors.IGyrometerReading) -> Double: ...
    @winrt_mixinmethod
    def get_AngularVelocityZ(self: Windows.Devices.Sensors.IGyrometerReading) -> Double: ...
    @winrt_mixinmethod
    def get_PerformanceCount(self: Windows.Devices.Sensors.IGyrometerReading2) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Sensors.IGyrometerReading2) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Timestamp = property(get_Timestamp, None)
    AngularVelocityX = property(get_AngularVelocityX, None)
    AngularVelocityY = property(get_AngularVelocityY, None)
    AngularVelocityZ = property(get_AngularVelocityZ, None)
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
class GyrometerReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IGyrometerReadingChangedEventArgs
    _classid_ = 'Windows.Devices.Sensors.GyrometerReadingChangedEventArgs'
    @winrt_mixinmethod
    def get_Reading(self: Windows.Devices.Sensors.IGyrometerReadingChangedEventArgs) -> Windows.Devices.Sensors.GyrometerReading: ...
    Reading = property(get_Reading, None)
class HingeAngleReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IHingeAngleReading
    _classid_ = 'Windows.Devices.Sensors.HingeAngleReading'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sensors.IHingeAngleReading) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_AngleInDegrees(self: Windows.Devices.Sensors.IHingeAngleReading) -> Double: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Sensors.IHingeAngleReading) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Timestamp = property(get_Timestamp, None)
    AngleInDegrees = property(get_AngleInDegrees, None)
    Properties = property(get_Properties, None)
class HingeAngleSensor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IHingeAngleSensor
    _classid_ = 'Windows.Devices.Sensors.HingeAngleSensor'
    @winrt_mixinmethod
    def GetCurrentReadingAsync(self: Windows.Devices.Sensors.IHingeAngleSensor) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.HingeAngleReading]: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sensors.IHingeAngleSensor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MinReportThresholdInDegrees(self: Windows.Devices.Sensors.IHingeAngleSensor) -> Double: ...
    @winrt_mixinmethod
    def get_ReportThresholdInDegrees(self: Windows.Devices.Sensors.IHingeAngleSensor) -> Double: ...
    @winrt_mixinmethod
    def put_ReportThresholdInDegrees(self: Windows.Devices.Sensors.IHingeAngleSensor, value: Double) -> Void: ...
    @winrt_mixinmethod
    def add_ReadingChanged(self: Windows.Devices.Sensors.IHingeAngleSensor, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.HingeAngleSensor, Windows.Devices.Sensors.HingeAngleSensorReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadingChanged(self: Windows.Devices.Sensors.IHingeAngleSensor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Sensors.IHingeAngleSensorStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.Sensors.IHingeAngleSensorStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.HingeAngleSensor]: ...
    @winrt_classmethod
    def GetRelatedToAdjacentPanelsAsync(cls: Windows.Devices.Sensors.IHingeAngleSensorStatics, firstPanelId: WinRT_String, secondPanelId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.HingeAngleSensor]: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Sensors.IHingeAngleSensorStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.HingeAngleSensor]: ...
    DeviceId = property(get_DeviceId, None)
    MinReportThresholdInDegrees = property(get_MinReportThresholdInDegrees, None)
    ReportThresholdInDegrees = property(get_ReportThresholdInDegrees, put_ReportThresholdInDegrees)
class HingeAngleSensorReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IHingeAngleSensorReadingChangedEventArgs
    _classid_ = 'Windows.Devices.Sensors.HingeAngleSensorReadingChangedEventArgs'
    @winrt_mixinmethod
    def get_Reading(self: Windows.Devices.Sensors.IHingeAngleSensorReadingChangedEventArgs) -> Windows.Devices.Sensors.HingeAngleReading: ...
    Reading = property(get_Reading, None)
HumanEngagement = Int32
HumanEngagement_Unknown: HumanEngagement = 0
HumanEngagement_Engaged: HumanEngagement = 1
HumanEngagement_Unengaged: HumanEngagement = 2
HumanPresence = Int32
HumanPresence_Unknown: HumanPresence = 0
HumanPresence_Present: HumanPresence = 1
HumanPresence_NotPresent: HumanPresence = 2
class HumanPresenceFeatures(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IHumanPresenceFeatures
    _classid_ = 'Windows.Devices.Sensors.HumanPresenceFeatures'
    @winrt_mixinmethod
    def get_SensorId(self: Windows.Devices.Sensors.IHumanPresenceFeatures) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SupportedWakeOrLockDistancesInMillimeters(self: Windows.Devices.Sensors.IHumanPresenceFeatures) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_mixinmethod
    def get_IsWakeOnApproachSupported(self: Windows.Devices.Sensors.IHumanPresenceFeatures) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsLockOnLeaveSupported(self: Windows.Devices.Sensors.IHumanPresenceFeatures) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsAttentionAwareDimmingSupported(self: Windows.Devices.Sensors.IHumanPresenceFeatures) -> Boolean: ...
    SensorId = property(get_SensorId, None)
    SupportedWakeOrLockDistancesInMillimeters = property(get_SupportedWakeOrLockDistancesInMillimeters, None)
    IsWakeOnApproachSupported = property(get_IsWakeOnApproachSupported, None)
    IsLockOnLeaveSupported = property(get_IsLockOnLeaveSupported, None)
    IsAttentionAwareDimmingSupported = property(get_IsAttentionAwareDimmingSupported, None)
class HumanPresenceSensor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IHumanPresenceSensor
    _classid_ = 'Windows.Devices.Sensors.HumanPresenceSensor'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sensors.IHumanPresenceSensor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MaxDetectableDistanceInMillimeters(self: Windows.Devices.Sensors.IHumanPresenceSensor) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_MinDetectableDistanceInMillimeters(self: Windows.Devices.Sensors.IHumanPresenceSensor) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def GetCurrentReading(self: Windows.Devices.Sensors.IHumanPresenceSensor) -> Windows.Devices.Sensors.HumanPresenceSensorReading: ...
    @winrt_mixinmethod
    def add_ReadingChanged(self: Windows.Devices.Sensors.IHumanPresenceSensor, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.HumanPresenceSensor, Windows.Devices.Sensors.HumanPresenceSensorReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadingChanged(self: Windows.Devices.Sensors.IHumanPresenceSensor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Sensors.IHumanPresenceSensorStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Sensors.IHumanPresenceSensorStatics, sensorId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.HumanPresenceSensor]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.Sensors.IHumanPresenceSensorStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.HumanPresenceSensor]: ...
    DeviceId = property(get_DeviceId, None)
    MaxDetectableDistanceInMillimeters = property(get_MaxDetectableDistanceInMillimeters, None)
    MinDetectableDistanceInMillimeters = property(get_MinDetectableDistanceInMillimeters, None)
class HumanPresenceSensorReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IHumanPresenceSensorReading
    _classid_ = 'Windows.Devices.Sensors.HumanPresenceSensorReading'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sensors.IHumanPresenceSensorReading) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Presence(self: Windows.Devices.Sensors.IHumanPresenceSensorReading) -> Windows.Devices.Sensors.HumanPresence: ...
    @winrt_mixinmethod
    def get_Engagement(self: Windows.Devices.Sensors.IHumanPresenceSensorReading) -> Windows.Devices.Sensors.HumanEngagement: ...
    @winrt_mixinmethod
    def get_DistanceInMillimeters(self: Windows.Devices.Sensors.IHumanPresenceSensorReading) -> Windows.Foundation.IReference[UInt32]: ...
    Timestamp = property(get_Timestamp, None)
    Presence = property(get_Presence, None)
    Engagement = property(get_Engagement, None)
    DistanceInMillimeters = property(get_DistanceInMillimeters, None)
class HumanPresenceSensorReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IHumanPresenceSensorReadingChangedEventArgs
    _classid_ = 'Windows.Devices.Sensors.HumanPresenceSensorReadingChangedEventArgs'
    @winrt_mixinmethod
    def get_Reading(self: Windows.Devices.Sensors.IHumanPresenceSensorReadingChangedEventArgs) -> Windows.Devices.Sensors.HumanPresenceSensorReading: ...
    Reading = property(get_Reading, None)
class HumanPresenceSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IHumanPresenceSettings
    _classid_ = 'Windows.Devices.Sensors.HumanPresenceSettings'
    @winrt_mixinmethod
    def get_SensorId(self: Windows.Devices.Sensors.IHumanPresenceSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SensorId(self: Windows.Devices.Sensors.IHumanPresenceSettings, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsWakeOnApproachEnabled(self: Windows.Devices.Sensors.IHumanPresenceSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsWakeOnApproachEnabled(self: Windows.Devices.Sensors.IHumanPresenceSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_WakeOnApproachDistanceInMillimeters(self: Windows.Devices.Sensors.IHumanPresenceSettings) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_WakeOnApproachDistanceInMillimeters(self: Windows.Devices.Sensors.IHumanPresenceSettings, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_IsLockOnLeaveEnabled(self: Windows.Devices.Sensors.IHumanPresenceSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsLockOnLeaveEnabled(self: Windows.Devices.Sensors.IHumanPresenceSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_LockOnLeaveDistanceInMillimeters(self: Windows.Devices.Sensors.IHumanPresenceSettings) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_LockOnLeaveDistanceInMillimeters(self: Windows.Devices.Sensors.IHumanPresenceSettings, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def get_LockOnLeaveTimeout(self: Windows.Devices.Sensors.IHumanPresenceSettings) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_LockOnLeaveTimeout(self: Windows.Devices.Sensors.IHumanPresenceSettings, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_IsAttentionAwareDimmingEnabled(self: Windows.Devices.Sensors.IHumanPresenceSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAttentionAwareDimmingEnabled(self: Windows.Devices.Sensors.IHumanPresenceSettings, value: Boolean) -> Void: ...
    @winrt_classmethod
    def GetCurrentSettingsAsync(cls: Windows.Devices.Sensors.IHumanPresenceSettingsStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.HumanPresenceSettings]: ...
    @winrt_classmethod
    def GetCurrentSettings(cls: Windows.Devices.Sensors.IHumanPresenceSettingsStatics) -> Windows.Devices.Sensors.HumanPresenceSettings: ...
    @winrt_classmethod
    def UpdateSettingsAsync(cls: Windows.Devices.Sensors.IHumanPresenceSettingsStatics, settings: Windows.Devices.Sensors.HumanPresenceSettings) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def UpdateSettings(cls: Windows.Devices.Sensors.IHumanPresenceSettingsStatics, settings: Windows.Devices.Sensors.HumanPresenceSettings) -> Void: ...
    @winrt_classmethod
    def GetSupportedFeaturesForSensorIdAsync(cls: Windows.Devices.Sensors.IHumanPresenceSettingsStatics, sensorId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.HumanPresenceFeatures]: ...
    @winrt_classmethod
    def GetSupportedFeaturesForSensorId(cls: Windows.Devices.Sensors.IHumanPresenceSettingsStatics, sensorId: WinRT_String) -> Windows.Devices.Sensors.HumanPresenceFeatures: ...
    @winrt_classmethod
    def GetSupportedLockOnLeaveTimeouts(cls: Windows.Devices.Sensors.IHumanPresenceSettingsStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.TimeSpan]: ...
    @winrt_classmethod
    def add_SettingsChanged(cls: Windows.Devices.Sensors.IHumanPresenceSettingsStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_SettingsChanged(cls: Windows.Devices.Sensors.IHumanPresenceSettingsStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    SensorId = property(get_SensorId, put_SensorId)
    IsWakeOnApproachEnabled = property(get_IsWakeOnApproachEnabled, put_IsWakeOnApproachEnabled)
    WakeOnApproachDistanceInMillimeters = property(get_WakeOnApproachDistanceInMillimeters, put_WakeOnApproachDistanceInMillimeters)
    IsLockOnLeaveEnabled = property(get_IsLockOnLeaveEnabled, put_IsLockOnLeaveEnabled)
    LockOnLeaveDistanceInMillimeters = property(get_LockOnLeaveDistanceInMillimeters, put_LockOnLeaveDistanceInMillimeters)
    LockOnLeaveTimeout = property(get_LockOnLeaveTimeout, put_LockOnLeaveTimeout)
    IsAttentionAwareDimmingEnabled = property(get_IsAttentionAwareDimmingEnabled, put_IsAttentionAwareDimmingEnabled)
class IAccelerometer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{df184548-2711-4da7-8098-4b82205d3c7d}')
    @winrt_commethod(6)
    def GetCurrentReading(self) -> Windows.Devices.Sensors.AccelerometerReading: ...
    @winrt_commethod(7)
    def get_MinimumReportInterval(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_ReportInterval(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_ReportInterval(self) -> UInt32: ...
    @winrt_commethod(10)
    def add_ReadingChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Accelerometer, Windows.Devices.Sensors.AccelerometerReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ReadingChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_Shaken(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Accelerometer, Windows.Devices.Sensors.AccelerometerShakenEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Shaken(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
class IAccelerometer2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e8f092ee-4964-401a-b602-220d7153c60a}')
    @winrt_commethod(6)
    def put_ReadingTransform(self, value: Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_commethod(7)
    def get_ReadingTransform(self) -> Windows.Graphics.Display.DisplayOrientations: ...
    ReadingTransform = property(get_ReadingTransform, put_ReadingTransform)
class IAccelerometer3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{87e0022a-ed80-49eb-bf8a-a4ea31e5cd84}')
    @winrt_commethod(6)
    def put_ReportLatency(self, value: UInt32) -> Void: ...
    @winrt_commethod(7)
    def get_ReportLatency(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_MaxBatchSize(self) -> UInt32: ...
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
class IAccelerometer4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1d373c4f-42d3-45b2-8144-ab7fb665eb59}')
    @winrt_commethod(6)
    def get_ReadingType(self) -> Windows.Devices.Sensors.AccelerometerReadingType: ...
    ReadingType = property(get_ReadingType, None)
class IAccelerometer5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7e7e7021-def4-53a6-af43-806fd538edf6}')
    @winrt_commethod(6)
    def get_ReportThreshold(self) -> Windows.Devices.Sensors.AccelerometerDataThreshold: ...
    ReportThreshold = property(get_ReportThreshold, None)
class IAccelerometerDataThreshold(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f92c1b68-6320-5577-879e-9942621c3dd9}')
    @winrt_commethod(6)
    def get_XAxisInGForce(self) -> Double: ...
    @winrt_commethod(7)
    def put_XAxisInGForce(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_YAxisInGForce(self) -> Double: ...
    @winrt_commethod(9)
    def put_YAxisInGForce(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_ZAxisInGForce(self) -> Double: ...
    @winrt_commethod(11)
    def put_ZAxisInGForce(self, value: Double) -> Void: ...
    XAxisInGForce = property(get_XAxisInGForce, put_XAxisInGForce)
    YAxisInGForce = property(get_YAxisInGForce, put_YAxisInGForce)
    ZAxisInGForce = property(get_ZAxisInGForce, put_ZAxisInGForce)
class IAccelerometerDeviceId(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7eac64a9-97d5-446d-ab5a-917df9b96a2c}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IAccelerometerReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b9fe7acb-d351-40af-8bb6-7aa9ae641fb7}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_AccelerationX(self) -> Double: ...
    @winrt_commethod(8)
    def get_AccelerationY(self) -> Double: ...
    @winrt_commethod(9)
    def get_AccelerationZ(self) -> Double: ...
    Timestamp = property(get_Timestamp, None)
    AccelerationX = property(get_AccelerationX, None)
    AccelerationY = property(get_AccelerationY, None)
    AccelerationZ = property(get_AccelerationZ, None)
class IAccelerometerReading2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0a864aa2-15ae-4a40-be55-db58d7de7389}')
    @winrt_commethod(6)
    def get_PerformanceCount(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
class IAccelerometerReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0095c65b-b6ac-475a-9f44-8b32d35a3f25}')
    @winrt_commethod(6)
    def get_Reading(self) -> Windows.Devices.Sensors.AccelerometerReading: ...
    Reading = property(get_Reading, None)
class IAccelerometerShakenEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{95ff01d1-4a28-4f35-98e8-8178aae4084a}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    Timestamp = property(get_Timestamp, None)
class IAccelerometerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a5e28b74-5a87-4a2d-becc-0f906ea061dd}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Devices.Sensors.Accelerometer: ...
class IAccelerometerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c4c4842f-d86b-4685-b2d7-3396f798d57b}')
    @winrt_commethod(6)
    def GetDefaultWithAccelerometerReadingType(self, readingType: Windows.Devices.Sensors.AccelerometerReadingType) -> Windows.Devices.Sensors.Accelerometer: ...
class IAccelerometerStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9de218cf-455d-4cf3-8200-70e1410340f8}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.Accelerometer]: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self, readingType: Windows.Devices.Sensors.AccelerometerReadingType) -> WinRT_String: ...
class IActivitySensor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{cd7a630c-fb5f-48eb-b09b-a2708d1c61ef}')
    @winrt_commethod(6)
    def GetCurrentReadingAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.ActivitySensorReading]: ...
    @winrt_commethod(7)
    def get_SubscribedActivities(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.Sensors.ActivityType]: ...
    @winrt_commethod(8)
    def get_PowerInMilliwatts(self) -> Double: ...
    @winrt_commethod(9)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_SupportedActivities(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Sensors.ActivityType]: ...
    @winrt_commethod(11)
    def get_MinimumReportInterval(self) -> UInt32: ...
    @winrt_commethod(12)
    def add_ReadingChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.ActivitySensor, Windows.Devices.Sensors.ActivitySensorReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_ReadingChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    SubscribedActivities = property(get_SubscribedActivities, None)
    PowerInMilliwatts = property(get_PowerInMilliwatts, None)
    DeviceId = property(get_DeviceId, None)
    SupportedActivities = property(get_SupportedActivities, None)
    MinimumReportInterval = property(get_MinimumReportInterval, None)
class IActivitySensorReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{85125a96-1472-40a2-b2ae-e1ef29226c78}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_Activity(self) -> Windows.Devices.Sensors.ActivityType: ...
    @winrt_commethod(8)
    def get_Confidence(self) -> Windows.Devices.Sensors.ActivitySensorReadingConfidence: ...
    Timestamp = property(get_Timestamp, None)
    Activity = property(get_Activity, None)
    Confidence = property(get_Confidence, None)
class IActivitySensorReadingChangeReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4f3c2915-d93b-47bd-960a-f20fb2f322b9}')
    @winrt_commethod(6)
    def get_Reading(self) -> Windows.Devices.Sensors.ActivitySensorReading: ...
    Reading = property(get_Reading, None)
class IActivitySensorReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{de386717-aeb6-4ec7-946a-d9cc19b951ec}')
    @winrt_commethod(6)
    def get_Reading(self) -> Windows.Devices.Sensors.ActivitySensorReading: ...
    Reading = property(get_Reading, None)
class IActivitySensorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a71e0e9d-ee8b-45d1-b25b-08cc0df92ab6}')
    @winrt_commethod(6)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.ActivitySensor]: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.ActivitySensor]: ...
    @winrt_commethod(9)
    def GetSystemHistoryAsync(self, fromTime: Windows.Foundation.DateTime) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sensors.ActivitySensorReading]]: ...
    @winrt_commethod(10)
    def GetSystemHistoryWithDurationAsync(self, fromTime: Windows.Foundation.DateTime, duration: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sensors.ActivitySensorReading]]: ...
class IActivitySensorTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2c9e6612-b9ca-4677-b263-243297f79d3a}')
    @winrt_commethod(6)
    def ReadReports(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Sensors.ActivitySensorReadingChangeReport]: ...
class IAltimeter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{72f057fd-8f04-49f1-b4a7-f4e363b701a2}')
    @winrt_commethod(6)
    def GetCurrentReading(self) -> Windows.Devices.Sensors.AltimeterReading: ...
    @winrt_commethod(7)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_MinimumReportInterval(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_ReportInterval(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_ReportInterval(self) -> UInt32: ...
    @winrt_commethod(11)
    def add_ReadingChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Altimeter, Windows.Devices.Sensors.AltimeterReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_ReadingChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
class IAltimeter2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c9471bf9-2add-48f5-9f08-3d0c7660d938}')
    @winrt_commethod(6)
    def put_ReportLatency(self, value: UInt32) -> Void: ...
    @winrt_commethod(7)
    def get_ReportLatency(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_MaxBatchSize(self) -> UInt32: ...
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
class IAltimeterReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{fbe8ef73-7f5e-48c8-aa1a-f1f3befc1144}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_AltitudeChangeInMeters(self) -> Double: ...
    Timestamp = property(get_Timestamp, None)
    AltitudeChangeInMeters = property(get_AltitudeChangeInMeters, None)
class IAltimeterReading2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{543a1bd9-6d0b-42b2-bd69-bc8fae0f782c}')
    @winrt_commethod(6)
    def get_PerformanceCount(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
class IAltimeterReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7069d077-446d-47f7-998c-ebc23b45e4a2}')
    @winrt_commethod(6)
    def get_Reading(self) -> Windows.Devices.Sensors.AltimeterReading: ...
    Reading = property(get_Reading, None)
class IAltimeterStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9eb4d7c3-e5ac-47ce-8eef-d3718168c01f}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Devices.Sensors.Altimeter: ...
class IBarometer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{934475a8-78bf-452f-b017-f0209ce6dab4}')
    @winrt_commethod(6)
    def GetCurrentReading(self) -> Windows.Devices.Sensors.BarometerReading: ...
    @winrt_commethod(7)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_MinimumReportInterval(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_ReportInterval(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_ReportInterval(self) -> UInt32: ...
    @winrt_commethod(11)
    def add_ReadingChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Barometer, Windows.Devices.Sensors.BarometerReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_ReadingChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
class IBarometer2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{32bcc418-3eeb-4d04-9574-7633a8781f9f}')
    @winrt_commethod(6)
    def put_ReportLatency(self, value: UInt32) -> Void: ...
    @winrt_commethod(7)
    def get_ReportLatency(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_MaxBatchSize(self) -> UInt32: ...
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
class IBarometer3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0e35f0ea-02b5-5a04-b03d-822084863a54}')
    @winrt_commethod(6)
    def get_ReportThreshold(self) -> Windows.Devices.Sensors.BarometerDataThreshold: ...
    ReportThreshold = property(get_ReportThreshold, None)
class IBarometerDataThreshold(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{076b952c-cb62-5a90-a0d1-f85e4a936394}')
    @winrt_commethod(6)
    def get_Hectopascals(self) -> Double: ...
    @winrt_commethod(7)
    def put_Hectopascals(self, value: Double) -> Void: ...
    Hectopascals = property(get_Hectopascals, put_Hectopascals)
class IBarometerReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f5b9d2e6-1df6-4a1a-a7ad-321d4f5db247}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_StationPressureInHectopascals(self) -> Double: ...
    Timestamp = property(get_Timestamp, None)
    StationPressureInHectopascals = property(get_StationPressureInHectopascals, None)
class IBarometerReading2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{85a244eb-90c5-4875-891c-3865b4c357e7}')
    @winrt_commethod(6)
    def get_PerformanceCount(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
class IBarometerReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3d84945f-037b-404f-9bbb-6232d69543c3}')
    @winrt_commethod(6)
    def get_Reading(self) -> Windows.Devices.Sensors.BarometerReading: ...
    Reading = property(get_Reading, None)
class IBarometerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{286b270a-02e3-4f86-84fc-fdd892b5940f}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Devices.Sensors.Barometer: ...
class IBarometerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{8fc6b1e7-95ff-44ac-878e-d65c8308c34c}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.Barometer]: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self) -> WinRT_String: ...
class ICompass(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{292ffa94-1b45-403c-ba06-b106dba69a64}')
    @winrt_commethod(6)
    def GetCurrentReading(self) -> Windows.Devices.Sensors.CompassReading: ...
    @winrt_commethod(7)
    def get_MinimumReportInterval(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_ReportInterval(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_ReportInterval(self) -> UInt32: ...
    @winrt_commethod(10)
    def add_ReadingChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Compass, Windows.Devices.Sensors.CompassReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ReadingChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
class ICompass2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{36f26d09-c7d7-434f-b461-979ddfc2322f}')
    @winrt_commethod(6)
    def put_ReadingTransform(self, value: Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_commethod(7)
    def get_ReadingTransform(self) -> Windows.Graphics.Display.DisplayOrientations: ...
    ReadingTransform = property(get_ReadingTransform, put_ReadingTransform)
class ICompass3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a424801b-c5ea-4d45-a0ec-4b791f041a89}')
    @winrt_commethod(6)
    def put_ReportLatency(self, value: UInt32) -> Void: ...
    @winrt_commethod(7)
    def get_ReportLatency(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_MaxBatchSize(self) -> UInt32: ...
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
class ICompass4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{291e7f11-ec32-5dcc-bfcb-0bb39eba5774}')
    @winrt_commethod(6)
    def get_ReportThreshold(self) -> Windows.Devices.Sensors.CompassDataThreshold: ...
    ReportThreshold = property(get_ReportThreshold, None)
class ICompassDataThreshold(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d15b52b3-d39d-5ec8-b2e4-f193e6ab34ed}')
    @winrt_commethod(6)
    def get_Degrees(self) -> Double: ...
    @winrt_commethod(7)
    def put_Degrees(self, value: Double) -> Void: ...
    Degrees = property(get_Degrees, put_Degrees)
class ICompassDeviceId(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d181ca29-b085-4b1d-870a-4ff57ba74fd4}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class ICompassReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{82911128-513d-4dc9-b781-5eedfbf02d0c}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_HeadingMagneticNorth(self) -> Double: ...
    @winrt_commethod(8)
    def get_HeadingTrueNorth(self) -> Windows.Foundation.IReference[Double]: ...
    Timestamp = property(get_Timestamp, None)
    HeadingMagneticNorth = property(get_HeadingMagneticNorth, None)
    HeadingTrueNorth = property(get_HeadingTrueNorth, None)
class ICompassReading2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b13a661e-51bb-4a12-bedd-ad47ff87d2e8}')
    @winrt_commethod(6)
    def get_PerformanceCount(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
class ICompassReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{8f1549b0-e8bc-4c7e-b009-4e41df137072}')
    @winrt_commethod(6)
    def get_Reading(self) -> Windows.Devices.Sensors.CompassReading: ...
    Reading = property(get_Reading, None)
class ICompassReadingHeadingAccuracy(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e761354e-8911-40f7-9e16-6ecc7daec5de}')
    @winrt_commethod(6)
    def get_HeadingAccuracy(self) -> Windows.Devices.Sensors.MagnetometerAccuracy: ...
    HeadingAccuracy = property(get_HeadingAccuracy, None)
class ICompassStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9abc97df-56ec-4c25-b54d-40a68bb5b269}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Devices.Sensors.Compass: ...
class ICompassStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0ace0ead-3baa-4990-9ce4-be0913754ed2}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.Compass]: ...
class IGyrometer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{fdb9a9c4-84b1-4ca2-9763-9b589506c70c}')
    @winrt_commethod(6)
    def GetCurrentReading(self) -> Windows.Devices.Sensors.GyrometerReading: ...
    @winrt_commethod(7)
    def get_MinimumReportInterval(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_ReportInterval(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_ReportInterval(self) -> UInt32: ...
    @winrt_commethod(10)
    def add_ReadingChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Gyrometer, Windows.Devices.Sensors.GyrometerReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ReadingChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
class IGyrometer2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{63df2443-8ce8-41c3-ac44-8698810b557f}')
    @winrt_commethod(6)
    def put_ReadingTransform(self, value: Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_commethod(7)
    def get_ReadingTransform(self) -> Windows.Graphics.Display.DisplayOrientations: ...
    ReadingTransform = property(get_ReadingTransform, put_ReadingTransform)
class IGyrometer3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5d6f88d5-8fbc-4484-914b-528adfd947b1}')
    @winrt_commethod(6)
    def put_ReportLatency(self, value: UInt32) -> Void: ...
    @winrt_commethod(7)
    def get_ReportLatency(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_MaxBatchSize(self) -> UInt32: ...
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
class IGyrometer4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0628a60c-4c4b-5096-94e6-c356df68bef7}')
    @winrt_commethod(6)
    def get_ReportThreshold(self) -> Windows.Devices.Sensors.GyrometerDataThreshold: ...
    ReportThreshold = property(get_ReportThreshold, None)
class IGyrometerDataThreshold(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{8648b31e-6e52-5259-bbad-242a69dc38c8}')
    @winrt_commethod(6)
    def get_XAxisInDegreesPerSecond(self) -> Double: ...
    @winrt_commethod(7)
    def put_XAxisInDegreesPerSecond(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_YAxisInDegreesPerSecond(self) -> Double: ...
    @winrt_commethod(9)
    def put_YAxisInDegreesPerSecond(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_ZAxisInDegreesPerSecond(self) -> Double: ...
    @winrt_commethod(11)
    def put_ZAxisInDegreesPerSecond(self, value: Double) -> Void: ...
    XAxisInDegreesPerSecond = property(get_XAxisInDegreesPerSecond, put_XAxisInDegreesPerSecond)
    YAxisInDegreesPerSecond = property(get_YAxisInDegreesPerSecond, put_YAxisInDegreesPerSecond)
    ZAxisInDegreesPerSecond = property(get_ZAxisInDegreesPerSecond, put_ZAxisInDegreesPerSecond)
class IGyrometerDeviceId(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1ee5e978-89a2-4275-9e95-7126f4708760}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IGyrometerReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b3d6de5c-1ee4-456f-9de7-e2493b5c8e03}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_AngularVelocityX(self) -> Double: ...
    @winrt_commethod(8)
    def get_AngularVelocityY(self) -> Double: ...
    @winrt_commethod(9)
    def get_AngularVelocityZ(self) -> Double: ...
    Timestamp = property(get_Timestamp, None)
    AngularVelocityX = property(get_AngularVelocityX, None)
    AngularVelocityY = property(get_AngularVelocityY, None)
    AngularVelocityZ = property(get_AngularVelocityZ, None)
class IGyrometerReading2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{16afe13c-2b89-44bb-822b-d1e1556ff09b}')
    @winrt_commethod(6)
    def get_PerformanceCount(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
class IGyrometerReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0fdf1895-6f9e-42ce-8d58-388c0ab8356d}')
    @winrt_commethod(6)
    def get_Reading(self) -> Windows.Devices.Sensors.GyrometerReading: ...
    Reading = property(get_Reading, None)
class IGyrometerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{83b6e7c9-e49d-4b39-86e6-cd554be4c5c1}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Devices.Sensors.Gyrometer: ...
class IGyrometerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ef83f7a1-d700-4204-9613-79c6b161df4e}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.Gyrometer]: ...
class IHingeAngleReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a3cd45b9-1bf1-4f65-a704-e2da04f182c0}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_AngleInDegrees(self) -> Double: ...
    @winrt_commethod(8)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Timestamp = property(get_Timestamp, None)
    AngleInDegrees = property(get_AngleInDegrees, None)
    Properties = property(get_Properties, None)
class IHingeAngleSensor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e9d3be02-bfdf-437f-8c29-88c77393d309}')
    @winrt_commethod(6)
    def GetCurrentReadingAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.HingeAngleReading]: ...
    @winrt_commethod(7)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_MinReportThresholdInDegrees(self) -> Double: ...
    @winrt_commethod(9)
    def get_ReportThresholdInDegrees(self) -> Double: ...
    @winrt_commethod(10)
    def put_ReportThresholdInDegrees(self, value: Double) -> Void: ...
    @winrt_commethod(11)
    def add_ReadingChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.HingeAngleSensor, Windows.Devices.Sensors.HingeAngleSensorReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_ReadingChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    MinReportThresholdInDegrees = property(get_MinReportThresholdInDegrees, None)
    ReportThresholdInDegrees = property(get_ReportThresholdInDegrees, put_ReportThresholdInDegrees)
class IHingeAngleSensorReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{24d9558b-fad0-42b8-a854-78923049a1ba}')
    @winrt_commethod(6)
    def get_Reading(self) -> Windows.Devices.Sensors.HingeAngleReading: ...
    Reading = property(get_Reading, None)
class IHingeAngleSensorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b7b63910-fbb1-4123-89ce-4ea34eb0dfca}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.HingeAngleSensor]: ...
    @winrt_commethod(8)
    def GetRelatedToAdjacentPanelsAsync(self, firstPanelId: WinRT_String, secondPanelId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.HingeAngleSensor]: ...
    @winrt_commethod(9)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.HingeAngleSensor]: ...
class IHumanPresenceFeatures(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{bdb09fda-3244-557a-bd29-8b004f59f2cc}')
    @winrt_commethod(6)
    def get_SensorId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SupportedWakeOrLockDistancesInMillimeters(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(8)
    def get_IsWakeOnApproachSupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsLockOnLeaveSupported(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsAttentionAwareDimmingSupported(self) -> Boolean: ...
    SensorId = property(get_SensorId, None)
    SupportedWakeOrLockDistancesInMillimeters = property(get_SupportedWakeOrLockDistancesInMillimeters, None)
    IsWakeOnApproachSupported = property(get_IsWakeOnApproachSupported, None)
    IsLockOnLeaveSupported = property(get_IsLockOnLeaveSupported, None)
    IsAttentionAwareDimmingSupported = property(get_IsAttentionAwareDimmingSupported, None)
class IHumanPresenceSensor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2116788b-e389-5cc3-9a97-cb17be1008bd}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_MaxDetectableDistanceInMillimeters(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(8)
    def get_MinDetectableDistanceInMillimeters(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(9)
    def GetCurrentReading(self) -> Windows.Devices.Sensors.HumanPresenceSensorReading: ...
    @winrt_commethod(10)
    def add_ReadingChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.HumanPresenceSensor, Windows.Devices.Sensors.HumanPresenceSensorReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ReadingChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    MaxDetectableDistanceInMillimeters = property(get_MaxDetectableDistanceInMillimeters, None)
    MinDetectableDistanceInMillimeters = property(get_MinDetectableDistanceInMillimeters, None)
class IHumanPresenceSensorReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{83533bf5-a85a-5d50-8be4-6072d745a3bb}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_Presence(self) -> Windows.Devices.Sensors.HumanPresence: ...
    @winrt_commethod(8)
    def get_Engagement(self) -> Windows.Devices.Sensors.HumanEngagement: ...
    @winrt_commethod(9)
    def get_DistanceInMillimeters(self) -> Windows.Foundation.IReference[UInt32]: ...
    Timestamp = property(get_Timestamp, None)
    Presence = property(get_Presence, None)
    Engagement = property(get_Engagement, None)
    DistanceInMillimeters = property(get_DistanceInMillimeters, None)
class IHumanPresenceSensorReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a9dc4583-fd69-5c5e-ab1f-942204eae2db}')
    @winrt_commethod(6)
    def get_Reading(self) -> Windows.Devices.Sensors.HumanPresenceSensorReading: ...
    Reading = property(get_Reading, None)
class IHumanPresenceSensorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2ae89842-dba9-56b2-9f27-eac69d621004}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, sensorId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.HumanPresenceSensor]: ...
    @winrt_commethod(8)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.HumanPresenceSensor]: ...
class IHumanPresenceSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ef4daf5b-07b7-5eb6-86bb-b7ff49ce44fb}')
    @winrt_commethod(6)
    def get_SensorId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_SensorId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_IsWakeOnApproachEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsWakeOnApproachEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_WakeOnApproachDistanceInMillimeters(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(11)
    def put_WakeOnApproachDistanceInMillimeters(self, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_commethod(12)
    def get_IsLockOnLeaveEnabled(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsLockOnLeaveEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_LockOnLeaveDistanceInMillimeters(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(15)
    def put_LockOnLeaveDistanceInMillimeters(self, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_commethod(16)
    def get_LockOnLeaveTimeout(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(17)
    def put_LockOnLeaveTimeout(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(18)
    def get_IsAttentionAwareDimmingEnabled(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_IsAttentionAwareDimmingEnabled(self, value: Boolean) -> Void: ...
    SensorId = property(get_SensorId, put_SensorId)
    IsWakeOnApproachEnabled = property(get_IsWakeOnApproachEnabled, put_IsWakeOnApproachEnabled)
    WakeOnApproachDistanceInMillimeters = property(get_WakeOnApproachDistanceInMillimeters, put_WakeOnApproachDistanceInMillimeters)
    IsLockOnLeaveEnabled = property(get_IsLockOnLeaveEnabled, put_IsLockOnLeaveEnabled)
    LockOnLeaveDistanceInMillimeters = property(get_LockOnLeaveDistanceInMillimeters, put_LockOnLeaveDistanceInMillimeters)
    LockOnLeaveTimeout = property(get_LockOnLeaveTimeout, put_LockOnLeaveTimeout)
    IsAttentionAwareDimmingEnabled = property(get_IsAttentionAwareDimmingEnabled, put_IsAttentionAwareDimmingEnabled)
class IHumanPresenceSettingsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7f343202-e010-52c4-af0c-04a8f1e033da}')
    @winrt_commethod(6)
    def GetCurrentSettingsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.HumanPresenceSettings]: ...
    @winrt_commethod(7)
    def GetCurrentSettings(self) -> Windows.Devices.Sensors.HumanPresenceSettings: ...
    @winrt_commethod(8)
    def UpdateSettingsAsync(self, settings: Windows.Devices.Sensors.HumanPresenceSettings) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def UpdateSettings(self, settings: Windows.Devices.Sensors.HumanPresenceSettings) -> Void: ...
    @winrt_commethod(10)
    def GetSupportedFeaturesForSensorIdAsync(self, sensorId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.HumanPresenceFeatures]: ...
    @winrt_commethod(11)
    def GetSupportedFeaturesForSensorId(self, sensorId: WinRT_String) -> Windows.Devices.Sensors.HumanPresenceFeatures: ...
    @winrt_commethod(12)
    def GetSupportedLockOnLeaveTimeouts(self) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(13)
    def add_SettingsChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_SettingsChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IInclinometer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2648ca6f-2286-406f-9161-f0c4bd806ebf}')
    @winrt_commethod(6)
    def GetCurrentReading(self) -> Windows.Devices.Sensors.InclinometerReading: ...
    @winrt_commethod(7)
    def get_MinimumReportInterval(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_ReportInterval(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_ReportInterval(self) -> UInt32: ...
    @winrt_commethod(10)
    def add_ReadingChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Inclinometer, Windows.Devices.Sensors.InclinometerReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ReadingChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
class IInclinometer2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{029f3393-28b2-45f8-bb16-61e86a7fae6e}')
    @winrt_commethod(6)
    def put_ReadingTransform(self, value: Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_commethod(7)
    def get_ReadingTransform(self) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_commethod(8)
    def get_ReadingType(self) -> Windows.Devices.Sensors.SensorReadingType: ...
    ReadingTransform = property(get_ReadingTransform, put_ReadingTransform)
    ReadingType = property(get_ReadingType, None)
class IInclinometer3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3a095004-d765-4384-a3d7-0283f3abe6ae}')
    @winrt_commethod(6)
    def put_ReportLatency(self, value: UInt32) -> Void: ...
    @winrt_commethod(7)
    def get_ReportLatency(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_MaxBatchSize(self) -> UInt32: ...
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
class IInclinometer4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{43852618-8fca-548e-bbf5-5c50412b6aa4}')
    @winrt_commethod(6)
    def get_ReportThreshold(self) -> Windows.Devices.Sensors.InclinometerDataThreshold: ...
    ReportThreshold = property(get_ReportThreshold, None)
class IInclinometerDataThreshold(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f80a4783-7bfe-545e-bb60-a0ebc47bd2fb}')
    @winrt_commethod(6)
    def get_PitchInDegrees(self) -> Single: ...
    @winrt_commethod(7)
    def put_PitchInDegrees(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_RollInDegrees(self) -> Single: ...
    @winrt_commethod(9)
    def put_RollInDegrees(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_YawInDegrees(self) -> Single: ...
    @winrt_commethod(11)
    def put_YawInDegrees(self, value: Single) -> Void: ...
    PitchInDegrees = property(get_PitchInDegrees, put_PitchInDegrees)
    RollInDegrees = property(get_RollInDegrees, put_RollInDegrees)
    YawInDegrees = property(get_YawInDegrees, put_YawInDegrees)
class IInclinometerDeviceId(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{01e91982-41ff-4406-ae83-62210ff16fe3}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IInclinometerReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9f44f055-b6f6-497f-b127-1a775e501458}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_PitchDegrees(self) -> Single: ...
    @winrt_commethod(8)
    def get_RollDegrees(self) -> Single: ...
    @winrt_commethod(9)
    def get_YawDegrees(self) -> Single: ...
    Timestamp = property(get_Timestamp, None)
    PitchDegrees = property(get_PitchDegrees, None)
    RollDegrees = property(get_RollDegrees, None)
    YawDegrees = property(get_YawDegrees, None)
class IInclinometerReading2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4f164781-e90b-4658-8915-0103e08a805a}')
    @winrt_commethod(6)
    def get_PerformanceCount(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
class IInclinometerReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4ae91dc1-e7eb-4938-8511-ae0d6b440438}')
    @winrt_commethod(6)
    def get_Reading(self) -> Windows.Devices.Sensors.InclinometerReading: ...
    Reading = property(get_Reading, None)
class IInclinometerReadingYawAccuracy(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b453e880-1fe3-4986-a257-e6ece2723949}')
    @winrt_commethod(6)
    def get_YawAccuracy(self) -> Windows.Devices.Sensors.MagnetometerAccuracy: ...
    YawAccuracy = property(get_YawAccuracy, None)
class IInclinometerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f22ec551-9c30-453a-8b49-3c3eeb33cb61}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Devices.Sensors.Inclinometer: ...
class IInclinometerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{043f9775-6a1e-499c-86e0-638c1a864b00}')
    @winrt_commethod(6)
    def GetDefaultForRelativeReadings(self) -> Windows.Devices.Sensors.Inclinometer: ...
class IInclinometerStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{bd9a4280-b91a-4829-9392-abc0b6bdf2b4}')
    @winrt_commethod(6)
    def GetDefaultWithSensorReadingType(self, sensorReadingtype: Windows.Devices.Sensors.SensorReadingType) -> Windows.Devices.Sensors.Inclinometer: ...
class IInclinometerStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e8ba96f9-6e85-4a83-aed0-d7cdcc9856c8}')
    @winrt_commethod(6)
    def GetDeviceSelector(self, readingType: Windows.Devices.Sensors.SensorReadingType) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.Inclinometer]: ...
class ILightSensor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f84c0718-0c54-47ae-922e-789f57fb03a0}')
    @winrt_commethod(6)
    def GetCurrentReading(self) -> Windows.Devices.Sensors.LightSensorReading: ...
    @winrt_commethod(7)
    def get_MinimumReportInterval(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_ReportInterval(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_ReportInterval(self) -> UInt32: ...
    @winrt_commethod(10)
    def add_ReadingChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.LightSensor, Windows.Devices.Sensors.LightSensorReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ReadingChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
class ILightSensor2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{486b24e8-a94c-4090-8f48-09f782a9f7d5}')
    @winrt_commethod(6)
    def put_ReportLatency(self, value: UInt32) -> Void: ...
    @winrt_commethod(7)
    def get_ReportLatency(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_MaxBatchSize(self) -> UInt32: ...
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
class ILightSensor3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4876d0ff-9f4c-5f72-adbd-a3471b063c00}')
    @winrt_commethod(6)
    def get_ReportThreshold(self) -> Windows.Devices.Sensors.LightSensorDataThreshold: ...
    ReportThreshold = property(get_ReportThreshold, None)
class ILightSensorDataThreshold(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b160afd1-878f-5492-9f2c-33dc3ae584a3}')
    @winrt_commethod(6)
    def get_LuxPercentage(self) -> Single: ...
    @winrt_commethod(7)
    def put_LuxPercentage(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_AbsoluteLux(self) -> Single: ...
    @winrt_commethod(9)
    def put_AbsoluteLux(self, value: Single) -> Void: ...
    LuxPercentage = property(get_LuxPercentage, put_LuxPercentage)
    AbsoluteLux = property(get_AbsoluteLux, put_AbsoluteLux)
class ILightSensorDeviceId(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7fee49f8-0afb-4f51-87f0-6c26375ce94f}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class ILightSensorReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ffdf6300-227c-4d2b-b302-fc0142485c68}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_IlluminanceInLux(self) -> Single: ...
    Timestamp = property(get_Timestamp, None)
    IlluminanceInLux = property(get_IlluminanceInLux, None)
class ILightSensorReading2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b7512185-44a3-44c9-8190-9ef6de0a8a74}')
    @winrt_commethod(6)
    def get_PerformanceCount(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
class ILightSensorReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a3a2f4cf-258b-420c-b8ab-8edd601ecf50}')
    @winrt_commethod(6)
    def get_Reading(self) -> Windows.Devices.Sensors.LightSensorReading: ...
    Reading = property(get_Reading, None)
class ILightSensorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{45db8c84-c3a8-471e-9a53-6457fad87c0e}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Devices.Sensors.LightSensor: ...
class ILightSensorStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0ec0a650-ddc6-40ab-ace3-ec3359d42c51}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.LightSensor]: ...
class IMagnetometer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{484f626e-d3c9-4111-b3f6-2cf1faa418d5}')
    @winrt_commethod(6)
    def GetCurrentReading(self) -> Windows.Devices.Sensors.MagnetometerReading: ...
    @winrt_commethod(7)
    def get_MinimumReportInterval(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_ReportInterval(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_ReportInterval(self) -> UInt32: ...
    @winrt_commethod(10)
    def add_ReadingChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Magnetometer, Windows.Devices.Sensors.MagnetometerReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ReadingChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
class IMagnetometer2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b4656c85-26f6-444b-a9e2-a23f966cd368}')
    @winrt_commethod(6)
    def put_ReadingTransform(self, value: Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_commethod(7)
    def get_ReadingTransform(self) -> Windows.Graphics.Display.DisplayOrientations: ...
    ReadingTransform = property(get_ReadingTransform, put_ReadingTransform)
class IMagnetometer3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{be93db7c-a625-48ef-acf7-fac104832671}')
    @winrt_commethod(6)
    def put_ReportLatency(self, value: UInt32) -> Void: ...
    @winrt_commethod(7)
    def get_ReportLatency(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_MaxBatchSize(self) -> UInt32: ...
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
class IMagnetometer4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{dfb17901-3e0f-508f-b24b-f2bb75015f40}')
    @winrt_commethod(6)
    def get_ReportThreshold(self) -> Windows.Devices.Sensors.MagnetometerDataThreshold: ...
    ReportThreshold = property(get_ReportThreshold, None)
class IMagnetometerDataThreshold(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d177cb01-9063-5fa5-b596-b445e9dc3401}')
    @winrt_commethod(6)
    def get_XAxisMicroteslas(self) -> Single: ...
    @winrt_commethod(7)
    def put_XAxisMicroteslas(self, value: Single) -> Void: ...
    @winrt_commethod(8)
    def get_YAxisMicroteslas(self) -> Single: ...
    @winrt_commethod(9)
    def put_YAxisMicroteslas(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_ZAxisMicroteslas(self) -> Single: ...
    @winrt_commethod(11)
    def put_ZAxisMicroteslas(self, value: Single) -> Void: ...
    XAxisMicroteslas = property(get_XAxisMicroteslas, put_XAxisMicroteslas)
    YAxisMicroteslas = property(get_YAxisMicroteslas, put_YAxisMicroteslas)
    ZAxisMicroteslas = property(get_ZAxisMicroteslas, put_ZAxisMicroteslas)
class IMagnetometerDeviceId(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{58b498c2-7e4b-404c-9fc5-5de8b40ebae3}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IMagnetometerReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0c2cc40d-ebfd-4e5c-bb11-afc29b3cae61}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_MagneticFieldX(self) -> Single: ...
    @winrt_commethod(8)
    def get_MagneticFieldY(self) -> Single: ...
    @winrt_commethod(9)
    def get_MagneticFieldZ(self) -> Single: ...
    @winrt_commethod(10)
    def get_DirectionalAccuracy(self) -> Windows.Devices.Sensors.MagnetometerAccuracy: ...
    Timestamp = property(get_Timestamp, None)
    MagneticFieldX = property(get_MagneticFieldX, None)
    MagneticFieldY = property(get_MagneticFieldY, None)
    MagneticFieldZ = property(get_MagneticFieldZ, None)
    DirectionalAccuracy = property(get_DirectionalAccuracy, None)
class IMagnetometerReading2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d4c95c61-61d9-404b-a328-066f177a1409}')
    @winrt_commethod(6)
    def get_PerformanceCount(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
class IMagnetometerReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{17eae872-2eb9-4ee7-8ad0-3127537d949b}')
    @winrt_commethod(6)
    def get_Reading(self) -> Windows.Devices.Sensors.MagnetometerReading: ...
    Reading = property(get_Reading, None)
class IMagnetometerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{853c64cc-0698-4dda-a6df-9cb9cc4ab40a}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Devices.Sensors.Magnetometer: ...
class IMagnetometerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2c0819f0-ffc6-4f89-a06f-18fa10792933}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.Magnetometer]: ...
class IOrientationSensor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5e354635-cf6b-4c63-abd8-10252b0bf6ec}')
    @winrt_commethod(6)
    def GetCurrentReading(self) -> Windows.Devices.Sensors.OrientationSensorReading: ...
    @winrt_commethod(7)
    def get_MinimumReportInterval(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_ReportInterval(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_ReportInterval(self) -> UInt32: ...
    @winrt_commethod(10)
    def add_ReadingChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.OrientationSensor, Windows.Devices.Sensors.OrientationSensorReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ReadingChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
class IOrientationSensor2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0d924cf9-2f1f-49c9-8042-4a1813d67760}')
    @winrt_commethod(6)
    def put_ReadingTransform(self, value: Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_commethod(7)
    def get_ReadingTransform(self) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_commethod(8)
    def get_ReadingType(self) -> Windows.Devices.Sensors.SensorReadingType: ...
    ReadingTransform = property(get_ReadingTransform, put_ReadingTransform)
    ReadingType = property(get_ReadingType, None)
class IOrientationSensor3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2cce578d-646b-48c5-b7ee-44fdc4c6aafd}')
    @winrt_commethod(6)
    def put_ReportLatency(self, value: UInt32) -> Void: ...
    @winrt_commethod(7)
    def get_ReportLatency(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_MaxBatchSize(self) -> UInt32: ...
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
class IOrientationSensorDeviceId(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5a69b648-4c29-49ec-b28f-ea1d117b66f0}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class IOrientationSensorReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4756c993-6595-4897-bcc6-d537ee757564}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_RotationMatrix(self) -> Windows.Devices.Sensors.SensorRotationMatrix: ...
    @winrt_commethod(8)
    def get_Quaternion(self) -> Windows.Devices.Sensors.SensorQuaternion: ...
    Timestamp = property(get_Timestamp, None)
    RotationMatrix = property(get_RotationMatrix, None)
    Quaternion = property(get_Quaternion, None)
class IOrientationSensorReading2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{00576e5f-49f8-4c05-9e07-24fac79408c3}')
    @winrt_commethod(6)
    def get_PerformanceCount(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(7)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
class IOrientationSensorReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{012c1186-c3ba-46bc-ae65-7a98996cbfb8}')
    @winrt_commethod(6)
    def get_Reading(self) -> Windows.Devices.Sensors.OrientationSensorReading: ...
    Reading = property(get_Reading, None)
class IOrientationSensorReadingYawAccuracy(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d1ac9824-3f5a-49a2-bc7b-1180bc38cd2b}')
    @winrt_commethod(6)
    def get_YawAccuracy(self) -> Windows.Devices.Sensors.MagnetometerAccuracy: ...
    YawAccuracy = property(get_YawAccuracy, None)
class IOrientationSensorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{10ef8712-fb4c-428a-898b-2765e409e669}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Devices.Sensors.OrientationSensor: ...
class IOrientationSensorStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{59da0d0b-d40a-4c71-9276-8a272a0a6619}')
    @winrt_commethod(6)
    def GetDefaultForRelativeReadings(self) -> Windows.Devices.Sensors.OrientationSensor: ...
class IOrientationSensorStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d82ce920-2777-40ff-9f59-d654b085f12f}')
    @winrt_commethod(6)
    def GetDefaultWithSensorReadingType(self, sensorReadingtype: Windows.Devices.Sensors.SensorReadingType) -> Windows.Devices.Sensors.OrientationSensor: ...
    @winrt_commethod(7)
    def GetDefaultWithSensorReadingTypeAndSensorOptimizationGoal(self, sensorReadingType: Windows.Devices.Sensors.SensorReadingType, optimizationGoal: Windows.Devices.Sensors.SensorOptimizationGoal) -> Windows.Devices.Sensors.OrientationSensor: ...
class IOrientationSensorStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a67feb55-2c85-4b28-a0fe-58c4b20495f5}')
    @winrt_commethod(6)
    def GetDeviceSelector(self, readingType: Windows.Devices.Sensors.SensorReadingType) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorWithSensorReadingTypeAndSensorOptimizationGoal(self, readingType: Windows.Devices.Sensors.SensorReadingType, optimizationGoal: Windows.Devices.Sensors.SensorOptimizationGoal) -> WinRT_String: ...
    @winrt_commethod(8)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.OrientationSensor]: ...
class IPedometer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9a1e013d-3d98-45f8-8920-8e4ecaca5f97}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_PowerInMilliwatts(self) -> Double: ...
    @winrt_commethod(8)
    def get_MinimumReportInterval(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_ReportInterval(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_ReportInterval(self) -> UInt32: ...
    @winrt_commethod(11)
    def add_ReadingChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Pedometer, Windows.Devices.Sensors.PedometerReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_ReadingChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    PowerInMilliwatts = property(get_PowerInMilliwatts, None)
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
class IPedometer2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e5a406df-2b81-4add-b2ff-77ab6c98ba19}')
    @winrt_commethod(6)
    def GetCurrentReadings(self) -> Windows.Foundation.Collections.IMapView[Windows.Devices.Sensors.PedometerStepKind, Windows.Devices.Sensors.PedometerReading]: ...
class IPedometerDataThresholdFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{cbad8f50-7a54-466b-9010-77a162fca5d7}')
    @winrt_commethod(6)
    def Create(self, sensor: Windows.Devices.Sensors.Pedometer, stepGoal: Int32) -> Windows.Devices.Sensors.PedometerDataThreshold: ...
class IPedometerReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2245dcf4-a8e1-432f-896a-be0dd9b02d24}')
    @winrt_commethod(6)
    def get_StepKind(self) -> Windows.Devices.Sensors.PedometerStepKind: ...
    @winrt_commethod(7)
    def get_CumulativeSteps(self) -> Int32: ...
    @winrt_commethod(8)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def get_CumulativeStepsDuration(self) -> Windows.Foundation.TimeSpan: ...
    StepKind = property(get_StepKind, None)
    CumulativeSteps = property(get_CumulativeSteps, None)
    Timestamp = property(get_Timestamp, None)
    CumulativeStepsDuration = property(get_CumulativeStepsDuration, None)
class IPedometerReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f855e47e-abbc-4456-86a8-25cf2b333742}')
    @winrt_commethod(6)
    def get_Reading(self) -> Windows.Devices.Sensors.PedometerReading: ...
    Reading = property(get_Reading, None)
class IPedometerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{82980a2f-4083-4dfb-b411-938ea0f4b946}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.Pedometer]: ...
    @winrt_commethod(7)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.Pedometer]: ...
    @winrt_commethod(8)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetSystemHistoryAsync(self, fromTime: Windows.Foundation.DateTime) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sensors.PedometerReading]]: ...
    @winrt_commethod(10)
    def GetSystemHistoryWithDurationAsync(self, fromTime: Windows.Foundation.DateTime, duration: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sensors.PedometerReading]]: ...
class IPedometerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{79f5c6bb-ce0e-4133-b47e-8627ea72f677}')
    @winrt_commethod(6)
    def GetReadingsFromTriggerDetails(self, triggerDetails: Windows.Devices.Sensors.SensorDataThresholdTriggerDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Sensors.PedometerReading]: ...
class IProximitySensor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{54c076b8-ecfb-4944-b928-74fc504d47ee}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_MaxDistanceInMillimeters(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(8)
    def get_MinDistanceInMillimeters(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(9)
    def GetCurrentReading(self) -> Windows.Devices.Sensors.ProximitySensorReading: ...
    @winrt_commethod(10)
    def add_ReadingChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.ProximitySensor, Windows.Devices.Sensors.ProximitySensorReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ReadingChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def CreateDisplayOnOffController(self) -> Windows.Devices.Sensors.ProximitySensorDisplayOnOffController: ...
    DeviceId = property(get_DeviceId, None)
    MaxDistanceInMillimeters = property(get_MaxDistanceInMillimeters, None)
    MinDistanceInMillimeters = property(get_MinDistanceInMillimeters, None)
class IProximitySensorDataThresholdFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{905ac121-6d27-4ad3-9db5-6467f2a5ad9d}')
    @winrt_commethod(6)
    def Create(self, sensor: Windows.Devices.Sensors.ProximitySensor) -> Windows.Devices.Sensors.ProximitySensorDataThreshold: ...
class IProximitySensorReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{71228d59-132d-4d5f-8ff9-2f0db8751ced}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_IsDetected(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_DistanceInMillimeters(self) -> Windows.Foundation.IReference[UInt32]: ...
    Timestamp = property(get_Timestamp, None)
    IsDetected = property(get_IsDetected, None)
    DistanceInMillimeters = property(get_DistanceInMillimeters, None)
class IProximitySensorReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{cfc2f366-c3e8-40fd-8cc3-67e289004938}')
    @winrt_commethod(6)
    def get_Reading(self) -> Windows.Devices.Sensors.ProximitySensorReading: ...
    Reading = property(get_Reading, None)
class IProximitySensorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{29186649-6269-4e57-a5ad-82be80813392}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromId(self, sensorId: WinRT_String) -> Windows.Devices.Sensors.ProximitySensor: ...
class IProximitySensorStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{cbf473ae-e9ca-422f-ad67-4c3d25df350c}')
    @winrt_commethod(6)
    def GetReadingsFromTriggerDetails(self, triggerDetails: Windows.Devices.Sensors.SensorDataThresholdTriggerDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Sensors.ProximitySensorReading]: ...
class ISensorDataThreshold(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{54daec61-fe4b-4e07-b260-3a4cdfbe396e}')
class ISensorDataThresholdTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9106f1b7-e88d-48b1-bc90-619c7b349391}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SensorType(self) -> Windows.Devices.Sensors.SensorType: ...
    DeviceId = property(get_DeviceId, None)
    SensorType = property(get_SensorType, None)
class ISensorQuaternion(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c9c5c827-c71c-46e7-9da3-36a193b232bc}')
    @winrt_commethod(6)
    def get_W(self) -> Single: ...
    @winrt_commethod(7)
    def get_X(self) -> Single: ...
    @winrt_commethod(8)
    def get_Y(self) -> Single: ...
    @winrt_commethod(9)
    def get_Z(self) -> Single: ...
    W = property(get_W, None)
    X = property(get_X, None)
    Y = property(get_Y, None)
    Z = property(get_Z, None)
class ISensorRotationMatrix(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0a3d5a67-22f4-4392-9538-65d0bd064aa6}')
    @winrt_commethod(6)
    def get_M11(self) -> Single: ...
    @winrt_commethod(7)
    def get_M12(self) -> Single: ...
    @winrt_commethod(8)
    def get_M13(self) -> Single: ...
    @winrt_commethod(9)
    def get_M21(self) -> Single: ...
    @winrt_commethod(10)
    def get_M22(self) -> Single: ...
    @winrt_commethod(11)
    def get_M23(self) -> Single: ...
    @winrt_commethod(12)
    def get_M31(self) -> Single: ...
    @winrt_commethod(13)
    def get_M32(self) -> Single: ...
    @winrt_commethod(14)
    def get_M33(self) -> Single: ...
    M11 = property(get_M11, None)
    M12 = property(get_M12, None)
    M13 = property(get_M13, None)
    M21 = property(get_M21, None)
    M22 = property(get_M22, None)
    M23 = property(get_M23, None)
    M31 = property(get_M31, None)
    M32 = property(get_M32, None)
    M33 = property(get_M33, None)
class ISimpleOrientationSensor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5ff53856-214a-4dee-a3f9-616f1ab06ffd}')
    @winrt_commethod(6)
    def GetCurrentOrientation(self) -> Windows.Devices.Sensors.SimpleOrientation: ...
    @winrt_commethod(7)
    def add_OrientationChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.SimpleOrientationSensor, Windows.Devices.Sensors.SimpleOrientationSensorOrientationChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_OrientationChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ISimpleOrientationSensor2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a277a798-8870-453e-8bd6-b8f5d8d7941b}')
    @winrt_commethod(6)
    def put_ReadingTransform(self, value: Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_commethod(7)
    def get_ReadingTransform(self) -> Windows.Graphics.Display.DisplayOrientations: ...
    ReadingTransform = property(get_ReadingTransform, put_ReadingTransform)
class ISimpleOrientationSensorDeviceId(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{fbc00acb-3b76-41f6-8091-30efe646d3cf}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
class ISimpleOrientationSensorOrientationChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{bcd5c660-23d4-4b4c-a22e-ba81ade0c601}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_Orientation(self) -> Windows.Devices.Sensors.SimpleOrientation: ...
    Timestamp = property(get_Timestamp, None)
    Orientation = property(get_Orientation, None)
class ISimpleOrientationSensorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{72ed066f-70aa-40c6-9b1b-3433f7459b4e}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Devices.Sensors.SimpleOrientationSensor: ...
class ISimpleOrientationSensorStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{848f9c7f-b138-4e11-8910-a2a2a3b56d83}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.SimpleOrientationSensor]: ...
class Inclinometer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IInclinometer
    _classid_ = 'Windows.Devices.Sensors.Inclinometer'
    @winrt_mixinmethod
    def GetCurrentReading(self: Windows.Devices.Sensors.IInclinometer) -> Windows.Devices.Sensors.InclinometerReading: ...
    @winrt_mixinmethod
    def get_MinimumReportInterval(self: Windows.Devices.Sensors.IInclinometer) -> UInt32: ...
    @winrt_mixinmethod
    def put_ReportInterval(self: Windows.Devices.Sensors.IInclinometer, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportInterval(self: Windows.Devices.Sensors.IInclinometer) -> UInt32: ...
    @winrt_mixinmethod
    def add_ReadingChanged(self: Windows.Devices.Sensors.IInclinometer, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Inclinometer, Windows.Devices.Sensors.InclinometerReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadingChanged(self: Windows.Devices.Sensors.IInclinometer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sensors.IInclinometerDeviceId) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ReadingTransform(self: Windows.Devices.Sensors.IInclinometer2, value: Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_mixinmethod
    def get_ReadingTransform(self: Windows.Devices.Sensors.IInclinometer2) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_mixinmethod
    def get_ReadingType(self: Windows.Devices.Sensors.IInclinometer2) -> Windows.Devices.Sensors.SensorReadingType: ...
    @winrt_mixinmethod
    def put_ReportLatency(self: Windows.Devices.Sensors.IInclinometer3, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportLatency(self: Windows.Devices.Sensors.IInclinometer3) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxBatchSize(self: Windows.Devices.Sensors.IInclinometer3) -> UInt32: ...
    @winrt_mixinmethod
    def get_ReportThreshold(self: Windows.Devices.Sensors.IInclinometer4) -> Windows.Devices.Sensors.InclinometerDataThreshold: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Sensors.IInclinometerStatics4, readingType: Windows.Devices.Sensors.SensorReadingType) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Sensors.IInclinometerStatics4, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.Inclinometer]: ...
    @winrt_classmethod
    def GetDefaultWithSensorReadingType(cls: Windows.Devices.Sensors.IInclinometerStatics3, sensorReadingtype: Windows.Devices.Sensors.SensorReadingType) -> Windows.Devices.Sensors.Inclinometer: ...
    @winrt_classmethod
    def GetDefaultForRelativeReadings(cls: Windows.Devices.Sensors.IInclinometerStatics2) -> Windows.Devices.Sensors.Inclinometer: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Devices.Sensors.IInclinometerStatics) -> Windows.Devices.Sensors.Inclinometer: ...
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
    DeviceId = property(get_DeviceId, None)
    ReadingTransform = property(get_ReadingTransform, put_ReadingTransform)
    ReadingType = property(get_ReadingType, None)
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
    ReportThreshold = property(get_ReportThreshold, None)
class InclinometerDataThreshold(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IInclinometerDataThreshold
    _classid_ = 'Windows.Devices.Sensors.InclinometerDataThreshold'
    @winrt_mixinmethod
    def get_PitchInDegrees(self: Windows.Devices.Sensors.IInclinometerDataThreshold) -> Single: ...
    @winrt_mixinmethod
    def put_PitchInDegrees(self: Windows.Devices.Sensors.IInclinometerDataThreshold, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RollInDegrees(self: Windows.Devices.Sensors.IInclinometerDataThreshold) -> Single: ...
    @winrt_mixinmethod
    def put_RollInDegrees(self: Windows.Devices.Sensors.IInclinometerDataThreshold, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_YawInDegrees(self: Windows.Devices.Sensors.IInclinometerDataThreshold) -> Single: ...
    @winrt_mixinmethod
    def put_YawInDegrees(self: Windows.Devices.Sensors.IInclinometerDataThreshold, value: Single) -> Void: ...
    PitchInDegrees = property(get_PitchInDegrees, put_PitchInDegrees)
    RollInDegrees = property(get_RollInDegrees, put_RollInDegrees)
    YawInDegrees = property(get_YawInDegrees, put_YawInDegrees)
class InclinometerReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IInclinometerReading
    _classid_ = 'Windows.Devices.Sensors.InclinometerReading'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sensors.IInclinometerReading) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_PitchDegrees(self: Windows.Devices.Sensors.IInclinometerReading) -> Single: ...
    @winrt_mixinmethod
    def get_RollDegrees(self: Windows.Devices.Sensors.IInclinometerReading) -> Single: ...
    @winrt_mixinmethod
    def get_YawDegrees(self: Windows.Devices.Sensors.IInclinometerReading) -> Single: ...
    @winrt_mixinmethod
    def get_YawAccuracy(self: Windows.Devices.Sensors.IInclinometerReadingYawAccuracy) -> Windows.Devices.Sensors.MagnetometerAccuracy: ...
    @winrt_mixinmethod
    def get_PerformanceCount(self: Windows.Devices.Sensors.IInclinometerReading2) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Sensors.IInclinometerReading2) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Timestamp = property(get_Timestamp, None)
    PitchDegrees = property(get_PitchDegrees, None)
    RollDegrees = property(get_RollDegrees, None)
    YawDegrees = property(get_YawDegrees, None)
    YawAccuracy = property(get_YawAccuracy, None)
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
class InclinometerReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IInclinometerReadingChangedEventArgs
    _classid_ = 'Windows.Devices.Sensors.InclinometerReadingChangedEventArgs'
    @winrt_mixinmethod
    def get_Reading(self: Windows.Devices.Sensors.IInclinometerReadingChangedEventArgs) -> Windows.Devices.Sensors.InclinometerReading: ...
    Reading = property(get_Reading, None)
class LightSensor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.ILightSensor
    _classid_ = 'Windows.Devices.Sensors.LightSensor'
    @winrt_mixinmethod
    def GetCurrentReading(self: Windows.Devices.Sensors.ILightSensor) -> Windows.Devices.Sensors.LightSensorReading: ...
    @winrt_mixinmethod
    def get_MinimumReportInterval(self: Windows.Devices.Sensors.ILightSensor) -> UInt32: ...
    @winrt_mixinmethod
    def put_ReportInterval(self: Windows.Devices.Sensors.ILightSensor, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportInterval(self: Windows.Devices.Sensors.ILightSensor) -> UInt32: ...
    @winrt_mixinmethod
    def add_ReadingChanged(self: Windows.Devices.Sensors.ILightSensor, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.LightSensor, Windows.Devices.Sensors.LightSensorReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadingChanged(self: Windows.Devices.Sensors.ILightSensor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sensors.ILightSensorDeviceId) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ReportLatency(self: Windows.Devices.Sensors.ILightSensor2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportLatency(self: Windows.Devices.Sensors.ILightSensor2) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxBatchSize(self: Windows.Devices.Sensors.ILightSensor2) -> UInt32: ...
    @winrt_mixinmethod
    def get_ReportThreshold(self: Windows.Devices.Sensors.ILightSensor3) -> Windows.Devices.Sensors.LightSensorDataThreshold: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Sensors.ILightSensorStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Sensors.ILightSensorStatics2, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.LightSensor]: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Devices.Sensors.ILightSensorStatics) -> Windows.Devices.Sensors.LightSensor: ...
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
    DeviceId = property(get_DeviceId, None)
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
    ReportThreshold = property(get_ReportThreshold, None)
class LightSensorDataThreshold(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.ILightSensorDataThreshold
    _classid_ = 'Windows.Devices.Sensors.LightSensorDataThreshold'
    @winrt_mixinmethod
    def get_LuxPercentage(self: Windows.Devices.Sensors.ILightSensorDataThreshold) -> Single: ...
    @winrt_mixinmethod
    def put_LuxPercentage(self: Windows.Devices.Sensors.ILightSensorDataThreshold, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_AbsoluteLux(self: Windows.Devices.Sensors.ILightSensorDataThreshold) -> Single: ...
    @winrt_mixinmethod
    def put_AbsoluteLux(self: Windows.Devices.Sensors.ILightSensorDataThreshold, value: Single) -> Void: ...
    LuxPercentage = property(get_LuxPercentage, put_LuxPercentage)
    AbsoluteLux = property(get_AbsoluteLux, put_AbsoluteLux)
class LightSensorReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.ILightSensorReading
    _classid_ = 'Windows.Devices.Sensors.LightSensorReading'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sensors.ILightSensorReading) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_IlluminanceInLux(self: Windows.Devices.Sensors.ILightSensorReading) -> Single: ...
    @winrt_mixinmethod
    def get_PerformanceCount(self: Windows.Devices.Sensors.ILightSensorReading2) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Sensors.ILightSensorReading2) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Timestamp = property(get_Timestamp, None)
    IlluminanceInLux = property(get_IlluminanceInLux, None)
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
class LightSensorReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.ILightSensorReadingChangedEventArgs
    _classid_ = 'Windows.Devices.Sensors.LightSensorReadingChangedEventArgs'
    @winrt_mixinmethod
    def get_Reading(self: Windows.Devices.Sensors.ILightSensorReadingChangedEventArgs) -> Windows.Devices.Sensors.LightSensorReading: ...
    Reading = property(get_Reading, None)
class Magnetometer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IMagnetometer
    _classid_ = 'Windows.Devices.Sensors.Magnetometer'
    @winrt_mixinmethod
    def GetCurrentReading(self: Windows.Devices.Sensors.IMagnetometer) -> Windows.Devices.Sensors.MagnetometerReading: ...
    @winrt_mixinmethod
    def get_MinimumReportInterval(self: Windows.Devices.Sensors.IMagnetometer) -> UInt32: ...
    @winrt_mixinmethod
    def put_ReportInterval(self: Windows.Devices.Sensors.IMagnetometer, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportInterval(self: Windows.Devices.Sensors.IMagnetometer) -> UInt32: ...
    @winrt_mixinmethod
    def add_ReadingChanged(self: Windows.Devices.Sensors.IMagnetometer, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Magnetometer, Windows.Devices.Sensors.MagnetometerReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadingChanged(self: Windows.Devices.Sensors.IMagnetometer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sensors.IMagnetometerDeviceId) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ReadingTransform(self: Windows.Devices.Sensors.IMagnetometer2, value: Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_mixinmethod
    def get_ReadingTransform(self: Windows.Devices.Sensors.IMagnetometer2) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_mixinmethod
    def put_ReportLatency(self: Windows.Devices.Sensors.IMagnetometer3, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportLatency(self: Windows.Devices.Sensors.IMagnetometer3) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxBatchSize(self: Windows.Devices.Sensors.IMagnetometer3) -> UInt32: ...
    @winrt_mixinmethod
    def get_ReportThreshold(self: Windows.Devices.Sensors.IMagnetometer4) -> Windows.Devices.Sensors.MagnetometerDataThreshold: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Sensors.IMagnetometerStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Sensors.IMagnetometerStatics2, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.Magnetometer]: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Devices.Sensors.IMagnetometerStatics) -> Windows.Devices.Sensors.Magnetometer: ...
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
    DeviceId = property(get_DeviceId, None)
    ReadingTransform = property(get_ReadingTransform, put_ReadingTransform)
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
    ReportThreshold = property(get_ReportThreshold, None)
MagnetometerAccuracy = Int32
MagnetometerAccuracy_Unknown: MagnetometerAccuracy = 0
MagnetometerAccuracy_Unreliable: MagnetometerAccuracy = 1
MagnetometerAccuracy_Approximate: MagnetometerAccuracy = 2
MagnetometerAccuracy_High: MagnetometerAccuracy = 3
class MagnetometerDataThreshold(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IMagnetometerDataThreshold
    _classid_ = 'Windows.Devices.Sensors.MagnetometerDataThreshold'
    @winrt_mixinmethod
    def get_XAxisMicroteslas(self: Windows.Devices.Sensors.IMagnetometerDataThreshold) -> Single: ...
    @winrt_mixinmethod
    def put_XAxisMicroteslas(self: Windows.Devices.Sensors.IMagnetometerDataThreshold, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_YAxisMicroteslas(self: Windows.Devices.Sensors.IMagnetometerDataThreshold) -> Single: ...
    @winrt_mixinmethod
    def put_YAxisMicroteslas(self: Windows.Devices.Sensors.IMagnetometerDataThreshold, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_ZAxisMicroteslas(self: Windows.Devices.Sensors.IMagnetometerDataThreshold) -> Single: ...
    @winrt_mixinmethod
    def put_ZAxisMicroteslas(self: Windows.Devices.Sensors.IMagnetometerDataThreshold, value: Single) -> Void: ...
    XAxisMicroteslas = property(get_XAxisMicroteslas, put_XAxisMicroteslas)
    YAxisMicroteslas = property(get_YAxisMicroteslas, put_YAxisMicroteslas)
    ZAxisMicroteslas = property(get_ZAxisMicroteslas, put_ZAxisMicroteslas)
class MagnetometerReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IMagnetometerReading
    _classid_ = 'Windows.Devices.Sensors.MagnetometerReading'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sensors.IMagnetometerReading) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_MagneticFieldX(self: Windows.Devices.Sensors.IMagnetometerReading) -> Single: ...
    @winrt_mixinmethod
    def get_MagneticFieldY(self: Windows.Devices.Sensors.IMagnetometerReading) -> Single: ...
    @winrt_mixinmethod
    def get_MagneticFieldZ(self: Windows.Devices.Sensors.IMagnetometerReading) -> Single: ...
    @winrt_mixinmethod
    def get_DirectionalAccuracy(self: Windows.Devices.Sensors.IMagnetometerReading) -> Windows.Devices.Sensors.MagnetometerAccuracy: ...
    @winrt_mixinmethod
    def get_PerformanceCount(self: Windows.Devices.Sensors.IMagnetometerReading2) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Sensors.IMagnetometerReading2) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Timestamp = property(get_Timestamp, None)
    MagneticFieldX = property(get_MagneticFieldX, None)
    MagneticFieldY = property(get_MagneticFieldY, None)
    MagneticFieldZ = property(get_MagneticFieldZ, None)
    DirectionalAccuracy = property(get_DirectionalAccuracy, None)
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
class MagnetometerReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IMagnetometerReadingChangedEventArgs
    _classid_ = 'Windows.Devices.Sensors.MagnetometerReadingChangedEventArgs'
    @winrt_mixinmethod
    def get_Reading(self: Windows.Devices.Sensors.IMagnetometerReadingChangedEventArgs) -> Windows.Devices.Sensors.MagnetometerReading: ...
    Reading = property(get_Reading, None)
class OrientationSensor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IOrientationSensor
    _classid_ = 'Windows.Devices.Sensors.OrientationSensor'
    @winrt_mixinmethod
    def GetCurrentReading(self: Windows.Devices.Sensors.IOrientationSensor) -> Windows.Devices.Sensors.OrientationSensorReading: ...
    @winrt_mixinmethod
    def get_MinimumReportInterval(self: Windows.Devices.Sensors.IOrientationSensor) -> UInt32: ...
    @winrt_mixinmethod
    def put_ReportInterval(self: Windows.Devices.Sensors.IOrientationSensor, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportInterval(self: Windows.Devices.Sensors.IOrientationSensor) -> UInt32: ...
    @winrt_mixinmethod
    def add_ReadingChanged(self: Windows.Devices.Sensors.IOrientationSensor, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.OrientationSensor, Windows.Devices.Sensors.OrientationSensorReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadingChanged(self: Windows.Devices.Sensors.IOrientationSensor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sensors.IOrientationSensorDeviceId) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ReadingTransform(self: Windows.Devices.Sensors.IOrientationSensor2, value: Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_mixinmethod
    def get_ReadingTransform(self: Windows.Devices.Sensors.IOrientationSensor2) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_mixinmethod
    def get_ReadingType(self: Windows.Devices.Sensors.IOrientationSensor2) -> Windows.Devices.Sensors.SensorReadingType: ...
    @winrt_mixinmethod
    def put_ReportLatency(self: Windows.Devices.Sensors.IOrientationSensor3, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportLatency(self: Windows.Devices.Sensors.IOrientationSensor3) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxBatchSize(self: Windows.Devices.Sensors.IOrientationSensor3) -> UInt32: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Sensors.IOrientationSensorStatics4, readingType: Windows.Devices.Sensors.SensorReadingType) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorWithSensorReadingTypeAndSensorOptimizationGoal(cls: Windows.Devices.Sensors.IOrientationSensorStatics4, readingType: Windows.Devices.Sensors.SensorReadingType, optimizationGoal: Windows.Devices.Sensors.SensorOptimizationGoal) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Sensors.IOrientationSensorStatics4, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.OrientationSensor]: ...
    @winrt_classmethod
    def GetDefaultWithSensorReadingType(cls: Windows.Devices.Sensors.IOrientationSensorStatics3, sensorReadingtype: Windows.Devices.Sensors.SensorReadingType) -> Windows.Devices.Sensors.OrientationSensor: ...
    @winrt_classmethod
    def GetDefaultWithSensorReadingTypeAndSensorOptimizationGoal(cls: Windows.Devices.Sensors.IOrientationSensorStatics3, sensorReadingType: Windows.Devices.Sensors.SensorReadingType, optimizationGoal: Windows.Devices.Sensors.SensorOptimizationGoal) -> Windows.Devices.Sensors.OrientationSensor: ...
    @winrt_classmethod
    def GetDefaultForRelativeReadings(cls: Windows.Devices.Sensors.IOrientationSensorStatics2) -> Windows.Devices.Sensors.OrientationSensor: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Devices.Sensors.IOrientationSensorStatics) -> Windows.Devices.Sensors.OrientationSensor: ...
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
    DeviceId = property(get_DeviceId, None)
    ReadingTransform = property(get_ReadingTransform, put_ReadingTransform)
    ReadingType = property(get_ReadingType, None)
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
class OrientationSensorReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IOrientationSensorReading
    _classid_ = 'Windows.Devices.Sensors.OrientationSensorReading'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sensors.IOrientationSensorReading) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_RotationMatrix(self: Windows.Devices.Sensors.IOrientationSensorReading) -> Windows.Devices.Sensors.SensorRotationMatrix: ...
    @winrt_mixinmethod
    def get_Quaternion(self: Windows.Devices.Sensors.IOrientationSensorReading) -> Windows.Devices.Sensors.SensorQuaternion: ...
    @winrt_mixinmethod
    def get_YawAccuracy(self: Windows.Devices.Sensors.IOrientationSensorReadingYawAccuracy) -> Windows.Devices.Sensors.MagnetometerAccuracy: ...
    @winrt_mixinmethod
    def get_PerformanceCount(self: Windows.Devices.Sensors.IOrientationSensorReading2) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Sensors.IOrientationSensorReading2) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Timestamp = property(get_Timestamp, None)
    RotationMatrix = property(get_RotationMatrix, None)
    Quaternion = property(get_Quaternion, None)
    YawAccuracy = property(get_YawAccuracy, None)
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
class OrientationSensorReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IOrientationSensorReadingChangedEventArgs
    _classid_ = 'Windows.Devices.Sensors.OrientationSensorReadingChangedEventArgs'
    @winrt_mixinmethod
    def get_Reading(self: Windows.Devices.Sensors.IOrientationSensorReadingChangedEventArgs) -> Windows.Devices.Sensors.OrientationSensorReading: ...
    Reading = property(get_Reading, None)
class Pedometer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IPedometer
    _classid_ = 'Windows.Devices.Sensors.Pedometer'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sensors.IPedometer) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PowerInMilliwatts(self: Windows.Devices.Sensors.IPedometer) -> Double: ...
    @winrt_mixinmethod
    def get_MinimumReportInterval(self: Windows.Devices.Sensors.IPedometer) -> UInt32: ...
    @winrt_mixinmethod
    def put_ReportInterval(self: Windows.Devices.Sensors.IPedometer, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportInterval(self: Windows.Devices.Sensors.IPedometer) -> UInt32: ...
    @winrt_mixinmethod
    def add_ReadingChanged(self: Windows.Devices.Sensors.IPedometer, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Pedometer, Windows.Devices.Sensors.PedometerReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadingChanged(self: Windows.Devices.Sensors.IPedometer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetCurrentReadings(self: Windows.Devices.Sensors.IPedometer2) -> Windows.Foundation.Collections.IMapView[Windows.Devices.Sensors.PedometerStepKind, Windows.Devices.Sensors.PedometerReading]: ...
    @winrt_classmethod
    def GetReadingsFromTriggerDetails(cls: Windows.Devices.Sensors.IPedometerStatics2, triggerDetails: Windows.Devices.Sensors.SensorDataThresholdTriggerDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Sensors.PedometerReading]: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Sensors.IPedometerStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.Pedometer]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.Sensors.IPedometerStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.Pedometer]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Sensors.IPedometerStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetSystemHistoryAsync(cls: Windows.Devices.Sensors.IPedometerStatics, fromTime: Windows.Foundation.DateTime) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sensors.PedometerReading]]: ...
    @winrt_classmethod
    def GetSystemHistoryWithDurationAsync(cls: Windows.Devices.Sensors.IPedometerStatics, fromTime: Windows.Foundation.DateTime, duration: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Sensors.PedometerReading]]: ...
    DeviceId = property(get_DeviceId, None)
    PowerInMilliwatts = property(get_PowerInMilliwatts, None)
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
class PedometerDataThreshold(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.ISensorDataThreshold
    _classid_ = 'Windows.Devices.Sensors.PedometerDataThreshold'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Sensors.IPedometerDataThresholdFactory, sensor: Windows.Devices.Sensors.Pedometer, stepGoal: Int32) -> Windows.Devices.Sensors.PedometerDataThreshold: ...
class PedometerReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IPedometerReading
    _classid_ = 'Windows.Devices.Sensors.PedometerReading'
    @winrt_mixinmethod
    def get_StepKind(self: Windows.Devices.Sensors.IPedometerReading) -> Windows.Devices.Sensors.PedometerStepKind: ...
    @winrt_mixinmethod
    def get_CumulativeSteps(self: Windows.Devices.Sensors.IPedometerReading) -> Int32: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sensors.IPedometerReading) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_CumulativeStepsDuration(self: Windows.Devices.Sensors.IPedometerReading) -> Windows.Foundation.TimeSpan: ...
    StepKind = property(get_StepKind, None)
    CumulativeSteps = property(get_CumulativeSteps, None)
    Timestamp = property(get_Timestamp, None)
    CumulativeStepsDuration = property(get_CumulativeStepsDuration, None)
class PedometerReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IPedometerReadingChangedEventArgs
    _classid_ = 'Windows.Devices.Sensors.PedometerReadingChangedEventArgs'
    @winrt_mixinmethod
    def get_Reading(self: Windows.Devices.Sensors.IPedometerReadingChangedEventArgs) -> Windows.Devices.Sensors.PedometerReading: ...
    Reading = property(get_Reading, None)
PedometerStepKind = Int32
PedometerStepKind_Unknown: PedometerStepKind = 0
PedometerStepKind_Walking: PedometerStepKind = 1
PedometerStepKind_Running: PedometerStepKind = 2
class ProximitySensor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IProximitySensor
    _classid_ = 'Windows.Devices.Sensors.ProximitySensor'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sensors.IProximitySensor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MaxDistanceInMillimeters(self: Windows.Devices.Sensors.IProximitySensor) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def get_MinDistanceInMillimeters(self: Windows.Devices.Sensors.IProximitySensor) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def GetCurrentReading(self: Windows.Devices.Sensors.IProximitySensor) -> Windows.Devices.Sensors.ProximitySensorReading: ...
    @winrt_mixinmethod
    def add_ReadingChanged(self: Windows.Devices.Sensors.IProximitySensor, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.ProximitySensor, Windows.Devices.Sensors.ProximitySensorReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadingChanged(self: Windows.Devices.Sensors.IProximitySensor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateDisplayOnOffController(self: Windows.Devices.Sensors.IProximitySensor) -> Windows.Devices.Sensors.ProximitySensorDisplayOnOffController: ...
    @winrt_classmethod
    def GetReadingsFromTriggerDetails(cls: Windows.Devices.Sensors.IProximitySensorStatics2, triggerDetails: Windows.Devices.Sensors.SensorDataThresholdTriggerDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Sensors.ProximitySensorReading]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Sensors.IProximitySensorStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromId(cls: Windows.Devices.Sensors.IProximitySensorStatics, sensorId: WinRT_String) -> Windows.Devices.Sensors.ProximitySensor: ...
    DeviceId = property(get_DeviceId, None)
    MaxDistanceInMillimeters = property(get_MaxDistanceInMillimeters, None)
    MinDistanceInMillimeters = property(get_MinDistanceInMillimeters, None)
class ProximitySensorDataThreshold(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.ISensorDataThreshold
    _classid_ = 'Windows.Devices.Sensors.ProximitySensorDataThreshold'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Sensors.IProximitySensorDataThresholdFactory, sensor: Windows.Devices.Sensors.ProximitySensor) -> Windows.Devices.Sensors.ProximitySensorDataThreshold: ...
class ProximitySensorDisplayOnOffController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.IClosable
    _classid_ = 'Windows.Devices.Sensors.ProximitySensorDisplayOnOffController'
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
class ProximitySensorReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IProximitySensorReading
    _classid_ = 'Windows.Devices.Sensors.ProximitySensorReading'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sensors.IProximitySensorReading) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_IsDetected(self: Windows.Devices.Sensors.IProximitySensorReading) -> Boolean: ...
    @winrt_mixinmethod
    def get_DistanceInMillimeters(self: Windows.Devices.Sensors.IProximitySensorReading) -> Windows.Foundation.IReference[UInt32]: ...
    Timestamp = property(get_Timestamp, None)
    IsDetected = property(get_IsDetected, None)
    DistanceInMillimeters = property(get_DistanceInMillimeters, None)
class ProximitySensorReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.IProximitySensorReadingChangedEventArgs
    _classid_ = 'Windows.Devices.Sensors.ProximitySensorReadingChangedEventArgs'
    @winrt_mixinmethod
    def get_Reading(self: Windows.Devices.Sensors.IProximitySensorReadingChangedEventArgs) -> Windows.Devices.Sensors.ProximitySensorReading: ...
    Reading = property(get_Reading, None)
class SensorDataThresholdTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.ISensorDataThresholdTriggerDetails
    _classid_ = 'Windows.Devices.Sensors.SensorDataThresholdTriggerDetails'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sensors.ISensorDataThresholdTriggerDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SensorType(self: Windows.Devices.Sensors.ISensorDataThresholdTriggerDetails) -> Windows.Devices.Sensors.SensorType: ...
    DeviceId = property(get_DeviceId, None)
    SensorType = property(get_SensorType, None)
SensorOptimizationGoal = Int32
SensorOptimizationGoal_Precision: SensorOptimizationGoal = 0
SensorOptimizationGoal_PowerEfficiency: SensorOptimizationGoal = 1
class SensorQuaternion(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.ISensorQuaternion
    _classid_ = 'Windows.Devices.Sensors.SensorQuaternion'
    @winrt_mixinmethod
    def get_W(self: Windows.Devices.Sensors.ISensorQuaternion) -> Single: ...
    @winrt_mixinmethod
    def get_X(self: Windows.Devices.Sensors.ISensorQuaternion) -> Single: ...
    @winrt_mixinmethod
    def get_Y(self: Windows.Devices.Sensors.ISensorQuaternion) -> Single: ...
    @winrt_mixinmethod
    def get_Z(self: Windows.Devices.Sensors.ISensorQuaternion) -> Single: ...
    W = property(get_W, None)
    X = property(get_X, None)
    Y = property(get_Y, None)
    Z = property(get_Z, None)
SensorReadingType = Int32
SensorReadingType_Absolute: SensorReadingType = 0
SensorReadingType_Relative: SensorReadingType = 1
class SensorRotationMatrix(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.ISensorRotationMatrix
    _classid_ = 'Windows.Devices.Sensors.SensorRotationMatrix'
    @winrt_mixinmethod
    def get_M11(self: Windows.Devices.Sensors.ISensorRotationMatrix) -> Single: ...
    @winrt_mixinmethod
    def get_M12(self: Windows.Devices.Sensors.ISensorRotationMatrix) -> Single: ...
    @winrt_mixinmethod
    def get_M13(self: Windows.Devices.Sensors.ISensorRotationMatrix) -> Single: ...
    @winrt_mixinmethod
    def get_M21(self: Windows.Devices.Sensors.ISensorRotationMatrix) -> Single: ...
    @winrt_mixinmethod
    def get_M22(self: Windows.Devices.Sensors.ISensorRotationMatrix) -> Single: ...
    @winrt_mixinmethod
    def get_M23(self: Windows.Devices.Sensors.ISensorRotationMatrix) -> Single: ...
    @winrt_mixinmethod
    def get_M31(self: Windows.Devices.Sensors.ISensorRotationMatrix) -> Single: ...
    @winrt_mixinmethod
    def get_M32(self: Windows.Devices.Sensors.ISensorRotationMatrix) -> Single: ...
    @winrt_mixinmethod
    def get_M33(self: Windows.Devices.Sensors.ISensorRotationMatrix) -> Single: ...
    M11 = property(get_M11, None)
    M12 = property(get_M12, None)
    M13 = property(get_M13, None)
    M21 = property(get_M21, None)
    M22 = property(get_M22, None)
    M23 = property(get_M23, None)
    M31 = property(get_M31, None)
    M32 = property(get_M32, None)
    M33 = property(get_M33, None)
SensorType = Int32
SensorType_Accelerometer: SensorType = 0
SensorType_ActivitySensor: SensorType = 1
SensorType_Barometer: SensorType = 2
SensorType_Compass: SensorType = 3
SensorType_CustomSensor: SensorType = 4
SensorType_Gyroscope: SensorType = 5
SensorType_ProximitySensor: SensorType = 6
SensorType_Inclinometer: SensorType = 7
SensorType_LightSensor: SensorType = 8
SensorType_OrientationSensor: SensorType = 9
SensorType_Pedometer: SensorType = 10
SensorType_RelativeInclinometer: SensorType = 11
SensorType_RelativeOrientationSensor: SensorType = 12
SensorType_SimpleOrientationSensor: SensorType = 13
SimpleOrientation = Int32
SimpleOrientation_NotRotated: SimpleOrientation = 0
SimpleOrientation_Rotated90DegreesCounterclockwise: SimpleOrientation = 1
SimpleOrientation_Rotated180DegreesCounterclockwise: SimpleOrientation = 2
SimpleOrientation_Rotated270DegreesCounterclockwise: SimpleOrientation = 3
SimpleOrientation_Faceup: SimpleOrientation = 4
SimpleOrientation_Facedown: SimpleOrientation = 5
class SimpleOrientationSensor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.ISimpleOrientationSensor
    _classid_ = 'Windows.Devices.Sensors.SimpleOrientationSensor'
    @winrt_mixinmethod
    def GetCurrentOrientation(self: Windows.Devices.Sensors.ISimpleOrientationSensor) -> Windows.Devices.Sensors.SimpleOrientation: ...
    @winrt_mixinmethod
    def add_OrientationChanged(self: Windows.Devices.Sensors.ISimpleOrientationSensor, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.SimpleOrientationSensor, Windows.Devices.Sensors.SimpleOrientationSensorOrientationChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OrientationChanged(self: Windows.Devices.Sensors.ISimpleOrientationSensor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sensors.ISimpleOrientationSensorDeviceId) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ReadingTransform(self: Windows.Devices.Sensors.ISimpleOrientationSensor2, value: Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_mixinmethod
    def get_ReadingTransform(self: Windows.Devices.Sensors.ISimpleOrientationSensor2) -> Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Sensors.ISimpleOrientationSensorStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Sensors.ISimpleOrientationSensorStatics2, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.SimpleOrientationSensor]: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Devices.Sensors.ISimpleOrientationSensorStatics) -> Windows.Devices.Sensors.SimpleOrientationSensor: ...
    DeviceId = property(get_DeviceId, None)
    ReadingTransform = property(get_ReadingTransform, put_ReadingTransform)
class SimpleOrientationSensorOrientationChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Sensors.ISimpleOrientationSensorOrientationChangedEventArgs
    _classid_ = 'Windows.Devices.Sensors.SimpleOrientationSensorOrientationChangedEventArgs'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sensors.ISimpleOrientationSensorOrientationChangedEventArgs) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Orientation(self: Windows.Devices.Sensors.ISimpleOrientationSensorOrientationChangedEventArgs) -> Windows.Devices.Sensors.SimpleOrientation: ...
    Timestamp = property(get_Timestamp, None)
    Orientation = property(get_Orientation, None)
make_head(_module, 'Accelerometer')
make_head(_module, 'AccelerometerDataThreshold')
make_head(_module, 'AccelerometerReading')
make_head(_module, 'AccelerometerReadingChangedEventArgs')
make_head(_module, 'AccelerometerShakenEventArgs')
make_head(_module, 'ActivitySensor')
make_head(_module, 'ActivitySensorReading')
make_head(_module, 'ActivitySensorReadingChangeReport')
make_head(_module, 'ActivitySensorReadingChangedEventArgs')
make_head(_module, 'ActivitySensorTriggerDetails')
make_head(_module, 'Altimeter')
make_head(_module, 'AltimeterReading')
make_head(_module, 'AltimeterReadingChangedEventArgs')
make_head(_module, 'Barometer')
make_head(_module, 'BarometerDataThreshold')
make_head(_module, 'BarometerReading')
make_head(_module, 'BarometerReadingChangedEventArgs')
make_head(_module, 'Compass')
make_head(_module, 'CompassDataThreshold')
make_head(_module, 'CompassReading')
make_head(_module, 'CompassReadingChangedEventArgs')
make_head(_module, 'Gyrometer')
make_head(_module, 'GyrometerDataThreshold')
make_head(_module, 'GyrometerReading')
make_head(_module, 'GyrometerReadingChangedEventArgs')
make_head(_module, 'HingeAngleReading')
make_head(_module, 'HingeAngleSensor')
make_head(_module, 'HingeAngleSensorReadingChangedEventArgs')
make_head(_module, 'HumanPresenceFeatures')
make_head(_module, 'HumanPresenceSensor')
make_head(_module, 'HumanPresenceSensorReading')
make_head(_module, 'HumanPresenceSensorReadingChangedEventArgs')
make_head(_module, 'HumanPresenceSettings')
make_head(_module, 'IAccelerometer')
make_head(_module, 'IAccelerometer2')
make_head(_module, 'IAccelerometer3')
make_head(_module, 'IAccelerometer4')
make_head(_module, 'IAccelerometer5')
make_head(_module, 'IAccelerometerDataThreshold')
make_head(_module, 'IAccelerometerDeviceId')
make_head(_module, 'IAccelerometerReading')
make_head(_module, 'IAccelerometerReading2')
make_head(_module, 'IAccelerometerReadingChangedEventArgs')
make_head(_module, 'IAccelerometerShakenEventArgs')
make_head(_module, 'IAccelerometerStatics')
make_head(_module, 'IAccelerometerStatics2')
make_head(_module, 'IAccelerometerStatics3')
make_head(_module, 'IActivitySensor')
make_head(_module, 'IActivitySensorReading')
make_head(_module, 'IActivitySensorReadingChangeReport')
make_head(_module, 'IActivitySensorReadingChangedEventArgs')
make_head(_module, 'IActivitySensorStatics')
make_head(_module, 'IActivitySensorTriggerDetails')
make_head(_module, 'IAltimeter')
make_head(_module, 'IAltimeter2')
make_head(_module, 'IAltimeterReading')
make_head(_module, 'IAltimeterReading2')
make_head(_module, 'IAltimeterReadingChangedEventArgs')
make_head(_module, 'IAltimeterStatics')
make_head(_module, 'IBarometer')
make_head(_module, 'IBarometer2')
make_head(_module, 'IBarometer3')
make_head(_module, 'IBarometerDataThreshold')
make_head(_module, 'IBarometerReading')
make_head(_module, 'IBarometerReading2')
make_head(_module, 'IBarometerReadingChangedEventArgs')
make_head(_module, 'IBarometerStatics')
make_head(_module, 'IBarometerStatics2')
make_head(_module, 'ICompass')
make_head(_module, 'ICompass2')
make_head(_module, 'ICompass3')
make_head(_module, 'ICompass4')
make_head(_module, 'ICompassDataThreshold')
make_head(_module, 'ICompassDeviceId')
make_head(_module, 'ICompassReading')
make_head(_module, 'ICompassReading2')
make_head(_module, 'ICompassReadingChangedEventArgs')
make_head(_module, 'ICompassReadingHeadingAccuracy')
make_head(_module, 'ICompassStatics')
make_head(_module, 'ICompassStatics2')
make_head(_module, 'IGyrometer')
make_head(_module, 'IGyrometer2')
make_head(_module, 'IGyrometer3')
make_head(_module, 'IGyrometer4')
make_head(_module, 'IGyrometerDataThreshold')
make_head(_module, 'IGyrometerDeviceId')
make_head(_module, 'IGyrometerReading')
make_head(_module, 'IGyrometerReading2')
make_head(_module, 'IGyrometerReadingChangedEventArgs')
make_head(_module, 'IGyrometerStatics')
make_head(_module, 'IGyrometerStatics2')
make_head(_module, 'IHingeAngleReading')
make_head(_module, 'IHingeAngleSensor')
make_head(_module, 'IHingeAngleSensorReadingChangedEventArgs')
make_head(_module, 'IHingeAngleSensorStatics')
make_head(_module, 'IHumanPresenceFeatures')
make_head(_module, 'IHumanPresenceSensor')
make_head(_module, 'IHumanPresenceSensorReading')
make_head(_module, 'IHumanPresenceSensorReadingChangedEventArgs')
make_head(_module, 'IHumanPresenceSensorStatics')
make_head(_module, 'IHumanPresenceSettings')
make_head(_module, 'IHumanPresenceSettingsStatics')
make_head(_module, 'IInclinometer')
make_head(_module, 'IInclinometer2')
make_head(_module, 'IInclinometer3')
make_head(_module, 'IInclinometer4')
make_head(_module, 'IInclinometerDataThreshold')
make_head(_module, 'IInclinometerDeviceId')
make_head(_module, 'IInclinometerReading')
make_head(_module, 'IInclinometerReading2')
make_head(_module, 'IInclinometerReadingChangedEventArgs')
make_head(_module, 'IInclinometerReadingYawAccuracy')
make_head(_module, 'IInclinometerStatics')
make_head(_module, 'IInclinometerStatics2')
make_head(_module, 'IInclinometerStatics3')
make_head(_module, 'IInclinometerStatics4')
make_head(_module, 'ILightSensor')
make_head(_module, 'ILightSensor2')
make_head(_module, 'ILightSensor3')
make_head(_module, 'ILightSensorDataThreshold')
make_head(_module, 'ILightSensorDeviceId')
make_head(_module, 'ILightSensorReading')
make_head(_module, 'ILightSensorReading2')
make_head(_module, 'ILightSensorReadingChangedEventArgs')
make_head(_module, 'ILightSensorStatics')
make_head(_module, 'ILightSensorStatics2')
make_head(_module, 'IMagnetometer')
make_head(_module, 'IMagnetometer2')
make_head(_module, 'IMagnetometer3')
make_head(_module, 'IMagnetometer4')
make_head(_module, 'IMagnetometerDataThreshold')
make_head(_module, 'IMagnetometerDeviceId')
make_head(_module, 'IMagnetometerReading')
make_head(_module, 'IMagnetometerReading2')
make_head(_module, 'IMagnetometerReadingChangedEventArgs')
make_head(_module, 'IMagnetometerStatics')
make_head(_module, 'IMagnetometerStatics2')
make_head(_module, 'IOrientationSensor')
make_head(_module, 'IOrientationSensor2')
make_head(_module, 'IOrientationSensor3')
make_head(_module, 'IOrientationSensorDeviceId')
make_head(_module, 'IOrientationSensorReading')
make_head(_module, 'IOrientationSensorReading2')
make_head(_module, 'IOrientationSensorReadingChangedEventArgs')
make_head(_module, 'IOrientationSensorReadingYawAccuracy')
make_head(_module, 'IOrientationSensorStatics')
make_head(_module, 'IOrientationSensorStatics2')
make_head(_module, 'IOrientationSensorStatics3')
make_head(_module, 'IOrientationSensorStatics4')
make_head(_module, 'IPedometer')
make_head(_module, 'IPedometer2')
make_head(_module, 'IPedometerDataThresholdFactory')
make_head(_module, 'IPedometerReading')
make_head(_module, 'IPedometerReadingChangedEventArgs')
make_head(_module, 'IPedometerStatics')
make_head(_module, 'IPedometerStatics2')
make_head(_module, 'IProximitySensor')
make_head(_module, 'IProximitySensorDataThresholdFactory')
make_head(_module, 'IProximitySensorReading')
make_head(_module, 'IProximitySensorReadingChangedEventArgs')
make_head(_module, 'IProximitySensorStatics')
make_head(_module, 'IProximitySensorStatics2')
make_head(_module, 'ISensorDataThreshold')
make_head(_module, 'ISensorDataThresholdTriggerDetails')
make_head(_module, 'ISensorQuaternion')
make_head(_module, 'ISensorRotationMatrix')
make_head(_module, 'ISimpleOrientationSensor')
make_head(_module, 'ISimpleOrientationSensor2')
make_head(_module, 'ISimpleOrientationSensorDeviceId')
make_head(_module, 'ISimpleOrientationSensorOrientationChangedEventArgs')
make_head(_module, 'ISimpleOrientationSensorStatics')
make_head(_module, 'ISimpleOrientationSensorStatics2')
make_head(_module, 'Inclinometer')
make_head(_module, 'InclinometerDataThreshold')
make_head(_module, 'InclinometerReading')
make_head(_module, 'InclinometerReadingChangedEventArgs')
make_head(_module, 'LightSensor')
make_head(_module, 'LightSensorDataThreshold')
make_head(_module, 'LightSensorReading')
make_head(_module, 'LightSensorReadingChangedEventArgs')
make_head(_module, 'Magnetometer')
make_head(_module, 'MagnetometerDataThreshold')
make_head(_module, 'MagnetometerReading')
make_head(_module, 'MagnetometerReadingChangedEventArgs')
make_head(_module, 'OrientationSensor')
make_head(_module, 'OrientationSensorReading')
make_head(_module, 'OrientationSensorReadingChangedEventArgs')
make_head(_module, 'Pedometer')
make_head(_module, 'PedometerDataThreshold')
make_head(_module, 'PedometerReading')
make_head(_module, 'PedometerReadingChangedEventArgs')
make_head(_module, 'ProximitySensor')
make_head(_module, 'ProximitySensorDataThreshold')
make_head(_module, 'ProximitySensorDisplayOnOffController')
make_head(_module, 'ProximitySensorReading')
make_head(_module, 'ProximitySensorReadingChangedEventArgs')
make_head(_module, 'SensorDataThresholdTriggerDetails')
make_head(_module, 'SensorQuaternion')
make_head(_module, 'SensorRotationMatrix')
make_head(_module, 'SimpleOrientationSensor')
make_head(_module, 'SimpleOrientationSensorOrientationChangedEventArgs')
