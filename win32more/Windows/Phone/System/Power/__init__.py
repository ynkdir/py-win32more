from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Phone.System.Power
import win32more.Windows.Win32.System.WinRT
class IPowerManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.Power.IPowerManagerStatics'
    _iid_ = Guid('{25de8fd0-1c5b-11e1-bddb-0800200c9a66}')
    @winrt_commethod(6)
    def get_PowerSavingMode(self) -> win32more.Windows.Phone.System.Power.PowerSavingMode: ...
    @winrt_commethod(7)
    def add_PowerSavingModeChanged(self, changeHandler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_PowerSavingModeChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PowerSavingMode = property(get_PowerSavingMode, None)
    PowerSavingModeChanged = event()
class IPowerManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.Power.IPowerManagerStatics2'
    _iid_ = Guid('{596236cf-1918-4551-a466-c51aae373bf8}')
    @winrt_commethod(6)
    def get_PowerSavingModeEnabled(self) -> Boolean: ...
    PowerSavingModeEnabled = property(get_PowerSavingModeEnabled, None)
class _PowerManager_Meta_(ComPtr.__class__):
    pass
class PowerManager(ComPtr, metaclass=_PowerManager_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.Power.PowerManager'
    @winrt_classmethod
    def get_PowerSavingMode(cls: win32more.Windows.Phone.System.Power.IPowerManagerStatics) -> win32more.Windows.Phone.System.Power.PowerSavingMode: ...
    @winrt_classmethod
    def add_PowerSavingModeChanged(cls: win32more.Windows.Phone.System.Power.IPowerManagerStatics, changeHandler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_PowerSavingModeChanged(cls: win32more.Windows.Phone.System.Power.IPowerManagerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_PowerSavingModeEnabled(cls: win32more.Windows.Phone.System.Power.IPowerManagerStatics2) -> Boolean: ...
    _PowerManager_Meta_.PowerSavingMode = property(get_PowerSavingMode, None)
    _PowerManager_Meta_.PowerSavingModeEnabled = property(get_PowerSavingModeEnabled, None)
class PowerSavingMode(Enum, Int32):
    Off = 0
    On = 1


make_ready(__name__)
