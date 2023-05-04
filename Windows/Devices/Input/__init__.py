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
import Windows.Devices.Haptics
import Windows.Devices.Input
import Windows.Foundation
import Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IKeyboardCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IKeyboardCapabilities'
    _iid_ = Guid('{3a3f9b56-6798-4bbc-833e-0f34b17c65ff}')
    @winrt_commethod(6)
    def get_KeyboardPresent(self) -> Int32: ...
    KeyboardPresent = property(get_KeyboardPresent, None)
class IMouseCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    MousePresent = property(get_MousePresent, None)
    VerticalWheelPresent = property(get_VerticalWheelPresent, None)
    HorizontalWheelPresent = property(get_HorizontalWheelPresent, None)
    SwapButtons = property(get_SwapButtons, None)
    NumberOfButtons = property(get_NumberOfButtons, None)
class IMouseDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IMouseDevice'
    _iid_ = Guid('{88edf458-f2c8-49f4-be1f-c256b388bc11}')
    @winrt_commethod(6)
    def add_MouseMoved(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.MouseDevice, Windows.Devices.Input.MouseEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_MouseMoved(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IMouseDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IMouseDeviceStatics'
    _iid_ = Guid('{484a9045-6d70-49db-8e68-46ffbd17d38d}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.Devices.Input.MouseDevice: ...
class IMouseEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IMouseEventArgs'
    _iid_ = Guid('{f625aa5d-2354-4cc7-9230-96941c969fde}')
    @winrt_commethod(6)
    def get_MouseDelta(self) -> Windows.Devices.Input.MouseDelta: ...
    MouseDelta = property(get_MouseDelta, None)
class IPenButtonListener(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenButtonListener'
    _iid_ = Guid('{8245c376-1ee3-53f7-b1f7-8334a16f2815}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_IsSupportedChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.PenButtonListener, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_IsSupportedChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_TailButtonClicked(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.PenButtonListener, Windows.Devices.Input.PenTailButtonClickedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_TailButtonClicked(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_TailButtonDoubleClicked(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.PenButtonListener, Windows.Devices.Input.PenTailButtonDoubleClickedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_TailButtonDoubleClicked(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_TailButtonLongPressed(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.PenButtonListener, Windows.Devices.Input.PenTailButtonLongPressedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_TailButtonLongPressed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IPenButtonListenerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenButtonListenerStatics'
    _iid_ = Guid('{19a8a584-862f-5f69-bfea-05f6584f133f}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Devices.Input.PenButtonListener: ...
class IPenDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenDevice'
    _iid_ = Guid('{31856eba-a738-5a8c-b8f6-f97ef68d18ef}')
    @winrt_commethod(6)
    def get_PenId(self) -> Guid: ...
    PenId = property(get_PenId, None)
class IPenDevice2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenDevice2'
    _iid_ = Guid('{0207d327-7fb8-5566-8c34-f8342037b7f9}')
    @winrt_commethod(6)
    def get_SimpleHapticsController(self) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IPenDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenDeviceStatics'
    _iid_ = Guid('{9dfbbe01-0966-5180-bcb4-b85060e39479}')
    @winrt_commethod(6)
    def GetFromPointerId(self, pointerId: UInt32) -> Windows.Devices.Input.PenDevice: ...
class IPenDockListener(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenDockListener'
    _iid_ = Guid('{759f4d90-1dc0-55cb-ad18-b9101456f592}')
    @winrt_commethod(6)
    def IsSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_IsSupportedChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.PenDockListener, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_IsSupportedChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_Docked(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.PenDockListener, Windows.Devices.Input.PenDockedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Docked(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_Undocked(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.PenDockListener, Windows.Devices.Input.PenUndockedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_Undocked(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IPenDockListenerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenDockListenerStatics'
    _iid_ = Guid('{cab75e9a-0016-5c72-969e-a97e11992a93}')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Devices.Input.PenDockListener: ...
class IPenDockedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenDockedEventArgs'
    _iid_ = Guid('{fd4277c6-ca63-5d4e-9ed3-a28a54521c8c}')
class IPenTailButtonClickedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenTailButtonClickedEventArgs'
    _iid_ = Guid('{5d2fb7b6-6ad3-5d3e-ab29-05ea2410e390}')
class IPenTailButtonDoubleClickedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenTailButtonDoubleClickedEventArgs'
    _iid_ = Guid('{846321a2-618a-5478-b04c-b358231da4a7}')
class IPenTailButtonLongPressedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenTailButtonLongPressedEventArgs'
    _iid_ = Guid('{f37c606e-c60a-5f42-b818-a53112406c13}')
class IPenUndockedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPenUndockedEventArgs'
    _iid_ = Guid('{ccd09150-261b-59e6-a5d4-c1964cd03feb}')
class IPointerDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPointerDevice'
    _iid_ = Guid('{93c9bafc-ebcb-467e-82c6-276feae36b5a}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_IsIntegrated(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_MaxContacts(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_PhysicalDeviceRect(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(10)
    def get_ScreenRect(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(11)
    def get_SupportedUsages(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Input.PointerDeviceUsage]: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    IsIntegrated = property(get_IsIntegrated, None)
    MaxContacts = property(get_MaxContacts, None)
    PhysicalDeviceRect = property(get_PhysicalDeviceRect, None)
    ScreenRect = property(get_ScreenRect, None)
    SupportedUsages = property(get_SupportedUsages, None)
class IPointerDevice2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPointerDevice2'
    _iid_ = Guid('{f8a6d2a0-c484-489f-ae3e-30d2ee1ffd3e}')
    @winrt_commethod(6)
    def get_MaxPointersWithZDistance(self) -> UInt32: ...
    MaxPointersWithZDistance = property(get_MaxPointersWithZDistance, None)
class IPointerDeviceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.IPointerDeviceStatics'
    _iid_ = Guid('{d8b89aa1-d1c6-416e-bd8d-5790914dc563}')
    @winrt_commethod(6)
    def GetPointerDevice(self, pointerId: UInt32) -> Windows.Devices.Input.PointerDevice: ...
    @winrt_commethod(7)
    def GetPointerDevices(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Input.PointerDevice]: ...
class ITouchCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Input.ITouchCapabilities'
    _iid_ = Guid('{20dd55f9-13f1-46c8-9285-2c05fa3eda6f}')
    @winrt_commethod(6)
    def get_TouchPresent(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Contacts(self) -> UInt32: ...
    TouchPresent = property(get_TouchPresent, None)
    Contacts = property(get_Contacts, None)
class KeyboardCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Input.IKeyboardCapabilities
    _classid_ = 'Windows.Devices.Input.KeyboardCapabilities'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Input.KeyboardCapabilities: ...
    @winrt_mixinmethod
    def get_KeyboardPresent(self: Windows.Devices.Input.IKeyboardCapabilities) -> Int32: ...
    KeyboardPresent = property(get_KeyboardPresent, None)
class MouseCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Input.IMouseCapabilities
    _classid_ = 'Windows.Devices.Input.MouseCapabilities'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Input.MouseCapabilities: ...
    @winrt_mixinmethod
    def get_MousePresent(self: Windows.Devices.Input.IMouseCapabilities) -> Int32: ...
    @winrt_mixinmethod
    def get_VerticalWheelPresent(self: Windows.Devices.Input.IMouseCapabilities) -> Int32: ...
    @winrt_mixinmethod
    def get_HorizontalWheelPresent(self: Windows.Devices.Input.IMouseCapabilities) -> Int32: ...
    @winrt_mixinmethod
    def get_SwapButtons(self: Windows.Devices.Input.IMouseCapabilities) -> Int32: ...
    @winrt_mixinmethod
    def get_NumberOfButtons(self: Windows.Devices.Input.IMouseCapabilities) -> UInt32: ...
    MousePresent = property(get_MousePresent, None)
    VerticalWheelPresent = property(get_VerticalWheelPresent, None)
    HorizontalWheelPresent = property(get_HorizontalWheelPresent, None)
    SwapButtons = property(get_SwapButtons, None)
    NumberOfButtons = property(get_NumberOfButtons, None)
class MouseDelta(EasyCastStructure):
    X: Int32
    Y: Int32
class MouseDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Input.IMouseDevice
    _classid_ = 'Windows.Devices.Input.MouseDevice'
    @winrt_mixinmethod
    def add_MouseMoved(self: Windows.Devices.Input.IMouseDevice, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.MouseDevice, Windows.Devices.Input.MouseEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MouseMoved(self: Windows.Devices.Input.IMouseDevice, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.Devices.Input.IMouseDeviceStatics) -> Windows.Devices.Input.MouseDevice: ...
class MouseEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Input.IMouseEventArgs
    _classid_ = 'Windows.Devices.Input.MouseEventArgs'
    @winrt_mixinmethod
    def get_MouseDelta(self: Windows.Devices.Input.IMouseEventArgs) -> Windows.Devices.Input.MouseDelta: ...
    MouseDelta = property(get_MouseDelta, None)
class PenButtonListener(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Input.IPenButtonListener
    _classid_ = 'Windows.Devices.Input.PenButtonListener'
    @winrt_mixinmethod
    def IsSupported(self: Windows.Devices.Input.IPenButtonListener) -> Boolean: ...
    @winrt_mixinmethod
    def add_IsSupportedChanged(self: Windows.Devices.Input.IPenButtonListener, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.PenButtonListener, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsSupportedChanged(self: Windows.Devices.Input.IPenButtonListener, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TailButtonClicked(self: Windows.Devices.Input.IPenButtonListener, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.PenButtonListener, Windows.Devices.Input.PenTailButtonClickedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TailButtonClicked(self: Windows.Devices.Input.IPenButtonListener, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TailButtonDoubleClicked(self: Windows.Devices.Input.IPenButtonListener, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.PenButtonListener, Windows.Devices.Input.PenTailButtonDoubleClickedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TailButtonDoubleClicked(self: Windows.Devices.Input.IPenButtonListener, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_TailButtonLongPressed(self: Windows.Devices.Input.IPenButtonListener, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.PenButtonListener, Windows.Devices.Input.PenTailButtonLongPressedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_TailButtonLongPressed(self: Windows.Devices.Input.IPenButtonListener, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Devices.Input.IPenButtonListenerStatics) -> Windows.Devices.Input.PenButtonListener: ...
class PenDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Input.IPenDevice
    _classid_ = 'Windows.Devices.Input.PenDevice'
    @winrt_mixinmethod
    def get_PenId(self: Windows.Devices.Input.IPenDevice) -> Guid: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: Windows.Devices.Input.IPenDevice2) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    @winrt_classmethod
    def GetFromPointerId(cls: Windows.Devices.Input.IPenDeviceStatics, pointerId: UInt32) -> Windows.Devices.Input.PenDevice: ...
    PenId = property(get_PenId, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class PenDockListener(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Input.IPenDockListener
    _classid_ = 'Windows.Devices.Input.PenDockListener'
    @winrt_mixinmethod
    def IsSupported(self: Windows.Devices.Input.IPenDockListener) -> Boolean: ...
    @winrt_mixinmethod
    def add_IsSupportedChanged(self: Windows.Devices.Input.IPenDockListener, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.PenDockListener, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsSupportedChanged(self: Windows.Devices.Input.IPenDockListener, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Docked(self: Windows.Devices.Input.IPenDockListener, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.PenDockListener, Windows.Devices.Input.PenDockedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Docked(self: Windows.Devices.Input.IPenDockListener, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Undocked(self: Windows.Devices.Input.IPenDockListener, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.PenDockListener, Windows.Devices.Input.PenUndockedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Undocked(self: Windows.Devices.Input.IPenDockListener, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Devices.Input.IPenDockListenerStatics) -> Windows.Devices.Input.PenDockListener: ...
class PenDockedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Input.IPenDockedEventArgs
    _classid_ = 'Windows.Devices.Input.PenDockedEventArgs'
class PenTailButtonClickedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Input.IPenTailButtonClickedEventArgs
    _classid_ = 'Windows.Devices.Input.PenTailButtonClickedEventArgs'
class PenTailButtonDoubleClickedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Input.IPenTailButtonDoubleClickedEventArgs
    _classid_ = 'Windows.Devices.Input.PenTailButtonDoubleClickedEventArgs'
class PenTailButtonLongPressedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Input.IPenTailButtonLongPressedEventArgs
    _classid_ = 'Windows.Devices.Input.PenTailButtonLongPressedEventArgs'
class PenUndockedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Input.IPenUndockedEventArgs
    _classid_ = 'Windows.Devices.Input.PenUndockedEventArgs'
class PointerDevice(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Input.IPointerDevice
    _classid_ = 'Windows.Devices.Input.PointerDevice'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: Windows.Devices.Input.IPointerDevice) -> Windows.Devices.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_IsIntegrated(self: Windows.Devices.Input.IPointerDevice) -> Boolean: ...
    @winrt_mixinmethod
    def get_MaxContacts(self: Windows.Devices.Input.IPointerDevice) -> UInt32: ...
    @winrt_mixinmethod
    def get_PhysicalDeviceRect(self: Windows.Devices.Input.IPointerDevice) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_ScreenRect(self: Windows.Devices.Input.IPointerDevice) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_SupportedUsages(self: Windows.Devices.Input.IPointerDevice) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Input.PointerDeviceUsage]: ...
    @winrt_mixinmethod
    def get_MaxPointersWithZDistance(self: Windows.Devices.Input.IPointerDevice2) -> UInt32: ...
    @winrt_classmethod
    def GetPointerDevice(cls: Windows.Devices.Input.IPointerDeviceStatics, pointerId: UInt32) -> Windows.Devices.Input.PointerDevice: ...
    @winrt_classmethod
    def GetPointerDevices(cls: Windows.Devices.Input.IPointerDeviceStatics) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Input.PointerDevice]: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    IsIntegrated = property(get_IsIntegrated, None)
    MaxContacts = property(get_MaxContacts, None)
    PhysicalDeviceRect = property(get_PhysicalDeviceRect, None)
    ScreenRect = property(get_ScreenRect, None)
    SupportedUsages = property(get_SupportedUsages, None)
    MaxPointersWithZDistance = property(get_MaxPointersWithZDistance, None)
PointerDeviceType = Int32
PointerDeviceType_Touch: PointerDeviceType = 0
PointerDeviceType_Pen: PointerDeviceType = 1
PointerDeviceType_Mouse: PointerDeviceType = 2
class PointerDeviceUsage(EasyCastStructure):
    UsagePage: UInt32
    Usage: UInt32
    MinLogical: Int32
    MaxLogical: Int32
    MinPhysical: Int32
    MaxPhysical: Int32
    Unit: UInt32
    PhysicalMultiplier: Single
class TouchCapabilities(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Input.ITouchCapabilities
    _classid_ = 'Windows.Devices.Input.TouchCapabilities'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Input.TouchCapabilities: ...
    @winrt_mixinmethod
    def get_TouchPresent(self: Windows.Devices.Input.ITouchCapabilities) -> Int32: ...
    @winrt_mixinmethod
    def get_Contacts(self: Windows.Devices.Input.ITouchCapabilities) -> UInt32: ...
    TouchPresent = property(get_TouchPresent, None)
    Contacts = property(get_Contacts, None)
make_head(_module, 'IKeyboardCapabilities')
make_head(_module, 'IMouseCapabilities')
make_head(_module, 'IMouseDevice')
make_head(_module, 'IMouseDeviceStatics')
make_head(_module, 'IMouseEventArgs')
make_head(_module, 'IPenButtonListener')
make_head(_module, 'IPenButtonListenerStatics')
make_head(_module, 'IPenDevice')
make_head(_module, 'IPenDevice2')
make_head(_module, 'IPenDeviceStatics')
make_head(_module, 'IPenDockListener')
make_head(_module, 'IPenDockListenerStatics')
make_head(_module, 'IPenDockedEventArgs')
make_head(_module, 'IPenTailButtonClickedEventArgs')
make_head(_module, 'IPenTailButtonDoubleClickedEventArgs')
make_head(_module, 'IPenTailButtonLongPressedEventArgs')
make_head(_module, 'IPenUndockedEventArgs')
make_head(_module, 'IPointerDevice')
make_head(_module, 'IPointerDevice2')
make_head(_module, 'IPointerDeviceStatics')
make_head(_module, 'ITouchCapabilities')
make_head(_module, 'KeyboardCapabilities')
make_head(_module, 'MouseCapabilities')
make_head(_module, 'MouseDelta')
make_head(_module, 'MouseDevice')
make_head(_module, 'MouseEventArgs')
make_head(_module, 'PenButtonListener')
make_head(_module, 'PenDevice')
make_head(_module, 'PenDockListener')
make_head(_module, 'PenDockedEventArgs')
make_head(_module, 'PenTailButtonClickedEventArgs')
make_head(_module, 'PenTailButtonDoubleClickedEventArgs')
make_head(_module, 'PenTailButtonLongPressedEventArgs')
make_head(_module, 'PenUndockedEventArgs')
make_head(_module, 'PointerDevice')
make_head(_module, 'PointerDeviceUsage')
make_head(_module, 'TouchCapabilities')
