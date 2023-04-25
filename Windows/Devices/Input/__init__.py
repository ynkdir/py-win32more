from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
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
class IKeyboardCapabilities(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3a3f9b56-6798-4bbc-83-3e-0f-34-b1-7c-65-ff')
    @winrt_commethod(6)
    def get_KeyboardPresent(self) -> Int32: ...
    KeyboardPresent = property(get_KeyboardPresent, None)
class IMouseCapabilities(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('bca5e023-7dd9-4b6b-9a-92-55-d4-3c-b3-8f-73')
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
class IMouseDevice(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('88edf458-f2c8-49f4-be-1f-c2-56-b3-88-bc-11')
    @winrt_commethod(6)
    def add_MouseMoved(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.MouseDevice, Windows.Devices.Input.MouseEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_MouseMoved(self, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IMouseDeviceStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('484a9045-6d70-49db-8e-68-46-ff-bd-17-d3-8d')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.Devices.Input.MouseDevice: ...
class IMouseEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f625aa5d-2354-4cc7-92-30-96-94-1c-96-9f-de')
    @winrt_commethod(6)
    def get_MouseDelta(self) -> Windows.Devices.Input.MouseDelta: ...
    MouseDelta = property(get_MouseDelta, None)
class IPenButtonListener(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8245c376-1ee3-53f7-b1-f7-83-34-a1-6f-28-15')
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
class IPenButtonListenerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('19a8a584-862f-5f69-bf-ea-05-f6-58-4f-13-3f')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Devices.Input.PenButtonListener: ...
class IPenDevice(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('31856eba-a738-5a8c-b8-f6-f9-7e-f6-8d-18-ef')
    @winrt_commethod(6)
    def get_PenId(self) -> Guid: ...
    PenId = property(get_PenId, None)
class IPenDevice2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0207d327-7fb8-5566-8c-34-f8-34-20-37-b7-f9')
    @winrt_commethod(6)
    def get_SimpleHapticsController(self) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class IPenDeviceStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9dfbbe01-0966-5180-bc-b4-b8-50-60-e3-94-79')
    @winrt_commethod(6)
    def GetFromPointerId(self, pointerId: UInt32) -> Windows.Devices.Input.PenDevice: ...
class IPenDockListener(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('759f4d90-1dc0-55cb-ad-18-b9-10-14-56-f5-92')
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
class IPenDockListenerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cab75e9a-0016-5c72-96-9e-a9-7e-11-99-2a-93')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Devices.Input.PenDockListener: ...
class IPenDockedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fd4277c6-ca63-5d4e-9e-d3-a2-8a-54-52-1c-8c')
class IPenTailButtonClickedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5d2fb7b6-6ad3-5d3e-ab-29-05-ea-24-10-e3-90')
class IPenTailButtonDoubleClickedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('846321a2-618a-5478-b0-4c-b3-58-23-1d-a4-a7')
class IPenTailButtonLongPressedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f37c606e-c60a-5f42-b8-18-a5-31-12-40-6c-13')
class IPenUndockedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ccd09150-261b-59e6-a5-d4-c1-96-4c-d0-3f-eb')
class IPointerDevice(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('93c9bafc-ebcb-467e-82-c6-27-6f-ea-e3-6b-5a')
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
class IPointerDevice2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f8a6d2a0-c484-489f-ae-3e-30-d2-ee-1f-fd-3e')
    @winrt_commethod(6)
    def get_MaxPointersWithZDistance(self) -> UInt32: ...
    MaxPointersWithZDistance = property(get_MaxPointersWithZDistance, None)
class IPointerDeviceStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d8b89aa1-d1c6-416e-bd-8d-57-90-91-4d-c5-63')
    @winrt_commethod(6)
    def GetPointerDevice(self, pointerId: UInt32) -> Windows.Devices.Input.PointerDevice: ...
    @winrt_commethod(7)
    def GetPointerDevices(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Input.PointerDevice]: ...
class ITouchCapabilities(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('20dd55f9-13f1-46c8-92-85-2c-05-fa-3e-da-6f')
    @winrt_commethod(6)
    def get_TouchPresent(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Contacts(self) -> UInt32: ...
    TouchPresent = property(get_TouchPresent, None)
    Contacts = property(get_Contacts, None)
class KeyboardCapabilities(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.KeyboardCapabilities'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Input.KeyboardCapabilities: ...
    @winrt_mixinmethod
    def get_KeyboardPresent(self: Windows.Devices.Input.IKeyboardCapabilities) -> Int32: ...
    KeyboardPresent = property(get_KeyboardPresent, None)
class MouseCapabilities(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.MouseCapabilities'
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
class MouseDevice(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.MouseDevice'
    @winrt_mixinmethod
    def add_MouseMoved(self: Windows.Devices.Input.IMouseDevice, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Input.MouseDevice, Windows.Devices.Input.MouseEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MouseMoved(self: Windows.Devices.Input.IMouseDevice, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.Devices.Input.IMouseDeviceStatics) -> Windows.Devices.Input.MouseDevice: ...
class MouseEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.MouseEventArgs'
    @winrt_mixinmethod
    def get_MouseDelta(self: Windows.Devices.Input.IMouseEventArgs) -> Windows.Devices.Input.MouseDelta: ...
    MouseDelta = property(get_MouseDelta, None)
class PenButtonListener(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.PenButtonListener'
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
class PenDevice(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.PenDevice'
    @winrt_mixinmethod
    def get_PenId(self: Windows.Devices.Input.IPenDevice) -> Guid: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: Windows.Devices.Input.IPenDevice2) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    @winrt_classmethod
    def GetFromPointerId(cls: Windows.Devices.Input.IPenDeviceStatics, pointerId: UInt32) -> Windows.Devices.Input.PenDevice: ...
    PenId = property(get_PenId, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
class PenDockListener(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.PenDockListener'
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
class PenDockedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.PenDockedEventArgs'
class PenTailButtonClickedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.PenTailButtonClickedEventArgs'
class PenTailButtonDoubleClickedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.PenTailButtonDoubleClickedEventArgs'
class PenTailButtonLongPressedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.PenTailButtonLongPressedEventArgs'
class PenUndockedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.PenUndockedEventArgs'
class PointerDevice(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.PointerDevice'
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
class TouchCapabilities(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Input.TouchCapabilities'
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
