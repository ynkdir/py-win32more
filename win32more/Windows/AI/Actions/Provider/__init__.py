from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.AI.Actions
import win32more.Windows.AI.Actions.Provider
import win32more.Windows.Foundation
class IActionFeedbackHandler(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.Provider.IActionFeedbackHandler'
    _iid_ = Guid('{a3fc3c51-a8c6-52c8-ad77-37bf3e2b565c}')
    @winrt_commethod(6)
    def ProcessFeedbackAsync(self, context: win32more.Windows.AI.Actions.ActionInvocationContext, feedback: win32more.Windows.AI.Actions.ActionFeedback) -> win32more.Windows.Foundation.IAsyncAction: ...
class IActionProvider(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.AI.Actions.Provider.IActionProvider'
    _iid_ = Guid('{62906c47-3d07-55f1-aefa-1522505afbbe}')
    @winrt_commethod(6)
    def InvokeAsync(self, context: win32more.Windows.AI.Actions.ActionInvocationContext) -> win32more.Windows.Foundation.IAsyncAction: ...


make_ready(__name__)
