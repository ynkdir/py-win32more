from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.UI.WindowManagement
import win32more.Windows.UI.WindowManagement.Preview
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IWindowManagementPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.Preview.IWindowManagementPreview'
    _iid_ = Guid('{4ef55b0d-561d-513c-a67c-2c02b69cef41}')
class IWindowManagementPreviewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WindowManagement.Preview.IWindowManagementPreviewStatics'
    _iid_ = Guid('{0f9725c6-c004-5a23-8fd2-8d092ce2704a}')
    @winrt_commethod(6)
    def SetPreferredMinSize(self, window: win32more.Windows.UI.WindowManagement.AppWindow, preferredFrameMinSize: win32more.Windows.Foundation.Size) -> Void: ...
class WindowManagementPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WindowManagement.Preview.IWindowManagementPreview
    _classid_ = 'Windows.UI.WindowManagement.Preview.WindowManagementPreview'
    @winrt_classmethod
    def SetPreferredMinSize(cls: win32more.Windows.UI.WindowManagement.Preview.IWindowManagementPreviewStatics, window: win32more.Windows.UI.WindowManagement.AppWindow, preferredFrameMinSize: win32more.Windows.Foundation.Size) -> Void: ...
make_head(_module, 'IWindowManagementPreview')
make_head(_module, 'IWindowManagementPreviewStatics')
make_head(_module, 'WindowManagementPreview')
