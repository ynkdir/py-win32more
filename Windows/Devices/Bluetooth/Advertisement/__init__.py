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
import Windows.Devices.Bluetooth.Advertisement
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
class BluetoothLEAdvertisement(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    @winrt_mixinmethod
    def get_Flags(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement) -> Windows.Foundation.IReference[Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFlags]: ...
    @winrt_mixinmethod
    def put_Flags(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement, value: Windows.Foundation.IReference[Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFlags]) -> Void: ...
    @winrt_mixinmethod
    def get_LocalName(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LocalName(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ServiceUuids(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement) -> Windows.Foundation.Collections.IVector[Guid]: ...
    @winrt_mixinmethod
    def get_ManufacturerData(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement) -> Windows.Foundation.Collections.IVector[Windows.Devices.Bluetooth.Advertisement.BluetoothLEManufacturerData]: ...
    @winrt_mixinmethod
    def get_DataSections(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement) -> Windows.Foundation.Collections.IVector[Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataSection]: ...
    @winrt_mixinmethod
    def GetManufacturerDataByCompanyId(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement, companyId: UInt16) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.Advertisement.BluetoothLEManufacturerData]: ...
    @winrt_mixinmethod
    def GetSectionsByType(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement, type: Byte) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataSection]: ...
    Flags = property(get_Flags, put_Flags)
    LocalName = property(get_LocalName, put_LocalName)
    ServiceUuids = property(get_ServiceUuids, None)
    ManufacturerData = property(get_ManufacturerData, None)
    DataSections = property(get_DataSections, None)
class BluetoothLEAdvertisementBytePattern(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementBytePattern'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementBytePattern: ...
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementBytePatternFactory, dataType: Byte, offset: Int16, data: Windows.Storage.Streams.IBuffer) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementBytePattern: ...
    @winrt_mixinmethod
    def get_DataType(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementBytePattern) -> Byte: ...
    @winrt_mixinmethod
    def put_DataType(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementBytePattern, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementBytePattern) -> Int16: ...
    @winrt_mixinmethod
    def put_Offset(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementBytePattern, value: Int16) -> Void: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementBytePattern) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_Data(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementBytePattern, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    DataType = property(get_DataType, put_DataType)
    Offset = property(get_Offset, put_Offset)
    Data = property(get_Data, put_Data)
class BluetoothLEAdvertisementDataSection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataSection'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataSectionFactory, dataType: Byte, data: Windows.Storage.Streams.IBuffer) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataSection: ...
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataSection: ...
    @winrt_mixinmethod
    def get_DataType(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataSection) -> Byte: ...
    @winrt_mixinmethod
    def put_DataType(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataSection, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataSection) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_Data(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataSection, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    DataType = property(get_DataType, put_DataType)
    Data = property(get_Data, put_Data)
class BluetoothLEAdvertisementDataTypes(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataTypes'
    @winrt_classmethod
    def get_Flags(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_IncompleteService16BitUuids(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_CompleteService16BitUuids(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_IncompleteService32BitUuids(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_CompleteService32BitUuids(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_IncompleteService128BitUuids(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_CompleteService128BitUuids(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_ShortenedLocalName(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_CompleteLocalName(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_TxPowerLevel(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_PeripheralConnectionIntervalRange(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_ServiceSolicitation16BitUuids(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_ServiceSolicitation32BitUuids(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_ServiceSolicitation128BitUuids(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_ServiceData16BitUuids(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_ServiceData32BitUuids(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_ServiceData128BitUuids(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_PublicTargetAddress(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_RandomTargetAddress(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_Appearance(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_AdvertisingInterval(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_ManufacturerSpecificData(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    Flags = property(get_Flags, None)
    IncompleteService16BitUuids = property(get_IncompleteService16BitUuids, None)
    CompleteService16BitUuids = property(get_CompleteService16BitUuids, None)
    IncompleteService32BitUuids = property(get_IncompleteService32BitUuids, None)
    CompleteService32BitUuids = property(get_CompleteService32BitUuids, None)
    IncompleteService128BitUuids = property(get_IncompleteService128BitUuids, None)
    CompleteService128BitUuids = property(get_CompleteService128BitUuids, None)
    ShortenedLocalName = property(get_ShortenedLocalName, None)
    CompleteLocalName = property(get_CompleteLocalName, None)
    TxPowerLevel = property(get_TxPowerLevel, None)
    PeripheralConnectionIntervalRange = property(get_PeripheralConnectionIntervalRange, None)
    ServiceSolicitation16BitUuids = property(get_ServiceSolicitation16BitUuids, None)
    ServiceSolicitation32BitUuids = property(get_ServiceSolicitation32BitUuids, None)
    ServiceSolicitation128BitUuids = property(get_ServiceSolicitation128BitUuids, None)
    ServiceData16BitUuids = property(get_ServiceData16BitUuids, None)
    ServiceData32BitUuids = property(get_ServiceData32BitUuids, None)
    ServiceData128BitUuids = property(get_ServiceData128BitUuids, None)
    PublicTargetAddress = property(get_PublicTargetAddress, None)
    RandomTargetAddress = property(get_RandomTargetAddress, None)
    Appearance = property(get_Appearance, None)
    AdvertisingInterval = property(get_AdvertisingInterval, None)
    ManufacturerSpecificData = property(get_ManufacturerSpecificData, None)
class BluetoothLEAdvertisementFilter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter: ...
    @winrt_mixinmethod
    def get_Advertisement(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementFilter) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    @winrt_mixinmethod
    def put_Advertisement(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementFilter, value: Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement) -> Void: ...
    @winrt_mixinmethod
    def get_BytePatterns(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementFilter) -> Windows.Foundation.Collections.IVector[Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementBytePattern]: ...
    Advertisement = property(get_Advertisement, put_Advertisement)
    BytePatterns = property(get_BytePatterns, None)
BluetoothLEAdvertisementFlags = UInt32
BluetoothLEAdvertisementFlags_None: BluetoothLEAdvertisementFlags = 0
BluetoothLEAdvertisementFlags_LimitedDiscoverableMode: BluetoothLEAdvertisementFlags = 1
BluetoothLEAdvertisementFlags_GeneralDiscoverableMode: BluetoothLEAdvertisementFlags = 2
BluetoothLEAdvertisementFlags_ClassicNotSupported: BluetoothLEAdvertisementFlags = 4
BluetoothLEAdvertisementFlags_DualModeControllerCapable: BluetoothLEAdvertisementFlags = 8
BluetoothLEAdvertisementFlags_DualModeHostCapable: BluetoothLEAdvertisementFlags = 16
class BluetoothLEAdvertisementPublisher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisher'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisher: ...
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisherFactory, advertisement: Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisher: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatus: ...
    @winrt_mixinmethod
    def get_Advertisement(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher) -> Void: ...
    @winrt_mixinmethod
    def add_StatusChanged(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisher, Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatusChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusChanged(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_PreferredTransmitPowerLevelInDBm(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher2) -> Windows.Foundation.IReference[Int16]: ...
    @winrt_mixinmethod
    def put_PreferredTransmitPowerLevelInDBm(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher2, value: Windows.Foundation.IReference[Int16]) -> Void: ...
    @winrt_mixinmethod
    def get_UseExtendedAdvertisement(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher2) -> Boolean: ...
    @winrt_mixinmethod
    def put_UseExtendedAdvertisement(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsAnonymous(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAnonymous(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeTransmitPowerLevel(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeTransmitPowerLevel(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher2, value: Boolean) -> Void: ...
    Status = property(get_Status, None)
    Advertisement = property(get_Advertisement, None)
    PreferredTransmitPowerLevelInDBm = property(get_PreferredTransmitPowerLevelInDBm, put_PreferredTransmitPowerLevelInDBm)
    UseExtendedAdvertisement = property(get_UseExtendedAdvertisement, put_UseExtendedAdvertisement)
    IsAnonymous = property(get_IsAnonymous, put_IsAnonymous)
    IncludeTransmitPowerLevel = property(get_IncludeTransmitPowerLevel, put_IncludeTransmitPowerLevel)
BluetoothLEAdvertisementPublisherStatus = Int32
BluetoothLEAdvertisementPublisherStatus_Created: BluetoothLEAdvertisementPublisherStatus = 0
BluetoothLEAdvertisementPublisherStatus_Waiting: BluetoothLEAdvertisementPublisherStatus = 1
BluetoothLEAdvertisementPublisherStatus_Started: BluetoothLEAdvertisementPublisherStatus = 2
BluetoothLEAdvertisementPublisherStatus_Stopping: BluetoothLEAdvertisementPublisherStatus = 3
BluetoothLEAdvertisementPublisherStatus_Stopped: BluetoothLEAdvertisementPublisherStatus = 4
BluetoothLEAdvertisementPublisherStatus_Aborted: BluetoothLEAdvertisementPublisherStatus = 5
class BluetoothLEAdvertisementPublisherStatusChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatusChangedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisherStatusChangedEventArgs) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatus: ...
    @winrt_mixinmethod
    def get_Error(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisherStatusChangedEventArgs) -> Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_mixinmethod
    def get_SelectedTransmitPowerLevelInDBm(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisherStatusChangedEventArgs2) -> Windows.Foundation.IReference[Int16]: ...
    Status = property(get_Status, None)
    Error = property(get_Error, None)
    SelectedTransmitPowerLevelInDBm = property(get_SelectedTransmitPowerLevelInDBm, None)
class BluetoothLEAdvertisementReceivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementReceivedEventArgs'
    @winrt_mixinmethod
    def get_RawSignalStrengthInDBm(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs) -> Int16: ...
    @winrt_mixinmethod
    def get_BluetoothAddress(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs) -> UInt64: ...
    @winrt_mixinmethod
    def get_AdvertisementType(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementType: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Advertisement(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    @winrt_mixinmethod
    def get_BluetoothAddressType(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs2) -> Windows.Devices.Bluetooth.BluetoothAddressType: ...
    @winrt_mixinmethod
    def get_TransmitPowerLevelInDBm(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs2) -> Windows.Foundation.IReference[Int16]: ...
    @winrt_mixinmethod
    def get_IsAnonymous(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsConnectable(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsScannable(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDirected(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsScanResponse(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs2) -> Boolean: ...
    RawSignalStrengthInDBm = property(get_RawSignalStrengthInDBm, None)
    BluetoothAddress = property(get_BluetoothAddress, None)
    AdvertisementType = property(get_AdvertisementType, None)
    Timestamp = property(get_Timestamp, None)
    Advertisement = property(get_Advertisement, None)
    BluetoothAddressType = property(get_BluetoothAddressType, None)
    TransmitPowerLevelInDBm = property(get_TransmitPowerLevelInDBm, None)
    IsAnonymous = property(get_IsAnonymous, None)
    IsConnectable = property(get_IsConnectable, None)
    IsScannable = property(get_IsScannable, None)
    IsDirected = property(get_IsDirected, None)
    IsScanResponse = property(get_IsScanResponse, None)
BluetoothLEAdvertisementType = Int32
BluetoothLEAdvertisementType_ConnectableUndirected: BluetoothLEAdvertisementType = 0
BluetoothLEAdvertisementType_ConnectableDirected: BluetoothLEAdvertisementType = 1
BluetoothLEAdvertisementType_ScannableUndirected: BluetoothLEAdvertisementType = 2
BluetoothLEAdvertisementType_NonConnectableUndirected: BluetoothLEAdvertisementType = 3
BluetoothLEAdvertisementType_ScanResponse: BluetoothLEAdvertisementType = 4
BluetoothLEAdvertisementType_Extended: BluetoothLEAdvertisementType = 5
class BluetoothLEAdvertisementWatcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcher'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcher: ...
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcherFactory, advertisementFilter: Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcher: ...
    @winrt_mixinmethod
    def get_MinSamplingInterval(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MaxSamplingInterval(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MinOutOfRangeTimeout(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MaxOutOfRangeTimeout(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcherStatus: ...
    @winrt_mixinmethod
    def get_ScanningMode(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEScanningMode: ...
    @winrt_mixinmethod
    def put_ScanningMode(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher, value: Windows.Devices.Bluetooth.Advertisement.BluetoothLEScanningMode) -> Void: ...
    @winrt_mixinmethod
    def get_SignalStrengthFilter(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter: ...
    @winrt_mixinmethod
    def put_SignalStrengthFilter(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher, value: Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter) -> Void: ...
    @winrt_mixinmethod
    def get_AdvertisementFilter(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter: ...
    @winrt_mixinmethod
    def put_AdvertisementFilter(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher, value: Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> Void: ...
    @winrt_mixinmethod
    def add_Received(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcher, Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Received(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcher, Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcherStoppedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AllowExtendedAdvertisements(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher2) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowExtendedAdvertisements(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher2, value: Boolean) -> Void: ...
    MinSamplingInterval = property(get_MinSamplingInterval, None)
    MaxSamplingInterval = property(get_MaxSamplingInterval, None)
    MinOutOfRangeTimeout = property(get_MinOutOfRangeTimeout, None)
    MaxOutOfRangeTimeout = property(get_MaxOutOfRangeTimeout, None)
    Status = property(get_Status, None)
    ScanningMode = property(get_ScanningMode, put_ScanningMode)
    SignalStrengthFilter = property(get_SignalStrengthFilter, put_SignalStrengthFilter)
    AdvertisementFilter = property(get_AdvertisementFilter, put_AdvertisementFilter)
    AllowExtendedAdvertisements = property(get_AllowExtendedAdvertisements, put_AllowExtendedAdvertisements)
BluetoothLEAdvertisementWatcherStatus = Int32
BluetoothLEAdvertisementWatcherStatus_Created: BluetoothLEAdvertisementWatcherStatus = 0
BluetoothLEAdvertisementWatcherStatus_Started: BluetoothLEAdvertisementWatcherStatus = 1
BluetoothLEAdvertisementWatcherStatus_Stopping: BluetoothLEAdvertisementWatcherStatus = 2
BluetoothLEAdvertisementWatcherStatus_Stopped: BluetoothLEAdvertisementWatcherStatus = 3
BluetoothLEAdvertisementWatcherStatus_Aborted: BluetoothLEAdvertisementWatcherStatus = 4
class BluetoothLEAdvertisementWatcherStoppedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcherStoppedEventArgs'
    @winrt_mixinmethod
    def get_Error(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcherStoppedEventArgs) -> Windows.Devices.Bluetooth.BluetoothError: ...
    Error = property(get_Error, None)
class BluetoothLEManufacturerData(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEManufacturerData'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEManufacturerData: ...
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEManufacturerDataFactory, companyId: UInt16, data: Windows.Storage.Streams.IBuffer) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEManufacturerData: ...
    @winrt_mixinmethod
    def get_CompanyId(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEManufacturerData) -> UInt16: ...
    @winrt_mixinmethod
    def put_CompanyId(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEManufacturerData, value: UInt16) -> Void: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEManufacturerData) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_Data(self: Windows.Devices.Bluetooth.Advertisement.IBluetoothLEManufacturerData, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    CompanyId = property(get_CompanyId, put_CompanyId)
    Data = property(get_Data, put_Data)
BluetoothLEScanningMode = Int32
BluetoothLEScanningMode_Passive: BluetoothLEScanningMode = 0
BluetoothLEScanningMode_Active: BluetoothLEScanningMode = 1
BluetoothLEScanningMode_None: BluetoothLEScanningMode = 2
class IBluetoothLEAdvertisement(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('066fb2b7-33d1-4e7d-83-67-cf-81-d0-f7-96-53')
    @winrt_commethod(6)
    def get_Flags(self) -> Windows.Foundation.IReference[Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFlags]: ...
    @winrt_commethod(7)
    def put_Flags(self, value: Windows.Foundation.IReference[Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFlags]) -> Void: ...
    @winrt_commethod(8)
    def get_LocalName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_LocalName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_ServiceUuids(self) -> Windows.Foundation.Collections.IVector[Guid]: ...
    @winrt_commethod(11)
    def get_ManufacturerData(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.Bluetooth.Advertisement.BluetoothLEManufacturerData]: ...
    @winrt_commethod(12)
    def get_DataSections(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataSection]: ...
    @winrt_commethod(13)
    def GetManufacturerDataByCompanyId(self, companyId: UInt16) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.Advertisement.BluetoothLEManufacturerData]: ...
    @winrt_commethod(14)
    def GetSectionsByType(self, type: Byte) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataSection]: ...
    Flags = property(get_Flags, put_Flags)
    LocalName = property(get_LocalName, put_LocalName)
    ServiceUuids = property(get_ServiceUuids, None)
    ManufacturerData = property(get_ManufacturerData, None)
    DataSections = property(get_DataSections, None)
class IBluetoothLEAdvertisementBytePattern(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fbfad7f2-b9c5-4a08-bc-51-50-2f-8e-f6-8a-79')
    @winrt_commethod(6)
    def get_DataType(self) -> Byte: ...
    @winrt_commethod(7)
    def put_DataType(self, value: Byte) -> Void: ...
    @winrt_commethod(8)
    def get_Offset(self) -> Int16: ...
    @winrt_commethod(9)
    def put_Offset(self, value: Int16) -> Void: ...
    @winrt_commethod(10)
    def get_Data(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(11)
    def put_Data(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    DataType = property(get_DataType, put_DataType)
    Offset = property(get_Offset, put_Offset)
    Data = property(get_Data, put_Data)
class IBluetoothLEAdvertisementBytePatternFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c2e24d73-fd5c-4ec3-be-2a-9c-a6-fa-11-b7-bd')
    @winrt_commethod(6)
    def Create(self, dataType: Byte, offset: Int16, data: Windows.Storage.Streams.IBuffer) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementBytePattern: ...
class IBluetoothLEAdvertisementDataSection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d7213314-3a43-40f9-b6-f0-92-bf-ef-c3-4a-e3')
    @winrt_commethod(6)
    def get_DataType(self) -> Byte: ...
    @winrt_commethod(7)
    def put_DataType(self, value: Byte) -> Void: ...
    @winrt_commethod(8)
    def get_Data(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def put_Data(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    DataType = property(get_DataType, put_DataType)
    Data = property(get_Data, put_Data)
class IBluetoothLEAdvertisementDataSectionFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e7a40942-a845-4045-bf-7e-3e-99-71-db-8a-6b')
    @winrt_commethod(6)
    def Create(self, dataType: Byte, data: Windows.Storage.Streams.IBuffer) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataSection: ...
class IBluetoothLEAdvertisementDataTypesStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3bb6472f-0606-434b-a7-6e-74-15-9f-06-84-d3')
    @winrt_commethod(6)
    def get_Flags(self) -> Byte: ...
    @winrt_commethod(7)
    def get_IncompleteService16BitUuids(self) -> Byte: ...
    @winrt_commethod(8)
    def get_CompleteService16BitUuids(self) -> Byte: ...
    @winrt_commethod(9)
    def get_IncompleteService32BitUuids(self) -> Byte: ...
    @winrt_commethod(10)
    def get_CompleteService32BitUuids(self) -> Byte: ...
    @winrt_commethod(11)
    def get_IncompleteService128BitUuids(self) -> Byte: ...
    @winrt_commethod(12)
    def get_CompleteService128BitUuids(self) -> Byte: ...
    @winrt_commethod(13)
    def get_ShortenedLocalName(self) -> Byte: ...
    @winrt_commethod(14)
    def get_CompleteLocalName(self) -> Byte: ...
    @winrt_commethod(15)
    def get_TxPowerLevel(self) -> Byte: ...
    @winrt_commethod(16)
    def get_PeripheralConnectionIntervalRange(self) -> Byte: ...
    @winrt_commethod(17)
    def get_ServiceSolicitation16BitUuids(self) -> Byte: ...
    @winrt_commethod(18)
    def get_ServiceSolicitation32BitUuids(self) -> Byte: ...
    @winrt_commethod(19)
    def get_ServiceSolicitation128BitUuids(self) -> Byte: ...
    @winrt_commethod(20)
    def get_ServiceData16BitUuids(self) -> Byte: ...
    @winrt_commethod(21)
    def get_ServiceData32BitUuids(self) -> Byte: ...
    @winrt_commethod(22)
    def get_ServiceData128BitUuids(self) -> Byte: ...
    @winrt_commethod(23)
    def get_PublicTargetAddress(self) -> Byte: ...
    @winrt_commethod(24)
    def get_RandomTargetAddress(self) -> Byte: ...
    @winrt_commethod(25)
    def get_Appearance(self) -> Byte: ...
    @winrt_commethod(26)
    def get_AdvertisingInterval(self) -> Byte: ...
    @winrt_commethod(27)
    def get_ManufacturerSpecificData(self) -> Byte: ...
    Flags = property(get_Flags, None)
    IncompleteService16BitUuids = property(get_IncompleteService16BitUuids, None)
    CompleteService16BitUuids = property(get_CompleteService16BitUuids, None)
    IncompleteService32BitUuids = property(get_IncompleteService32BitUuids, None)
    CompleteService32BitUuids = property(get_CompleteService32BitUuids, None)
    IncompleteService128BitUuids = property(get_IncompleteService128BitUuids, None)
    CompleteService128BitUuids = property(get_CompleteService128BitUuids, None)
    ShortenedLocalName = property(get_ShortenedLocalName, None)
    CompleteLocalName = property(get_CompleteLocalName, None)
    TxPowerLevel = property(get_TxPowerLevel, None)
    PeripheralConnectionIntervalRange = property(get_PeripheralConnectionIntervalRange, None)
    ServiceSolicitation16BitUuids = property(get_ServiceSolicitation16BitUuids, None)
    ServiceSolicitation32BitUuids = property(get_ServiceSolicitation32BitUuids, None)
    ServiceSolicitation128BitUuids = property(get_ServiceSolicitation128BitUuids, None)
    ServiceData16BitUuids = property(get_ServiceData16BitUuids, None)
    ServiceData32BitUuids = property(get_ServiceData32BitUuids, None)
    ServiceData128BitUuids = property(get_ServiceData128BitUuids, None)
    PublicTargetAddress = property(get_PublicTargetAddress, None)
    RandomTargetAddress = property(get_RandomTargetAddress, None)
    Appearance = property(get_Appearance, None)
    AdvertisingInterval = property(get_AdvertisingInterval, None)
    ManufacturerSpecificData = property(get_ManufacturerSpecificData, None)
class IBluetoothLEAdvertisementFilter(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('131eb0d3-d04e-47b1-83-7e-49-40-5b-f6-f8-0f')
    @winrt_commethod(6)
    def get_Advertisement(self) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    @winrt_commethod(7)
    def put_Advertisement(self, value: Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement) -> Void: ...
    @winrt_commethod(8)
    def get_BytePatterns(self) -> Windows.Foundation.Collections.IVector[Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementBytePattern]: ...
    Advertisement = property(get_Advertisement, put_Advertisement)
    BytePatterns = property(get_BytePatterns, None)
class IBluetoothLEAdvertisementPublisher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cde820f9-d9fa-43d6-a2-64-dd-d8-b7-da-8b-78')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatus: ...
    @winrt_commethod(7)
    def get_Advertisement(self) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    @winrt_commethod(8)
    def Start(self) -> Void: ...
    @winrt_commethod(9)
    def Stop(self) -> Void: ...
    @winrt_commethod(10)
    def add_StatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisher, Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatusChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_StatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Status = property(get_Status, None)
    Advertisement = property(get_Advertisement, None)
class IBluetoothLEAdvertisementPublisher2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fbdb545e-56f1-510f-a4-34-21-7f-bd-9e-7b-d2')
    @winrt_commethod(6)
    def get_PreferredTransmitPowerLevelInDBm(self) -> Windows.Foundation.IReference[Int16]: ...
    @winrt_commethod(7)
    def put_PreferredTransmitPowerLevelInDBm(self, value: Windows.Foundation.IReference[Int16]) -> Void: ...
    @winrt_commethod(8)
    def get_UseExtendedAdvertisement(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_UseExtendedAdvertisement(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_IsAnonymous(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsAnonymous(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IncludeTransmitPowerLevel(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IncludeTransmitPowerLevel(self, value: Boolean) -> Void: ...
    PreferredTransmitPowerLevelInDBm = property(get_PreferredTransmitPowerLevelInDBm, put_PreferredTransmitPowerLevelInDBm)
    UseExtendedAdvertisement = property(get_UseExtendedAdvertisement, put_UseExtendedAdvertisement)
    IsAnonymous = property(get_IsAnonymous, put_IsAnonymous)
    IncludeTransmitPowerLevel = property(get_IncludeTransmitPowerLevel, put_IncludeTransmitPowerLevel)
class IBluetoothLEAdvertisementPublisherFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5c5f065e-b863-4981-a1-af-1c-54-4d-8b-0c-0d')
    @winrt_commethod(6)
    def Create(self, advertisement: Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisher: ...
class IBluetoothLEAdvertisementPublisherStatusChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('09c2bd9f-2dff-4b23-86-ee-0d-14-fb-94-ae-ae')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatus: ...
    @winrt_commethod(7)
    def get_Error(self) -> Windows.Devices.Bluetooth.BluetoothError: ...
    Status = property(get_Status, None)
    Error = property(get_Error, None)
class IBluetoothLEAdvertisementPublisherStatusChangedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8f62790e-dc88-5c8b-b3-4e-10-b3-21-85-0f-88')
    @winrt_commethod(6)
    def get_SelectedTransmitPowerLevelInDBm(self) -> Windows.Foundation.IReference[Int16]: ...
    SelectedTransmitPowerLevelInDBm = property(get_SelectedTransmitPowerLevelInDBm, None)
class IBluetoothLEAdvertisementReceivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('27987ddf-e596-41be-8d-43-9e-67-31-d4-a9-13')
    @winrt_commethod(6)
    def get_RawSignalStrengthInDBm(self) -> Int16: ...
    @winrt_commethod(7)
    def get_BluetoothAddress(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_AdvertisementType(self) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementType: ...
    @winrt_commethod(9)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def get_Advertisement(self) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    RawSignalStrengthInDBm = property(get_RawSignalStrengthInDBm, None)
    BluetoothAddress = property(get_BluetoothAddress, None)
    AdvertisementType = property(get_AdvertisementType, None)
    Timestamp = property(get_Timestamp, None)
    Advertisement = property(get_Advertisement, None)
class IBluetoothLEAdvertisementReceivedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('12d9c87b-0399-5f0e-a3-48-53-b0-2b-6b-16-2e')
    @winrt_commethod(6)
    def get_BluetoothAddressType(self) -> Windows.Devices.Bluetooth.BluetoothAddressType: ...
    @winrt_commethod(7)
    def get_TransmitPowerLevelInDBm(self) -> Windows.Foundation.IReference[Int16]: ...
    @winrt_commethod(8)
    def get_IsAnonymous(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsConnectable(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsScannable(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsDirected(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsScanResponse(self) -> Boolean: ...
    BluetoothAddressType = property(get_BluetoothAddressType, None)
    TransmitPowerLevelInDBm = property(get_TransmitPowerLevelInDBm, None)
    IsAnonymous = property(get_IsAnonymous, None)
    IsConnectable = property(get_IsConnectable, None)
    IsScannable = property(get_IsScannable, None)
    IsDirected = property(get_IsDirected, None)
    IsScanResponse = property(get_IsScanResponse, None)
class IBluetoothLEAdvertisementWatcher(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a6ac336f-f3d3-4297-8d-6c-c8-1e-a6-62-3f-40')
    @winrt_commethod(6)
    def get_MinSamplingInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_MaxSamplingInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_MinOutOfRangeTimeout(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_MaxOutOfRangeTimeout(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_Status(self) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcherStatus: ...
    @winrt_commethod(11)
    def get_ScanningMode(self) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEScanningMode: ...
    @winrt_commethod(12)
    def put_ScanningMode(self, value: Windows.Devices.Bluetooth.Advertisement.BluetoothLEScanningMode) -> Void: ...
    @winrt_commethod(13)
    def get_SignalStrengthFilter(self) -> Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter: ...
    @winrt_commethod(14)
    def put_SignalStrengthFilter(self, value: Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter) -> Void: ...
    @winrt_commethod(15)
    def get_AdvertisementFilter(self) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter: ...
    @winrt_commethod(16)
    def put_AdvertisementFilter(self, value: Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter) -> Void: ...
    @winrt_commethod(17)
    def Start(self) -> Void: ...
    @winrt_commethod(18)
    def Stop(self) -> Void: ...
    @winrt_commethod(19)
    def add_Received(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcher, Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_Received(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_Stopped(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcher, Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcherStoppedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_Stopped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    MinSamplingInterval = property(get_MinSamplingInterval, None)
    MaxSamplingInterval = property(get_MaxSamplingInterval, None)
    MinOutOfRangeTimeout = property(get_MinOutOfRangeTimeout, None)
    MaxOutOfRangeTimeout = property(get_MaxOutOfRangeTimeout, None)
    Status = property(get_Status, None)
    ScanningMode = property(get_ScanningMode, put_ScanningMode)
    SignalStrengthFilter = property(get_SignalStrengthFilter, put_SignalStrengthFilter)
    AdvertisementFilter = property(get_AdvertisementFilter, put_AdvertisementFilter)
class IBluetoothLEAdvertisementWatcher2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('01bf26bc-b164-5805-90-a3-e8-a7-99-7f-f2-25')
    @winrt_commethod(6)
    def get_AllowExtendedAdvertisements(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowExtendedAdvertisements(self, value: Boolean) -> Void: ...
    AllowExtendedAdvertisements = property(get_AllowExtendedAdvertisements, put_AllowExtendedAdvertisements)
class IBluetoothLEAdvertisementWatcherFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9aaf2d56-39ac-453e-b3-2a-85-c6-57-e0-17-f1')
    @winrt_commethod(6)
    def Create(self, advertisementFilter: Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcher: ...
class IBluetoothLEAdvertisementWatcherStoppedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('dd40f84d-e7b9-43e3-9c-04-06-85-d0-85-fd-8c')
    @winrt_commethod(6)
    def get_Error(self) -> Windows.Devices.Bluetooth.BluetoothError: ...
    Error = property(get_Error, None)
class IBluetoothLEManufacturerData(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('912dba18-6963-4533-b0-61-46-94-da-fb-34-e5')
    @winrt_commethod(6)
    def get_CompanyId(self) -> UInt16: ...
    @winrt_commethod(7)
    def put_CompanyId(self, value: UInt16) -> Void: ...
    @winrt_commethod(8)
    def get_Data(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def put_Data(self, value: Windows.Storage.Streams.IBuffer) -> Void: ...
    CompanyId = property(get_CompanyId, put_CompanyId)
    Data = property(get_Data, put_Data)
class IBluetoothLEManufacturerDataFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c09b39f8-319a-441e-8d-e5-66-a8-1e-87-7a-6c')
    @winrt_commethod(6)
    def Create(self, companyId: UInt16, data: Windows.Storage.Streams.IBuffer) -> Windows.Devices.Bluetooth.Advertisement.BluetoothLEManufacturerData: ...
make_head(_module, 'BluetoothLEAdvertisement')
make_head(_module, 'BluetoothLEAdvertisementBytePattern')
make_head(_module, 'BluetoothLEAdvertisementDataSection')
make_head(_module, 'BluetoothLEAdvertisementDataTypes')
make_head(_module, 'BluetoothLEAdvertisementFilter')
make_head(_module, 'BluetoothLEAdvertisementPublisher')
make_head(_module, 'BluetoothLEAdvertisementPublisherStatusChangedEventArgs')
make_head(_module, 'BluetoothLEAdvertisementReceivedEventArgs')
make_head(_module, 'BluetoothLEAdvertisementWatcher')
make_head(_module, 'BluetoothLEAdvertisementWatcherStoppedEventArgs')
make_head(_module, 'BluetoothLEManufacturerData')
make_head(_module, 'IBluetoothLEAdvertisement')
make_head(_module, 'IBluetoothLEAdvertisementBytePattern')
make_head(_module, 'IBluetoothLEAdvertisementBytePatternFactory')
make_head(_module, 'IBluetoothLEAdvertisementDataSection')
make_head(_module, 'IBluetoothLEAdvertisementDataSectionFactory')
make_head(_module, 'IBluetoothLEAdvertisementDataTypesStatics')
make_head(_module, 'IBluetoothLEAdvertisementFilter')
make_head(_module, 'IBluetoothLEAdvertisementPublisher')
make_head(_module, 'IBluetoothLEAdvertisementPublisher2')
make_head(_module, 'IBluetoothLEAdvertisementPublisherFactory')
make_head(_module, 'IBluetoothLEAdvertisementPublisherStatusChangedEventArgs')
make_head(_module, 'IBluetoothLEAdvertisementPublisherStatusChangedEventArgs2')
make_head(_module, 'IBluetoothLEAdvertisementReceivedEventArgs')
make_head(_module, 'IBluetoothLEAdvertisementReceivedEventArgs2')
make_head(_module, 'IBluetoothLEAdvertisementWatcher')
make_head(_module, 'IBluetoothLEAdvertisementWatcher2')
make_head(_module, 'IBluetoothLEAdvertisementWatcherFactory')
make_head(_module, 'IBluetoothLEAdvertisementWatcherStoppedEventArgs')
make_head(_module, 'IBluetoothLEManufacturerData')
make_head(_module, 'IBluetoothLEManufacturerDataFactory')
