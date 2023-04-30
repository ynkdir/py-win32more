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
import Windows.Devices.Background
import Windows.Foundation
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class DeviceServicingDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Background.DeviceServicingDetails'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Background.IDeviceServicingDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Arguments(self: Windows.Devices.Background.IDeviceServicingDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ExpectedDuration(self: Windows.Devices.Background.IDeviceServicingDetails) -> Windows.Foundation.TimeSpan: ...
    DeviceId = property(get_DeviceId, None)
    Arguments = property(get_Arguments, None)
    ExpectedDuration = property(get_ExpectedDuration, None)
class DeviceUseDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Background.DeviceUseDetails'
    @winrt_mixinmethod
    def get_DeviceId(self: Windows.Devices.Background.IDeviceUseDetails) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Arguments(self: Windows.Devices.Background.IDeviceUseDetails) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    Arguments = property(get_Arguments, None)
class IDeviceServicingDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('4aabee29-2344-4ac4-85-27-4a-8e-f6-90-56-45')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Arguments(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ExpectedDuration(self) -> Windows.Foundation.TimeSpan: ...
    DeviceId = property(get_DeviceId, None)
    Arguments = property(get_Arguments, None)
    ExpectedDuration = property(get_ExpectedDuration, None)
class IDeviceUseDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('7d565141-557e-4154-b9-94-e4-f7-a1-1f-b3-23')
    @winrt_commethod(6)
    def get_DeviceId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Arguments(self) -> WinRT_String: ...
    DeviceId = property(get_DeviceId, None)
    Arguments = property(get_Arguments, None)
make_head(_module, 'DeviceServicingDetails')
make_head(_module, 'DeviceUseDetails')
make_head(_module, 'IDeviceServicingDetails')
make_head(_module, 'IDeviceUseDetails')
