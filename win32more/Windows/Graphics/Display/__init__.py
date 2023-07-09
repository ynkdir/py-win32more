from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics
import win32more.Windows.Graphics.Display
import win32more.Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AdvancedColorInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Display.IAdvancedColorInfo
    _classid_ = 'Windows.Graphics.Display.AdvancedColorInfo'
    @winrt_mixinmethod
    def get_CurrentAdvancedColorKind(self: win32more.Windows.Graphics.Display.IAdvancedColorInfo) -> win32more.Windows.Graphics.Display.AdvancedColorKind: ...
    @winrt_mixinmethod
    def get_RedPrimary(self: win32more.Windows.Graphics.Display.IAdvancedColorInfo) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_GreenPrimary(self: win32more.Windows.Graphics.Display.IAdvancedColorInfo) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_BluePrimary(self: win32more.Windows.Graphics.Display.IAdvancedColorInfo) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_WhitePoint(self: win32more.Windows.Graphics.Display.IAdvancedColorInfo) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_MaxLuminanceInNits(self: win32more.Windows.Graphics.Display.IAdvancedColorInfo) -> Single: ...
    @winrt_mixinmethod
    def get_MinLuminanceInNits(self: win32more.Windows.Graphics.Display.IAdvancedColorInfo) -> Single: ...
    @winrt_mixinmethod
    def get_MaxAverageFullFrameLuminanceInNits(self: win32more.Windows.Graphics.Display.IAdvancedColorInfo) -> Single: ...
    @winrt_mixinmethod
    def get_SdrWhiteLevelInNits(self: win32more.Windows.Graphics.Display.IAdvancedColorInfo) -> Single: ...
    @winrt_mixinmethod
    def IsHdrMetadataFormatCurrentlySupported(self: win32more.Windows.Graphics.Display.IAdvancedColorInfo, format: win32more.Windows.Graphics.Display.HdrMetadataFormat) -> Boolean: ...
    @winrt_mixinmethod
    def IsAdvancedColorKindAvailable(self: win32more.Windows.Graphics.Display.IAdvancedColorInfo, kind: win32more.Windows.Graphics.Display.AdvancedColorKind) -> Boolean: ...
    CurrentAdvancedColorKind = property(get_CurrentAdvancedColorKind, None)
    RedPrimary = property(get_RedPrimary, None)
    GreenPrimary = property(get_GreenPrimary, None)
    BluePrimary = property(get_BluePrimary, None)
    WhitePoint = property(get_WhitePoint, None)
    MaxLuminanceInNits = property(get_MaxLuminanceInNits, None)
    MinLuminanceInNits = property(get_MinLuminanceInNits, None)
    MaxAverageFullFrameLuminanceInNits = property(get_MaxAverageFullFrameLuminanceInNits, None)
    SdrWhiteLevelInNits = property(get_SdrWhiteLevelInNits, None)
