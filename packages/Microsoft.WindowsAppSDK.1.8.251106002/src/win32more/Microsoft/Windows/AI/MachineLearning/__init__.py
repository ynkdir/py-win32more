from __future__ import annotations
from win32more._prelude import *
import win32more.Microsoft.Windows.AI.MachineLearning
import win32more.Windows.ApplicationModel
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
class CatalogModelInfo(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInfo
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.CatalogModelInfo'
    @winrt_mixinmethod
    def get_Id(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInfo) -> hstr: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInfo) -> hstr: ...
    @winrt_mixinmethod
    def get_Publisher(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInfo) -> hstr: ...
    @winrt_mixinmethod
    def get_SourceId(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInfo) -> hstr: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInfo) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_ExecutionProviders(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInfo) -> win32more.Windows.Foundation.Collections.IVectorView[hstr]: ...
    @winrt_mixinmethod
    def get_ModelSizeInBytes(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInfo) -> UInt64: ...
    @winrt_mixinmethod
    def get_Version(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInfo) -> hstr: ...
    @winrt_mixinmethod
    def get_License(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInfo) -> hstr: ...
    @winrt_mixinmethod
    def get_LicenseUri(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInfo) -> hstr: ...
    @winrt_mixinmethod
    def get_LicenseText(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInfo) -> hstr: ...
    @winrt_mixinmethod
    def GetStatus(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInfo) -> win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelStatus: ...
    @winrt_mixinmethod
    def GetInstanceAsync(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInfo) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelInstanceResult, Double]: ...
    @winrt_mixinmethod
    def GetInstanceAsync2(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInfo, additionalHeaders: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[hstr, hstr]]) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelInstanceResult, Double]: ...
    ExecutionProviders = property(get_ExecutionProviders, None)
    Id = property(get_Id, None)
    License = property(get_License, None)
    LicenseText = property(get_LicenseText, None)
    LicenseUri = property(get_LicenseUri, None)
    ModelSizeInBytes = property(get_ModelSizeInBytes, None)
    Name = property(get_Name, None)
    Publisher = property(get_Publisher, None)
    SourceId = property(get_SourceId, None)
    Uri = property(get_Uri, None)
    Version = property(get_Version, None)
class CatalogModelInstance(ComPtr):
    extends: IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInstance
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.CatalogModelInstance'
    @winrt_mixinmethod
    def get_ModelPaths(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInstance) -> win32more.Windows.Foundation.Collections.IVectorView[hstr]: ...
    @winrt_mixinmethod
    def get_ModelInfo(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInstance) -> win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelInfo: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    ModelInfo = property(get_ModelInfo, None)
    ModelPaths = property(get_ModelPaths, None)
class CatalogModelInstanceResult(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInstanceResult
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.CatalogModelInstanceResult'
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInstanceResult) -> win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelInstanceStatus: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInstanceResult) -> win32more.Windows.Foundation.HResult: ...
    @winrt_mixinmethod
    def get_DiagnosticText(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInstanceResult) -> hstr: ...
    @winrt_mixinmethod
    def GetInstance(self: win32more.Microsoft.Windows.AI.MachineLearning.ICatalogModelInstanceResult) -> win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelInstance: ...
    DiagnosticText = property(get_DiagnosticText, None)
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
class CatalogModelInstanceStatus(Enum, Int32):
    Available = 0
    InProgress = 1
    Unavailable = 2
class CatalogModelStatus(Enum, Int32):
    Ready = 0
    NotReady = 1
