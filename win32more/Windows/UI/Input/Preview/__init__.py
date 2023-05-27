from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.UI.Input
import win32more.Windows.UI.Input.Preview
import win32more.Windows.UI.WindowManagement
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
make_head(_module, 'IInputActivationListenerPreviewStatics')
make_head(_module, 'InputActivationListenerPreview')
