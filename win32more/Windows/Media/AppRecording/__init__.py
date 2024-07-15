from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Media.AppRecording
import win32more.Windows.Storage
import win32more.Windows.Win32.System.WinRT
AppRecordingContract: UInt32 = 65536
class AppRecordingManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.AppRecording.IAppRecordingManager
    _classid_ = 'Windows.Media.AppRecording.AppRecordingManager'
    @winrt_mixinmethod
    def GetStatus(self: win32more.Windows.Media.AppRecording.IAppRecordingManager) -> win32more.Windows.Media.AppRecording.AppRecordingStatus: ...
    @winrt_mixinmethod
    def StartRecordingToFileAsync(self: win32more.Windows.Media.AppRecording.IAppRecordingManager, file: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.AppRecording.AppRecordingResult]: ...
    @winrt_mixinmethod
    def RecordTimeSpanToFileAsync(self: win32more.Windows.Media.AppRecording.IAppRecordingManager, startTime: win32more.Windows.Foundation.DateTime, duration: win32more.Windows.Foundation.TimeSpan, file: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.AppRecording.AppRecordingResult]: ...
    @winrt_mixinmethod
    def get_SupportedScreenshotMediaEncodingSubtypes(self: win32more.Windows.Media.AppRecording.IAppRecordingManager) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def SaveScreenshotToFilesAsync(self: win32more.Windows.Media.AppRecording.IAppRecordingManager, folder: win32more.Windows.Storage.StorageFolder, filenamePrefix: WinRT_String, option: win32more.Windows.Media.AppRecording.AppRecordingSaveScreenshotOption, requestedFormats: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.AppRecording.AppRecordingSaveScreenshotResult]: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Media.AppRecording.IAppRecordingManagerStatics) -> win32more.Windows.Media.AppRecording.AppRecordingManager: ...
    SupportedScreenshotMediaEncodingSubtypes = property(get_SupportedScreenshotMediaEncodingSubtypes, None)
class AppRecordingResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.AppRecording.IAppRecordingResult
    _classid_ = 'Windows.Media.AppRecording.AppRecordingResult'
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.Media.AppRecording.IAppRecordingResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Media.AppRecording.IAppRecordingResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Media.AppRecording.IAppRecordingResult) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_IsFileTruncated(self: win32more.Windows.Media.AppRecording.IAppRecordingResult) -> Boolean: ...
    Duration = property(get_Duration, None)
    ExtendedError = property(get_ExtendedError, None)
    IsFileTruncated = property(get_IsFileTruncated, None)
    Succeeded = property(get_Succeeded, None)
class AppRecordingSaveScreenshotOption(Enum, Int32):
    None_ = 0
    HdrContentVisible = 1
class AppRecordingSaveScreenshotResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.AppRecording.IAppRecordingSaveScreenshotResult
    _classid_ = 'Windows.Media.AppRecording.AppRecordingSaveScreenshotResult'
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.Media.AppRecording.IAppRecordingSaveScreenshotResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.Media.AppRecording.IAppRecordingSaveScreenshotResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_SavedScreenshotInfos(self: win32more.Windows.Media.AppRecording.IAppRecordingSaveScreenshotResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.AppRecording.AppRecordingSavedScreenshotInfo]: ...
    ExtendedError = property(get_ExtendedError, None)
    SavedScreenshotInfos = property(get_SavedScreenshotInfos, None)
    Succeeded = property(get_Succeeded, None)
class AppRecordingSavedScreenshotInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.AppRecording.IAppRecordingSavedScreenshotInfo
    _classid_ = 'Windows.Media.AppRecording.AppRecordingSavedScreenshotInfo'
    @winrt_mixinmethod
    def get_File(self: win32more.Windows.Media.AppRecording.IAppRecordingSavedScreenshotInfo) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def get_MediaEncodingSubtype(self: win32more.Windows.Media.AppRecording.IAppRecordingSavedScreenshotInfo) -> WinRT_String: ...
    File = property(get_File, None)
    MediaEncodingSubtype = property(get_MediaEncodingSubtype, None)
