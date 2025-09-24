from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.System.Diagnostics.Telemetry
class IPlatformTelemetryClientStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.System.Diagnostics.Telemetry.IPlatformTelemetryClientStatics'
    _iid_ = Guid('{9bf3f25d-d5c3-4eea-8dbe-9c8dbb0d9d8f}')
    @winrt_commethod(6)
    def Register(self, id: WinRT_String) -> win32more.Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationResult: ...
    @winrt_commethod(7)
    def RegisterWithSettings(self, id: WinRT_String, settings: win32more.Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationSettings) -> win32more.Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationResult: ...
class IPlatformTelemetryRegistrationResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.System.Diagnostics.Telemetry.IPlatformTelemetryRegistrationResult'
    _iid_ = Guid('{4d8518ab-2292-49bd-a15a-3d71d2145112}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationStatus: ...
    Status = property(get_Status, None)
class IPlatformTelemetryRegistrationSettings(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.System.Diagnostics.Telemetry.IPlatformTelemetryRegistrationSettings'
    _iid_ = Guid('{819a8582-ca19-415e-bb79-9c224bfa3a73}')
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
class PlatformTelemetryClient(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.System.Diagnostics.Telemetry.PlatformTelemetryClient'
    @winrt_classmethod
    def Register(cls: win32more.Windows.System.Diagnostics.Telemetry.IPlatformTelemetryClientStatics, id: WinRT_String) -> win32more.Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationResult: ...
    @winrt_classmethod
    def RegisterWithSettings(cls: win32more.Windows.System.Diagnostics.Telemetry.IPlatformTelemetryClientStatics, id: WinRT_String, settings: win32more.Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationSettings) -> win32more.Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationResult: ...
class PlatformTelemetryRegistrationResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.System.Diagnostics.Telemetry.IPlatformTelemetryRegistrationResult
    _classid_ = 'Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.System.Diagnostics.Telemetry.IPlatformTelemetryRegistrationResult) -> win32more.Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationStatus: ...
    Status = property(get_Status, None)
class PlatformTelemetryRegistrationSettings(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.System.Diagnostics.Telemetry.IPlatformTelemetryRegistrationSettings
    _classid_ = 'Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationSettings'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationSettings.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.System.Diagnostics.Telemetry.PlatformTelemetryRegistrationSettings: ...
    @winrt_mixinmethod
    def get_StorageSize(self: win32more.Windows.System.Diagnostics.Telemetry.IPlatformTelemetryRegistrationSettings) -> UInt32: ...
    @winrt_mixinmethod
    def put_StorageSize(self: win32more.Windows.System.Diagnostics.Telemetry.IPlatformTelemetryRegistrationSettings, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_UploadQuotaSize(self: win32more.Windows.System.Diagnostics.Telemetry.IPlatformTelemetryRegistrationSettings) -> UInt32: ...
    @winrt_mixinmethod
    def put_UploadQuotaSize(self: win32more.Windows.System.Diagnostics.Telemetry.IPlatformTelemetryRegistrationSettings, value: UInt32) -> Void: ...
    StorageSize = property(get_StorageSize, put_StorageSize)
    UploadQuotaSize = property(get_UploadQuotaSize, put_UploadQuotaSize)
class PlatformTelemetryRegistrationStatus(Enum, Int32):
    Success = 0
    SettingsOutOfRange = 1
    UnknownFailure = 2


make_ready(__name__)
