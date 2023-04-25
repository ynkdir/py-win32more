from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.System.WinRT
import Windows.UI.Input
import Windows.UI.Input.Preview
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
class IInputActivationListenerPreviewStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f0551ce5-0de6-5be0-a5-89-f7-37-20-1a-45-82')
    @winrt_commethod(6)
    def CreateForApplicationWindow(self, window: Windows.UI.WindowManagement.AppWindow) -> Windows.UI.Input.InputActivationListener: ...
class InputActivationListenerPreview(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Preview.InputActivationListenerPreview'
    @winrt_classmethod
    def CreateForApplicationWindow(cls: Windows.UI.Input.Preview.IInputActivationListenerPreviewStatics, window: Windows.UI.WindowManagement.AppWindow) -> Windows.UI.Input.InputActivationListener: ...
make_head(_module, 'IInputActivationListenerPreviewStatics')
make_head(_module, 'InputActivationListenerPreview')
