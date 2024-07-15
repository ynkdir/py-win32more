from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Management.Policies
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.Win32.System.WinRT
class INamedPolicyData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Policies.INamedPolicyData'
    _iid_ = Guid('{38dcb198-95ac-4077-a643-8078cae26400}')
    @winrt_commethod(6)
    def get_Area(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Kind(self) -> win32more.Windows.Management.Policies.NamedPolicyKind: ...
    @winrt_commethod(9)
    def get_IsManaged(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsUserPolicy(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_User(self) -> win32more.Windows.System.User: ...
    @winrt_commethod(12)
    def GetBoolean(self) -> Boolean: ...
    @winrt_commethod(13)
    def GetBinary(self) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_commethod(14)
    def GetInt32(self) -> Int32: ...
    @winrt_commethod(15)
    def GetInt64(self) -> Int64: ...
    @winrt_commethod(16)
    def GetString(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def add_Changed(self, changedHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Policies.NamedPolicyData, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_Changed(self, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Area = property(get_Area, None)
    IsManaged = property(get_IsManaged, None)
    IsUserPolicy = property(get_IsUserPolicy, None)
    Kind = property(get_Kind, None)
    Name = property(get_Name, None)
    User = property(get_User, None)
    Changed = event()
class INamedPolicyStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Policies.INamedPolicyStatics'
    _iid_ = Guid('{7f793be7-76c4-4058-8cad-67662cd05f0d}')
    @winrt_commethod(6)
    def GetPolicyFromPath(self, area: WinRT_String, name: WinRT_String) -> win32more.Windows.Management.Policies.NamedPolicyData: ...
    @winrt_commethod(7)
    def GetPolicyFromPathForUser(self, user: win32more.Windows.System.User, area: WinRT_String, name: WinRT_String) -> win32more.Windows.Management.Policies.NamedPolicyData: ...
class NamedPolicy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Management.Policies.NamedPolicy'
    @winrt_classmethod
    def GetPolicyFromPath(cls: win32more.Windows.Management.Policies.INamedPolicyStatics, area: WinRT_String, name: WinRT_String) -> win32more.Windows.Management.Policies.NamedPolicyData: ...
    @winrt_classmethod
    def GetPolicyFromPathForUser(cls: win32more.Windows.Management.Policies.INamedPolicyStatics, user: win32more.Windows.System.User, area: WinRT_String, name: WinRT_String) -> win32more.Windows.Management.Policies.NamedPolicyData: ...
class NamedPolicyData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Management.Policies.INamedPolicyData
    _classid_ = 'Windows.Management.Policies.NamedPolicyData'
    @winrt_mixinmethod
    def get_Area(self: win32more.Windows.Management.Policies.INamedPolicyData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Management.Policies.INamedPolicyData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Management.Policies.INamedPolicyData) -> win32more.Windows.Management.Policies.NamedPolicyKind: ...
    @winrt_mixinmethod
    def get_IsManaged(self: win32more.Windows.Management.Policies.INamedPolicyData) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsUserPolicy(self: win32more.Windows.Management.Policies.INamedPolicyData) -> Boolean: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.Management.Policies.INamedPolicyData) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def GetBoolean(self: win32more.Windows.Management.Policies.INamedPolicyData) -> Boolean: ...
    @winrt_mixinmethod
    def GetBinary(self: win32more.Windows.Management.Policies.INamedPolicyData) -> win32more.Windows.Storage.Streams.IBuffer: ...
    @winrt_mixinmethod
    def GetInt32(self: win32more.Windows.Management.Policies.INamedPolicyData) -> Int32: ...
    @winrt_mixinmethod
    def GetInt64(self: win32more.Windows.Management.Policies.INamedPolicyData) -> Int64: ...
    @winrt_mixinmethod
    def GetString(self: win32more.Windows.Management.Policies.INamedPolicyData) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_Changed(self: win32more.Windows.Management.Policies.INamedPolicyData, changedHandler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Management.Policies.NamedPolicyData, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Changed(self: win32more.Windows.Management.Policies.INamedPolicyData, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Area = property(get_Area, None)
    IsManaged = property(get_IsManaged, None)
    IsUserPolicy = property(get_IsUserPolicy, None)
    Kind = property(get_Kind, None)
    Name = property(get_Name, None)
    User = property(get_User, None)
    Changed = event()
class NamedPolicyKind(Enum, Int32):
    Invalid = 0
    Binary = 1
    Boolean = 2
    Int32 = 3
    Int64 = 4
    String = 5


make_ready(__name__)
