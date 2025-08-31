from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Devices.Geolocation
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Services.Maps.OfflineMaps
class IOfflineMapPackage(ComPtr):
    extends: IInspectable
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
    def add_StatusChanged(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackage, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def RequestStartDownloadAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageStartDownloadResult]: ...
    DisplayName = property(get_DisplayName, None)
    EnclosingRegionName = property(get_EnclosingRegionName, None)
    EstimatedSizeInBytes = property(get_EstimatedSizeInBytes, None)
    Status = property(get_Status, None)
    StatusChanged = event()
class IOfflineMapPackageQueryResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Services.Maps.OfflineMaps.IOfflineMapPackageQueryResult'
    _iid_ = Guid('{55585411-39e1-4e41-a4e1-5f4872bee199}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryStatus: ...
    @winrt_commethod(7)
    def get_Packages(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackage]: ...
    Packages = property(get_Packages, None)
    Status = property(get_Status, None)
class IOfflineMapPackageStartDownloadResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Services.Maps.OfflineMaps.IOfflineMapPackageStartDownloadResult'
    _iid_ = Guid('{d965b918-d4d6-4afe-9378-3ec71ef11c3d}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageStartDownloadStatus: ...
    Status = property(get_Status, None)
class IOfflineMapPackageStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Services.Maps.OfflineMaps.IOfflineMapPackageStatics'
    _iid_ = Guid('{185e7922-a831-4ab0-941f-6998fa929285}')
    @winrt_commethod(6)
    def FindPackagesAsync(self, queryPoint: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult]: ...
    @winrt_commethod(7)
    def FindPackagesInBoundingBoxAsync(self, queryBoundingBox: win32more.Windows.Devices.Geolocation.GeoboundingBox) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult]: ...
    @winrt_commethod(8)
    def FindPackagesInGeocircleAsync(self, queryCircle: win32more.Windows.Devices.Geolocation.Geocircle) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult]: ...
class OfflineMapPackage(ComPtr):
    extends: IInspectable
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
    def add_StatusChanged(self: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackage, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackage, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def RequestStartDownloadAsync(self: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackage) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageStartDownloadResult]: ...
    @winrt_classmethod
    def FindPackagesAsync(cls: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackageStatics, queryPoint: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult]: ...
    @winrt_classmethod
    def FindPackagesInBoundingBoxAsync(cls: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackageStatics, queryBoundingBox: win32more.Windows.Devices.Geolocation.GeoboundingBox) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult]: ...
    @winrt_classmethod
    def FindPackagesInGeocircleAsync(cls: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackageStatics, queryCircle: win32more.Windows.Devices.Geolocation.Geocircle) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult]: ...
    DisplayName = property(get_DisplayName, None)
    EnclosingRegionName = property(get_EnclosingRegionName, None)
    EstimatedSizeInBytes = property(get_EstimatedSizeInBytes, None)
    Status = property(get_Status, None)
    StatusChanged = event()
class OfflineMapPackageQueryResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackageQueryResult
    _classid_ = 'Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackageQueryResult) -> win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageQueryStatus: ...
    @winrt_mixinmethod
    def get_Packages(self: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackageQueryResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackage]: ...
    Packages = property(get_Packages, None)
    Status = property(get_Status, None)
class OfflineMapPackageQueryStatus(Enum, Int32):
    Success = 0
    UnknownError = 1
    InvalidCredentials = 2
    NetworkFailure = 3
class OfflineMapPackageStartDownloadResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackageStartDownloadResult
    _classid_ = 'Windows.Services.Maps.OfflineMaps.OfflineMapPackageStartDownloadResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Services.Maps.OfflineMaps.IOfflineMapPackageStartDownloadResult) -> win32more.Windows.Services.Maps.OfflineMaps.OfflineMapPackageStartDownloadStatus: ...
    Status = property(get_Status, None)
class OfflineMapPackageStartDownloadStatus(Enum, Int32):
    Success = 0
    UnknownError = 1
    InvalidCredentials = 2
    DeniedWithoutCapability = 3
class OfflineMapPackageStatus(Enum, Int32):
    NotDownloaded = 0
    Downloading = 1
    Downloaded = 2
    Deleting = 3


make_ready(__name__)
