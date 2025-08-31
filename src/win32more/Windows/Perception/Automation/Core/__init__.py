from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Foundation
import win32more.Windows.Perception.Automation.Core
class CorePerceptionAutomation(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Perception.Automation.Core.CorePerceptionAutomation'
    @winrt_classmethod
    def SetActivationFactoryProvider(cls: win32more.Windows.Perception.Automation.Core.ICorePerceptionAutomationStatics, provider: win32more.Windows.Foundation.IGetActivationFactory) -> Void: ...
class ICorePerceptionAutomationStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Perception.Automation.Core.ICorePerceptionAutomationStatics'
    _iid_ = Guid('{0bb04541-4ce2-4923-9a76-8187ecc59112}')
    @winrt_commethod(6)
    def SetActivationFactoryProvider(self, provider: win32more.Windows.Foundation.IGetActivationFactory) -> Void: ...
PerceptionAutomationCoreContract: UInt32 = 65536


make_ready(__name__)
