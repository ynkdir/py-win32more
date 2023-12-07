from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Gaming.Input
import win32more.Windows.Gaming.Input.Custom
import win32more.Windows.Storage.Streams
class GameControllerFactoryManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Custom.GameControllerFactoryManager'
    @winrt_classmethod
    def TryGetFactoryControllerFromGameController(cls: win32more.Windows.Gaming.Input.Custom.IGameControllerFactoryManagerStatics2, factory: win32more.Windows.Gaming.Input.Custom.ICustomGameControllerFactory, gameController: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.IGameController: ...
    @winrt_classmethod
    def RegisterCustomFactoryForGipInterface(cls: win32more.Windows.Gaming.Input.Custom.IGameControllerFactoryManagerStatics, factory: win32more.Windows.Gaming.Input.Custom.ICustomGameControllerFactory, interfaceId: Guid) -> Void: ...
    @winrt_classmethod
    def RegisterCustomFactoryForHardwareId(cls: win32more.Windows.Gaming.Input.Custom.IGameControllerFactoryManagerStatics, factory: win32more.Windows.Gaming.Input.Custom.ICustomGameControllerFactory, hardwareVendorId: UInt16, hardwareProductId: UInt16) -> Void: ...
    @winrt_classmethod
    def RegisterCustomFactoryForXusbType(cls: win32more.Windows.Gaming.Input.Custom.IGameControllerFactoryManagerStatics, factory: win32more.Windows.Gaming.Input.Custom.ICustomGameControllerFactory, xusbType: win32more.Windows.Gaming.Input.Custom.XusbDeviceType, xusbSubtype: win32more.Windows.Gaming.Input.Custom.XusbDeviceSubtype) -> Void: ...
class GameControllerVersionInfo(EasyCastStructure):
    Major: UInt16
    Minor: UInt16
    Build: UInt16
    Revision: UInt16
class GipFirmwareUpdateProgress(EasyCastStructure):
    PercentCompleted: Double
    CurrentComponentId: UInt32
class GipFirmwareUpdateResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Input.Custom.IGipFirmwareUpdateResult
    _classid_ = 'Windows.Gaming.Input.Custom.GipFirmwareUpdateResult'
    @winrt_mixinmethod
    def get_ExtendedErrorCode(self: win32more.Windows.Gaming.Input.Custom.IGipFirmwareUpdateResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_FinalComponentId(self: win32more.Windows.Gaming.Input.Custom.IGipFirmwareUpdateResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Gaming.Input.Custom.IGipFirmwareUpdateResult) -> win32more.Windows.Gaming.Input.Custom.GipFirmwareUpdateStatus: ...
    ExtendedErrorCode = property(get_ExtendedErrorCode, None)
    FinalComponentId = property(get_FinalComponentId, None)
    Status = property(get_Status, None)
GipFirmwareUpdateStatus = Int32
GipFirmwareUpdateStatus_Completed: GipFirmwareUpdateStatus = 0
GipFirmwareUpdateStatus_UpToDate: GipFirmwareUpdateStatus = 1
GipFirmwareUpdateStatus_Failed: GipFirmwareUpdateStatus = 2
class GipGameControllerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Input.Custom.IGipGameControllerProvider
    _classid_ = 'Windows.Gaming.Input.Custom.GipGameControllerProvider'
    @winrt_mixinmethod
    def SendMessage(self: win32more.Windows.Gaming.Input.Custom.IGipGameControllerProvider, messageClass: win32more.Windows.Gaming.Input.Custom.GipMessageClass, messageId: Byte, messageBuffer: Annotated[SZArray[Byte], 'In']) -> Void: ...
    @winrt_mixinmethod
    def SendReceiveMessage(self: win32more.Windows.Gaming.Input.Custom.IGipGameControllerProvider, messageClass: win32more.Windows.Gaming.Input.Custom.GipMessageClass, messageId: Byte, requestMessageBuffer: Annotated[SZArray[Byte], 'In'], responseMessageBuffer: Annotated[SZArray[Byte], 'Out']) -> Void: ...
    @winrt_mixinmethod
    def UpdateFirmwareAsync(self: win32more.Windows.Gaming.Input.Custom.IGipGameControllerProvider, firmwareImage: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Gaming.Input.Custom.GipFirmwareUpdateResult, win32more.Windows.Gaming.Input.Custom.GipFirmwareUpdateProgress]: ...
    @winrt_mixinmethod
    def get_FirmwareVersionInfo(self: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> win32more.Windows.Gaming.Input.Custom.GameControllerVersionInfo: ...
    @winrt_mixinmethod
    def get_HardwareProductId(self: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> UInt16: ...
    @winrt_mixinmethod
    def get_HardwareVendorId(self: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> UInt16: ...
    @winrt_mixinmethod
    def get_HardwareVersionInfo(self: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> win32more.Windows.Gaming.Input.Custom.GameControllerVersionInfo: ...
    @winrt_mixinmethod
    def get_IsConnected(self: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> Boolean: ...
    FirmwareVersionInfo = property(get_FirmwareVersionInfo, None)
    HardwareProductId = property(get_HardwareProductId, None)
    HardwareVendorId = property(get_HardwareVendorId, None)
    HardwareVersionInfo = property(get_HardwareVersionInfo, None)
    IsConnected = property(get_IsConnected, None)
GipMessageClass = Int32
GipMessageClass_Command: GipMessageClass = 0
GipMessageClass_LowLatency: GipMessageClass = 1
GipMessageClass_StandardLatency: GipMessageClass = 2
class HidGameControllerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Input.Custom.IHidGameControllerProvider
    _classid_ = 'Windows.Gaming.Input.Custom.HidGameControllerProvider'
    @winrt_mixinmethod
    def get_UsageId(self: win32more.Windows.Gaming.Input.Custom.IHidGameControllerProvider) -> UInt16: ...
    @winrt_mixinmethod
    def get_UsagePage(self: win32more.Windows.Gaming.Input.Custom.IHidGameControllerProvider) -> UInt16: ...
    @winrt_mixinmethod
    def GetFeatureReport(self: win32more.Windows.Gaming.Input.Custom.IHidGameControllerProvider, reportId: Byte, reportBuffer: Annotated[SZArray[Byte], 'Out']) -> Void: ...
    @winrt_mixinmethod
    def SendFeatureReport(self: win32more.Windows.Gaming.Input.Custom.IHidGameControllerProvider, reportId: Byte, reportBuffer: Annotated[SZArray[Byte], 'In']) -> Void: ...
    @winrt_mixinmethod
    def SendOutputReport(self: win32more.Windows.Gaming.Input.Custom.IHidGameControllerProvider, reportId: Byte, reportBuffer: Annotated[SZArray[Byte], 'In']) -> Void: ...
    @winrt_mixinmethod
    def get_FirmwareVersionInfo(self: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> win32more.Windows.Gaming.Input.Custom.GameControllerVersionInfo: ...
    @winrt_mixinmethod
    def get_HardwareProductId(self: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> UInt16: ...
    @winrt_mixinmethod
    def get_HardwareVendorId(self: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> UInt16: ...
    @winrt_mixinmethod
    def get_HardwareVersionInfo(self: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> win32more.Windows.Gaming.Input.Custom.GameControllerVersionInfo: ...
    @winrt_mixinmethod
    def get_IsConnected(self: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> Boolean: ...
    UsageId = property(get_UsageId, None)
    UsagePage = property(get_UsagePage, None)
    FirmwareVersionInfo = property(get_FirmwareVersionInfo, None)
    HardwareProductId = property(get_HardwareProductId, None)
    HardwareVendorId = property(get_HardwareVendorId, None)
    HardwareVersionInfo = property(get_HardwareVersionInfo, None)
    IsConnected = property(get_IsConnected, None)
class ICustomGameControllerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Custom.ICustomGameControllerFactory'
    _iid_ = Guid('{69a0ae5e-758e-4cbe-ace6-62155fe9126f}')
    @winrt_commethod(6)
    def CreateGameController(self, provider: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def OnGameControllerAdded(self, value: win32more.Windows.Gaming.Input.IGameController) -> Void: ...
    @winrt_commethod(8)
    def OnGameControllerRemoved(self, value: win32more.Windows.Gaming.Input.IGameController) -> Void: ...
class IGameControllerFactoryManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Custom.IGameControllerFactoryManagerStatics'
    _iid_ = Guid('{36cb66e3-d0a1-4986-a24c-40b137deba9e}')
    @winrt_commethod(6)
    def RegisterCustomFactoryForGipInterface(self, factory: win32more.Windows.Gaming.Input.Custom.ICustomGameControllerFactory, interfaceId: Guid) -> Void: ...
    @winrt_commethod(7)
    def RegisterCustomFactoryForHardwareId(self, factory: win32more.Windows.Gaming.Input.Custom.ICustomGameControllerFactory, hardwareVendorId: UInt16, hardwareProductId: UInt16) -> Void: ...
    @winrt_commethod(8)
    def RegisterCustomFactoryForXusbType(self, factory: win32more.Windows.Gaming.Input.Custom.ICustomGameControllerFactory, xusbType: win32more.Windows.Gaming.Input.Custom.XusbDeviceType, xusbSubtype: win32more.Windows.Gaming.Input.Custom.XusbDeviceSubtype) -> Void: ...
class IGameControllerFactoryManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Custom.IGameControllerFactoryManagerStatics2'
    _iid_ = Guid('{eace5644-19df-4115-b32a-2793e2aea3bb}')
    @winrt_commethod(6)
    def TryGetFactoryControllerFromGameController(self, factory: win32more.Windows.Gaming.Input.Custom.ICustomGameControllerFactory, gameController: win32more.Windows.Gaming.Input.IGameController) -> win32more.Windows.Gaming.Input.IGameController: ...
class IGameControllerInputSink(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Custom.IGameControllerInputSink'
    _iid_ = Guid('{1ff6f922-c640-4c78-a820-9a715c558bcb}')
    @winrt_commethod(6)
    def OnInputResumed(self, timestamp: UInt64) -> Void: ...
    @winrt_commethod(7)
    def OnInputSuspended(self, timestamp: UInt64) -> Void: ...
class IGameControllerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Custom.IGameControllerProvider'
    _iid_ = Guid('{e6d73982-2996-4559-b16c-3e57d46e58d6}')
    @winrt_commethod(6)
    def get_FirmwareVersionInfo(self) -> win32more.Windows.Gaming.Input.Custom.GameControllerVersionInfo: ...
    @winrt_commethod(7)
    def get_HardwareProductId(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_HardwareVendorId(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_HardwareVersionInfo(self) -> win32more.Windows.Gaming.Input.Custom.GameControllerVersionInfo: ...
    @winrt_commethod(10)
    def get_IsConnected(self) -> Boolean: ...
    FirmwareVersionInfo = property(get_FirmwareVersionInfo, None)
    HardwareProductId = property(get_HardwareProductId, None)
    HardwareVendorId = property(get_HardwareVendorId, None)
    HardwareVersionInfo = property(get_HardwareVersionInfo, None)
    IsConnected = property(get_IsConnected, None)
class IGipFirmwareUpdateResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Custom.IGipFirmwareUpdateResult'
    _iid_ = Guid('{6b794d32-8553-4292-8e03-e16651a2f8bc}')
    @winrt_commethod(6)
    def get_ExtendedErrorCode(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_FinalComponentId(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Status(self) -> win32more.Windows.Gaming.Input.Custom.GipFirmwareUpdateStatus: ...
    ExtendedErrorCode = property(get_ExtendedErrorCode, None)
    FinalComponentId = property(get_FinalComponentId, None)
    Status = property(get_Status, None)
class IGipGameControllerInputSink(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Custom.IGipGameControllerInputSink'
    _iid_ = Guid('{a2108abf-09f1-43bc-a140-80f899ec36fb}')
    @winrt_commethod(6)
    def OnKeyReceived(self, timestamp: UInt64, keyCode: Byte, isPressed: Boolean) -> Void: ...
    @winrt_commethod(7)
    def OnMessageReceived(self, timestamp: UInt64, messageClass: win32more.Windows.Gaming.Input.Custom.GipMessageClass, messageId: Byte, sequenceId: Byte, messageBuffer: Annotated[SZArray[Byte], 'In']) -> Void: ...
class IGipGameControllerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Custom.IGipGameControllerProvider'
    _iid_ = Guid('{dbcf1e19-1af5-45a8-bf02-a0ee50c823fc}')
    @winrt_commethod(6)
    def SendMessage(self, messageClass: win32more.Windows.Gaming.Input.Custom.GipMessageClass, messageId: Byte, messageBuffer: Annotated[SZArray[Byte], 'In']) -> Void: ...
    @winrt_commethod(7)
    def SendReceiveMessage(self, messageClass: win32more.Windows.Gaming.Input.Custom.GipMessageClass, messageId: Byte, requestMessageBuffer: Annotated[SZArray[Byte], 'In'], responseMessageBuffer: Annotated[SZArray[Byte], 'Out']) -> Void: ...
    @winrt_commethod(8)
    def UpdateFirmwareAsync(self, firmwareImage: win32more.Windows.Storage.Streams.IInputStream) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Gaming.Input.Custom.GipFirmwareUpdateResult, win32more.Windows.Gaming.Input.Custom.GipFirmwareUpdateProgress]: ...
class IHidGameControllerInputSink(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Custom.IHidGameControllerInputSink'
    _iid_ = Guid('{f754c322-182d-40e4-a126-fcee4ffa1e31}')
    @winrt_commethod(6)
    def OnInputReportReceived(self, timestamp: UInt64, reportId: Byte, reportBuffer: Annotated[SZArray[Byte], 'In']) -> Void: ...
class IHidGameControllerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Custom.IHidGameControllerProvider'
    _iid_ = Guid('{95ce3af4-abf0-4b68-a081-3b7de73ff0e7}')
    @winrt_commethod(6)
    def get_UsageId(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_UsagePage(self) -> UInt16: ...
    @winrt_commethod(8)
    def GetFeatureReport(self, reportId: Byte, reportBuffer: Annotated[SZArray[Byte], 'Out']) -> Void: ...
    @winrt_commethod(9)
    def SendFeatureReport(self, reportId: Byte, reportBuffer: Annotated[SZArray[Byte], 'In']) -> Void: ...
    @winrt_commethod(10)
    def SendOutputReport(self, reportId: Byte, reportBuffer: Annotated[SZArray[Byte], 'In']) -> Void: ...
    UsageId = property(get_UsageId, None)
    UsagePage = property(get_UsagePage, None)
class IXusbGameControllerInputSink(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Custom.IXusbGameControllerInputSink'
    _iid_ = Guid('{b2ac1d95-6ecb-42b3-8aab-025401ca4712}')
    @winrt_commethod(6)
    def OnInputReceived(self, timestamp: UInt64, reportId: Byte, inputBuffer: Annotated[SZArray[Byte], 'In']) -> Void: ...
class IXusbGameControllerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Gaming.Input.Custom.IXusbGameControllerProvider'
    _iid_ = Guid('{6e2971eb-0efb-48b4-808b-837643b2f216}')
    @winrt_commethod(6)
    def SetVibration(self, lowFrequencyMotorSpeed: Double, highFrequencyMotorSpeed: Double) -> Void: ...
XusbDeviceSubtype = Int32
XusbDeviceSubtype_Unknown: XusbDeviceSubtype = 0
XusbDeviceSubtype_Gamepad: XusbDeviceSubtype = 1
XusbDeviceSubtype_ArcadePad: XusbDeviceSubtype = 2
XusbDeviceSubtype_ArcadeStick: XusbDeviceSubtype = 3
XusbDeviceSubtype_FlightStick: XusbDeviceSubtype = 4
XusbDeviceSubtype_Wheel: XusbDeviceSubtype = 5
XusbDeviceSubtype_Guitar: XusbDeviceSubtype = 6
XusbDeviceSubtype_GuitarAlternate: XusbDeviceSubtype = 7
XusbDeviceSubtype_GuitarBass: XusbDeviceSubtype = 8
XusbDeviceSubtype_DrumKit: XusbDeviceSubtype = 9
XusbDeviceSubtype_DancePad: XusbDeviceSubtype = 10
XusbDeviceType = Int32
XusbDeviceType_Unknown: XusbDeviceType = 0
XusbDeviceType_Gamepad: XusbDeviceType = 1
class XusbGameControllerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Gaming.Input.Custom.IXusbGameControllerProvider
    _classid_ = 'Windows.Gaming.Input.Custom.XusbGameControllerProvider'
    @winrt_mixinmethod
    def SetVibration(self: win32more.Windows.Gaming.Input.Custom.IXusbGameControllerProvider, lowFrequencyMotorSpeed: Double, highFrequencyMotorSpeed: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FirmwareVersionInfo(self: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> win32more.Windows.Gaming.Input.Custom.GameControllerVersionInfo: ...
    @winrt_mixinmethod
    def get_HardwareProductId(self: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> UInt16: ...
    @winrt_mixinmethod
    def get_HardwareVendorId(self: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> UInt16: ...
    @winrt_mixinmethod
    def get_HardwareVersionInfo(self: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> win32more.Windows.Gaming.Input.Custom.GameControllerVersionInfo: ...
    @winrt_mixinmethod
    def get_IsConnected(self: win32more.Windows.Gaming.Input.Custom.IGameControllerProvider) -> Boolean: ...
    FirmwareVersionInfo = property(get_FirmwareVersionInfo, None)
    HardwareProductId = property(get_HardwareProductId, None)
    HardwareVendorId = property(get_HardwareVendorId, None)
    HardwareVersionInfo = property(get_HardwareVersionInfo, None)
    IsConnected = property(get_IsConnected, None)
make_ready(__name__)
