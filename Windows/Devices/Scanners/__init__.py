from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Devices.Scanners
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics.Printing
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
class IImageScanner(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Scanners.IImageScanner'
    _iid_ = Guid('{53a88f78-5298-48a0-8da3-8087519665e0}')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_DefaultScanSource(self) -> Windows.Devices.Scanners.ImageScannerScanSource: ...
    @winrt_commethod(8)
    def IsScanSourceSupported(self, value: Windows.Devices.Scanners.ImageScannerScanSource) -> Boolean: ...
    @winrt_commethod(9)
    def get_FlatbedConfiguration(self) -> Windows.Devices.Scanners.ImageScannerFlatbedConfiguration: ...
    @winrt_commethod(10)
    def get_FeederConfiguration(self) -> Windows.Devices.Scanners.ImageScannerFeederConfiguration: ...
    @winrt_commethod(11)
    def get_AutoConfiguration(self) -> Windows.Devices.Scanners.ImageScannerAutoConfiguration: ...
    @winrt_commethod(12)
    def IsPreviewSupported(self, scanSource: Windows.Devices.Scanners.ImageScannerScanSource) -> Boolean: ...
    @winrt_commethod(13)
    def ScanPreviewToStreamAsync(self, scanSource: Windows.Devices.Scanners.ImageScannerScanSource, targetStream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Scanners.ImageScannerPreviewResult]: ...
    @winrt_commethod(14)
    def ScanFilesToFolderAsync(self, scanSource: Windows.Devices.Scanners.ImageScannerScanSource, storageFolder: Windows.Storage.StorageFolder) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Devices.Scanners.ImageScannerScanResult, UInt32]: ...
    DeviceId = property(get_DeviceId, None)
    DefaultScanSource = property(get_DefaultScanSource, None)
    FlatbedConfiguration = property(get_FlatbedConfiguration, None)
    FeederConfiguration = property(get_FeederConfiguration, None)
    AutoConfiguration = property(get_AutoConfiguration, None)
class IImageScannerFeederConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Scanners.IImageScannerFeederConfiguration'
    _iid_ = Guid('{74bdacee-fa97-4c17-8280-40e39c6dcc67}')
    @winrt_commethod(6)
    def get_CanAutoDetectPageSize(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_AutoDetectPageSize(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_AutoDetectPageSize(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_PageSize(self) -> Windows.Graphics.Printing.PrintMediaSize: ...
    @winrt_commethod(10)
    def put_PageSize(self, value: Windows.Graphics.Printing.PrintMediaSize) -> Void: ...
    @winrt_commethod(11)
    def get_PageOrientation(self) -> Windows.Graphics.Printing.PrintOrientation: ...
    @winrt_commethod(12)
    def put_PageOrientation(self, value: Windows.Graphics.Printing.PrintOrientation) -> Void: ...
    @winrt_commethod(13)
    def get_PageSizeDimensions(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(14)
    def IsPageSizeSupported(self, pageSize: Windows.Graphics.Printing.PrintMediaSize, pageOrientation: Windows.Graphics.Printing.PrintOrientation) -> Boolean: ...
    @winrt_commethod(15)
    def get_MaxNumberOfPages(self) -> UInt32: ...
    @winrt_commethod(16)
    def put_MaxNumberOfPages(self, value: UInt32) -> Void: ...
    @winrt_commethod(17)
    def get_CanScanDuplex(self) -> Boolean: ...
    @winrt_commethod(18)
    def get_Duplex(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_Duplex(self, value: Boolean) -> Void: ...
    @winrt_commethod(20)
    def get_CanScanAhead(self) -> Boolean: ...
    @winrt_commethod(21)
    def get_ScanAhead(self) -> Boolean: ...
    @winrt_commethod(22)
    def put_ScanAhead(self, value: Boolean) -> Void: ...
    CanAutoDetectPageSize = property(get_CanAutoDetectPageSize, None)
    AutoDetectPageSize = property(get_AutoDetectPageSize, put_AutoDetectPageSize)
    PageSize = property(get_PageSize, put_PageSize)
    PageOrientation = property(get_PageOrientation, put_PageOrientation)
    PageSizeDimensions = property(get_PageSizeDimensions, None)
    MaxNumberOfPages = property(get_MaxNumberOfPages, put_MaxNumberOfPages)
    CanScanDuplex = property(get_CanScanDuplex, None)
    Duplex = property(get_Duplex, put_Duplex)
    CanScanAhead = property(get_CanScanAhead, None)
    ScanAhead = property(get_ScanAhead, put_ScanAhead)
class IImageScannerFormatConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Scanners.IImageScannerFormatConfiguration'
    _iid_ = Guid('{ae275d11-dadf-4010-bf10-cca5c83dcbb0}')
    @winrt_commethod(6)
    def get_DefaultFormat(self) -> Windows.Devices.Scanners.ImageScannerFormat: ...
    @winrt_commethod(7)
    def get_Format(self) -> Windows.Devices.Scanners.ImageScannerFormat: ...
    @winrt_commethod(8)
    def put_Format(self, value: Windows.Devices.Scanners.ImageScannerFormat) -> Void: ...
    @winrt_commethod(9)
    def IsFormatSupported(self, value: Windows.Devices.Scanners.ImageScannerFormat) -> Boolean: ...
    DefaultFormat = property(get_DefaultFormat, None)
    Format = property(get_Format, put_Format)
class IImageScannerPreviewResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Scanners.IImageScannerPreviewResult'
    _iid_ = Guid('{08b7fe8e-8891-441d-be9c-176fa109c8bb}')
    @winrt_commethod(6)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Format(self) -> Windows.Devices.Scanners.ImageScannerFormat: ...
    Succeeded = property(get_Succeeded, None)
    Format = property(get_Format, None)
class IImageScannerScanResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Scanners.IImageScannerScanResult'
    _iid_ = Guid('{c91624cd-9037-4e48-84c1-ac0975076bc5}')
    @winrt_commethod(6)
    def get_ScannedFiles(self) -> Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFile]: ...
    ScannedFiles = property(get_ScannedFiles, None)
class IImageScannerSourceConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Scanners.IImageScannerSourceConfiguration'
    _iid_ = Guid('{bfb50055-0b44-4c82-9e89-205f9c234e59}')
    @winrt_commethod(6)
    def get_MinScanArea(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(7)
    def get_MaxScanArea(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(8)
    def get_SelectedScanRegion(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def put_SelectedScanRegion(self, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(10)
    def get_AutoCroppingMode(self) -> Windows.Devices.Scanners.ImageScannerAutoCroppingMode: ...
    @winrt_commethod(11)
    def put_AutoCroppingMode(self, value: Windows.Devices.Scanners.ImageScannerAutoCroppingMode) -> Void: ...
    @winrt_commethod(12)
    def IsAutoCroppingModeSupported(self, value: Windows.Devices.Scanners.ImageScannerAutoCroppingMode) -> Boolean: ...
    @winrt_commethod(13)
    def get_MinResolution(self) -> Windows.Devices.Scanners.ImageScannerResolution: ...
    @winrt_commethod(14)
    def get_MaxResolution(self) -> Windows.Devices.Scanners.ImageScannerResolution: ...
    @winrt_commethod(15)
    def get_OpticalResolution(self) -> Windows.Devices.Scanners.ImageScannerResolution: ...
    @winrt_commethod(16)
    def get_DesiredResolution(self) -> Windows.Devices.Scanners.ImageScannerResolution: ...
    @winrt_commethod(17)
    def put_DesiredResolution(self, value: Windows.Devices.Scanners.ImageScannerResolution) -> Void: ...
    @winrt_commethod(18)
    def get_ActualResolution(self) -> Windows.Devices.Scanners.ImageScannerResolution: ...
    @winrt_commethod(19)
    def get_DefaultColorMode(self) -> Windows.Devices.Scanners.ImageScannerColorMode: ...
    @winrt_commethod(20)
    def get_ColorMode(self) -> Windows.Devices.Scanners.ImageScannerColorMode: ...
    @winrt_commethod(21)
    def put_ColorMode(self, value: Windows.Devices.Scanners.ImageScannerColorMode) -> Void: ...
    @winrt_commethod(22)
    def IsColorModeSupported(self, value: Windows.Devices.Scanners.ImageScannerColorMode) -> Boolean: ...
    @winrt_commethod(23)
    def get_MinBrightness(self) -> Int32: ...
    @winrt_commethod(24)
    def get_MaxBrightness(self) -> Int32: ...
    @winrt_commethod(25)
    def get_BrightnessStep(self) -> UInt32: ...
    @winrt_commethod(26)
    def get_DefaultBrightness(self) -> Int32: ...
    @winrt_commethod(27)
    def get_Brightness(self) -> Int32: ...
    @winrt_commethod(28)
    def put_Brightness(self, value: Int32) -> Void: ...
    @winrt_commethod(29)
    def get_MinContrast(self) -> Int32: ...
    @winrt_commethod(30)
    def get_MaxContrast(self) -> Int32: ...
    @winrt_commethod(31)
    def get_ContrastStep(self) -> UInt32: ...
    @winrt_commethod(32)
    def get_DefaultContrast(self) -> Int32: ...
    @winrt_commethod(33)
    def get_Contrast(self) -> Int32: ...
    @winrt_commethod(34)
    def put_Contrast(self, value: Int32) -> Void: ...
    MinScanArea = property(get_MinScanArea, None)
    MaxScanArea = property(get_MaxScanArea, None)
    SelectedScanRegion = property(get_SelectedScanRegion, put_SelectedScanRegion)
    AutoCroppingMode = property(get_AutoCroppingMode, put_AutoCroppingMode)
    MinResolution = property(get_MinResolution, None)
    MaxResolution = property(get_MaxResolution, None)
    OpticalResolution = property(get_OpticalResolution, None)
    DesiredResolution = property(get_DesiredResolution, put_DesiredResolution)
    ActualResolution = property(get_ActualResolution, None)
    DefaultColorMode = property(get_DefaultColorMode, None)
    ColorMode = property(get_ColorMode, put_ColorMode)
    MinBrightness = property(get_MinBrightness, None)
    MaxBrightness = property(get_MaxBrightness, None)
    BrightnessStep = property(get_BrightnessStep, None)
    DefaultBrightness = property(get_DefaultBrightness, None)
    Brightness = property(get_Brightness, put_Brightness)
    MinContrast = property(get_MinContrast, None)
    MaxContrast = property(get_MaxContrast, None)
    ContrastStep = property(get_ContrastStep, None)
    DefaultContrast = property(get_DefaultContrast, None)
    Contrast = property(get_Contrast, put_Contrast)
class IImageScannerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Scanners.IImageScannerStatics'
    _iid_ = Guid('{bc57e70e-d804-4477-9fb5-b911b5473897}')
    @winrt_commethod(6)
    def FromIdAsync(self, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Scanners.ImageScanner]: ...
    @winrt_commethod(7)
    def GetDeviceSelector(self) -> WinRT_String: ...
class ImageScanner(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Scanners.IImageScanner
    _classid_ = 'Windows.Devices.Scanners.ImageScanner'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Scanners.IImageScanner) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DefaultScanSource(self: Windows.Devices.Scanners.IImageScanner) -> Windows.Devices.Scanners.ImageScannerScanSource: ...
    @winrt_mixinmethod
    def IsScanSourceSupported(self: Windows.Devices.Scanners.IImageScanner, value: Windows.Devices.Scanners.ImageScannerScanSource) -> Boolean: ...
    @winrt_mixinmethod
    def get_FlatbedConfiguration(self: Windows.Devices.Scanners.IImageScanner) -> Windows.Devices.Scanners.ImageScannerFlatbedConfiguration: ...
    @winrt_mixinmethod
    def get_FeederConfiguration(self: Windows.Devices.Scanners.IImageScanner) -> Windows.Devices.Scanners.ImageScannerFeederConfiguration: ...
    @winrt_mixinmethod
    def get_AutoConfiguration(self: Windows.Devices.Scanners.IImageScanner) -> Windows.Devices.Scanners.ImageScannerAutoConfiguration: ...
    @winrt_mixinmethod
    def IsPreviewSupported(self: Windows.Devices.Scanners.IImageScanner, scanSource: Windows.Devices.Scanners.ImageScannerScanSource) -> Boolean: ...
    @winrt_mixinmethod
    def ScanPreviewToStreamAsync(self: Windows.Devices.Scanners.IImageScanner, scanSource: Windows.Devices.Scanners.ImageScannerScanSource, targetStream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Scanners.ImageScannerPreviewResult]: ...
    @winrt_mixinmethod
    def ScanFilesToFolderAsync(self: Windows.Devices.Scanners.IImageScanner, scanSource: Windows.Devices.Scanners.ImageScannerScanSource, storageFolder: Windows.Storage.StorageFolder) -> Windows.Foundation.IAsyncOperationWithProgress[Windows.Devices.Scanners.ImageScannerScanResult, UInt32]: ...
    @winrt_classmethod
    def FromIdAsync(cls: Windows.Devices.Scanners.IImageScannerStatics, deviceId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Scanners.ImageScanner]: ...
    @winrt_classmethod
    def GetDeviceSelector(cls: Windows.Devices.Scanners.IImageScannerStatics) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    DefaultScanSource = property(get_DefaultScanSource, None)
    FlatbedConfiguration = property(get_FlatbedConfiguration, None)
    FeederConfiguration = property(get_FeederConfiguration, None)
    AutoConfiguration = property(get_AutoConfiguration, None)
class ImageScannerAutoConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Scanners.IImageScannerFormatConfiguration
    _classid_ = 'Windows.Devices.Scanners.ImageScannerAutoConfiguration'
    @winrt_mixinmethod
    def get_DefaultFormat(self: Windows.Devices.Scanners.IImageScannerFormatConfiguration) -> Windows.Devices.Scanners.ImageScannerFormat: ...
    @winrt_mixinmethod
    def get_Format(self: Windows.Devices.Scanners.IImageScannerFormatConfiguration) -> Windows.Devices.Scanners.ImageScannerFormat: ...
    @winrt_mixinmethod
    def put_Format(self: Windows.Devices.Scanners.IImageScannerFormatConfiguration, value: Windows.Devices.Scanners.ImageScannerFormat) -> Void: ...
    @winrt_mixinmethod
    def IsFormatSupported(self: Windows.Devices.Scanners.IImageScannerFormatConfiguration, value: Windows.Devices.Scanners.ImageScannerFormat) -> Boolean: ...
    DefaultFormat = property(get_DefaultFormat, None)
    Format = property(get_Format, put_Format)
ImageScannerAutoCroppingMode = Int32
ImageScannerAutoCroppingMode_Disabled: ImageScannerAutoCroppingMode = 0
ImageScannerAutoCroppingMode_SingleRegion: ImageScannerAutoCroppingMode = 1
ImageScannerAutoCroppingMode_MultipleRegion: ImageScannerAutoCroppingMode = 2
ImageScannerColorMode = Int32
ImageScannerColorMode_Color: ImageScannerColorMode = 0
ImageScannerColorMode_Grayscale: ImageScannerColorMode = 1
ImageScannerColorMode_Monochrome: ImageScannerColorMode = 2
ImageScannerColorMode_AutoColor: ImageScannerColorMode = 3
class ImageScannerFeederConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Scanners.IImageScannerFormatConfiguration
    _classid_ = 'Windows.Devices.Scanners.ImageScannerFeederConfiguration'
    @winrt_mixinmethod
    def get_DefaultFormat(self: Windows.Devices.Scanners.IImageScannerFormatConfiguration) -> Windows.Devices.Scanners.ImageScannerFormat: ...
    @winrt_mixinmethod
    def get_Format(self: Windows.Devices.Scanners.IImageScannerFormatConfiguration) -> Windows.Devices.Scanners.ImageScannerFormat: ...
    @winrt_mixinmethod
    def put_Format(self: Windows.Devices.Scanners.IImageScannerFormatConfiguration, value: Windows.Devices.Scanners.ImageScannerFormat) -> Void: ...
    @winrt_mixinmethod
    def IsFormatSupported(self: Windows.Devices.Scanners.IImageScannerFormatConfiguration, value: Windows.Devices.Scanners.ImageScannerFormat) -> Boolean: ...
    @winrt_mixinmethod
    def get_MinScanArea(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_MaxScanArea(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_SelectedScanRegion(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_SelectedScanRegion(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_AutoCroppingMode(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Devices.Scanners.ImageScannerAutoCroppingMode: ...
    @winrt_mixinmethod
    def put_AutoCroppingMode(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration, value: Windows.Devices.Scanners.ImageScannerAutoCroppingMode) -> Void: ...
    @winrt_mixinmethod
    def IsAutoCroppingModeSupported(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration, value: Windows.Devices.Scanners.ImageScannerAutoCroppingMode) -> Boolean: ...
    @winrt_mixinmethod
    def get_MinResolution(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Devices.Scanners.ImageScannerResolution: ...
    @winrt_mixinmethod
    def get_MaxResolution(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Devices.Scanners.ImageScannerResolution: ...
    @winrt_mixinmethod
    def get_OpticalResolution(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Devices.Scanners.ImageScannerResolution: ...
    @winrt_mixinmethod
    def get_DesiredResolution(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Devices.Scanners.ImageScannerResolution: ...
    @winrt_mixinmethod
    def put_DesiredResolution(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration, value: Windows.Devices.Scanners.ImageScannerResolution) -> Void: ...
    @winrt_mixinmethod
    def get_ActualResolution(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Devices.Scanners.ImageScannerResolution: ...
    @winrt_mixinmethod
    def get_DefaultColorMode(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Devices.Scanners.ImageScannerColorMode: ...
    @winrt_mixinmethod
    def get_ColorMode(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Devices.Scanners.ImageScannerColorMode: ...
    @winrt_mixinmethod
    def put_ColorMode(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration, value: Windows.Devices.Scanners.ImageScannerColorMode) -> Void: ...
    @winrt_mixinmethod
    def IsColorModeSupported(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration, value: Windows.Devices.Scanners.ImageScannerColorMode) -> Boolean: ...
    @winrt_mixinmethod
    def get_MinBrightness(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxBrightness(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_BrightnessStep(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> UInt32: ...
    @winrt_mixinmethod
    def get_DefaultBrightness(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_Brightness(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def put_Brightness(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_MinContrast(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxContrast(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_ContrastStep(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> UInt32: ...
    @winrt_mixinmethod
    def get_DefaultContrast(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_Contrast(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def put_Contrast(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_CanAutoDetectPageSize(self: Windows.Devices.Scanners.IImageScannerFeederConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def get_AutoDetectPageSize(self: Windows.Devices.Scanners.IImageScannerFeederConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoDetectPageSize(self: Windows.Devices.Scanners.IImageScannerFeederConfiguration, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PageSize(self: Windows.Devices.Scanners.IImageScannerFeederConfiguration) -> Windows.Graphics.Printing.PrintMediaSize: ...
    @winrt_mixinmethod
    def put_PageSize(self: Windows.Devices.Scanners.IImageScannerFeederConfiguration, value: Windows.Graphics.Printing.PrintMediaSize) -> Void: ...
    @winrt_mixinmethod
    def get_PageOrientation(self: Windows.Devices.Scanners.IImageScannerFeederConfiguration) -> Windows.Graphics.Printing.PrintOrientation: ...
    @winrt_mixinmethod
    def put_PageOrientation(self: Windows.Devices.Scanners.IImageScannerFeederConfiguration, value: Windows.Graphics.Printing.PrintOrientation) -> Void: ...
    @winrt_mixinmethod
    def get_PageSizeDimensions(self: Windows.Devices.Scanners.IImageScannerFeederConfiguration) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def IsPageSizeSupported(self: Windows.Devices.Scanners.IImageScannerFeederConfiguration, pageSize: Windows.Graphics.Printing.PrintMediaSize, pageOrientation: Windows.Graphics.Printing.PrintOrientation) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxNumberOfPages(self: Windows.Devices.Scanners.IImageScannerFeederConfiguration) -> UInt32: ...
    @winrt_mixinmethod
    def put_MaxNumberOfPages(self: Windows.Devices.Scanners.IImageScannerFeederConfiguration, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_CanScanDuplex(self: Windows.Devices.Scanners.IImageScannerFeederConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def get_Duplex(self: Windows.Devices.Scanners.IImageScannerFeederConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def put_Duplex(self: Windows.Devices.Scanners.IImageScannerFeederConfiguration, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CanScanAhead(self: Windows.Devices.Scanners.IImageScannerFeederConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def get_ScanAhead(self: Windows.Devices.Scanners.IImageScannerFeederConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def put_ScanAhead(self: Windows.Devices.Scanners.IImageScannerFeederConfiguration, value: Boolean) -> Void: ...
    DefaultFormat = property(get_DefaultFormat, None)
    Format = property(get_Format, put_Format)
    MinScanArea = property(get_MinScanArea, None)
    MaxScanArea = property(get_MaxScanArea, None)
    SelectedScanRegion = property(get_SelectedScanRegion, put_SelectedScanRegion)
    AutoCroppingMode = property(get_AutoCroppingMode, put_AutoCroppingMode)
    MinResolution = property(get_MinResolution, None)
    MaxResolution = property(get_MaxResolution, None)
    OpticalResolution = property(get_OpticalResolution, None)
    DesiredResolution = property(get_DesiredResolution, put_DesiredResolution)
    ActualResolution = property(get_ActualResolution, None)
    DefaultColorMode = property(get_DefaultColorMode, None)
    ColorMode = property(get_ColorMode, put_ColorMode)
    MinBrightness = property(get_MinBrightness, None)
    MaxBrightness = property(get_MaxBrightness, None)
    BrightnessStep = property(get_BrightnessStep, None)
    DefaultBrightness = property(get_DefaultBrightness, None)
    Brightness = property(get_Brightness, put_Brightness)
    MinContrast = property(get_MinContrast, None)
    MaxContrast = property(get_MaxContrast, None)
    ContrastStep = property(get_ContrastStep, None)
    DefaultContrast = property(get_DefaultContrast, None)
    Contrast = property(get_Contrast, put_Contrast)
    CanAutoDetectPageSize = property(get_CanAutoDetectPageSize, None)
    AutoDetectPageSize = property(get_AutoDetectPageSize, put_AutoDetectPageSize)
    PageSize = property(get_PageSize, put_PageSize)
    PageOrientation = property(get_PageOrientation, put_PageOrientation)
    PageSizeDimensions = property(get_PageSizeDimensions, None)
    MaxNumberOfPages = property(get_MaxNumberOfPages, put_MaxNumberOfPages)
    CanScanDuplex = property(get_CanScanDuplex, None)
    Duplex = property(get_Duplex, put_Duplex)
    CanScanAhead = property(get_CanScanAhead, None)
    ScanAhead = property(get_ScanAhead, put_ScanAhead)
class ImageScannerFlatbedConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Scanners.IImageScannerFormatConfiguration
    _classid_ = 'Windows.Devices.Scanners.ImageScannerFlatbedConfiguration'
    @winrt_mixinmethod
    def get_DefaultFormat(self: Windows.Devices.Scanners.IImageScannerFormatConfiguration) -> Windows.Devices.Scanners.ImageScannerFormat: ...
    @winrt_mixinmethod
    def get_Format(self: Windows.Devices.Scanners.IImageScannerFormatConfiguration) -> Windows.Devices.Scanners.ImageScannerFormat: ...
    @winrt_mixinmethod
    def put_Format(self: Windows.Devices.Scanners.IImageScannerFormatConfiguration, value: Windows.Devices.Scanners.ImageScannerFormat) -> Void: ...
    @winrt_mixinmethod
    def IsFormatSupported(self: Windows.Devices.Scanners.IImageScannerFormatConfiguration, value: Windows.Devices.Scanners.ImageScannerFormat) -> Boolean: ...
    @winrt_mixinmethod
    def get_MinScanArea(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_MaxScanArea(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_SelectedScanRegion(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_SelectedScanRegion(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_AutoCroppingMode(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Devices.Scanners.ImageScannerAutoCroppingMode: ...
    @winrt_mixinmethod
    def put_AutoCroppingMode(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration, value: Windows.Devices.Scanners.ImageScannerAutoCroppingMode) -> Void: ...
    @winrt_mixinmethod
    def IsAutoCroppingModeSupported(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration, value: Windows.Devices.Scanners.ImageScannerAutoCroppingMode) -> Boolean: ...
    @winrt_mixinmethod
    def get_MinResolution(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Devices.Scanners.ImageScannerResolution: ...
    @winrt_mixinmethod
    def get_MaxResolution(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Devices.Scanners.ImageScannerResolution: ...
    @winrt_mixinmethod
    def get_OpticalResolution(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Devices.Scanners.ImageScannerResolution: ...
    @winrt_mixinmethod
    def get_DesiredResolution(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Devices.Scanners.ImageScannerResolution: ...
    @winrt_mixinmethod
    def put_DesiredResolution(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration, value: Windows.Devices.Scanners.ImageScannerResolution) -> Void: ...
    @winrt_mixinmethod
    def get_ActualResolution(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Devices.Scanners.ImageScannerResolution: ...
    @winrt_mixinmethod
    def get_DefaultColorMode(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Devices.Scanners.ImageScannerColorMode: ...
    @winrt_mixinmethod
    def get_ColorMode(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Windows.Devices.Scanners.ImageScannerColorMode: ...
    @winrt_mixinmethod
    def put_ColorMode(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration, value: Windows.Devices.Scanners.ImageScannerColorMode) -> Void: ...
    @winrt_mixinmethod
    def IsColorModeSupported(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration, value: Windows.Devices.Scanners.ImageScannerColorMode) -> Boolean: ...
    @winrt_mixinmethod
    def get_MinBrightness(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxBrightness(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_BrightnessStep(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> UInt32: ...
    @winrt_mixinmethod
    def get_DefaultBrightness(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_Brightness(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def put_Brightness(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_MinContrast(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_MaxContrast(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_ContrastStep(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> UInt32: ...
    @winrt_mixinmethod
    def get_DefaultContrast(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def get_Contrast(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration) -> Int32: ...
    @winrt_mixinmethod
    def put_Contrast(self: Windows.Devices.Scanners.IImageScannerSourceConfiguration, value: Int32) -> Void: ...
    DefaultFormat = property(get_DefaultFormat, None)
    Format = property(get_Format, put_Format)
    MinScanArea = property(get_MinScanArea, None)
    MaxScanArea = property(get_MaxScanArea, None)
    SelectedScanRegion = property(get_SelectedScanRegion, put_SelectedScanRegion)
    AutoCroppingMode = property(get_AutoCroppingMode, put_AutoCroppingMode)
    MinResolution = property(get_MinResolution, None)
    MaxResolution = property(get_MaxResolution, None)
    OpticalResolution = property(get_OpticalResolution, None)
    DesiredResolution = property(get_DesiredResolution, put_DesiredResolution)
    ActualResolution = property(get_ActualResolution, None)
    DefaultColorMode = property(get_DefaultColorMode, None)
    ColorMode = property(get_ColorMode, put_ColorMode)
    MinBrightness = property(get_MinBrightness, None)
    MaxBrightness = property(get_MaxBrightness, None)
    BrightnessStep = property(get_BrightnessStep, None)
    DefaultBrightness = property(get_DefaultBrightness, None)
    Brightness = property(get_Brightness, put_Brightness)
    MinContrast = property(get_MinContrast, None)
    MaxContrast = property(get_MaxContrast, None)
    ContrastStep = property(get_ContrastStep, None)
    DefaultContrast = property(get_DefaultContrast, None)
    Contrast = property(get_Contrast, put_Contrast)
ImageScannerFormat = Int32
ImageScannerFormat_Jpeg: ImageScannerFormat = 0
ImageScannerFormat_Png: ImageScannerFormat = 1
ImageScannerFormat_DeviceIndependentBitmap: ImageScannerFormat = 2
ImageScannerFormat_Tiff: ImageScannerFormat = 3
ImageScannerFormat_Xps: ImageScannerFormat = 4
ImageScannerFormat_OpenXps: ImageScannerFormat = 5
ImageScannerFormat_Pdf: ImageScannerFormat = 6
class ImageScannerPreviewResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Scanners.IImageScannerPreviewResult
    _classid_ = 'Windows.Devices.Scanners.ImageScannerPreviewResult'
    @winrt_mixinmethod
    def get_Succeeded(self: Windows.Devices.Scanners.IImageScannerPreviewResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_Format(self: Windows.Devices.Scanners.IImageScannerPreviewResult) -> Windows.Devices.Scanners.ImageScannerFormat: ...
    Succeeded = property(get_Succeeded, None)
    Format = property(get_Format, None)
class ImageScannerResolution(EasyCastStructure):
    DpiX: Single
    DpiY: Single
class ImageScannerScanResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Scanners.IImageScannerScanResult
    _classid_ = 'Windows.Devices.Scanners.ImageScannerScanResult'
    @winrt_mixinmethod
    def get_ScannedFiles(self: Windows.Devices.Scanners.IImageScannerScanResult) -> Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFile]: ...
    ScannedFiles = property(get_ScannedFiles, None)
ImageScannerScanSource = Int32
ImageScannerScanSource_Default: ImageScannerScanSource = 0
ImageScannerScanSource_Flatbed: ImageScannerScanSource = 1
ImageScannerScanSource_Feeder: ImageScannerScanSource = 2
ImageScannerScanSource_AutoConfigured: ImageScannerScanSource = 3
ScannerDeviceContract: UInt32 = 65536
make_head(_module, 'IImageScanner')
make_head(_module, 'IImageScannerFeederConfiguration')
make_head(_module, 'IImageScannerFormatConfiguration')
make_head(_module, 'IImageScannerPreviewResult')
make_head(_module, 'IImageScannerScanResult')
make_head(_module, 'IImageScannerSourceConfiguration')
make_head(_module, 'IImageScannerStatics')
make_head(_module, 'ImageScanner')
make_head(_module, 'ImageScannerAutoConfiguration')
make_head(_module, 'ImageScannerFeederConfiguration')
make_head(_module, 'ImageScannerFlatbedConfiguration')
make_head(_module, 'ImageScannerPreviewResult')
make_head(_module, 'ImageScannerResolution')
make_head(_module, 'ImageScannerScanResult')
