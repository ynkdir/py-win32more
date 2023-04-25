from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.System.WinRT
import Windows.Devices.Bluetooth
import Windows.Devices.Bluetooth.GenericAttributeProfile
import Windows.Devices.Enumeration
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class GattCharacteristic(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic'
    @winrt_mixinmethod
    def GetDescriptors(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic, descriptorUuid: Guid) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptor]: ...
    @winrt_mixinmethod
    def get_CharacteristicProperties(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties: ...
    @winrt_mixinmethod
    def get_ProtectionLevel(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_mixinmethod
    def put_ProtectionLevel(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic, value: Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_mixinmethod
    def get_UserDescription(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Uuid(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic) -> Guid: ...
    @winrt_mixinmethod
    def get_AttributeHandle(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic) -> UInt16: ...
    @winrt_mixinmethod
    def get_PresentationFormats(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormat]: ...
    @winrt_mixinmethod
    def ReadValueAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadResult]: ...
    @winrt_mixinmethod
    def ReadValueWithCacheModeAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadResult]: ...
    @winrt_mixinmethod
    def WriteValueAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic, value: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
    @winrt_mixinmethod
    def WriteValueWithOptionAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic, value: Windows.Storage.Streams.IBuffer, writeOption: Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteOption) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
    @winrt_mixinmethod
    def ReadClientCharacteristicConfigurationDescriptorAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadClientCharacteristicConfigurationDescriptorResult]: ...
    @winrt_mixinmethod
    def WriteClientCharacteristicConfigurationDescriptorAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic, clientCharacteristicConfigurationDescriptorValue: Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientCharacteristicConfigurationDescriptorValue) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
    @winrt_mixinmethod
    def add_ValueChanged(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic, valueChangedHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic, Windows.Devices.Bluetooth.GenericAttributeProfile.GattValueChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ValueChanged(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic, valueChangedEventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Service(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic2) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService: ...
    @winrt_mixinmethod
    def GetAllDescriptors(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic2) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptor]: ...
    @winrt_mixinmethod
    def GetDescriptorsAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic3) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorsResult]: ...
    @winrt_mixinmethod
    def GetDescriptorsWithCacheModeAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic3, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorsResult]: ...
    @winrt_mixinmethod
    def GetDescriptorsForUuidAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic3, descriptorUuid: Guid) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorsResult]: ...
    @winrt_mixinmethod
    def GetDescriptorsForUuidWithCacheModeAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic3, descriptorUuid: Guid, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorsResult]: ...
    @winrt_mixinmethod
    def WriteValueWithResultAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic3, value: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
    @winrt_mixinmethod
    def WriteValueWithResultAndOptionAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic3, value: Windows.Storage.Streams.IBuffer, writeOption: Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteOption) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
    @winrt_mixinmethod
    def WriteClientCharacteristicConfigurationDescriptorWithResultAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristic3, clientCharacteristicConfigurationDescriptorValue: Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientCharacteristicConfigurationDescriptorValue) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
    @winrt_classmethod
    def ConvertShortIdToUuid(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicStatics, shortId: UInt16) -> Guid: ...
    CharacteristicProperties = property(get_CharacteristicProperties, None)
    ProtectionLevel = property(get_ProtectionLevel, put_ProtectionLevel)
    UserDescription = property(get_UserDescription, None)
    Uuid = property(get_Uuid, None)
    AttributeHandle = property(get_AttributeHandle, None)
    PresentationFormats = property(get_PresentationFormats, None)
    Service = property(get_Service, None)
