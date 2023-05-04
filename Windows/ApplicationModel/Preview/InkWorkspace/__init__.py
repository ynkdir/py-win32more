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
import Windows.ApplicationModel.Preview.InkWorkspace
import Windows.Foundation
import Windows.Graphics.Imaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IInkWorkspaceHostedAppManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{fe0a7990-5e59-4bb7-8a63-7d218cd96300}')
    @winrt_commethod(6)
    def SetThumbnailAsync(self, bitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Windows.Foundation.IAsyncAction: ...
class IInkWorkspaceHostedAppManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{cbfd8cc5-a162-4bc4-84ee-e8716d5233c5}')
    @winrt_commethod(6)
    def GetForCurrentApp(self) -> Windows.ApplicationModel.Preview.InkWorkspace.InkWorkspaceHostedAppManager: ...
class InkWorkspaceHostedAppManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.Preview.InkWorkspace.InkWorkspaceHostedAppManager'
    @winrt_mixinmethod
    def SetThumbnailAsync(self: Windows.ApplicationModel.Preview.InkWorkspace.IInkWorkspaceHostedAppManager, bitmap: Windows.Graphics.Imaging.SoftwareBitmap) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetForCurrentApp(cls: Windows.ApplicationModel.Preview.InkWorkspace.IInkWorkspaceHostedAppManagerStatics) -> Windows.ApplicationModel.Preview.InkWorkspace.InkWorkspaceHostedAppManager: ...
PreviewInkWorkspaceContract: UInt32 = 65536
make_head(_module, 'IInkWorkspaceHostedAppManager')
make_head(_module, 'IInkWorkspaceHostedAppManagerStatics')
make_head(_module, 'InkWorkspaceHostedAppManager')
