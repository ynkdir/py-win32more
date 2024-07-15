from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation.Collections
import win32more.Windows.Globalization.Collation
import win32more.Windows.Win32.System.WinRT
class CharacterGrouping(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Globalization.Collation.ICharacterGrouping
    _classid_ = 'Windows.Globalization.Collation.CharacterGrouping'
    @winrt_mixinmethod
    def get_First(self: win32more.Windows.Globalization.Collation.ICharacterGrouping) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Windows.Globalization.Collation.ICharacterGrouping) -> WinRT_String: ...
    First = property(get_First, None)
    Label = property(get_Label, None)
class CharacterGroupings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.Globalization.Collation.CharacterGrouping]]
    default_interface: win32more.Windows.Globalization.Collation.ICharacterGroupings
    _classid_ = 'Windows.Globalization.Collation.CharacterGroupings'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Globalization.Collation.CharacterGroupings.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Globalization.Collation.CharacterGroupings.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Globalization.Collation.CharacterGroupings: ...
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Globalization.Collation.ICharacterGroupingsFactory, language: WinRT_String) -> win32more.Windows.Globalization.Collation.CharacterGroupings: ...
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Globalization.Collation.ICharacterGroupings, text: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Globalization.Collation.CharacterGrouping], index: UInt32) -> win32more.Windows.Globalization.Collation.CharacterGrouping: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Globalization.Collation.CharacterGrouping]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Globalization.Collation.CharacterGrouping], value: win32more.Windows.Globalization.Collation.CharacterGrouping, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Globalization.Collation.CharacterGrouping], startIndex: UInt32, items: FillArray[win32more.Windows.Globalization.Collation.CharacterGrouping]) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Globalization.Collation.CharacterGrouping]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Globalization.Collation.CharacterGrouping]: ...
    Size = property(get_Size, None)
class ICharacterGrouping(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.Collation.ICharacterGrouping'
    _iid_ = Guid('{fae761bb-805d-4bb0-95bb-c1f7c3e8eb8e}')
    @winrt_commethod(6)
    def get_First(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Label(self) -> WinRT_String: ...
    First = property(get_First, None)
    Label = property(get_Label, None)
class ICharacterGroupings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.Globalization.Collation.CharacterGrouping]]
    _classid_ = 'Windows.Globalization.Collation.ICharacterGroupings'
    _iid_ = Guid('{b8d20a75-d4cf-4055-80e5-ce169c226496}')
    @winrt_commethod(6)
    def Lookup(self, text: WinRT_String) -> WinRT_String: ...
class ICharacterGroupingsFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.Collation.ICharacterGroupingsFactory'
    _iid_ = Guid('{99ea9fd9-886d-4401-9f98-69c82d4c2f78}')
    @winrt_commethod(6)
    def Create(self, language: WinRT_String) -> win32more.Windows.Globalization.Collation.CharacterGroupings: ...


make_ready(__name__)
