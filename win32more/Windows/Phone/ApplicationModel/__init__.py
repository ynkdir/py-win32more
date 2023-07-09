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
import win32more.Windows.Phone.ApplicationModel
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class _ApplicationProfile_Meta_(ComPtr.__class__):
    pass
class ApplicationProfile(ComPtr, metaclass=_ApplicationProfile_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.ApplicationModel.ApplicationProfile'
    @winrt_classmethod
    def get_Modes(cls: win32more.Windows.Phone.ApplicationModel.IApplicationProfileStatics) -> win32more.Windows.Phone.ApplicationModel.ApplicationProfileModes: ...
    _ApplicationProfile_Meta_.Modes = property(get_Modes.__wrapped__, None)
ApplicationProfileModes = UInt32
ApplicationProfileModes_Default: ApplicationProfileModes = 0
ApplicationProfileModes_Alternate: ApplicationProfileModes = 1
class IApplicationProfileStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.ApplicationModel.IApplicationProfileStatics'
    _iid_ = Guid('{d5008ab4-7e7a-11e1-a7f2-b0a14824019b}')
    @winrt_commethod(6)
    def get_Modes(self) -> win32more.Windows.Phone.ApplicationModel.ApplicationProfileModes: ...
    Modes = property(get_Modes, None)
make_head(_module, 'ApplicationProfile')
make_head(_module, 'IApplicationProfileStatics')
