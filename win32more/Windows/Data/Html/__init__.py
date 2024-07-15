from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Data.Html
import win32more.Windows.Win32.System.WinRT
class HtmlUtilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Html.HtmlUtilities'
    @winrt_classmethod
    def ConvertToText(cls: win32more.Windows.Data.Html.IHtmlUtilities, html: WinRT_String) -> WinRT_String: ...
class IHtmlUtilities(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Data.Html.IHtmlUtilities'
    _iid_ = Guid('{fec00add-2399-4fac-b5a7-05e9acd7181d}')
    @winrt_commethod(6)
    def ConvertToText(self, html: WinRT_String) -> WinRT_String: ...


make_ready(__name__)
