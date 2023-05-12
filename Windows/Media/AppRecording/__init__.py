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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Media.AppRecording
import Windows.Storage
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
AppRecordingContract: UInt32 = 65536
class AppRecordingManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.AppRecording.IAppRecordingManager
    _classid_ = 'Windows.Media.AppRecording.AppRecordingManager'
    @winrt_mixinmethod
    def GetStatus(self: Windows.Media.AppRecording.IAppRecordingManager) -> Windows.Media.AppRecording.AppRecordingStatus: ...
    @winrt_mixinmethod
    def StartRecordingToFileAsync(self: Windows.Media.AppRecording.IAppRecordingManager, file: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Media.AppRecording.AppRecordingResult]: ...
    @winrt_mixinmethod
    def RecordTimeSpanToFileAsync(self: Windows.Media.AppRecording.IAppRecordingManager, startTime: Windows.Foundation.DateTime, duration: Windows.Foundation.TimeSpan, file: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Media.AppRecording.AppRecordingResult]: ...
    @winrt_mixinmethod
    def get_SupportedScreenshotMediaEncodingSubtypes(self: Windows.Media.AppRecording.IAppRecordingManager) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def SaveScreenshotToFilesAsync(self: Windows.Media.AppRecording.IAppRecordingManager, folder: Windows.Storage.StorageFolder, filenamePrefix: WinRT_String, option: Windows.Media.AppRecording.AppRecordingSaveScreenshotOption, requestedFormats: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Media.AppRecording.AppRecordingSaveScreenshotResult]: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Media.AppRecording.IAppRecordingManagerStatics) -> Windows.Media.AppRecording.AppRecordingManager: ...
    SupportedScreenshotMediaEncodingSubtypes = property(get_SupportedScreenshotMediaEncodingSubtypes, None)
class AppRecordingResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.AppRecording.IAppRecordingResult
    _classid_ = 'Windows.Media.AppRecording.AppRecordingResult'
    @winrt_mixinmethod
    def get_Succeeded(self: Windows.Media.AppRecording.IAppRecordingResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Media.AppRecording.IAppRecordingResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.Media.AppRecording.IAppRecordingResult) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_IsFileTruncated(self: Windows.Media.AppRecording.IAppRecordingResult) -> Boolean: ...
    Succeeded = property(get_Succeeded, None)
    ExtendedError = property(get_ExtendedError, None)
    Duration = property(get_Duration, None)
    IsFileTruncated = property(get_IsFileTruncated, None)
AppRecordingSaveScreenshotOption = Int32
AppRecordingSaveScreenshotOption_None: AppRecordingSaveScreenshotOption = 0
AppRecordingSaveScreenshotOption_HdrContentVisible: AppRecordingSaveScreenshotOption = 1
class AppRecordingSaveScreenshotResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.AppRecording.IAppRecordingSaveScreenshotResult
    _classid_ = 'Windows.Media.AppRecording.AppRecordingSaveScreenshotResult'
    @winrt_mixinmethod
    def get_Succeeded(self: Windows.Media.AppRecording.IAppRecordingSaveScreenshotResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.Media.AppRecording.IAppRecordingSaveScreenshotResult) -> Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_SavedScreenshotInfos(self: Windows.Media.AppRecording.IAppRecordingSaveScreenshotResult) -> Windows.Foundation.Collections.IVectorView[Windows.Media.AppRecording.AppRecordingSavedScreenshotInfo]: ...
    Succeeded = property(get_Succeeded, None)
    ExtendedError = property(get_ExtendedError, None)
    SavedScreenshotInfos = property(get_SavedScreenshotInfos, None)
class AppRecordingSavedScreenshotInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.AppRecording.IAppRecordingSavedScreenshotInfo
    _classid_ = 'Windows.Media.AppRecording.AppRecordingSavedScreenshotInfo'
    @winrt_mixinmethod
    def get_File(self: Windows.Media.AppRecording.IAppRecordingSavedScreenshotInfo) -> Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def get_MediaEncodingSubtype(self: Windows.Media.AppRecording.IAppRecordingSavedScreenshotInfo) -> WinRT_String: ...
    File = property(get_File, None)
    MediaEncodingSubtype = property(get_MediaEncodingSubtype, None)
