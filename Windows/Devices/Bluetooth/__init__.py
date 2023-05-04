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
import Windows.Devices.Bluetooth
import Windows.Devices.Bluetooth.GenericAttributeProfile
import Windows.Devices.Bluetooth.Rfcomm
import Windows.Devices.Enumeration
import Windows.Devices.Radios
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Networking
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
class BluetoothAdapter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothAdapter'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Bluetooth.IBluetoothAdapter) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BluetoothAddress(self: Windows.Devices.Bluetooth.IBluetoothAdapter) -> UInt64: ...
    @winrt_mixinmethod
    def get_IsClassicSupported(self: Windows.Devices.Bluetooth.IBluetoothAdapter) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsLowEnergySupported(self: Windows.Devices.Bluetooth.IBluetoothAdapter) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPeripheralRoleSupported(self: Windows.Devices.Bluetooth.IBluetoothAdapter) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCentralRoleSupported(self: Windows.Devices.Bluetooth.IBluetoothAdapter) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsAdvertisementOffloadSupported(self: Windows.Devices.Bluetooth.IBluetoothAdapter) -> Boolean: ...
    @winrt_mixinmethod
    def GetRadioAsync(self: Windows.Devices.Bluetooth.IBluetoothAdapter) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Radios.Radio]: ...
    @winrt_mixinmethod
    def get_AreClassicSecureConnectionsSupported(self: Windows.Devices.Bluetooth.IBluetoothAdapter2) -> Boolean: ...
    @winrt_mixinmethod
    def get_AreLowEnergySecureConnectionsSupported(self: Windows.Devices.Bluetooth.IBluetoothAdapter2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsExtendedAdvertisingSupported(self: Windows.Devices.Bluetooth.IBluetoothAdapter3) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxAdvertisementDataLength(self: Windows.Devices.Bluetooth.IBluetoothAdapter3) -> UInt32: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Bluetooth.IBluetoothAdapterStatics) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Bluetooth.IBluetoothAdapterStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.BluetoothAdapter]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.Bluetooth.IBluetoothAdapterStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.BluetoothAdapter]: ...
    DeviceId = property(get_DeviceId, None)
    BluetoothAddress = property(get_BluetoothAddress, None)
    IsClassicSupported = property(get_IsClassicSupported, None)
    IsLowEnergySupported = property(get_IsLowEnergySupported, None)
    IsPeripheralRoleSupported = property(get_IsPeripheralRoleSupported, None)
    IsCentralRoleSupported = property(get_IsCentralRoleSupported, None)
    IsAdvertisementOffloadSupported = property(get_IsAdvertisementOffloadSupported, None)
    AreClassicSecureConnectionsSupported = property(get_AreClassicSecureConnectionsSupported, None)
    AreLowEnergySecureConnectionsSupported = property(get_AreLowEnergySecureConnectionsSupported, None)
    IsExtendedAdvertisingSupported = property(get_IsExtendedAdvertisingSupported, None)
    MaxAdvertisementDataLength = property(get_MaxAdvertisementDataLength, None)
BluetoothAddressType = Int32
BluetoothAddressType_Public: BluetoothAddressType = 0
BluetoothAddressType_Random: BluetoothAddressType = 1
BluetoothAddressType_Unspecified: BluetoothAddressType = 2
BluetoothCacheMode = Int32
BluetoothCacheMode_Cached: BluetoothCacheMode = 0
BluetoothCacheMode_Uncached: BluetoothCacheMode = 1
class BluetoothClassOfDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothClassOfDevice'
    @winrt_mixinmethod
    def get_RawValue(self: Windows.Devices.Bluetooth.IBluetoothClassOfDevice) -> UInt32: ...
    @winrt_mixinmethod
    def get_MajorClass(self: Windows.Devices.Bluetooth.IBluetoothClassOfDevice) -> Windows.Devices.Bluetooth.BluetoothMajorClass: ...
    @winrt_mixinmethod
    def get_MinorClass(self: Windows.Devices.Bluetooth.IBluetoothClassOfDevice) -> Windows.Devices.Bluetooth.BluetoothMinorClass: ...
    @winrt_mixinmethod
    def get_ServiceCapabilities(self: Windows.Devices.Bluetooth.IBluetoothClassOfDevice) -> Windows.Devices.Bluetooth.BluetoothServiceCapabilities: ...
    @winrt_classmethod
    def FromRawValue(cls: Windows.Devices.Bluetooth.IBluetoothClassOfDeviceStatics, rawValue: UInt32) -> Windows.Devices.Bluetooth.BluetoothClassOfDevice: ...
    @winrt_classmethod
    def FromParts(cls: Windows.Devices.Bluetooth.IBluetoothClassOfDeviceStatics, majorClass: Windows.Devices.Bluetooth.BluetoothMajorClass, minorClass: Windows.Devices.Bluetooth.BluetoothMinorClass, serviceCapabilities: Windows.Devices.Bluetooth.BluetoothServiceCapabilities) -> Windows.Devices.Bluetooth.BluetoothClassOfDevice: ...
    RawValue = property(get_RawValue, None)
    MajorClass = property(get_MajorClass, None)
    MinorClass = property(get_MinorClass, None)
    ServiceCapabilities = property(get_ServiceCapabilities, None)
