from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Media
import win32more.Windows.Media.Core.Preview
import win32more.Windows.Win32.System.WinRT
class ISoundLevelBrokerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.Preview.ISoundLevelBrokerStatics'
    _iid_ = Guid('{6a633961-dbed-464c-a09a-33412f5caa3f}')
    @winrt_commethod(6)
    def get_SoundLevel(self) -> win32more.Windows.Media.SoundLevel: ...
    @winrt_commethod(7)
    def add_SoundLevelChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_SoundLevelChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    SoundLevel = property(get_SoundLevel, None)
    SoundLevelChanged = event()
class _SoundLevelBroker_Meta_(ComPtr.__class__):
    pass
class SoundLevelBroker(ComPtr, metaclass=_SoundLevelBroker_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.Core.Preview.SoundLevelBroker'
    @winrt_classmethod
    def get_SoundLevel(cls: win32more.Windows.Media.Core.Preview.ISoundLevelBrokerStatics) -> win32more.Windows.Media.SoundLevel: ...
    @winrt_classmethod
    def add_SoundLevelChanged(cls: win32more.Windows.Media.Core.Preview.ISoundLevelBrokerStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_SoundLevelChanged(cls: win32more.Windows.Media.Core.Preview.ISoundLevelBrokerStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    _SoundLevelBroker_Meta_.SoundLevel = property(get_SoundLevel, None)


make_ready(__name__)