class AppRecordingStatus(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.AppRecording.IAppRecordingStatus
    _classid_ = 'Windows.Media.AppRecording.AppRecordingStatus'
    @winrt_mixinmethod
    def get_CanRecord(self: Windows.Media.AppRecording.IAppRecordingStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanRecordTimeSpan(self: Windows.Media.AppRecording.IAppRecordingStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_HistoricalBufferDuration(self: Windows.Media.AppRecording.IAppRecordingStatus) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Details(self: Windows.Media.AppRecording.IAppRecordingStatus) -> Windows.Media.AppRecording.AppRecordingStatusDetails: ...
    CanRecord = property(get_CanRecord, None)
    CanRecordTimeSpan = property(get_CanRecordTimeSpan, None)
    HistoricalBufferDuration = property(get_HistoricalBufferDuration, None)
    Details = property(get_Details, None)
class AppRecordingStatusDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.AppRecording.IAppRecordingStatusDetails
    _classid_ = 'Windows.Media.AppRecording.AppRecordingStatusDetails'
    @winrt_mixinmethod
    def get_IsAnyAppBroadcasting(self: Windows.Media.AppRecording.IAppRecordingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCaptureResourceUnavailable(self: Windows.Media.AppRecording.IAppRecordingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsGameStreamInProgress(self: Windows.Media.AppRecording.IAppRecordingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTimeSpanRecordingDisabled(self: Windows.Media.AppRecording.IAppRecordingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsGpuConstrained(self: Windows.Media.AppRecording.IAppRecordingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsAppInactive(self: Windows.Media.AppRecording.IAppRecordingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBlockedForApp(self: Windows.Media.AppRecording.IAppRecordingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDisabledByUser(self: Windows.Media.AppRecording.IAppRecordingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDisabledBySystem(self: Windows.Media.AppRecording.IAppRecordingStatusDetails) -> Boolean: ...
    IsAnyAppBroadcasting = property(get_IsAnyAppBroadcasting, None)
    IsCaptureResourceUnavailable = property(get_IsCaptureResourceUnavailable, None)
    IsGameStreamInProgress = property(get_IsGameStreamInProgress, None)
    IsTimeSpanRecordingDisabled = property(get_IsTimeSpanRecordingDisabled, None)
    IsGpuConstrained = property(get_IsGpuConstrained, None)
    IsAppInactive = property(get_IsAppInactive, None)
    IsBlockedForApp = property(get_IsBlockedForApp, None)
    IsDisabledByUser = property(get_IsDisabledByUser, None)
    IsDisabledBySystem = property(get_IsDisabledBySystem, None)
class IAppRecordingManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppRecording.IAppRecordingManager'
    _iid_ = Guid('{e7e26076-a044-48e2-a512-3094d574c7cc}')
    @winrt_commethod(6)
    def GetStatus(self) -> Windows.Media.AppRecording.AppRecordingStatus: ...
    @winrt_commethod(7)
    def StartRecordingToFileAsync(self, file: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Media.AppRecording.AppRecordingResult]: ...
    @winrt_commethod(8)
    def RecordTimeSpanToFileAsync(self, startTime: Windows.Foundation.DateTime, duration: Windows.Foundation.TimeSpan, file: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Media.AppRecording.AppRecordingResult]: ...
    @winrt_commethod(9)
    def get_SupportedScreenshotMediaEncodingSubtypes(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def SaveScreenshotToFilesAsync(self, folder: Windows.Storage.StorageFolder, filenamePrefix: WinRT_String, option: Windows.Media.AppRecording.AppRecordingSaveScreenshotOption, requestedFormats: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Media.AppRecording.AppRecordingSaveScreenshotResult]: ...
    SupportedScreenshotMediaEncodingSubtypes = property(get_SupportedScreenshotMediaEncodingSubtypes, None)
class IAppRecordingManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppRecording.IAppRecordingManagerStatics'
    _iid_ = Guid('{50e709f7-38ce-4bd3-9db2-e72bbe9de11d}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Media.AppRecording.AppRecordingManager: ...
class IAppRecordingResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppRecording.IAppRecordingResult'
    _iid_ = Guid('{3a900864-c66d-46f9-b2d9-5bc2dad070d7}')
    @winrt_commethod(6)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_Duration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_IsFileTruncated(self) -> Boolean: ...
    Succeeded = property(get_Succeeded, None)
    ExtendedError = property(get_ExtendedError, None)
    Duration = property(get_Duration, None)
    IsFileTruncated = property(get_IsFileTruncated, None)
class IAppRecordingSaveScreenshotResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppRecording.IAppRecordingSaveScreenshotResult'
    _iid_ = Guid('{9c5b8d0a-0abb-4457-aaee-24f9c12ec778}')
    @winrt_commethod(6)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_SavedScreenshotInfos(self) -> Windows.Foundation.Collections.IVectorView[Windows.Media.AppRecording.AppRecordingSavedScreenshotInfo]: ...
    Succeeded = property(get_Succeeded, None)
    ExtendedError = property(get_ExtendedError, None)
    SavedScreenshotInfos = property(get_SavedScreenshotInfos, None)
class IAppRecordingSavedScreenshotInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppRecording.IAppRecordingSavedScreenshotInfo'
    _iid_ = Guid('{9b642d0a-189a-4d00-bf25-e1bb1249d594}')
    @winrt_commethod(6)
    def get_File(self) -> Windows.Storage.StorageFile: ...
    @winrt_commethod(7)
    def get_MediaEncodingSubtype(self) -> WinRT_String: ...
    File = property(get_File, None)
    MediaEncodingSubtype = property(get_MediaEncodingSubtype, None)
class IAppRecordingStatus(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppRecording.IAppRecordingStatus'
    _iid_ = Guid('{1d0cc82c-bc18-4b8a-a6ef-127efab3b5d9}')
    @winrt_commethod(6)
    def get_CanRecord(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_CanRecordTimeSpan(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_HistoricalBufferDuration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_Details(self) -> Windows.Media.AppRecording.AppRecordingStatusDetails: ...
    CanRecord = property(get_CanRecord, None)
    CanRecordTimeSpan = property(get_CanRecordTimeSpan, None)
    HistoricalBufferDuration = property(get_HistoricalBufferDuration, None)
    Details = property(get_Details, None)
class IAppRecordingStatusDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    IsCaptureResourceUnavailable = property(get_IsCaptureResourceUnavailable, None)
    IsGameStreamInProgress = property(get_IsGameStreamInProgress, None)
    IsTimeSpanRecordingDisabled = property(get_IsTimeSpanRecordingDisabled, None)
    IsGpuConstrained = property(get_IsGpuConstrained, None)
    IsAppInactive = property(get_IsAppInactive, None)
    IsBlockedForApp = property(get_IsBlockedForApp, None)
    IsDisabledByUser = property(get_IsDisabledByUser, None)
    IsDisabledBySystem = property(get_IsDisabledBySystem, None)
make_head(_module, 'AppRecordingManager')
make_head(_module, 'AppRecordingResult')
make_head(_module, 'AppRecordingSaveScreenshotResult')
make_head(_module, 'AppRecordingSavedScreenshotInfo')
make_head(_module, 'AppRecordingStatus')
make_head(_module, 'AppRecordingStatusDetails')
make_head(_module, 'IAppRecordingManager')
make_head(_module, 'IAppRecordingManagerStatics')
make_head(_module, 'IAppRecordingResult')
make_head(_module, 'IAppRecordingSaveScreenshotResult')
make_head(_module, 'IAppRecordingSavedScreenshotInfo')
make_head(_module, 'IAppRecordingStatus')
make_head(_module, 'IAppRecordingStatusDetails')
