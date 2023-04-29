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
import Windows.Foundation
import Windows.Gaming.UI
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class GameBar(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Gaming.UI.GameBar'
    @winrt_classmethod
    def add_VisibilityChanged(cls: Windows.Gaming.UI.IGameBarStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_VisibilityChanged(cls: Windows.Gaming.UI.IGameBarStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_IsInputRedirectedChanged(cls: Windows.Gaming.UI.IGameBarStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_IsInputRedirectedChanged(cls: Windows.Gaming.UI.IGameBarStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_Visible(cls: Windows.Gaming.UI.IGameBarStatics) -> Boolean: ...
    @winrt_classmethod
    def get_IsInputRedirected(cls: Windows.Gaming.UI.IGameBarStatics) -> Boolean: ...
    Visible = property(get_Visible, None)
    IsInputRedirected = property(get_IsInputRedirected, None)
GameChatMessageOrigin = Int32
GameChatMessageOrigin_Voice: GameChatMessageOrigin = 0
GameChatMessageOrigin_Text: GameChatMessageOrigin = 1
class GameChatOverlay(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Gaming.UI.GameChatOverlay'
    @winrt_mixinmethod
    def get_DesiredPosition(self: Windows.Gaming.UI.IGameChatOverlay) -> Windows.Gaming.UI.GameChatOverlayPosition: ...
    @winrt_mixinmethod
    def put_DesiredPosition(self: Windows.Gaming.UI.IGameChatOverlay, value: Windows.Gaming.UI.GameChatOverlayPosition) -> Void: ...
    @winrt_mixinmethod
    def AddMessage(self: Windows.Gaming.UI.IGameChatOverlay, sender: WinRT_String, message: WinRT_String, origin: Windows.Gaming.UI.GameChatMessageOrigin) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Gaming.UI.IGameChatOverlayStatics) -> Windows.Gaming.UI.GameChatOverlay: ...
    DesiredPosition = property(get_DesiredPosition, put_DesiredPosition)
GameChatOverlayPosition = Int32
GameChatOverlayPosition_BottomCenter: GameChatOverlayPosition = 0
GameChatOverlayPosition_BottomLeft: GameChatOverlayPosition = 1
GameChatOverlayPosition_BottomRight: GameChatOverlayPosition = 2
GameChatOverlayPosition_MiddleRight: GameChatOverlayPosition = 3
GameChatOverlayPosition_MiddleLeft: GameChatOverlayPosition = 4
GameChatOverlayPosition_TopCenter: GameChatOverlayPosition = 5
GameChatOverlayPosition_TopLeft: GameChatOverlayPosition = 6
GameChatOverlayPosition_TopRight: GameChatOverlayPosition = 7
class IGameBarStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('1db9a292-cc78-4173-be-45-b6-1e-67-28-3e-a7')
    @winrt_commethod(6)
    def add_VisibilityChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_VisibilityChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_IsInputRedirectedChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_IsInputRedirectedChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def get_Visible(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsInputRedirected(self) -> Boolean: ...
    Visible = property(get_Visible, None)
    IsInputRedirected = property(get_IsInputRedirected, None)
class IGameChatOverlay(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fbc64865-f6fc-4a48-ae-07-03-ac-6e-d4-37-04')
    @winrt_commethod(6)
    def get_DesiredPosition(self) -> Windows.Gaming.UI.GameChatOverlayPosition: ...
    @winrt_commethod(7)
    def put_DesiredPosition(self, value: Windows.Gaming.UI.GameChatOverlayPosition) -> Void: ...
    @winrt_commethod(8)
    def AddMessage(self, sender: WinRT_String, message: WinRT_String, origin: Windows.Gaming.UI.GameChatMessageOrigin) -> Void: ...
    DesiredPosition = property(get_DesiredPosition, put_DesiredPosition)
class IGameChatOverlayStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('89acf614-7867-49f7-96-87-25-d9-db-f4-44-d1')
    @winrt_commethod(6)
    def GetDefault(self) -> Windows.Gaming.UI.GameChatOverlay: ...
make_head(_module, 'GameBar')
make_head(_module, 'GameChatOverlay')
make_head(_module, 'IGameBarStatics')
make_head(_module, 'IGameChatOverlay')
make_head(_module, 'IGameChatOverlayStatics')
