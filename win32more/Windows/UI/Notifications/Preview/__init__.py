from __future__ import annotations
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
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
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
