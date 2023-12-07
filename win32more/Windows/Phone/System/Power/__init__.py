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
import win32more.Windows.Foundation
import win32more.Windows.Phone.System.Power
class IPowerManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.Power.IPowerManagerStatics'
    _iid_ = Guid('{25de8fd0-1c5b-11e1-bddb-0800200c9a66}')
    @winrt_commethod(6)
    def get_PowerSavingMode(self) -> win32more.Windows.Phone.System.Power.PowerSavingMode: ...
    @winrt_commethod(7)
    def add_PowerSavingModeChanged(self, changeHandler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_PowerSavingModeChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PowerSavingMode = property(get_PowerSavingMode, None)
class IPowerManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.Power.IPowerManagerStatics2'
    _iid_ = Guid('{596236cf-1918-4551-a466-c51aae373bf8}')
    @winrt_commethod(6)
    def get_PowerSavingModeEnabled(self) -> Boolean: ...
    PowerSavingModeEnabled = property(get_PowerSavingModeEnabled, None)
class _PowerManager_Meta_(ComPtr.__class__):
    pass
class PowerManager(ComPtr, metaclass=_PowerManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.Power.PowerManager'
    @winrt_classmethod
    def get_PowerSavingMode(cls: win32more.Windows.Phone.System.Power.IPowerManagerStatics) -> win32more.Windows.Phone.System.Power.PowerSavingMode: ...
    @winrt_classmethod
    def add_PowerSavingModeChanged(cls: win32more.Windows.Phone.System.Power.IPowerManagerStatics, changeHandler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_PowerSavingModeChanged(cls: win32more.Windows.Phone.System.Power.IPowerManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_PowerSavingModeEnabled(cls: win32more.Windows.Phone.System.Power.IPowerManagerStatics2) -> Boolean: ...
    _PowerManager_Meta_.PowerSavingMode = property(get_PowerSavingMode.__wrapped__, None)
    _PowerManager_Meta_.PowerSavingModeEnabled = property(get_PowerSavingModeEnabled.__wrapped__, None)
PowerSavingMode = Int32
PowerSavingMode_Off: PowerSavingMode = 0
PowerSavingMode_On: PowerSavingMode = 1
make_ready(__name__)
