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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.System.Power.Diagnostics
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class _BackgroundEnergyDiagnostics_Meta_(ComPtr.__class__):
    pass
class BackgroundEnergyDiagnostics(ComPtr, metaclass=_BackgroundEnergyDiagnostics_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Power.Diagnostics.BackgroundEnergyDiagnostics'
    @winrt_classmethod
    def get_DeviceSpecificConversionFactor(cls: win32more.Windows.System.Power.Diagnostics.IBackgroundEnergyDiagnosticsStatics) -> Double: ...
    @winrt_classmethod
    def ComputeTotalEnergyUsage(cls: win32more.Windows.System.Power.Diagnostics.IBackgroundEnergyDiagnosticsStatics) -> UInt64: ...
    @winrt_classmethod
    def ResetTotalEnergyUsage(cls: win32more.Windows.System.Power.Diagnostics.IBackgroundEnergyDiagnosticsStatics) -> Void: ...
    _BackgroundEnergyDiagnostics_Meta_.DeviceSpecificConversionFactor = property(get_DeviceSpecificConversionFactor.__wrapped__, None)
class _ForegroundEnergyDiagnostics_Meta_(ComPtr.__class__):
    pass
class ForegroundEnergyDiagnostics(ComPtr, metaclass=_ForegroundEnergyDiagnostics_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Power.Diagnostics.ForegroundEnergyDiagnostics'
    @winrt_classmethod
    def get_DeviceSpecificConversionFactor(cls: win32more.Windows.System.Power.Diagnostics.IForegroundEnergyDiagnosticsStatics) -> Double: ...
    @winrt_classmethod
    def ComputeTotalEnergyUsage(cls: win32more.Windows.System.Power.Diagnostics.IForegroundEnergyDiagnosticsStatics) -> UInt64: ...
    @winrt_classmethod
    def ResetTotalEnergyUsage(cls: win32more.Windows.System.Power.Diagnostics.IForegroundEnergyDiagnosticsStatics) -> Void: ...
    _ForegroundEnergyDiagnostics_Meta_.DeviceSpecificConversionFactor = property(get_DeviceSpecificConversionFactor.__wrapped__, None)
class IBackgroundEnergyDiagnosticsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Power.Diagnostics.IBackgroundEnergyDiagnosticsStatics'
    _iid_ = Guid('{d7663702-d3a6-46e0-8f9b-50b95bb4f9c5}')
    @winrt_commethod(6)
    def get_DeviceSpecificConversionFactor(self) -> Double: ...
    @winrt_commethod(7)
    def ComputeTotalEnergyUsage(self) -> UInt64: ...
    @winrt_commethod(8)
    def ResetTotalEnergyUsage(self) -> Void: ...
    DeviceSpecificConversionFactor = property(get_DeviceSpecificConversionFactor, None)
class IForegroundEnergyDiagnosticsStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Power.Diagnostics.IForegroundEnergyDiagnosticsStatics'
    _iid_ = Guid('{23ca0917-cd07-4609-be15-8fe894c5e41e}')
    @winrt_commethod(6)
    def get_DeviceSpecificConversionFactor(self) -> Double: ...
    @winrt_commethod(7)
    def ComputeTotalEnergyUsage(self) -> UInt64: ...
    @winrt_commethod(8)
    def ResetTotalEnergyUsage(self) -> Void: ...
    DeviceSpecificConversionFactor = property(get_DeviceSpecificConversionFactor, None)
make_head(_module, 'BackgroundEnergyDiagnostics')
make_head(_module, 'ForegroundEnergyDiagnostics')
make_head(_module, 'IBackgroundEnergyDiagnosticsStatics')
make_head(_module, 'IForegroundEnergyDiagnosticsStatics')
