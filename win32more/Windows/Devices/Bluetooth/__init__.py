from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Bluetooth
import win32more.Windows.Devices.Bluetooth.GenericAttributeProfile
import win32more.Windows.Devices.Bluetooth.Rfcomm
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Devices.Radios
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Networking
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class BluetoothAdapter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.IBluetoothAdapter
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothAdapter'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Bluetooth.IBluetoothAdapter) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BluetoothAddress(self: win32more.Windows.Devices.Bluetooth.IBluetoothAdapter) -> UInt64: ...
    @winrt_mixinmethod
    def get_IsClassicSupported(self: win32more.Windows.Devices.Bluetooth.IBluetoothAdapter) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsLowEnergySupported(self: win32more.Windows.Devices.Bluetooth.IBluetoothAdapter) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPeripheralRoleSupported(self: win32more.Windows.Devices.Bluetooth.IBluetoothAdapter) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCentralRoleSupported(self: win32more.Windows.Devices.Bluetooth.IBluetoothAdapter) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsAdvertisementOffloadSupported(self: win32more.Windows.Devices.Bluetooth.IBluetoothAdapter) -> Boolean: ...
    @winrt_mixinmethod
    def GetRadioAsync(self: win32more.Windows.Devices.Bluetooth.IBluetoothAdapter) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Radios.Radio]: ...
    @winrt_mixinmethod
    def get_AreClassicSecureConnectionsSupported(self: win32more.Windows.Devices.Bluetooth.IBluetoothAdapter2) -> Boolean: ...
    @winrt_mixinmethod
    def get_AreLowEnergySecureConnectionsSupported(self: win32more.Windows.Devices.Bluetooth.IBluetoothAdapter2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsExtendedAdvertisingSupported(self: win32more.Windows.Devices.Bluetooth.IBluetoothAdapter3) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxAdvertisementDataLength(self: win32more.Windows.Devices.Bluetooth.IBluetoothAdapter3) -> UInt32: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Bluetooth.IBluetoothAdapterStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Bluetooth.IBluetoothAdapterStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.BluetoothAdapter]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: win32more.Windows.Devices.Bluetooth.IBluetoothAdapterStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.BluetoothAdapter]: ...
    AreClassicSecureConnectionsSupported = property(get_AreClassicSecureConnectionsSupported, None)
    AreLowEnergySecureConnectionsSupported = property(get_AreLowEnergySecureConnectionsSupported, None)
    BluetoothAddress = property(get_BluetoothAddress, None)
    DeviceId = property(get_DeviceId, None)
    IsAdvertisementOffloadSupported = property(get_IsAdvertisementOffloadSupported, None)
    IsCentralRoleSupported = property(get_IsCentralRoleSupported, None)
    IsClassicSupported = property(get_IsClassicSupported, None)
    IsExtendedAdvertisingSupported = property(get_IsExtendedAdvertisingSupported, None)
    IsLowEnergySupported = property(get_IsLowEnergySupported, None)
    IsPeripheralRoleSupported = property(get_IsPeripheralRoleSupported, None)
    MaxAdvertisementDataLength = property(get_MaxAdvertisementDataLength, None)
class BluetoothAddressType(Enum, Int32):
    Public = 0
    Random = 1
    Unspecified = 2
class BluetoothCacheMode(Enum, Int32):
    Cached = 0
    Uncached = 1
class BluetoothClassOfDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.IBluetoothClassOfDevice
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothClassOfDevice'
    @winrt_mixinmethod
    def get_RawValue(self: win32more.Windows.Devices.Bluetooth.IBluetoothClassOfDevice) -> UInt32: ...
    @winrt_mixinmethod
    def get_MajorClass(self: win32more.Windows.Devices.Bluetooth.IBluetoothClassOfDevice) -> win32more.Windows.Devices.Bluetooth.BluetoothMajorClass: ...
    @winrt_mixinmethod
    def get_MinorClass(self: win32more.Windows.Devices.Bluetooth.IBluetoothClassOfDevice) -> win32more.Windows.Devices.Bluetooth.BluetoothMinorClass: ...
    @winrt_mixinmethod
    def get_ServiceCapabilities(self: win32more.Windows.Devices.Bluetooth.IBluetoothClassOfDevice) -> win32more.Windows.Devices.Bluetooth.BluetoothServiceCapabilities: ...
    @winrt_classmethod
    def FromRawValue(cls: win32more.Windows.Devices.Bluetooth.IBluetoothClassOfDeviceStatics, rawValue: UInt32) -> win32more.Windows.Devices.Bluetooth.BluetoothClassOfDevice: ...
    @winrt_classmethod
    def FromParts(cls: win32more.Windows.Devices.Bluetooth.IBluetoothClassOfDeviceStatics, majorClass: win32more.Windows.Devices.Bluetooth.BluetoothMajorClass, minorClass: win32more.Windows.Devices.Bluetooth.BluetoothMinorClass, serviceCapabilities: win32more.Windows.Devices.Bluetooth.BluetoothServiceCapabilities) -> win32more.Windows.Devices.Bluetooth.BluetoothClassOfDevice: ...
    MajorClass = property(get_MajorClass, None)
    MinorClass = property(get_MinorClass, None)
    RawValue = property(get_RawValue, None)
    ServiceCapabilities = property(get_ServiceCapabilities, None)
class BluetoothConnectionStatus(Enum, Int32):
    Disconnected = 0
    Connected = 1
class BluetoothDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Bluetooth.IBluetoothDevice
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothDevice'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HostName(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice) -> win32more.Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ClassOfDevice(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice) -> win32more.Windows.Devices.Bluetooth.BluetoothClassOfDevice: ...
    @winrt_mixinmethod
    def get_SdpRecords(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def get_RfcommServices(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceService]: ...
    @winrt_mixinmethod
    def get_ConnectionStatus(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice) -> win32more.Windows.Devices.Bluetooth.BluetoothConnectionStatus: ...
    @winrt_mixinmethod
    def get_BluetoothAddress(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice) -> UInt64: ...
    @winrt_mixinmethod
    def add_NameChanged(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.BluetoothDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NameChanged(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SdpRecordsChanged(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.BluetoothDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SdpRecordsChanged(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ConnectionStatusChanged(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.BluetoothDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionStatusChanged(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceInformation(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice2) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_DeviceAccessInformation(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice3) -> win32more.Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_mixinmethod
    def RequestAccessAsync(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceAccessStatus]: ...
    @winrt_mixinmethod
    def GetRfcommServicesAsync(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceServicesResult]: ...
    @winrt_mixinmethod
    def GetRfcommServicesWithCacheModeAsync(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice3, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceServicesResult]: ...
    @winrt_mixinmethod
    def GetRfcommServicesForIdAsync(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice3, serviceId: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceServicesResult]: ...
    @winrt_mixinmethod
    def GetRfcommServicesForIdWithCacheModeAsync(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice3, serviceId: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceServicesResult]: ...
    @winrt_mixinmethod
    def get_BluetoothDeviceId(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice4) -> win32more.Windows.Devices.Bluetooth.BluetoothDeviceId: ...
    @winrt_mixinmethod
    def get_WasSecureConnectionUsedForPairing(self: win32more.Windows.Devices.Bluetooth.IBluetoothDevice5) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelectorFromPairingState(cls: win32more.Windows.Devices.Bluetooth.IBluetoothDeviceStatics2, pairingState: Boolean) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromConnectionStatus(cls: win32more.Windows.Devices.Bluetooth.IBluetoothDeviceStatics2, connectionStatus: win32more.Windows.Devices.Bluetooth.BluetoothConnectionStatus) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromDeviceName(cls: win32more.Windows.Devices.Bluetooth.IBluetoothDeviceStatics2, deviceName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromBluetoothAddress(cls: win32more.Windows.Devices.Bluetooth.IBluetoothDeviceStatics2, bluetoothAddress: UInt64) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromClassOfDevice(cls: win32more.Windows.Devices.Bluetooth.IBluetoothDeviceStatics2, classOfDevice: win32more.Windows.Devices.Bluetooth.BluetoothClassOfDevice) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Bluetooth.IBluetoothDeviceStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.BluetoothDevice]: ...
    @winrt_classmethod
    def FromHostNameAsync(cls: win32more.Windows.Devices.Bluetooth.IBluetoothDeviceStatics, hostName: win32more.Windows.Networking.HostName) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.BluetoothDevice]: ...
    @winrt_classmethod
    def FromBluetoothAddressAsync(cls: win32more.Windows.Devices.Bluetooth.IBluetoothDeviceStatics, address: UInt64) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.BluetoothDevice]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Bluetooth.IBluetoothDeviceStatics) -> WinRT_String: ...
    BluetoothAddress = property(get_BluetoothAddress, None)
    BluetoothDeviceId = property(get_BluetoothDeviceId, None)
    ClassOfDevice = property(get_ClassOfDevice, None)
    ConnectionStatus = property(get_ConnectionStatus, None)
    DeviceAccessInformation = property(get_DeviceAccessInformation, None)
    DeviceId = property(get_DeviceId, None)
    DeviceInformation = property(get_DeviceInformation, None)
    HostName = property(get_HostName, None)
    Name = property(get_Name, None)
    RfcommServices = property(get_RfcommServices, None)
    SdpRecords = property(get_SdpRecords, None)
    WasSecureConnectionUsedForPairing = property(get_WasSecureConnectionUsedForPairing, None)
    NameChanged = event()
    SdpRecordsChanged = event()
    ConnectionStatusChanged = event()
class BluetoothDeviceId(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.IBluetoothDeviceId
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothDeviceId'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Bluetooth.IBluetoothDeviceId) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsClassicDevice(self: win32more.Windows.Devices.Bluetooth.IBluetoothDeviceId) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsLowEnergyDevice(self: win32more.Windows.Devices.Bluetooth.IBluetoothDeviceId) -> Boolean: ...
    @winrt_classmethod
    def FromId(cls: win32more.Windows.Devices.Bluetooth.IBluetoothDeviceIdStatics, deviceId: WinRT_String) -> win32more.Windows.Devices.Bluetooth.BluetoothDeviceId: ...
    Id = property(get_Id, None)
    IsClassicDevice = property(get_IsClassicDevice, None)
    IsLowEnergyDevice = property(get_IsLowEnergyDevice, None)
class BluetoothError(Enum, Int32):
    Success = 0
    RadioNotAvailable = 1
    ResourceInUse = 2
    DeviceNotConnected = 3
    OtherError = 4
    DisabledByPolicy = 5
    NotSupported = 6
    DisabledByUser = 7
    ConsentRequired = 8
    TransportNotSupported = 9
class BluetoothLEAppearance(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearance
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothLEAppearance'
    @winrt_mixinmethod
    def get_RawValue(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearance) -> UInt16: ...
    @winrt_mixinmethod
    def get_Category(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearance) -> UInt16: ...
    @winrt_mixinmethod
    def get_SubCategory(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearance) -> UInt16: ...
    @winrt_classmethod
    def FromRawValue(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceStatics, rawValue: UInt16) -> win32more.Windows.Devices.Bluetooth.BluetoothLEAppearance: ...
    @winrt_classmethod
    def FromParts(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceStatics, appearanceCategory: UInt16, appearanceSubCategory: UInt16) -> win32more.Windows.Devices.Bluetooth.BluetoothLEAppearance: ...
    Category = property(get_Category, None)
    RawValue = property(get_RawValue, None)
    SubCategory = property(get_SubCategory, None)
class _BluetoothLEAppearanceCategories_Meta_(ComPtr.__class__):
    pass
class BluetoothLEAppearanceCategories(ComPtr, metaclass=_BluetoothLEAppearanceCategories_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothLEAppearanceCategories'
    @winrt_classmethod
    def get_Uncategorized(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Phone(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Computer(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Watch(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Clock(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Display(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_RemoteControl(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_EyeGlasses(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Tag(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Keyring(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_MediaPlayer(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_BarcodeScanner(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Thermometer(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_HeartRate(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_BloodPressure(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_HumanInterfaceDevice(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_GlucoseMeter(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_RunningWalking(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Cycling(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_PulseOximeter(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_WeightScale(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_OutdoorSportActivity(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    _BluetoothLEAppearanceCategories_Meta_.BarcodeScanner = property(get_BarcodeScanner, None)
    _BluetoothLEAppearanceCategories_Meta_.BloodPressure = property(get_BloodPressure, None)
    _BluetoothLEAppearanceCategories_Meta_.Clock = property(get_Clock, None)
    _BluetoothLEAppearanceCategories_Meta_.Computer = property(get_Computer, None)
    _BluetoothLEAppearanceCategories_Meta_.Cycling = property(get_Cycling, None)
    _BluetoothLEAppearanceCategories_Meta_.Display = property(get_Display, None)
    _BluetoothLEAppearanceCategories_Meta_.EyeGlasses = property(get_EyeGlasses, None)
    _BluetoothLEAppearanceCategories_Meta_.GlucoseMeter = property(get_GlucoseMeter, None)
    _BluetoothLEAppearanceCategories_Meta_.HeartRate = property(get_HeartRate, None)
    _BluetoothLEAppearanceCategories_Meta_.HumanInterfaceDevice = property(get_HumanInterfaceDevice, None)
    _BluetoothLEAppearanceCategories_Meta_.Keyring = property(get_Keyring, None)
    _BluetoothLEAppearanceCategories_Meta_.MediaPlayer = property(get_MediaPlayer, None)
    _BluetoothLEAppearanceCategories_Meta_.OutdoorSportActivity = property(get_OutdoorSportActivity, None)
    _BluetoothLEAppearanceCategories_Meta_.Phone = property(get_Phone, None)
    _BluetoothLEAppearanceCategories_Meta_.PulseOximeter = property(get_PulseOximeter, None)
    _BluetoothLEAppearanceCategories_Meta_.RemoteControl = property(get_RemoteControl, None)
    _BluetoothLEAppearanceCategories_Meta_.RunningWalking = property(get_RunningWalking, None)
    _BluetoothLEAppearanceCategories_Meta_.Tag = property(get_Tag, None)
    _BluetoothLEAppearanceCategories_Meta_.Thermometer = property(get_Thermometer, None)
    _BluetoothLEAppearanceCategories_Meta_.Uncategorized = property(get_Uncategorized, None)
    _BluetoothLEAppearanceCategories_Meta_.Watch = property(get_Watch, None)
    _BluetoothLEAppearanceCategories_Meta_.WeightScale = property(get_WeightScale, None)
class _BluetoothLEAppearanceSubcategories_Meta_(ComPtr.__class__):
    pass
class BluetoothLEAppearanceSubcategories(ComPtr, metaclass=_BluetoothLEAppearanceSubcategories_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothLEAppearanceSubcategories'
    @winrt_classmethod
    def get_Generic(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_SportsWatch(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_ThermometerEar(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_HeartRateBelt(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_BloodPressureArm(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_BloodPressureWrist(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Keyboard(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Mouse(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Joystick(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Gamepad(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_DigitizerTablet(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_CardReader(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_DigitalPen(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_BarcodeScanner(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_RunningWalkingInShoe(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_RunningWalkingOnShoe(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_RunningWalkingOnHip(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_CyclingComputer(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_CyclingSpeedSensor(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_CyclingCadenceSensor(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_CyclingPowerSensor(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_CyclingSpeedCadenceSensor(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_OximeterFingertip(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_OximeterWristWorn(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_LocationDisplay(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_LocationNavigationDisplay(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_LocationPod(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_LocationNavigationPod(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    _BluetoothLEAppearanceSubcategories_Meta_.BarcodeScanner = property(get_BarcodeScanner, None)
    _BluetoothLEAppearanceSubcategories_Meta_.BloodPressureArm = property(get_BloodPressureArm, None)
    _BluetoothLEAppearanceSubcategories_Meta_.BloodPressureWrist = property(get_BloodPressureWrist, None)
    _BluetoothLEAppearanceSubcategories_Meta_.CardReader = property(get_CardReader, None)
    _BluetoothLEAppearanceSubcategories_Meta_.CyclingCadenceSensor = property(get_CyclingCadenceSensor, None)
    _BluetoothLEAppearanceSubcategories_Meta_.CyclingComputer = property(get_CyclingComputer, None)
    _BluetoothLEAppearanceSubcategories_Meta_.CyclingPowerSensor = property(get_CyclingPowerSensor, None)
    _BluetoothLEAppearanceSubcategories_Meta_.CyclingSpeedCadenceSensor = property(get_CyclingSpeedCadenceSensor, None)
    _BluetoothLEAppearanceSubcategories_Meta_.CyclingSpeedSensor = property(get_CyclingSpeedSensor, None)
    _BluetoothLEAppearanceSubcategories_Meta_.DigitalPen = property(get_DigitalPen, None)
    _BluetoothLEAppearanceSubcategories_Meta_.DigitizerTablet = property(get_DigitizerTablet, None)
    _BluetoothLEAppearanceSubcategories_Meta_.Gamepad = property(get_Gamepad, None)
    _BluetoothLEAppearanceSubcategories_Meta_.Generic = property(get_Generic, None)
    _BluetoothLEAppearanceSubcategories_Meta_.HeartRateBelt = property(get_HeartRateBelt, None)
    _BluetoothLEAppearanceSubcategories_Meta_.Joystick = property(get_Joystick, None)
    _BluetoothLEAppearanceSubcategories_Meta_.Keyboard = property(get_Keyboard, None)
    _BluetoothLEAppearanceSubcategories_Meta_.LocationDisplay = property(get_LocationDisplay, None)
    _BluetoothLEAppearanceSubcategories_Meta_.LocationNavigationDisplay = property(get_LocationNavigationDisplay, None)
    _BluetoothLEAppearanceSubcategories_Meta_.LocationNavigationPod = property(get_LocationNavigationPod, None)
    _BluetoothLEAppearanceSubcategories_Meta_.LocationPod = property(get_LocationPod, None)
    _BluetoothLEAppearanceSubcategories_Meta_.Mouse = property(get_Mouse, None)
    _BluetoothLEAppearanceSubcategories_Meta_.OximeterFingertip = property(get_OximeterFingertip, None)
    _BluetoothLEAppearanceSubcategories_Meta_.OximeterWristWorn = property(get_OximeterWristWorn, None)
    _BluetoothLEAppearanceSubcategories_Meta_.RunningWalkingInShoe = property(get_RunningWalkingInShoe, None)
    _BluetoothLEAppearanceSubcategories_Meta_.RunningWalkingOnHip = property(get_RunningWalkingOnHip, None)
    _BluetoothLEAppearanceSubcategories_Meta_.RunningWalkingOnShoe = property(get_RunningWalkingOnShoe, None)
    _BluetoothLEAppearanceSubcategories_Meta_.SportsWatch = property(get_SportsWatch, None)
    _BluetoothLEAppearanceSubcategories_Meta_.ThermometerEar = property(get_ThermometerEar, None)
class BluetoothLEConnectionParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.IBluetoothLEConnectionParameters
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothLEConnectionParameters'
    @winrt_mixinmethod
    def get_LinkTimeout(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEConnectionParameters) -> UInt16: ...
    @winrt_mixinmethod
    def get_ConnectionLatency(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEConnectionParameters) -> UInt16: ...
    @winrt_mixinmethod
    def get_ConnectionInterval(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEConnectionParameters) -> UInt16: ...
    ConnectionInterval = property(get_ConnectionInterval, None)
    ConnectionLatency = property(get_ConnectionLatency, None)
    LinkTimeout = property(get_LinkTimeout, None)
class BluetoothLEConnectionPhy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.IBluetoothLEConnectionPhy
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothLEConnectionPhy'
    @winrt_mixinmethod
    def get_TransmitInfo(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEConnectionPhy) -> win32more.Windows.Devices.Bluetooth.BluetoothLEConnectionPhyInfo: ...
    @winrt_mixinmethod
    def get_ReceiveInfo(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEConnectionPhy) -> win32more.Windows.Devices.Bluetooth.BluetoothLEConnectionPhyInfo: ...
    ReceiveInfo = property(get_ReceiveInfo, None)
    TransmitInfo = property(get_TransmitInfo, None)
class BluetoothLEConnectionPhyInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.IBluetoothLEConnectionPhyInfo
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothLEConnectionPhyInfo'
    @winrt_mixinmethod
    def get_IsUncoded1MPhy(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEConnectionPhyInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsUncoded2MPhy(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEConnectionPhyInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCodedPhy(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEConnectionPhyInfo) -> Boolean: ...
    IsCodedPhy = property(get_IsCodedPhy, None)
    IsUncoded1MPhy = property(get_IsUncoded1MPhy, None)
    IsUncoded2MPhy = property(get_IsUncoded2MPhy, None)
class BluetoothLEDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothLEDevice'
    @winrt_mixinmethod
    def get_DeviceId(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_GattServices(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_mixinmethod
    def get_ConnectionStatus(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice) -> win32more.Windows.Devices.Bluetooth.BluetoothConnectionStatus: ...
    @winrt_mixinmethod
    def get_BluetoothAddress(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice) -> UInt64: ...
    @winrt_mixinmethod
    def GetGattService(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice, serviceUuid: Guid) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService: ...
    @winrt_mixinmethod
    def add_NameChanged(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.BluetoothLEDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NameChanged(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GattServicesChanged(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.BluetoothLEDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GattServicesChanged(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ConnectionStatusChanged(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.BluetoothLEDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionStatusChanged(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceInformation(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice2) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_Appearance(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice2) -> win32more.Windows.Devices.Bluetooth.BluetoothLEAppearance: ...
    @winrt_mixinmethod
    def get_BluetoothAddressType(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice2) -> win32more.Windows.Devices.Bluetooth.BluetoothAddressType: ...
    @winrt_mixinmethod
    def get_DeviceAccessInformation(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice3) -> win32more.Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_mixinmethod
    def RequestAccessAsync(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceAccessStatus]: ...
    @winrt_mixinmethod
    def GetGattServicesAsync(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_mixinmethod
    def GetGattServicesWithCacheModeAsync(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice3, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_mixinmethod
    def GetGattServicesForUuidAsync(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice3, serviceUuid: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_mixinmethod
    def GetGattServicesForUuidWithCacheModeAsync(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice3, serviceUuid: Guid, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_mixinmethod
    def get_BluetoothDeviceId(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice4) -> win32more.Windows.Devices.Bluetooth.BluetoothDeviceId: ...
    @winrt_mixinmethod
    def get_WasSecureConnectionUsedForPairing(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice5) -> Boolean: ...
    @winrt_mixinmethod
    def GetConnectionParameters(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice6) -> win32more.Windows.Devices.Bluetooth.BluetoothLEConnectionParameters: ...
    @winrt_mixinmethod
    def GetConnectionPhy(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice6) -> win32more.Windows.Devices.Bluetooth.BluetoothLEConnectionPhy: ...
    @winrt_mixinmethod
    def RequestPreferredConnectionParameters(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice6, preferredConnectionParameters: win32more.Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParameters) -> win32more.Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParametersRequest: ...
    @winrt_mixinmethod
    def add_ConnectionParametersChanged(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice6, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.BluetoothLEDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionParametersChanged(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice6, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ConnectionPhyChanged(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice6, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.BluetoothLEDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionPhyChanged(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEDevice6, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelectorFromPairingState(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics2, pairingState: Boolean) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromConnectionStatus(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics2, connectionStatus: win32more.Windows.Devices.Bluetooth.BluetoothConnectionStatus) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromDeviceName(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics2, deviceName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromBluetoothAddress(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics2, bluetoothAddress: UInt64) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromBluetoothAddressWithBluetoothAddressType(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics2, bluetoothAddress: UInt64, bluetoothAddressType: win32more.Windows.Devices.Bluetooth.BluetoothAddressType) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromAppearance(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics2, appearance: win32more.Windows.Devices.Bluetooth.BluetoothLEAppearance) -> WinRT_String: ...
    @winrt_classmethod
    def FromBluetoothAddressWithBluetoothAddressTypeAsync(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics2, bluetoothAddress: UInt64, bluetoothAddressType: win32more.Windows.Devices.Bluetooth.BluetoothAddressType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.BluetoothLEDevice]: ...
    @winrt_classmethod
    def FromIdAsync(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.BluetoothLEDevice]: ...
    @winrt_classmethod
    def FromBluetoothAddressAsync(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics, bluetoothAddress: UInt64) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.BluetoothLEDevice]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics) -> WinRT_String: ...
    Appearance = property(get_Appearance, None)
    BluetoothAddress = property(get_BluetoothAddress, None)
    BluetoothAddressType = property(get_BluetoothAddressType, None)
    BluetoothDeviceId = property(get_BluetoothDeviceId, None)
    ConnectionStatus = property(get_ConnectionStatus, None)
    DeviceAccessInformation = property(get_DeviceAccessInformation, None)
    DeviceId = property(get_DeviceId, None)
    DeviceInformation = property(get_DeviceInformation, None)
    GattServices = property(get_GattServices, None)
    Name = property(get_Name, None)
    WasSecureConnectionUsedForPairing = property(get_WasSecureConnectionUsedForPairing, None)
    NameChanged = event()
    GattServicesChanged = event()
    ConnectionStatusChanged = event()
    ConnectionParametersChanged = event()
    ConnectionPhyChanged = event()
class _BluetoothLEPreferredConnectionParameters_Meta_(ComPtr.__class__):
    pass
class BluetoothLEPreferredConnectionParameters(ComPtr, metaclass=_BluetoothLEPreferredConnectionParameters_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParameters
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParameters'
    @winrt_mixinmethod
    def get_LinkTimeout(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParameters) -> UInt16: ...
    @winrt_mixinmethod
    def get_ConnectionLatency(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParameters) -> UInt16: ...
    @winrt_mixinmethod
    def get_MinConnectionInterval(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParameters) -> UInt16: ...
    @winrt_mixinmethod
    def get_MaxConnectionInterval(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParameters) -> UInt16: ...
    @winrt_classmethod
    def get_Balanced(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParametersStatics) -> win32more.Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParameters: ...
    @winrt_classmethod
    def get_ThroughputOptimized(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParametersStatics) -> win32more.Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParameters: ...
    @winrt_classmethod
    def get_PowerOptimized(cls: win32more.Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParametersStatics) -> win32more.Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParameters: ...
    ConnectionLatency = property(get_ConnectionLatency, None)
    LinkTimeout = property(get_LinkTimeout, None)
    MaxConnectionInterval = property(get_MaxConnectionInterval, None)
    MinConnectionInterval = property(get_MinConnectionInterval, None)
    _BluetoothLEPreferredConnectionParameters_Meta_.Balanced = property(get_Balanced, None)
    _BluetoothLEPreferredConnectionParameters_Meta_.PowerOptimized = property(get_PowerOptimized, None)
    _BluetoothLEPreferredConnectionParameters_Meta_.ThroughputOptimized = property(get_ThroughputOptimized, None)
class BluetoothLEPreferredConnectionParametersRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParametersRequest
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParametersRequest'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParametersRequest) -> win32more.Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParametersRequestStatus: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Status = property(get_Status, None)
class BluetoothLEPreferredConnectionParametersRequestStatus(Enum, Int32):
    Unspecified = 0
    Success = 1
    DeviceNotAvailable = 2
    AccessDenied = 3
class BluetoothMajorClass(Enum, Int32):
    Miscellaneous = 0
    Computer = 1
    Phone = 2
    NetworkAccessPoint = 3
    AudioVideo = 4
    Peripheral = 5
    Imaging = 6
    Wearable = 7
    Toy = 8
    Health = 9
class BluetoothMinorClass(Enum, Int32):
    Uncategorized = 0
    ComputerDesktop = 1
    ComputerServer = 2
    ComputerLaptop = 3
    ComputerHandheld = 4
    ComputerPalmSize = 5
    ComputerWearable = 6
    ComputerTablet = 7
    PhoneCellular = 1
    PhoneCordless = 2
    PhoneSmartPhone = 3
    PhoneWired = 4
    PhoneIsdn = 5
    NetworkFullyAvailable = 0
    NetworkUsed01To17Percent = 8
    NetworkUsed17To33Percent = 16
    NetworkUsed33To50Percent = 24
    NetworkUsed50To67Percent = 32
    NetworkUsed67To83Percent = 40
    NetworkUsed83To99Percent = 48
    NetworkNoServiceAvailable = 56
    AudioVideoWearableHeadset = 1
    AudioVideoHandsFree = 2
    AudioVideoMicrophone = 4
    AudioVideoLoudspeaker = 5
    AudioVideoHeadphones = 6
    AudioVideoPortableAudio = 7
    AudioVideoCarAudio = 8
    AudioVideoSetTopBox = 9
    AudioVideoHifiAudioDevice = 10
    AudioVideoVcr = 11
    AudioVideoVideoCamera = 12
    AudioVideoCamcorder = 13
    AudioVideoVideoMonitor = 14
    AudioVideoVideoDisplayAndLoudspeaker = 15
    AudioVideoVideoConferencing = 16
    AudioVideoGamingOrToy = 18
    PeripheralJoystick = 1
    PeripheralGamepad = 2
    PeripheralRemoteControl = 3
    PeripheralSensing = 4
    PeripheralDigitizerTablet = 5
    PeripheralCardReader = 6
    PeripheralDigitalPen = 7
    PeripheralHandheldScanner = 8
    PeripheralHandheldGesture = 9
    WearableWristwatch = 1
    WearablePager = 2
    WearableJacket = 3
    WearableHelmet = 4
    WearableGlasses = 5
    ToyRobot = 1
    ToyVehicle = 2
    ToyDoll = 3
    ToyController = 4
    ToyGame = 5
    HealthBloodPressureMonitor = 1
    HealthThermometer = 2
    HealthWeighingScale = 3
    HealthGlucoseMeter = 4
    HealthPulseOximeter = 5
    HealthHeartRateMonitor = 6
    HealthHealthDataDisplay = 7
    HealthStepCounter = 8
    HealthBodyCompositionAnalyzer = 9
    HealthPeakFlowMonitor = 10
    HealthMedicationMonitor = 11
    HealthKneeProsthesis = 12
    HealthAnkleProsthesis = 13
    HealthGenericHealthManager = 14
    HealthPersonalMobilityDevice = 15
class BluetoothServiceCapabilities(Enum, UInt32):
    None_ = 0
    LimitedDiscoverableMode = 1
    PositioningService = 8
    NetworkingService = 16
    RenderingService = 32
    CapturingService = 64
    ObjectTransferService = 128
    AudioService = 256
    TelephoneService = 512
    InformationService = 1024
class BluetoothSignalStrengthFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Bluetooth.IBluetoothSignalStrengthFilter
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter: ...
    @winrt_mixinmethod
    def get_InRangeThresholdInDBm(self: win32more.Windows.Devices.Bluetooth.IBluetoothSignalStrengthFilter) -> win32more.Windows.Foundation.IReference[Int16]: ...
    @winrt_mixinmethod
    def put_InRangeThresholdInDBm(self: win32more.Windows.Devices.Bluetooth.IBluetoothSignalStrengthFilter, value: win32more.Windows.Foundation.IReference[Int16]) -> Void: ...
    @winrt_mixinmethod
    def get_OutOfRangeThresholdInDBm(self: win32more.Windows.Devices.Bluetooth.IBluetoothSignalStrengthFilter) -> win32more.Windows.Foundation.IReference[Int16]: ...
    @winrt_mixinmethod
    def put_OutOfRangeThresholdInDBm(self: win32more.Windows.Devices.Bluetooth.IBluetoothSignalStrengthFilter, value: win32more.Windows.Foundation.IReference[Int16]) -> Void: ...
    @winrt_mixinmethod
    def get_OutOfRangeTimeout(self: win32more.Windows.Devices.Bluetooth.IBluetoothSignalStrengthFilter) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_OutOfRangeTimeout(self: win32more.Windows.Devices.Bluetooth.IBluetoothSignalStrengthFilter, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_SamplingInterval(self: win32more.Windows.Devices.Bluetooth.IBluetoothSignalStrengthFilter) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_SamplingInterval(self: win32more.Windows.Devices.Bluetooth.IBluetoothSignalStrengthFilter, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    InRangeThresholdInDBm = property(get_InRangeThresholdInDBm, put_InRangeThresholdInDBm)
    OutOfRangeThresholdInDBm = property(get_OutOfRangeThresholdInDBm, put_OutOfRangeThresholdInDBm)
    OutOfRangeTimeout = property(get_OutOfRangeTimeout, put_OutOfRangeTimeout)
    SamplingInterval = property(get_SamplingInterval, put_SamplingInterval)
class BluetoothUuidHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothUuidHelper'
    @winrt_classmethod
    def FromShortId(cls: win32more.Windows.Devices.Bluetooth.IBluetoothUuidHelperStatics, shortId: UInt32) -> Guid: ...
    @winrt_classmethod
    def TryGetShortId(cls: win32more.Windows.Devices.Bluetooth.IBluetoothUuidHelperStatics, uuid: Guid) -> win32more.Windows.Foundation.IReference[UInt32]: ...
class IBluetoothAdapter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothAdapter'
    _iid_ = Guid('{7974f04c-5f7a-4a34-9225-a855f84b1a8b}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_BluetoothAddress(self) -> UInt64: ...
    @winrt_commethod(8)
    def get_IsClassicSupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsLowEnergySupported(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsPeripheralRoleSupported(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsCentralRoleSupported(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsAdvertisementOffloadSupported(self) -> Boolean: ...
    @winrt_commethod(13)
    def GetRadioAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Radios.Radio]: ...
    BluetoothAddress = property(get_BluetoothAddress, None)
    DeviceId = property(get_DeviceId, None)
    IsAdvertisementOffloadSupported = property(get_IsAdvertisementOffloadSupported, None)
    IsCentralRoleSupported = property(get_IsCentralRoleSupported, None)
    IsClassicSupported = property(get_IsClassicSupported, None)
    IsLowEnergySupported = property(get_IsLowEnergySupported, None)
    IsPeripheralRoleSupported = property(get_IsPeripheralRoleSupported, None)
class IBluetoothAdapter2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothAdapter2'
    _iid_ = Guid('{ac94cecc-24d5-41b3-916d-1097c50b102b}')
    @winrt_commethod(6)
    def get_AreClassicSecureConnectionsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AreLowEnergySecureConnectionsSupported(self) -> Boolean: ...
    AreClassicSecureConnectionsSupported = property(get_AreClassicSecureConnectionsSupported, None)
    AreLowEnergySecureConnectionsSupported = property(get_AreLowEnergySecureConnectionsSupported, None)
class IBluetoothAdapter3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothAdapter3'
    _iid_ = Guid('{8f8624e0-cba9-5211-9f89-3aac62b4c6b8}')
    @winrt_commethod(6)
    def get_IsExtendedAdvertisingSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_MaxAdvertisementDataLength(self) -> UInt32: ...
    IsExtendedAdvertisingSupported = property(get_IsExtendedAdvertisingSupported, None)
    MaxAdvertisementDataLength = property(get_MaxAdvertisementDataLength, None)
class IBluetoothAdapterStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothAdapterStatics'
    _iid_ = Guid('{8b02fb6a-ac4c-4741-8661-8eab7d17ea9f}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.BluetoothAdapter]: ...
    @winrt_commethod(8)
    def GetDefaultAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.BluetoothAdapter]: ...
class IBluetoothClassOfDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothClassOfDevice'
    _iid_ = Guid('{d640227e-d7d7-4661-9454-65039ca17a2b}')
    @winrt_commethod(6)
    def get_RawValue(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_MajorClass(self) -> win32more.Windows.Devices.Bluetooth.BluetoothMajorClass: ...
    @winrt_commethod(8)
    def get_MinorClass(self) -> win32more.Windows.Devices.Bluetooth.BluetoothMinorClass: ...
    @winrt_commethod(9)
    def get_ServiceCapabilities(self) -> win32more.Windows.Devices.Bluetooth.BluetoothServiceCapabilities: ...
    MajorClass = property(get_MajorClass, None)
    MinorClass = property(get_MinorClass, None)
    RawValue = property(get_RawValue, None)
    ServiceCapabilities = property(get_ServiceCapabilities, None)
class IBluetoothClassOfDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothClassOfDeviceStatics'
    _iid_ = Guid('{e46135bd-0fa2-416c-91b4-c1e48ca061c1}')
    @winrt_commethod(6)
    def FromRawValue(self, rawValue: UInt32) -> win32more.Windows.Devices.Bluetooth.BluetoothClassOfDevice: ...
    @winrt_commethod(7)
    def FromParts(self, majorClass: win32more.Windows.Devices.Bluetooth.BluetoothMajorClass, minorClass: win32more.Windows.Devices.Bluetooth.BluetoothMinorClass, serviceCapabilities: win32more.Windows.Devices.Bluetooth.BluetoothServiceCapabilities) -> win32more.Windows.Devices.Bluetooth.BluetoothClassOfDevice: ...
class IBluetoothDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothDevice'
    _iid_ = Guid('{2335b156-90d2-4a04-aef5-0e20b9e6b707}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_HostName(self) -> win32more.Windows.Networking.HostName: ...
    @winrt_commethod(8)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ClassOfDevice(self) -> win32more.Windows.Devices.Bluetooth.BluetoothClassOfDevice: ...
    @winrt_commethod(10)
    def get_SdpRecords(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(11)
    def get_RfcommServices(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceService]: ...
    @winrt_commethod(12)
    def get_ConnectionStatus(self) -> win32more.Windows.Devices.Bluetooth.BluetoothConnectionStatus: ...
    @winrt_commethod(13)
    def get_BluetoothAddress(self) -> UInt64: ...
    @winrt_commethod(14)
    def add_NameChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.BluetoothDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_NameChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_SdpRecordsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.BluetoothDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_SdpRecordsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_ConnectionStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.BluetoothDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_ConnectionStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BluetoothAddress = property(get_BluetoothAddress, None)
    ClassOfDevice = property(get_ClassOfDevice, None)
    ConnectionStatus = property(get_ConnectionStatus, None)
    DeviceId = property(get_DeviceId, None)
    HostName = property(get_HostName, None)
    Name = property(get_Name, None)
    RfcommServices = property(get_RfcommServices, None)
    SdpRecords = property(get_SdpRecords, None)
    NameChanged = event()
    SdpRecordsChanged = event()
    ConnectionStatusChanged = event()
class IBluetoothDevice2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothDevice2'
    _iid_ = Guid('{0133f954-b156-4dd0-b1f5-c11bc31a5163}')
    @winrt_commethod(6)
    def get_DeviceInformation(self) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    DeviceInformation = property(get_DeviceInformation, None)
class IBluetoothDevice3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothDevice3'
    _iid_ = Guid('{57fff78b-651a-4454-b90f-eb21ef0b0d71}')
    @winrt_commethod(6)
    def get_DeviceAccessInformation(self) -> win32more.Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_commethod(7)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceAccessStatus]: ...
    @winrt_commethod(8)
    def GetRfcommServicesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceServicesResult]: ...
    @winrt_commethod(9)
    def GetRfcommServicesWithCacheModeAsync(self, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceServicesResult]: ...
    @winrt_commethod(10)
    def GetRfcommServicesForIdAsync(self, serviceId: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceServicesResult]: ...
    @winrt_commethod(11)
    def GetRfcommServicesForIdWithCacheModeAsync(self, serviceId: win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceServicesResult]: ...
    DeviceAccessInformation = property(get_DeviceAccessInformation, None)
class IBluetoothDevice4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothDevice4'
    _iid_ = Guid('{817c34ad-0e9c-42b2-a8dc-3e8094940d12}')
    @winrt_commethod(6)
    def get_BluetoothDeviceId(self) -> win32more.Windows.Devices.Bluetooth.BluetoothDeviceId: ...
    BluetoothDeviceId = property(get_BluetoothDeviceId, None)
class IBluetoothDevice5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothDevice5'
    _iid_ = Guid('{b5e0b385-5e85-4559-a10d-1c7281379f96}')
    @winrt_commethod(6)
    def get_WasSecureConnectionUsedForPairing(self) -> Boolean: ...
    WasSecureConnectionUsedForPairing = property(get_WasSecureConnectionUsedForPairing, None)
class IBluetoothDeviceId(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothDeviceId'
    _iid_ = Guid('{c17949af-57c1-4642-bcce-e6c06b20ae76}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsClassicDevice(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsLowEnergyDevice(self) -> Boolean: ...
    Id = property(get_Id, None)
    IsClassicDevice = property(get_IsClassicDevice, None)
    IsLowEnergyDevice = property(get_IsLowEnergyDevice, None)
class IBluetoothDeviceIdStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothDeviceIdStatics'
    _iid_ = Guid('{a7884e67-3efb-4f31-bbc2-810e09977404}')
    @winrt_commethod(6)
    def FromId(self, deviceId: WinRT_String) -> win32more.Windows.Devices.Bluetooth.BluetoothDeviceId: ...
class IBluetoothDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothDeviceStatics'
    _iid_ = Guid('{0991df51-57db-4725-bbd7-84f64327ec2c}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.BluetoothDevice]: ...
    @winrt_commethod(7)
    def FromHostNameAsync(self, hostName: win32more.Windows.Networking.HostName) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.BluetoothDevice]: ...
    @winrt_commethod(8)
    def FromBluetoothAddressAsync(self, address: UInt64) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.BluetoothDevice]: ...
    @winrt_commethod(9)
    def GetDeviceSelector(self) -> WinRT_String: ...
class IBluetoothDeviceStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothDeviceStatics2'
    _iid_ = Guid('{c29e8e2f-4e14-4477-aa1b-b8b47e5b7ece}')
    @winrt_commethod(6)
    def GetDeviceSelectorFromPairingState(self, pairingState: Boolean) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorFromConnectionStatus(self, connectionStatus: win32more.Windows.Devices.Bluetooth.BluetoothConnectionStatus) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetDeviceSelectorFromDeviceName(self, deviceName: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetDeviceSelectorFromBluetoothAddress(self, bluetoothAddress: UInt64) -> WinRT_String: ...
    @winrt_commethod(10)
    def GetDeviceSelectorFromClassOfDevice(self, classOfDevice: win32more.Windows.Devices.Bluetooth.BluetoothClassOfDevice) -> WinRT_String: ...
class IBluetoothLEAppearance(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothLEAppearance'
    _iid_ = Guid('{5d2079f2-66a8-4258-985e-02b4d9509f18}')
    @winrt_commethod(6)
    def get_RawValue(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_Category(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_SubCategory(self) -> UInt16: ...
    Category = property(get_Category, None)
    RawValue = property(get_RawValue, None)
    SubCategory = property(get_SubCategory, None)
class IBluetoothLEAppearanceCategoriesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics'
    _iid_ = Guid('{6d4d54fe-046a-4185-aab6-824cf0610861}')
    @winrt_commethod(6)
    def get_Uncategorized(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_Phone(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_Computer(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_Watch(self) -> UInt16: ...
    @winrt_commethod(10)
    def get_Clock(self) -> UInt16: ...
    @winrt_commethod(11)
    def get_Display(self) -> UInt16: ...
    @winrt_commethod(12)
    def get_RemoteControl(self) -> UInt16: ...
    @winrt_commethod(13)
    def get_EyeGlasses(self) -> UInt16: ...
    @winrt_commethod(14)
    def get_Tag(self) -> UInt16: ...
    @winrt_commethod(15)
    def get_Keyring(self) -> UInt16: ...
    @winrt_commethod(16)
    def get_MediaPlayer(self) -> UInt16: ...
    @winrt_commethod(17)
    def get_BarcodeScanner(self) -> UInt16: ...
    @winrt_commethod(18)
    def get_Thermometer(self) -> UInt16: ...
    @winrt_commethod(19)
    def get_HeartRate(self) -> UInt16: ...
    @winrt_commethod(20)
    def get_BloodPressure(self) -> UInt16: ...
    @winrt_commethod(21)
    def get_HumanInterfaceDevice(self) -> UInt16: ...
    @winrt_commethod(22)
    def get_GlucoseMeter(self) -> UInt16: ...
    @winrt_commethod(23)
    def get_RunningWalking(self) -> UInt16: ...
    @winrt_commethod(24)
    def get_Cycling(self) -> UInt16: ...
    @winrt_commethod(25)
    def get_PulseOximeter(self) -> UInt16: ...
    @winrt_commethod(26)
    def get_WeightScale(self) -> UInt16: ...
    @winrt_commethod(27)
    def get_OutdoorSportActivity(self) -> UInt16: ...
    BarcodeScanner = property(get_BarcodeScanner, None)
    BloodPressure = property(get_BloodPressure, None)
    Clock = property(get_Clock, None)
    Computer = property(get_Computer, None)
    Cycling = property(get_Cycling, None)
    Display = property(get_Display, None)
    EyeGlasses = property(get_EyeGlasses, None)
    GlucoseMeter = property(get_GlucoseMeter, None)
    HeartRate = property(get_HeartRate, None)
    HumanInterfaceDevice = property(get_HumanInterfaceDevice, None)
    Keyring = property(get_Keyring, None)
    MediaPlayer = property(get_MediaPlayer, None)
    OutdoorSportActivity = property(get_OutdoorSportActivity, None)
    Phone = property(get_Phone, None)
    PulseOximeter = property(get_PulseOximeter, None)
    RemoteControl = property(get_RemoteControl, None)
    RunningWalking = property(get_RunningWalking, None)
    Tag = property(get_Tag, None)
    Thermometer = property(get_Thermometer, None)
    Uncategorized = property(get_Uncategorized, None)
    Watch = property(get_Watch, None)
    WeightScale = property(get_WeightScale, None)
class IBluetoothLEAppearanceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothLEAppearanceStatics'
    _iid_ = Guid('{a193c0c7-4504-4f4a-9ba5-cd1054e5e065}')
    @winrt_commethod(6)
    def FromRawValue(self, rawValue: UInt16) -> win32more.Windows.Devices.Bluetooth.BluetoothLEAppearance: ...
    @winrt_commethod(7)
    def FromParts(self, appearanceCategory: UInt16, appearanceSubCategory: UInt16) -> win32more.Windows.Devices.Bluetooth.BluetoothLEAppearance: ...
class IBluetoothLEAppearanceSubcategoriesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics'
    _iid_ = Guid('{e57ba606-2144-415a-8312-71ccf291f8d1}')
    @winrt_commethod(6)
    def get_Generic(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_SportsWatch(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_ThermometerEar(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_HeartRateBelt(self) -> UInt16: ...
    @winrt_commethod(10)
    def get_BloodPressureArm(self) -> UInt16: ...
    @winrt_commethod(11)
    def get_BloodPressureWrist(self) -> UInt16: ...
    @winrt_commethod(12)
    def get_Keyboard(self) -> UInt16: ...
    @winrt_commethod(13)
    def get_Mouse(self) -> UInt16: ...
    @winrt_commethod(14)
    def get_Joystick(self) -> UInt16: ...
    @winrt_commethod(15)
    def get_Gamepad(self) -> UInt16: ...
    @winrt_commethod(16)
    def get_DigitizerTablet(self) -> UInt16: ...
    @winrt_commethod(17)
    def get_CardReader(self) -> UInt16: ...
    @winrt_commethod(18)
    def get_DigitalPen(self) -> UInt16: ...
    @winrt_commethod(19)
    def get_BarcodeScanner(self) -> UInt16: ...
    @winrt_commethod(20)
    def get_RunningWalkingInShoe(self) -> UInt16: ...
    @winrt_commethod(21)
    def get_RunningWalkingOnShoe(self) -> UInt16: ...
    @winrt_commethod(22)
    def get_RunningWalkingOnHip(self) -> UInt16: ...
    @winrt_commethod(23)
    def get_CyclingComputer(self) -> UInt16: ...
    @winrt_commethod(24)
    def get_CyclingSpeedSensor(self) -> UInt16: ...
    @winrt_commethod(25)
    def get_CyclingCadenceSensor(self) -> UInt16: ...
    @winrt_commethod(26)
    def get_CyclingPowerSensor(self) -> UInt16: ...
    @winrt_commethod(27)
    def get_CyclingSpeedCadenceSensor(self) -> UInt16: ...
    @winrt_commethod(28)
    def get_OximeterFingertip(self) -> UInt16: ...
    @winrt_commethod(29)
    def get_OximeterWristWorn(self) -> UInt16: ...
    @winrt_commethod(30)
    def get_LocationDisplay(self) -> UInt16: ...
    @winrt_commethod(31)
    def get_LocationNavigationDisplay(self) -> UInt16: ...
    @winrt_commethod(32)
    def get_LocationPod(self) -> UInt16: ...
    @winrt_commethod(33)
    def get_LocationNavigationPod(self) -> UInt16: ...
    BarcodeScanner = property(get_BarcodeScanner, None)
    BloodPressureArm = property(get_BloodPressureArm, None)
    BloodPressureWrist = property(get_BloodPressureWrist, None)
    CardReader = property(get_CardReader, None)
    CyclingCadenceSensor = property(get_CyclingCadenceSensor, None)
    CyclingComputer = property(get_CyclingComputer, None)
    CyclingPowerSensor = property(get_CyclingPowerSensor, None)
    CyclingSpeedCadenceSensor = property(get_CyclingSpeedCadenceSensor, None)
    CyclingSpeedSensor = property(get_CyclingSpeedSensor, None)
    DigitalPen = property(get_DigitalPen, None)
    DigitizerTablet = property(get_DigitizerTablet, None)
    Gamepad = property(get_Gamepad, None)
    Generic = property(get_Generic, None)
    HeartRateBelt = property(get_HeartRateBelt, None)
    Joystick = property(get_Joystick, None)
    Keyboard = property(get_Keyboard, None)
    LocationDisplay = property(get_LocationDisplay, None)
    LocationNavigationDisplay = property(get_LocationNavigationDisplay, None)
    LocationNavigationPod = property(get_LocationNavigationPod, None)
    LocationPod = property(get_LocationPod, None)
    Mouse = property(get_Mouse, None)
    OximeterFingertip = property(get_OximeterFingertip, None)
    OximeterWristWorn = property(get_OximeterWristWorn, None)
    RunningWalkingInShoe = property(get_RunningWalkingInShoe, None)
    RunningWalkingOnHip = property(get_RunningWalkingOnHip, None)
    RunningWalkingOnShoe = property(get_RunningWalkingOnShoe, None)
    SportsWatch = property(get_SportsWatch, None)
    ThermometerEar = property(get_ThermometerEar, None)
class IBluetoothLEConnectionParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothLEConnectionParameters'
    _iid_ = Guid('{33cb0771-8da9-508f-a366-1ca388c929ab}')
    @winrt_commethod(6)
    def get_LinkTimeout(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_ConnectionLatency(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_ConnectionInterval(self) -> UInt16: ...
    ConnectionInterval = property(get_ConnectionInterval, None)
    ConnectionLatency = property(get_ConnectionLatency, None)
    LinkTimeout = property(get_LinkTimeout, None)
class IBluetoothLEConnectionPhy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothLEConnectionPhy'
    _iid_ = Guid('{781e5e48-621e-5a7e-8be6-1b9561ff63c9}')
    @winrt_commethod(6)
    def get_TransmitInfo(self) -> win32more.Windows.Devices.Bluetooth.BluetoothLEConnectionPhyInfo: ...
    @winrt_commethod(7)
    def get_ReceiveInfo(self) -> win32more.Windows.Devices.Bluetooth.BluetoothLEConnectionPhyInfo: ...
    ReceiveInfo = property(get_ReceiveInfo, None)
    TransmitInfo = property(get_TransmitInfo, None)
class IBluetoothLEConnectionPhyInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothLEConnectionPhyInfo'
    _iid_ = Guid('{9a100bdd-602e-5c27-a1ae-b230015a6394}')
    @winrt_commethod(6)
    def get_IsUncoded1MPhy(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsUncoded2MPhy(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsCodedPhy(self) -> Boolean: ...
    IsCodedPhy = property(get_IsCodedPhy, None)
    IsUncoded1MPhy = property(get_IsUncoded1MPhy, None)
    IsUncoded2MPhy = property(get_IsUncoded2MPhy, None)
class IBluetoothLEDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothLEDevice'
    _iid_ = Guid('{b5ee2f7b-4ad8-4642-ac48-80a0b500e887}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_GattServices(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_commethod(9)
    def get_ConnectionStatus(self) -> win32more.Windows.Devices.Bluetooth.BluetoothConnectionStatus: ...
    @winrt_commethod(10)
    def get_BluetoothAddress(self) -> UInt64: ...
    @winrt_commethod(11)
    def GetGattService(self, serviceUuid: Guid) -> win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService: ...
    @winrt_commethod(12)
    def add_NameChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.BluetoothLEDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_NameChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_GattServicesChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.BluetoothLEDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_GattServicesChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_ConnectionStatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.BluetoothLEDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_ConnectionStatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BluetoothAddress = property(get_BluetoothAddress, None)
    ConnectionStatus = property(get_ConnectionStatus, None)
    DeviceId = property(get_DeviceId, None)
    GattServices = property(get_GattServices, None)
    Name = property(get_Name, None)
    NameChanged = event()
    GattServicesChanged = event()
    ConnectionStatusChanged = event()
class IBluetoothLEDevice2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothLEDevice2'
    _iid_ = Guid('{26f062b3-7aee-4d31-baba-b1b9775f5916}')
    @winrt_commethod(6)
    def get_DeviceInformation(self) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_commethod(7)
    def get_Appearance(self) -> win32more.Windows.Devices.Bluetooth.BluetoothLEAppearance: ...
    @winrt_commethod(8)
    def get_BluetoothAddressType(self) -> win32more.Windows.Devices.Bluetooth.BluetoothAddressType: ...
    Appearance = property(get_Appearance, None)
    BluetoothAddressType = property(get_BluetoothAddressType, None)
    DeviceInformation = property(get_DeviceInformation, None)
class IBluetoothLEDevice3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothLEDevice3'
    _iid_ = Guid('{aee9e493-44ac-40dc-af33-b2c13c01ca46}')
    @winrt_commethod(6)
    def get_DeviceAccessInformation(self) -> win32more.Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_commethod(7)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Enumeration.DeviceAccessStatus]: ...
    @winrt_commethod(8)
    def GetGattServicesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_commethod(9)
    def GetGattServicesWithCacheModeAsync(self, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_commethod(10)
    def GetGattServicesForUuidAsync(self, serviceUuid: Guid) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_commethod(11)
    def GetGattServicesForUuidWithCacheModeAsync(self, serviceUuid: Guid, cacheMode: win32more.Windows.Devices.Bluetooth.BluetoothCacheMode) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    DeviceAccessInformation = property(get_DeviceAccessInformation, None)
class IBluetoothLEDevice4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothLEDevice4'
    _iid_ = Guid('{2b605031-2248-4b2f-acf0-7cee36fc5870}')
    @winrt_commethod(6)
    def get_BluetoothDeviceId(self) -> win32more.Windows.Devices.Bluetooth.BluetoothDeviceId: ...
    BluetoothDeviceId = property(get_BluetoothDeviceId, None)
class IBluetoothLEDevice5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothLEDevice5'
    _iid_ = Guid('{9d6a1260-5287-458e-95ba-17c8b7bb326e}')
    @winrt_commethod(6)
    def get_WasSecureConnectionUsedForPairing(self) -> Boolean: ...
    WasSecureConnectionUsedForPairing = property(get_WasSecureConnectionUsedForPairing, None)
class IBluetoothLEDevice6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothLEDevice6'
    _iid_ = Guid('{ca7190ef-0cae-573c-a1ca-e1fc5bfc39e2}')
    @winrt_commethod(6)
    def GetConnectionParameters(self) -> win32more.Windows.Devices.Bluetooth.BluetoothLEConnectionParameters: ...
    @winrt_commethod(7)
    def GetConnectionPhy(self) -> win32more.Windows.Devices.Bluetooth.BluetoothLEConnectionPhy: ...
    @winrt_commethod(8)
    def RequestPreferredConnectionParameters(self, preferredConnectionParameters: win32more.Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParameters) -> win32more.Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParametersRequest: ...
    @winrt_commethod(9)
    def add_ConnectionParametersChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.BluetoothLEDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_ConnectionParametersChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_ConnectionPhyChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Bluetooth.BluetoothLEDevice, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_ConnectionPhyChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ConnectionParametersChanged = event()
    ConnectionPhyChanged = event()
class IBluetoothLEDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics'
    _iid_ = Guid('{c8cf1a19-f0b6-4bf0-8689-41303de2d9f4}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.BluetoothLEDevice]: ...
    @winrt_commethod(7)
    def FromBluetoothAddressAsync(self, bluetoothAddress: UInt64) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.BluetoothLEDevice]: ...
    @winrt_commethod(8)
    def GetDeviceSelector(self) -> WinRT_String: ...
class IBluetoothLEDeviceStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics2'
    _iid_ = Guid('{5f12c06b-3bac-43e8-ad16-563271bd41c2}')
    @winrt_commethod(6)
    def GetDeviceSelectorFromPairingState(self, pairingState: Boolean) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorFromConnectionStatus(self, connectionStatus: win32more.Windows.Devices.Bluetooth.BluetoothConnectionStatus) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetDeviceSelectorFromDeviceName(self, deviceName: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetDeviceSelectorFromBluetoothAddress(self, bluetoothAddress: UInt64) -> WinRT_String: ...
    @winrt_commethod(10)
    def GetDeviceSelectorFromBluetoothAddressWithBluetoothAddressType(self, bluetoothAddress: UInt64, bluetoothAddressType: win32more.Windows.Devices.Bluetooth.BluetoothAddressType) -> WinRT_String: ...
    @winrt_commethod(11)
    def GetDeviceSelectorFromAppearance(self, appearance: win32more.Windows.Devices.Bluetooth.BluetoothLEAppearance) -> WinRT_String: ...
    @winrt_commethod(12)
    def FromBluetoothAddressWithBluetoothAddressTypeAsync(self, bluetoothAddress: UInt64, bluetoothAddressType: win32more.Windows.Devices.Bluetooth.BluetoothAddressType) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Bluetooth.BluetoothLEDevice]: ...
class IBluetoothLEPreferredConnectionParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParameters'
    _iid_ = Guid('{f2f44344-7372-5f7b-9b34-29c944f5a715}')
    @winrt_commethod(6)
    def get_LinkTimeout(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_ConnectionLatency(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_MinConnectionInterval(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_MaxConnectionInterval(self) -> UInt16: ...
    ConnectionLatency = property(get_ConnectionLatency, None)
    LinkTimeout = property(get_LinkTimeout, None)
    MaxConnectionInterval = property(get_MaxConnectionInterval, None)
    MinConnectionInterval = property(get_MinConnectionInterval, None)
class IBluetoothLEPreferredConnectionParametersRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParametersRequest'
    _iid_ = Guid('{8a375276-a528-5266-b661-cce6a5ff9739}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParametersRequestStatus: ...
    Status = property(get_Status, None)
class IBluetoothLEPreferredConnectionParametersStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParametersStatics'
    _iid_ = Guid('{0e3e8edc-2751-55aa-a838-8faeee818d72}')
    @winrt_commethod(6)
    def get_Balanced(self) -> win32more.Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParameters: ...
    @winrt_commethod(7)
    def get_ThroughputOptimized(self) -> win32more.Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParameters: ...
    @winrt_commethod(8)
    def get_PowerOptimized(self) -> win32more.Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParameters: ...
    Balanced = property(get_Balanced, None)
    PowerOptimized = property(get_PowerOptimized, None)
    ThroughputOptimized = property(get_ThroughputOptimized, None)
class IBluetoothSignalStrengthFilter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothSignalStrengthFilter'
    _iid_ = Guid('{df7b7391-6bb5-4cfe-90b1-5d7324edcf7f}')
    @winrt_commethod(6)
    def get_InRangeThresholdInDBm(self) -> win32more.Windows.Foundation.IReference[Int16]: ...
    @winrt_commethod(7)
    def put_InRangeThresholdInDBm(self, value: win32more.Windows.Foundation.IReference[Int16]) -> Void: ...
    @winrt_commethod(8)
    def get_OutOfRangeThresholdInDBm(self) -> win32more.Windows.Foundation.IReference[Int16]: ...
    @winrt_commethod(9)
    def put_OutOfRangeThresholdInDBm(self, value: win32more.Windows.Foundation.IReference[Int16]) -> Void: ...
    @winrt_commethod(10)
    def get_OutOfRangeTimeout(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(11)
    def put_OutOfRangeTimeout(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_commethod(12)
    def get_SamplingInterval(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(13)
    def put_SamplingInterval(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.TimeSpan]) -> Void: ...
    InRangeThresholdInDBm = property(get_InRangeThresholdInDBm, put_InRangeThresholdInDBm)
    OutOfRangeThresholdInDBm = property(get_OutOfRangeThresholdInDBm, put_OutOfRangeThresholdInDBm)
    OutOfRangeTimeout = property(get_OutOfRangeTimeout, put_OutOfRangeTimeout)
    SamplingInterval = property(get_SamplingInterval, put_SamplingInterval)
class IBluetoothUuidHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.IBluetoothUuidHelperStatics'
    _iid_ = Guid('{17df0cd8-cf74-4b21-afe6-f57a11bcdea0}')
    @winrt_commethod(6)
    def FromShortId(self, shortId: UInt32) -> Guid: ...
    @winrt_commethod(7)
    def TryGetShortId(self, uuid: Guid) -> win32more.Windows.Foundation.IReference[UInt32]: ...


make_ready(__name__)
