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
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Phone.System.Power
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPowerManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.Power.IPowerManagerStatics'
    _iid_ = Guid('{25de8fd0-1c5b-11e1-bddb-0800200c9a66}')
    @winrt_commethod(6)
    def get_PowerSavingMode(self) -> Windows.Phone.System.Power.PowerSavingMode: ...
    @winrt_commethod(7)
    def add_PowerSavingModeChanged(self, changeHandler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_PowerSavingModeChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    PowerSavingMode = property(get_PowerSavingMode, None)
class IPowerManagerStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.Power.IPowerManagerStatics2'
    _iid_ = Guid('{596236cf-1918-4551-a466-c51aae373bf8}')
    @winrt_commethod(6)
    def get_PowerSavingModeEnabled(self) -> Boolean: ...
    PowerSavingModeEnabled = property(get_PowerSavingModeEnabled, None)
class _PowerManager_Meta_(ComPtr.__class__):
    pass
class PowerManager(ComPtr, metaclass=_PowerManager_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.Power.PowerManager'
    @winrt_classmethod
    def get_PowerSavingMode(cls: Windows.Phone.System.Power.IPowerManagerStatics) -> Windows.Phone.System.Power.PowerSavingMode: ...
    @winrt_classmethod
    def add_PowerSavingModeChanged(cls: Windows.Phone.System.Power.IPowerManagerStatics, changeHandler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_PowerSavingModeChanged(cls: Windows.Phone.System.Power.IPowerManagerStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_PowerSavingModeEnabled(cls: Windows.Phone.System.Power.IPowerManagerStatics2) -> Boolean: ...
    _PowerManager_Meta_.PowerSavingMode = property(get_PowerSavingMode.__wrapped__, None)
    _PowerManager_Meta_.PowerSavingModeEnabled = property(get_PowerSavingModeEnabled.__wrapped__, None)
PowerSavingMode = Int32
PowerSavingMode_Off: PowerSavingMode = 0
PowerSavingMode_On: PowerSavingMode = 1
make_head(_module, 'IPowerManagerStatics')
make_head(_module, 'IPowerManagerStatics2')
make_head(_module, 'PowerManager')
