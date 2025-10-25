from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.System.RemoteDesktop
class IInteractiveSessionStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.IInteractiveSessionStatics'
    _iid_ = Guid('{60884631-dd3a-4576-9c8d-e8027618bdce}')
    @winrt_commethod(6)
    def get_IsRemote(self) -> Boolean: ...
    IsRemote = property(get_IsRemote, None)
class _InteractiveSession_Meta_(ComPtr.__class__):
    pass
class InteractiveSession(ComPtr, metaclass=_InteractiveSession_Meta_):
    extends: IInspectable
    _classid_ = 'Windows.System.RemoteDesktop.InteractiveSession'
    @winrt_classmethod
    def get_IsRemote(cls: win32more.Windows.System.RemoteDesktop.IInteractiveSessionStatics) -> Boolean: ...
    _InteractiveSession_Meta_.IsRemote = property(get_IsRemote, None)


make_ready(__name__)
