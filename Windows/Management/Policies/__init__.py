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
import Windows.Foundation
import Windows.Management.Policies
import Windows.Storage.Streams
import Windows.System
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class INamedPolicyData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Policies.INamedPolicyData'
    _iid_ = Guid('{38dcb198-95ac-4077-a643-8078cae26400}')
    @winrt_commethod(6)
    def get_Area(self: Windows.Management.Policies.INamedPolicyData) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Name(self: Windows.Management.Policies.INamedPolicyData) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Kind(self: Windows.Management.Policies.INamedPolicyData) -> Windows.Management.Policies.NamedPolicyKind: ...
    @winrt_commethod(9)
    def get_IsManaged(self: Windows.Management.Policies.INamedPolicyData) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsUserPolicy(self: Windows.Management.Policies.INamedPolicyData) -> Boolean: ...
    @winrt_commethod(11)
    def get_User(self: Windows.Management.Policies.INamedPolicyData) -> Windows.System.User: ...
    @winrt_commethod(12)
    def GetBoolean(self: Windows.Management.Policies.INamedPolicyData) -> Boolean: ...
    @winrt_commethod(13)
    def GetBinary(self: Windows.Management.Policies.INamedPolicyData) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(14)
    def GetInt32(self: Windows.Management.Policies.INamedPolicyData) -> Int32: ...
    @winrt_commethod(15)
    def GetInt64(self: Windows.Management.Policies.INamedPolicyData) -> Int64: ...
    @winrt_commethod(16)
    def GetString(self: Windows.Management.Policies.INamedPolicyData) -> WinRT_String: ...
    @winrt_commethod(17)
    def add_Changed(self: Windows.Management.Policies.INamedPolicyData, changedHandler: Windows.Foundation.TypedEventHandler[Windows.Management.Policies.NamedPolicyData, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_Changed(self: Windows.Management.Policies.INamedPolicyData, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Area = property(get_Area, None)
    Name = property(get_Name, None)
    Kind = property(get_Kind, None)
    IsManaged = property(get_IsManaged, None)
    IsUserPolicy = property(get_IsUserPolicy, None)
    User = property(get_User, None)
class INamedPolicyStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Policies.INamedPolicyStatics'
    _iid_ = Guid('{7f793be7-76c4-4058-8cad-67662cd05f0d}')
    @winrt_commethod(6)
    def GetPolicyFromPath(self: Windows.Management.Policies.INamedPolicyStatics, area: WinRT_String, name: WinRT_String) -> Windows.Management.Policies.NamedPolicyData: ...
    @winrt_commethod(7)
    def GetPolicyFromPathForUser(self: Windows.Management.Policies.INamedPolicyStatics, user: Windows.System.User, area: WinRT_String, name: WinRT_String) -> Windows.Management.Policies.NamedPolicyData: ...
class NamedPolicy(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Policies.NamedPolicy'
    @winrt_classmethod
    def GetPolicyFromPath(cls: Windows.Management.Policies.INamedPolicyStatics, area: WinRT_String, name: WinRT_String) -> Windows.Management.Policies.NamedPolicyData: ...
    @winrt_classmethod
    def GetPolicyFromPathForUser(cls: Windows.Management.Policies.INamedPolicyStatics, user: Windows.System.User, area: WinRT_String, name: WinRT_String) -> Windows.Management.Policies.NamedPolicyData: ...
class NamedPolicyData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Management.Policies.INamedPolicyData
    _classid_ = 'Windows.Management.Policies.NamedPolicyData'
    @winrt_mixinmethod
    def get_Area(self: Windows.Management.Policies.INamedPolicyData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.Management.Policies.INamedPolicyData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.Management.Policies.INamedPolicyData) -> Windows.Management.Policies.NamedPolicyKind: ...
    @winrt_mixinmethod
    def get_IsManaged(self: Windows.Management.Policies.INamedPolicyData) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsUserPolicy(self: Windows.Management.Policies.INamedPolicyData) -> Boolean: ...
    @winrt_mixinmethod
    def get_User(self: Windows.Management.Policies.INamedPolicyData) -> Windows.System.User: ...
    @winrt_mixinmethod
    def GetBoolean(self: Windows.Management.Policies.INamedPolicyData) -> Boolean: ...
    @winrt_mixinmethod
    def GetBinary(self: Windows.Management.Policies.INamedPolicyData) -> Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def GetInt32(self: Windows.Management.Policies.INamedPolicyData) -> Int32: ...
    @winrt_mixinmethod
    def GetInt64(self: Windows.Management.Policies.INamedPolicyData) -> Int64: ...
    @winrt_mixinmethod
    def GetString(self: Windows.Management.Policies.INamedPolicyData) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_Changed(self: Windows.Management.Policies.INamedPolicyData, changedHandler: Windows.Foundation.TypedEventHandler[Windows.Management.Policies.NamedPolicyData, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: Windows.Management.Policies.INamedPolicyData, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Area = property(get_Area, None)
    Name = property(get_Name, None)
    Kind = property(get_Kind, None)
    IsManaged = property(get_IsManaged, None)
    IsUserPolicy = property(get_IsUserPolicy, None)
    User = property(get_User, None)
NamedPolicyKind = Int32
NamedPolicyKind_Invalid: NamedPolicyKind = 0
NamedPolicyKind_Binary: NamedPolicyKind = 1
NamedPolicyKind_Boolean: NamedPolicyKind = 2
NamedPolicyKind_Int32: NamedPolicyKind = 3
NamedPolicyKind_Int64: NamedPolicyKind = 4
NamedPolicyKind_String: NamedPolicyKind = 5
make_head(_module, 'INamedPolicyData')
make_head(_module, 'INamedPolicyStatics')
make_head(_module, 'NamedPolicy')
make_head(_module, 'NamedPolicyData')
