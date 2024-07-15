from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics
import win32more.Windows.Graphics.Display
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
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
    BluePrimary = property(get_BluePrimary, None)
    CurrentAdvancedColorKind = property(get_CurrentAdvancedColorKind, None)
    GreenPrimary = property(get_GreenPrimary, None)
    MaxAverageFullFrameLuminanceInNits = property(get_MaxAverageFullFrameLuminanceInNits, None)
    MaxLuminanceInNits = property(get_MaxLuminanceInNits, None)
    MinLuminanceInNits = property(get_MinLuminanceInNits, None)
    RedPrimary = property(get_RedPrimary, None)
    SdrWhiteLevelInNits = property(get_SdrWhiteLevelInNits, None)
    WhitePoint = property(get_WhitePoint, None)
class AdvancedColorKind(Enum, Int32):
    StandardDynamicRange = 0
    WideColorGamut = 1
    HighDynamicRange = 2
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
    def add_IsSupportedChanged(self: win32more.Windows.Graphics.Display.IBrightnessOverride, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.BrightnessOverride, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsSupportedChanged(self: win32more.Windows.Graphics.Display.IBrightnessOverride, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_IsOverrideActiveChanged(self: win32more.Windows.Graphics.Display.IBrightnessOverride, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.BrightnessOverride, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsOverrideActiveChanged(self: win32more.Windows.Graphics.Display.IBrightnessOverride, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_BrightnessLevelChanged(self: win32more.Windows.Graphics.Display.IBrightnessOverride, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.BrightnessOverride, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BrightnessLevelChanged(self: win32more.Windows.Graphics.Display.IBrightnessOverride, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefaultForSystem(cls: win32more.Windows.Graphics.Display.IBrightnessOverrideStatics) -> win32more.Windows.Graphics.Display.BrightnessOverride: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.Graphics.Display.IBrightnessOverrideStatics) -> win32more.Windows.Graphics.Display.BrightnessOverride: ...
    @winrt_classmethod
    def SaveForSystemAsync(cls: win32more.Windows.Graphics.Display.IBrightnessOverrideStatics, value: win32more.Windows.Graphics.Display.BrightnessOverride) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    BrightnessLevel = property(get_BrightnessLevel, None)
    IsOverrideActive = property(get_IsOverrideActive, None)
    IsSupported = property(get_IsSupported, None)
    IsSupportedChanged = event()
    IsOverrideActiveChanged = event()
    BrightnessLevelChanged = event()
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
class DisplayBrightnessOverrideOptions(Enum, UInt32):
    None_ = 0
    UseDimmedPolicyWhenBatteryIsLow = 1
class DisplayBrightnessOverrideScenario(Enum, Int32):
    IdleBrightness = 0
    BarcodeReadingBrightness = 1
    FullBrightness = 2
class DisplayBrightnessScenario(Enum, Int32):
    DefaultBrightness = 0
    IdleBrightness = 1
    BarcodeReadingBrightness = 2
    FullBrightness = 3
class DisplayColorOverrideScenario(Enum, Int32):
    Accurate = 0
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
    def add_CanOverrideChanged(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayEnhancementOverride, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CanOverrideChanged(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_IsOverrideActiveChanged(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayEnhancementOverride, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsOverrideActiveChanged(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DisplayEnhancementOverrideCapabilitiesChanged(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayEnhancementOverride, win32more.Windows.Graphics.Display.DisplayEnhancementOverrideCapabilitiesChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DisplayEnhancementOverrideCapabilitiesChanged(self: win32more.Windows.Graphics.Display.IDisplayEnhancementOverride, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.Graphics.Display.IDisplayEnhancementOverrideStatics) -> win32more.Windows.Graphics.Display.DisplayEnhancementOverride: ...
    BrightnessOverrideSettings = property(get_BrightnessOverrideSettings, put_BrightnessOverrideSettings)
    CanOverride = property(get_CanOverride, None)
    ColorOverrideSettings = property(get_ColorOverrideSettings, put_ColorOverrideSettings)
    IsOverrideActive = property(get_IsOverrideActive, None)
    CanOverrideChanged = event()
    IsOverrideActiveChanged = event()
    DisplayEnhancementOverrideCapabilitiesChanged = event()
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
    def add_OrientationChanged(self: win32more.Windows.Graphics.Display.IDisplayInformation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
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
    def add_DpiChanged(self: win32more.Windows.Graphics.Display.IDisplayInformation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DpiChanged(self: win32more.Windows.Graphics.Display.IDisplayInformation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_StereoEnabled(self: win32more.Windows.Graphics.Display.IDisplayInformation) -> Boolean: ...
    @winrt_mixinmethod
    def add_StereoEnabledChanged(self: win32more.Windows.Graphics.Display.IDisplayInformation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StereoEnabledChanged(self: win32more.Windows.Graphics.Display.IDisplayInformation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetColorProfileAsync(self: win32more.Windows.Graphics.Display.IDisplayInformation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def add_ColorProfileChanged(self: win32more.Windows.Graphics.Display.IDisplayInformation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
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
    def add_AdvancedColorInfoChanged(self: win32more.Windows.Graphics.Display.IDisplayInformation5, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AdvancedColorInfoChanged(self: win32more.Windows.Graphics.Display.IDisplayInformation5, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.Graphics.Display.IDisplayInformationStatics) -> win32more.Windows.Graphics.Display.DisplayInformation: ...
    @winrt_classmethod
    def get_AutoRotationPreferences(cls: win32more.Windows.Graphics.Display.IDisplayInformationStatics) -> win32more.Windows.Graphics.Display.DisplayOrientations: ...
    @winrt_classmethod
    def put_AutoRotationPreferences(cls: win32more.Windows.Graphics.Display.IDisplayInformationStatics, value: win32more.Windows.Graphics.Display.DisplayOrientations) -> Void: ...
    @winrt_classmethod
    def add_DisplayContentsInvalidated(cls: win32more.Windows.Graphics.Display.IDisplayInformationStatics, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_DisplayContentsInvalidated(cls: win32more.Windows.Graphics.Display.IDisplayInformationStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentOrientation = property(get_CurrentOrientation, None)
    DiagonalSizeInInches = property(get_DiagonalSizeInInches, None)
    LogicalDpi = property(get_LogicalDpi, None)
    NativeOrientation = property(get_NativeOrientation, None)
    RawDpiX = property(get_RawDpiX, None)
    RawDpiY = property(get_RawDpiY, None)
    RawPixelsPerViewPixel = property(get_RawPixelsPerViewPixel, None)
    ResolutionScale = property(get_ResolutionScale, None)
    ScreenHeightInRawPixels = property(get_ScreenHeightInRawPixels, None)
    ScreenWidthInRawPixels = property(get_ScreenWidthInRawPixels, None)
    StereoEnabled = property(get_StereoEnabled, None)
    _DisplayInformation_Meta_.AutoRotationPreferences = property(get_AutoRotationPreferences, put_AutoRotationPreferences)
    OrientationChanged = event()
    DpiChanged = event()
    StereoEnabledChanged = event()
    ColorProfileChanged = event()
    AdvancedColorInfoChanged = event()
class DisplayOrientations(Enum, UInt32):
    None_ = 0
    Landscape = 1
    Portrait = 2
    LandscapeFlipped = 4
    PortraitFlipped = 8
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
    _DisplayProperties_Meta_.AutoRotationPreferences = property(get_AutoRotationPreferences, put_AutoRotationPreferences)
    _DisplayProperties_Meta_.CurrentOrientation = property(get_CurrentOrientation, None)
    _DisplayProperties_Meta_.LogicalDpi = property(get_LogicalDpi, None)
    _DisplayProperties_Meta_.NativeOrientation = property(get_NativeOrientation, None)
    _DisplayProperties_Meta_.ResolutionScale = property(get_ResolutionScale, None)
    _DisplayProperties_Meta_.StereoEnabled = property(get_StereoEnabled, None)
class DisplayPropertiesEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dbdd8b01-f1a1-46d1-9ee3-543bcc995980}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
class DisplayServices(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Graphics.Display.IDisplayServices
    _classid_ = 'Windows.Graphics.Display.DisplayServices'
    @winrt_classmethod
    def FindAll(cls: win32more.Windows.Graphics.Display.IDisplayServicesStatics) -> ReceiveArray[win32more.Windows.Graphics.DisplayId]: ...
class HdrMetadataFormat(Enum, Int32):
    Hdr10 = 0
    Hdr10Plus = 1
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
    BluePrimary = property(get_BluePrimary, None)
    CurrentAdvancedColorKind = property(get_CurrentAdvancedColorKind, None)
    GreenPrimary = property(get_GreenPrimary, None)
    MaxAverageFullFrameLuminanceInNits = property(get_MaxAverageFullFrameLuminanceInNits, None)
    MaxLuminanceInNits = property(get_MaxLuminanceInNits, None)
    MinLuminanceInNits = property(get_MinLuminanceInNits, None)
    RedPrimary = property(get_RedPrimary, None)
    SdrWhiteLevelInNits = property(get_SdrWhiteLevelInNits, None)
    WhitePoint = property(get_WhitePoint, None)
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
    def add_IsSupportedChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.BrightnessOverride, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_IsSupportedChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_IsOverrideActiveChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.BrightnessOverride, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_IsOverrideActiveChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_BrightnessLevelChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.BrightnessOverride, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_BrightnessLevelChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BrightnessLevel = property(get_BrightnessLevel, None)
    IsOverrideActive = property(get_IsOverrideActive, None)
    IsSupported = property(get_IsSupported, None)
    IsSupportedChanged = event()
    IsOverrideActiveChanged = event()
    BrightnessLevelChanged = event()
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
    def add_CanOverrideChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayEnhancementOverride, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_CanOverrideChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_IsOverrideActiveChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayEnhancementOverride, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_IsOverrideActiveChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_DisplayEnhancementOverrideCapabilitiesChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayEnhancementOverride, win32more.Windows.Graphics.Display.DisplayEnhancementOverrideCapabilitiesChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_DisplayEnhancementOverrideCapabilitiesChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BrightnessOverrideSettings = property(get_BrightnessOverrideSettings, put_BrightnessOverrideSettings)
    CanOverride = property(get_CanOverride, None)
    ColorOverrideSettings = property(get_ColorOverrideSettings, put_ColorOverrideSettings)
    IsOverrideActive = property(get_IsOverrideActive, None)
    CanOverrideChanged = event()
    IsOverrideActiveChanged = event()
    DisplayEnhancementOverrideCapabilitiesChanged = event()
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
    def add_OrientationChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
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
    def add_DpiChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_DpiChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def get_StereoEnabled(self) -> Boolean: ...
    @winrt_commethod(17)
    def add_StereoEnabledChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_StereoEnabledChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def GetColorProfileAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_commethod(20)
    def add_ColorProfileChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_ColorProfileChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentOrientation = property(get_CurrentOrientation, None)
    LogicalDpi = property(get_LogicalDpi, None)
    NativeOrientation = property(get_NativeOrientation, None)
    RawDpiX = property(get_RawDpiX, None)
    RawDpiY = property(get_RawDpiY, None)
    ResolutionScale = property(get_ResolutionScale, None)
    StereoEnabled = property(get_StereoEnabled, None)
    OrientationChanged = event()
    DpiChanged = event()
    StereoEnabledChanged = event()
    ColorProfileChanged = event()
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
    ScreenHeightInRawPixels = property(get_ScreenHeightInRawPixels, None)
    ScreenWidthInRawPixels = property(get_ScreenWidthInRawPixels, None)
class IDisplayInformation5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IDisplayInformation5'
    _iid_ = Guid('{3a5442dc-2cde-4a8d-80d1-21dc5adcc1aa}')
    @winrt_commethod(6)
    def GetAdvancedColorInfo(self) -> win32more.Windows.Graphics.Display.AdvancedColorInfo: ...
    @winrt_commethod(7)
    def add_AdvancedColorInfoChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_AdvancedColorInfoChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AdvancedColorInfoChanged = event()
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
    def add_DisplayContentsInvalidated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_DisplayContentsInvalidated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AutoRotationPreferences = property(get_AutoRotationPreferences, put_AutoRotationPreferences)
    DisplayContentsInvalidated = event()
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
    AutoRotationPreferences = property(get_AutoRotationPreferences, put_AutoRotationPreferences)
    CurrentOrientation = property(get_CurrentOrientation, None)
    LogicalDpi = property(get_LogicalDpi, None)
    NativeOrientation = property(get_NativeOrientation, None)
    ResolutionScale = property(get_ResolutionScale, None)
    StereoEnabled = property(get_StereoEnabled, None)
    OrientationChanged = event()
    LogicalDpiChanged = event()
    StereoEnabledChanged = event()
    ColorProfileChanged = event()
    DisplayContentsInvalidated = event()
class IDisplayServices(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IDisplayServices'
    _iid_ = Guid('{1b54f32b-890d-5747-bd26-fdbdeb0c8a71}')
class IDisplayServicesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Display.IDisplayServicesStatics'
    _iid_ = Guid('{dc2096bf-730a-5560-b461-91c13d692e0c}')
    @winrt_commethod(6)
    def FindAll(self) -> ReceiveArray[win32more.Windows.Graphics.DisplayId]: ...
class NitRange(Structure):
    MinNits: Single
    MaxNits: Single
    StepSizeNits: Single
class ResolutionScale(Enum, Int32):
    Invalid = 0
    Scale100Percent = 100
    Scale120Percent = 120
    Scale125Percent = 125
    Scale140Percent = 140
    Scale150Percent = 150
    Scale160Percent = 160
    Scale175Percent = 175
    Scale180Percent = 180
    Scale200Percent = 200
    Scale225Percent = 225
    Scale250Percent = 250
    Scale300Percent = 300
    Scale350Percent = 350
    Scale400Percent = 400
    Scale450Percent = 450
    Scale500Percent = 500


make_ready(__name__)
