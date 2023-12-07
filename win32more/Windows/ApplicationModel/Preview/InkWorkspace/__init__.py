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
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.Preview.InkWorkspace
import win32more.Windows.Foundation
import win32more.Windows.Graphics.Imaging
class IInkWorkspaceHostedAppManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.InkWorkspace.IInkWorkspaceHostedAppManager'
    _iid_ = Guid('{fe0a7990-5e59-4bb7-8a63-7d218cd96300}')
    @winrt_commethod(6)
    def SetThumbnailAsync(self, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Foundation.IAsyncAction: ...
class IInkWorkspaceHostedAppManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.InkWorkspace.IInkWorkspaceHostedAppManagerStatics'
    _iid_ = Guid('{cbfd8cc5-a162-4bc4-84ee-e8716d5233c5}')
    @winrt_commethod(6)
    def GetForCurrentApp(self) -> win32more.Windows.ApplicationModel.Preview.InkWorkspace.InkWorkspaceHostedAppManager: ...
class InkWorkspaceHostedAppManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Preview.InkWorkspace.IInkWorkspaceHostedAppManager
    _classid_ = 'Windows.ApplicationModel.Preview.InkWorkspace.InkWorkspaceHostedAppManager'
    @winrt_mixinmethod
    def SetThumbnailAsync(self: win32more.Windows.ApplicationModel.Preview.InkWorkspace.IInkWorkspaceHostedAppManager, bitmap: win32more.Windows.Graphics.Imaging.SoftwareBitmap) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetForCurrentApp(cls: win32more.Windows.ApplicationModel.Preview.InkWorkspace.IInkWorkspaceHostedAppManagerStatics) -> win32more.Windows.ApplicationModel.Preview.InkWorkspace.InkWorkspaceHostedAppManager: ...
PreviewInkWorkspaceContract: UInt32 = 65536
make_ready(__name__)
