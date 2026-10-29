from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.ApplicationModel.Overlay
import win32more.Windows.Foundation
class IOverlayActivatedEventArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Overlay.IOverlayActivatedEventArgs'
    _iid_ = Guid('{277092d8-617c-50ba-9e57-6dc25078beb0}')
    @winrt_commethod(6)
    def get_Command(self) -> win32more.Windows.ApplicationModel.Overlay.OverlayCommand: ...
    Command = property(get_Command, None)
class IOverlayApp(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Overlay.IOverlayApp'
    _iid_ = Guid('{0410c228-3813-54fc-b402-88520526d1f5}')
    @winrt_commethod(6)
    def StartAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def DisconnectAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def get_VisualState(self) -> win32more.Windows.ApplicationModel.Overlay.OverlayVisualState: ...
    @winrt_commethod(9)
    def add_VisualStateChanged(self, handler: win32more.Windows.Foundation.EventHandler[IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_VisualStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def RequestInteractiveAsync(self, command: win32more.Windows.ApplicationModel.Overlay.OverlayCommand) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(12)
    def ExitInteractiveAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def SetPersistentModeEnabled(self, enabled: Boolean) -> Void: ...
    @winrt_commethod(14)
    def SetUnreadNotificationCount(self, count: UInt32) -> Void: ...
    @winrt_commethod(15)
    def SetHasActiveNotification(self, hasActive: Boolean) -> Void: ...
    @winrt_commethod(16)
    def add_Activated(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.ApplicationModel.Overlay.OverlayActivatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_Activated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_VisualTransition(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.ApplicationModel.Overlay.OverlayVisualTransitionEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_VisualTransition(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_Disconnected(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.ApplicationModel.Overlay.OverlayDisconnectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_Disconnected(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    VisualState = property(get_VisualState, None)
    Activated = event(add_Activated, remove_Activated)
    Disconnected = event(add_Disconnected, remove_Disconnected)
    VisualStateChanged = event(add_VisualStateChanged, remove_VisualStateChanged)
    VisualTransition = event(add_VisualTransition, remove_VisualTransition)
class IOverlayAppOptions(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Overlay.IOverlayAppOptions'
    _iid_ = Guid('{9e0dd89a-0f2a-5cfd-805d-dbb13164c146}')
    @winrt_commethod(6)
    def get_CustomTransitionAnimations(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_CustomTransitionAnimations(self, value: Boolean) -> Void: ...
    CustomTransitionAnimations = property(get_CustomTransitionAnimations, put_CustomTransitionAnimations)
class IOverlayAppStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Overlay.IOverlayAppStatics'
    _iid_ = Guid('{2c112604-c435-53d0-9be6-6431e39eb26c}')
    @winrt_commethod(6)
    def Create(self, hwnd: Int64) -> win32more.Windows.ApplicationModel.Overlay.OverlayApp: ...
    @winrt_commethod(7)
    def Create2(self, hwnd: Int64, options: win32more.Windows.ApplicationModel.Overlay.OverlayAppOptions) -> win32more.Windows.ApplicationModel.Overlay.OverlayApp: ...
class IOverlayCommand(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Overlay.IOverlayCommand'
    _iid_ = Guid('{dde596f8-6093-5029-8cbc-06b046d328dc}')
    @winrt_commethod(6)
    def get_Source(self) -> win32more.Windows.ApplicationModel.Overlay.OverlayCommandSource: ...
    @winrt_commethod(7)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    Source = property(get_Source, None)
    Uri = property(get_Uri, None)
class IOverlayCommandFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Overlay.IOverlayCommandFactory'
    _iid_ = Guid('{10210bb2-4755-520d-802b-7490c260f802}')
    @winrt_commethod(6)
    def CreateInstance(self, source: win32more.Windows.ApplicationModel.Overlay.OverlayCommandSource, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.ApplicationModel.Overlay.OverlayCommand: ...
class IOverlayDisconnectedEventArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Overlay.IOverlayDisconnectedEventArgs'
    _iid_ = Guid('{9573e2be-6692-513e-9ed4-71642a182d42}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
class IOverlayVisualTransitionEventArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.ApplicationModel.Overlay.IOverlayVisualTransitionEventArgs'
    _iid_ = Guid('{0cc0e9dd-b088-5f81-a02b-c925259a464d}')
    @winrt_commethod(6)
    def get_NewState(self) -> win32more.Windows.ApplicationModel.Overlay.OverlayVisualState: ...
    @winrt_commethod(7)
    def get_Command(self) -> win32more.Windows.ApplicationModel.Overlay.OverlayCommand: ...
    @winrt_commethod(8)
    def get_TransitionAnimation(self) -> win32more.Windows.ApplicationModel.Overlay.OverlayTransitionAnimation: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Command = property(get_Command, None)
    NewState = property(get_NewState, None)
    TransitionAnimation = property(get_TransitionAnimation, None)
class OverlayActivatedEventArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.ApplicationModel.Overlay.IOverlayActivatedEventArgs
    _classid_ = 'Windows.ApplicationModel.Overlay.OverlayActivatedEventArgs'
    @winrt_mixinmethod
    def get_Command(self: win32more.Windows.ApplicationModel.Overlay.IOverlayActivatedEventArgs) -> win32more.Windows.ApplicationModel.Overlay.OverlayCommand: ...
    Command = property(get_Command, None)
class OverlayApp(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.ApplicationModel.Overlay.IOverlayApp
    _classid_ = 'Windows.ApplicationModel.Overlay.OverlayApp'
    @winrt_mixinmethod
    def StartAsync(self: win32more.Windows.ApplicationModel.Overlay.IOverlayApp) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def DisconnectAsync(self: win32more.Windows.ApplicationModel.Overlay.IOverlayApp) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_VisualState(self: win32more.Windows.ApplicationModel.Overlay.IOverlayApp) -> win32more.Windows.ApplicationModel.Overlay.OverlayVisualState: ...
    @winrt_mixinmethod
    def add_VisualStateChanged(self: win32more.Windows.ApplicationModel.Overlay.IOverlayApp, handler: win32more.Windows.Foundation.EventHandler[IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VisualStateChanged(self: win32more.Windows.ApplicationModel.Overlay.IOverlayApp, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def RequestInteractiveAsync(self: win32more.Windows.ApplicationModel.Overlay.IOverlayApp, command: win32more.Windows.ApplicationModel.Overlay.OverlayCommand) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ExitInteractiveAsync(self: win32more.Windows.ApplicationModel.Overlay.IOverlayApp) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SetPersistentModeEnabled(self: win32more.Windows.ApplicationModel.Overlay.IOverlayApp, enabled: Boolean) -> Void: ...
    @winrt_mixinmethod
    def SetUnreadNotificationCount(self: win32more.Windows.ApplicationModel.Overlay.IOverlayApp, count: UInt32) -> Void: ...
    @winrt_mixinmethod
    def SetHasActiveNotification(self: win32more.Windows.ApplicationModel.Overlay.IOverlayApp, hasActive: Boolean) -> Void: ...
    @winrt_mixinmethod
    def add_Activated(self: win32more.Windows.ApplicationModel.Overlay.IOverlayApp, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.ApplicationModel.Overlay.OverlayActivatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Activated(self: win32more.Windows.ApplicationModel.Overlay.IOverlayApp, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_VisualTransition(self: win32more.Windows.ApplicationModel.Overlay.IOverlayApp, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.ApplicationModel.Overlay.OverlayVisualTransitionEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VisualTransition(self: win32more.Windows.ApplicationModel.Overlay.IOverlayApp, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Disconnected(self: win32more.Windows.ApplicationModel.Overlay.IOverlayApp, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.ApplicationModel.Overlay.OverlayDisconnectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Disconnected(self: win32more.Windows.ApplicationModel.Overlay.IOverlayApp, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.ApplicationModel.Overlay.IOverlayAppStatics, hwnd: Int64) -> win32more.Windows.ApplicationModel.Overlay.OverlayApp: ...
    @winrt_classmethod
    def Create2(cls: win32more.Windows.ApplicationModel.Overlay.IOverlayAppStatics, hwnd: Int64, options: win32more.Windows.ApplicationModel.Overlay.OverlayAppOptions) -> win32more.Windows.ApplicationModel.Overlay.OverlayApp: ...
    VisualState = property(get_VisualState, None)
    Activated = event(add_Activated, remove_Activated)
    Disconnected = event(add_Disconnected, remove_Disconnected)
    VisualStateChanged = event(add_VisualStateChanged, remove_VisualStateChanged)
    VisualTransition = event(add_VisualTransition, remove_VisualTransition)
class OverlayAppOptions(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.ApplicationModel.Overlay.IOverlayAppOptions
    _classid_ = 'Windows.ApplicationModel.Overlay.OverlayAppOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.ApplicationModel.Overlay.OverlayAppOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.ApplicationModel.Overlay.OverlayAppOptions: ...
    @winrt_mixinmethod
    def get_CustomTransitionAnimations(self: win32more.Windows.ApplicationModel.Overlay.IOverlayAppOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_CustomTransitionAnimations(self: win32more.Windows.ApplicationModel.Overlay.IOverlayAppOptions, value: Boolean) -> Void: ...
    CustomTransitionAnimations = property(get_CustomTransitionAnimations, put_CustomTransitionAnimations)
class OverlayCommand(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.ApplicationModel.Overlay.IOverlayCommand
    _classid_ = 'Windows.ApplicationModel.Overlay.OverlayCommand'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.ApplicationModel.Overlay.OverlayCommand.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.ApplicationModel.Overlay.IOverlayCommandFactory, source: win32more.Windows.ApplicationModel.Overlay.OverlayCommandSource, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.ApplicationModel.Overlay.OverlayCommand: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.ApplicationModel.Overlay.IOverlayCommand) -> win32more.Windows.ApplicationModel.Overlay.OverlayCommandSource: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.ApplicationModel.Overlay.IOverlayCommand) -> win32more.Windows.Foundation.Uri: ...
    Source = property(get_Source, None)
    Uri = property(get_Uri, None)
class OverlayCommandSource(Enum, Int32):
    _name_ = 'Windows.ApplicationModel.Overlay.OverlayCommandSource'
    Keyboard = 0
    Gamepad = 1
    Programmatic = 2
    Pointer = 3
OverlayContract: UInt32 = 65536
class OverlayDisconnectedEventArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.ApplicationModel.Overlay.IOverlayDisconnectedEventArgs
    _classid_ = 'Windows.ApplicationModel.Overlay.OverlayDisconnectedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Overlay.IOverlayDisconnectedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
class OverlayTransitionAnimation(Enum, Int32):
    _name_ = 'Windows.ApplicationModel.Overlay.OverlayTransitionAnimation'
    Disabled = 0
    PlatformAuto = 1
    Fade = 2
    SlideLeft = 3
    SlideRight = 4
class OverlayVisualState(Enum, Int32):
    _name_ = 'Windows.ApplicationModel.Overlay.OverlayVisualState'
    Hidden = 0
    Persistent = 1
    Interactive = 2
class OverlayVisualTransitionEventArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.ApplicationModel.Overlay.IOverlayVisualTransitionEventArgs
    _classid_ = 'Windows.ApplicationModel.Overlay.OverlayVisualTransitionEventArgs'
    @winrt_mixinmethod
    def get_NewState(self: win32more.Windows.ApplicationModel.Overlay.IOverlayVisualTransitionEventArgs) -> win32more.Windows.ApplicationModel.Overlay.OverlayVisualState: ...
    @winrt_mixinmethod
    def get_Command(self: win32more.Windows.ApplicationModel.Overlay.IOverlayVisualTransitionEventArgs) -> win32more.Windows.ApplicationModel.Overlay.OverlayCommand: ...
    @winrt_mixinmethod
    def get_TransitionAnimation(self: win32more.Windows.ApplicationModel.Overlay.IOverlayVisualTransitionEventArgs) -> win32more.Windows.ApplicationModel.Overlay.OverlayTransitionAnimation: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Overlay.IOverlayVisualTransitionEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Command = property(get_Command, None)
    NewState = property(get_NewState, None)
    TransitionAnimation = property(get_TransitionAnimation, None)


make_ready(__name__)
