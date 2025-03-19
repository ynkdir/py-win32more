from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI
import win32more.Microsoft.UI.Composition
import win32more.Microsoft.UI.Composition.SystemBackdrops
import win32more.Windows.Foundation
import win32more.Windows.UI
import win32more.Windows.UI.Composition
import win32more.Windows.UI.Core
import win32more.Windows.Win32.System.WinRT
class DesktopAcrylicController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.UI.Composition.SystemBackdrops.IDesktopAcrylicController
    _classid_ = 'Microsoft.UI.Composition.SystemBackdrops.DesktopAcrylicController'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Composition.SystemBackdrops.DesktopAcrylicController.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Composition.SystemBackdrops.DesktopAcrylicController: ...
    @winrt_mixinmethod
    def RemoveAllSystemBackdropTargets(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropControllerWithTargets) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IDesktopAcrylicController3) -> win32more.Microsoft.UI.Composition.SystemBackdrops.DesktopAcrylicKind: ...
    @winrt_mixinmethod
    def put_Kind(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IDesktopAcrylicController3, value: win32more.Microsoft.UI.Composition.SystemBackdrops.DesktopAcrylicKind) -> Void: ...
    @winrt_mixinmethod
    def SetTargetWithWindowId(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropController, windowId: win32more.Microsoft.UI.WindowId, desktopWindowTarget: win32more.Windows.UI.Composition.CompositionTarget) -> Boolean: ...
    @winrt_mixinmethod
    def SetTargetWithCoreWindow(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropController, coreWindow: win32more.Windows.UI.Core.CoreWindow, compositionTarget: win32more.Windows.UI.Composition.CompositionTarget) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropControllerWithTargets) -> win32more.Microsoft.UI.Composition.SystemBackdrops.SystemBackdropState: ...
    @winrt_mixinmethod
    def AddSystemBackdropTarget(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropControllerWithTargets, systemBackdropTarget: win32more.Microsoft.UI.Composition.ICompositionSupportsSystemBackdrop) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsClosed(self: win32more.Microsoft.UI.IClosableNotifier) -> Boolean: ...
    @winrt_mixinmethod
    def RemoveSystemBackdropTarget(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropControllerWithTargets, systemBackdropTarget: win32more.Microsoft.UI.Composition.ICompositionSupportsSystemBackdrop) -> Boolean: ...
    @winrt_mixinmethod
    def SetSystemBackdropConfiguration(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropControllerWithTargets, configuration: win32more.Microsoft.UI.Composition.SystemBackdrops.SystemBackdropConfiguration) -> Void: ...
    @winrt_mixinmethod
    def add_StateChanged(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropControllerWithTargets, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropControllerWithTargets, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def put_FallbackColor(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IDesktopAcrylicController, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropControllerWithTargets, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_FallbackColor(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IDesktopAcrylicController) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def add_Closed(self: win32more.Microsoft.UI.IClosableNotifier, handler: win32more.Microsoft.UI.ClosableNotifierHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: win32more.Microsoft.UI.IClosableNotifier, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameworkClosed(self: win32more.Microsoft.UI.IClosableNotifier, handler: win32more.Microsoft.UI.ClosableNotifierHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameworkClosed(self: win32more.Microsoft.UI.IClosableNotifier, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_LuminosityOpacity(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IDesktopAcrylicController) -> Single: ...
    @winrt_mixinmethod
    def put_LuminosityOpacity(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IDesktopAcrylicController, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_TintColor(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IDesktopAcrylicController) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_TintColor(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IDesktopAcrylicController, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_TintOpacity(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IDesktopAcrylicController) -> Single: ...
    @winrt_mixinmethod
    def put_TintOpacity(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IDesktopAcrylicController, value: Single) -> Void: ...
    @winrt_mixinmethod
    def ResetProperties(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IDesktopAcrylicController2) -> Void: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Microsoft.UI.Composition.SystemBackdrops.IDesktopAcrylicControllerStatics) -> Boolean: ...
    FallbackColor = property(get_FallbackColor, put_FallbackColor)
    IsClosed = property(get_IsClosed, None)
    Kind = property(get_Kind, put_Kind)
    LuminosityOpacity = property(get_LuminosityOpacity, put_LuminosityOpacity)
    State = property(get_State, None)
    TintColor = property(get_TintColor, put_TintColor)
    TintOpacity = property(get_TintOpacity, put_TintOpacity)
    StateChanged = event()
    Closed = event()
    FrameworkClosed = event()
class DesktopAcrylicKind(Enum, Int32):
    Default = 0
    Base = 1
    Thin = 2
class IDesktopAcrylicController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.SystemBackdrops.IDesktopAcrylicController'
    _iid_ = Guid('{7c20a6af-8eb3-5f08-bdfc-6d35e35dfe45}')
    @winrt_commethod(6)
    def get_FallbackColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_FallbackColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_LuminosityOpacity(self) -> Single: ...
    @winrt_commethod(9)
    def put_LuminosityOpacity(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_TintColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(11)
    def put_TintColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(12)
    def get_TintOpacity(self) -> Single: ...
    @winrt_commethod(13)
    def put_TintOpacity(self, value: Single) -> Void: ...
    FallbackColor = property(get_FallbackColor, put_FallbackColor)
    LuminosityOpacity = property(get_LuminosityOpacity, put_LuminosityOpacity)
    TintColor = property(get_TintColor, put_TintColor)
    TintOpacity = property(get_TintOpacity, put_TintOpacity)
class IDesktopAcrylicController2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.SystemBackdrops.IDesktopAcrylicController2'
    _iid_ = Guid('{88e0a368-dfc7-5971-a50b-40df5aa5f5c2}')
    @winrt_commethod(6)
    def ResetProperties(self) -> Void: ...
class IDesktopAcrylicController3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.SystemBackdrops.IDesktopAcrylicController3'
    _iid_ = Guid('{30d917e6-02d3-59ca-b440-bf9d2e7cc140}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Microsoft.UI.Composition.SystemBackdrops.DesktopAcrylicKind: ...
    @winrt_commethod(7)
    def put_Kind(self, value: win32more.Microsoft.UI.Composition.SystemBackdrops.DesktopAcrylicKind) -> Void: ...
    Kind = property(get_Kind, put_Kind)
class IDesktopAcrylicControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.SystemBackdrops.IDesktopAcrylicControllerStatics'
    _iid_ = Guid('{a9e8f790-79ef-5416-9b67-6bcfe867c8b7}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
class IMicaController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.SystemBackdrops.IMicaController'
    _iid_ = Guid('{2de996a9-0a2a-5889-a89c-1f84060a8cab}')
    @winrt_commethod(6)
    def get_FallbackColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_FallbackColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_LuminosityOpacity(self) -> Single: ...
    @winrt_commethod(9)
    def put_LuminosityOpacity(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_TintColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(11)
    def put_TintColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(12)
    def get_TintOpacity(self) -> Single: ...
    @winrt_commethod(13)
    def put_TintOpacity(self, value: Single) -> Void: ...
    FallbackColor = property(get_FallbackColor, put_FallbackColor)
    LuminosityOpacity = property(get_LuminosityOpacity, put_LuminosityOpacity)
    TintColor = property(get_TintColor, put_TintColor)
    TintOpacity = property(get_TintOpacity, put_TintOpacity)
class IMicaController2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.SystemBackdrops.IMicaController2'
    _iid_ = Guid('{f1ed4a52-d9ca-506e-9586-caaefd3aa971}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Microsoft.UI.Composition.SystemBackdrops.MicaKind: ...
    @winrt_commethod(7)
    def put_Kind(self, value: win32more.Microsoft.UI.Composition.SystemBackdrops.MicaKind) -> Void: ...
    @winrt_commethod(8)
    def ResetProperties(self) -> Void: ...
    Kind = property(get_Kind, put_Kind)
class IMicaControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.SystemBackdrops.IMicaControllerStatics'
    _iid_ = Guid('{7d85d834-d514-5250-b7c4-0b7850d1efdc}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
class ISystemBackdropConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropConfiguration'
    _iid_ = Guid('{ebcce1b9-0e0c-5431-ab0e-00f3f0669962}')
    @winrt_commethod(6)
    def get_HighContrastBackgroundColor(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_commethod(7)
    def put_HighContrastBackgroundColor(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_commethod(8)
    def get_IsHighContrast(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsHighContrast(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_IsInputActive(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsInputActive(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_Theme(self) -> win32more.Microsoft.UI.Composition.SystemBackdrops.SystemBackdropTheme: ...
    @winrt_commethod(13)
    def put_Theme(self, value: win32more.Microsoft.UI.Composition.SystemBackdrops.SystemBackdropTheme) -> Void: ...
    HighContrastBackgroundColor = property(get_HighContrastBackgroundColor, put_HighContrastBackgroundColor)
    IsHighContrast = property(get_IsHighContrast, put_IsHighContrast)
    IsInputActive = property(get_IsInputActive, put_IsInputActive)
    Theme = property(get_Theme, put_Theme)
class ISystemBackdropController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropController'
    _iid_ = Guid('{5632d76c-0b74-5b52-aa33-80262068aeb2}')
    @winrt_commethod(6)
    def SetTargetWithWindowId(self, windowId: win32more.Microsoft.UI.WindowId, desktopWindowTarget: win32more.Windows.UI.Composition.CompositionTarget) -> Boolean: ...
    @winrt_commethod(7)
    def SetTargetWithCoreWindow(self, coreWindow: win32more.Windows.UI.Core.CoreWindow, compositionTarget: win32more.Windows.UI.Composition.CompositionTarget) -> Boolean: ...
class ISystemBackdropControllerWithTargets(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    _classid_ = 'Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropControllerWithTargets'
    _iid_ = Guid('{9c56fe7c-98eb-5f89-ad97-dad57fc30c8c}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Microsoft.UI.Composition.SystemBackdrops.SystemBackdropState: ...
    @winrt_commethod(7)
    def AddSystemBackdropTarget(self, systemBackdropTarget: win32more.Microsoft.UI.Composition.ICompositionSupportsSystemBackdrop) -> Boolean: ...
    @winrt_commethod(8)
    def RemoveAllSystemBackdropTargets(self) -> Void: ...
    @winrt_commethod(9)
    def RemoveSystemBackdropTarget(self, systemBackdropTarget: win32more.Microsoft.UI.Composition.ICompositionSupportsSystemBackdrop) -> Boolean: ...
    @winrt_commethod(10)
    def SetSystemBackdropConfiguration(self, configuration: win32more.Microsoft.UI.Composition.SystemBackdrops.SystemBackdropConfiguration) -> Void: ...
    @winrt_commethod(11)
    def add_StateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropControllerWithTargets, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_StateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    State = property(get_State, None)
    StateChanged = event()
class MicaController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.UI.Composition.SystemBackdrops.IMicaController
    _classid_ = 'Microsoft.UI.Composition.SystemBackdrops.MicaController'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Composition.SystemBackdrops.MicaController.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Composition.SystemBackdrops.MicaController: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropControllerWithTargets, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Closed(self: win32more.Microsoft.UI.IClosableNotifier, handler: win32more.Microsoft.UI.ClosableNotifierHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: win32more.Microsoft.UI.IClosableNotifier, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameworkClosed(self: win32more.Microsoft.UI.IClosableNotifier, handler: win32more.Microsoft.UI.ClosableNotifierHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameworkClosed(self: win32more.Microsoft.UI.IClosableNotifier, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ResetProperties(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IMicaController2) -> Void: ...
    @winrt_mixinmethod
    def get_IsClosed(self: win32more.Microsoft.UI.IClosableNotifier) -> Boolean: ...
    @winrt_mixinmethod
    def get_FallbackColor(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IMicaController) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_FallbackColor(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IMicaController, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_LuminosityOpacity(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IMicaController) -> Single: ...
    @winrt_mixinmethod
    def put_LuminosityOpacity(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IMicaController, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_TintColor(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IMicaController) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_TintColor(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IMicaController, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_TintOpacity(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IMicaController) -> Single: ...
    @winrt_mixinmethod
    def put_TintOpacity(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IMicaController, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IMicaController2) -> win32more.Microsoft.UI.Composition.SystemBackdrops.MicaKind: ...
    @winrt_mixinmethod
    def put_Kind(self: win32more.Microsoft.UI.Composition.SystemBackdrops.IMicaController2, value: win32more.Microsoft.UI.Composition.SystemBackdrops.MicaKind) -> Void: ...
    @winrt_mixinmethod
    def SetTargetWithWindowId(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropController, windowId: win32more.Microsoft.UI.WindowId, desktopWindowTarget: win32more.Windows.UI.Composition.CompositionTarget) -> Boolean: ...
    @winrt_mixinmethod
    def SetTargetWithCoreWindow(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropController, coreWindow: win32more.Windows.UI.Core.CoreWindow, compositionTarget: win32more.Windows.UI.Composition.CompositionTarget) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropControllerWithTargets) -> win32more.Microsoft.UI.Composition.SystemBackdrops.SystemBackdropState: ...
    @winrt_mixinmethod
    def AddSystemBackdropTarget(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropControllerWithTargets, systemBackdropTarget: win32more.Microsoft.UI.Composition.ICompositionSupportsSystemBackdrop) -> Boolean: ...
    @winrt_mixinmethod
    def RemoveAllSystemBackdropTargets(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropControllerWithTargets) -> Void: ...
    @winrt_mixinmethod
    def RemoveSystemBackdropTarget(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropControllerWithTargets, systemBackdropTarget: win32more.Microsoft.UI.Composition.ICompositionSupportsSystemBackdrop) -> Boolean: ...
    @winrt_mixinmethod
    def SetSystemBackdropConfiguration(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropControllerWithTargets, configuration: win32more.Microsoft.UI.Composition.SystemBackdrops.SystemBackdropConfiguration) -> Void: ...
    @winrt_mixinmethod
    def add_StateChanged(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropControllerWithTargets, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropControllerWithTargets, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def IsSupported(cls: win32more.Microsoft.UI.Composition.SystemBackdrops.IMicaControllerStatics) -> Boolean: ...
    FallbackColor = property(get_FallbackColor, put_FallbackColor)
    IsClosed = property(get_IsClosed, None)
    Kind = property(get_Kind, put_Kind)
    LuminosityOpacity = property(get_LuminosityOpacity, put_LuminosityOpacity)
    State = property(get_State, None)
    TintColor = property(get_TintColor, put_TintColor)
    TintOpacity = property(get_TintOpacity, put_TintOpacity)
    Closed = event()
    FrameworkClosed = event()
    StateChanged = event()
class MicaKind(Enum, Int32):
    Base = 0
    BaseAlt = 1
class SystemBackdropConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropConfiguration
    _classid_ = 'Microsoft.UI.Composition.SystemBackdrops.SystemBackdropConfiguration'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Composition.SystemBackdrops.SystemBackdropConfiguration.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Composition.SystemBackdrops.SystemBackdropConfiguration: ...
    @winrt_mixinmethod
    def get_HighContrastBackgroundColor(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropConfiguration) -> win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]: ...
    @winrt_mixinmethod
    def get_IsInputActive(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def get_Theme(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropConfiguration) -> win32more.Microsoft.UI.Composition.SystemBackdrops.SystemBackdropTheme: ...
    @winrt_mixinmethod
    def put_IsInputActive(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropConfiguration, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def put_Theme(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropConfiguration, value: win32more.Microsoft.UI.Composition.SystemBackdrops.SystemBackdropTheme) -> Void: ...
    @winrt_mixinmethod
    def get_IsHighContrast(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def put_HighContrastBackgroundColor(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropConfiguration, value: win32more.Windows.Foundation.IReference[win32more.Windows.UI.Color]) -> Void: ...
    @winrt_mixinmethod
    def put_IsHighContrast(self: win32more.Microsoft.UI.Composition.SystemBackdrops.ISystemBackdropConfiguration, value: Boolean) -> Void: ...
    HighContrastBackgroundColor = property(get_HighContrastBackgroundColor, put_HighContrastBackgroundColor)
    IsHighContrast = property(get_IsHighContrast, put_IsHighContrast)
    IsInputActive = property(get_IsInputActive, put_IsInputActive)
    Theme = property(get_Theme, put_Theme)
class SystemBackdropState(Enum, Int32):
    Active = 0
    Fallback = 1
    HighContrast = 2
class SystemBackdropTheme(Enum, Int32):
    Default = 0
    Light = 1
    Dark = 2


make_ready(__name__)
