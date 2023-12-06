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
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.UI.Composition
import win32more.Windows.UI.Composition.Core
class CompositorController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Composition.Core.ICompositorController
    _classid_ = 'Windows.UI.Composition.Core.CompositorController'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.UI.Composition.Core.CompositorController.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Composition.Core.CompositorController: ...
    @winrt_mixinmethod
    def get_Compositor(self: win32more.Windows.UI.Composition.Core.ICompositorController) -> win32more.Windows.UI.Composition.Compositor: ...
    @winrt_mixinmethod
    def Commit(self: win32more.Windows.UI.Composition.Core.ICompositorController) -> Void: ...
    @winrt_mixinmethod
    def EnsurePreviousCommitCompletedAsync(self: win32more.Windows.UI.Composition.Core.ICompositorController) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_CommitNeeded(self: win32more.Windows.UI.Composition.Core.ICompositorController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Composition.Core.CompositorController, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CommitNeeded(self: win32more.Windows.UI.Composition.Core.ICompositorController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Compositor = property(get_Compositor, None)
class ICompositorController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Composition.Core.ICompositorController'
    _iid_ = Guid('{2d75f35a-70a7-4395-ba2d-cef0b18399f9}')
    @winrt_commethod(6)
    def get_Compositor(self) -> win32more.Windows.UI.Composition.Compositor: ...
    @winrt_commethod(7)
    def Commit(self) -> Void: ...
    @winrt_commethod(8)
    def EnsurePreviousCommitCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def add_CommitNeeded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Composition.Core.CompositorController, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_CommitNeeded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Compositor = property(get_Compositor, None)
make_ready(__name__)