class ExecutionProvider(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProvider
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.ExecutionProvider'
    @winrt_mixinmethod
    def get_Name(self: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProvider) -> hstr: ...
    @winrt_mixinmethod
    def get_LibraryPath(self: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProvider) -> hstr: ...
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
    def get_DiagnosticText(self: win32more.Microsoft.Windows.AI.MachineLearning.IExecutionProviderReadyResult) -> hstr: ...
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
class ICatalogModelInfo(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.ICatalogModelInfo'
    _iid_ = Guid('{62057faa-3def-509f-9ed2-aef1e0de21a4}')
    @winrt_commethod(6)
    def get_Id(self) -> hstr: ...
    @winrt_commethod(7)
    def get_Name(self) -> hstr: ...
    @winrt_commethod(8)
    def get_Publisher(self) -> hstr: ...
    @winrt_commethod(9)
    def get_SourceId(self) -> hstr: ...
    @winrt_commethod(10)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(11)
    def get_ExecutionProviders(self) -> win32more.Windows.Foundation.Collections.IVectorView[hstr]: ...
    @winrt_commethod(12)
    def get_ModelSizeInBytes(self) -> UInt64: ...
    @winrt_commethod(13)
    def get_Version(self) -> hstr: ...
    @winrt_commethod(14)
    def get_License(self) -> hstr: ...
    @winrt_commethod(15)
    def get_LicenseUri(self) -> hstr: ...
    @winrt_commethod(16)
    def get_LicenseText(self) -> hstr: ...
    @winrt_commethod(17)
    def GetStatus(self) -> win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelStatus: ...
    @winrt_commethod(18)
    def GetInstanceAsync(self) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelInstanceResult, Double]: ...
    @winrt_commethod(19)
    def GetInstanceAsync2(self, additionalHeaders: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[hstr, hstr]]) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelInstanceResult, Double]: ...
    ExecutionProviders = property(get_ExecutionProviders, None)
    Id = property(get_Id, None)
    License = property(get_License, None)
    LicenseText = property(get_LicenseText, None)
    LicenseUri = property(get_LicenseUri, None)
    ModelSizeInBytes = property(get_ModelSizeInBytes, None)
    Name = property(get_Name, None)
    Publisher = property(get_Publisher, None)
    SourceId = property(get_SourceId, None)
    Uri = property(get_Uri, None)
    Version = property(get_Version, None)
