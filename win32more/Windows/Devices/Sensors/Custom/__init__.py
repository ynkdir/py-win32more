from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Sensors.Custom
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class CustomSensor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sensors.Custom.ICustomSensor
    _classid_ = 'Windows.Devices.Sensors.Custom.CustomSensor'
    @winrt_mixinmethod
    def GetCurrentReading(self: win32more.Windows.Devices.Sensors.Custom.ICustomSensor) -> win32more.Windows.Devices.Sensors.Custom.CustomSensorReading: ...
    @winrt_mixinmethod
    def get_MinimumReportInterval(self: win32more.Windows.Devices.Sensors.Custom.ICustomSensor) -> UInt32: ...
    @winrt_mixinmethod
    def put_ReportInterval(self: win32more.Windows.Devices.Sensors.Custom.ICustomSensor, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportInterval(self: win32more.Windows.Devices.Sensors.Custom.ICustomSensor) -> UInt32: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Sensors.Custom.ICustomSensor) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_ReadingChanged(self: win32more.Windows.Devices.Sensors.Custom.ICustomSensor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Sensors.Custom.CustomSensor, win32more.Windows.Devices.Sensors.Custom.CustomSensorReadingChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadingChanged(self: win32more.Windows.Devices.Sensors.Custom.ICustomSensor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_ReportLatency(self: win32more.Windows.Devices.Sensors.Custom.ICustomSensor2, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_ReportLatency(self: win32more.Windows.Devices.Sensors.Custom.ICustomSensor2) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxBatchSize(self: win32more.Windows.Devices.Sensors.Custom.ICustomSensor2) -> UInt32: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Sensors.Custom.ICustomSensorStatics, interfaceId: Guid) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Sensors.Custom.ICustomSensorStatics, sensorId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sensors.Custom.CustomSensor]: ...
    DeviceId = property(get_DeviceId, None)
    MaxBatchSize = property(get_MaxBatchSize, None)
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
    ReadingChanged = event()
class CustomSensorReading(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sensors.Custom.ICustomSensorReading
    _classid_ = 'Windows.Devices.Sensors.Custom.CustomSensorReading'
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Sensors.Custom.ICustomSensorReading) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.Devices.Sensors.Custom.ICustomSensorReading) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def get_PerformanceCount(self: win32more.Windows.Devices.Sensors.Custom.ICustomSensorReading2) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    PerformanceCount = property(get_PerformanceCount, None)
    Properties = property(get_Properties, None)
    Timestamp = property(get_Timestamp, None)
class CustomSensorReadingChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Sensors.Custom.ICustomSensorReadingChangedEventArgs
    _classid_ = 'Windows.Devices.Sensors.Custom.CustomSensorReadingChangedEventArgs'
    @winrt_mixinmethod
    def get_Reading(self: win32more.Windows.Devices.Sensors.Custom.ICustomSensorReadingChangedEventArgs) -> win32more.Windows.Devices.Sensors.Custom.CustomSensorReading: ...
    Reading = property(get_Reading, None)
class ICustomSensor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sensors.Custom.ICustomSensor'
    _iid_ = Guid('{a136f9ad-4034-4b4d-99dd-531aac649c09}')
    @winrt_commethod(6)
    def GetCurrentReading(self) -> win32more.Windows.Devices.Sensors.Custom.CustomSensorReading: ...
    @winrt_commethod(7)
    def get_MinimumReportInterval(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_ReportInterval(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_ReportInterval(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def add_ReadingChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Sensors.Custom.CustomSensor, win32more.Windows.Devices.Sensors.Custom.CustomSensorReadingChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_ReadingChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    MinimumReportInterval = property(get_MinimumReportInterval, None)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
    ReadingChanged = event()
class ICustomSensor2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sensors.Custom.ICustomSensor2'
    _iid_ = Guid('{20db3111-ec58-4d9f-bfbd-e77825088510}')
    @winrt_commethod(6)
    def put_ReportLatency(self, value: UInt32) -> Void: ...
    @winrt_commethod(7)
    def get_ReportLatency(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_MaxBatchSize(self) -> UInt32: ...
    MaxBatchSize = property(get_MaxBatchSize, None)
    ReportLatency = property(get_ReportLatency, put_ReportLatency)
class ICustomSensorReading(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sensors.Custom.ICustomSensorReading'
    _iid_ = Guid('{64004f4d-446a-4366-a87a-5f963268ec53}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_Properties(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    Properties = property(get_Properties, None)
    Timestamp = property(get_Timestamp, None)
class ICustomSensorReading2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sensors.Custom.ICustomSensorReading2'
    _iid_ = Guid('{223c98ea-bf73-4992-9a48-d3c897594ccb}')
    @winrt_commethod(6)
    def get_PerformanceCount(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    PerformanceCount = property(get_PerformanceCount, None)
class ICustomSensorReadingChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sensors.Custom.ICustomSensorReadingChangedEventArgs'
    _iid_ = Guid('{6b202023-cffd-4cc1-8ff0-e21823d76fcc}')
    @winrt_commethod(6)
    def get_Reading(self) -> win32more.Windows.Devices.Sensors.Custom.CustomSensorReading: ...
    Reading = property(get_Reading, None)
class ICustomSensorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Sensors.Custom.ICustomSensorStatics'
    _iid_ = Guid('{992052cf-f422-4c7d-836b-e7dc74a7124b}')
    @winrt_commethod(6)
    def GetDeviceSelector(self, interfaceId: Guid) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, sensorId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Sensors.Custom.CustomSensor]: ...


make_ready(__name__)
