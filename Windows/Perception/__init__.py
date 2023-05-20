from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.Perception
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IPerceptionTimestamp(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.IPerceptionTimestamp'
    _iid_ = Guid('{87c24804-a22e-4adb-ba26-d78ef639bcf4}')
    @winrt_commethod(6)
    def get_TargetTime(self) -> Windows.Foundation.DateTime: ...
    @winrt_commethod(7)
    def get_PredictionAmount(self) -> Windows.Foundation.TimeSpan: ...
    TargetTime = property(get_TargetTime, None)
    PredictionAmount = property(get_PredictionAmount, None)
class IPerceptionTimestamp2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.IPerceptionTimestamp2'
    _iid_ = Guid('{e354b7ed-2bd1-41b7-9ed0-74a15c354537}')
    @winrt_commethod(6)
    def get_SystemRelativeTargetTime(self) -> Windows.Foundation.TimeSpan: ...
    SystemRelativeTargetTime = property(get_SystemRelativeTargetTime, None)
class IPerceptionTimestampHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.IPerceptionTimestampHelperStatics'
    _iid_ = Guid('{47a611d4-a9df-4edc-855d-f4d339d967ac}')
    @winrt_commethod(6)
    def FromHistoricalTargetTime(self, targetTime: Windows.Foundation.DateTime) -> Windows.Perception.PerceptionTimestamp: ...
class IPerceptionTimestampHelperStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.IPerceptionTimestampHelperStatics2'
    _iid_ = Guid('{73d1a7fe-3fb9-4571-87d4-3c920a5e86eb}')
    @winrt_commethod(6)
    def FromSystemRelativeTargetTime(self, targetTime: Windows.Foundation.TimeSpan) -> Windows.Perception.PerceptionTimestamp: ...
class PerceptionTimestamp(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Perception.IPerceptionTimestamp
    _classid_ = 'Windows.Perception.PerceptionTimestamp'
    @winrt_mixinmethod
    def get_TargetTime(self: Windows.Perception.IPerceptionTimestamp) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_PredictionAmount(self: Windows.Perception.IPerceptionTimestamp) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_SystemRelativeTargetTime(self: Windows.Perception.IPerceptionTimestamp2) -> Windows.Foundation.TimeSpan: ...
    TargetTime = property(get_TargetTime, None)
    PredictionAmount = property(get_PredictionAmount, None)
    SystemRelativeTargetTime = property(get_SystemRelativeTargetTime, None)
class PerceptionTimestampHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Perception.PerceptionTimestampHelper'
    @winrt_classmethod
    def FromSystemRelativeTargetTime(cls: Windows.Perception.IPerceptionTimestampHelperStatics2, targetTime: Windows.Foundation.TimeSpan) -> Windows.Perception.PerceptionTimestamp: ...
    @winrt_classmethod
    def FromHistoricalTargetTime(cls: Windows.Perception.IPerceptionTimestampHelperStatics, targetTime: Windows.Foundation.DateTime) -> Windows.Perception.PerceptionTimestamp: ...
make_head(_module, 'IPerceptionTimestamp')
make_head(_module, 'IPerceptionTimestamp2')
make_head(_module, 'IPerceptionTimestampHelperStatics')
make_head(_module, 'IPerceptionTimestampHelperStatics2')
make_head(_module, 'PerceptionTimestamp')
make_head(_module, 'PerceptionTimestampHelper')
