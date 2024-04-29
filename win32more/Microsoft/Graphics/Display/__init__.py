from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import FillArray, Generic, K, MulticastDelegate, PassArray, ReceiveArray, T, TProgress, TResult, TSender, V, WinRT_String, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Graphics.Display
import win32more.Microsoft.UI
import win32more.Microsoft.UI.Dispatching
import win32more.Windows.Foundation
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class DisplayAdvancedColorInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Graphics.Display.IDisplayAdvancedColorInfo
    _classid_ = 'Microsoft.Graphics.Display.DisplayAdvancedColorInfo'
    @winrt_mixinmethod
    def get_CurrentAdvancedColorKind(self: win32more.Microsoft.Graphics.Display.IDisplayAdvancedColorInfo) -> win32more.Microsoft.Graphics.Display.DisplayAdvancedColorKind: ...
    @winrt_mixinmethod
    def get_RedPrimary(self: win32more.Microsoft.Graphics.Display.IDisplayAdvancedColorInfo) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_GreenPrimary(self: win32more.Microsoft.Graphics.Display.IDisplayAdvancedColorInfo) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_BluePrimary(self: win32more.Microsoft.Graphics.Display.IDisplayAdvancedColorInfo) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_WhitePoint(self: win32more.Microsoft.Graphics.Display.IDisplayAdvancedColorInfo) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_MaxLuminanceInNits(self: win32more.Microsoft.Graphics.Display.IDisplayAdvancedColorInfo) -> Double: ...
    @winrt_mixinmethod
    def get_MinLuminanceInNits(self: win32more.Microsoft.Graphics.Display.IDisplayAdvancedColorInfo) -> Double: ...
    @winrt_mixinmethod
    def get_MaxAverageFullFrameLuminanceInNits(self: win32more.Microsoft.Graphics.Display.IDisplayAdvancedColorInfo) -> Double: ...
    @winrt_mixinmethod
    def get_SdrWhiteLevelInNits(self: win32more.Microsoft.Graphics.Display.IDisplayAdvancedColorInfo) -> Double: ...
    @winrt_mixinmethod
    def IsHdrMetadataFormatCurrentlySupported(self: win32more.Microsoft.Graphics.Display.IDisplayAdvancedColorInfo, format: win32more.Microsoft.Graphics.Display.DisplayHdrMetadataFormat) -> Boolean: ...
    @winrt_mixinmethod
    def IsAdvancedColorKindAvailable(self: win32more.Microsoft.Graphics.Display.IDisplayAdvancedColorInfo, kind: win32more.Microsoft.Graphics.Display.DisplayAdvancedColorKind) -> Boolean: ...
    BluePrimary = property(get_BluePrimary, None)
    CurrentAdvancedColorKind = property(get_CurrentAdvancedColorKind, None)
    GreenPrimary = property(get_GreenPrimary, None)
    MaxAverageFullFrameLuminanceInNits = property(get_MaxAverageFullFrameLuminanceInNits, None)
    MaxLuminanceInNits = property(get_MaxLuminanceInNits, None)
    MinLuminanceInNits = property(get_MinLuminanceInNits, None)
    RedPrimary = property(get_RedPrimary, None)
    SdrWhiteLevelInNits = property(get_SdrWhiteLevelInNits, None)
    WhitePoint = property(get_WhitePoint, None)
class DisplayAdvancedColorKind(Int32):  # enum
    StandardDynamicRange = 0
    WideColorGamut = 1
    HighDynamicRange = 2
class DisplayHdrMetadataFormat(Int32):  # enum
    Hdr10 = 0
    Hdr10Plus = 1
class DisplayInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Graphics.Display.IDisplayInformation
    _classid_ = 'Microsoft.Graphics.Display.DisplayInformation'
    @winrt_mixinmethod
    def get_IsStereoEnabled(self: win32more.Microsoft.Graphics.Display.IDisplayInformation) -> Boolean: ...
    @winrt_mixinmethod
    def GetColorProfileAsync(self: win32more.Microsoft.Graphics.Display.IDisplayInformation) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def add_IsStereoEnabledChanged(self: win32more.Microsoft.Graphics.Display.IDisplayInformation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsStereoEnabledChanged(self: win32more.Microsoft.Graphics.Display.IDisplayInformation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DispatcherQueue(self: win32more.Microsoft.Graphics.Display.IDisplayInformation) -> win32more.Microsoft.UI.Dispatching.DispatcherQueue: ...
    @winrt_mixinmethod
    def GetColorProfile(self: win32more.Microsoft.Graphics.Display.IDisplayInformation) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def add_ColorProfileChanged(self: win32more.Microsoft.Graphics.Display.IDisplayInformation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ColorProfileChanged(self: win32more.Microsoft.Graphics.Display.IDisplayInformation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetAdvancedColorInfo(self: win32more.Microsoft.Graphics.Display.IDisplayInformation) -> win32more.Microsoft.Graphics.Display.DisplayAdvancedColorInfo: ...
    @winrt_mixinmethod
    def add_AdvancedColorInfoChanged(self: win32more.Microsoft.Graphics.Display.IDisplayInformation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AdvancedColorInfoChanged(self: win32more.Microsoft.Graphics.Display.IDisplayInformation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Destroyed(self: win32more.Microsoft.Graphics.Display.IDisplayInformation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Destroyed(self: win32more.Microsoft.Graphics.Display.IDisplayInformation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateForWindowId(cls: win32more.Microsoft.Graphics.Display.IDisplayInformationStatics, windowId: win32more.Microsoft.UI.WindowId) -> win32more.Microsoft.Graphics.Display.DisplayInformation: ...
    @winrt_classmethod
    def CreateForDisplayId(cls: win32more.Microsoft.Graphics.Display.IDisplayInformationStatics, displayId: win32more.Microsoft.UI.DisplayId) -> win32more.Microsoft.Graphics.Display.DisplayInformation: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
    IsStereoEnabled = property(get_IsStereoEnabled, None)
class IDisplayAdvancedColorInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Display.IDisplayAdvancedColorInfo'
    _iid_ = Guid('{b44f0f47-7065-5175-ba3e-714489c85a3e}')
    @winrt_commethod(6)
    def get_CurrentAdvancedColorKind(self) -> win32more.Microsoft.Graphics.Display.DisplayAdvancedColorKind: ...
    @winrt_commethod(7)
    def get_RedPrimary(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_GreenPrimary(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def get_BluePrimary(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(10)
    def get_WhitePoint(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(11)
    def get_MaxLuminanceInNits(self) -> Double: ...
    @winrt_commethod(12)
    def get_MinLuminanceInNits(self) -> Double: ...
    @winrt_commethod(13)
    def get_MaxAverageFullFrameLuminanceInNits(self) -> Double: ...
    @winrt_commethod(14)
    def get_SdrWhiteLevelInNits(self) -> Double: ...
    @winrt_commethod(15)
    def IsHdrMetadataFormatCurrentlySupported(self, format: win32more.Microsoft.Graphics.Display.DisplayHdrMetadataFormat) -> Boolean: ...
    @winrt_commethod(16)
    def IsAdvancedColorKindAvailable(self, kind: win32more.Microsoft.Graphics.Display.DisplayAdvancedColorKind) -> Boolean: ...
    BluePrimary = property(get_BluePrimary, None)
    CurrentAdvancedColorKind = property(get_CurrentAdvancedColorKind, None)
    GreenPrimary = property(get_GreenPrimary, None)
    MaxAverageFullFrameLuminanceInNits = property(get_MaxAverageFullFrameLuminanceInNits, None)
    MaxLuminanceInNits = property(get_MaxLuminanceInNits, None)
    MinLuminanceInNits = property(get_MinLuminanceInNits, None)
    RedPrimary = property(get_RedPrimary, None)
    SdrWhiteLevelInNits = property(get_SdrWhiteLevelInNits, None)
    WhitePoint = property(get_WhitePoint, None)
class IDisplayInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Display.IDisplayInformation'
    _iid_ = Guid('{f0d58d4f-84ce-5b27-b222-4f8f7dc0aaeb}')
    @winrt_commethod(6)
    def get_DispatcherQueue(self) -> win32more.Microsoft.UI.Dispatching.DispatcherQueue: ...
    @winrt_commethod(7)
    def get_IsStereoEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def add_IsStereoEnabledChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_IsStereoEnabledChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def GetColorProfileAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_commethod(11)
    def GetColorProfile(self) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(12)
    def add_ColorProfileChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_ColorProfileChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def GetAdvancedColorInfo(self) -> win32more.Microsoft.Graphics.Display.DisplayAdvancedColorInfo: ...
    @winrt_commethod(15)
    def add_AdvancedColorInfoChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_AdvancedColorInfoChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_Destroyed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Graphics.Display.DisplayInformation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_Destroyed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
    IsStereoEnabled = property(get_IsStereoEnabled, None)
class IDisplayInformationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Graphics.Display.IDisplayInformationStatics'
    _iid_ = Guid('{2de85048-37fa-56c0-ac30-47e2044d7ea8}')
    @winrt_commethod(6)
    def CreateForWindowId(self, windowId: win32more.Microsoft.UI.WindowId) -> win32more.Microsoft.Graphics.Display.DisplayInformation: ...
    @winrt_commethod(7)
    def CreateForDisplayId(self, displayId: win32more.Microsoft.UI.DisplayId) -> win32more.Microsoft.Graphics.Display.DisplayInformation: ...


make_ready(__name__)
