from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Embedded.DeviceLockdown
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
DeviceLockdownContract: UInt32 = 65536
class DeviceLockdownProfile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Embedded.DeviceLockdown.DeviceLockdownProfile'
    @winrt_classmethod
    def GetSupportedLockdownProfiles(cls: win32more.Windows.Embedded.DeviceLockdown.IDeviceLockdownProfileStatics) -> win32more.Windows.Foundation.Collections.IVectorView[Guid]: ...
    @winrt_classmethod
    def GetCurrentLockdownProfile(cls: win32more.Windows.Embedded.DeviceLockdown.IDeviceLockdownProfileStatics) -> Guid: ...
    @winrt_classmethod
    def ApplyLockdownProfileAsync(cls: win32more.Windows.Embedded.DeviceLockdown.IDeviceLockdownProfileStatics, profileID: Guid) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def GetLockdownProfileInformation(cls: win32more.Windows.Embedded.DeviceLockdown.IDeviceLockdownProfileStatics, profileID: Guid) -> win32more.Windows.Embedded.DeviceLockdown.DeviceLockdownProfileInformation: ...
class DeviceLockdownProfileInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Embedded.DeviceLockdown.IDeviceLockdownProfileInformation
    _classid_ = 'Windows.Embedded.DeviceLockdown.DeviceLockdownProfileInformation'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.Embedded.DeviceLockdown.IDeviceLockdownProfileInformation) -> WinRT_String: ...
    Name = property(get_Name, None)
class IDeviceLockdownProfileInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Embedded.DeviceLockdown.IDeviceLockdownProfileInformation'
    _iid_ = Guid('{7980e14e-45b1-4a96-92fc-62756b739678}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    Name = property(get_Name, None)
class IDeviceLockdownProfileStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Embedded.DeviceLockdown.IDeviceLockdownProfileStatics'
    _iid_ = Guid('{622f6965-f9a8-41a1-a691-88cd80c7a069}')
    @winrt_commethod(6)
    def GetSupportedLockdownProfiles(self) -> win32more.Windows.Foundation.Collections.IVectorView[Guid]: ...
    @winrt_commethod(7)
    def GetCurrentLockdownProfile(self) -> Guid: ...
    @winrt_commethod(8)
    def ApplyLockdownProfileAsync(self, profileID: Guid) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def GetLockdownProfileInformation(self, profileID: Guid) -> win32more.Windows.Embedded.DeviceLockdown.DeviceLockdownProfileInformation: ...


make_ready(__name__)
