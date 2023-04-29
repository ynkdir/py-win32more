from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.AI.MachineLearning.Preview
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics.Imaging
import Windows.Storage
import Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
FeatureElementKindPreview = Int32
FeatureElementKindPreview_Undefined: FeatureElementKindPreview = 0
FeatureElementKindPreview_Float: FeatureElementKindPreview = 1
FeatureElementKindPreview_UInt8: FeatureElementKindPreview = 2
FeatureElementKindPreview_Int8: FeatureElementKindPreview = 3
FeatureElementKindPreview_UInt16: FeatureElementKindPreview = 4
FeatureElementKindPreview_Int16: FeatureElementKindPreview = 5
FeatureElementKindPreview_Int32: FeatureElementKindPreview = 6
FeatureElementKindPreview_Int64: FeatureElementKindPreview = 7
FeatureElementKindPreview_String: FeatureElementKindPreview = 8
FeatureElementKindPreview_Boolean: FeatureElementKindPreview = 9
FeatureElementKindPreview_Float16: FeatureElementKindPreview = 10
FeatureElementKindPreview_Double: FeatureElementKindPreview = 11
FeatureElementKindPreview_UInt32: FeatureElementKindPreview = 12
FeatureElementKindPreview_UInt64: FeatureElementKindPreview = 13
FeatureElementKindPreview_Complex64: FeatureElementKindPreview = 14
FeatureElementKindPreview_Complex128: FeatureElementKindPreview = 15
class IImageVariableDescriptorPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7ae1fa72-029e-4dc5-a2-f8-5f-b7-63-15-41-50')
    @winrt_commethod(6)
    def get_BitmapPixelFormat(self) -> Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_commethod(7)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Height(self) -> UInt32: ...
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
class IInferencingOptionsPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('47bc8205-4d36-47a9-8f-68-ff-cb-33-9d-d0-fc')
    @winrt_commethod(6)
    def get_PreferredDeviceKind(self) -> Windows.AI.MachineLearning.Preview.LearningModelDeviceKindPreview: ...
    @winrt_commethod(7)
    def put_PreferredDeviceKind(self, value: Windows.AI.MachineLearning.Preview.LearningModelDeviceKindPreview) -> Void: ...
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
    PreferredDeviceKind = property(get_PreferredDeviceKind, put_PreferredDeviceKind)
    IsTracingEnabled = property(get_IsTracingEnabled, put_IsTracingEnabled)
    MaxBatchSize = property(get_MaxBatchSize, put_MaxBatchSize)
    MinimizeMemoryAllocation = property(get_MinimizeMemoryAllocation, put_MinimizeMemoryAllocation)
    ReclaimMemoryAfterEvaluation = property(get_ReclaimMemoryAfterEvaluation, put_ReclaimMemoryAfterEvaluation)
class ILearningModelBindingPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('93c901e8-6c78-4b4f-ae-c1-a6-bb-9e-69-16-24')
    @winrt_commethod(6)
    def Bind(self, name: WinRT_String, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_commethod(7)
    def BindWithProperties(self, name: WinRT_String, value: Windows.Win32.System.WinRT.IInspectable_head, metadata: Windows.Foundation.Collections.IPropertySet) -> Void: ...
    @winrt_commethod(8)
    def Clear(self) -> Void: ...
class ILearningModelBindingPreviewFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('48b8219f-1e51-4d77-ae-50-3e-c1-64-ad-34-80')
    @winrt_commethod(6)
    def CreateFromModel(self, model: Windows.AI.MachineLearning.Preview.LearningModelPreview) -> Windows.AI.MachineLearning.Preview.LearningModelBindingPreview: ...
class ILearningModelDescriptionPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f52c09c6-8611-40ad-8e-59-de-3f-d7-03-0a-40')
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
    def get_Metadata(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_commethod(12)
    def get_InputFeatures(self) -> Windows.Foundation.Collections.IIterable[Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview]: ...
    @winrt_commethod(13)
    def get_OutputFeatures(self) -> Windows.Foundation.Collections.IIterable[Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview]: ...
    Author = property(get_Author, None)
    Name = property(get_Name, None)
    Domain = property(get_Domain, None)
    Description = property(get_Description, None)
    Version = property(get_Version, None)
    Metadata = property(get_Metadata, None)
    InputFeatures = property(get_InputFeatures, None)
    OutputFeatures = property(get_OutputFeatures, None)
class ILearningModelEvaluationResultPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('df25ea9f-9863-4088-84-98-87-a1-f4-68-6f-92')
    @winrt_commethod(6)
    def get_CorrelationId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Outputs(self) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    CorrelationId = property(get_CorrelationId, None)
    Outputs = property(get_Outputs, None)
class ILearningModelPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('049c266a-93b4-478c-ae-b8-70-15-7b-f0-ff-94')
    @winrt_commethod(6)
    def EvaluateAsync(self, binding: Windows.AI.MachineLearning.Preview.LearningModelBindingPreview, correlationId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.Preview.LearningModelEvaluationResultPreview]: ...
    @winrt_commethod(7)
    def EvaluateFeaturesAsync(self, features: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], correlationId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.Preview.LearningModelEvaluationResultPreview]: ...
    @winrt_commethod(8)
    def get_Description(self) -> Windows.AI.MachineLearning.Preview.LearningModelDescriptionPreview: ...
    @winrt_commethod(9)
    def get_InferencingOptions(self) -> Windows.AI.MachineLearning.Preview.InferencingOptionsPreview: ...
    @winrt_commethod(10)
    def put_InferencingOptions(self, value: Windows.AI.MachineLearning.Preview.InferencingOptionsPreview) -> Void: ...
    Description = property(get_Description, None)
    InferencingOptions = property(get_InferencingOptions, put_InferencingOptions)
class ILearningModelPreviewStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('164bbb60-8465-4786-8b-93-2c-16-a8-92-89-d7')
    @winrt_commethod(6)
    def LoadModelFromStorageFileAsync(self, modelFile: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.Preview.LearningModelPreview]: ...
    @winrt_commethod(7)
    def LoadModelFromStreamAsync(self, modelStream: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.Preview.LearningModelPreview]: ...
class ILearningModelVariableDescriptorPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b13df682-fc30-492b-8e-a0-ed-1f-53-c0-b0-38')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ModelFeatureKind(self) -> Windows.AI.MachineLearning.Preview.LearningModelFeatureKindPreview: ...
    @winrt_commethod(9)
    def get_IsRequired(self) -> Boolean: ...
    Name = property(get_Name, None)
    Description = property(get_Description, None)
    ModelFeatureKind = property(get_ModelFeatureKind, None)
    IsRequired = property(get_IsRequired, None)
class IMapVariableDescriptorPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3cb38370-c02b-4236-b3-e8-6b-dc-a4-9c-31-29')
    @winrt_commethod(6)
    def get_KeyKind(self) -> Windows.AI.MachineLearning.Preview.FeatureElementKindPreview: ...
    @winrt_commethod(7)
    def get_ValidStringKeys(self) -> Windows.Foundation.Collections.IIterable[WinRT_String]: ...
    @winrt_commethod(8)
    def get_ValidIntegerKeys(self) -> Windows.Foundation.Collections.IIterable[Int64]: ...
    @winrt_commethod(9)
    def get_Fields(self) -> Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview: ...
    KeyKind = property(get_KeyKind, None)
    ValidStringKeys = property(get_ValidStringKeys, None)
    ValidIntegerKeys = property(get_ValidIntegerKeys, None)
    Fields = property(get_Fields, None)
class ISequenceVariableDescriptorPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9cd8f292-98b2-4530-a1-b6-2d-ed-5f-ec-bc-26')
    @winrt_commethod(6)
    def get_ElementType(self) -> Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview: ...
    ElementType = property(get_ElementType, None)
class ITensorVariableDescriptorPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a80f501a-9aac-4233-97-84-ac-ea-f9-25-10-b5')
    @winrt_commethod(6)
    def get_DataType(self) -> Windows.AI.MachineLearning.Preview.FeatureElementKindPreview: ...
    @winrt_commethod(7)
    def get_Shape(self) -> Windows.Foundation.Collections.IIterable[Int64]: ...
    DataType = property(get_DataType, None)
    Shape = property(get_Shape, None)
class ImageVariableDescriptorPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.AI.MachineLearning.Preview.ImageVariableDescriptorPreview'
    @winrt_mixinmethod
    def get_BitmapPixelFormat(self: Windows.AI.MachineLearning.Preview.IImageVariableDescriptorPreview) -> Windows.Graphics.Imaging.BitmapPixelFormat: ...
    @winrt_mixinmethod
    def get_Width(self: Windows.AI.MachineLearning.Preview.IImageVariableDescriptorPreview) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: Windows.AI.MachineLearning.Preview.IImageVariableDescriptorPreview) -> UInt32: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ModelFeatureKind(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> Windows.AI.MachineLearning.Preview.LearningModelFeatureKindPreview: ...
    @winrt_mixinmethod
    def get_IsRequired(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> Boolean: ...
    BitmapPixelFormat = property(get_BitmapPixelFormat, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    Name = property(get_Name, None)
    Description = property(get_Description, None)
    ModelFeatureKind = property(get_ModelFeatureKind, None)
    IsRequired = property(get_IsRequired, None)
class InferencingOptionsPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.AI.MachineLearning.Preview.InferencingOptionsPreview'
    @winrt_mixinmethod
    def get_PreferredDeviceKind(self: Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview) -> Windows.AI.MachineLearning.Preview.LearningModelDeviceKindPreview: ...
    @winrt_mixinmethod
    def put_PreferredDeviceKind(self: Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview, value: Windows.AI.MachineLearning.Preview.LearningModelDeviceKindPreview) -> Void: ...
    @winrt_mixinmethod
    def get_IsTracingEnabled(self: Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsTracingEnabled(self: Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MaxBatchSize(self: Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview) -> Int32: ...
    @winrt_mixinmethod
    def put_MaxBatchSize(self: Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_MinimizeMemoryAllocation(self: Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview) -> Boolean: ...
    @winrt_mixinmethod
    def put_MinimizeMemoryAllocation(self: Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ReclaimMemoryAfterEvaluation(self: Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview) -> Boolean: ...
    @winrt_mixinmethod
    def put_ReclaimMemoryAfterEvaluation(self: Windows.AI.MachineLearning.Preview.IInferencingOptionsPreview, value: Boolean) -> Void: ...
    PreferredDeviceKind = property(get_PreferredDeviceKind, put_PreferredDeviceKind)
    IsTracingEnabled = property(get_IsTracingEnabled, put_IsTracingEnabled)
    MaxBatchSize = property(get_MaxBatchSize, put_MaxBatchSize)
    MinimizeMemoryAllocation = property(get_MinimizeMemoryAllocation, put_MinimizeMemoryAllocation)
    ReclaimMemoryAfterEvaluation = property(get_ReclaimMemoryAfterEvaluation, put_ReclaimMemoryAfterEvaluation)
class LearningModelBindingPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.AI.MachineLearning.Preview.LearningModelBindingPreview'
    @winrt_factorymethod
    def CreateFromModel(cls: Windows.AI.MachineLearning.Preview.ILearningModelBindingPreviewFactory, model: Windows.AI.MachineLearning.Preview.LearningModelPreview) -> Windows.AI.MachineLearning.Preview.LearningModelBindingPreview: ...
    @winrt_mixinmethod
    def Bind(self: Windows.AI.MachineLearning.Preview.ILearningModelBindingPreview, name: WinRT_String, value: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
    @winrt_mixinmethod
    def BindWithProperties(self: Windows.AI.MachineLearning.Preview.ILearningModelBindingPreview, name: WinRT_String, value: Windows.Win32.System.WinRT.IInspectable_head, metadata: Windows.Foundation.Collections.IPropertySet) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.AI.MachineLearning.Preview.ILearningModelBindingPreview) -> Void: ...
    @winrt_mixinmethod
    def Lookup(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]) -> UInt32: ...
    @winrt_mixinmethod
    def HasKey(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], key: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Split(self: Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], first: POINTER(Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]), second: POINTER(Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head])) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Collections.IKeyValuePair[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]]: ...
    Size = property(get_Size, None)
class LearningModelDescriptionPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.AI.MachineLearning.Preview.LearningModelDescriptionPreview'
    @winrt_mixinmethod
    def get_Author(self: Windows.AI.MachineLearning.Preview.ILearningModelDescriptionPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.AI.MachineLearning.Preview.ILearningModelDescriptionPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Domain(self: Windows.AI.MachineLearning.Preview.ILearningModelDescriptionPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.AI.MachineLearning.Preview.ILearningModelDescriptionPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Version(self: Windows.AI.MachineLearning.Preview.ILearningModelDescriptionPreview) -> Int64: ...
    @winrt_mixinmethod
    def get_Metadata(self: Windows.AI.MachineLearning.Preview.ILearningModelDescriptionPreview) -> Windows.Foundation.Collections.IMapView[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_InputFeatures(self: Windows.AI.MachineLearning.Preview.ILearningModelDescriptionPreview) -> Windows.Foundation.Collections.IIterable[Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview]: ...
    @winrt_mixinmethod
    def get_OutputFeatures(self: Windows.AI.MachineLearning.Preview.ILearningModelDescriptionPreview) -> Windows.Foundation.Collections.IIterable[Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview]: ...
    Author = property(get_Author, None)
    Name = property(get_Name, None)
    Domain = property(get_Domain, None)
    Description = property(get_Description, None)
    Version = property(get_Version, None)
    Metadata = property(get_Metadata, None)
    InputFeatures = property(get_InputFeatures, None)
    OutputFeatures = property(get_OutputFeatures, None)
LearningModelDeviceKindPreview = Int32
LearningModelDeviceKindPreview_LearningDeviceAny: LearningModelDeviceKindPreview = 0
LearningModelDeviceKindPreview_LearningDeviceCpu: LearningModelDeviceKindPreview = 1
LearningModelDeviceKindPreview_LearningDeviceGpu: LearningModelDeviceKindPreview = 2
LearningModelDeviceKindPreview_LearningDeviceNpu: LearningModelDeviceKindPreview = 3
LearningModelDeviceKindPreview_LearningDeviceDsp: LearningModelDeviceKindPreview = 4
LearningModelDeviceKindPreview_LearningDeviceFpga: LearningModelDeviceKindPreview = 5
class LearningModelEvaluationResultPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.AI.MachineLearning.Preview.LearningModelEvaluationResultPreview'
    @winrt_mixinmethod
    def get_CorrelationId(self: Windows.AI.MachineLearning.Preview.ILearningModelEvaluationResultPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Outputs(self: Windows.AI.MachineLearning.Preview.ILearningModelEvaluationResultPreview) -> Windows.Foundation.Collections.IMapView[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head]: ...
    CorrelationId = property(get_CorrelationId, None)
    Outputs = property(get_Outputs, None)
LearningModelFeatureKindPreview = Int32
LearningModelFeatureKindPreview_Undefined: LearningModelFeatureKindPreview = 0
LearningModelFeatureKindPreview_Tensor: LearningModelFeatureKindPreview = 1
LearningModelFeatureKindPreview_Sequence: LearningModelFeatureKindPreview = 2
LearningModelFeatureKindPreview_Map: LearningModelFeatureKindPreview = 3
LearningModelFeatureKindPreview_Image: LearningModelFeatureKindPreview = 4
class LearningModelPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.AI.MachineLearning.Preview.LearningModelPreview'
    @winrt_mixinmethod
    def EvaluateAsync(self: Windows.AI.MachineLearning.Preview.ILearningModelPreview, binding: Windows.AI.MachineLearning.Preview.LearningModelBindingPreview, correlationId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.Preview.LearningModelEvaluationResultPreview]: ...
    @winrt_mixinmethod
    def EvaluateFeaturesAsync(self: Windows.AI.MachineLearning.Preview.ILearningModelPreview, features: Windows.Foundation.Collections.IMap[WinRT_String, Windows.Win32.System.WinRT.IInspectable_head], correlationId: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.Preview.LearningModelEvaluationResultPreview]: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.AI.MachineLearning.Preview.ILearningModelPreview) -> Windows.AI.MachineLearning.Preview.LearningModelDescriptionPreview: ...
    @winrt_mixinmethod
    def get_InferencingOptions(self: Windows.AI.MachineLearning.Preview.ILearningModelPreview) -> Windows.AI.MachineLearning.Preview.InferencingOptionsPreview: ...
    @winrt_mixinmethod
    def put_InferencingOptions(self: Windows.AI.MachineLearning.Preview.ILearningModelPreview, value: Windows.AI.MachineLearning.Preview.InferencingOptionsPreview) -> Void: ...
    @winrt_classmethod
    def LoadModelFromStorageFileAsync(cls: Windows.AI.MachineLearning.Preview.ILearningModelPreviewStatics, modelFile: Windows.Storage.IStorageFile) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.Preview.LearningModelPreview]: ...
    @winrt_classmethod
    def LoadModelFromStreamAsync(cls: Windows.AI.MachineLearning.Preview.ILearningModelPreviewStatics, modelStream: Windows.Storage.Streams.IRandomAccessStreamReference) -> Windows.Foundation.IAsyncOperation[Windows.AI.MachineLearning.Preview.LearningModelPreview]: ...
    Description = property(get_Description, None)
    InferencingOptions = property(get_InferencingOptions, put_InferencingOptions)
class LearningModelVariableDescriptorPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.AI.MachineLearning.Preview.LearningModelVariableDescriptorPreview'
    @winrt_mixinmethod
    def get_Name(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ModelFeatureKind(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> Windows.AI.MachineLearning.Preview.LearningModelFeatureKindPreview: ...
    @winrt_mixinmethod
    def get_IsRequired(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> Boolean: ...
    Name = property(get_Name, None)
    Description = property(get_Description, None)
    ModelFeatureKind = property(get_ModelFeatureKind, None)
    IsRequired = property(get_IsRequired, None)
MachineLearningPreviewContract: UInt32 = 131072
class MapVariableDescriptorPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.AI.MachineLearning.Preview.MapVariableDescriptorPreview'
    @winrt_mixinmethod
    def get_KeyKind(self: Windows.AI.MachineLearning.Preview.IMapVariableDescriptorPreview) -> Windows.AI.MachineLearning.Preview.FeatureElementKindPreview: ...
    @winrt_mixinmethod
    def get_ValidStringKeys(self: Windows.AI.MachineLearning.Preview.IMapVariableDescriptorPreview) -> Windows.Foundation.Collections.IIterable[WinRT_String]: ...
    @winrt_mixinmethod
    def get_ValidIntegerKeys(self: Windows.AI.MachineLearning.Preview.IMapVariableDescriptorPreview) -> Windows.Foundation.Collections.IIterable[Int64]: ...
    @winrt_mixinmethod
    def get_Fields(self: Windows.AI.MachineLearning.Preview.IMapVariableDescriptorPreview) -> Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ModelFeatureKind(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> Windows.AI.MachineLearning.Preview.LearningModelFeatureKindPreview: ...
    @winrt_mixinmethod
    def get_IsRequired(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> Boolean: ...
    KeyKind = property(get_KeyKind, None)
    ValidStringKeys = property(get_ValidStringKeys, None)
    ValidIntegerKeys = property(get_ValidIntegerKeys, None)
    Fields = property(get_Fields, None)
    Name = property(get_Name, None)
    Description = property(get_Description, None)
    ModelFeatureKind = property(get_ModelFeatureKind, None)
    IsRequired = property(get_IsRequired, None)
class SequenceVariableDescriptorPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.AI.MachineLearning.Preview.SequenceVariableDescriptorPreview'
    @winrt_mixinmethod
    def get_ElementType(self: Windows.AI.MachineLearning.Preview.ISequenceVariableDescriptorPreview) -> Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ModelFeatureKind(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> Windows.AI.MachineLearning.Preview.LearningModelFeatureKindPreview: ...
    @winrt_mixinmethod
    def get_IsRequired(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> Boolean: ...
    ElementType = property(get_ElementType, None)
    Name = property(get_Name, None)
    Description = property(get_Description, None)
    ModelFeatureKind = property(get_ModelFeatureKind, None)
    IsRequired = property(get_IsRequired, None)
class TensorVariableDescriptorPreview(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.AI.MachineLearning.Preview.TensorVariableDescriptorPreview'
    @winrt_mixinmethod
    def get_DataType(self: Windows.AI.MachineLearning.Preview.ITensorVariableDescriptorPreview) -> Windows.AI.MachineLearning.Preview.FeatureElementKindPreview: ...
    @winrt_mixinmethod
    def get_Shape(self: Windows.AI.MachineLearning.Preview.ITensorVariableDescriptorPreview) -> Windows.Foundation.Collections.IIterable[Int64]: ...
    @winrt_mixinmethod
    def get_Name(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ModelFeatureKind(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> Windows.AI.MachineLearning.Preview.LearningModelFeatureKindPreview: ...
    @winrt_mixinmethod
    def get_IsRequired(self: Windows.AI.MachineLearning.Preview.ILearningModelVariableDescriptorPreview) -> Boolean: ...
    DataType = property(get_DataType, None)
    Shape = property(get_Shape, None)
    Name = property(get_Name, None)
    Description = property(get_Description, None)
    ModelFeatureKind = property(get_ModelFeatureKind, None)
    IsRequired = property(get_IsRequired, None)
make_head(_module, 'IImageVariableDescriptorPreview')
make_head(_module, 'IInferencingOptionsPreview')
make_head(_module, 'ILearningModelBindingPreview')
make_head(_module, 'ILearningModelBindingPreviewFactory')
make_head(_module, 'ILearningModelDescriptionPreview')
make_head(_module, 'ILearningModelEvaluationResultPreview')
make_head(_module, 'ILearningModelPreview')
make_head(_module, 'ILearningModelPreviewStatics')
make_head(_module, 'ILearningModelVariableDescriptorPreview')
make_head(_module, 'IMapVariableDescriptorPreview')
make_head(_module, 'ISequenceVariableDescriptorPreview')
make_head(_module, 'ITensorVariableDescriptorPreview')
make_head(_module, 'ImageVariableDescriptorPreview')
make_head(_module, 'InferencingOptionsPreview')
make_head(_module, 'LearningModelBindingPreview')
make_head(_module, 'LearningModelDescriptionPreview')
make_head(_module, 'LearningModelEvaluationResultPreview')
make_head(_module, 'LearningModelPreview')
make_head(_module, 'LearningModelVariableDescriptorPreview')
make_head(_module, 'MapVariableDescriptorPreview')
make_head(_module, 'SequenceVariableDescriptorPreview')
make_head(_module, 'TensorVariableDescriptorPreview')
