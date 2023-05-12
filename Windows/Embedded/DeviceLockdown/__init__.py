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
import Windows.Embedded.DeviceLockdown
import Windows.Foundation
import Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
DeviceLockdownContract: UInt32 = 65536
class DeviceLockdownProfile(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Embedded.DeviceLockdown.DeviceLockdownProfile'
    @winrt_classmethod
    def GetSupportedLockdownProfiles(cls: Windows.Embedded.DeviceLockdown.IDeviceLockdownProfileStatics) -> Windows.Foundation.Collections.IVectorView[Guid]: ...
    @winrt_classmethod
    def GetCurrentLockdownProfile(cls: Windows.Embedded.DeviceLockdown.IDeviceLockdownProfileStatics) -> Guid: ...
    @winrt_classmethod
    def ApplyLockdownProfileAsync(cls: Windows.Embedded.DeviceLockdown.IDeviceLockdownProfileStatics, profileID: Guid) -> Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetLockdownProfileInformation(cls: Windows.Embedded.DeviceLockdown.IDeviceLockdownProfileStatics, profileID: Guid) -> Windows.Embedded.DeviceLockdown.DeviceLockdownProfileInformation: ...
class DeviceLockdownProfileInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Embedded.DeviceLockdown.IDeviceLockdownProfileInformation
    _classid_ = 'Windows.Embedded.DeviceLockdown.DeviceLockdownProfileInformation'
    @winrt_mixinmethod
    def get_Name(self: Windows.Embedded.DeviceLockdown.IDeviceLockdownProfileInformation) -> WinRT_String: ...
    Name = property(get_Name, None)
class IDeviceLockdownProfileInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Embedded.DeviceLockdown.IDeviceLockdownProfileInformation'
    _iid_ = Guid('{7980e14e-45b1-4a96-92fc-62756b739678}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    Name = property(get_Name, None)
class IDeviceLockdownProfileStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Embedded.DeviceLockdown.IDeviceLockdownProfileStatics'
    _iid_ = Guid('{622f6965-f9a8-41a1-a691-88cd80c7a069}')
    @winrt_commethod(6)
    def GetSupportedLockdownProfiles(self) -> Windows.Foundation.Collections.IVectorView[Guid]: ...
    @winrt_commethod(7)
    def GetCurrentLockdownProfile(self) -> Guid: ...
    @winrt_commethod(8)
    def ApplyLockdownProfileAsync(self, profileID: Guid) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def GetLockdownProfileInformation(self, profileID: Guid) -> Windows.Embedded.DeviceLockdown.DeviceLockdownProfileInformation: ...
make_head(_module, 'DeviceLockdownProfile')
make_head(_module, 'DeviceLockdownProfileInformation')
make_head(_module, 'IDeviceLockdownProfileInformation')
make_head(_module, 'IDeviceLockdownProfileStatics')
