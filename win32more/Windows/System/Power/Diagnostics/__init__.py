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
import win32more.Windows.System.Power.Diagnostics
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


make_ready(__name__)
