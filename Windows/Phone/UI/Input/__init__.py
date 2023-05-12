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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Phone.UI.Input
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class BackPressedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Phone.UI.Input.IBackPressedEventArgs
    _classid_ = 'Windows.Phone.UI.Input.BackPressedEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: Windows.Phone.UI.Input.IBackPressedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.Phone.UI.Input.IBackPressedEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class CameraEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Phone.UI.Input.ICameraEventArgs
    _classid_ = 'Windows.Phone.UI.Input.CameraEventArgs'
class HardwareButtons(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.UI.Input.HardwareButtons'
    @winrt_classmethod
    def add_BackPressed(cls: Windows.Phone.UI.Input.IHardwareButtonsStatics, handler: Windows.Foundation.EventHandler[Windows.Phone.UI.Input.BackPressedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_BackPressed(cls: Windows.Phone.UI.Input.IHardwareButtonsStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_CameraHalfPressed(cls: Windows.Phone.UI.Input.IHardwareButtonsStatics2, handler: Windows.Foundation.EventHandler[Windows.Phone.UI.Input.CameraEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_CameraHalfPressed(cls: Windows.Phone.UI.Input.IHardwareButtonsStatics2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_CameraPressed(cls: Windows.Phone.UI.Input.IHardwareButtonsStatics2, handler: Windows.Foundation.EventHandler[Windows.Phone.UI.Input.CameraEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_CameraPressed(cls: Windows.Phone.UI.Input.IHardwareButtonsStatics2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_CameraReleased(cls: Windows.Phone.UI.Input.IHardwareButtonsStatics2, handler: Windows.Foundation.EventHandler[Windows.Phone.UI.Input.CameraEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_CameraReleased(cls: Windows.Phone.UI.Input.IHardwareButtonsStatics2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IBackPressedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.UI.Input.IBackPressedEventArgs'
    _iid_ = Guid('{f6f555ff-64ec-42a2-b93b-2fbc0c36a121}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class ICameraEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.UI.Input.ICameraEventArgs'
    _iid_ = Guid('{b4063bda-201f-473d-bc69-e9e4ac57c9d0}')
class IHardwareButtonsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.UI.Input.IHardwareButtonsStatics'
    _iid_ = Guid('{594b8780-da66-4fd8-a776-7506bd0cbfa7}')
    @winrt_commethod(6)
    def add_BackPressed(self, handler: Windows.Foundation.EventHandler[Windows.Phone.UI.Input.BackPressedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_BackPressed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IHardwareButtonsStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.UI.Input.IHardwareButtonsStatics2'
    _iid_ = Guid('{39c6c274-993f-40dd-854c-831a8934b92e}')
    @winrt_commethod(6)
    def add_CameraHalfPressed(self, handler: Windows.Foundation.EventHandler[Windows.Phone.UI.Input.CameraEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CameraHalfPressed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_CameraPressed(self, handler: Windows.Foundation.EventHandler[Windows.Phone.UI.Input.CameraEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_CameraPressed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_CameraReleased(self, handler: Windows.Foundation.EventHandler[Windows.Phone.UI.Input.CameraEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_CameraReleased(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
make_head(_module, 'BackPressedEventArgs')
make_head(_module, 'CameraEventArgs')
make_head(_module, 'HardwareButtons')
make_head(_module, 'IBackPressedEventArgs')
make_head(_module, 'ICameraEventArgs')
make_head(_module, 'IHardwareButtonsStatics')
make_head(_module, 'IHardwareButtonsStatics2')