class ICatalogModelInstance(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.ICatalogModelInstance'
    _iid_ = Guid('{9e920521-5e06-5c30-b0c2-8af313efb756}')
    @winrt_commethod(6)
    def get_ModelPaths(self) -> win32more.Windows.Foundation.Collections.IVectorView[hstr]: ...
    @winrt_commethod(7)
    def get_ModelInfo(self) -> win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelInfo: ...
    ModelInfo = property(get_ModelInfo, None)
    ModelPaths = property(get_ModelPaths, None)
class ICatalogModelInstanceResult(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.ICatalogModelInstanceResult'
    _iid_ = Guid('{b3701b71-61fa-5185-a2ce-8df6e6a5c66d}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelInstanceStatus: ...
    @winrt_commethod(7)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    @winrt_commethod(8)
    def get_DiagnosticText(self) -> hstr: ...
    @winrt_commethod(9)
    def GetInstance(self) -> win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelInstance: ...
    DiagnosticText = property(get_DiagnosticText, None)
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
class IExecutionProvider(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.IExecutionProvider'
    _iid_ = Guid('{98356468-cf23-504f-b29c-9347781925ff}')
    @winrt_commethod(6)
    def get_Name(self) -> hstr: ...
    @winrt_commethod(7)
    def get_LibraryPath(self) -> hstr: ...
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
    def get_DiagnosticText(self) -> hstr: ...
    DiagnosticText = property(get_DiagnosticText, None)
    ExtendedError = property(get_ExtendedError, None)
    Status = property(get_Status, None)
class IModelCatalog(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.IModelCatalog'
    _iid_ = Guid('{8cae018c-49f5-5080-abb8-ef4a1df356da}')
    @winrt_commethod(6)
    def get_Sources(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Windows.AI.MachineLearning.ModelCatalogSource]: ...
    @winrt_commethod(7)
    def get_ExecutionProviders(self) -> win32more.Windows.Foundation.Collections.IVector[hstr]: ...
    @winrt_commethod(8)
    def GetAvailableModel(self, idOrName: hstr) -> win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelInfo: ...
    @winrt_commethod(9)
    def GetAvailableModels(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelInfo]: ...
    @winrt_commethod(10)
    def FindModelAsync(self, idOrName: hstr) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelInfo]: ...
    @winrt_commethod(11)
    def FindAllModelsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelInfo]]: ...
    ExecutionProviders = property(get_ExecutionProviders, None)
    Sources = property(get_Sources, None)
class IModelCatalogFactory(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.IModelCatalogFactory'
    _iid_ = Guid('{2942d7bd-6243-511f-a12c-42cb151b625f}')
    @winrt_commethod(6)
    def CreateInstance(self, sources: PassArray[win32more.Microsoft.Windows.AI.MachineLearning.ModelCatalogSource]) -> win32more.Microsoft.Windows.AI.MachineLearning.ModelCatalog: ...
class IModelCatalogSource(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.IModelCatalogSource'
    _iid_ = Guid('{3117952c-8dc3-54c9-94fa-bf6f38cbfce9}')
    @winrt_commethod(6)
    def get_Id(self) -> hstr: ...
    @winrt_commethod(7)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    Id = property(get_Id, None)
    Uri = property(get_Uri, None)
class IModelCatalogSourceStatics(ComPtr):
    extends: IInspectable
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.IModelCatalogSourceStatics'
    _iid_ = Guid('{deba0a9b-6eda-571a-9a05-5a7e2a0531ef}')
    @winrt_commethod(6)
    def CreateFromUriAsync(self, location: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.MachineLearning.ModelCatalogSource]: ...
    @winrt_commethod(7)
    def CreateFromUriAsync2(self, location: win32more.Windows.Foundation.Uri, additionalHeaders: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[hstr, hstr]]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.MachineLearning.ModelCatalogSource]: ...
MachineLearningContract: UInt32 = 131072
class ModelCatalog(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.MachineLearning.IModelCatalog
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.ModelCatalog'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Windows.AI.MachineLearning.ModelCatalog.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Windows.AI.MachineLearning.IModelCatalogFactory, sources: PassArray[win32more.Microsoft.Windows.AI.MachineLearning.ModelCatalogSource]) -> win32more.Microsoft.Windows.AI.MachineLearning.ModelCatalog: ...
    @winrt_mixinmethod
    def get_Sources(self: win32more.Microsoft.Windows.AI.MachineLearning.IModelCatalog) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Windows.AI.MachineLearning.ModelCatalogSource]: ...
    @winrt_mixinmethod
    def get_ExecutionProviders(self: win32more.Microsoft.Windows.AI.MachineLearning.IModelCatalog) -> win32more.Windows.Foundation.Collections.IVector[hstr]: ...
    @winrt_mixinmethod
    def GetAvailableModel(self: win32more.Microsoft.Windows.AI.MachineLearning.IModelCatalog, idOrName: hstr) -> win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelInfo: ...
    @winrt_mixinmethod
    def GetAvailableModels(self: win32more.Microsoft.Windows.AI.MachineLearning.IModelCatalog) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelInfo]: ...
    @winrt_mixinmethod
    def FindModelAsync(self: win32more.Microsoft.Windows.AI.MachineLearning.IModelCatalog, idOrName: hstr) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelInfo]: ...
    @winrt_mixinmethod
    def FindAllModelsAsync(self: win32more.Microsoft.Windows.AI.MachineLearning.IModelCatalog) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Windows.AI.MachineLearning.CatalogModelInfo]]: ...
    ExecutionProviders = property(get_ExecutionProviders, None)
    Sources = property(get_Sources, None)
class ModelCatalogSource(ComPtr):
    extends: IInspectable
    default_interface: win32more.Microsoft.Windows.AI.MachineLearning.IModelCatalogSource
    _classid_ = 'Microsoft.Windows.AI.MachineLearning.ModelCatalogSource'
    @winrt_mixinmethod
    def get_Id(self: win32more.Microsoft.Windows.AI.MachineLearning.IModelCatalogSource) -> hstr: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Microsoft.Windows.AI.MachineLearning.IModelCatalogSource) -> win32more.Windows.Foundation.Uri: ...
    @winrt_classmethod
    def CreateFromUriAsync(cls: win32more.Microsoft.Windows.AI.MachineLearning.IModelCatalogSourceStatics, location: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.MachineLearning.ModelCatalogSource]: ...
    @winrt_classmethod
    def CreateFromUriAsync2(cls: win32more.Microsoft.Windows.AI.MachineLearning.IModelCatalogSourceStatics, location: win32more.Windows.Foundation.Uri, additionalHeaders: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[hstr, hstr]]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Windows.AI.MachineLearning.ModelCatalogSource]: ...
    Id = property(get_Id, None)
    Uri = property(get_Uri, None)


make_ready(__name__)
