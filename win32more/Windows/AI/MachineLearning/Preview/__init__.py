from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.AI.MachineLearning.Preview
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics.Imaging
import win32more.Windows.Storage
import win32more.Windows.Storage.Streams
import win32more.Windows.Win32.System.WinRT
class FeatureElementKindPreview(Enum, Int32):
    Undefined = 0
    Float = 1
    UInt8 = 2
    Int8 = 3
    UInt16 = 4
    Int16 = 5
    Int32 = 6
    Int64 = 7
    String = 8
    Boolean = 9
    Float16 = 10
    Double = 11
    UInt32 = 12
    UInt64 = 13
    Complex64 = 14
    Complex128 = 15
class IImageVariableDescriptorPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.Preview.IImageVariableDescriptorPreview'
    _iid_ = Guid('{7ae1fa72-029e-4dc5-a2f8-5fb763154150}')
    @winrt_commethod(6)
    def get_BitmapPixelFormat(self) -> win32more.Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_commethod(7)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Height(self) -> UInt32: ...
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    Height = property(get_Height, None)
    Width = property(get_Width, None)
class IInferencingOptionsPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview'
    _iid_ = Guid('{47bc8205-4d36-47a9-8f68-ffcb339dd0fc}')
    @winrt_commethod(6)
    def get_PreferredDeviceKind(self) -> win32more.Windows.AI.MachineLearning.Preview.LearningModelDeviceKindPreview: ...
    @winrt_commethod(7)
    def put_PreferredDeviceKind(self, value: win32more.Windows.AI.MachineLearning.Preview.LearningModelDeviceKindPreview) -> Void: ...
    @winrt_commethod(8)
    def get_IsTracingEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsTracingEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_MaxBatchSize(self) -> Int32: ...
    @winrt_commethod(11)
    def put_MaxBatchSize(self, value: Int32) -> Void: ...
    @winrt_commethod(12)
    def get_MinimizeMemoryAllocation(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_MinimizeMemoryAllocation(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_ReclaimMemoryAfterEvaluation(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_ReclaimMemoryAfterEvaluation(self, value: Boolean) -> Void: ...
    IsTracingEnabled = property(get_IsTracingEnabled, put_IsTracingEnabled)
    MaxBatchSize = property(get_MaxBatchSize, put_MaxBatchSize)
    MinimizeMemoryAllocation = property(get_MinimizeMemoryAllocation, put_MinimizeMemoryAllocation)
    PreferredDeviceKind = property(get_PreferredDeviceKind, put_PreferredDeviceKind)
    ReclaimMemoryAfterEvaluation = property(get_ReclaimMemoryAfterEvaluation, put_ReclaimMemoryAfterEvaluation)
class ILearningModelBindingPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[MappingProtocol[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]
    _classid_ = 'Windows.AI.MachineLearning.Preview.ILearningModelBindingPreview'
    _iid_ = Guid('{93c901e8-6c78-4b4f-aec1-a6bb9e691624}')
    @winrt_commethod(6)
    def Bind(self, name: WinRT_String, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(7)
    def BindWithProperties(self, name: WinRT_String, value: win32more.Windows.Win32.System.WinRT.IInspectable, metadata: win32more.Windows.Foundation.Collections.IPropertySet) -> Void: ...
    @winrt_commethod(8)
    def Clear(self) -> Void: ...
class ILearningModelBindingPreviewFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.Preview.ILearningModelBindingPreviewFactory'
    _iid_ = Guid('{48b8219f-1e51-4d77-ae50-3ec164ad3480}')
    @winrt_commethod(6)
    def CreateFromModel(self, model: win32more.Windows.AI.MachineLearning.Preview.LearningModelPreview) -> win32more.Windows.AI.MachineLearning.Preview.LearningModelBindingPreview: ...
class ILearningModelDescriptionPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.Preview.ILearningModelDescriptionPreview'
    _iid_ = Guid('{f52c09c6-8611-40ad-8e59-de3fd7030a40}')
    @winrt_commethod(6)
    def get_Author(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Domain(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Version(self) -> Int64: ...
    @winrt_commethod(11)
    def get_Metadata(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_commethod(12)
    def get_InputFeatures(self) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview]: ...
    @winrt_commethod(13)
    def get_OutputFeatures(self) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview]: ...
    Author = property(get_Author, None)
    Description = property(get_Description, None)
    Domain = property(get_Domain, None)
    InputFeatures = property(get_InputFeatures, None)
    Metadata = property(get_Metadata, None)
    Name = property(get_Name, None)
    OutputFeatures = property(get_OutputFeatures, None)
    Version = property(get_Version, None)
class ILearningModelEvaluationResultPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.Preview.ILearningModelEvaluationResultPreview'
    _iid_ = Guid('{df25ea9f-9863-4088-8498-87a1f4686f92}')
    @winrt_commethod(6)
    def get_CorrelationId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Outputs(self) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    CorrelationId = property(get_CorrelationId, None)
    Outputs = property(get_Outputs, None)
class ILearningModelPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.Preview.ILearningModelPreview'
    _iid_ = Guid('{049c266a-93b4-478c-aeb8-70157bf0ff94}')
    @winrt_commethod(6)
    def EvaluateAsync(self, binding: win32more.Windows.AI.MachineLearning.Preview.LearningModelBindingPreview, correlationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.Preview.LearningModelEvaluationResultPreview]: ...
    @winrt_commethod(7)
    def EvaluateFeaturesAsync(self, features: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], correlationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.Preview.LearningModelEvaluationResultPreview]: ...
    @winrt_commethod(8)
    def get_Description(self) -> win32more.Windows.AI.MachineLearning.Preview.LearningModelDescriptionPreview: ...
    @winrt_commethod(9)
    def get_InferencingOptions(self) -> win32more.Windows.AI.MachineLearning.Preview.InferencingOptionsPreview: ...
    @winrt_commethod(10)
    def put_InferencingOptions(self, value: win32more.Windows.AI.MachineLearning.Preview.InferencingOptionsPreview) -> Void: ...
    Description = property(get_Description, None)
    InferencingOptions = property(get_InferencingOptions, put_InferencingOptions)
class ILearningModelPreviewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.Preview.ILearningModelPreviewStatics'
    _iid_ = Guid('{164bbb60-8465-4786-8b93-2c16a89289d7}')
    @winrt_commethod(6)
    def LoadModelFromStorageFileAsync(self, modelFile: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.Preview.LearningModelPreview]: ...
    @winrt_commethod(7)
    def LoadModelFromStreamAsync(self, modelStream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.Preview.LearningModelPreview]: ...
class ILearningModelVariableDescriptorPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview'
    _iid_ = Guid('{b13df682-fc30-492b-8ea0-ed1f53c0b038}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ModelFeatureKind(self) -> win32more.Windows.AI.MachineLearning.Preview.LearningModelFeatureKindPreview: ...
    @winrt_commethod(9)
    def get_IsRequired(self) -> Boolean: ...
    Description = property(get_Description, None)
    IsRequired = property(get_IsRequired, None)
    ModelFeatureKind = property(get_ModelFeatureKind, None)
    Name = property(get_Name, None)
class IMapVariableDescriptorPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.Preview.IMapVariableDescriptorPreview'
    _iid_ = Guid('{3cb38370-c02b-4236-b3e8-6bdca49c3129}')
    @winrt_commethod(6)
    def get_KeyKind(self) -> win32more.Windows.AI.MachineLearning.Preview.FeatureElementKindPreview: ...
    @winrt_commethod(7)
    def get_ValidStringKeys(self) -> win32more.Windows.Foundation.Collections.IIterable[WinRT_String]: ...
    @winrt_commethod(8)
    def get_ValidIntegerKeys(self) -> win32more.Windows.Foundation.Collections.IIterable[Int64]: ...
    @winrt_commethod(9)
    def get_Fields(self) -> win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview: ...
    Fields = property(get_Fields, None)
    KeyKind = property(get_KeyKind, None)
    ValidIntegerKeys = property(get_ValidIntegerKeys, None)
    ValidStringKeys = property(get_ValidStringKeys, None)
class ISequenceVariableDescriptorPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.Preview.ISequenceVariableDescriptorPreview'
    _iid_ = Guid('{9cd8f292-98b2-4530-a1b6-2ded5fecbc26}')
    @winrt_commethod(6)
    def get_ElementType(self) -> win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview: ...
    ElementType = property(get_ElementType, None)
class ITensorVariableDescriptorPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.AI.MachineLearning.Preview.ITensorVariableDescriptorPreview'
    _iid_ = Guid('{a80f501a-9aac-4233-9784-aceaf92510b5}')
    @winrt_commethod(6)
    def get_DataType(self) -> win32more.Windows.AI.MachineLearning.Preview.FeatureElementKindPreview: ...
    @winrt_commethod(7)
    def get_Shape(self) -> win32more.Windows.Foundation.Collections.IIterable[Int64]: ...
    DataType = property(get_DataType, None)
    Shape = property(get_Shape, None)
class ImageVariableDescriptorPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.AI.MachineLearning.Preview.IImageVariableDescriptorPreview
    _classid_ = 'Windows.AI.MachineLearning.Preview.ImageVariableDescriptorPreview'
    @winrt_mixinmethod
    def get_BitmapPixelFormat(self: win32more.Windows.AI.MachineLearning.Preview.IImageVariableDescriptorPreview) -> win32more.Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_mixinmethod
    def get_Width(self: win32more.Windows.AI.MachineLearning.Preview.IImageVariableDescriptorPreview) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: win32more.Windows.AI.MachineLearning.Preview.IImageVariableDescriptorPreview) -> UInt32: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ModelFeatureKind(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> win32more.Windows.AI.MachineLearning.Preview.LearningModelFeatureKindPreview: ...
    @winrt_mixinmethod
    def get_IsRequired(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> Boolean: ...
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    Description = property(get_Description, None)
    Height = property(get_Height, None)
    IsRequired = property(get_IsRequired, None)
    ModelFeatureKind = property(get_ModelFeatureKind, None)
    Name = property(get_Name, None)
    Width = property(get_Width, None)
class InferencingOptionsPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview
    _classid_ = 'Windows.AI.MachineLearning.Preview.InferencingOptionsPreview'
    @winrt_mixinmethod
    def get_PreferredDeviceKind(self: win32more.Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview) -> win32more.Windows.AI.MachineLearning.Preview.LearningModelDeviceKindPreview: ...
    @winrt_mixinmethod
    def put_PreferredDeviceKind(self: win32more.Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview, value: win32more.Windows.AI.MachineLearning.Preview.LearningModelDeviceKindPreview) -> Void: ...
    @winrt_mixinmethod
    def get_IsTracingEnabled(self: win32more.Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsTracingEnabled(self: win32more.Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MaxBatchSize(self: win32more.Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview) -> Int32: ...
    @winrt_mixinmethod
    def put_MaxBatchSize(self: win32more.Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_MinimizeMemoryAllocation(self: win32more.Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview) -> Boolean: ...
    @winrt_mixinmethod
    def put_MinimizeMemoryAllocation(self: win32more.Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ReclaimMemoryAfterEvaluation(self: win32more.Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview) -> Boolean: ...
    @winrt_mixinmethod
    def put_ReclaimMemoryAfterEvaluation(self: win32more.Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview, value: Boolean) -> Void: ...
    IsTracingEnabled = property(get_IsTracingEnabled, put_IsTracingEnabled)
    MaxBatchSize = property(get_MaxBatchSize, put_MaxBatchSize)
    MinimizeMemoryAllocation = property(get_MinimizeMemoryAllocation, put_MinimizeMemoryAllocation)
    PreferredDeviceKind = property(get_PreferredDeviceKind, put_PreferredDeviceKind)
    ReclaimMemoryAfterEvaluation = property(get_ReclaimMemoryAfterEvaluation, put_ReclaimMemoryAfterEvaluation)
class LearningModelBindingPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[MappingProtocol[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]
    default_interface: win32more.Windows.AI.MachineLearning.Preview.ILearningModelBindingPreview
    _classid_ = 'Windows.AI.MachineLearning.Preview.LearningModelBindingPreview'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.AI.MachineLearning.Preview.LearningModelBindingPreview.CreateFromModel(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateFromModel(cls: win32more.Windows.AI.MachineLearning.Preview.ILearningModelBindingPreviewFactory, model: win32more.Windows.AI.MachineLearning.Preview.LearningModelPreview) -> win32more.Windows.AI.MachineLearning.Preview.LearningModelBindingPreview: ...
    @winrt_mixinmethod
    def Bind(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelBindingPreview, name: WinRT_String, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def BindWithProperties(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelBindingPreview, name: WinRT_String, value: win32more.Windows.Win32.System.WinRT.IInspectable, metadata: win32more.Windows.Foundation.Collections.IPropertySet) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelBindingPreview) -> Void: ...
    @winrt_mixinmethod
    def Lookup(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Split(self: win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], first: POINTER(win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]), second: POINTER(win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable])) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]]: ...
    Size = property(get_Size, None)
class LearningModelDescriptionPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.AI.MachineLearning.Preview.ILearningModelDescriptionPreview
    _classid_ = 'Windows.AI.MachineLearning.Preview.LearningModelDescriptionPreview'
    @winrt_mixinmethod
    def get_Author(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelDescriptionPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelDescriptionPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Domain(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelDescriptionPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelDescriptionPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Version(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelDescriptionPreview) -> Int64: ...
    @winrt_mixinmethod
    def get_Metadata(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelDescriptionPreview) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_InputFeatures(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelDescriptionPreview) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview]: ...
    @winrt_mixinmethod
    def get_OutputFeatures(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelDescriptionPreview) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview]: ...
    Author = property(get_Author, None)
    Description = property(get_Description, None)
    Domain = property(get_Domain, None)
    InputFeatures = property(get_InputFeatures, None)
    Metadata = property(get_Metadata, None)
    Name = property(get_Name, None)
    OutputFeatures = property(get_OutputFeatures, None)
    Version = property(get_Version, None)
class LearningModelDeviceKindPreview(Enum, Int32):
    LearningDeviceAny = 0
    LearningDeviceCpu = 1
    LearningDeviceGpu = 2
    LearningDeviceNpu = 3
    LearningDeviceDsp = 4
    LearningDeviceFpga = 5
class LearningModelEvaluationResultPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.AI.MachineLearning.Preview.ILearningModelEvaluationResultPreview
    _classid_ = 'Windows.AI.MachineLearning.Preview.LearningModelEvaluationResultPreview'
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelEvaluationResultPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Outputs(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelEvaluationResultPreview) -> win32more.Windows.Foundation.Collections.IMapView[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    CorrelationId = property(get_CorrelationId, None)
    Outputs = property(get_Outputs, None)
class LearningModelFeatureKindPreview(Enum, Int32):
    Undefined = 0
    Tensor = 1
    Sequence = 2
    Map = 3
    Image = 4
class LearningModelPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.AI.MachineLearning.Preview.ILearningModelPreview
    _classid_ = 'Windows.AI.MachineLearning.Preview.LearningModelPreview'
    @winrt_mixinmethod
    def EvaluateAsync(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelPreview, binding: win32more.Windows.AI.MachineLearning.Preview.LearningModelBindingPreview, correlationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.Preview.LearningModelEvaluationResultPreview]: ...
    @winrt_mixinmethod
    def EvaluateFeaturesAsync(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelPreview, features: win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable], correlationId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.Preview.LearningModelEvaluationResultPreview]: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelPreview) -> win32more.Windows.AI.MachineLearning.Preview.LearningModelDescriptionPreview: ...
    @winrt_mixinmethod
    def get_InferencingOptions(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelPreview) -> win32more.Windows.AI.MachineLearning.Preview.InferencingOptionsPreview: ...
    @winrt_mixinmethod
    def put_InferencingOptions(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelPreview, value: win32more.Windows.AI.MachineLearning.Preview.InferencingOptionsPreview) -> Void: ...
    @winrt_classmethod
    def LoadModelFromStorageFileAsync(cls: win32more.Windows.AI.MachineLearning.Preview.ILearningModelPreviewStatics, modelFile: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.Preview.LearningModelPreview]: ...
    @winrt_classmethod
    def LoadModelFromStreamAsync(cls: win32more.Windows.AI.MachineLearning.Preview.ILearningModelPreviewStatics, modelStream: win32more.Windows.Storage.Streams.IRandomAccessStreamReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.AI.MachineLearning.Preview.LearningModelPreview]: ...
    Description = property(get_Description, None)
    InferencingOptions = property(get_InferencingOptions, put_InferencingOptions)
class LearningModelVariableDescriptorPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview
    _classid_ = 'Windows.AI.MachineLearning.Preview.LearningModelVariableDescriptorPreview'
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ModelFeatureKind(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> win32more.Windows.AI.MachineLearning.Preview.LearningModelFeatureKindPreview: ...
    @winrt_mixinmethod
    def get_IsRequired(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> Boolean: ...
    Description = property(get_Description, None)
    IsRequired = property(get_IsRequired, None)
    ModelFeatureKind = property(get_ModelFeatureKind, None)
    Name = property(get_Name, None)
MachineLearningPreviewContract: UInt32 = 131072
class MapVariableDescriptorPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.AI.MachineLearning.Preview.IMapVariableDescriptorPreview
    _classid_ = 'Windows.AI.MachineLearning.Preview.MapVariableDescriptorPreview'
    @winrt_mixinmethod
    def get_KeyKind(self: win32more.Windows.AI.MachineLearning.Preview.IMapVariableDescriptorPreview) -> win32more.Windows.AI.MachineLearning.Preview.FeatureElementKindPreview: ...
    @winrt_mixinmethod
    def get_ValidStringKeys(self: win32more.Windows.AI.MachineLearning.Preview.IMapVariableDescriptorPreview) -> win32more.Windows.Foundation.Collections.IIterable[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ValidIntegerKeys(self: win32more.Windows.AI.MachineLearning.Preview.IMapVariableDescriptorPreview) -> win32more.Windows.Foundation.Collections.IIterable[Int64]: ...
    @winrt_mixinmethod
    def get_Fields(self: win32more.Windows.AI.MachineLearning.Preview.IMapVariableDescriptorPreview) -> win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ModelFeatureKind(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> win32more.Windows.AI.MachineLearning.Preview.LearningModelFeatureKindPreview: ...
    @winrt_mixinmethod
    def get_IsRequired(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> Boolean: ...
    Description = property(get_Description, None)
    Fields = property(get_Fields, None)
    IsRequired = property(get_IsRequired, None)
    KeyKind = property(get_KeyKind, None)
    ModelFeatureKind = property(get_ModelFeatureKind, None)
    Name = property(get_Name, None)
    ValidIntegerKeys = property(get_ValidIntegerKeys, None)
    ValidStringKeys = property(get_ValidStringKeys, None)
class SequenceVariableDescriptorPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.AI.MachineLearning.Preview.ISequenceVariableDescriptorPreview
    _classid_ = 'Windows.AI.MachineLearning.Preview.SequenceVariableDescriptorPreview'
    @winrt_mixinmethod
    def get_ElementType(self: win32more.Windows.AI.MachineLearning.Preview.ISequenceVariableDescriptorPreview) -> win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ModelFeatureKind(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> win32more.Windows.AI.MachineLearning.Preview.LearningModelFeatureKindPreview: ...
    @winrt_mixinmethod
    def get_IsRequired(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> Boolean: ...
    Description = property(get_Description, None)
    ElementType = property(get_ElementType, None)
    IsRequired = property(get_IsRequired, None)
    ModelFeatureKind = property(get_ModelFeatureKind, None)
    Name = property(get_Name, None)
class TensorVariableDescriptorPreview(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.AI.MachineLearning.Preview.ITensorVariableDescriptorPreview
    _classid_ = 'Windows.AI.MachineLearning.Preview.TensorVariableDescriptorPreview'
    @winrt_mixinmethod
    def get_DataType(self: win32more.Windows.AI.MachineLearning.Preview.ITensorVariableDescriptorPreview) -> win32more.Windows.AI.MachineLearning.Preview.FeatureElementKindPreview: ...
    @winrt_mixinmethod
    def get_Shape(self: win32more.Windows.AI.MachineLearning.Preview.ITensorVariableDescriptorPreview) -> win32more.Windows.Foundation.Collections.IIterable[Int64]: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ModelFeatureKind(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> win32more.Windows.AI.MachineLearning.Preview.LearningModelFeatureKindPreview: ...
    @winrt_mixinmethod
    def get_IsRequired(self: win32more.Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> Boolean: ...
    DataType = property(get_DataType, None)
    Description = property(get_Description, None)
    IsRequired = property(get_IsRequired, None)
    ModelFeatureKind = property(get_ModelFeatureKind, None)
    Name = property(get_Name, None)
    Shape = property(get_Shape, None)


make_ready(__name__)
