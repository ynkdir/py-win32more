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
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.Pwm.Provider
import win32more.Windows.Foundation.Collections
class IPwmControllerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Pwm.Provider.IPwmControllerProvider'
    _iid_ = Guid('{1300593b-e2e3-40a4-b7d9-48dff0377a52}')
    @winrt_commethod(6)
    def get_PinCount(self) -> Int32: ...
    @winrt_commethod(7)
    def get_ActualFrequency(self) -> Double: ...
    @winrt_commethod(8)
    def SetDesiredFrequency(self, frequency: Double) -> Double: ...
    @winrt_commethod(9)
    def get_MaxFrequency(self) -> Double: ...
    @winrt_commethod(10)
    def get_MinFrequency(self) -> Double: ...
    @winrt_commethod(11)
    def AcquirePin(self, pin: Int32) -> Void: ...
    @winrt_commethod(12)
    def ReleasePin(self, pin: Int32) -> Void: ...
    @winrt_commethod(13)
    def EnablePin(self, pin: Int32) -> Void: ...
    @winrt_commethod(14)
    def DisablePin(self, pin: Int32) -> Void: ...
    @winrt_commethod(15)
    def SetPulseParameters(self, pin: Int32, dutyCycle: Double, invertPolarity: Boolean) -> Void: ...
    PinCount = property(get_PinCount, None)
    ActualFrequency = property(get_ActualFrequency, None)
    MaxFrequency = property(get_MaxFrequency, None)
    MinFrequency = property(get_MinFrequency, None)
class IPwmProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Pwm.Provider.IPwmProvider'
    _iid_ = Guid('{a3301228-52f1-47b0-9349-66ba43d25902}')
    @winrt_commethod(6)
    def GetControllers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Pwm.Provider.IPwmControllerProvider]: ...
make_ready(__name__)
