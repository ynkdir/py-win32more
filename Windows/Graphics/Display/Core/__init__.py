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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics.Display.Core
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
HdmiDisplayColorSpace = Int32
HdmiDisplayColorSpace_RgbLimited: HdmiDisplayColorSpace = 0
HdmiDisplayColorSpace_RgbFull: HdmiDisplayColorSpace = 1
HdmiDisplayColorSpace_BT2020: HdmiDisplayColorSpace = 2
HdmiDisplayColorSpace_BT709: HdmiDisplayColorSpace = 3
class HdmiDisplayHdr2086Metadata(EasyCastStructure):
    RedPrimaryX: UInt16
    RedPrimaryY: UInt16
    GreenPrimaryX: UInt16
    GreenPrimaryY: UInt16
    BluePrimaryX: UInt16
    BluePrimaryY: UInt16
    WhitePointX: UInt16
    WhitePointY: UInt16
    MaxMasteringLuminance: UInt16
    MinMasteringLuminance: UInt16
    MaxContentLightLevel: UInt16
    MaxFrameAverageLightLevel: UInt16
HdmiDisplayHdrOption = Int32
HdmiDisplayHdrOption_None: HdmiDisplayHdrOption = 0
HdmiDisplayHdrOption_EotfSdr: HdmiDisplayHdrOption = 1
HdmiDisplayHdrOption_Eotf2084: HdmiDisplayHdrOption = 2
HdmiDisplayHdrOption_DolbyVisionLowLatency: HdmiDisplayHdrOption = 3
class HdmiDisplayInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Display.Core.IHdmiDisplayInformation
    _classid_ = 'Windows.Graphics.Display.Core.HdmiDisplayInformation'
    @winrt_mixinmethod
    def GetSupportedDisplayModes(self: Windows.Graphics.Display.Core.IHdmiDisplayInformation) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Display.Core.HdmiDisplayMode]: ...
    @winrt_mixinmethod
    def GetCurrentDisplayMode(self: Windows.Graphics.Display.Core.IHdmiDisplayInformation) -> Windows.Graphics.Display.Core.HdmiDisplayMode: ...
    @winrt_mixinmethod
    def SetDefaultDisplayModeAsync(self: Windows.Graphics.Display.Core.IHdmiDisplayInformation) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RequestSetCurrentDisplayModeAsync(self: Windows.Graphics.Display.Core.IHdmiDisplayInformation, mode: Windows.Graphics.Display.Core.HdmiDisplayMode) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestSetCurrentDisplayModeWithHdrAsync(self: Windows.Graphics.Display.Core.IHdmiDisplayInformation, mode: Windows.Graphics.Display.Core.HdmiDisplayMode, hdrOption: Windows.Graphics.Display.Core.HdmiDisplayHdrOption) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestSetCurrentDisplayModeWithHdrAndMetadataAsync(self: Windows.Graphics.Display.Core.IHdmiDisplayInformation, mode: Windows.Graphics.Display.Core.HdmiDisplayMode, hdrOption: Windows.Graphics.Display.Core.HdmiDisplayHdrOption, hdrMetadata: Windows.Graphics.Display.Core.HdmiDisplayHdr2086Metadata) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_DisplayModesChanged(self: Windows.Graphics.Display.Core.IHdmiDisplayInformation, value: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.Core.HdmiDisplayInformation, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DisplayModesChanged(self: Windows.Graphics.Display.Core.IHdmiDisplayInformation, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.Graphics.Display.Core.IHdmiDisplayInformationStatics) -> Windows.Graphics.Display.Core.HdmiDisplayInformation: ...
class HdmiDisplayMode(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Graphics.Display.Core.IHdmiDisplayMode
    _classid_ = 'Windows.Graphics.Display.Core.HdmiDisplayMode'
    @winrt_mixinmethod
    def get_ResolutionWidthInRawPixels(self: Windows.Graphics.Display.Core.IHdmiDisplayMode) -> UInt32: ...
    @winrt_mixinmethod
    def get_ResolutionHeightInRawPixels(self: Windows.Graphics.Display.Core.IHdmiDisplayMode) -> UInt32: ...
    @winrt_mixinmethod
    def get_RefreshRate(self: Windows.Graphics.Display.Core.IHdmiDisplayMode) -> Double: ...
    @winrt_mixinmethod
    def get_StereoEnabled(self: Windows.Graphics.Display.Core.IHdmiDisplayMode) -> Boolean: ...
    @winrt_mixinmethod
    def get_BitsPerPixel(self: Windows.Graphics.Display.Core.IHdmiDisplayMode) -> UInt16: ...
    @winrt_mixinmethod
    def IsEqual(self: Windows.Graphics.Display.Core.IHdmiDisplayMode, mode: Windows.Graphics.Display.Core.HdmiDisplayMode) -> Boolean: ...
    @winrt_mixinmethod
    def get_ColorSpace(self: Windows.Graphics.Display.Core.IHdmiDisplayMode) -> Windows.Graphics.Display.Core.HdmiDisplayColorSpace: ...
    @winrt_mixinmethod
    def get_PixelEncoding(self: Windows.Graphics.Display.Core.IHdmiDisplayMode) -> Windows.Graphics.Display.Core.HdmiDisplayPixelEncoding: ...
    @winrt_mixinmethod
    def get_IsSdrLuminanceSupported(self: Windows.Graphics.Display.Core.IHdmiDisplayMode) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSmpte2084Supported(self: Windows.Graphics.Display.Core.IHdmiDisplayMode) -> Boolean: ...
    @winrt_mixinmethod
    def get_Is2086MetadataSupported(self: Windows.Graphics.Display.Core.IHdmiDisplayMode) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDolbyVisionLowLatencySupported(self: Windows.Graphics.Display.Core.IHdmiDisplayMode2) -> Boolean: ...
    ResolutionWidthInRawPixels = property(get_ResolutionWidthInRawPixels, None)
    ResolutionHeightInRawPixels = property(get_ResolutionHeightInRawPixels, None)
    RefreshRate = property(get_RefreshRate, None)
    StereoEnabled = property(get_StereoEnabled, None)
    BitsPerPixel = property(get_BitsPerPixel, None)
    ColorSpace = property(get_ColorSpace, None)
    PixelEncoding = property(get_PixelEncoding, None)
    IsSdrLuminanceSupported = property(get_IsSdrLuminanceSupported, None)
    IsSmpte2084Supported = property(get_IsSmpte2084Supported, None)
    Is2086MetadataSupported = property(get_Is2086MetadataSupported, None)
    IsDolbyVisionLowLatencySupported = property(get_IsDolbyVisionLowLatencySupported, None)
HdmiDisplayPixelEncoding = Int32
HdmiDisplayPixelEncoding_Rgb444: HdmiDisplayPixelEncoding = 0
HdmiDisplayPixelEncoding_Ycc444: HdmiDisplayPixelEncoding = 1
HdmiDisplayPixelEncoding_Ycc422: HdmiDisplayPixelEncoding = 2
HdmiDisplayPixelEncoding_Ycc420: HdmiDisplayPixelEncoding = 3
class IHdmiDisplayInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.Core.IHdmiDisplayInformation'
    _iid_ = Guid('{130b3c0a-f565-476e-abd5-ea05aee74c69}')
    @winrt_commethod(6)
    def GetSupportedDisplayModes(self) -> Windows.Foundation.Collections.IVectorView[Windows.Graphics.Display.Core.HdmiDisplayMode]: ...
    @winrt_commethod(7)
    def GetCurrentDisplayMode(self) -> Windows.Graphics.Display.Core.HdmiDisplayMode: ...
    @winrt_commethod(8)
    def SetDefaultDisplayModeAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def RequestSetCurrentDisplayModeAsync(self, mode: Windows.Graphics.Display.Core.HdmiDisplayMode) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(10)
    def RequestSetCurrentDisplayModeWithHdrAsync(self, mode: Windows.Graphics.Display.Core.HdmiDisplayMode, hdrOption: Windows.Graphics.Display.Core.HdmiDisplayHdrOption) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(11)
    def RequestSetCurrentDisplayModeWithHdrAndMetadataAsync(self, mode: Windows.Graphics.Display.Core.HdmiDisplayMode, hdrOption: Windows.Graphics.Display.Core.HdmiDisplayHdrOption, hdrMetadata: Windows.Graphics.Display.Core.HdmiDisplayHdr2086Metadata) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(12)
    def add_DisplayModesChanged(self, value: Windows.Foundation.TypedEventHandler[Windows.Graphics.Display.Core.HdmiDisplayInformation, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_DisplayModesChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IHdmiDisplayInformationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.Core.IHdmiDisplayInformationStatics'
    _iid_ = Guid('{6ce6b260-f42a-4a15-914c-7b8e2a5a65df}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.Graphics.Display.Core.HdmiDisplayInformation: ...
class IHdmiDisplayMode(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.Core.IHdmiDisplayMode'
    _iid_ = Guid('{0c06d5ad-1b90-4f51-9981-ef5a1c0ddf66}')
    @winrt_commethod(6)
    def get_ResolutionWidthInRawPixels(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_ResolutionHeightInRawPixels(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_RefreshRate(self) -> Double: ...
    @winrt_commethod(9)
    def get_StereoEnabled(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_BitsPerPixel(self) -> UInt16: ...
    @winrt_commethod(11)
    def IsEqual(self, mode: Windows.Graphics.Display.Core.HdmiDisplayMode) -> Boolean: ...
    @winrt_commethod(12)
    def get_ColorSpace(self) -> Windows.Graphics.Display.Core.HdmiDisplayColorSpace: ...
    @winrt_commethod(13)
    def get_PixelEncoding(self) -> Windows.Graphics.Display.Core.HdmiDisplayPixelEncoding: ...
    @winrt_commethod(14)
    def get_IsSdrLuminanceSupported(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_IsSmpte2084Supported(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_Is2086MetadataSupported(self) -> Boolean: ...
    ResolutionWidthInRawPixels = property(get_ResolutionWidthInRawPixels, None)
    ResolutionHeightInRawPixels = property(get_ResolutionHeightInRawPixels, None)
    RefreshRate = property(get_RefreshRate, None)
    StereoEnabled = property(get_StereoEnabled, None)
    BitsPerPixel = property(get_BitsPerPixel, None)
    ColorSpace = property(get_ColorSpace, None)
    PixelEncoding = property(get_PixelEncoding, None)
    IsSdrLuminanceSupported = property(get_IsSdrLuminanceSupported, None)
    IsSmpte2084Supported = property(get_IsSmpte2084Supported, None)
    Is2086MetadataSupported = property(get_Is2086MetadataSupported, None)
class IHdmiDisplayMode2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.Core.IHdmiDisplayMode2'
    _iid_ = Guid('{07cd4e9f-4b3c-42b8-84e7-895368718af2}')
    @winrt_commethod(6)
    def get_IsDolbyVisionLowLatencySupported(self) -> Boolean: ...
    IsDolbyVisionLowLatencySupported = property(get_IsDolbyVisionLowLatencySupported, None)
make_head(_module, 'HdmiDisplayHdr2086Metadata')
make_head(_module, 'HdmiDisplayInformation')
make_head(_module, 'HdmiDisplayMode')
make_head(_module, 'IHdmiDisplayInformation')
make_head(_module, 'IHdmiDisplayInformationStatics')
make_head(_module, 'IHdmiDisplayMode')
make_head(_module, 'IHdmiDisplayMode2')
