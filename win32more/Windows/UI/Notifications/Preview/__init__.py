from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.UI
import win32more.Windows.UI.Notifications.Preview
class IToastOcclusionManagerPreviewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.Preview.IToastOcclusionManagerPreviewStatics'
    _iid_ = Guid('{507e5c83-50f9-5412-8953-b65c18cfab12}')
    @winrt_commethod(6)
    def SetToastWindowMargin(self, appWindowId: win32more.Windows.UI.WindowId, margin: Double) -> Void: ...
class ToastOcclusionManagerPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Notifications.Preview.ToastOcclusionManagerPreview'
    @winrt_classmethod
    def SetToastWindowMargin(cls: win32more.Windows.UI.Notifications.Preview.IToastOcclusionManagerPreviewStatics, appWindowId: win32more.Windows.UI.WindowId, margin: Double) -> Void: ...
make_ready(__name__)
