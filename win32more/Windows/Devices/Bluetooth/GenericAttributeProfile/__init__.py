from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Bluetooth
import win32more.Windows.Devices.Bluetooth.GenericAttributeProfile
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class GattCharacteristic(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic'
    @winrt_mixinmethod
    def GetDescriptors(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic, descriptorUuid: Guid) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptor]: ...
    @winrt_mixinmethod
    def get_CharacteristicProperties(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties: ...
    @winrt_mixinmethod
    def get_ProtectionLevel(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_mixinmethod
    def put_ProtectionLevel(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic, value: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_mixinmethod
    def get_UserDescription(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Uuid(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic) -> Guid: ...
    @winrt_mixinmethod
    def get_AttributeHandle(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic) -> UInt16: ...
    @winrt_mixinmethod
    def get_PresentationFormats(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormat]: ...
    @winrt_mixinmethod
    def ReadValueAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadResult]: ...
    @winrt_mixinmethod
    def ReadValueWithCacheModeAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadResult]: ...
    @winrt_mixinmethod
    def WriteValueAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic, value: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
    @winrt_mixinmethod
    def WriteValueWithOptionAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic, value: win32more.Windows.Storage.Streams.IBuffer, writeOption: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
    @winrt_mixinmethod
    def ReadClientCharacteristicConfigurationDescriptorAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadClientCharacteristicConfigurationDescriptorResult]: ...
    @winrt_mixinmethod
    def WriteClientCharacteristicConfigurationDescriptorAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic, clientCharacteristicConfigurationDescriptorValue: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientCharacteristicConfigurationDescriptorValue) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
    @winrt_mixinmethod
    def add_ValueChanged(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic, valueChangedHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic, win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattValueChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ValueChanged(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic, valueChangedEventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Service(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic2) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService: ...
    @winrt_mixinmethod
    def GetAllDescriptors(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptor]: ...
    @winrt_mixinmethod
    def GetDescriptorsAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorsResult]: ...
    @winrt_mixinmethod
    def GetDescriptorsWithCacheModeAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic3, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorsResult]: ...
    @winrt_mixinmethod
    def GetDescriptorsForUuidAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic3, descriptorUuid: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorsResult]: ...
    @winrt_mixinmethod
    def GetDescriptorsForUuidWithCacheModeAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic3, descriptorUuid: Guid, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorsResult]: ...
    @winrt_mixinmethod
    def WriteValueWithResultAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic3, value: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
    @winrt_mixinmethod
    def WriteValueWithResultAndOptionAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic3, value: win32more.Windows.Storage.Streams.IBuffer, writeOption: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
    @winrt_mixinmethod
    def WriteClientCharacteristicConfigurationDescriptorWithResultAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic3, clientCharacteristicConfigurationDescriptorValue: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientCharacteristicConfigurationDescriptorValue) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
    @winrt_classmethod
    def ConvertShortIdToUuid(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicStatics, shortId: UInt16) -> Guid: ...
    AttributeHandle = property(get_AttributeHandle, None)
    CharacteristicProperties = property(get_CharacteristicProperties, None)
    PresentationFormats = property(get_PresentationFormats, None)
    ProtectionLevel = property(get_ProtectionLevel, put_ProtectionLevel)
    Service = property(get_Service, None)
    UserDescription = property(get_UserDescription, None)
    Uuid = property(get_Uuid, None)
    ValueChanged = event()
class GattCharacteristicProperties(Enum, UInt32):
    None_ = 0
    Broadcast = 1
    Read = 2
    WriteWithoutResponse = 4
    Write = 8
    Notify = 16
    Indicate = 32
    AuthenticatedSignedWrites = 64
    ExtendedProperties = 128
    ReliableWrites = 256
    WritableAuxiliaries = 512
class _GattCharacteristicUuids_Meta_(ComPtr.__class__):
    pass
