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
import Windows.Devices.PointOfService
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics.Imaging
import Windows.Storage
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
class BarcodeScanner(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IBarcodeScanner
    _classid_ = 'Windows.Devices.PointOfService.BarcodeScanner'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.PointOfService.IBarcodeScanner) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Capabilities(self: Windows.Devices.PointOfService.IBarcodeScanner) -> Windows.Devices.PointOfService.BarcodeScannerCapabilities: ...
    @winrt_mixinmethod
    def ClaimScannerAsync(self: Windows.Devices.PointOfService.IBarcodeScanner) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.ClaimedBarcodeScanner]: ...
    @winrt_mixinmethod
    def CheckHealthAsync(self: Windows.Devices.PointOfService.IBarcodeScanner, level: Windows.Devices.PointOfService.UnifiedPosHealthCheckLevel) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetSupportedSymbologiesAsync(self: Windows.Devices.PointOfService.IBarcodeScanner) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[UInt32]]: ...
    @winrt_mixinmethod
    def IsSymbologySupportedAsync(self: Windows.Devices.PointOfService.IBarcodeScanner, barcodeSymbology: UInt32) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RetrieveStatisticsAsync(self: Windows.Devices.PointOfService.IBarcodeScanner, statisticsCategories: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def GetSupportedProfiles(self: Windows.Devices.PointOfService.IBarcodeScanner) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def IsProfileSupported(self: Windows.Devices.PointOfService.IBarcodeScanner, profile: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def add_StatusUpdated(self: Windows.Devices.PointOfService.IBarcodeScanner, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.BarcodeScanner, Windows.Devices.PointOfService.BarcodeScannerStatusUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusUpdated(self: Windows.Devices.PointOfService.IBarcodeScanner, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_VideoDeviceId(self: Windows.Devices.PointOfService.IBarcodeScanner2) -> WinRT_String: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelectorWithConnectionTypes(cls: Windows.Devices.PointOfService.IBarcodeScannerStatics2, connectionTypes: Windows.Devices.PointOfService.PosConnectionTypes) -> WinRT_String: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.PointOfService.IBarcodeScannerStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.BarcodeScanner]: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.PointOfService.IBarcodeScannerStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.BarcodeScanner]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.PointOfService.IBarcodeScannerStatics) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    Capabilities = property(get_Capabilities, None)
    VideoDeviceId = property(get_VideoDeviceId, None)
class BarcodeScannerCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IBarcodeScannerCapabilities
    _classid_ = 'Windows.Devices.PointOfService.BarcodeScannerCapabilities'
    @winrt_mixinmethod
    def get_PowerReportingType(self: Windows.Devices.PointOfService.IBarcodeScannerCapabilities) -> Windows.Devices.PointOfService.UnifiedPosPowerReportingType: ...
    @winrt_mixinmethod
    def get_IsStatisticsReportingSupported(self: Windows.Devices.PointOfService.IBarcodeScannerCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsStatisticsUpdatingSupported(self: Windows.Devices.PointOfService.IBarcodeScannerCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsImagePreviewSupported(self: Windows.Devices.PointOfService.IBarcodeScannerCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSoftwareTriggerSupported(self: Windows.Devices.PointOfService.IBarcodeScannerCapabilities1) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsVideoPreviewSupported(self: Windows.Devices.PointOfService.IBarcodeScannerCapabilities2) -> Boolean: ...
    PowerReportingType = property(get_PowerReportingType, None)
    IsStatisticsReportingSupported = property(get_IsStatisticsReportingSupported, None)
    IsStatisticsUpdatingSupported = property(get_IsStatisticsUpdatingSupported, None)
    IsImagePreviewSupported = property(get_IsImagePreviewSupported, None)
    IsSoftwareTriggerSupported = property(get_IsSoftwareTriggerSupported, None)
    IsVideoPreviewSupported = property(get_IsVideoPreviewSupported, None)
class BarcodeScannerDataReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IBarcodeScannerDataReceivedEventArgs
    _classid_ = 'Windows.Devices.PointOfService.BarcodeScannerDataReceivedEventArgs'
    @winrt_mixinmethod
    def get_Report(self: Windows.Devices.PointOfService.IBarcodeScannerDataReceivedEventArgs) -> Windows.Devices.PointOfService.BarcodeScannerReport: ...
    Report = property(get_Report, None)
class BarcodeScannerErrorOccurredEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IBarcodeScannerErrorOccurredEventArgs
    _classid_ = 'Windows.Devices.PointOfService.BarcodeScannerErrorOccurredEventArgs'
    @winrt_mixinmethod
    def get_PartialInputData(self: Windows.Devices.PointOfService.IBarcodeScannerErrorOccurredEventArgs) -> Windows.Devices.PointOfService.BarcodeScannerReport: ...
    @winrt_mixinmethod
    def get_IsRetriable(self: Windows.Devices.PointOfService.IBarcodeScannerErrorOccurredEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_ErrorData(self: Windows.Devices.PointOfService.IBarcodeScannerErrorOccurredEventArgs) -> Windows.Devices.PointOfService.UnifiedPosErrorData: ...
    PartialInputData = property(get_PartialInputData, None)
    IsRetriable = property(get_IsRetriable, None)
    ErrorData = property(get_ErrorData, None)
class BarcodeScannerImagePreviewReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IBarcodeScannerImagePreviewReceivedEventArgs
    _classid_ = 'Windows.Devices.PointOfService.BarcodeScannerImagePreviewReceivedEventArgs'
    @winrt_mixinmethod
    def get_Preview(self: Windows.Devices.PointOfService.IBarcodeScannerImagePreviewReceivedEventArgs) -> Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    Preview = property(get_Preview, None)
class BarcodeScannerReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IBarcodeScannerReport
    _classid_ = 'Windows.Devices.PointOfService.BarcodeScannerReport'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Devices.PointOfService.IBarcodeScannerReportFactory, scanDataType: UInt32, scanData: Windows.Storage.Streams.IBuffer, scanDataLabel: Windows.Storage.Streams.IBuffer) -> Windows.Devices.PointOfService.BarcodeScannerReport: ...
    @winrt_mixinmethod
    def get_ScanDataType(self: Windows.Devices.PointOfService.IBarcodeScannerReport) -> UInt32: ...
    @winrt_mixinmethod
    def get_ScanData(self: Windows.Devices.PointOfService.IBarcodeScannerReport) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_ScanDataLabel(self: Windows.Devices.PointOfService.IBarcodeScannerReport) -> Windows.Storage.Streams.IBuffer: ...
    ScanDataType = property(get_ScanDataType, None)
    ScanData = property(get_ScanData, None)
    ScanDataLabel = property(get_ScanDataLabel, None)
BarcodeScannerStatus = Int32
BarcodeScannerStatus_Online: BarcodeScannerStatus = 0
BarcodeScannerStatus_Off: BarcodeScannerStatus = 1
BarcodeScannerStatus_Offline: BarcodeScannerStatus = 2
BarcodeScannerStatus_OffOrOffline: BarcodeScannerStatus = 3
BarcodeScannerStatus_Extended: BarcodeScannerStatus = 4
class BarcodeScannerStatusUpdatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IBarcodeScannerStatusUpdatedEventArgs
    _classid_ = 'Windows.Devices.PointOfService.BarcodeScannerStatusUpdatedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.PointOfService.IBarcodeScannerStatusUpdatedEventArgs) -> Windows.Devices.PointOfService.BarcodeScannerStatus: ...
    @winrt_mixinmethod
    def get_ExtendedStatus(self: Windows.Devices.PointOfService.IBarcodeScannerStatusUpdatedEventArgs) -> UInt32: ...
    Status = property(get_Status, None)
    ExtendedStatus = property(get_ExtendedStatus, None)
class BarcodeSymbologies(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.BarcodeSymbologies'
    @winrt_classmethod
    def get_Gs1DWCode(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics2) -> UInt32: ...
    @winrt_classmethod
    def get_Unknown(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Ean8(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Ean8Add2(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Ean8Add5(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Eanv(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_EanvAdd2(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_EanvAdd5(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Ean13(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Ean13Add2(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Ean13Add5(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Isbn(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_IsbnAdd5(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Ismn(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_IsmnAdd2(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_IsmnAdd5(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Issn(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_IssnAdd2(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_IssnAdd5(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Ean99(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Ean99Add2(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Ean99Add5(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Upca(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_UpcaAdd2(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_UpcaAdd5(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Upce(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_UpceAdd2(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_UpceAdd5(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_UpcCoupon(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_TfStd(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_TfDis(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_TfInt(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_TfInd(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_TfMat(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_TfIata(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Gs1DatabarType1(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Gs1DatabarType2(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Gs1DatabarType3(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Code39(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Code39Ex(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Trioptic39(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Code32(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Pzn(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Code93(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Code93Ex(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Code128(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Gs1128(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Gs1128Coupon(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_UccEan128(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Sisac(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Isbt(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Codabar(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Code11(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Msi(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Plessey(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Telepen(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Code16k(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_CodablockA(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_CodablockF(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Codablock128(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Code49(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Aztec(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_DataCode(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_DataMatrix(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_HanXin(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Maxicode(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_MicroPdf417(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_MicroQr(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Pdf417(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Qr(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_MsTag(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Ccab(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Ccc(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Tlc39(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_AusPost(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_CanPost(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_ChinaPost(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_DutchKix(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_InfoMail(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_ItalianPost25(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_ItalianPost39(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_JapanPost(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_KoreanPost(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_SwedenPost(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_UkPost(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_UsIntelligent(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_UsIntelligentPkg(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_UsPlanet(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_UsPostNet(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Us4StateFics(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_OcrA(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_OcrB(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Micr(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_ExtendedBase(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics) -> UInt32: ...
    @winrt_classmethod
    def GetName(cls: Windows.Devices.PointOfService.IBarcodeSymbologiesStatics, scanDataType: UInt32) -> WinRT_String: ...
    Gs1DWCode = property(get_Gs1DWCode, None)
    Unknown = property(get_Unknown, None)
    Ean8 = property(get_Ean8, None)
    Ean8Add2 = property(get_Ean8Add2, None)
    Ean8Add5 = property(get_Ean8Add5, None)
    Eanv = property(get_Eanv, None)
    EanvAdd2 = property(get_EanvAdd2, None)
    EanvAdd5 = property(get_EanvAdd5, None)
    Ean13 = property(get_Ean13, None)
    Ean13Add2 = property(get_Ean13Add2, None)
    Ean13Add5 = property(get_Ean13Add5, None)
    Isbn = property(get_Isbn, None)
    IsbnAdd5 = property(get_IsbnAdd5, None)
    Ismn = property(get_Ismn, None)
    IsmnAdd2 = property(get_IsmnAdd2, None)
    IsmnAdd5 = property(get_IsmnAdd5, None)
    Issn = property(get_Issn, None)
    IssnAdd2 = property(get_IssnAdd2, None)
    IssnAdd5 = property(get_IssnAdd5, None)
    Ean99 = property(get_Ean99, None)
    Ean99Add2 = property(get_Ean99Add2, None)
    Ean99Add5 = property(get_Ean99Add5, None)
    Upca = property(get_Upca, None)
    UpcaAdd2 = property(get_UpcaAdd2, None)
    UpcaAdd5 = property(get_UpcaAdd5, None)
    Upce = property(get_Upce, None)
    UpceAdd2 = property(get_UpceAdd2, None)
    UpceAdd5 = property(get_UpceAdd5, None)
    UpcCoupon = property(get_UpcCoupon, None)
    TfStd = property(get_TfStd, None)
    TfDis = property(get_TfDis, None)
    TfInt = property(get_TfInt, None)
    TfInd = property(get_TfInd, None)
    TfMat = property(get_TfMat, None)
    TfIata = property(get_TfIata, None)
    Gs1DatabarType1 = property(get_Gs1DatabarType1, None)
    Gs1DatabarType2 = property(get_Gs1DatabarType2, None)
    Gs1DatabarType3 = property(get_Gs1DatabarType3, None)
    Code39 = property(get_Code39, None)
    Code39Ex = property(get_Code39Ex, None)
    Trioptic39 = property(get_Trioptic39, None)
    Code32 = property(get_Code32, None)
    Pzn = property(get_Pzn, None)
    Code93 = property(get_Code93, None)
    Code93Ex = property(get_Code93Ex, None)
    Code128 = property(get_Code128, None)
    Gs1128 = property(get_Gs1128, None)
    Gs1128Coupon = property(get_Gs1128Coupon, None)
    UccEan128 = property(get_UccEan128, None)
    Sisac = property(get_Sisac, None)
    Isbt = property(get_Isbt, None)
    Codabar = property(get_Codabar, None)
    Code11 = property(get_Code11, None)
    Msi = property(get_Msi, None)
    Plessey = property(get_Plessey, None)
    Telepen = property(get_Telepen, None)
    Code16k = property(get_Code16k, None)
    CodablockA = property(get_CodablockA, None)
    CodablockF = property(get_CodablockF, None)
    Codablock128 = property(get_Codablock128, None)
    Code49 = property(get_Code49, None)
    Aztec = property(get_Aztec, None)
    DataCode = property(get_DataCode, None)
    DataMatrix = property(get_DataMatrix, None)
    HanXin = property(get_HanXin, None)
    Maxicode = property(get_Maxicode, None)
    MicroPdf417 = property(get_MicroPdf417, None)
    MicroQr = property(get_MicroQr, None)
    Pdf417 = property(get_Pdf417, None)
    Qr = property(get_Qr, None)
    MsTag = property(get_MsTag, None)
    Ccab = property(get_Ccab, None)
    Ccc = property(get_Ccc, None)
    Tlc39 = property(get_Tlc39, None)
    AusPost = property(get_AusPost, None)
    CanPost = property(get_CanPost, None)
    ChinaPost = property(get_ChinaPost, None)
    DutchKix = property(get_DutchKix, None)
    InfoMail = property(get_InfoMail, None)
    ItalianPost25 = property(get_ItalianPost25, None)
    ItalianPost39 = property(get_ItalianPost39, None)
    JapanPost = property(get_JapanPost, None)
    KoreanPost = property(get_KoreanPost, None)
    SwedenPost = property(get_SwedenPost, None)
    UkPost = property(get_UkPost, None)
    UsIntelligent = property(get_UsIntelligent, None)
    UsIntelligentPkg = property(get_UsIntelligentPkg, None)
    UsPlanet = property(get_UsPlanet, None)
    UsPostNet = property(get_UsPostNet, None)
    Us4StateFics = property(get_Us4StateFics, None)
    OcrA = property(get_OcrA, None)
    OcrB = property(get_OcrB, None)
    Micr = property(get_Micr, None)
    ExtendedBase = property(get_ExtendedBase, None)
class BarcodeSymbologyAttributes(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IBarcodeSymbologyAttributes
    _classid_ = 'Windows.Devices.PointOfService.BarcodeSymbologyAttributes'
    @winrt_mixinmethod
    def get_IsCheckDigitValidationEnabled(self: Windows.Devices.PointOfService.IBarcodeSymbologyAttributes) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCheckDigitValidationEnabled(self: Windows.Devices.PointOfService.IBarcodeSymbologyAttributes, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsCheckDigitValidationSupported(self: Windows.Devices.PointOfService.IBarcodeSymbologyAttributes) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCheckDigitTransmissionEnabled(self: Windows.Devices.PointOfService.IBarcodeSymbologyAttributes) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCheckDigitTransmissionEnabled(self: Windows.Devices.PointOfService.IBarcodeSymbologyAttributes, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsCheckDigitTransmissionSupported(self: Windows.Devices.PointOfService.IBarcodeSymbologyAttributes) -> Boolean: ...
    @winrt_mixinmethod
    def get_DecodeLength1(self: Windows.Devices.PointOfService.IBarcodeSymbologyAttributes) -> UInt32: ...
    @winrt_mixinmethod
    def put_DecodeLength1(self: Windows.Devices.PointOfService.IBarcodeSymbologyAttributes, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_DecodeLength2(self: Windows.Devices.PointOfService.IBarcodeSymbologyAttributes) -> UInt32: ...
    @winrt_mixinmethod
    def put_DecodeLength2(self: Windows.Devices.PointOfService.IBarcodeSymbologyAttributes, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_DecodeLengthKind(self: Windows.Devices.PointOfService.IBarcodeSymbologyAttributes) -> Windows.Devices.PointOfService.BarcodeSymbologyDecodeLengthKind: ...
    @winrt_mixinmethod
    def put_DecodeLengthKind(self: Windows.Devices.PointOfService.IBarcodeSymbologyAttributes, value: Windows.Devices.PointOfService.BarcodeSymbologyDecodeLengthKind) -> Void: ...
    @winrt_mixinmethod
    def get_IsDecodeLengthSupported(self: Windows.Devices.PointOfService.IBarcodeSymbologyAttributes) -> Boolean: ...
    IsCheckDigitValidationEnabled = property(get_IsCheckDigitValidationEnabled, put_IsCheckDigitValidationEnabled)
    IsCheckDigitValidationSupported = property(get_IsCheckDigitValidationSupported, None)
    IsCheckDigitTransmissionEnabled = property(get_IsCheckDigitTransmissionEnabled, put_IsCheckDigitTransmissionEnabled)
    IsCheckDigitTransmissionSupported = property(get_IsCheckDigitTransmissionSupported, None)
    DecodeLength1 = property(get_DecodeLength1, put_DecodeLength1)
    DecodeLength2 = property(get_DecodeLength2, put_DecodeLength2)
    DecodeLengthKind = property(get_DecodeLengthKind, put_DecodeLengthKind)
    IsDecodeLengthSupported = property(get_IsDecodeLengthSupported, None)
BarcodeSymbologyDecodeLengthKind = Int32
BarcodeSymbologyDecodeLengthKind_AnyLength: BarcodeSymbologyDecodeLengthKind = 0
BarcodeSymbologyDecodeLengthKind_Discrete: BarcodeSymbologyDecodeLengthKind = 1
BarcodeSymbologyDecodeLengthKind_Range: BarcodeSymbologyDecodeLengthKind = 2
class CashDrawer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ICashDrawer
    _classid_ = 'Windows.Devices.PointOfService.CashDrawer'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.PointOfService.ICashDrawer) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Capabilities(self: Windows.Devices.PointOfService.ICashDrawer) -> Windows.Devices.PointOfService.CashDrawerCapabilities: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.PointOfService.ICashDrawer) -> Windows.Devices.PointOfService.CashDrawerStatus: ...
    @winrt_mixinmethod
    def get_IsDrawerOpen(self: Windows.Devices.PointOfService.ICashDrawer) -> Boolean: ...
    @winrt_mixinmethod
    def get_DrawerEventSource(self: Windows.Devices.PointOfService.ICashDrawer) -> Windows.Devices.PointOfService.CashDrawerEventSource: ...
    @winrt_mixinmethod
    def ClaimDrawerAsync(self: Windows.Devices.PointOfService.ICashDrawer) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.ClaimedCashDrawer]: ...
    @winrt_mixinmethod
    def CheckHealthAsync(self: Windows.Devices.PointOfService.ICashDrawer, level: Windows.Devices.PointOfService.UnifiedPosHealthCheckLevel) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetStatisticsAsync(self: Windows.Devices.PointOfService.ICashDrawer, statisticsCategories: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def add_StatusUpdated(self: Windows.Devices.PointOfService.ICashDrawer, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.CashDrawer, Windows.Devices.PointOfService.CashDrawerStatusUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusUpdated(self: Windows.Devices.PointOfService.ICashDrawer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelectorWithConnectionTypes(cls: Windows.Devices.PointOfService.ICashDrawerStatics2, connectionTypes: Windows.Devices.PointOfService.PosConnectionTypes) -> WinRT_String: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.PointOfService.ICashDrawerStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.CashDrawer]: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.PointOfService.ICashDrawerStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.CashDrawer]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.PointOfService.ICashDrawerStatics) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    Capabilities = property(get_Capabilities, None)
    Status = property(get_Status, None)
    IsDrawerOpen = property(get_IsDrawerOpen, None)
    DrawerEventSource = property(get_DrawerEventSource, None)
class CashDrawerCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ICashDrawerCapabilities
    _classid_ = 'Windows.Devices.PointOfService.CashDrawerCapabilities'
    @winrt_mixinmethod
    def get_PowerReportingType(self: Windows.Devices.PointOfService.ICashDrawerCapabilities) -> Windows.Devices.PointOfService.UnifiedPosPowerReportingType: ...
    @winrt_mixinmethod
    def get_IsStatisticsReportingSupported(self: Windows.Devices.PointOfService.ICashDrawerCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsStatisticsUpdatingSupported(self: Windows.Devices.PointOfService.ICashDrawerCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsStatusReportingSupported(self: Windows.Devices.PointOfService.ICashDrawerCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsStatusMultiDrawerDetectSupported(self: Windows.Devices.PointOfService.ICashDrawerCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDrawerOpenSensorAvailable(self: Windows.Devices.PointOfService.ICashDrawerCapabilities) -> Boolean: ...
    PowerReportingType = property(get_PowerReportingType, None)
    IsStatisticsReportingSupported = property(get_IsStatisticsReportingSupported, None)
    IsStatisticsUpdatingSupported = property(get_IsStatisticsUpdatingSupported, None)
    IsStatusReportingSupported = property(get_IsStatusReportingSupported, None)
    IsStatusMultiDrawerDetectSupported = property(get_IsStatusMultiDrawerDetectSupported, None)
    IsDrawerOpenSensorAvailable = property(get_IsDrawerOpenSensorAvailable, None)
class CashDrawerCloseAlarm(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ICashDrawerCloseAlarm
    _classid_ = 'Windows.Devices.PointOfService.CashDrawerCloseAlarm'
    @winrt_mixinmethod
    def put_AlarmTimeout(self: Windows.Devices.PointOfService.ICashDrawerCloseAlarm, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_AlarmTimeout(self: Windows.Devices.PointOfService.ICashDrawerCloseAlarm) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_BeepFrequency(self: Windows.Devices.PointOfService.ICashDrawerCloseAlarm, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_BeepFrequency(self: Windows.Devices.PointOfService.ICashDrawerCloseAlarm) -> UInt32: ...
    @winrt_mixinmethod
    def put_BeepDuration(self: Windows.Devices.PointOfService.ICashDrawerCloseAlarm, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_BeepDuration(self: Windows.Devices.PointOfService.ICashDrawerCloseAlarm) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_BeepDelay(self: Windows.Devices.PointOfService.ICashDrawerCloseAlarm, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_BeepDelay(self: Windows.Devices.PointOfService.ICashDrawerCloseAlarm) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def add_AlarmTimeoutExpired(self: Windows.Devices.PointOfService.ICashDrawerCloseAlarm, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.CashDrawerCloseAlarm, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AlarmTimeoutExpired(self: Windows.Devices.PointOfService.ICashDrawerCloseAlarm, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def StartAsync(self: Windows.Devices.PointOfService.ICashDrawerCloseAlarm) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    AlarmTimeout = property(get_AlarmTimeout, put_AlarmTimeout)
    BeepFrequency = property(get_BeepFrequency, put_BeepFrequency)
    BeepDuration = property(get_BeepDuration, put_BeepDuration)
    BeepDelay = property(get_BeepDelay, put_BeepDelay)
class CashDrawerClosedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ICashDrawerEventSourceEventArgs
    _classid_ = 'Windows.Devices.PointOfService.CashDrawerClosedEventArgs'
    @winrt_mixinmethod
    def get_CashDrawer(self: Windows.Devices.PointOfService.ICashDrawerEventSourceEventArgs) -> Windows.Devices.PointOfService.CashDrawer: ...
    CashDrawer = property(get_CashDrawer, None)
class CashDrawerEventSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ICashDrawerEventSource
    _classid_ = 'Windows.Devices.PointOfService.CashDrawerEventSource'
    @winrt_mixinmethod
    def add_DrawerClosed(self: Windows.Devices.PointOfService.ICashDrawerEventSource, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.CashDrawerEventSource, Windows.Devices.PointOfService.CashDrawerClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DrawerClosed(self: Windows.Devices.PointOfService.ICashDrawerEventSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DrawerOpened(self: Windows.Devices.PointOfService.ICashDrawerEventSource, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.CashDrawerEventSource, Windows.Devices.PointOfService.CashDrawerOpenedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DrawerOpened(self: Windows.Devices.PointOfService.ICashDrawerEventSource, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class CashDrawerOpenedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ICashDrawerEventSourceEventArgs
    _classid_ = 'Windows.Devices.PointOfService.CashDrawerOpenedEventArgs'
    @winrt_mixinmethod
    def get_CashDrawer(self: Windows.Devices.PointOfService.ICashDrawerEventSourceEventArgs) -> Windows.Devices.PointOfService.CashDrawer: ...
    CashDrawer = property(get_CashDrawer, None)
class CashDrawerStatus(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ICashDrawerStatus
    _classid_ = 'Windows.Devices.PointOfService.CashDrawerStatus'
    @winrt_mixinmethod
    def get_StatusKind(self: Windows.Devices.PointOfService.ICashDrawerStatus) -> Windows.Devices.PointOfService.CashDrawerStatusKind: ...
    @winrt_mixinmethod
    def get_ExtendedStatus(self: Windows.Devices.PointOfService.ICashDrawerStatus) -> UInt32: ...
    StatusKind = property(get_StatusKind, None)
    ExtendedStatus = property(get_ExtendedStatus, None)
CashDrawerStatusKind = Int32
CashDrawerStatusKind_Online: CashDrawerStatusKind = 0
CashDrawerStatusKind_Off: CashDrawerStatusKind = 1
CashDrawerStatusKind_Offline: CashDrawerStatusKind = 2
CashDrawerStatusKind_OffOrOffline: CashDrawerStatusKind = 3
CashDrawerStatusKind_Extended: CashDrawerStatusKind = 4
class CashDrawerStatusUpdatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ICashDrawerStatusUpdatedEventArgs
    _classid_ = 'Windows.Devices.PointOfService.CashDrawerStatusUpdatedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.PointOfService.ICashDrawerStatusUpdatedEventArgs) -> Windows.Devices.PointOfService.CashDrawerStatus: ...
    Status = property(get_Status, None)
class ClaimedBarcodeScanner(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IClaimedBarcodeScanner
    _classid_ = 'Windows.Devices.PointOfService.ClaimedBarcodeScanner'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDisabledOnDataReceived(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDisabledOnDataReceived(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDecodeDataEnabled(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDecodeDataEnabled(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner) -> Boolean: ...
    @winrt_mixinmethod
    def EnableAsync(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DisableAsync(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RetainDevice(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner) -> Void: ...
    @winrt_mixinmethod
    def SetActiveSymbologiesAsync(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner, symbologies: Windows.Foundation.Collections.IIterable[UInt32]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ResetStatisticsAsync(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner, statisticsCategories: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def UpdateStatisticsAsync(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner, statistics: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetActiveProfileAsync(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner, profile: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_DataReceived(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedBarcodeScanner, Windows.Devices.PointOfService.BarcodeScannerDataReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DataReceived(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TriggerPressed(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner, handler: Windows.Foundation.EventHandler[Windows.Devices.PointOfService.ClaimedBarcodeScanner]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TriggerPressed(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TriggerReleased(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner, handler: Windows.Foundation.EventHandler[Windows.Devices.PointOfService.ClaimedBarcodeScanner]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TriggerReleased(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ReleaseDeviceRequested(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner, handler: Windows.Foundation.EventHandler[Windows.Devices.PointOfService.ClaimedBarcodeScanner]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReleaseDeviceRequested(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ImagePreviewReceived(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedBarcodeScanner, Windows.Devices.PointOfService.BarcodeScannerImagePreviewReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ImagePreviewReceived(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ErrorOccurred(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedBarcodeScanner, Windows.Devices.PointOfService.BarcodeScannerErrorOccurredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ErrorOccurred(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def StartSoftwareTriggerAsync(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner1) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def StopSoftwareTriggerAsync(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner1) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetSymbologyAttributesAsync(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner2, barcodeSymbology: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.BarcodeSymbologyAttributes]: ...
    @winrt_mixinmethod
    def SetSymbologyAttributesAsync(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner2, barcodeSymbology: UInt32, attributes: Windows.Devices.PointOfService.BarcodeSymbologyAttributes) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def ShowVideoPreviewAsync(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner3) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def HideVideoPreview(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner3) -> Void: ...
    @winrt_mixinmethod
    def put_IsVideoPreviewShownOnEnable(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsVideoPreviewShownOnEnable(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner3) -> Boolean: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner4, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedBarcodeScanner, Windows.Devices.PointOfService.ClaimedBarcodeScannerClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.Devices.PointOfService.IClaimedBarcodeScanner4, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    IsEnabled = property(get_IsEnabled, None)
    IsDisabledOnDataReceived = property(get_IsDisabledOnDataReceived, put_IsDisabledOnDataReceived)
    IsDecodeDataEnabled = property(get_IsDecodeDataEnabled, put_IsDecodeDataEnabled)
    IsVideoPreviewShownOnEnable = property(get_IsVideoPreviewShownOnEnable, put_IsVideoPreviewShownOnEnable)
class ClaimedBarcodeScannerClosedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IClaimedBarcodeScannerClosedEventArgs
    _classid_ = 'Windows.Devices.PointOfService.ClaimedBarcodeScannerClosedEventArgs'
class ClaimedCashDrawer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IClaimedCashDrawer
    _classid_ = 'Windows.Devices.PointOfService.ClaimedCashDrawer'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.PointOfService.IClaimedCashDrawer) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Devices.PointOfService.IClaimedCashDrawer) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDrawerOpen(self: Windows.Devices.PointOfService.IClaimedCashDrawer) -> Boolean: ...
    @winrt_mixinmethod
    def get_CloseAlarm(self: Windows.Devices.PointOfService.IClaimedCashDrawer) -> Windows.Devices.PointOfService.CashDrawerCloseAlarm: ...
    @winrt_mixinmethod
    def OpenDrawerAsync(self: Windows.Devices.PointOfService.IClaimedCashDrawer) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def EnableAsync(self: Windows.Devices.PointOfService.IClaimedCashDrawer) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def DisableAsync(self: Windows.Devices.PointOfService.IClaimedCashDrawer) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RetainDeviceAsync(self: Windows.Devices.PointOfService.IClaimedCashDrawer) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def ResetStatisticsAsync(self: Windows.Devices.PointOfService.IClaimedCashDrawer, statisticsCategories: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def UpdateStatisticsAsync(self: Windows.Devices.PointOfService.IClaimedCashDrawer, statistics: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_ReleaseDeviceRequested(self: Windows.Devices.PointOfService.IClaimedCashDrawer, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedCashDrawer, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReleaseDeviceRequested(self: Windows.Devices.PointOfService.IClaimedCashDrawer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.Devices.PointOfService.IClaimedCashDrawer2, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedCashDrawer, Windows.Devices.PointOfService.ClaimedCashDrawerClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.Devices.PointOfService.IClaimedCashDrawer2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    IsEnabled = property(get_IsEnabled, None)
    IsDrawerOpen = property(get_IsDrawerOpen, None)
    CloseAlarm = property(get_CloseAlarm, None)
class ClaimedCashDrawerClosedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IClaimedCashDrawerClosedEventArgs
    _classid_ = 'Windows.Devices.PointOfService.ClaimedCashDrawerClosedEventArgs'
class ClaimedJournalPrinter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IClaimedJournalPrinter
    _classid_ = 'Windows.Devices.PointOfService.ClaimedJournalPrinter'
    @winrt_mixinmethod
    def CreateJob(self: Windows.Devices.PointOfService.IClaimedJournalPrinter) -> Windows.Devices.PointOfService.JournalPrintJob: ...
    @winrt_mixinmethod
    def put_CharactersPerLine(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CharactersPerLine(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> UInt32: ...
    @winrt_mixinmethod
    def put_LineHeight(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_LineHeight(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> UInt32: ...
    @winrt_mixinmethod
    def put_LineSpacing(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_LineSpacing(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> UInt32: ...
    @winrt_mixinmethod
    def get_LineWidth(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> UInt32: ...
    @winrt_mixinmethod
    def put_IsLetterQuality(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsLetterQuality(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPaperNearEnd(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def put_ColorCartridge(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation, value: Windows.Devices.PointOfService.PosPrinterColorCartridge) -> Void: ...
    @winrt_mixinmethod
    def get_ColorCartridge(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Windows.Devices.PointOfService.PosPrinterColorCartridge: ...
    @winrt_mixinmethod
    def get_IsCoverOpen(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCartridgeRemoved(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCartridgeEmpty(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsHeadCleaning(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPaperEmpty(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsReadyToPrint(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def ValidateData(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation, data: WinRT_String) -> Boolean: ...
    CharactersPerLine = property(get_CharactersPerLine, put_CharactersPerLine)
    LineHeight = property(get_LineHeight, put_LineHeight)
    LineSpacing = property(get_LineSpacing, put_LineSpacing)
    LineWidth = property(get_LineWidth, None)
    IsLetterQuality = property(get_IsLetterQuality, put_IsLetterQuality)
    IsPaperNearEnd = property(get_IsPaperNearEnd, None)
    ColorCartridge = property(get_ColorCartridge, put_ColorCartridge)
    IsCoverOpen = property(get_IsCoverOpen, None)
    IsCartridgeRemoved = property(get_IsCartridgeRemoved, None)
    IsCartridgeEmpty = property(get_IsCartridgeEmpty, None)
    IsHeadCleaning = property(get_IsHeadCleaning, None)
    IsPaperEmpty = property(get_IsPaperEmpty, None)
    IsReadyToPrint = property(get_IsReadyToPrint, None)
class ClaimedLineDisplay(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IClaimedLineDisplay
    _classid_ = 'Windows.Devices.PointOfService.ClaimedLineDisplay'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.PointOfService.IClaimedLineDisplay) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Capabilities(self: Windows.Devices.PointOfService.IClaimedLineDisplay) -> Windows.Devices.PointOfService.LineDisplayCapabilities: ...
    @winrt_mixinmethod
    def get_PhysicalDeviceName(self: Windows.Devices.PointOfService.IClaimedLineDisplay) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PhysicalDeviceDescription(self: Windows.Devices.PointOfService.IClaimedLineDisplay) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceControlDescription(self: Windows.Devices.PointOfService.IClaimedLineDisplay) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceControlVersion(self: Windows.Devices.PointOfService.IClaimedLineDisplay) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceServiceVersion(self: Windows.Devices.PointOfService.IClaimedLineDisplay) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DefaultWindow(self: Windows.Devices.PointOfService.IClaimedLineDisplay) -> Windows.Devices.PointOfService.LineDisplayWindow: ...
    @winrt_mixinmethod
    def RetainDevice(self: Windows.Devices.PointOfService.IClaimedLineDisplay) -> Void: ...
    @winrt_mixinmethod
    def add_ReleaseDeviceRequested(self: Windows.Devices.PointOfService.IClaimedLineDisplay, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedLineDisplay, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReleaseDeviceRequested(self: Windows.Devices.PointOfService.IClaimedLineDisplay, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetStatisticsAsync(self: Windows.Devices.PointOfService.IClaimedLineDisplay2, statisticsCategories: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def CheckHealthAsync(self: Windows.Devices.PointOfService.IClaimedLineDisplay2, level: Windows.Devices.PointOfService.UnifiedPosHealthCheckLevel) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def CheckPowerStatusAsync(self: Windows.Devices.PointOfService.IClaimedLineDisplay2) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.LineDisplayPowerStatus]: ...
    @winrt_mixinmethod
    def add_StatusUpdated(self: Windows.Devices.PointOfService.IClaimedLineDisplay2, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedLineDisplay, Windows.Devices.PointOfService.LineDisplayStatusUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusUpdated(self: Windows.Devices.PointOfService.IClaimedLineDisplay2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedScreenSizesInCharacters(self: Windows.Devices.PointOfService.IClaimedLineDisplay2) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Size]: ...
    @winrt_mixinmethod
    def get_MaxBitmapSizeInPixels(self: Windows.Devices.PointOfService.IClaimedLineDisplay2) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_SupportedCharacterSets(self: Windows.Devices.PointOfService.IClaimedLineDisplay2) -> Windows.Foundation.Collections.IVectorView[Int32]: ...
    @winrt_mixinmethod
    def get_CustomGlyphs(self: Windows.Devices.PointOfService.IClaimedLineDisplay2) -> Windows.Devices.PointOfService.LineDisplayCustomGlyphs: ...
    @winrt_mixinmethod
    def GetAttributes(self: Windows.Devices.PointOfService.IClaimedLineDisplay2) -> Windows.Devices.PointOfService.LineDisplayAttributes: ...
    @winrt_mixinmethod
    def TryUpdateAttributesAsync(self: Windows.Devices.PointOfService.IClaimedLineDisplay2, attributes: Windows.Devices.PointOfService.LineDisplayAttributes) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TrySetDescriptorAsync(self: Windows.Devices.PointOfService.IClaimedLineDisplay2, descriptor: UInt32, descriptorState: Windows.Devices.PointOfService.LineDisplayDescriptorState) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryClearDescriptorsAsync(self: Windows.Devices.PointOfService.IClaimedLineDisplay2) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryCreateWindowAsync(self: Windows.Devices.PointOfService.IClaimedLineDisplay2, viewport: Windows.Foundation.Rect, windowSize: Windows.Foundation.Size) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.LineDisplayWindow]: ...
    @winrt_mixinmethod
    def TryStoreStorageFileBitmapAsync(self: Windows.Devices.PointOfService.IClaimedLineDisplay2, bitmap: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.LineDisplayStoredBitmap]: ...
    @winrt_mixinmethod
    def TryStoreStorageFileBitmapWithAlignmentAsync(self: Windows.Devices.PointOfService.IClaimedLineDisplay2, bitmap: Windows.Storage.StorageFile, horizontalAlignment: Windows.Devices.PointOfService.LineDisplayHorizontalAlignment, verticalAlignment: Windows.Devices.PointOfService.LineDisplayVerticalAlignment) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.LineDisplayStoredBitmap]: ...
    @winrt_mixinmethod
    def TryStoreStorageFileBitmapWithAlignmentAndWidthAsync(self: Windows.Devices.PointOfService.IClaimedLineDisplay2, bitmap: Windows.Storage.StorageFile, horizontalAlignment: Windows.Devices.PointOfService.LineDisplayHorizontalAlignment, verticalAlignment: Windows.Devices.PointOfService.LineDisplayVerticalAlignment, widthInPixels: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.LineDisplayStoredBitmap]: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.Devices.PointOfService.IClaimedLineDisplay3, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedLineDisplay, Windows.Devices.PointOfService.ClaimedLineDisplayClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.Devices.PointOfService.IClaimedLineDisplay3, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.PointOfService.IClaimedLineDisplayStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.ClaimedLineDisplay]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.PointOfService.IClaimedLineDisplayStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorWithConnectionTypes(cls: Windows.Devices.PointOfService.IClaimedLineDisplayStatics, connectionTypes: Windows.Devices.PointOfService.PosConnectionTypes) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    Capabilities = property(get_Capabilities, None)
    PhysicalDeviceName = property(get_PhysicalDeviceName, None)
    PhysicalDeviceDescription = property(get_PhysicalDeviceDescription, None)
    DeviceControlDescription = property(get_DeviceControlDescription, None)
    DeviceControlVersion = property(get_DeviceControlVersion, None)
    DeviceServiceVersion = property(get_DeviceServiceVersion, None)
    DefaultWindow = property(get_DefaultWindow, None)
    SupportedScreenSizesInCharacters = property(get_SupportedScreenSizesInCharacters, None)
    MaxBitmapSizeInPixels = property(get_MaxBitmapSizeInPixels, None)
    SupportedCharacterSets = property(get_SupportedCharacterSets, None)
    CustomGlyphs = property(get_CustomGlyphs, None)
class ClaimedLineDisplayClosedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IClaimedLineDisplayClosedEventArgs
    _classid_ = 'Windows.Devices.PointOfService.ClaimedLineDisplayClosedEventArgs'
class ClaimedMagneticStripeReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IClaimedMagneticStripeReader
    _classid_ = 'Windows.Devices.PointOfService.ClaimedMagneticStripeReader'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDisabledOnDataReceived(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDisabledOnDataReceived(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsDecodeDataEnabled(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDecodeDataEnabled(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDeviceAuthenticated(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader) -> Boolean: ...
    @winrt_mixinmethod
    def put_DataEncryptionAlgorithm(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_DataEncryptionAlgorithm(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader) -> UInt32: ...
    @winrt_mixinmethod
    def put_TracksToRead(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, value: Windows.Devices.PointOfService.MagneticStripeReaderTrackIds) -> Void: ...
    @winrt_mixinmethod
    def get_TracksToRead(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader) -> Windows.Devices.PointOfService.MagneticStripeReaderTrackIds: ...
    @winrt_mixinmethod
    def put_IsTransmitSentinelsEnabled(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsTransmitSentinelsEnabled(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader) -> Boolean: ...
    @winrt_mixinmethod
    def EnableAsync(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DisableAsync(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RetainDevice(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader) -> Void: ...
    @winrt_mixinmethod
    def SetErrorReportingType(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, value: Windows.Devices.PointOfService.MagneticStripeReaderErrorReportingType) -> Void: ...
    @winrt_mixinmethod
    def RetrieveDeviceAuthenticationDataAsync(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def AuthenticateDeviceAsync(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, responseToken: c_char_p_no) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DeAuthenticateDeviceAsync(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, responseToken: c_char_p_no) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def UpdateKeyAsync(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, key: WinRT_String, keyName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ResetStatisticsAsync(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, statisticsCategories: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def UpdateStatisticsAsync(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, statistics: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_BankCardDataReceived(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedMagneticStripeReader, Windows.Devices.PointOfService.MagneticStripeReaderBankCardDataReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BankCardDataReceived(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AamvaCardDataReceived(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedMagneticStripeReader, Windows.Devices.PointOfService.MagneticStripeReaderAamvaCardDataReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AamvaCardDataReceived(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VendorSpecificDataReceived(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedMagneticStripeReader, Windows.Devices.PointOfService.MagneticStripeReaderVendorSpecificCardDataReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VendorSpecificDataReceived(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ReleaseDeviceRequested(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, handler: Windows.Foundation.EventHandler[Windows.Devices.PointOfService.ClaimedMagneticStripeReader]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReleaseDeviceRequested(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ErrorOccurred(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedMagneticStripeReader, Windows.Devices.PointOfService.MagneticStripeReaderErrorOccurredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ErrorOccurred(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader2, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedMagneticStripeReader, Windows.Devices.PointOfService.ClaimedMagneticStripeReaderClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.Devices.PointOfService.IClaimedMagneticStripeReader2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    IsEnabled = property(get_IsEnabled, None)
    IsDisabledOnDataReceived = property(get_IsDisabledOnDataReceived, put_IsDisabledOnDataReceived)
    IsDecodeDataEnabled = property(get_IsDecodeDataEnabled, put_IsDecodeDataEnabled)
    IsDeviceAuthenticated = property(get_IsDeviceAuthenticated, None)
    DataEncryptionAlgorithm = property(get_DataEncryptionAlgorithm, put_DataEncryptionAlgorithm)
    TracksToRead = property(get_TracksToRead, put_TracksToRead)
    IsTransmitSentinelsEnabled = property(get_IsTransmitSentinelsEnabled, put_IsTransmitSentinelsEnabled)
class ClaimedMagneticStripeReaderClosedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IClaimedMagneticStripeReaderClosedEventArgs
    _classid_ = 'Windows.Devices.PointOfService.ClaimedMagneticStripeReaderClosedEventArgs'
class ClaimedPosPrinter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IClaimedPosPrinter
    _classid_ = 'Windows.Devices.PointOfService.ClaimedPosPrinter'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.PointOfService.IClaimedPosPrinter) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: Windows.Devices.PointOfService.IClaimedPosPrinter) -> Boolean: ...
    @winrt_mixinmethod
    def put_CharacterSet(self: Windows.Devices.PointOfService.IClaimedPosPrinter, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CharacterSet(self: Windows.Devices.PointOfService.IClaimedPosPrinter) -> UInt32: ...
    @winrt_mixinmethod
    def get_IsCoverOpen(self: Windows.Devices.PointOfService.IClaimedPosPrinter) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCharacterSetMappingEnabled(self: Windows.Devices.PointOfService.IClaimedPosPrinter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsCharacterSetMappingEnabled(self: Windows.Devices.PointOfService.IClaimedPosPrinter) -> Boolean: ...
    @winrt_mixinmethod
    def put_MapMode(self: Windows.Devices.PointOfService.IClaimedPosPrinter, value: Windows.Devices.PointOfService.PosPrinterMapMode) -> Void: ...
    @winrt_mixinmethod
    def get_MapMode(self: Windows.Devices.PointOfService.IClaimedPosPrinter) -> Windows.Devices.PointOfService.PosPrinterMapMode: ...
    @winrt_mixinmethod
    def get_Receipt(self: Windows.Devices.PointOfService.IClaimedPosPrinter) -> Windows.Devices.PointOfService.ClaimedReceiptPrinter: ...
    @winrt_mixinmethod
    def get_Slip(self: Windows.Devices.PointOfService.IClaimedPosPrinter) -> Windows.Devices.PointOfService.ClaimedSlipPrinter: ...
    @winrt_mixinmethod
    def get_Journal(self: Windows.Devices.PointOfService.IClaimedPosPrinter) -> Windows.Devices.PointOfService.ClaimedJournalPrinter: ...
    @winrt_mixinmethod
    def EnableAsync(self: Windows.Devices.PointOfService.IClaimedPosPrinter) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def DisableAsync(self: Windows.Devices.PointOfService.IClaimedPosPrinter) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RetainDeviceAsync(self: Windows.Devices.PointOfService.IClaimedPosPrinter) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def ResetStatisticsAsync(self: Windows.Devices.PointOfService.IClaimedPosPrinter, statisticsCategories: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def UpdateStatisticsAsync(self: Windows.Devices.PointOfService.IClaimedPosPrinter, statistics: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_ReleaseDeviceRequested(self: Windows.Devices.PointOfService.IClaimedPosPrinter, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedPosPrinter, Windows.Devices.PointOfService.PosPrinterReleaseDeviceRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ReleaseDeviceRequested(self: Windows.Devices.PointOfService.IClaimedPosPrinter, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.Devices.PointOfService.IClaimedPosPrinter2, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedPosPrinter, Windows.Devices.PointOfService.ClaimedPosPrinterClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.Devices.PointOfService.IClaimedPosPrinter2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    IsEnabled = property(get_IsEnabled, None)
    CharacterSet = property(get_CharacterSet, put_CharacterSet)
    IsCoverOpen = property(get_IsCoverOpen, None)
    IsCharacterSetMappingEnabled = property(get_IsCharacterSetMappingEnabled, put_IsCharacterSetMappingEnabled)
    MapMode = property(get_MapMode, put_MapMode)
    Receipt = property(get_Receipt, None)
    Slip = property(get_Slip, None)
    Journal = property(get_Journal, None)
class ClaimedPosPrinterClosedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IClaimedPosPrinterClosedEventArgs
    _classid_ = 'Windows.Devices.PointOfService.ClaimedPosPrinterClosedEventArgs'
class ClaimedReceiptPrinter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IClaimedReceiptPrinter
    _classid_ = 'Windows.Devices.PointOfService.ClaimedReceiptPrinter'
    @winrt_mixinmethod
    def get_SidewaysMaxLines(self: Windows.Devices.PointOfService.IClaimedReceiptPrinter) -> UInt32: ...
    @winrt_mixinmethod
    def get_SidewaysMaxChars(self: Windows.Devices.PointOfService.IClaimedReceiptPrinter) -> UInt32: ...
    @winrt_mixinmethod
    def get_LinesToPaperCut(self: Windows.Devices.PointOfService.IClaimedReceiptPrinter) -> UInt32: ...
    @winrt_mixinmethod
    def get_PageSize(self: Windows.Devices.PointOfService.IClaimedReceiptPrinter) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_PrintArea(self: Windows.Devices.PointOfService.IClaimedReceiptPrinter) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def CreateJob(self: Windows.Devices.PointOfService.IClaimedReceiptPrinter) -> Windows.Devices.PointOfService.ReceiptPrintJob: ...
    @winrt_mixinmethod
    def put_CharactersPerLine(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CharactersPerLine(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> UInt32: ...
    @winrt_mixinmethod
    def put_LineHeight(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_LineHeight(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> UInt32: ...
    @winrt_mixinmethod
    def put_LineSpacing(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_LineSpacing(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> UInt32: ...
    @winrt_mixinmethod
    def get_LineWidth(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> UInt32: ...
    @winrt_mixinmethod
    def put_IsLetterQuality(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsLetterQuality(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPaperNearEnd(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def put_ColorCartridge(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation, value: Windows.Devices.PointOfService.PosPrinterColorCartridge) -> Void: ...
    @winrt_mixinmethod
    def get_ColorCartridge(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Windows.Devices.PointOfService.PosPrinterColorCartridge: ...
    @winrt_mixinmethod
    def get_IsCoverOpen(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCartridgeRemoved(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCartridgeEmpty(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsHeadCleaning(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPaperEmpty(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsReadyToPrint(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def ValidateData(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation, data: WinRT_String) -> Boolean: ...
    SidewaysMaxLines = property(get_SidewaysMaxLines, None)
    SidewaysMaxChars = property(get_SidewaysMaxChars, None)
    LinesToPaperCut = property(get_LinesToPaperCut, None)
    PageSize = property(get_PageSize, None)
    PrintArea = property(get_PrintArea, None)
    CharactersPerLine = property(get_CharactersPerLine, put_CharactersPerLine)
    LineHeight = property(get_LineHeight, put_LineHeight)
    LineSpacing = property(get_LineSpacing, put_LineSpacing)
    LineWidth = property(get_LineWidth, None)
    IsLetterQuality = property(get_IsLetterQuality, put_IsLetterQuality)
    IsPaperNearEnd = property(get_IsPaperNearEnd, None)
    ColorCartridge = property(get_ColorCartridge, put_ColorCartridge)
    IsCoverOpen = property(get_IsCoverOpen, None)
    IsCartridgeRemoved = property(get_IsCartridgeRemoved, None)
    IsCartridgeEmpty = property(get_IsCartridgeEmpty, None)
    IsHeadCleaning = property(get_IsHeadCleaning, None)
    IsPaperEmpty = property(get_IsPaperEmpty, None)
    IsReadyToPrint = property(get_IsReadyToPrint, None)
class ClaimedSlipPrinter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IClaimedSlipPrinter
    _classid_ = 'Windows.Devices.PointOfService.ClaimedSlipPrinter'
    @winrt_mixinmethod
    def get_SidewaysMaxLines(self: Windows.Devices.PointOfService.IClaimedSlipPrinter) -> UInt32: ...
    @winrt_mixinmethod
    def get_SidewaysMaxChars(self: Windows.Devices.PointOfService.IClaimedSlipPrinter) -> UInt32: ...
    @winrt_mixinmethod
    def get_MaxLines(self: Windows.Devices.PointOfService.IClaimedSlipPrinter) -> UInt32: ...
    @winrt_mixinmethod
    def get_LinesNearEndToEnd(self: Windows.Devices.PointOfService.IClaimedSlipPrinter) -> UInt32: ...
    @winrt_mixinmethod
    def get_PrintSide(self: Windows.Devices.PointOfService.IClaimedSlipPrinter) -> Windows.Devices.PointOfService.PosPrinterPrintSide: ...
    @winrt_mixinmethod
    def get_PageSize(self: Windows.Devices.PointOfService.IClaimedSlipPrinter) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_PrintArea(self: Windows.Devices.PointOfService.IClaimedSlipPrinter) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def OpenJaws(self: Windows.Devices.PointOfService.IClaimedSlipPrinter) -> Void: ...
    @winrt_mixinmethod
    def CloseJaws(self: Windows.Devices.PointOfService.IClaimedSlipPrinter) -> Void: ...
    @winrt_mixinmethod
    def InsertSlipAsync(self: Windows.Devices.PointOfService.IClaimedSlipPrinter, timeout: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RemoveSlipAsync(self: Windows.Devices.PointOfService.IClaimedSlipPrinter, timeout: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def ChangePrintSide(self: Windows.Devices.PointOfService.IClaimedSlipPrinter, printSide: Windows.Devices.PointOfService.PosPrinterPrintSide) -> Void: ...
    @winrt_mixinmethod
    def CreateJob(self: Windows.Devices.PointOfService.IClaimedSlipPrinter) -> Windows.Devices.PointOfService.SlipPrintJob: ...
    @winrt_mixinmethod
    def put_CharactersPerLine(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CharactersPerLine(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> UInt32: ...
    @winrt_mixinmethod
    def put_LineHeight(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_LineHeight(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> UInt32: ...
    @winrt_mixinmethod
    def put_LineSpacing(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_LineSpacing(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> UInt32: ...
    @winrt_mixinmethod
    def get_LineWidth(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> UInt32: ...
    @winrt_mixinmethod
    def put_IsLetterQuality(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsLetterQuality(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPaperNearEnd(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def put_ColorCartridge(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation, value: Windows.Devices.PointOfService.PosPrinterColorCartridge) -> Void: ...
    @winrt_mixinmethod
    def get_ColorCartridge(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Windows.Devices.PointOfService.PosPrinterColorCartridge: ...
    @winrt_mixinmethod
    def get_IsCoverOpen(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCartridgeRemoved(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCartridgeEmpty(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsHeadCleaning(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPaperEmpty(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsReadyToPrint(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation) -> Boolean: ...
    @winrt_mixinmethod
    def ValidateData(self: Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation, data: WinRT_String) -> Boolean: ...
    SidewaysMaxLines = property(get_SidewaysMaxLines, None)
    SidewaysMaxChars = property(get_SidewaysMaxChars, None)
    MaxLines = property(get_MaxLines, None)
    LinesNearEndToEnd = property(get_LinesNearEndToEnd, None)
    PrintSide = property(get_PrintSide, None)
    PageSize = property(get_PageSize, None)
    PrintArea = property(get_PrintArea, None)
    CharactersPerLine = property(get_CharactersPerLine, put_CharactersPerLine)
    LineHeight = property(get_LineHeight, put_LineHeight)
    LineSpacing = property(get_LineSpacing, put_LineSpacing)
    LineWidth = property(get_LineWidth, None)
    IsLetterQuality = property(get_IsLetterQuality, put_IsLetterQuality)
    IsPaperNearEnd = property(get_IsPaperNearEnd, None)
    ColorCartridge = property(get_ColorCartridge, put_ColorCartridge)
    IsCoverOpen = property(get_IsCoverOpen, None)
    IsCartridgeRemoved = property(get_IsCartridgeRemoved, None)
    IsCartridgeEmpty = property(get_IsCartridgeEmpty, None)
    IsHeadCleaning = property(get_IsHeadCleaning, None)
    IsPaperEmpty = property(get_IsPaperEmpty, None)
    IsReadyToPrint = property(get_IsReadyToPrint, None)
class IBarcodeScanner(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IBarcodeScanner'
    _iid_ = Guid('{bea33e06-b264-4f03-a9c1-45b20f01134f}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Capabilities(self) -> Windows.Devices.PointOfService.BarcodeScannerCapabilities: ...
    @winrt_commethod(8)
    def ClaimScannerAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.ClaimedBarcodeScanner]: ...
    @winrt_commethod(9)
    def CheckHealthAsync(self, level: Windows.Devices.PointOfService.UnifiedPosHealthCheckLevel) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(10)
    def GetSupportedSymbologiesAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[UInt32]]: ...
    @winrt_commethod(11)
    def IsSymbologySupportedAsync(self, barcodeSymbology: UInt32) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(12)
    def RetrieveStatisticsAsync(self, statisticsCategories: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(13)
    def GetSupportedProfiles(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(14)
    def IsProfileSupported(self, profile: WinRT_String) -> Boolean: ...
    @winrt_commethod(15)
    def add_StatusUpdated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.BarcodeScanner, Windows.Devices.PointOfService.BarcodeScannerStatusUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_StatusUpdated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    Capabilities = property(get_Capabilities, None)
class IBarcodeScanner2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IBarcodeScanner2'
    _iid_ = Guid('{89215167-8cee-436d-89ab-8dfb43bb4286}')
    @winrt_commethod(6)
    def get_VideoDeviceId(self) -> WinRT_String: ...
    VideoDeviceId = property(get_VideoDeviceId, None)
class IBarcodeScannerCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IBarcodeScannerCapabilities'
    _iid_ = Guid('{c60691e4-f2c8-4420-a307-b12ef6622857}')
    @winrt_commethod(6)
    def get_PowerReportingType(self) -> Windows.Devices.PointOfService.UnifiedPosPowerReportingType: ...
    @winrt_commethod(7)
    def get_IsStatisticsReportingSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsStatisticsUpdatingSupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsImagePreviewSupported(self) -> Boolean: ...
    PowerReportingType = property(get_PowerReportingType, None)
    IsStatisticsReportingSupported = property(get_IsStatisticsReportingSupported, None)
    IsStatisticsUpdatingSupported = property(get_IsStatisticsUpdatingSupported, None)
    IsImagePreviewSupported = property(get_IsImagePreviewSupported, None)
class IBarcodeScannerCapabilities1(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IBarcodeScannerCapabilities1'
    _iid_ = Guid('{8e5ab3e9-0e2c-472f-a1cc-ee8054b6a684}')
    @winrt_commethod(6)
    def get_IsSoftwareTriggerSupported(self) -> Boolean: ...
    IsSoftwareTriggerSupported = property(get_IsSoftwareTriggerSupported, None)
class IBarcodeScannerCapabilities2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IBarcodeScannerCapabilities2'
    _iid_ = Guid('{f211cfec-e1a1-4ea8-9abc-92b1596270ab}')
    @winrt_commethod(6)
    def get_IsVideoPreviewSupported(self) -> Boolean: ...
    IsVideoPreviewSupported = property(get_IsVideoPreviewSupported, None)
class IBarcodeScannerDataReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IBarcodeScannerDataReceivedEventArgs'
    _iid_ = Guid('{4234a7e2-ed97-467d-ad2b-01e44313a929}')
    @winrt_commethod(6)
    def get_Report(self) -> Windows.Devices.PointOfService.BarcodeScannerReport: ...
    Report = property(get_Report, None)
class IBarcodeScannerErrorOccurredEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IBarcodeScannerErrorOccurredEventArgs'
    _iid_ = Guid('{2cd2602f-cf3a-4002-a75a-c5ec468f0a20}')
    @winrt_commethod(6)
    def get_PartialInputData(self) -> Windows.Devices.PointOfService.BarcodeScannerReport: ...
    @winrt_commethod(7)
    def get_IsRetriable(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ErrorData(self) -> Windows.Devices.PointOfService.UnifiedPosErrorData: ...
    PartialInputData = property(get_PartialInputData, None)
    IsRetriable = property(get_IsRetriable, None)
    ErrorData = property(get_ErrorData, None)
class IBarcodeScannerImagePreviewReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IBarcodeScannerImagePreviewReceivedEventArgs'
    _iid_ = Guid('{f3b7de85-6e8b-434e-9f58-06ef26bc4baf}')
    @winrt_commethod(6)
    def get_Preview(self) -> Windows.Storage.Streams.IRandomAccessStreamWithContentType: ...
    Preview = property(get_Preview, None)
class IBarcodeScannerReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IBarcodeScannerReport'
    _iid_ = Guid('{5ce4d8b0-a489-4b96-86c4-f0bf8a37753d}')
    @winrt_commethod(6)
    def get_ScanDataType(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_ScanData(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def get_ScanDataLabel(self) -> Windows.Storage.Streams.IBuffer: ...
    ScanDataType = property(get_ScanDataType, None)
    ScanData = property(get_ScanData, None)
    ScanDataLabel = property(get_ScanDataLabel, None)
class IBarcodeScannerReportFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IBarcodeScannerReportFactory'
    _iid_ = Guid('{a2547326-2013-457c-8963-49c15dca78ce}')
    @winrt_commethod(6)
    def CreateInstance(self, scanDataType: UInt32, scanData: Windows.Storage.Streams.IBuffer, scanDataLabel: Windows.Storage.Streams.IBuffer) -> Windows.Devices.PointOfService.BarcodeScannerReport: ...
class IBarcodeScannerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IBarcodeScannerStatics'
    _iid_ = Guid('{5d115f6f-da49-41e8-8c8c-f0cb62a9c4fc}')
    @winrt_commethod(6)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.BarcodeScanner]: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.BarcodeScanner]: ...
    @winrt_commethod(8)
    def GetDeviceSelector(self) -> WinRT_String: ...
class IBarcodeScannerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IBarcodeScannerStatics2'
    _iid_ = Guid('{b8652473-a36f-4007-b1d0-279ebe92a656}')
    @winrt_commethod(6)
    def GetDeviceSelectorWithConnectionTypes(self, connectionTypes: Windows.Devices.PointOfService.PosConnectionTypes) -> WinRT_String: ...
class IBarcodeScannerStatusUpdatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IBarcodeScannerStatusUpdatedEventArgs'
    _iid_ = Guid('{355d8586-9c43-462b-a91a-816dc97f452c}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.PointOfService.BarcodeScannerStatus: ...
    @winrt_commethod(7)
    def get_ExtendedStatus(self) -> UInt32: ...
    Status = property(get_Status, None)
    ExtendedStatus = property(get_ExtendedStatus, None)
class IBarcodeSymbologiesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IBarcodeSymbologiesStatics'
    _iid_ = Guid('{ca8549bb-06d2-43f4-a44b-c620679fd8d0}')
    @winrt_commethod(6)
    def get_Unknown(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Ean8(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Ean8Add2(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Ean8Add5(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_Eanv(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_EanvAdd2(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_EanvAdd5(self) -> UInt32: ...
    @winrt_commethod(13)
    def get_Ean13(self) -> UInt32: ...
    @winrt_commethod(14)
    def get_Ean13Add2(self) -> UInt32: ...
    @winrt_commethod(15)
    def get_Ean13Add5(self) -> UInt32: ...
    @winrt_commethod(16)
    def get_Isbn(self) -> UInt32: ...
    @winrt_commethod(17)
    def get_IsbnAdd5(self) -> UInt32: ...
    @winrt_commethod(18)
    def get_Ismn(self) -> UInt32: ...
    @winrt_commethod(19)
    def get_IsmnAdd2(self) -> UInt32: ...
    @winrt_commethod(20)
    def get_IsmnAdd5(self) -> UInt32: ...
    @winrt_commethod(21)
    def get_Issn(self) -> UInt32: ...
    @winrt_commethod(22)
    def get_IssnAdd2(self) -> UInt32: ...
    @winrt_commethod(23)
    def get_IssnAdd5(self) -> UInt32: ...
    @winrt_commethod(24)
    def get_Ean99(self) -> UInt32: ...
    @winrt_commethod(25)
    def get_Ean99Add2(self) -> UInt32: ...
    @winrt_commethod(26)
    def get_Ean99Add5(self) -> UInt32: ...
    @winrt_commethod(27)
    def get_Upca(self) -> UInt32: ...
    @winrt_commethod(28)
    def get_UpcaAdd2(self) -> UInt32: ...
    @winrt_commethod(29)
    def get_UpcaAdd5(self) -> UInt32: ...
    @winrt_commethod(30)
    def get_Upce(self) -> UInt32: ...
    @winrt_commethod(31)
    def get_UpceAdd2(self) -> UInt32: ...
    @winrt_commethod(32)
    def get_UpceAdd5(self) -> UInt32: ...
    @winrt_commethod(33)
    def get_UpcCoupon(self) -> UInt32: ...
    @winrt_commethod(34)
    def get_TfStd(self) -> UInt32: ...
    @winrt_commethod(35)
    def get_TfDis(self) -> UInt32: ...
    @winrt_commethod(36)
    def get_TfInt(self) -> UInt32: ...
    @winrt_commethod(37)
    def get_TfInd(self) -> UInt32: ...
    @winrt_commethod(38)
    def get_TfMat(self) -> UInt32: ...
    @winrt_commethod(39)
    def get_TfIata(self) -> UInt32: ...
    @winrt_commethod(40)
    def get_Gs1DatabarType1(self) -> UInt32: ...
    @winrt_commethod(41)
    def get_Gs1DatabarType2(self) -> UInt32: ...
    @winrt_commethod(42)
    def get_Gs1DatabarType3(self) -> UInt32: ...
    @winrt_commethod(43)
    def get_Code39(self) -> UInt32: ...
    @winrt_commethod(44)
    def get_Code39Ex(self) -> UInt32: ...
    @winrt_commethod(45)
    def get_Trioptic39(self) -> UInt32: ...
    @winrt_commethod(46)
    def get_Code32(self) -> UInt32: ...
    @winrt_commethod(47)
    def get_Pzn(self) -> UInt32: ...
    @winrt_commethod(48)
    def get_Code93(self) -> UInt32: ...
    @winrt_commethod(49)
    def get_Code93Ex(self) -> UInt32: ...
    @winrt_commethod(50)
    def get_Code128(self) -> UInt32: ...
    @winrt_commethod(51)
    def get_Gs1128(self) -> UInt32: ...
    @winrt_commethod(52)
    def get_Gs1128Coupon(self) -> UInt32: ...
    @winrt_commethod(53)
    def get_UccEan128(self) -> UInt32: ...
    @winrt_commethod(54)
    def get_Sisac(self) -> UInt32: ...
    @winrt_commethod(55)
    def get_Isbt(self) -> UInt32: ...
    @winrt_commethod(56)
    def get_Codabar(self) -> UInt32: ...
    @winrt_commethod(57)
    def get_Code11(self) -> UInt32: ...
    @winrt_commethod(58)
    def get_Msi(self) -> UInt32: ...
    @winrt_commethod(59)
    def get_Plessey(self) -> UInt32: ...
    @winrt_commethod(60)
    def get_Telepen(self) -> UInt32: ...
    @winrt_commethod(61)
    def get_Code16k(self) -> UInt32: ...
    @winrt_commethod(62)
    def get_CodablockA(self) -> UInt32: ...
    @winrt_commethod(63)
    def get_CodablockF(self) -> UInt32: ...
    @winrt_commethod(64)
    def get_Codablock128(self) -> UInt32: ...
    @winrt_commethod(65)
    def get_Code49(self) -> UInt32: ...
    @winrt_commethod(66)
    def get_Aztec(self) -> UInt32: ...
    @winrt_commethod(67)
    def get_DataCode(self) -> UInt32: ...
    @winrt_commethod(68)
    def get_DataMatrix(self) -> UInt32: ...
    @winrt_commethod(69)
    def get_HanXin(self) -> UInt32: ...
    @winrt_commethod(70)
    def get_Maxicode(self) -> UInt32: ...
    @winrt_commethod(71)
    def get_MicroPdf417(self) -> UInt32: ...
    @winrt_commethod(72)
    def get_MicroQr(self) -> UInt32: ...
    @winrt_commethod(73)
    def get_Pdf417(self) -> UInt32: ...
    @winrt_commethod(74)
    def get_Qr(self) -> UInt32: ...
    @winrt_commethod(75)
    def get_MsTag(self) -> UInt32: ...
    @winrt_commethod(76)
    def get_Ccab(self) -> UInt32: ...
    @winrt_commethod(77)
    def get_Ccc(self) -> UInt32: ...
    @winrt_commethod(78)
    def get_Tlc39(self) -> UInt32: ...
    @winrt_commethod(79)
    def get_AusPost(self) -> UInt32: ...
    @winrt_commethod(80)
    def get_CanPost(self) -> UInt32: ...
    @winrt_commethod(81)
    def get_ChinaPost(self) -> UInt32: ...
    @winrt_commethod(82)
    def get_DutchKix(self) -> UInt32: ...
    @winrt_commethod(83)
    def get_InfoMail(self) -> UInt32: ...
    @winrt_commethod(84)
    def get_ItalianPost25(self) -> UInt32: ...
    @winrt_commethod(85)
    def get_ItalianPost39(self) -> UInt32: ...
    @winrt_commethod(86)
    def get_JapanPost(self) -> UInt32: ...
    @winrt_commethod(87)
    def get_KoreanPost(self) -> UInt32: ...
    @winrt_commethod(88)
    def get_SwedenPost(self) -> UInt32: ...
    @winrt_commethod(89)
    def get_UkPost(self) -> UInt32: ...
    @winrt_commethod(90)
    def get_UsIntelligent(self) -> UInt32: ...
    @winrt_commethod(91)
    def get_UsIntelligentPkg(self) -> UInt32: ...
    @winrt_commethod(92)
    def get_UsPlanet(self) -> UInt32: ...
    @winrt_commethod(93)
    def get_UsPostNet(self) -> UInt32: ...
    @winrt_commethod(94)
    def get_Us4StateFics(self) -> UInt32: ...
    @winrt_commethod(95)
    def get_OcrA(self) -> UInt32: ...
    @winrt_commethod(96)
    def get_OcrB(self) -> UInt32: ...
    @winrt_commethod(97)
    def get_Micr(self) -> UInt32: ...
    @winrt_commethod(98)
    def get_ExtendedBase(self) -> UInt32: ...
    @winrt_commethod(99)
    def GetName(self, scanDataType: UInt32) -> WinRT_String: ...
    Unknown = property(get_Unknown, None)
    Ean8 = property(get_Ean8, None)
    Ean8Add2 = property(get_Ean8Add2, None)
    Ean8Add5 = property(get_Ean8Add5, None)
    Eanv = property(get_Eanv, None)
    EanvAdd2 = property(get_EanvAdd2, None)
    EanvAdd5 = property(get_EanvAdd5, None)
    Ean13 = property(get_Ean13, None)
    Ean13Add2 = property(get_Ean13Add2, None)
    Ean13Add5 = property(get_Ean13Add5, None)
    Isbn = property(get_Isbn, None)
    IsbnAdd5 = property(get_IsbnAdd5, None)
    Ismn = property(get_Ismn, None)
    IsmnAdd2 = property(get_IsmnAdd2, None)
    IsmnAdd5 = property(get_IsmnAdd5, None)
    Issn = property(get_Issn, None)
    IssnAdd2 = property(get_IssnAdd2, None)
    IssnAdd5 = property(get_IssnAdd5, None)
    Ean99 = property(get_Ean99, None)
    Ean99Add2 = property(get_Ean99Add2, None)
    Ean99Add5 = property(get_Ean99Add5, None)
    Upca = property(get_Upca, None)
    UpcaAdd2 = property(get_UpcaAdd2, None)
    UpcaAdd5 = property(get_UpcaAdd5, None)
    Upce = property(get_Upce, None)
    UpceAdd2 = property(get_UpceAdd2, None)
    UpceAdd5 = property(get_UpceAdd5, None)
    UpcCoupon = property(get_UpcCoupon, None)
    TfStd = property(get_TfStd, None)
    TfDis = property(get_TfDis, None)
    TfInt = property(get_TfInt, None)
    TfInd = property(get_TfInd, None)
    TfMat = property(get_TfMat, None)
    TfIata = property(get_TfIata, None)
    Gs1DatabarType1 = property(get_Gs1DatabarType1, None)
    Gs1DatabarType2 = property(get_Gs1DatabarType2, None)
    Gs1DatabarType3 = property(get_Gs1DatabarType3, None)
    Code39 = property(get_Code39, None)
    Code39Ex = property(get_Code39Ex, None)
    Trioptic39 = property(get_Trioptic39, None)
    Code32 = property(get_Code32, None)
    Pzn = property(get_Pzn, None)
    Code93 = property(get_Code93, None)
    Code93Ex = property(get_Code93Ex, None)
    Code128 = property(get_Code128, None)
    Gs1128 = property(get_Gs1128, None)
    Gs1128Coupon = property(get_Gs1128Coupon, None)
    UccEan128 = property(get_UccEan128, None)
    Sisac = property(get_Sisac, None)
    Isbt = property(get_Isbt, None)
    Codabar = property(get_Codabar, None)
    Code11 = property(get_Code11, None)
    Msi = property(get_Msi, None)
    Plessey = property(get_Plessey, None)
    Telepen = property(get_Telepen, None)
    Code16k = property(get_Code16k, None)
    CodablockA = property(get_CodablockA, None)
    CodablockF = property(get_CodablockF, None)
    Codablock128 = property(get_Codablock128, None)
    Code49 = property(get_Code49, None)
    Aztec = property(get_Aztec, None)
    DataCode = property(get_DataCode, None)
    DataMatrix = property(get_DataMatrix, None)
    HanXin = property(get_HanXin, None)
    Maxicode = property(get_Maxicode, None)
    MicroPdf417 = property(get_MicroPdf417, None)
    MicroQr = property(get_MicroQr, None)
    Pdf417 = property(get_Pdf417, None)
    Qr = property(get_Qr, None)
    MsTag = property(get_MsTag, None)
    Ccab = property(get_Ccab, None)
    Ccc = property(get_Ccc, None)
    Tlc39 = property(get_Tlc39, None)
    AusPost = property(get_AusPost, None)
    CanPost = property(get_CanPost, None)
    ChinaPost = property(get_ChinaPost, None)
    DutchKix = property(get_DutchKix, None)
    InfoMail = property(get_InfoMail, None)
    ItalianPost25 = property(get_ItalianPost25, None)
    ItalianPost39 = property(get_ItalianPost39, None)
    JapanPost = property(get_JapanPost, None)
    KoreanPost = property(get_KoreanPost, None)
    SwedenPost = property(get_SwedenPost, None)
    UkPost = property(get_UkPost, None)
    UsIntelligent = property(get_UsIntelligent, None)
    UsIntelligentPkg = property(get_UsIntelligentPkg, None)
    UsPlanet = property(get_UsPlanet, None)
    UsPostNet = property(get_UsPostNet, None)
    Us4StateFics = property(get_Us4StateFics, None)
    OcrA = property(get_OcrA, None)
    OcrB = property(get_OcrB, None)
    Micr = property(get_Micr, None)
    ExtendedBase = property(get_ExtendedBase, None)
class IBarcodeSymbologiesStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IBarcodeSymbologiesStatics2'
    _iid_ = Guid('{8b7518f4-99d0-40bf-9424-b91d6dd4c6e0}')
    @winrt_commethod(6)
    def get_Gs1DWCode(self) -> UInt32: ...
    Gs1DWCode = property(get_Gs1DWCode, None)
class IBarcodeSymbologyAttributes(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IBarcodeSymbologyAttributes'
    _iid_ = Guid('{66413a78-ab7a-4ada-8ece-936014b2ead7}')
    @winrt_commethod(6)
    def get_IsCheckDigitValidationEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsCheckDigitValidationEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsCheckDigitValidationSupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsCheckDigitTransmissionEnabled(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsCheckDigitTransmissionEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_IsCheckDigitTransmissionSupported(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_DecodeLength1(self) -> UInt32: ...
    @winrt_commethod(13)
    def put_DecodeLength1(self, value: UInt32) -> Void: ...
    @winrt_commethod(14)
    def get_DecodeLength2(self) -> UInt32: ...
    @winrt_commethod(15)
    def put_DecodeLength2(self, value: UInt32) -> Void: ...
    @winrt_commethod(16)
    def get_DecodeLengthKind(self) -> Windows.Devices.PointOfService.BarcodeSymbologyDecodeLengthKind: ...
    @winrt_commethod(17)
    def put_DecodeLengthKind(self, value: Windows.Devices.PointOfService.BarcodeSymbologyDecodeLengthKind) -> Void: ...
    @winrt_commethod(18)
    def get_IsDecodeLengthSupported(self) -> Boolean: ...
    IsCheckDigitValidationEnabled = property(get_IsCheckDigitValidationEnabled, put_IsCheckDigitValidationEnabled)
    IsCheckDigitValidationSupported = property(get_IsCheckDigitValidationSupported, None)
    IsCheckDigitTransmissionEnabled = property(get_IsCheckDigitTransmissionEnabled, put_IsCheckDigitTransmissionEnabled)
    IsCheckDigitTransmissionSupported = property(get_IsCheckDigitTransmissionSupported, None)
    DecodeLength1 = property(get_DecodeLength1, put_DecodeLength1)
    DecodeLength2 = property(get_DecodeLength2, put_DecodeLength2)
    DecodeLengthKind = property(get_DecodeLengthKind, put_DecodeLengthKind)
    IsDecodeLengthSupported = property(get_IsDecodeLengthSupported, None)
class ICashDrawer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ICashDrawer'
    _iid_ = Guid('{9f88f5c8-de54-4aee-a890-920bcbfe30fc}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Capabilities(self) -> Windows.Devices.PointOfService.CashDrawerCapabilities: ...
    @winrt_commethod(8)
    def get_Status(self) -> Windows.Devices.PointOfService.CashDrawerStatus: ...
    @winrt_commethod(9)
    def get_IsDrawerOpen(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_DrawerEventSource(self) -> Windows.Devices.PointOfService.CashDrawerEventSource: ...
    @winrt_commethod(11)
    def ClaimDrawerAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.ClaimedCashDrawer]: ...
    @winrt_commethod(12)
    def CheckHealthAsync(self, level: Windows.Devices.PointOfService.UnifiedPosHealthCheckLevel) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(13)
    def GetStatisticsAsync(self, statisticsCategories: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(14)
    def add_StatusUpdated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.CashDrawer, Windows.Devices.PointOfService.CashDrawerStatusUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_StatusUpdated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    Capabilities = property(get_Capabilities, None)
    Status = property(get_Status, None)
    IsDrawerOpen = property(get_IsDrawerOpen, None)
    DrawerEventSource = property(get_DrawerEventSource, None)
class ICashDrawerCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ICashDrawerCapabilities'
    _iid_ = Guid('{0bc6de0b-e8e7-4b1f-b1d1-3e501ad08247}')
    @winrt_commethod(6)
    def get_PowerReportingType(self) -> Windows.Devices.PointOfService.UnifiedPosPowerReportingType: ...
    @winrt_commethod(7)
    def get_IsStatisticsReportingSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsStatisticsUpdatingSupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsStatusReportingSupported(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsStatusMultiDrawerDetectSupported(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsDrawerOpenSensorAvailable(self) -> Boolean: ...
    PowerReportingType = property(get_PowerReportingType, None)
    IsStatisticsReportingSupported = property(get_IsStatisticsReportingSupported, None)
    IsStatisticsUpdatingSupported = property(get_IsStatisticsUpdatingSupported, None)
    IsStatusReportingSupported = property(get_IsStatusReportingSupported, None)
    IsStatusMultiDrawerDetectSupported = property(get_IsStatusMultiDrawerDetectSupported, None)
    IsDrawerOpenSensorAvailable = property(get_IsDrawerOpenSensorAvailable, None)
class ICashDrawerCloseAlarm(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ICashDrawerCloseAlarm'
    _iid_ = Guid('{6bf88cc7-6f63-430e-ab3b-95d75ffbe87f}')
    @winrt_commethod(6)
    def put_AlarmTimeout(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(7)
    def get_AlarmTimeout(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def put_BeepFrequency(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_BeepFrequency(self) -> UInt32: ...
    @winrt_commethod(10)
    def put_BeepDuration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(11)
    def get_BeepDuration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(12)
    def put_BeepDelay(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(13)
    def get_BeepDelay(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(14)
    def add_AlarmTimeoutExpired(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.CashDrawerCloseAlarm, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_AlarmTimeoutExpired(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def StartAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    AlarmTimeout = property(get_AlarmTimeout, put_AlarmTimeout)
    BeepFrequency = property(get_BeepFrequency, put_BeepFrequency)
    BeepDuration = property(get_BeepDuration, put_BeepDuration)
    BeepDelay = property(get_BeepDelay, put_BeepDelay)
class ICashDrawerEventSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ICashDrawerEventSource'
    _iid_ = Guid('{e006e46c-f2f9-442f-8dd6-06c10a4227ba}')
    @winrt_commethod(6)
    def add_DrawerClosed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.CashDrawerEventSource, Windows.Devices.PointOfService.CashDrawerClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_DrawerClosed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_DrawerOpened(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.CashDrawerEventSource, Windows.Devices.PointOfService.CashDrawerOpenedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_DrawerOpened(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICashDrawerEventSourceEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ICashDrawerEventSourceEventArgs'
    _iid_ = Guid('{69cb3bc1-147f-421c-9c23-090123bb786c}')
    @winrt_commethod(6)
    def get_CashDrawer(self) -> Windows.Devices.PointOfService.CashDrawer: ...
    CashDrawer = property(get_CashDrawer, None)
class ICashDrawerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ICashDrawerStatics'
    _iid_ = Guid('{dfa0955a-d437-4fff-b547-dda969a4f883}')
    @winrt_commethod(6)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.CashDrawer]: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.CashDrawer]: ...
    @winrt_commethod(8)
    def GetDeviceSelector(self) -> WinRT_String: ...
class ICashDrawerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ICashDrawerStatics2'
    _iid_ = Guid('{3e818121-8c42-40e8-9c0e-40297048104c}')
    @winrt_commethod(6)
    def GetDeviceSelectorWithConnectionTypes(self, connectionTypes: Windows.Devices.PointOfService.PosConnectionTypes) -> WinRT_String: ...
class ICashDrawerStatus(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ICashDrawerStatus'
    _iid_ = Guid('{6bbd78bf-dca1-4e06-99eb-5af6a5aec108}')
    @winrt_commethod(6)
    def get_StatusKind(self) -> Windows.Devices.PointOfService.CashDrawerStatusKind: ...
    @winrt_commethod(7)
    def get_ExtendedStatus(self) -> UInt32: ...
    StatusKind = property(get_StatusKind, None)
    ExtendedStatus = property(get_ExtendedStatus, None)
class ICashDrawerStatusUpdatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ICashDrawerStatusUpdatedEventArgs'
    _iid_ = Guid('{30aae98a-0d70-459c-9553-87e124c52488}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.PointOfService.CashDrawerStatus: ...
    Status = property(get_Status, None)
class IClaimedBarcodeScanner(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedBarcodeScanner'
    _iid_ = Guid('{4a63b49c-8fa4-4332-bb26-945d11d81e0f}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_IsDisabledOnDataReceived(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_IsDisabledOnDataReceived(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsDecodeDataEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_IsDecodeDataEnabled(self) -> Boolean: ...
    @winrt_commethod(12)
    def EnableAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def DisableAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(14)
    def RetainDevice(self) -> Void: ...
    @winrt_commethod(15)
    def SetActiveSymbologiesAsync(self, symbologies: Windows.Foundation.Collections.IIterable[UInt32]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(16)
    def ResetStatisticsAsync(self, statisticsCategories: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(17)
    def UpdateStatisticsAsync(self, statistics: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(18)
    def SetActiveProfileAsync(self, profile: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(19)
    def add_DataReceived(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedBarcodeScanner, Windows.Devices.PointOfService.BarcodeScannerDataReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_DataReceived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_TriggerPressed(self, handler: Windows.Foundation.EventHandler[Windows.Devices.PointOfService.ClaimedBarcodeScanner]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_TriggerPressed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(23)
    def add_TriggerReleased(self, handler: Windows.Foundation.EventHandler[Windows.Devices.PointOfService.ClaimedBarcodeScanner]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_TriggerReleased(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(25)
    def add_ReleaseDeviceRequested(self, handler: Windows.Foundation.EventHandler[Windows.Devices.PointOfService.ClaimedBarcodeScanner]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(26)
    def remove_ReleaseDeviceRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(27)
    def add_ImagePreviewReceived(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedBarcodeScanner, Windows.Devices.PointOfService.BarcodeScannerImagePreviewReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(28)
    def remove_ImagePreviewReceived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(29)
    def add_ErrorOccurred(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedBarcodeScanner, Windows.Devices.PointOfService.BarcodeScannerErrorOccurredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(30)
    def remove_ErrorOccurred(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    IsEnabled = property(get_IsEnabled, None)
    IsDisabledOnDataReceived = property(get_IsDisabledOnDataReceived, put_IsDisabledOnDataReceived)
    IsDecodeDataEnabled = property(get_IsDecodeDataEnabled, put_IsDecodeDataEnabled)
class IClaimedBarcodeScanner1(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedBarcodeScanner1'
    _iid_ = Guid('{f61aad0c-8551-42b4-998c-970c20210a22}')
    @winrt_commethod(6)
    def StartSoftwareTriggerAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def StopSoftwareTriggerAsync(self) -> Windows.Foundation.IAsyncAction: ...
class IClaimedBarcodeScanner2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedBarcodeScanner2'
    _iid_ = Guid('{e3b59e8c-2d8b-4f70-8af3-3448bedd5fe2}')
    @winrt_commethod(6)
    def GetSymbologyAttributesAsync(self, barcodeSymbology: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.BarcodeSymbologyAttributes]: ...
    @winrt_commethod(7)
    def SetSymbologyAttributesAsync(self, barcodeSymbology: UInt32, attributes: Windows.Devices.PointOfService.BarcodeSymbologyAttributes) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IClaimedBarcodeScanner3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedBarcodeScanner3'
    _iid_ = Guid('{e6ceb430-712e-45fc-8b86-cd55f5aef79d}')
    @winrt_commethod(6)
    def ShowVideoPreviewAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(7)
    def HideVideoPreview(self) -> Void: ...
    @winrt_commethod(8)
    def put_IsVideoPreviewShownOnEnable(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_IsVideoPreviewShownOnEnable(self) -> Boolean: ...
    IsVideoPreviewShownOnEnable = property(get_IsVideoPreviewShownOnEnable, put_IsVideoPreviewShownOnEnable)
class IClaimedBarcodeScanner4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedBarcodeScanner4'
    _iid_ = Guid('{5d501f97-376a-41a8-a230-2f37c1949dde}')
    @winrt_commethod(6)
    def add_Closed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedBarcodeScanner, Windows.Devices.PointOfService.ClaimedBarcodeScannerClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Closed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IClaimedBarcodeScannerClosedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedBarcodeScannerClosedEventArgs'
    _iid_ = Guid('{cf7d5489-a22c-4c65-a901-88d77d833954}')
class IClaimedCashDrawer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedCashDrawer'
    _iid_ = Guid('{ca3f99af-abb8-42c1-8a84-5c66512f5a75}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsDrawerOpen(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_CloseAlarm(self) -> Windows.Devices.PointOfService.CashDrawerCloseAlarm: ...
    @winrt_commethod(10)
    def OpenDrawerAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(11)
    def EnableAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(12)
    def DisableAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(13)
    def RetainDeviceAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(14)
    def ResetStatisticsAsync(self, statisticsCategories: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(15)
    def UpdateStatisticsAsync(self, statistics: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(16)
    def add_ReleaseDeviceRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedCashDrawer, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_ReleaseDeviceRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    IsEnabled = property(get_IsEnabled, None)
    IsDrawerOpen = property(get_IsDrawerOpen, None)
    CloseAlarm = property(get_CloseAlarm, None)
class IClaimedCashDrawer2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedCashDrawer2'
    _iid_ = Guid('{9cbab5a2-de42-4d5b-b0c1-9b57a2ba89c3}')
    @winrt_commethod(6)
    def add_Closed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedCashDrawer, Windows.Devices.PointOfService.ClaimedCashDrawerClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Closed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IClaimedCashDrawerClosedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedCashDrawerClosedEventArgs'
    _iid_ = Guid('{cc573f33-3f34-4c5c-baae-deadf16cd7fa}')
class IClaimedJournalPrinter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedJournalPrinter'
    _iid_ = Guid('{67ea0630-517d-487f-9fdf-d2e0a0a264a5}')
    @winrt_commethod(6)
    def CreateJob(self) -> Windows.Devices.PointOfService.JournalPrintJob: ...
class IClaimedLineDisplay(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedLineDisplay'
    _iid_ = Guid('{120ac970-9a75-4acf-aae7-09972bcf8794}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Capabilities(self) -> Windows.Devices.PointOfService.LineDisplayCapabilities: ...
    @winrt_commethod(8)
    def get_PhysicalDeviceName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_PhysicalDeviceDescription(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_DeviceControlDescription(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_DeviceControlVersion(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_DeviceServiceVersion(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_DefaultWindow(self) -> Windows.Devices.PointOfService.LineDisplayWindow: ...
    @winrt_commethod(14)
    def RetainDevice(self) -> Void: ...
    @winrt_commethod(15)
    def add_ReleaseDeviceRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedLineDisplay, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_ReleaseDeviceRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    Capabilities = property(get_Capabilities, None)
    PhysicalDeviceName = property(get_PhysicalDeviceName, None)
    PhysicalDeviceDescription = property(get_PhysicalDeviceDescription, None)
    DeviceControlDescription = property(get_DeviceControlDescription, None)
    DeviceControlVersion = property(get_DeviceControlVersion, None)
    DeviceServiceVersion = property(get_DeviceServiceVersion, None)
    DefaultWindow = property(get_DefaultWindow, None)
class IClaimedLineDisplay2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedLineDisplay2'
    _iid_ = Guid('{a31c75ed-41f5-4e76-a074-795e47a46e97}')
    @winrt_commethod(6)
    def GetStatisticsAsync(self, statisticsCategories: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(7)
    def CheckHealthAsync(self, level: Windows.Devices.PointOfService.UnifiedPosHealthCheckLevel) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(8)
    def CheckPowerStatusAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.LineDisplayPowerStatus]: ...
    @winrt_commethod(9)
    def add_StatusUpdated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedLineDisplay, Windows.Devices.PointOfService.LineDisplayStatusUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_StatusUpdated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def get_SupportedScreenSizesInCharacters(self) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Size]: ...
    @winrt_commethod(12)
    def get_MaxBitmapSizeInPixels(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(13)
    def get_SupportedCharacterSets(self) -> Windows.Foundation.Collections.IVectorView[Int32]: ...
    @winrt_commethod(14)
    def get_CustomGlyphs(self) -> Windows.Devices.PointOfService.LineDisplayCustomGlyphs: ...
    @winrt_commethod(15)
    def GetAttributes(self) -> Windows.Devices.PointOfService.LineDisplayAttributes: ...
    @winrt_commethod(16)
    def TryUpdateAttributesAsync(self, attributes: Windows.Devices.PointOfService.LineDisplayAttributes) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(17)
    def TrySetDescriptorAsync(self, descriptor: UInt32, descriptorState: Windows.Devices.PointOfService.LineDisplayDescriptorState) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(18)
    def TryClearDescriptorsAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(19)
    def TryCreateWindowAsync(self, viewport: Windows.Foundation.Rect, windowSize: Windows.Foundation.Size) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.LineDisplayWindow]: ...
    @winrt_commethod(20)
    def TryStoreStorageFileBitmapAsync(self, bitmap: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.LineDisplayStoredBitmap]: ...
    @winrt_commethod(21)
    def TryStoreStorageFileBitmapWithAlignmentAsync(self, bitmap: Windows.Storage.StorageFile, horizontalAlignment: Windows.Devices.PointOfService.LineDisplayHorizontalAlignment, verticalAlignment: Windows.Devices.PointOfService.LineDisplayVerticalAlignment) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.LineDisplayStoredBitmap]: ...
    @winrt_commethod(22)
    def TryStoreStorageFileBitmapWithAlignmentAndWidthAsync(self, bitmap: Windows.Storage.StorageFile, horizontalAlignment: Windows.Devices.PointOfService.LineDisplayHorizontalAlignment, verticalAlignment: Windows.Devices.PointOfService.LineDisplayVerticalAlignment, widthInPixels: Int32) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.LineDisplayStoredBitmap]: ...
    SupportedScreenSizesInCharacters = property(get_SupportedScreenSizesInCharacters, None)
    MaxBitmapSizeInPixels = property(get_MaxBitmapSizeInPixels, None)
    SupportedCharacterSets = property(get_SupportedCharacterSets, None)
    CustomGlyphs = property(get_CustomGlyphs, None)
class IClaimedLineDisplay3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedLineDisplay3'
    _iid_ = Guid('{642ecd92-e9d4-4ecc-af75-329c274cd18f}')
    @winrt_commethod(6)
    def add_Closed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedLineDisplay, Windows.Devices.PointOfService.ClaimedLineDisplayClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Closed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IClaimedLineDisplayClosedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedLineDisplayClosedEventArgs'
    _iid_ = Guid('{f915f364-d3d5-4f10-b511-90939edfacd8}')
class IClaimedLineDisplayStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedLineDisplayStatics'
    _iid_ = Guid('{78ca98fb-8b6b-4973-86f0-3e570c351825}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.ClaimedLineDisplay]: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def GetDeviceSelectorWithConnectionTypes(self, connectionTypes: Windows.Devices.PointOfService.PosConnectionTypes) -> WinRT_String: ...
class IClaimedMagneticStripeReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedMagneticStripeReader'
    _iid_ = Guid('{475ca8f3-9417-48bc-b9d7-4163a7844c02}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_IsDisabledOnDataReceived(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_IsDisabledOnDataReceived(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsDecodeDataEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_IsDecodeDataEnabled(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsDeviceAuthenticated(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_DataEncryptionAlgorithm(self, value: UInt32) -> Void: ...
    @winrt_commethod(14)
    def get_DataEncryptionAlgorithm(self) -> UInt32: ...
    @winrt_commethod(15)
    def put_TracksToRead(self, value: Windows.Devices.PointOfService.MagneticStripeReaderTrackIds) -> Void: ...
    @winrt_commethod(16)
    def get_TracksToRead(self) -> Windows.Devices.PointOfService.MagneticStripeReaderTrackIds: ...
    @winrt_commethod(17)
    def put_IsTransmitSentinelsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_IsTransmitSentinelsEnabled(self) -> Boolean: ...
    @winrt_commethod(19)
    def EnableAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(20)
    def DisableAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(21)
    def RetainDevice(self) -> Void: ...
    @winrt_commethod(22)
    def SetErrorReportingType(self, value: Windows.Devices.PointOfService.MagneticStripeReaderErrorReportingType) -> Void: ...
    @winrt_commethod(23)
    def RetrieveDeviceAuthenticationDataAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(24)
    def AuthenticateDeviceAsync(self, responseToken: c_char_p_no) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(25)
    def DeAuthenticateDeviceAsync(self, responseToken: c_char_p_no) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(26)
    def UpdateKeyAsync(self, key: WinRT_String, keyName: WinRT_String) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(27)
    def ResetStatisticsAsync(self, statisticsCategories: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(28)
    def UpdateStatisticsAsync(self, statistics: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(29)
    def add_BankCardDataReceived(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedMagneticStripeReader, Windows.Devices.PointOfService.MagneticStripeReaderBankCardDataReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(30)
    def remove_BankCardDataReceived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(31)
    def add_AamvaCardDataReceived(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedMagneticStripeReader, Windows.Devices.PointOfService.MagneticStripeReaderAamvaCardDataReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(32)
    def remove_AamvaCardDataReceived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(33)
    def add_VendorSpecificDataReceived(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedMagneticStripeReader, Windows.Devices.PointOfService.MagneticStripeReaderVendorSpecificCardDataReceivedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(34)
    def remove_VendorSpecificDataReceived(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(35)
    def add_ReleaseDeviceRequested(self, handler: Windows.Foundation.EventHandler[Windows.Devices.PointOfService.ClaimedMagneticStripeReader]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(36)
    def remove_ReleaseDeviceRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(37)
    def add_ErrorOccurred(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedMagneticStripeReader, Windows.Devices.PointOfService.MagneticStripeReaderErrorOccurredEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(38)
    def remove_ErrorOccurred(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    IsEnabled = property(get_IsEnabled, None)
    IsDisabledOnDataReceived = property(get_IsDisabledOnDataReceived, put_IsDisabledOnDataReceived)
    IsDecodeDataEnabled = property(get_IsDecodeDataEnabled, put_IsDecodeDataEnabled)
    IsDeviceAuthenticated = property(get_IsDeviceAuthenticated, None)
    DataEncryptionAlgorithm = property(get_DataEncryptionAlgorithm, put_DataEncryptionAlgorithm)
    TracksToRead = property(get_TracksToRead, put_TracksToRead)
    IsTransmitSentinelsEnabled = property(get_IsTransmitSentinelsEnabled, put_IsTransmitSentinelsEnabled)
class IClaimedMagneticStripeReader2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedMagneticStripeReader2'
    _iid_ = Guid('{236fafdf-e2dc-4d7d-9c78-060df2bf2928}')
    @winrt_commethod(6)
    def add_Closed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedMagneticStripeReader, Windows.Devices.PointOfService.ClaimedMagneticStripeReaderClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Closed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IClaimedMagneticStripeReaderClosedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedMagneticStripeReaderClosedEventArgs'
    _iid_ = Guid('{14ada93a-adcd-4c80-acda-c3eaed2647e1}')
class IClaimedPosPrinter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedPosPrinter'
    _iid_ = Guid('{6d64ce0c-e03e-4b14-a38e-c28c34b86353}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_CharacterSet(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_CharacterSet(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_IsCoverOpen(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsCharacterSetMappingEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IsCharacterSetMappingEnabled(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_MapMode(self, value: Windows.Devices.PointOfService.PosPrinterMapMode) -> Void: ...
    @winrt_commethod(14)
    def get_MapMode(self) -> Windows.Devices.PointOfService.PosPrinterMapMode: ...
    @winrt_commethod(15)
    def get_Receipt(self) -> Windows.Devices.PointOfService.ClaimedReceiptPrinter: ...
    @winrt_commethod(16)
    def get_Slip(self) -> Windows.Devices.PointOfService.ClaimedSlipPrinter: ...
    @winrt_commethod(17)
    def get_Journal(self) -> Windows.Devices.PointOfService.ClaimedJournalPrinter: ...
    @winrt_commethod(18)
    def EnableAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(19)
    def DisableAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(20)
    def RetainDeviceAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(21)
    def ResetStatisticsAsync(self, statisticsCategories: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(22)
    def UpdateStatisticsAsync(self, statistics: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(23)
    def add_ReleaseDeviceRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedPosPrinter, Windows.Devices.PointOfService.PosPrinterReleaseDeviceRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_ReleaseDeviceRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    IsEnabled = property(get_IsEnabled, None)
    CharacterSet = property(get_CharacterSet, put_CharacterSet)
    IsCoverOpen = property(get_IsCoverOpen, None)
    IsCharacterSetMappingEnabled = property(get_IsCharacterSetMappingEnabled, put_IsCharacterSetMappingEnabled)
    MapMode = property(get_MapMode, put_MapMode)
    Receipt = property(get_Receipt, None)
    Slip = property(get_Slip, None)
    Journal = property(get_Journal, None)
class IClaimedPosPrinter2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedPosPrinter2'
    _iid_ = Guid('{5bf7a3d5-5198-437a-82df-589993fa77e1}')
    @winrt_commethod(6)
    def add_Closed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.ClaimedPosPrinter, Windows.Devices.PointOfService.ClaimedPosPrinterClosedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Closed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IClaimedPosPrinterClosedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedPosPrinterClosedEventArgs'
    _iid_ = Guid('{e2b7a27b-4d40-471d-92ed-63375b18c788}')
class IClaimedReceiptPrinter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedReceiptPrinter'
    _iid_ = Guid('{9ad27a74-dd61-4ee2-9837-5b5d72d538b9}')
    @winrt_commethod(6)
    def get_SidewaysMaxLines(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_SidewaysMaxChars(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_LinesToPaperCut(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_PageSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(10)
    def get_PrintArea(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(11)
    def CreateJob(self) -> Windows.Devices.PointOfService.ReceiptPrintJob: ...
    SidewaysMaxLines = property(get_SidewaysMaxLines, None)
    SidewaysMaxChars = property(get_SidewaysMaxChars, None)
    LinesToPaperCut = property(get_LinesToPaperCut, None)
    PageSize = property(get_PageSize, None)
    PrintArea = property(get_PrintArea, None)
class IClaimedSlipPrinter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IClaimedSlipPrinter'
    _iid_ = Guid('{bd5deff2-af90-4e8a-b77b-e3ae9ca63a7f}')
    @winrt_commethod(6)
    def get_SidewaysMaxLines(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_SidewaysMaxChars(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_MaxLines(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_LinesNearEndToEnd(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_PrintSide(self) -> Windows.Devices.PointOfService.PosPrinterPrintSide: ...
    @winrt_commethod(11)
    def get_PageSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(12)
    def get_PrintArea(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(13)
    def OpenJaws(self) -> Void: ...
    @winrt_commethod(14)
    def CloseJaws(self) -> Void: ...
    @winrt_commethod(15)
    def InsertSlipAsync(self, timeout: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(16)
    def RemoveSlipAsync(self, timeout: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(17)
    def ChangePrintSide(self, printSide: Windows.Devices.PointOfService.PosPrinterPrintSide) -> Void: ...
    @winrt_commethod(18)
    def CreateJob(self) -> Windows.Devices.PointOfService.SlipPrintJob: ...
    SidewaysMaxLines = property(get_SidewaysMaxLines, None)
    SidewaysMaxChars = property(get_SidewaysMaxChars, None)
    MaxLines = property(get_MaxLines, None)
    LinesNearEndToEnd = property(get_LinesNearEndToEnd, None)
    PrintSide = property(get_PrintSide, None)
    PageSize = property(get_PageSize, None)
    PrintArea = property(get_PrintArea, None)
class ICommonClaimedPosPrinterStation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ICommonClaimedPosPrinterStation'
    _iid_ = Guid('{b7eb66a8-fe8a-4cfb-8b42-e35b280cb27c}')
    @winrt_commethod(6)
    def put_CharactersPerLine(self, value: UInt32) -> Void: ...
    @winrt_commethod(7)
    def get_CharactersPerLine(self) -> UInt32: ...
    @winrt_commethod(8)
    def put_LineHeight(self, value: UInt32) -> Void: ...
    @winrt_commethod(9)
    def get_LineHeight(self) -> UInt32: ...
    @winrt_commethod(10)
    def put_LineSpacing(self, value: UInt32) -> Void: ...
    @winrt_commethod(11)
    def get_LineSpacing(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_LineWidth(self) -> UInt32: ...
    @winrt_commethod(13)
    def put_IsLetterQuality(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_IsLetterQuality(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_IsPaperNearEnd(self) -> Boolean: ...
    @winrt_commethod(16)
    def put_ColorCartridge(self, value: Windows.Devices.PointOfService.PosPrinterColorCartridge) -> Void: ...
    @winrt_commethod(17)
    def get_ColorCartridge(self) -> Windows.Devices.PointOfService.PosPrinterColorCartridge: ...
    @winrt_commethod(18)
    def get_IsCoverOpen(self) -> Boolean: ...
    @winrt_commethod(19)
    def get_IsCartridgeRemoved(self) -> Boolean: ...
    @winrt_commethod(20)
    def get_IsCartridgeEmpty(self) -> Boolean: ...
    @winrt_commethod(21)
    def get_IsHeadCleaning(self) -> Boolean: ...
    @winrt_commethod(22)
    def get_IsPaperEmpty(self) -> Boolean: ...
    @winrt_commethod(23)
    def get_IsReadyToPrint(self) -> Boolean: ...
    @winrt_commethod(24)
    def ValidateData(self, data: WinRT_String) -> Boolean: ...
    CharactersPerLine = property(get_CharactersPerLine, put_CharactersPerLine)
    LineHeight = property(get_LineHeight, put_LineHeight)
    LineSpacing = property(get_LineSpacing, put_LineSpacing)
    LineWidth = property(get_LineWidth, None)
    IsLetterQuality = property(get_IsLetterQuality, put_IsLetterQuality)
    IsPaperNearEnd = property(get_IsPaperNearEnd, None)
    ColorCartridge = property(get_ColorCartridge, put_ColorCartridge)
    IsCoverOpen = property(get_IsCoverOpen, None)
    IsCartridgeRemoved = property(get_IsCartridgeRemoved, None)
    IsCartridgeEmpty = property(get_IsCartridgeEmpty, None)
    IsHeadCleaning = property(get_IsHeadCleaning, None)
    IsPaperEmpty = property(get_IsPaperEmpty, None)
    IsReadyToPrint = property(get_IsReadyToPrint, None)
class ICommonPosPrintStationCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities'
    _iid_ = Guid('{de5b52ca-e02e-40e9-9e5e-1b488e6aacfc}')
    @winrt_commethod(6)
    def get_IsPrinterPresent(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsDualColorSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ColorCartridgeCapabilities(self) -> Windows.Devices.PointOfService.PosPrinterColorCapabilities: ...
    @winrt_commethod(9)
    def get_CartridgeSensors(self) -> Windows.Devices.PointOfService.PosPrinterCartridgeSensors: ...
    @winrt_commethod(10)
    def get_IsBoldSupported(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsItalicSupported(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsUnderlineSupported(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_IsDoubleHighPrintSupported(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_IsDoubleWidePrintSupported(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_IsDoubleHighDoubleWidePrintSupported(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_IsPaperEmptySensorSupported(self) -> Boolean: ...
    @winrt_commethod(17)
    def get_IsPaperNearEndSensorSupported(self) -> Boolean: ...
    @winrt_commethod(18)
    def get_SupportedCharactersPerLine(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    IsPrinterPresent = property(get_IsPrinterPresent, None)
    IsDualColorSupported = property(get_IsDualColorSupported, None)
    ColorCartridgeCapabilities = property(get_ColorCartridgeCapabilities, None)
    CartridgeSensors = property(get_CartridgeSensors, None)
    IsBoldSupported = property(get_IsBoldSupported, None)
    IsItalicSupported = property(get_IsItalicSupported, None)
    IsUnderlineSupported = property(get_IsUnderlineSupported, None)
    IsDoubleHighPrintSupported = property(get_IsDoubleHighPrintSupported, None)
    IsDoubleWidePrintSupported = property(get_IsDoubleWidePrintSupported, None)
    IsDoubleHighDoubleWidePrintSupported = property(get_IsDoubleHighDoubleWidePrintSupported, None)
    IsPaperEmptySensorSupported = property(get_IsPaperEmptySensorSupported, None)
    IsPaperNearEndSensorSupported = property(get_IsPaperNearEndSensorSupported, None)
    SupportedCharactersPerLine = property(get_SupportedCharactersPerLine, None)
class ICommonReceiptSlipCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities'
    _iid_ = Guid('{09286b8b-9873-4d05-bfbe-4727a6038f69}')
    @winrt_commethod(6)
    def get_IsBarcodeSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsBitmapSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsLeft90RotationSupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsRight90RotationSupported(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Is180RotationSupported(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsPrintAreaSupported(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_RuledLineCapabilities(self) -> Windows.Devices.PointOfService.PosPrinterRuledLineCapabilities: ...
    @winrt_commethod(13)
    def get_SupportedBarcodeRotations(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.PointOfService.PosPrinterRotation]: ...
    @winrt_commethod(14)
    def get_SupportedBitmapRotations(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.PointOfService.PosPrinterRotation]: ...
    IsBarcodeSupported = property(get_IsBarcodeSupported, None)
    IsBitmapSupported = property(get_IsBitmapSupported, None)
    IsLeft90RotationSupported = property(get_IsLeft90RotationSupported, None)
    IsRight90RotationSupported = property(get_IsRight90RotationSupported, None)
    Is180RotationSupported = property(get_Is180RotationSupported, None)
    IsPrintAreaSupported = property(get_IsPrintAreaSupported, None)
    RuledLineCapabilities = property(get_RuledLineCapabilities, None)
    SupportedBarcodeRotations = property(get_SupportedBarcodeRotations, None)
    SupportedBitmapRotations = property(get_SupportedBitmapRotations, None)
class IJournalPrintJob(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IJournalPrintJob'
    _iid_ = Guid('{9f4f2864-f3f0-55d0-8c39-74cc91783eed}')
    @winrt_commethod(6)
    def Print(self, data: WinRT_String, printOptions: Windows.Devices.PointOfService.PosPrinterPrintOptions) -> Void: ...
    @winrt_commethod(7)
    def FeedPaperByLine(self, lineCount: Int32) -> Void: ...
    @winrt_commethod(8)
    def FeedPaperByMapModeUnit(self, distance: Int32) -> Void: ...
class IJournalPrinterCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IJournalPrinterCapabilities'
    _iid_ = Guid('{3b5ccc43-e047-4463-bb58-17b5ba1d8056}')
class IJournalPrinterCapabilities2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IJournalPrinterCapabilities2'
    _iid_ = Guid('{03b0b645-33b8-533b-baaa-a4389283ab0a}')
    @winrt_commethod(6)
    def get_IsReverseVideoSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsStrikethroughSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsSuperscriptSupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsSubscriptSupported(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsReversePaperFeedByLineSupported(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsReversePaperFeedByMapModeUnitSupported(self) -> Boolean: ...
    IsReverseVideoSupported = property(get_IsReverseVideoSupported, None)
    IsStrikethroughSupported = property(get_IsStrikethroughSupported, None)
    IsSuperscriptSupported = property(get_IsSuperscriptSupported, None)
    IsSubscriptSupported = property(get_IsSubscriptSupported, None)
    IsReversePaperFeedByLineSupported = property(get_IsReversePaperFeedByLineSupported, None)
    IsReversePaperFeedByMapModeUnitSupported = property(get_IsReversePaperFeedByMapModeUnitSupported, None)
class ILineDisplay(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ILineDisplay'
    _iid_ = Guid('{24f5df4e-3c99-44e2-b73f-e51be3637a8c}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Capabilities(self) -> Windows.Devices.PointOfService.LineDisplayCapabilities: ...
    @winrt_commethod(8)
    def get_PhysicalDeviceName(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_PhysicalDeviceDescription(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_DeviceControlDescription(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_DeviceControlVersion(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_DeviceServiceVersion(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def ClaimAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.ClaimedLineDisplay]: ...
    DeviceId = property(get_DeviceId, None)
    Capabilities = property(get_Capabilities, None)
    PhysicalDeviceName = property(get_PhysicalDeviceName, None)
    PhysicalDeviceDescription = property(get_PhysicalDeviceDescription, None)
    DeviceControlDescription = property(get_DeviceControlDescription, None)
    DeviceControlVersion = property(get_DeviceControlVersion, None)
    DeviceServiceVersion = property(get_DeviceServiceVersion, None)
class ILineDisplay2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ILineDisplay2'
    _iid_ = Guid('{c296a628-ef44-40f3-bd1c-b04c6a5cdc7d}')
    @winrt_commethod(6)
    def CheckPowerStatusAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.LineDisplayPowerStatus]: ...
class ILineDisplayAttributes(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ILineDisplayAttributes'
    _iid_ = Guid('{c17de99c-229a-4c14-a6f1-b4e4b1fead92}')
    @winrt_commethod(6)
    def get_IsPowerNotifyEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsPowerNotifyEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Brightness(self) -> Int32: ...
    @winrt_commethod(9)
    def put_Brightness(self, value: Int32) -> Void: ...
    @winrt_commethod(10)
    def get_BlinkRate(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def put_BlinkRate(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(12)
    def get_ScreenSizeInCharacters(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(13)
    def put_ScreenSizeInCharacters(self, value: Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(14)
    def get_CharacterSet(self) -> Int32: ...
    @winrt_commethod(15)
    def put_CharacterSet(self, value: Int32) -> Void: ...
    @winrt_commethod(16)
    def get_IsCharacterSetMappingEnabled(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_IsCharacterSetMappingEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_CurrentWindow(self) -> Windows.Devices.PointOfService.LineDisplayWindow: ...
    @winrt_commethod(19)
    def put_CurrentWindow(self, value: Windows.Devices.PointOfService.LineDisplayWindow) -> Void: ...
    IsPowerNotifyEnabled = property(get_IsPowerNotifyEnabled, put_IsPowerNotifyEnabled)
    Brightness = property(get_Brightness, put_Brightness)
    BlinkRate = property(get_BlinkRate, put_BlinkRate)
    ScreenSizeInCharacters = property(get_ScreenSizeInCharacters, put_ScreenSizeInCharacters)
    CharacterSet = property(get_CharacterSet, put_CharacterSet)
    IsCharacterSetMappingEnabled = property(get_IsCharacterSetMappingEnabled, put_IsCharacterSetMappingEnabled)
    CurrentWindow = property(get_CurrentWindow, put_CurrentWindow)
class ILineDisplayCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ILineDisplayCapabilities'
    _iid_ = Guid('{5a15b5d1-8dc5-4b9c-9172-303e47b70c55}')
    @winrt_commethod(6)
    def get_IsStatisticsReportingSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsStatisticsUpdatingSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_PowerReportingType(self) -> Windows.Devices.PointOfService.UnifiedPosPowerReportingType: ...
    @winrt_commethod(9)
    def get_CanChangeScreenSize(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_CanDisplayBitmaps(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_CanReadCharacterAtCursor(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_CanMapCharacterSets(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_CanDisplayCustomGlyphs(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_CanReverse(self) -> Windows.Devices.PointOfService.LineDisplayTextAttributeGranularity: ...
    @winrt_commethod(15)
    def get_CanBlink(self) -> Windows.Devices.PointOfService.LineDisplayTextAttributeGranularity: ...
    @winrt_commethod(16)
    def get_CanChangeBlinkRate(self) -> Boolean: ...
    @winrt_commethod(17)
    def get_IsBrightnessSupported(self) -> Boolean: ...
    @winrt_commethod(18)
    def get_IsCursorSupported(self) -> Boolean: ...
    @winrt_commethod(19)
    def get_IsHorizontalMarqueeSupported(self) -> Boolean: ...
    @winrt_commethod(20)
    def get_IsVerticalMarqueeSupported(self) -> Boolean: ...
    @winrt_commethod(21)
    def get_IsInterCharacterWaitSupported(self) -> Boolean: ...
    @winrt_commethod(22)
    def get_SupportedDescriptors(self) -> UInt32: ...
    @winrt_commethod(23)
    def get_SupportedWindows(self) -> UInt32: ...
    IsStatisticsReportingSupported = property(get_IsStatisticsReportingSupported, None)
    IsStatisticsUpdatingSupported = property(get_IsStatisticsUpdatingSupported, None)
    PowerReportingType = property(get_PowerReportingType, None)
    CanChangeScreenSize = property(get_CanChangeScreenSize, None)
    CanDisplayBitmaps = property(get_CanDisplayBitmaps, None)
    CanReadCharacterAtCursor = property(get_CanReadCharacterAtCursor, None)
    CanMapCharacterSets = property(get_CanMapCharacterSets, None)
    CanDisplayCustomGlyphs = property(get_CanDisplayCustomGlyphs, None)
    CanReverse = property(get_CanReverse, None)
    CanBlink = property(get_CanBlink, None)
    CanChangeBlinkRate = property(get_CanChangeBlinkRate, None)
    IsBrightnessSupported = property(get_IsBrightnessSupported, None)
    IsCursorSupported = property(get_IsCursorSupported, None)
    IsHorizontalMarqueeSupported = property(get_IsHorizontalMarqueeSupported, None)
    IsVerticalMarqueeSupported = property(get_IsVerticalMarqueeSupported, None)
    IsInterCharacterWaitSupported = property(get_IsInterCharacterWaitSupported, None)
    SupportedDescriptors = property(get_SupportedDescriptors, None)
    SupportedWindows = property(get_SupportedWindows, None)
class ILineDisplayCursor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ILineDisplayCursor'
    _iid_ = Guid('{ecdffc45-754a-4e3b-ab2b-151181085605}')
    @winrt_commethod(6)
    def get_CanCustomize(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsBlinkSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsBlockSupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsHalfBlockSupported(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsUnderlineSupported(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsReverseSupported(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsOtherSupported(self) -> Boolean: ...
    @winrt_commethod(13)
    def GetAttributes(self) -> Windows.Devices.PointOfService.LineDisplayCursorAttributes: ...
    @winrt_commethod(14)
    def TryUpdateAttributesAsync(self, attributes: Windows.Devices.PointOfService.LineDisplayCursorAttributes) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    CanCustomize = property(get_CanCustomize, None)
    IsBlinkSupported = property(get_IsBlinkSupported, None)
    IsBlockSupported = property(get_IsBlockSupported, None)
    IsHalfBlockSupported = property(get_IsHalfBlockSupported, None)
    IsUnderlineSupported = property(get_IsUnderlineSupported, None)
    IsReverseSupported = property(get_IsReverseSupported, None)
    IsOtherSupported = property(get_IsOtherSupported, None)
class ILineDisplayCursorAttributes(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ILineDisplayCursorAttributes'
    _iid_ = Guid('{4e2d54fe-4ffd-4190-aae1-ce285f20c896}')
    @winrt_commethod(6)
    def get_IsBlinkEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsBlinkEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CursorType(self) -> Windows.Devices.PointOfService.LineDisplayCursorType: ...
    @winrt_commethod(9)
    def put_CursorType(self, value: Windows.Devices.PointOfService.LineDisplayCursorType) -> Void: ...
    @winrt_commethod(10)
    def get_IsAutoAdvanceEnabled(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsAutoAdvanceEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_Position(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(13)
    def put_Position(self, value: Windows.Foundation.Point) -> Void: ...
    IsBlinkEnabled = property(get_IsBlinkEnabled, put_IsBlinkEnabled)
    CursorType = property(get_CursorType, put_CursorType)
    IsAutoAdvanceEnabled = property(get_IsAutoAdvanceEnabled, put_IsAutoAdvanceEnabled)
    Position = property(get_Position, put_Position)
class ILineDisplayCustomGlyphs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ILineDisplayCustomGlyphs'
    _iid_ = Guid('{2257f63c-f263-44f1-a1a0-e750a6a0ec54}')
    @winrt_commethod(6)
    def get_SizeInPixels(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(7)
    def get_SupportedGlyphCodes(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(8)
    def TryRedefineAsync(self, glyphCode: UInt32, glyphData: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    SizeInPixels = property(get_SizeInPixels, None)
    SupportedGlyphCodes = property(get_SupportedGlyphCodes, None)
class ILineDisplayMarquee(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ILineDisplayMarquee'
    _iid_ = Guid('{a3d33e3e-f46a-4b7a-bc21-53eb3b57f8b4}')
    @winrt_commethod(6)
    def get_Format(self) -> Windows.Devices.PointOfService.LineDisplayMarqueeFormat: ...
    @winrt_commethod(7)
    def put_Format(self, value: Windows.Devices.PointOfService.LineDisplayMarqueeFormat) -> Void: ...
    @winrt_commethod(8)
    def get_RepeatWaitInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def put_RepeatWaitInterval(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(10)
    def get_ScrollWaitInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def put_ScrollWaitInterval(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(12)
    def TryStartScrollingAsync(self, direction: Windows.Devices.PointOfService.LineDisplayScrollDirection) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(13)
    def TryStopScrollingAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    Format = property(get_Format, put_Format)
    RepeatWaitInterval = property(get_RepeatWaitInterval, put_RepeatWaitInterval)
    ScrollWaitInterval = property(get_ScrollWaitInterval, put_ScrollWaitInterval)
class ILineDisplayStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ILineDisplayStatics'
    _iid_ = Guid('{022dc0b6-11b0-4690-9547-0b39c5af2114}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.LineDisplay]: ...
    @winrt_commethod(7)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.LineDisplay]: ...
    @winrt_commethod(8)
    def GetDeviceSelector(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetDeviceSelectorWithConnectionTypes(self, connectionTypes: Windows.Devices.PointOfService.PosConnectionTypes) -> WinRT_String: ...
class ILineDisplayStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ILineDisplayStatics2'
    _iid_ = Guid('{600c3f1c-77ab-4968-a7de-c02ff169f2cc}')
    @winrt_commethod(6)
    def get_StatisticsCategorySelector(self) -> Windows.Devices.PointOfService.LineDisplayStatisticsCategorySelector: ...
    StatisticsCategorySelector = property(get_StatisticsCategorySelector, None)
class ILineDisplayStatisticsCategorySelector(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ILineDisplayStatisticsCategorySelector'
    _iid_ = Guid('{b521c46b-9274-4d24-94f3-b6017b832444}')
    @winrt_commethod(6)
    def get_AllStatistics(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_UnifiedPosStatistics(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ManufacturerStatistics(self) -> WinRT_String: ...
    AllStatistics = property(get_AllStatistics, None)
    UnifiedPosStatistics = property(get_UnifiedPosStatistics, None)
    ManufacturerStatistics = property(get_ManufacturerStatistics, None)
class ILineDisplayStatusUpdatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ILineDisplayStatusUpdatedEventArgs'
    _iid_ = Guid('{ddd57c1a-86fb-4eba-93d1-6f5eda52b752}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.PointOfService.LineDisplayPowerStatus: ...
    Status = property(get_Status, None)
class ILineDisplayStoredBitmap(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ILineDisplayStoredBitmap'
    _iid_ = Guid('{f621515b-d81e-43ba-bf1b-bcfa3c785ba0}')
    @winrt_commethod(6)
    def get_EscapeSequence(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def TryDeleteAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    EscapeSequence = property(get_EscapeSequence, None)
class ILineDisplayWindow(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ILineDisplayWindow'
    _iid_ = Guid('{d21feef4-2364-4be5-bee1-851680af4964}')
    @winrt_commethod(6)
    def get_SizeInCharacters(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(7)
    def get_InterCharacterWaitInterval(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(8)
    def put_InterCharacterWaitInterval(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(9)
    def TryRefreshAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(10)
    def TryDisplayTextAsync(self, text: WinRT_String, displayAttribute: Windows.Devices.PointOfService.LineDisplayTextAttribute) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(11)
    def TryDisplayTextAtPositionAsync(self, text: WinRT_String, displayAttribute: Windows.Devices.PointOfService.LineDisplayTextAttribute, startPosition: Windows.Foundation.Point) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(12)
    def TryDisplayTextNormalAsync(self, text: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(13)
    def TryScrollTextAsync(self, direction: Windows.Devices.PointOfService.LineDisplayScrollDirection, numberOfColumnsOrRows: UInt32) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(14)
    def TryClearTextAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    SizeInCharacters = property(get_SizeInCharacters, None)
    InterCharacterWaitInterval = property(get_InterCharacterWaitInterval, put_InterCharacterWaitInterval)
class ILineDisplayWindow2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ILineDisplayWindow2'
    _iid_ = Guid('{a95ce2e6-bdd8-4365-8e11-de94de8dff02}')
    @winrt_commethod(6)
    def get_Cursor(self) -> Windows.Devices.PointOfService.LineDisplayCursor: ...
    @winrt_commethod(7)
    def get_Marquee(self) -> Windows.Devices.PointOfService.LineDisplayMarquee: ...
    @winrt_commethod(8)
    def ReadCharacterAtCursorAsync(self) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_commethod(9)
    def TryDisplayStoredBitmapAtCursorAsync(self, bitmap: Windows.Devices.PointOfService.LineDisplayStoredBitmap) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(10)
    def TryDisplayStorageFileBitmapAtCursorAsync(self, bitmap: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(11)
    def TryDisplayStorageFileBitmapAtCursorWithAlignmentAsync(self, bitmap: Windows.Storage.StorageFile, horizontalAlignment: Windows.Devices.PointOfService.LineDisplayHorizontalAlignment, verticalAlignment: Windows.Devices.PointOfService.LineDisplayVerticalAlignment) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(12)
    def TryDisplayStorageFileBitmapAtCursorWithAlignmentAndWidthAsync(self, bitmap: Windows.Storage.StorageFile, horizontalAlignment: Windows.Devices.PointOfService.LineDisplayHorizontalAlignment, verticalAlignment: Windows.Devices.PointOfService.LineDisplayVerticalAlignment, widthInPixels: Int32) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(13)
    def TryDisplayStorageFileBitmapAtPointAsync(self, bitmap: Windows.Storage.StorageFile, offsetInPixels: Windows.Foundation.Point) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(14)
    def TryDisplayStorageFileBitmapAtPointWithWidthAsync(self, bitmap: Windows.Storage.StorageFile, offsetInPixels: Windows.Foundation.Point, widthInPixels: Int32) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    Cursor = property(get_Cursor, None)
    Marquee = property(get_Marquee, None)
class IMagneticStripeReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IMagneticStripeReader'
    _iid_ = Guid('{1a92b015-47c3-468a-9333-0c6517574883}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Capabilities(self) -> Windows.Devices.PointOfService.MagneticStripeReaderCapabilities: ...
    @winrt_commethod(8)
    def get_SupportedCardTypes(self) -> POINTER(UInt32): ...
    @winrt_commethod(9)
    def get_DeviceAuthenticationProtocol(self) -> Windows.Devices.PointOfService.MagneticStripeReaderAuthenticationProtocol: ...
    @winrt_commethod(10)
    def CheckHealthAsync(self, level: Windows.Devices.PointOfService.UnifiedPosHealthCheckLevel) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(11)
    def ClaimReaderAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.ClaimedMagneticStripeReader]: ...
    @winrt_commethod(12)
    def RetrieveStatisticsAsync(self, statisticsCategories: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_commethod(13)
    def GetErrorReportingType(self) -> Windows.Devices.PointOfService.MagneticStripeReaderErrorReportingType: ...
    @winrt_commethod(14)
    def add_StatusUpdated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.MagneticStripeReader, Windows.Devices.PointOfService.MagneticStripeReaderStatusUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_StatusUpdated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    Capabilities = property(get_Capabilities, None)
    SupportedCardTypes = property(get_SupportedCardTypes, None)
    DeviceAuthenticationProtocol = property(get_DeviceAuthenticationProtocol, None)
class IMagneticStripeReaderAamvaCardDataReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs'
    _iid_ = Guid('{0a4bbd51-c316-4910-87f3-7a62ba862d31}')
    @winrt_commethod(6)
    def get_Report(self) -> Windows.Devices.PointOfService.MagneticStripeReaderReport: ...
    @winrt_commethod(7)
    def get_LicenseNumber(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ExpirationDate(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Restrictions(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Class(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Endorsements(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_BirthDate(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_FirstName(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_Surname(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_Suffix(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_Gender(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_HairColor(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_EyeColor(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_Height(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def get_Weight(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def get_Address(self) -> WinRT_String: ...
    @winrt_commethod(22)
    def get_City(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def get_State(self) -> WinRT_String: ...
    @winrt_commethod(24)
    def get_PostalCode(self) -> WinRT_String: ...
    Report = property(get_Report, None)
    LicenseNumber = property(get_LicenseNumber, None)
    ExpirationDate = property(get_ExpirationDate, None)
    Restrictions = property(get_Restrictions, None)
    Class = property(get_Class, None)
    Endorsements = property(get_Endorsements, None)
    BirthDate = property(get_BirthDate, None)
    FirstName = property(get_FirstName, None)
    Surname = property(get_Surname, None)
    Suffix = property(get_Suffix, None)
    Gender = property(get_Gender, None)
    HairColor = property(get_HairColor, None)
    EyeColor = property(get_EyeColor, None)
    Height = property(get_Height, None)
    Weight = property(get_Weight, None)
    Address = property(get_Address, None)
    City = property(get_City, None)
    State = property(get_State, None)
    PostalCode = property(get_PostalCode, None)
class IMagneticStripeReaderBankCardDataReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IMagneticStripeReaderBankCardDataReceivedEventArgs'
    _iid_ = Guid('{2e958823-a31a-4763-882c-23725e39b08e}')
    @winrt_commethod(6)
    def get_Report(self) -> Windows.Devices.PointOfService.MagneticStripeReaderReport: ...
    @winrt_commethod(7)
    def get_AccountNumber(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ExpirationDate(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_ServiceCode(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_FirstName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_MiddleInitial(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Surname(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_Suffix(self) -> WinRT_String: ...
    Report = property(get_Report, None)
    AccountNumber = property(get_AccountNumber, None)
    ExpirationDate = property(get_ExpirationDate, None)
    ServiceCode = property(get_ServiceCode, None)
    Title = property(get_Title, None)
    FirstName = property(get_FirstName, None)
    MiddleInitial = property(get_MiddleInitial, None)
    Surname = property(get_Surname, None)
    Suffix = property(get_Suffix, None)
class IMagneticStripeReaderCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IMagneticStripeReaderCapabilities'
    _iid_ = Guid('{7128809c-c440-44a2-a467-469175d02896}')
    @winrt_commethod(6)
    def get_CardAuthentication(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_SupportedEncryptionAlgorithms(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_AuthenticationLevel(self) -> Windows.Devices.PointOfService.MagneticStripeReaderAuthenticationLevel: ...
    @winrt_commethod(9)
    def get_IsIsoSupported(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsJisOneSupported(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsJisTwoSupported(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_PowerReportingType(self) -> Windows.Devices.PointOfService.UnifiedPosPowerReportingType: ...
    @winrt_commethod(13)
    def get_IsStatisticsReportingSupported(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_IsStatisticsUpdatingSupported(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_IsTrackDataMaskingSupported(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_IsTransmitSentinelsSupported(self) -> Boolean: ...
    CardAuthentication = property(get_CardAuthentication, None)
    SupportedEncryptionAlgorithms = property(get_SupportedEncryptionAlgorithms, None)
    AuthenticationLevel = property(get_AuthenticationLevel, None)
    IsIsoSupported = property(get_IsIsoSupported, None)
    IsJisOneSupported = property(get_IsJisOneSupported, None)
    IsJisTwoSupported = property(get_IsJisTwoSupported, None)
    PowerReportingType = property(get_PowerReportingType, None)
    IsStatisticsReportingSupported = property(get_IsStatisticsReportingSupported, None)
    IsStatisticsUpdatingSupported = property(get_IsStatisticsUpdatingSupported, None)
    IsTrackDataMaskingSupported = property(get_IsTrackDataMaskingSupported, None)
    IsTransmitSentinelsSupported = property(get_IsTransmitSentinelsSupported, None)
class IMagneticStripeReaderCardTypesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IMagneticStripeReaderCardTypesStatics'
    _iid_ = Guid('{528f2c5d-2986-474f-8454-7ccd05928d5f}')
    @winrt_commethod(6)
    def get_Unknown(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Bank(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Aamva(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_ExtendedBase(self) -> UInt32: ...
    Unknown = property(get_Unknown, None)
    Bank = property(get_Bank, None)
    Aamva = property(get_Aamva, None)
    ExtendedBase = property(get_ExtendedBase, None)
class IMagneticStripeReaderEncryptionAlgorithmsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IMagneticStripeReaderEncryptionAlgorithmsStatics'
    _iid_ = Guid('{53b57350-c3db-4754-9c00-41392374a109}')
    @winrt_commethod(6)
    def get_None(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_TripleDesDukpt(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_ExtendedBase(self) -> UInt32: ...
    None = property(get_None, None)
    TripleDesDukpt = property(get_TripleDesDukpt, None)
    ExtendedBase = property(get_ExtendedBase, None)
class IMagneticStripeReaderErrorOccurredEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IMagneticStripeReaderErrorOccurredEventArgs'
    _iid_ = Guid('{1fedf95d-2c84-41ad-b778-f2356a789ab1}')
    @winrt_commethod(6)
    def get_Track1Status(self) -> Windows.Devices.PointOfService.MagneticStripeReaderTrackErrorType: ...
    @winrt_commethod(7)
    def get_Track2Status(self) -> Windows.Devices.PointOfService.MagneticStripeReaderTrackErrorType: ...
    @winrt_commethod(8)
    def get_Track3Status(self) -> Windows.Devices.PointOfService.MagneticStripeReaderTrackErrorType: ...
    @winrt_commethod(9)
    def get_Track4Status(self) -> Windows.Devices.PointOfService.MagneticStripeReaderTrackErrorType: ...
    @winrt_commethod(10)
    def get_ErrorData(self) -> Windows.Devices.PointOfService.UnifiedPosErrorData: ...
    @winrt_commethod(11)
    def get_PartialInputData(self) -> Windows.Devices.PointOfService.MagneticStripeReaderReport: ...
    Track1Status = property(get_Track1Status, None)
    Track2Status = property(get_Track2Status, None)
    Track3Status = property(get_Track3Status, None)
    Track4Status = property(get_Track4Status, None)
    ErrorData = property(get_ErrorData, None)
    PartialInputData = property(get_PartialInputData, None)
class IMagneticStripeReaderReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IMagneticStripeReaderReport'
    _iid_ = Guid('{6a5b6047-99b0-4188-bef1-eddf79f78fe6}')
    @winrt_commethod(6)
    def get_CardType(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Track1(self) -> Windows.Devices.PointOfService.MagneticStripeReaderTrackData: ...
    @winrt_commethod(8)
    def get_Track2(self) -> Windows.Devices.PointOfService.MagneticStripeReaderTrackData: ...
    @winrt_commethod(9)
    def get_Track3(self) -> Windows.Devices.PointOfService.MagneticStripeReaderTrackData: ...
    @winrt_commethod(10)
    def get_Track4(self) -> Windows.Devices.PointOfService.MagneticStripeReaderTrackData: ...
    @winrt_commethod(11)
    def get_Properties(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_commethod(12)
    def get_CardAuthenticationData(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(13)
    def get_CardAuthenticationDataLength(self) -> UInt32: ...
    @winrt_commethod(14)
    def get_AdditionalSecurityInformation(self) -> Windows.Storage.Streams.IBuffer: ...
    CardType = property(get_CardType, None)
    Track1 = property(get_Track1, None)
    Track2 = property(get_Track2, None)
    Track3 = property(get_Track3, None)
    Track4 = property(get_Track4, None)
    Properties = property(get_Properties, None)
    CardAuthenticationData = property(get_CardAuthenticationData, None)
    CardAuthenticationDataLength = property(get_CardAuthenticationDataLength, None)
    AdditionalSecurityInformation = property(get_AdditionalSecurityInformation, None)
class IMagneticStripeReaderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IMagneticStripeReaderStatics'
    _iid_ = Guid('{c45fab4a-efd7-4760-a5ce-15b0e47e94eb}')
    @winrt_commethod(6)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.MagneticStripeReader]: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.MagneticStripeReader]: ...
    @winrt_commethod(8)
    def GetDeviceSelector(self) -> WinRT_String: ...
class IMagneticStripeReaderStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IMagneticStripeReaderStatics2'
    _iid_ = Guid('{8cadc362-d667-48fa-86bc-f5ae1189262b}')
    @winrt_commethod(6)
    def GetDeviceSelectorWithConnectionTypes(self, connectionTypes: Windows.Devices.PointOfService.PosConnectionTypes) -> WinRT_String: ...
class IMagneticStripeReaderStatusUpdatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IMagneticStripeReaderStatusUpdatedEventArgs'
    _iid_ = Guid('{09cc6bb0-3262-401d-9e8a-e80d6358906b}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.PointOfService.MagneticStripeReaderStatus: ...
    @winrt_commethod(7)
    def get_ExtendedStatus(self) -> UInt32: ...
    Status = property(get_Status, None)
    ExtendedStatus = property(get_ExtendedStatus, None)
class IMagneticStripeReaderTrackData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IMagneticStripeReaderTrackData'
    _iid_ = Guid('{104cf671-4a9d-446e-abc5-20402307ba36}')
    @winrt_commethod(6)
    def get_Data(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(7)
    def get_DiscretionaryData(self) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(8)
    def get_EncryptedData(self) -> Windows.Storage.Streams.IBuffer: ...
    Data = property(get_Data, None)
    DiscretionaryData = property(get_DiscretionaryData, None)
    EncryptedData = property(get_EncryptedData, None)
class IMagneticStripeReaderVendorSpecificCardDataReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IMagneticStripeReaderVendorSpecificCardDataReceivedEventArgs'
    _iid_ = Guid('{af0a5514-59cc-4a60-99e8-99a53dace5aa}')
    @winrt_commethod(6)
    def get_Report(self) -> Windows.Devices.PointOfService.MagneticStripeReaderReport: ...
    Report = property(get_Report, None)
class IPosPrinter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IPosPrinter'
    _iid_ = Guid('{2a03c10e-9a19-4a01-994f-12dfad6adcbf}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Capabilities(self) -> Windows.Devices.PointOfService.PosPrinterCapabilities: ...
    @winrt_commethod(8)
    def get_SupportedCharacterSets(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(9)
    def get_SupportedTypeFaces(self) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def get_Status(self) -> Windows.Devices.PointOfService.PosPrinterStatus: ...
    @winrt_commethod(11)
    def ClaimPrinterAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.ClaimedPosPrinter]: ...
    @winrt_commethod(12)
    def CheckHealthAsync(self, level: Windows.Devices.PointOfService.UnifiedPosHealthCheckLevel) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(13)
    def GetStatisticsAsync(self, statisticsCategories: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(14)
    def add_StatusUpdated(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.PosPrinter, Windows.Devices.PointOfService.PosPrinterStatusUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_StatusUpdated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DeviceId = property(get_DeviceId, None)
    Capabilities = property(get_Capabilities, None)
    SupportedCharacterSets = property(get_SupportedCharacterSets, None)
    SupportedTypeFaces = property(get_SupportedTypeFaces, None)
    Status = property(get_Status, None)
class IPosPrinter2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IPosPrinter2'
    _iid_ = Guid('{248475e8-8b98-5517-8e48-760e86f68987}')
    @winrt_commethod(6)
    def get_SupportedBarcodeSymbologies(self) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_commethod(7)
    def GetFontProperty(self, typeface: WinRT_String) -> Windows.Devices.PointOfService.PosPrinterFontProperty: ...
    SupportedBarcodeSymbologies = property(get_SupportedBarcodeSymbologies, None)
class IPosPrinterCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IPosPrinterCapabilities'
    _iid_ = Guid('{cde95721-4380-4985-adc5-39db30cd93bc}')
    @winrt_commethod(6)
    def get_PowerReportingType(self) -> Windows.Devices.PointOfService.UnifiedPosPowerReportingType: ...
    @winrt_commethod(7)
    def get_IsStatisticsReportingSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsStatisticsUpdatingSupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_DefaultCharacterSet(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_HasCoverSensor(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_CanMapCharacterSet(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsTransactionSupported(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_Receipt(self) -> Windows.Devices.PointOfService.ReceiptPrinterCapabilities: ...
    @winrt_commethod(14)
    def get_Slip(self) -> Windows.Devices.PointOfService.SlipPrinterCapabilities: ...
    @winrt_commethod(15)
    def get_Journal(self) -> Windows.Devices.PointOfService.JournalPrinterCapabilities: ...
    PowerReportingType = property(get_PowerReportingType, None)
    IsStatisticsReportingSupported = property(get_IsStatisticsReportingSupported, None)
    IsStatisticsUpdatingSupported = property(get_IsStatisticsUpdatingSupported, None)
    DefaultCharacterSet = property(get_DefaultCharacterSet, None)
    HasCoverSensor = property(get_HasCoverSensor, None)
    CanMapCharacterSet = property(get_CanMapCharacterSet, None)
    IsTransactionSupported = property(get_IsTransactionSupported, None)
    Receipt = property(get_Receipt, None)
    Slip = property(get_Slip, None)
    Journal = property(get_Journal, None)
class IPosPrinterCharacterSetIdsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IPosPrinterCharacterSetIdsStatics'
    _iid_ = Guid('{5c709eff-709a-4fe7-b215-06a748a38b39}')
    @winrt_commethod(6)
    def get_Utf16LE(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Ascii(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Ansi(self) -> UInt32: ...
    Utf16LE = property(get_Utf16LE, None)
    Ascii = property(get_Ascii, None)
    Ansi = property(get_Ansi, None)
class IPosPrinterFontProperty(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IPosPrinterFontProperty'
    _iid_ = Guid('{a7f4e93a-f8ac-5f04-84d2-29b16d8a633c}')
    @winrt_commethod(6)
    def get_TypeFace(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsScalableToAnySize(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_CharacterSizes(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.PointOfService.SizeUInt32]: ...
    TypeFace = property(get_TypeFace, None)
    IsScalableToAnySize = property(get_IsScalableToAnySize, None)
    CharacterSizes = property(get_CharacterSizes, None)
class IPosPrinterJob(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IPosPrinterJob'
    _iid_ = Guid('{9a94005c-0615-4591-a58f-30f87edfe2e4}')
    @winrt_commethod(6)
    def Print(self, data: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def PrintLine(self, data: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def PrintNewline(self) -> Void: ...
    @winrt_commethod(9)
    def ExecuteAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IPosPrinterPrintOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IPosPrinterPrintOptions'
    _iid_ = Guid('{0a2e16fd-1d02-5a58-9d59-bfcde76fde86}')
    @winrt_commethod(6)
    def get_TypeFace(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_TypeFace(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_CharacterHeight(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_CharacterHeight(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_Bold(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_Bold(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_Italic(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_Italic(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_Underline(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_Underline(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_ReverseVideo(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_ReverseVideo(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_Strikethrough(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_Strikethrough(self, value: Boolean) -> Void: ...
    @winrt_commethod(20)
    def get_Superscript(self) -> Boolean: ...
    @winrt_commethod(21)
    def put_Superscript(self, value: Boolean) -> Void: ...
    @winrt_commethod(22)
    def get_Subscript(self) -> Boolean: ...
    @winrt_commethod(23)
    def put_Subscript(self, value: Boolean) -> Void: ...
    @winrt_commethod(24)
    def get_DoubleWide(self) -> Boolean: ...
    @winrt_commethod(25)
    def put_DoubleWide(self, value: Boolean) -> Void: ...
    @winrt_commethod(26)
    def get_DoubleHigh(self) -> Boolean: ...
    @winrt_commethod(27)
    def put_DoubleHigh(self, value: Boolean) -> Void: ...
    @winrt_commethod(28)
    def get_Alignment(self) -> Windows.Devices.PointOfService.PosPrinterAlignment: ...
    @winrt_commethod(29)
    def put_Alignment(self, value: Windows.Devices.PointOfService.PosPrinterAlignment) -> Void: ...
    @winrt_commethod(30)
    def get_CharacterSet(self) -> UInt32: ...
    @winrt_commethod(31)
    def put_CharacterSet(self, value: UInt32) -> Void: ...
    TypeFace = property(get_TypeFace, put_TypeFace)
    CharacterHeight = property(get_CharacterHeight, put_CharacterHeight)
    Bold = property(get_Bold, put_Bold)
    Italic = property(get_Italic, put_Italic)
    Underline = property(get_Underline, put_Underline)
    ReverseVideo = property(get_ReverseVideo, put_ReverseVideo)
    Strikethrough = property(get_Strikethrough, put_Strikethrough)
    Superscript = property(get_Superscript, put_Superscript)
    Subscript = property(get_Subscript, put_Subscript)
    DoubleWide = property(get_DoubleWide, put_DoubleWide)
    DoubleHigh = property(get_DoubleHigh, put_DoubleHigh)
    Alignment = property(get_Alignment, put_Alignment)
    CharacterSet = property(get_CharacterSet, put_CharacterSet)
class IPosPrinterReleaseDeviceRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IPosPrinterReleaseDeviceRequestedEventArgs'
    _iid_ = Guid('{2bcba359-1cef-40b2-9ecb-f927f856ae3c}')
class IPosPrinterStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IPosPrinterStatics'
    _iid_ = Guid('{8ce0d4ea-132f-4cdf-a64a-2d0d7c96a85b}')
    @winrt_commethod(6)
    def GetDefaultAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.PosPrinter]: ...
    @winrt_commethod(7)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.PosPrinter]: ...
    @winrt_commethod(8)
    def GetDeviceSelector(self) -> WinRT_String: ...
class IPosPrinterStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IPosPrinterStatics2'
    _iid_ = Guid('{eecd2c1c-b0d0-42e7-b137-b89b16244d41}')
    @winrt_commethod(6)
    def GetDeviceSelectorWithConnectionTypes(self, connectionTypes: Windows.Devices.PointOfService.PosConnectionTypes) -> WinRT_String: ...
class IPosPrinterStatus(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IPosPrinterStatus'
    _iid_ = Guid('{d1f0c730-da40-4328-bf76-5156fa33b747}')
    @winrt_commethod(6)
    def get_StatusKind(self) -> Windows.Devices.PointOfService.PosPrinterStatusKind: ...
    @winrt_commethod(7)
    def get_ExtendedStatus(self) -> UInt32: ...
    StatusKind = property(get_StatusKind, None)
    ExtendedStatus = property(get_ExtendedStatus, None)
class IPosPrinterStatusUpdatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IPosPrinterStatusUpdatedEventArgs'
    _iid_ = Guid('{2edb87df-13a6-428d-ba81-b0e7c3e5a3cd}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.PointOfService.PosPrinterStatus: ...
    Status = property(get_Status, None)
class IReceiptOrSlipJob(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IReceiptOrSlipJob'
    _iid_ = Guid('{532199be-c8c3-4dc2-89e9-5c4a37b34ddc}')
    @winrt_commethod(6)
    def SetBarcodeRotation(self, value: Windows.Devices.PointOfService.PosPrinterRotation) -> Void: ...
    @winrt_commethod(7)
    def SetPrintRotation(self, value: Windows.Devices.PointOfService.PosPrinterRotation, includeBitmaps: Boolean) -> Void: ...
    @winrt_commethod(8)
    def SetPrintArea(self, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(9)
    def SetBitmap(self, bitmapNumber: UInt32, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignment: Windows.Devices.PointOfService.PosPrinterAlignment) -> Void: ...
    @winrt_commethod(10)
    def SetBitmapCustomWidthStandardAlign(self, bitmapNumber: UInt32, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignment: Windows.Devices.PointOfService.PosPrinterAlignment, width: UInt32) -> Void: ...
    @winrt_commethod(11)
    def SetCustomAlignedBitmap(self, bitmapNumber: UInt32, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignmentDistance: UInt32) -> Void: ...
    @winrt_commethod(12)
    def SetBitmapCustomWidthCustomAlign(self, bitmapNumber: UInt32, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignmentDistance: UInt32, width: UInt32) -> Void: ...
    @winrt_commethod(13)
    def PrintSavedBitmap(self, bitmapNumber: UInt32) -> Void: ...
    @winrt_commethod(14)
    def DrawRuledLine(self, positionList: WinRT_String, lineDirection: Windows.Devices.PointOfService.PosPrinterLineDirection, lineWidth: UInt32, lineStyle: Windows.Devices.PointOfService.PosPrinterLineStyle, lineColor: UInt32) -> Void: ...
    @winrt_commethod(15)
    def PrintBarcode(self, data: WinRT_String, symbology: UInt32, height: UInt32, width: UInt32, textPosition: Windows.Devices.PointOfService.PosPrinterBarcodeTextPosition, alignment: Windows.Devices.PointOfService.PosPrinterAlignment) -> Void: ...
    @winrt_commethod(16)
    def PrintBarcodeCustomAlign(self, data: WinRT_String, symbology: UInt32, height: UInt32, width: UInt32, textPosition: Windows.Devices.PointOfService.PosPrinterBarcodeTextPosition, alignmentDistance: UInt32) -> Void: ...
    @winrt_commethod(17)
    def PrintBitmap(self, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignment: Windows.Devices.PointOfService.PosPrinterAlignment) -> Void: ...
    @winrt_commethod(18)
    def PrintBitmapCustomWidthStandardAlign(self, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignment: Windows.Devices.PointOfService.PosPrinterAlignment, width: UInt32) -> Void: ...
    @winrt_commethod(19)
    def PrintCustomAlignedBitmap(self, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignmentDistance: UInt32) -> Void: ...
    @winrt_commethod(20)
    def PrintBitmapCustomWidthCustomAlign(self, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignmentDistance: UInt32, width: UInt32) -> Void: ...
class IReceiptPrintJob(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IReceiptPrintJob'
    _iid_ = Guid('{aa96066e-acad-4b79-9d0f-c0cfc08dc77b}')
    @winrt_commethod(6)
    def MarkFeed(self, kind: Windows.Devices.PointOfService.PosPrinterMarkFeedKind) -> Void: ...
    @winrt_commethod(7)
    def CutPaper(self, percentage: Double) -> Void: ...
    @winrt_commethod(8)
    def CutPaperDefault(self) -> Void: ...
class IReceiptPrintJob2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IReceiptPrintJob2'
    _iid_ = Guid('{0cbc12e3-9e29-5179-bcd8-1811d3b9a10e}')
    @winrt_commethod(6)
    def StampPaper(self) -> Void: ...
    @winrt_commethod(7)
    def Print(self, data: WinRT_String, printOptions: Windows.Devices.PointOfService.PosPrinterPrintOptions) -> Void: ...
    @winrt_commethod(8)
    def FeedPaperByLine(self, lineCount: Int32) -> Void: ...
    @winrt_commethod(9)
    def FeedPaperByMapModeUnit(self, distance: Int32) -> Void: ...
class IReceiptPrinterCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IReceiptPrinterCapabilities'
    _iid_ = Guid('{b8f0b58f-51a8-43fc-9bd5-8de272a6415b}')
    @winrt_commethod(6)
    def get_CanCutPaper(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsStampSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_MarkFeedCapabilities(self) -> Windows.Devices.PointOfService.PosPrinterMarkFeedCapabilities: ...
    CanCutPaper = property(get_CanCutPaper, None)
    IsStampSupported = property(get_IsStampSupported, None)
    MarkFeedCapabilities = property(get_MarkFeedCapabilities, None)
class IReceiptPrinterCapabilities2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IReceiptPrinterCapabilities2'
    _iid_ = Guid('{20030638-8a2c-55ac-9a7b-7576d8869e99}')
    @winrt_commethod(6)
    def get_IsReverseVideoSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsStrikethroughSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsSuperscriptSupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsSubscriptSupported(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsReversePaperFeedByLineSupported(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsReversePaperFeedByMapModeUnitSupported(self) -> Boolean: ...
    IsReverseVideoSupported = property(get_IsReverseVideoSupported, None)
    IsStrikethroughSupported = property(get_IsStrikethroughSupported, None)
    IsSuperscriptSupported = property(get_IsSuperscriptSupported, None)
    IsSubscriptSupported = property(get_IsSubscriptSupported, None)
    IsReversePaperFeedByLineSupported = property(get_IsReversePaperFeedByLineSupported, None)
    IsReversePaperFeedByMapModeUnitSupported = property(get_IsReversePaperFeedByMapModeUnitSupported, None)
class ISlipPrintJob(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ISlipPrintJob'
    _iid_ = Guid('{5d88f95d-6131-5a4b-b7d5-8ef2da7b4165}')
    @winrt_commethod(6)
    def Print(self, data: WinRT_String, printOptions: Windows.Devices.PointOfService.PosPrinterPrintOptions) -> Void: ...
    @winrt_commethod(7)
    def FeedPaperByLine(self, lineCount: Int32) -> Void: ...
    @winrt_commethod(8)
    def FeedPaperByMapModeUnit(self, distance: Int32) -> Void: ...
class ISlipPrinterCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ISlipPrinterCapabilities'
    _iid_ = Guid('{99b16399-488c-4157-8ac2-9f57f708d3db}')
    @winrt_commethod(6)
    def get_IsFullLengthSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsBothSidesPrintingSupported(self) -> Boolean: ...
    IsFullLengthSupported = property(get_IsFullLengthSupported, None)
    IsBothSidesPrintingSupported = property(get_IsBothSidesPrintingSupported, None)
class ISlipPrinterCapabilities2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.ISlipPrinterCapabilities2'
    _iid_ = Guid('{6ff89671-2d1a-5000-87c2-b0851bfdf07e}')
    @winrt_commethod(6)
    def get_IsReverseVideoSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsStrikethroughSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsSuperscriptSupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsSubscriptSupported(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsReversePaperFeedByLineSupported(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsReversePaperFeedByMapModeUnitSupported(self) -> Boolean: ...
    IsReverseVideoSupported = property(get_IsReverseVideoSupported, None)
    IsStrikethroughSupported = property(get_IsStrikethroughSupported, None)
    IsSuperscriptSupported = property(get_IsSuperscriptSupported, None)
    IsSubscriptSupported = property(get_IsSubscriptSupported, None)
    IsReversePaperFeedByLineSupported = property(get_IsReversePaperFeedByLineSupported, None)
    IsReversePaperFeedByMapModeUnitSupported = property(get_IsReversePaperFeedByMapModeUnitSupported, None)
class IUnifiedPosErrorData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IUnifiedPosErrorData'
    _iid_ = Guid('{2b998c3a-555c-4889-8ed8-c599bb3a712a}')
    @winrt_commethod(6)
    def get_Message(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Severity(self) -> Windows.Devices.PointOfService.UnifiedPosErrorSeverity: ...
    @winrt_commethod(8)
    def get_Reason(self) -> Windows.Devices.PointOfService.UnifiedPosErrorReason: ...
    @winrt_commethod(9)
    def get_ExtendedReason(self) -> UInt32: ...
    Message = property(get_Message, None)
    Severity = property(get_Severity, None)
    Reason = property(get_Reason, None)
    ExtendedReason = property(get_ExtendedReason, None)
class IUnifiedPosErrorDataFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.IUnifiedPosErrorDataFactory'
    _iid_ = Guid('{4b982551-1ffe-451b-a368-63e0ce465f5a}')
    @winrt_commethod(6)
    def CreateInstance(self, message: WinRT_String, severity: Windows.Devices.PointOfService.UnifiedPosErrorSeverity, reason: Windows.Devices.PointOfService.UnifiedPosErrorReason, extendedReason: UInt32) -> Windows.Devices.PointOfService.UnifiedPosErrorData: ...
class JournalPrintJob(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IPosPrinterJob
    _classid_ = 'Windows.Devices.PointOfService.JournalPrintJob'
    @winrt_mixinmethod
    def Print(self: Windows.Devices.PointOfService.IPosPrinterJob, data: WinRT_String, printOptions: Windows.Devices.PointOfService.PosPrinterPrintOptions) -> Void: ...
    @winrt_mixinmethod
    def FeedPaperByLine(self: Windows.Devices.PointOfService.IJournalPrintJob, lineCount: Int32) -> Void: ...
    @winrt_mixinmethod
    def FeedPaperByMapModeUnit(self: Windows.Devices.PointOfService.IJournalPrintJob, distance: Int32) -> Void: ...
    @winrt_mixinmethod
    def Print(self: Windows.Devices.PointOfService.IPosPrinterJob, data: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def PrintLine(self: Windows.Devices.PointOfService.IPosPrinterJob, data: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def PrintNewline(self: Windows.Devices.PointOfService.IPosPrinterJob) -> Void: ...
    @winrt_mixinmethod
    def ExecuteAsync(self: Windows.Devices.PointOfService.IPosPrinterJob) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class JournalPrinterCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IJournalPrinterCapabilities
    _classid_ = 'Windows.Devices.PointOfService.JournalPrinterCapabilities'
    @winrt_mixinmethod
    def get_IsReverseVideoSupported(self: Windows.Devices.PointOfService.IJournalPrinterCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsStrikethroughSupported(self: Windows.Devices.PointOfService.IJournalPrinterCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSuperscriptSupported(self: Windows.Devices.PointOfService.IJournalPrinterCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSubscriptSupported(self: Windows.Devices.PointOfService.IJournalPrinterCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsReversePaperFeedByLineSupported(self: Windows.Devices.PointOfService.IJournalPrinterCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsReversePaperFeedByMapModeUnitSupported(self: Windows.Devices.PointOfService.IJournalPrinterCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPrinterPresent(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDualColorSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_ColorCartridgeCapabilities(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Windows.Devices.PointOfService.PosPrinterColorCapabilities: ...
    @winrt_mixinmethod
    def get_CartridgeSensors(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Windows.Devices.PointOfService.PosPrinterCartridgeSensors: ...
    @winrt_mixinmethod
    def get_IsBoldSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsItalicSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsUnderlineSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDoubleHighPrintSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDoubleWidePrintSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDoubleHighDoubleWidePrintSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPaperEmptySensorSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPaperNearEndSensorSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedCharactersPerLine(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    IsReverseVideoSupported = property(get_IsReverseVideoSupported, None)
    IsStrikethroughSupported = property(get_IsStrikethroughSupported, None)
    IsSuperscriptSupported = property(get_IsSuperscriptSupported, None)
    IsSubscriptSupported = property(get_IsSubscriptSupported, None)
    IsReversePaperFeedByLineSupported = property(get_IsReversePaperFeedByLineSupported, None)
    IsReversePaperFeedByMapModeUnitSupported = property(get_IsReversePaperFeedByMapModeUnitSupported, None)
    IsPrinterPresent = property(get_IsPrinterPresent, None)
    IsDualColorSupported = property(get_IsDualColorSupported, None)
    ColorCartridgeCapabilities = property(get_ColorCartridgeCapabilities, None)
    CartridgeSensors = property(get_CartridgeSensors, None)
    IsBoldSupported = property(get_IsBoldSupported, None)
    IsItalicSupported = property(get_IsItalicSupported, None)
    IsUnderlineSupported = property(get_IsUnderlineSupported, None)
    IsDoubleHighPrintSupported = property(get_IsDoubleHighPrintSupported, None)
    IsDoubleWidePrintSupported = property(get_IsDoubleWidePrintSupported, None)
    IsDoubleHighDoubleWidePrintSupported = property(get_IsDoubleHighDoubleWidePrintSupported, None)
    IsPaperEmptySensorSupported = property(get_IsPaperEmptySensorSupported, None)
    IsPaperNearEndSensorSupported = property(get_IsPaperNearEndSensorSupported, None)
    SupportedCharactersPerLine = property(get_SupportedCharactersPerLine, None)
class LineDisplay(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ILineDisplay
    _classid_ = 'Windows.Devices.PointOfService.LineDisplay'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.PointOfService.ILineDisplay) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Capabilities(self: Windows.Devices.PointOfService.ILineDisplay) -> Windows.Devices.PointOfService.LineDisplayCapabilities: ...
    @winrt_mixinmethod
    def get_PhysicalDeviceName(self: Windows.Devices.PointOfService.ILineDisplay) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PhysicalDeviceDescription(self: Windows.Devices.PointOfService.ILineDisplay) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceControlDescription(self: Windows.Devices.PointOfService.ILineDisplay) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceControlVersion(self: Windows.Devices.PointOfService.ILineDisplay) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DeviceServiceVersion(self: Windows.Devices.PointOfService.ILineDisplay) -> WinRT_String: ...
    @winrt_mixinmethod
    def ClaimAsync(self: Windows.Devices.PointOfService.ILineDisplay) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.ClaimedLineDisplay]: ...
    @winrt_mixinmethod
    def CheckPowerStatusAsync(self: Windows.Devices.PointOfService.ILineDisplay2) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.LineDisplayPowerStatus]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def get_StatisticsCategorySelector(cls: Windows.Devices.PointOfService.ILineDisplayStatics2) -> Windows.Devices.PointOfService.LineDisplayStatisticsCategorySelector: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.PointOfService.ILineDisplayStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.LineDisplay]: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.PointOfService.ILineDisplayStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.LineDisplay]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.PointOfService.ILineDisplayStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetDeviceSelectorWithConnectionTypes(cls: Windows.Devices.PointOfService.ILineDisplayStatics, connectionTypes: Windows.Devices.PointOfService.PosConnectionTypes) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    Capabilities = property(get_Capabilities, None)
    PhysicalDeviceName = property(get_PhysicalDeviceName, None)
    PhysicalDeviceDescription = property(get_PhysicalDeviceDescription, None)
    DeviceControlDescription = property(get_DeviceControlDescription, None)
    DeviceControlVersion = property(get_DeviceControlVersion, None)
    DeviceServiceVersion = property(get_DeviceServiceVersion, None)
    StatisticsCategorySelector = property(get_StatisticsCategorySelector, None)
class LineDisplayAttributes(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ILineDisplayAttributes
    _classid_ = 'Windows.Devices.PointOfService.LineDisplayAttributes'
    @winrt_mixinmethod
    def get_IsPowerNotifyEnabled(self: Windows.Devices.PointOfService.ILineDisplayAttributes) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPowerNotifyEnabled(self: Windows.Devices.PointOfService.ILineDisplayAttributes, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Brightness(self: Windows.Devices.PointOfService.ILineDisplayAttributes) -> Int32: ...
    @winrt_mixinmethod
    def put_Brightness(self: Windows.Devices.PointOfService.ILineDisplayAttributes, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_BlinkRate(self: Windows.Devices.PointOfService.ILineDisplayAttributes) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_BlinkRate(self: Windows.Devices.PointOfService.ILineDisplayAttributes, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_ScreenSizeInCharacters(self: Windows.Devices.PointOfService.ILineDisplayAttributes) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def put_ScreenSizeInCharacters(self: Windows.Devices.PointOfService.ILineDisplayAttributes, value: Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def get_CharacterSet(self: Windows.Devices.PointOfService.ILineDisplayAttributes) -> Int32: ...
    @winrt_mixinmethod
    def put_CharacterSet(self: Windows.Devices.PointOfService.ILineDisplayAttributes, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_IsCharacterSetMappingEnabled(self: Windows.Devices.PointOfService.ILineDisplayAttributes) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCharacterSetMappingEnabled(self: Windows.Devices.PointOfService.ILineDisplayAttributes, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CurrentWindow(self: Windows.Devices.PointOfService.ILineDisplayAttributes) -> Windows.Devices.PointOfService.LineDisplayWindow: ...
    @winrt_mixinmethod
    def put_CurrentWindow(self: Windows.Devices.PointOfService.ILineDisplayAttributes, value: Windows.Devices.PointOfService.LineDisplayWindow) -> Void: ...
    IsPowerNotifyEnabled = property(get_IsPowerNotifyEnabled, put_IsPowerNotifyEnabled)
    Brightness = property(get_Brightness, put_Brightness)
    BlinkRate = property(get_BlinkRate, put_BlinkRate)
    ScreenSizeInCharacters = property(get_ScreenSizeInCharacters, put_ScreenSizeInCharacters)
    CharacterSet = property(get_CharacterSet, put_CharacterSet)
    IsCharacterSetMappingEnabled = property(get_IsCharacterSetMappingEnabled, put_IsCharacterSetMappingEnabled)
    CurrentWindow = property(get_CurrentWindow, put_CurrentWindow)
class LineDisplayCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ILineDisplayCapabilities
    _classid_ = 'Windows.Devices.PointOfService.LineDisplayCapabilities'
    @winrt_mixinmethod
    def get_IsStatisticsReportingSupported(self: Windows.Devices.PointOfService.ILineDisplayCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsStatisticsUpdatingSupported(self: Windows.Devices.PointOfService.ILineDisplayCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_PowerReportingType(self: Windows.Devices.PointOfService.ILineDisplayCapabilities) -> Windows.Devices.PointOfService.UnifiedPosPowerReportingType: ...
    @winrt_mixinmethod
    def get_CanChangeScreenSize(self: Windows.Devices.PointOfService.ILineDisplayCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanDisplayBitmaps(self: Windows.Devices.PointOfService.ILineDisplayCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanReadCharacterAtCursor(self: Windows.Devices.PointOfService.ILineDisplayCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanMapCharacterSets(self: Windows.Devices.PointOfService.ILineDisplayCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanDisplayCustomGlyphs(self: Windows.Devices.PointOfService.ILineDisplayCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanReverse(self: Windows.Devices.PointOfService.ILineDisplayCapabilities) -> Windows.Devices.PointOfService.LineDisplayTextAttributeGranularity: ...
    @winrt_mixinmethod
    def get_CanBlink(self: Windows.Devices.PointOfService.ILineDisplayCapabilities) -> Windows.Devices.PointOfService.LineDisplayTextAttributeGranularity: ...
    @winrt_mixinmethod
    def get_CanChangeBlinkRate(self: Windows.Devices.PointOfService.ILineDisplayCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBrightnessSupported(self: Windows.Devices.PointOfService.ILineDisplayCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCursorSupported(self: Windows.Devices.PointOfService.ILineDisplayCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsHorizontalMarqueeSupported(self: Windows.Devices.PointOfService.ILineDisplayCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsVerticalMarqueeSupported(self: Windows.Devices.PointOfService.ILineDisplayCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsInterCharacterWaitSupported(self: Windows.Devices.PointOfService.ILineDisplayCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedDescriptors(self: Windows.Devices.PointOfService.ILineDisplayCapabilities) -> UInt32: ...
    @winrt_mixinmethod
    def get_SupportedWindows(self: Windows.Devices.PointOfService.ILineDisplayCapabilities) -> UInt32: ...
    IsStatisticsReportingSupported = property(get_IsStatisticsReportingSupported, None)
    IsStatisticsUpdatingSupported = property(get_IsStatisticsUpdatingSupported, None)
    PowerReportingType = property(get_PowerReportingType, None)
    CanChangeScreenSize = property(get_CanChangeScreenSize, None)
    CanDisplayBitmaps = property(get_CanDisplayBitmaps, None)
    CanReadCharacterAtCursor = property(get_CanReadCharacterAtCursor, None)
    CanMapCharacterSets = property(get_CanMapCharacterSets, None)
    CanDisplayCustomGlyphs = property(get_CanDisplayCustomGlyphs, None)
    CanReverse = property(get_CanReverse, None)
    CanBlink = property(get_CanBlink, None)
    CanChangeBlinkRate = property(get_CanChangeBlinkRate, None)
    IsBrightnessSupported = property(get_IsBrightnessSupported, None)
    IsCursorSupported = property(get_IsCursorSupported, None)
    IsHorizontalMarqueeSupported = property(get_IsHorizontalMarqueeSupported, None)
    IsVerticalMarqueeSupported = property(get_IsVerticalMarqueeSupported, None)
    IsInterCharacterWaitSupported = property(get_IsInterCharacterWaitSupported, None)
    SupportedDescriptors = property(get_SupportedDescriptors, None)
    SupportedWindows = property(get_SupportedWindows, None)
class LineDisplayCursor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ILineDisplayCursor
    _classid_ = 'Windows.Devices.PointOfService.LineDisplayCursor'
    @winrt_mixinmethod
    def get_CanCustomize(self: Windows.Devices.PointOfService.ILineDisplayCursor) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBlinkSupported(self: Windows.Devices.PointOfService.ILineDisplayCursor) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBlockSupported(self: Windows.Devices.PointOfService.ILineDisplayCursor) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsHalfBlockSupported(self: Windows.Devices.PointOfService.ILineDisplayCursor) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsUnderlineSupported(self: Windows.Devices.PointOfService.ILineDisplayCursor) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsReverseSupported(self: Windows.Devices.PointOfService.ILineDisplayCursor) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsOtherSupported(self: Windows.Devices.PointOfService.ILineDisplayCursor) -> Boolean: ...
    @winrt_mixinmethod
    def GetAttributes(self: Windows.Devices.PointOfService.ILineDisplayCursor) -> Windows.Devices.PointOfService.LineDisplayCursorAttributes: ...
    @winrt_mixinmethod
    def TryUpdateAttributesAsync(self: Windows.Devices.PointOfService.ILineDisplayCursor, attributes: Windows.Devices.PointOfService.LineDisplayCursorAttributes) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    CanCustomize = property(get_CanCustomize, None)
    IsBlinkSupported = property(get_IsBlinkSupported, None)
    IsBlockSupported = property(get_IsBlockSupported, None)
    IsHalfBlockSupported = property(get_IsHalfBlockSupported, None)
    IsUnderlineSupported = property(get_IsUnderlineSupported, None)
    IsReverseSupported = property(get_IsReverseSupported, None)
    IsOtherSupported = property(get_IsOtherSupported, None)
class LineDisplayCursorAttributes(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ILineDisplayCursorAttributes
    _classid_ = 'Windows.Devices.PointOfService.LineDisplayCursorAttributes'
    @winrt_mixinmethod
    def get_IsBlinkEnabled(self: Windows.Devices.PointOfService.ILineDisplayCursorAttributes) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsBlinkEnabled(self: Windows.Devices.PointOfService.ILineDisplayCursorAttributes, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CursorType(self: Windows.Devices.PointOfService.ILineDisplayCursorAttributes) -> Windows.Devices.PointOfService.LineDisplayCursorType: ...
    @winrt_mixinmethod
    def put_CursorType(self: Windows.Devices.PointOfService.ILineDisplayCursorAttributes, value: Windows.Devices.PointOfService.LineDisplayCursorType) -> Void: ...
    @winrt_mixinmethod
    def get_IsAutoAdvanceEnabled(self: Windows.Devices.PointOfService.ILineDisplayCursorAttributes) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAutoAdvanceEnabled(self: Windows.Devices.PointOfService.ILineDisplayCursorAttributes, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.Devices.PointOfService.ILineDisplayCursorAttributes) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Position(self: Windows.Devices.PointOfService.ILineDisplayCursorAttributes, value: Windows.Foundation.Point) -> Void: ...
    IsBlinkEnabled = property(get_IsBlinkEnabled, put_IsBlinkEnabled)
    CursorType = property(get_CursorType, put_CursorType)
    IsAutoAdvanceEnabled = property(get_IsAutoAdvanceEnabled, put_IsAutoAdvanceEnabled)
    Position = property(get_Position, put_Position)
LineDisplayCursorType = Int32
LineDisplayCursorType_None: LineDisplayCursorType = 0
LineDisplayCursorType_Block: LineDisplayCursorType = 1
LineDisplayCursorType_HalfBlock: LineDisplayCursorType = 2
LineDisplayCursorType_Underline: LineDisplayCursorType = 3
LineDisplayCursorType_Reverse: LineDisplayCursorType = 4
LineDisplayCursorType_Other: LineDisplayCursorType = 5
class LineDisplayCustomGlyphs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ILineDisplayCustomGlyphs
    _classid_ = 'Windows.Devices.PointOfService.LineDisplayCustomGlyphs'
    @winrt_mixinmethod
    def get_SizeInPixels(self: Windows.Devices.PointOfService.ILineDisplayCustomGlyphs) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_SupportedGlyphCodes(self: Windows.Devices.PointOfService.ILineDisplayCustomGlyphs) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_mixinmethod
    def TryRedefineAsync(self: Windows.Devices.PointOfService.ILineDisplayCustomGlyphs, glyphCode: UInt32, glyphData: Windows.Storage.Streams.IBuffer) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    SizeInPixels = property(get_SizeInPixels, None)
    SupportedGlyphCodes = property(get_SupportedGlyphCodes, None)
LineDisplayDescriptorState = Int32
LineDisplayDescriptorState_Off: LineDisplayDescriptorState = 0
LineDisplayDescriptorState_On: LineDisplayDescriptorState = 1
LineDisplayDescriptorState_Blink: LineDisplayDescriptorState = 2
LineDisplayHorizontalAlignment = Int32
LineDisplayHorizontalAlignment_Left: LineDisplayHorizontalAlignment = 0
LineDisplayHorizontalAlignment_Center: LineDisplayHorizontalAlignment = 1
LineDisplayHorizontalAlignment_Right: LineDisplayHorizontalAlignment = 2
class LineDisplayMarquee(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ILineDisplayMarquee
    _classid_ = 'Windows.Devices.PointOfService.LineDisplayMarquee'
    @winrt_mixinmethod
    def get_Format(self: Windows.Devices.PointOfService.ILineDisplayMarquee) -> Windows.Devices.PointOfService.LineDisplayMarqueeFormat: ...
    @winrt_mixinmethod
    def put_Format(self: Windows.Devices.PointOfService.ILineDisplayMarquee, value: Windows.Devices.PointOfService.LineDisplayMarqueeFormat) -> Void: ...
    @winrt_mixinmethod
    def get_RepeatWaitInterval(self: Windows.Devices.PointOfService.ILineDisplayMarquee) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_RepeatWaitInterval(self: Windows.Devices.PointOfService.ILineDisplayMarquee, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_ScrollWaitInterval(self: Windows.Devices.PointOfService.ILineDisplayMarquee) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_ScrollWaitInterval(self: Windows.Devices.PointOfService.ILineDisplayMarquee, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def TryStartScrollingAsync(self: Windows.Devices.PointOfService.ILineDisplayMarquee, direction: Windows.Devices.PointOfService.LineDisplayScrollDirection) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryStopScrollingAsync(self: Windows.Devices.PointOfService.ILineDisplayMarquee) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    Format = property(get_Format, put_Format)
    RepeatWaitInterval = property(get_RepeatWaitInterval, put_RepeatWaitInterval)
    ScrollWaitInterval = property(get_ScrollWaitInterval, put_ScrollWaitInterval)
LineDisplayMarqueeFormat = Int32
LineDisplayMarqueeFormat_None: LineDisplayMarqueeFormat = 0
LineDisplayMarqueeFormat_Walk: LineDisplayMarqueeFormat = 1
LineDisplayMarqueeFormat_Place: LineDisplayMarqueeFormat = 2
LineDisplayPowerStatus = Int32
LineDisplayPowerStatus_Unknown: LineDisplayPowerStatus = 0
LineDisplayPowerStatus_Online: LineDisplayPowerStatus = 1
LineDisplayPowerStatus_Off: LineDisplayPowerStatus = 2
LineDisplayPowerStatus_Offline: LineDisplayPowerStatus = 3
LineDisplayPowerStatus_OffOrOffline: LineDisplayPowerStatus = 4
LineDisplayScrollDirection = Int32
LineDisplayScrollDirection_Up: LineDisplayScrollDirection = 0
LineDisplayScrollDirection_Down: LineDisplayScrollDirection = 1
LineDisplayScrollDirection_Left: LineDisplayScrollDirection = 2
LineDisplayScrollDirection_Right: LineDisplayScrollDirection = 3
class LineDisplayStatisticsCategorySelector(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ILineDisplayStatisticsCategorySelector
    _classid_ = 'Windows.Devices.PointOfService.LineDisplayStatisticsCategorySelector'
    @winrt_mixinmethod
    def get_AllStatistics(self: Windows.Devices.PointOfService.ILineDisplayStatisticsCategorySelector) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UnifiedPosStatistics(self: Windows.Devices.PointOfService.ILineDisplayStatisticsCategorySelector) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ManufacturerStatistics(self: Windows.Devices.PointOfService.ILineDisplayStatisticsCategorySelector) -> WinRT_String: ...
    AllStatistics = property(get_AllStatistics, None)
    UnifiedPosStatistics = property(get_UnifiedPosStatistics, None)
    ManufacturerStatistics = property(get_ManufacturerStatistics, None)
class LineDisplayStatusUpdatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ILineDisplayStatusUpdatedEventArgs
    _classid_ = 'Windows.Devices.PointOfService.LineDisplayStatusUpdatedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.PointOfService.ILineDisplayStatusUpdatedEventArgs) -> Windows.Devices.PointOfService.LineDisplayPowerStatus: ...
    Status = property(get_Status, None)
class LineDisplayStoredBitmap(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ILineDisplayStoredBitmap
    _classid_ = 'Windows.Devices.PointOfService.LineDisplayStoredBitmap'
    @winrt_mixinmethod
    def get_EscapeSequence(self: Windows.Devices.PointOfService.ILineDisplayStoredBitmap) -> WinRT_String: ...
    @winrt_mixinmethod
    def TryDeleteAsync(self: Windows.Devices.PointOfService.ILineDisplayStoredBitmap) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    EscapeSequence = property(get_EscapeSequence, None)
LineDisplayTextAttribute = Int32
LineDisplayTextAttribute_Normal: LineDisplayTextAttribute = 0
LineDisplayTextAttribute_Blink: LineDisplayTextAttribute = 1
LineDisplayTextAttribute_Reverse: LineDisplayTextAttribute = 2
LineDisplayTextAttribute_ReverseBlink: LineDisplayTextAttribute = 3
LineDisplayTextAttributeGranularity = Int32
LineDisplayTextAttributeGranularity_NotSupported: LineDisplayTextAttributeGranularity = 0
LineDisplayTextAttributeGranularity_EntireDisplay: LineDisplayTextAttributeGranularity = 1
LineDisplayTextAttributeGranularity_PerCharacter: LineDisplayTextAttributeGranularity = 2
LineDisplayVerticalAlignment = Int32
LineDisplayVerticalAlignment_Top: LineDisplayVerticalAlignment = 0
LineDisplayVerticalAlignment_Center: LineDisplayVerticalAlignment = 1
LineDisplayVerticalAlignment_Bottom: LineDisplayVerticalAlignment = 2
class LineDisplayWindow(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ILineDisplayWindow
    _classid_ = 'Windows.Devices.PointOfService.LineDisplayWindow'
    @winrt_mixinmethod
    def get_SizeInCharacters(self: Windows.Devices.PointOfService.ILineDisplayWindow) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_InterCharacterWaitInterval(self: Windows.Devices.PointOfService.ILineDisplayWindow) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_InterCharacterWaitInterval(self: Windows.Devices.PointOfService.ILineDisplayWindow, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def TryRefreshAsync(self: Windows.Devices.PointOfService.ILineDisplayWindow) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryDisplayTextAsync(self: Windows.Devices.PointOfService.ILineDisplayWindow, text: WinRT_String, displayAttribute: Windows.Devices.PointOfService.LineDisplayTextAttribute) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryDisplayTextAtPositionAsync(self: Windows.Devices.PointOfService.ILineDisplayWindow, text: WinRT_String, displayAttribute: Windows.Devices.PointOfService.LineDisplayTextAttribute, startPosition: Windows.Foundation.Point) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryDisplayTextNormalAsync(self: Windows.Devices.PointOfService.ILineDisplayWindow, text: WinRT_String) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryScrollTextAsync(self: Windows.Devices.PointOfService.ILineDisplayWindow, direction: Windows.Devices.PointOfService.LineDisplayScrollDirection, numberOfColumnsOrRows: UInt32) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryClearTextAsync(self: Windows.Devices.PointOfService.ILineDisplayWindow) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_Cursor(self: Windows.Devices.PointOfService.ILineDisplayWindow2) -> Windows.Devices.PointOfService.LineDisplayCursor: ...
    @winrt_mixinmethod
    def get_Marquee(self: Windows.Devices.PointOfService.ILineDisplayWindow2) -> Windows.Devices.PointOfService.LineDisplayMarquee: ...
    @winrt_mixinmethod
    def ReadCharacterAtCursorAsync(self: Windows.Devices.PointOfService.ILineDisplayWindow2) -> Windows.Foundation.IAsyncOperation[UInt32]: ...
    @winrt_mixinmethod
    def TryDisplayStoredBitmapAtCursorAsync(self: Windows.Devices.PointOfService.ILineDisplayWindow2, bitmap: Windows.Devices.PointOfService.LineDisplayStoredBitmap) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryDisplayStorageFileBitmapAtCursorAsync(self: Windows.Devices.PointOfService.ILineDisplayWindow2, bitmap: Windows.Storage.StorageFile) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryDisplayStorageFileBitmapAtCursorWithAlignmentAsync(self: Windows.Devices.PointOfService.ILineDisplayWindow2, bitmap: Windows.Storage.StorageFile, horizontalAlignment: Windows.Devices.PointOfService.LineDisplayHorizontalAlignment, verticalAlignment: Windows.Devices.PointOfService.LineDisplayVerticalAlignment) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryDisplayStorageFileBitmapAtCursorWithAlignmentAndWidthAsync(self: Windows.Devices.PointOfService.ILineDisplayWindow2, bitmap: Windows.Storage.StorageFile, horizontalAlignment: Windows.Devices.PointOfService.LineDisplayHorizontalAlignment, verticalAlignment: Windows.Devices.PointOfService.LineDisplayVerticalAlignment, widthInPixels: Int32) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryDisplayStorageFileBitmapAtPointAsync(self: Windows.Devices.PointOfService.ILineDisplayWindow2, bitmap: Windows.Storage.StorageFile, offsetInPixels: Windows.Foundation.Point) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def TryDisplayStorageFileBitmapAtPointWithWidthAsync(self: Windows.Devices.PointOfService.ILineDisplayWindow2, bitmap: Windows.Storage.StorageFile, offsetInPixels: Windows.Foundation.Point, widthInPixels: Int32) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    SizeInCharacters = property(get_SizeInCharacters, None)
    InterCharacterWaitInterval = property(get_InterCharacterWaitInterval, put_InterCharacterWaitInterval)
    Cursor = property(get_Cursor, None)
    Marquee = property(get_Marquee, None)
class MagneticStripeReader(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IMagneticStripeReader
    _classid_ = 'Windows.Devices.PointOfService.MagneticStripeReader'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.PointOfService.IMagneticStripeReader) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Capabilities(self: Windows.Devices.PointOfService.IMagneticStripeReader) -> Windows.Devices.PointOfService.MagneticStripeReaderCapabilities: ...
    @winrt_mixinmethod
    def get_SupportedCardTypes(self: Windows.Devices.PointOfService.IMagneticStripeReader) -> POINTER(UInt32): ...
    @winrt_mixinmethod
    def get_DeviceAuthenticationProtocol(self: Windows.Devices.PointOfService.IMagneticStripeReader) -> Windows.Devices.PointOfService.MagneticStripeReaderAuthenticationProtocol: ...
    @winrt_mixinmethod
    def CheckHealthAsync(self: Windows.Devices.PointOfService.IMagneticStripeReader, level: Windows.Devices.PointOfService.UnifiedPosHealthCheckLevel) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def ClaimReaderAsync(self: Windows.Devices.PointOfService.IMagneticStripeReader) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.ClaimedMagneticStripeReader]: ...
    @winrt_mixinmethod
    def RetrieveStatisticsAsync(self: Windows.Devices.PointOfService.IMagneticStripeReader, statisticsCategories: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IBuffer]: ...
    @winrt_mixinmethod
    def GetErrorReportingType(self: Windows.Devices.PointOfService.IMagneticStripeReader) -> Windows.Devices.PointOfService.MagneticStripeReaderErrorReportingType: ...
    @winrt_mixinmethod
    def add_StatusUpdated(self: Windows.Devices.PointOfService.IMagneticStripeReader, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.MagneticStripeReader, Windows.Devices.PointOfService.MagneticStripeReaderStatusUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusUpdated(self: Windows.Devices.PointOfService.IMagneticStripeReader, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelectorWithConnectionTypes(cls: Windows.Devices.PointOfService.IMagneticStripeReaderStatics2, connectionTypes: Windows.Devices.PointOfService.PosConnectionTypes) -> WinRT_String: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.PointOfService.IMagneticStripeReaderStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.MagneticStripeReader]: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.PointOfService.IMagneticStripeReaderStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.MagneticStripeReader]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.PointOfService.IMagneticStripeReaderStatics) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    Capabilities = property(get_Capabilities, None)
    SupportedCardTypes = property(get_SupportedCardTypes, None)
    DeviceAuthenticationProtocol = property(get_DeviceAuthenticationProtocol, None)
class MagneticStripeReaderAamvaCardDataReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs
    _classid_ = 'Windows.Devices.PointOfService.MagneticStripeReaderAamvaCardDataReceivedEventArgs'
    @winrt_mixinmethod
    def get_Report(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> Windows.Devices.PointOfService.MagneticStripeReaderReport: ...
    @winrt_mixinmethod
    def get_LicenseNumber(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExpirationDate(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Restrictions(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Class(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Endorsements(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BirthDate(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FirstName(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Surname(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Suffix(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Gender(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HairColor(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EyeColor(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Height(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Weight(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Address(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_City(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PostalCode(self: Windows.Devices.PointOfService.IMagneticStripeReaderAamvaCardDataReceivedEventArgs) -> WinRT_String: ...
    Report = property(get_Report, None)
    LicenseNumber = property(get_LicenseNumber, None)
    ExpirationDate = property(get_ExpirationDate, None)
    Restrictions = property(get_Restrictions, None)
    Class = property(get_Class, None)
    Endorsements = property(get_Endorsements, None)
    BirthDate = property(get_BirthDate, None)
    FirstName = property(get_FirstName, None)
    Surname = property(get_Surname, None)
    Suffix = property(get_Suffix, None)
    Gender = property(get_Gender, None)
    HairColor = property(get_HairColor, None)
    EyeColor = property(get_EyeColor, None)
    Height = property(get_Height, None)
    Weight = property(get_Weight, None)
    Address = property(get_Address, None)
    City = property(get_City, None)
    State = property(get_State, None)
    PostalCode = property(get_PostalCode, None)
MagneticStripeReaderAuthenticationLevel = Int32
MagneticStripeReaderAuthenticationLevel_NotSupported: MagneticStripeReaderAuthenticationLevel = 0
MagneticStripeReaderAuthenticationLevel_Optional: MagneticStripeReaderAuthenticationLevel = 1
MagneticStripeReaderAuthenticationLevel_Required: MagneticStripeReaderAuthenticationLevel = 2
MagneticStripeReaderAuthenticationProtocol = Int32
MagneticStripeReaderAuthenticationProtocol_None: MagneticStripeReaderAuthenticationProtocol = 0
MagneticStripeReaderAuthenticationProtocol_ChallengeResponse: MagneticStripeReaderAuthenticationProtocol = 1
class MagneticStripeReaderBankCardDataReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IMagneticStripeReaderBankCardDataReceivedEventArgs
    _classid_ = 'Windows.Devices.PointOfService.MagneticStripeReaderBankCardDataReceivedEventArgs'
    @winrt_mixinmethod
    def get_Report(self: Windows.Devices.PointOfService.IMagneticStripeReaderBankCardDataReceivedEventArgs) -> Windows.Devices.PointOfService.MagneticStripeReaderReport: ...
    @winrt_mixinmethod
    def get_AccountNumber(self: Windows.Devices.PointOfService.IMagneticStripeReaderBankCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExpirationDate(self: Windows.Devices.PointOfService.IMagneticStripeReaderBankCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceCode(self: Windows.Devices.PointOfService.IMagneticStripeReaderBankCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Title(self: Windows.Devices.PointOfService.IMagneticStripeReaderBankCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FirstName(self: Windows.Devices.PointOfService.IMagneticStripeReaderBankCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MiddleInitial(self: Windows.Devices.PointOfService.IMagneticStripeReaderBankCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Surname(self: Windows.Devices.PointOfService.IMagneticStripeReaderBankCardDataReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Suffix(self: Windows.Devices.PointOfService.IMagneticStripeReaderBankCardDataReceivedEventArgs) -> WinRT_String: ...
    Report = property(get_Report, None)
    AccountNumber = property(get_AccountNumber, None)
    ExpirationDate = property(get_ExpirationDate, None)
    ServiceCode = property(get_ServiceCode, None)
    Title = property(get_Title, None)
    FirstName = property(get_FirstName, None)
    MiddleInitial = property(get_MiddleInitial, None)
    Surname = property(get_Surname, None)
    Suffix = property(get_Suffix, None)
class MagneticStripeReaderCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IMagneticStripeReaderCapabilities
    _classid_ = 'Windows.Devices.PointOfService.MagneticStripeReaderCapabilities'
    @winrt_mixinmethod
    def get_CardAuthentication(self: Windows.Devices.PointOfService.IMagneticStripeReaderCapabilities) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SupportedEncryptionAlgorithms(self: Windows.Devices.PointOfService.IMagneticStripeReaderCapabilities) -> UInt32: ...
    @winrt_mixinmethod
    def get_AuthenticationLevel(self: Windows.Devices.PointOfService.IMagneticStripeReaderCapabilities) -> Windows.Devices.PointOfService.MagneticStripeReaderAuthenticationLevel: ...
    @winrt_mixinmethod
    def get_IsIsoSupported(self: Windows.Devices.PointOfService.IMagneticStripeReaderCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsJisOneSupported(self: Windows.Devices.PointOfService.IMagneticStripeReaderCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsJisTwoSupported(self: Windows.Devices.PointOfService.IMagneticStripeReaderCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_PowerReportingType(self: Windows.Devices.PointOfService.IMagneticStripeReaderCapabilities) -> Windows.Devices.PointOfService.UnifiedPosPowerReportingType: ...
    @winrt_mixinmethod
    def get_IsStatisticsReportingSupported(self: Windows.Devices.PointOfService.IMagneticStripeReaderCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsStatisticsUpdatingSupported(self: Windows.Devices.PointOfService.IMagneticStripeReaderCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTrackDataMaskingSupported(self: Windows.Devices.PointOfService.IMagneticStripeReaderCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTransmitSentinelsSupported(self: Windows.Devices.PointOfService.IMagneticStripeReaderCapabilities) -> Boolean: ...
    CardAuthentication = property(get_CardAuthentication, None)
    SupportedEncryptionAlgorithms = property(get_SupportedEncryptionAlgorithms, None)
    AuthenticationLevel = property(get_AuthenticationLevel, None)
    IsIsoSupported = property(get_IsIsoSupported, None)
    IsJisOneSupported = property(get_IsJisOneSupported, None)
    IsJisTwoSupported = property(get_IsJisTwoSupported, None)
    PowerReportingType = property(get_PowerReportingType, None)
    IsStatisticsReportingSupported = property(get_IsStatisticsReportingSupported, None)
    IsStatisticsUpdatingSupported = property(get_IsStatisticsUpdatingSupported, None)
    IsTrackDataMaskingSupported = property(get_IsTrackDataMaskingSupported, None)
    IsTransmitSentinelsSupported = property(get_IsTransmitSentinelsSupported, None)
class MagneticStripeReaderCardTypes(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.MagneticStripeReaderCardTypes'
    @winrt_classmethod
    def get_Unknown(cls: Windows.Devices.PointOfService.IMagneticStripeReaderCardTypesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Bank(cls: Windows.Devices.PointOfService.IMagneticStripeReaderCardTypesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Aamva(cls: Windows.Devices.PointOfService.IMagneticStripeReaderCardTypesStatics) -> UInt32: ...
    @winrt_classmethod
    def get_ExtendedBase(cls: Windows.Devices.PointOfService.IMagneticStripeReaderCardTypesStatics) -> UInt32: ...
    Unknown = property(get_Unknown, None)
    Bank = property(get_Bank, None)
    Aamva = property(get_Aamva, None)
    ExtendedBase = property(get_ExtendedBase, None)
class MagneticStripeReaderEncryptionAlgorithms(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.MagneticStripeReaderEncryptionAlgorithms'
    @winrt_classmethod
    def get_None(cls: Windows.Devices.PointOfService.IMagneticStripeReaderEncryptionAlgorithmsStatics) -> UInt32: ...
    @winrt_classmethod
    def get_TripleDesDukpt(cls: Windows.Devices.PointOfService.IMagneticStripeReaderEncryptionAlgorithmsStatics) -> UInt32: ...
    @winrt_classmethod
    def get_ExtendedBase(cls: Windows.Devices.PointOfService.IMagneticStripeReaderEncryptionAlgorithmsStatics) -> UInt32: ...
    None = property(get_None, None)
    TripleDesDukpt = property(get_TripleDesDukpt, None)
    ExtendedBase = property(get_ExtendedBase, None)
class MagneticStripeReaderErrorOccurredEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IMagneticStripeReaderErrorOccurredEventArgs
    _classid_ = 'Windows.Devices.PointOfService.MagneticStripeReaderErrorOccurredEventArgs'
    @winrt_mixinmethod
    def get_Track1Status(self: Windows.Devices.PointOfService.IMagneticStripeReaderErrorOccurredEventArgs) -> Windows.Devices.PointOfService.MagneticStripeReaderTrackErrorType: ...
    @winrt_mixinmethod
    def get_Track2Status(self: Windows.Devices.PointOfService.IMagneticStripeReaderErrorOccurredEventArgs) -> Windows.Devices.PointOfService.MagneticStripeReaderTrackErrorType: ...
    @winrt_mixinmethod
    def get_Track3Status(self: Windows.Devices.PointOfService.IMagneticStripeReaderErrorOccurredEventArgs) -> Windows.Devices.PointOfService.MagneticStripeReaderTrackErrorType: ...
    @winrt_mixinmethod
    def get_Track4Status(self: Windows.Devices.PointOfService.IMagneticStripeReaderErrorOccurredEventArgs) -> Windows.Devices.PointOfService.MagneticStripeReaderTrackErrorType: ...
    @winrt_mixinmethod
    def get_ErrorData(self: Windows.Devices.PointOfService.IMagneticStripeReaderErrorOccurredEventArgs) -> Windows.Devices.PointOfService.UnifiedPosErrorData: ...
    @winrt_mixinmethod
    def get_PartialInputData(self: Windows.Devices.PointOfService.IMagneticStripeReaderErrorOccurredEventArgs) -> Windows.Devices.PointOfService.MagneticStripeReaderReport: ...
    Track1Status = property(get_Track1Status, None)
    Track2Status = property(get_Track2Status, None)
    Track3Status = property(get_Track3Status, None)
    Track4Status = property(get_Track4Status, None)
    ErrorData = property(get_ErrorData, None)
    PartialInputData = property(get_PartialInputData, None)
MagneticStripeReaderErrorReportingType = Int32
MagneticStripeReaderErrorReportingType_CardLevel: MagneticStripeReaderErrorReportingType = 0
MagneticStripeReaderErrorReportingType_TrackLevel: MagneticStripeReaderErrorReportingType = 1
class MagneticStripeReaderReport(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IMagneticStripeReaderReport
    _classid_ = 'Windows.Devices.PointOfService.MagneticStripeReaderReport'
    @winrt_mixinmethod
    def get_CardType(self: Windows.Devices.PointOfService.IMagneticStripeReaderReport) -> UInt32: ...
    @winrt_mixinmethod
    def get_Track1(self: Windows.Devices.PointOfService.IMagneticStripeReaderReport) -> Windows.Devices.PointOfService.MagneticStripeReaderTrackData: ...
    @winrt_mixinmethod
    def get_Track2(self: Windows.Devices.PointOfService.IMagneticStripeReaderReport) -> Windows.Devices.PointOfService.MagneticStripeReaderTrackData: ...
    @winrt_mixinmethod
    def get_Track3(self: Windows.Devices.PointOfService.IMagneticStripeReaderReport) -> Windows.Devices.PointOfService.MagneticStripeReaderTrackData: ...
    @winrt_mixinmethod
    def get_Track4(self: Windows.Devices.PointOfService.IMagneticStripeReaderReport) -> Windows.Devices.PointOfService.MagneticStripeReaderTrackData: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.Devices.PointOfService.IMagneticStripeReaderReport) -> Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_CardAuthenticationData(self: Windows.Devices.PointOfService.IMagneticStripeReaderReport) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_CardAuthenticationDataLength(self: Windows.Devices.PointOfService.IMagneticStripeReaderReport) -> UInt32: ...
    @winrt_mixinmethod
    def get_AdditionalSecurityInformation(self: Windows.Devices.PointOfService.IMagneticStripeReaderReport) -> Windows.Storage.Streams.IBuffer: ...
    CardType = property(get_CardType, None)
    Track1 = property(get_Track1, None)
    Track2 = property(get_Track2, None)
    Track3 = property(get_Track3, None)
    Track4 = property(get_Track4, None)
    Properties = property(get_Properties, None)
    CardAuthenticationData = property(get_CardAuthenticationData, None)
    CardAuthenticationDataLength = property(get_CardAuthenticationDataLength, None)
    AdditionalSecurityInformation = property(get_AdditionalSecurityInformation, None)
MagneticStripeReaderStatus = Int32
MagneticStripeReaderStatus_Unauthenticated: MagneticStripeReaderStatus = 0
MagneticStripeReaderStatus_Authenticated: MagneticStripeReaderStatus = 1
MagneticStripeReaderStatus_Extended: MagneticStripeReaderStatus = 2
class MagneticStripeReaderStatusUpdatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IMagneticStripeReaderStatusUpdatedEventArgs
    _classid_ = 'Windows.Devices.PointOfService.MagneticStripeReaderStatusUpdatedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.PointOfService.IMagneticStripeReaderStatusUpdatedEventArgs) -> Windows.Devices.PointOfService.MagneticStripeReaderStatus: ...
    @winrt_mixinmethod
    def get_ExtendedStatus(self: Windows.Devices.PointOfService.IMagneticStripeReaderStatusUpdatedEventArgs) -> UInt32: ...
    Status = property(get_Status, None)
    ExtendedStatus = property(get_ExtendedStatus, None)
class MagneticStripeReaderTrackData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IMagneticStripeReaderTrackData
    _classid_ = 'Windows.Devices.PointOfService.MagneticStripeReaderTrackData'
    @winrt_mixinmethod
    def get_Data(self: Windows.Devices.PointOfService.IMagneticStripeReaderTrackData) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_DiscretionaryData(self: Windows.Devices.PointOfService.IMagneticStripeReaderTrackData) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def get_EncryptedData(self: Windows.Devices.PointOfService.IMagneticStripeReaderTrackData) -> Windows.Storage.Streams.IBuffer: ...
    Data = property(get_Data, None)
    DiscretionaryData = property(get_DiscretionaryData, None)
    EncryptedData = property(get_EncryptedData, None)
MagneticStripeReaderTrackErrorType = Int32
MagneticStripeReaderTrackErrorType_None: MagneticStripeReaderTrackErrorType = 0
MagneticStripeReaderTrackErrorType_StartSentinelError: MagneticStripeReaderTrackErrorType = 1
MagneticStripeReaderTrackErrorType_EndSentinelError: MagneticStripeReaderTrackErrorType = 2
MagneticStripeReaderTrackErrorType_ParityError: MagneticStripeReaderTrackErrorType = 3
MagneticStripeReaderTrackErrorType_LrcError: MagneticStripeReaderTrackErrorType = 4
MagneticStripeReaderTrackErrorType_Unknown: MagneticStripeReaderTrackErrorType = -1
MagneticStripeReaderTrackIds = Int32
MagneticStripeReaderTrackIds_None: MagneticStripeReaderTrackIds = 0
MagneticStripeReaderTrackIds_Track1: MagneticStripeReaderTrackIds = 1
MagneticStripeReaderTrackIds_Track2: MagneticStripeReaderTrackIds = 2
MagneticStripeReaderTrackIds_Track3: MagneticStripeReaderTrackIds = 4
MagneticStripeReaderTrackIds_Track4: MagneticStripeReaderTrackIds = 8
class MagneticStripeReaderVendorSpecificCardDataReceivedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IMagneticStripeReaderVendorSpecificCardDataReceivedEventArgs
    _classid_ = 'Windows.Devices.PointOfService.MagneticStripeReaderVendorSpecificCardDataReceivedEventArgs'
    @winrt_mixinmethod
    def get_Report(self: Windows.Devices.PointOfService.IMagneticStripeReaderVendorSpecificCardDataReceivedEventArgs) -> Windows.Devices.PointOfService.MagneticStripeReaderReport: ...
    Report = property(get_Report, None)
PosConnectionTypes = UInt32
PosConnectionTypes_Local: PosConnectionTypes = 1
PosConnectionTypes_IP: PosConnectionTypes = 2
PosConnectionTypes_Bluetooth: PosConnectionTypes = 4
PosConnectionTypes_All: PosConnectionTypes = 4294967295
class PosPrinter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IPosPrinter
    _classid_ = 'Windows.Devices.PointOfService.PosPrinter'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.PointOfService.IPosPrinter) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Capabilities(self: Windows.Devices.PointOfService.IPosPrinter) -> Windows.Devices.PointOfService.PosPrinterCapabilities: ...
    @winrt_mixinmethod
    def get_SupportedCharacterSets(self: Windows.Devices.PointOfService.IPosPrinter) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_mixinmethod
    def get_SupportedTypeFaces(self: Windows.Devices.PointOfService.IPosPrinter) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.PointOfService.IPosPrinter) -> Windows.Devices.PointOfService.PosPrinterStatus: ...
    @winrt_mixinmethod
    def ClaimPrinterAsync(self: Windows.Devices.PointOfService.IPosPrinter) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.ClaimedPosPrinter]: ...
    @winrt_mixinmethod
    def CheckHealthAsync(self: Windows.Devices.PointOfService.IPosPrinter, level: Windows.Devices.PointOfService.UnifiedPosHealthCheckLevel) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GetStatisticsAsync(self: Windows.Devices.PointOfService.IPosPrinter, statisticsCategories: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def add_StatusUpdated(self: Windows.Devices.PointOfService.IPosPrinter, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.PointOfService.PosPrinter, Windows.Devices.PointOfService.PosPrinterStatusUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusUpdated(self: Windows.Devices.PointOfService.IPosPrinter, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_SupportedBarcodeSymbologies(self: Windows.Devices.PointOfService.IPosPrinter2) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    @winrt_mixinmethod
    def GetFontProperty(self: Windows.Devices.PointOfService.IPosPrinter2, typeface: WinRT_String) -> Windows.Devices.PointOfService.PosPrinterFontProperty: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def GetDeviceSelectorWithConnectionTypes(cls: Windows.Devices.PointOfService.IPosPrinterStatics2, connectionTypes: Windows.Devices.PointOfService.PosConnectionTypes) -> WinRT_String: ...
    @winrt_classmethod
    def GetDefaultAsync(cls: Windows.Devices.PointOfService.IPosPrinterStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.PosPrinter]: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.PointOfService.IPosPrinterStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.PointOfService.PosPrinter]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.PointOfService.IPosPrinterStatics) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    Capabilities = property(get_Capabilities, None)
    SupportedCharacterSets = property(get_SupportedCharacterSets, None)
    SupportedTypeFaces = property(get_SupportedTypeFaces, None)
    Status = property(get_Status, None)
    SupportedBarcodeSymbologies = property(get_SupportedBarcodeSymbologies, None)
PosPrinterAlignment = Int32
PosPrinterAlignment_Left: PosPrinterAlignment = 0
PosPrinterAlignment_Center: PosPrinterAlignment = 1
PosPrinterAlignment_Right: PosPrinterAlignment = 2
PosPrinterBarcodeTextPosition = Int32
PosPrinterBarcodeTextPosition_None: PosPrinterBarcodeTextPosition = 0
PosPrinterBarcodeTextPosition_Above: PosPrinterBarcodeTextPosition = 1
PosPrinterBarcodeTextPosition_Below: PosPrinterBarcodeTextPosition = 2
class PosPrinterCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IPosPrinterCapabilities
    _classid_ = 'Windows.Devices.PointOfService.PosPrinterCapabilities'
    @winrt_mixinmethod
    def get_PowerReportingType(self: Windows.Devices.PointOfService.IPosPrinterCapabilities) -> Windows.Devices.PointOfService.UnifiedPosPowerReportingType: ...
    @winrt_mixinmethod
    def get_IsStatisticsReportingSupported(self: Windows.Devices.PointOfService.IPosPrinterCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsStatisticsUpdatingSupported(self: Windows.Devices.PointOfService.IPosPrinterCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_DefaultCharacterSet(self: Windows.Devices.PointOfService.IPosPrinterCapabilities) -> UInt32: ...
    @winrt_mixinmethod
    def get_HasCoverSensor(self: Windows.Devices.PointOfService.IPosPrinterCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanMapCharacterSet(self: Windows.Devices.PointOfService.IPosPrinterCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTransactionSupported(self: Windows.Devices.PointOfService.IPosPrinterCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_Receipt(self: Windows.Devices.PointOfService.IPosPrinterCapabilities) -> Windows.Devices.PointOfService.ReceiptPrinterCapabilities: ...
    @winrt_mixinmethod
    def get_Slip(self: Windows.Devices.PointOfService.IPosPrinterCapabilities) -> Windows.Devices.PointOfService.SlipPrinterCapabilities: ...
    @winrt_mixinmethod
    def get_Journal(self: Windows.Devices.PointOfService.IPosPrinterCapabilities) -> Windows.Devices.PointOfService.JournalPrinterCapabilities: ...
    PowerReportingType = property(get_PowerReportingType, None)
    IsStatisticsReportingSupported = property(get_IsStatisticsReportingSupported, None)
    IsStatisticsUpdatingSupported = property(get_IsStatisticsUpdatingSupported, None)
    DefaultCharacterSet = property(get_DefaultCharacterSet, None)
    HasCoverSensor = property(get_HasCoverSensor, None)
    CanMapCharacterSet = property(get_CanMapCharacterSet, None)
    IsTransactionSupported = property(get_IsTransactionSupported, None)
    Receipt = property(get_Receipt, None)
    Slip = property(get_Slip, None)
    Journal = property(get_Journal, None)
PosPrinterCartridgeSensors = UInt32
PosPrinterCartridgeSensors_None: PosPrinterCartridgeSensors = 0
PosPrinterCartridgeSensors_Removed: PosPrinterCartridgeSensors = 1
PosPrinterCartridgeSensors_Empty: PosPrinterCartridgeSensors = 2
PosPrinterCartridgeSensors_HeadCleaning: PosPrinterCartridgeSensors = 4
PosPrinterCartridgeSensors_NearEnd: PosPrinterCartridgeSensors = 8
class PosPrinterCharacterSetIds(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.PointOfService.PosPrinterCharacterSetIds'
    @winrt_classmethod
    def get_Utf16LE(cls: Windows.Devices.PointOfService.IPosPrinterCharacterSetIdsStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Ascii(cls: Windows.Devices.PointOfService.IPosPrinterCharacterSetIdsStatics) -> UInt32: ...
    @winrt_classmethod
    def get_Ansi(cls: Windows.Devices.PointOfService.IPosPrinterCharacterSetIdsStatics) -> UInt32: ...
    Utf16LE = property(get_Utf16LE, None)
    Ascii = property(get_Ascii, None)
    Ansi = property(get_Ansi, None)
PosPrinterColorCapabilities = UInt32
PosPrinterColorCapabilities_None: PosPrinterColorCapabilities = 0
PosPrinterColorCapabilities_Primary: PosPrinterColorCapabilities = 1
PosPrinterColorCapabilities_Custom1: PosPrinterColorCapabilities = 2
PosPrinterColorCapabilities_Custom2: PosPrinterColorCapabilities = 4
PosPrinterColorCapabilities_Custom3: PosPrinterColorCapabilities = 8
PosPrinterColorCapabilities_Custom4: PosPrinterColorCapabilities = 16
PosPrinterColorCapabilities_Custom5: PosPrinterColorCapabilities = 32
PosPrinterColorCapabilities_Custom6: PosPrinterColorCapabilities = 64
PosPrinterColorCapabilities_Cyan: PosPrinterColorCapabilities = 128
PosPrinterColorCapabilities_Magenta: PosPrinterColorCapabilities = 256
PosPrinterColorCapabilities_Yellow: PosPrinterColorCapabilities = 512
PosPrinterColorCapabilities_Full: PosPrinterColorCapabilities = 1024
PosPrinterColorCartridge = Int32
PosPrinterColorCartridge_Unknown: PosPrinterColorCartridge = 0
PosPrinterColorCartridge_Primary: PosPrinterColorCartridge = 1
PosPrinterColorCartridge_Custom1: PosPrinterColorCartridge = 2
PosPrinterColorCartridge_Custom2: PosPrinterColorCartridge = 3
PosPrinterColorCartridge_Custom3: PosPrinterColorCartridge = 4
PosPrinterColorCartridge_Custom4: PosPrinterColorCartridge = 5
PosPrinterColorCartridge_Custom5: PosPrinterColorCartridge = 6
PosPrinterColorCartridge_Custom6: PosPrinterColorCartridge = 7
PosPrinterColorCartridge_Cyan: PosPrinterColorCartridge = 8
PosPrinterColorCartridge_Magenta: PosPrinterColorCartridge = 9
PosPrinterColorCartridge_Yellow: PosPrinterColorCartridge = 10
class PosPrinterFontProperty(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IPosPrinterFontProperty
    _classid_ = 'Windows.Devices.PointOfService.PosPrinterFontProperty'
    @winrt_mixinmethod
    def get_TypeFace(self: Windows.Devices.PointOfService.IPosPrinterFontProperty) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsScalableToAnySize(self: Windows.Devices.PointOfService.IPosPrinterFontProperty) -> Boolean: ...
    @winrt_mixinmethod
    def get_CharacterSizes(self: Windows.Devices.PointOfService.IPosPrinterFontProperty) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.PointOfService.SizeUInt32]: ...
    TypeFace = property(get_TypeFace, None)
    IsScalableToAnySize = property(get_IsScalableToAnySize, None)
    CharacterSizes = property(get_CharacterSizes, None)
PosPrinterLineDirection = Int32
PosPrinterLineDirection_Horizontal: PosPrinterLineDirection = 0
PosPrinterLineDirection_Vertical: PosPrinterLineDirection = 1
PosPrinterLineStyle = Int32
PosPrinterLineStyle_SingleSolid: PosPrinterLineStyle = 0
PosPrinterLineStyle_DoubleSolid: PosPrinterLineStyle = 1
PosPrinterLineStyle_Broken: PosPrinterLineStyle = 2
PosPrinterLineStyle_Chain: PosPrinterLineStyle = 3
PosPrinterMapMode = Int32
PosPrinterMapMode_Dots: PosPrinterMapMode = 0
PosPrinterMapMode_Twips: PosPrinterMapMode = 1
PosPrinterMapMode_English: PosPrinterMapMode = 2
PosPrinterMapMode_Metric: PosPrinterMapMode = 3
PosPrinterMarkFeedCapabilities = UInt32
PosPrinterMarkFeedCapabilities_None: PosPrinterMarkFeedCapabilities = 0
PosPrinterMarkFeedCapabilities_ToTakeUp: PosPrinterMarkFeedCapabilities = 1
PosPrinterMarkFeedCapabilities_ToCutter: PosPrinterMarkFeedCapabilities = 2
PosPrinterMarkFeedCapabilities_ToCurrentTopOfForm: PosPrinterMarkFeedCapabilities = 4
PosPrinterMarkFeedCapabilities_ToNextTopOfForm: PosPrinterMarkFeedCapabilities = 8
PosPrinterMarkFeedKind = Int32
PosPrinterMarkFeedKind_ToTakeUp: PosPrinterMarkFeedKind = 0
PosPrinterMarkFeedKind_ToCutter: PosPrinterMarkFeedKind = 1
PosPrinterMarkFeedKind_ToCurrentTopOfForm: PosPrinterMarkFeedKind = 2
PosPrinterMarkFeedKind_ToNextTopOfForm: PosPrinterMarkFeedKind = 3
class PosPrinterPrintOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IPosPrinterPrintOptions
    _classid_ = 'Windows.Devices.PointOfService.PosPrinterPrintOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.PointOfService.PosPrinterPrintOptions: ...
    @winrt_mixinmethod
    def get_TypeFace(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TypeFace(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CharacterHeight(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions) -> UInt32: ...
    @winrt_mixinmethod
    def put_CharacterHeight(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Bold(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_Bold(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Italic(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_Italic(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Underline(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_Underline(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ReverseVideo(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_ReverseVideo(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Strikethrough(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_Strikethrough(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Superscript(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_Superscript(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Subscript(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_Subscript(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DoubleWide(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_DoubleWide(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DoubleHigh(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_DoubleHigh(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Alignment(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions) -> Windows.Devices.PointOfService.PosPrinterAlignment: ...
    @winrt_mixinmethod
    def put_Alignment(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions, value: Windows.Devices.PointOfService.PosPrinterAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_CharacterSet(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions) -> UInt32: ...
    @winrt_mixinmethod
    def put_CharacterSet(self: Windows.Devices.PointOfService.IPosPrinterPrintOptions, value: UInt32) -> Void: ...
    TypeFace = property(get_TypeFace, put_TypeFace)
    CharacterHeight = property(get_CharacterHeight, put_CharacterHeight)
    Bold = property(get_Bold, put_Bold)
    Italic = property(get_Italic, put_Italic)
    Underline = property(get_Underline, put_Underline)
    ReverseVideo = property(get_ReverseVideo, put_ReverseVideo)
    Strikethrough = property(get_Strikethrough, put_Strikethrough)
    Superscript = property(get_Superscript, put_Superscript)
    Subscript = property(get_Subscript, put_Subscript)
    DoubleWide = property(get_DoubleWide, put_DoubleWide)
    DoubleHigh = property(get_DoubleHigh, put_DoubleHigh)
    Alignment = property(get_Alignment, put_Alignment)
    CharacterSet = property(get_CharacterSet, put_CharacterSet)
PosPrinterPrintSide = Int32
PosPrinterPrintSide_Unknown: PosPrinterPrintSide = 0
PosPrinterPrintSide_Side1: PosPrinterPrintSide = 1
PosPrinterPrintSide_Side2: PosPrinterPrintSide = 2
class PosPrinterReleaseDeviceRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IPosPrinterReleaseDeviceRequestedEventArgs
    _classid_ = 'Windows.Devices.PointOfService.PosPrinterReleaseDeviceRequestedEventArgs'
PosPrinterRotation = Int32
PosPrinterRotation_Normal: PosPrinterRotation = 0
PosPrinterRotation_Right90: PosPrinterRotation = 1
PosPrinterRotation_Left90: PosPrinterRotation = 2
PosPrinterRotation_Rotate180: PosPrinterRotation = 3
PosPrinterRuledLineCapabilities = UInt32
PosPrinterRuledLineCapabilities_None: PosPrinterRuledLineCapabilities = 0
PosPrinterRuledLineCapabilities_Horizontal: PosPrinterRuledLineCapabilities = 1
PosPrinterRuledLineCapabilities_Vertical: PosPrinterRuledLineCapabilities = 2
class PosPrinterStatus(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IPosPrinterStatus
    _classid_ = 'Windows.Devices.PointOfService.PosPrinterStatus'
    @winrt_mixinmethod
    def get_StatusKind(self: Windows.Devices.PointOfService.IPosPrinterStatus) -> Windows.Devices.PointOfService.PosPrinterStatusKind: ...
    @winrt_mixinmethod
    def get_ExtendedStatus(self: Windows.Devices.PointOfService.IPosPrinterStatus) -> UInt32: ...
    StatusKind = property(get_StatusKind, None)
    ExtendedStatus = property(get_ExtendedStatus, None)
PosPrinterStatusKind = Int32
PosPrinterStatusKind_Online: PosPrinterStatusKind = 0
PosPrinterStatusKind_Off: PosPrinterStatusKind = 1
PosPrinterStatusKind_Offline: PosPrinterStatusKind = 2
PosPrinterStatusKind_OffOrOffline: PosPrinterStatusKind = 3
PosPrinterStatusKind_Extended: PosPrinterStatusKind = 4
class PosPrinterStatusUpdatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IPosPrinterStatusUpdatedEventArgs
    _classid_ = 'Windows.Devices.PointOfService.PosPrinterStatusUpdatedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.PointOfService.IPosPrinterStatusUpdatedEventArgs) -> Windows.Devices.PointOfService.PosPrinterStatus: ...
    Status = property(get_Status, None)
class ReceiptPrintJob(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IReceiptPrintJob
    _classid_ = 'Windows.Devices.PointOfService.ReceiptPrintJob'
    @winrt_mixinmethod
    def MarkFeed(self: Windows.Devices.PointOfService.IReceiptPrintJob, kind: Windows.Devices.PointOfService.PosPrinterMarkFeedKind) -> Void: ...
    @winrt_mixinmethod
    def CutPaper(self: Windows.Devices.PointOfService.IReceiptPrintJob, percentage: Double) -> Void: ...
    @winrt_mixinmethod
    def CutPaperDefault(self: Windows.Devices.PointOfService.IReceiptPrintJob) -> Void: ...
    @winrt_mixinmethod
    def StampPaper(self: Windows.Devices.PointOfService.IReceiptPrintJob2) -> Void: ...
    @winrt_mixinmethod
    def Print(self: Windows.Devices.PointOfService.IPosPrinterJob, data: WinRT_String, printOptions: Windows.Devices.PointOfService.PosPrinterPrintOptions) -> Void: ...
    @winrt_mixinmethod
    def FeedPaperByLine(self: Windows.Devices.PointOfService.IReceiptPrintJob2, lineCount: Int32) -> Void: ...
    @winrt_mixinmethod
    def FeedPaperByMapModeUnit(self: Windows.Devices.PointOfService.IReceiptPrintJob2, distance: Int32) -> Void: ...
    @winrt_mixinmethod
    def SetBarcodeRotation(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, value: Windows.Devices.PointOfService.PosPrinterRotation) -> Void: ...
    @winrt_mixinmethod
    def SetPrintRotation(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, value: Windows.Devices.PointOfService.PosPrinterRotation, includeBitmaps: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetPrintArea(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def SetBitmap(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, bitmapNumber: UInt32, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignment: Windows.Devices.PointOfService.PosPrinterAlignment) -> Void: ...
    @winrt_mixinmethod
    def SetBitmapCustomWidthStandardAlign(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, bitmapNumber: UInt32, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignment: Windows.Devices.PointOfService.PosPrinterAlignment, width: UInt32) -> Void: ...
    @winrt_mixinmethod
    def SetCustomAlignedBitmap(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, bitmapNumber: UInt32, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignmentDistance: UInt32) -> Void: ...
    @winrt_mixinmethod
    def SetBitmapCustomWidthCustomAlign(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, bitmapNumber: UInt32, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignmentDistance: UInt32, width: UInt32) -> Void: ...
    @winrt_mixinmethod
    def PrintSavedBitmap(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, bitmapNumber: UInt32) -> Void: ...
    @winrt_mixinmethod
    def DrawRuledLine(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, positionList: WinRT_String, lineDirection: Windows.Devices.PointOfService.PosPrinterLineDirection, lineWidth: UInt32, lineStyle: Windows.Devices.PointOfService.PosPrinterLineStyle, lineColor: UInt32) -> Void: ...
    @winrt_mixinmethod
    def PrintBarcode(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, data: WinRT_String, symbology: UInt32, height: UInt32, width: UInt32, textPosition: Windows.Devices.PointOfService.PosPrinterBarcodeTextPosition, alignment: Windows.Devices.PointOfService.PosPrinterAlignment) -> Void: ...
    @winrt_mixinmethod
    def PrintBarcodeCustomAlign(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, data: WinRT_String, symbology: UInt32, height: UInt32, width: UInt32, textPosition: Windows.Devices.PointOfService.PosPrinterBarcodeTextPosition, alignmentDistance: UInt32) -> Void: ...
    @winrt_mixinmethod
    def PrintBitmap(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignment: Windows.Devices.PointOfService.PosPrinterAlignment) -> Void: ...
    @winrt_mixinmethod
    def PrintBitmapCustomWidthStandardAlign(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignment: Windows.Devices.PointOfService.PosPrinterAlignment, width: UInt32) -> Void: ...
    @winrt_mixinmethod
    def PrintCustomAlignedBitmap(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignmentDistance: UInt32) -> Void: ...
    @winrt_mixinmethod
    def PrintBitmapCustomWidthCustomAlign(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignmentDistance: UInt32, width: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Print(self: Windows.Devices.PointOfService.IPosPrinterJob, data: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def PrintLine(self: Windows.Devices.PointOfService.IPosPrinterJob, data: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def PrintNewline(self: Windows.Devices.PointOfService.IPosPrinterJob) -> Void: ...
    @winrt_mixinmethod
    def ExecuteAsync(self: Windows.Devices.PointOfService.IPosPrinterJob) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class ReceiptPrinterCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IReceiptPrinterCapabilities
    _classid_ = 'Windows.Devices.PointOfService.ReceiptPrinterCapabilities'
    @winrt_mixinmethod
    def get_CanCutPaper(self: Windows.Devices.PointOfService.IReceiptPrinterCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsStampSupported(self: Windows.Devices.PointOfService.IReceiptPrinterCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_MarkFeedCapabilities(self: Windows.Devices.PointOfService.IReceiptPrinterCapabilities) -> Windows.Devices.PointOfService.PosPrinterMarkFeedCapabilities: ...
    @winrt_mixinmethod
    def get_IsReverseVideoSupported(self: Windows.Devices.PointOfService.IReceiptPrinterCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsStrikethroughSupported(self: Windows.Devices.PointOfService.IReceiptPrinterCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSuperscriptSupported(self: Windows.Devices.PointOfService.IReceiptPrinterCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSubscriptSupported(self: Windows.Devices.PointOfService.IReceiptPrinterCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsReversePaperFeedByLineSupported(self: Windows.Devices.PointOfService.IReceiptPrinterCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsReversePaperFeedByMapModeUnitSupported(self: Windows.Devices.PointOfService.IReceiptPrinterCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBarcodeSupported(self: Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBitmapSupported(self: Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsLeft90RotationSupported(self: Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRight90RotationSupported(self: Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_Is180RotationSupported(self: Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPrintAreaSupported(self: Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_RuledLineCapabilities(self: Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities) -> Windows.Devices.PointOfService.PosPrinterRuledLineCapabilities: ...
    @winrt_mixinmethod
    def get_SupportedBarcodeRotations(self: Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.PointOfService.PosPrinterRotation]: ...
    @winrt_mixinmethod
    def get_SupportedBitmapRotations(self: Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.PointOfService.PosPrinterRotation]: ...
    @winrt_mixinmethod
    def get_IsPrinterPresent(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDualColorSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_ColorCartridgeCapabilities(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Windows.Devices.PointOfService.PosPrinterColorCapabilities: ...
    @winrt_mixinmethod
    def get_CartridgeSensors(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Windows.Devices.PointOfService.PosPrinterCartridgeSensors: ...
    @winrt_mixinmethod
    def get_IsBoldSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsItalicSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsUnderlineSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDoubleHighPrintSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDoubleWidePrintSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDoubleHighDoubleWidePrintSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPaperEmptySensorSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPaperNearEndSensorSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedCharactersPerLine(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    CanCutPaper = property(get_CanCutPaper, None)
    IsStampSupported = property(get_IsStampSupported, None)
    MarkFeedCapabilities = property(get_MarkFeedCapabilities, None)
    IsReverseVideoSupported = property(get_IsReverseVideoSupported, None)
    IsStrikethroughSupported = property(get_IsStrikethroughSupported, None)
    IsSuperscriptSupported = property(get_IsSuperscriptSupported, None)
    IsSubscriptSupported = property(get_IsSubscriptSupported, None)
    IsReversePaperFeedByLineSupported = property(get_IsReversePaperFeedByLineSupported, None)
    IsReversePaperFeedByMapModeUnitSupported = property(get_IsReversePaperFeedByMapModeUnitSupported, None)
    IsBarcodeSupported = property(get_IsBarcodeSupported, None)
    IsBitmapSupported = property(get_IsBitmapSupported, None)
    IsLeft90RotationSupported = property(get_IsLeft90RotationSupported, None)
    IsRight90RotationSupported = property(get_IsRight90RotationSupported, None)
    Is180RotationSupported = property(get_Is180RotationSupported, None)
    IsPrintAreaSupported = property(get_IsPrintAreaSupported, None)
    RuledLineCapabilities = property(get_RuledLineCapabilities, None)
    SupportedBarcodeRotations = property(get_SupportedBarcodeRotations, None)
    SupportedBitmapRotations = property(get_SupportedBitmapRotations, None)
    IsPrinterPresent = property(get_IsPrinterPresent, None)
    IsDualColorSupported = property(get_IsDualColorSupported, None)
    ColorCartridgeCapabilities = property(get_ColorCartridgeCapabilities, None)
    CartridgeSensors = property(get_CartridgeSensors, None)
    IsBoldSupported = property(get_IsBoldSupported, None)
    IsItalicSupported = property(get_IsItalicSupported, None)
    IsUnderlineSupported = property(get_IsUnderlineSupported, None)
    IsDoubleHighPrintSupported = property(get_IsDoubleHighPrintSupported, None)
    IsDoubleWidePrintSupported = property(get_IsDoubleWidePrintSupported, None)
    IsDoubleHighDoubleWidePrintSupported = property(get_IsDoubleHighDoubleWidePrintSupported, None)
    IsPaperEmptySensorSupported = property(get_IsPaperEmptySensorSupported, None)
    IsPaperNearEndSensorSupported = property(get_IsPaperNearEndSensorSupported, None)
    SupportedCharactersPerLine = property(get_SupportedCharactersPerLine, None)
class SizeUInt32(EasyCastStructure):
    Width: UInt32
    Height: UInt32
class SlipPrintJob(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IReceiptOrSlipJob
    _classid_ = 'Windows.Devices.PointOfService.SlipPrintJob'
    @winrt_mixinmethod
    def Print(self: Windows.Devices.PointOfService.IPosPrinterJob, data: WinRT_String, printOptions: Windows.Devices.PointOfService.PosPrinterPrintOptions) -> Void: ...
    @winrt_mixinmethod
    def FeedPaperByLine(self: Windows.Devices.PointOfService.ISlipPrintJob, lineCount: Int32) -> Void: ...
    @winrt_mixinmethod
    def FeedPaperByMapModeUnit(self: Windows.Devices.PointOfService.ISlipPrintJob, distance: Int32) -> Void: ...
    @winrt_mixinmethod
    def SetBarcodeRotation(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, value: Windows.Devices.PointOfService.PosPrinterRotation) -> Void: ...
    @winrt_mixinmethod
    def SetPrintRotation(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, value: Windows.Devices.PointOfService.PosPrinterRotation, includeBitmaps: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetPrintArea(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def SetBitmap(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, bitmapNumber: UInt32, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignment: Windows.Devices.PointOfService.PosPrinterAlignment) -> Void: ...
    @winrt_mixinmethod
    def SetBitmapCustomWidthStandardAlign(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, bitmapNumber: UInt32, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignment: Windows.Devices.PointOfService.PosPrinterAlignment, width: UInt32) -> Void: ...
    @winrt_mixinmethod
    def SetCustomAlignedBitmap(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, bitmapNumber: UInt32, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignmentDistance: UInt32) -> Void: ...
    @winrt_mixinmethod
    def SetBitmapCustomWidthCustomAlign(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, bitmapNumber: UInt32, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignmentDistance: UInt32, width: UInt32) -> Void: ...
    @winrt_mixinmethod
    def PrintSavedBitmap(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, bitmapNumber: UInt32) -> Void: ...
    @winrt_mixinmethod
    def DrawRuledLine(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, positionList: WinRT_String, lineDirection: Windows.Devices.PointOfService.PosPrinterLineDirection, lineWidth: UInt32, lineStyle: Windows.Devices.PointOfService.PosPrinterLineStyle, lineColor: UInt32) -> Void: ...
    @winrt_mixinmethod
    def PrintBarcode(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, data: WinRT_String, symbology: UInt32, height: UInt32, width: UInt32, textPosition: Windows.Devices.PointOfService.PosPrinterBarcodeTextPosition, alignment: Windows.Devices.PointOfService.PosPrinterAlignment) -> Void: ...
    @winrt_mixinmethod
    def PrintBarcodeCustomAlign(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, data: WinRT_String, symbology: UInt32, height: UInt32, width: UInt32, textPosition: Windows.Devices.PointOfService.PosPrinterBarcodeTextPosition, alignmentDistance: UInt32) -> Void: ...
    @winrt_mixinmethod
    def PrintBitmap(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignment: Windows.Devices.PointOfService.PosPrinterAlignment) -> Void: ...
    @winrt_mixinmethod
    def PrintBitmapCustomWidthStandardAlign(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignment: Windows.Devices.PointOfService.PosPrinterAlignment, width: UInt32) -> Void: ...
    @winrt_mixinmethod
    def PrintCustomAlignedBitmap(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignmentDistance: UInt32) -> Void: ...
    @winrt_mixinmethod
    def PrintBitmapCustomWidthCustomAlign(self: Windows.Devices.PointOfService.IReceiptOrSlipJob, bitmap: Windows.Graphics.Imaging.BitmapFrame, alignmentDistance: UInt32, width: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Print(self: Windows.Devices.PointOfService.IPosPrinterJob, data: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def PrintLine(self: Windows.Devices.PointOfService.IPosPrinterJob, data: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def PrintNewline(self: Windows.Devices.PointOfService.IPosPrinterJob) -> Void: ...
    @winrt_mixinmethod
    def ExecuteAsync(self: Windows.Devices.PointOfService.IPosPrinterJob) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class SlipPrinterCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.ISlipPrinterCapabilities
    _classid_ = 'Windows.Devices.PointOfService.SlipPrinterCapabilities'
    @winrt_mixinmethod
    def get_IsFullLengthSupported(self: Windows.Devices.PointOfService.ISlipPrinterCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBothSidesPrintingSupported(self: Windows.Devices.PointOfService.ISlipPrinterCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsReverseVideoSupported(self: Windows.Devices.PointOfService.ISlipPrinterCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsStrikethroughSupported(self: Windows.Devices.PointOfService.ISlipPrinterCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSuperscriptSupported(self: Windows.Devices.PointOfService.ISlipPrinterCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSubscriptSupported(self: Windows.Devices.PointOfService.ISlipPrinterCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsReversePaperFeedByLineSupported(self: Windows.Devices.PointOfService.ISlipPrinterCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsReversePaperFeedByMapModeUnitSupported(self: Windows.Devices.PointOfService.ISlipPrinterCapabilities2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBarcodeSupported(self: Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBitmapSupported(self: Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsLeft90RotationSupported(self: Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRight90RotationSupported(self: Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_Is180RotationSupported(self: Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPrintAreaSupported(self: Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_RuledLineCapabilities(self: Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities) -> Windows.Devices.PointOfService.PosPrinterRuledLineCapabilities: ...
    @winrt_mixinmethod
    def get_SupportedBarcodeRotations(self: Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.PointOfService.PosPrinterRotation]: ...
    @winrt_mixinmethod
    def get_SupportedBitmapRotations(self: Windows.Devices.PointOfService.ICommonReceiptSlipCapabilities) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.PointOfService.PosPrinterRotation]: ...
    @winrt_mixinmethod
    def get_IsPrinterPresent(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDualColorSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_ColorCartridgeCapabilities(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Windows.Devices.PointOfService.PosPrinterColorCapabilities: ...
    @winrt_mixinmethod
    def get_CartridgeSensors(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Windows.Devices.PointOfService.PosPrinterCartridgeSensors: ...
    @winrt_mixinmethod
    def get_IsBoldSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsItalicSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsUnderlineSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDoubleHighPrintSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDoubleWidePrintSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDoubleHighDoubleWidePrintSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPaperEmptySensorSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPaperNearEndSensorSupported(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_SupportedCharactersPerLine(self: Windows.Devices.PointOfService.ICommonPosPrintStationCapabilities) -> Windows.Foundation.Collections.IVectorView[UInt32]: ...
    IsFullLengthSupported = property(get_IsFullLengthSupported, None)
    IsBothSidesPrintingSupported = property(get_IsBothSidesPrintingSupported, None)
    IsReverseVideoSupported = property(get_IsReverseVideoSupported, None)
    IsStrikethroughSupported = property(get_IsStrikethroughSupported, None)
    IsSuperscriptSupported = property(get_IsSuperscriptSupported, None)
    IsSubscriptSupported = property(get_IsSubscriptSupported, None)
    IsReversePaperFeedByLineSupported = property(get_IsReversePaperFeedByLineSupported, None)
    IsReversePaperFeedByMapModeUnitSupported = property(get_IsReversePaperFeedByMapModeUnitSupported, None)
    IsBarcodeSupported = property(get_IsBarcodeSupported, None)
    IsBitmapSupported = property(get_IsBitmapSupported, None)
    IsLeft90RotationSupported = property(get_IsLeft90RotationSupported, None)
    IsRight90RotationSupported = property(get_IsRight90RotationSupported, None)
    Is180RotationSupported = property(get_Is180RotationSupported, None)
    IsPrintAreaSupported = property(get_IsPrintAreaSupported, None)
    RuledLineCapabilities = property(get_RuledLineCapabilities, None)
    SupportedBarcodeRotations = property(get_SupportedBarcodeRotations, None)
    SupportedBitmapRotations = property(get_SupportedBitmapRotations, None)
    IsPrinterPresent = property(get_IsPrinterPresent, None)
    IsDualColorSupported = property(get_IsDualColorSupported, None)
    ColorCartridgeCapabilities = property(get_ColorCartridgeCapabilities, None)
    CartridgeSensors = property(get_CartridgeSensors, None)
    IsBoldSupported = property(get_IsBoldSupported, None)
    IsItalicSupported = property(get_IsItalicSupported, None)
    IsUnderlineSupported = property(get_IsUnderlineSupported, None)
    IsDoubleHighPrintSupported = property(get_IsDoubleHighPrintSupported, None)
    IsDoubleWidePrintSupported = property(get_IsDoubleWidePrintSupported, None)
    IsDoubleHighDoubleWidePrintSupported = property(get_IsDoubleHighDoubleWidePrintSupported, None)
    IsPaperEmptySensorSupported = property(get_IsPaperEmptySensorSupported, None)
    IsPaperNearEndSensorSupported = property(get_IsPaperNearEndSensorSupported, None)
    SupportedCharactersPerLine = property(get_SupportedCharactersPerLine, None)
class UnifiedPosErrorData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.PointOfService.IUnifiedPosErrorData
    _classid_ = 'Windows.Devices.PointOfService.UnifiedPosErrorData'
    @winrt_factorymethod
    def CreateInstance(cls: Windows.Devices.PointOfService.IUnifiedPosErrorDataFactory, message: WinRT_String, severity: Windows.Devices.PointOfService.UnifiedPosErrorSeverity, reason: Windows.Devices.PointOfService.UnifiedPosErrorReason, extendedReason: UInt32) -> Windows.Devices.PointOfService.UnifiedPosErrorData: ...
    @winrt_mixinmethod
    def get_Message(self: Windows.Devices.PointOfService.IUnifiedPosErrorData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Severity(self: Windows.Devices.PointOfService.IUnifiedPosErrorData) -> Windows.Devices.PointOfService.UnifiedPosErrorSeverity: ...
    @winrt_mixinmethod
    def get_Reason(self: Windows.Devices.PointOfService.IUnifiedPosErrorData) -> Windows.Devices.PointOfService.UnifiedPosErrorReason: ...
    @winrt_mixinmethod
    def get_ExtendedReason(self: Windows.Devices.PointOfService.IUnifiedPosErrorData) -> UInt32: ...
    Message = property(get_Message, None)
    Severity = property(get_Severity, None)
    Reason = property(get_Reason, None)
    ExtendedReason = property(get_ExtendedReason, None)
UnifiedPosErrorReason = Int32
UnifiedPosErrorReason_UnknownErrorReason: UnifiedPosErrorReason = 0
UnifiedPosErrorReason_NoService: UnifiedPosErrorReason = 1
UnifiedPosErrorReason_Disabled: UnifiedPosErrorReason = 2
UnifiedPosErrorReason_Illegal: UnifiedPosErrorReason = 3
UnifiedPosErrorReason_NoHardware: UnifiedPosErrorReason = 4
UnifiedPosErrorReason_Closed: UnifiedPosErrorReason = 5
UnifiedPosErrorReason_Offline: UnifiedPosErrorReason = 6
UnifiedPosErrorReason_Failure: UnifiedPosErrorReason = 7
UnifiedPosErrorReason_Timeout: UnifiedPosErrorReason = 8
UnifiedPosErrorReason_Busy: UnifiedPosErrorReason = 9
UnifiedPosErrorReason_Extended: UnifiedPosErrorReason = 10
UnifiedPosErrorSeverity = Int32
UnifiedPosErrorSeverity_UnknownErrorSeverity: UnifiedPosErrorSeverity = 0
UnifiedPosErrorSeverity_Warning: UnifiedPosErrorSeverity = 1
UnifiedPosErrorSeverity_Recoverable: UnifiedPosErrorSeverity = 2
UnifiedPosErrorSeverity_Unrecoverable: UnifiedPosErrorSeverity = 3
UnifiedPosErrorSeverity_AssistanceRequired: UnifiedPosErrorSeverity = 4
UnifiedPosErrorSeverity_Fatal: UnifiedPosErrorSeverity = 5
UnifiedPosHealthCheckLevel = Int32
UnifiedPosHealthCheckLevel_UnknownHealthCheckLevel: UnifiedPosHealthCheckLevel = 0
UnifiedPosHealthCheckLevel_POSInternal: UnifiedPosHealthCheckLevel = 1
UnifiedPosHealthCheckLevel_External: UnifiedPosHealthCheckLevel = 2
UnifiedPosHealthCheckLevel_Interactive: UnifiedPosHealthCheckLevel = 3
UnifiedPosPowerReportingType = Int32
UnifiedPosPowerReportingType_UnknownPowerReportingType: UnifiedPosPowerReportingType = 0
UnifiedPosPowerReportingType_Standard: UnifiedPosPowerReportingType = 1
UnifiedPosPowerReportingType_Advanced: UnifiedPosPowerReportingType = 2
make_head(_module, 'BarcodeScanner')
make_head(_module, 'BarcodeScannerCapabilities')
make_head(_module, 'BarcodeScannerDataReceivedEventArgs')
make_head(_module, 'BarcodeScannerErrorOccurredEventArgs')
make_head(_module, 'BarcodeScannerImagePreviewReceivedEventArgs')
make_head(_module, 'BarcodeScannerReport')
make_head(_module, 'BarcodeScannerStatusUpdatedEventArgs')
make_head(_module, 'BarcodeSymbologies')
make_head(_module, 'BarcodeSymbologyAttributes')
make_head(_module, 'CashDrawer')
make_head(_module, 'CashDrawerCapabilities')
make_head(_module, 'CashDrawerCloseAlarm')
make_head(_module, 'CashDrawerClosedEventArgs')
make_head(_module, 'CashDrawerEventSource')
make_head(_module, 'CashDrawerOpenedEventArgs')
make_head(_module, 'CashDrawerStatus')
make_head(_module, 'CashDrawerStatusUpdatedEventArgs')
make_head(_module, 'ClaimedBarcodeScanner')
make_head(_module, 'ClaimedBarcodeScannerClosedEventArgs')
make_head(_module, 'ClaimedCashDrawer')
make_head(_module, 'ClaimedCashDrawerClosedEventArgs')
make_head(_module, 'ClaimedJournalPrinter')
make_head(_module, 'ClaimedLineDisplay')
make_head(_module, 'ClaimedLineDisplayClosedEventArgs')
make_head(_module, 'ClaimedMagneticStripeReader')
make_head(_module, 'ClaimedMagneticStripeReaderClosedEventArgs')
make_head(_module, 'ClaimedPosPrinter')
make_head(_module, 'ClaimedPosPrinterClosedEventArgs')
make_head(_module, 'ClaimedReceiptPrinter')
make_head(_module, 'ClaimedSlipPrinter')
make_head(_module, 'IBarcodeScanner')
make_head(_module, 'IBarcodeScanner2')
make_head(_module, 'IBarcodeScannerCapabilities')
make_head(_module, 'IBarcodeScannerCapabilities1')
make_head(_module, 'IBarcodeScannerCapabilities2')
make_head(_module, 'IBarcodeScannerDataReceivedEventArgs')
make_head(_module, 'IBarcodeScannerErrorOccurredEventArgs')
make_head(_module, 'IBarcodeScannerImagePreviewReceivedEventArgs')
make_head(_module, 'IBarcodeScannerReport')
make_head(_module, 'IBarcodeScannerReportFactory')
make_head(_module, 'IBarcodeScannerStatics')
make_head(_module, 'IBarcodeScannerStatics2')
make_head(_module, 'IBarcodeScannerStatusUpdatedEventArgs')
make_head(_module, 'IBarcodeSymbologiesStatics')
make_head(_module, 'IBarcodeSymbologiesStatics2')
make_head(_module, 'IBarcodeSymbologyAttributes')
make_head(_module, 'ICashDrawer')
make_head(_module, 'ICashDrawerCapabilities')
make_head(_module, 'ICashDrawerCloseAlarm')
make_head(_module, 'ICashDrawerEventSource')
make_head(_module, 'ICashDrawerEventSourceEventArgs')
make_head(_module, 'ICashDrawerStatics')
make_head(_module, 'ICashDrawerStatics2')
make_head(_module, 'ICashDrawerStatus')
make_head(_module, 'ICashDrawerStatusUpdatedEventArgs')
make_head(_module, 'IClaimedBarcodeScanner')
make_head(_module, 'IClaimedBarcodeScanner1')
make_head(_module, 'IClaimedBarcodeScanner2')
make_head(_module, 'IClaimedBarcodeScanner3')
make_head(_module, 'IClaimedBarcodeScanner4')
make_head(_module, 'IClaimedBarcodeScannerClosedEventArgs')
make_head(_module, 'IClaimedCashDrawer')
make_head(_module, 'IClaimedCashDrawer2')
make_head(_module, 'IClaimedCashDrawerClosedEventArgs')
make_head(_module, 'IClaimedJournalPrinter')
make_head(_module, 'IClaimedLineDisplay')
make_head(_module, 'IClaimedLineDisplay2')
make_head(_module, 'IClaimedLineDisplay3')
make_head(_module, 'IClaimedLineDisplayClosedEventArgs')
make_head(_module, 'IClaimedLineDisplayStatics')
make_head(_module, 'IClaimedMagneticStripeReader')
make_head(_module, 'IClaimedMagneticStripeReader2')
make_head(_module, 'IClaimedMagneticStripeReaderClosedEventArgs')
make_head(_module, 'IClaimedPosPrinter')
make_head(_module, 'IClaimedPosPrinter2')
make_head(_module, 'IClaimedPosPrinterClosedEventArgs')
make_head(_module, 'IClaimedReceiptPrinter')
make_head(_module, 'IClaimedSlipPrinter')
make_head(_module, 'ICommonClaimedPosPrinterStation')
make_head(_module, 'ICommonPosPrintStationCapabilities')
make_head(_module, 'ICommonReceiptSlipCapabilities')
make_head(_module, 'IJournalPrintJob')
make_head(_module, 'IJournalPrinterCapabilities')
make_head(_module, 'IJournalPrinterCapabilities2')
make_head(_module, 'ILineDisplay')
make_head(_module, 'ILineDisplay2')
make_head(_module, 'ILineDisplayAttributes')
make_head(_module, 'ILineDisplayCapabilities')
make_head(_module, 'ILineDisplayCursor')
make_head(_module, 'ILineDisplayCursorAttributes')
make_head(_module, 'ILineDisplayCustomGlyphs')
make_head(_module, 'ILineDisplayMarquee')
make_head(_module, 'ILineDisplayStatics')
make_head(_module, 'ILineDisplayStatics2')
make_head(_module, 'ILineDisplayStatisticsCategorySelector')
make_head(_module, 'ILineDisplayStatusUpdatedEventArgs')
make_head(_module, 'ILineDisplayStoredBitmap')
make_head(_module, 'ILineDisplayWindow')
make_head(_module, 'ILineDisplayWindow2')
make_head(_module, 'IMagneticStripeReader')
make_head(_module, 'IMagneticStripeReaderAamvaCardDataReceivedEventArgs')
make_head(_module, 'IMagneticStripeReaderBankCardDataReceivedEventArgs')
make_head(_module, 'IMagneticStripeReaderCapabilities')
make_head(_module, 'IMagneticStripeReaderCardTypesStatics')
make_head(_module, 'IMagneticStripeReaderEncryptionAlgorithmsStatics')
make_head(_module, 'IMagneticStripeReaderErrorOccurredEventArgs')
make_head(_module, 'IMagneticStripeReaderReport')
make_head(_module, 'IMagneticStripeReaderStatics')
make_head(_module, 'IMagneticStripeReaderStatics2')
make_head(_module, 'IMagneticStripeReaderStatusUpdatedEventArgs')
make_head(_module, 'IMagneticStripeReaderTrackData')
make_head(_module, 'IMagneticStripeReaderVendorSpecificCardDataReceivedEventArgs')
make_head(_module, 'IPosPrinter')
make_head(_module, 'IPosPrinter2')
make_head(_module, 'IPosPrinterCapabilities')
make_head(_module, 'IPosPrinterCharacterSetIdsStatics')
make_head(_module, 'IPosPrinterFontProperty')
make_head(_module, 'IPosPrinterJob')
make_head(_module, 'IPosPrinterPrintOptions')
make_head(_module, 'IPosPrinterReleaseDeviceRequestedEventArgs')
make_head(_module, 'IPosPrinterStatics')
make_head(_module, 'IPosPrinterStatics2')
make_head(_module, 'IPosPrinterStatus')
make_head(_module, 'IPosPrinterStatusUpdatedEventArgs')
make_head(_module, 'IReceiptOrSlipJob')
make_head(_module, 'IReceiptPrintJob')
make_head(_module, 'IReceiptPrintJob2')
make_head(_module, 'IReceiptPrinterCapabilities')
make_head(_module, 'IReceiptPrinterCapabilities2')
make_head(_module, 'ISlipPrintJob')
make_head(_module, 'ISlipPrinterCapabilities')
make_head(_module, 'ISlipPrinterCapabilities2')
make_head(_module, 'IUnifiedPosErrorData')
make_head(_module, 'IUnifiedPosErrorDataFactory')
make_head(_module, 'JournalPrintJob')
make_head(_module, 'JournalPrinterCapabilities')
make_head(_module, 'LineDisplay')
make_head(_module, 'LineDisplayAttributes')
make_head(_module, 'LineDisplayCapabilities')
make_head(_module, 'LineDisplayCursor')
make_head(_module, 'LineDisplayCursorAttributes')
make_head(_module, 'LineDisplayCustomGlyphs')
make_head(_module, 'LineDisplayMarquee')
make_head(_module, 'LineDisplayStatisticsCategorySelector')
make_head(_module, 'LineDisplayStatusUpdatedEventArgs')
make_head(_module, 'LineDisplayStoredBitmap')
make_head(_module, 'LineDisplayWindow')
make_head(_module, 'MagneticStripeReader')
make_head(_module, 'MagneticStripeReaderAamvaCardDataReceivedEventArgs')
make_head(_module, 'MagneticStripeReaderBankCardDataReceivedEventArgs')
make_head(_module, 'MagneticStripeReaderCapabilities')
make_head(_module, 'MagneticStripeReaderCardTypes')
make_head(_module, 'MagneticStripeReaderEncryptionAlgorithms')
make_head(_module, 'MagneticStripeReaderErrorOccurredEventArgs')
make_head(_module, 'MagneticStripeReaderReport')
make_head(_module, 'MagneticStripeReaderStatusUpdatedEventArgs')
make_head(_module, 'MagneticStripeReaderTrackData')
make_head(_module, 'MagneticStripeReaderVendorSpecificCardDataReceivedEventArgs')
make_head(_module, 'PosPrinter')
make_head(_module, 'PosPrinterCapabilities')
make_head(_module, 'PosPrinterCharacterSetIds')
make_head(_module, 'PosPrinterFontProperty')
make_head(_module, 'PosPrinterPrintOptions')
make_head(_module, 'PosPrinterReleaseDeviceRequestedEventArgs')
make_head(_module, 'PosPrinterStatus')
make_head(_module, 'PosPrinterStatusUpdatedEventArgs')
make_head(_module, 'ReceiptPrintJob')
make_head(_module, 'ReceiptPrinterCapabilities')
make_head(_module, 'SizeUInt32')
make_head(_module, 'SlipPrintJob')
make_head(_module, 'SlipPrinterCapabilities')
make_head(_module, 'UnifiedPosErrorData')
