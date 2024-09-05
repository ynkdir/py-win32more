from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Windows.Globalization
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class _ApplicationLanguages_Meta_(ComPtr.__class__):
    pass
class ApplicationLanguages(ComPtr, metaclass=_ApplicationLanguages_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Globalization.ApplicationLanguages'
    @winrt_classmethod
    def get_Languages(cls: win32more.Microsoft.Windows.Globalization.IApplicationLanguagesStatics) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def get_ManifestLanguages(cls: win32more.Microsoft.Windows.Globalization.IApplicationLanguagesStatics) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_classmethod
    def get_PrimaryLanguageOverride(cls: win32more.Microsoft.Windows.Globalization.IApplicationLanguagesStatics) -> WinRT_String: ...
    @winrt_classmethod
    def put_PrimaryLanguageOverride(cls: win32more.Microsoft.Windows.Globalization.IApplicationLanguagesStatics, value: WinRT_String) -> Void: ...
    _ApplicationLanguages_Meta_.Languages = property(get_Languages, None)
    _ApplicationLanguages_Meta_.ManifestLanguages = property(get_ManifestLanguages, None)
    _ApplicationLanguages_Meta_.PrimaryLanguageOverride = property(get_PrimaryLanguageOverride, put_PrimaryLanguageOverride)
class IApplicationLanguagesStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Windows.Globalization.IApplicationLanguagesStatics'
    _iid_ = Guid('{58dfcef9-08ec-5086-8af1-d5beab79250a}')
    @winrt_commethod(6)
    def get_Languages(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(7)
    def get_ManifestLanguages(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def get_PrimaryLanguageOverride(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_PrimaryLanguageOverride(self, value: WinRT_String) -> Void: ...
    Languages = property(get_Languages, None)
    ManifestLanguages = property(get_ManifestLanguages, None)
    PrimaryLanguageOverride = property(get_PrimaryLanguageOverride, put_PrimaryLanguageOverride)


make_ready(__name__)
