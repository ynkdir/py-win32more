from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Bluetooth
import win32more.Windows.Devices.Bluetooth.Advertisement
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class BluetoothLEAdvertisement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    @winrt_mixinmethod
    def get_Flags(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement) -> win32more.Windows.Foundation.IReference[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFlags]: ...
    @winrt_mixinmethod
    def put_Flags(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement, value: win32more.Windows.Foundation.IReference[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFlags]) -> Void: ...
    @winrt_mixinmethod
    def get_LocalName(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_LocalName(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ServiceUuids(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement) -> win32more.Windows.Foundation.Collections.IVector[Guid]: ...
    @winrt_mixinmethod
    def get_ManufacturerData(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEManufacturerData]: ...
    @winrt_mixinmethod
    def get_DataSections(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataSection]: ...
    @winrt_mixinmethod
    def GetManufacturerDataByCompanyId(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement, companyId: UInt16) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEManufacturerData]: ...
    @winrt_mixinmethod
    def GetSectionsByType(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement, type: Byte) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataSection]: ...
    DataSections = property(get_DataSections, None)
    Flags = property(get_Flags, put_Flags)
    LocalName = property(get_LocalName, put_LocalName)
    ManufacturerData = property(get_ManufacturerData, None)
    ServiceUuids = property(get_ServiceUuids, None)
