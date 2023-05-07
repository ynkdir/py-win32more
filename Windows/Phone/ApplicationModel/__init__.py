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
import Windows.Phone.ApplicationModel
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.ApplicationModel.ApplicationProfile'
    @winrt_classmethod
    def get_Modes(cls: Windows.Phone.ApplicationModel.IApplicationProfileStatics) -> Windows.Phone.ApplicationModel.ApplicationProfileModes: ...
    _ApplicationProfile_Meta_.Modes = property(get_Modes.__wrapped__, None)
ApplicationProfileModes = UInt32
ApplicationProfileModes_Default: ApplicationProfileModes = 0
ApplicationProfileModes_Alternate: ApplicationProfileModes = 1
class IApplicationProfileStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.ApplicationModel.IApplicationProfileStatics'
    _iid_ = Guid('{d5008ab4-7e7a-11e1-a7f2-b0a14824019b}')
    @winrt_commethod(6)
    def get_Modes(self: Windows.Phone.ApplicationModel.IApplicationProfileStatics) -> Windows.Phone.ApplicationModel.ApplicationProfileModes: ...
    Modes = property(get_Modes, None)
make_head(_module, 'ApplicationProfile')
make_head(_module, 'IApplicationProfileStatics')
