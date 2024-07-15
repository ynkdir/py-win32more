from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.System.Display
import win32more.Windows.Win32.System.WinRT
class DisplayRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.System.Display.IDisplayRequest
    _classid_ = 'Windows.System.Display.DisplayRequest'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.System.Display.DisplayRequest.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.System.Display.DisplayRequest: ...
    @winrt_mixinmethod
    def RequestActive(self: win32more.Windows.System.Display.IDisplayRequest) -> Void: ...
    @winrt_mixinmethod
    def RequestRelease(self: win32more.Windows.System.Display.IDisplayRequest) -> Void: ...
class IDisplayRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.System.Display.IDisplayRequest'
    _iid_ = Guid('{e5732044-f49f-4b60-8dd4-5e7e3a632ac0}')
    @winrt_commethod(6)
    def RequestActive(self) -> Void: ...
    @winrt_commethod(7)
    def RequestRelease(self) -> Void: ...


make_ready(__name__)
