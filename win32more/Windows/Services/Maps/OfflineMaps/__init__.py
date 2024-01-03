from __future__ import annotations
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
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.Geolocation
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Services.Maps.OfflineMaps
class IOfflineMapPackage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.OfflineMaps.IOfflineMapPackage'
    _iid_ = Guid('{a797673b-a5b5-4144-b525-e68c8862664b}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageStatus: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_EnclosingRegionName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_EstimatedSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(10)
    def remove_StatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_StatusChanged(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackage, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def RequestStartDownloadAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageStartDownloadResult]: ...
    Status = property(get_Status, None)
    DisplayName = property(get_DisplayName, None)
    EnclosingRegionName = property(get_EnclosingRegionName, None)
    EstimatedSizeInBytes = property(get_EstimatedSizeInBytes, None)
class IOfflineMapPackageQueryResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.OfflineMaps.IOfflineMapPackageQueryResult'
    _iid_ = Guid('{55585411-39e1-4e41-a4e1-5f4872bee199}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryStatus: ...
    @winrt_commethod(7)
    def get_Packages(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackage]: ...
    Status = property(get_Status, None)
    Packages = property(get_Packages, None)
class IOfflineMapPackageStartDownloadResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.OfflineMaps.IOfflineMapPackageStartDownloadResult'
    _iid_ = Guid('{d965b918-d4d6-4afe-9378-3ec71ef11c3d}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageStartDownloadStatus: ...
    Status = property(get_Status, None)
class IOfflineMapPackageStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.OfflineMaps.IOfflineMapPackageStatics'
    _iid_ = Guid('{185e7922-a831-4ab0-941f-6998fa929285}')
    @winrt_commethod(6)
    def FindPackagesAsync(self, queryPoint: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult]: ...
    @winrt_commethod(7)
    def FindPackagesInBoundingBoxAsync(self, queryBoundingBox: win32more.Windows.Devices.Geolocation.GeoboundingBox) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult]: ...
    @winrt_commethod(8)
    def FindPackagesInGeocircleAsync(self, queryCircle: win32more.Windows.Devices.Geolocation.Geocircle) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult]: ...
class OfflineMapPackage(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackage
    _classid_ = 'Windows.Services.Maps.OfflineMaps.OfflineMapPackage'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackage) -> win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageStatus: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EnclosingRegionName(self: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackage) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EstimatedSizeInBytes(self: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackage) -> UInt64: ...
    @winrt_mixinmethod
    def remove_StatusChanged(self: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackage, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StatusChanged(self: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackage, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackage, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def RequestStartDownloadAsync(self: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackage) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageStartDownloadResult]: ...
    @winrt_classmethod
    def FindPackagesAsync(cls: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackageStatics, queryPoint: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult]: ...
    @winrt_classmethod
    def FindPackagesInBoundingBoxAsync(cls: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackageStatics, queryBoundingBox: win32more.Windows.Devices.Geolocation.GeoboundingBox) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult]: ...
    @winrt_classmethod
    def FindPackagesInGeocircleAsync(cls: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackageStatics, queryCircle: win32more.Windows.Devices.Geolocation.Geocircle) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult]: ...
    Status = property(get_Status, None)
    DisplayName = property(get_DisplayName, None)
    EnclosingRegionName = property(get_EnclosingRegionName, None)
    EstimatedSizeInBytes = property(get_EstimatedSizeInBytes, None)
class OfflineMapPackageQueryResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackageQueryResult
    _classid_ = 'Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackageQueryResult) -> win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryStatus: ...
    @winrt_mixinmethod
    def get_Packages(self: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackageQueryResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackage]: ...
    Status = property(get_Status, None)
    Packages = property(get_Packages, None)
OfflineMapPackageQueryStatus = Int32
OfflineMapPackageQueryStatus_Success: OfflineMapPackageQueryStatus = 0
OfflineMapPackageQueryStatus_UnknownError: OfflineMapPackageQueryStatus = 1
OfflineMapPackageQueryStatus_InvalidCredentials: OfflineMapPackageQueryStatus = 2
OfflineMapPackageQueryStatus_NetworkFailure: OfflineMapPackageQueryStatus = 3
class OfflineMapPackageStartDownloadResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackageStartDownloadResult
    _classid_ = 'Windows.Services.Maps.OfflineMaps.OfflineMapPackageStartDownloadResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackageStartDownloadResult) -> win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageStartDownloadStatus: ...
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


make_ready(__name__)
