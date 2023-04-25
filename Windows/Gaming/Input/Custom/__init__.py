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
import Windows.Foundation
import Windows.Gaming.Input
import Windows.Gaming.Input.Custom
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
class GameControllerFactoryManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Gaming.Input.Custom.GameControllerFactoryManager'
    @winrt_classmethod
    def TryGetFactoryControllerFromGameController(cls: Windows.Gaming.Input.Custom.IGameControllerFactoryManagerStatics2, factory: Windows.Gaming.Input.Custom.ICustomGameControllerFactory, gameController: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.IGameController: ...
    @winrt_classmethod
    def RegisterCustomFactoryForGipInterface(cls: Windows.Gaming.Input.Custom.IGameControllerFactoryManagerStatics, factory: Windows.Gaming.Input.Custom.ICustomGameControllerFactory, interfaceId: Guid) -> Void: ...
    @winrt_classmethod
    def RegisterCustomFactoryForHardwareId(cls: Windows.Gaming.Input.Custom.IGameControllerFactoryManagerStatics, factory: Windows.Gaming.Input.Custom.ICustomGameControllerFactory, hardwareVendorId: UInt16, hardwareProductId: UInt16) -> Void: ...
    @winrt_classmethod
    def RegisterCustomFactoryForXusbType(cls: Windows.Gaming.Input.Custom.IGameControllerFactoryManagerStatics, factory: Windows.Gaming.Input.Custom.ICustomGameControllerFactory, xusbType: Windows.Gaming.Input.Custom.XusbDeviceType, xusbSubtype: Windows.Gaming.Input.Custom.XusbDeviceSubtype) -> Void: ...
class GameControllerVersionInfo(EasyCastStructure):
    Major: UInt16
    Minor: UInt16
    Build: UInt16
    Revision: UInt16
class GipFirmwareUpdateProgress(EasyCastStructure):
    PercentCompleted: Double
    CurrentComponentId: UInt32
class GipFirmwareUpdateResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Gaming.Input.Custom.GipFirmwareUpdateResult'
    @winrt_mixinmethod
    def get_ExtendedErrorCode(self: Windows.Gaming.Input.Custom.IGipFirmwareUpdateResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_FinalComponentId(self: Windows.Gaming.Input.Custom.IGipFirmwareUpdateResult) -> UInt32: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Gaming.Input.Custom.IGipFirmwareUpdateResult) -> Windows.Gaming.Input.Custom.GipFirmwareUpdateStatus: ...
    ExtendedErrorCode = property(get_ExtendedErrorCode, None)
    FinalComponentId = property(get_FinalComponentId, None)
    Status = property(get_Status, None)
GipFirmwareUpdateStatus = Int32
GipFirmwareUpdateStatus_Completed: GipFirmwareUpdateStatus = 0
GipFirmwareUpdateStatus_UpToDate: GipFirmwareUpdateStatus = 1
GipFirmwareUpdateStatus_Failed: GipFirmwareUpdateStatus = 2
class GipGameControllerProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Gaming.Input.Custom.GipGameControllerProvider'
    @winrt_mixinmethod
    def SendMessage(self: Windows.Gaming.Input.Custom.IGipGameControllerProvider, messageClass: Windows.Gaming.Input.Custom.GipMessageClass, messageId: Byte, messageBuffer: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def SendReceiveMessage(self: Windows.Gaming.Input.Custom.IGipGameControllerProvider, messageClass: Windows.Gaming.Input.Custom.GipMessageClass, messageId: Byte, requestMessageBuffer: c_char_p_no, responseMessageBuffer: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def UpdateFirmwareAsync(self: Windows.Gaming.Input.Custom.IGipGameControllerProvider, firmwareImage: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Gaming.Input.Custom.GipFirmwareUpdateResult, Windows.Gaming.Input.Custom.GipFirmwareUpdateProgress]: ...
    @winrt_mixinmethod
    def get_FirmwareVersionInfo(self: Windows.Gaming.Input.Custom.IGameControllerProvider) -> Windows.Gaming.Input.Custom.GameControllerVersionInfo: ...
    @winrt_mixinmethod
    def get_HardwareProductId(self: Windows.Gaming.Input.Custom.IGameControllerProvider) -> UInt16: ...
    @winrt_mixinmethod
    def get_HardwareVendorId(self: Windows.Gaming.Input.Custom.IGameControllerProvider) -> UInt16: ...
    @winrt_mixinmethod
    def get_HardwareVersionInfo(self: Windows.Gaming.Input.Custom.IGameControllerProvider) -> Windows.Gaming.Input.Custom.GameControllerVersionInfo: ...
    @winrt_mixinmethod
    def get_IsConnected(self: Windows.Gaming.Input.Custom.IGameControllerProvider) -> Boolean: ...
    FirmwareVersionInfo = property(get_FirmwareVersionInfo, None)
    HardwareProductId = property(get_HardwareProductId, None)
    HardwareVendorId = property(get_HardwareVendorId, None)
    HardwareVersionInfo = property(get_HardwareVersionInfo, None)
    IsConnected = property(get_IsConnected, None)
GipMessageClass = Int32
GipMessageClass_Command: GipMessageClass = 0
GipMessageClass_LowLatency: GipMessageClass = 1
GipMessageClass_StandardLatency: GipMessageClass = 2
class HidGameControllerProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Gaming.Input.Custom.HidGameControllerProvider'
    @winrt_mixinmethod
    def get_UsageId(self: Windows.Gaming.Input.Custom.IHidGameControllerProvider) -> UInt16: ...
    @winrt_mixinmethod
    def get_UsagePage(self: Windows.Gaming.Input.Custom.IHidGameControllerProvider) -> UInt16: ...
    @winrt_mixinmethod
    def GetFeatureReport(self: Windows.Gaming.Input.Custom.IHidGameControllerProvider, reportId: Byte, reportBuffer: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def SendFeatureReport(self: Windows.Gaming.Input.Custom.IHidGameControllerProvider, reportId: Byte, reportBuffer: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def SendOutputReport(self: Windows.Gaming.Input.Custom.IHidGameControllerProvider, reportId: Byte, reportBuffer: c_char_p_no) -> Void: ...
    @winrt_mixinmethod
    def get_FirmwareVersionInfo(self: Windows.Gaming.Input.Custom.IGameControllerProvider) -> Windows.Gaming.Input.Custom.GameControllerVersionInfo: ...
    @winrt_mixinmethod
    def get_HardwareProductId(self: Windows.Gaming.Input.Custom.IGameControllerProvider) -> UInt16: ...
    @winrt_mixinmethod
    def get_HardwareVendorId(self: Windows.Gaming.Input.Custom.IGameControllerProvider) -> UInt16: ...
    @winrt_mixinmethod
    def get_HardwareVersionInfo(self: Windows.Gaming.Input.Custom.IGameControllerProvider) -> Windows.Gaming.Input.Custom.GameControllerVersionInfo: ...
    @winrt_mixinmethod
    def get_IsConnected(self: Windows.Gaming.Input.Custom.IGameControllerProvider) -> Boolean: ...
    UsageId = property(get_UsageId, None)
    UsagePage = property(get_UsagePage, None)
    FirmwareVersionInfo = property(get_FirmwareVersionInfo, None)
    HardwareProductId = property(get_HardwareProductId, None)
    HardwareVendorId = property(get_HardwareVendorId, None)
    HardwareVersionInfo = property(get_HardwareVersionInfo, None)
    IsConnected = property(get_IsConnected, None)
class ICustomGameControllerFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('69a0ae5e-758e-4cbe-ac-e6-62-15-5f-e9-12-6f')
    @winrt_commethod(6)
    def CreateGameController(self, provider: Windows.Gaming.Input.Custom.IGameControllerProvider) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(7)
    def OnGameControllerAdded(self, value: Windows.Gaming.Input.IGameController) -> Void: ...
    @winrt_commethod(8)
    def OnGameControllerRemoved(self, value: Windows.Gaming.Input.IGameController) -> Void: ...
class IGameControllerFactoryManagerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('36cb66e3-d0a1-4986-a2-4c-40-b1-37-de-ba-9e')
    @winrt_commethod(6)
    def RegisterCustomFactoryForGipInterface(self, factory: Windows.Gaming.Input.Custom.ICustomGameControllerFactory, interfaceId: Guid) -> Void: ...
    @winrt_commethod(7)
    def RegisterCustomFactoryForHardwareId(self, factory: Windows.Gaming.Input.Custom.ICustomGameControllerFactory, hardwareVendorId: UInt16, hardwareProductId: UInt16) -> Void: ...
    @winrt_commethod(8)
    def RegisterCustomFactoryForXusbType(self, factory: Windows.Gaming.Input.Custom.ICustomGameControllerFactory, xusbType: Windows.Gaming.Input.Custom.XusbDeviceType, xusbSubtype: Windows.Gaming.Input.Custom.XusbDeviceSubtype) -> Void: ...
class IGameControllerFactoryManagerStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('eace5644-19df-4115-b3-2a-27-93-e2-ae-a3-bb')
    @winrt_commethod(6)
    def TryGetFactoryControllerFromGameController(self, factory: Windows.Gaming.Input.Custom.ICustomGameControllerFactory, gameController: Windows.Gaming.Input.IGameController) -> Windows.Gaming.Input.IGameController: ...
class IGameControllerInputSink(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1ff6f922-c640-4c78-a8-20-9a-71-5c-55-8b-cb')
    @winrt_commethod(6)
    def OnInputResumed(self, timestamp: UInt64) -> Void: ...
    @winrt_commethod(7)
    def OnInputSuspended(self, timestamp: UInt64) -> Void: ...
class IGameControllerProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e6d73982-2996-4559-b1-6c-3e-57-d4-6e-58-d6')
    @winrt_commethod(6)
    def get_FirmwareVersionInfo(self) -> Windows.Gaming.Input.Custom.GameControllerVersionInfo: ...
    @winrt_commethod(7)
    def get_HardwareProductId(self) -> UInt16: ...
    @winrt_commethod(8)
    def get_HardwareVendorId(self) -> UInt16: ...
    @winrt_commethod(9)
    def get_HardwareVersionInfo(self) -> Windows.Gaming.Input.Custom.GameControllerVersionInfo: ...
    @winrt_commethod(10)
    def get_IsConnected(self) -> Boolean: ...
    FirmwareVersionInfo = property(get_FirmwareVersionInfo, None)
    HardwareProductId = property(get_HardwareProductId, None)
    HardwareVendorId = property(get_HardwareVendorId, None)
    HardwareVersionInfo = property(get_HardwareVersionInfo, None)
    IsConnected = property(get_IsConnected, None)
class IGipFirmwareUpdateResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6b794d32-8553-4292-8e-03-e1-66-51-a2-f8-bc')
    @winrt_commethod(6)
    def get_ExtendedErrorCode(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_FinalComponentId(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Status(self) -> Windows.Gaming.Input.Custom.GipFirmwareUpdateStatus: ...
    ExtendedErrorCode = property(get_ExtendedErrorCode, None)
    FinalComponentId = property(get_FinalComponentId, None)
    Status = property(get_Status, None)
class IGipGameControllerInputSink(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a2108abf-09f1-43bc-a1-40-80-f8-99-ec-36-fb')
    @winrt_commethod(6)
    def OnKeyReceived(self, timestamp: UInt64, keyCode: Byte, isPressed: Boolean) -> Void: ...
    @winrt_commethod(7)
    def OnMessageReceived(self, timestamp: UInt64, messageClass: Windows.Gaming.Input.Custom.GipMessageClass, messageId: Byte, sequenceId: Byte, messageBuffer: c_char_p_no) -> Void: ...
class IGipGameControllerProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('dbcf1e19-1af5-45a8-bf-02-a0-ee-50-c8-23-fc')
    @winrt_commethod(6)
    def SendMessage(self, messageClass: Windows.Gaming.Input.Custom.GipMessageClass, messageId: Byte, messageBuffer: c_char_p_no) -> Void: ...
    @winrt_commethod(7)
    def SendReceiveMessage(self, messageClass: Windows.Gaming.Input.Custom.GipMessageClass, messageId: Byte, requestMessageBuffer: c_char_p_no, responseMessageBuffer: c_char_p_no) -> Void: ...
    @winrt_commethod(8)
    def UpdateFirmwareAsync(self, firmwareImage: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Gaming.Input.Custom.GipFirmwareUpdateResult, Windows.Gaming.Input.Custom.GipFirmwareUpdateProgress]: ...
class IHidGameControllerInputSink(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f754c322-182d-40e4-a1-26-fc-ee-4f-fa-1e-31')
    @winrt_commethod(6)
    def OnInputReportReceived(self, timestamp: UInt64, reportId: Byte, reportBuffer: c_char_p_no) -> Void: ...
class IHidGameControllerProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('95ce3af4-abf0-4b68-a0-81-3b-7d-e7-3f-f0-e7')
    @winrt_commethod(6)
    def get_UsageId(self) -> UInt16: ...
    @winrt_commethod(7)
    def get_UsagePage(self) -> UInt16: ...
    @winrt_commethod(8)
    def GetFeatureReport(self, reportId: Byte, reportBuffer: c_char_p_no) -> Void: ...
    @winrt_commethod(9)
    def SendFeatureReport(self, reportId: Byte, reportBuffer: c_char_p_no) -> Void: ...
    @winrt_commethod(10)
    def SendOutputReport(self, reportId: Byte, reportBuffer: c_char_p_no) -> Void: ...
    UsageId = property(get_UsageId, None)
    UsagePage = property(get_UsagePage, None)
class IXusbGameControllerInputSink(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b2ac1d95-6ecb-42b3-8a-ab-02-54-01-ca-47-12')
    @winrt_commethod(6)
    def OnInputReceived(self, timestamp: UInt64, reportId: Byte, inputBuffer: c_char_p_no) -> Void: ...
class IXusbGameControllerProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6e2971eb-0efb-48b4-80-8b-83-76-43-b2-f2-16')
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
class XusbGameControllerProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Gaming.Input.Custom.XusbGameControllerProvider'
    @winrt_mixinmethod
    def SetVibration(self: Windows.Gaming.Input.Custom.IXusbGameControllerProvider, lowFrequencyMotorSpeed: Double, highFrequencyMotorSpeed: Double) -> Void: ...
    @winrt_mixinmethod
    def get_FirmwareVersionInfo(self: Windows.Gaming.Input.Custom.IGameControllerProvider) -> Windows.Gaming.Input.Custom.GameControllerVersionInfo: ...
    @winrt_mixinmethod
    def get_HardwareProductId(self: Windows.Gaming.Input.Custom.IGameControllerProvider) -> UInt16: ...
    @winrt_mixinmethod
    def get_HardwareVendorId(self: Windows.Gaming.Input.Custom.IGameControllerProvider) -> UInt16: ...
    @winrt_mixinmethod
    def get_HardwareVersionInfo(self: Windows.Gaming.Input.Custom.IGameControllerProvider) -> Windows.Gaming.Input.Custom.GameControllerVersionInfo: ...
    @winrt_mixinmethod
    def get_IsConnected(self: Windows.Gaming.Input.Custom.IGameControllerProvider) -> Boolean: ...
    FirmwareVersionInfo = property(get_FirmwareVersionInfo, None)
    HardwareProductId = property(get_HardwareProductId, None)
    HardwareVendorId = property(get_HardwareVendorId, None)
    HardwareVersionInfo = property(get_HardwareVersionInfo, None)
    IsConnected = property(get_IsConnected, None)
make_head(_module, 'GameControllerFactoryManager')
make_head(_module, 'GameControllerVersionInfo')
make_head(_module, 'GipFirmwareUpdateProgress')
make_head(_module, 'GipFirmwareUpdateResult')
make_head(_module, 'GipGameControllerProvider')
make_head(_module, 'HidGameControllerProvider')
make_head(_module, 'ICustomGameControllerFactory')
make_head(_module, 'IGameControllerFactoryManagerStatics')
make_head(_module, 'IGameControllerFactoryManagerStatics2')
make_head(_module, 'IGameControllerInputSink')
make_head(_module, 'IGameControllerProvider')
make_head(_module, 'IGipFirmwareUpdateResult')
make_head(_module, 'IGipGameControllerInputSink')
make_head(_module, 'IGipGameControllerProvider')
make_head(_module, 'IHidGameControllerInputSink')
make_head(_module, 'IHidGameControllerProvider')
make_head(_module, 'IXusbGameControllerInputSink')
make_head(_module, 'IXusbGameControllerProvider')
make_head(_module, 'XusbGameControllerProvider')
