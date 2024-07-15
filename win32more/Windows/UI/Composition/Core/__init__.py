from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.UI.Composition
import win32more.Windows.UI.Composition.Core
import win32more.Windows.Win32.System.WinRT
class CompositorController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.UI.Composition.Core.ICompositorController
    _classid_ = 'Windows.UI.Composition.Core.CompositorController'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Composition.Core.CompositorController.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
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
    CommitNeeded = event()
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
    CommitNeeded = event()


make_ready(__name__)
