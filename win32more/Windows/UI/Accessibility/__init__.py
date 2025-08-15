from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Foundation
import win32more.Windows.UI.Accessibility
class IScreenReaderPositionChangedEventArgs(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Accessibility.IScreenReaderPositionChangedEventArgs'
    _iid_ = Guid('{557eb5e5-54d0-5ccd-9fc5-ed33357f8a9f}')
    @winrt_commethod(6)
    def get_ScreenPositionInRawPixels(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_IsReadingText(self) -> Boolean: ...
    IsReadingText = property(get_IsReadingText, None)
    ScreenPositionInRawPixels = property(get_ScreenPositionInRawPixels, None)
class IScreenReaderService(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.UI.Accessibility.IScreenReaderService'
    _iid_ = Guid('{19475427-eac0-50d3-bdd9-9b487a226256}')
    @winrt_commethod(6)
    def get_CurrentScreenReaderPosition(self) -> win32more.Windows.UI.Accessibility.ScreenReaderPositionChangedEventArgs: ...
    @winrt_commethod(7)
    def add_ScreenReaderPositionChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Accessibility.ScreenReaderService, win32more.Windows.UI.Accessibility.ScreenReaderPositionChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_ScreenReaderPositionChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CurrentScreenReaderPosition = property(get_CurrentScreenReaderPosition, None)
    ScreenReaderPositionChanged = event()
class ScreenReaderPositionChangedEventArgs(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Accessibility.IScreenReaderPositionChangedEventArgs
    _classid_ = 'Windows.UI.Accessibility.ScreenReaderPositionChangedEventArgs'
    @winrt_mixinmethod
    def get_ScreenPositionInRawPixels(self: win32more.Windows.UI.Accessibility.IScreenReaderPositionChangedEventArgs) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_IsReadingText(self: win32more.Windows.UI.Accessibility.IScreenReaderPositionChangedEventArgs) -> Boolean: ...
    IsReadingText = property(get_IsReadingText, None)
    ScreenPositionInRawPixels = property(get_ScreenPositionInRawPixels, None)
class ScreenReaderService(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.UI.Accessibility.IScreenReaderService
    _classid_ = 'Windows.UI.Accessibility.ScreenReaderService'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Accessibility.ScreenReaderService.CreateInstance(*args))
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
    ScreenReaderPositionChanged = event()


make_ready(__name__)
