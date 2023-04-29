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
import Windows.Devices.Sensors.Custom
import Windows.Foundation
import Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class CustomSensor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Sensors.Custom.CustomSensor'
    @winrt_mixinmethod
    def GetCurrentReading(self: Windows.Devices.Sensors.Custom.ICustomSensor) -> Windows.Devices.Sensors.Custom.CustomSensorReading: ...
    @winrt_mixinmethod
    def get_MinimumReportInterval(self: Windows.Devices.Sensors.Custom.ICustomSensor) -> UInt32: ...
    @winrt_mixinmethod
    def put_ReportInterval(self: Windows.Devices.Sensors.Custom.ICustomSensor, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportInterval(self: Windows.Devices.Sensors.Custom.ICustomSensor) -> UInt32: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Sensors.Custom.ICustomSensor) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_ReadingChanged(self: Windows.Devices.Sensors.Custom.ICustomSensor, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Custom.CustomSensor, Windows.Devices.Sensors.Custom.CustomSensorReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadingChanged(self: Windows.Devices.Sensors.Custom.ICustomSensor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_ReportLatency(self: Windows.Devices.Sensors.Custom.ICustomSensor2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportLatency(self: Windows.Devices.Sensors.Custom.ICustomSensor2) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxBatchSize(self: Windows.Devices.Sensors.Custom.ICustomSensor2) -> UInt32: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Sensors.Custom.ICustomSensorStatics, interfaceId: Guid) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Sensors.Custom.ICustomSensorStatics, sensorId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.Custom.CustomSensor]: ...
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
    DeviceId = property(get_DeviceId, None)
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
class CustomSensorReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Sensors.Custom.CustomSensorReading'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Sensors.Custom.ICustomSensorReading) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.Sensors.Custom.ICustomSensorReading) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    @winrt_mixinmethod
    def get_PerformanceCount(self: Windows.Devices.Sensors.Custom.ICustomSensorReading2) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    Timestamp = property(get_Timestamp, None)
    Properties = property(get_Properties, None)
    PerformanceCount = property(get_PerformanceCount, None)
class CustomSensorReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Sensors.Custom.CustomSensorReadingChangedEventArgs'
    @winrt_mixinmethod
    def get_Reading(self: Windows.Devices.Sensors.Custom.ICustomSensorReadingChangedEventArgs) -> Windows.Devices.Sensors.Custom.CustomSensorReading: ...
    Reading = property(get_Reading, None)
class ICustomSensor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a136f9ad-4034-4b4d-99-dd-53-1a-ac-64-9c-09')
    @winrt_commethod(6)
    def GetCurrentReading(self) -> Windows.Devices.Sensors.Custom.CustomSensorReading: ...
    @winrt_commethod(7)
    def get_MinimumReportInterval(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_ReportInterval(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_ReportInterval(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def add_ReadingChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Sensors.Custom.CustomSensor, Windows.Devices.Sensors.Custom.CustomSensorReadingChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_ReadingChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
    DeviceId = property(get_DeviceId, None)
class ICustomSensor2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('20db3111-ec58-4d9f-bf-bd-e7-78-25-08-85-10')
    @winrt_commethod(6)
    def put_ReportLatency(self, value: UInt32) -> Void: ...
    @winrt_commethod(7)
    def get_ReportLatency(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_MaxBatchSize(self) -> UInt32: ...
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    MaxBatchSize = property(get_MaxBatchSize, None)
class ICustomSensorReading(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('64004f4d-446a-4366-a8-7a-5f-96-32-68-ec-53')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    Timestamp = property(get_Timestamp, None)
    Properties = property(get_Properties, None)
class ICustomSensorReading2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('223c98ea-bf73-4992-9a-48-d3-c8-97-59-4c-cb')
    @winrt_commethod(6)
    def get_PerformanceCount(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    PerformanceCount = property(get_PerformanceCount, None)
class ICustomSensorReadingChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6b202023-cffd-4cc1-8f-f0-e2-18-23-d7-6f-cc')
    @winrt_commethod(6)
    def get_Reading(self) -> Windows.Devices.Sensors.Custom.CustomSensorReading: ...
    Reading = property(get_Reading, None)
class ICustomSensorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('992052cf-f422-4c7d-83-6b-e7-dc-74-a7-12-4b')
    @winrt_commethod(6)
    def GetDeviceSelector(self, interfaceId: Guid) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, sensorId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Sensors.Custom.CustomSensor]: ...
make_head(_module, 'CustomSensor')
make_head(_module, 'CustomSensorReading')
make_head(_module, 'CustomSensorReadingChangedEventArgs')
make_head(_module, 'ICustomSensor')
make_head(_module, 'ICustomSensor2')
make_head(_module, 'ICustomSensorReading')
make_head(_module, 'ICustomSensorReading2')
make_head(_module, 'ICustomSensorReadingChangedEventArgs')
make_head(_module, 'ICustomSensorStatics')