class BluetoothLEAdvertisementBytePattern(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementBytePattern
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementBytePattern'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementBytePattern.CreateInstance(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementBytePattern.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementBytePattern: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementBytePatternFactory, dataType: Byte, offset: Int16, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementBytePattern: ...
    @winrt_mixinmethod
    def get_DataType(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementBytePattern) -> Byte: ...
    @winrt_mixinmethod
    def put_DataType(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementBytePattern, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementBytePattern) -> Int16: ...
    @winrt_mixinmethod
    def put_Offset(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementBytePattern, value: Int16) -> Void: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementBytePattern) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_Data(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementBytePattern, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    Data = property(get_Data, put_Data)
    DataType = property(get_DataType, put_DataType)
    Offset = property(get_Offset, put_Offset)
class BluetoothLEAdvertisementDataSection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataSection
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataSection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataSection.CreateInstance(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataSection.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataSection: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataSectionFactory, dataType: Byte, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataSection: ...
    @winrt_mixinmethod
    def get_DataType(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataSection) -> Byte: ...
    @winrt_mixinmethod
    def put_DataType(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataSection, value: Byte) -> Void: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataSection) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_Data(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataSection, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    Data = property(get_Data, put_Data)
    DataType = property(get_DataType, put_DataType)
class _BluetoothLEAdvertisementDataTypes_Meta_(ComPtr.__class__):
    pass
class BluetoothLEAdvertisementDataTypes(ComPtr, metaclass=_BluetoothLEAdvertisementDataTypes_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataTypes'
    @winrt_classmethod
    def get_Flags(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_IncompleteService16BitUuids(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_CompleteService16BitUuids(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_IncompleteService32BitUuids(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_CompleteService32BitUuids(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_IncompleteService128BitUuids(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_CompleteService128BitUuids(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_ShortenedLocalName(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_CompleteLocalName(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_TxPowerLevel(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_PeripheralConnectionIntervalRange(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_ServiceSolicitation16BitUuids(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_ServiceSolicitation32BitUuids(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_ServiceSolicitation128BitUuids(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_ServiceData16BitUuids(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_ServiceData32BitUuids(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_ServiceData128BitUuids(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_PublicTargetAddress(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_RandomTargetAddress(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_Appearance(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_AdvertisingInterval(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    @winrt_classmethod
    def get_ManufacturerSpecificData(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics) -> Byte: ...
    _BluetoothLEAdvertisementDataTypes_Meta_.AdvertisingInterval = property(get_AdvertisingInterval, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.Appearance = property(get_Appearance, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.CompleteLocalName = property(get_CompleteLocalName, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.CompleteService128BitUuids = property(get_CompleteService128BitUuids, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.CompleteService16BitUuids = property(get_CompleteService16BitUuids, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.CompleteService32BitUuids = property(get_CompleteService32BitUuids, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.Flags = property(get_Flags, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.IncompleteService128BitUuids = property(get_IncompleteService128BitUuids, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.IncompleteService16BitUuids = property(get_IncompleteService16BitUuids, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.IncompleteService32BitUuids = property(get_IncompleteService32BitUuids, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.ManufacturerSpecificData = property(get_ManufacturerSpecificData, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.PeripheralConnectionIntervalRange = property(get_PeripheralConnectionIntervalRange, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.PublicTargetAddress = property(get_PublicTargetAddress, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.RandomTargetAddress = property(get_RandomTargetAddress, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.ServiceData128BitUuids = property(get_ServiceData128BitUuids, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.ServiceData16BitUuids = property(get_ServiceData16BitUuids, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.ServiceData32BitUuids = property(get_ServiceData32BitUuids, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.ServiceSolicitation128BitUuids = property(get_ServiceSolicitation128BitUuids, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.ServiceSolicitation16BitUuids = property(get_ServiceSolicitation16BitUuids, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.ServiceSolicitation32BitUuids = property(get_ServiceSolicitation32BitUuids, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.ShortenedLocalName = property(get_ShortenedLocalName, None)
    _BluetoothLEAdvertisementDataTypes_Meta_.TxPowerLevel = property(get_TxPowerLevel, None)
class BluetoothLEAdvertisementFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementFilter
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter: ...
    @winrt_mixinmethod
    def get_Advertisement(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementFilter) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    @winrt_mixinmethod
    def put_Advertisement(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementFilter, value: win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement) -> Void: ...
    @winrt_mixinmethod
    def get_BytePatterns(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementFilter) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementBytePattern]: ...
    Advertisement = property(get_Advertisement, put_Advertisement)
    BytePatterns = property(get_BytePatterns, None)
class BluetoothLEAdvertisementFlags(Enum, UInt32):
    None_ = 0
    LimitedDiscoverableMode = 1
    GeneralDiscoverableMode = 2
    ClassicNotSupported = 4
    DualModeControllerCapable = 8
    DualModeHostCapable = 16
class BluetoothLEAdvertisementPublisher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisher'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisher.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisher.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisher: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisherFactory, advertisement: win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisher: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatus: ...
    @winrt_mixinmethod
    def get_Advertisement(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher) -> Void: ...
    @winrt_mixinmethod
    def add_StatusChanged(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisher, win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusChanged(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_PreferredTransmitPowerLevelInDBm(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher2) -> win32more.Windows.Foundation.IReference[Int16]: ...
    @winrt_mixinmethod
    def put_PreferredTransmitPowerLevelInDBm(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher2, value: win32more.Windows.Foundation.IReference[Int16]) -> Void: ...
    @winrt_mixinmethod
    def get_UseExtendedAdvertisement(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher2) -> Boolean: ...
    @winrt_mixinmethod
    def put_UseExtendedAdvertisement(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsAnonymous(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAnonymous(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IncludeTransmitPowerLevel(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IncludeTransmitPowerLevel(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher2, value: Boolean) -> Void: ...
    Advertisement = property(get_Advertisement, None)
    IncludeTransmitPowerLevel = property(get_IncludeTransmitPowerLevel, put_IncludeTransmitPowerLevel)
    IsAnonymous = property(get_IsAnonymous, put_IsAnonymous)
    PreferredTransmitPowerLevelInDBm = property(get_PreferredTransmitPowerLevelInDBm, put_PreferredTransmitPowerLevelInDBm)
    Status = property(get_Status, None)
    UseExtendedAdvertisement = property(get_UseExtendedAdvertisement, put_UseExtendedAdvertisement)
    StatusChanged = event()
class BluetoothLEAdvertisementPublisherStatus(Enum, Int32):
    Created = 0
    Waiting = 1
    Started = 2
    Stopping = 3
    Stopped = 4
    Aborted = 5
class BluetoothLEAdvertisementPublisherStatusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisherStatusChangedEventArgs
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatusChangedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisherStatusChangedEventArgs) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatus: ...
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisherStatusChangedEventArgs) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    @winrt_mixinmethod
    def get_SelectedTransmitPowerLevelInDBm(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisherStatusChangedEventArgs2) -> win32more.Windows.Foundation.IReference[Int16]: ...
    Error = property(get_Error, None)
    SelectedTransmitPowerLevelInDBm = property(get_SelectedTransmitPowerLevelInDBm, None)
    Status = property(get_Status, None)
class BluetoothLEAdvertisementReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementReceivedEventArgs'
    @winrt_mixinmethod
    def get_RawSignalStrengthInDBm(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs) -> Int16: ...
    @winrt_mixinmethod
    def get_BluetoothAddress(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs) -> UInt64: ...
    @winrt_mixinmethod
    def get_AdvertisementType(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementType: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Advertisement(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    @winrt_mixinmethod
    def get_BluetoothAddressType(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs2) -> win32more.Windows.Devices.Bluetooth.BluetoothAddressType: ...
    @winrt_mixinmethod
    def get_TransmitPowerLevelInDBm(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs2) -> win32more.Windows.Foundation.IReference[Int16]: ...
    @winrt_mixinmethod
    def get_IsAnonymous(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsConnectable(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsScannable(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDirected(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsScanResponse(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs2) -> Boolean: ...
    Advertisement = property(get_Advertisement, None)
    AdvertisementType = property(get_AdvertisementType, None)
    BluetoothAddress = property(get_BluetoothAddress, None)
    BluetoothAddressType = property(get_BluetoothAddressType, None)
    IsAnonymous = property(get_IsAnonymous, None)
    IsConnectable = property(get_IsConnectable, None)
    IsDirected = property(get_IsDirected, None)
    IsScanResponse = property(get_IsScanResponse, None)
    IsScannable = property(get_IsScannable, None)
    RawSignalStrengthInDBm = property(get_RawSignalStrengthInDBm, None)
    Timestamp = property(get_Timestamp, None)
    TransmitPowerLevelInDBm = property(get_TransmitPowerLevelInDBm, None)
class BluetoothLEAdvertisementType(Enum, Int32):
    ConnectableUndirected = 0
    ConnectableDirected = 1
    ScannableUndirected = 2
    NonConnectableUndirected = 3
    ScanResponse = 4
    Extended = 5
class BluetoothLEAdvertisementWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcher'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcher.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcher.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcher: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcherFactory, advertisementFilter: win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcher: ...
    @winrt_mixinmethod
    def get_MinSamplingInterval(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MaxSamplingInterval(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MinOutOfRangeTimeout(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_MaxOutOfRangeTimeout(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcherStatus: ...
    @winrt_mixinmethod
    def get_ScanningMode(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEScanningMode: ...
    @winrt_mixinmethod
    def put_ScanningMode(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher, value: win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEScanningMode) -> Void: ...
    @winrt_mixinmethod
    def get_SignalStrengthFilter(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> win32more.Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter: ...
    @winrt_mixinmethod
    def put_SignalStrengthFilter(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher, value: win32more.Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter) -> Void: ...
    @winrt_mixinmethod
    def get_AdvertisementFilter(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter: ...
    @winrt_mixinmethod
    def put_AdvertisementFilter(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher, value: win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher) -> Void: ...
    @winrt_mixinmethod
    def add_Received(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcher, win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Received(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Stopped(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcher, win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcherStoppedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Stopped(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AllowExtendedAdvertisements(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher2) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowExtendedAdvertisements(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher2, value: Boolean) -> Void: ...
    AdvertisementFilter = property(get_AdvertisementFilter, put_AdvertisementFilter)
    AllowExtendedAdvertisements = property(get_AllowExtendedAdvertisements, put_AllowExtendedAdvertisements)
    MaxOutOfRangeTimeout = property(get_MaxOutOfRangeTimeout, None)
    MaxSamplingInterval = property(get_MaxSamplingInterval, None)
    MinOutOfRangeTimeout = property(get_MinOutOfRangeTimeout, None)
    MinSamplingInterval = property(get_MinSamplingInterval, None)
    ScanningMode = property(get_ScanningMode, put_ScanningMode)
    SignalStrengthFilter = property(get_SignalStrengthFilter, put_SignalStrengthFilter)
    Status = property(get_Status, None)
    Received = event()
    Stopped = event()
class BluetoothLEAdvertisementWatcherStatus(Enum, Int32):
    Created = 0
    Started = 1
    Stopping = 2
    Stopped = 3
    Aborted = 4
class BluetoothLEAdvertisementWatcherStoppedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcherStoppedEventArgs
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcherStoppedEventArgs'
    @winrt_mixinmethod
    def get_Error(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcherStoppedEventArgs) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    Error = property(get_Error, None)
class BluetoothLEManufacturerData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEManufacturerData
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.BluetoothLEManufacturerData'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEManufacturerData.CreateInstance(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEManufacturerData.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEManufacturerData: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEManufacturerDataFactory, companyId: UInt16, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEManufacturerData: ...
    @winrt_mixinmethod
    def get_CompanyId(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEManufacturerData) -> UInt16: ...
    @winrt_mixinmethod
    def put_CompanyId(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEManufacturerData, value: UInt16) -> Void: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEManufacturerData) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def put_Data(self: win32more.Windows.Devices.Bluetooth.Advertisement.IBluetoothLEManufacturerData, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    CompanyId = property(get_CompanyId, put_CompanyId)
    Data = property(get_Data, put_Data)
class BluetoothLEScanningMode(Enum, Int32):
    Passive = 0
    Active = 1
    None_ = 2
class IBluetoothLEAdvertisement(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisement'
    _iid_ = Guid('{066fb2b7-33d1-4e7d-8367-cf81d0f79653}')
    @winrt_commethod(6)
    def get_Flags(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFlags]: ...
    @winrt_commethod(7)
    def put_Flags(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFlags]) -> Void: ...
    @winrt_commethod(8)
    def get_LocalName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_LocalName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_ServiceUuids(self) -> win32more.Windows.Foundation.Collections.IVector[Guid]: ...
    @winrt_commethod(11)
    def get_ManufacturerData(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEManufacturerData]: ...
    @winrt_commethod(12)
    def get_DataSections(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataSection]: ...
    @winrt_commethod(13)
    def GetManufacturerDataByCompanyId(self, companyId: UInt16) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEManufacturerData]: ...
    @winrt_commethod(14)
    def GetSectionsByType(self, type: Byte) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataSection]: ...
    DataSections = property(get_DataSections, None)
    Flags = property(get_Flags, put_Flags)
    LocalName = property(get_LocalName, put_LocalName)
    ManufacturerData = property(get_ManufacturerData, None)
    ServiceUuids = property(get_ServiceUuids, None)
class IBluetoothLEAdvertisementBytePattern(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementBytePattern'
    _iid_ = Guid('{fbfad7f2-b9c5-4a08-bc51-502f8ef68a79}')
    @winrt_commethod(6)
    def get_DataType(self) -> Byte: ...
    @winrt_commethod(7)
    def put_DataType(self, value: Byte) -> Void: ...
    @winrt_commethod(8)
    def get_Offset(self) -> Int16: ...
    @winrt_commethod(9)
    def put_Offset(self, value: Int16) -> Void: ...
    @winrt_commethod(10)
    def get_Data(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(11)
    def put_Data(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    Data = property(get_Data, put_Data)
    DataType = property(get_DataType, put_DataType)
    Offset = property(get_Offset, put_Offset)
class IBluetoothLEAdvertisementBytePatternFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementBytePatternFactory'
    _iid_ = Guid('{c2e24d73-fd5c-4ec3-be2a-9ca6fa11b7bd}')
    @winrt_commethod(6)
    def Create(self, dataType: Byte, offset: Int16, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementBytePattern: ...
class IBluetoothLEAdvertisementDataSection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataSection'
    _iid_ = Guid('{d7213314-3a43-40f9-b6f0-92bfefc34ae3}')
    @winrt_commethod(6)
    def get_DataType(self) -> Byte: ...
    @winrt_commethod(7)
    def put_DataType(self, value: Byte) -> Void: ...
    @winrt_commethod(8)
    def get_Data(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def put_Data(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    Data = property(get_Data, put_Data)
    DataType = property(get_DataType, put_DataType)
class IBluetoothLEAdvertisementDataSectionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataSectionFactory'
    _iid_ = Guid('{e7a40942-a845-4045-bf7e-3e9971db8a6b}')
    @winrt_commethod(6)
    def Create(self, dataType: Byte, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementDataSection: ...
class IBluetoothLEAdvertisementDataTypesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementDataTypesStatics'
    _iid_ = Guid('{3bb6472f-0606-434b-a76e-74159f0684d3}')
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
    AdvertisingInterval = property(get_AdvertisingInterval, None)
    Appearance = property(get_Appearance, None)
    CompleteLocalName = property(get_CompleteLocalName, None)
    CompleteService128BitUuids = property(get_CompleteService128BitUuids, None)
    CompleteService16BitUuids = property(get_CompleteService16BitUuids, None)
    CompleteService32BitUuids = property(get_CompleteService32BitUuids, None)
    Flags = property(get_Flags, None)
    IncompleteService128BitUuids = property(get_IncompleteService128BitUuids, None)
    IncompleteService16BitUuids = property(get_IncompleteService16BitUuids, None)
    IncompleteService32BitUuids = property(get_IncompleteService32BitUuids, None)
    ManufacturerSpecificData = property(get_ManufacturerSpecificData, None)
    PeripheralConnectionIntervalRange = property(get_PeripheralConnectionIntervalRange, None)
    PublicTargetAddress = property(get_PublicTargetAddress, None)
    RandomTargetAddress = property(get_RandomTargetAddress, None)
    ServiceData128BitUuids = property(get_ServiceData128BitUuids, None)
    ServiceData16BitUuids = property(get_ServiceData16BitUuids, None)
    ServiceData32BitUuids = property(get_ServiceData32BitUuids, None)
    ServiceSolicitation128BitUuids = property(get_ServiceSolicitation128BitUuids, None)
    ServiceSolicitation16BitUuids = property(get_ServiceSolicitation16BitUuids, None)
    ServiceSolicitation32BitUuids = property(get_ServiceSolicitation32BitUuids, None)
    ShortenedLocalName = property(get_ShortenedLocalName, None)
    TxPowerLevel = property(get_TxPowerLevel, None)
class IBluetoothLEAdvertisementFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementFilter'
    _iid_ = Guid('{131eb0d3-d04e-47b1-837e-49405bf6f80f}')
    @winrt_commethod(6)
    def get_Advertisement(self) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    @winrt_commethod(7)
    def put_Advertisement(self, value: win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement) -> Void: ...
    @winrt_commethod(8)
    def get_BytePatterns(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementBytePattern]: ...
    Advertisement = property(get_Advertisement, put_Advertisement)
    BytePatterns = property(get_BytePatterns, None)
class IBluetoothLEAdvertisementPublisher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher'
    _iid_ = Guid('{cde820f9-d9fa-43d6-a264-ddd8b7da8b78}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatus: ...
    @winrt_commethod(7)
    def get_Advertisement(self) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    @winrt_commethod(8)
    def Start(self) -> Void: ...
    @winrt_commethod(9)
    def Stop(self) -> Void: ...
    @winrt_commethod(10)
    def add_StatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisher, win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_StatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Advertisement = property(get_Advertisement, None)
    Status = property(get_Status, None)
    StatusChanged = event()
class IBluetoothLEAdvertisementPublisher2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisher2'
    _iid_ = Guid('{fbdb545e-56f1-510f-a434-217fbd9e7bd2}')
    @winrt_commethod(6)
    def get_PreferredTransmitPowerLevelInDBm(self) -> win32more.Windows.Foundation.IReference[Int16]: ...
    @winrt_commethod(7)
    def put_PreferredTransmitPowerLevelInDBm(self, value: win32more.Windows.Foundation.IReference[Int16]) -> Void: ...
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
    IncludeTransmitPowerLevel = property(get_IncludeTransmitPowerLevel, put_IncludeTransmitPowerLevel)
    IsAnonymous = property(get_IsAnonymous, put_IsAnonymous)
    PreferredTransmitPowerLevelInDBm = property(get_PreferredTransmitPowerLevelInDBm, put_PreferredTransmitPowerLevelInDBm)
    UseExtendedAdvertisement = property(get_UseExtendedAdvertisement, put_UseExtendedAdvertisement)
class IBluetoothLEAdvertisementPublisherFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisherFactory'
    _iid_ = Guid('{5c5f065e-b863-4981-a1af-1c544d8b0c0d}')
    @winrt_commethod(6)
    def Create(self, advertisement: win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisher: ...
class IBluetoothLEAdvertisementPublisherStatusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisherStatusChangedEventArgs'
    _iid_ = Guid('{09c2bd9f-2dff-4b23-86ee-0d14fb94aeae}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementPublisherStatus: ...
    @winrt_commethod(7)
    def get_Error(self) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    Error = property(get_Error, None)
    Status = property(get_Status, None)
class IBluetoothLEAdvertisementPublisherStatusChangedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementPublisherStatusChangedEventArgs2'
    _iid_ = Guid('{8f62790e-dc88-5c8b-b34e-10b321850f88}')
    @winrt_commethod(6)
    def get_SelectedTransmitPowerLevelInDBm(self) -> win32more.Windows.Foundation.IReference[Int16]: ...
    SelectedTransmitPowerLevelInDBm = property(get_SelectedTransmitPowerLevelInDBm, None)
class IBluetoothLEAdvertisementReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs'
    _iid_ = Guid('{27987ddf-e596-41be-8d43-9e6731d4a913}')
    @winrt_commethod(6)
    def get_RawSignalStrengthInDBm(self) -> Int16: ...
    @winrt_commethod(7)
    def get_BluetoothAddress(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_AdvertisementType(self) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementType: ...
    @winrt_commethod(9)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def get_Advertisement(self) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisement: ...
    Advertisement = property(get_Advertisement, None)
    AdvertisementType = property(get_AdvertisementType, None)
    BluetoothAddress = property(get_BluetoothAddress, None)
    RawSignalStrengthInDBm = property(get_RawSignalStrengthInDBm, None)
    Timestamp = property(get_Timestamp, None)
class IBluetoothLEAdvertisementReceivedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementReceivedEventArgs2'
    _iid_ = Guid('{12d9c87b-0399-5f0e-a348-53b02b6b162e}')
    @winrt_commethod(6)
    def get_BluetoothAddressType(self) -> win32more.Windows.Devices.Bluetooth.BluetoothAddressType: ...
    @winrt_commethod(7)
    def get_TransmitPowerLevelInDBm(self) -> win32more.Windows.Foundation.IReference[Int16]: ...
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
    IsAnonymous = property(get_IsAnonymous, None)
    IsConnectable = property(get_IsConnectable, None)
    IsDirected = property(get_IsDirected, None)
    IsScanResponse = property(get_IsScanResponse, None)
    IsScannable = property(get_IsScannable, None)
    TransmitPowerLevelInDBm = property(get_TransmitPowerLevelInDBm, None)
class IBluetoothLEAdvertisementWatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher'
    _iid_ = Guid('{a6ac336f-f3d3-4297-8d6c-c81ea6623f40}')
    @winrt_commethod(6)
    def get_MinSamplingInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_MaxSamplingInterval(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def get_MinOutOfRangeTimeout(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_MaxOutOfRangeTimeout(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_Status(self) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcherStatus: ...
    @winrt_commethod(11)
    def get_ScanningMode(self) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEScanningMode: ...
    @winrt_commethod(12)
    def put_ScanningMode(self, value: win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEScanningMode) -> Void: ...
    @winrt_commethod(13)
    def get_SignalStrengthFilter(self) -> win32more.Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter: ...
    @winrt_commethod(14)
    def put_SignalStrengthFilter(self, value: win32more.Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter) -> Void: ...
    @winrt_commethod(15)
    def get_AdvertisementFilter(self) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter: ...
    @winrt_commethod(16)
    def put_AdvertisementFilter(self, value: win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter) -> Void: ...
    @winrt_commethod(17)
    def Start(self) -> Void: ...
    @winrt_commethod(18)
    def Stop(self) -> Void: ...
    @winrt_commethod(19)
    def add_Received(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcher, win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_Received(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_Stopped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcher, win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcherStoppedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_Stopped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AdvertisementFilter = property(get_AdvertisementFilter, put_AdvertisementFilter)
    MaxOutOfRangeTimeout = property(get_MaxOutOfRangeTimeout, None)
    MaxSamplingInterval = property(get_MaxSamplingInterval, None)
    MinOutOfRangeTimeout = property(get_MinOutOfRangeTimeout, None)
    MinSamplingInterval = property(get_MinSamplingInterval, None)
    ScanningMode = property(get_ScanningMode, put_ScanningMode)
    SignalStrengthFilter = property(get_SignalStrengthFilter, put_SignalStrengthFilter)
    Status = property(get_Status, None)
    Received = event()
    Stopped = event()
class IBluetoothLEAdvertisementWatcher2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcher2'
    _iid_ = Guid('{01bf26bc-b164-5805-90a3-e8a7997ff225}')
    @winrt_commethod(6)
    def get_AllowExtendedAdvertisements(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowExtendedAdvertisements(self, value: Boolean) -> Void: ...
    AllowExtendedAdvertisements = property(get_AllowExtendedAdvertisements, put_AllowExtendedAdvertisements)
class IBluetoothLEAdvertisementWatcherFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcherFactory'
    _iid_ = Guid('{9aaf2d56-39ac-453e-b32a-85c657e017f1}')
    @winrt_commethod(6)
    def Create(self, advertisementFilter: win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementFilter) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEAdvertisementWatcher: ...
class IBluetoothLEAdvertisementWatcherStoppedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEAdvertisementWatcherStoppedEventArgs'
    _iid_ = Guid('{dd40f84d-e7b9-43e3-9c04-0685d085fd8c}')
    @winrt_commethod(6)
    def get_Error(self) -> win32more.Windows.Devices.Bluetooth.BluetoothError: ...
    Error = property(get_Error, None)
class IBluetoothLEManufacturerData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEManufacturerData'
    _iid_ = Guid('{912dba18-6963-4533-b061-4694dafb34e5}')
    @winrt_commethod(6)
    def get_CompanyId(self) -> UInt16: ...
    @winrt_commethod(7)
    def put_CompanyId(self, value: UInt16) -> Void: ...
    @winrt_commethod(8)
    def get_Data(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(9)
    def put_Data(self, value: win32more.Windows.Storage.Streams.IBuffer) -> Void: ...
    CompanyId = property(get_CompanyId, put_CompanyId)
    Data = property(get_Data, put_Data)
class IBluetoothLEManufacturerDataFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.Advertisement.IBluetoothLEManufacturerDataFactory'
    _iid_ = Guid('{c09b39f8-319a-441e-8de5-66a81e877a6c}')
    @winrt_commethod(6)
    def Create(self, companyId: UInt16, data: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Devices.Bluetooth.Advertisement.BluetoothLEManufacturerData: ...


make_ready(__name__)