class AppRecordingStatus(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.AppRecording.IAppRecordingStatus
    _classid_ = 'Windows.Media.AppRecording.AppRecordingStatus'
    @winrt_mixinmethod
    def get_CanRecord(self: win32more.Windows.Media.AppRecording.IAppRecordingStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanRecordTimeSpan(self: win32more.Windows.Media.AppRecording.IAppRecordingStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_HistoricalBufferDuration(self: win32more.Windows.Media.AppRecording.IAppRecordingStatus) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Details(self: win32more.Windows.Media.AppRecording.IAppRecordingStatus) -> win32more.Windows.Media.AppRecording.AppRecordingStatusDetails: ...
    CanRecord = property(get_CanRecord, None)
    CanRecordTimeSpan = property(get_CanRecordTimeSpan, None)
    Details = property(get_Details, None)
    HistoricalBufferDuration = property(get_HistoricalBufferDuration, None)
class AppRecordingStatusDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.AppRecording.IAppRecordingStatusDetails
    _classid_ = 'Windows.Media.AppRecording.AppRecordingStatusDetails'
    @winrt_mixinmethod
    def get_IsAnyAppBroadcasting(self: win32more.Windows.Media.AppRecording.IAppRecordingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCaptureResourceUnavailable(self: win32more.Windows.Media.AppRecording.IAppRecordingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsGameStreamInProgress(self: win32more.Windows.Media.AppRecording.IAppRecordingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTimeSpanRecordingDisabled(self: win32more.Windows.Media.AppRecording.IAppRecordingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsGpuConstrained(self: win32more.Windows.Media.AppRecording.IAppRecordingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsAppInactive(self: win32more.Windows.Media.AppRecording.IAppRecordingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBlockedForApp(self: win32more.Windows.Media.AppRecording.IAppRecordingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDisabledByUser(self: win32more.Windows.Media.AppRecording.IAppRecordingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDisabledBySystem(self: win32more.Windows.Media.AppRecording.IAppRecordingStatusDetails) -> Boolean: ...
    IsAnyAppBroadcasting = property(get_IsAnyAppBroadcasting, None)
    IsAppInactive = property(get_IsAppInactive, None)
    IsBlockedForApp = property(get_IsBlockedForApp, None)
    IsCaptureResourceUnavailable = property(get_IsCaptureResourceUnavailable, None)
    IsDisabledBySystem = property(get_IsDisabledBySystem, None)
    IsDisabledByUser = property(get_IsDisabledByUser, None)
    IsGameStreamInProgress = property(get_IsGameStreamInProgress, None)
    IsGpuConstrained = property(get_IsGpuConstrained, None)
    IsTimeSpanRecordingDisabled = property(get_IsTimeSpanRecordingDisabled, None)
class IAppRecordingManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppRecording.IAppRecordingManager'
    _iid_ = Guid('{e7e26076-a044-48e2-a512-3094d574c7cc}')
    @winrt_commethod(6)
    def GetStatus(self) -> win32more.Windows.Media.AppRecording.AppRecordingStatus: ...
    @winrt_commethod(7)
    def StartRecordingToFileAsync(self, file: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.AppRecording.AppRecordingResult]: ...
    @winrt_commethod(8)
    def RecordTimeSpanToFileAsync(self, startTime: win32more.Windows.Foundation.DateTime, duration: win32more.Windows.Foundation.TimeSpan, file: win32more.Windows.Storage.StorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.AppRecording.AppRecordingResult]: ...
    @winrt_commethod(9)
    def get_SupportedScreenshotMediaEncodingSubtypes(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def SaveScreenshotToFilesAsync(self, folder: win32more.Windows.Storage.StorageFolder, filenamePrefix: WinRT_String, option: win32more.Windows.Media.AppRecording.AppRecordingSaveScreenshotOption, requestedFormats: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Media.AppRecording.AppRecordingSaveScreenshotResult]: ...
    SupportedScreenshotMediaEncodingSubtypes = property(get_SupportedScreenshotMediaEncodingSubtypes, None)
class IAppRecordingManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppRecording.IAppRecordingManagerStatics'
    _iid_ = Guid('{50e709f7-38ce-4bd3-9db2-e72bbe9de11d}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Media.AppRecording.AppRecordingManager: ...
class IAppRecordingResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppRecording.IAppRecordingResult'
    _iid_ = Guid('{3a900864-c66d-46f9-b2d9-5bc2dad070d7}')
    @winrt_commethod(6)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_IsFileTruncated(self) -> Boolean: ...
    Duration = property(get_Duration, None)
    ExtendedError = property(get_ExtendedError, None)
    IsFileTruncated = property(get_IsFileTruncated, None)
    Succeeded = property(get_Succeeded, None)
class IAppRecordingSaveScreenshotResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppRecording.IAppRecordingSaveScreenshotResult'
    _iid_ = Guid('{9c5b8d0a-0abb-4457-aaee-24f9c12ec778}')
    @winrt_commethod(6)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_SavedScreenshotInfos(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Media.AppRecording.AppRecordingSavedScreenshotInfo]: ...
    ExtendedError = property(get_ExtendedError, None)
    SavedScreenshotInfos = property(get_SavedScreenshotInfos, None)
    Succeeded = property(get_Succeeded, None)
class IAppRecordingSavedScreenshotInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppRecording.IAppRecordingSavedScreenshotInfo'
    _iid_ = Guid('{9b642d0a-189a-4d00-bf25-e1bb1249d594}')
    @winrt_commethod(6)
    def get_File(self) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_commethod(7)
    def get_MediaEncodingSubtype(self) -> WinRT_String: ...
    File = property(get_File, None)
    MediaEncodingSubtype = property(get_MediaEncodingSubtype, None)
class IAppRecordingStatus(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppRecording.IAppRecordingStatus'
    _iid_ = Guid('{1d0cc82c-bc18-4b8a-a6ef-127efab3b5d9}')
    @winrt_commethod(6)
    def get_CanRecord(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_CanRecordTimeSpan(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_HistoricalBufferDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_Details(self) -> win32more.Windows.Media.AppRecording.AppRecordingStatusDetails: ...
    CanRecord = property(get_CanRecord, None)
    CanRecordTimeSpan = property(get_CanRecordTimeSpan, None)
    Details = property(get_Details, None)
    HistoricalBufferDuration = property(get_HistoricalBufferDuration, None)
class IAppRecordingStatusDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppRecording.IAppRecordingStatusDetails'
    _iid_ = Guid('{b538a9b0-14ed-4412-ac45-6d672c9c9949}')
    @winrt_commethod(6)
    def get_IsAnyAppBroadcasting(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsCaptureResourceUnavailable(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsGameStreamInProgress(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsTimeSpanRecordingDisabled(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsGpuConstrained(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsAppInactive(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsBlockedForApp(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_IsDisabledByUser(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_IsDisabledBySystem(self) -> Boolean: ...
    IsAnyAppBroadcasting = property(get_IsAnyAppBroadcasting, None)
    IsAppInactive = property(get_IsAppInactive, None)
    IsBlockedForApp = property(get_IsBlockedForApp, None)
    IsCaptureResourceUnavailable = property(get_IsCaptureResourceUnavailable, None)
    IsDisabledBySystem = property(get_IsDisabledBySystem, None)
    IsDisabledByUser = property(get_IsDisabledByUser, None)
    IsGameStreamInProgress = property(get_IsGameStreamInProgress, None)
    IsGpuConstrained = property(get_IsGpuConstrained, None)
    IsTimeSpanRecordingDisabled = property(get_IsTimeSpanRecordingDisabled, None)


make_ready(__name__)
