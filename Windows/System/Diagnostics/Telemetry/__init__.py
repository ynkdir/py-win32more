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
import Windows.System.Diagnostics.Telemetry
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPlatformTelemetryClientStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9bf3f25d-d5c3-4eea-8d-be-9c-8d-bb-0d-9d-8f')
    @winrt_commethod(6)
    def Register(self, id: WinRT_String) -> Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationResult: ...
    @winrt_commethod(7)
    def RegisterWithSettings(self, id: WinRT_String, settings: Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationSettings) -> Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationResult: ...
class IPlatformTelemetryRegistrationResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4d8518ab-2292-49bd-a1-5a-3d-71-d2-14-51-12')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationStatus: ...
    Status = property(get_Status, None)
class IPlatformTelemetryRegistrationSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('819a8582-ca19-415e-bb-79-9c-22-4b-fa-3a-73')
    @winrt_commethod(6)
    def get_StorageSize(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_StorageSize(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_UploadQuotaSize(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_UploadQuotaSize(self, value: UInt32) -> Void: ...
    StorageSize = property(get_StorageSize, put_StorageSize)
    UploadQuotaSize = property(get_UploadQuotaSize, put_UploadQuotaSize)
class PlatformTelemetryClient(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Diagnostics.Telemetry.PlatformTelemetryClient'
    @winrt_classmethod
    def Register(cls: Windows.System.Diagnostics.Telemetry.IPlatformTelemetryClientStatics, id: WinRT_String) -> Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationResult: ...
    @winrt_classmethod
    def RegisterWithSettings(cls: Windows.System.Diagnostics.Telemetry.IPlatformTelemetryClientStatics, id: WinRT_String, settings: Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationSettings) -> Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationResult: ...
class PlatformTelemetryRegistrationResult(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.System.Diagnostics.Telemetry.IPlatformTelemetryRegistrationResult) -> Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationStatus: ...
    Status = property(get_Status, None)
class PlatformTelemetryRegistrationSettings(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationSettings'
    @winrt_activatemethod
    def New(cls) -> Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationSettings: ...
    @winrt_mixinmethod
    def get_StorageSize(self: Windows.System.Diagnostics.Telemetry.IPlatformTelemetryRegistrationSettings) -> UInt32: ...
    @winrt_mixinmethod
    def put_StorageSize(self: Windows.System.Diagnostics.Telemetry.IPlatformTelemetryRegistrationSettings, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_UploadQuotaSize(self: Windows.System.Diagnostics.Telemetry.IPlatformTelemetryRegistrationSettings) -> UInt32: ...
    @winrt_mixinmethod
    def put_UploadQuotaSize(self: Windows.System.Diagnostics.Telemetry.IPlatformTelemetryRegistrationSettings, value: UInt32) -> Void: ...
    StorageSize = property(get_StorageSize, put_StorageSize)
    UploadQuotaSize = property(get_UploadQuotaSize, put_UploadQuotaSize)
PlatformTelemetryRegistrationStatus = Int32
PlatformTelemetryRegistrationStatus_Success: PlatformTelemetryRegistrationStatus = 0
PlatformTelemetryRegistrationStatus_SettingsOutOfRange: PlatformTelemetryRegistrationStatus = 1
PlatformTelemetryRegistrationStatus_UnknownFailure: PlatformTelemetryRegistrationStatus = 2
make_head(_module, 'IPlatformTelemetryClientStatics')
make_head(_module, 'IPlatformTelemetryRegistrationResult')
make_head(_module, 'IPlatformTelemetryRegistrationSettings')
make_head(_module, 'PlatformTelemetryClient')
make_head(_module, 'PlatformTelemetryRegistrationResult')
make_head(_module, 'PlatformTelemetryRegistrationSettings')
