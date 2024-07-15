from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Windows.System
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class _EnvironmentManager_Meta_(ComPtr.__class__):
    pass
class EnvironmentManager(ComPtr, metaclass=_EnvironmentManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Windows.System.IEnvironmentManager
    _classid_ = 'Microsoft.Windows.System.EnvironmentManager'
    @winrt_mixinmethod
    def GetEnvironmentVariables(self: win32more.Microsoft.Windows.System.IEnvironmentManager) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def GetEnvironmentVariable(self: win32more.Microsoft.Windows.System.IEnvironmentManager, name: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def SetEnvironmentVariable(self: win32more.Microsoft.Windows.System.IEnvironmentManager, name: WinRT_String, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def AppendToPath(self: win32more.Microsoft.Windows.System.IEnvironmentManager, path: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RemoveFromPath(self: win32more.Microsoft.Windows.System.IEnvironmentManager, path: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def AddExecutableFileExtension(self: win32more.Microsoft.Windows.System.IEnvironmentManager, pathExt: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RemoveExecutableFileExtension(self: win32more.Microsoft.Windows.System.IEnvironmentManager, pathExt: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AreChangesTracked(self: win32more.Microsoft.Windows.System.IEnvironmentManager2) -> Boolean: ...
    @winrt_classmethod
    def GetForProcess(cls: win32more.Microsoft.Windows.System.IEnvironmentManagerStatics) -> win32more.Microsoft.Windows.System.EnvironmentManager: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Microsoft.Windows.System.IEnvironmentManagerStatics) -> win32more.Microsoft.Windows.System.EnvironmentManager: ...
    @winrt_classmethod
    def GetForMachine(cls: win32more.Microsoft.Windows.System.IEnvironmentManagerStatics) -> win32more.Microsoft.Windows.System.EnvironmentManager: ...
    @winrt_classmethod
    def get_IsSupported(cls: win32more.Microsoft.Windows.System.IEnvironmentManagerStatics) -> Boolean: ...
    AreChangesTracked = property(get_AreChangesTracked, None)
    _EnvironmentManager_Meta_.IsSupported = property(get_IsSupported, None)
EnvironmentManagerContract: UInt32 = 131072
class IEnvironmentManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.System.IEnvironmentManager'
    _iid_ = Guid('{d1b239bb-7013-5176-b02a-63477410d986}')
    @winrt_commethod(6)
    def GetEnvironmentVariables(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_commethod(7)
    def GetEnvironmentVariable(self, name: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(8)
    def SetEnvironmentVariable(self, name: WinRT_String, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def AppendToPath(self, path: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def RemoveFromPath(self, path: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def AddExecutableFileExtension(self, pathExt: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def RemoveExecutableFileExtension(self, pathExt: WinRT_String) -> Void: ...
class IEnvironmentManager2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.System.IEnvironmentManager2'
    _iid_ = Guid('{cfc0ad51-02b7-57ff-8ca7-e015251737cb}')
    @winrt_commethod(6)
    def get_AreChangesTracked(self) -> Boolean: ...
    AreChangesTracked = property(get_AreChangesTracked, None)
class IEnvironmentManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.System.IEnvironmentManagerStatics'
    _iid_ = Guid('{407b1522-6156-5398-93fd-d6411c35e7b1}')
    @winrt_commethod(6)
    def GetForProcess(self) -> win32more.Microsoft.Windows.System.EnvironmentManager: ...
    @winrt_commethod(7)
    def GetForUser(self) -> win32more.Microsoft.Windows.System.EnvironmentManager: ...
    @winrt_commethod(8)
    def GetForMachine(self) -> win32more.Microsoft.Windows.System.EnvironmentManager: ...
    @winrt_commethod(9)
    def get_IsSupported(self) -> Boolean: ...
    IsSupported = property(get_IsSupported, None)


make_ready(__name__)
