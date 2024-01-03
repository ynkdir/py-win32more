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
import win32more.Windows.UI.Input
import win32more.Windows.UI.Input.Preview
import win32more.Windows.UI.WindowManagement
class IInputActivationListenerPreviewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Preview.IInputActivationListenerPreviewStatics'
    _iid_ = Guid('{f0551ce5-0de6-5be0-a589-f737201a4582}')
    @winrt_commethod(6)
    def CreateForApplicationWindow(self, window: win32more.Windows.UI.WindowManagement.AppWindow) -> win32more.Windows.UI.Input.InputActivationListener: ...
class InputActivationListenerPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Preview.InputActivationListenerPreview'
    @winrt_classmethod
    def CreateForApplicationWindow(cls: win32more.Windows.UI.Input.Preview.IInputActivationListenerPreviewStatics, window: win32more.Windows.UI.WindowManagement.AppWindow) -> win32more.Windows.UI.Input.InputActivationListener: ...


make_ready(__name__)
