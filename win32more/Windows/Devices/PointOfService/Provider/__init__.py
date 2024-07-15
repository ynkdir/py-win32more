from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.PointOfService
import win32more.Windows.Devices.PointOfService.Provider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class BarcodeScannerDisableScannerRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerDisableScannerRequest
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerDisableScannerRequest'
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerDisableScannerRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerDisableScannerRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerDisableScannerRequest2, reason: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAndDescriptionAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerDisableScannerRequest2, reason: Int32, failedReasonDescription: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class BarcodeScannerDisableScannerRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerDisableScannerRequestEventArgs
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerDisableScannerRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerDisableScannerRequestEventArgs) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerDisableScannerRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerDisableScannerRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class BarcodeScannerEnableScannerRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerEnableScannerRequest
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerEnableScannerRequest'
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerEnableScannerRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerEnableScannerRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerEnableScannerRequest2, reason: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAndDescriptionAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerEnableScannerRequest2, reason: Int32, failedReasonDescription: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class BarcodeScannerEnableScannerRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerEnableScannerRequestEventArgs
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerEnableScannerRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerEnableScannerRequestEventArgs) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerEnableScannerRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerEnableScannerRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class BarcodeScannerFrameReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerFrameReader
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReader'
    @winrt_mixinmethod
    def StartAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerFrameReader) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def StopAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerFrameReader) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def TryAcquireLatestFrameAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerFrameReader) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerVideoFrame]: ...
    @winrt_mixinmethod
    def get_Connection(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerFrameReader) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection: ...
    @winrt_mixinmethod
    def add_FrameArrived(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerFrameReader, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReader, win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReaderFrameArrivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameArrived(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerFrameReader, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Connection = property(get_Connection, None)
    FrameArrived = event()
class BarcodeScannerFrameReaderFrameArrivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerFrameReaderFrameArrivedEventArgs
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReaderFrameArrivedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerFrameReaderFrameArrivedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
class BarcodeScannerGetSymbologyAttributesRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequest
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerGetSymbologyAttributesRequest'
    @winrt_mixinmethod
    def get_Symbology(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequest) -> UInt32: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequest, attributes: win32more.Windows.Devices.PointOfService.BarcodeSymbologyAttributes) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequest2, reason: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAndDescriptionAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequest2, reason: Int32, failedReasonDescription: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    Symbology = property(get_Symbology, None)
class BarcodeScannerGetSymbologyAttributesRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequestEventArgs
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerGetSymbologyAttributesRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequestEventArgs) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerGetSymbologyAttributesRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class BarcodeScannerHideVideoPreviewRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerHideVideoPreviewRequest
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerHideVideoPreviewRequest'
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerHideVideoPreviewRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerHideVideoPreviewRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerHideVideoPreviewRequest2, reason: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAndDescriptionAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerHideVideoPreviewRequest2, reason: Int32, failedReasonDescription: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class BarcodeScannerHideVideoPreviewRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerHideVideoPreviewRequestEventArgs
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerHideVideoPreviewRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerHideVideoPreviewRequestEventArgs) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerHideVideoPreviewRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerHideVideoPreviewRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class BarcodeScannerProviderConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_VideoDeviceId(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SupportedSymbologies(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection) -> win32more.Windows.Foundation.Collections.IVector[UInt32]: ...
    @winrt_mixinmethod
    def get_CompanyName(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CompanyName(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Version(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Version(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection) -> Void: ...
    @winrt_mixinmethod
    def ReportScannedDataAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, report: win32more.Windows.Devices.PointOfService.BarcodeScannerReport) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportTriggerStateAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, state: win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerTriggerState) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportErrorAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, errorData: win32more.Windows.Devices.PointOfService.UnifiedPosErrorData) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportErrorAsyncWithScanReport(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, errorData: win32more.Windows.Devices.PointOfService.UnifiedPosErrorData, isRetriable: Boolean, scanReport: win32more.Windows.Devices.PointOfService.BarcodeScannerReport) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_EnableScannerRequested(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerEnableScannerRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnableScannerRequested(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DisableScannerRequested(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerDisableScannerRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DisableScannerRequested(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SetActiveSymbologiesRequested(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerSetActiveSymbologiesRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SetActiveSymbologiesRequested(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StartSoftwareTriggerRequested(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerStartSoftwareTriggerRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StartSoftwareTriggerRequested(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StopSoftwareTriggerRequested(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerStopSoftwareTriggerRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StopSoftwareTriggerRequested(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GetBarcodeSymbologyAttributesRequested(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerGetSymbologyAttributesRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GetBarcodeSymbologyAttributesRequested(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SetBarcodeSymbologyAttributesRequested(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerSetSymbologyAttributesRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SetBarcodeSymbologyAttributesRequested(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HideVideoPreviewRequested(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerHideVideoPreviewRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HideVideoPreviewRequested(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateFrameReaderAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReader]: ...
    @winrt_mixinmethod
    def CreateFrameReaderWithFormatAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection2, preferredFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReader]: ...
    @winrt_mixinmethod
    def CreateFrameReaderWithFormatAndSizeAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection2, preferredFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, preferredSize: win32more.Windows.Graphics.Imaging.BitmapSize) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReader]: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    CompanyName = property(get_CompanyName, put_CompanyName)
    Id = property(get_Id, None)
    Name = property(get_Name, put_Name)
    SupportedSymbologies = property(get_SupportedSymbologies, None)
    Version = property(get_Version, put_Version)
    VideoDeviceId = property(get_VideoDeviceId, None)
    EnableScannerRequested = event()
    DisableScannerRequested = event()
    SetActiveSymbologiesRequested = event()
    StartSoftwareTriggerRequested = event()
    StopSoftwareTriggerRequested = event()
    GetBarcodeSymbologyAttributesRequested = event()
    SetBarcodeSymbologyAttributesRequested = event()
    HideVideoPreviewRequested = event()
class BarcodeScannerProviderTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderTriggerDetails
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerProviderTriggerDetails'
    @winrt_mixinmethod
    def get_Connection(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderTriggerDetails) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection: ...
    Connection = property(get_Connection, None)
class BarcodeScannerSetActiveSymbologiesRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequest
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerSetActiveSymbologiesRequest'
    @winrt_mixinmethod
    def get_Symbologies(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequest) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequest2, reason: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAndDescriptionAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequest2, reason: Int32, failedReasonDescription: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    Symbologies = property(get_Symbologies, None)
class BarcodeScannerSetActiveSymbologiesRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequestEventArgs
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerSetActiveSymbologiesRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequestEventArgs) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerSetActiveSymbologiesRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class BarcodeScannerSetSymbologyAttributesRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequest
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerSetSymbologyAttributesRequest'
    @winrt_mixinmethod
    def get_Symbology(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequest) -> UInt32: ...
    @winrt_mixinmethod
    def get_Attributes(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequest) -> win32more.Windows.Devices.PointOfService.BarcodeSymbologyAttributes: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequest2, reason: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAndDescriptionAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequest2, reason: Int32, failedReasonDescription: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
    Attributes = property(get_Attributes, None)
    Symbology = property(get_Symbology, None)
class BarcodeScannerSetSymbologyAttributesRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequestEventArgs
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerSetSymbologyAttributesRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequestEventArgs) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerSetSymbologyAttributesRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class BarcodeScannerStartSoftwareTriggerRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerStartSoftwareTriggerRequest
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerStartSoftwareTriggerRequest'
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerStartSoftwareTriggerRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerStartSoftwareTriggerRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerStartSoftwareTriggerRequest2, reason: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAndDescriptionAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerStartSoftwareTriggerRequest2, reason: Int32, failedReasonDescription: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class BarcodeScannerStartSoftwareTriggerRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerStartSoftwareTriggerRequestEventArgs
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerStartSoftwareTriggerRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerStartSoftwareTriggerRequestEventArgs) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerStartSoftwareTriggerRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerStartSoftwareTriggerRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class BarcodeScannerStopSoftwareTriggerRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerStopSoftwareTriggerRequest
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerStopSoftwareTriggerRequest'
    @winrt_mixinmethod
    def ReportCompletedAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerStopSoftwareTriggerRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerStopSoftwareTriggerRequest) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerStopSoftwareTriggerRequest2, reason: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAndDescriptionAsync(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerStopSoftwareTriggerRequest2, reason: Int32, failedReasonDescription: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class BarcodeScannerStopSoftwareTriggerRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerStopSoftwareTriggerRequestEventArgs
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerStopSoftwareTriggerRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerStopSoftwareTriggerRequestEventArgs) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerStopSoftwareTriggerRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerStopSoftwareTriggerRequestEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class BarcodeScannerTriggerState(Enum, Int32):
    Released = 0
    Pressed = 1
class BarcodeScannerVideoFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerVideoFrame
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeScannerVideoFrame'
    @winrt_mixinmethod
    def get_Format(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerVideoFrame) -> win32more.Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_mixinmethod
    def get_Width(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerVideoFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerVideoFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_PixelData(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeScannerVideoFrame) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Format = property(get_Format, None)
    Height = property(get_Height, None)
    PixelData = property(get_PixelData, None)
    Width = property(get_Width, None)
class BarcodeSymbologyAttributesBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.PointOfService.Provider.IBarcodeSymbologyAttributesBuilder
    _classid_ = 'Windows.Devices.PointOfService.Provider.BarcodeSymbologyAttributesBuilder'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.PointOfService.Provider.BarcodeSymbologyAttributesBuilder.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeSymbologyAttributesBuilder: ...
    @winrt_mixinmethod
    def get_IsCheckDigitValidationSupported(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeSymbologyAttributesBuilder) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCheckDigitValidationSupported(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeSymbologyAttributesBuilder, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsCheckDigitTransmissionSupported(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeSymbologyAttributesBuilder) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCheckDigitTransmissionSupported(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeSymbologyAttributesBuilder, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDecodeLengthSupported(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeSymbologyAttributesBuilder) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDecodeLengthSupported(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeSymbologyAttributesBuilder, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def CreateAttributes(self: win32more.Windows.Devices.PointOfService.Provider.IBarcodeSymbologyAttributesBuilder) -> win32more.Windows.Devices.PointOfService.BarcodeSymbologyAttributes: ...
    IsCheckDigitTransmissionSupported = property(get_IsCheckDigitTransmissionSupported, put_IsCheckDigitTransmissionSupported)
    IsCheckDigitValidationSupported = property(get_IsCheckDigitValidationSupported, put_IsCheckDigitValidationSupported)
    IsDecodeLengthSupported = property(get_IsDecodeLengthSupported, put_IsDecodeLengthSupported)
class IBarcodeScannerDisableScannerRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerDisableScannerRequest'
    _iid_ = Guid('{88ecf7c0-37b9-4275-8e77-c8e52ae5a9c8}')
    @winrt_commethod(6)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerDisableScannerRequest2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerDisableScannerRequest2'
    _iid_ = Guid('{ccdfe625-65c3-4ccc-b457-f39c7a9ea60d}')
    @winrt_commethod(6)
    def ReportFailedWithFailedReasonAsync(self, reason: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedWithFailedReasonAndDescriptionAsync(self, reason: Int32, failedReasonDescription: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerDisableScannerRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerDisableScannerRequestEventArgs'
    _iid_ = Guid('{7006e142-e802-46f5-b604-352a15ce9232}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerDisableScannerRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IBarcodeScannerEnableScannerRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerEnableScannerRequest'
    _iid_ = Guid('{c0b3e9ba-816a-452b-bd77-b7e453ec446d}')
    @winrt_commethod(6)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerEnableScannerRequest2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerEnableScannerRequest2'
    _iid_ = Guid('{71a4f2a8-9905-41ac-9121-b645916a84a1}')
    @winrt_commethod(6)
    def ReportFailedWithFailedReasonAsync(self, reason: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedWithFailedReasonAndDescriptionAsync(self, reason: Int32, failedReasonDescription: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerEnableScannerRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerEnableScannerRequestEventArgs'
    _iid_ = Guid('{956c9419-7b4e-4451-8c41-8e10cfbc5b41}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerEnableScannerRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IBarcodeScannerFrameReader(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerFrameReader'
    _iid_ = Guid('{dbc72b07-64c3-482b-93c8-65fb33c22208}')
    @winrt_commethod(6)
    def StartAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def StopAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def TryAcquireLatestFrameAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerVideoFrame]: ...
    @winrt_commethod(9)
    def get_Connection(self) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection: ...
    @winrt_commethod(10)
    def add_FrameArrived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReader, win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReaderFrameArrivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_FrameArrived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Connection = property(get_Connection, None)
    FrameArrived = event()
class IBarcodeScannerFrameReaderFrameArrivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerFrameReaderFrameArrivedEventArgs'
    _iid_ = Guid('{b0bbd604-54fd-436d-8629-712e787223dd}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
class IBarcodeScannerGetSymbologyAttributesRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequest'
    _iid_ = Guid('{9774c46a-58e4-4c5f-b8e9-e41467632700}')
    @winrt_commethod(6)
    def get_Symbology(self) -> UInt32: ...
    @winrt_commethod(7)
    def ReportCompletedAsync(self, attributes: win32more.Windows.Devices.PointOfService.BarcodeSymbologyAttributes) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    Symbology = property(get_Symbology, None)
class IBarcodeScannerGetSymbologyAttributesRequest2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequest2'
    _iid_ = Guid('{6a6a2b13-75a8-49fb-b852-bfb93d760af7}')
    @winrt_commethod(6)
    def ReportFailedWithFailedReasonAsync(self, reason: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedWithFailedReasonAndDescriptionAsync(self, reason: Int32, failedReasonDescription: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerGetSymbologyAttributesRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequestEventArgs'
    _iid_ = Guid('{7f89de3e-fb5d-493c-b402-356b24d574a6}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerGetSymbologyAttributesRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IBarcodeScannerHideVideoPreviewRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerHideVideoPreviewRequest'
    _iid_ = Guid('{fa4ebe7f-6670-40e1-b90b-bb10d8d425fa}')
    @winrt_commethod(6)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerHideVideoPreviewRequest2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerHideVideoPreviewRequest2'
    _iid_ = Guid('{7e28435d-9814-431d-a2f2-d6248c5ad4b5}')
    @winrt_commethod(6)
    def ReportFailedWithFailedReasonAsync(self, reason: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedWithFailedReasonAndDescriptionAsync(self, reason: Int32, failedReasonDescription: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerHideVideoPreviewRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerHideVideoPreviewRequestEventArgs'
    _iid_ = Guid('{16a281fc-d6be-4bc7-9df1-33741f3eadea}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerHideVideoPreviewRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IBarcodeScannerProviderConnection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection'
    _iid_ = Guid('{b44acbed-0b3a-4fa3-86c5-491ea30780eb}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_VideoDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SupportedSymbologies(self) -> win32more.Windows.Foundation.Collections.IVector[UInt32]: ...
    @winrt_commethod(9)
    def get_CompanyName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_CompanyName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_Name(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_Version(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_Version(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def Start(self) -> Void: ...
    @winrt_commethod(16)
    def ReportScannedDataAsync(self, report: win32more.Windows.Devices.PointOfService.BarcodeScannerReport) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def ReportTriggerStateAsync(self, state: win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerTriggerState) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def ReportErrorAsync(self, errorData: win32more.Windows.Devices.PointOfService.UnifiedPosErrorData) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(19)
    def ReportErrorAsyncWithScanReport(self, errorData: win32more.Windows.Devices.PointOfService.UnifiedPosErrorData, isRetriable: Boolean, scanReport: win32more.Windows.Devices.PointOfService.BarcodeScannerReport) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(20)
    def add_EnableScannerRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerEnableScannerRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_EnableScannerRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def add_DisableScannerRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerDisableScannerRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_DisableScannerRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(24)
    def add_SetActiveSymbologiesRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerSetActiveSymbologiesRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(25)
    def remove_SetActiveSymbologiesRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(26)
    def add_StartSoftwareTriggerRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerStartSoftwareTriggerRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(27)
    def remove_StartSoftwareTriggerRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(28)
    def add_StopSoftwareTriggerRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerStopSoftwareTriggerRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(29)
    def remove_StopSoftwareTriggerRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(30)
    def add_GetBarcodeSymbologyAttributesRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerGetSymbologyAttributesRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(31)
    def remove_GetBarcodeSymbologyAttributesRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(32)
    def add_SetBarcodeSymbologyAttributesRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerSetSymbologyAttributesRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(33)
    def remove_SetBarcodeSymbologyAttributesRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(34)
    def add_HideVideoPreviewRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerHideVideoPreviewRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(35)
    def remove_HideVideoPreviewRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CompanyName = property(get_CompanyName, put_CompanyName)
    Id = property(get_Id, None)
    Name = property(get_Name, put_Name)
    SupportedSymbologies = property(get_SupportedSymbologies, None)
    Version = property(get_Version, put_Version)
    VideoDeviceId = property(get_VideoDeviceId, None)
    EnableScannerRequested = event()
    DisableScannerRequested = event()
    SetActiveSymbologiesRequested = event()
    StartSoftwareTriggerRequested = event()
    StopSoftwareTriggerRequested = event()
    GetBarcodeSymbologyAttributesRequested = event()
    SetBarcodeSymbologyAttributesRequested = event()
    HideVideoPreviewRequested = event()
class IBarcodeScannerProviderConnection2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection2'
    _iid_ = Guid('{be9b53cd-1134-418c-a06b-04423a73f3d7}')
    @winrt_commethod(6)
    def CreateFrameReaderAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReader]: ...
    @winrt_commethod(7)
    def CreateFrameReaderWithFormatAsync(self, preferredFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReader]: ...
    @winrt_commethod(8)
    def CreateFrameReaderWithFormatAndSizeAsync(self, preferredFormat: win32more.Windows.Graphics.Imaging.BitmapPixelFormat, preferredSize: win32more.Windows.Graphics.Imaging.BitmapSize) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReader]: ...
class IBarcodeScannerProviderTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderTriggerDetails'
    _iid_ = Guid('{50856d82-24e3-48ce-99c7-70aac1cbc9f7}')
    @winrt_commethod(6)
    def get_Connection(self) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection: ...
    Connection = property(get_Connection, None)
class IBarcodeScannerSetActiveSymbologiesRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequest'
    _iid_ = Guid('{db3f32b9-f7da-41a1-9f79-07bcd95f0bdf}')
    @winrt_commethod(6)
    def get_Symbologies(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(7)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    Symbologies = property(get_Symbologies, None)
class IBarcodeScannerSetActiveSymbologiesRequest2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequest2'
    _iid_ = Guid('{f5ff6edf-fa9a-4749-b11b-e8fccb75bc6b}')
    @winrt_commethod(6)
    def ReportFailedWithFailedReasonAsync(self, reason: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedWithFailedReasonAndDescriptionAsync(self, reason: Int32, failedReasonDescription: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerSetActiveSymbologiesRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequestEventArgs'
    _iid_ = Guid('{06305afa-7bf6-4d52-801a-330272f60ae1}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerSetActiveSymbologiesRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IBarcodeScannerSetSymbologyAttributesRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequest'
    _iid_ = Guid('{32fb814f-a37f-48b0-acea-dce1480f12ae}')
    @winrt_commethod(6)
    def get_Symbology(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Attributes(self) -> win32more.Windows.Devices.PointOfService.BarcodeSymbologyAttributes: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    Attributes = property(get_Attributes, None)
    Symbology = property(get_Symbology, None)
class IBarcodeScannerSetSymbologyAttributesRequest2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequest2'
    _iid_ = Guid('{dffbbfc1-dba8-4b77-be1e-b56cd72f65b3}')
    @winrt_commethod(6)
    def ReportFailedWithFailedReasonAsync(self, reason: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedWithFailedReasonAndDescriptionAsync(self, reason: Int32, failedReasonDescription: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerSetSymbologyAttributesRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequestEventArgs'
    _iid_ = Guid('{b2b89809-9824-47d4-85bd-d0077baa7bd2}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerSetSymbologyAttributesRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IBarcodeScannerStartSoftwareTriggerRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerStartSoftwareTriggerRequest'
    _iid_ = Guid('{e3fa7b27-ff62-4454-af4a-cb6144a3e3f7}')
    @winrt_commethod(6)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerStartSoftwareTriggerRequest2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerStartSoftwareTriggerRequest2'
    _iid_ = Guid('{eb72a25c-6658-4765-a68e-327482653deb}')
    @winrt_commethod(6)
    def ReportFailedWithFailedReasonAsync(self, reason: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedWithFailedReasonAndDescriptionAsync(self, reason: Int32, failedReasonDescription: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerStartSoftwareTriggerRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerStartSoftwareTriggerRequestEventArgs'
    _iid_ = Guid('{2305d843-c88f-4f3b-8c3b-d3df071051ec}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerStartSoftwareTriggerRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IBarcodeScannerStopSoftwareTriggerRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerStopSoftwareTriggerRequest'
    _iid_ = Guid('{6f9faf35-e287-4ca8-b70d-5a91d694f668}')
    @winrt_commethod(6)
    def ReportCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerStopSoftwareTriggerRequest2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerStopSoftwareTriggerRequest2'
    _iid_ = Guid('{cb57c5dd-fe50-49f8-a0b4-bdc230814da2}')
    @winrt_commethod(6)
    def ReportFailedWithFailedReasonAsync(self, reason: Int32) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedWithFailedReasonAndDescriptionAsync(self, reason: Int32, failedReasonDescription: WinRT_String) -> win32more.Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerStopSoftwareTriggerRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerStopSoftwareTriggerRequestEventArgs'
    _iid_ = Guid('{eac34450-4eb7-481a-9273-147a273b99b8}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Windows.Devices.PointOfService.Provider.BarcodeScannerStopSoftwareTriggerRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IBarcodeScannerVideoFrame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeScannerVideoFrame'
    _iid_ = Guid('{7e585248-9df7-4121-a175-801d8000112e}')
    @winrt_commethod(6)
    def get_Format(self) -> win32more.Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_commethod(7)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Height(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_PixelData(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    Format = property(get_Format, None)
    Height = property(get_Height, None)
    PixelData = property(get_PixelData, None)
    Width = property(get_Width, None)
class IBarcodeSymbologyAttributesBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.Provider.IBarcodeSymbologyAttributesBuilder'
    _iid_ = Guid('{c57b0cbf-e4f5-40b9-84cf-e63fbaea42b4}')
    @winrt_commethod(6)
    def get_IsCheckDigitValidationSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsCheckDigitValidationSupported(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsCheckDigitTransmissionSupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsCheckDigitTransmissionSupported(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_IsDecodeLengthSupported(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsDecodeLengthSupported(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def CreateAttributes(self) -> win32more.Windows.Devices.PointOfService.BarcodeSymbologyAttributes: ...
    IsCheckDigitTransmissionSupported = property(get_IsCheckDigitTransmissionSupported, put_IsCheckDigitTransmissionSupported)
    IsCheckDigitValidationSupported = property(get_IsCheckDigitValidationSupported, put_IsCheckDigitValidationSupported)
    IsDecodeLengthSupported = property(get_IsDecodeLengthSupported, put_IsDecodeLengthSupported)


make_ready(__name__)
