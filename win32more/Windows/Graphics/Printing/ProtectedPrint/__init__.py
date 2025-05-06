from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, FlexibleArray, Guid, Int16, Int32, Int64, IntPtr, NativeBitfieldAttribute, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Graphics.Printing.ProtectedPrint
import win32more.Windows.Win32.System.WinRT
class IWindowsProtectedPrintInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.ProtectedPrint.IWindowsProtectedPrintInfoStatics'
    _iid_ = Guid('{a7d212f3-4168-5485-98ab-d89d04603b40}')
    @winrt_commethod(6)
    def get_IsProtectedPrintEnabled(self) -> Boolean: ...
    IsProtectedPrintEnabled = property(get_IsProtectedPrintEnabled, None)
class _WindowsProtectedPrintInfo_Meta_(ComPtr.__class__):
    pass
class WindowsProtectedPrintInfo(ComPtr, metaclass=_WindowsProtectedPrintInfo_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Graphics.Printing.ProtectedPrint.WindowsProtectedPrintInfo'
    @winrt_classmethod
    def get_IsProtectedPrintEnabled(cls: win32more.Windows.Graphics.Printing.ProtectedPrint.IWindowsProtectedPrintInfoStatics) -> Boolean: ...
    _WindowsProtectedPrintInfo_Meta_.IsProtectedPrintEnabled = property(get_IsProtectedPrintEnabled, None)


make_ready(__name__)
