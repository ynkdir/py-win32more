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
import Windows.Foundation.Collections
import Windows.Globalization.Collation
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class CharacterGrouping(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Globalization.Collation.ICharacterGrouping
    _classid_ = 'Windows.Globalization.Collation.CharacterGrouping'
    @winrt_mixinmethod
    def get_First(self: Windows.Globalization.Collation.ICharacterGrouping) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Label(self: Windows.Globalization.Collation.ICharacterGrouping) -> WinRT_String: ...
    First = property(get_First, None)
    Label = property(get_Label, None)
class CharacterGroupings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Globalization.Collation.ICharacterGroupings
    _classid_ = 'Windows.Globalization.Collation.CharacterGroupings'
    @winrt_activatemethod
    def New(cls) -> Windows.Globalization.Collation.CharacterGroupings: ...
    @winrt_factorymethod
    def Create(cls: Windows.Globalization.Collation.ICharacterGroupingsFactory, language: WinRT_String) -> Windows.Globalization.Collation.CharacterGroupings: ...
    @winrt_mixinmethod
    def Lookup(self: Windows.Globalization.Collation.ICharacterGroupings, text: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVectorView[Windows.Globalization.Collation.CharacterGrouping], index: UInt32) -> Windows.Globalization.Collation.CharacterGrouping: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVectorView[Windows.Globalization.Collation.CharacterGrouping]) -> UInt32: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVectorView[Windows.Globalization.Collation.CharacterGrouping], value: Windows.Globalization.Collation.CharacterGrouping, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVectorView[Windows.Globalization.Collation.CharacterGrouping], startIndex: UInt32, items: POINTER(Windows.Globalization.Collation.CharacterGrouping)) -> UInt32: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Globalization.Collation.CharacterGrouping]) -> Windows.Foundation.Collections.IIterator[Windows.Globalization.Collation.CharacterGrouping]: ...
    Size = property(get_Size, None)
class ICharacterGrouping(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.Collation.ICharacterGrouping'
    _iid_ = Guid('{fae761bb-805d-4bb0-95bb-c1f7c3e8eb8e}')
    @winrt_commethod(6)
    def get_First(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Label(self) -> WinRT_String: ...
    First = property(get_First, None)
    Label = property(get_Label, None)
class ICharacterGroupings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.Collation.ICharacterGroupings'
    _iid_ = Guid('{b8d20a75-d4cf-4055-80e5-ce169c226496}')
    @winrt_commethod(6)
    def Lookup(self, text: WinRT_String) -> WinRT_String: ...
class ICharacterGroupingsFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Globalization.Collation.ICharacterGroupingsFactory'
    _iid_ = Guid('{99ea9fd9-886d-4401-9f98-69c82d4c2f78}')
    @winrt_commethod(6)
    def Create(self, language: WinRT_String) -> Windows.Globalization.Collation.CharacterGroupings: ...
make_head(_module, 'CharacterGrouping')
make_head(_module, 'CharacterGroupings')
make_head(_module, 'ICharacterGrouping')
make_head(_module, 'ICharacterGroupings')
make_head(_module, 'ICharacterGroupingsFactory')
