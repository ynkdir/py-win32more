from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Haptics
import win32more.Windows.Devices.Input
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class IKeyboardCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IKeyboardCapabilities'
    _iid_ = Guid('{3a3f9b56-6798-4bbc-833e-0f34b17c65ff}')
    @winrt_commethod(6)
    def get_KeyboardPresent(self) -> Int32: ...
    KeyboardPresent = property(get_KeyboardPresent, None)
class IMouseCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IMouseCapabilities'
    _iid_ = Guid('{bca5e023-7dd9-4b6b-9a92-55d43cb38f73}')
    @winrt_commethod(6)
    def get_MousePresent(self) -> Int32: ...
    @winrt_commethod(7)
    def get_VerticalWheelPresent(self) -> Int32: ...
    @winrt_commethod(8)
    def get_HorizontalWheelPresent(self) -> Int32: ...
    @winrt_commethod(9)
    def get_SwapButtons(self) -> Int32: ...
    @winrt_commethod(10)
    def get_NumberOfButtons(self) -> UInt32: ...
    HorizontalWheelPresent = property(get_HorizontalWheelPresent, None)
    MousePresent = property(get_MousePresent, None)
    NumberOfButtons = property(get_NumberOfButtons, None)
    SwapButtons = property(get_SwapButtons, None)
    VerticalWheelPresent = property(get_VerticalWheelPresent, None)
class IMouseDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IMouseDevice'
    _iid_ = Guid('{88edf458-f2c8-49f4-be1f-c256b388bc11}')
    @winrt_commethod(6)
    def add_MouseMoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.MouseDevice, win32more.Windows.Devices.Input.MouseEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_MouseMoved(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    MouseMoved = event()
class IMouseDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IMouseDeviceStatics'
    _iid_ = Guid('{484a9045-6d70-49db-8e68-46ffbd17d38d}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.Devices.Input.MouseDevice: ...
class IMouseEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IMouseEventArgs'
    _iid_ = Guid('{f625aa5d-2354-4cc7-9230-96941c969fde}')
    @winrt_commethod(6)
    def get_MouseDelta(self) -> win32more.Windows.Devices.Input.MouseDelta: ...
    MouseDelta = property(get_MouseDelta, None)
class IPenButtonListener(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenButtonListener'
    _iid_ = Guid('{8245c376-1ee3-53f7-b1f7-8334a16f2815}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_IsSupportedChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.PenButtonListener, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_IsSupportedChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_TailButtonClicked(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.PenButtonListener, win32more.Windows.Devices.Input.PenTailButtonClickedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_TailButtonClicked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_TailButtonDoubleClicked(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.PenButtonListener, win32more.Windows.Devices.Input.PenTailButtonDoubleClickedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_TailButtonDoubleClicked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_TailButtonLongPressed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.PenButtonListener, win32more.Windows.Devices.Input.PenTailButtonLongPressedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_TailButtonLongPressed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsSupportedChanged = event()
    TailButtonClicked = event()
    TailButtonDoubleClicked = event()
    TailButtonLongPressed = event()
class IPenButtonListenerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenButtonListenerStatics'
    _iid_ = Guid('{19a8a584-862f-5f69-bfea-05f6584f133f}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Devices.Input.PenButtonListener: ...
class IPenDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenDevice'
    _iid_ = Guid('{31856eba-a738-5a8c-b8f6-f97ef68d18ef}')
    @winrt_commethod(6)
    def get_PenId(self) -> Guid: ...
    PenId = property(get_PenId, None)
class IPenDevice2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenDevice2'
    _iid_ = Guid('{0207d327-7fb8-5566-8c34-f8342037b7f9}')
    @winrt_commethod(6)
    def get_SimpleHapticsController(self) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IPenDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenDeviceStatics'
    _iid_ = Guid('{9dfbbe01-0966-5180-bcb4-b85060e39479}')
    @winrt_commethod(6)
    def GetFromPointerId(self, pointerId: UInt32) -> win32more.Windows.Devices.Input.PenDevice: ...
class IPenDockListener(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenDockListener'
    _iid_ = Guid('{759f4d90-1dc0-55cb-ad18-b9101456f592}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_IsSupportedChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.PenDockListener, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_IsSupportedChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_Docked(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.PenDockListener, win32more.Windows.Devices.Input.PenDockedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Docked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Undocked(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.PenDockListener, win32more.Windows.Devices.Input.PenUndockedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Undocked(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsSupportedChanged = event()
    Docked = event()
    Undocked = event()
class IPenDockListenerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenDockListenerStatics'
    _iid_ = Guid('{cab75e9a-0016-5c72-969e-a97e11992a93}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Devices.Input.PenDockListener: ...
class IPenDockedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenDockedEventArgs'
    _iid_ = Guid('{fd4277c6-ca63-5d4e-9ed3-a28a54521c8c}')
class IPenTailButtonClickedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenTailButtonClickedEventArgs'
    _iid_ = Guid('{5d2fb7b6-6ad3-5d3e-ab29-05ea2410e390}')
class IPenTailButtonDoubleClickedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenTailButtonDoubleClickedEventArgs'
    _iid_ = Guid('{846321a2-618a-5478-b04c-b358231da4a7}')
class IPenTailButtonLongPressedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenTailButtonLongPressedEventArgs'
    _iid_ = Guid('{f37c606e-c60a-5f42-b818-a53112406c13}')
class IPenUndockedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenUndockedEventArgs'
    _iid_ = Guid('{ccd09150-261b-59e6-a5d4-c1964cd03feb}')
class IPointerDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPointerDevice'
    _iid_ = Guid('{93c9bafc-ebcb-467e-82c6-276feae36b5a}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_IsIntegrated(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_MaxContacts(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_PhysicalDeviceRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(10)
    def get_ScreenRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(11)
    def get_SupportedUsages(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Input.PointerDeviceUsage]: ...
    IsIntegrated = property(get_IsIntegrated, None)
    MaxContacts = property(get_MaxContacts, None)
    PhysicalDeviceRect = property(get_PhysicalDeviceRect, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    ScreenRect = property(get_ScreenRect, None)
    SupportedUsages = property(get_SupportedUsages, None)
class IPointerDevice2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPointerDevice2'
    _iid_ = Guid('{f8a6d2a0-c484-489f-ae3e-30d2ee1ffd3e}')
    @winrt_commethod(6)
    def get_MaxPointersWithZDistance(self) -> UInt32: ...
    MaxPointersWithZDistance = property(get_MaxPointersWithZDistance, None)
class IPointerDeviceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPointerDeviceStatics'
    _iid_ = Guid('{d8b89aa1-d1c6-416e-bd8d-5790914dc563}')
    @winrt_commethod(6)
    def GetPointerDevice(self, pointerId: UInt32) -> win32more.Windows.Devices.Input.PointerDevice: ...
    @winrt_commethod(7)
    def GetPointerDevices(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Input.PointerDevice]: ...
class ITouchCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.ITouchCapabilities'
    _iid_ = Guid('{20dd55f9-13f1-46c8-9285-2c05fa3eda6f}')
    @winrt_commethod(6)
    def get_TouchPresent(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Contacts(self) -> UInt32: ...
    Contacts = property(get_Contacts, None)
    TouchPresent = property(get_TouchPresent, None)
class KeyboardCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.IKeyboardCapabilities
    _classid_ = 'Windows.Devices.Input.KeyboardCapabilities'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Input.KeyboardCapabilities.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Input.KeyboardCapabilities: ...
    @winrt_mixinmethod
    def get_KeyboardPresent(self: win32more.Windows.Devices.Input.IKeyboardCapabilities) -> Int32: ...
    KeyboardPresent = property(get_KeyboardPresent, None)
class MouseCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.IMouseCapabilities
    _classid_ = 'Windows.Devices.Input.MouseCapabilities'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Input.MouseCapabilities.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Input.MouseCapabilities: ...
    @winrt_mixinmethod
    def get_MousePresent(self: win32more.Windows.Devices.Input.IMouseCapabilities) -> Int32: ...
    @winrt_mixinmethod
    def get_VerticalWheelPresent(self: win32more.Windows.Devices.Input.IMouseCapabilities) -> Int32: ...
    @winrt_mixinmethod
    def get_HorizontalWheelPresent(self: win32more.Windows.Devices.Input.IMouseCapabilities) -> Int32: ...
    @winrt_mixinmethod
    def get_SwapButtons(self: win32more.Windows.Devices.Input.IMouseCapabilities) -> Int32: ...
    @winrt_mixinmethod
    def get_NumberOfButtons(self: win32more.Windows.Devices.Input.IMouseCapabilities) -> UInt32: ...
    HorizontalWheelPresent = property(get_HorizontalWheelPresent, None)
    MousePresent = property(get_MousePresent, None)
    NumberOfButtons = property(get_NumberOfButtons, None)
    SwapButtons = property(get_SwapButtons, None)
    VerticalWheelPresent = property(get_VerticalWheelPresent, None)
class MouseDelta(Structure):
    X: Int32
    Y: Int32
class MouseDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.IMouseDevice
    _classid_ = 'Windows.Devices.Input.MouseDevice'
    @winrt_mixinmethod
    def add_MouseMoved(self: win32more.Windows.Devices.Input.IMouseDevice, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.MouseDevice, win32more.Windows.Devices.Input.MouseEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MouseMoved(self: win32more.Windows.Devices.Input.IMouseDevice, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.Devices.Input.IMouseDeviceStatics) -> win32more.Windows.Devices.Input.MouseDevice: ...
    MouseMoved = event()
class MouseEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.IMouseEventArgs
    _classid_ = 'Windows.Devices.Input.MouseEventArgs'
    @winrt_mixinmethod
    def get_MouseDelta(self: win32more.Windows.Devices.Input.IMouseEventArgs) -> win32more.Windows.Devices.Input.MouseDelta: ...
    MouseDelta = property(get_MouseDelta, None)
class PenButtonListener(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.IPenButtonListener
    _classid_ = 'Windows.Devices.Input.PenButtonListener'
    @winrt_mixinmethod
    def IsSupported(self: win32more.Windows.Devices.Input.IPenButtonListener) -> Boolean: ...
    @winrt_mixinmethod
    def add_IsSupportedChanged(self: win32more.Windows.Devices.Input.IPenButtonListener, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.PenButtonListener, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsSupportedChanged(self: win32more.Windows.Devices.Input.IPenButtonListener, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TailButtonClicked(self: win32more.Windows.Devices.Input.IPenButtonListener, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.PenButtonListener, win32more.Windows.Devices.Input.PenTailButtonClickedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TailButtonClicked(self: win32more.Windows.Devices.Input.IPenButtonListener, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TailButtonDoubleClicked(self: win32more.Windows.Devices.Input.IPenButtonListener, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.PenButtonListener, win32more.Windows.Devices.Input.PenTailButtonDoubleClickedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TailButtonDoubleClicked(self: win32more.Windows.Devices.Input.IPenButtonListener, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TailButtonLongPressed(self: win32more.Windows.Devices.Input.IPenButtonListener, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.PenButtonListener, win32more.Windows.Devices.Input.PenTailButtonLongPressedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TailButtonLongPressed(self: win32more.Windows.Devices.Input.IPenButtonListener, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Devices.Input.IPenButtonListenerStatics) -> win32more.Windows.Devices.Input.PenButtonListener: ...
    IsSupportedChanged = event()
    TailButtonClicked = event()
    TailButtonDoubleClicked = event()
    TailButtonLongPressed = event()
class PenDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.IPenDevice
    _classid_ = 'Windows.Devices.Input.PenDevice'
    @winrt_mixinmethod
    def get_PenId(self: win32more.Windows.Devices.Input.IPenDevice) -> Guid: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: win32more.Windows.Devices.Input.IPenDevice2) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    @winrt_classmethod
    def GetFromPointerId(cls: win32more.Windows.Devices.Input.IPenDeviceStatics, pointerId: UInt32) -> win32more.Windows.Devices.Input.PenDevice: ...
    PenId = property(get_PenId, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class PenDockListener(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.IPenDockListener
    _classid_ = 'Windows.Devices.Input.PenDockListener'
    @winrt_mixinmethod
    def IsSupported(self: win32more.Windows.Devices.Input.IPenDockListener) -> Boolean: ...
    @winrt_mixinmethod
    def add_IsSupportedChanged(self: win32more.Windows.Devices.Input.IPenDockListener, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.PenDockListener, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsSupportedChanged(self: win32more.Windows.Devices.Input.IPenDockListener, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Docked(self: win32more.Windows.Devices.Input.IPenDockListener, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.PenDockListener, win32more.Windows.Devices.Input.PenDockedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Docked(self: win32more.Windows.Devices.Input.IPenDockListener, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Undocked(self: win32more.Windows.Devices.Input.IPenDockListener, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Input.PenDockListener, win32more.Windows.Devices.Input.PenUndockedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Undocked(self: win32more.Windows.Devices.Input.IPenDockListener, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Devices.Input.IPenDockListenerStatics) -> win32more.Windows.Devices.Input.PenDockListener: ...
    IsSupportedChanged = event()
    Docked = event()
    Undocked = event()
class PenDockedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.IPenDockedEventArgs
    _classid_ = 'Windows.Devices.Input.PenDockedEventArgs'
class PenTailButtonClickedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.IPenTailButtonClickedEventArgs
    _classid_ = 'Windows.Devices.Input.PenTailButtonClickedEventArgs'
class PenTailButtonDoubleClickedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.IPenTailButtonDoubleClickedEventArgs
    _classid_ = 'Windows.Devices.Input.PenTailButtonDoubleClickedEventArgs'
class PenTailButtonLongPressedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.IPenTailButtonLongPressedEventArgs
    _classid_ = 'Windows.Devices.Input.PenTailButtonLongPressedEventArgs'
class PenUndockedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.IPenUndockedEventArgs
    _classid_ = 'Windows.Devices.Input.PenUndockedEventArgs'
class PointerDevice(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.IPointerDevice
    _classid_ = 'Windows.Devices.Input.PointerDevice'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Windows.Devices.Input.IPointerDevice) -> win32more.Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_IsIntegrated(self: win32more.Windows.Devices.Input.IPointerDevice) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxContacts(self: win32more.Windows.Devices.Input.IPointerDevice) -> UInt32: ...
    @winrt_mixinmethod
    def get_PhysicalDeviceRect(self: win32more.Windows.Devices.Input.IPointerDevice) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_ScreenRect(self: win32more.Windows.Devices.Input.IPointerDevice) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_SupportedUsages(self: win32more.Windows.Devices.Input.IPointerDevice) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Input.PointerDeviceUsage]: ...
    @winrt_mixinmethod
    def get_MaxPointersWithZDistance(self: win32more.Windows.Devices.Input.IPointerDevice2) -> UInt32: ...
    @winrt_classmethod
    def GetPointerDevice(cls: win32more.Windows.Devices.Input.IPointerDeviceStatics, pointerId: UInt32) -> win32more.Windows.Devices.Input.PointerDevice: ...
    @winrt_classmethod
    def GetPointerDevices(cls: win32more.Windows.Devices.Input.IPointerDeviceStatics) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Input.PointerDevice]: ...
    IsIntegrated = property(get_IsIntegrated, None)
    MaxContacts = property(get_MaxContacts, None)
    MaxPointersWithZDistance = property(get_MaxPointersWithZDistance, None)
    PhysicalDeviceRect = property(get_PhysicalDeviceRect, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    ScreenRect = property(get_ScreenRect, None)
    SupportedUsages = property(get_SupportedUsages, None)
class PointerDeviceType(Enum, Int32):
    Touch = 0
    Pen = 1
    Mouse = 2
    Touchpad = 3
class PointerDeviceUsage(Structure):
    UsagePage: UInt32
    Usage: UInt32
    MinLogical: Int32
    MaxLogical: Int32
    MinPhysical: Int32
    MaxPhysical: Int32
    Unit: UInt32
    PhysicalMultiplier: Single
class TouchCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Input.ITouchCapabilities
    _classid_ = 'Windows.Devices.Input.TouchCapabilities'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Input.TouchCapabilities.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Input.TouchCapabilities: ...
    @winrt_mixinmethod
    def get_TouchPresent(self: win32more.Windows.Devices.Input.ITouchCapabilities) -> Int32: ...
    @winrt_mixinmethod
    def get_Contacts(self: win32more.Windows.Devices.Input.ITouchCapabilities) -> UInt32: ...
    Contacts = property(get_Contacts, None)
    TouchPresent = property(get_TouchPresent, None)


make_ready(__name__)
