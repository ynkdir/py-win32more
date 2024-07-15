from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.UI.Core.Preview
import win32more.Windows.UI.WindowManagement
import win32more.Windows.Win32.System.WinRT
class CoreAppWindowPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Core.Preview.ICoreAppWindowPreview
    _classid_ = 'Windows.UI.Core.Preview.CoreAppWindowPreview'
    @winrt_classmethod
    def GetIdFromWindow(cls: win32more.Windows.UI.Core.Preview.ICoreAppWindowPreviewStatics, window: win32more.Windows.UI.WindowManagement.AppWindow) -> Int32: ...
class ICoreAppWindowPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.Preview.ICoreAppWindowPreview'
    _iid_ = Guid('{a4f6e665-365e-5fde-87a5-9543c3a15aa8}')
class ICoreAppWindowPreviewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.Preview.ICoreAppWindowPreviewStatics'
    _iid_ = Guid('{33ac21be-423b-5db6-8a8e-4dc87353b75b}')
    @winrt_commethod(6)
    def GetIdFromWindow(self, window: win32more.Windows.UI.WindowManagement.AppWindow) -> Int32: ...
class ISystemNavigationCloseRequestedPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.Preview.ISystemNavigationCloseRequestedPreviewEventArgs'
    _iid_ = Guid('{83d00de1-cbe5-4f31-8414-361da046518f}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Handled = property(get_Handled, put_Handled)
class ISystemNavigationManagerPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.Preview.ISystemNavigationManagerPreview'
    _iid_ = Guid('{ec5f0488-6425-4777-a536-cb5634427f0d}')
    @winrt_commethod(6)
    def add_CloseRequested(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.UI.Core.Preview.SystemNavigationCloseRequestedPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CloseRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CloseRequested = event()
class ISystemNavigationManagerPreviewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.Preview.ISystemNavigationManagerPreviewStatics'
    _iid_ = Guid('{0e971360-df74-4bce-84cb-bd1181ac0a71}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.UI.Core.Preview.SystemNavigationManagerPreview: ...
class SystemNavigationCloseRequestedPreviewEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Core.Preview.ISystemNavigationCloseRequestedPreviewEventArgs
    _classid_ = 'Windows.UI.Core.Preview.SystemNavigationCloseRequestedPreviewEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.UI.Core.Preview.ISystemNavigationCloseRequestedPreviewEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.UI.Core.Preview.ISystemNavigationCloseRequestedPreviewEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.Core.Preview.ISystemNavigationCloseRequestedPreviewEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Handled = property(get_Handled, put_Handled)
class SystemNavigationManagerPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Core.Preview.ISystemNavigationManagerPreview
    _classid_ = 'Windows.UI.Core.Preview.SystemNavigationManagerPreview'
    @winrt_mixinmethod
    def add_CloseRequested(self: win32more.Windows.UI.Core.Preview.ISystemNavigationManagerPreview, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.UI.Core.Preview.SystemNavigationCloseRequestedPreviewEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CloseRequested(self: win32more.Windows.UI.Core.Preview.ISystemNavigationManagerPreview, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.UI.Core.Preview.ISystemNavigationManagerPreviewStatics) -> win32more.Windows.UI.Core.Preview.SystemNavigationManagerPreview: ...
    CloseRequested = event()


make_ready(__name__)