AdvancedColorKind = Int32
AdvancedColorKind_StandardDynamicRange: AdvancedColorKind = 0
AdvancedColorKind_WideColorGamut: AdvancedColorKind = 1
AdvancedColorKind_HighDynamicRange: AdvancedColorKind = 2
class BrightnessOverride(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Display.IBrightnessOverride
    _classid_ = 'Windows.Graphics.Display.BrightnessOverride'
    @winrt_mixinmethod
    def get_IsSupported(self: win32more.Windows.Graphics.Display.IBrightnessOverride) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsOverrideActive(self: win32more.Windows.Graphics.Display.IBrightnessOverride) -> Boolean: ...
    @winrt_mixinmethod
    def get_BrightnessLevel(self: win32more.Windows.Graphics.Display.IBrightnessOverride) -> Double: ...
    @winrt_mixinmethod
    def SetBrightnessLevel(self: win32more.Windows.Graphics.Display.IBrightnessOverride, brightnessLevel: Double, options: win32more.Windows.Graphics.Display.DisplayBrightnessOverrideOptions) -> Void: ...
    @winrt_mixinmethod
    def SetBrightnessScenario(self: win32more.Windows.Graphics.Display.IBrightnessOverride, scenario: win32more.Windows.Graphics.Display.DisplayBrightnessScenario, options: win32more.Windows.Graphics.Display.DisplayBrightnessOverrideOptions) -> Void: ...
    @winrt_mixinmethod
    def GetLevelForScenario(self: win32more.Windows.Graphics.Display.IBrightnessOverride, scenario: win32more.Windows.Graphics.Display.DisplayBrightnessScenario) -> Double: ...
    @winrt_mixinmethod
    def StartOverride(self: win32more.Windows.Graphics.Display.IBrightnessOverride) -> Void: ...
    @winrt_mixinmethod
    def StopOverride(self: win32more.Windows.Graphics.Display.IBrightnessOverride) -> Void: ...
    @winrt_mixinmethod
    def add_IsSupportedChanged(self: win32more.Windows.Graphics.Display.IBrightnessOverride, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.BrightnessOverride, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsSupportedChanged(self: win32more.Windows.Graphics.Display.IBrightnessOverride, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_IsOverrideActiveChanged(self: win32more.Windows.Graphics.Display.IBrightnessOverride, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.BrightnessOverride, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsOverrideActiveChanged(self: win32more.Windows.Graphics.Display.IBrightnessOverride, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_BrightnessLevelChanged(self: win32more.Windows.Graphics.Display.IBrightnessOverride, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.BrightnessOverride, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BrightnessLevelChanged(self: win32more.Windows.Graphics.Display.IBrightnessOverride, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefaultForSystem(cls: win32more.Windows.Graphics.Display.IBrightnessOverrideStatics) -> win32more.Windows.Graphics.Display.BrightnessOverride: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.Graphics.Display.IBrightnessOverrideStatics) -> win32more.Windows.Graphics.Display.BrightnessOverride: ...
    @winrt_classmethod
    def SaveForSystemAsync(cls: win32more.Windows.Graphics.Display.IBrightnessOverrideStatics, value: win32more.Windows.Graphics.Display.BrightnessOverride) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    IsSupported = property(get_IsSupported, None)
    IsOverrideActive = property(get_IsOverrideActive, None)
    BrightnessLevel = property(get_BrightnessLevel, None)
class BrightnessOverrideSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Display.IBrightnessOverrideSettings
    _classid_ = 'Windows.Graphics.Display.BrightnessOverrideSettings'
    @winrt_mixinmethod
    def get_DesiredLevel(self: win32more.Windows.Graphics.Display.IBrightnessOverrideSettings) -> Double: ...
    @winrt_mixinmethod
    def get_DesiredNits(self: win32more.Windows.Graphics.Display.IBrightnessOverrideSettings) -> Single: ...
    @winrt_classmethod
    def CreateFromLevel(cls: win32more.Windows.Graphics.Display.IBrightnessOverrideSettingsStatics, level: Double) -> win32more.Windows.Graphics.Display.BrightnessOverrideSettings: ...
    @winrt_classmethod
    def CreateFromNits(cls: win32more.Windows.Graphics.Display.IBrightnessOverrideSettingsStatics, nits: Single) -> win32more.Windows.Graphics.Display.BrightnessOverrideSettings: ...
    @winrt_classmethod
    def CreateFromDisplayBrightnessOverrideScenario(cls: win32more.Windows.Graphics.Display.IBrightnessOverrideSettingsStatics, overrideScenario: win32more.Windows.Graphics.Display.DisplayBrightnessOverrideScenario) -> win32more.Windows.Graphics.Display.BrightnessOverrideSettings: ...
    DesiredLevel = property(get_DesiredLevel, None)
    DesiredNits = property(get_DesiredNits, None)
class ColorOverrideSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Display.IColorOverrideSettings
    _classid_ = 'Windows.Graphics.Display.ColorOverrideSettings'
    @winrt_mixinmethod
    def get_DesiredDisplayColorOverrideScenario(self: win32more.Windows.Graphics.Display.IColorOverrideSettings) -> win32more.Windows.Graphics.Display.DisplayColorOverrideScenario: ...
    @winrt_classmethod
    def CreateFromDisplayColorOverrideScenario(cls: win32more.Windows.Graphics.Display.IColorOverrideSettingsStatics, overrideScenario: win32more.Windows.Graphics.Display.DisplayColorOverrideScenario) -> win32more.Windows.Graphics.Display.ColorOverrideSettings: ...
    DesiredDisplayColorOverrideScenario = property(get_DesiredDisplayColorOverrideScenario, None)
DisplayBrightnessOverrideOptions = UInt32
DisplayBrightnessOverrideOptions_None: DisplayBrightnessOverrideOptions = 0
DisplayBrightnessOverrideOptions_UseDimmedPolicyWhenBatteryIsLow: DisplayBrightnessOverrideOptions = 1
DisplayBrightnessOverrideScenario = Int32
DisplayBrightnessOverrideScenario_IdleBrightness: DisplayBrightnessOverrideScenario = 0
DisplayBrightnessOverrideScenario_BarcodeReadingBrightness: DisplayBrightnessOverrideScenario = 1
DisplayBrightnessOverrideScenario_FullBrightness: DisplayBrightnessOverrideScenario = 2
DisplayBrightnessScenario = Int32
DisplayBrightnessScenario_DefaultBrightness: DisplayBrightnessScenario = 0
DisplayBrightnessScenario_IdleBrightness: DisplayBrightnessScenario = 1
DisplayBrightnessScenario_BarcodeReadingBrightness: DisplayBrightnessScenario = 2
DisplayBrightnessScenario_FullBrightness: DisplayBrightnessScenario = 3
DisplayColorOverrideScenario = Int32
DisplayColorOverrideScenario_Accurate: DisplayColorOverrideScenario = 0
class DisplayEnhancementOverride(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride
    _classid_ = 'Windows.Graphics.Display.DisplayEnhancementOverride'
    @winrt_mixinmethod
    def get_ColorOverrideSettings(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride) -> win32more.Windows.Graphics.Display.ColorOverrideSettings: ...
    @winrt_mixinmethod
    def put_ColorOverrideSettings(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride, value: win32more.Windows.Graphics.Display.ColorOverrideSettings) -> Void: ...
    @winrt_mixinmethod
    def get_BrightnessOverrideSettings(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride) -> win32more.Windows.Graphics.Display.BrightnessOverrideSettings: ...
    @winrt_mixinmethod
    def put_BrightnessOverrideSettings(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride, value: win32more.Windows.Graphics.Display.BrightnessOverrideSettings) -> Void: ...
    @winrt_mixinmethod
    def get_CanOverride(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsOverrideActive(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride) -> Boolean: ...
    @winrt_mixinmethod
    def GetCurrentDisplayEnhancementOverrideCapabilities(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride) -> win32more.Windows.Graphics.Display.DisplayEnhancementOverrideCapabilities: ...
    @winrt_mixinmethod
    def RequestOverride(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride) -> Void: ...
    @winrt_mixinmethod
    def StopOverride(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride) -> Void: ...
    @winrt_mixinmethod
    def add_CanOverrideChanged(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayEnhancementOverride, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CanOverrideChanged(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_IsOverrideActiveChanged(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayEnhancementOverride, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsOverrideActiveChanged(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DisplayEnhancementOverrideCapabilitiesChanged(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayEnhancementOverride, win32more.Windows.Graphics.Display.DisplayEnhancementOverrideCapabilitiesChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DisplayEnhancementOverrideCapabilitiesChanged(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.Graphics.Display.IDisplayEnhancementOverrideStatics) -> win32more.Windows.Graphics.Display.DisplayEnhancementOverride: ...
    ColorOverrideSettings = property(get_ColorOverrideSettings, put_ColorOverrideSettings)
    BrightnessOverrideSettings = property(get_BrightnessOverrideSettings, put_BrightnessOverrideSettings)
    CanOverride = property(get_CanOverride, None)
    IsOverrideActive = property(get_IsOverrideActive, None)
class DisplayEnhancementOverrideCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Display.IDisplayEnhancementOverrideCapabilities
    _classid_ = 'Windows.Graphics.Display.DisplayEnhancementOverrideCapabilities'
    @winrt_mixinmethod
    def get_IsBrightnessControlSupported(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverrideCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBrightnessNitsControlSupported(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverrideCapabilities) -> Boolean: ...
    @winrt_mixinmethod
    def GetSupportedNitRanges(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverrideCapabilities) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Display.NitRange]: ...
    IsBrightnessControlSupported = property(get_IsBrightnessControlSupported, None)
    IsBrightnessNitsControlSupported = property(get_IsBrightnessNitsControlSupported, None)
class DisplayEnhancementOverrideCapabilitiesChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Display.IDisplayEnhancementOverrideCapabilitiesChangedEventArgs
    _classid_ = 'Windows.Graphics.Display.DisplayEnhancementOverrideCapabilitiesChangedEventArgs'
    @winrt_mixinmethod
    def get_Capabilities(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverrideCapabilitiesChangedEventArgs) -> win32more.Windows.Graphics.Display.DisplayEnhancementOverrideCapabilities: ...
    Capabilities = property(get_Capabilities, None)
class _DisplayInformation_Meta_(ComPtr.__class__):
    pass
class DisplayInformation(ComPtr, metaclass=_DisplayInformation_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Display.IDisplayInformation
    _classid_ = 'Windows.Graphics.Display.DisplayInformation'
    @winrt_mixinmethod
    def get_CurrentOrientation(self: win32more.Windows.Graphics.Display.IDisplayInformation) -> win32more.Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_mixinmethod
    def get_NativeOrientation(self: win32more.Windows.Graphics.Display.IDisplayInformation) -> win32more.Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_mixinmethod
    def add_OrientationChanged(self: win32more.Windows.Graphics.Display.IDisplayInformation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_OrientationChanged(self: win32more.Windows.Graphics.Display.IDisplayInformation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_ResolutionScale(self: win32more.Windows.Graphics.Display.IDisplayInformation) -> win32more.Windows.Graphics.Display.ResolutionScale: ...
    @winrt_mixinmethod
    def get_LogicalDpi(self: win32more.Windows.Graphics.Display.IDisplayInformation) -> Single: ...
    @winrt_mixinmethod
    def get_RawDpiX(self: win32more.Windows.Graphics.Display.IDisplayInformation) -> Single: ...
    @winrt_mixinmethod
    def get_RawDpiY(self: win32more.Windows.Graphics.Display.IDisplayInformation) -> Single: ...
    @winrt_mixinmethod
    def add_DpiChanged(self: win32more.Windows.Graphics.Display.IDisplayInformation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DpiChanged(self: win32more.Windows.Graphics.Display.IDisplayInformation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_StereoEnabled(self: win32more.Windows.Graphics.Display.IDisplayInformation) -> Boolean: ...
    @winrt_mixinmethod
    def add_StereoEnabledChanged(self: win32more.Windows.Graphics.Display.IDisplayInformation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StereoEnabledChanged(self: win32more.Windows.Graphics.Display.IDisplayInformation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetColorProfileAsync(self: win32more.Windows.Graphics.Display.IDisplayInformation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def add_ColorProfileChanged(self: win32more.Windows.Graphics.Display.IDisplayInformation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ColorProfileChanged(self: win32more.Windows.Graphics.Display.IDisplayInformation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_RawPixelsPerViewPixel(self: win32more.Windows.Graphics.Display.IDisplayInformation2) -> Double: ...
    @winrt_mixinmethod
    def get_DiagonalSizeInInches(self: win32more.Windows.Graphics.Display.IDisplayInformation3) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_ScreenWidthInRawPixels(self: win32more.Windows.Graphics.Display.IDisplayInformation4) -> UInt32: ...
    @winrt_mixinmethod
    def get_ScreenHeightInRawPixels(self: win32more.Windows.Graphics.Display.IDisplayInformation4) -> UInt32: ...
    @winrt_mixinmethod
    def GetAdvancedColorInfo(self: win32more.Windows.Graphics.Display.IDisplayInformation5) -> win32more.Windows.Graphics.Display.AdvancedColorInfo: ...
    @winrt_mixinmethod
    def add_AdvancedColorInfoChanged(self: win32more.Windows.Graphics.Display.IDisplayInformation5, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AdvancedColorInfoChanged(self: win32more.Windows.Graphics.Display.IDisplayInformation5, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.Graphics.Display.IDisplayInformationStatics) -> win32more.Windows.Graphics.Display.DisplayInformation: ...
    @winrt_classmethod
    def get_AutoRotationPreferences(cls: win32more.Windows.Graphics.Display.IDisplayInformationStatics) -> win32more.Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_classmethod
    def put_AutoRotationPreferences(cls: win32more.Windows.Graphics.Display.IDisplayInformationStatics, value: win32more.Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_classmethod
    def add_DisplayContentsInvalidated(cls: win32more.Windows.Graphics.Display.IDisplayInformationStatics, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_DisplayContentsInvalidated(cls: win32more.Windows.Graphics.Display.IDisplayInformationStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentOrientation = property(get_CurrentOrientation, None)
    NativeOrientation = property(get_NativeOrientation, None)
    ResolutionScale = property(get_ResolutionScale, None)
    LogicalDpi = property(get_LogicalDpi, None)
    RawDpiX = property(get_RawDpiX, None)
    RawDpiY = property(get_RawDpiY, None)
    StereoEnabled = property(get_StereoEnabled, None)
    RawPixelsPerViewPixel = property(get_RawPixelsPerViewPixel, None)
    DiagonalSizeInInches = property(get_DiagonalSizeInInches, None)
    ScreenWidthInRawPixels = property(get_ScreenWidthInRawPixels, None)
    ScreenHeightInRawPixels = property(get_ScreenHeightInRawPixels, None)
    _DisplayInformation_Meta_.AutoRotationPreferences = property(get_AutoRotationPreferences.__wrapped__, put_AutoRotationPreferences.__wrapped__)
DisplayOrientations = UInt32
DisplayOrientations_None: DisplayOrientations = 0
DisplayOrientations_Landscape: DisplayOrientations = 1
DisplayOrientations_Portrait: DisplayOrientations = 2
DisplayOrientations_LandscapeFlipped: DisplayOrientations = 4
DisplayOrientations_PortraitFlipped: DisplayOrientations = 8
class _DisplayProperties_Meta_(ComPtr.__class__):
    pass
class DisplayProperties(ComPtr, metaclass=_DisplayProperties_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.DisplayProperties'
    @winrt_classmethod
    def get_CurrentOrientation(cls: win32more.Windows.Graphics.Display.IDisplayPropertiesStatics) -> win32more.Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_classmethod
    def get_NativeOrientation(cls: win32more.Windows.Graphics.Display.IDisplayPropertiesStatics) -> win32more.Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_classmethod
    def get_AutoRotationPreferences(cls: win32more.Windows.Graphics.Display.IDisplayPropertiesStatics) -> win32more.Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_classmethod
    def put_AutoRotationPreferences(cls: win32more.Windows.Graphics.Display.IDisplayPropertiesStatics, value: win32more.Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_classmethod
    def add_OrientationChanged(cls: win32more.Windows.Graphics.Display.IDisplayPropertiesStatics, handler: win32more.Windows.Graphics.Display.DisplayPropertiesEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_OrientationChanged(cls: win32more.Windows.Graphics.Display.IDisplayPropertiesStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_ResolutionScale(cls: win32more.Windows.Graphics.Display.IDisplayPropertiesStatics) -> win32more.Windows.Graphics.Display.ResolutionScale: ...
    @winrt_classmethod
    def get_LogicalDpi(cls: win32more.Windows.Graphics.Display.IDisplayPropertiesStatics) -> Single: ...
    @winrt_classmethod
    def add_LogicalDpiChanged(cls: win32more.Windows.Graphics.Display.IDisplayPropertiesStatics, handler: win32more.Windows.Graphics.Display.DisplayPropertiesEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_LogicalDpiChanged(cls: win32more.Windows.Graphics.Display.IDisplayPropertiesStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_StereoEnabled(cls: win32more.Windows.Graphics.Display.IDisplayPropertiesStatics) -> Boolean: ...
    @winrt_classmethod
    def add_StereoEnabledChanged(cls: win32more.Windows.Graphics.Display.IDisplayPropertiesStatics, handler: win32more.Windows.Graphics.Display.DisplayPropertiesEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_StereoEnabledChanged(cls: win32more.Windows.Graphics.Display.IDisplayPropertiesStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetColorProfileAsync(cls: win32more.Windows.Graphics.Display.IDisplayPropertiesStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_classmethod
    def add_ColorProfileChanged(cls: win32more.Windows.Graphics.Display.IDisplayPropertiesStatics, handler: win32more.Windows.Graphics.Display.DisplayPropertiesEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_ColorProfileChanged(cls: win32more.Windows.Graphics.Display.IDisplayPropertiesStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_DisplayContentsInvalidated(cls: win32more.Windows.Graphics.Display.IDisplayPropertiesStatics, handler: win32more.Windows.Graphics.Display.DisplayPropertiesEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_DisplayContentsInvalidated(cls: win32more.Windows.Graphics.Display.IDisplayPropertiesStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    _DisplayProperties_Meta_.CurrentOrientation = property(get_CurrentOrientation.__wrapped__, None)
    _DisplayProperties_Meta_.NativeOrientation = property(get_NativeOrientation.__wrapped__, None)
    _DisplayProperties_Meta_.AutoRotationPreferences = property(get_AutoRotationPreferences.__wrapped__, put_AutoRotationPreferences.__wrapped__)
    _DisplayProperties_Meta_.ResolutionScale = property(get_ResolutionScale.__wrapped__, None)
    _DisplayProperties_Meta_.LogicalDpi = property(get_LogicalDpi.__wrapped__, None)
    _DisplayProperties_Meta_.StereoEnabled = property(get_StereoEnabled.__wrapped__, None)
class DisplayPropertiesEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dbdd8b01-f1a1-46d1-9ee3-543bcc995980}')
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
class DisplayServices(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Display.IDisplayServices
    _classid_ = 'Windows.Graphics.Display.DisplayServices'
    @winrt_classmethod
    def FindAll(cls: win32more.Windows.Graphics.Display.IDisplayServicesStatics) -> SZArray[win32more.Windows.Graphics.DisplayId]: ...
HdrMetadataFormat = Int32
HdrMetadataFormat_Hdr10: HdrMetadataFormat = 0
HdrMetadataFormat_Hdr10Plus: HdrMetadataFormat = 1
class IAdvancedColorInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IAdvancedColorInfo'
    _iid_ = Guid('{8797dcfb-b229-4081-ae9a-2cc85e34ad6a}')
    @winrt_commethod(6)
    def get_CurrentAdvancedColorKind(self) -> win32more.Windows.Graphics.Display.AdvancedColorKind: ...
    @winrt_commethod(7)
    def get_RedPrimary(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_GreenPrimary(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def get_BluePrimary(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(10)
    def get_WhitePoint(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(11)
    def get_MaxLuminanceInNits(self) -> Single: ...
    @winrt_commethod(12)
    def get_MinLuminanceInNits(self) -> Single: ...
    @winrt_commethod(13)
    def get_MaxAverageFullFrameLuminanceInNits(self) -> Single: ...
    @winrt_commethod(14)
    def get_SdrWhiteLevelInNits(self) -> Single: ...
    @winrt_commethod(15)
    def IsHdrMetadataFormatCurrentlySupported(self, format: win32more.Windows.Graphics.Display.HdrMetadataFormat) -> Boolean: ...
    @winrt_commethod(16)
    def IsAdvancedColorKindAvailable(self, kind: win32more.Windows.Graphics.Display.AdvancedColorKind) -> Boolean: ...
    CurrentAdvancedColorKind = property(get_CurrentAdvancedColorKind, None)
    RedPrimary = property(get_RedPrimary, None)
    GreenPrimary = property(get_GreenPrimary, None)
    BluePrimary = property(get_BluePrimary, None)
    WhitePoint = property(get_WhitePoint, None)
    MaxLuminanceInNits = property(get_MaxLuminanceInNits, None)
    MinLuminanceInNits = property(get_MinLuminanceInNits, None)
    MaxAverageFullFrameLuminanceInNits = property(get_MaxAverageFullFrameLuminanceInNits, None)
    SdrWhiteLevelInNits = property(get_SdrWhiteLevelInNits, None)
class IBrightnessOverride(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IBrightnessOverride'
    _iid_ = Guid('{96c9621a-c143-4392-bedd-4a7e9574c8fd}')
    @winrt_commethod(6)
    def get_IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsOverrideActive(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_BrightnessLevel(self) -> Double: ...
    @winrt_commethod(9)
    def SetBrightnessLevel(self, brightnessLevel: Double, options: win32more.Windows.Graphics.Display.DisplayBrightnessOverrideOptions) -> Void: ...
    @winrt_commethod(10)
    def SetBrightnessScenario(self, scenario: win32more.Windows.Graphics.Display.DisplayBrightnessScenario, options: win32more.Windows.Graphics.Display.DisplayBrightnessOverrideOptions) -> Void: ...
    @winrt_commethod(11)
    def GetLevelForScenario(self, scenario: win32more.Windows.Graphics.Display.DisplayBrightnessScenario) -> Double: ...
    @winrt_commethod(12)
    def StartOverride(self) -> Void: ...
    @winrt_commethod(13)
    def StopOverride(self) -> Void: ...
    @winrt_commethod(14)
    def add_IsSupportedChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.BrightnessOverride, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_IsSupportedChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_IsOverrideActiveChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.BrightnessOverride, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_IsOverrideActiveChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_BrightnessLevelChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.BrightnessOverride, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_BrightnessLevelChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsSupported = property(get_IsSupported, None)
    IsOverrideActive = property(get_IsOverrideActive, None)
    BrightnessLevel = property(get_BrightnessLevel, None)
class IBrightnessOverrideSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IBrightnessOverrideSettings'
    _iid_ = Guid('{d112ab2a-7604-4dba-bcf8-4b6f49502cb0}')
    @winrt_commethod(6)
    def get_DesiredLevel(self) -> Double: ...
    @winrt_commethod(7)
    def get_DesiredNits(self) -> Single: ...
    DesiredLevel = property(get_DesiredLevel, None)
    DesiredNits = property(get_DesiredNits, None)
class IBrightnessOverrideSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IBrightnessOverrideSettingsStatics'
    _iid_ = Guid('{d487dc90-6f74-440b-b383-5fe96cf00b0f}')
    @winrt_commethod(6)
    def CreateFromLevel(self, level: Double) -> win32more.Windows.Graphics.Display.BrightnessOverrideSettings: ...
    @winrt_commethod(7)
    def CreateFromNits(self, nits: Single) -> win32more.Windows.Graphics.Display.BrightnessOverrideSettings: ...
    @winrt_commethod(8)
    def CreateFromDisplayBrightnessOverrideScenario(self, overrideScenario: win32more.Windows.Graphics.Display.DisplayBrightnessOverrideScenario) -> win32more.Windows.Graphics.Display.BrightnessOverrideSettings: ...
class IBrightnessOverrideStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IBrightnessOverrideStatics'
    _iid_ = Guid('{03a7b9ed-e1f1-4a68-a11f-946ad8ce5393}')
    @winrt_commethod(6)
    def GetDefaultForSystem(self) -> win32more.Windows.Graphics.Display.BrightnessOverride: ...
    @winrt_commethod(7)
    def GetForCurrentView(self) -> win32more.Windows.Graphics.Display.BrightnessOverride: ...
    @winrt_commethod(8)
    def SaveForSystemAsync(self, value: win32more.Windows.Graphics.Display.BrightnessOverride) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class IColorOverrideSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IColorOverrideSettings'
    _iid_ = Guid('{fbefa134-4a81-4c4d-a5b6-7d1b5c4bd00b}')
    @winrt_commethod(6)
    def get_DesiredDisplayColorOverrideScenario(self) -> win32more.Windows.Graphics.Display.DisplayColorOverrideScenario: ...
    DesiredDisplayColorOverrideScenario = property(get_DesiredDisplayColorOverrideScenario, None)
class IColorOverrideSettingsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IColorOverrideSettingsStatics'
    _iid_ = Guid('{b068e05f-c41f-4ac9-afab-827ab6248f9a}')
    @winrt_commethod(6)
    def CreateFromDisplayColorOverrideScenario(self, overrideScenario: win32more.Windows.Graphics.Display.DisplayColorOverrideScenario) -> win32more.Windows.Graphics.Display.ColorOverrideSettings: ...
class IDisplayEnhancementOverride(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IDisplayEnhancementOverride'
    _iid_ = Guid('{429594cf-d97a-4b02-a428-5c4292f7f522}')
    @winrt_commethod(6)
    def get_ColorOverrideSettings(self) -> win32more.Windows.Graphics.Display.ColorOverrideSettings: ...
    @winrt_commethod(7)
    def put_ColorOverrideSettings(self, value: win32more.Windows.Graphics.Display.ColorOverrideSettings) -> Void: ...
    @winrt_commethod(8)
    def get_BrightnessOverrideSettings(self) -> win32more.Windows.Graphics.Display.BrightnessOverrideSettings: ...
    @winrt_commethod(9)
    def put_BrightnessOverrideSettings(self, value: win32more.Windows.Graphics.Display.BrightnessOverrideSettings) -> Void: ...
    @winrt_commethod(10)
    def get_CanOverride(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsOverrideActive(self) -> Boolean: ...
    @winrt_commethod(12)
    def GetCurrentDisplayEnhancementOverrideCapabilities(self) -> win32more.Windows.Graphics.Display.DisplayEnhancementOverrideCapabilities: ...
    @winrt_commethod(13)
    def RequestOverride(self) -> Void: ...
    @winrt_commethod(14)
    def StopOverride(self) -> Void: ...
    @winrt_commethod(15)
    def add_CanOverrideChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayEnhancementOverride, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_CanOverrideChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_IsOverrideActiveChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayEnhancementOverride, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_IsOverrideActiveChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_DisplayEnhancementOverrideCapabilitiesChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayEnhancementOverride, win32more.Windows.Graphics.Display.DisplayEnhancementOverrideCapabilitiesChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_DisplayEnhancementOverrideCapabilitiesChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ColorOverrideSettings = property(get_ColorOverrideSettings, put_ColorOverrideSettings)
    BrightnessOverrideSettings = property(get_BrightnessOverrideSettings, put_BrightnessOverrideSettings)
    CanOverride = property(get_CanOverride, None)
    IsOverrideActive = property(get_IsOverrideActive, None)
class IDisplayEnhancementOverrideCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IDisplayEnhancementOverrideCapabilities'
    _iid_ = Guid('{457060de-ee5a-47b7-9918-1e51e812ccc8}')
    @winrt_commethod(6)
    def get_IsBrightnessControlSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsBrightnessNitsControlSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def GetSupportedNitRanges(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Graphics.Display.NitRange]: ...
    IsBrightnessControlSupported = property(get_IsBrightnessControlSupported, None)
    IsBrightnessNitsControlSupported = property(get_IsBrightnessNitsControlSupported, None)
class IDisplayEnhancementOverrideCapabilitiesChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IDisplayEnhancementOverrideCapabilitiesChangedEventArgs'
    _iid_ = Guid('{db61e664-15fa-49da-8b77-07dbd2af585d}')
    @winrt_commethod(6)
    def get_Capabilities(self) -> win32more.Windows.Graphics.Display.DisplayEnhancementOverrideCapabilities: ...
    Capabilities = property(get_Capabilities, None)
class IDisplayEnhancementOverrideStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IDisplayEnhancementOverrideStatics'
    _iid_ = Guid('{cf5b7ec1-9791-4453-b013-29b6f778e519}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.Graphics.Display.DisplayEnhancementOverride: ...
class IDisplayInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IDisplayInformation'
    _iid_ = Guid('{bed112ae-adc3-4dc9-ae65-851f4d7d4799}')
    @winrt_commethod(6)
    def get_CurrentOrientation(self) -> win32more.Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_commethod(7)
    def get_NativeOrientation(self) -> win32more.Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_commethod(8)
    def add_OrientationChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_OrientationChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_ResolutionScale(self) -> win32more.Windows.Graphics.Display.ResolutionScale: ...
    @winrt_commethod(11)
    def get_LogicalDpi(self) -> Single: ...
    @winrt_commethod(12)
    def get_RawDpiX(self) -> Single: ...
    @winrt_commethod(13)
    def get_RawDpiY(self) -> Single: ...
    @winrt_commethod(14)
    def add_DpiChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_DpiChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_StereoEnabled(self) -> Boolean: ...
    @winrt_commethod(17)
    def add_StereoEnabledChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_StereoEnabledChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def GetColorProfileAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_commethod(20)
    def add_ColorProfileChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_ColorProfileChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentOrientation = property(get_CurrentOrientation, None)
    NativeOrientation = property(get_NativeOrientation, None)
    ResolutionScale = property(get_ResolutionScale, None)
    LogicalDpi = property(get_LogicalDpi, None)
    RawDpiX = property(get_RawDpiX, None)
    RawDpiY = property(get_RawDpiY, None)
    StereoEnabled = property(get_StereoEnabled, None)
class IDisplayInformation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IDisplayInformation2'
    _iid_ = Guid('{4dcd0021-fad1-4b8e-8edf-775887b8bf19}')
    @winrt_commethod(6)
    def get_RawPixelsPerViewPixel(self) -> Double: ...
    RawPixelsPerViewPixel = property(get_RawPixelsPerViewPixel, None)
class IDisplayInformation3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IDisplayInformation3'
    _iid_ = Guid('{db15011d-0f09-4466-8ff3-11de9a3c929a}')
    @winrt_commethod(6)
    def get_DiagonalSizeInInches(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    DiagonalSizeInInches = property(get_DiagonalSizeInInches, None)
class IDisplayInformation4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IDisplayInformation4'
    _iid_ = Guid('{c972ce2f-1242-46be-b536-e1aafe9e7acf}')
    @winrt_commethod(6)
    def get_ScreenWidthInRawPixels(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_ScreenHeightInRawPixels(self) -> UInt32: ...
    ScreenWidthInRawPixels = property(get_ScreenWidthInRawPixels, None)
    ScreenHeightInRawPixels = property(get_ScreenHeightInRawPixels, None)
class IDisplayInformation5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IDisplayInformation5'
    _iid_ = Guid('{3a5442dc-2cde-4a8d-80d1-21dc5adcc1aa}')
    @winrt_commethod(6)
    def GetAdvancedColorInfo(self) -> win32more.Windows.Graphics.Display.AdvancedColorInfo: ...
    @winrt_commethod(7)
    def add_AdvancedColorInfoChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_AdvancedColorInfoChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IDisplayInformationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IDisplayInformationStatics'
    _iid_ = Guid('{c6a02a6c-d452-44dc-ba07-96f3c6adf9d1}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.Graphics.Display.DisplayInformation: ...
    @winrt_commethod(7)
    def get_AutoRotationPreferences(self) -> win32more.Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_commethod(8)
    def put_AutoRotationPreferences(self, value: win32more.Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_commethod(9)
    def add_DisplayContentsInvalidated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_DisplayContentsInvalidated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AutoRotationPreferences = property(get_AutoRotationPreferences, put_AutoRotationPreferences)
class IDisplayPropertiesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IDisplayPropertiesStatics'
    _iid_ = Guid('{6937ed8d-30ea-4ded-8271-4553ff02f68a}')
    @winrt_commethod(6)
    def get_CurrentOrientation(self) -> win32more.Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_commethod(7)
    def get_NativeOrientation(self) -> win32more.Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_commethod(8)
    def get_AutoRotationPreferences(self) -> win32more.Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_commethod(9)
    def put_AutoRotationPreferences(self, value: win32more.Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_commethod(10)
    def add_OrientationChanged(self, handler: win32more.Windows.Graphics.Display.DisplayPropertiesEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_OrientationChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def get_ResolutionScale(self) -> win32more.Windows.Graphics.Display.ResolutionScale: ...
    @winrt_commethod(13)
    def get_LogicalDpi(self) -> Single: ...
    @winrt_commethod(14)
    def add_LogicalDpiChanged(self, handler: win32more.Windows.Graphics.Display.DisplayPropertiesEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_LogicalDpiChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_StereoEnabled(self) -> Boolean: ...
    @winrt_commethod(17)
    def add_StereoEnabledChanged(self, handler: win32more.Windows.Graphics.Display.DisplayPropertiesEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_StereoEnabledChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def GetColorProfileAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_commethod(20)
    def add_ColorProfileChanged(self, handler: win32more.Windows.Graphics.Display.DisplayPropertiesEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_ColorProfileChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def add_DisplayContentsInvalidated(self, handler: win32more.Windows.Graphics.Display.DisplayPropertiesEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_DisplayContentsInvalidated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentOrientation = property(get_CurrentOrientation, None)
    NativeOrientation = property(get_NativeOrientation, None)
    AutoRotationPreferences = property(get_AutoRotationPreferences, put_AutoRotationPreferences)
    ResolutionScale = property(get_ResolutionScale, None)
    LogicalDpi = property(get_LogicalDpi, None)
    StereoEnabled = property(get_StereoEnabled, None)
class IDisplayServices(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IDisplayServices'
    _iid_ = Guid('{1b54f32b-890d-5747-bd26-fdbdeb0c8a71}')
class IDisplayServicesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IDisplayServicesStatics'
    _iid_ = Guid('{dc2096bf-730a-5560-b461-91c13d692e0c}')
    @winrt_commethod(6)
    def FindAll(self) -> SZArray[win32more.Windows.Graphics.DisplayId]: ...
class NitRange(EasyCastStructure):
    MinNits: Single
    MaxNits: Single
    StepSizeNits: Single
ResolutionScale = Int32
ResolutionScale_Invalid: ResolutionScale = 0
ResolutionScale_Scale100Percent: ResolutionScale = 100
ResolutionScale_Scale120Percent: ResolutionScale = 120
ResolutionScale_Scale125Percent: ResolutionScale = 125
ResolutionScale_Scale140Percent: ResolutionScale = 140
ResolutionScale_Scale150Percent: ResolutionScale = 150
ResolutionScale_Scale160Percent: ResolutionScale = 160
ResolutionScale_Scale175Percent: ResolutionScale = 175
ResolutionScale_Scale180Percent: ResolutionScale = 180
ResolutionScale_Scale200Percent: ResolutionScale = 200
ResolutionScale_Scale225Percent: ResolutionScale = 225
ResolutionScale_Scale250Percent: ResolutionScale = 250
ResolutionScale_Scale300Percent: ResolutionScale = 300
ResolutionScale_Scale350Percent: ResolutionScale = 350
ResolutionScale_Scale400Percent: ResolutionScale = 400
ResolutionScale_Scale450Percent: ResolutionScale = 450
ResolutionScale_Scale500Percent: ResolutionScale = 500
make_head(_module, 'AdvancedColorInfo')
make_head(_module, 'BrightnessOverride')
make_head(_module, 'BrightnessOverrideSettings')
make_head(_module, 'ColorOverrideSettings')
make_head(_module, 'DisplayEnhancementOverride')
make_head(_module, 'DisplayEnhancementOverrideCapabilities')
make_head(_module, 'DisplayEnhancementOverrideCapabilitiesChangedEventArgs')
make_head(_module, 'DisplayInformation')
make_head(_module, 'DisplayProperties')
make_head(_module, 'DisplayServices')
make_head(_module, 'IAdvancedColorInfo')
make_head(_module, 'IBrightnessOverride')
make_head(_module, 'IBrightnessOverrideSettings')
make_head(_module, 'IBrightnessOverrideSettingsStatics')
make_head(_module, 'IBrightnessOverrideStatics')
make_head(_module, 'IColorOverrideSettings')
make_head(_module, 'IColorOverrideSettingsStatics')
make_head(_module, 'IDisplayEnhancementOverride')
make_head(_module, 'IDisplayEnhancementOverrideCapabilities')
make_head(_module, 'IDisplayEnhancementOverrideCapabilitiesChangedEventArgs')
make_head(_module, 'IDisplayEnhancementOverrideStatics')
make_head(_module, 'IDisplayInformation')
make_head(_module, 'IDisplayInformation2')
make_head(_module, 'IDisplayInformation3')
make_head(_module, 'IDisplayInformation4')
make_head(_module, 'IDisplayInformation5')
make_head(_module, 'IDisplayInformationStatics')
make_head(_module, 'IDisplayPropertiesStatics')
make_head(_module, 'IDisplayServices')
make_head(_module, 'IDisplayServicesStatics')
make_head(_module, 'NitRange')