BluetoothConnectionStatus = Int32
BluetoothConnectionStatus_Disconnected: BluetoothConnectionStatus = 0
BluetoothConnectionStatus_Connected: BluetoothConnectionStatus = 1
class BluetoothDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothDevice'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Bluetooth.IBluetoothDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HostName(self: Windows.Devices.Bluetooth.IBluetoothDevice) -> Windows.Networking.HostName: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Devices.Bluetooth.IBluetoothDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ClassOfDevice(self: Windows.Devices.Bluetooth.IBluetoothDevice) -> Windows.Devices.Bluetooth.BluetoothClassOfDevice: ...
    @winrt_mixinmethod
    def get_SdpRecords(self: Windows.Devices.Bluetooth.IBluetoothDevice) -> Windows.Foundation.Collections.IVectorView[Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def get_RfcommServices(self: Windows.Devices.Bluetooth.IBluetoothDevice) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceService]: ...
    @winrt_mixinmethod
    def get_ConnectionStatus(self: Windows.Devices.Bluetooth.IBluetoothDevice) -> Windows.Devices.Bluetooth.BluetoothConnectionStatus: ...
    @winrt_mixinmethod
    def get_BluetoothAddress(self: Windows.Devices.Bluetooth.IBluetoothDevice) -> UInt64: ...
    @winrt_mixinmethod
    def add_NameChanged(self: Windows.Devices.Bluetooth.IBluetoothDevice, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.BluetoothDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NameChanged(self: Windows.Devices.Bluetooth.IBluetoothDevice, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SdpRecordsChanged(self: Windows.Devices.Bluetooth.IBluetoothDevice, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.BluetoothDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SdpRecordsChanged(self: Windows.Devices.Bluetooth.IBluetoothDevice, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ConnectionStatusChanged(self: Windows.Devices.Bluetooth.IBluetoothDevice, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.BluetoothDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionStatusChanged(self: Windows.Devices.Bluetooth.IBluetoothDevice, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceInformation(self: Windows.Devices.Bluetooth.IBluetoothDevice2) -> Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_DeviceAccessInformation(self: Windows.Devices.Bluetooth.IBluetoothDevice3) -> Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_mixinmethod
    def RequestAccessAsync(self: Windows.Devices.Bluetooth.IBluetoothDevice3) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceAccessStatus]: ...
    @winrt_mixinmethod
    def GetRfcommServicesAsync(self: Windows.Devices.Bluetooth.IBluetoothDevice3) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceServicesResult]: ...
    @winrt_mixinmethod
    def GetRfcommServicesWithCacheModeAsync(self: Windows.Devices.Bluetooth.IBluetoothDevice3, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceServicesResult]: ...
    @winrt_mixinmethod
    def GetRfcommServicesForIdAsync(self: Windows.Devices.Bluetooth.IBluetoothDevice3, serviceId: Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceServicesResult]: ...
    @winrt_mixinmethod
    def GetRfcommServicesForIdWithCacheModeAsync(self: Windows.Devices.Bluetooth.IBluetoothDevice3, serviceId: Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceServicesResult]: ...
    @winrt_mixinmethod
    def get_BluetoothDeviceId(self: Windows.Devices.Bluetooth.IBluetoothDevice4) -> Windows.Devices.Bluetooth.BluetoothDeviceId: ...
    @winrt_mixinmethod
    def get_WasSecureConnectionUsedForPairing(self: Windows.Devices.Bluetooth.IBluetoothDevice5) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelectorFromPairingState(cls: Windows.Devices.Bluetooth.IBluetoothDeviceStatics2, pairingState: Boolean) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromConnectionStatus(cls: Windows.Devices.Bluetooth.IBluetoothDeviceStatics2, connectionStatus: Windows.Devices.Bluetooth.BluetoothConnectionStatus) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromDeviceName(cls: Windows.Devices.Bluetooth.IBluetoothDeviceStatics2, deviceName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromBluetoothAddress(cls: Windows.Devices.Bluetooth.IBluetoothDeviceStatics2, bluetoothAddress: UInt64) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromClassOfDevice(cls: Windows.Devices.Bluetooth.IBluetoothDeviceStatics2, classOfDevice: Windows.Devices.Bluetooth.BluetoothClassOfDevice) -> WinRT_String: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Bluetooth.IBluetoothDeviceStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.BluetoothDevice]: ...
    @winrt_classmethod
    def FromHostNameAsync(cls: Windows.Devices.Bluetooth.IBluetoothDeviceStatics, hostName: Windows.Networking.HostName) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.BluetoothDevice]: ...
    @winrt_classmethod
    def FromBluetoothAddressAsync(cls: Windows.Devices.Bluetooth.IBluetoothDeviceStatics, address: UInt64) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.BluetoothDevice]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Bluetooth.IBluetoothDeviceStatics) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    HostName = property(get_HostName, None)
    Name = property(get_Name, None)
    ClassOfDevice = property(get_ClassOfDevice, None)
    SdpRecords = property(get_SdpRecords, None)
    RfcommServices = property(get_RfcommServices, None)
    ConnectionStatus = property(get_ConnectionStatus, None)
    BluetoothAddress = property(get_BluetoothAddress, None)
    DeviceInformation = property(get_DeviceInformation, None)
    DeviceAccessInformation = property(get_DeviceAccessInformation, None)
    BluetoothDeviceId = property(get_BluetoothDeviceId, None)
    WasSecureConnectionUsedForPairing = property(get_WasSecureConnectionUsedForPairing, None)
class BluetoothDeviceId(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothDeviceId'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Bluetooth.IBluetoothDeviceId) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsClassicDevice(self: Windows.Devices.Bluetooth.IBluetoothDeviceId) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsLowEnergyDevice(self: Windows.Devices.Bluetooth.IBluetoothDeviceId) -> Boolean: ...
    @winrt_classmethod
    def FromId(cls: Windows.Devices.Bluetooth.IBluetoothDeviceIdStatics, deviceId: WinRT_String) -> Windows.Devices.Bluetooth.BluetoothDeviceId: ...
    Id = property(get_Id, None)
    IsClassicDevice = property(get_IsClassicDevice, None)
    IsLowEnergyDevice = property(get_IsLowEnergyDevice, None)
BluetoothError = Int32
BluetoothError_Success: BluetoothError = 0
BluetoothError_RadioNotAvailable: BluetoothError = 1
BluetoothError_ResourceInUse: BluetoothError = 2
BluetoothError_DeviceNotConnected: BluetoothError = 3
BluetoothError_OtherError: BluetoothError = 4
BluetoothError_DisabledByPolicy: BluetoothError = 5
BluetoothError_NotSupported: BluetoothError = 6
BluetoothError_DisabledByUser: BluetoothError = 7
BluetoothError_ConsentRequired: BluetoothError = 8
BluetoothError_TransportNotSupported: BluetoothError = 9
class BluetoothLEAppearance(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothLEAppearance'
    @winrt_mixinmethod
    def get_RawValue(self: Windows.Devices.Bluetooth.IBluetoothLEAppearance) -> UInt16: ...
    @winrt_mixinmethod
    def get_Category(self: Windows.Devices.Bluetooth.IBluetoothLEAppearance) -> UInt16: ...
    @winrt_mixinmethod
    def get_SubCategory(self: Windows.Devices.Bluetooth.IBluetoothLEAppearance) -> UInt16: ...
    @winrt_classmethod
    def FromRawValue(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceStatics, rawValue: UInt16) -> Windows.Devices.Bluetooth.BluetoothLEAppearance: ...
    @winrt_classmethod
    def FromParts(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceStatics, appearanceCategory: UInt16, appearanceSubCategory: UInt16) -> Windows.Devices.Bluetooth.BluetoothLEAppearance: ...
    RawValue = property(get_RawValue, None)
    Category = property(get_Category, None)
    SubCategory = property(get_SubCategory, None)
class BluetoothLEAppearanceCategories(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothLEAppearanceCategories'
    @winrt_classmethod
    def get_Uncategorized(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Phone(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Computer(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Watch(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Clock(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Display(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_RemoteControl(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_EyeGlasses(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Tag(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Keyring(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_MediaPlayer(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_BarcodeScanner(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Thermometer(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_HeartRate(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_BloodPressure(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_HumanInterfaceDevice(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_GlucoseMeter(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_RunningWalking(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Cycling(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_PulseOximeter(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_WeightScale(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_OutdoorSportActivity(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceCategoriesStatics) -> UInt16: ...
    Uncategorized = property(get_Uncategorized, None)
    Phone = property(get_Phone, None)
    Computer = property(get_Computer, None)
    Watch = property(get_Watch, None)
    Clock = property(get_Clock, None)
    Display = property(get_Display, None)
    RemoteControl = property(get_RemoteControl, None)
    EyeGlasses = property(get_EyeGlasses, None)
    Tag = property(get_Tag, None)
    Keyring = property(get_Keyring, None)
    MediaPlayer = property(get_MediaPlayer, None)
    BarcodeScanner = property(get_BarcodeScanner, None)
    Thermometer = property(get_Thermometer, None)
    HeartRate = property(get_HeartRate, None)
    BloodPressure = property(get_BloodPressure, None)
    HumanInterfaceDevice = property(get_HumanInterfaceDevice, None)
    GlucoseMeter = property(get_GlucoseMeter, None)
    RunningWalking = property(get_RunningWalking, None)
    Cycling = property(get_Cycling, None)
    PulseOximeter = property(get_PulseOximeter, None)
    WeightScale = property(get_WeightScale, None)
    OutdoorSportActivity = property(get_OutdoorSportActivity, None)
class BluetoothLEAppearanceSubcategories(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothLEAppearanceSubcategories'
    @winrt_classmethod
    def get_Generic(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_SportsWatch(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_ThermometerEar(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_HeartRateBelt(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_BloodPressureArm(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_BloodPressureWrist(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Keyboard(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Mouse(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Joystick(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_Gamepad(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_DigitizerTablet(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_CardReader(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_DigitalPen(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_BarcodeScanner(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_RunningWalkingInShoe(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_RunningWalkingOnShoe(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_RunningWalkingOnHip(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_CyclingComputer(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_CyclingSpeedSensor(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_CyclingCadenceSensor(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_CyclingPowerSensor(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_CyclingSpeedCadenceSensor(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_OximeterFingertip(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_OximeterWristWorn(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_LocationDisplay(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_LocationNavigationDisplay(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_LocationPod(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    @winrt_classmethod
    def get_LocationNavigationPod(cls: Windows.Devices.Bluetooth.IBluetoothLEAppearanceSubcategoriesStatics) -> UInt16: ...
    Generic = property(get_Generic, None)
    SportsWatch = property(get_SportsWatch, None)
    ThermometerEar = property(get_ThermometerEar, None)
    HeartRateBelt = property(get_HeartRateBelt, None)
    BloodPressureArm = property(get_BloodPressureArm, None)
    BloodPressureWrist = property(get_BloodPressureWrist, None)
    Keyboard = property(get_Keyboard, None)
    Mouse = property(get_Mouse, None)
    Joystick = property(get_Joystick, None)
    Gamepad = property(get_Gamepad, None)
    DigitizerTablet = property(get_DigitizerTablet, None)
    CardReader = property(get_CardReader, None)
    DigitalPen = property(get_DigitalPen, None)
    BarcodeScanner = property(get_BarcodeScanner, None)
    RunningWalkingInShoe = property(get_RunningWalkingInShoe, None)
    RunningWalkingOnShoe = property(get_RunningWalkingOnShoe, None)
    RunningWalkingOnHip = property(get_RunningWalkingOnHip, None)
    CyclingComputer = property(get_CyclingComputer, None)
    CyclingSpeedSensor = property(get_CyclingSpeedSensor, None)
    CyclingCadenceSensor = property(get_CyclingCadenceSensor, None)
    CyclingPowerSensor = property(get_CyclingPowerSensor, None)
    CyclingSpeedCadenceSensor = property(get_CyclingSpeedCadenceSensor, None)
    OximeterFingertip = property(get_OximeterFingertip, None)
    OximeterWristWorn = property(get_OximeterWristWorn, None)
    LocationDisplay = property(get_LocationDisplay, None)
    LocationNavigationDisplay = property(get_LocationNavigationDisplay, None)
    LocationPod = property(get_LocationPod, None)
    LocationNavigationPod = property(get_LocationNavigationPod, None)
class BluetoothLEConnectionParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothLEConnectionParameters'
    @winrt_mixinmethod
    def get_LinkTimeout(self: Windows.Devices.Bluetooth.IBluetoothLEConnectionParameters) -> UInt16: ...
    @winrt_mixinmethod
    def get_ConnectionLatency(self: Windows.Devices.Bluetooth.IBluetoothLEConnectionParameters) -> UInt16: ...
    @winrt_mixinmethod
    def get_ConnectionInterval(self: Windows.Devices.Bluetooth.IBluetoothLEConnectionParameters) -> UInt16: ...
    LinkTimeout = property(get_LinkTimeout, None)
    ConnectionLatency = property(get_ConnectionLatency, None)
    ConnectionInterval = property(get_ConnectionInterval, None)
class BluetoothLEConnectionPhy(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothLEConnectionPhy'
    @winrt_mixinmethod
    def get_TransmitInfo(self: Windows.Devices.Bluetooth.IBluetoothLEConnectionPhy) -> Windows.Devices.Bluetooth.BluetoothLEConnectionPhyInfo: ...
    @winrt_mixinmethod
    def get_ReceiveInfo(self: Windows.Devices.Bluetooth.IBluetoothLEConnectionPhy) -> Windows.Devices.Bluetooth.BluetoothLEConnectionPhyInfo: ...
    TransmitInfo = property(get_TransmitInfo, None)
    ReceiveInfo = property(get_ReceiveInfo, None)
class BluetoothLEConnectionPhyInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothLEConnectionPhyInfo'
    @winrt_mixinmethod
    def get_IsUncoded1MPhy(self: Windows.Devices.Bluetooth.IBluetoothLEConnectionPhyInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsUncoded2MPhy(self: Windows.Devices.Bluetooth.IBluetoothLEConnectionPhyInfo) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCodedPhy(self: Windows.Devices.Bluetooth.IBluetoothLEConnectionPhyInfo) -> Boolean: ...
    IsUncoded1MPhy = property(get_IsUncoded1MPhy, None)
    IsUncoded2MPhy = property(get_IsUncoded2MPhy, None)
    IsCodedPhy = property(get_IsCodedPhy, None)
class BluetoothLEDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothLEDevice'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Bluetooth.IBluetoothLEDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Devices.Bluetooth.IBluetoothLEDevice) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_GattServices(self: Windows.Devices.Bluetooth.IBluetoothLEDevice) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_mixinmethod
    def get_ConnectionStatus(self: Windows.Devices.Bluetooth.IBluetoothLEDevice) -> Windows.Devices.Bluetooth.BluetoothConnectionStatus: ...
    @winrt_mixinmethod
    def get_BluetoothAddress(self: Windows.Devices.Bluetooth.IBluetoothLEDevice) -> UInt64: ...
    @winrt_mixinmethod
    def GetGattService(self: Windows.Devices.Bluetooth.IBluetoothLEDevice, serviceUuid: Guid) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService: ...
    @winrt_mixinmethod
    def add_NameChanged(self: Windows.Devices.Bluetooth.IBluetoothLEDevice, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.BluetoothLEDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NameChanged(self: Windows.Devices.Bluetooth.IBluetoothLEDevice, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GattServicesChanged(self: Windows.Devices.Bluetooth.IBluetoothLEDevice, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.BluetoothLEDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GattServicesChanged(self: Windows.Devices.Bluetooth.IBluetoothLEDevice, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ConnectionStatusChanged(self: Windows.Devices.Bluetooth.IBluetoothLEDevice, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.BluetoothLEDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionStatusChanged(self: Windows.Devices.Bluetooth.IBluetoothLEDevice, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DeviceInformation(self: Windows.Devices.Bluetooth.IBluetoothLEDevice2) -> Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_Appearance(self: Windows.Devices.Bluetooth.IBluetoothLEDevice2) -> Windows.Devices.Bluetooth.BluetoothLEAppearance: ...
    @winrt_mixinmethod
    def get_BluetoothAddressType(self: Windows.Devices.Bluetooth.IBluetoothLEDevice2) -> Windows.Devices.Bluetooth.BluetoothAddressType: ...
    @winrt_mixinmethod
    def get_DeviceAccessInformation(self: Windows.Devices.Bluetooth.IBluetoothLEDevice3) -> Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_mixinmethod
    def RequestAccessAsync(self: Windows.Devices.Bluetooth.IBluetoothLEDevice3) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceAccessStatus]: ...
    @winrt_mixinmethod
    def GetGattServicesAsync(self: Windows.Devices.Bluetooth.IBluetoothLEDevice3) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_mixinmethod
    def GetGattServicesWithCacheModeAsync(self: Windows.Devices.Bluetooth.IBluetoothLEDevice3, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_mixinmethod
    def GetGattServicesForUuidAsync(self: Windows.Devices.Bluetooth.IBluetoothLEDevice3, serviceUuid: Guid) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_mixinmethod
    def GetGattServicesForUuidWithCacheModeAsync(self: Windows.Devices.Bluetooth.IBluetoothLEDevice3, serviceUuid: Guid, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_mixinmethod
    def get_BluetoothDeviceId(self: Windows.Devices.Bluetooth.IBluetoothLEDevice4) -> Windows.Devices.Bluetooth.BluetoothDeviceId: ...
    @winrt_mixinmethod
    def get_WasSecureConnectionUsedForPairing(self: Windows.Devices.Bluetooth.IBluetoothLEDevice5) -> Boolean: ...
    @winrt_mixinmethod
    def GetConnectionParameters(self: Windows.Devices.Bluetooth.IBluetoothLEDevice6) -> Windows.Devices.Bluetooth.BluetoothLEConnectionParameters: ...
    @winrt_mixinmethod
    def GetConnectionPhy(self: Windows.Devices.Bluetooth.IBluetoothLEDevice6) -> Windows.Devices.Bluetooth.BluetoothLEConnectionPhy: ...
    @winrt_mixinmethod
    def RequestPreferredConnectionParameters(self: Windows.Devices.Bluetooth.IBluetoothLEDevice6, preferredConnectionParameters: Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParameters) -> Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParametersRequest: ...
    @winrt_mixinmethod
    def add_ConnectionParametersChanged(self: Windows.Devices.Bluetooth.IBluetoothLEDevice6, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.BluetoothLEDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionParametersChanged(self: Windows.Devices.Bluetooth.IBluetoothLEDevice6, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ConnectionPhyChanged(self: Windows.Devices.Bluetooth.IBluetoothLEDevice6, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.BluetoothLEDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ConnectionPhyChanged(self: Windows.Devices.Bluetooth.IBluetoothLEDevice6, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelectorFromPairingState(cls: Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics2, pairingState: Boolean) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromConnectionStatus(cls: Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics2, connectionStatus: Windows.Devices.Bluetooth.BluetoothConnectionStatus) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromDeviceName(cls: Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics2, deviceName: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromBluetoothAddress(cls: Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics2, bluetoothAddress: UInt64) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromBluetoothAddressWithBluetoothAddressType(cls: Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics2, bluetoothAddress: UInt64, bluetoothAddressType: Windows.Devices.Bluetooth.BluetoothAddressType) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorFromAppearance(cls: Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics2, appearance: Windows.Devices.Bluetooth.BluetoothLEAppearance) -> WinRT_String: ...
    @winrt_classmethod
    def FromBluetoothAddressWithBluetoothAddressTypeAsync(cls: Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics2, bluetoothAddress: UInt64, bluetoothAddressType: Windows.Devices.Bluetooth.BluetoothAddressType) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.BluetoothLEDevice]: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.BluetoothLEDevice]: ...
    @winrt_classmethod
    def FromBluetoothAddressAsync(cls: Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics, bluetoothAddress: UInt64) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.BluetoothLEDevice]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Bluetooth.IBluetoothLEDeviceStatics) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    Name = property(get_Name, None)
    GattServices = property(get_GattServices, None)
    ConnectionStatus = property(get_ConnectionStatus, None)
    BluetoothAddress = property(get_BluetoothAddress, None)
    DeviceInformation = property(get_DeviceInformation, None)
    Appearance = property(get_Appearance, None)
    BluetoothAddressType = property(get_BluetoothAddressType, None)
    DeviceAccessInformation = property(get_DeviceAccessInformation, None)
    BluetoothDeviceId = property(get_BluetoothDeviceId, None)
    WasSecureConnectionUsedForPairing = property(get_WasSecureConnectionUsedForPairing, None)
class BluetoothLEPreferredConnectionParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParameters'
    @winrt_mixinmethod
    def get_LinkTimeout(self: Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParameters) -> UInt16: ...
    @winrt_mixinmethod
    def get_ConnectionLatency(self: Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParameters) -> UInt16: ...
    @winrt_mixinmethod
    def get_MinConnectionInterval(self: Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParameters) -> UInt16: ...
    @winrt_mixinmethod
    def get_MaxConnectionInterval(self: Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParameters) -> UInt16: ...
    @winrt_classmethod
    def get_Balanced(cls: Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParametersStatics) -> Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParameters: ...
    @winrt_classmethod
    def get_ThroughputOptimized(cls: Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParametersStatics) -> Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParameters: ...
    @winrt_classmethod
    def get_PowerOptimized(cls: Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParametersStatics) -> Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParameters: ...
    LinkTimeout = property(get_LinkTimeout, None)
    ConnectionLatency = property(get_ConnectionLatency, None)
    MinConnectionInterval = property(get_MinConnectionInterval, None)
    MaxConnectionInterval = property(get_MaxConnectionInterval, None)
    Balanced = property(get_Balanced, None)
    ThroughputOptimized = property(get_ThroughputOptimized, None)
    PowerOptimized = property(get_PowerOptimized, None)
class BluetoothLEPreferredConnectionParametersRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParametersRequest'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Bluetooth.IBluetoothLEPreferredConnectionParametersRequest) -> Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParametersRequestStatus: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Status = property(get_Status, None)
BluetoothLEPreferredConnectionParametersRequestStatus = Int32
BluetoothLEPreferredConnectionParametersRequestStatus_Unspecified: BluetoothLEPreferredConnectionParametersRequestStatus = 0
BluetoothLEPreferredConnectionParametersRequestStatus_Success: BluetoothLEPreferredConnectionParametersRequestStatus = 1
BluetoothLEPreferredConnectionParametersRequestStatus_DeviceNotAvailable: BluetoothLEPreferredConnectionParametersRequestStatus = 2
BluetoothLEPreferredConnectionParametersRequestStatus_AccessDenied: BluetoothLEPreferredConnectionParametersRequestStatus = 3
BluetoothMajorClass = Int32
BluetoothMajorClass_Miscellaneous: BluetoothMajorClass = 0
BluetoothMajorClass_Computer: BluetoothMajorClass = 1
BluetoothMajorClass_Phone: BluetoothMajorClass = 2
BluetoothMajorClass_NetworkAccessPoint: BluetoothMajorClass = 3
BluetoothMajorClass_AudioVideo: BluetoothMajorClass = 4
BluetoothMajorClass_Peripheral: BluetoothMajorClass = 5
BluetoothMajorClass_Imaging: BluetoothMajorClass = 6
BluetoothMajorClass_Wearable: BluetoothMajorClass = 7
BluetoothMajorClass_Toy: BluetoothMajorClass = 8
BluetoothMajorClass_Health: BluetoothMajorClass = 9
BluetoothMinorClass = Int32
BluetoothMinorClass_Uncategorized: BluetoothMinorClass = 0
BluetoothMinorClass_ComputerDesktop: BluetoothMinorClass = 1
BluetoothMinorClass_ComputerServer: BluetoothMinorClass = 2
BluetoothMinorClass_ComputerLaptop: BluetoothMinorClass = 3
BluetoothMinorClass_ComputerHandheld: BluetoothMinorClass = 4
BluetoothMinorClass_ComputerPalmSize: BluetoothMinorClass = 5
BluetoothMinorClass_ComputerWearable: BluetoothMinorClass = 6
BluetoothMinorClass_ComputerTablet: BluetoothMinorClass = 7
BluetoothMinorClass_PhoneCellular: BluetoothMinorClass = 1
BluetoothMinorClass_PhoneCordless: BluetoothMinorClass = 2
BluetoothMinorClass_PhoneSmartPhone: BluetoothMinorClass = 3
BluetoothMinorClass_PhoneWired: BluetoothMinorClass = 4
BluetoothMinorClass_PhoneIsdn: BluetoothMinorClass = 5
BluetoothMinorClass_NetworkFullyAvailable: BluetoothMinorClass = 0
BluetoothMinorClass_NetworkUsed01To17Percent: BluetoothMinorClass = 8
BluetoothMinorClass_NetworkUsed17To33Percent: BluetoothMinorClass = 16
BluetoothMinorClass_NetworkUsed33To50Percent: BluetoothMinorClass = 24
BluetoothMinorClass_NetworkUsed50To67Percent: BluetoothMinorClass = 32
BluetoothMinorClass_NetworkUsed67To83Percent: BluetoothMinorClass = 40
BluetoothMinorClass_NetworkUsed83To99Percent: BluetoothMinorClass = 48
BluetoothMinorClass_NetworkNoServiceAvailable: BluetoothMinorClass = 56
BluetoothMinorClass_AudioVideoWearableHeadset: BluetoothMinorClass = 1
BluetoothMinorClass_AudioVideoHandsFree: BluetoothMinorClass = 2
BluetoothMinorClass_AudioVideoMicrophone: BluetoothMinorClass = 4
BluetoothMinorClass_AudioVideoLoudspeaker: BluetoothMinorClass = 5
BluetoothMinorClass_AudioVideoHeadphones: BluetoothMinorClass = 6
BluetoothMinorClass_AudioVideoPortableAudio: BluetoothMinorClass = 7
BluetoothMinorClass_AudioVideoCarAudio: BluetoothMinorClass = 8
BluetoothMinorClass_AudioVideoSetTopBox: BluetoothMinorClass = 9
BluetoothMinorClass_AudioVideoHifiAudioDevice: BluetoothMinorClass = 10
BluetoothMinorClass_AudioVideoVcr: BluetoothMinorClass = 11
BluetoothMinorClass_AudioVideoVideoCamera: BluetoothMinorClass = 12
BluetoothMinorClass_AudioVideoCamcorder: BluetoothMinorClass = 13
BluetoothMinorClass_AudioVideoVideoMonitor: BluetoothMinorClass = 14
BluetoothMinorClass_AudioVideoVideoDisplayAndLoudspeaker: BluetoothMinorClass = 15
BluetoothMinorClass_AudioVideoVideoConferencing: BluetoothMinorClass = 16
BluetoothMinorClass_AudioVideoGamingOrToy: BluetoothMinorClass = 18
BluetoothMinorClass_PeripheralJoystick: BluetoothMinorClass = 1
BluetoothMinorClass_PeripheralGamepad: BluetoothMinorClass = 2
BluetoothMinorClass_PeripheralRemoteControl: BluetoothMinorClass = 3
BluetoothMinorClass_PeripheralSensing: BluetoothMinorClass = 4
BluetoothMinorClass_PeripheralDigitizerTablet: BluetoothMinorClass = 5
BluetoothMinorClass_PeripheralCardReader: BluetoothMinorClass = 6
BluetoothMinorClass_PeripheralDigitalPen: BluetoothMinorClass = 7
BluetoothMinorClass_PeripheralHandheldScanner: BluetoothMinorClass = 8
BluetoothMinorClass_PeripheralHandheldGesture: BluetoothMinorClass = 9
BluetoothMinorClass_WearableWristwatch: BluetoothMinorClass = 1
BluetoothMinorClass_WearablePager: BluetoothMinorClass = 2
BluetoothMinorClass_WearableJacket: BluetoothMinorClass = 3
BluetoothMinorClass_WearableHelmet: BluetoothMinorClass = 4
BluetoothMinorClass_WearableGlasses: BluetoothMinorClass = 5
BluetoothMinorClass_ToyRobot: BluetoothMinorClass = 1
BluetoothMinorClass_ToyVehicle: BluetoothMinorClass = 2
BluetoothMinorClass_ToyDoll: BluetoothMinorClass = 3
BluetoothMinorClass_ToyController: BluetoothMinorClass = 4
BluetoothMinorClass_ToyGame: BluetoothMinorClass = 5
BluetoothMinorClass_HealthBloodPressureMonitor: BluetoothMinorClass = 1
BluetoothMinorClass_HealthThermometer: BluetoothMinorClass = 2
BluetoothMinorClass_HealthWeighingScale: BluetoothMinorClass = 3
BluetoothMinorClass_HealthGlucoseMeter: BluetoothMinorClass = 4
BluetoothMinorClass_HealthPulseOximeter: BluetoothMinorClass = 5
BluetoothMinorClass_HealthHeartRateMonitor: BluetoothMinorClass = 6
BluetoothMinorClass_HealthHealthDataDisplay: BluetoothMinorClass = 7
BluetoothMinorClass_HealthStepCounter: BluetoothMinorClass = 8
BluetoothMinorClass_HealthBodyCompositionAnalyzer: BluetoothMinorClass = 9
BluetoothMinorClass_HealthPeakFlowMonitor: BluetoothMinorClass = 10
BluetoothMinorClass_HealthMedicationMonitor: BluetoothMinorClass = 11
BluetoothMinorClass_HealthKneeProsthesis: BluetoothMinorClass = 12
BluetoothMinorClass_HealthAnkleProsthesis: BluetoothMinorClass = 13
BluetoothMinorClass_HealthGenericHealthManager: BluetoothMinorClass = 14
BluetoothMinorClass_HealthPersonalMobilityDevice: BluetoothMinorClass = 15
BluetoothServiceCapabilities = UInt32
BluetoothServiceCapabilities_None: BluetoothServiceCapabilities = 0
BluetoothServiceCapabilities_LimitedDiscoverableMode: BluetoothServiceCapabilities = 1
BluetoothServiceCapabilities_PositioningService: BluetoothServiceCapabilities = 8
BluetoothServiceCapabilities_NetworkingService: BluetoothServiceCapabilities = 16
BluetoothServiceCapabilities_RenderingService: BluetoothServiceCapabilities = 32
BluetoothServiceCapabilities_CapturingService: BluetoothServiceCapabilities = 64
BluetoothServiceCapabilities_ObjectTransferService: BluetoothServiceCapabilities = 128
BluetoothServiceCapabilities_AudioService: BluetoothServiceCapabilities = 256
BluetoothServiceCapabilities_TelephoneService: BluetoothServiceCapabilities = 512
BluetoothServiceCapabilities_InformationService: BluetoothServiceCapabilities = 1024
class BluetoothSignalStrengthFilter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Bluetooth.BluetoothSignalStrengthFilter: ...
    @winrt_mixinmethod
    def get_InRangeThresholdInDBm(self: Windows.Devices.Bluetooth.IBluetoothSignalStrengthFilter) -> Windows.Foundation.IReference[Int16]: ...
    @winrt_mixinmethod
    def put_InRangeThresholdInDBm(self: Windows.Devices.Bluetooth.IBluetoothSignalStrengthFilter, value: Windows.Foundation.IReference[Int16]) -> Void: ...
    @winrt_mixinmethod
    def get_OutOfRangeThresholdInDBm(self: Windows.Devices.Bluetooth.IBluetoothSignalStrengthFilter) -> Windows.Foundation.IReference[Int16]: ...
    @winrt_mixinmethod
    def put_OutOfRangeThresholdInDBm(self: Windows.Devices.Bluetooth.IBluetoothSignalStrengthFilter, value: Windows.Foundation.IReference[Int16]) -> Void: ...
    @winrt_mixinmethod
    def get_OutOfRangeTimeout(self: Windows.Devices.Bluetooth.IBluetoothSignalStrengthFilter) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_OutOfRangeTimeout(self: Windows.Devices.Bluetooth.IBluetoothSignalStrengthFilter, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_SamplingInterval(self: Windows.Devices.Bluetooth.IBluetoothSignalStrengthFilter) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_SamplingInterval(self: Windows.Devices.Bluetooth.IBluetoothSignalStrengthFilter, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    InRangeThresholdInDBm = property(get_InRangeThresholdInDBm, put_InRangeThresholdInDBm)
    OutOfRangeThresholdInDBm = property(get_OutOfRangeThresholdInDBm, put_OutOfRangeThresholdInDBm)
    OutOfRangeTimeout = property(get_OutOfRangeTimeout, put_OutOfRangeTimeout)
    SamplingInterval = property(get_SamplingInterval, put_SamplingInterval)
class BluetoothUuidHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Bluetooth.BluetoothUuidHelper'
    @winrt_classmethod
    def FromShortId(cls: Windows.Devices.Bluetooth.IBluetoothUuidHelperStatics, shortId: UInt32) -> Guid: ...
    @winrt_classmethod
    def TryGetShortId(cls: Windows.Devices.Bluetooth.IBluetoothUuidHelperStatics, uuid: Guid) -> Windows.Foundation.IReference[UInt32]: ...
class IBluetoothAdapter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    def GetRadioAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Radios.Radio]: ...
    DeviceId = property(get_DeviceId, None)
    BluetoothAddress = property(get_BluetoothAddress, None)
    IsClassicSupported = property(get_IsClassicSupported, None)
    IsLowEnergySupported = property(get_IsLowEnergySupported, None)
    IsPeripheralRoleSupported = property(get_IsPeripheralRoleSupported, None)
    IsCentralRoleSupported = property(get_IsCentralRoleSupported, None)
    IsAdvertisementOffloadSupported = property(get_IsAdvertisementOffloadSupported, None)
class IBluetoothAdapter2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ac94cecc-24d5-41b3-916d-1097c50b102b}')
    @winrt_commethod(6)
    def get_AreClassicSecureConnectionsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AreLowEnergySecureConnectionsSupported(self) -> Boolean: ...
    AreClassicSecureConnectionsSupported = property(get_AreClassicSecureConnectionsSupported, None)
    AreLowEnergySecureConnectionsSupported = property(get_AreLowEnergySecureConnectionsSupported, None)
class IBluetoothAdapter3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{8f8624e0-cba9-5211-9f89-3aac62b4c6b8}')
    @winrt_commethod(6)
    def get_IsExtendedAdvertisingSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_MaxAdvertisementDataLength(self) -> UInt32: ...
    IsExtendedAdvertisingSupported = property(get_IsExtendedAdvertisingSupported, None)
    MaxAdvertisementDataLength = property(get_MaxAdvertisementDataLength, None)
class IBluetoothAdapterStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{8b02fb6a-ac4c-4741-8661-8eab7d17ea9f}')
    @winrt_commethod(6)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.BluetoothAdapter]: ...
    @winrt_commethod(8)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.BluetoothAdapter]: ...
class IBluetoothClassOfDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d640227e-d7d7-4661-9454-65039ca17a2b}')
    @winrt_commethod(6)
    def get_RawValue(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_MajorClass(self) -> Windows.Devices.Bluetooth.BluetoothMajorClass: ...
    @winrt_commethod(8)
    def get_MinorClass(self) -> Windows.Devices.Bluetooth.BluetoothMinorClass: ...
    @winrt_commethod(9)
    def get_ServiceCapabilities(self) -> Windows.Devices.Bluetooth.BluetoothServiceCapabilities: ...
    RawValue = property(get_RawValue, None)
    MajorClass = property(get_MajorClass, None)
    MinorClass = property(get_MinorClass, None)
    ServiceCapabilities = property(get_ServiceCapabilities, None)
class IBluetoothClassOfDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e46135bd-0fa2-416c-91b4-c1e48ca061c1}')
    @winrt_commethod(6)
    def FromRawValue(self, rawValue: UInt32) -> Windows.Devices.Bluetooth.BluetoothClassOfDevice: ...
    @winrt_commethod(7)
    def FromParts(self, majorClass: Windows.Devices.Bluetooth.BluetoothMajorClass, minorClass: Windows.Devices.Bluetooth.BluetoothMinorClass, serviceCapabilities: Windows.Devices.Bluetooth.BluetoothServiceCapabilities) -> Windows.Devices.Bluetooth.BluetoothClassOfDevice: ...
class IBluetoothDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2335b156-90d2-4a04-aef5-0e20b9e6b707}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_HostName(self) -> Windows.Networking.HostName: ...
    @winrt_commethod(8)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ClassOfDevice(self) -> Windows.Devices.Bluetooth.BluetoothClassOfDevice: ...
    @winrt_commethod(10)
    def get_SdpRecords(self) -> Windows.Foundation.Collections.IVectorView[Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(11)
    def get_RfcommServices(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceService]: ...
    @winrt_commethod(12)
    def get_ConnectionStatus(self) -> Windows.Devices.Bluetooth.BluetoothConnectionStatus: ...
    @winrt_commethod(13)
    def get_BluetoothAddress(self) -> UInt64: ...
    @winrt_commethod(14)
    def add_NameChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.BluetoothDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_NameChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_SdpRecordsChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.BluetoothDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_SdpRecordsChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_ConnectionStatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.BluetoothDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_ConnectionStatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    HostName = property(get_HostName, None)
    Name = property(get_Name, None)
    ClassOfDevice = property(get_ClassOfDevice, None)
    SdpRecords = property(get_SdpRecords, None)
    RfcommServices = property(get_RfcommServices, None)
    ConnectionStatus = property(get_ConnectionStatus, None)
    BluetoothAddress = property(get_BluetoothAddress, None)
class IBluetoothDevice2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0133f954-b156-4dd0-b1f5-c11bc31a5163}')
    @winrt_commethod(6)
    def get_DeviceInformation(self) -> Windows.Devices.Enumeration.DeviceInformation: ...
    DeviceInformation = property(get_DeviceInformation, None)
class IBluetoothDevice3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{57fff78b-651a-4454-b90f-eb21ef0b0d71}')
    @winrt_commethod(6)
    def get_DeviceAccessInformation(self) -> Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_commethod(7)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceAccessStatus]: ...
    @winrt_commethod(8)
    def GetRfcommServicesAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceServicesResult]: ...
    @winrt_commethod(9)
    def GetRfcommServicesWithCacheModeAsync(self, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceServicesResult]: ...
    @winrt_commethod(10)
    def GetRfcommServicesForIdAsync(self, serviceId: Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceServicesResult]: ...
    @winrt_commethod(11)
    def GetRfcommServicesForIdWithCacheModeAsync(self, serviceId: Windows.Devices.Bluetooth.Rfcomm.RfcommServiceId, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.Rfcomm.RfcommDeviceServicesResult]: ...
    DeviceAccessInformation = property(get_DeviceAccessInformation, None)
class IBluetoothDevice4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{817c34ad-0e9c-42b2-a8dc-3e8094940d12}')
    @winrt_commethod(6)
    def get_BluetoothDeviceId(self) -> Windows.Devices.Bluetooth.BluetoothDeviceId: ...
    BluetoothDeviceId = property(get_BluetoothDeviceId, None)
class IBluetoothDevice5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b5e0b385-5e85-4559-a10d-1c7281379f96}')
    @winrt_commethod(6)
    def get_WasSecureConnectionUsedForPairing(self) -> Boolean: ...
    WasSecureConnectionUsedForPairing = property(get_WasSecureConnectionUsedForPairing, None)
class IBluetoothDeviceId(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a7884e67-3efb-4f31-bbc2-810e09977404}')
    @winrt_commethod(6)
    def FromId(self, deviceId: WinRT_String) -> Windows.Devices.Bluetooth.BluetoothDeviceId: ...
class IBluetoothDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0991df51-57db-4725-bbd7-84f64327ec2c}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.BluetoothDevice]: ...
    @winrt_commethod(7)
    def FromHostNameAsync(self, hostName: Windows.Networking.HostName) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.BluetoothDevice]: ...
    @winrt_commethod(8)
    def FromBluetoothAddressAsync(self, address: UInt64) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.BluetoothDevice]: ...
    @winrt_commethod(9)
    def GetDeviceSelector(self) -> WinRT_String: ...
class IBluetoothDeviceStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c29e8e2f-4e14-4477-aa1b-b8b47e5b7ece}')
    @winrt_commethod(6)
    def GetDeviceSelectorFromPairingState(self, pairingState: Boolean) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorFromConnectionStatus(self, connectionStatus: Windows.Devices.Bluetooth.BluetoothConnectionStatus) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetDeviceSelectorFromDeviceName(self, deviceName: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetDeviceSelectorFromBluetoothAddress(self, bluetoothAddress: UInt64) -> WinRT_String: ...
    @winrt_commethod(10)
    def GetDeviceSelectorFromClassOfDevice(self, classOfDevice: Windows.Devices.Bluetooth.BluetoothClassOfDevice) -> WinRT_String: ...
class IBluetoothLEAppearance(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5d2079f2-66a8-4258-985e-02b4d9509f18}')
    @winrt_commethod(6)
    def get_RawValue(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_Category(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_SubCategory(self) -> UInt16: ...
    RawValue = property(get_RawValue, None)
    Category = property(get_Category, None)
    SubCategory = property(get_SubCategory, None)
class IBluetoothLEAppearanceCategoriesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    Uncategorized = property(get_Uncategorized, None)
    Phone = property(get_Phone, None)
    Computer = property(get_Computer, None)
    Watch = property(get_Watch, None)
    Clock = property(get_Clock, None)
    Display = property(get_Display, None)
    RemoteControl = property(get_RemoteControl, None)
    EyeGlasses = property(get_EyeGlasses, None)
    Tag = property(get_Tag, None)
    Keyring = property(get_Keyring, None)
    MediaPlayer = property(get_MediaPlayer, None)
    BarcodeScanner = property(get_BarcodeScanner, None)
    Thermometer = property(get_Thermometer, None)
    HeartRate = property(get_HeartRate, None)
    BloodPressure = property(get_BloodPressure, None)
    HumanInterfaceDevice = property(get_HumanInterfaceDevice, None)
    GlucoseMeter = property(get_GlucoseMeter, None)
    RunningWalking = property(get_RunningWalking, None)
    Cycling = property(get_Cycling, None)
    PulseOximeter = property(get_PulseOximeter, None)
    WeightScale = property(get_WeightScale, None)
    OutdoorSportActivity = property(get_OutdoorSportActivity, None)
class IBluetoothLEAppearanceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{a193c0c7-4504-4f4a-9ba5-cd1054e5e065}')
    @winrt_commethod(6)
    def FromRawValue(self, rawValue: UInt16) -> Windows.Devices.Bluetooth.BluetoothLEAppearance: ...
    @winrt_commethod(7)
    def FromParts(self, appearanceCategory: UInt16, appearanceSubCategory: UInt16) -> Windows.Devices.Bluetooth.BluetoothLEAppearance: ...
class IBluetoothLEAppearanceSubcategoriesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    Generic = property(get_Generic, None)
    SportsWatch = property(get_SportsWatch, None)
    ThermometerEar = property(get_ThermometerEar, None)
    HeartRateBelt = property(get_HeartRateBelt, None)
    BloodPressureArm = property(get_BloodPressureArm, None)
    BloodPressureWrist = property(get_BloodPressureWrist, None)
    Keyboard = property(get_Keyboard, None)
    Mouse = property(get_Mouse, None)
    Joystick = property(get_Joystick, None)
    Gamepad = property(get_Gamepad, None)
    DigitizerTablet = property(get_DigitizerTablet, None)
    CardReader = property(get_CardReader, None)
    DigitalPen = property(get_DigitalPen, None)
    BarcodeScanner = property(get_BarcodeScanner, None)
    RunningWalkingInShoe = property(get_RunningWalkingInShoe, None)
    RunningWalkingOnShoe = property(get_RunningWalkingOnShoe, None)
    RunningWalkingOnHip = property(get_RunningWalkingOnHip, None)
    CyclingComputer = property(get_CyclingComputer, None)
    CyclingSpeedSensor = property(get_CyclingSpeedSensor, None)
    CyclingCadenceSensor = property(get_CyclingCadenceSensor, None)
    CyclingPowerSensor = property(get_CyclingPowerSensor, None)
    CyclingSpeedCadenceSensor = property(get_CyclingSpeedCadenceSensor, None)
    OximeterFingertip = property(get_OximeterFingertip, None)
    OximeterWristWorn = property(get_OximeterWristWorn, None)
    LocationDisplay = property(get_LocationDisplay, None)
    LocationNavigationDisplay = property(get_LocationNavigationDisplay, None)
    LocationPod = property(get_LocationPod, None)
    LocationNavigationPod = property(get_LocationNavigationPod, None)
class IBluetoothLEConnectionParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{33cb0771-8da9-508f-a366-1ca388c929ab}')
    @winrt_commethod(6)
    def get_LinkTimeout(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_ConnectionLatency(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_ConnectionInterval(self) -> UInt16: ...
    LinkTimeout = property(get_LinkTimeout, None)
    ConnectionLatency = property(get_ConnectionLatency, None)
    ConnectionInterval = property(get_ConnectionInterval, None)
class IBluetoothLEConnectionPhy(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{781e5e48-621e-5a7e-8be6-1b9561ff63c9}')
    @winrt_commethod(6)
    def get_TransmitInfo(self) -> Windows.Devices.Bluetooth.BluetoothLEConnectionPhyInfo: ...
    @winrt_commethod(7)
    def get_ReceiveInfo(self) -> Windows.Devices.Bluetooth.BluetoothLEConnectionPhyInfo: ...
    TransmitInfo = property(get_TransmitInfo, None)
    ReceiveInfo = property(get_ReceiveInfo, None)
class IBluetoothLEConnectionPhyInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9a100bdd-602e-5c27-a1ae-b230015a6394}')
    @winrt_commethod(6)
    def get_IsUncoded1MPhy(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsUncoded2MPhy(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsCodedPhy(self) -> Boolean: ...
    IsUncoded1MPhy = property(get_IsUncoded1MPhy, None)
    IsUncoded2MPhy = property(get_IsUncoded2MPhy, None)
    IsCodedPhy = property(get_IsCodedPhy, None)
class IBluetoothLEDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b5ee2f7b-4ad8-4642-ac48-80a0b500e887}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_GattServices(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService]: ...
    @winrt_commethod(9)
    def get_ConnectionStatus(self) -> Windows.Devices.Bluetooth.BluetoothConnectionStatus: ...
    @winrt_commethod(10)
    def get_BluetoothAddress(self) -> UInt64: ...
    @winrt_commethod(11)
    def GetGattService(self, serviceUuid: Guid) -> Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceService: ...
    @winrt_commethod(12)
    def add_NameChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.BluetoothLEDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_NameChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_GattServicesChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.BluetoothLEDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_GattServicesChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_ConnectionStatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.BluetoothLEDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_ConnectionStatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    Name = property(get_Name, None)
    GattServices = property(get_GattServices, None)
    ConnectionStatus = property(get_ConnectionStatus, None)
    BluetoothAddress = property(get_BluetoothAddress, None)
class IBluetoothLEDevice2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{26f062b3-7aee-4d31-baba-b1b9775f5916}')
    @winrt_commethod(6)
    def get_DeviceInformation(self) -> Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_commethod(7)
    def get_Appearance(self) -> Windows.Devices.Bluetooth.BluetoothLEAppearance: ...
    @winrt_commethod(8)
    def get_BluetoothAddressType(self) -> Windows.Devices.Bluetooth.BluetoothAddressType: ...
    DeviceInformation = property(get_DeviceInformation, None)
    Appearance = property(get_Appearance, None)
    BluetoothAddressType = property(get_BluetoothAddressType, None)
class IBluetoothLEDevice3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{aee9e493-44ac-40dc-af33-b2c13c01ca46}')
    @winrt_commethod(6)
    def get_DeviceAccessInformation(self) -> Windows.Devices.Enumeration.DeviceAccessInformation: ...
    @winrt_commethod(7)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Enumeration.DeviceAccessStatus]: ...
    @winrt_commethod(8)
    def GetGattServicesAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_commethod(9)
    def GetGattServicesWithCacheModeAsync(self, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_commethod(10)
    def GetGattServicesForUuidAsync(self, serviceUuid: Guid) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    @winrt_commethod(11)
    def GetGattServicesForUuidWithCacheModeAsync(self, serviceUuid: Guid, cacheMode: Windows.Devices.Bluetooth.BluetoothCacheMode) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.GenericAttributeProfile.GattDeviceServicesResult]: ...
    DeviceAccessInformation = property(get_DeviceAccessInformation, None)
class IBluetoothLEDevice4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2b605031-2248-4b2f-acf0-7cee36fc5870}')
    @winrt_commethod(6)
    def get_BluetoothDeviceId(self) -> Windows.Devices.Bluetooth.BluetoothDeviceId: ...
    BluetoothDeviceId = property(get_BluetoothDeviceId, None)
class IBluetoothLEDevice5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9d6a1260-5287-458e-95ba-17c8b7bb326e}')
    @winrt_commethod(6)
    def get_WasSecureConnectionUsedForPairing(self) -> Boolean: ...
    WasSecureConnectionUsedForPairing = property(get_WasSecureConnectionUsedForPairing, None)
class IBluetoothLEDevice6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ca7190ef-0cae-573c-a1ca-e1fc5bfc39e2}')
    @winrt_commethod(6)
    def GetConnectionParameters(self) -> Windows.Devices.Bluetooth.BluetoothLEConnectionParameters: ...
    @winrt_commethod(7)
    def GetConnectionPhy(self) -> Windows.Devices.Bluetooth.BluetoothLEConnectionPhy: ...
    @winrt_commethod(8)
    def RequestPreferredConnectionParameters(self, preferredConnectionParameters: Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParameters) -> Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParametersRequest: ...
    @winrt_commethod(9)
    def add_ConnectionParametersChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.BluetoothLEDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_ConnectionParametersChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_ConnectionPhyChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Bluetooth.BluetoothLEDevice, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_ConnectionPhyChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IBluetoothLEDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c8cf1a19-f0b6-4bf0-8689-41303de2d9f4}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.BluetoothLEDevice]: ...
    @winrt_commethod(7)
    def FromBluetoothAddressAsync(self, bluetoothAddress: UInt64) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.BluetoothLEDevice]: ...
    @winrt_commethod(8)
    def GetDeviceSelector(self) -> WinRT_String: ...
class IBluetoothLEDeviceStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5f12c06b-3bac-43e8-ad16-563271bd41c2}')
    @winrt_commethod(6)
    def GetDeviceSelectorFromPairingState(self, pairingState: Boolean) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetDeviceSelectorFromConnectionStatus(self, connectionStatus: Windows.Devices.Bluetooth.BluetoothConnectionStatus) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetDeviceSelectorFromDeviceName(self, deviceName: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetDeviceSelectorFromBluetoothAddress(self, bluetoothAddress: UInt64) -> WinRT_String: ...
    @winrt_commethod(10)
    def GetDeviceSelectorFromBluetoothAddressWithBluetoothAddressType(self, bluetoothAddress: UInt64, bluetoothAddressType: Windows.Devices.Bluetooth.BluetoothAddressType) -> WinRT_String: ...
    @winrt_commethod(11)
    def GetDeviceSelectorFromAppearance(self, appearance: Windows.Devices.Bluetooth.BluetoothLEAppearance) -> WinRT_String: ...
    @winrt_commethod(12)
    def FromBluetoothAddressWithBluetoothAddressTypeAsync(self, bluetoothAddress: UInt64, bluetoothAddressType: Windows.Devices.Bluetooth.BluetoothAddressType) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Bluetooth.BluetoothLEDevice]: ...
class IBluetoothLEPreferredConnectionParameters(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f2f44344-7372-5f7b-9b34-29c944f5a715}')
    @winrt_commethod(6)
    def get_LinkTimeout(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_ConnectionLatency(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_MinConnectionInterval(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_MaxConnectionInterval(self) -> UInt16: ...
    LinkTimeout = property(get_LinkTimeout, None)
    ConnectionLatency = property(get_ConnectionLatency, None)
    MinConnectionInterval = property(get_MinConnectionInterval, None)
    MaxConnectionInterval = property(get_MaxConnectionInterval, None)
class IBluetoothLEPreferredConnectionParametersRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{8a375276-a528-5266-b661-cce6a5ff9739}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParametersRequestStatus: ...
    Status = property(get_Status, None)
class IBluetoothLEPreferredConnectionParametersStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0e3e8edc-2751-55aa-a838-8faeee818d72}')
    @winrt_commethod(6)
    def get_Balanced(self) -> Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParameters: ...
    @winrt_commethod(7)
    def get_ThroughputOptimized(self) -> Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParameters: ...
    @winrt_commethod(8)
    def get_PowerOptimized(self) -> Windows.Devices.Bluetooth.BluetoothLEPreferredConnectionParameters: ...
    Balanced = property(get_Balanced, None)
    ThroughputOptimized = property(get_ThroughputOptimized, None)
    PowerOptimized = property(get_PowerOptimized, None)
class IBluetoothSignalStrengthFilter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{df7b7391-6bb5-4cfe-90b1-5d7324edcf7f}')
    @winrt_commethod(6)
    def get_InRangeThresholdInDBm(self) -> Windows.Foundation.IReference[Int16]: ...
    @winrt_commethod(7)
    def put_InRangeThresholdInDBm(self, value: Windows.Foundation.IReference[Int16]) -> Void: ...
    @winrt_commethod(8)
    def get_OutOfRangeThresholdInDBm(self) -> Windows.Foundation.IReference[Int16]: ...
    @winrt_commethod(9)
    def put_OutOfRangeThresholdInDBm(self, value: Windows.Foundation.IReference[Int16]) -> Void: ...
    @winrt_commethod(10)
    def get_OutOfRangeTimeout(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(11)
    def put_OutOfRangeTimeout(self, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_commethod(12)
    def get_SamplingInterval(self) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(13)
    def put_SamplingInterval(self, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    InRangeThresholdInDBm = property(get_InRangeThresholdInDBm, put_InRangeThresholdInDBm)
    OutOfRangeThresholdInDBm = property(get_OutOfRangeThresholdInDBm, put_OutOfRangeThresholdInDBm)
    OutOfRangeTimeout = property(get_OutOfRangeTimeout, put_OutOfRangeTimeout)
    SamplingInterval = property(get_SamplingInterval, put_SamplingInterval)
class IBluetoothUuidHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{17df0cd8-cf74-4b21-afe6-f57a11bcdea0}')
    @winrt_commethod(6)
    def FromShortId(self, shortId: UInt32) -> Guid: ...
    @winrt_commethod(7)
    def TryGetShortId(self, uuid: Guid) -> Windows.Foundation.IReference[UInt32]: ...
make_head(_module, 'BluetoothAdapter')
make_head(_module, 'BluetoothClassOfDevice')
make_head(_module, 'BluetoothDevice')
make_head(_module, 'BluetoothDeviceId')
make_head(_module, 'BluetoothLEAppearance')
make_head(_module, 'BluetoothLEAppearanceCategories')
make_head(_module, 'BluetoothLEAppearanceSubcategories')
make_head(_module, 'BluetoothLEConnectionParameters')
make_head(_module, 'BluetoothLEConnectionPhy')
make_head(_module, 'BluetoothLEConnectionPhyInfo')
make_head(_module, 'BluetoothLEDevice')
make_head(_module, 'BluetoothLEPreferredConnectionParameters')
make_head(_module, 'BluetoothLEPreferredConnectionParametersRequest')
make_head(_module, 'BluetoothSignalStrengthFilter')
make_head(_module, 'BluetoothUuidHelper')
make_head(_module, 'IBluetoothAdapter')
make_head(_module, 'IBluetoothAdapter2')
make_head(_module, 'IBluetoothAdapter3')
make_head(_module, 'IBluetoothAdapterStatics')
make_head(_module, 'IBluetoothClassOfDevice')
make_head(_module, 'IBluetoothClassOfDeviceStatics')
make_head(_module, 'IBluetoothDevice')
make_head(_module, 'IBluetoothDevice2')
make_head(_module, 'IBluetoothDevice3')
make_head(_module, 'IBluetoothDevice4')
make_head(_module, 'IBluetoothDevice5')
make_head(_module, 'IBluetoothDeviceId')
make_head(_module, 'IBluetoothDeviceIdStatics')
make_head(_module, 'IBluetoothDeviceStatics')
make_head(_module, 'IBluetoothDeviceStatics2')
make_head(_module, 'IBluetoothLEAppearance')
make_head(_module, 'IBluetoothLEAppearanceCategoriesStatics')
make_head(_module, 'IBluetoothLEAppearanceStatics')
make_head(_module, 'IBluetoothLEAppearanceSubcategoriesStatics')
make_head(_module, 'IBluetoothLEConnectionParameters')
make_head(_module, 'IBluetoothLEConnectionPhy')
make_head(_module, 'IBluetoothLEConnectionPhyInfo')
make_head(_module, 'IBluetoothLEDevice')
make_head(_module, 'IBluetoothLEDevice2')
make_head(_module, 'IBluetoothLEDevice3')
make_head(_module, 'IBluetoothLEDevice4')
make_head(_module, 'IBluetoothLEDevice5')
make_head(_module, 'IBluetoothLEDevice6')
make_head(_module, 'IBluetoothLEDeviceStatics')
make_head(_module, 'IBluetoothLEDeviceStatics2')
make_head(_module, 'IBluetoothLEPreferredConnectionParameters')
make_head(_module, 'IBluetoothLEPreferredConnectionParametersRequest')
make_head(_module, 'IBluetoothLEPreferredConnectionParametersStatics')
make_head(_module, 'IBluetoothSignalStrengthFilter')
make_head(_module, 'IBluetoothUuidHelperStatics')
