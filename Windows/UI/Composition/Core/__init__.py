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
import Windows.UI.Composition
import Windows.UI.Composition.Core
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class CompositorController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Core.CompositorController'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Composition.Core.CompositorController: ...
    @winrt_mixinmethod
    def get_Compositor(self: Windows.UI.Composition.Core.ICompositorController) -> Windows.UI.Composition.Compositor: ...
    @winrt_mixinmethod
    def Commit(self: Windows.UI.Composition.Core.ICompositorController) -> Void: ...
    @winrt_mixinmethod
    def EnsurePreviousCommitCompletedAsync(self: Windows.UI.Composition.Core.ICompositorController) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_CommitNeeded(self: Windows.UI.Composition.Core.ICompositorController, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Composition.Core.CompositorController, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CommitNeeded(self: Windows.UI.Composition.Core.ICompositorController, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Compositor = property(get_Compositor, None)
class ICompositorController(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2d75f35a-70a7-4395-ba2d-cef0b18399f9}')
    @winrt_commethod(6)
    def get_Compositor(self) -> Windows.UI.Composition.Compositor: ...
    @winrt_commethod(7)
    def Commit(self) -> Void: ...
    @winrt_commethod(8)
    def EnsurePreviousCommitCompletedAsync(self) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def add_CommitNeeded(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Composition.Core.CompositorController, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_CommitNeeded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Compositor = property(get_Compositor, None)
make_head(_module, 'CompositorController')
make_head(_module, 'ICompositorController')
