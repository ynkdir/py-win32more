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
import Windows.UI.WindowManagement
import Windows.UI.WindowManagement.Preview
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4ef55b0d-561d-513c-a67c-2c02b69cef41}')
class IWindowManagementPreviewStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0f9725c6-c004-5a23-8fd2-8d092ce2704a}')
    @winrt_commethod(6)
    def SetPreferredMinSize(self, window: Windows.UI.WindowManagement.AppWindow, preferredFrameMinSize: Windows.Foundation.Size) -> Void: ...
class WindowManagementPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WindowManagement.Preview.IWindowManagementPreview
    _classid_ = 'Windows.UI.WindowManagement.Preview.WindowManagementPreview'
    @winrt_classmethod
    def SetPreferredMinSize(cls: Windows.UI.WindowManagement.Preview.IWindowManagementPreviewStatics, window: Windows.UI.WindowManagement.AppWindow, preferredFrameMinSize: Windows.Foundation.Size) -> Void: ...
make_head(_module, 'IWindowManagementPreview')
make_head(_module, 'IWindowManagementPreviewStatics')
make_head(_module, 'WindowManagementPreview')
