from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Microsoft.Windows.AI.MachineLearning
import win32more.Windows.ApplicationModel
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
class ExecutionProvider(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProvider
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.ExecutionProvider'
    @winrt_mixinmethod
    def get_Name(self: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_LibraryPath(self: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PackageId(self: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProvider) -> win32more.Windows.ApplicationModel.PackageId: ...
    @winrt_mixinmethod
    def get_ReadyState(self: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProvider) -> win32more.Microsoft.Windows.AI.MachineLearning.ExecutionProviderReadyState: ...
    @winrt_mixinmethod
    def get_Certification(self: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProvider) -> win32more.Microsoft.Windows.AI.MachineLearning.ExecutionProviderCertification: ...
    @winrt_mixinmethod
    def EnsureReadyAsync(self: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProvider) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.MachineLearning.ExecutionProviderReadyResult, Double]: ...
    @winrt_mixinmethod
    def TryRegister(self: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProvider) -> Boolean: ...
    Certification = property(get_Certification, None)
    LibraryPath = property(get_LibraryPath, None)
    Name = property(get_Name, None)
    PackageId = property(get_PackageId, None)
    ReadyState = property(get_ReadyState, None)
class ExecutionProviderCatalog(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProviderCatalog
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.ExecutionProviderCatalog'
    @winrt_mixinmethod
    def FindAllProviders(self: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProviderCatalog) -> ReceiveArray[win32more.Microsoft.Windows.AI.MachineLearning.ExecutionProvider]: ...
    @winrt_mixinmethod
    def EnsureAndRegisterCertifiedAsync(self: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProviderCatalog) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Windows.AI.MachineLearning.ExecutionProvider], Double]: ...
    @winrt_mixinmethod
    def RegisterCertifiedAsync(self: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProviderCatalog) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Windows.AI.MachineLearning.ExecutionProvider], Double]: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProviderCatalogStatics) -> win32more.Microsoft.Windows.AI.MachineLearning.ExecutionProviderCatalog: ...
class ExecutionProviderCertification(Enum, Int32):
    Unknown = 0
    Certified = 1
    Uncertified = 2
class ExecutionProviderReadyResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProviderReadyResult
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.ExecutionProviderReadyResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProviderReadyResult) -> win32more.Microsoft.Windows.AI.MachineLearning.ExecutionProviderReadyResultState: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProviderReadyResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_DiagnosticText(self: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProviderReadyResult) -> WinRT_String: ...
    DiagnosticText = property(get_DiagnosticText, None)
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
class ExecutionProviderReadyResultState(Enum, Int32):
    InProgress = 0
    Success = 1
    Failure = 2
class ExecutionProviderReadyState(Enum, Int32):
    Ready = 0
    NotReady = 1
    NotPresent = 2
class IExecutionProvider(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.IExecutionProvider'
    _iid_ = Guid('{98356468-cf23-504f-b29c-9347781925ff}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_LibraryPath(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_PackageId(self) -> win32more.Windows.ApplicationModel.PackageId: ...
    @winrt_commethod(9)
    def get_ReadyState(self) -> win32more.Microsoft.Windows.AI.MachineLearning.ExecutionProviderReadyState: ...
    @winrt_commethod(10)
    def get_Certification(self) -> win32more.Microsoft.Windows.AI.MachineLearning.ExecutionProviderCertification: ...
    @winrt_commethod(11)
    def EnsureReadyAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.MachineLearning.ExecutionProviderReadyResult, Double]: ...
    @winrt_commethod(12)
    def TryRegister(self) -> Boolean: ...
    Certification = property(get_Certification, None)
    LibraryPath = property(get_LibraryPath, None)
    Name = property(get_Name, None)
    PackageId = property(get_PackageId, None)
    ReadyState = property(get_ReadyState, None)
class IExecutionProviderCatalog(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.IExecutionProviderCatalog'
    _iid_ = Guid('{aa9bfe14-2222-5921-8002-4d2a205ea03c}')
    @winrt_commethod(6)
    def FindAllProviders(self) -> ReceiveArray[win32more.Microsoft.Windows.AI.MachineLearning.ExecutionProvider]: ...
    @winrt_commethod(7)
    def EnsureAndRegisterCertifiedAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Windows.AI.MachineLearning.ExecutionProvider], Double]: ...
    @winrt_commethod(8)
    def RegisterCertifiedAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Windows.AI.MachineLearning.ExecutionProvider], Double]: ...
class IExecutionProviderCatalogStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.IExecutionProviderCatalogStatics'
    _iid_ = Guid('{550def98-2611-5433-afb8-43673b610848}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Microsoft.Windows.AI.MachineLearning.ExecutionProviderCatalog: ...
class IExecutionProviderReadyResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.IExecutionProviderReadyResult'
    _iid_ = Guid('{91c1724d-93c7-5284-adbe-ba2bd7be7c79}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Microsoft.Windows.AI.MachineLearning.ExecutionProviderReadyResultState: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_DiagnosticText(self) -> WinRT_String: ...
    DiagnosticText = property(get_DiagnosticText, None)
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
MachineLearningContract: UInt32 = 131072


make_ready(__name__)
