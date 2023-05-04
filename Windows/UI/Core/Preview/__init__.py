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
import Windows.Foundation
import Windows.UI.Core.Preview
import Windows.UI.WindowManagement
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class CoreAppWindowPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.Preview.ICoreAppWindowPreview
    _classid_ = 'Windows.UI.Core.Preview.CoreAppWindowPreview'
    @winrt_classmethod
    def GetIdFromWindow(cls: Windows.UI.Core.Preview.ICoreAppWindowPreviewStatics, window: Windows.UI.WindowManagement.AppWindow) -> Int32: ...
class ICoreAppWindowPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.Preview.ICoreAppWindowPreview'
    _iid_ = Guid('{a4f6e665-365e-5fde-87a5-9543c3a15aa8}')
class ICoreAppWindowPreviewStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.Preview.ICoreAppWindowPreviewStatics'
    _iid_ = Guid('{33ac21be-423b-5db6-8a8e-4dc87353b75b}')
    @winrt_commethod(6)
    def GetIdFromWindow(self, window: Windows.UI.WindowManagement.AppWindow) -> Int32: ...
class ISystemNavigationCloseRequestedPreviewEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.Preview.ISystemNavigationCloseRequestedPreviewEventArgs'
    _iid_ = Guid('{83d00de1-cbe5-4f31-8414-361da046518f}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    Handled = property(get_Handled, put_Handled)
class ISystemNavigationManagerPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.Preview.ISystemNavigationManagerPreview'
    _iid_ = Guid('{ec5f0488-6425-4777-a536-cb5634427f0d}')
    @winrt_commethod(6)
    def add_CloseRequested(self, handler: Windows.Foundation.EventHandler[Windows.UI.Core.Preview.SystemNavigationCloseRequestedPreviewEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_CloseRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ISystemNavigationManagerPreviewStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Core.Preview.ISystemNavigationManagerPreviewStatics'
    _iid_ = Guid('{0e971360-df74-4bce-84cb-bd1181ac0a71}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.Core.Preview.SystemNavigationManagerPreview: ...
class SystemNavigationCloseRequestedPreviewEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.Preview.ISystemNavigationCloseRequestedPreviewEventArgs
    _classid_ = 'Windows.UI.Core.Preview.SystemNavigationCloseRequestedPreviewEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: Windows.UI.Core.Preview.ISystemNavigationCloseRequestedPreviewEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.UI.Core.Preview.ISystemNavigationCloseRequestedPreviewEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.UI.Core.Preview.ISystemNavigationCloseRequestedPreviewEventArgs) -> Windows.Foundation.Deferral: ...
    Handled = property(get_Handled, put_Handled)
class SystemNavigationManagerPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Core.Preview.ISystemNavigationManagerPreview
    _classid_ = 'Windows.UI.Core.Preview.SystemNavigationManagerPreview'
    @winrt_mixinmethod
    def add_CloseRequested(self: Windows.UI.Core.Preview.ISystemNavigationManagerPreview, handler: Windows.Foundation.EventHandler[Windows.UI.Core.Preview.SystemNavigationCloseRequestedPreviewEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CloseRequested(self: Windows.UI.Core.Preview.ISystemNavigationManagerPreview, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.Core.Preview.ISystemNavigationManagerPreviewStatics) -> Windows.UI.Core.Preview.SystemNavigationManagerPreview: ...
make_head(_module, 'CoreAppWindowPreview')
make_head(_module, 'ICoreAppWindowPreview')
make_head(_module, 'ICoreAppWindowPreviewStatics')
make_head(_module, 'ISystemNavigationCloseRequestedPreviewEventArgs')
make_head(_module, 'ISystemNavigationManagerPreview')
make_head(_module, 'ISystemNavigationManagerPreviewStatics')
make_head(_module, 'SystemNavigationCloseRequestedPreviewEventArgs')
make_head(_module, 'SystemNavigationManagerPreview')
