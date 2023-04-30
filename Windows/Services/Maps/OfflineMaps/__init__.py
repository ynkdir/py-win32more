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
import Windows.Devices.Geolocation
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Services.Maps.OfflineMaps
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IOfflineMapPackage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('a797673b-a5b5-4144-b5-25-e6-8c-88-62-66-4b')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Services.Maps.OfflineMaps.OfflineMapPackageStatus: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_EnclosingRegionName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_EstimatedSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(10)
    def remove_StatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_StatusChanged(self, value: Windows.Foundation.TypedEventHandler[Windows.Services.Maps.OfflineMaps.OfflineMapPackage, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def RequestStartDownloadAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.OfflineMaps.OfflineMapPackageStartDownloadResult]: ...
    Status = property(get_Status, None)
    DisplayName = property(get_DisplayName, None)
    EnclosingRegionName = property(get_EnclosingRegionName, None)
    EstimatedSizeInBytes = property(get_EstimatedSizeInBytes, None)
class IOfflineMapPackageQueryResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('55585411-39e1-4e41-a4-e1-5f-48-72-be-e1-99')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryStatus: ...
    @winrt_commethod(7)
    def get_Packages(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.OfflineMaps.OfflineMapPackage]: ...
    Status = property(get_Status, None)
    Packages = property(get_Packages, None)
class IOfflineMapPackageStartDownloadResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d965b918-d4d6-4afe-93-78-3e-c7-1e-f1-1c-3d')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Services.Maps.OfflineMaps.OfflineMapPackageStartDownloadStatus: ...
    Status = property(get_Status, None)
class IOfflineMapPackageStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('185e7922-a831-4ab0-94-1f-69-98-fa-92-92-85')
    @winrt_commethod(6)
    def FindPackagesAsync(self, queryPoint: Windows.Devices.Geolocation.Geopoint) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult]: ...
    @winrt_commethod(7)
    def FindPackagesInBoundingBoxAsync(self, queryBoundingBox: Windows.Devices.Geolocation.GeoboundingBox) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult]: ...
    @winrt_commethod(8)
    def FindPackagesInGeocircleAsync(self, queryCircle: Windows.Devices.Geolocation.Geocircle) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult]: ...
class OfflineMapPackage(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.OfflineMaps.OfflineMapPackage'
    @winrt_mixinmethod
    def get_Status(self: Windows.Services.Maps.OfflineMaps.IOfflineMapPackage) -> Windows.Services.Maps.OfflineMaps.OfflineMapPackageStatus: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Services.Maps.OfflineMaps.IOfflineMapPackage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EnclosingRegionName(self: Windows.Services.Maps.OfflineMaps.IOfflineMapPackage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EstimatedSizeInBytes(self: Windows.Services.Maps.OfflineMaps.IOfflineMapPackage) -> UInt64: ...
    @winrt_mixinmethod
    def remove_StatusChanged(self: Windows.Services.Maps.OfflineMaps.IOfflineMapPackage, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StatusChanged(self: Windows.Services.Maps.OfflineMaps.IOfflineMapPackage, value: Windows.Foundation.TypedEventHandler[Windows.Services.Maps.OfflineMaps.OfflineMapPackage, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def RequestStartDownloadAsync(self: Windows.Services.Maps.OfflineMaps.IOfflineMapPackage) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.OfflineMaps.OfflineMapPackageStartDownloadResult]: ...
    @winrt_classmethod
    def FindPackagesAsync(cls: Windows.Services.Maps.OfflineMaps.IOfflineMapPackageStatics, queryPoint: Windows.Devices.Geolocation.Geopoint) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult]: ...
    @winrt_classmethod
    def FindPackagesInBoundingBoxAsync(cls: Windows.Services.Maps.OfflineMaps.IOfflineMapPackageStatics, queryBoundingBox: Windows.Devices.Geolocation.GeoboundingBox) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult]: ...
    @winrt_classmethod
    def FindPackagesInGeocircleAsync(cls: Windows.Services.Maps.OfflineMaps.IOfflineMapPackageStatics, queryCircle: Windows.Devices.Geolocation.Geocircle) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult]: ...
    Status = property(get_Status, None)
    DisplayName = property(get_DisplayName, None)
    EnclosingRegionName = property(get_EnclosingRegionName, None)
    EstimatedSizeInBytes = property(get_EstimatedSizeInBytes, None)
class OfflineMapPackageQueryResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Services.Maps.OfflineMaps.IOfflineMapPackageQueryResult) -> Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryStatus: ...
    @winrt_mixinmethod
    def get_Packages(self: Windows.Services.Maps.OfflineMaps.IOfflineMapPackageQueryResult) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.OfflineMaps.OfflineMapPackage]: ...
    Status = property(get_Status, None)
    Packages = property(get_Packages, None)
OfflineMapPackageQueryStatus = Int32
OfflineMapPackageQueryStatus_Success: OfflineMapPackageQueryStatus = 0
OfflineMapPackageQueryStatus_UnknownError: OfflineMapPackageQueryStatus = 1
OfflineMapPackageQueryStatus_InvalidCredentials: OfflineMapPackageQueryStatus = 2
OfflineMapPackageQueryStatus_NetworkFailure: OfflineMapPackageQueryStatus = 3
class OfflineMapPackageStartDownloadResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.OfflineMaps.OfflineMapPackageStartDownloadResult'
    @winrt_mixinmethod
    def get_Status(self: Windows.Services.Maps.OfflineMaps.IOfflineMapPackageStartDownloadResult) -> Windows.Services.Maps.OfflineMaps.OfflineMapPackageStartDownloadStatus: ...
    Status = property(get_Status, None)
OfflineMapPackageStartDownloadStatus = Int32
OfflineMapPackageStartDownloadStatus_Success: OfflineMapPackageStartDownloadStatus = 0
OfflineMapPackageStartDownloadStatus_UnknownError: OfflineMapPackageStartDownloadStatus = 1
OfflineMapPackageStartDownloadStatus_InvalidCredentials: OfflineMapPackageStartDownloadStatus = 2
OfflineMapPackageStartDownloadStatus_DeniedWithoutCapability: OfflineMapPackageStartDownloadStatus = 3
OfflineMapPackageStatus = Int32
OfflineMapPackageStatus_NotDownloaded: OfflineMapPackageStatus = 0
OfflineMapPackageStatus_Downloading: OfflineMapPackageStatus = 1
OfflineMapPackageStatus_Downloaded: OfflineMapPackageStatus = 2
OfflineMapPackageStatus_Deleting: OfflineMapPackageStatus = 3
make_head(_module, 'IOfflineMapPackage')
make_head(_module, 'IOfflineMapPackageQueryResult')
make_head(_module, 'IOfflineMapPackageStartDownloadResult')
make_head(_module, 'IOfflineMapPackageStatics')
make_head(_module, 'OfflineMapPackage')
make_head(_module, 'OfflineMapPackageQueryResult')
make_head(_module, 'OfflineMapPackageStartDownloadResult')
