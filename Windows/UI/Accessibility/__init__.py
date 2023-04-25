from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.System.WinRT
import Windows.Foundation
import Windows.UI.Accessibility
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IScreenReaderPositionChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('557eb5e5-54d0-5ccd-9f-c5-ed-33-35-7f-8a-9f')
    @winrt_commethod(6)
    def get_ScreenPositionInRawPixels(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_IsReadingText(self) -> Boolean: ...
    ScreenPositionInRawPixels = property(get_ScreenPositionInRawPixels, None)
    IsReadingText = property(get_IsReadingText, None)
class IScreenReaderService(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('19475427-eac0-50d3-bd-d9-9b-48-7a-22-62-56')
    @winrt_commethod(6)
    def get_CurrentScreenReaderPosition(self) -> Windows.UI.Accessibility.ScreenReaderPositionChangedEventArgs: ...
    @winrt_commethod(7)
    def add_ScreenReaderPositionChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Accessibility.ScreenReaderService, Windows.UI.Accessibility.ScreenReaderPositionChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_ScreenReaderPositionChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentScreenReaderPosition = property(get_CurrentScreenReaderPosition, None)
class ScreenReaderPositionChangedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Accessibility.ScreenReaderPositionChangedEventArgs'
    @winrt_mixinmethod
    def get_ScreenPositionInRawPixels(self: Windows.UI.Accessibility.IScreenReaderPositionChangedEventArgs) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_IsReadingText(self: Windows.UI.Accessibility.IScreenReaderPositionChangedEventArgs) -> Boolean: ...
    ScreenPositionInRawPixels = property(get_ScreenPositionInRawPixels, None)
    IsReadingText = property(get_IsReadingText, None)
class ScreenReaderService(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Accessibility.ScreenReaderService'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Accessibility.ScreenReaderService: ...
    @winrt_mixinmethod
    def get_CurrentScreenReaderPosition(self: Windows.UI.Accessibility.IScreenReaderService) -> Windows.UI.Accessibility.ScreenReaderPositionChangedEventArgs: ...
    @winrt_mixinmethod
    def add_ScreenReaderPositionChanged(self: Windows.UI.Accessibility.IScreenReaderService, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Accessibility.ScreenReaderService, Windows.UI.Accessibility.ScreenReaderPositionChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScreenReaderPositionChanged(self: Windows.UI.Accessibility.IScreenReaderService, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentScreenReaderPosition = property(get_CurrentScreenReaderPosition, None)
make_head(_module, 'IScreenReaderPositionChangedEventArgs')
make_head(_module, 'IScreenReaderService')
make_head(_module, 'ScreenReaderPositionChangedEventArgs')
make_head(_module, 'ScreenReaderService')
