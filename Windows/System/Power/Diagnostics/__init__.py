from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.System.Power.Diagnostics
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class BackgroundEnergyDiagnostics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Power.Diagnostics.BackgroundEnergyDiagnostics'
    @winrt_classmethod
    def get_DeviceSpecificConversionFactor(cls: Windows.System.Power.Diagnostics.IBackgroundEnergyDiagnosticsStatics) -> Double: ...
    @winrt_classmethod
    def ComputeTotalEnergyUsage(cls: Windows.System.Power.Diagnostics.IBackgroundEnergyDiagnosticsStatics) -> UInt64: ...
    @winrt_classmethod
    def ResetTotalEnergyUsage(cls: Windows.System.Power.Diagnostics.IBackgroundEnergyDiagnosticsStatics) -> Void: ...
    DeviceSpecificConversionFactor = property(get_DeviceSpecificConversionFactor, None)
class ForegroundEnergyDiagnostics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.System.Power.Diagnostics.ForegroundEnergyDiagnostics'
    @winrt_classmethod
    def get_DeviceSpecificConversionFactor(cls: Windows.System.Power.Diagnostics.IForegroundEnergyDiagnosticsStatics) -> Double: ...
    @winrt_classmethod
    def ComputeTotalEnergyUsage(cls: Windows.System.Power.Diagnostics.IForegroundEnergyDiagnosticsStatics) -> UInt64: ...
    @winrt_classmethod
    def ResetTotalEnergyUsage(cls: Windows.System.Power.Diagnostics.IForegroundEnergyDiagnosticsStatics) -> Void: ...
    DeviceSpecificConversionFactor = property(get_DeviceSpecificConversionFactor, None)
class IBackgroundEnergyDiagnosticsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d7663702-d3a6-46e0-8f-9b-50-b9-5b-b4-f9-c5')
    @winrt_commethod(6)
    def get_DeviceSpecificConversionFactor(self) -> Double: ...
    @winrt_commethod(7)
    def ComputeTotalEnergyUsage(self) -> UInt64: ...
    @winrt_commethod(8)
    def ResetTotalEnergyUsage(self) -> Void: ...
    DeviceSpecificConversionFactor = property(get_DeviceSpecificConversionFactor, None)
class IForegroundEnergyDiagnosticsStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('23ca0917-cd07-4609-be-15-8f-e8-94-c5-e4-1e')
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
