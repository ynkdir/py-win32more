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
import win32more.Windows.Foundation
import win32more.Windows.UI.WindowManagement
import win32more.Windows.UI.WindowManagement.Preview
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


make_ready(__name__)
