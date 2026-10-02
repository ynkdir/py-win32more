from __future__ import annotations
from win32more._prelude import *
import win32more.Microsoft.Windows.AI
import win32more.Windows.Foundation
class AICapabilities(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.AICapabilities'
    @winrt_classmethod
    def HasAICapability(cls: win32more.Microsoft.Windows.AI.IAICapabilitiesStatics, category: win32more.Microsoft.Windows.AI.AICapabilityCategory) -> Boolean: ...
class AICapabilityCategory(Enum, Int32):
    _name_ = 'Microsoft.Windows.AI.AICapabilityCategory'
    CopilotPlusPC = 0
AIFeatureReadyContract: UInt32 = 262144
class AIFeatureReadyResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.IAIFeatureReadyResult
    _classid_ = 'Microsoft.Windows.AI.AIFeatureReadyResult'
    @winrt_mixinmethod
    def get_Error(self: win32more.Microsoft.Windows.AI.IAIFeatureReadyResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_ErrorDisplayText(self: win32more.Microsoft.Windows.AI.IAIFeatureReadyResult) -> hstr: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Microsoft.Windows.AI.IAIFeatureReadyResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.Windows.AI.IAIFeatureReadyResult) -> win32more.Microsoft.Windows.AI.AIFeatureReadyResultState: ...
    @winrt_mixinmethod
    def get_PackageInstallationFailed(self: win32more.Microsoft.Windows.AI.IAIFeatureReadyResult2) -> Boolean: ...
    Error = property(get_Error, None)
    ErrorDisplayText = property(get_ErrorDisplayText, None)
    ExtendedError = property(get_ExtendedError, None)
    PackageInstallationFailed = property(get_PackageInstallationFailed, None)
    Status = property(get_Status, None)
class AIFeatureReadyResultState(Enum, Int32):
    _name_ = 'Microsoft.Windows.AI.AIFeatureReadyResultState'
    InProgress = 0
    Success = 1
    Failure = 2
class AIFeatureReadyState(Enum, Int32):
    _name_ = 'Microsoft.Windows.AI.AIFeatureReadyState'
    Ready = 0
    NotReady = 1
    NotSupportedOnCurrentSystem = 2
    DisabledByUser = 3
class IAICapabilitiesStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.IAICapabilitiesStatics'
    _iid_ = Guid('{37968861-98ee-599c-aa38-aa79866d6ddc}')
    @winrt_commethod(6)
    def HasAICapability(self, category: win32more.Microsoft.Windows.AI.AICapabilityCategory) -> Boolean: ...
class IAIFeatureReadyResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.IAIFeatureReadyResult'
    _iid_ = Guid('{936a78a6-c242-5937-9814-e512d4193a6d}')
    @winrt_commethod(6)
    def get_Error(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(7)
    def get_ErrorDisplayText(self) -> hstr: ...
    @winrt_commethod(8)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(9)
    def get_Status(self) -> win32more.Microsoft.Windows.AI.AIFeatureReadyResultState: ...
    Error = property(get_Error, None)
    ErrorDisplayText = property(get_ErrorDisplayText, None)
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
class IAIFeatureReadyResult2(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.IAIFeatureReadyResult2'
    _iid_ = Guid('{ec5f1d67-43c1-5bdb-b9f4-a0c7110582cb}')
    @winrt_commethod(6)
    def get_PackageInstallationFailed(self) -> Boolean: ...
    PackageInstallationFailed = property(get_PackageInstallationFailed, None)


make_ready(__name__)