class GattCharacteristicUuids(ComPtr, metaclass=_GattCharacteristicUuids_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicUuids'
    @winrt_classmethod
    def get_AlertCategoryId(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_AlertCategoryIdBitMask(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_AlertLevel(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_AlertNotificationControlPoint(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_AlertStatus(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_GapAppearance(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_BootKeyboardInputReport(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_BootKeyboardOutputReport(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_BootMouseInputReport(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_CurrentTime(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_CyclingPowerControlPoint(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_CyclingPowerFeature(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_CyclingPowerMeasurement(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_CyclingPowerVector(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_DateTime(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_DayDateTime(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_DayOfWeek(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_GapDeviceName(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_DstOffset(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ExactTime256(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_FirmwareRevisionString(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_HardwareRevisionString(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_HidControlPoint(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_HidInformation(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_Ieee1107320601RegulatoryCertificationDataList(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_LnControlPoint(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_LnFeature(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_LocalTimeInformation(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_LocationAndSpeed(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ManufacturerNameString(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ModelNumberString(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_Navigation(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_NewAlert(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_GapPeripheralPreferredConnectionParameters(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_GapPeripheralPrivacyFlag(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_PnpId(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_PositionQuality(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ProtocolMode(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_GapReconnectionAddress(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ReferenceTimeInformation(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_Report(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ReportMap(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_RingerControlPoint(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_RingerSetting(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ScanIntervalWindow(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ScanRefresh(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_SerialNumberString(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_GattServiceChanged(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_SoftwareRevisionString(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_SupportedNewAlertCategory(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_SupportUnreadAlertCategory(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_SystemId(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_TimeAccuracy(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_TimeSource(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_TimeUpdateControlPoint(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_TimeUpdateState(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_TimeWithDst(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_TimeZone(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_TxPowerLevel(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_UnreadAlertStatus(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_BatteryLevel(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_BloodPressureFeature(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_BloodPressureMeasurement(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_BodySensorLocation(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_CscFeature(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_CscMeasurement(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_GlucoseFeature(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_GlucoseMeasurement(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_GlucoseMeasurementContext(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_HeartRateControlPoint(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_HeartRateMeasurement(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_IntermediateCuffPressure(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_IntermediateTemperature(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_MeasurementInterval(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_RecordAccessControlPoint(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_RscFeature(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_RscMeasurement(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_SCControlPoint(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_SensorLocation(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_TemperatureMeasurement(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_TemperatureType(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    _GattCharacteristicUuids_Meta_.AlertCategoryId = property(get_AlertCategoryId, None)
    _GattCharacteristicUuids_Meta_.AlertCategoryIdBitMask = property(get_AlertCategoryIdBitMask, None)
    _GattCharacteristicUuids_Meta_.AlertLevel = property(get_AlertLevel, None)
    _GattCharacteristicUuids_Meta_.AlertNotificationControlPoint = property(get_AlertNotificationControlPoint, None)
    _GattCharacteristicUuids_Meta_.AlertStatus = property(get_AlertStatus, None)
    _GattCharacteristicUuids_Meta_.BatteryLevel = property(get_BatteryLevel, None)
    _GattCharacteristicUuids_Meta_.BloodPressureFeature = property(get_BloodPressureFeature, None)
    _GattCharacteristicUuids_Meta_.BloodPressureMeasurement = property(get_BloodPressureMeasurement, None)
    _GattCharacteristicUuids_Meta_.BodySensorLocation = property(get_BodySensorLocation, None)
    _GattCharacteristicUuids_Meta_.BootKeyboardInputReport = property(get_BootKeyboardInputReport, None)
    _GattCharacteristicUuids_Meta_.BootKeyboardOutputReport = property(get_BootKeyboardOutputReport, None)
    _GattCharacteristicUuids_Meta_.BootMouseInputReport = property(get_BootMouseInputReport, None)
    _GattCharacteristicUuids_Meta_.CscFeature = property(get_CscFeature, None)
    _GattCharacteristicUuids_Meta_.CscMeasurement = property(get_CscMeasurement, None)
    _GattCharacteristicUuids_Meta_.CurrentTime = property(get_CurrentTime, None)
    _GattCharacteristicUuids_Meta_.CyclingPowerControlPoint = property(get_CyclingPowerControlPoint, None)
    _GattCharacteristicUuids_Meta_.CyclingPowerFeature = property(get_CyclingPowerFeature, None)
    _GattCharacteristicUuids_Meta_.CyclingPowerMeasurement = property(get_CyclingPowerMeasurement, None)
    _GattCharacteristicUuids_Meta_.CyclingPowerVector = property(get_CyclingPowerVector, None)
    _GattCharacteristicUuids_Meta_.DateTime = property(get_DateTime, None)
    _GattCharacteristicUuids_Meta_.DayDateTime = property(get_DayDateTime, None)
    _GattCharacteristicUuids_Meta_.DayOfWeek = property(get_DayOfWeek, None)
    _GattCharacteristicUuids_Meta_.DstOffset = property(get_DstOffset, None)
    _GattCharacteristicUuids_Meta_.ExactTime256 = property(get_ExactTime256, None)
    _GattCharacteristicUuids_Meta_.FirmwareRevisionString = property(get_FirmwareRevisionString, None)
    _GattCharacteristicUuids_Meta_.GapAppearance = property(get_GapAppearance, None)
    _GattCharacteristicUuids_Meta_.GapDeviceName = property(get_GapDeviceName, None)
    _GattCharacteristicUuids_Meta_.GapPeripheralPreferredConnectionParameters = property(get_GapPeripheralPreferredConnectionParameters, None)
    _GattCharacteristicUuids_Meta_.GapPeripheralPrivacyFlag = property(get_GapPeripheralPrivacyFlag, None)
    _GattCharacteristicUuids_Meta_.GapReconnectionAddress = property(get_GapReconnectionAddress, None)
    _GattCharacteristicUuids_Meta_.GattServiceChanged = property(get_GattServiceChanged, None)
    _GattCharacteristicUuids_Meta_.GlucoseFeature = property(get_GlucoseFeature, None)
    _GattCharacteristicUuids_Meta_.GlucoseMeasurement = property(get_GlucoseMeasurement, None)
    _GattCharacteristicUuids_Meta_.GlucoseMeasurementContext = property(get_GlucoseMeasurementContext, None)
    _GattCharacteristicUuids_Meta_.HardwareRevisionString = property(get_HardwareRevisionString, None)
    _GattCharacteristicUuids_Meta_.HeartRateControlPoint = property(get_HeartRateControlPoint, None)
    _GattCharacteristicUuids_Meta_.HeartRateMeasurement = property(get_HeartRateMeasurement, None)
    _GattCharacteristicUuids_Meta_.HidControlPoint = property(get_HidControlPoint, None)
    _GattCharacteristicUuids_Meta_.HidInformation = property(get_HidInformation, None)
    _GattCharacteristicUuids_Meta_.Ieee1107320601RegulatoryCertificationDataList = property(get_Ieee1107320601RegulatoryCertificationDataList, None)
    _GattCharacteristicUuids_Meta_.IntermediateCuffPressure = property(get_IntermediateCuffPressure, None)
    _GattCharacteristicUuids_Meta_.IntermediateTemperature = property(get_IntermediateTemperature, None)
    _GattCharacteristicUuids_Meta_.LnControlPoint = property(get_LnControlPoint, None)
    _GattCharacteristicUuids_Meta_.LnFeature = property(get_LnFeature, None)
    _GattCharacteristicUuids_Meta_.LocalTimeInformation = property(get_LocalTimeInformation, None)
    _GattCharacteristicUuids_Meta_.LocationAndSpeed = property(get_LocationAndSpeed, None)
    _GattCharacteristicUuids_Meta_.ManufacturerNameString = property(get_ManufacturerNameString, None)
    _GattCharacteristicUuids_Meta_.MeasurementInterval = property(get_MeasurementInterval, None)
    _GattCharacteristicUuids_Meta_.ModelNumberString = property(get_ModelNumberString, None)
    _GattCharacteristicUuids_Meta_.Navigation = property(get_Navigation, None)
    _GattCharacteristicUuids_Meta_.NewAlert = property(get_NewAlert, None)
    _GattCharacteristicUuids_Meta_.PnpId = property(get_PnpId, None)
    _GattCharacteristicUuids_Meta_.PositionQuality = property(get_PositionQuality, None)
    _GattCharacteristicUuids_Meta_.ProtocolMode = property(get_ProtocolMode, None)
    _GattCharacteristicUuids_Meta_.RecordAccessControlPoint = property(get_RecordAccessControlPoint, None)
    _GattCharacteristicUuids_Meta_.ReferenceTimeInformation = property(get_ReferenceTimeInformation, None)
    _GattCharacteristicUuids_Meta_.Report = property(get_Report, None)
    _GattCharacteristicUuids_Meta_.ReportMap = property(get_ReportMap, None)
    _GattCharacteristicUuids_Meta_.RingerControlPoint = property(get_RingerControlPoint, None)
    _GattCharacteristicUuids_Meta_.RingerSetting = property(get_RingerSetting, None)
    _GattCharacteristicUuids_Meta_.RscFeature = property(get_RscFeature, None)
    _GattCharacteristicUuids_Meta_.RscMeasurement = property(get_RscMeasurement, None)
    _GattCharacteristicUuids_Meta_.SCControlPoint = property(get_SCControlPoint, None)
    _GattCharacteristicUuids_Meta_.ScanIntervalWindow = property(get_ScanIntervalWindow, None)
    _GattCharacteristicUuids_Meta_.ScanRefresh = property(get_ScanRefresh, None)
    _GattCharacteristicUuids_Meta_.SensorLocation = property(get_SensorLocation, None)
    _GattCharacteristicUuids_Meta_.SerialNumberString = property(get_SerialNumberString, None)
    _GattCharacteristicUuids_Meta_.SoftwareRevisionString = property(get_SoftwareRevisionString, None)
    _GattCharacteristicUuids_Meta_.SupportUnreadAlertCategory = property(get_SupportUnreadAlertCategory, None)
    _GattCharacteristicUuids_Meta_.SupportedNewAlertCategory = property(get_SupportedNewAlertCategory, None)
    _GattCharacteristicUuids_Meta_.SystemId = property(get_SystemId, None)
    _GattCharacteristicUuids_Meta_.TemperatureMeasurement = property(get_TemperatureMeasurement, None)
    _GattCharacteristicUuids_Meta_.TemperatureType = property(get_TemperatureType, None)
    _GattCharacteristicUuids_Meta_.TimeAccuracy = property(get_TimeAccuracy, None)
    _GattCharacteristicUuids_Meta_.TimeSource = property(get_TimeSource, None)
    _GattCharacteristicUuids_Meta_.TimeUpdateControlPoint = property(get_TimeUpdateControlPoint, None)
    _GattCharacteristicUuids_Meta_.TimeUpdateState = property(get_TimeUpdateState, None)
    _GattCharacteristicUuids_Meta_.TimeWithDst = property(get_TimeWithDst, None)
    _GattCharacteristicUuids_Meta_.TimeZone = property(get_TimeZone, None)
    _GattCharacteristicUuids_Meta_.TxPowerLevel = property(get_TxPowerLevel, None)
    _GattCharacteristicUuids_Meta_.UnreadAlertStatus = property(get_UnreadAlertStatus, None)
class GattCharacteristicsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicsResult
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicsResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicsResult) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_mixinmethod
    def get_ProtocolError(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicsResult) -> win32more.Windows.Foundation.IReference[Byte]: ...
    @winrt_mixinmethod
    def get_Characteristics(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicsResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic]: ...
    Characteristics = property(get_Characteristics, None)
    ProtocolError = property(get_ProtocolError, None)
    Status = property(get_Status, None)
class GattClientCharacteristicConfigurationDescriptorValue(Enum, Int32):
    None_ = 0
    Notify = 1
    Indicate = 2
class GattClientNotificationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattClientNotificationResult
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientNotificationResult'
    @winrt_mixinmethod
    def get_SubscribedClient(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattClientNotificationResult) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSubscribedClient: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattClientNotificationResult) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_mixinmethod
    def get_ProtocolError(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattClientNotificationResult) -> win32more.Windows.Foundation.IReference[Byte]: ...
    @winrt_mixinmethod
    def get_BytesSent(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattClientNotificationResult2) -> UInt16: ...
    BytesSent = property(get_BytesSent, None)
    ProtocolError = property(get_ProtocolError, None)
    Status = property(get_Status, None)
    SubscribedClient = property(get_SubscribedClient, None)
class GattCommunicationStatus(Enum, Int32):
    Success = 0
    Unreachable = 1
    ProtocolError = 2
    AccessDenied = 3
class GattDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptor'
    @winrt_mixinmethod
    def get_ProtectionLevel(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_mixinmethod
    def put_ProtectionLevel(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor, value: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_mixinmethod
    def get_Uuid(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor) -> Guid: ...
    @winrt_mixinmethod
    def get_AttributeHandle(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor) -> UInt16: ...
    @winrt_mixinmethod
    def ReadValueAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadResult]: ...
    @winrt_mixinmethod
    def ReadValueWithCacheModeAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadResult]: ...
    @winrt_mixinmethod
    def WriteValueAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor, value: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
    @winrt_mixinmethod
    def WriteValueWithResultAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor2, value: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
    @winrt_classmethod
    def ConvertShortIdToUuid(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorStatics, shortId: UInt16) -> Guid: ...
    AttributeHandle = property(get_AttributeHandle, None)
    ProtectionLevel = property(get_ProtectionLevel, put_ProtectionLevel)
    Uuid = property(get_Uuid, None)
class _GattDescriptorUuids_Meta_(ComPtr.__class__):
    pass
class GattDescriptorUuids(ComPtr, metaclass=_GattDescriptorUuids_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorUuids'
    @winrt_classmethod
    def get_CharacteristicAggregateFormat(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_CharacteristicExtendedProperties(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_CharacteristicPresentationFormat(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_CharacteristicUserDescription(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_ClientCharacteristicConfiguration(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_ServerCharacteristicConfiguration(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorUuidsStatics) -> Guid: ...
    _GattDescriptorUuids_Meta_.CharacteristicAggregateFormat = property(get_CharacteristicAggregateFormat, None)
    _GattDescriptorUuids_Meta_.CharacteristicExtendedProperties = property(get_CharacteristicExtendedProperties, None)
    _GattDescriptorUuids_Meta_.CharacteristicPresentationFormat = property(get_CharacteristicPresentationFormat, None)
    _GattDescriptorUuids_Meta_.CharacteristicUserDescription = property(get_CharacteristicUserDescription, None)
    _GattDescriptorUuids_Meta_.ClientCharacteristicConfiguration = property(get_ClientCharacteristicConfiguration, None)
    _GattDescriptorUuids_Meta_.ServerCharacteristicConfiguration = property(get_ServerCharacteristicConfiguration, None)
class GattDescriptorsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorsResult
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorsResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorsResult) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_mixinmethod
    def get_ProtocolError(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorsResult) -> win32more.Windows.Foundation.IReference[Byte]: ...
    @winrt_mixinmethod
    def get_Descriptors(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorsResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptor]: ...
    Descriptors = property(get_Descriptors, None)
    ProtocolError = property(get_ProtocolError, None)
    Status = property(get_Status, None)
class GattDeviceService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService'
    @winrt_mixinmethod
    def GetCharacteristics(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService, characteristicUuid: Guid) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic]: ...
    @winrt_mixinmethod
    def GetIncludedServices(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService, serviceUuid: Guid) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Uuid(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService) -> Guid: ...
    @winrt_mixinmethod
    def get_AttributeHandle(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService) -> UInt16: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_Device(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService2) -> win32more.Windows.Devices.Bluetooth.BluetoothLEDevice: ...
    @winrt_mixinmethod
    def get_ParentServices(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_mixinmethod
    def GetAllCharacteristics(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic]: ...
    @winrt_mixinmethod
    def GetAllIncludedServices(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_mixinmethod
    def get_DeviceAccessInformation(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3) -> win32more.Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession: ...
    @winrt_mixinmethod
    def get_SharingMode(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSharingMode: ...
    @winrt_mixinmethod
    def RequestAccessAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceAccessStatus]: ...
    @winrt_mixinmethod
    def OpenAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3, sharingMode: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSharingMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattOpenStatus]: ...
    @winrt_mixinmethod
    def GetCharacteristicsAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicsResult]: ...
    @winrt_mixinmethod
    def GetCharacteristicsWithCacheModeAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicsResult]: ...
    @winrt_mixinmethod
    def GetCharacteristicsForUuidAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3, characteristicUuid: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicsResult]: ...
    @winrt_mixinmethod
    def GetCharacteristicsForUuidWithCacheModeAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3, characteristicUuid: Guid, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicsResult]: ...
    @winrt_mixinmethod
    def GetIncludedServicesAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_mixinmethod
    def GetIncludedServicesWithCacheModeAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_mixinmethod
    def GetIncludedServicesForUuidAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3, serviceUuid: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_mixinmethod
    def GetIncludedServicesForUuidWithCacheModeAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3, serviceUuid: Guid, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_classmethod
    def FromIdWithSharingModeAsync(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics2, deviceId: WinRT_String, sharingMode: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSharingMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_classmethod
    def GetDeviceSelectorForBluetoothDeviceId(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics2, bluetoothDeviceId: win32more.Windows.Devices.Bluetooth.BluetoothDeviceId) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorForBluetoothDeviceIdWithCacheMode(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics2, bluetoothDeviceId: win32more.Windows.Devices.Bluetooth.BluetoothDeviceId, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorForBluetoothDeviceIdAndUuid(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics2, bluetoothDeviceId: win32more.Windows.Devices.Bluetooth.BluetoothDeviceId, serviceUuid: Guid) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorForBluetoothDeviceIdAndUuidWithCacheMode(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics2, bluetoothDeviceId: win32more.Windows.Devices.Bluetooth.BluetoothDeviceId, serviceUuid: Guid, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_classmethod
    def GetDeviceSelectorFromUuid(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics, serviceUuid: Guid) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromShortId(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics, serviceShortId: UInt16) -> WinRT_String: ...
    @winrt_classmethod
    def ConvertShortIdToUuid(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics, shortId: UInt16) -> Guid: ...
    AttributeHandle = property(get_AttributeHandle, None)
    Device = property(get_Device, None)
    DeviceAccessInformation = property(get_DeviceAccessInformation, None)
    DeviceId = property(get_DeviceId, None)
    ParentServices = property(get_ParentServices, None)
    Session = property(get_Session, None)
    SharingMode = property(get_SharingMode, None)
    Uuid = property(get_Uuid, None)
class GattDeviceServicesResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServicesResult
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServicesResult) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_mixinmethod
    def get_ProtocolError(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServicesResult) -> win32more.Windows.Foundation.IReference[Byte]: ...
    @winrt_mixinmethod
    def get_Services(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServicesResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    ProtocolError = property(get_ProtocolError, None)
    Services = property(get_Services, None)
    Status = property(get_Status, None)
class GattLocalCharacteristic(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic'
    @winrt_mixinmethod
    def get_Uuid(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic) -> Guid: ...
    @winrt_mixinmethod
    def get_StaticValue(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_CharacteristicProperties(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties: ...
    @winrt_mixinmethod
    def get_ReadProtectionLevel(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_mixinmethod
    def get_WriteProtectionLevel(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_mixinmethod
    def CreateDescriptorAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic, descriptorUuid: Guid, parameters: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptorParameters) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptorResult]: ...
    @winrt_mixinmethod
    def get_Descriptors(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptor]: ...
    @winrt_mixinmethod
    def get_UserDescription(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PresentationFormats(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormat]: ...
    @winrt_mixinmethod
    def get_SubscribedClients(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSubscribedClient]: ...
    @winrt_mixinmethod
    def add_SubscribedClientsChanged(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SubscribedClientsChanged(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ReadRequested(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic, win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadRequested(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WriteRequested(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic, win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WriteRequested(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def NotifyValueAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic, value: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientNotificationResult]]: ...
    @winrt_mixinmethod
    def NotifyValueForSubscribedClientAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic, value: win32more.Windows.Storage.Streams.IBuffer, subscribedClient: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSubscribedClient) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientNotificationResult]: ...
    CharacteristicProperties = property(get_CharacteristicProperties, None)
    Descriptors = property(get_Descriptors, None)
    PresentationFormats = property(get_PresentationFormats, None)
    ReadProtectionLevel = property(get_ReadProtectionLevel, None)
    StaticValue = property(get_StaticValue, None)
    SubscribedClients = property(get_SubscribedClients, None)
    UserDescription = property(get_UserDescription, None)
    Uuid = property(get_Uuid, None)
    WriteProtectionLevel = property(get_WriteProtectionLevel, None)
    SubscribedClientsChanged = event()
    ReadRequested = event()
    WriteRequested = event()
class GattLocalCharacteristicParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristicParameters'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristicParameters.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristicParameters: ...
    @winrt_mixinmethod
    def put_StaticValue(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_StaticValue(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_CharacteristicProperties(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters, value: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties) -> Void: ...
    @winrt_mixinmethod
    def get_CharacteristicProperties(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties: ...
    @winrt_mixinmethod
    def put_ReadProtectionLevel(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters, value: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_mixinmethod
    def get_ReadProtectionLevel(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_mixinmethod
    def put_WriteProtectionLevel(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters, value: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_mixinmethod
    def get_WriteProtectionLevel(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_mixinmethod
    def put_UserDescription(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_UserDescription(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PresentationFormats(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormat]: ...
    CharacteristicProperties = property(get_CharacteristicProperties, put_CharacteristicProperties)
    PresentationFormats = property(get_PresentationFormats, None)
    ReadProtectionLevel = property(get_ReadProtectionLevel, put_ReadProtectionLevel)
    StaticValue = property(get_StaticValue, put_StaticValue)
    UserDescription = property(get_UserDescription, put_UserDescription)
    WriteProtectionLevel = property(get_WriteProtectionLevel, put_WriteProtectionLevel)
class GattLocalCharacteristicResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicResult
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristicResult'
    @winrt_mixinmethod
    def get_Characteristic(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicResult) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic: ...
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicResult) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    Characteristic = property(get_Characteristic, None)
    Error = property(get_Error, None)
class GattLocalDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptor
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptor'
    @winrt_mixinmethod
    def get_Uuid(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptor) -> Guid: ...
    @winrt_mixinmethod
    def get_StaticValue(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptor) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_ReadProtectionLevel(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptor) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_mixinmethod
    def get_WriteProtectionLevel(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptor) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_mixinmethod
    def add_ReadRequested(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptor, win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadRequested(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WriteRequested(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptor, win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WriteRequested(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ReadProtectionLevel = property(get_ReadProtectionLevel, None)
    StaticValue = property(get_StaticValue, None)
    Uuid = property(get_Uuid, None)
    WriteProtectionLevel = property(get_WriteProtectionLevel, None)
    ReadRequested = event()
    WriteRequested = event()
class GattLocalDescriptorParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorParameters
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptorParameters'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptorParameters.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptorParameters: ...
    @winrt_mixinmethod
    def put_StaticValue(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorParameters, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_StaticValue(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorParameters) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_ReadProtectionLevel(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorParameters, value: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_mixinmethod
    def get_ReadProtectionLevel(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorParameters) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_mixinmethod
    def put_WriteProtectionLevel(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorParameters, value: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_mixinmethod
    def get_WriteProtectionLevel(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorParameters) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    ReadProtectionLevel = property(get_ReadProtectionLevel, put_ReadProtectionLevel)
    StaticValue = property(get_StaticValue, put_StaticValue)
    WriteProtectionLevel = property(get_WriteProtectionLevel, put_WriteProtectionLevel)
class GattLocalDescriptorResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorResult
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptorResult'
    @winrt_mixinmethod
    def get_Descriptor(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorResult) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptor: ...
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorResult) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    Descriptor = property(get_Descriptor, None)
    Error = property(get_Error, None)
class GattLocalService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalService
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalService'
    @winrt_mixinmethod
    def get_Uuid(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalService) -> Guid: ...
    @winrt_mixinmethod
    def CreateCharacteristicAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalService, characteristicUuid: Guid, parameters: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristicParameters) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristicResult]: ...
    @winrt_mixinmethod
    def get_Characteristics(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalService) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic]: ...
    Characteristics = property(get_Characteristics, None)
    Uuid = property(get_Uuid, None)
class GattOpenStatus(Enum, Int32):
    Unspecified = 0
    Success = 1
    AlreadyOpened = 2
    NotFound = 3
    SharingViolation = 4
    AccessDenied = 5
class _GattPresentationFormat_Meta_(ComPtr.__class__):
    pass
class GattPresentationFormat(ComPtr, metaclass=_GattPresentationFormat_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormat
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormat'
    @winrt_mixinmethod
    def get_FormatType(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormat) -> Byte: ...
    @winrt_mixinmethod
    def get_Exponent(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormat) -> Int32: ...
    @winrt_mixinmethod
    def get_Unit(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormat) -> UInt16: ...
    @winrt_mixinmethod
    def get_Namespace(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormat) -> Byte: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormat) -> UInt16: ...
    @winrt_classmethod
    def FromParts(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatStatics2, formatType: Byte, exponent: Int32, unit: UInt16, namespaceId: Byte, description: UInt16) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormat: ...
    @winrt_classmethod
    def get_BluetoothSigAssignedNumbers(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatStatics) -> Byte: ...
    Description = property(get_Description, None)
    Exponent = property(get_Exponent, None)
    FormatType = property(get_FormatType, None)
    Namespace = property(get_Namespace, None)
    Unit = property(get_Unit, None)
    _GattPresentationFormat_Meta_.BluetoothSigAssignedNumbers = property(get_BluetoothSigAssignedNumbers, None)
class _GattPresentationFormatTypes_Meta_(ComPtr.__class__):
    pass
class GattPresentationFormatTypes(ComPtr, metaclass=_GattPresentationFormatTypes_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormatTypes'
    @winrt_classmethod
    def get_Boolean(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_Bit2(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_Nibble(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_UInt8(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_UInt12(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_UInt16(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_UInt24(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_UInt32(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_UInt48(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_UInt64(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_UInt128(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_SInt8(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_SInt12(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_SInt16(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_SInt24(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_SInt32(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_SInt48(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_SInt64(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_SInt128(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_Float32(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_Float64(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_SFloat(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_Float(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_DUInt16(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_Utf8(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_Utf16(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_Struct(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    _GattPresentationFormatTypes_Meta_.Bit2 = property(get_Bit2, None)
    _GattPresentationFormatTypes_Meta_.Boolean = property(get_Boolean, None)
    _GattPresentationFormatTypes_Meta_.DUInt16 = property(get_DUInt16, None)
    _GattPresentationFormatTypes_Meta_.Float = property(get_Float, None)
    _GattPresentationFormatTypes_Meta_.Float32 = property(get_Float32, None)
    _GattPresentationFormatTypes_Meta_.Float64 = property(get_Float64, None)
    _GattPresentationFormatTypes_Meta_.Nibble = property(get_Nibble, None)
    _GattPresentationFormatTypes_Meta_.SFloat = property(get_SFloat, None)
    _GattPresentationFormatTypes_Meta_.SInt12 = property(get_SInt12, None)
    _GattPresentationFormatTypes_Meta_.SInt128 = property(get_SInt128, None)
    _GattPresentationFormatTypes_Meta_.SInt16 = property(get_SInt16, None)
    _GattPresentationFormatTypes_Meta_.SInt24 = property(get_SInt24, None)
    _GattPresentationFormatTypes_Meta_.SInt32 = property(get_SInt32, None)
    _GattPresentationFormatTypes_Meta_.SInt48 = property(get_SInt48, None)
    _GattPresentationFormatTypes_Meta_.SInt64 = property(get_SInt64, None)
    _GattPresentationFormatTypes_Meta_.SInt8 = property(get_SInt8, None)
    _GattPresentationFormatTypes_Meta_.Struct = property(get_Struct, None)
    _GattPresentationFormatTypes_Meta_.UInt12 = property(get_UInt12, None)
    _GattPresentationFormatTypes_Meta_.UInt128 = property(get_UInt128, None)
    _GattPresentationFormatTypes_Meta_.UInt16 = property(get_UInt16, None)
    _GattPresentationFormatTypes_Meta_.UInt24 = property(get_UInt24, None)
    _GattPresentationFormatTypes_Meta_.UInt32 = property(get_UInt32, None)
    _GattPresentationFormatTypes_Meta_.UInt48 = property(get_UInt48, None)
    _GattPresentationFormatTypes_Meta_.UInt64 = property(get_UInt64, None)
    _GattPresentationFormatTypes_Meta_.UInt8 = property(get_UInt8, None)
    _GattPresentationFormatTypes_Meta_.Utf16 = property(get_Utf16, None)
    _GattPresentationFormatTypes_Meta_.Utf8 = property(get_Utf8, None)
class GattProtectionLevel(Enum, Int32):
    Plain = 0
    AuthenticationRequired = 1
    EncryptionRequired = 2
    EncryptionAndAuthenticationRequired = 3
class _GattProtocolError_Meta_(ComPtr.__class__):
    pass
class GattProtocolError(ComPtr, metaclass=_GattProtocolError_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtocolError'
    @winrt_classmethod
    def get_InvalidHandle(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_ReadNotPermitted(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_WriteNotPermitted(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_InvalidPdu(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_InsufficientAuthentication(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_RequestNotSupported(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_InvalidOffset(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_InsufficientAuthorization(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_PrepareQueueFull(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_AttributeNotFound(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_AttributeNotLong(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_InsufficientEncryptionKeySize(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_InvalidAttributeValueLength(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_UnlikelyError(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_InsufficientEncryption(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_UnsupportedGroupType(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_InsufficientResources(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    _GattProtocolError_Meta_.AttributeNotFound = property(get_AttributeNotFound, None)
    _GattProtocolError_Meta_.AttributeNotLong = property(get_AttributeNotLong, None)
    _GattProtocolError_Meta_.InsufficientAuthentication = property(get_InsufficientAuthentication, None)
    _GattProtocolError_Meta_.InsufficientAuthorization = property(get_InsufficientAuthorization, None)
    _GattProtocolError_Meta_.InsufficientEncryption = property(get_InsufficientEncryption, None)
    _GattProtocolError_Meta_.InsufficientEncryptionKeySize = property(get_InsufficientEncryptionKeySize, None)
    _GattProtocolError_Meta_.InsufficientResources = property(get_InsufficientResources, None)
    _GattProtocolError_Meta_.InvalidAttributeValueLength = property(get_InvalidAttributeValueLength, None)
    _GattProtocolError_Meta_.InvalidHandle = property(get_InvalidHandle, None)
    _GattProtocolError_Meta_.InvalidOffset = property(get_InvalidOffset, None)
    _GattProtocolError_Meta_.InvalidPdu = property(get_InvalidPdu, None)
    _GattProtocolError_Meta_.PrepareQueueFull = property(get_PrepareQueueFull, None)
    _GattProtocolError_Meta_.ReadNotPermitted = property(get_ReadNotPermitted, None)
    _GattProtocolError_Meta_.RequestNotSupported = property(get_RequestNotSupported, None)
    _GattProtocolError_Meta_.UnlikelyError = property(get_UnlikelyError, None)
    _GattProtocolError_Meta_.UnsupportedGroupType = property(get_UnsupportedGroupType, None)
    _GattProtocolError_Meta_.WriteNotPermitted = property(get_WriteNotPermitted, None)
class GattReadClientCharacteristicConfigurationDescriptorResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadClientCharacteristicConfigurationDescriptorResult
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadClientCharacteristicConfigurationDescriptorResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadClientCharacteristicConfigurationDescriptorResult) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_mixinmethod
    def get_ClientCharacteristicConfigurationDescriptor(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadClientCharacteristicConfigurationDescriptorResult) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientCharacteristicConfigurationDescriptorValue: ...
    @winrt_mixinmethod
    def get_ProtocolError(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadClientCharacteristicConfigurationDescriptorResult2) -> win32more.Windows.Foundation.IReference[Byte]: ...
    ClientCharacteristicConfigurationDescriptor = property(get_ClientCharacteristicConfigurationDescriptor, None)
    ProtocolError = property(get_ProtocolError, None)
    Status = property(get_Status, None)
class GattReadRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequest
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequest'
    @winrt_mixinmethod
    def get_Offset(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequest) -> UInt32: ...
    @winrt_mixinmethod
    def get_Length(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequest) -> UInt32: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequest) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestState: ...
    @winrt_mixinmethod
    def add_StateChanged(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequest, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequest, win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequest, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def RespondWithValue(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequest, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def RespondWithProtocolError(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequest, protocolError: Byte) -> Void: ...
    Length = property(get_Length, None)
    Offset = property(get_Offset, None)
    State = property(get_State, None)
    StateChanged = event()
class GattReadRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequestedEventArgs
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequestedEventArgs'
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequestedEventArgs) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def GetRequestAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequestedEventArgs) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequest]: ...
    Session = property(get_Session, None)
class GattReadResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadResult
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadResult) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadResult) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_ProtocolError(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadResult2) -> win32more.Windows.Foundation.IReference[Byte]: ...
    ProtocolError = property(get_ProtocolError, None)
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class GattReliableWriteTransaction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReliableWriteTransaction
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattReliableWriteTransaction'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReliableWriteTransaction.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReliableWriteTransaction: ...
    @winrt_mixinmethod
    def WriteValue(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReliableWriteTransaction, characteristic: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def CommitAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReliableWriteTransaction) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
    @winrt_mixinmethod
    def CommitWithResultAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReliableWriteTransaction2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
class GattRequestState(Enum, Int32):
    Pending = 0
    Completed = 1
    Canceled = 2
class GattRequestStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattRequestStateChangedEventArgs
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestStateChangedEventArgs'
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattRequestStateChangedEventArgs) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestState: ...
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattRequestStateChangedEventArgs) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    Error = property(get_Error, None)
    State = property(get_State, None)
class GattServiceProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProvider
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProvider'
    @winrt_mixinmethod
    def get_Service(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProvider) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalService: ...
    @winrt_mixinmethod
    def get_AdvertisementStatus(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProvider) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisementStatus: ...
    @winrt_mixinmethod
    def add_AdvertisementStatusChanged(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProvider, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProvider, win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisementStatusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AdvertisementStatusChanged(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProvider, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def StartAdvertising(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProvider) -> Void: ...
    @winrt_mixinmethod
    def StartAdvertisingWithParameters(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProvider, parameters: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisingParameters) -> Void: ...
    @winrt_mixinmethod
    def StopAdvertising(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProvider) -> Void: ...
    @winrt_classmethod
    def CreateAsync(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderStatics, serviceUuid: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderResult]: ...
    AdvertisementStatus = property(get_AdvertisementStatus, None)
    Service = property(get_Service, None)
    AdvertisementStatusChanged = event()
class GattServiceProviderAdvertisementStatus(Enum, Int32):
    Created = 0
    Stopped = 1
    Started = 2
    Aborted = 3
    StartedWithoutAllAdvertisementData = 4
class GattServiceProviderAdvertisementStatusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisementStatusChangedEventArgs
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisementStatusChangedEventArgs'
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisementStatusChangedEventArgs) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisementStatusChangedEventArgs) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisementStatus: ...
    Error = property(get_Error, None)
    Status = property(get_Status, None)
class GattServiceProviderAdvertisingParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisingParameters
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisingParameters'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisingParameters.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisingParameters: ...
    @winrt_mixinmethod
    def put_IsConnectable(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisingParameters, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsConnectable(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisingParameters) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDiscoverable(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisingParameters, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDiscoverable(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisingParameters) -> Boolean: ...
    @winrt_mixinmethod
    def put_ServiceData(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisingParameters2, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_ServiceData(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisingParameters2) -> win32more.Windows.Storage.Streams.IBuffer: ...
    IsConnectable = property(get_IsConnectable, put_IsConnectable)
    IsDiscoverable = property(get_IsDiscoverable, put_IsDiscoverable)
    ServiceData = property(get_ServiceData, put_ServiceData)
class GattServiceProviderResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderResult
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderResult'
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderResult) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_mixinmethod
    def get_ServiceProvider(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderResult) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProvider: ...
    Error = property(get_Error, None)
    ServiceProvider = property(get_ServiceProvider, None)
class _GattServiceUuids_Meta_(ComPtr.__class__):
    pass
class GattServiceUuids(ComPtr, metaclass=_GattServiceUuids_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceUuids'
    @winrt_classmethod
    def get_AlertNotification(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_CurrentTime(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_CyclingPower(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_DeviceInformation(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_HumanInterfaceDevice(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ImmediateAlert(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_LinkLoss(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_LocationAndNavigation(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_NextDstChange(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_PhoneAlertStatus(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ReferenceTimeUpdate(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ScanParameters(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_TxPower(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_Battery(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_BloodPressure(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_CyclingSpeedAndCadence(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_GenericAccess(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_GenericAttribute(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_Glucose(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_HealthThermometer(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_HeartRate(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_RunningSpeedAndCadence(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics) -> Guid: ...
    _GattServiceUuids_Meta_.AlertNotification = property(get_AlertNotification, None)
    _GattServiceUuids_Meta_.Battery = property(get_Battery, None)
    _GattServiceUuids_Meta_.BloodPressure = property(get_BloodPressure, None)
    _GattServiceUuids_Meta_.CurrentTime = property(get_CurrentTime, None)
    _GattServiceUuids_Meta_.CyclingPower = property(get_CyclingPower, None)
    _GattServiceUuids_Meta_.CyclingSpeedAndCadence = property(get_CyclingSpeedAndCadence, None)
    _GattServiceUuids_Meta_.DeviceInformation = property(get_DeviceInformation, None)
    _GattServiceUuids_Meta_.GenericAccess = property(get_GenericAccess, None)
    _GattServiceUuids_Meta_.GenericAttribute = property(get_GenericAttribute, None)
    _GattServiceUuids_Meta_.Glucose = property(get_Glucose, None)
    _GattServiceUuids_Meta_.HealthThermometer = property(get_HealthThermometer, None)
    _GattServiceUuids_Meta_.HeartRate = property(get_HeartRate, None)
    _GattServiceUuids_Meta_.HumanInterfaceDevice = property(get_HumanInterfaceDevice, None)
    _GattServiceUuids_Meta_.ImmediateAlert = property(get_ImmediateAlert, None)
    _GattServiceUuids_Meta_.LinkLoss = property(get_LinkLoss, None)
    _GattServiceUuids_Meta_.LocationAndNavigation = property(get_LocationAndNavigation, None)
    _GattServiceUuids_Meta_.NextDstChange = property(get_NextDstChange, None)
    _GattServiceUuids_Meta_.PhoneAlertStatus = property(get_PhoneAlertStatus, None)
    _GattServiceUuids_Meta_.ReferenceTimeUpdate = property(get_ReferenceTimeUpdate, None)
    _GattServiceUuids_Meta_.RunningSpeedAndCadence = property(get_RunningSpeedAndCadence, None)
    _GattServiceUuids_Meta_.ScanParameters = property(get_ScanParameters, None)
    _GattServiceUuids_Meta_.TxPower = property(get_TxPower, None)
class GattSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession) -> win32more.Windows.Devices.Bluetooth.BluetoothDeviceId: ...
    @winrt_mixinmethod
    def get_CanMaintainConnection(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession) -> Boolean: ...
    @winrt_mixinmethod
    def put_MaintainConnection(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MaintainConnection(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxPduSize(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession) -> UInt16: ...
    @winrt_mixinmethod
    def get_SessionStatus(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSessionStatus: ...
    @winrt_mixinmethod
    def add_MaxPduSizeChanged(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MaxPduSizeChanged(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SessionStatusChanged(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession, win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSessionStatusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SessionStatusChanged(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def FromDeviceIdAsync(cls: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSessionStatics, deviceId: win32more.Windows.Devices.Bluetooth.BluetoothDeviceId) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession]: ...
    CanMaintainConnection = property(get_CanMaintainConnection, None)
    DeviceId = property(get_DeviceId, None)
    MaintainConnection = property(get_MaintainConnection, put_MaintainConnection)
    MaxPduSize = property(get_MaxPduSize, None)
    SessionStatus = property(get_SessionStatus, None)
    MaxPduSizeChanged = event()
    SessionStatusChanged = event()
class GattSessionStatus(Enum, Int32):
    Closed = 0
    Active = 1
class GattSessionStatusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSessionStatusChangedEventArgs
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattSessionStatusChangedEventArgs'
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSessionStatusChangedEventArgs) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSessionStatusChangedEventArgs) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSessionStatus: ...
    Error = property(get_Error, None)
    Status = property(get_Status, None)
class GattSharingMode(Enum, Int32):
    Unspecified = 0
    Exclusive = 1
    SharedReadOnly = 2
    SharedReadAndWrite = 3
class GattSubscribedClient(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSubscribedClient
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattSubscribedClient'
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSubscribedClient) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession: ...
    @winrt_mixinmethod
    def get_MaxNotificationSize(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSubscribedClient) -> UInt16: ...
    @winrt_mixinmethod
    def add_MaxNotificationSizeChanged(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSubscribedClient, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSubscribedClient, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MaxNotificationSizeChanged(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSubscribedClient, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    MaxNotificationSize = property(get_MaxNotificationSize, None)
    Session = property(get_Session, None)
    MaxNotificationSizeChanged = event()
class GattValueChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattValueChangedEventArgs
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattValueChangedEventArgs'
    @winrt_mixinmethod
    def get_CharacteristicValue(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattValueChangedEventArgs) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattValueChangedEventArgs) -> win32more.Windows.Foundation.DateTime: ...
    CharacteristicValue = property(get_CharacteristicValue, None)
    Timestamp = property(get_Timestamp, None)
class GattWriteOption(Enum, Int32):
    WriteWithResponse = 0
    WriteWithoutResponse = 1
class GattWriteRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequest
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequest'
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequest) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Offset(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequest) -> UInt32: ...
    @winrt_mixinmethod
    def get_Option(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequest) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteOption: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequest) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestState: ...
    @winrt_mixinmethod
    def add_StateChanged(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequest, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequest, win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequest, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Respond(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequest) -> Void: ...
    @winrt_mixinmethod
    def RespondWithProtocolError(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequest, protocolError: Byte) -> Void: ...
    Offset = property(get_Offset, None)
    Option = property(get_Option, None)
    State = property(get_State, None)
    Value = property(get_Value, None)
    StateChanged = event()
class GattWriteRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequestedEventArgs
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequestedEventArgs'
    @winrt_mixinmethod
    def get_Session(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequestedEventArgs) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def GetRequestAsync(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequestedEventArgs) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequest]: ...
    Session = property(get_Session, None)
class GattWriteResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteResult
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteResult) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_mixinmethod
    def get_ProtocolError(self: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteResult) -> win32more.Windows.Foundation.IReference[Byte]: ...
    ProtocolError = property(get_ProtocolError, None)
    Status = property(get_Status, None)
class IGattCharacteristic(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic'
    _iid_ = Guid('{59cb50c1-5934-4f68-a198-eb864fa44e6b}')
    @winrt_commethod(6)
    def GetDescriptors(self, descriptorUuid: Guid) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptor]: ...
    @winrt_commethod(7)
    def get_CharacteristicProperties(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties: ...
    @winrt_commethod(8)
    def get_ProtectionLevel(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_commethod(9)
    def put_ProtectionLevel(self, value: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_commethod(10)
    def get_UserDescription(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Uuid(self) -> Guid: ...
    @winrt_commethod(12)
    def get_AttributeHandle(self) -> UInt16: ...
    @winrt_commethod(13)
    def get_PresentationFormats(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormat]: ...
    @winrt_commethod(14)
    def ReadValueAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadResult]: ...
    @winrt_commethod(15)
    def ReadValueWithCacheModeAsync(self, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadResult]: ...
    @winrt_commethod(16)
    def WriteValueAsync(self, value: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
    @winrt_commethod(17)
    def WriteValueWithOptionAsync(self, value: win32more.Windows.Storage.Streams.IBuffer, writeOption: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
    @winrt_commethod(18)
    def ReadClientCharacteristicConfigurationDescriptorAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadClientCharacteristicConfigurationDescriptorResult]: ...
    @winrt_commethod(19)
    def WriteClientCharacteristicConfigurationDescriptorAsync(self, clientCharacteristicConfigurationDescriptorValue: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientCharacteristicConfigurationDescriptorValue) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
    @winrt_commethod(20)
    def add_ValueChanged(self, valueChangedHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic, win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattValueChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_ValueChanged(self, valueChangedEventCookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AttributeHandle = property(get_AttributeHandle, None)
    CharacteristicProperties = property(get_CharacteristicProperties, None)
    PresentationFormats = property(get_PresentationFormats, None)
    ProtectionLevel = property(get_ProtectionLevel, put_ProtectionLevel)
    UserDescription = property(get_UserDescription, None)
    Uuid = property(get_Uuid, None)
    ValueChanged = event()
class IGattCharacteristic2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic2'
    _iid_ = Guid('{ae1ab578-ec06-4764-b780-9835a1d35d6e}')
    @winrt_commethod(6)
    def get_Service(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService: ...
    @winrt_commethod(7)
    def GetAllDescriptors(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptor]: ...
    Service = property(get_Service, None)
class IGattCharacteristic3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic3'
    _iid_ = Guid('{3f3c663e-93d4-406b-b817-db81f8ed53b3}')
    @winrt_commethod(6)
    def GetDescriptorsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorsResult]: ...
    @winrt_commethod(7)
    def GetDescriptorsWithCacheModeAsync(self, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorsResult]: ...
    @winrt_commethod(8)
    def GetDescriptorsForUuidAsync(self, descriptorUuid: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorsResult]: ...
    @winrt_commethod(9)
    def GetDescriptorsForUuidWithCacheModeAsync(self, descriptorUuid: Guid, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorsResult]: ...
    @winrt_commethod(10)
    def WriteValueWithResultAsync(self, value: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
    @winrt_commethod(11)
    def WriteValueWithResultAndOptionAsync(self, value: win32more.Windows.Storage.Streams.IBuffer, writeOption: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteOption) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
    @winrt_commethod(12)
    def WriteClientCharacteristicConfigurationDescriptorWithResultAsync(self, clientCharacteristicConfigurationDescriptorValue: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientCharacteristicConfigurationDescriptorValue) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
class IGattCharacteristicStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicStatics'
    _iid_ = Guid('{59cb50c3-5934-4f68-a198-eb864fa44e6b}')
    @winrt_commethod(6)
    def ConvertShortIdToUuid(self, shortId: UInt16) -> Guid: ...
class IGattCharacteristicUuidsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics'
    _iid_ = Guid('{58fa4586-b1de-470c-b7de-0d11ff44f4b7}')
    @winrt_commethod(6)
    def get_BatteryLevel(self) -> Guid: ...
    @winrt_commethod(7)
    def get_BloodPressureFeature(self) -> Guid: ...
    @winrt_commethod(8)
    def get_BloodPressureMeasurement(self) -> Guid: ...
    @winrt_commethod(9)
    def get_BodySensorLocation(self) -> Guid: ...
    @winrt_commethod(10)
    def get_CscFeature(self) -> Guid: ...
    @winrt_commethod(11)
    def get_CscMeasurement(self) -> Guid: ...
    @winrt_commethod(12)
    def get_GlucoseFeature(self) -> Guid: ...
    @winrt_commethod(13)
    def get_GlucoseMeasurement(self) -> Guid: ...
    @winrt_commethod(14)
    def get_GlucoseMeasurementContext(self) -> Guid: ...
    @winrt_commethod(15)
    def get_HeartRateControlPoint(self) -> Guid: ...
    @winrt_commethod(16)
    def get_HeartRateMeasurement(self) -> Guid: ...
    @winrt_commethod(17)
    def get_IntermediateCuffPressure(self) -> Guid: ...
    @winrt_commethod(18)
    def get_IntermediateTemperature(self) -> Guid: ...
    @winrt_commethod(19)
    def get_MeasurementInterval(self) -> Guid: ...
    @winrt_commethod(20)
    def get_RecordAccessControlPoint(self) -> Guid: ...
    @winrt_commethod(21)
    def get_RscFeature(self) -> Guid: ...
    @winrt_commethod(22)
    def get_RscMeasurement(self) -> Guid: ...
    @winrt_commethod(23)
    def get_SCControlPoint(self) -> Guid: ...
    @winrt_commethod(24)
    def get_SensorLocation(self) -> Guid: ...
    @winrt_commethod(25)
    def get_TemperatureMeasurement(self) -> Guid: ...
    @winrt_commethod(26)
    def get_TemperatureType(self) -> Guid: ...
    BatteryLevel = property(get_BatteryLevel, None)
    BloodPressureFeature = property(get_BloodPressureFeature, None)
    BloodPressureMeasurement = property(get_BloodPressureMeasurement, None)
    BodySensorLocation = property(get_BodySensorLocation, None)
    CscFeature = property(get_CscFeature, None)
    CscMeasurement = property(get_CscMeasurement, None)
    GlucoseFeature = property(get_GlucoseFeature, None)
    GlucoseMeasurement = property(get_GlucoseMeasurement, None)
    GlucoseMeasurementContext = property(get_GlucoseMeasurementContext, None)
    HeartRateControlPoint = property(get_HeartRateControlPoint, None)
    HeartRateMeasurement = property(get_HeartRateMeasurement, None)
    IntermediateCuffPressure = property(get_IntermediateCuffPressure, None)
    IntermediateTemperature = property(get_IntermediateTemperature, None)
    MeasurementInterval = property(get_MeasurementInterval, None)
    RecordAccessControlPoint = property(get_RecordAccessControlPoint, None)
    RscFeature = property(get_RscFeature, None)
    RscMeasurement = property(get_RscMeasurement, None)
    SCControlPoint = property(get_SCControlPoint, None)
    SensorLocation = property(get_SensorLocation, None)
    TemperatureMeasurement = property(get_TemperatureMeasurement, None)
    TemperatureType = property(get_TemperatureType, None)
class IGattCharacteristicUuidsStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2'
    _iid_ = Guid('{1855b425-d46e-4a2c-9c3f-ed6dea29e7be}')
    @winrt_commethod(6)
    def get_AlertCategoryId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_AlertCategoryIdBitMask(self) -> Guid: ...
    @winrt_commethod(8)
    def get_AlertLevel(self) -> Guid: ...
    @winrt_commethod(9)
    def get_AlertNotificationControlPoint(self) -> Guid: ...
    @winrt_commethod(10)
    def get_AlertStatus(self) -> Guid: ...
    @winrt_commethod(11)
    def get_GapAppearance(self) -> Guid: ...
    @winrt_commethod(12)
    def get_BootKeyboardInputReport(self) -> Guid: ...
    @winrt_commethod(13)
    def get_BootKeyboardOutputReport(self) -> Guid: ...
    @winrt_commethod(14)
    def get_BootMouseInputReport(self) -> Guid: ...
    @winrt_commethod(15)
    def get_CurrentTime(self) -> Guid: ...
    @winrt_commethod(16)
    def get_CyclingPowerControlPoint(self) -> Guid: ...
    @winrt_commethod(17)
    def get_CyclingPowerFeature(self) -> Guid: ...
    @winrt_commethod(18)
    def get_CyclingPowerMeasurement(self) -> Guid: ...
    @winrt_commethod(19)
    def get_CyclingPowerVector(self) -> Guid: ...
    @winrt_commethod(20)
    def get_DateTime(self) -> Guid: ...
    @winrt_commethod(21)
    def get_DayDateTime(self) -> Guid: ...
    @winrt_commethod(22)
    def get_DayOfWeek(self) -> Guid: ...
    @winrt_commethod(23)
    def get_GapDeviceName(self) -> Guid: ...
    @winrt_commethod(24)
    def get_DstOffset(self) -> Guid: ...
    @winrt_commethod(25)
    def get_ExactTime256(self) -> Guid: ...
    @winrt_commethod(26)
    def get_FirmwareRevisionString(self) -> Guid: ...
    @winrt_commethod(27)
    def get_HardwareRevisionString(self) -> Guid: ...
    @winrt_commethod(28)
    def get_HidControlPoint(self) -> Guid: ...
    @winrt_commethod(29)
    def get_HidInformation(self) -> Guid: ...
    @winrt_commethod(30)
    def get_Ieee1107320601RegulatoryCertificationDataList(self) -> Guid: ...
    @winrt_commethod(31)
    def get_LnControlPoint(self) -> Guid: ...
    @winrt_commethod(32)
    def get_LnFeature(self) -> Guid: ...
    @winrt_commethod(33)
    def get_LocalTimeInformation(self) -> Guid: ...
    @winrt_commethod(34)
    def get_LocationAndSpeed(self) -> Guid: ...
    @winrt_commethod(35)
    def get_ManufacturerNameString(self) -> Guid: ...
    @winrt_commethod(36)
    def get_ModelNumberString(self) -> Guid: ...
    @winrt_commethod(37)
    def get_Navigation(self) -> Guid: ...
    @winrt_commethod(38)
    def get_NewAlert(self) -> Guid: ...
    @winrt_commethod(39)
    def get_GapPeripheralPreferredConnectionParameters(self) -> Guid: ...
    @winrt_commethod(40)
    def get_GapPeripheralPrivacyFlag(self) -> Guid: ...
    @winrt_commethod(41)
    def get_PnpId(self) -> Guid: ...
    @winrt_commethod(42)
    def get_PositionQuality(self) -> Guid: ...
    @winrt_commethod(43)
    def get_ProtocolMode(self) -> Guid: ...
    @winrt_commethod(44)
    def get_GapReconnectionAddress(self) -> Guid: ...
    @winrt_commethod(45)
    def get_ReferenceTimeInformation(self) -> Guid: ...
    @winrt_commethod(46)
    def get_Report(self) -> Guid: ...
    @winrt_commethod(47)
    def get_ReportMap(self) -> Guid: ...
    @winrt_commethod(48)
    def get_RingerControlPoint(self) -> Guid: ...
    @winrt_commethod(49)
    def get_RingerSetting(self) -> Guid: ...
    @winrt_commethod(50)
    def get_ScanIntervalWindow(self) -> Guid: ...
    @winrt_commethod(51)
    def get_ScanRefresh(self) -> Guid: ...
    @winrt_commethod(52)
    def get_SerialNumberString(self) -> Guid: ...
    @winrt_commethod(53)
    def get_GattServiceChanged(self) -> Guid: ...
    @winrt_commethod(54)
    def get_SoftwareRevisionString(self) -> Guid: ...
    @winrt_commethod(55)
    def get_SupportedNewAlertCategory(self) -> Guid: ...
    @winrt_commethod(56)
    def get_SupportUnreadAlertCategory(self) -> Guid: ...
    @winrt_commethod(57)
    def get_SystemId(self) -> Guid: ...
    @winrt_commethod(58)
    def get_TimeAccuracy(self) -> Guid: ...
    @winrt_commethod(59)
    def get_TimeSource(self) -> Guid: ...
    @winrt_commethod(60)
    def get_TimeUpdateControlPoint(self) -> Guid: ...
    @winrt_commethod(61)
    def get_TimeUpdateState(self) -> Guid: ...
    @winrt_commethod(62)
    def get_TimeWithDst(self) -> Guid: ...
    @winrt_commethod(63)
    def get_TimeZone(self) -> Guid: ...
    @winrt_commethod(64)
    def get_TxPowerLevel(self) -> Guid: ...
    @winrt_commethod(65)
    def get_UnreadAlertStatus(self) -> Guid: ...
    AlertCategoryId = property(get_AlertCategoryId, None)
    AlertCategoryIdBitMask = property(get_AlertCategoryIdBitMask, None)
    AlertLevel = property(get_AlertLevel, None)
    AlertNotificationControlPoint = property(get_AlertNotificationControlPoint, None)
    AlertStatus = property(get_AlertStatus, None)
    BootKeyboardInputReport = property(get_BootKeyboardInputReport, None)
    BootKeyboardOutputReport = property(get_BootKeyboardOutputReport, None)
    BootMouseInputReport = property(get_BootMouseInputReport, None)
    CurrentTime = property(get_CurrentTime, None)
    CyclingPowerControlPoint = property(get_CyclingPowerControlPoint, None)
    CyclingPowerFeature = property(get_CyclingPowerFeature, None)
    CyclingPowerMeasurement = property(get_CyclingPowerMeasurement, None)
    CyclingPowerVector = property(get_CyclingPowerVector, None)
    DateTime = property(get_DateTime, None)
    DayDateTime = property(get_DayDateTime, None)
    DayOfWeek = property(get_DayOfWeek, None)
    DstOffset = property(get_DstOffset, None)
    ExactTime256 = property(get_ExactTime256, None)
    FirmwareRevisionString = property(get_FirmwareRevisionString, None)
    GapAppearance = property(get_GapAppearance, None)
    GapDeviceName = property(get_GapDeviceName, None)
    GapPeripheralPreferredConnectionParameters = property(get_GapPeripheralPreferredConnectionParameters, None)
    GapPeripheralPrivacyFlag = property(get_GapPeripheralPrivacyFlag, None)
    GapReconnectionAddress = property(get_GapReconnectionAddress, None)
    GattServiceChanged = property(get_GattServiceChanged, None)
    HardwareRevisionString = property(get_HardwareRevisionString, None)
    HidControlPoint = property(get_HidControlPoint, None)
    HidInformation = property(get_HidInformation, None)
    Ieee1107320601RegulatoryCertificationDataList = property(get_Ieee1107320601RegulatoryCertificationDataList, None)
    LnControlPoint = property(get_LnControlPoint, None)
    LnFeature = property(get_LnFeature, None)
    LocalTimeInformation = property(get_LocalTimeInformation, None)
    LocationAndSpeed = property(get_LocationAndSpeed, None)
    ManufacturerNameString = property(get_ManufacturerNameString, None)
    ModelNumberString = property(get_ModelNumberString, None)
    Navigation = property(get_Navigation, None)
    NewAlert = property(get_NewAlert, None)
    PnpId = property(get_PnpId, None)
    PositionQuality = property(get_PositionQuality, None)
    ProtocolMode = property(get_ProtocolMode, None)
    ReferenceTimeInformation = property(get_ReferenceTimeInformation, None)
    Report = property(get_Report, None)
    ReportMap = property(get_ReportMap, None)
    RingerControlPoint = property(get_RingerControlPoint, None)
    RingerSetting = property(get_RingerSetting, None)
    ScanIntervalWindow = property(get_ScanIntervalWindow, None)
    ScanRefresh = property(get_ScanRefresh, None)
    SerialNumberString = property(get_SerialNumberString, None)
    SoftwareRevisionString = property(get_SoftwareRevisionString, None)
    SupportUnreadAlertCategory = property(get_SupportUnreadAlertCategory, None)
    SupportedNewAlertCategory = property(get_SupportedNewAlertCategory, None)
    SystemId = property(get_SystemId, None)
    TimeAccuracy = property(get_TimeAccuracy, None)
    TimeSource = property(get_TimeSource, None)
    TimeUpdateControlPoint = property(get_TimeUpdateControlPoint, None)
    TimeUpdateState = property(get_TimeUpdateState, None)
    TimeWithDst = property(get_TimeWithDst, None)
    TimeZone = property(get_TimeZone, None)
    TxPowerLevel = property(get_TxPowerLevel, None)
    UnreadAlertStatus = property(get_UnreadAlertStatus, None)
class IGattCharacteristicsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicsResult'
    _iid_ = Guid('{1194945c-b257-4f3e-9db7-f68bc9a9aef2}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_commethod(7)
    def get_ProtocolError(self) -> win32more.Windows.Foundation.IReference[Byte]: ...
    @winrt_commethod(8)
    def get_Characteristics(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic]: ...
    Characteristics = property(get_Characteristics, None)
    ProtocolError = property(get_ProtocolError, None)
    Status = property(get_Status, None)
class IGattClientNotificationResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattClientNotificationResult'
    _iid_ = Guid('{506d5599-0112-419a-8e3b-ae21afabd2c2}')
    @winrt_commethod(6)
    def get_SubscribedClient(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSubscribedClient: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_commethod(8)
    def get_ProtocolError(self) -> win32more.Windows.Foundation.IReference[Byte]: ...
    ProtocolError = property(get_ProtocolError, None)
    Status = property(get_Status, None)
    SubscribedClient = property(get_SubscribedClient, None)
class IGattClientNotificationResult2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattClientNotificationResult2'
    _iid_ = Guid('{8faec497-45e0-497e-9582-29a1fe281ad5}')
    @winrt_commethod(6)
    def get_BytesSent(self) -> UInt16: ...
    BytesSent = property(get_BytesSent, None)
class IGattDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor'
    _iid_ = Guid('{92055f2b-8084-4344-b4c2-284de19a8506}')
    @winrt_commethod(6)
    def get_ProtectionLevel(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_commethod(7)
    def put_ProtectionLevel(self, value: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_commethod(8)
    def get_Uuid(self) -> Guid: ...
    @winrt_commethod(9)
    def get_AttributeHandle(self) -> UInt16: ...
    @winrt_commethod(10)
    def ReadValueAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadResult]: ...
    @winrt_commethod(11)
    def ReadValueWithCacheModeAsync(self, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadResult]: ...
    @winrt_commethod(12)
    def WriteValueAsync(self, value: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
    AttributeHandle = property(get_AttributeHandle, None)
    ProtectionLevel = property(get_ProtectionLevel, put_ProtectionLevel)
    Uuid = property(get_Uuid, None)
class IGattDescriptor2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor2'
    _iid_ = Guid('{8f563d39-d630-406c-ba11-10cdd16b0e5e}')
    @winrt_commethod(6)
    def WriteValueWithResultAsync(self, value: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
class IGattDescriptorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorStatics'
    _iid_ = Guid('{92055f2d-8084-4344-b4c2-284de19a8506}')
    @winrt_commethod(6)
    def ConvertShortIdToUuid(self, shortId: UInt16) -> Guid: ...
class IGattDescriptorUuidsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorUuidsStatics'
    _iid_ = Guid('{a6f862ce-9cfc-42f1-9185-ff37b75181d3}')
    @winrt_commethod(6)
    def get_CharacteristicAggregateFormat(self) -> Guid: ...
    @winrt_commethod(7)
    def get_CharacteristicExtendedProperties(self) -> Guid: ...
    @winrt_commethod(8)
    def get_CharacteristicPresentationFormat(self) -> Guid: ...
    @winrt_commethod(9)
    def get_CharacteristicUserDescription(self) -> Guid: ...
    @winrt_commethod(10)
    def get_ClientCharacteristicConfiguration(self) -> Guid: ...
    @winrt_commethod(11)
    def get_ServerCharacteristicConfiguration(self) -> Guid: ...
    CharacteristicAggregateFormat = property(get_CharacteristicAggregateFormat, None)
    CharacteristicExtendedProperties = property(get_CharacteristicExtendedProperties, None)
    CharacteristicPresentationFormat = property(get_CharacteristicPresentationFormat, None)
    CharacteristicUserDescription = property(get_CharacteristicUserDescription, None)
    ClientCharacteristicConfiguration = property(get_ClientCharacteristicConfiguration, None)
    ServerCharacteristicConfiguration = property(get_ServerCharacteristicConfiguration, None)
class IGattDescriptorsResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorsResult'
    _iid_ = Guid('{9bc091f3-95e7-4489-8d25-ff81955a57b9}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_commethod(7)
    def get_ProtocolError(self) -> win32more.Windows.Foundation.IReference[Byte]: ...
    @winrt_commethod(8)
    def get_Descriptors(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptor]: ...
    Descriptors = property(get_Descriptors, None)
    ProtocolError = property(get_ProtocolError, None)
    Status = property(get_Status, None)
class IGattDeviceService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService'
    _iid_ = Guid('{ac7b7c05-b33c-47cf-990f-6b8f5577df71}')
    @winrt_commethod(6)
    def GetCharacteristics(self, characteristicUuid: Guid) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic]: ...
    @winrt_commethod(7)
    def GetIncludedServices(self, serviceUuid: Guid) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_commethod(8)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Uuid(self) -> Guid: ...
    @winrt_commethod(10)
    def get_AttributeHandle(self) -> UInt16: ...
    AttributeHandle = property(get_AttributeHandle, None)
    DeviceId = property(get_DeviceId, None)
    Uuid = property(get_Uuid, None)
class IGattDeviceService2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService2'
    _iid_ = Guid('{fc54520b-0b0d-4708-bae0-9ffd9489bc59}')
    @winrt_commethod(6)
    def get_Device(self) -> win32more.Windows.Devices.Bluetooth.BluetoothLEDevice: ...
    @winrt_commethod(7)
    def get_ParentServices(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_commethod(8)
    def GetAllCharacteristics(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic]: ...
    @winrt_commethod(9)
    def GetAllIncludedServices(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    Device = property(get_Device, None)
    ParentServices = property(get_ParentServices, None)
class IGattDeviceService3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3'
    _iid_ = Guid('{b293a950-0c53-437c-a9b3-5c3210c6e569}')
    @winrt_commethod(6)
    def get_DeviceAccessInformation(self) -> win32more.Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_commethod(7)
    def get_Session(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession: ...
    @winrt_commethod(8)
    def get_SharingMode(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSharingMode: ...
    @winrt_commethod(9)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceAccessStatus]: ...
    @winrt_commethod(10)
    def OpenAsync(self, sharingMode: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSharingMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattOpenStatus]: ...
    @winrt_commethod(11)
    def GetCharacteristicsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicsResult]: ...
    @winrt_commethod(12)
    def GetCharacteristicsWithCacheModeAsync(self, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicsResult]: ...
    @winrt_commethod(13)
    def GetCharacteristicsForUuidAsync(self, characteristicUuid: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicsResult]: ...
    @winrt_commethod(14)
    def GetCharacteristicsForUuidWithCacheModeAsync(self, characteristicUuid: Guid, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicsResult]: ...
    @winrt_commethod(15)
    def GetIncludedServicesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_commethod(16)
    def GetIncludedServicesWithCacheModeAsync(self, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_commethod(17)
    def GetIncludedServicesForUuidAsync(self, serviceUuid: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_commethod(18)
    def GetIncludedServicesForUuidWithCacheModeAsync(self, serviceUuid: Guid, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    DeviceAccessInformation = property(get_DeviceAccessInformation, None)
    Session = property(get_Session, None)
    SharingMode = property(get_SharingMode, None)
class IGattDeviceServiceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics'
    _iid_ = Guid('{196d0022-faad-45dc-ae5b-2ac3184e84db}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_commethod(7)
    def GetDeviceSelectorFromUuid(self, serviceUuid: Guid) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetDeviceSelectorFromShortId(self, serviceShortId: UInt16) -> WinRT_String: ...
    @winrt_commethod(9)
    def ConvertShortIdToUuid(self, shortId: UInt16) -> Guid: ...
class IGattDeviceServiceStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics2'
    _iid_ = Guid('{0604186e-24a6-4b0d-a2f2-30cc01545d25}')
    @winrt_commethod(6)
    def FromIdWithSharingModeAsync(self, deviceId: WinRT_String, sharingMode: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSharingMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_commethod(7)
    def GetDeviceSelectorForBluetoothDeviceId(self, bluetoothDeviceId: win32more.Windows.Devices.Bluetooth.BluetoothDeviceId) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetDeviceSelectorForBluetoothDeviceIdWithCacheMode(self, bluetoothDeviceId: win32more.Windows.Devices.Bluetooth.BluetoothDeviceId, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetDeviceSelectorForBluetoothDeviceIdAndUuid(self, bluetoothDeviceId: win32more.Windows.Devices.Bluetooth.BluetoothDeviceId, serviceUuid: Guid) -> WinRT_String: ...
    @winrt_commethod(10)
    def GetDeviceSelectorForBluetoothDeviceIdAndUuidWithCacheMode(self, bluetoothDeviceId: win32more.Windows.Devices.Bluetooth.BluetoothDeviceId, serviceUuid: Guid, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> WinRT_String: ...
class IGattDeviceServicesResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServicesResult'
    _iid_ = Guid('{171dd3ee-016d-419d-838a-576cf475a3d8}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_commethod(7)
    def get_ProtocolError(self) -> win32more.Windows.Foundation.IReference[Byte]: ...
    @winrt_commethod(8)
    def get_Services(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    ProtocolError = property(get_ProtocolError, None)
    Services = property(get_Services, None)
    Status = property(get_Status, None)
class IGattLocalCharacteristic(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic'
    _iid_ = Guid('{aede376d-5412-4d74-92a8-8deb8526829c}')
    @winrt_commethod(6)
    def get_Uuid(self) -> Guid: ...
    @winrt_commethod(7)
    def get_StaticValue(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def get_CharacteristicProperties(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties: ...
    @winrt_commethod(9)
    def get_ReadProtectionLevel(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_commethod(10)
    def get_WriteProtectionLevel(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_commethod(11)
    def CreateDescriptorAsync(self, descriptorUuid: Guid, parameters: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptorParameters) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptorResult]: ...
    @winrt_commethod(12)
    def get_Descriptors(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptor]: ...
    @winrt_commethod(13)
    def get_UserDescription(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_PresentationFormats(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormat]: ...
    @winrt_commethod(15)
    def get_SubscribedClients(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSubscribedClient]: ...
    @winrt_commethod(16)
    def add_SubscribedClientsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_SubscribedClientsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_ReadRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic, win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_ReadRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_WriteRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic, win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_WriteRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def NotifyValueAsync(self, value: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientNotificationResult]]: ...
    @winrt_commethod(23)
    def NotifyValueForSubscribedClientAsync(self, value: win32more.Windows.Storage.Streams.IBuffer, subscribedClient: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSubscribedClient) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientNotificationResult]: ...
    CharacteristicProperties = property(get_CharacteristicProperties, None)
    Descriptors = property(get_Descriptors, None)
    PresentationFormats = property(get_PresentationFormats, None)
    ReadProtectionLevel = property(get_ReadProtectionLevel, None)
    StaticValue = property(get_StaticValue, None)
    SubscribedClients = property(get_SubscribedClients, None)
    UserDescription = property(get_UserDescription, None)
    Uuid = property(get_Uuid, None)
    WriteProtectionLevel = property(get_WriteProtectionLevel, None)
    SubscribedClientsChanged = event()
    ReadRequested = event()
    WriteRequested = event()
class IGattLocalCharacteristicParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters'
    _iid_ = Guid('{faf73db4-4cff-44c7-8445-040e6ead0063}')
    @winrt_commethod(6)
    def put_StaticValue(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(7)
    def get_StaticValue(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def put_CharacteristicProperties(self, value: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties) -> Void: ...
    @winrt_commethod(9)
    def get_CharacteristicProperties(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties: ...
    @winrt_commethod(10)
    def put_ReadProtectionLevel(self, value: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_commethod(11)
    def get_ReadProtectionLevel(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_commethod(12)
    def put_WriteProtectionLevel(self, value: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_commethod(13)
    def get_WriteProtectionLevel(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_commethod(14)
    def put_UserDescription(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_UserDescription(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_PresentationFormats(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormat]: ...
    CharacteristicProperties = property(get_CharacteristicProperties, put_CharacteristicProperties)
    PresentationFormats = property(get_PresentationFormats, None)
    ReadProtectionLevel = property(get_ReadProtectionLevel, put_ReadProtectionLevel)
    StaticValue = property(get_StaticValue, put_StaticValue)
    UserDescription = property(get_UserDescription, put_UserDescription)
    WriteProtectionLevel = property(get_WriteProtectionLevel, put_WriteProtectionLevel)
class IGattLocalCharacteristicResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicResult'
    _iid_ = Guid('{7975de9b-0170-4397-9666-92f863f12ee6}')
    @winrt_commethod(6)
    def get_Characteristic(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic: ...
    @winrt_commethod(7)
    def get_Error(self) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    Characteristic = property(get_Characteristic, None)
    Error = property(get_Error, None)
class IGattLocalDescriptor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptor'
    _iid_ = Guid('{f48ebe06-789d-4a4b-8652-bd017b5d2fc6}')
    @winrt_commethod(6)
    def get_Uuid(self) -> Guid: ...
    @winrt_commethod(7)
    def get_StaticValue(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def get_ReadProtectionLevel(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_commethod(9)
    def get_WriteProtectionLevel(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_commethod(10)
    def add_ReadRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptor, win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ReadRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_WriteRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptor, win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_WriteRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ReadProtectionLevel = property(get_ReadProtectionLevel, None)
    StaticValue = property(get_StaticValue, None)
    Uuid = property(get_Uuid, None)
    WriteProtectionLevel = property(get_WriteProtectionLevel, None)
    ReadRequested = event()
    WriteRequested = event()
class IGattLocalDescriptorParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorParameters'
    _iid_ = Guid('{5fdede6a-f3c1-4b66-8c4b-e3d2293b40e9}')
    @winrt_commethod(6)
    def put_StaticValue(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(7)
    def get_StaticValue(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def put_ReadProtectionLevel(self, value: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_commethod(9)
    def get_ReadProtectionLevel(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_commethod(10)
    def put_WriteProtectionLevel(self, value: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_commethod(11)
    def get_WriteProtectionLevel(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    ReadProtectionLevel = property(get_ReadProtectionLevel, put_ReadProtectionLevel)
    StaticValue = property(get_StaticValue, put_StaticValue)
    WriteProtectionLevel = property(get_WriteProtectionLevel, put_WriteProtectionLevel)
class IGattLocalDescriptorResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorResult'
    _iid_ = Guid('{375791be-321f-4366-bfc1-3bc6b82c79f8}')
    @winrt_commethod(6)
    def get_Descriptor(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptor: ...
    @winrt_commethod(7)
    def get_Error(self) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    Descriptor = property(get_Descriptor, None)
    Error = property(get_Error, None)
class IGattLocalService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalService'
    _iid_ = Guid('{f513e258-f7f7-4902-b803-57fcc7d6fe83}')
    @winrt_commethod(6)
    def get_Uuid(self) -> Guid: ...
    @winrt_commethod(7)
    def CreateCharacteristicAsync(self, characteristicUuid: Guid, parameters: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristicParameters) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristicResult]: ...
    @winrt_commethod(8)
    def get_Characteristics(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic]: ...
    Characteristics = property(get_Characteristics, None)
    Uuid = property(get_Uuid, None)
class IGattPresentationFormat(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormat'
    _iid_ = Guid('{196d0021-faad-45dc-ae5b-2ac3184e84db}')
    @winrt_commethod(6)
    def get_FormatType(self) -> Byte: ...
    @winrt_commethod(7)
    def get_Exponent(self) -> Int32: ...
    @winrt_commethod(8)
    def get_Unit(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_Namespace(self) -> Byte: ...
    @winrt_commethod(10)
    def get_Description(self) -> UInt16: ...
    Description = property(get_Description, None)
    Exponent = property(get_Exponent, None)
    FormatType = property(get_FormatType, None)
    Namespace = property(get_Namespace, None)
    Unit = property(get_Unit, None)
class IGattPresentationFormatStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatStatics'
    _iid_ = Guid('{196d0020-faad-45dc-ae5b-2ac3184e84db}')
    @winrt_commethod(6)
    def get_BluetoothSigAssignedNumbers(self) -> Byte: ...
    BluetoothSigAssignedNumbers = property(get_BluetoothSigAssignedNumbers, None)
class IGattPresentationFormatStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatStatics2'
    _iid_ = Guid('{a9c21713-b82f-435e-b634-21fd85a43c07}')
    @winrt_commethod(6)
    def FromParts(self, formatType: Byte, exponent: Int32, unit: UInt16, namespaceId: Byte, description: UInt16) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormat: ...
class IGattPresentationFormatTypesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics'
    _iid_ = Guid('{faf1ba0a-30ba-409c-bef7-cffb6d03b8fb}')
    @winrt_commethod(6)
    def get_Boolean(self) -> Byte: ...
    @winrt_commethod(7)
    def get_Bit2(self) -> Byte: ...
    @winrt_commethod(8)
    def get_Nibble(self) -> Byte: ...
    @winrt_commethod(9)
    def get_UInt8(self) -> Byte: ...
    @winrt_commethod(10)
    def get_UInt12(self) -> Byte: ...
    @winrt_commethod(11)
    def get_UInt16(self) -> Byte: ...
    @winrt_commethod(12)
    def get_UInt24(self) -> Byte: ...
    @winrt_commethod(13)
    def get_UInt32(self) -> Byte: ...
    @winrt_commethod(14)
    def get_UInt48(self) -> Byte: ...
    @winrt_commethod(15)
    def get_UInt64(self) -> Byte: ...
    @winrt_commethod(16)
    def get_UInt128(self) -> Byte: ...
    @winrt_commethod(17)
    def get_SInt8(self) -> Byte: ...
    @winrt_commethod(18)
    def get_SInt12(self) -> Byte: ...
    @winrt_commethod(19)
    def get_SInt16(self) -> Byte: ...
    @winrt_commethod(20)
    def get_SInt24(self) -> Byte: ...
    @winrt_commethod(21)
    def get_SInt32(self) -> Byte: ...
    @winrt_commethod(22)
    def get_SInt48(self) -> Byte: ...
    @winrt_commethod(23)
    def get_SInt64(self) -> Byte: ...
    @winrt_commethod(24)
    def get_SInt128(self) -> Byte: ...
    @winrt_commethod(25)
    def get_Float32(self) -> Byte: ...
    @winrt_commethod(26)
    def get_Float64(self) -> Byte: ...
    @winrt_commethod(27)
    def get_SFloat(self) -> Byte: ...
    @winrt_commethod(28)
    def get_Float(self) -> Byte: ...
    @winrt_commethod(29)
    def get_DUInt16(self) -> Byte: ...
    @winrt_commethod(30)
    def get_Utf8(self) -> Byte: ...
    @winrt_commethod(31)
    def get_Utf16(self) -> Byte: ...
    @winrt_commethod(32)
    def get_Struct(self) -> Byte: ...
    Bit2 = property(get_Bit2, None)
    Boolean = property(get_Boolean, None)
    DUInt16 = property(get_DUInt16, None)
    Float = property(get_Float, None)
    Float32 = property(get_Float32, None)
    Float64 = property(get_Float64, None)
    Nibble = property(get_Nibble, None)
    SFloat = property(get_SFloat, None)
    SInt12 = property(get_SInt12, None)
    SInt128 = property(get_SInt128, None)
    SInt16 = property(get_SInt16, None)
    SInt24 = property(get_SInt24, None)
    SInt32 = property(get_SInt32, None)
    SInt48 = property(get_SInt48, None)
    SInt64 = property(get_SInt64, None)
    SInt8 = property(get_SInt8, None)
    Struct = property(get_Struct, None)
    UInt12 = property(get_UInt12, None)
    UInt128 = property(get_UInt128, None)
    UInt16 = property(get_UInt16, None)
    UInt24 = property(get_UInt24, None)
    UInt32 = property(get_UInt32, None)
    UInt48 = property(get_UInt48, None)
    UInt64 = property(get_UInt64, None)
    UInt8 = property(get_UInt8, None)
    Utf16 = property(get_Utf16, None)
    Utf8 = property(get_Utf8, None)
class IGattProtocolErrorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics'
    _iid_ = Guid('{ca46c5c5-0ecc-4809-bea3-cf79bc991e37}')
    @winrt_commethod(6)
    def get_InvalidHandle(self) -> Byte: ...
    @winrt_commethod(7)
    def get_ReadNotPermitted(self) -> Byte: ...
    @winrt_commethod(8)
    def get_WriteNotPermitted(self) -> Byte: ...
    @winrt_commethod(9)
    def get_InvalidPdu(self) -> Byte: ...
    @winrt_commethod(10)
    def get_InsufficientAuthentication(self) -> Byte: ...
    @winrt_commethod(11)
    def get_RequestNotSupported(self) -> Byte: ...
    @winrt_commethod(12)
    def get_InvalidOffset(self) -> Byte: ...
    @winrt_commethod(13)
    def get_InsufficientAuthorization(self) -> Byte: ...
    @winrt_commethod(14)
    def get_PrepareQueueFull(self) -> Byte: ...
    @winrt_commethod(15)
    def get_AttributeNotFound(self) -> Byte: ...
    @winrt_commethod(16)
    def get_AttributeNotLong(self) -> Byte: ...
    @winrt_commethod(17)
    def get_InsufficientEncryptionKeySize(self) -> Byte: ...
    @winrt_commethod(18)
    def get_InvalidAttributeValueLength(self) -> Byte: ...
    @winrt_commethod(19)
    def get_UnlikelyError(self) -> Byte: ...
    @winrt_commethod(20)
    def get_InsufficientEncryption(self) -> Byte: ...
    @winrt_commethod(21)
    def get_UnsupportedGroupType(self) -> Byte: ...
    @winrt_commethod(22)
    def get_InsufficientResources(self) -> Byte: ...
    AttributeNotFound = property(get_AttributeNotFound, None)
    AttributeNotLong = property(get_AttributeNotLong, None)
    InsufficientAuthentication = property(get_InsufficientAuthentication, None)
    InsufficientAuthorization = property(get_InsufficientAuthorization, None)
    InsufficientEncryption = property(get_InsufficientEncryption, None)
    InsufficientEncryptionKeySize = property(get_InsufficientEncryptionKeySize, None)
    InsufficientResources = property(get_InsufficientResources, None)
    InvalidAttributeValueLength = property(get_InvalidAttributeValueLength, None)
    InvalidHandle = property(get_InvalidHandle, None)
    InvalidOffset = property(get_InvalidOffset, None)
    InvalidPdu = property(get_InvalidPdu, None)
    PrepareQueueFull = property(get_PrepareQueueFull, None)
    ReadNotPermitted = property(get_ReadNotPermitted, None)
    RequestNotSupported = property(get_RequestNotSupported, None)
    UnlikelyError = property(get_UnlikelyError, None)
    UnsupportedGroupType = property(get_UnsupportedGroupType, None)
    WriteNotPermitted = property(get_WriteNotPermitted, None)
class IGattReadClientCharacteristicConfigurationDescriptorResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadClientCharacteristicConfigurationDescriptorResult'
    _iid_ = Guid('{63a66f09-1aea-4c4c-a50f-97bae474b348}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_commethod(7)
    def get_ClientCharacteristicConfigurationDescriptor(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientCharacteristicConfigurationDescriptorValue: ...
    ClientCharacteristicConfigurationDescriptor = property(get_ClientCharacteristicConfigurationDescriptor, None)
    Status = property(get_Status, None)
class IGattReadClientCharacteristicConfigurationDescriptorResult2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadClientCharacteristicConfigurationDescriptorResult2'
    _iid_ = Guid('{1bf1a59d-ba4d-4622-8651-f4ee150d0a5d}')
    @winrt_commethod(6)
    def get_ProtocolError(self) -> win32more.Windows.Foundation.IReference[Byte]: ...
    ProtocolError = property(get_ProtocolError, None)
class IGattReadRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequest'
    _iid_ = Guid('{f1dd6535-6acd-42a6-a4bb-d789dae0043e}')
    @winrt_commethod(6)
    def get_Offset(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Length(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_State(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestState: ...
    @winrt_commethod(9)
    def add_StateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequest, win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_StateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def RespondWithValue(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(12)
    def RespondWithProtocolError(self, protocolError: Byte) -> Void: ...
    Length = property(get_Length, None)
    Offset = property(get_Offset, None)
    State = property(get_State, None)
    StateChanged = event()
class IGattReadRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequestedEventArgs'
    _iid_ = Guid('{93497243-f39c-484b-8ab6-996ba486cfa3}')
    @winrt_commethod(6)
    def get_Session(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_commethod(8)
    def GetRequestAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequest]: ...
    Session = property(get_Session, None)
class IGattReadResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadResult'
    _iid_ = Guid('{63a66f08-1aea-4c4c-a50f-97bae474b348}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_commethod(7)
    def get_Value(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class IGattReadResult2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadResult2'
    _iid_ = Guid('{a10f50a0-fb43-48af-baaa-638a5c6329fe}')
    @winrt_commethod(6)
    def get_ProtocolError(self) -> win32more.Windows.Foundation.IReference[Byte]: ...
    ProtocolError = property(get_ProtocolError, None)
class IGattReliableWriteTransaction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReliableWriteTransaction'
    _iid_ = Guid('{63a66f07-1aea-4c4c-a50f-97bae474b348}')
    @winrt_commethod(6)
    def WriteValue(self, characteristic: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(7)
    def CommitAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
class IGattReliableWriteTransaction2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReliableWriteTransaction2'
    _iid_ = Guid('{51113987-ef12-462f-9fb2-a1a43a679416}')
    @winrt_commethod(6)
    def CommitWithResultAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
class IGattRequestStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattRequestStateChangedEventArgs'
    _iid_ = Guid('{e834d92c-27be-44b3-9d0d-4fc6e808dd3f}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestState: ...
    @winrt_commethod(7)
    def get_Error(self) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    Error = property(get_Error, None)
    State = property(get_State, None)
class IGattServiceProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProvider'
    _iid_ = Guid('{7822b3cd-2889-4f86-a051-3f0aed1c2760}')
    @winrt_commethod(6)
    def get_Service(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalService: ...
    @winrt_commethod(7)
    def get_AdvertisementStatus(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisementStatus: ...
    @winrt_commethod(8)
    def add_AdvertisementStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProvider, win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisementStatusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_AdvertisementStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def StartAdvertising(self) -> Void: ...
    @winrt_commethod(11)
    def StartAdvertisingWithParameters(self, parameters: win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisingParameters) -> Void: ...
    @winrt_commethod(12)
    def StopAdvertising(self) -> Void: ...
    AdvertisementStatus = property(get_AdvertisementStatus, None)
    Service = property(get_Service, None)
    AdvertisementStatusChanged = event()
class IGattServiceProviderAdvertisementStatusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisementStatusChangedEventArgs'
    _iid_ = Guid('{59a5aa65-fa21-4ffc-b155-04d928012686}')
    @winrt_commethod(6)
    def get_Error(self) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisementStatus: ...
    Error = property(get_Error, None)
    Status = property(get_Status, None)
class IGattServiceProviderAdvertisingParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisingParameters'
    _iid_ = Guid('{e2ce31ab-6315-4c22-9bd7-781dbc3d8d82}')
    @winrt_commethod(6)
    def put_IsConnectable(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_IsConnectable(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_IsDiscoverable(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_IsDiscoverable(self) -> Boolean: ...
    IsConnectable = property(get_IsConnectable, put_IsConnectable)
    IsDiscoverable = property(get_IsDiscoverable, put_IsDiscoverable)
class IGattServiceProviderAdvertisingParameters2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisingParameters2'
    _iid_ = Guid('{ff68468d-ca92-4434-9743-0e90988ad879}')
    @winrt_commethod(6)
    def put_ServiceData(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(7)
    def get_ServiceData(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    ServiceData = property(get_ServiceData, put_ServiceData)
class IGattServiceProviderResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderResult'
    _iid_ = Guid('{764696d8-c53e-428c-8a48-67afe02c3ae6}')
    @winrt_commethod(6)
    def get_Error(self) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_commethod(7)
    def get_ServiceProvider(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProvider: ...
    Error = property(get_Error, None)
    ServiceProvider = property(get_ServiceProvider, None)
class IGattServiceProviderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderStatics'
    _iid_ = Guid('{31794063-5256-4054-a4f4-7bbe7755a57e}')
    @winrt_commethod(6)
    def CreateAsync(self, serviceUuid: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderResult]: ...
class IGattServiceUuidsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics'
    _iid_ = Guid('{6dc57058-9aba-4417-b8f2-dce016d34ee2}')
    @winrt_commethod(6)
    def get_Battery(self) -> Guid: ...
    @winrt_commethod(7)
    def get_BloodPressure(self) -> Guid: ...
    @winrt_commethod(8)
    def get_CyclingSpeedAndCadence(self) -> Guid: ...
    @winrt_commethod(9)
    def get_GenericAccess(self) -> Guid: ...
    @winrt_commethod(10)
    def get_GenericAttribute(self) -> Guid: ...
    @winrt_commethod(11)
    def get_Glucose(self) -> Guid: ...
    @winrt_commethod(12)
    def get_HealthThermometer(self) -> Guid: ...
    @winrt_commethod(13)
    def get_HeartRate(self) -> Guid: ...
    @winrt_commethod(14)
    def get_RunningSpeedAndCadence(self) -> Guid: ...
    Battery = property(get_Battery, None)
    BloodPressure = property(get_BloodPressure, None)
    CyclingSpeedAndCadence = property(get_CyclingSpeedAndCadence, None)
    GenericAccess = property(get_GenericAccess, None)
    GenericAttribute = property(get_GenericAttribute, None)
    Glucose = property(get_Glucose, None)
    HealthThermometer = property(get_HealthThermometer, None)
    HeartRate = property(get_HeartRate, None)
    RunningSpeedAndCadence = property(get_RunningSpeedAndCadence, None)
class IGattServiceUuidsStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2'
    _iid_ = Guid('{d2ae94f5-3d15-4f79-9c0c-eaafa675155c}')
    @winrt_commethod(6)
    def get_AlertNotification(self) -> Guid: ...
    @winrt_commethod(7)
    def get_CurrentTime(self) -> Guid: ...
    @winrt_commethod(8)
    def get_CyclingPower(self) -> Guid: ...
    @winrt_commethod(9)
    def get_DeviceInformation(self) -> Guid: ...
    @winrt_commethod(10)
    def get_HumanInterfaceDevice(self) -> Guid: ...
    @winrt_commethod(11)
    def get_ImmediateAlert(self) -> Guid: ...
    @winrt_commethod(12)
    def get_LinkLoss(self) -> Guid: ...
    @winrt_commethod(13)
    def get_LocationAndNavigation(self) -> Guid: ...
    @winrt_commethod(14)
    def get_NextDstChange(self) -> Guid: ...
    @winrt_commethod(15)
    def get_PhoneAlertStatus(self) -> Guid: ...
    @winrt_commethod(16)
    def get_ReferenceTimeUpdate(self) -> Guid: ...
    @winrt_commethod(17)
    def get_ScanParameters(self) -> Guid: ...
    @winrt_commethod(18)
    def get_TxPower(self) -> Guid: ...
    AlertNotification = property(get_AlertNotification, None)
    CurrentTime = property(get_CurrentTime, None)
    CyclingPower = property(get_CyclingPower, None)
    DeviceInformation = property(get_DeviceInformation, None)
    HumanInterfaceDevice = property(get_HumanInterfaceDevice, None)
    ImmediateAlert = property(get_ImmediateAlert, None)
    LinkLoss = property(get_LinkLoss, None)
    LocationAndNavigation = property(get_LocationAndNavigation, None)
    NextDstChange = property(get_NextDstChange, None)
    PhoneAlertStatus = property(get_PhoneAlertStatus, None)
    ReferenceTimeUpdate = property(get_ReferenceTimeUpdate, None)
    ScanParameters = property(get_ScanParameters, None)
    TxPower = property(get_TxPower, None)
class IGattSession(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession'
    _iid_ = Guid('{d23b5143-e04e-4c24-999c-9c256f9856b1}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> win32more.Windows.Devices.Bluetooth.BluetoothDeviceId: ...
    @winrt_commethod(7)
    def get_CanMaintainConnection(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_MaintainConnection(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_MaintainConnection(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_MaxPduSize(self) -> UInt16: ...
    @winrt_commethod(11)
    def get_SessionStatus(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSessionStatus: ...
    @winrt_commethod(12)
    def add_MaxPduSizeChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_MaxPduSizeChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_SessionStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession, win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSessionStatusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_SessionStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CanMaintainConnection = property(get_CanMaintainConnection, None)
    DeviceId = property(get_DeviceId, None)
    MaintainConnection = property(get_MaintainConnection, put_MaintainConnection)
    MaxPduSize = property(get_MaxPduSize, None)
    SessionStatus = property(get_SessionStatus, None)
    MaxPduSizeChanged = event()
    SessionStatusChanged = event()
class IGattSessionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSessionStatics'
    _iid_ = Guid('{2e65b95c-539f-4db7-82a8-73bdbbf73ebf}')
    @winrt_commethod(6)
    def FromDeviceIdAsync(self, deviceId: win32more.Windows.Devices.Bluetooth.BluetoothDeviceId) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession]: ...
class IGattSessionStatusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSessionStatusChangedEventArgs'
    _iid_ = Guid('{7605b72e-837f-404c-ab34-3163f39ddf32}')
    @winrt_commethod(6)
    def get_Error(self) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSessionStatus: ...
    Error = property(get_Error, None)
    Status = property(get_Status, None)
class IGattSubscribedClient(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSubscribedClient'
    _iid_ = Guid('{736e9001-15a4-4ec2-9248-e3f20d463be9}')
    @winrt_commethod(6)
    def get_Session(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession: ...
    @winrt_commethod(7)
    def get_MaxNotificationSize(self) -> UInt16: ...
    @winrt_commethod(8)
    def add_MaxNotificationSizeChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSubscribedClient, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_MaxNotificationSizeChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    MaxNotificationSize = property(get_MaxNotificationSize, None)
    Session = property(get_Session, None)
    MaxNotificationSizeChanged = event()
class IGattValueChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattValueChangedEventArgs'
    _iid_ = Guid('{d21bdb54-06e3-4ed8-a263-acfac8ba7313}')
    @winrt_commethod(6)
    def get_CharacteristicValue(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    CharacteristicValue = property(get_CharacteristicValue, None)
    Timestamp = property(get_Timestamp, None)
class IGattWriteRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequest'
    _iid_ = Guid('{aeb6a9ed-de2f-4fc2-a9a8-94ea7844f13d}')
    @winrt_commethod(6)
    def get_Value(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_Offset(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Option(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteOption: ...
    @winrt_commethod(9)
    def get_State(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestState: ...
    @winrt_commethod(10)
    def add_StateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequest, win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_StateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def Respond(self) -> Void: ...
    @winrt_commethod(13)
    def RespondWithProtocolError(self, protocolError: Byte) -> Void: ...
    Offset = property(get_Offset, None)
    Option = property(get_Option, None)
    State = property(get_State, None)
    Value = property(get_Value, None)
    StateChanged = event()
class IGattWriteRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequestedEventArgs'
    _iid_ = Guid('{2dec8bbe-a73a-471a-94d5-037deadd0806}')
    @winrt_commethod(6)
    def get_Session(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_commethod(8)
    def GetRequestAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequest]: ...
    Session = property(get_Session, None)
class IGattWriteResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteResult'
    _iid_ = Guid('{4991ddb1-cb2b-44f7-99fc-d29a2871dc9b}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_commethod(7)
    def get_ProtocolError(self) -> win32more.Windows.Foundation.IReference[Byte]: ...
    ProtocolError = property(get_ProtocolError, None)
    Status = property(get_Status, None)


make_ready(__name__)
