from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Devices.PointOfService
import Windows.Devices.PointOfService.Provider
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics.Imaging
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
class BarcodeScannerDisableScannerRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerDisableScannerRequest'
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerDisableScannerRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerDisableScannerRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerDisableScannerRequest2, reason: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAndDescriptionAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerDisableScannerRequest2, reason: Int32, failedReasonDescription: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class BarcodeScannerDisableScannerRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerDisableScannerRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerDisableScannerRequestEventArgs) -> Windows.Devices.PointOfService.Provider.BarcodeScannerDisableScannerRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerDisableScannerRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class BarcodeScannerEnableScannerRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerEnableScannerRequest'
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerEnableScannerRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerEnableScannerRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerEnableScannerRequest2, reason: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAndDescriptionAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerEnableScannerRequest2, reason: Int32, failedReasonDescription: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class BarcodeScannerEnableScannerRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerEnableScannerRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerEnableScannerRequestEventArgs) -> Windows.Devices.PointOfService.Provider.BarcodeScannerEnableScannerRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerEnableScannerRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class BarcodeScannerFrameReader(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReader'
    @winrt_mixinmethod
    def StartAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerFrameReader) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def StopAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerFrameReader) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def TryAcquireLatestFrameAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerFrameReader) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.Provider.BarcodeScannerVideoFrame]: ...
    @winrt_mixinmethod
    def get_Connection(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerFrameReader) -> Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection: ...
    @winrt_mixinmethod
    def add_FrameArrived(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerFrameReader, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReader, Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReaderFrameArrivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameArrived(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerFrameReader, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Connection = property(get_Connection, None)
class BarcodeScannerFrameReaderFrameArrivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReaderFrameArrivedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerFrameReaderFrameArrivedEventArgs) -> Windows.Foundation.Deferral: ...
class BarcodeScannerGetSymbologyAttributesRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerGetSymbologyAttributesRequest'
    @winrt_mixinmethod
    def get_Symbology(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequest) -> UInt32: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequest, attributes: Windows.Devices.PointOfService.BarcodeSymbologyAttributes) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequest2, reason: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAndDescriptionAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequest2, reason: Int32, failedReasonDescription: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    Symbology = property(get_Symbology, None)
class BarcodeScannerGetSymbologyAttributesRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerGetSymbologyAttributesRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequestEventArgs) -> Windows.Devices.PointOfService.Provider.BarcodeScannerGetSymbologyAttributesRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerGetSymbologyAttributesRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class BarcodeScannerHideVideoPreviewRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerHideVideoPreviewRequest'
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerHideVideoPreviewRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerHideVideoPreviewRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerHideVideoPreviewRequest2, reason: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAndDescriptionAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerHideVideoPreviewRequest2, reason: Int32, failedReasonDescription: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class BarcodeScannerHideVideoPreviewRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerHideVideoPreviewRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerHideVideoPreviewRequestEventArgs) -> Windows.Devices.PointOfService.Provider.BarcodeScannerHideVideoPreviewRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerHideVideoPreviewRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class BarcodeScannerProviderConnection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_VideoDeviceId(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SupportedSymbologies(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection) -> Windows.Foundation.Collections.IVector[UInt32]: ...
    @winrt_mixinmethod
    def get_CompanyName(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CompanyName(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Name(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Version(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Version(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection) -> Void: ...
    @winrt_mixinmethod
    def ReportScannedDataAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, report: Windows.Devices.PointOfService.BarcodeScannerReport) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportTriggerStateAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, state: Windows.Devices.PointOfService.Provider.BarcodeScannerTriggerState) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportErrorAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, errorData: Windows.Devices.PointOfService.UnifiedPosErrorData) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportErrorAsyncWithScanReport(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, errorData: Windows.Devices.PointOfService.UnifiedPosErrorData, isRetriable: Boolean, scanReport: Windows.Devices.PointOfService.BarcodeScannerReport) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_EnableScannerRequested(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, Windows.Devices.PointOfService.Provider.BarcodeScannerEnableScannerRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnableScannerRequested(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DisableScannerRequested(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, Windows.Devices.PointOfService.Provider.BarcodeScannerDisableScannerRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DisableScannerRequested(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SetActiveSymbologiesRequested(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, Windows.Devices.PointOfService.Provider.BarcodeScannerSetActiveSymbologiesRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SetActiveSymbologiesRequested(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StartSoftwareTriggerRequested(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, Windows.Devices.PointOfService.Provider.BarcodeScannerStartSoftwareTriggerRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StartSoftwareTriggerRequested(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StopSoftwareTriggerRequested(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, Windows.Devices.PointOfService.Provider.BarcodeScannerStopSoftwareTriggerRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StopSoftwareTriggerRequested(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GetBarcodeSymbologyAttributesRequested(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, Windows.Devices.PointOfService.Provider.BarcodeScannerGetSymbologyAttributesRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GetBarcodeSymbologyAttributesRequested(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SetBarcodeSymbologyAttributesRequested(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, Windows.Devices.PointOfService.Provider.BarcodeScannerSetSymbologyAttributesRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SetBarcodeSymbologyAttributesRequested(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HideVideoPreviewRequested(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, Windows.Devices.PointOfService.Provider.BarcodeScannerHideVideoPreviewRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HideVideoPreviewRequested(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreateFrameReaderAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection2) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReader]: ...
    @winrt_mixinmethod
    def CreateFrameReaderWithFormatAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection2, preferredFormat: Windows.Graphics.Imaging.BitmapPixelFormat) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReader]: ...
    @winrt_mixinmethod
    def CreateFrameReaderWithFormatAndSizeAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderConnection2, preferredFormat: Windows.Graphics.Imaging.BitmapPixelFormat, preferredSize: Windows.Graphics.Imaging.BitmapSize) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReader]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Id = property(get_Id, None)
    VideoDeviceId = property(get_VideoDeviceId, None)
    SupportedSymbologies = property(get_SupportedSymbologies, None)
    CompanyName = property(get_CompanyName, put_CompanyName)
    Name = property(get_Name, put_Name)
    Version = property(get_Version, put_Version)
class BarcodeScannerProviderTriggerDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerProviderTriggerDetails'
    @winrt_mixinmethod
    def get_Connection(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerProviderTriggerDetails) -> Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection: ...
    Connection = property(get_Connection, None)
class BarcodeScannerSetActiveSymbologiesRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerSetActiveSymbologiesRequest'
    @winrt_mixinmethod
    def get_Symbologies(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequest) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequest2, reason: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAndDescriptionAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequest2, reason: Int32, failedReasonDescription: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    Symbologies = property(get_Symbologies, None)
class BarcodeScannerSetActiveSymbologiesRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerSetActiveSymbologiesRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequestEventArgs) -> Windows.Devices.PointOfService.Provider.BarcodeScannerSetActiveSymbologiesRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerSetActiveSymbologiesRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class BarcodeScannerSetSymbologyAttributesRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerSetSymbologyAttributesRequest'
    @winrt_mixinmethod
    def get_Symbology(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequest) -> UInt32: ...
    @winrt_mixinmethod
    def get_Attributes(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequest) -> Windows.Devices.PointOfService.BarcodeSymbologyAttributes: ...
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequest2, reason: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAndDescriptionAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequest2, reason: Int32, failedReasonDescription: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    Symbology = property(get_Symbology, None)
    Attributes = property(get_Attributes, None)
class BarcodeScannerSetSymbologyAttributesRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerSetSymbologyAttributesRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequestEventArgs) -> Windows.Devices.PointOfService.Provider.BarcodeScannerSetSymbologyAttributesRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerSetSymbologyAttributesRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class BarcodeScannerStartSoftwareTriggerRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerStartSoftwareTriggerRequest'
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerStartSoftwareTriggerRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerStartSoftwareTriggerRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerStartSoftwareTriggerRequest2, reason: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAndDescriptionAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerStartSoftwareTriggerRequest2, reason: Int32, failedReasonDescription: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class BarcodeScannerStartSoftwareTriggerRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerStartSoftwareTriggerRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerStartSoftwareTriggerRequestEventArgs) -> Windows.Devices.PointOfService.Provider.BarcodeScannerStartSoftwareTriggerRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerStartSoftwareTriggerRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class BarcodeScannerStopSoftwareTriggerRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerStopSoftwareTriggerRequest'
    @winrt_mixinmethod
    def ReportCompletedAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerStopSoftwareTriggerRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerStopSoftwareTriggerRequest) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerStopSoftwareTriggerRequest2, reason: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ReportFailedWithFailedReasonAndDescriptionAsync(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerStopSoftwareTriggerRequest2, reason: Int32, failedReasonDescription: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class BarcodeScannerStopSoftwareTriggerRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerStopSoftwareTriggerRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerStopSoftwareTriggerRequestEventArgs) -> Windows.Devices.PointOfService.Provider.BarcodeScannerStopSoftwareTriggerRequest: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerStopSoftwareTriggerRequestEventArgs) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
BarcodeScannerTriggerState = Int32
BarcodeScannerTriggerState_Released: BarcodeScannerTriggerState = 0
BarcodeScannerTriggerState_Pressed: BarcodeScannerTriggerState = 1
class BarcodeScannerVideoFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeScannerVideoFrame'
    @winrt_mixinmethod
    def get_Format(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerVideoFrame) -> Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_mixinmethod
    def get_Width(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerVideoFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerVideoFrame) -> UInt32: ...
    @winrt_mixinmethod
    def get_PixelData(self: Windows.Devices.PointOfService.Provider.IBarcodeScannerVideoFrame) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Format = property(get_Format, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    PixelData = property(get_PixelData, None)
class BarcodeSymbologyAttributesBuilder(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.PointOfService.Provider.BarcodeSymbologyAttributesBuilder'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.PointOfService.Provider.BarcodeSymbologyAttributesBuilder: ...
    @winrt_mixinmethod
    def get_IsCheckDigitValidationSupported(self: Windows.Devices.PointOfService.Provider.IBarcodeSymbologyAttributesBuilder) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCheckDigitValidationSupported(self: Windows.Devices.PointOfService.Provider.IBarcodeSymbologyAttributesBuilder, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsCheckDigitTransmissionSupported(self: Windows.Devices.PointOfService.Provider.IBarcodeSymbologyAttributesBuilder) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCheckDigitTransmissionSupported(self: Windows.Devices.PointOfService.Provider.IBarcodeSymbologyAttributesBuilder, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDecodeLengthSupported(self: Windows.Devices.PointOfService.Provider.IBarcodeSymbologyAttributesBuilder) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDecodeLengthSupported(self: Windows.Devices.PointOfService.Provider.IBarcodeSymbologyAttributesBuilder, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def CreateAttributes(self: Windows.Devices.PointOfService.Provider.IBarcodeSymbologyAttributesBuilder) -> Windows.Devices.PointOfService.BarcodeSymbologyAttributes: ...
    IsCheckDigitValidationSupported = property(get_IsCheckDigitValidationSupported, put_IsCheckDigitValidationSupported)
    IsCheckDigitTransmissionSupported = property(get_IsCheckDigitTransmissionSupported, put_IsCheckDigitTransmissionSupported)
    IsDecodeLengthSupported = property(get_IsDecodeLengthSupported, put_IsDecodeLengthSupported)
class IBarcodeScannerDisableScannerRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('88ecf7c0-37b9-4275-8e-77-c8-e5-2a-e5-a9-c8')
    @winrt_commethod(6)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerDisableScannerRequest2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ccdfe625-65c3-4ccc-b4-57-f3-9c-7a-9e-a6-0d')
    @winrt_commethod(6)
    def ReportFailedWithFailedReasonAsync(self, reason: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedWithFailedReasonAndDescriptionAsync(self, reason: Int32, failedReasonDescription: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerDisableScannerRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7006e142-e802-46f5-b6-04-35-2a-15-ce-92-32')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.Devices.PointOfService.Provider.BarcodeScannerDisableScannerRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IBarcodeScannerEnableScannerRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c0b3e9ba-816a-452b-bd-77-b7-e4-53-ec-44-6d')
    @winrt_commethod(6)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerEnableScannerRequest2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('71a4f2a8-9905-41ac-91-21-b6-45-91-6a-84-a1')
    @winrt_commethod(6)
    def ReportFailedWithFailedReasonAsync(self, reason: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedWithFailedReasonAndDescriptionAsync(self, reason: Int32, failedReasonDescription: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerEnableScannerRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('956c9419-7b4e-4451-8c-41-8e-10-cf-bc-5b-41')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.Devices.PointOfService.Provider.BarcodeScannerEnableScannerRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IBarcodeScannerFrameReader(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('dbc72b07-64c3-482b-93-c8-65-fb-33-c2-22-08')
    @winrt_commethod(6)
    def StartAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def StopAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def TryAcquireLatestFrameAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.Provider.BarcodeScannerVideoFrame]: ...
    @winrt_commethod(9)
    def get_Connection(self) -> Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection: ...
    @winrt_commethod(10)
    def add_FrameArrived(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReader, Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReaderFrameArrivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_FrameArrived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Connection = property(get_Connection, None)
class IBarcodeScannerFrameReaderFrameArrivedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b0bbd604-54fd-436d-86-29-71-2e-78-72-23-dd')
    @winrt_commethod(6)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
class IBarcodeScannerGetSymbologyAttributesRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9774c46a-58e4-4c5f-b8-e9-e4-14-67-63-27-00')
    @winrt_commethod(6)
    def get_Symbology(self) -> UInt32: ...
    @winrt_commethod(7)
    def ReportCompletedAsync(self, attributes: Windows.Devices.PointOfService.BarcodeSymbologyAttributes) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    Symbology = property(get_Symbology, None)
class IBarcodeScannerGetSymbologyAttributesRequest2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6a6a2b13-75a8-49fb-b8-52-bf-b9-3d-76-0a-f7')
    @winrt_commethod(6)
    def ReportFailedWithFailedReasonAsync(self, reason: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedWithFailedReasonAndDescriptionAsync(self, reason: Int32, failedReasonDescription: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerGetSymbologyAttributesRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7f89de3e-fb5d-493c-b4-02-35-6b-24-d5-74-a6')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.Devices.PointOfService.Provider.BarcodeScannerGetSymbologyAttributesRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IBarcodeScannerHideVideoPreviewRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fa4ebe7f-6670-40e1-b9-0b-bb-10-d8-d4-25-fa')
    @winrt_commethod(6)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerHideVideoPreviewRequest2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7e28435d-9814-431d-a2-f2-d6-24-8c-5a-d4-b5')
    @winrt_commethod(6)
    def ReportFailedWithFailedReasonAsync(self, reason: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedWithFailedReasonAndDescriptionAsync(self, reason: Int32, failedReasonDescription: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerHideVideoPreviewRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('16a281fc-d6be-4bc7-9d-f1-33-74-1f-3e-ad-ea')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.Devices.PointOfService.Provider.BarcodeScannerHideVideoPreviewRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IBarcodeScannerProviderConnection(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b44acbed-0b3a-4fa3-86-c5-49-1e-a3-07-80-eb')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_VideoDeviceId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SupportedSymbologies(self) -> Windows.Foundation.Collections.IVector[UInt32]: ...
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
    def ReportScannedDataAsync(self, report: Windows.Devices.PointOfService.BarcodeScannerReport) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def ReportTriggerStateAsync(self, state: Windows.Devices.PointOfService.Provider.BarcodeScannerTriggerState) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def ReportErrorAsync(self, errorData: Windows.Devices.PointOfService.UnifiedPosErrorData) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(19)
    def ReportErrorAsyncWithScanReport(self, errorData: Windows.Devices.PointOfService.UnifiedPosErrorData, isRetriable: Boolean, scanReport: Windows.Devices.PointOfService.BarcodeScannerReport) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(20)
    def add_EnableScannerRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, Windows.Devices.PointOfService.Provider.BarcodeScannerEnableScannerRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_EnableScannerRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def add_DisableScannerRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, Windows.Devices.PointOfService.Provider.BarcodeScannerDisableScannerRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_DisableScannerRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(24)
    def add_SetActiveSymbologiesRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, Windows.Devices.PointOfService.Provider.BarcodeScannerSetActiveSymbologiesRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(25)
    def remove_SetActiveSymbologiesRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(26)
    def add_StartSoftwareTriggerRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, Windows.Devices.PointOfService.Provider.BarcodeScannerStartSoftwareTriggerRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(27)
    def remove_StartSoftwareTriggerRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(28)
    def add_StopSoftwareTriggerRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, Windows.Devices.PointOfService.Provider.BarcodeScannerStopSoftwareTriggerRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(29)
    def remove_StopSoftwareTriggerRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(30)
    def add_GetBarcodeSymbologyAttributesRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, Windows.Devices.PointOfService.Provider.BarcodeScannerGetSymbologyAttributesRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(31)
    def remove_GetBarcodeSymbologyAttributesRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(32)
    def add_SetBarcodeSymbologyAttributesRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, Windows.Devices.PointOfService.Provider.BarcodeScannerSetSymbologyAttributesRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(33)
    def remove_SetBarcodeSymbologyAttributesRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(34)
    def add_HideVideoPreviewRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection, Windows.Devices.PointOfService.Provider.BarcodeScannerHideVideoPreviewRequestEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(35)
    def remove_HideVideoPreviewRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Id = property(get_Id, None)
    VideoDeviceId = property(get_VideoDeviceId, None)
    SupportedSymbologies = property(get_SupportedSymbologies, None)
    CompanyName = property(get_CompanyName, put_CompanyName)
    Name = property(get_Name, put_Name)
    Version = property(get_Version, put_Version)
class IBarcodeScannerProviderConnection2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('be9b53cd-1134-418c-a0-6b-04-42-3a-73-f3-d7')
    @winrt_commethod(6)
    def CreateFrameReaderAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReader]: ...
    @winrt_commethod(7)
    def CreateFrameReaderWithFormatAsync(self, preferredFormat: Windows.Graphics.Imaging.BitmapPixelFormat) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReader]: ...
    @winrt_commethod(8)
    def CreateFrameReaderWithFormatAndSizeAsync(self, preferredFormat: Windows.Graphics.Imaging.BitmapPixelFormat, preferredSize: Windows.Graphics.Imaging.BitmapSize) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.Provider.BarcodeScannerFrameReader]: ...
class IBarcodeScannerProviderTriggerDetails(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('50856d82-24e3-48ce-99-c7-70-aa-c1-cb-c9-f7')
    @winrt_commethod(6)
    def get_Connection(self) -> Windows.Devices.PointOfService.Provider.BarcodeScannerProviderConnection: ...
    Connection = property(get_Connection, None)
class IBarcodeScannerSetActiveSymbologiesRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('db3f32b9-f7da-41a1-9f-79-07-bc-d9-5f-0b-df')
    @winrt_commethod(6)
    def get_Symbologies(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(7)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    Symbologies = property(get_Symbologies, None)
class IBarcodeScannerSetActiveSymbologiesRequest2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f5ff6edf-fa9a-4749-b1-1b-e8-fc-cb-75-bc-6b')
    @winrt_commethod(6)
    def ReportFailedWithFailedReasonAsync(self, reason: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedWithFailedReasonAndDescriptionAsync(self, reason: Int32, failedReasonDescription: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerSetActiveSymbologiesRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('06305afa-7bf6-4d52-80-1a-33-02-72-f6-0a-e1')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.Devices.PointOfService.Provider.BarcodeScannerSetActiveSymbologiesRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IBarcodeScannerSetSymbologyAttributesRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('32fb814f-a37f-48b0-ac-ea-dc-e1-48-0f-12-ae')
    @winrt_commethod(6)
    def get_Symbology(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Attributes(self) -> Windows.Devices.PointOfService.BarcodeSymbologyAttributes: ...
    @winrt_commethod(8)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    Symbology = property(get_Symbology, None)
    Attributes = property(get_Attributes, None)
class IBarcodeScannerSetSymbologyAttributesRequest2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('dffbbfc1-dba8-4b77-be-1e-b5-6c-d7-2f-65-b3')
    @winrt_commethod(6)
    def ReportFailedWithFailedReasonAsync(self, reason: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedWithFailedReasonAndDescriptionAsync(self, reason: Int32, failedReasonDescription: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerSetSymbologyAttributesRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b2b89809-9824-47d4-85-bd-d0-07-7b-aa-7b-d2')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.Devices.PointOfService.Provider.BarcodeScannerSetSymbologyAttributesRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IBarcodeScannerStartSoftwareTriggerRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e3fa7b27-ff62-4454-af-4a-cb-61-44-a3-e3-f7')
    @winrt_commethod(6)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerStartSoftwareTriggerRequest2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('eb72a25c-6658-4765-a6-8e-32-74-82-65-3d-eb')
    @winrt_commethod(6)
    def ReportFailedWithFailedReasonAsync(self, reason: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedWithFailedReasonAndDescriptionAsync(self, reason: Int32, failedReasonDescription: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerStartSoftwareTriggerRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2305d843-c88f-4f3b-8c-3b-d3-df-07-10-51-ec')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.Devices.PointOfService.Provider.BarcodeScannerStartSoftwareTriggerRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IBarcodeScannerStopSoftwareTriggerRequest(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6f9faf35-e287-4ca8-b7-0d-5a-91-d6-94-f6-68')
    @winrt_commethod(6)
    def ReportCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedAsync(self) -> Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerStopSoftwareTriggerRequest2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cb57c5dd-fe50-49f8-a0-b4-bd-c2-30-81-4d-a2')
    @winrt_commethod(6)
    def ReportFailedWithFailedReasonAsync(self, reason: Int32) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ReportFailedWithFailedReasonAndDescriptionAsync(self, reason: Int32, failedReasonDescription: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
class IBarcodeScannerStopSoftwareTriggerRequestEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('eac34450-4eb7-481a-92-73-14-7a-27-3b-99-b8')
    @winrt_commethod(6)
    def get_Request(self) -> Windows.Devices.PointOfService.Provider.BarcodeScannerStopSoftwareTriggerRequest: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
class IBarcodeScannerVideoFrame(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7e585248-9df7-4121-a1-75-80-1d-80-00-11-2e')
    @winrt_commethod(6)
    def get_Format(self) -> Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_commethod(7)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Height(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_PixelData(self) -> Windows.Storage.Streams.IBuffer: ...
    Format = property(get_Format, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    PixelData = property(get_PixelData, None)
class IBarcodeSymbologyAttributesBuilder(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c57b0cbf-e4f5-40b9-84-cf-e6-3f-ba-ea-42-b4')
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
    def CreateAttributes(self) -> Windows.Devices.PointOfService.BarcodeSymbologyAttributes: ...
    IsCheckDigitValidationSupported = property(get_IsCheckDigitValidationSupported, put_IsCheckDigitValidationSupported)
    IsCheckDigitTransmissionSupported = property(get_IsCheckDigitTransmissionSupported, put_IsCheckDigitTransmissionSupported)
    IsDecodeLengthSupported = property(get_IsDecodeLengthSupported, put_IsDecodeLengthSupported)
make_head(_module, 'BarcodeScannerDisableScannerRequest')
make_head(_module, 'BarcodeScannerDisableScannerRequestEventArgs')
make_head(_module, 'BarcodeScannerEnableScannerRequest')
make_head(_module, 'BarcodeScannerEnableScannerRequestEventArgs')
make_head(_module, 'BarcodeScannerFrameReader')
make_head(_module, 'BarcodeScannerFrameReaderFrameArrivedEventArgs')
make_head(_module, 'BarcodeScannerGetSymbologyAttributesRequest')
make_head(_module, 'BarcodeScannerGetSymbologyAttributesRequestEventArgs')
make_head(_module, 'BarcodeScannerHideVideoPreviewRequest')
make_head(_module, 'BarcodeScannerHideVideoPreviewRequestEventArgs')
make_head(_module, 'BarcodeScannerProviderConnection')
make_head(_module, 'BarcodeScannerProviderTriggerDetails')
make_head(_module, 'BarcodeScannerSetActiveSymbologiesRequest')
make_head(_module, 'BarcodeScannerSetActiveSymbologiesRequestEventArgs')
make_head(_module, 'BarcodeScannerSetSymbologyAttributesRequest')
make_head(_module, 'BarcodeScannerSetSymbologyAttributesRequestEventArgs')
make_head(_module, 'BarcodeScannerStartSoftwareTriggerRequest')
make_head(_module, 'BarcodeScannerStartSoftwareTriggerRequestEventArgs')
make_head(_module, 'BarcodeScannerStopSoftwareTriggerRequest')
make_head(_module, 'BarcodeScannerStopSoftwareTriggerRequestEventArgs')
make_head(_module, 'BarcodeScannerVideoFrame')
make_head(_module, 'BarcodeSymbologyAttributesBuilder')
make_head(_module, 'IBarcodeScannerDisableScannerRequest')
make_head(_module, 'IBarcodeScannerDisableScannerRequest2')
make_head(_module, 'IBarcodeScannerDisableScannerRequestEventArgs')
make_head(_module, 'IBarcodeScannerEnableScannerRequest')
make_head(_module, 'IBarcodeScannerEnableScannerRequest2')
make_head(_module, 'IBarcodeScannerEnableScannerRequestEventArgs')
make_head(_module, 'IBarcodeScannerFrameReader')
make_head(_module, 'IBarcodeScannerFrameReaderFrameArrivedEventArgs')
make_head(_module, 'IBarcodeScannerGetSymbologyAttributesRequest')
make_head(_module, 'IBarcodeScannerGetSymbologyAttributesRequest2')
make_head(_module, 'IBarcodeScannerGetSymbologyAttributesRequestEventArgs')
make_head(_module, 'IBarcodeScannerHideVideoPreviewRequest')
make_head(_module, 'IBarcodeScannerHideVideoPreviewRequest2')
make_head(_module, 'IBarcodeScannerHideVideoPreviewRequestEventArgs')
make_head(_module, 'IBarcodeScannerProviderConnection')
make_head(_module, 'IBarcodeScannerProviderConnection2')
make_head(_module, 'IBarcodeScannerProviderTriggerDetails')
make_head(_module, 'IBarcodeScannerSetActiveSymbologiesRequest')
make_head(_module, 'IBarcodeScannerSetActiveSymbologiesRequest2')
make_head(_module, 'IBarcodeScannerSetActiveSymbologiesRequestEventArgs')
make_head(_module, 'IBarcodeScannerSetSymbologyAttributesRequest')
make_head(_module, 'IBarcodeScannerSetSymbologyAttributesRequest2')
make_head(_module, 'IBarcodeScannerSetSymbologyAttributesRequestEventArgs')
make_head(_module, 'IBarcodeScannerStartSoftwareTriggerRequest')
make_head(_module, 'IBarcodeScannerStartSoftwareTriggerRequest2')
make_head(_module, 'IBarcodeScannerStartSoftwareTriggerRequestEventArgs')
make_head(_module, 'IBarcodeScannerStopSoftwareTriggerRequest')
make_head(_module, 'IBarcodeScannerStopSoftwareTriggerRequest2')
make_head(_module, 'IBarcodeScannerStopSoftwareTriggerRequestEventArgs')
make_head(_module, 'IBarcodeScannerVideoFrame')
make_head(_module, 'IBarcodeSymbologyAttributesBuilder')
