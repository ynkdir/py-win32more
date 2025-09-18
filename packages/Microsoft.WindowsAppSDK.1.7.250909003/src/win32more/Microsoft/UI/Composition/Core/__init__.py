from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Microsoft.UI.Composition
import win32more.Microsoft.UI.Composition.Core
import win32more.Windows.Foundation
class CompositorController(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.UI.Composition.Core.ICompositorController
    _classid_ = 'Microsoft.UI.Composition.Core.CompositorController'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Composition.Core.CompositorController.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Composition.Core.CompositorController: ...
    @winrt_mixinmethod
    def get_Compositor(self: win32more.Microsoft.UI.Composition.Core.ICompositorController) -> win32more.Microsoft.UI.Composition.Compositor: ...
    @winrt_mixinmethod
    def Commit(self: win32more.Microsoft.UI.Composition.Core.ICompositorController) -> Void: ...
    @winrt_mixinmethod
    def EnsurePreviousCommitCompletedAsync(self: win32more.Microsoft.UI.Composition.Core.ICompositorController) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def add_CommitNeeded(self: win32more.Microsoft.UI.Composition.Core.ICompositorController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Composition.Core.CompositorController, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CommitNeeded(self: win32more.Microsoft.UI.Composition.Core.ICompositorController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Compositor = property(get_Compositor, None)
    CommitNeeded = event()
class ICompositorController(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.UI.Composition.Core.ICompositorController'
    _iid_ = Guid('{cc107cdc-558f-5d1a-96a5-a735ac04386b}')
    @winrt_commethod(6)
    def get_Compositor(self) -> win32more.Microsoft.UI.Composition.Compositor: ...
    @winrt_commethod(7)
    def Commit(self) -> Void: ...
    @winrt_commethod(8)
    def EnsurePreviousCommitCompletedAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(9)
    def add_CommitNeeded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Composition.Core.CompositorController, IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_CommitNeeded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Compositor = property(get_Compositor, None)
    CommitNeeded = event()


make_ready(__name__)