GattCharacteristicProperties = UInt32
GattCharacteristicProperties_None: GattCharacteristicProperties = 0
GattCharacteristicProperties_Broadcast: GattCharacteristicProperties = 1
GattCharacteristicProperties_Read: GattCharacteristicProperties = 2
GattCharacteristicProperties_WriteWithoutResponse: GattCharacteristicProperties = 4
GattCharacteristicProperties_Write: GattCharacteristicProperties = 8
GattCharacteristicProperties_Notify: GattCharacteristicProperties = 16
GattCharacteristicProperties_Indicate: GattCharacteristicProperties = 32
GattCharacteristicProperties_AuthenticatedSignedWrites: GattCharacteristicProperties = 64
GattCharacteristicProperties_ExtendedProperties: GattCharacteristicProperties = 128
GattCharacteristicProperties_ReliableWrites: GattCharacteristicProperties = 256
GattCharacteristicProperties_WritableAuxiliaries: GattCharacteristicProperties = 512
class GattCharacteristicUuids(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicUuids'
    @winrt_classmethod
    def get_AlertCategoryId(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_AlertCategoryIdBitMask(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_AlertLevel(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_AlertNotificationControlPoint(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_AlertStatus(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_GapAppearance(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_BootKeyboardInputReport(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_BootKeyboardOutputReport(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_BootMouseInputReport(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_CurrentTime(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_CyclingPowerControlPoint(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_CyclingPowerFeature(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_CyclingPowerMeasurement(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_CyclingPowerVector(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_DateTime(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_DayDateTime(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_DayOfWeek(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_GapDeviceName(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_DstOffset(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ExactTime256(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_FirmwareRevisionString(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_HardwareRevisionString(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_HidControlPoint(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_HidInformation(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_Ieee1107320601RegulatoryCertificationDataList(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_LnControlPoint(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_LnFeature(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_LocalTimeInformation(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_LocationAndSpeed(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ManufacturerNameString(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ModelNumberString(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_Navigation(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_NewAlert(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_GapPeripheralPreferredConnectionParameters(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_GapPeripheralPrivacyFlag(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_PnpId(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_PositionQuality(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ProtocolMode(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_GapReconnectionAddress(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ReferenceTimeInformation(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_Report(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ReportMap(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_RingerControlPoint(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_RingerSetting(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ScanIntervalWindow(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ScanRefresh(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_SerialNumberString(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_GattServiceChanged(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_SoftwareRevisionString(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_SupportedNewAlertCategory(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_SupportUnreadAlertCategory(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_SystemId(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_TimeAccuracy(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_TimeSource(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_TimeUpdateControlPoint(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_TimeUpdateState(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_TimeWithDst(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_TimeZone(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_TxPowerLevel(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_UnreadAlertStatus(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_BatteryLevel(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_BloodPressureFeature(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_BloodPressureMeasurement(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_BodySensorLocation(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_CscFeature(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_CscMeasurement(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_GlucoseFeature(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_GlucoseMeasurement(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_GlucoseMeasurementContext(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_HeartRateControlPoint(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_HeartRateMeasurement(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_IntermediateCuffPressure(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_IntermediateTemperature(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_MeasurementInterval(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_RecordAccessControlPoint(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_RscFeature(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_RscMeasurement(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_SCControlPoint(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_SensorLocation(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_TemperatureMeasurement(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_TemperatureType(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicUuidsStatics) -> Guid: ...
    AlertCategoryId = property(get_AlertCategoryId, None)
    AlertCategoryIdBitMask = property(get_AlertCategoryIdBitMask, None)
    AlertLevel = property(get_AlertLevel, None)
    AlertNotificationControlPoint = property(get_AlertNotificationControlPoint, None)
    AlertStatus = property(get_AlertStatus, None)
    GapAppearance = property(get_GapAppearance, None)
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
    GapDeviceName = property(get_GapDeviceName, None)
    DstOffset = property(get_DstOffset, None)
    ExactTime256 = property(get_ExactTime256, None)
    FirmwareRevisionString = property(get_FirmwareRevisionString, None)
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
    GapPeripheralPreferredConnectionParameters = property(get_GapPeripheralPreferredConnectionParameters, None)
    GapPeripheralPrivacyFlag = property(get_GapPeripheralPrivacyFlag, None)
    PnpId = property(get_PnpId, None)
    PositionQuality = property(get_PositionQuality, None)
    ProtocolMode = property(get_ProtocolMode, None)
    GapReconnectionAddress = property(get_GapReconnectionAddress, None)
    ReferenceTimeInformation = property(get_ReferenceTimeInformation, None)
    Report = property(get_Report, None)
    ReportMap = property(get_ReportMap, None)
    RingerControlPoint = property(get_RingerControlPoint, None)
    RingerSetting = property(get_RingerSetting, None)
    ScanIntervalWindow = property(get_ScanIntervalWindow, None)
    ScanRefresh = property(get_ScanRefresh, None)
    SerialNumberString = property(get_SerialNumberString, None)
    GattServiceChanged = property(get_GattServiceChanged, None)
    SoftwareRevisionString = property(get_SoftwareRevisionString, None)
    SupportedNewAlertCategory = property(get_SupportedNewAlertCategory, None)
    SupportUnreadAlertCategory = property(get_SupportUnreadAlertCategory, None)
    SystemId = property(get_SystemId, None)
    TimeAccuracy = property(get_TimeAccuracy, None)
    TimeSource = property(get_TimeSource, None)
    TimeUpdateControlPoint = property(get_TimeUpdateControlPoint, None)
    TimeUpdateState = property(get_TimeUpdateState, None)
    TimeWithDst = property(get_TimeWithDst, None)
    TimeZone = property(get_TimeZone, None)
    TxPowerLevel = property(get_TxPowerLevel, None)
    UnreadAlertStatus = property(get_UnreadAlertStatus, None)
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
class GattCharacteristicsResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicsResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicsResult) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_mixinmethod
    def get_ProtocolError(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicsResult) -> Windows.Foundation.IReference[Byte]: ...
    @winrt_mixinmethod
    def get_Characteristics(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattCharacteristicsResult) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic]: ...
    Status = property(get_Status, None)
    ProtocolError = property(get_ProtocolError, None)
    Characteristics = property(get_Characteristics, None)
GattClientCharacteristicConfigurationDescriptorValue = Int32
GattClientCharacteristicConfigurationDescriptorValue_None: GattClientCharacteristicConfigurationDescriptorValue = 0
GattClientCharacteristicConfigurationDescriptorValue_Notify: GattClientCharacteristicConfigurationDescriptorValue = 1
GattClientCharacteristicConfigurationDescriptorValue_Indicate: GattClientCharacteristicConfigurationDescriptorValue = 2
class GattClientNotificationResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientNotificationResult'
    @winrt_mixinmethod
    def get_SubscribedClient(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattClientNotificationResult) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattSubscribedClient: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattClientNotificationResult) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_mixinmethod
    def get_ProtocolError(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattClientNotificationResult) -> Windows.Foundation.IReference[Byte]: ...
    @winrt_mixinmethod
    def get_BytesSent(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattClientNotificationResult2) -> UInt16: ...
    SubscribedClient = property(get_SubscribedClient, None)
    Status = property(get_Status, None)
    ProtocolError = property(get_ProtocolError, None)
    BytesSent = property(get_BytesSent, None)
GattCommunicationStatus = Int32
GattCommunicationStatus_Success: GattCommunicationStatus = 0
GattCommunicationStatus_Unreachable: GattCommunicationStatus = 1
GattCommunicationStatus_ProtocolError: GattCommunicationStatus = 2
GattCommunicationStatus_AccessDenied: GattCommunicationStatus = 3
class GattDescriptor(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptor'
    @winrt_mixinmethod
    def get_ProtectionLevel(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_mixinmethod
    def put_ProtectionLevel(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor, value: Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_mixinmethod
    def get_Uuid(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor) -> Guid: ...
    @winrt_mixinmethod
    def get_AttributeHandle(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor) -> UInt16: ...
    @winrt_mixinmethod
    def ReadValueAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadResult]: ...
    @winrt_mixinmethod
    def ReadValueWithCacheModeAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadResult]: ...
    @winrt_mixinmethod
    def WriteValueAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor, value: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
    @winrt_mixinmethod
    def WriteValueWithResultAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptor2, value: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
    @winrt_classmethod
    def ConvertShortIdToUuid(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorStatics, shortId: UInt16) -> Guid: ...
    ProtectionLevel = property(get_ProtectionLevel, put_ProtectionLevel)
    Uuid = property(get_Uuid, None)
    AttributeHandle = property(get_AttributeHandle, None)
class GattDescriptorUuids(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorUuids'
    @winrt_classmethod
    def get_CharacteristicAggregateFormat(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_CharacteristicExtendedProperties(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_CharacteristicPresentationFormat(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_CharacteristicUserDescription(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_ClientCharacteristicConfiguration(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_ServerCharacteristicConfiguration(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorUuidsStatics) -> Guid: ...
    CharacteristicAggregateFormat = property(get_CharacteristicAggregateFormat, None)
    CharacteristicExtendedProperties = property(get_CharacteristicExtendedProperties, None)
    CharacteristicPresentationFormat = property(get_CharacteristicPresentationFormat, None)
    CharacteristicUserDescription = property(get_CharacteristicUserDescription, None)
    ClientCharacteristicConfiguration = property(get_ClientCharacteristicConfiguration, None)
    ServerCharacteristicConfiguration = property(get_ServerCharacteristicConfiguration, None)
class GattDescriptorsResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorsResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorsResult) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_mixinmethod
    def get_ProtocolError(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorsResult) -> Windows.Foundation.IReference[Byte]: ...
    @winrt_mixinmethod
    def get_Descriptors(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDescriptorsResult) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptor]: ...
    Status = property(get_Status, None)
    ProtocolError = property(get_ProtocolError, None)
    Descriptors = property(get_Descriptors, None)
class GattDeviceService(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService'
    @winrt_mixinmethod
    def GetCharacteristics(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService, characteristicUuid: Guid) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic]: ...
    @winrt_mixinmethod
    def GetIncludedServices(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService, serviceUuid: Guid) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Uuid(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService) -> Guid: ...
    @winrt_mixinmethod
    def get_AttributeHandle(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService) -> UInt16: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_Device(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService2) -> Windows.Devices.Bluetooth.BluetoothLEDevice: ...
    @winrt_mixinmethod
    def get_ParentServices(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService2) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_mixinmethod
    def GetAllCharacteristics(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService2) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic]: ...
    @winrt_mixinmethod
    def GetAllIncludedServices(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService2) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_mixinmethod
    def get_DeviceAccessInformation(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3) -> Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_mixinmethod
    def get_Session(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession: ...
    @winrt_mixinmethod
    def get_SharingMode(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattSharingMode: ...
    @winrt_mixinmethod
    def RequestAccessAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceAccessStatus]: ...
    @winrt_mixinmethod
    def OpenAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3, sharingMode: Windows.Devices.Bluetooth.GenericAttributeProfile.GattSharingMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattOpenStatus]: ...
    @winrt_mixinmethod
    def GetCharacteristicsAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicsResult]: ...
    @winrt_mixinmethod
    def GetCharacteristicsWithCacheModeAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicsResult]: ...
    @winrt_mixinmethod
    def GetCharacteristicsForUuidAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3, characteristicUuid: Guid) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicsResult]: ...
    @winrt_mixinmethod
    def GetCharacteristicsForUuidWithCacheModeAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3, characteristicUuid: Guid, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicsResult]: ...
    @winrt_mixinmethod
    def GetIncludedServicesAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_mixinmethod
    def GetIncludedServicesWithCacheModeAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_mixinmethod
    def GetIncludedServicesForUuidAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3, serviceUuid: Guid) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_mixinmethod
    def GetIncludedServicesForUuidWithCacheModeAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceService3, serviceUuid: Guid, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_classmethod
    def FromIdWithSharingModeAsync(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics2, deviceId: WinRT_String, sharingMode: Windows.Devices.Bluetooth.GenericAttributeProfile.GattSharingMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_classmethod
    def GetDeviceSelectorForBluetoothDeviceId(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics2, bluetoothDeviceId: Windows.Devices.Bluetooth.BluetoothDeviceId) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorForBluetoothDeviceIdWithCacheMode(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics2, bluetoothDeviceId: Windows.Devices.Bluetooth.BluetoothDeviceId, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorForBluetoothDeviceIdAndUuid(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics2, bluetoothDeviceId: Windows.Devices.Bluetooth.BluetoothDeviceId, serviceUuid: Guid) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorForBluetoothDeviceIdAndUuidWithCacheMode(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics2, bluetoothDeviceId: Windows.Devices.Bluetooth.BluetoothDeviceId, serviceUuid: Guid, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_classmethod
    def GetDeviceSelectorFromUuid(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics, serviceUuid: Guid) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromShortId(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics, serviceShortId: UInt16) -> WinRT_String: ...
    @winrt_classmethod
    def ConvertShortIdToUuid(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServiceStatics, shortId: UInt16) -> Guid: ...
    DeviceId = property(get_DeviceId, None)
    Uuid = property(get_Uuid, None)
    AttributeHandle = property(get_AttributeHandle, None)
    Device = property(get_Device, None)
    ParentServices = property(get_ParentServices, None)
    DeviceAccessInformation = property(get_DeviceAccessInformation, None)
    Session = property(get_Session, None)
    SharingMode = property(get_SharingMode, None)
class GattDeviceServicesResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServicesResult) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_mixinmethod
    def get_ProtocolError(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServicesResult) -> Windows.Foundation.IReference[Byte]: ...
    @winrt_mixinmethod
    def get_Services(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattDeviceServicesResult) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    Status = property(get_Status, None)
    ProtocolError = property(get_ProtocolError, None)
    Services = property(get_Services, None)
class GattLocalCharacteristic(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic'
    @winrt_mixinmethod
    def get_Uuid(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic) -> Guid: ...
    @winrt_mixinmethod
    def get_StaticValue(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_CharacteristicProperties(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties: ...
    @winrt_mixinmethod
    def get_ReadProtectionLevel(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_mixinmethod
    def get_WriteProtectionLevel(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_mixinmethod
    def CreateDescriptorAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic, descriptorUuid: Guid, parameters: Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptorParameters) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptorResult]: ...
    @winrt_mixinmethod
    def get_Descriptors(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptor]: ...
    @winrt_mixinmethod
    def get_UserDescription(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PresentationFormats(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormat]: ...
    @winrt_mixinmethod
    def get_SubscribedClients(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattSubscribedClient]: ...
    @winrt_mixinmethod
    def add_SubscribedClientsChanged(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SubscribedClientsChanged(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ReadRequested(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic, Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadRequested(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WriteRequested(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic, Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WriteRequested(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def NotifyValueAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic, value: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientNotificationResult]]: ...
    @winrt_mixinmethod
    def NotifyValueForSubscribedClientAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristic, value: Windows.Storage.Streams.IBuffer, subscribedClient: Windows.Devices.Bluetooth.GenericAttributeProfile.GattSubscribedClient) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientNotificationResult]: ...
    Uuid = property(get_Uuid, None)
    StaticValue = property(get_StaticValue, None)
    CharacteristicProperties = property(get_CharacteristicProperties, None)
    ReadProtectionLevel = property(get_ReadProtectionLevel, None)
    WriteProtectionLevel = property(get_WriteProtectionLevel, None)
    Descriptors = property(get_Descriptors, None)
    UserDescription = property(get_UserDescription, None)
    PresentationFormats = property(get_PresentationFormats, None)
    SubscribedClients = property(get_SubscribedClients, None)
class GattLocalCharacteristicParameters(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristicParameters'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristicParameters: ...
    @winrt_mixinmethod
    def put_StaticValue(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_StaticValue(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_CharacteristicProperties(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters, value: Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties) -> Void: ...
    @winrt_mixinmethod
    def get_CharacteristicProperties(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties: ...
    @winrt_mixinmethod
    def put_ReadProtectionLevel(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters, value: Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_mixinmethod
    def get_ReadProtectionLevel(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_mixinmethod
    def put_WriteProtectionLevel(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters, value: Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_mixinmethod
    def get_WriteProtectionLevel(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_mixinmethod
    def put_UserDescription(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_UserDescription(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PresentationFormats(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicParameters) -> Windows.Foundation.Collections.IVector[Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormat]: ...
    StaticValue = property(get_StaticValue, put_StaticValue)
    CharacteristicProperties = property(get_CharacteristicProperties, put_CharacteristicProperties)
    ReadProtectionLevel = property(get_ReadProtectionLevel, put_ReadProtectionLevel)
    WriteProtectionLevel = property(get_WriteProtectionLevel, put_WriteProtectionLevel)
    UserDescription = property(get_UserDescription, put_UserDescription)
    PresentationFormats = property(get_PresentationFormats, None)
class GattLocalCharacteristicResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristicResult'
    @winrt_mixinmethod
    def get_Characteristic(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicResult) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic: ...
    @winrt_mixinmethod
    def get_Error(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalCharacteristicResult) -> Windows.Devices.Bluetooth.BluetoothError: ...
    Characteristic = property(get_Characteristic, None)
    Error = property(get_Error, None)
class GattLocalDescriptor(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptor'
    @winrt_mixinmethod
    def get_Uuid(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptor) -> Guid: ...
    @winrt_mixinmethod
    def get_StaticValue(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptor) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_ReadProtectionLevel(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptor) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_mixinmethod
    def get_WriteProtectionLevel(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptor) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_mixinmethod
    def add_ReadRequested(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptor, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptor, Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReadRequested(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WriteRequested(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptor, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptor, Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WriteRequested(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Uuid = property(get_Uuid, None)
    StaticValue = property(get_StaticValue, None)
    ReadProtectionLevel = property(get_ReadProtectionLevel, None)
    WriteProtectionLevel = property(get_WriteProtectionLevel, None)
class GattLocalDescriptorParameters(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptorParameters'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptorParameters: ...
    @winrt_mixinmethod
    def put_StaticValue(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorParameters, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_StaticValue(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorParameters) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_ReadProtectionLevel(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorParameters, value: Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_mixinmethod
    def get_ReadProtectionLevel(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorParameters) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_mixinmethod
    def put_WriteProtectionLevel(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorParameters, value: Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_mixinmethod
    def get_WriteProtectionLevel(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorParameters) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    StaticValue = property(get_StaticValue, put_StaticValue)
    ReadProtectionLevel = property(get_ReadProtectionLevel, put_ReadProtectionLevel)
    WriteProtectionLevel = property(get_WriteProtectionLevel, put_WriteProtectionLevel)
class GattLocalDescriptorResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptorResult'
    @winrt_mixinmethod
    def get_Descriptor(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorResult) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptor: ...
    @winrt_mixinmethod
    def get_Error(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalDescriptorResult) -> Windows.Devices.Bluetooth.BluetoothError: ...
    Descriptor = property(get_Descriptor, None)
    Error = property(get_Error, None)
class GattLocalService(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalService'
    @winrt_mixinmethod
    def get_Uuid(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalService) -> Guid: ...
    @winrt_mixinmethod
    def CreateCharacteristicAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalService, characteristicUuid: Guid, parameters: Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristicParameters) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristicResult]: ...
    @winrt_mixinmethod
    def get_Characteristics(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattLocalService) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic]: ...
    Uuid = property(get_Uuid, None)
    Characteristics = property(get_Characteristics, None)
GattOpenStatus = Int32
GattOpenStatus_Unspecified: GattOpenStatus = 0
GattOpenStatus_Success: GattOpenStatus = 1
GattOpenStatus_AlreadyOpened: GattOpenStatus = 2
GattOpenStatus_NotFound: GattOpenStatus = 3
GattOpenStatus_SharingViolation: GattOpenStatus = 4
GattOpenStatus_AccessDenied: GattOpenStatus = 5
class GattPresentationFormat(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormat'
    @winrt_mixinmethod
    def get_FormatType(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormat) -> Byte: ...
    @winrt_mixinmethod
    def get_Exponent(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormat) -> Int32: ...
    @winrt_mixinmethod
    def get_Unit(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormat) -> UInt16: ...
    @winrt_mixinmethod
    def get_Namespace(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormat) -> Byte: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormat) -> UInt16: ...
    @winrt_classmethod
    def FromParts(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatStatics2, formatType: Byte, exponent: Int32, unit: UInt16, namespaceId: Byte, description: UInt16) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormat: ...
    @winrt_classmethod
    def get_BluetoothSigAssignedNumbers(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatStatics) -> Byte: ...
    FormatType = property(get_FormatType, None)
    Exponent = property(get_Exponent, None)
    Unit = property(get_Unit, None)
    Namespace = property(get_Namespace, None)
    Description = property(get_Description, None)
    BluetoothSigAssignedNumbers = property(get_BluetoothSigAssignedNumbers, None)
class GattPresentationFormatTypes(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormatTypes'
    @winrt_classmethod
    def get_Boolean(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_Bit2(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_Nibble(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_UInt8(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_UInt12(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_UInt16(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_UInt24(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_UInt32(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_UInt48(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_UInt64(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_UInt128(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_SInt8(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_SInt12(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_SInt16(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_SInt24(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_SInt32(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_SInt48(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_SInt64(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_SInt128(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_Float32(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_Float64(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_SFloat(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_Float(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_DUInt16(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_Utf8(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_Utf16(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_Struct(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattPresentationFormatTypesStatics) -> Byte: ...
    Boolean = property(get_Boolean, None)
    Bit2 = property(get_Bit2, None)
    Nibble = property(get_Nibble, None)
    UInt8 = property(get_UInt8, None)
    UInt12 = property(get_UInt12, None)
    UInt16 = property(get_UInt16, None)
    UInt24 = property(get_UInt24, None)
    UInt32 = property(get_UInt32, None)
    UInt48 = property(get_UInt48, None)
    UInt64 = property(get_UInt64, None)
    UInt128 = property(get_UInt128, None)
    SInt8 = property(get_SInt8, None)
    SInt12 = property(get_SInt12, None)
    SInt16 = property(get_SInt16, None)
    SInt24 = property(get_SInt24, None)
    SInt32 = property(get_SInt32, None)
    SInt48 = property(get_SInt48, None)
    SInt64 = property(get_SInt64, None)
    SInt128 = property(get_SInt128, None)
    Float32 = property(get_Float32, None)
    Float64 = property(get_Float64, None)
    SFloat = property(get_SFloat, None)
    Float = property(get_Float, None)
    DUInt16 = property(get_DUInt16, None)
    Utf8 = property(get_Utf8, None)
    Utf16 = property(get_Utf16, None)
    Struct = property(get_Struct, None)
GattProtectionLevel = Int32
GattProtectionLevel_Plain: GattProtectionLevel = 0
GattProtectionLevel_AuthenticationRequired: GattProtectionLevel = 1
GattProtectionLevel_EncryptionRequired: GattProtectionLevel = 2
GattProtectionLevel_EncryptionAndAuthenticationRequired: GattProtectionLevel = 3
class GattProtocolError(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtocolError'
    @winrt_classmethod
    def get_InvalidHandle(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_ReadNotPermitted(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_WriteNotPermitted(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_InvalidPdu(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_InsufficientAuthentication(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_RequestNotSupported(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_InvalidOffset(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_InsufficientAuthorization(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_PrepareQueueFull(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_AttributeNotFound(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_AttributeNotLong(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_InsufficientEncryptionKeySize(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_InvalidAttributeValueLength(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_UnlikelyError(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_InsufficientEncryption(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_UnsupportedGroupType(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    @winrt_classmethod
    def get_InsufficientResources(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattProtocolErrorStatics) -> Byte: ...
    InvalidHandle = property(get_InvalidHandle, None)
    ReadNotPermitted = property(get_ReadNotPermitted, None)
    WriteNotPermitted = property(get_WriteNotPermitted, None)
    InvalidPdu = property(get_InvalidPdu, None)
    InsufficientAuthentication = property(get_InsufficientAuthentication, None)
    RequestNotSupported = property(get_RequestNotSupported, None)
    InvalidOffset = property(get_InvalidOffset, None)
    InsufficientAuthorization = property(get_InsufficientAuthorization, None)
    PrepareQueueFull = property(get_PrepareQueueFull, None)
    AttributeNotFound = property(get_AttributeNotFound, None)
    AttributeNotLong = property(get_AttributeNotLong, None)
    InsufficientEncryptionKeySize = property(get_InsufficientEncryptionKeySize, None)
    InvalidAttributeValueLength = property(get_InvalidAttributeValueLength, None)
    UnlikelyError = property(get_UnlikelyError, None)
    InsufficientEncryption = property(get_InsufficientEncryption, None)
    UnsupportedGroupType = property(get_UnsupportedGroupType, None)
    InsufficientResources = property(get_InsufficientResources, None)
class GattReadClientCharacteristicConfigurationDescriptorResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadClientCharacteristicConfigurationDescriptorResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadClientCharacteristicConfigurationDescriptorResult) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_mixinmethod
    def get_ClientCharacteristicConfigurationDescriptor(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadClientCharacteristicConfigurationDescriptorResult) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientCharacteristicConfigurationDescriptorValue: ...
    @winrt_mixinmethod
    def get_ProtocolError(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadClientCharacteristicConfigurationDescriptorResult2) -> Windows.Foundation.IReference[Byte]: ...
    Status = property(get_Status, None)
    ClientCharacteristicConfigurationDescriptor = property(get_ClientCharacteristicConfigurationDescriptor, None)
    ProtocolError = property(get_ProtocolError, None)
class GattReadRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequest'
    @winrt_mixinmethod
    def get_Offset(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequest) -> UInt32: ...
    @winrt_mixinmethod
    def get_Length(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequest) -> UInt32: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequest) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestState: ...
    @winrt_mixinmethod
    def add_StateChanged(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequest, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequest, Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequest, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def RespondWithValue(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequest, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def RespondWithProtocolError(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequest, protocolError: Byte) -> Void: ...
    Offset = property(get_Offset, None)
    Length = property(get_Length, None)
    State = property(get_State, None)
class GattReadRequestedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequestedEventArgs'
    @winrt_mixinmethod
    def get_Session(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequestedEventArgs) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def GetRequestAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadRequestedEventArgs) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequest]: ...
    Session = property(get_Session, None)
class GattReadResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadResult) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadResult) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_ProtocolError(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReadResult2) -> Windows.Foundation.IReference[Byte]: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
    ProtocolError = property(get_ProtocolError, None)
class GattReliableWriteTransaction(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattReliableWriteTransaction'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattReliableWriteTransaction: ...
    @winrt_mixinmethod
    def WriteValue(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReliableWriteTransaction, characteristic: Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def CommitAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReliableWriteTransaction) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
    @winrt_mixinmethod
    def CommitWithResultAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattReliableWriteTransaction2) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
GattRequestState = Int32
GattRequestState_Pending: GattRequestState = 0
GattRequestState_Completed: GattRequestState = 1
GattRequestState_Canceled: GattRequestState = 2
class GattRequestStateChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestStateChangedEventArgs'
    @winrt_mixinmethod
    def get_State(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattRequestStateChangedEventArgs) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestState: ...
    @winrt_mixinmethod
    def get_Error(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattRequestStateChangedEventArgs) -> Windows.Devices.Bluetooth.BluetoothError: ...
    State = property(get_State, None)
    Error = property(get_Error, None)
class GattServiceProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProvider'
    @winrt_mixinmethod
    def get_Service(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProvider) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalService: ...
    @winrt_mixinmethod
    def get_AdvertisementStatus(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProvider) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisementStatus: ...
    @winrt_mixinmethod
    def add_AdvertisementStatusChanged(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProvider, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProvider, Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisementStatusChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AdvertisementStatusChanged(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProvider, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def StartAdvertising(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProvider) -> Void: ...
    @winrt_mixinmethod
    def StartAdvertisingWithParameters(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProvider, parameters: Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisingParameters) -> Void: ...
    @winrt_mixinmethod
    def StopAdvertising(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProvider) -> Void: ...
    @winrt_classmethod
    def CreateAsync(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderStatics, serviceUuid: Guid) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderResult]: ...
    Service = property(get_Service, None)
    AdvertisementStatus = property(get_AdvertisementStatus, None)
GattServiceProviderAdvertisementStatus = Int32
GattServiceProviderAdvertisementStatus_Created: GattServiceProviderAdvertisementStatus = 0
GattServiceProviderAdvertisementStatus_Stopped: GattServiceProviderAdvertisementStatus = 1
GattServiceProviderAdvertisementStatus_Started: GattServiceProviderAdvertisementStatus = 2
GattServiceProviderAdvertisementStatus_Aborted: GattServiceProviderAdvertisementStatus = 3
GattServiceProviderAdvertisementStatus_StartedWithoutAllAdvertisementData: GattServiceProviderAdvertisementStatus = 4
class GattServiceProviderAdvertisementStatusChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisementStatusChangedEventArgs'
    @winrt_mixinmethod
    def get_Error(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisementStatusChangedEventArgs) -> Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisementStatusChangedEventArgs) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisementStatus: ...
    Error = property(get_Error, None)
    Status = property(get_Status, None)
class GattServiceProviderAdvertisingParameters(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisingParameters'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisingParameters: ...
    @winrt_mixinmethod
    def put_IsConnectable(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisingParameters, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsConnectable(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisingParameters) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDiscoverable(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisingParameters, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDiscoverable(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisingParameters) -> Boolean: ...
    @winrt_mixinmethod
    def put_ServiceData(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisingParameters2, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_mixinmethod
    def get_ServiceData(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderAdvertisingParameters2) -> Windows.Storage.Streams.IBuffer: ...
    IsConnectable = property(get_IsConnectable, put_IsConnectable)
    IsDiscoverable = property(get_IsDiscoverable, put_IsDiscoverable)
    ServiceData = property(get_ServiceData, put_ServiceData)
class GattServiceProviderResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderResult'
    @winrt_mixinmethod
    def get_Error(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderResult) -> Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_mixinmethod
    def get_ServiceProvider(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceProviderResult) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProvider: ...
    Error = property(get_Error, None)
    ServiceProvider = property(get_ServiceProvider, None)
class GattServiceUuids(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceUuids'
    @winrt_classmethod
    def get_AlertNotification(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_CurrentTime(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_CyclingPower(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_DeviceInformation(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_HumanInterfaceDevice(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ImmediateAlert(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_LinkLoss(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_LocationAndNavigation(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_NextDstChange(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_PhoneAlertStatus(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ReferenceTimeUpdate(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_ScanParameters(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_TxPower(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics2) -> Guid: ...
    @winrt_classmethod
    def get_Battery(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_BloodPressure(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_CyclingSpeedAndCadence(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_GenericAccess(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_GenericAttribute(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_Glucose(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_HealthThermometer(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_HeartRate(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics) -> Guid: ...
    @winrt_classmethod
    def get_RunningSpeedAndCadence(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattServiceUuidsStatics) -> Guid: ...
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
    Battery = property(get_Battery, None)
    BloodPressure = property(get_BloodPressure, None)
    CyclingSpeedAndCadence = property(get_CyclingSpeedAndCadence, None)
    GenericAccess = property(get_GenericAccess, None)
    GenericAttribute = property(get_GenericAttribute, None)
    Glucose = property(get_Glucose, None)
    HealthThermometer = property(get_HealthThermometer, None)
    HeartRate = property(get_HeartRate, None)
    RunningSpeedAndCadence = property(get_RunningSpeedAndCadence, None)
class GattSession(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession) -> Windows.Devices.Bluetooth.BluetoothDeviceId: ...
    @winrt_mixinmethod
    def get_CanMaintainConnection(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession) -> Boolean: ...
    @winrt_mixinmethod
    def put_MaintainConnection(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MaintainConnection(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxPduSize(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession) -> UInt16: ...
    @winrt_mixinmethod
    def get_SessionStatus(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattSessionStatus: ...
    @winrt_mixinmethod
    def add_MaxPduSizeChanged(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MaxPduSizeChanged(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SessionStatusChanged(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession, Windows.Devices.Bluetooth.GenericAttributeProfile.GattSessionStatusChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SessionStatusChanged(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSession, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def FromDeviceIdAsync(cls: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSessionStatics, deviceId: Windows.Devices.Bluetooth.BluetoothDeviceId) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession]: ...
    DeviceId = property(get_DeviceId, None)
    CanMaintainConnection = property(get_CanMaintainConnection, None)
    MaintainConnection = property(get_MaintainConnection, put_MaintainConnection)
    MaxPduSize = property(get_MaxPduSize, None)
    SessionStatus = property(get_SessionStatus, None)
GattSessionStatus = Int32
GattSessionStatus_Closed: GattSessionStatus = 0
GattSessionStatus_Active: GattSessionStatus = 1
class GattSessionStatusChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattSessionStatusChangedEventArgs'
    @winrt_mixinmethod
    def get_Error(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSessionStatusChangedEventArgs) -> Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSessionStatusChangedEventArgs) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattSessionStatus: ...
    Error = property(get_Error, None)
    Status = property(get_Status, None)
GattSharingMode = Int32
GattSharingMode_Unspecified: GattSharingMode = 0
GattSharingMode_Exclusive: GattSharingMode = 1
GattSharingMode_SharedReadOnly: GattSharingMode = 2
GattSharingMode_SharedReadAndWrite: GattSharingMode = 3
class GattSubscribedClient(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattSubscribedClient'
    @winrt_mixinmethod
    def get_Session(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSubscribedClient) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession: ...
    @winrt_mixinmethod
    def get_MaxNotificationSize(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSubscribedClient) -> UInt16: ...
    @winrt_mixinmethod
    def add_MaxNotificationSizeChanged(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSubscribedClient, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattSubscribedClient, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MaxNotificationSizeChanged(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattSubscribedClient, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Session = property(get_Session, None)
    MaxNotificationSize = property(get_MaxNotificationSize, None)
class GattValueChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattValueChangedEventArgs'
    @winrt_mixinmethod
    def get_CharacteristicValue(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattValueChangedEventArgs) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattValueChangedEventArgs) -> Windows.Foundation.DateTime: ...
    CharacteristicValue = property(get_CharacteristicValue, None)
    Timestamp = property(get_Timestamp, None)
GattWriteOption = Int32
GattWriteOption_WriteWithResponse: GattWriteOption = 0
GattWriteOption_WriteWithoutResponse: GattWriteOption = 1
class GattWriteRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequest'
    @winrt_mixinmethod
    def get_Value(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequest) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_Offset(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequest) -> UInt32: ...
    @winrt_mixinmethod
    def get_Option(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequest) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteOption: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequest) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestState: ...
    @winrt_mixinmethod
    def add_StateChanged(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequest, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequest, Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequest, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Respond(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequest) -> Void: ...
    @winrt_mixinmethod
    def RespondWithProtocolError(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequest, protocolError: Byte) -> Void: ...
    Value = property(get_Value, None)
    Offset = property(get_Offset, None)
    Option = property(get_Option, None)
    State = property(get_State, None)
class GattWriteRequestedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequestedEventArgs'
    @winrt_mixinmethod
    def get_Session(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequestedEventArgs) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def GetRequestAsync(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteRequestedEventArgs) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequest]: ...
    Session = property(get_Session, None)
class GattWriteResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteResult) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_mixinmethod
    def get_ProtocolError(self: Windows.Devices.Bluetooth.GenericAttributeProfile.IGattWriteResult) -> Windows.Foundation.IReference[Byte]: ...
    Status = property(get_Status, None)
    ProtocolError = property(get_ProtocolError, None)
class IGattCharacteristic(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('59cb50c1-5934-4f68-a1-98-eb-86-4f-a4-4e-6b')
    @winrt_commethod(6)
    def GetDescriptors(self, descriptorUuid: Guid) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptor]: ...
    @winrt_commethod(7)
    def get_CharacteristicProperties(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties: ...
    @winrt_commethod(8)
    def get_ProtectionLevel(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_commethod(9)
    def put_ProtectionLevel(self, value: Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_commethod(10)
    def get_UserDescription(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Uuid(self) -> Guid: ...
    @winrt_commethod(12)
    def get_AttributeHandle(self) -> UInt16: ...
    @winrt_commethod(13)
    def get_PresentationFormats(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormat]: ...
    @winrt_commethod(14)
    def ReadValueAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadResult]: ...
    @winrt_commethod(15)
    def ReadValueWithCacheModeAsync(self, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadResult]: ...
    @winrt_commethod(16)
    def WriteValueAsync(self, value: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
    @winrt_commethod(17)
    def WriteValueWithOptionAsync(self, value: Windows.Storage.Streams.IBuffer, writeOption: Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteOption) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
    @winrt_commethod(18)
    def ReadClientCharacteristicConfigurationDescriptorAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadClientCharacteristicConfigurationDescriptorResult]: ...
    @winrt_commethod(19)
    def WriteClientCharacteristicConfigurationDescriptorAsync(self, clientCharacteristicConfigurationDescriptorValue: Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientCharacteristicConfigurationDescriptorValue) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
    @winrt_commethod(20)
    def add_ValueChanged(self, valueChangedHandler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic, Windows.Devices.Bluetooth.GenericAttributeProfile.GattValueChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_ValueChanged(self, valueChangedEventCookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    CharacteristicProperties = property(get_CharacteristicProperties, None)
    ProtectionLevel = property(get_ProtectionLevel, put_ProtectionLevel)
    UserDescription = property(get_UserDescription, None)
    Uuid = property(get_Uuid, None)
    AttributeHandle = property(get_AttributeHandle, None)
    PresentationFormats = property(get_PresentationFormats, None)
class IGattCharacteristic2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ae1ab578-ec06-4764-b7-80-98-35-a1-d3-5d-6e')
    @winrt_commethod(6)
    def get_Service(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService: ...
    @winrt_commethod(7)
    def GetAllDescriptors(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptor]: ...
    Service = property(get_Service, None)
class IGattCharacteristic3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3f3c663e-93d4-406b-b8-17-db-81-f8-ed-53-b3')
    @winrt_commethod(6)
    def GetDescriptorsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorsResult]: ...
    @winrt_commethod(7)
    def GetDescriptorsWithCacheModeAsync(self, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorsResult]: ...
    @winrt_commethod(8)
    def GetDescriptorsForUuidAsync(self, descriptorUuid: Guid) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorsResult]: ...
    @winrt_commethod(9)
    def GetDescriptorsForUuidWithCacheModeAsync(self, descriptorUuid: Guid, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptorsResult]: ...
    @winrt_commethod(10)
    def WriteValueWithResultAsync(self, value: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
    @winrt_commethod(11)
    def WriteValueWithResultAndOptionAsync(self, value: Windows.Storage.Streams.IBuffer, writeOption: Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteOption) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
    @winrt_commethod(12)
    def WriteClientCharacteristicConfigurationDescriptorWithResultAsync(self, clientCharacteristicConfigurationDescriptorValue: Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientCharacteristicConfigurationDescriptorValue) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
class IGattCharacteristicStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('59cb50c3-5934-4f68-a1-98-eb-86-4f-a4-4e-6b')
    @winrt_commethod(6)
    def ConvertShortIdToUuid(self, shortId: UInt16) -> Guid: ...
class IGattCharacteristicUuidsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('58fa4586-b1de-470c-b7-de-0d-11-ff-44-f4-b7')
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
class IGattCharacteristicUuidsStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1855b425-d46e-4a2c-9c-3f-ed-6d-ea-29-e7-be')
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
    GapAppearance = property(get_GapAppearance, None)
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
    GapDeviceName = property(get_GapDeviceName, None)
    DstOffset = property(get_DstOffset, None)
    ExactTime256 = property(get_ExactTime256, None)
    FirmwareRevisionString = property(get_FirmwareRevisionString, None)
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
    GapPeripheralPreferredConnectionParameters = property(get_GapPeripheralPreferredConnectionParameters, None)
    GapPeripheralPrivacyFlag = property(get_GapPeripheralPrivacyFlag, None)
    PnpId = property(get_PnpId, None)
    PositionQuality = property(get_PositionQuality, None)
    ProtocolMode = property(get_ProtocolMode, None)
    GapReconnectionAddress = property(get_GapReconnectionAddress, None)
    ReferenceTimeInformation = property(get_ReferenceTimeInformation, None)
    Report = property(get_Report, None)
    ReportMap = property(get_ReportMap, None)
    RingerControlPoint = property(get_RingerControlPoint, None)
    RingerSetting = property(get_RingerSetting, None)
    ScanIntervalWindow = property(get_ScanIntervalWindow, None)
    ScanRefresh = property(get_ScanRefresh, None)
    SerialNumberString = property(get_SerialNumberString, None)
    GattServiceChanged = property(get_GattServiceChanged, None)
    SoftwareRevisionString = property(get_SoftwareRevisionString, None)
    SupportedNewAlertCategory = property(get_SupportedNewAlertCategory, None)
    SupportUnreadAlertCategory = property(get_SupportUnreadAlertCategory, None)
    SystemId = property(get_SystemId, None)
    TimeAccuracy = property(get_TimeAccuracy, None)
    TimeSource = property(get_TimeSource, None)
    TimeUpdateControlPoint = property(get_TimeUpdateControlPoint, None)
    TimeUpdateState = property(get_TimeUpdateState, None)
    TimeWithDst = property(get_TimeWithDst, None)
    TimeZone = property(get_TimeZone, None)
    TxPowerLevel = property(get_TxPowerLevel, None)
    UnreadAlertStatus = property(get_UnreadAlertStatus, None)
class IGattCharacteristicsResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1194945c-b257-4f3e-9d-b7-f6-8b-c9-a9-ae-f2')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_commethod(7)
    def get_ProtocolError(self) -> Windows.Foundation.IReference[Byte]: ...
    @winrt_commethod(8)
    def get_Characteristics(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic]: ...
    Status = property(get_Status, None)
    ProtocolError = property(get_ProtocolError, None)
    Characteristics = property(get_Characteristics, None)
class IGattClientNotificationResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('506d5599-0112-419a-8e-3b-ae-21-af-ab-d2-c2')
    @winrt_commethod(6)
    def get_SubscribedClient(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattSubscribedClient: ...
    @winrt_commethod(7)
    def get_Status(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_commethod(8)
    def get_ProtocolError(self) -> Windows.Foundation.IReference[Byte]: ...
    SubscribedClient = property(get_SubscribedClient, None)
    Status = property(get_Status, None)
    ProtocolError = property(get_ProtocolError, None)
class IGattClientNotificationResult2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8faec497-45e0-497e-95-82-29-a1-fe-28-1a-d5')
    @winrt_commethod(6)
    def get_BytesSent(self) -> UInt16: ...
    BytesSent = property(get_BytesSent, None)
class IGattDescriptor(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('92055f2b-8084-4344-b4-c2-28-4d-e1-9a-85-06')
    @winrt_commethod(6)
    def get_ProtectionLevel(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_commethod(7)
    def put_ProtectionLevel(self, value: Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_commethod(8)
    def get_Uuid(self) -> Guid: ...
    @winrt_commethod(9)
    def get_AttributeHandle(self) -> UInt16: ...
    @winrt_commethod(10)
    def ReadValueAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadResult]: ...
    @winrt_commethod(11)
    def ReadValueWithCacheModeAsync(self, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadResult]: ...
    @winrt_commethod(12)
    def WriteValueAsync(self, value: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
    ProtectionLevel = property(get_ProtectionLevel, put_ProtectionLevel)
    Uuid = property(get_Uuid, None)
    AttributeHandle = property(get_AttributeHandle, None)
class IGattDescriptor2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8f563d39-d630-406c-ba-11-10-cd-d1-6b-0e-5e')
    @winrt_commethod(6)
    def WriteValueWithResultAsync(self, value: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
class IGattDescriptorStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('92055f2d-8084-4344-b4-c2-28-4d-e1-9a-85-06')
    @winrt_commethod(6)
    def ConvertShortIdToUuid(self, shortId: UInt16) -> Guid: ...
class IGattDescriptorUuidsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a6f862ce-9cfc-42f1-91-85-ff-37-b7-51-81-d3')
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
class IGattDescriptorsResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9bc091f3-95e7-4489-8d-25-ff-81-95-5a-57-b9')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_commethod(7)
    def get_ProtocolError(self) -> Windows.Foundation.IReference[Byte]: ...
    @winrt_commethod(8)
    def get_Descriptors(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDescriptor]: ...
    Status = property(get_Status, None)
    ProtocolError = property(get_ProtocolError, None)
    Descriptors = property(get_Descriptors, None)
class IGattDeviceService(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ac7b7c05-b33c-47cf-99-0f-6b-8f-55-77-df-71')
    @winrt_commethod(6)
    def GetCharacteristics(self, characteristicUuid: Guid) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic]: ...
    @winrt_commethod(7)
    def GetIncludedServices(self, serviceUuid: Guid) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_commethod(8)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Uuid(self) -> Guid: ...
    @winrt_commethod(10)
    def get_AttributeHandle(self) -> UInt16: ...
    DeviceId = property(get_DeviceId, None)
    Uuid = property(get_Uuid, None)
    AttributeHandle = property(get_AttributeHandle, None)
class IGattDeviceService2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fc54520b-0b0d-4708-ba-e0-9f-fd-94-89-bc-59')
    @winrt_commethod(6)
    def get_Device(self) -> Windows.Devices.Bluetooth.BluetoothLEDevice: ...
    @winrt_commethod(7)
    def get_ParentServices(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_commethod(8)
    def GetAllCharacteristics(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic]: ...
    @winrt_commethod(9)
    def GetAllIncludedServices(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    Device = property(get_Device, None)
    ParentServices = property(get_ParentServices, None)
class IGattDeviceService3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b293a950-0c53-437c-a9-b3-5c-32-10-c6-e5-69')
    @winrt_commethod(6)
    def get_DeviceAccessInformation(self) -> Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_commethod(7)
    def get_Session(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession: ...
    @winrt_commethod(8)
    def get_SharingMode(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattSharingMode: ...
    @winrt_commethod(9)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceAccessStatus]: ...
    @winrt_commethod(10)
    def OpenAsync(self, sharingMode: Windows.Devices.Bluetooth.GenericAttributeProfile.GattSharingMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattOpenStatus]: ...
    @winrt_commethod(11)
    def GetCharacteristicsAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicsResult]: ...
    @winrt_commethod(12)
    def GetCharacteristicsWithCacheModeAsync(self, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicsResult]: ...
    @winrt_commethod(13)
    def GetCharacteristicsForUuidAsync(self, characteristicUuid: Guid) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicsResult]: ...
    @winrt_commethod(14)
    def GetCharacteristicsForUuidWithCacheModeAsync(self, characteristicUuid: Guid, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicsResult]: ...
    @winrt_commethod(15)
    def GetIncludedServicesAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_commethod(16)
    def GetIncludedServicesWithCacheModeAsync(self, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_commethod(17)
    def GetIncludedServicesForUuidAsync(self, serviceUuid: Guid) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_commethod(18)
    def GetIncludedServicesForUuidWithCacheModeAsync(self, serviceUuid: Guid, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    DeviceAccessInformation = property(get_DeviceAccessInformation, None)
    Session = property(get_Session, None)
    SharingMode = property(get_SharingMode, None)
class IGattDeviceServiceStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('196d0022-faad-45dc-ae-5b-2a-c3-18-4e-84-db')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_commethod(7)
    def GetDeviceSelectorFromUuid(self, serviceUuid: Guid) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetDeviceSelectorFromShortId(self, serviceShortId: UInt16) -> WinRT_String: ...
    @winrt_commethod(9)
    def ConvertShortIdToUuid(self, shortId: UInt16) -> Guid: ...
class IGattDeviceServiceStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0604186e-24a6-4b0d-a2-f2-30-cc-01-54-5d-25')
    @winrt_commethod(6)
    def FromIdWithSharingModeAsync(self, deviceId: WinRT_String, sharingMode: Windows.Devices.Bluetooth.GenericAttributeProfile.GattSharingMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_commethod(7)
    def GetDeviceSelectorForBluetoothDeviceId(self, bluetoothDeviceId: Windows.Devices.Bluetooth.BluetoothDeviceId) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetDeviceSelectorForBluetoothDeviceIdWithCacheMode(self, bluetoothDeviceId: Windows.Devices.Bluetooth.BluetoothDeviceId, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetDeviceSelectorForBluetoothDeviceIdAndUuid(self, bluetoothDeviceId: Windows.Devices.Bluetooth.BluetoothDeviceId, serviceUuid: Guid) -> WinRT_String: ...
    @winrt_commethod(10)
    def GetDeviceSelectorForBluetoothDeviceIdAndUuidWithCacheMode(self, bluetoothDeviceId: Windows.Devices.Bluetooth.BluetoothDeviceId, serviceUuid: Guid, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> WinRT_String: ...
class IGattDeviceServicesResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('171dd3ee-016d-419d-83-8a-57-6c-f4-75-a3-d8')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_commethod(7)
    def get_ProtocolError(self) -> Windows.Foundation.IReference[Byte]: ...
    @winrt_commethod(8)
    def get_Services(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    Status = property(get_Status, None)
    ProtocolError = property(get_ProtocolError, None)
    Services = property(get_Services, None)
class IGattLocalCharacteristic(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('aede376d-5412-4d74-92-a8-8d-eb-85-26-82-9c')
    @winrt_commethod(6)
    def get_Uuid(self) -> Guid: ...
    @winrt_commethod(7)
    def get_StaticValue(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def get_CharacteristicProperties(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties: ...
    @winrt_commethod(9)
    def get_ReadProtectionLevel(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_commethod(10)
    def get_WriteProtectionLevel(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_commethod(11)
    def CreateDescriptorAsync(self, descriptorUuid: Guid, parameters: Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptorParameters) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptorResult]: ...
    @winrt_commethod(12)
    def get_Descriptors(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptor]: ...
    @winrt_commethod(13)
    def get_UserDescription(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_PresentationFormats(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormat]: ...
    @winrt_commethod(15)
    def get_SubscribedClients(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattSubscribedClient]: ...
    @winrt_commethod(16)
    def add_SubscribedClientsChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_SubscribedClientsChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_ReadRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic, Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_ReadRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_WriteRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic, Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_WriteRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def NotifyValueAsync(self, value: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientNotificationResult]]: ...
    @winrt_commethod(23)
    def NotifyValueForSubscribedClientAsync(self, value: Windows.Storage.Streams.IBuffer, subscribedClient: Windows.Devices.Bluetooth.GenericAttributeProfile.GattSubscribedClient) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientNotificationResult]: ...
    Uuid = property(get_Uuid, None)
    StaticValue = property(get_StaticValue, None)
    CharacteristicProperties = property(get_CharacteristicProperties, None)
    ReadProtectionLevel = property(get_ReadProtectionLevel, None)
    WriteProtectionLevel = property(get_WriteProtectionLevel, None)
    Descriptors = property(get_Descriptors, None)
    UserDescription = property(get_UserDescription, None)
    PresentationFormats = property(get_PresentationFormats, None)
    SubscribedClients = property(get_SubscribedClients, None)
class IGattLocalCharacteristicParameters(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('faf73db4-4cff-44c7-84-45-04-0e-6e-ad-00-63')
    @winrt_commethod(6)
    def put_StaticValue(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(7)
    def get_StaticValue(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def put_CharacteristicProperties(self, value: Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties) -> Void: ...
    @winrt_commethod(9)
    def get_CharacteristicProperties(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristicProperties: ...
    @winrt_commethod(10)
    def put_ReadProtectionLevel(self, value: Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_commethod(11)
    def get_ReadProtectionLevel(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_commethod(12)
    def put_WriteProtectionLevel(self, value: Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_commethod(13)
    def get_WriteProtectionLevel(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_commethod(14)
    def put_UserDescription(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_UserDescription(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_PresentationFormats(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormat]: ...
    StaticValue = property(get_StaticValue, put_StaticValue)
    CharacteristicProperties = property(get_CharacteristicProperties, put_CharacteristicProperties)
    ReadProtectionLevel = property(get_ReadProtectionLevel, put_ReadProtectionLevel)
    WriteProtectionLevel = property(get_WriteProtectionLevel, put_WriteProtectionLevel)
    UserDescription = property(get_UserDescription, put_UserDescription)
    PresentationFormats = property(get_PresentationFormats, None)
class IGattLocalCharacteristicResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7975de9b-0170-4397-96-66-92-f8-63-f1-2e-e6')
    @winrt_commethod(6)
    def get_Characteristic(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic: ...
    @winrt_commethod(7)
    def get_Error(self) -> Windows.Devices.Bluetooth.BluetoothError: ...
    Characteristic = property(get_Characteristic, None)
    Error = property(get_Error, None)
class IGattLocalDescriptor(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f48ebe06-789d-4a4b-86-52-bd-01-7b-5d-2f-c6')
    @winrt_commethod(6)
    def get_Uuid(self) -> Guid: ...
    @winrt_commethod(7)
    def get_StaticValue(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def get_ReadProtectionLevel(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_commethod(9)
    def get_WriteProtectionLevel(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_commethod(10)
    def add_ReadRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptor, Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ReadRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_WriteRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptor, Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_WriteRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Uuid = property(get_Uuid, None)
    StaticValue = property(get_StaticValue, None)
    ReadProtectionLevel = property(get_ReadProtectionLevel, None)
    WriteProtectionLevel = property(get_WriteProtectionLevel, None)
class IGattLocalDescriptorParameters(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5fdede6a-f3c1-4b66-8c-4b-e3-d2-29-3b-40-e9')
    @winrt_commethod(6)
    def put_StaticValue(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(7)
    def get_StaticValue(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def put_ReadProtectionLevel(self, value: Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_commethod(9)
    def get_ReadProtectionLevel(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    @winrt_commethod(10)
    def put_WriteProtectionLevel(self, value: Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel) -> Void: ...
    @winrt_commethod(11)
    def get_WriteProtectionLevel(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattProtectionLevel: ...
    StaticValue = property(get_StaticValue, put_StaticValue)
    ReadProtectionLevel = property(get_ReadProtectionLevel, put_ReadProtectionLevel)
    WriteProtectionLevel = property(get_WriteProtectionLevel, put_WriteProtectionLevel)
class IGattLocalDescriptorResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('375791be-321f-4366-bf-c1-3b-c6-b8-2c-79-f8')
    @winrt_commethod(6)
    def get_Descriptor(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalDescriptor: ...
    @winrt_commethod(7)
    def get_Error(self) -> Windows.Devices.Bluetooth.BluetoothError: ...
    Descriptor = property(get_Descriptor, None)
    Error = property(get_Error, None)
class IGattLocalService(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f513e258-f7f7-4902-b8-03-57-fc-c7-d6-fe-83')
    @winrt_commethod(6)
    def get_Uuid(self) -> Guid: ...
    @winrt_commethod(7)
    def CreateCharacteristicAsync(self, characteristicUuid: Guid, parameters: Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristicParameters) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristicResult]: ...
    @winrt_commethod(8)
    def get_Characteristics(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalCharacteristic]: ...
    Uuid = property(get_Uuid, None)
    Characteristics = property(get_Characteristics, None)
class IGattPresentationFormat(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('196d0021-faad-45dc-ae-5b-2a-c3-18-4e-84-db')
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
    FormatType = property(get_FormatType, None)
    Exponent = property(get_Exponent, None)
    Unit = property(get_Unit, None)
    Namespace = property(get_Namespace, None)
    Description = property(get_Description, None)
class IGattPresentationFormatStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('196d0020-faad-45dc-ae-5b-2a-c3-18-4e-84-db')
    @winrt_commethod(6)
    def get_BluetoothSigAssignedNumbers(self) -> Byte: ...
    BluetoothSigAssignedNumbers = property(get_BluetoothSigAssignedNumbers, None)
class IGattPresentationFormatStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a9c21713-b82f-435e-b6-34-21-fd-85-a4-3c-07')
    @winrt_commethod(6)
    def FromParts(self, formatType: Byte, exponent: Int32, unit: UInt16, namespaceId: Byte, description: UInt16) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattPresentationFormat: ...
class IGattPresentationFormatTypesStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('faf1ba0a-30ba-409c-be-f7-cf-fb-6d-03-b8-fb')
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
    Boolean = property(get_Boolean, None)
    Bit2 = property(get_Bit2, None)
    Nibble = property(get_Nibble, None)
    UInt8 = property(get_UInt8, None)
    UInt12 = property(get_UInt12, None)
    UInt16 = property(get_UInt16, None)
    UInt24 = property(get_UInt24, None)
    UInt32 = property(get_UInt32, None)
    UInt48 = property(get_UInt48, None)
    UInt64 = property(get_UInt64, None)
    UInt128 = property(get_UInt128, None)
    SInt8 = property(get_SInt8, None)
    SInt12 = property(get_SInt12, None)
    SInt16 = property(get_SInt16, None)
    SInt24 = property(get_SInt24, None)
    SInt32 = property(get_SInt32, None)
    SInt48 = property(get_SInt48, None)
    SInt64 = property(get_SInt64, None)
    SInt128 = property(get_SInt128, None)
    Float32 = property(get_Float32, None)
    Float64 = property(get_Float64, None)
    SFloat = property(get_SFloat, None)
    Float = property(get_Float, None)
    DUInt16 = property(get_DUInt16, None)
    Utf8 = property(get_Utf8, None)
    Utf16 = property(get_Utf16, None)
    Struct = property(get_Struct, None)
class IGattProtocolErrorStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ca46c5c5-0ecc-4809-be-a3-cf-79-bc-99-1e-37')
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
    InvalidHandle = property(get_InvalidHandle, None)
    ReadNotPermitted = property(get_ReadNotPermitted, None)
    WriteNotPermitted = property(get_WriteNotPermitted, None)
    InvalidPdu = property(get_InvalidPdu, None)
    InsufficientAuthentication = property(get_InsufficientAuthentication, None)
    RequestNotSupported = property(get_RequestNotSupported, None)
    InvalidOffset = property(get_InvalidOffset, None)
    InsufficientAuthorization = property(get_InsufficientAuthorization, None)
    PrepareQueueFull = property(get_PrepareQueueFull, None)
    AttributeNotFound = property(get_AttributeNotFound, None)
    AttributeNotLong = property(get_AttributeNotLong, None)
    InsufficientEncryptionKeySize = property(get_InsufficientEncryptionKeySize, None)
    InvalidAttributeValueLength = property(get_InvalidAttributeValueLength, None)
    UnlikelyError = property(get_UnlikelyError, None)
    InsufficientEncryption = property(get_InsufficientEncryption, None)
    UnsupportedGroupType = property(get_UnsupportedGroupType, None)
    InsufficientResources = property(get_InsufficientResources, None)
class IGattReadClientCharacteristicConfigurationDescriptorResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('63a66f09-1aea-4c4c-a5-0f-97-ba-e4-74-b3-48')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_commethod(7)
    def get_ClientCharacteristicConfigurationDescriptor(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattClientCharacteristicConfigurationDescriptorValue: ...
    Status = property(get_Status, None)
    ClientCharacteristicConfigurationDescriptor = property(get_ClientCharacteristicConfigurationDescriptor, None)
class IGattReadClientCharacteristicConfigurationDescriptorResult2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1bf1a59d-ba4d-4622-86-51-f4-ee-15-0d-0a-5d')
    @winrt_commethod(6)
    def get_ProtocolError(self) -> Windows.Foundation.IReference[Byte]: ...
    ProtocolError = property(get_ProtocolError, None)
class IGattReadRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f1dd6535-6acd-42a6-a4-bb-d7-89-da-e0-04-3e')
    @winrt_commethod(6)
    def get_Offset(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Length(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_State(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestState: ...
    @winrt_commethod(9)
    def add_StateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequest, Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_StateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def RespondWithValue(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(12)
    def RespondWithProtocolError(self, protocolError: Byte) -> Void: ...
    Offset = property(get_Offset, None)
    Length = property(get_Length, None)
    State = property(get_State, None)
class IGattReadRequestedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('93497243-f39c-484b-8a-b6-99-6b-a4-86-cf-a3')
    @winrt_commethod(6)
    def get_Session(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    @winrt_commethod(8)
    def GetRequestAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattReadRequest]: ...
    Session = property(get_Session, None)
class IGattReadResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('63a66f08-1aea-4c4c-a5-0f-97-ba-e4-74-b3-48')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_commethod(7)
    def get_Value(self) -> Windows.Storage.Streams.IBuffer: ...
    Status = property(get_Status, None)
    Value = property(get_Value, None)
class IGattReadResult2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a10f50a0-fb43-48af-ba-aa-63-8a-5c-63-29-fe')
    @winrt_commethod(6)
    def get_ProtocolError(self) -> Windows.Foundation.IReference[Byte]: ...
    ProtocolError = property(get_ProtocolError, None)
class IGattReliableWriteTransaction(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('63a66f07-1aea-4c4c-a5-0f-97-ba-e4-74-b3-48')
    @winrt_commethod(6)
    def WriteValue(self, characteristic: Windows.Devices.Bluetooth.GenericAttributeProfile.GattCharacteristic, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(7)
    def CommitAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus]: ...
class IGattReliableWriteTransaction2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('51113987-ef12-462f-9f-b2-a1-a4-3a-67-94-16')
    @winrt_commethod(6)
    def CommitWithResultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteResult]: ...
class IGattRequestStateChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e834d92c-27be-44b3-9d-0d-4f-c6-e8-08-dd-3f')
    @winrt_commethod(6)
    def get_State(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestState: ...
    @winrt_commethod(7)
    def get_Error(self) -> Windows.Devices.Bluetooth.BluetoothError: ...
    State = property(get_State, None)
    Error = property(get_Error, None)
class IGattServiceProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7822b3cd-2889-4f86-a0-51-3f-0a-ed-1c-27-60')
    @winrt_commethod(6)
    def get_Service(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattLocalService: ...
    @winrt_commethod(7)
    def get_AdvertisementStatus(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisementStatus: ...
    @winrt_commethod(8)
    def add_AdvertisementStatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProvider, Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisementStatusChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_AdvertisementStatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def StartAdvertising(self) -> Void: ...
    @winrt_commethod(11)
    def StartAdvertisingWithParameters(self, parameters: Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisingParameters) -> Void: ...
    @winrt_commethod(12)
    def StopAdvertising(self) -> Void: ...
    Service = property(get_Service, None)
    AdvertisementStatus = property(get_AdvertisementStatus, None)
class IGattServiceProviderAdvertisementStatusChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('59a5aa65-fa21-4ffc-b1-55-04-d9-28-01-26-86')
    @winrt_commethod(6)
    def get_Error(self) -> Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_commethod(7)
    def get_Status(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderAdvertisementStatus: ...
    Error = property(get_Error, None)
    Status = property(get_Status, None)
class IGattServiceProviderAdvertisingParameters(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e2ce31ab-6315-4c22-9b-d7-78-1d-bc-3d-8d-82')
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
class IGattServiceProviderAdvertisingParameters2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ff68468d-ca92-4434-97-43-0e-90-98-8a-d8-79')
    @winrt_commethod(6)
    def put_ServiceData(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    @winrt_commethod(7)
    def get_ServiceData(self) -> Windows.Storage.Streams.IBuffer: ...
    ServiceData = property(get_ServiceData, put_ServiceData)
class IGattServiceProviderResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('764696d8-c53e-428c-8a-48-67-af-e0-2c-3a-e6')
    @winrt_commethod(6)
    def get_Error(self) -> Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_commethod(7)
    def get_ServiceProvider(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProvider: ...
    Error = property(get_Error, None)
    ServiceProvider = property(get_ServiceProvider, None)
class IGattServiceProviderStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('31794063-5256-4054-a4-f4-7b-be-77-55-a5-7e')
    @winrt_commethod(6)
    def CreateAsync(self, serviceUuid: Guid) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattServiceProviderResult]: ...
class IGattServiceUuidsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6dc57058-9aba-4417-b8-f2-dc-e0-16-d3-4e-e2')
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
class IGattServiceUuidsStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d2ae94f5-3d15-4f79-9c-0c-ea-af-a6-75-15-5c')
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
class IGattSession(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d23b5143-e04e-4c24-99-9c-9c-25-6f-98-56-b1')
    @winrt_commethod(6)
    def get_DeviceId(self) -> Windows.Devices.Bluetooth.BluetoothDeviceId: ...
    @winrt_commethod(7)
    def get_CanMaintainConnection(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_MaintainConnection(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_MaintainConnection(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_MaxPduSize(self) -> UInt16: ...
    @winrt_commethod(11)
    def get_SessionStatus(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattSessionStatus: ...
    @winrt_commethod(12)
    def add_MaxPduSizeChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_MaxPduSizeChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_SessionStatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession, Windows.Devices.Bluetooth.GenericAttributeProfile.GattSessionStatusChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_SessionStatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    CanMaintainConnection = property(get_CanMaintainConnection, None)
    MaintainConnection = property(get_MaintainConnection, put_MaintainConnection)
    MaxPduSize = property(get_MaxPduSize, None)
    SessionStatus = property(get_SessionStatus, None)
class IGattSessionStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2e65b95c-539f-4db7-82-a8-73-bd-bb-f7-3e-bf')
    @winrt_commethod(6)
    def FromDeviceIdAsync(self, deviceId: Windows.Devices.Bluetooth.BluetoothDeviceId) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession]: ...
class IGattSessionStatusChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7605b72e-837f-404c-ab-34-31-63-f3-9d-df-32')
    @winrt_commethod(6)
    def get_Error(self) -> Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_commethod(7)
    def get_Status(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattSessionStatus: ...
    Error = property(get_Error, None)
    Status = property(get_Status, None)
class IGattSubscribedClient(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('736e9001-15a4-4ec2-92-48-e3-f2-0d-46-3b-e9')
    @winrt_commethod(6)
    def get_Session(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession: ...
    @winrt_commethod(7)
    def get_MaxNotificationSize(self) -> UInt16: ...
    @winrt_commethod(8)
    def add_MaxNotificationSizeChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattSubscribedClient, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_MaxNotificationSizeChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Session = property(get_Session, None)
    MaxNotificationSize = property(get_MaxNotificationSize, None)
class IGattValueChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d21bdb54-06e3-4ed8-a2-63-ac-fa-c8-ba-73-13')
    @winrt_commethod(6)
    def get_CharacteristicValue(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    CharacteristicValue = property(get_CharacteristicValue, None)
    Timestamp = property(get_Timestamp, None)
class IGattWriteRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('aeb6a9ed-de2f-4fc2-a9-a8-94-ea-78-44-f1-3d')
    @winrt_commethod(6)
    def get_Value(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_Offset(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Option(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteOption: ...
    @winrt_commethod(9)
    def get_State(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestState: ...
    @winrt_commethod(10)
    def add_StateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequest, Windows.Devices.Bluetooth.GenericAttributeProfile.GattRequestStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_StateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def Respond(self) -> Void: ...
    @winrt_commethod(13)
    def RespondWithProtocolError(self, protocolError: Byte) -> Void: ...
    Value = property(get_Value, None)
    Offset = property(get_Offset, None)
    Option = property(get_Option, None)
    State = property(get_State, None)
class IGattWriteRequestedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2dec8bbe-a73a-471a-94-d5-03-7d-ea-dd-08-06')
    @winrt_commethod(6)
    def get_Session(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattSession: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    @winrt_commethod(8)
    def GetRequestAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattWriteRequest]: ...
    Session = property(get_Session, None)
class IGattWriteResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4991ddb1-cb2b-44f7-99-fc-d2-9a-28-71-dc-9b')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattCommunicationStatus: ...
    @winrt_commethod(7)
    def get_ProtocolError(self) -> Windows.Foundation.IReference[Byte]: ...
    Status = property(get_Status, None)
    ProtocolError = property(get_ProtocolError, None)
make_head(_module, 'GattCharacteristic')
make_head(_module, 'GattCharacteristicUuids')
make_head(_module, 'GattCharacteristicsResult')
make_head(_module, 'GattClientNotificationResult')
make_head(_module, 'GattDescriptor')
make_head(_module, 'GattDescriptorUuids')
make_head(_module, 'GattDescriptorsResult')
make_head(_module, 'GattDeviceService')
make_head(_module, 'GattDeviceServicesResult')
make_head(_module, 'GattLocalCharacteristic')
make_head(_module, 'GattLocalCharacteristicParameters')
make_head(_module, 'GattLocalCharacteristicResult')
make_head(_module, 'GattLocalDescriptor')
make_head(_module, 'GattLocalDescriptorParameters')
make_head(_module, 'GattLocalDescriptorResult')
make_head(_module, 'GattLocalService')
make_head(_module, 'GattPresentationFormat')
make_head(_module, 'GattPresentationFormatTypes')
make_head(_module, 'GattProtocolError')
make_head(_module, 'GattReadClientCharacteristicConfigurationDescriptorResult')
make_head(_module, 'GattReadRequest')
make_head(_module, 'GattReadRequestedEventArgs')
make_head(_module, 'GattReadResult')
make_head(_module, 'GattReliableWriteTransaction')
make_head(_module, 'GattRequestStateChangedEventArgs')
make_head(_module, 'GattServiceProvider')
make_head(_module, 'GattServiceProviderAdvertisementStatusChangedEventArgs')
make_head(_module, 'GattServiceProviderAdvertisingParameters')
make_head(_module, 'GattServiceProviderResult')
make_head(_module, 'GattServiceUuids')
make_head(_module, 'GattSession')
make_head(_module, 'GattSessionStatusChangedEventArgs')
make_head(_module, 'GattSubscribedClient')
make_head(_module, 'GattValueChangedEventArgs')
make_head(_module, 'GattWriteRequest')
make_head(_module, 'GattWriteRequestedEventArgs')
make_head(_module, 'GattWriteResult')
make_head(_module, 'IGattCharacteristic')
make_head(_module, 'IGattCharacteristic2')
make_head(_module, 'IGattCharacteristic3')
make_head(_module, 'IGattCharacteristicStatics')
make_head(_module, 'IGattCharacteristicUuidsStatics')
make_head(_module, 'IGattCharacteristicUuidsStatics2')
make_head(_module, 'IGattCharacteristicsResult')
make_head(_module, 'IGattClientNotificationResult')
make_head(_module, 'IGattClientNotificationResult2')
make_head(_module, 'IGattDescriptor')
make_head(_module, 'IGattDescriptor2')
make_head(_module, 'IGattDescriptorStatics')
make_head(_module, 'IGattDescriptorUuidsStatics')
make_head(_module, 'IGattDescriptorsResult')
make_head(_module, 'IGattDeviceService')
make_head(_module, 'IGattDeviceService2')
make_head(_module, 'IGattDeviceService3')
make_head(_module, 'IGattDeviceServiceStatics')
make_head(_module, 'IGattDeviceServiceStatics2')
make_head(_module, 'IGattDeviceServicesResult')
make_head(_module, 'IGattLocalCharacteristic')
make_head(_module, 'IGattLocalCharacteristicParameters')
make_head(_module, 'IGattLocalCharacteristicResult')
make_head(_module, 'IGattLocalDescriptor')
make_head(_module, 'IGattLocalDescriptorParameters')
make_head(_module, 'IGattLocalDescriptorResult')
make_head(_module, 'IGattLocalService')
make_head(_module, 'IGattPresentationFormat')
make_head(_module, 'IGattPresentationFormatStatics')
make_head(_module, 'IGattPresentationFormatStatics2')
make_head(_module, 'IGattPresentationFormatTypesStatics')
make_head(_module, 'IGattProtocolErrorStatics')
make_head(_module, 'IGattReadClientCharacteristicConfigurationDescriptorResult')
make_head(_module, 'IGattReadClientCharacteristicConfigurationDescriptorResult2')
make_head(_module, 'IGattReadRequest')
make_head(_module, 'IGattReadRequestedEventArgs')
make_head(_module, 'IGattReadResult')
make_head(_module, 'IGattReadResult2')
make_head(_module, 'IGattReliableWriteTransaction')
make_head(_module, 'IGattReliableWriteTransaction2')
make_head(_module, 'IGattRequestStateChangedEventArgs')
make_head(_module, 'IGattServiceProvider')
make_head(_module, 'IGattServiceProviderAdvertisementStatusChangedEventArgs')
make_head(_module, 'IGattServiceProviderAdvertisingParameters')
make_head(_module, 'IGattServiceProviderAdvertisingParameters2')
make_head(_module, 'IGattServiceProviderResult')
make_head(_module, 'IGattServiceProviderStatics')
make_head(_module, 'IGattServiceUuidsStatics')
make_head(_module, 'IGattServiceUuidsStatics2')
make_head(_module, 'IGattSession')
make_head(_module, 'IGattSessionStatics')
make_head(_module, 'IGattSessionStatusChangedEventArgs')
make_head(_module, 'IGattSubscribedClient')
make_head(_module, 'IGattValueChangedEventArgs')
make_head(_module, 'IGattWriteRequest')
make_head(_module, 'IGattWriteRequestedEventArgs')
make_head(_module, 'IGattWriteResult')
