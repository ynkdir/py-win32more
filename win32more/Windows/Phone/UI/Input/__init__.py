from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Phone.UI.Input
import win32more.Windows.Win32.System.WinRT
class BackPressedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.UI.Input.IBackPressedEventArgs
    _classid_ = 'Windows.Phone.UI.Input.BackPressedEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.Phone.UI.Input.IBackPressedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.Phone.UI.Input.IBackPressedEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class CameraEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Phone.UI.Input.ICameraEventArgs
    _classid_ = 'Windows.Phone.UI.Input.CameraEventArgs'
class HardwareButtons(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.UI.Input.HardwareButtons'
    @winrt_classmethod
    def add_BackPressed(cls: win32more.Windows.Phone.UI.Input.IHardwareButtonsStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Phone.UI.Input.BackPressedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_BackPressed(cls: win32more.Windows.Phone.UI.Input.IHardwareButtonsStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_CameraHalfPressed(cls: win32more.Windows.Phone.UI.Input.IHardwareButtonsStatics2, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Phone.UI.Input.CameraEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_CameraHalfPressed(cls: win32more.Windows.Phone.UI.Input.IHardwareButtonsStatics2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_CameraPressed(cls: win32more.Windows.Phone.UI.Input.IHardwareButtonsStatics2, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Phone.UI.Input.CameraEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_CameraPressed(cls: win32more.Windows.Phone.UI.Input.IHardwareButtonsStatics2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_CameraReleased(cls: win32more.Windows.Phone.UI.Input.IHardwareButtonsStatics2, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Phone.UI.Input.CameraEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_CameraReleased(cls: win32more.Windows.Phone.UI.Input.IHardwareButtonsStatics2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class IBackPressedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.UI.Input.IBackPressedEventArgs'
    _iid_ = Guid('{f6f555ff-64ec-42a2-b93b-2fbc0c36a121}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class ICameraEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.UI.Input.ICameraEventArgs'
    _iid_ = Guid('{b4063bda-201f-473d-bc69-e9e4ac57c9d0}')
class IHardwareButtonsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.UI.Input.IHardwareButtonsStatics'
    _iid_ = Guid('{594b8780-da66-4fd8-a776-7506bd0cbfa7}')
    @winrt_commethod(6)
    def add_BackPressed(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Phone.UI.Input.BackPressedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_BackPressed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BackPressed = event()
class IHardwareButtonsStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.UI.Input.IHardwareButtonsStatics2'
    _iid_ = Guid('{39c6c274-993f-40dd-854c-831a8934b92e}')
    @winrt_commethod(6)
    def add_CameraHalfPressed(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Phone.UI.Input.CameraEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CameraHalfPressed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_CameraPressed(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Phone.UI.Input.CameraEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_CameraPressed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_CameraReleased(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Phone.UI.Input.CameraEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_CameraReleased(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CameraHalfPressed = event()
    CameraPressed = event()
    CameraReleased = event()


make_ready(__name__)
