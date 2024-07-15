from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics.Display.Core
import win32more.Windows.Win32.System.WinRT
class HdmiDisplayColorSpace(Enum, Int32):
    RgbLimited = 0
    RgbFull = 1
    BT2020 = 2
    BT709 = 3
class HdmiDisplayHdr2086Metadata(Structure):
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
class HdmiDisplayHdrOption(Enum, Int32):
    None_ = 0
    EotfSdr = 1
    Eotf2084 = 2
    DolbyVisionLowLatency = 3
class HdmiDisplayInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Display.Core.IHdmiDisplayInformation
    _classid_ = 'Windows.Graphics.Display.Core.HdmiDisplayInformation'
    @winrt_mixinmethod
    def GetSupportedDisplayModes(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayInformation) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Display.Core.HdmiDisplayMode]: ...
    @winrt_mixinmethod
    def GetCurrentDisplayMode(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayInformation) -> win32more.Windows.Graphics.Display.Core.HdmiDisplayMode: ...
    @winrt_mixinmethod
    def SetDefaultDisplayModeAsync(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayInformation) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def RequestSetCurrentDisplayModeAsync(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayInformation, mode: win32more.Windows.Graphics.Display.Core.HdmiDisplayMode) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestSetCurrentDisplayModeWithHdrAsync(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayInformation, mode: win32more.Windows.Graphics.Display.Core.HdmiDisplayMode, hdrOption: win32more.Windows.Graphics.Display.Core.HdmiDisplayHdrOption) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def RequestSetCurrentDisplayModeWithHdrAndMetadataAsync(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayInformation, mode: win32more.Windows.Graphics.Display.Core.HdmiDisplayMode, hdrOption: win32more.Windows.Graphics.Display.Core.HdmiDisplayHdrOption, hdrMetadata: win32more.Windows.Graphics.Display.Core.HdmiDisplayHdr2086Metadata) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def add_DisplayModesChanged(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayInformation, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.Core.HdmiDisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DisplayModesChanged(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayInformation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.Graphics.Display.Core.IHdmiDisplayInformationStatics) -> win32more.Windows.Graphics.Display.Core.HdmiDisplayInformation: ...
    DisplayModesChanged = event()
class HdmiDisplayMode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Display.Core.IHdmiDisplayMode
    _classid_ = 'Windows.Graphics.Display.Core.HdmiDisplayMode'
    @winrt_mixinmethod
    def get_ResolutionWidthInRawPixels(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayMode) -> UInt32: ...
    @winrt_mixinmethod
    def get_ResolutionHeightInRawPixels(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayMode) -> UInt32: ...
    @winrt_mixinmethod
    def get_RefreshRate(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayMode) -> Double: ...
    @winrt_mixinmethod
    def get_StereoEnabled(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayMode) -> Boolean: ...
    @winrt_mixinmethod
    def get_BitsPerPixel(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayMode) -> UInt16: ...
    @winrt_mixinmethod
    def IsEqual(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayMode, mode: win32more.Windows.Graphics.Display.Core.HdmiDisplayMode) -> Boolean: ...
    @winrt_mixinmethod
    def get_ColorSpace(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayMode) -> win32more.Windows.Graphics.Display.Core.HdmiDisplayColorSpace: ...
    @winrt_mixinmethod
    def get_PixelEncoding(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayMode) -> win32more.Windows.Graphics.Display.Core.HdmiDisplayPixelEncoding: ...
    @winrt_mixinmethod
    def get_IsSdrLuminanceSupported(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayMode) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSmpte2084Supported(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayMode) -> Boolean: ...
    @winrt_mixinmethod
    def get_Is2086MetadataSupported(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayMode) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDolbyVisionLowLatencySupported(self: win32more.Windows.Graphics.Display.Core.IHdmiDisplayMode2) -> Boolean: ...
    BitsPerPixel = property(get_BitsPerPixel, None)
    ColorSpace = property(get_ColorSpace, None)
    Is2086MetadataSupported = property(get_Is2086MetadataSupported, None)
    IsDolbyVisionLowLatencySupported = property(get_IsDolbyVisionLowLatencySupported, None)
    IsSdrLuminanceSupported = property(get_IsSdrLuminanceSupported, None)
    IsSmpte2084Supported = property(get_IsSmpte2084Supported, None)
    PixelEncoding = property(get_PixelEncoding, None)
    RefreshRate = property(get_RefreshRate, None)
    ResolutionHeightInRawPixels = property(get_ResolutionHeightInRawPixels, None)
    ResolutionWidthInRawPixels = property(get_ResolutionWidthInRawPixels, None)
    StereoEnabled = property(get_StereoEnabled, None)
class HdmiDisplayPixelEncoding(Enum, Int32):
    Rgb444 = 0
    Ycc444 = 1
    Ycc422 = 2
    Ycc420 = 3
class IHdmiDisplayInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.Core.IHdmiDisplayInformation'
    _iid_ = Guid('{130b3c0a-f565-476e-abd5-ea05aee74c69}')
    @winrt_commethod(6)
    def GetSupportedDisplayModes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Display.Core.HdmiDisplayMode]: ...
    @winrt_commethod(7)
    def GetCurrentDisplayMode(self) -> win32more.Windows.Graphics.Display.Core.HdmiDisplayMode: ...
    @winrt_commethod(8)
    def SetDefaultDisplayModeAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def RequestSetCurrentDisplayModeAsync(self, mode: win32more.Windows.Graphics.Display.Core.HdmiDisplayMode) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(10)
    def RequestSetCurrentDisplayModeWithHdrAsync(self, mode: win32more.Windows.Graphics.Display.Core.HdmiDisplayMode, hdrOption: win32more.Windows.Graphics.Display.Core.HdmiDisplayHdrOption) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(11)
    def RequestSetCurrentDisplayModeWithHdrAndMetadataAsync(self, mode: win32more.Windows.Graphics.Display.Core.HdmiDisplayMode, hdrOption: win32more.Windows.Graphics.Display.Core.HdmiDisplayHdrOption, hdrMetadata: win32more.Windows.Graphics.Display.Core.HdmiDisplayHdr2086Metadata) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(12)
    def add_DisplayModesChanged(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.Core.HdmiDisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_DisplayModesChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DisplayModesChanged = event()
class IHdmiDisplayInformationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.Core.IHdmiDisplayInformationStatics'
    _iid_ = Guid('{6ce6b260-f42a-4a15-914c-7b8e2a5a65df}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.Graphics.Display.Core.HdmiDisplayInformation: ...
class IHdmiDisplayMode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    def IsEqual(self, mode: win32more.Windows.Graphics.Display.Core.HdmiDisplayMode) -> Boolean: ...
    @winrt_commethod(12)
    def get_ColorSpace(self) -> win32more.Windows.Graphics.Display.Core.HdmiDisplayColorSpace: ...
    @winrt_commethod(13)
    def get_PixelEncoding(self) -> win32more.Windows.Graphics.Display.Core.HdmiDisplayPixelEncoding: ...
    @winrt_commethod(14)
    def get_IsSdrLuminanceSupported(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_IsSmpte2084Supported(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_Is2086MetadataSupported(self) -> Boolean: ...
    BitsPerPixel = property(get_BitsPerPixel, None)
    ColorSpace = property(get_ColorSpace, None)
    Is2086MetadataSupported = property(get_Is2086MetadataSupported, None)
    IsSdrLuminanceSupported = property(get_IsSdrLuminanceSupported, None)
    IsSmpte2084Supported = property(get_IsSmpte2084Supported, None)
    PixelEncoding = property(get_PixelEncoding, None)
    RefreshRate = property(get_RefreshRate, None)
    ResolutionHeightInRawPixels = property(get_ResolutionHeightInRawPixels, None)
    ResolutionWidthInRawPixels = property(get_ResolutionWidthInRawPixels, None)
    StereoEnabled = property(get_StereoEnabled, None)
class IHdmiDisplayMode2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.Core.IHdmiDisplayMode2'
    _iid_ = Guid('{07cd4e9f-4b3c-42b8-84e7-895368718af2}')
    @winrt_commethod(6)
    def get_IsDolbyVisionLowLatencySupported(self) -> Boolean: ...
    IsDolbyVisionLowLatencySupported = property(get_IsDolbyVisionLowLatencySupported, None)


make_ready(__name__)
