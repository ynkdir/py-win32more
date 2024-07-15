from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Phone.System.Profile
import win32more.Windows.Win32.System.WinRT
class IRetailModeStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.Profile.IRetailModeStatics'
    _iid_ = Guid('{d7ded029-fdda-43e7-93fb-e53ab6e89ec3}')
    @winrt_commethod(6)
    def get_RetailModeEnabled(self) -> Boolean: ...
    RetailModeEnabled = property(get_RetailModeEnabled, None)
class _RetailMode_Meta_(ComPtr.__class__):
    pass
class RetailMode(ComPtr, metaclass=_RetailMode_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Phone.System.Profile.RetailMode'
    @winrt_classmethod
    def get_RetailModeEnabled(cls: win32more.Windows.Phone.System.Profile.IRetailModeStatics) -> Boolean: ...
    _RetailMode_Meta_.RetailModeEnabled = property(get_RetailModeEnabled, None)


make_ready(__name__)
