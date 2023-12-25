from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.UI.Accessibility
class IScreenReaderPositionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Accessibility.IScreenReaderPositionChangedEventArgs'
    _iid_ = Guid('{557eb5e5-54d0-5ccd-9fc5-ed33357f8a9f}')
    @winrt_commethod(6)
    def get_ScreenPositionInRawPixels(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_IsReadingText(self) -> Boolean: ...
    ScreenPositionInRawPixels = property(get_ScreenPositionInRawPixels, None)
    IsReadingText = property(get_IsReadingText, None)
class IScreenReaderService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Accessibility.IScreenReaderService'
    _iid_ = Guid('{19475427-eac0-50d3-bdd9-9b487a226256}')
    @winrt_commethod(6)
    def get_CurrentScreenReaderPosition(self) -> win32more.Windows.UI.Accessibility.ScreenReaderPositionChangedEventArgs: ...
    @winrt_commethod(7)
    def add_ScreenReaderPositionChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Accessibility.ScreenReaderService, win32more.Windows.UI.Accessibility.ScreenReaderPositionChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_ScreenReaderPositionChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentScreenReaderPosition = property(get_CurrentScreenReaderPosition, None)
class ScreenReaderPositionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Accessibility.IScreenReaderPositionChangedEventArgs
    _classid_ = 'Windows.UI.Accessibility.ScreenReaderPositionChangedEventArgs'
    @winrt_mixinmethod
    def get_ScreenPositionInRawPixels(self: win32more.Windows.UI.Accessibility.IScreenReaderPositionChangedEventArgs) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_IsReadingText(self: win32more.Windows.UI.Accessibility.IScreenReaderPositionChangedEventArgs) -> Boolean: ...
    ScreenPositionInRawPixels = property(get_ScreenPositionInRawPixels, None)
    IsReadingText = property(get_IsReadingText, None)
class ScreenReaderService(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Accessibility.IScreenReaderService
    _classid_ = 'Windows.UI.Accessibility.ScreenReaderService'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.UI.Accessibility.ScreenReaderService.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Accessibility.ScreenReaderService: ...
    @winrt_mixinmethod
    def get_CurrentScreenReaderPosition(self: win32more.Windows.UI.Accessibility.IScreenReaderService) -> win32more.Windows.UI.Accessibility.ScreenReaderPositionChangedEventArgs: ...
    @winrt_mixinmethod
    def add_ScreenReaderPositionChanged(self: win32more.Windows.UI.Accessibility.IScreenReaderService, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Accessibility.ScreenReaderService, win32more.Windows.UI.Accessibility.ScreenReaderPositionChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScreenReaderPositionChanged(self: win32more.Windows.UI.Accessibility.IScreenReaderService, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentScreenReaderPosition = property(get_CurrentScreenReaderPosition, None)
make_ready(__name__)
