from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
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
class IScreenReaderPositionChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Accessibility.IScreenReaderPositionChangedEventArgs'
    _iid_ = Guid('{557eb5e5-54d0-5ccd-9fc5-ed33357f8a9f}')
    @winrt_commethod(6)
    def get_ScreenPositionInRawPixels(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_IsReadingText(self) -> Boolean: ...
    ScreenPositionInRawPixels = property(get_ScreenPositionInRawPixels, None)
    IsReadingText = property(get_IsReadingText, None)
class IScreenReaderService(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Accessibility.IScreenReaderService'
    _iid_ = Guid('{19475427-eac0-50d3-bdd9-9b487a226256}')
    @winrt_commethod(6)
    def get_CurrentScreenReaderPosition(self) -> Windows.UI.Accessibility.ScreenReaderPositionChangedEventArgs: ...
    @winrt_commethod(7)
    def add_ScreenReaderPositionChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Accessibility.ScreenReaderService, Windows.UI.Accessibility.ScreenReaderPositionChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_ScreenReaderPositionChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentScreenReaderPosition = property(get_CurrentScreenReaderPosition, None)
class ScreenReaderPositionChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Accessibility.IScreenReaderPositionChangedEventArgs
    _classid_ = 'Windows.UI.Accessibility.ScreenReaderPositionChangedEventArgs'
    @winrt_mixinmethod
    def get_ScreenPositionInRawPixels(self: Windows.UI.Accessibility.IScreenReaderPositionChangedEventArgs) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_IsReadingText(self: Windows.UI.Accessibility.IScreenReaderPositionChangedEventArgs) -> Boolean: ...
    ScreenPositionInRawPixels = property(get_ScreenPositionInRawPixels, None)
    IsReadingText = property(get_IsReadingText, None)
class ScreenReaderService(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Accessibility.IScreenReaderService
    _classid_ = 'Windows.UI.Accessibility.ScreenReaderService'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Accessibility.ScreenReaderService: ...
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
